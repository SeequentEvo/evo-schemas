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

from setuptools import build_meta as _origin
from setuptools.build_meta import *  # noqa F403


def _prebuild() -> None:
    import os
    import shutil
    from pathlib import Path

    from code_generator.parser import run_parser_on_object_schemas
    from code_generator.python_generator import generate_python_files

    root_dir = Path(__file__).parent.parent.absolute()
    output_dir = root_dir / "docs" / "python" / "evo_schemas"
    if output_dir.exists():
        shutil.rmtree(output_dir)

    parser = run_parser_on_object_schemas()
    generate_python_files(parser, output_dir)

    def keep(directory: str, filename: str) -> bool:
        if os.path.isdir(os.path.join(directory, filename)):
            return True
        if filename.lower().endswith(".schema.json"):
            return True
        return False

    def schema_filter(directory, contents):
        return [f for f in contents if not keep(directory, f)]

    shutil.copytree(src=root_dir / "schema", dst=output_dir / "schema", ignore=schema_filter)


def get_requires_for_build_editable(*args, **kwargs):
    _prebuild()
    return _origin.get_requires_for_build_editable(*args, **kwargs)


def get_requires_for_build_wheel(*args, **kwargs):
    _prebuild()
    return _origin.get_requires_for_build_wheel(*args, **kwargs)


def get_requires_for_build_sdist(*args, **kwargs):
    _prebuild()
    return _origin.get_requires_for_build_sdist(*args, **kwargs)
