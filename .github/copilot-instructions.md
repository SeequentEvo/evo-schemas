# Copilot Instructions for evo-schemas

## Important: Open Source information boundary

This repository is **Open Source** under the Apache 2.0 licence. All content — including these instructions, schemas, documentation, issues, and pull requests — is publicly visible.

When working in this repository:

- **DO** reference anything that is already public: this repo, its issues and PRs, other public repositories in the `SeequentEvo` org, and the public [Seequent Developer Portal](https://developer.seequent.com/).
- **DO NOT** reference, link to, or externalise information from any private repository, internal tooling, or non-public infrastructure — even if you have access to such resources. This includes repository paths, CI/CD pipelines, internal documentation, and any other content not intended for public consumption.

## Project overview

This repository defines Seequent's geoscience object schemas using JSON Schema Draft 2020-12. It also generates Python dataclasses from those schemas and publishes the `evo-schemas` package to PyPI. The schemas describe metadata and data serialisation for geoscience objects used in Seequent's Evo platform.

## Python virtual environment

This project requires a Python virtual environment. Always activate the virtualenv before running any Python commands:

```bash
python3 -m venv .venv          # Create (if needed)
source .venv/bin/activate       # Activate
pip install .[test]             # Install dev dependencies
```

If you encounter `command not found` errors for `pytest`, `pre-commit`, or other tools, the virtualenv is not activated.

## Build, test, and lint

```bash
pytest                                  # Run all tests
pytest tests/test_schemas_custom.py     # Single test file
pytest -k "pointset"                    # Filter by name
pre-commit run --all-files              # Lint (ruff + black)
make generate-schema-docs               # Generate doc tables + UML
```

Formatting: Black (line length 120, target py310/py311). Linting: Ruff (rules E, F, I; line length 120). Both run as pre-commit hooks and in CI.

## Architecture

### Schema hierarchy (schema/)

Schemas are organised into three tiers under `schema/`:

- **elements/** — Primitive data types (arrays, colors, units). Lowest level; no composition.
- **components/** — Reusable composed structures (attributes, geometries, CRS). Built from elements and other components.
- **objects/** — Top-level geoscience objects (pointset, triangle-mesh, block-model). Built from components using `allOf` composition. These are the schemas consumers validate against.

Each schema lives at `schema/<tier>/<name>/<semver>/<name>.schema.json`. Multiple versions coexist side by side.

### Key files

- `schema/geoscience-objects.schema.json` — Auto-generated root schema (updated by pre-commit hook; do not edit).
- `tools/clone_schema.py` — Version-bump a schema and cascade updates to dependents.
- `tools/schemas.py` — `generate_json_schema()` scaffolds a new schema file.
- `tools/code_generator/` — Generates Python dataclasses from schemas during build. Do not edit generated Python files.

### Key conventions (enforced by tests)

- Property names: **snake_case**. File/folder names: **kebab-case**.
- Every schema must have a non-empty `description` and specify `$schema` as Draft 2020-12.
- Objects must have a `schema` const matching `$id`, listed in `required`.
- Objects must compose `base-object-properties` or `base-spatial-data-properties` via `allOf`.
- `unevaluatedProperties: false` only on objects (not elements or components).
- Latest schema versions must only reference latest versions of other schemas.
- JSON formatting: 2-space indent, no key sorting, no ASCII escaping (enforced by pre-commit).
- All commits must be signed with verified signatures.

## Documentation

Documentation lives in `docs/` and is rendered on the [Seequent Developer Portal](https://developer.seequent.com/docs/data-structures/geoscience-objects). The docs use [Docusaurus](https://docusaurus.io/) MDX format with custom components. Never edit files in `docs/schemas/generated/` — they are overwritten by `make generate-schema-docs`.

## Path-specific instructions

Domain-specific guidance is provided via path-specific instruction files in `.github/instructions/`. These are automatically loaded by Copilot when working on files that match their `applyTo` patterns:

| Instruction file | Applies to | Content |
|---|---|---|
| `workflow.instructions.md` | All files | Collaborative workflow, question-asking, commits |
| `schema-authoring.instructions.md` | `schema/**/*.json` | Creating and modifying schemas |
| `schema-versioning.instructions.md` | `schema/**/*.json` | Version-bumping with `clone_schema.py` |
| `documentation.instructions.md` | `docs/**/*.md`, `docs/**/*.mdx` | Documentation style guide and templates |
