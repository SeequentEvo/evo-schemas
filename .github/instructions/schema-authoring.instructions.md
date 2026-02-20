---
applyTo: "schema/**/*.json"
---
# Schema authoring

## Creating a new schema

### Prerequisites

An accepted RFC (`rfc/accepted` label) is required for new schemas and major version bumps. Minor and patch iterations on existing schemas do not require an RFC, but should reference the original RFC if one exists. Read the RFC discussion for design decisions and reviewer expectations. The RFC workflow is:

1. **Open an RFC issue** using the [RFC issue template](https://github.com/SeequentEvo/evo-schemas/issues/new?template=rfc.yaml). The template requires: Summary, Motivation, Basic example, Detailed design, Drawbacks, Alternatives, and Adoption strategy.
2. **Discussion** — Maintainers and community discuss the proposal.
3. **Acceptance** — Label changes from `rfc/open` to `rfc/accepted`.
4. **Implementation** — Work proceeds via a pull request.

### Create the schema file

Use the scaffolding tool:

```python
from tools.schemas import generate_json_schema
generate_json_schema()
```

Or copy a simple existing schema (e.g., `schema/objects/pointset/1.3.0/pointset.schema.json`) and modify it. The file must live at `schema/<tier>/<name>/<semver>/<name>.schema.json`.

### Structural requirements (enforced by tests)

- **Draft**: Set `$schema` to `https://json-schema.org/draft/2020-12/schema`.
- **`$id`**: Must match the file's path relative to `schema/` (e.g., `objects/pointset/1.3.0/pointset.schema.json`).
- **`description`**: Must be non-empty and meaningful.
- **Property names**: Must be `snake_case`.
- **File/folder names**: Must be `kebab-case`.
- **Base composition**: Objects must compose `base-object-properties` or `base-spatial-data-properties` via `allOf`.
- **`schema` const**: Objects must have a `schema` property whose value is `const` matching the `$id`, and it must appear in `required`.
- **`unevaluatedProperties: false`**: Only on objects, never on elements or components (it blocks further composition).
- **Version consistency**: The latest version of a schema must only reference the latest versions of other schemas. An object must not mix multiple versions of the same subschema.

## Schema composition conventions

- **`allOf`** is used for inheritance. Objects compose `base-object-properties` or `base-spatial-data-properties` via `allOf` to inherit common fields (uuid, name, etc.) without nesting.
- **`oneOf`** is used for discriminated unions. Subschemas use a constant `attribute_type` field as the discriminator.
- **`unevaluatedProperties: false`** must only appear on objects (not elements or components), as it blocks further composition.

## Decompose into components

Before creating new components, check whether existing components already provide the functionality you need — reuse is strongly preferred over duplication. Browse `schema/components/` and the component documentation in `docs/schemas/components/` to find candidates.

If your schema includes structures that are not already covered and could be reused by other schemas, break them out into new components under `schema/components/`. Follow existing decomposition patterns — for example, the `drilling-campaign` schema introduced `hole-collars`, `hole-chunks`, and `desurvey-method` as separate components.

## Provide examples

Create example JSON instances in `examples/<schema-version>/<tier>/<name>.json`. The version folder corresponds to the individual schema version the example validates against (e.g., an example for `pointset` v1.3.0 lives in `examples/1.3.0/objects/`). Multiple examples for the same schema can coexist using suffixed names (e.g., `block-model-1.json`, `block-model-2.json`).

Tests in `test_json_examples.py` validate all examples against their schemas. When creating or modifying a schema, provide or update matching examples.

## Write documentation

Create a doc page following the documentation style guide (automatically loaded when editing `docs/` files). Key steps:

- Create the doc page at `docs/schemas/objects/<name>.md` (or `components/` or `elements/`).
- Add the schema to the listing in `docs/schemas/index.md`.
- Run `make generate-schema-docs` to produce flat property tables and UML diagrams.
- Maintain cross-references bidirectionally.

## Validate

```bash
pytest                          # Full test suite
pre-commit run --all-files      # Linting, formatting, root schema update
```

Common issues: `$id` not matching file path, missing `description`, property names not in `snake_case`, referencing non-latest versions of subschemas.

## Open a pull request

Open a PR from your fork to `SeequentEvo/evo-schemas:main`. In the PR description:

- Reference the RFC issue (e.g., "Implements RFC #21").
- Describe the schema and any new components introduced.
- Complete the checklist from the PR template.

A typical schema PR includes: schema JSON file(s), new components/elements (if any), example instances, a documentation page, updated `docs/schemas/index.md`, regenerated `docs/schemas/generated/` content, and an updated root schema.

## Schema development lifecycle

The lifecycle states: **Problem → Solution → Tech Preview → Supported → (Deprecated)**.

- **Tech Preview**: Merged, published, usable, but not yet covered by SLAs or deprecation guarantees.
- **Supported**: Full SLAs and deprecation policy apply.
- **Deprecated**: No longer recommended for new integrations.

The [Seequent Developer Portal](https://developer.seequent.com/docs/data-structures/geoscience-objects) is the authoritative source for a schema's current lifecycle state.

## Contribution model

This repository follows a **fork-based contribution model**:

1. Fork `SeequentEvo/evo-schemas` to your personal GitHub account.
2. Create a feature branch on your fork.
3. Open a pull request from your fork to `SeequentEvo/evo-schemas:main`.
4. PRs should follow the PR template and reference the relevant RFC issue if applicable.
