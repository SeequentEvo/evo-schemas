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

import builtins
import pathlib

from tools.code_generator.parser import SchemaClass, SchemaProperty, run_parser_on_object_schemas
from tools.schemas import schema_base_path


class MarkdownGenerator:
    def __init__(self, parser, path: pathlib.Path):
        self.parser = parser
        self.path = path
        path.mkdir(parents=True, exist_ok=True)

    def _get_path(self, cls) -> str:
        name = "-".join(cls.name[1:])
        return f"{cls.name[0]}/{name}.md"

    def _get_name(self, cls, include_version=True) -> str:
        name = cls.name[1]
        if include_version:
            return f"{name} (v{cls.name[2]})"
        return name

    def _get_link(self, cls):
        return f"../{self._get_path(cls)}"

    def _get_flags(self, prop, inherited: bool = False) -> str:
        flags = []
        if inherited:
            flags.append(f"[⬆️]({self._get_link(prop.parent)})")
        if prop.name in prop.parent.required:
            flags.append("✅")

        return " ".join(flags)

    def _get_type(self, prop) -> str:
        prop_type = prop.type if isinstance(prop, SchemaProperty) else prop
        match prop_type:
            case "boolean" | "integer" | "number" | "object" | "string":
                return prop_type.title()
            case builtins.str:
                return "String"
            case builtins.int:
                return "Integer"
            case "array":
                return f"Array[{self._get_type(prop.items)}]"
            case SchemaClass():
                return f"[{self._get_name(prop_type, include_version=False)}]({self._get_link(prop_type)})"
            case _:
                raise ValueError(f"Unknown type {prop_type}")

    def _generate_props(self, cls, inherited: bool = False):
        for base_cls in cls.baseclasses or []:
            yield from self._generate_props(base_cls, inherited=True)

        for prop in cls.props:
            name = prop.name
            type_ = self._get_type(prop)
            description = prop.description or ""
            flags = self._get_flags(prop, inherited)
            yield f"| {name} | {type_} | {description} | {flags} |\n"

    def generate(self):
        for cls in self.parser.iter_classes():
            path = self.path / self._get_path(cls)
            path.parent.mkdir(exist_ok=True)
            with path.open("w", encoding="utf-8") as f:
                f.write(f"### {self._get_name(cls)}\n")
                if cls.description:
                    f.write(f"{cls.description}\n")
                f.write("\n")
                f.write("| Property | Type | Description | Flags |\n")
                f.write("|---|---|---|---|\n")
                f.writelines(self._generate_props(cls, inherited=False))
                f.write("\n")
                f.write(
                    """
#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

"""
                )

            pass


def generate_markdown_files(parser, result_path=None) -> pathlib.Path:
    if result_path is None:
        result_path = (schema_base_path() / ".." / "docs" / "md").resolve()

    generator = MarkdownGenerator(parser, result_path)
    generator.generate()
    return result_path


def main():
    parser = run_parser_on_object_schemas()
    generate_markdown_files(parser)


if __name__ == "__main__":
    main()
