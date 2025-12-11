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

import builtins
import collections
import contextlib
import os
import pathlib
import re
import shutil
from abc import ABC, abstractmethod
from collections.abc import Iterator
from dataclasses import dataclass, field
from functools import partial
from typing import ClassVar

import black

try:
    from ..schemas import schema_base_path
except ImportError:  # schemas is a top-level module in the build system
    from schemas import schema_base_path

from .parser import SchemaClass, SchemaProperty


@dataclass
class PythonFile:
    path: str
    imports: set[str] = field(default_factory=set)
    imported_classes: set[tuple[str, str, str | None, ...]] = field(default_factory=set)
    lines: list[str] = field(default_factory=list)
    deferred_classes: list[tuple[list[tuple[str, ...]], list[str]]] = field(default_factory=list)


class ClassHandled(Exception):
    # Exception raised as a 'success' indicator for simple class-handlers
    pass


class _AbstractValidator(ABC):
    INDENTATION: ClassVar[str] = "    "
    indent: int

    @abstractmethod
    def __iter__(self) -> Iterator[str]:
        raise NotImplementedError("Validator not implemented")


@dataclass
class ModelValidator(_AbstractValidator):
    IMPORT: ClassVar[tuple[str, str, str | None, ...]] = ("elements", "serialiser", None, "ValidationFailed")

    condition: str
    error_message: str
    indent: int = 0

    def _rewrite_condition(self):
        if m := re.match(r"^(\S+) in (\(.*\))", self.condition):
            return f"if {m.group(1)} not in {m.group(2)}:"
        if m := re.match(r"(\S+) is not (.*)", self.condition):
            return f"if {m.group(1)} is {m.group(2)}:"
        return f"if not {self.condition}:"

    def __iter__(self) -> Iterator[str]:
        error_type = self.IMPORT[-1]
        indent = self.INDENTATION * self.indent
        yield f"{indent}{self._rewrite_condition()}"
        yield f"{indent}{self.INDENTATION}raise {error_type}({self.error_message!r})"


@dataclass
class CombinedValidator(_AbstractValidator):
    entry: str
    validators: list[_AbstractValidator]
    indent: int = 0
    imports: set[tuple[str, str, str | None, ...]] = field(default_factory=set)

    def __post_init__(self):
        for validator in self.validators:
            match validator:
                case ModelValidator():
                    self.imports.add(validator.IMPORT)
                case CombinedValidator():
                    self.imports.update(validator.imports)
                case _:
                    raise NotImplementedError(f"Unable to combine validator {type(validator)}")

    def __iter__(self) -> Iterator[str]:
        # multiple lines - indent
        indent = self.INDENTATION * self.indent
        yield f"{indent}{self.entry}"
        for validator in self.validators:
            validator.indent = self.indent + 1
            yield from validator


class DeferOutput(Exception):
    def __init__(self, classes):
        self.classes = classes


