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
from glob import iglob
from pathlib import Path


def json_file_to_dict(path):
    """Turns the JSON file specified by pathinto a python dict
    by loading the file as JSON."""
    schema_json = {}
    with open(path, encoding="utf-8") as file:
        schema_json = json.load(file)
    return schema_json


def generate_all_paths(base_path, pattern):
    """Generator that gathers all the files under the base path according
    to the supplied pattern. Searches recursively.

    base_path -- Path object
    pattern -- glob pattern"""
    glob_pattern = base_path.as_posix() + pattern
    for path in iglob(glob_pattern, recursive=True):
        yield Path(path).as_posix()
