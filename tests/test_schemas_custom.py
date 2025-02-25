"""
   Copyright © 2025 Bentley Systems, Incorporated
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import itertools
import pprint
import re
import types
from collections import defaultdict
from pathlib import Path

import pytest
import semver
from jsonschema.validators import Draft202012Validator, create, validator_for

from tools.common import generate_all_paths, json_file_to_dict
from tools.schema_walker import SchemaWalker
from tools.schemas import (
    check_schema_against_draft,
    generate_all_schema_paths,
    generate_latest_schema_paths,
    schema_base_path,
    unittest_schema_base_path,
)

dict_values = type({}.values())  # this is not part of 'types'


def generate_all_paths_including_test_schemas(exclude_lineage=False):
    """Generator that gathers all the schema files in the schema
    directory and the test-schema directory"""
    schema_paths = generate_all_paths(schema_base_path(), "/**/*.json")
    if exclude_lineage:
        schema_paths = filter(lambda pth: not pth.endswith("lineage.schema.json"), schema_paths)

    return itertools.chain(
        schema_paths,
        generate_all_paths(unittest_schema_base_path(), "/*.json"),
    )


def generate_object_schema_paths():
    """Generator that gathers all the schema files in the schema
    objects directory and *not* the test-schema directory"""
    return generate_all_paths(schema_base_path(), "/objects/**/*.json")


@pytest.mark.parametrize("schema_path", generate_all_schema_paths())
def test_id_matches_schema_location(schema_path):
    schema = json_file_to_dict(schema_path)
    schema_id = schema["$id"]
    schema_root = schema_base_path().as_posix()
    assert schema_id == schema_path.removeprefix(schema_root)


@pytest.mark.parametrize("schema_path", generate_all_schema_paths())
def test_schema_folder_matches_schema_filename_or_filename_prefix(schema_path):
    # the schema path should be /schema/<type>/<name>/<version>/<name>.schema.json
    # or /schema/<type>/<name>/<version>/<items_folder>/<name>_<item>.schema.json
    # this test ensures that the two <name> fields match
    folder, _, filename = Path(schema_path).parts[-3:]
    if semver.Version.is_valid(folder):
        folder, _, _, filename = Path(schema_path).parts[-4:]
        assert filename.startswith(folder)
    else:
        assert folder == filename.removesuffix(".schema.json")


@pytest.mark.parametrize("schema_path", generate_all_paths_including_test_schemas())
def test_check_schema_draft(schema_path):
    schema = json_file_to_dict(schema_path)
    assert "$schema" in schema, "The schema must specify a schema draft under the key $schema"

    dummy_validator = create(meta_schema={"$id": ""})
    validator = validator_for(schema, default=dummy_validator)
    meta_schema_name = schema["$schema"]
    assert validator is not dummy_validator, f"schema '{meta_schema_name}', does not exist"

    assert validator is Draft202012Validator, f"schema '{meta_schema_name}' must be the latest (Draft 2020-12)"

    check_schema_against_draft(schema)  # will raise an exception on failure


@pytest.mark.parametrize("schema_path", generate_all_paths_including_test_schemas())
def test_schema_has_description(schema_path):
    schema = json_file_to_dict(schema_path)
    assert "description" in schema, "Description is missing"
    assert isinstance(schema["description"], str), "Description is not of type String"
    assert len(schema["description"]) > 0, "Description is empty"


@pytest.mark.parametrize("schema_path", generate_all_paths_including_test_schemas(exclude_lineage=True))
def test_property_names_are_snake_case(subtests, schema_path):
    class SnakeCaseWalker(SchemaWalker):
        walk_subschemas = False
        SNAKE_CASE_RE = re.compile(r"^[a-z][a-z0-9]*(_[a-z0-9]+)*$")

        def property_(self, validator, prop, _, schema):
            with subtests.test(msg=prop):
                assert self.SNAKE_CASE_RE.match(prop) is not None, f"Failed for {prop}"
            yield from super().property_(validator, prop, _, schema)

    schema = json_file_to_dict(schema_path)
    SnakeCaseWalker(schema).walk()


@pytest.mark.parametrize("schema_path", generate_all_schema_paths())
def test_schema_names_are_kebab_case(schema_path):
    assert (
        re.match(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*\.schema\.json$", Path(schema_path).name) is not None
    ), f"Failed for {schema_path}"


@pytest.mark.parametrize("schema_path", generate_object_schema_paths())
def test_base_object_property_set_on_objects(schema_path):
    """Checks if objects use our base set of properties. These properties
    should be 'inherited' from our base-object-properties component by using
    allOf and composing the base-object-properties with the properties of the
    object.
    Also checks that the object has a 'schema' property which is 'const' and matches the '$id' value.
    """
    required_all_of_refs = {"base-object-properties.schema.json", "base-spatial-data-properties.schema.json"}
    actual_all_of_refs = set()
    schema_props = []

    class MinimumPropertySetWalker(SchemaWalker):
        walk_subschemas = False

        def allOf(self, validator, allOf, instance, schema):
            super().allOf(validator, allOf, instance, schema)
            for index, subschema in enumerate(allOf):
                if "$ref" in subschema:
                    actual_all_of_refs.add(Path(subschema["$ref"]).name)

        def property_(self, validator, prop, _, schema):
            if self._property == ["/", "schema"]:
                assert "const" in schema, "'schema' property needs to be const"
                assert len(schema) == 1, "'schema' property should only contain 'const' keyword"
                schema_props.append(schema["const"])
            yield from super().property_(validator, prop, _, schema)

    schema = json_file_to_dict(schema_path)
    MinimumPropertySetWalker(schema).walk()
    assert (
        len(required_all_of_refs & actual_all_of_refs) > 0
    ), f"Missing a reference to one of the base properties: {required_all_of_refs}"

    assert "schema" in schema.get("required", []), "'schema' property must be 'required'"
    assert len(schema_props) == 1, "Objects need exactly one 'schema' property"
    assert schema_props[0] == schema.get("$id"), "Schema '$id' needs to match 'schema' property"


@pytest.mark.parametrize("schema_path", generate_all_paths_including_test_schemas(exclude_lineage=True))
def test_property_properties(subtests, schema_path):
    """Checks if properties have required properties"""
    required_properties = [("description",), ("type", "const", "$ref", "allOf", "anyOf", "oneOf")]

    class MinimumPropertySetWalker(SchemaWalker):
        walk_subschemas = False

        def property_(self, validator, prop, _, schema):
            actual_properties = set(schema)
            with subtests.test(msg=prop):
                for req in required_properties:
                    with subtests.test(msg=req):
                        if prop == "schema":
                            # we don't expect any properties on the schema field
                            continue
                        if prop == "attribute_type" and any(p in actual_properties for p in ("const", "enum")):
                            # this is a hack and we have to find a better solution if we add more properties:
                            # the attribute_type is defined in a base-class and the subclass defines the value (const)
                            continue
                        assert any(
                            r in actual_properties for r in req
                        ), f"property '{prop}' is missing '{', '.join(req)}'"
            yield from super().property_(validator, prop, _, schema)

    schema = json_file_to_dict(schema_path)
    MinimumPropertySetWalker(schema).walk()


@pytest.mark.parametrize("schema_path", generate_all_paths_including_test_schemas())
def test_required_list_only_contains_valid_properties(schema_path):
    all_properties = defaultdict(list)
    required_properties = {}

    class RequiredListWalker(SchemaWalker):
        walk_subschemas = False

        def required(self, validator, required, _, schema):
            if {"properties", "allOf"}.intersection(schema):
                # collect required properties if the sub-schema has properties
                required_properties[tuple(self._scope)] = required

        def property_(self, validator, prop, _, schema):
            all_properties[tuple(self._scope[:-1])].append(prop)
            yield from super().property_(validator, prop, _, schema)

        def example(self, validator, example, _, schema):
            result = self._validate_example(example)
            validation_should_pass = example.get("pass", True)
            if validation_should_pass:
                assert result is None, f"Example validation failed: '{example}', reason={result}"
            else:
                assert result is not None, f"Example validation passed but should have failed: '{example}'"

    def flatten(i):
        # helper that flattens iterables of any depth into a list of unique items
        if not isinstance(i, (list, tuple, set, types.GeneratorType, dict_values)):
            return [i]
        return list(set(k for j in i for k in flatten(j)))

    def iter_prop_groups(props):
        if not props:
            # nothing to process - yield an empty list
            yield []
            return

        if () in props:
            # root item - return its properties
            yield props[()]
            return

        # build a group of subgroups
        groups = defaultdict(lambda: defaultdict(dict))
        for k, v in props.items():
            # k is a tuple of scopes, each scope is also a tuple
            # k[0][0] is the type of the first scope (i.e. oneOf, anyOf, AllOf, <property name>)
            # k[0][1:] is the remainder of the first scope (e.g. the branch number in a oneOff)
            # k[1:] contains the remaining part of the scope
            groups[k[0][0]][k[0][1:]][k[1:]] = v

        group_outputs = []
        for key, group in groups.items():
            # key is the type of the first scope
            # group is a dict over the remainder of the first scope
            if key not in ("oneOf", "anyOf", "allOf"):
                # fixed property, handled by caller directly
                continue

            child_items = {}
            for k, child in group.items():
                # k is the branch number of the first scope
                # child is a dict over the remaining parts of the scope
                child_props = iter_prop_groups(child)  # all properties that this child would generate
                child_items[k] = flatten(child_props)  # we only care about the worst case (all properties)
            if key == "oneOf":
                # oneOf - check child items individually
                group_output = list(child_items.values())
            elif key == "anyOf":
                # anyOf - checking items individuall is the worst case. No need for permutations
                group_output = list(child_items.values())
            elif key == "allOf":
                # allOf - merge everything together
                group_output = [flatten(child_items.values())]
            group_outputs.append(group_output)

        for g in itertools.product(*group_outputs):
            # check the cartesian product of all groups
            yield flatten(g)

    def iter_subschema_permutations(scope):
        fixed_props = []
        complex_props = {}
        for k, props in all_properties.items():
            if k == scope:
                # root property - just collect these
                fixed_props.extend(props)
            elif k[: len(scope)] == scope:
                # nested property - collect with the remainder of the scope
                complex_props[k[len(scope) :]] = props
            elif scope[:-1] == k:
                # nested required property - collect with the remainder of the scope
                fixed_props.extend(props)

        for group in iter_prop_groups(complex_props):
            yield fixed_props + group

    schema = json_file_to_dict(schema_path)
    RequiredListWalker(schema).walk()

    for scope, required_props in required_properties.items():
        assert len(required_props) == len(set(required_props)), "Duplicate entries found in 'required' list"

        for actual_props in iter_subschema_permutations(scope):
            # all possible permutations of properties must match the 'required' field
            assert set(required_props).issubset(set(actual_props)), "'required' list contains invalid property"


@pytest.mark.parametrize("schema_path", generate_latest_schema_paths())
def test_latest_version_references_latest_version(subtests, schema_path):
    # These schemas are no longer maintained, so their last versions will not necessarily reference the newest versions
    # of other schemas
    DEPRECATED_SCHEMAS = {
        "planar-structural-data",
        "structural-lineations-pointset",
        "structural-planar-data-pointset",
        "interval-downholes",
    }

    def is_latest_schema_path(schema_path):
        path = Path(schema_path)
        group_directory = path.parent
        if semver.Version.is_valid(group_directory.parent.name):
            group_directory = path.parent.parent
        all_versions = map(lambda p: p.name, group_directory.parent.iterdir())
        latest_version = max(all_versions, key=semver.Version.parse)
        schema_version = semver.Version.parse(group_directory.stem + group_directory.suffix)
        return latest_version == schema_version

    class LatestReferencesWalker(SchemaWalker):
        def __init__(self, schema):
            super().__init__(schema)

        def dollar_ref(self, validator, ref, _, schema):
            if not ref.startswith("#"):  # local fragments/references are always the same version.
                resolved_ref = f"schema/{ref}"
                with subtests.test(msg=ref):
                    assert is_latest_schema_path(resolved_ref), f"Failed for {ref}. Must reference the latest version."

    # Sanity test. The latest should be passed to the test!
    assert is_latest_schema_path(schema_path), f"{schema_path} is not the latest version of the schema."

    schema_name = Path(schema_path).name.split(".")[0]
    if schema_name not in DEPRECATED_SCHEMAS:
        schema = json_file_to_dict(schema_path)

        walker = LatestReferencesWalker(schema)
        walker.walk()


@pytest.mark.parametrize("schema_path", generate_object_schema_paths())
def test_schema_uses_single_version_of_subschemas(subtests, schema_path):
    class ReferencesWalker(SchemaWalker):
        def __init__(self, schema):
            super().__init__(schema)
            self._failed = False  # stops after the first error to avoid spam
            self._walked_refs = set()  # avoid scanning the same refs multiple times
            self._references: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))

        def dollar_ref(self, validator, ref, instance, schema):
            if self._failed:
                return
            if ref in self._walked_refs:
                return
            self._walked_refs.add(ref)

            if not ref.startswith("#"):
                version, filename = Path(ref.removesuffix(".schema.json")).parts[-2:]
                if not semver.Version.is_valid(version):
                    version, _, filename = Path(ref).parts[-3:]

                self._references[filename][version].add(self.scope_repr)
                if len(self._references[filename]) > 1:
                    with subtests.test(msg=ref):
                        self._failed = True
                        pprint.pp(self._references[filename])
                        assert False, f"Multiple versions of {filename} used"

            yield from super().dollar_ref(validator, ref, instance, schema)

    schema = json_file_to_dict(schema_path)
    walker = ReferencesWalker(schema)
    walker.walk()


def test_all_components_and_elements_used():
    # check that all components and elements are used
    allowed_unused = {
        "/elements/integer-array-2/1.0.1/integer-array-2.schema.json",
        "/elements/integer-array-3/1.0.1/integer-array-3.schema.json",
    }

    queue = set(generate_object_schema_paths())
    used_schemas = set()

    class ReferencesWalker(SchemaWalker):
        def __init__(self, schema):
            super().__init__(schema)

        def dollar_ref(self, validator, ref, _, schema):
            if ref.startswith("#"):  # ignore local fragments/references
                return
            schema_path = (schema_base_path() / ref.lstrip("/")).as_posix()
            queue.add(schema_path)

    def check_schema(schema_path):
        schema = json_file_to_dict(schema_path)
        used_schemas.add(schema_path)
        walker = ReferencesWalker(schema)
        walker.walk()

    while queue:
        check_schema(queue.pop())

    all_schemas = set(generate_all_schema_paths())
    unused_schemas = {f"/{Path(p).relative_to(schema_base_path()).as_posix()}" for p in (all_schemas - used_schemas)}
    unused_schemas -= allowed_unused
    assert not unused_schemas


@pytest.mark.parametrize("schema_path", generate_all_paths(unittest_schema_base_path(), "/*.json"))
def test_walking_subschemas(schema_path):
    # Simple test for easier debugging than a large object schema.
    schema = json_file_to_dict(schema_path)

    walker = SchemaWalker(schema)
    walker.walk()