class PythonGenerator:
    INDENT = "    "

    def __init__(self, parser, path):
        self.parser = parser
        self.path = str(path)
        self._indent = 0
        self._files: dict[str, PythonFile] = dict()
        self._file: PythonFile | None = None
        os.makedirs(path, exist_ok=True)

    @contextlib.contextmanager
    def indent(self):
        self._indent += 1
        yield
        self._indent -= 1

    def _class_name(self, item, track=True):
        if isinstance(item, SchemaClass) and item.checks.get("format") == "uuid":
            item = "uuid.UUID"
            self._file.imports.add("import uuid")
        elif isinstance(item, SchemaClass):
            item = item.name

        if isinstance(item, str):
            return item

        if track:
            self._file.imported_classes.add(item)
        group, schema, version, *other = item

        if version is None:  # not a class
            assert len(other) == 1
            return other[0]

        result = [schema.title().replace("-", ""), "V" + version.replace(".", "_")]
        for o in other:
            result.append(re.sub(r"[._\-]", "", o.title()))
        return "_".join(result)

    def _quote(self, v):
        if isinstance(v, str):
            return f'"{v}"'
        return f"{v}"

    def _module_name(self, name):
        return ".".join([name[0], name[1].replace("-", "_")])

    def _get_type(self, item, items=None):
        if isinstance(item, SchemaProperty):
            prop_type, items_type = item.type, item.items
        else:
            prop_type, items_type = item, items

        match prop_type:
            case builtins.int | builtins.str:
                return prop_type.__name__
            case "null":
                return "None"
            case "boolean":
                return "bool"
            case "integer":
                return "int"
            case "number":
                return "float"
            case "string":
                if isinstance(item, (SchemaClass, SchemaProperty)) and item.checks.get("format") == "uuid":
                    self._file.imports.add("import uuid")
                    return "uuid.UUID"
                else:
                    return "str"
            case "object":
                if items_type is None:
                    items_type = "typing.Any"
                    self._file.imports.add("import typing")
                else:
                    items_type = self._get_type(items_type)
                return f"dict[str, {items_type}]"
            case "array":
                assert items_type is not None
                return f"list[{self._get_type(items_type)}]"
            case SchemaClass():
                return self._class_name(prop_type)
            case _:
                raise NotImplementedError(f"Unknown type {prop_type}")

    def _get_type_validators(self, item, item_name, items=None, depth=0) -> list[_AbstractValidator]:
        py_prop_type = self._get_type(item, items=items)

        if isinstance(item, SchemaProperty):
            prop_type, items = item.type, item.items
        else:
            prop_type = item

        validators: list[_AbstractValidator] = []

        match prop_type:
            case "string" | "number" | "integer" | "boolean" | builtins.int | builtins.str:
                validators.append(
                    ModelValidator(
                        condition=f"isinstance({item_name}, {py_prop_type})",
                        error_message=f"{item_name} is not {py_prop_type}",
                    )
                )

            case SchemaClass():
                if prop_type.items:
                    validators.extend(self._get_type_validators("array", item_name, items=prop_type.items))
                elif "collection" in prop_type.checks:
                    func = prop_type.checks["collection"]
                    self._file.imported_classes.add((prop_type.name[0], prop_type.name[1], None, func))
                    validators.append(
                        ModelValidator(condition=f"{func}({item_name})", error_message=f"{func}({item_name}) failed")
                    )
                else:
                    validators.append(
                        ModelValidator(
                            condition=f"isinstance({item_name}, {py_prop_type})",
                            error_message=f"{item_name} is not {py_prop_type}",
                        )
                    )
            case "object":
                validators.append(
                    ModelValidator(
                        condition=f"isinstance({item_name}, dict)",
                        error_message=f"{item_name} is not a dict",
                    )
                )
                key_check = "isinstance(k, str)"
                if items is None:
                    validators.append(
                        CombinedValidator(
                            entry=f"for k in {item_name}:",
                            validators=[
                                ModelValidator(
                                    condition=key_check,
                                    error_message=f"{key_check} failed",
                                ),
                            ],
                        )
                    )
                else:
                    value_validators = self._get_type_validators(items, "v")
                    validators.append(
                        CombinedValidator(
                            entry=f"for k, v in {item_name}.items():",
                            validators=[
                                ModelValidator(condition=key_check, error_message=f"{key_check} failed"),
                                *value_validators,
                            ],
                        )
                    )

            case "array":
                variable_name = "vw"[depth]
                validators.append(
                    ModelValidator(
                        condition=f"isinstance({item_name}, list)", error_message=f"{item_name} is not a list"
                    )
                )
                assert items is not None
                item_checks = self._get_type_validators(items, variable_name, depth=depth + 1)
                if isinstance(item, SchemaProperty) and "items" in item.checks:
                    for condition in self._get_condition(item.checks["items"], "v", type_checked=True):
                        item_checks.append(ModelValidator(condition=condition, error_message=f"{condition} failed"))
                validators.append(
                    CombinedValidator(entry=f"for {variable_name} in {item_name}:", validators=item_checks)
                )

            case _:
                raise NotImplementedError
        return validators

    def _doc_string(self, line):
        if "\n" in line:
            # PEP-257
            for idx, part in enumerate(line.split("\n")):
                if idx == 0:
                    yield f'"""{part}'
                    yield " "
                else:
                    yield part
            yield '"""'
        else:
            yield f'"""{line}"""'

    def _get_condition(self, checks, prop_name, type_checked=False):
        assert isinstance(checks, (SchemaClass, SchemaProperty, dict)), type(checks)

        if isinstance(checks, (SchemaClass, SchemaProperty)):
            checks = checks.checks
        checks = checks.copy()

        def type_check(v):
            nonlocal type_checked
            if not type_checked:
                type_checked = True
                yield f"isinstance({prop_name}, {type(v).__name__})"

        # using if-statements to enforce a certain order of checks

        if (v := checks.pop("type", None)) is not None:
            py_type = self._get_type(v)
            type_checked = True
            if py_type == "None":
                yield f"{prop_name} is None"
            elif py_type == "str" and checks.get("format") == "uuid":
                yield f"isinstance({prop_name}, uuid.UUID)"
                checks.pop("format")
            else:
                yield f"isinstance({prop_name}, {py_type})"

        if (v := checks.pop("const", None)) is not None:
            yield from type_check(v)
            yield f"{prop_name} == {self._quote(v)}"

        if v := checks.pop("enum", None):
            items = ", ".join(self._quote(i) for i in v)
            yield f"{prop_name} in ({items})"

        if (v := checks.pop("exclusive_minimum", None)) is not None:
            yield from type_check(v)
            if "exclusive_maximum" in checks:
                w = checks.pop("exclusive_maximum")
                yield from type_check(w)
                yield f"{v} < {prop_name} < {w}"
            else:
                yield f"{v} < {prop_name}"

        if (v := checks.pop("exclusive_maximum", None)) is not None:
            yield from type_check(v)
            yield f"{prop_name} < {v}"

        if v := checks.pop("format", None):
            match v:
                case "uuid":
                    pass  # Handled by type check
                case "date-time":
                    self._file.imported_classes.add(("elements", "serialiser", None, "Serialiser"))
                    yield from type_check("")
                    yield f"Serialiser.is_date_time({prop_name})"
                case "uri":
                    self._file.imported_classes.add(("elements", "serialiser", None, "Serialiser"))
                    yield from type_check("")
                    yield f"Serialiser.is_uri({prop_name})"
                case "json-pointer":
                    self._file.imported_classes.add(("elements", "serialiser", None, "Serialiser"))
                    yield from type_check("")
                    yield f"Serialiser.is_json_pointer({prop_name})"
                case _:
                    raise NotImplementedError

        if (v := checks.pop("minimum", None)) is not None:
            yield from type_check(v)
            if "maximum" in checks:
                w = checks.pop("maximum")
                yield from type_check(w)
                if v == w:
                    yield f"{prop_name} == {v}"
                else:
                    yield f"{v} <= {prop_name} <= {w}"
            else:
                yield f"{v} <= {prop_name}"

        if (v := checks.pop("maximum", None)) is not None:
            yield from type_check(v)
            yield f"{prop_name} <= {v}"

        if (v := checks.pop("min_items", None)) is not None:
            yield from type_check(v)
            if "max_items" in checks:
                w = checks.pop("max_items")
                yield from type_check(w)
                if v == w:
                    yield f"len({prop_name}) == {v}"
                else:
                    yield f"{v} <= len({prop_name}) <= {w}"
            else:
                yield f"{v} <= len({prop_name})"

        if (v := checks.pop("max_items", None)) is not None:
            yield from type_check(v)
            yield f"len({prop_name}) <= {v}"

        if v := checks.pop("pattern", None):
            self._file.imports.add("import re")
            yield from type_check("")
            yield f're.match(r"{v}", {prop_name})'

        checks.pop("items", None)

        if checks:
            raise NotImplementedError

    def _generate_property(self, prop, is_required, handle_default, validators: list[_AbstractValidator]):
        has_default_values = not is_required or "const" in prop.checks
        if has_default_values != handle_default:
            return

        # name
        line = f"{prop.name}: "

        # type
        line += self._get_type(prop)
        property_validators = self._get_type_validators(prop, f"self.{prop.name}")

        # default value
        default = prop.checks.get("const", prop.checks.pop("default", None))
        if default is not None:
            is_required = True
            if prop.type in ("string", str):
                default = f'"{default}"'
            line += f" = {default}"

        for condition in self._get_condition(prop, f"self.{prop.name}", type_checked=True):
            property_validators.append(ModelValidator(condition=condition, error_message=f"{condition} failed"))

        if not is_required:
            line += " | None = None"
            if property_validators:
                property_validators = [
                    CombinedValidator(entry=f"if self.{prop.name} is not None:", validators=property_validators)
                ]
        validators.extend(property_validators)

        yield line

        # description
        if prop.description:
            yield from self._doc_string(prop.description)

    def _generate_simple_type(self, cls):
        if cls.allOf or cls.oneOf or cls.props or cls.baseclasses or cls.items:
            return
        if "type" in cls.checks:
            # class has a fixed type and nothing else, replace the classname with the type.
            cls.name = self._get_type(cls.checks["type"], cls.items)
            raise ClassHandled

        if "const" in cls.checks:
            # has a "const" check and nothing else. Derive the type and replace the classname
            value = cls.checks["const"]
            if isinstance(value, str):
                cls.name = "str"
            else:
                raise NotImplementedError
            raise ClassHandled

        raise NotImplementedError

    def _generate_array_type(self, cls):
        if not cls.items:
            return

        yield f"{self._class_name(cls, track=False)} = list[{self._class_name(cls.items)}]"
        raise ClassHandled

    def _generate_collection(self, cls):
        # Generates a union-type definition and a type-check function (if required)
        if len(cls.oneOf) == 0:
            return

        assert not cls.allOf and not cls.props and not cls.baseclasses

        defer_output_for = []
        [one_of] = cls.oneOf

        def item_name(item):
            name = self._class_name(item)
            if len(item.name) < len(cls.name) and cls.name[: len(item.name)] == item.name:
                # recursive lookup, we need to defer generation of this class - record the class name
                defer_output_for.append(item.name)
            return name

        items = [item_name(item) for item in one_of.items.values()]
        items = list(dict.fromkeys(items))  # make unique while preserving order
        items = " | ".join(items)
        cls_name = self._class_name(cls, track=False)
        func_name = "is_" + re.sub(r"(?<!^)(?=[A-Z])", "_", cls_name).replace("__", "_").lower()
        yield f"{cls_name} = {items}"

        # collect conditions for simple objects (non-dataclass items)
        condition_lines = []
        dataclasses = []
        for item in one_of.items.values():
            conditions = self._get_condition(item, "value")
            condition = " and ".join(conditions)
            if condition:
                condition_lines.append(f"if {condition}:")
                if item.description:
                    condition_lines.append(f"{self.INDENT}# {item.description}")
                condition_lines.append(f"{self.INDENT}return True")
            else:
                dataclasses.append(item)

        if condition_lines:
            cls.checks["collection"] = func_name
            yield f"def {func_name}(value):"
            with self.indent():
                # add conditions for complex items
                for item in dataclasses:
                    yield f"if isinstance(value, {self._class_name(item)}):"
                    if item.description:
                        yield f"{self.INDENT}# {item.description}"
                    yield f"{self.INDENT}return True"

                # other conditions
                for line in condition_lines:
                    yield line
                yield "return False"

        if defer_output_for:
            # deferred output - raise to signal to the caller.
            raise DeferOutput(defer_output_for)
        raise ClassHandled

    @staticmethod
    def _replace_fraction(full_name: str, match: re.Match):
        numerator_map = {
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine",
        }
        denominator_map = {
            "2": "half",
            "4": "quarter",
            "8": "eighth",
            "16": "sixteenth",
            "30": "thirtieth",
            "32": "thirty_twoth",
            "64": "sixty_fourth",
        }

        numerator, denominator = match.groups()
        if numerator not in numerator_map:
            raise NotImplementedError(f"unknown numerator {numerator} in {full_name}")
        if denominator not in denominator_map:
            raise NotImplementedError(f"unknown denominator {denominator} in {full_name}")

        return f"{numerator_map[numerator]}_{denominator_map[denominator]}"

    @staticmethod
    def _unit_member_name(value: str):
        """Makes a valid python identifier from a unit string value used as an enum member name

        The values come from OSDU unit strings that can contain arbitrary characters, so need fixing for python.
        This is a best effort - not every name will be particularly readable. See comments below for what gets replaced.
        """
        full_name = value
        if not value:
            return "None_"

        for pattern, replacement in (
            (r"(\d+)/(\d+)", partial(PythonGenerator._replace_fraction, full_name)),  # Fractional numbers e.g. 1/16 in
            (r"(\d+)\.(\d+)", r"\g<1>_point_\g<2>"),  # Decimal numbers e.g. 0.1 ft
            (r"\-", r"Minus"),  # Minus signs, only present in exponents e.g. 1E-6 bbl/acre
            (r" ", r"_"),  # Spaces
            (r"%", r"percent"),  # Percentage units
            (r"\$", r"dollars"),  # Dollar units
            (r"(.+)/(.+)", r"\g<1>_per_\g<2>"),  # Unit ratios e.g. m/s
            (r"\[(.+?)\]", r"_\g<1>"),  # Detail suffixes e.g. gal[UK]/ft3, %[vol]
            (r"\((.+?)\)", r"\g<1>"),  # Brackets (used for algebraic grouping) e.g. m3/(d.m)
            (r"(.+)\.(.+)", r"\g<1>_\g<2>"),  # Dot used as multiplication symbol e.g. mol/(s.m2)
            (r"^in$", r"in_"),  # Inches, special case as `in` is a python keyword
        ):
            # Replace all occurrences, which may overlap - but check for infinite loops and abort if required
            value, count = re.subn(pattern, replacement, value)
            attempts = 1
            while count and attempts < 100:
                value, count = re.subn(pattern, replacement, value)
                attempts += 1
            if attempts == 100:
                raise ValueError(f"infinite loop found while creating enum member name from {full_name}")

        return f"Unit_{value}"

    @staticmethod
    def _member_name(value: str):
        """Makes a valid python identifier from an enum value (that isn't a unit string) used as an enum member name"""
        return f"ENUM_{value.upper()}" if value else "NONE"

    def _generate_enum(self, cls):
        if cls.enum is None:
            return
        assert not cls.allOf and not cls.props and not cls.baseclasses

        self._file.imports.add("import enum")
        yield f"class {self._class_name(cls, track=False)}(str, enum.Enum):"
        with self.indent():
            for value in cls.enum:
                if "elements/unit" in cls.ref:
                    yield f'{PythonGenerator._unit_member_name(value)} = "{value}"'
                else:
                    yield f'{PythonGenerator._member_name(value)} = "{value}"'
        raise ClassHandled

    def _generate_post_init(self, baseclasses, validators: list[_AbstractValidator]):
        yield "def __post_init__(self):"
        add_pass = True
        with self.indent():
            if baseclasses:
                for baseclass in baseclasses:
                    yield f"{self._class_name(baseclass)}.__post_init__(self)"
                add_pass = False

            for v in validators:
                match v:
                    case ModelValidator():
                        yield from v
                        self._file.imported_classes.add(v.IMPORT)
                    case CombinedValidator():
                        yield from v
                        self._file.imported_classes.update(v.imports)
                add_pass = False

            if add_pass:
                yield "pass"

    def _collect_all_properties(self, cls):
        """
        Recursively collect all properties from baseclasses and the current class.
        """
        # Collect properties from the current class
        properties = {prop.name: prop for prop in getattr(cls, "props", [])}

        # Collect properties from baseclasses
        for base in getattr(cls, "baseclasses", []) or []:
            base_cls = base if isinstance(base, SchemaClass) else self.parser.classes.get(base)
            if base_cls:
                for prop in self._collect_all_properties(base_cls):
                    properties[prop.name] = prop

        return list(properties.values())

    def _collect_all_required_properties(self, cls):
        """
        Recursively collect all required property names from baseclasses and the current class.
        """
        # Collect required properties from the current class
        required = set(getattr(cls, "required", []))

        # Collect required properties from baseclasses
        for base in getattr(cls, "baseclasses", []) or []:
            base_cls = base if isinstance(base, SchemaClass) else self.parser.classes.get(base)
            if base_cls:
                required.update(self._collect_all_required_properties(base_cls))

        return required

    def _format_doc_string(self, cls):
        """
        Formats the docstring for a class, including its description and attributes.

        A Google-style docstring format is used to allow for parsing the attributes in IDEs, as they're not always
        directly in the root class.
        """
        all_properties = self._collect_all_properties(cls)
        all_required = self._collect_all_required_properties(cls)
        doc_lines = []

        # description
        if cls.description:
            doc_lines += [cls.description, ""]

        # attributes
        if all_properties:
            doc_lines.append("Attributes:")
            for prop in all_properties:
                optional = ", optional" if prop.name not in all_required else ""
                description = f": {prop.description}" if prop.description else ""
                doc_lines.append(f"{self.INDENT}{prop.name} ({self._get_type(prop)}{optional}){description}")

        if doc_lines:
            yield from self._doc_string("\n".join(doc_lines))

    def _generate_class(self, cls):
        try:
            yield from self._generate_collection(cls)
            yield from self._generate_enum(cls)
            yield from self._generate_array_type(cls)
            self._generate_simple_type(cls)

        except ClassHandled:
            return

        validators: list[_AbstractValidator] = []
        # decorator
        self._file.imports.add("import dataclasses")
        yield "@dataclasses.dataclass(kw_only=True)"

        # class declaration
        if cls.baseclasses:
            baseclasses = ", ".join(self._class_name(baseclass) for baseclass in cls.baseclasses)
            yield f"class {self._class_name(cls, track=False)}({baseclasses}):"
        else:
            yield f"class {self._class_name(cls, track=False)}(Serialiser):"
            self._file.imported_classes.add(("elements", "serialiser", None, "Serialiser"))

        with self.indent():
            yield from self._format_doc_string(cls)

            # add schema id as class attribute
            schema_id = cls.schema.get("$id")
            has_id = schema_id is not None and "#/$defs" not in schema_id
            if has_id:
                yield f'SCHEMA_ID = "{schema_id}"'
                yield " "

            # properties
            has_props = len(cls.props) > 0 or has_id
            for handle_default in (False, True):
                for prop in cls.props:
                    yield from self._generate_property(
                        prop=prop,
                        is_required=prop.name in cls.required,
                        handle_default=handle_default,
                        validators=validators,
                    )
            # add validators for remaining "required" rules, this happens if an existing schema with an optional
            # property is extended by making that property mandatory.
            for prop_name in set(cls.required).difference(p.name for p in cls.props):
                validators.append(
                    ModelValidator(
                        condition=f"self.{prop_name} is not None", error_message=f"self.{prop_name} is required"
                    )
                )

            # post_init
            if validators or (baseclasses and len(baseclasses) > 1):
                yield from self._generate_post_init(cls.baseclasses, validators)
            elif not has_props:
                yield "pass"

    def _handle_deferred_classes(self, cls_name):
        for classes, lines in self._file.deferred_classes:
            if cls_name in classes:
                classes.remove(cls_name)
                if not classes:
                    self._file.lines.extend(lines)

    def _add_class_to_file(self, cls):
        module = self._module_name(cls.name)
        if module not in self._files:
            folder, filename = module.split(".")
            path = os.path.join(self.path, folder, f"{filename}.py")
            self._file = self._files[module] = PythonFile(path=os.path.join(self.path, path))
        else:
            self._file = self._files[module]

        lines = []
        try:
            for line in self._generate_class(cls):
                if line:
                    lines.append(self.INDENT * self._indent + line)
        except DeferOutput as exc:
            self._file.imports.add("from __future__ import annotations\n")
            self._file.deferred_classes.append((exc.classes, lines))
        else:
            self._file.lines.extend(lines)
        self._handle_deferred_classes(cls.name)

    def _relative_import_src(self, import_from: str, import_to: str) -> str | None:
        if import_from == import_to:
            return None

        import_from_group = import_from.split(".")[0]
        if import_to == "__init__":
            return f".{import_from_group}"

        if import_to.startswith(import_from_group):
            return import_from[len(import_from_group) :]
        return f"..{import_from}"

    def _write_module(self, module, file):
        if not file.lines and not file.imported_classes:
            return
        lines = []

        # import external packages
        lines.extend(sorted(file.imports) + [""])

        # group local imports
        local_imports = collections.defaultdict(set)
        for cls in file.imported_classes:
            module_name = self._module_name(cls)
            import_from = self._relative_import_src(import_from=module_name, import_to=module)
            if import_from is not None:
                local_imports[import_from].add(self._class_name(cls, track=False))

        # sort and output local imports
        for m in sorted(local_imports):
            lines.append(f"from {m} import " + ", ".join(sorted(local_imports[m])))

        # append file content
        lines.extend(file.lines)

        # run black over the file
        mode = black.Mode(target_versions={black.TargetVersion.PY310}, line_length=120)
        content = "\n".join(lines)
        try:
            content = black.format_file_contents(content, fast=True, mode=mode)
        except black.NothingChanged:
            pass
        except black.InvalidInput:
            print(f"Failed to format {module}")

        os.makedirs(os.path.dirname(file.path), exist_ok=True)
        with open(file.path, "w") as f:
            f.write(content)

    def generate(self):
        helpers = os.path.abspath(os.path.join(__file__, "..", "helpers"))
        module_roots = dict()
        for root in ("", "objects", "components", "elements"):
            if root:
                module_name = f"{root}.__init__"
                if root == "elements":
                    kwargs = dict(imported_classes={("elements", "serialiser", None, "Serialiser")})
                else:
                    kwargs = dict()
            else:
                module_name = "__init__"
                kwargs = dict(
                    imports={"import json"}, imported_classes={("elements", "serialiser", None, "Serialiser")}
                )

            module_roots[root] = f = PythonFile(path=os.path.join(self.path, root, "__init__.py"), **kwargs)
            self._files[module_name] = f

        schema_lookup = collections.defaultdict(dict)
        for cls in self.parser.iter_classes():
            self._add_class_to_file(cls)
            if cls.is_root:
                module_roots[""].imported_classes.add(cls.name)
                schema_lookup[""][cls.ref] = cls.name
            if isinstance(cls.name, tuple) and cls.name[0] in module_roots:
                module_roots[cls.name[0]].imported_classes.add(cls.name)
            if cls.ref and "#/$defs" not in cls.ref:
                schema_lookup[cls.name[0]][cls.ref] = cls.name

        # write lookup and de-serialiser
        for root_name, root in module_roots.items():
            root.lines.append(f"{root_name}{'_' if root_name else ''}schema_lookup = {{")
            for k, v in sorted(schema_lookup[root_name].items()):
                root.lines.append(f'{self.INDENT}"{k}": {self._class_name(v, track=False)},')
            root.lines.append("}")

        with open(os.path.join(helpers, "python_deserialiser.py"), "r") as f:
            for line in f:
                module_roots[""].lines.append(line)

        for module, file in self._files.items():
            self._write_module(module, file)

        # write helpers
        shutil.copy(os.path.join(helpers, "python_serialiser.py"), os.path.join(self.path, "elements", "serialiser.py"))


def generate_python_files(parser, result_path=None) -> pathlib.Path:
    """Generates schema python files at the specified path (or a default)

    Returns the path at which the schemas were generated.
    """
    if result_path is None:
        result_path = (schema_base_path() / ".." / "docs" / "python" / "evo_schemas").resolve()
    generator = PythonGenerator(parser, result_path)
    generator.generate()
    return result_path
