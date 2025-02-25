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

import os
from pathlib import Path

from jsonschema import FormatChecker, RefResolver, validate

from .common import generate_all_paths, json_file_to_dict
from .schemas import schema_base_path


def examples_base_path():
    return Path("examples")


def generate_all_example_paths():
    """Generator that gathers all the example JSON files in the examples
    directory. Useful for performing tests or actions over all examples."""
    return generate_all_paths(examples_base_path(), "/**/*.json")


def example_schema_dict(example):
    """Load the schema obj as a Python dictionary from the example's
    $schema field"""
    if "schema" in example:
        schema = example["schema"]
    elif "$schema" in example:
        schema = example.pop("$schema")
    else:
        raise ValueError("Schema property missing")
    schema_path = schema_base_path().joinpath(schema.lstrip(r"\/"))
    return json_file_to_dict(schema_path)


def disallow_unevaluated_properties(schema, skip=False):
    if not isinstance(schema, dict):
        return schema
    if not skip and "properties" in schema:
        schema["unevaluatedProperties"] = False

    for k in schema:
        v = schema[k]
        if k == "$ref":
            # If the reference is to a local section (fragment) then don't append a skip.
            # This will only occur in top-level objects that have very custom
            # components that have no need to be broken out.
            if "#" not in v:
                schema[k] = f"{v}?{skip}"
        elif isinstance(v, dict):
            schema[k] = disallow_unevaluated_properties(v)
        elif isinstance(v, list):
            schema[k] = [disallow_unevaluated_properties(i, skip=k == "allOf") for i in v]
    return schema


def file_system_ref_resolver():
    """Creates a RefResolver based on the filesystem. The base path is the
    schema directory."""
    base_path = Path(os.getcwd()).joinpath(schema_base_path())

    # This handler knows how to load JSON files on the file system
    # using the repo layout.
    def handler(uri):
        if "?" in uri:
            path, skip = uri.removeprefix("file:///").split("?")
        else:
            # When the URI contains a fragment, we are referencing something
            # in the local schema. We don't want to skip them, just load the local schema again.
            path, skip = uri.removeprefix("file:///"), "False"
        schema = json_file_to_dict(base_path.joinpath(path).as_posix())
        return disallow_unevaluated_properties(schema, skip=skip == "True")

    resolver = RefResolver(
        base_uri=f"{base_path.as_uri()}/", referrer=True, cache_remote=True, handlers={"file": handler}
    )

    return resolver


def validate_data(data_to_validate, schema):
    """Validates the data against the schema passed in using a RefResolver that
    does not require a running http server."""
    resolver = file_system_ref_resolver()
    schema = disallow_unevaluated_properties(schema)
    format_checker = FormatChecker()
    validate(data_to_validate, schema, resolver=resolver, format_checker=format_checker)
