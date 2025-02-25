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

import argparse
import os
import pathlib
import re

import git as GitPython
import github as PyGithub
import semver
from github.Repository import Repository

repo_root = pathlib.Path(__file__).parent.parent.absolute()
examples_root = repo_root / "examples"
schema_root = repo_root / "schema"


github_repo: Repository | None = None


def does_file_exist_on_main(file_path) -> bool:
    if github_repo is None:
        return True
    try:
        github_repo.get_contents(file_path, "main")
    except PyGithub.GithubException as exc:
        if exc.status == 404:
            return False
        raise
    return True


def initialise_git():
    # If the token is set up, we can use it to check if schemas already exist on main.
    # If they don't exist, the default prompt changes to 'Modify' instead of 'Bump'.
    if not (github_token := os.environ.get("GITHUB_TOKEN")):
        return

    git = GitPython.Repo(repo_root)
    if git.active_branch.name == "main":
        return

    remote = next(git.remote().urls)
    if m := re.match("git@github.com:(?P<org>[^/]+)/(?P<repo>[^/]+).git", remote):
        org = m.group("org")
        repo = m.group("repo")
    else:
        return

    auth = PyGithub.Auth.Token(github_token)
    gh = PyGithub.Github(auth=auth)
    org = gh.get_organization(org)

    global github_repo
    github_repo = org.get_repo(repo)


def get_version(schema_id: pathlib.PurePosixPath):
    return semver.Version.parse(schema_id.parent.name)


def is_latest_version_of_schema(schema_id: pathlib.PurePosixPath, options):
    if schema_id in options.new_schemas:
        return True
    if any(schema_id.is_relative_to(new_schema_id.parent.parent) for new_schema_id in options.new_schemas):
        return False

    current_version = get_version(schema_id)
    path = schema_root / schema_id
    for path in path.parent.parent.iterdir():
        if not any(path.iterdir()):
            continue  # empty folder
        version = semver.Version.parse(path.name)
        if version > current_version:
            return False
    return True


def find_usages(schema_id: pathlib.PurePosixPath, options):
    for path in schema_root.rglob("*.json"):
        content = path.read_text(encoding="utf-8")
        if f'"/{schema_id}"' not in content:
            continue
        content_schema_id = pathlib.PurePosixPath(path.relative_to(schema_root))
        if content_schema_id == schema_id:
            continue
        if str(content_schema_id) == "geoscience-objects.schema.json":
            continue  # root schema is auto-generated
        if not is_latest_version_of_schema(content_schema_id, options):
            continue
        yield content_schema_id
    for content_schema_id, content in options.new_schemas.items():
        if f'"/{schema_id}"' not in content:
            continue
        yield content_schema_id


def update_content(to_update, old, new, options):
    print(f" - updating {to_update}, using {new} now")
    options.new_schemas[to_update] = options.new_schemas[to_update].replace(str(old), str(new))


def copy_examples(old_schema_id, new_schema_id, options):
    schema_type, schema_name, old_schema_version, _ = old_schema_id.parts
    _, _, new_schema_version, _ = new_schema_id.parts
    for old_example in (examples_root / old_schema_version / schema_type).glob(f"{schema_name}*.json"):
        content = old_example.read_text(encoding="utf-8")
        new_example = pathlib.Path(new_schema_version) / schema_type / old_example.name
        options.new_examples[new_example] = content.replace(str(old_schema_id), str(new_schema_id))


def clone_schema(schema_id: pathlib.PurePosixPath, options):
    print(f"Cloning {schema_id}")
    old_version = get_version(schema_id)
    new_version = old_version.next_version(part=options.part)
    new_schema_id = schema_id.parent.parent / str(new_version) / schema_id.name
    if new_schema_id in options.new_schemas:
        return new_schema_id

    usages = list(find_usages(schema_id, options))
    options.new_schemas[new_schema_id] = (schema_root / schema_id).read_text(encoding="utf-8")
    update_content(new_schema_id, schema_id, new_schema_id, options)
    copy_examples(schema_id, new_schema_id, options)

    for usage in usages:
        if usage in options.new_schemas:
            update_content(usage, schema_id, new_schema_id, options)
        else:
            print(f"{usage} uses {schema_id}")
            if does_file_exist_on_main(f"/schema/{usage}"):
                default = "b"
                prompt = "[B/m/s]"
            else:
                default = "m"
                prompt = "[b/M/s]"
                print("- schema does not exist on main")
            if options.prompt:
                choice = None
                while choice not in ("b", "m", "s"):
                    choice = input(f"Bump version, Modify or Skip? {prompt}: ").lower() or default
            else:
                choice = default
            match choice:
                case "b":  # Bump
                    new_usage = clone_schema(usage, options)
                    update_content(new_usage, schema_id, new_schema_id, options)
                case "m":  # Modify
                    options.new_schemas[usage] = (schema_root / usage).read_text(encoding="utf-8")
                    update_content(usage, schema_id, new_schema_id, options)
    return new_schema_id


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("schema", help="The schema to clone, use the schema $id")
    parser.add_argument(
        "-p", "--part", choices=["major", "minor", "patch"], default="patch", help="Part of the version to bump."
    )
    parser.add_argument(
        "-y", "--yes", action="store_false", dest="prompt", help="Automatically apply changes, do not ask the user."
    )
    parser.add_argument("-f", "--force", action="store_true", help="Allow cloning schemas that are not on main.")
    options = parser.parse_args()
    options.new_schemas = {}
    options.new_examples = {}

    initialise_git()
    if not options.force and not does_file_exist_on_main(f"/schema{options.schema}"):
        print("Schema is not on main, use --force to clone anyway.")
        return

    schema = pathlib.PurePosixPath(options.schema)
    if schema.is_absolute():
        schema = schema.relative_to("/")
    clone_schema(schema, options)

    for schema_id, content in options.new_schemas.items():
        path = schema_root / schema_id
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    for example_path, content in options.new_examples.items():
        path = examples_root / example_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
