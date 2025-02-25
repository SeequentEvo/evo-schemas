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

import pytest

from tools.common import json_file_to_dict
from tools.example_instances import example_schema_dict, generate_all_example_paths, validate_data


@pytest.mark.parametrize("example_path", generate_all_example_paths())
def test_validate_examples(example_path):
    example = json_file_to_dict(example_path)
    example_schema = example_schema_dict(example)
    validate_data(example, example_schema)
