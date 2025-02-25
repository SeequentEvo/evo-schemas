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

import pathlib
import sys

from common import generate_all_paths
from schemas import schema_base_path

MAIN_TEMPLATE = """\
{{
  "$id": "/geoscience-objects.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "description": "A collection of all Seequent Geoscience Objects",
  "type": "object",
  "oneOf": [
{objects}
  ]
}}
"""

OBJECT_TEMPLATE = """\
    {{
      "$ref": "{ref}"
    }}\
"""


def main() -> int:
    root = schema_base_path()
    full_paths = generate_all_paths(root, "/objects/**/*.json")
    schema_ids = sorted(f"/{pathlib.Path(p).relative_to(root).as_posix()}" for p in full_paths)
    schema_json = [OBJECT_TEMPLATE.format(ref=schema) for schema in schema_ids]
    objects = ",\n".join(schema_json)
    schema = MAIN_TEMPLATE.format(objects=objects)

    schema_path = root / "geoscience-objects.schema.json"
    if schema_path.exists() and schema == schema_path.read_text(encoding="utf-8"):
        return 0

    schema_path.write_text(schema, encoding="utf-8")
    print("Updated root schema")
    return 1


if __name__ == "__main__":
    sys.exit(main())
