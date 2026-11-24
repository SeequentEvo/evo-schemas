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


def all_errors(errors):
    for error in errors:
        yield error
        yield from all_errors(error.context)


def assert_expected_error(errors, expected):
    if expected is None:
        assert not errors, [error.message for error in errors]
        return

    matches = [
        error
        for error in all_errors(errors)
        if error.validator == expected["keyword"]
        and list(error.absolute_path) == expected["path"]
        and expected.get("message_contains", "") in error.message
        and list(error.absolute_schema_path)[: len(expected.get("schema_prefix", []))]
        == expected.get("schema_prefix", [])
    ]
    assert matches, [
        (error.validator, list(error.absolute_path), list(error.absolute_schema_path), error.message)
        for error in all_errors(errors)
    ]
