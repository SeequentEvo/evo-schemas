---
applyTo: "schema/**/*.json"
---
# Schema versioning

## When to bump

Follow the versioning policy (detailed in `docs/versioning-and-release-process/schema-versioning-policy.md`):

- **MAJOR** — Breaking changes: new required fields, type changes, renames, restructuring, making optional fields required, breaking enum changes, adding new `allOf` references.
- **MINOR** — Backwards-compatible additions: new optional fields, new enum values, loosened restrictions, new `oneOf` alternatives.
- **PATCH** — Non-data-affecting changes: description improvements, clarifications, component refactoring that doesn't change the flattened schema.

## Using clone_schema.py

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

## After bumping

1. Review the cascaded changes to ensure they are correct.
2. Update the documentation page(s) to reference the new version. If a new major version is added alongside an existing documented version, create a separate doc page using the `<name>-<version>.md` naming convention.
3. Run `make generate-schema-docs` to regenerate property tables and UML diagrams.
4. Run `pytest` and `pre-commit run --all-files` to validate.
5. Update or create example instances for the new version.
