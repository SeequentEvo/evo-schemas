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
"""PlantUML visualizer for schema objects"""

import os
from collections import defaultdict
from pathlib import Path
from textwrap import dedent, indent
from typing import Union

from .code_generator.markdown_generator import MarkdownGenerator
from .code_generator.parser import SchemaClass, run_parser_on_object_schemas


class SchemaType:
    """Simplified schema object"""

    def __init__(self, schema):
        self.schema = schema
        self.object_type = schema.name[1]
        self.object_version = schema.name[2]

    @property
    def id(self):
        return self.schema.id

    @property
    def name(self):
        return self.schema.name[1]

    @property
    def baseclasses(self):
        return self.schema.baseclasses

    @property
    def props(self):
        return self.schema.props


class SchemaVisualizer:
    _identifier_map = {"components": "abstract", "elements": "abstract", "objects": "class"}
    _mermaid_format_string = dedent(
        """\
        ---
        config:
            class:
                hideEmptyMembersBox: true
        ---

        classDiagram
        {}
        """
    )
    _plantuml_format_string = dedent(
        """\
        @startuml
        hide empty members
        set separator ::
        skinparam class {{
            BackgroundColor Gainsboro
            HeaderBackgroundColor #444
            BackgroundColor<< implicit interface >> White
            FontColor automatic
            StereotypeFontColor automatic
        }}
        {}
        @enduml"""
    )
    _type_map = {
        "int": "integer",
        "str": "string",
    }

    def __init__(self):
        # Dictionary of objects and their versions
        self._objects = defaultdict(list)
        # Dictionary of all SchemaTypes
        self._types = dict()
        self._index_all_objects()

    def _index_all_objects(self) -> None:
        """Build an index of all objects and their versions"""
        parser = run_parser_on_object_schemas()
        for schema in parser.iter_classes():
            schema_type = SchemaType(schema)
            self._types[schema_type.id] = schema_type
            if schema.is_root:
                self._objects[schema_type.object_type].append(schema_type)

    def get_last_version(self, object_type: str) -> SchemaType:
        """Get the latest version of the schema object by name

        Parameters
        ----------
        object_type : str
            Name of the schema object

        Returns
        -------
        SchemaType
            Simplified schema object
        """
        try:
            last_version = self._objects[object_type][-1]
        except (IndexError, KeyError):
            raise KeyError(f'Schema for "{object_type}" not found')
        return last_version

    def _get_hierarchy(self, schema_type: SchemaType) -> list:
        """Get the base class hierarchy of the schema type (recursively)

        Parameters
        ----------
        schema_type : SchemaType
            Simplified schema object

        Returns
        -------
        list
            List of base classes
        """
        base_classes = []
        if schema_type.baseclasses:
            for base_class in schema_type.baseclasses:
                base_object = self._types[base_class.id]
                if base_object:
                    base_classes.extend(self._get_hierarchy(base_object))
        base_classes.append(schema_type)
        return base_classes

    @staticmethod
    def _make_full_name(schema: SchemaClass) -> str:
        """Generate full name of the schema

        Parameters
        ----------
        schema : SchemaClass
            Schema object

        Returns
        -------
        str
            Full name of the schema
        """
        full_name = f"{schema.name[0]}/" + "-".join(schema.name[1:])
        return full_name

    @staticmethod
    def _make_mermaid_association_line(full_name: str, type_name: str, prop_name: str) -> str:
        """Generate Mermaid code for an inline reference to another schema

        Parameters
        ----------
        full_name : str
            Full name of the current schema
        type_name : str
            Full name of the referenced schema
        prop_name : str
            Name of the property that references the schema

        Returns
        -------
        str
            Mermaid code for the association line
        """
        association_line = f"`{full_name}` *-- `{type_name}` : ref {prop_name}*"
        return association_line

    @staticmethod
    def _make_mermaid_prop_line(
        prop_name: str, type_name: str, ref: bool = False, parent: bool = False, const=None
    ) -> str:
        """Generate Mermaid code for the property line

        Parameters
        ----------
        prop_name : str
            Property name
        type_name : str
            Type of the property or reference to a schema
        ref : bool
            True if the property is a reference to another schema
        parent : bool
            True if the property is a parent property
        const : str
            Constant value of the property (if applicable)

        Returns
        -------
        str
            Mermaid code for the property line
        """
        prop_line = (
            f"    {prop_name}: {type_name}"
            f'{" = " + str(const) if const is not None else ""}'
            f'{"*" if parent else ""}'
        )
        return prop_line

    @staticmethod
    def _make_mermaid_parentage_line(parent_name: str, current_name: str) -> str:
        """
        Generate Mermaid code for the parentage line

        Parameters
        ----------
        parent_name : str
            Name of the parent class
        current_name : str
            Full name of the current class

        Returns
        -------
        str
            Mermaid code for the parentage line
        """
        parent_line = f"`{parent_name}` <|-- `{current_name}`"
        return parent_line

    @staticmethod
    def _make_plantuml_association_line(full_name: str, type_name: str, prop_name: str) -> str:
        """Generate PlantUML code for an inline reference to another schema

        Parameters
        ----------
        full_name : str
            Full name of the current schema
        type_name : str
            Full name of the referenced schema
        prop_name : str
            Name of the property that references the schema

        Returns
        -------
        str
            PlantUML code for the association line
        """
        association_line = f'"{full_name}" *-r[#gray]- "{type_name}" : ref: <i>{prop_name}</i>'
        return association_line

    @staticmethod
    def _make_plantuml_prop_line(
        prop_name: str, type_name: str, ref: bool = False, parent: bool = False, const=None
    ) -> str:
        """Generate PlantUML code for the property line

        Parameters
        ----------
        prop_name : str
            Property name
        type_name : str
            Type of the property or reference to a schema
        ref : bool
            True if the property is a reference to another schema
        parent : bool
            True if the property is a parent property
        const : str
            Constant value of the property (if applicable)

        Returns
        -------
        str
            PlantUML code for the property line
        """
        prop_line = (
            f'  {"<font color=gray>" if parent else ""}'
            f"{prop_name}: "
            f'{"<i>" if ref else ""}{type_name}{"</i>" if ref else ""}'
            f'{" = " + str(const) if const is not None else ""}'
            f'{"</font>" if parent else ""}'
        )
        return prop_line

    @staticmethod
    def _make_plantuml_parentage_line(parent_name: str, current_name: str) -> str:
        """
        Generate PlantUML code for the parentage line

        Parameters
        ----------
        parent_name : str
            Name of the parent class
        current_name : str
            Full name of the current class

        Returns
        -------
        str
            PlantUML code for the parentage line
        """
        parent_line = f'"{parent_name}" <|-- "{current_name}"'
        return parent_line

    def _find_schema_for_ref(self, ref: str) -> Union[SchemaType, None]:
        """Find the schema object for a reference

        Parameters
        ----------
        ref : str
            Reference to a schema object

        Returns
        -------
        Union[SchemaType, None]
            Simplified schema object or None
        """
        if "def" in ref:
            return None
        ref_schema_name, ref_schema_version = ref.split("/")[2:4]
        try:
            ref_schema = next(
                (
                    item
                    for item in self._types.values()
                    if item.schema.name[1] == ref_schema_name and item.schema.name[2] == ref_schema_version
                )
            )
        except StopIteration:
            return None
        else:
            return ref_schema

    def _generate_mermaid_for_subtree(
        self, schema_type: SchemaType, render_associations: int, seen: Union[set, None] = None
    ) -> list:
        """Generate Mermaid code for the object hierarchy of a schema type

        Parameters
        ----------
        schema_type : SchemaType
            Simplified schema object
        render_associations : int
            Number of levels to render references to other schemas
        seen : Union[set, None]
            List of seen schema objects (used for deduplication)

        Returns
        -------
        list
            List of Mermaid code lines
        """
        parent = None
        lines = []
        extra_schemas = dict()
        associations = []
        parent_props = defaultdict(list)
        hierarchy = self._get_hierarchy(schema_type)
        if seen is None:
            seen = set()
        for schema_ref in hierarchy:
            render_schema = schema_ref.id not in seen
            schema_ref_hierarchy = self._get_hierarchy(schema_ref)
            full_name = self._make_full_name(schema_ref.schema)
            implicit_interface = len(schema_ref.schema.name) > 3
            identifier = schema_ref.schema.name[0][:-1] if not implicit_interface else "implicit"
            if render_schema:
                lines.append(f"class `{full_name}`:::schema{identifier.title()}" + " {")
            current_prop_names = [prop.name for prop in schema_ref.props]
            parent_lines = []
            for parent_id in (item.id for item in schema_ref_hierarchy):
                possible_parent_lines = parent_props[parent_id]
                for line in possible_parent_lines:
                    for prop_name in current_prop_names:
                        if prop_name in line:
                            break
                    else:
                        parent_lines.append(line)
            else:
                if render_schema:
                    lines.extend(parent_lines)
            for prop in schema_ref.props:
                if not hasattr(prop, "type") or prop.name == "schema":
                    continue
                elif isinstance(prop.type, SchemaClass):
                    if render_associations > 0:
                        extra_schemas[self._types[prop.type.id].id] = self._types[prop.type.id]
                    ref_name = self._make_full_name(prop.type)
                    propline = self._make_mermaid_prop_line(prop.name, ref_name, ref=True)
                    parent_props[schema_ref.id].append(
                        self._make_mermaid_prop_line(prop.name, ref_name, ref=True, parent=True)
                    )
                    association = self._make_mermaid_association_line(full_name, ref_name, prop.name)
                    if render_schema:
                        associations.append(association)
                elif isinstance(prop.type, type):
                    type_name = self._type_map.get(prop.type.__name__, prop.type.__name__)
                    const_value = prop.schema.get("const", None)
                    propline = self._make_mermaid_prop_line(prop.name, type_name, const=const_value)
                    parent_props[schema_ref.id].append(
                        self._make_mermaid_prop_line(prop.name, type_name, parent=True, const=const_value)
                    )
                else:
                    propline = self._make_mermaid_prop_line(prop.name, prop.type)
                    parent_props[schema_ref.id].append(self._make_mermaid_prop_line(prop.name, prop.type, parent=True))
                if render_schema:
                    lines.append(propline)
            if render_schema:
                lines.append("}")
            for candidate_parent in schema_ref_hierarchy[:-1]:
                if parent is not None and candidate_parent in self._get_hierarchy(parent)[:-1]:
                    continue
                parentage = self._make_mermaid_parentage_line(self._make_full_name(candidate_parent.schema), full_name)
                if render_schema:
                    lines.append(parentage)
            seen.add(schema_ref.id)
            parent = schema_ref
        if render_associations > 0:
            lines.extend(associations)
        for schema_ref in extra_schemas.values():
            sublines = self._generate_mermaid_for_subtree(schema_ref, render_associations - 1, seen=seen)
            lines.extend(sublines)
        return lines

    def generate_mermaid(self, schema_type: SchemaType, render_associations: int = 10) -> str:
        """Generate Mermaid code for the object hierarchy

        Parameters
        ----------
        schema_type : SchemaType
            Simplified schema object
        render_associations : int
            Number of levels to render references to other schemas

        Returns
        -------
        str
            Mermaid code for the object hierarchy
        """
        uml_body = indent("\n".join(self._generate_mermaid_for_subtree(schema_type, render_associations)), "    ")
        mermaid = self._mermaid_format_string.format(uml_body)
        return mermaid

    def _generate_plantuml_for_subtree(
        self, schema_type: SchemaType, render_associations: int, seen: Union[set, None] = None
    ) -> list:
        """Generate PlantUML code for the object hierarchy of a schema type

        Parameters
        ----------
        schema_type : SchemaType
            Simplified schema object
        render_associations : int
            Number of levels to render references to other schemas
        seen : Union[set, None]
            List of seen schema objects (used for deduplication)

        Returns
        -------
        list
            List of PlantUML code lines
        """
        parent = None
        lines = []
        extra_schemas = dict()
        associations = []
        parent_props = defaultdict(list)
        hierarchy = self._get_hierarchy(schema_type)
        if seen is None:
            seen = set()
        for schema_ref in hierarchy:
            render_schema = schema_ref.id not in seen
            schema_ref_hierarchy = self._get_hierarchy(schema_ref)
            full_name = self._make_full_name(schema_ref.schema)
            identifier = self._identifier_map[schema_ref.schema.name[0]]
            implicit_interface = len(schema_ref.schema.name) > 3
            if render_schema:
                lines.append(
                    f'{"interface" if implicit_interface else identifier} "{full_name}"'
                    f'{" <<implicit interface>>" if implicit_interface else ""}'
                    " {"
                )
            current_prop_names = [prop.name for prop in schema_ref.props]
            parent_lines = []
            for parent_id in (item.id for item in schema_ref_hierarchy):
                possible_parent_lines = parent_props[parent_id]
                for line in possible_parent_lines:
                    for prop_name in current_prop_names:
                        if prop_name in line:
                            break
                    else:
                        parent_lines.append(line)
            else:
                if render_schema:
                    lines.extend(parent_lines)
            if parent_lines and len(schema_ref.props) > 0:
                if render_schema:
                    lines.append("  ..")
            for prop in schema_ref.props:
                if not hasattr(prop, "type") or prop.name == "schema":
                    continue
                elif isinstance(prop.type, SchemaClass):
                    if render_associations > 0:
                        extra_schemas[self._types[prop.type.id].id] = self._types[prop.type.id]
                    ref_name = self._make_full_name(prop.type)
                    propline = self._make_plantuml_prop_line(prop.name, ref_name, ref=True)
                    parent_props[schema_ref.id].append(
                        self._make_plantuml_prop_line(prop.name, ref_name, ref=True, parent=True)
                    )
                    association = self._make_plantuml_association_line(full_name, ref_name, prop.name)
                    if render_schema:
                        associations.append(association)
                elif isinstance(prop.type, type):
                    type_name = self._type_map.get(prop.type.__name__, prop.type.__name__)
                    const_value = prop.schema.get("const", None)
                    propline = self._make_plantuml_prop_line(prop.name, type_name, const=const_value)
                    parent_props[schema_ref.id].append(
                        self._make_plantuml_prop_line(prop.name, type_name, parent=True, const=const_value)
                    )
                else:
                    propline = self._make_plantuml_prop_line(prop.name, prop.type)
                    parent_props[schema_ref.id].append(self._make_plantuml_prop_line(prop.name, prop.type, parent=True))
                if render_schema:
                    lines.append(propline)
            if render_schema:
                lines.append("}")
            for candidate_parent in schema_ref_hierarchy[:-1]:
                if parent is not None and candidate_parent in self._get_hierarchy(parent)[:-1]:
                    continue
                parentage = self._make_plantuml_parentage_line(self._make_full_name(candidate_parent.schema), full_name)
                if render_schema:
                    lines.append(parentage)
            seen.add(schema_ref.id)
            parent = schema_ref
        if render_associations > 0:
            lines.extend(associations)
        for schema_ref in extra_schemas.values():
            sublines = self._generate_plantuml_for_subtree(schema_ref, render_associations - 1, seen=seen)
            lines.extend(sublines)
        return lines

    def generate_plantuml(self, schema_type: SchemaType, render_associations: int = 10) -> str:
        """Generate PlantUML code for the object hierarchy

        Parameters
        ----------
        schema_type : SchemaType
            Simplified schema object
        render_associations : int
            Number of levels to render references to other schemas

        Returns
        -------
        str
            PlantUML code for the object hierarchy
        """
        uml_body = "\n".join(self._generate_plantuml_for_subtree(schema_type, render_associations))
        plantuml = self._plantuml_format_string.format(uml_body)
        return plantuml

    def generate_doc(self, schema_type: SchemaType) -> str:
        """Generate documentation for the geoscience object

        Parameters
        ----------
        schema_type : SchemaType
            Simplified schema object

        Returns
        -------
        str
            Documentation for the geoscience object
        """
        hierarchy = self._get_hierarchy(schema_type)
        title = f"{schema_type.name} v{schema_type.object_version}"
        property_lines = []
        last_ref = None
        for schema_ref in hierarchy:
            # Generate horizontal rules between sections
            if last_ref is not None:
                property_lines.append("---")
            last_ref = schema_ref

            # Generate section header
            if schema_ref is schema_type:
                property_lines.append("##### Defined on this object")
            else:
                property_lines.append(f"##### Inherited from `{schema_ref.name}`")

            #  Generate props
            for prop in schema_ref.props:
                if not hasattr(prop, "type") or prop.name == "schema":
                    continue
                elif isinstance(prop.type, SchemaClass) and len(prop.type.name) <= 3:
                    ref_name = self._make_full_name(prop.type)
                    propline = f"`{prop.name}` *{ref_name}*"
                elif isinstance(prop.type, SchemaClass):
                    if "oneOf" in prop.schema:
                        oneof = prop.schema["oneOf"]
                        typebundle = []
                        for item in oneof:
                            if "type" in item:
                                if item["type"] == "null":
                                    typebundle.append("null")
                                else:
                                    typebundle.append(
                                        f"*{item['type']}{' (' + item['format'] + ')' if 'format' in item else ''}*"
                                    )
                            elif "$ref" in item:
                                try:
                                    ref_schema_name, ref_schema_version = item["$ref"].split("/")[2:4]
                                    ref_schema = next(
                                        (
                                            item
                                            for item in self._types.values()
                                            if item.schema.name[1] == ref_schema_name
                                            and item.schema.name[2] == ref_schema_version
                                        )
                                    )
                                except StopIteration:
                                    pass
                                else:
                                    typebundle.append(f"*{self._make_full_name(ref_schema.schema)}*")
                            elif "const" in item:
                                typebundle.append(f"const *{item['const']}*")
                            else:
                                print(schema_ref.name)
                                print("Unhandled oneOf:", item)
                        propline = f"`{prop.name}` {' | '.join(typebundle)}"
                    elif "allOf" in prop.schema:
                        allof = prop.schema["allOf"]
                        typebundle = []
                        allof_no_requireds = [item for item in allof if "required" not in item]
                        for item in allof_no_requireds:
                            if "type" in item:
                                typebundle.append(
                                    f"*{item['type']}{' (' + item['format'] + ')' if 'format' in item else ''}*"
                                )
                            elif "$ref" in item:
                                ref_schema = self._find_schema_for_ref(item["$ref"])
                                if ref_schema is not None:
                                    typebundle.append(f"*{self._make_full_name(ref_schema.schema)}*")
                                else:
                                    typebundle.append("*object*")
                            elif "properties" in item:
                                for subpropname, subprop in item["properties"].items():
                                    if "ref" in subprop:
                                        ref_schema = self._find_schema_for_ref(subprop["$ref"])
                                        if ref_schema is None:
                                            typebundle.append(f"`{subpropname}` *object*")
                                        else:
                                            typebundle.append(
                                                f"`{subpropname}` *{self._make_full_name(ref_schema.schema)}*"
                                            )
                                    elif "allOf" in subprop:
                                        for subsubprop in subprop["allOf"]:
                                            ref_schema = self._find_schema_for_ref(subsubprop["$ref"])
                                            if ref_schema is None:
                                                typebundle.append(f"`{subpropname}` *object*")
                                            else:
                                                typebundle.append(
                                                    f"`{subpropname}` *{self._make_full_name(ref_schema.schema)}*"
                                                )
                                    else:
                                        typebundle.append(f"`{subpropname}` *object*")
                            elif "const" in item:
                                typebundle.append(f"const *{item['const']}*")
                            else:
                                print(schema_ref.name)
                                print("Unhandled allOf:", item)
                        if len(allof_no_requireds) > 1:
                            propline = f"`{prop.name}` all of [{', '.join(typebundle)}]"
                        else:
                            propline = f"`{prop.name}` {typebundle[0]}"
                    elif "$ref" in prop.schema:
                        ref_schema = self._find_schema_for_ref(prop.schema["$ref"])
                        if ref_schema is not None:
                            propline = f"`{prop.name}` *{self._make_full_name(ref_schema.schema)}*"
                        else:
                            propline = f"`{prop.name}` *object*"
                    elif "properties" in prop.schema:
                        lprops = ", ".join((f"`{_}`" for _ in prop.schema["properties"].keys()))
                        propline = f"`{prop.name}` *object* with props {lprops}"
                    else:
                        propline = f"`{prop.name}` *object*"
                elif isinstance(prop.type, type):
                    type_name = self._type_map.get(prop.type.__name__, prop.type.__name__)
                    const_value = prop.schema.get("const", None)
                    propline = (
                        f"`{prop.name}` *{type_name}*{' = const ' + const_value if const_value is not None else ''}"
                    )
                else:
                    propline = f"`{prop.name}` *{prop.type}*"
                property_lines.append(
                    f"{'**Required**' if prop.name in schema_ref.schema.required else '**Optional**'} {propline}"
                )
                property_lines.append(f"> {prop.schema.get('description', 'No description available')}\n  ")

        docstring = "\n".join(
            (
                f"#### {title}\n",
                schema_type.schema.description,
                "\n\n".join(property_lines),
            )
        )
        if docstring is None:
            docstring = "No documentation available"
        return docstring

    def main_cli(self):
        """CLI for the PlantUML visualizer"""
        import argparse

        parser = argparse.ArgumentParser(description="Generate PlantUML code for the schema objects")
        parser.add_argument("--autodoc", action="store_true", help="Generate PlantUML code for all schemas")
        parser.add_argument("object_type", nargs="?", help="Name of the schema object")
        parser.add_argument(
            "--associations",
            type=int,
            default=10,
            help="Number of levels to render references to other schemas (default: 10)",
        )
        parser.add_argument(
            "--schema_version",
            type=str,
            default=None,
            help="Version of the schema object (default: latest version)",
        )
        parser.add_argument(
            "--output_dir",
            type=str,
            default=Path.cwd() / "docs" / "schemas" / "generated",
            help="Output directory for the generated documentation (default: docs/schemas/generated)",
        )
        parser.add_argument(
            "--output_mermaid",
            action="store_true",
            help="Output Mermaid code to the console (default: False)",
        )
        parser.add_argument(
            "--output_plantuml",
            action="store_true",
            help="Output PlantUML code to the console (default: False)",
        )
        parser.add_argument(
            "--output_doc",
            action="store_true",
            help="Output documentation to the console (default: False)",
        )
        args = parser.parse_args()
        if args.autodoc:
            output_dir = Path(args.output_dir)
            os.makedirs(output_dir, exist_ok=True)
            schema_count = 0
            schema_version_count = 0
            uml_dir = output_dir / "uml"
            os.makedirs(uml_dir, exist_ok=True)
            flatmd_dir = output_dir / "flatmd"
            os.makedirs(flatmd_dir, exist_ok=True)
            for schema_object_list in self._objects.values():
                schema_count += 1
                for schema_object in schema_object_list:
                    schema_version_count += 1
                    # Generate Mermaid code
                    mermaid = self.generate_mermaid(schema_object, args.associations)
                    outfile = f"{schema_object.name}-{schema_object.object_version}.mmd"
                    with open(uml_dir / outfile, "w") as fp:
                        fp.write(mermaid)
            print(f"Generated docs code for {schema_count} schema objects with {schema_version_count} total versions")
            print("Running Markdown generator for flattened schema model...")
            generator = MarkdownGenerator(run_parser_on_object_schemas(), flatmd_dir)
            generator.generate()
            print(f"Output directory: {output_dir}")
            sys.exit(0)
        elif args.object_type is None:
            parser.error("the following arguments are required: object_type")
        elif args.schema_version is None:
            try:
                schema_object = self.get_last_version(args.object_type)
            except KeyError:
                parser.error(f'schema for "{args.object_type}" not found')
        else:
            try:
                schema_object_list = self._objects[args.object_type]
                schema_object = next(obj for obj in schema_object_list if obj.object_version == args.schema_version)
            except StopIteration:
                parser.error(f'schema for "{args.object_type}" version "{args.schema_version}" not found')

        if args.output_mermaid:
            mermaid = self.generate_mermaid(schema_object, args.associations)
            print(mermaid)

        if args.output_plantuml:
            if args.output_mermaid:
                print("\n\n")
            plantuml = self.generate_plantuml(schema_object, args.associations)
            print(plantuml)

        if args.output_doc:
            if args.output_plantuml or args.output_mermaid:
                print("\n\n")
            documentation = self.generate_doc(schema_object)
            print(documentation)


if __name__ == "__main__":
    import sys

    try:
        SchemaVisualizer().main_cli()
    except Exception as err:
        print(f"Error: {err.args[0]}")
        sys.exit(1)
