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

import contextlib
import functools
import json
import urllib.parse

import jsonschema


class SchemaWalker:
    walk_subschemas = True

    def __init__(self, schema=None):
        if schema is not None:
            self._reset(schema)

    def _reset(self, schema):
        self._scope = ["/"]
        self._property = ["/"]
        our_validators = {
            "$id": self.dollar_id,
            "$schema": self.dollar_schema,
            "$comment": self.dollar_comment,
            "description": self.description,
            "default": self.default,
            "examples": self.examples,
            "$defs": self.dollar_defs,
        }
        for k, v in jsonschema.Draft202012Validator.VALIDATORS.items():
            k_mangled = k.replace("$", "dollar_")
            our_validators[k] = getattr(self, k_mangled, functools.partial(self._not_implemented, k, v))

        self._validator_cls = jsonschema.validators.extend(jsonschema.Draft202012Validator, our_validators)
        self._validator = self._validator_cls(schema)
        self.schema = schema

    @contextlib.contextmanager
    def scope(self, scope):
        self._scope.append(scope)
        try:
            yield
        finally:
            self._scope.pop(-1)

    @property
    def scope_repr(self):
        return "/".join(str(p) for s in self._scope for p in s)

    @contextlib.contextmanager
    def prop(self, prop):
        self._property.append(prop)
        try:
            yield
        finally:
            self._property.pop(-1)

    @property
    def prop_repr(self):
        return f"{self.scope_repr}::{'/'.join(self._property)}"

    def descend(self, schema, path=None, schema_path=None, instance=None):
        validator = self._validator_cls(schema)
        for error in validator.iter_errors(instance):
            yield error

    def walk(self, instance=None):
        self._validator.validate(instance)

    def additionalProperties(self, validator, aP, _, schema):
        pass

    def oneOf(self, validator, oneOf, instance, schema):
        for index, subschema in enumerate(oneOf):
            scope = ("oneOf", index)
            with self.scope(scope):
                list(self.descend(subschema, schema_path=index, instance=instance))

    def anyOf(self, validator, anyOf, instance, schema):
        for index, subschema in enumerate(anyOf):
            scope = ("anyOf", index)
            with self.scope(scope):
                list(self.descend(subschema, schema_path=index, instance=instance))

    def allOf(self, validator, allOf, instance, schema):
        for index, subschema in enumerate(allOf):
            scope = ("allOf", index)
            with self.scope(scope):
                list(self.descend(subschema, schema_path=index, instance=instance))

    def const(self, validator, const, _, schema):
        pass

    def description(self, validator, description, _, schema):
        pass

    def default(self, validator, default, _, schema):
        pass

    def dollar_id(self, validator, schema_id, _, schema):
        pass

    def dollar_schema(self, validator, schema_schema, _, schema):
        pass

    def dollar_comment(self, validator, comment, _, schema):
        pass

    def dollar_ref(self, validator, ref, instance, schema):
        if not self.walk_subschemas:
            return

        if ref.startswith("/components") or ref.startswith("/elements"):
            with open(f"schema{ref}", encoding="utf-8") as f:
                resolved = json.load(f)
            saved_schema = self.schema
            self.schema = resolved
            yield from self.descend(resolved, instance=instance)
            self.schema = saved_schema
        elif "#/$defs" in ref:
            ref = ref.lstrip("#/")
            parts = urllib.parse.unquote(ref).split("/")
            resolved = self.schema
            for part in parts:
                try:
                    resolved = resolved[part]
                except (TypeError, LookupError):
                    raise jsonschema.exceptions.RefResolutionError(
                        f"Unresolvable JSON pointer: {ref!r}",
                    )
            # $defs is always in the same document, so don't copy
            # and restore self.schema, in case more things reference
            # the current document from within $defs
            yield from self.descend(resolved)
        else:
            raise ValueError(f"Unknown $ref: '{ref}")

    def dollar_defs(self, validator, defs, _, schema):
        for k, v in defs.items():
            # the $defs field is an object with a bunch of
            # subobjects that are supposed to be valid schemas
            # https://json-schema.org/draft/2020-12/json-schema-core.html#name-schema-re-use-with-defs
            with self.scope(("$defs", k)):
                yield from self.descend(v)

    def enum(self, validator, enums, _, schema):
        pass

    def example(self, validator, example, _, schema):
        pass

    def _validate_example(self, example):
        validator = jsonschema.Draft202012Validator(self._validator.schema)
        try:
            validator.validate(example)
        except Exception as exc:
            return str(exc)

    def examples(self, validator, examples, _, schema):
        for example in examples:
            self.example(validator, example, _, schema)

    def exclusiveMinimum(self, validator, minimum, _, schema):
        pass

    def exclusiveMaximum(validator, maximum, instance, schema):
        pass

    def format(self, validator, format, _, schema):
        pass

    def items(self, validator, items, instance, schema):
        yield from self.descend(schema=items, path=0, instance=instance)

    def maximum(self, validator, maximum, _, schema):
        pass

    def maxItems(self, validator, mI, _, schema):
        pass

    def maxLength(self, validator, mL, _, schema):
        pass

    def minimum(self, validator, minimum, _, schema):
        pass

    def minItems(self, validator, mI, _, schema):
        pass

    def minLength(self, validator, mL, _, schema):
        pass

    def pattern(self, validator, pattern, _, schema):
        pass

    def property_(self, validator, prop, instance, schema):
        yield from self.descend(schema, path=prop, schema_path=prop, instance=instance)

    def properties(self, validator, properties, instance, schema):
        for property, subschema in properties.items():
            with self.prop(property), self.scope((property,)):
                yield from self.property_(validator, property, instance, subschema)

    def required(self, validator, required, _, schema):
        for property in required:
            pass

    def type(self, validator, types, _, schema):
        pass

    def unevaluatedProperties(self, validator, unevaluatedProperties, _, schema):
        pass

    def uniqueItems(self, validator, uI, _, schema):
        pass

    def _not_implemented(self, kind, old_validator, validator, a, b, c):
        print(f"Validator for '{kind}' not yet implemented")
