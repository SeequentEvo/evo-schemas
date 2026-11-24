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

from functools import lru_cache
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from tests.schema_validation import assert_expected_error
from tools.common import json_file_to_dict
from tools.example_instances import disallow_unevaluated_properties, file_system_ref_resolver

FIXTURES = Path(__file__).parent / "fixtures" / "object-validation"
CASES = json_file_to_dict(FIXTURES / "index.json")


@lru_cache
def validator_for(schema_id):
    schema = json_file_to_dict(Path("schema") / schema_id.lstrip("/"))
    schema = disallow_unevaluated_properties(schema)
    return Draft202012Validator(
        schema, resolver=file_system_ref_resolver(), format_checker=Draft202012Validator.FORMAT_CHECKER
    )


def test_fixture_index_is_complete():
    files = {path.name for path in (FIXTURES / "payloads").glob("*.json")}
    assert files == set(CASES)
    assert CASES


@pytest.mark.parametrize("filename, case", CASES.items(), ids=CASES.keys())
def test_object_validation(filename, case):
    payload = json_file_to_dict(FIXTURES / "payloads" / filename)
    assert payload["schema"] == case["schema"]
    errors = list(validator_for(case["schema"]).iter_errors(payload))
    assert_expected_error(errors, case["expected"])
