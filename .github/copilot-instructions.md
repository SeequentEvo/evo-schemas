# Copilot Instructions for evo-schemas

## Important: Open Source information boundary

This repository (`SeequentEvo/evo-schemas`) is **Open Source** under the Apache 2.0 licence. All content in this repo — including these instructions, schemas, documentation, issues, and pull requests — is publicly visible.

Repositories under the `seequent` GitHub organisation (as distinct from `SeequentEvo`) are **not** open source. When working in this repository:

- **DO** reference anything in the `SeequentEvo` org, this repo's issues/PRs, and the public [Seequent Developer Portal](https://developer.seequent.com/).
- **DO NOT** reference internal repository paths, internal tooling, CI/CD pipelines, or any resources from the `seequent` GitHub org. Even if you have access to private repositories, do not introduce references to them in code, documentation, or commit messages within this repo.

Documentation authored in this repository's `docs/` directory is rendered on the Seequent Developer Portal. The sync mechanism is outside this repo's scope — your responsibility is to get the docs right in `docs/`; rendering happens downstream.

## Project overview

This repository defines Seequent's geoscience object schemas using JSON Schema Draft 2020-12. It also generates Python dataclasses from those schemas and publishes the `evo-schemas` package to PyPI. The schemas describe metadata and data serialisation for geoscience objects used in Seequent's Evo platform.

## Python virtual environment

This project requires a Python virtual environment for development and running the test suite. Always activate the virtualenv before running any Python commands (tests, linting, tools, doc generation):

```bash
# Create a virtualenv (if one doesn't already exist)
python3 -m venv .venv

# Activate it (required before any dev work)
source .venv/bin/activate

# Install the package with test dependencies
pip install .[test]
```

The `.venv/` directory is the conventional location. If you encounter `command not found` errors for `pytest`, `pre-commit`, or other tools, it almost certainly means the virtualenv is not activated.

## Build, test, and lint

```bash
# Install dev dependencies (virtualenv must be active)
pip install .[test]

# Run all tests
pytest

# Run a single test file
pytest tests/test_schemas_custom.py

# Run a single test by name
pytest tests/test_schemas_custom.py::test_property_names_are_snake_case

# Run a single parametrized test for a specific schema
pytest tests/test_schemas_custom.py::test_check_schema_draft -k "pointset"

# Lint (via pre-commit hooks — ruff + black)
pre-commit run --all-files

# Generate schema documentation (Markdown + UML)
make generate-schema-docs
```

Formatting: Black (line length 120, target py310/py311). Linting: Ruff (rules E, F, I; line length 120). Both run as pre-commit hooks and in CI.

## Architecture

### Schema hierarchy (schema/)

Schemas are organised into three tiers under `schema/`:

