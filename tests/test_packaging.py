"""Test that our github test matrix matches the supported python versions."""
import itertools
from typing import TYPE_CHECKING

import yaml

if TYPE_CHECKING:
    # Hide the import shenanigans that follow from our IDE / type-checkers
    import tomllib
else:
    # In reality we need to deal with tomllib not being available for
    # python3.10, by using the backport package tomli.
    try:
        import tomllib
    except ModuleNotFoundError:
        import tomli as tomllib

from pathlib import Path

from packaging.specifiers import SpecifierSet


def _get_required_python() -> SpecifierSet:
    pyproj_data = tomllib.loads((Path(__file__).parents[1] / "pyproject.toml").read_text())
    requires_python = pyproj_data["project"]["requires-python"]
    return SpecifierSet(requires_python)


def _get_allowed_python_versions(spec: SpecifierSet) -> list[str]:
    candidates = [
        f"{major}.{minor}"
        for major, minor in itertools.product(
            ["3", "4"],  # major versions, even including a hypothetical python 4.x
            range(0, 50),  # minor versions up to 50
        )
    ]
    return list(spec.filter(candidates))


def _get_tested_pythons():
    test_workflow_file = Path(__file__).parents[1] / ".github" / "workflows" / "run-tests.yml"
    assert test_workflow_file.exists()
    workflow_data = yaml.safe_load(test_workflow_file.read_text())
    return workflow_data["jobs"]["unit-tests"]["strategy"]["matrix"]["python-version"]


def test_supported_python_version_matches_gha_matrix():
    required_python_spec = _get_required_python()
    allowed_pythons = _get_allowed_python_versions(required_python_spec)
    assert allowed_pythons == _get_tested_pythons()
