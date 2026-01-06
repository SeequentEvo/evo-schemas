#  Copyright © 2025 Bentley Systems, Incorporated
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#      http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import json
import typing
from dataclasses import dataclass, field

try:
    from ..common import generate_all_paths, json_file_to_dict
    from ..schema_walker import SchemaWalker
    from ..schemas import schema_base_path
except ImportError:  # common, schema_walker, and schemas are top-level modules in the build system.
    from common import generate_all_paths, json_file_to_dict
    from schema_walker import SchemaWalker
    from schemas import schema_base_path


@dataclass
class SchemaClass:
    schema: str | None = None
    ref: str | None = None
    is_root: bool = False
    name: tuple[str, ...] | None = None
    description: str | None = None
    comment: str | None = None
    baseclasses: list[int] | None = None
    allOf: list["AllOfInstance"] = field(default_factory=list)
    oneOf: list["OneOfInstance"] = field(default_factory=list)
    props: list = field(default_factory=list)
    enum: list[str] | None = None
    items: str | type | None = None
    required: list[str] = field(default_factory=list)
    checks: dict[str, typing.Any] = field(default_factory=dict)

    @property
    def id(self):
        return id(self.schema)

    @property
    def parent(self):
        return self


@dataclass
class SchemaProperty:
    schema: str | None = None
    name: str | None = None
    parent: SchemaClass | None = None
    description: str | None = None
    comment: str | None = None
    type: str | type | None = None
    enum: list[str] | None = None
    items: str | type | None = None
    checks: dict[str, typing.Any] = field(default_factory=dict)

    @property
    def id(self):
        return id(self.schema)


@dataclass
class AllOfInstance:
    parent: typing.Union[SchemaClass, "AllOfInstance", "OneOfInstance"]
    items: list[SchemaClass] = field(default_factory=list)


@dataclass
class OneOfInstance:
    parent: SchemaClass
    items: dict[str, SchemaClass] = field(default_factory=dict)