- **elements/** — Primitive data types (arrays, colors, units). Lowest level; no composition.
- **components/** — Reusable composed structures (attributes, geometries, CRS). Built from elements and other components.
- **objects/** — Top-level geoscience objects (pointset, triangle-mesh, block-model). Built from components using `allOf` composition. These are the schemas consumers validate against.

Each schema lives at `schema/<tier>/<name>/<semver>/<name>.schema.json`. Multiple versions of a schema coexist side by side.

### Schema composition conventions

- **`allOf`** is used for inheritance. Objects compose `base-object-properties` or `base-spatial-data-properties` via `allOf` to inherit common fields (uuid, name, etc.) without nesting.
- **`oneOf`** is used for discriminated unions. Subschemas use a constant `attribute_type` field as the discriminator.
- **`unevaluatedProperties: false`** must only appear on objects (not elements or components), as it blocks further composition.

### Root schema

`schema/geoscience-objects.schema.json` is an auto-generated root schema aggregating all objects. It is updated by a pre-commit hook (`tools/update_root_schema.py`) — do not edit manually.

### Python package (docs/python/evo_schemas/)

Python dataclasses are auto-generated from schemas during the build via a custom setuptools build backend (`tools/build_meta.py`). The code generator lives in `tools/code_generator/`. Do not edit generated Python files directly.

### Tooling (tools/)

- `clone_schema.py` — Version-bump a schema and cascade updates to all dependents. Run with `python tools/clone_schema.py <schema-$id>`.
- `schemas.py` — `generate_json_schema()` creates a new schema file with the correct path and boilerplate.
- `example_instances.py` — Validates example JSON instances in `examples/` against their schemas.
- `schema_walker.py` — Recursive schema visitor used by tests and tools.

## Key conventions

### Schema standards (enforced by tests)

- All property names must be **snake_case**.
- Schema file names must be **kebab-case** (`<name>.schema.json`).
- The folder name must match the schema file name (minus `.schema.json`).
- Every schema must have a non-empty `description` and specify `$schema` as Draft 2020-12.
- Every object must have a `schema` property that is `const` matching the schema's `$id`, and it must be listed in `required`.
- Objects must reference either `base-object-properties` or `base-spatial-data-properties` via `allOf`.
- The latest version of a schema must only reference the latest versions of other schemas.
- An object must not reference multiple versions of the same subschema.

### Versioning schemas

Use `tools/clone_schema.py` to create a new version of a schema. It handles copying the schema, bumping the version directory, updating `$id` and `schema` const, cascading reference updates to dependent schemas, and copying matching example files.

### Examples (examples/)

Example JSON instances live in `examples/<schema-version>/<tier>/<name>.json`. The version folder corresponds to the individual schema version that the example validates against (e.g., an example for `pointset` v1.3.0 lives in `examples/1.3.0/objects/`). When `tools/clone_schema.py` bumps a schema version, it automatically copies examples from the old version folder to the new one, updating the `schema` reference inside each file. Multiple examples for the same schema can coexist using suffixed names (e.g., `block-model-1.json`, `block-model-2.json`).

Tests in `test_json_examples.py` validate all examples against their schemas. When creating or modifying a schema, provide or update matching examples.

### Commits

All commits must be signed with verified signatures. A pre-commit hook (`tools/audit-commits.sh`) audits commit metadata.

### JSON formatting

Pre-commit hooks enforce: 2-space indent, no key sorting, no ASCII escaping. The `pretty-format-json` hook auto-fixes on commit.

## Documentation system

### Overview

Documentation lives in `docs/` and is rendered on the [Seequent Developer Portal](https://developer.seequent.com/docs/data-structures/geoscience-objects). The docs use [Docusaurus](https://docusaurus.io/) MDX format with custom components. The doc tree is structured as follows:

- `docs/index.md` — Landing page for the Geoscience Objects section.
- `docs/schemas/` — Per-object schema documentation pages plus `index.md` (the object listing).
- `docs/schemas/components/` — Documentation for selected reusable components.
- `docs/schemas/generated/` — **Auto-generated content; do not edit.** Contains `flatmd/` (flat property tables) and `uml/` (Mermaid class diagrams).
- `docs/understanding-schemas/` — Conceptual guides (attributes, parts, blob storage, cell-type geometry).
- `docs/versioning-and-release-process/` — Schema versioning policy and development lifecycle.

The `_category_.json` files in doc directories control Docusaurus sidebar labels and ordering.

### Schema documentation pages

Each schema object has a corresponding doc page in `docs/schemas/`. Use `docs/schemas/pointset.md` as the canonical template when writing a new page. The standard structure is:

```mdx
import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './generated/flatmd/objects/<name>-<version>.md';

<OverlineWithVersion title="Geoscience Objects" version="<version>" badge="<supported|techPreview>" />

# <schema-name>

<SchemaUri uri="schema/objects/<name>/<version>/<name>.schema.json" />

<!-- Description and usage guidance -->

## Properties

<FlatProperties />

::mermaid[generated/uml/<name>-<version>.mmd]
```

Key rules for doc pages:

- Import and use the Docusaurus components exactly as shown — `OverlineWithVersion`, `SchemaUri`, and `FlatProperties`.
- The `badge` attribute reflects the schema's lifecycle state. Currently implemented values are `"supported"` and `"techPreview"`, but additional states from the lifecycle (e.g., `"deprecated"`) may be implemented in future.
- When a schema has multiple major versions documented, use `<name>-<version>.md` naming (e.g., `gravity-1.2.0.md` and `gravity-2.0.0.md`). For single-version schemas, use `<name>.md`.
- Add the schema to `docs/schemas/index.md` (the object listing page).
- Some pages use `import Alert from '@mui/material/Alert'` for callout boxes — this is standard Docusaurus MDX.

### Generating documentation

Auto-generated files (property tables and UML diagrams) are produced by:

```bash
make generate-schema-docs
# or equivalently:
python -m tools.documentation --autodoc
```

Run this after creating or modifying schemas. **Never edit files in `docs/schemas/generated/`** — they will be overwritten.

## RFC and schema development process

### The RFC workflow

New schemas (and significant changes to existing schemas) begin with an RFC (Request for Comment). The process is:

1. **Open an RFC issue** using the [RFC issue template](https://github.com/SeequentEvo/evo-schemas/issues/new?template=rfc.yaml). The template requires: Summary, Motivation, Basic example, Detailed design, Drawbacks, Alternatives, and Adoption strategy. The issue is automatically labelled `rfc` and `rfc/open`.
2. **Discussion** — Maintainers and community discuss the proposal on the issue thread. This often includes design refinements, component decomposition advice, and edge-case analysis.
3. **Acceptance** — When the RFC is accepted, its label changes from `rfc/open` to `rfc/accepted` and an assignee is designated.
4. **Implementation** — Work proceeds via a pull request (see "How to create a new schema" below).

Active and historical RFCs can be found by searching [issues labelled `rfc`](https://github.com/SeequentEvo/evo-schemas/labels/rfc).

### Schema development lifecycle

The lifecycle states for a schema are: **Problem → Solution → Tech Preview → Supported → (Deprecated)**.

- **Tech Preview**: The schema is merged, published, and usable, but not yet covered by SLAs or deprecation guarantees. Doc pages use `badge="techPreview"`.
- **Supported**: Full SLAs and deprecation policy apply. Doc pages use `badge="supported"`.
- **Deprecated**: The schema is no longer recommended for new integrations.

Each lifecycle state may correspond to a `badge` value in the documentation. Currently only `"supported"` and `"techPreview"` badges are implemented; other states may gain badge support as the tooling evolves.

The [Seequent Developer Portal](https://developer.seequent.com/docs/data-structures/geoscience-objects) is the authoritative source for a schema's current lifecycle state.

### Contribution model

This repository follows a **fork-based contribution model**:

1. Fork `SeequentEvo/evo-schemas` to your personal GitHub account.
2. Create a feature branch on your fork.
3. Open a pull request from your fork to `SeequentEvo/evo-schemas:main`.
4. PRs should follow the [PR template](.github/pull_request_template.md) and reference the relevant RFC issue if applicable.

Schema PRs typically receive thorough review covering schema structure, naming conventions, composition patterns, and description quality.

## How to create a new schema

This section describes the end-to-end process for implementing a new geoscience object schema, from accepted RFC to merged PR.

### 1. Prerequisites

Ensure an RFC has been accepted (`rfc/accepted` label) or that this is an iteration on an existing schema. Read the RFC discussion for design decisions and reviewer expectations.

### 2. Create the schema file

Use the scaffolding tool to create the schema at the correct path:

```python
from tools.schemas import generate_json_schema
generate_json_schema()
```

Alternatively, copy a simple existing schema (e.g., `schema/objects/pointset/1.3.0/pointset.schema.json`) and modify it. The file must live at `schema/<tier>/<name>/<semver>/<name>.schema.json`.

### 3. Structural requirements

All of the following are enforced by the test suite (`pytest`):

- **Draft**: Set `$schema` to `https://json-schema.org/draft/2020-12/schema`.
- **`$id`**: Must match the file's path relative to `schema/` (e.g., `objects/pointset/1.3.0/pointset.schema.json`).
- **`description`**: Must be non-empty and meaningful.
- **Property names**: Must be `snake_case`.
- **File/folder names**: Must be `kebab-case`.
- **Base composition**: Objects must compose `base-object-properties` or `base-spatial-data-properties` via `allOf`.
- **`schema` const**: Objects must have a `schema` property whose value is `const` matching the `$id`, and it must appear in `required`.
- **`unevaluatedProperties: false`**: Only on objects, never on elements or components (it blocks further composition).
- **Version consistency**: The latest version of a schema must only reference the latest versions of other schemas. An object must not mix multiple versions of the same subschema.

### 4. Decompose into components

If your schema includes structures that could be reused by other schemas, break them out into components under `schema/components/`. Follow the existing decomposition patterns — for example, the `drilling-campaign` schema introduced `hole-collars`, `hole-chunks`, and `desurvey-method` as separate components.

### 5. Provide examples

Create example JSON instances in `examples/<schema-version>/<tier>/<name>.json`. Tests in `test_json_examples.py` validate all examples against their schemas. Ensure examples cover representative use cases.

### 6. Write documentation

Create a doc page at `docs/schemas/<name>.md` following the template described in the "Schema documentation pages" section above. Then:

- Add the schema to the listing in `docs/schemas/index.md`.
- Run `make generate-schema-docs` to produce the flat property tables and UML diagrams.

### 7. Validate

```bash
# Run the full test suite
pytest

# Run all pre-commit hooks (linting, formatting, root schema update)
pre-commit run --all-files
```

Fix any failures before opening a PR. Common issues include: `$id` not matching the file path, missing `description` fields, property names not in `snake_case`, or referencing non-latest versions of subschemas.

### 8. Open a pull request

Open a PR from your fork to `SeequentEvo/evo-schemas:main`. In the PR description:

- Reference the RFC issue (e.g., "Implements RFC #21").
- Describe the schema and any new components introduced.
- Complete the checklist from the PR template.

A typical schema PR includes: schema JSON file(s), new components/elements (if any), example instances, a documentation page, updated `docs/schemas/index.md`, regenerated `docs/schemas/generated/` content, and an updated root schema.

## How to version-bump an existing schema

### When to bump

Follow the versioning policy (detailed in `docs/versioning-and-release-process/schema-versioning-policy.md`):

- **MAJOR** — Breaking changes: new required fields, type changes, renames, restructuring, making optional fields required, breaking enum changes, adding new `allOf` references.
- **MINOR** — Backwards-compatible additions: new optional fields, new enum values, loosened restrictions, new `oneOf` alternatives.
- **PATCH** — Non-data-affecting changes: description improvements, clarifications, component refactoring that doesn't change the flattened schema.

### Using clone_schema.py

The `tools/clone_schema.py` script automates version bumping with cascading updates:

```bash
python tools/clone_schema.py <schema-$id>
# Example:
python tools/clone_schema.py objects/pointset/1.3.0/pointset.schema.json
```

The script will:

1. Prompt for the new version (MAJOR, MINOR, or PATCH bump).
2. Copy the schema to the new version directory, updating `$id` and `schema` const.
3. Identify all schemas that reference the bumped schema and interactively prompt to bump, modify, or skip each dependent.
4. Copy matching example files to the new version directory.

Use this tool rather than attempting manual version management — it handles the cascading updates that are easy to get wrong by hand.

### After bumping

1. Review the cascaded changes to ensure they are correct.
2. Update the documentation page(s) to reference the new version. If a new major version is added alongside an existing documented version, create a separate doc page using the `<name>-<version>.md` naming convention.
3. Run `make generate-schema-docs` to regenerate property tables and UML diagrams.
4. Run `pytest` and `pre-commit run --all-files` to validate.
5. Update or create example instances for the new version.
