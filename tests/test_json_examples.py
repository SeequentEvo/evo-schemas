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

from tools.common import generate_all_paths, json_file_to_dict
from tools.example_instances import example_schema_dict, examples_base_path, generate_all_example_paths, validate_data


@pytest.mark.parametrize("example_path", generate_all_example_paths())
def test_validate_examples(example_path):
    example = json_file_to_dict(example_path)
    example_schema = example_schema_dict(example)
    validate_data(example, example_schema)


@pytest.mark.parametrize(
    "example_path",
    generate_all_paths(examples_base_path(), "/**/block-model*.json"),
)
def test_block_model_group_refs_are_coherent(example_path: str) -> None:
    """Check that group parent and attribute membership references are coherent in the examples.

    There are a couple of key rules that are not structurally enforced in the schema, but the
    examples should definitely get right:

    1. There should not be a cycle between attribute groups - following parent_group_uuid should not
       loop back to itself.
    2. Every parent_group_uuid should be an actual valid parent_group_uuid
    3. The block_model_group_uuid on a block-model-attribute, if not null, should refer to an
       actual group's uuid.

    While the schema doesn't directly enfroce these constraints - they are not structural and
    are enforced service-side - we should not be publishing examples that breach those rules.
    """
    example = json_file_to_dict(example_path)

    groups = example.get("groups", [])
    groups_by_id = {group["group_uuid"]: group for group in groups}
    group_ids = set(groups_by_id)
    assert len(group_ids) == len(groups), f"{example_path}: group UUIDs must be unique"

    for group in groups:
        parent_group_uuid = group.get("parent_group_uuid")
        ancestor_ids = {group["group_uuid"]}
        while parent_group_uuid is not None:
            assert parent_group_uuid in group_ids, f"{example_path}: parent group UUID must reference a group"
            assert parent_group_uuid not in ancestor_ids, f"{example_path}: group hierarchy must not be circular"
            ancestor_ids.add(parent_group_uuid)
            parent_group_uuid = groups_by_id[parent_group_uuid].get("parent_group_uuid")

    for attribute in example.get("attributes", []):
        group_uuid = attribute.get("block_model_group_uuid")
        if group_uuid is not None:
            assert group_uuid in group_ids, f"{example_path}: attribute group UUID must reference a group"
