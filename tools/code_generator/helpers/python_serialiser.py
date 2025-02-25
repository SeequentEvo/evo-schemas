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

from __future__ import annotations

import builtins
import copy
import dataclasses
import datetime
import functools
import json
import types
import typing
import uuid
from typing import Any

import jsonpointer
from rfc3986_validator import validate_rfc3986

try:
    from enum import EnumType
except ImportError:
    from enum import EnumMeta as EnumType


class ValidationFailed(Exception):
    pass


class GSONEncoder(json.JSONEncoder):
    """GeoScience Object Notation Encoder"""

    def default(self, o: Any) -> Any:
        if isinstance(o, Serialiser):
            return o.as_dict()
        elif isinstance(o, uuid.UUID):
            return str(o)
        else:
            return super().default(o)


class Serialiser:
    SCHEMA_ID = None

    @staticmethod
    def is_date_time(value):
        try:
            datetime.datetime.fromisoformat(value)
        except ValueError:
            return False
        return True

    @staticmethod
    def is_uri(value):
        return isinstance(value, str) and validate_rfc3986(value, rule="URI") is not None

    @staticmethod
    def is_json_pointer(value):
        try:
            jsonpointer.JsonPointer(value)
        except jsonpointer.JsonPointerException:
            return False
        return True

    @classmethod
    def _dict_value(cls, value):
        match value:
            case Serialiser():
                return value.as_dict()
            case list() | tuple() | set():
                return type(value)([cls._dict_value(i) for i in value])
            case dict():
                return {str(k): cls._dict_value(v) for k, v in value.items()}
            case _:
                return copy.deepcopy(value)

    def as_dict(self):
        new_dict = {}
        for field in dataclasses.fields(self):
            value = getattr(self, field.name)
            if value is None and field.default is None:
                continue
            else:
                new_dict[field.name] = self._dict_value(value)
        return new_dict

    def json_dump(self, fp, **kwargs):
        return json.dump(self, fp, cls=GSONEncoder, **kwargs)

    def json_dumps(self, **kwargs):
        return json.dumps(self, cls=GSONEncoder, **kwargs)

    @staticmethod
    def _split_schema_id(schema_id: str) -> tuple[str, str, tuple[int, int, int]]:
        # returns the item group, item name and version
        try:
            _, item_group, item_name, version_str, _ = schema_id.split("/")
        except (AttributeError, ValueError) as exc:
            raise ValidationFailed(f"Invalid schema id '{schema_id}'") from exc

        try:
            major_version, minor_version, patch_version = (int(part) for part in version_str.split("."))
        except (AttributeError, ValueError) as exc:
            raise ValidationFailed(f"Invalid schema version in '{schema_id}'") from exc

        return item_group, item_name, (major_version, minor_version, patch_version)

    @classmethod
    def _get_compatible_object_type(cls, object_schemas: dict[str, "Serialiser"], schema_id: str) -> "Serialiser":
        # finds a matching class or a backwards compatible candidate.
        if schema_id in object_schemas:
            return object_schemas[schema_id]

        group, obj_name, version = cls._split_schema_id(schema_id)
        if group != "objects":
            raise ValidationFailed(f"Invalid schema id '{schema_id}'")
        major_version, _, _ = version

        # find schemas with the same major version
        candidates = [schema for schema in object_schemas if schema.startswith(f"/{group}/{obj_name}/{major_version}.")]
        if not candidates:
            raise ValidationFailed(f"No compatible schema found for '{schema_id}'")

        # get the latest version
        candidate = max(candidates, key=cls._split_schema_id)
        return object_schemas[candidate]

    @classmethod
    def from_json(cls, *loader_args, object_schemas, loader, **loader_kwargs):
        obj_dict = loader(*loader_args, **loader_kwargs)
        schema_id = obj_dict["schema"]
        klass = cls._get_compatible_object_type(object_schemas, schema_id)

        if fuzzy := klass.SCHEMA_ID != schema_id:
            obj_dict["schema"] = klass.SCHEMA_ID

        return klass.from_dict(obj_dict, fuzzy=fuzzy)

    @classmethod
    def from_json_wrapper(cls, object_schemas, loader):
        return functools.partial(cls.from_json, object_schemas=object_schemas, loader=loader)

    @classmethod
    def _get_valid_items(cls, iterator, item_classes, match_callback, fuzzy):
        for items in iterator:
            try:
                if isinstance(item_classes, tuple):
                    yield tuple(match_callback(item_cls, item) for item_cls, item in zip(item_classes, items))
                else:
                    yield match_callback(item_classes, items)
            except ValidationFailed:
                if not fuzzy:
                    raise

    @classmethod
    def _match_type(cls, t, value, name, fuzzy):
        _match = functools.partial(cls._match_type, name=name, fuzzy=fuzzy)  # shortcut

        if t is typing.Any:  # we can't match typing.Any
            return value

        if dataclasses.is_dataclass(t):  # we can't match dataclasses
            return t.from_dict(value, fuzzy=fuzzy)

        match t:
            case builtins.float if isinstance(value, (float, int)):
                return t(value)

            case builtins.int if isinstance(value, (float, int)):
                result = t(value)
                if result != value:
                    raise cls._validation_error(t, value, name)
                return result

            case builtins.bool | builtins.str | types.NoneType:
                if type(value) is not t:
                    raise cls._validation_error(t, value, name)
                return value

            case uuid.UUID if isinstance(value, uuid.UUID):
                return value

            case uuid.UUID if isinstance(value, str):
                try:
                    return uuid.UUID(value)
                except ValueError as exc:
                    raise cls._validation_error(t, value, name) from exc

            case types.UnionType():
                sub_types = sorted(typing.get_args(t), key=lambda x: x.__module__ == "builtins")
                for sub_type in sub_types:
                    try:
                        return _match(sub_type, value)
                    except ValidationFailed:
                        pass
                raise cls._validation_error(t, value, name)

            case types.GenericAlias():
                container_cls = typing.get_origin(t)

                if container_cls in (list, tuple):
                    [item_classes] = typing.get_args(t)
                    iterator = value
                elif container_cls is dict:
                    item_classes = typing.get_args(t)
                    iterator = value.items()
                else:
                    raise NotImplementedError
                items = cls._get_valid_items(iterator, item_classes, _match, fuzzy=fuzzy)
                return container_cls(items)

            case EnumType():
                try:
                    return t(value)
                except ValueError as exc:
                    raise cls._validation_error(t, value, name) from exc

            case _:
                raise cls._validation_error(t, value, name)

    @classmethod
    def _validation_error(cls, t, value, name) -> ValidationFailed:
        msg = f"Validation failed for {cls.__name__}.{name}: expected type {t} got {type(value)}"
        return ValidationFailed(msg)

    @classmethod
    def from_dict(cls, data, *, fuzzy=False):
        if not isinstance(data, dict):
            raise ValidationFailed(f"f'{cls.__name__} cannot be constructed from {type(data)}: '{data}'")

        type_hints = None
        remaining_attributes = set(data)  # keep track of used attributes
        kw = {}

        for field in dataclasses.fields(cls):
            if field.name not in data:
                if field.default is not dataclasses.MISSING:
                    kw[field.name] = field.default
                    continue
                raise ValidationFailed(f"{cls.__name__} missing value for {field.name}")

            # use type hints
            if type_hints is None:
                type_hints = typing.get_type_hints(cls)
            field_type = type_hints[field.name]
            kw[field.name] = cls._match_type(field_type, data[field.name], field.name, fuzzy)
            remaining_attributes.remove(field.name)

        if remaining_attributes and not fuzzy:
            raise ValidationFailed(f"{cls.__name__} unknown attributes: '{', '.join(remaining_attributes)}'")

        return cls(**kw)
