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

import sys
from pathlib import Path

from tools.code_generator.parser import run_parser_on_object_schemas
from tools.code_generator.python_generator import generate_python_files


def test_dataclasses():
    # Test models can be built
    parser = run_parser_on_object_schemas()
    output_path = generate_python_files(parser)

    # Test models can be imported without error
    sys.path[:0] = [str(output_path.parent)]

    from evo.schemas import components, elements, objects  # noqa: F401


def test_examples():
    # Tests that the examples can be serialised/deserialised

    script_path = (Path(__file__).parent / ".." / "examples" / "code_generator").resolve()
    sys.path[:0] = [str(script_path)]
    import python_example

    python_example.test_all_examples()


if __name__ == "__main__":
    test_dataclasses()