class Parser(SchemaWalker):
    walk_subschemas = True

    classes = dict()
    known_refs = dict()

    def __init__(self, sources):
        super().__init__()
        self.sources = sources

    def walk(self):
        for src in self.sources:
            schema = json_file_to_dict(src)
            instance = SchemaClass(schema=schema, ref=schema["$id"], is_root=True)
            self.classes[instance.id] = instance
            self.known_refs[schema["$id"]] = instance
            self._reset(schema)
            super().walk(instance)

        for cls in self.classes.values():
            self.resolve_allOf(cls)

    def _instance(self, instance, schema):
        match instance:
            case SchemaClass():
                return instance

            case SchemaProperty():
                return instance

            case AllOfInstance():
                return self._instance(instance.parent, schema)

            case OneOfInstance():
                if (child := instance.items.get(id(schema))) is not None:
                    return child
                if (child := self.classes.get(id(schema))) is None:
                    child_name = self._cls_name_private(instance.parent, schema)
                    child = SchemaClass(schema=schema, name=child_name)
                    self.classes[child.id] = child
                instance.items[id(schema)] = child
                return child

            case _:
                raise NotImplementedError

    @staticmethod
    def _cls_name_from_schema_id(schema_id):
        category = ""
        if schema_id.count("/") == 5:
            _, group, parent, version, subgroup, name = schema_id.split("/")
            name = name.replace(".schema.json", "")
            category = parent + "_" + subgroup
            return group, name, version, category
        else:
            _, group, name, version, _ = schema_id.split("/")
            return group, name, version

    def _get_cls_name(self, instance, schema):
        if isinstance(instance, OneOfInstance):
            instance = instance.parent
        else:
            instance = self._instance(instance, schema)
        return instance.parent.name if isinstance(instance, SchemaProperty) else instance.name

    def _cls_name_private(self, instance, schema):
        parent_name = self._get_cls_name(instance, schema)
        instance = self._instance(instance, schema)
        if isinstance(instance, SchemaProperty):
            if instance.name is parent_name:
                return parent_name
            return parent_name + (instance.name,)
        if len(schema.get("required", [])) == 1:
            child_name = (schema["required"][0],)
        elif self._scope[-1][0] == "oneOf":
            child_name = "Option", str(self._scope[-1][1])
        else:
            raise NotImplementedError
        return parent_name + child_name

    def additionalProperties(self, validator, aP, instance, schema):
        if isinstance(instance, SchemaProperty):
            item_instance = SchemaProperty(schema=schema)
            yield from self.descend(aP, instance=item_instance)
            instance.items = item_instance.type

    def oneOf(self, validator, oneOf, instance, schema):
        one_of_instance = OneOfInstance(parent=instance)
        instance.oneOf.append(one_of_instance)
        super().oneOf(validator, oneOf, one_of_instance, schema)
        # one-of branches with a $ref create 2 classes, merge them
        item_ids = list(one_of_instance.items)
        for idx in range(len(item_ids) - 1):
            first = one_of_instance.items[item_ids[idx]]
            second = one_of_instance.items[item_ids[idx + 1]]
            if first.schema.get("$ref", 1) == second.schema.get("$id", 2):
                for attr in ("comment", "description"):
                    if getattr(first, attr) is not None and getattr(second, attr) is None:
                        setattr(second, attr, getattr(first, attr))
                one_of_instance.items.pop(first.id)
                self.classes.pop(first.id)

    def allOf(self, validator, allOf, instance, schema):
        assert isinstance(instance, SchemaClass)
        all_of_instance = AllOfInstance(parent=instance)
        instance.allOf.append(all_of_instance)
        super().allOf(validator, allOf, all_of_instance, schema)

    def const(self, validator, const, instance, schema):
        assert isinstance(instance, (SchemaProperty, OneOfInstance))
        instance = self._instance(instance, schema)
        instance.checks["const"] = const
        if isinstance(instance, SchemaProperty) and instance.type is None:
            instance.type = type(const)

    def description(self, validator, description, instance, schema):
        assert isinstance(instance, (SchemaClass, SchemaProperty, OneOfInstance, AllOfInstance))
        instance = self._instance(instance, schema)
        if instance.description is None:
            instance.description = description

    def default(self, validator, default, instance, schema):
        assert isinstance(instance, (SchemaClass, SchemaProperty))
        instance.checks["default"] = default

    def dollar_id(self, validator, schema_id, instance, schema):
        assert isinstance(instance, SchemaClass)
        if schema_id.startswith("#/$defs/"):
            return
        instance.name = self._cls_name_from_schema_id(schema_id)

    def dollar_schema(self, validator, schema_schema, instance, schema):
        pass

    def dollar_comment(self, validator, comment, instance, schema):
        assert isinstance(instance, SchemaClass)
        instance.comment = comment

    def dollar_ref(self, validator, ref, instance, schema):
        assert isinstance(instance, (SchemaClass, SchemaProperty, AllOfInstance, OneOfInstance))

        full_ref = self.schema["$id"] + ref if ref.startswith("#/$defs/") else ref
        if full_ref not in self.known_refs:
            if ref.startswith("/components") or ref.startswith("/elements"):
                with open(schema_base_path() / ref[1:], encoding="utf-8") as f:
                    resolved = json.load(f)
                assert ref == resolved["$id"]
                resolved_instance = SchemaClass(schema=resolved, ref=full_ref)
                self.classes[resolved_instance.id] = resolved_instance
                self.known_refs[full_ref] = resolved_instance

                saved_schema, self.schema = self.schema, resolved
                yield from self.descend(resolved, instance=resolved_instance)
                self.schema = saved_schema
            elif ref.startswith("#/$defs/"):
                ref_name = ref[len("#/$defs/") :]
                assert "$defs" in self.schema
                assert ref_name in self.schema["$defs"], f"Unknown $ref: '{ref}'"
                resolved = self.schema["$defs"][ref_name]
                resolved["$id"] = ref  # this field is not present in defs, but we need it to merge one-of lists
                base_name = self._get_cls_name(instance, schema)
                resolved_name = base_name + (ref_name,)
                resolved_instance = SchemaClass(schema=resolved, ref=full_ref, name=resolved_name)
                self.classes[resolved_instance.id] = resolved_instance
                self.known_refs[full_ref] = resolved_instance
                yield from self.descend(resolved, instance=resolved_instance)
            else:
                raise ValueError(f"Unknown $ref: '{ref}")
        else:
            resolved_instance = self.known_refs[full_ref]
            resolved = resolved_instance.schema

        if isinstance(instance, AllOfInstance):
            instance.items.append(resolved_instance)
        elif isinstance(instance, SchemaProperty):
            instance.type = resolved_instance
        elif isinstance(instance, OneOfInstance):
            self._instance(instance, resolved)
        else:
            raise NotImplementedError

    def dollar_defs(self, validator, defs, _, schema):
        pass

    def enum(self, validator, enums, instance, schema):
        assert isinstance(instance, (SchemaClass, SchemaProperty))
        assert len(enums) > 0
        assert all(isinstance(value, type(enums[0])) for value in enums)
        instance.enum = enums
        instance.checks["enum"] = enums
        if isinstance(instance, SchemaProperty) and instance.type is None:
            instance.type = type(enums[0])

    def exclusiveMinimum(self, validator, minimum, instance, schema):
        assert isinstance(instance, (SchemaClass, SchemaProperty))
        instance.checks["exclusive_minimum"] = minimum

    def exclusiveMaximum(validator, maximum, instance, schema):
        assert isinstance(instance, (SchemaClass, SchemaProperty))
        instance.checks["exclusive_maximum"] = maximum

    def format(self, validator, format, instance, schema):
        assert isinstance(instance, (SchemaProperty, OneOfInstance))
        self._instance(instance, schema).checks["format"] = format

    def items(self, validator, items, instance, schema):
        property_name = "Item" if isinstance(instance, SchemaClass) else instance.name
        prop_instance = SchemaProperty(schema=items, parent=instance.parent, name=property_name)
        type_instance = self._capture_type(prop_instance, items)
        yield from self.descend(items, path="items", schema_path="items", instance=type_instance)

        if prop_instance is not type_instance:
            instance.items = type_instance
        elif prop_instance.type == "array":
            instance.items = prop_instance
            instance.checks["items"] = prop_instance.checks.copy()
            prop_instance.checks.clear()
        else:
            instance.items = prop_instance.type
            instance.checks["items"] = prop_instance.checks

    def maximum(self, validator, maximum, instance, schema):
        assert isinstance(instance, SchemaProperty)
        instance.checks["maximum"] = maximum

    def maxItems(self, validator, mI, instance, schema):
        assert isinstance(instance, SchemaProperty)
        instance.checks["max_items"] = mI

    def minimum(self, validator, minimum, instance, schema):
        assert isinstance(instance, (SchemaClass, SchemaProperty))
        instance.checks["minimum"] = minimum

    def minItems(self, validator, mI, instance, schema):
        assert isinstance(instance, SchemaProperty)
        instance.checks["min_items"] = mI

    def pattern(self, validator, pattern, instance, schema):
        assert isinstance(instance, (SchemaProperty, OneOfInstance))
        self._instance(instance, schema).checks["pattern"] = pattern

    def _capture_type(self, prop_instance, schema):
        if schema.get("type") == "object" and "properties" in schema:
            pass
        elif any(x in schema for x in ("oneOf", "allOf")):
            pass
        else:
            return prop_instance
        # local class
        prop_class_instance = SchemaClass(schema=schema, name=self._cls_name_private(prop_instance, schema))
        self.classes[prop_class_instance.id] = prop_class_instance
        prop_instance.type = prop_class_instance
        prop_instance.description = prop_class_instance.description
        return prop_class_instance

    def property_(self, validator, prop, instance, schema):
        assert isinstance(instance, SchemaClass)
        prop_instance = SchemaProperty(schema=schema, name=prop, parent=instance)
        instance.props.append(prop_instance)

        type_instance = self._capture_type(prop_instance, schema)
        yield from self.descend(schema, path=prop, schema_path=prop, instance=type_instance)
        if prop_instance.description is None:
            prop_instance.description = type_instance.description

    def properties(self, validator, properties, instance, schema):
        assert isinstance(instance, (SchemaClass, AllOfInstance, OneOfInstance))
        instance = self._instance(instance, schema)
        for property, subschema in properties.items():
            with self.prop(property), self.scope((property,)):
                yield from self.property_(validator, property, instance, subschema)

    def required(self, validator, required, instance, schema):
        assert isinstance(instance, (SchemaClass, OneOfInstance, AllOfInstance))
        self._instance(instance, schema).required = required

    def type(self, validator, types, instance, schema):
        assert isinstance(instance, (SchemaClass, SchemaProperty, OneOfInstance, AllOfInstance))
        if isinstance(instance, SchemaProperty):
            match types:
                case "boolean" | "integer" | "number" | "string" | "object" | "array":
                    instance.type = types
                    return
                case _:
                    raise NotImplementedError

        if isinstance(instance, OneOfInstance):
            match types:
                case "object":
                    self._instance(instance, schema)
                    return

                case "string" | "null":
                    child = self._instance(instance, schema)
                    child.checks["type"] = types
                    return

                case _:
                    raise NotImplementedError

        if isinstance(instance, AllOfInstance):
            match types:
                case "object":
                    return

                case _:
                    raise NotImplementedError

        if isinstance(instance, SchemaClass):
            match types:
                case "object":
                    pass

                case "string" | "number" | "integer" | "array":
                    instance.checks["type"] = types

                case _:
                    raise NotImplementedError

        if id(schema) in self.classes:
            # existing class
            return

        raise NotImplementedError

    def unevaluatedProperties(self, validator, unevaluatedProperties, instance, schema):
        pass

    @classmethod
    def resolve_allOf(cls, instance):
        assert isinstance(instance, SchemaClass)
        if len(instance.allOf) == 0:
            return
        if len(instance.allOf) > 1:
            raise NotImplementedError  # only one allOf supported

        [all_of] = instance.allOf
        instance.baseclasses = all_of.items
        instance.allOf = []

    def required_classes(self, instance):
        assert isinstance(instance, SchemaClass)
        required = []
        if instance.baseclasses is not None:
            for baseclass in instance.baseclasses:
                required.append(baseclass)

        if isinstance(instance.items, SchemaClass):
            required.append(instance.items)

        for prop in instance.props:
            if isinstance(prop.type, SchemaClass):
                required.append(prop.type)
            if isinstance(prop.items, SchemaClass):
                required.append(prop.items)

        for one_of in instance.oneOf:
            for item in one_of.items.values():
                assert isinstance(item, SchemaClass)
                required.append(item)
        return [item.id for item in required if instance.name[: len(item.name)] != item.name]

    def iter_classes(self):
        queue = list(self.classes)
        done = set()

        while queue:
            item = queue.pop(0)
            if item in done:
                continue
            instance = self.classes[item]
            required = self.required_classes(instance)
            if set(required) - done:
                queue = required + [item] + queue
                continue

            yield instance
            done.add(item)


def run_parser_on_object_schemas():
    schemas = list(generate_all_paths(schema_base_path(), "/objects/**/*.json"))
    parser = Parser(schemas)
    parser.walk()
    return parser


def run_parser_on_all_schemas():
    schemas = []
    schemas.extend(generate_all_paths(schema_base_path(), "/objects/**/*.json"))
    schemas.extend(generate_all_paths(schema_base_path(), "/components/**/*.json"))
    schemas.extend(generate_all_paths(schema_base_path(), "/elements/**/*.json"))
    parser = Parser(schemas)
    parser.walk()
    return parser
