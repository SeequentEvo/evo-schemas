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
import operator
import os
import os.path
from collections import defaultdict
from pathlib import Path

import semver
from jsonschema.validators import Draft202012Validator, validator_for

try:
    from .common import generate_all_paths
except ImportError:  # common is a top-level module in the build system.
    from common import generate_all_paths


def _repo_root_path():
    return (Path(__file__).parent / "..").resolve()


def schema_base_path():
    """Schema base path from the root of the repository."""
    return _repo_root_path() / "schema"


def unittest_schema_base_path():
    """Test schema base path from the root of the repository."""
    return _repo_root_path() / "tests" / "schema"


def generate_all_schema_paths():
    """Generator that gathers all the schema files in the schema
    directory. Useful for performing tests or actions over all schemas."""
    return generate_all_paths(schema_base_path(), "/*/**/*.schema.json")


def generate_latest_schema_paths():
    def schema_path_version(schema_path):
        path = Path(schema_path)
        if semver.Version.is_valid(path.parent.name):
            return semver.Version.parse(path.parent.name)
        elif semver.Version.is_valid(path.parent.parent.name):
            return semver.Version.parse(path.parent.parent.name)
        else:
            raise ValueError("Version cannot be extracted from the schema path.")

    path_and_versions_by_schema_file_name = defaultdict(list)
    for schema_path in generate_all_schema_paths():
        schema_file_name = os.path.basename(schema_path)
        path_and_versions_by_schema_file_name[schema_file_name].append((schema_path, schema_path_version(schema_path)))

    for _, path_and_versions in path_and_versions_by_schema_file_name.items():
        (path, _) = max(path_and_versions, key=operator.itemgetter(1))
        yield path


def generate_json_schema(schema_name, version):
    """Generates a JSON schema as a new file in this repository.
    The file will be placed under the 'schema' directory using the
    correct folder structure. Simply provide the name of the schema
    and a version, both as strings.

    The function will raise if such a schema already exists.

    Note that the schema is made such that it will not pass unit tests.
    For example, the description is empty.

    Example:
    generate_json_schema("components/rotation", "1.0.0")

    --> Creates the file at schema/rotation/1.0.0/rotation.schema.json
    with the contents as follows

    {
        "$id": "/components/rotation/1.0.0/rotation.schema.json",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "description": "",
        "type": "object",
    }
    """
    base_path = schema_base_path()
    schema_name = schema_name.lstrip(r"\/")
    schema_file_name = Path(schema_name).stem + ".schema.json"
    schema_path = os.path.join(base_path.as_posix(), schema_name, version, schema_file_name)
    if os.path.exists(schema_path):
        raise FileExistsError(
            f"A schema already exists at {os.path.normpath(schema_path)}. Perhaps choose a newer version."
        )
    json_object = {
        "$id": "/" + Path(schema_path).relative_to(base_path).as_posix(),
        "$schema": Draft202012Validator.META_SCHEMA["$id"],
        "description": "",
        "type": "object",
    }

    os.makedirs(os.path.split(schema_path)[0], exist_ok=True)
    with open(schema_path, mode="w", encoding="utf-8") as schema_file:
        json.dump(json_object, schema_file, indent=4)


def check_schema_against_draft(schema):
    """Checks the schema against the draft of the json-schema that
    the schema specifies in its $schema field. ie: check the schema
    against its metaschema. Defaults to Draft 2020-12 when none
    is specified in the schema."""
    latest_version = Draft202012Validator
    validator = validator_for(schema, default=latest_version)
    validator.check_schema(schema)
