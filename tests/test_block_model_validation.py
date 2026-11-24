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
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from tests.schema_validation import assert_expected_error
from tools.common import json_file_to_dict
from tools.example_instances import disallow_unevaluated_properties, file_system_ref_resolver

FIXTURES = Path(__file__).parent / "fixtures" / "block-model-1.3.0"
SCHEMA = Path("schema/objects/block-model/1.3.0/block-model.schema.json")
CASES = json_file_to_dict(FIXTURES / "index.json")


@pytest.fixture(scope="module")
def validator():
    schema = disallow_unevaluated_properties(json_file_to_dict(SCHEMA))
    return Draft202012Validator(
        schema, resolver=file_system_ref_resolver(), format_checker=Draft202012Validator.FORMAT_CHECKER
    )


def test_fixture_index_is_complete():
    files = {path.name for path in (FIXTURES / "payloads").glob("*.json")}
    assert files == set(CASES)
    assert CASES


@pytest.mark.parametrize("filename, expected", CASES.items(), ids=CASES.keys())
def test_block_model_validation(filename, expected, validator):
    with (FIXTURES / "payloads" / filename).open(encoding="utf-8") as file:
        payload = json.load(file)
    assert_expected_error(list(validator.iter_errors(payload)), expected)
