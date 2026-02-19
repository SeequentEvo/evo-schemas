import Alert from '@mui/material/Alert';

# Documentation Conventions

This page describes how the schema documentation in this repository is structured and how to contribute new or updated documentation pages. If you are adding a new schema, updating an existing one, or improving documentation quality, this guide will help you follow the established patterns.

<Alert severity="info">
Documentation authored in `docs/` is rendered on the [Seequent Developer Portal](https://developer.seequent.com/docs/data-structures/geoscience-objects). Changes to documentation take effect on the portal once merged to `main`.
</Alert>

## Documentation structure

The documentation is organised to mirror the three-tier schema hierarchy:

```
docs/schemas/
├── index.md              # Schemas landing page
├── objects/              # Object schema documentation
├── components/           # Component schema documentation
├── elements/             # Element schema documentation
└── generated/            # Auto-generated content (do not edit)
```

Each tier has its own directory containing an `index.md` (a domain-grouped listing of all schemas in that tier) and individual documentation pages for each schema. The `generated/` directory contains auto-generated flat property tables and UML diagrams — these are produced by `make generate-schema-docs` and must not be edited manually.

The `_category_.json` files in each directory control Docusaurus sidebar labels and ordering. Objects appear first, then components, then elements — reflecting the top-down hierarchy that most readers will follow.

## Page templates

### Object schemas

Object pages use the full template with lifecycle badging:

```mdx
import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/<name>-<version>.md';

<OverlineWithVersion title="Geoscience Objects" version="<version>" badge="<supported|techPreview>" />

# <name>

<SchemaUri uri="schema/objects/<name>/<version>/<name>.schema.json" />

<!-- Key components (if object uses specialised components) -->
<!-- See also (if related objects exist) -->

<!-- Description -->

## Properties

<FlatProperties />

::mermaid[../generated/uml/<name>-<version>.mmd]
```

The `badge` attribute reflects the schema's lifecycle state as described in the [Schema Development Lifecycle](schema-development-lifecycle.md). Use `"supported"` or `"techPreview"` as appropriate.

For objects with multiple documented major versions (e.g., `gravity`), use version-suffixed filenames: `gravity-1.2.0.md`, `gravity-2.0.0.md`.

### Component schemas

Component pages follow a similar structure but omit `OverlineWithVersion` (components do not have independent lifecycle states):

```mdx
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/<name>-<version>.md';

# <name>

<SchemaUri uri="schema/components/<name>/<version>/<name>.schema.json" />

<!-- Description -->

**See also:** [related-component](related-component.md) (relationship description).

**Used by:** [consuming-object](../objects/consuming-object.md).

## Properties

<FlatProperties />
```

### Element schemas

Element pages are the simplest. Most elements are stable primitives and rarely need lifecycle badging or extensive cross-referencing:

```mdx
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/elements/<name>-<version>.md';

# <name>

<SchemaUri uri="schema/elements/<name>/<version>/<name>.schema.json" />

<!-- Description: data format, encoding, width/shape semantics -->

**See also:** [related-element](related-element.md) (relationship description).

## Properties

<FlatProperties />
```

## Writing descriptions

Descriptions should help a reader understand the schema's purpose and role without needing to read the raw JSON. Focus on:

- **What** the schema represents and when it is used.
- **Key properties** — call out important fields, especially those with non-obvious semantics.
- **Relationships** — how this schema connects to others in the hierarchy.

Keep descriptions concise. The auto-generated property table already documents every field; prose should add context, not duplicate it.

## Cross-referencing

Cross-references help readers navigate between related schemas. There are three types:

### "Key components" — composition references (objects only)

Links from an object to the specialised components it composes, giving readers a forward-navigation path. Only include components specific to the object or a small family — skip ubiquitous components like `locations` or `scalar-attribute`:

```markdown
**Key components:**
- [survey-collection](../components/survey-collection.md) — Logical grouping of survey measurements
- [survey-attribute-definition](../components/survey-attribute-definition.md) — Common properties for survey measurement attributes
```

### "See also" — peer references

Links between schemas at the same tier that share a relationship (siblings, counterparts, dimensional variants):

```markdown
**See also:** [vertices-3d](vertices-3d.md) (3D counterpart).
```

### "Used by" — consumer references

Links from a schema to the schemas that directly reference it, one tier up (component → object, element → component):

```markdown
**Used by:** [drilling-campaign](../objects/drilling-campaign.md), [downhole-collection](../objects/downhole-collection.md).
```

Skip "Used by" for schemas that are referenced so broadly that listing consumers adds noise rather than value (e.g., `base-spatial-data-properties`, `attribute-list-property`, most array elements).

When multiple cross-reference types are present, the ordering is: "Key components" first (objects only), then "See also", then "Used by" (components/elements only), then `## Properties`.

## Index pages

Each tier has an `index.md` that groups schemas by functional domain rather than alphabetically. This aids discoverability — a reader looking for drilling-related schemas can jump straight to the relevant section.

When adding a new schema, add it to the appropriate section of the relevant index page. Each section should have:

- A brief summary sentence between the heading and the first entry.
- Entries in the format: `* [Display name](file.md) — brief description`.
- Ordering from general/abstract to specific/concrete within each section.

For multi-version objects, use sub-bullets for version links:

```markdown
* Gravity — potential-field gravity survey data
  * [1.2.0](gravity-1.2.0.md)
  * [2.0.0](gravity-2.0.0.md)
```

## Deprecation notices

When a schema is deprecated, add an alert immediately after the `<SchemaUri>` line:

```mdx
import Alert from '@mui/material/Alert';

<Alert severity="warning">
This component is deprecated and will be removed in a future schema version. New integrations should not rely on this component.
</Alert>
```

Annotate the entry in the relevant `index.md` with `(deprecated)`. Keep deprecation messages factual — state that the schema is deprecated and advise against new use, but do not reference unreleased replacements or internal services.

## Generating documentation

After creating or modifying schemas, regenerate the flat property tables and UML diagrams:

```bash
make generate-schema-docs
```

This populates `docs/schemas/generated/`. Always run this before opening a PR that includes schema changes. If a generated file is not produced for a particular schema (this can happen for schemas that use pure `allOf` composition with no additional properties), replace the `<FlatProperties />` tag with a prose note directing the reader to the base schema's properties.

## Checklist for new documentation

- [ ] Doc page follows the appropriate tier template (object, component, or element).
- [ ] Description explains purpose and key properties.
- [ ] Cross-references ("See also" and/or "Used by") are present where appropriate.
- [ ] Schema is listed in the correct section of the tier's `index.md`.
- [ ] `make generate-schema-docs` has been run.
- [ ] Page renders correctly in a local build.
