---
applyTo: "docs/**/*.md,docs/**/*.mdx"
---
# Documentation style guide

## Directory structure

Documentation is organised into three parallel subdirectories under `docs/schemas/`:

```
docs/schemas/
├── index.md              # Schemas landing page (tier overview)
├── objects/              # Object schema docs
│   ├── _category_.json   # {"label": "Objects", "position": 1}
│   ├── index.md          # Object index (domain-grouped)
│   ├── _img/             # Object-specific images
│   └── *.md              # Individual object doc pages
├── components/           # Component schema docs
│   ├── _category_.json   # {"label": "Components", "position": 2}
│   ├── index.md          # Component index (domain-grouped)
│   └── *.md              # Individual component doc pages
├── elements/             # Element schema docs
│   ├── _category_.json   # {"label": "Elements", "position": 3}
│   ├── index.md          # Element index (domain-grouped)
│   └── *.md              # Individual element doc pages
└── generated/            # Auto-generated content (do not edit)
    ├── flatmd/           # Flat property tables
    └── uml/              # Mermaid class diagrams
```

### Casing conventions

- **Proper nouns** (e.g., "Geoscience Objects", "Evo") retain title case everywhere.
- **Sidebar labels and headings** use sentence case (e.g., "Evo schemas", "Understanding schemas") unless they are proper nouns.

### Path conventions by tier

| From | To | Path pattern |
|---|---|---|
| Object page | Generated flatmd | `../generated/flatmd/objects/<name>-<version>.md` |
| Object page | Generated UML | `../generated/uml/<name>-<version>.mmd` |
| Object page | Component page | `../components/<name>.md` |
| Object page | Understanding guide | `../../understanding-schemas/<name>.md` |
| Object page | Sibling object | `<name>.md` (same directory) |
| Component page | Generated flatmd | `../generated/flatmd/components/<name>-<version>.md` |
| Component page | Object page | `../objects/<name>.md` |
| Component page | Sibling component | `<name>.md` (same directory) |
| Element page | Generated flatmd | `../generated/flatmd/elements/<name>-<version>.md` |
| Element page | Sibling element | `<name>.md` (same directory) |

## Object documentation template

```mdx
import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/<name>-<version>.md';

<OverlineWithVersion title="Geoscience Objects" version="<version>" badge="<supported|techPreview>" />

# <name>

<SchemaUri uri="schema/objects/<name>/<version>/<name>.schema.json" />

<!-- Description: what this object represents, key properties, usage context -->

## Properties

<FlatProperties />

::mermaid[../generated/uml/<name>-<version>.mmd]
```

Key rules:
- **`OverlineWithVersion`** is required for objects — they have lifecycle states (`supported`, `techPreview`).
- Use `docs/schemas/objects/pointset.md` as the canonical template.
- For multi-version objects, use `<name>-<version>.md` naming (e.g., `gravity-1.2.0.md`, `gravity-2.0.0.md`). Single-version schemas use `<name>.md`.
- Some pages use `import Alert from '@mui/material/Alert'` for callout boxes.

### Object cross-reference sections

Place immediately after `<SchemaUri>`, before intro text or `## Properties`:

1. **`**Key components:**`** — Bullet list with em-dash–separated role descriptions. Only include components specific to the object or a small group — skip ubiquitous ones like `locations`, `scalar-attribute`, or generic attribute types.
2. **`**See also:**`** — Peer cross-references to related objects (variants, counterparts). Bold-inline format.

```markdown
**Key components:**
- [survey-collection](../components/survey-collection.md) — Logical grouping of survey measurements
- [survey-attribute-definition](../components/survey-attribute-definition.md) — Common properties for survey measurement attributes

**See also:** [tensor-3d-grid](tensor-3d-grid.md) (3D counterpart), [regular-2d-grid](regular-2d-grid.md) (equal cell sizes).
```

For objects without specialised components (e.g., `pointset`), omit "Key components" entirely.

## Component documentation template

```mdx
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/<name>-<version>.md';

# <name>

<SchemaUri uri="schema/components/<name>/<version>/<name>.schema.json" />

<!-- Description: what this component is, what it does, key properties -->

**Used by:** [object-a](../objects/object-a.md), [object-b](../objects/object-b.md).

**See also:** [sibling](sibling.md) (relationship description).

## Properties

<FlatProperties />
```

- No `OverlineWithVersion` or badge — components don't have lifecycle states.
- Title uses the component's kebab-case name as-is.

## Element documentation template

```mdx
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/elements/<name>-<version>.md';

# <name>

<SchemaUri uri="schema/elements/<name>/<version>/<name>.schema.json" />

<!-- Description: what this element represents, data format, encoding details -->

**See also:** [sibling](sibling.md) (relationship description).

## Properties

<FlatProperties />
```

- No `OverlineWithVersion` or badge — elements are stable primitives.
- **"Used by" is rarely useful** — most elements are consumed by many components. Only include for specialised elements with ≤5 consumers.
- **Encoding details matter** — note binary encoding format (e.g., float64, uint64) and `binary_data_shape` semantics.
- For array families with a base type and width specialisations (e.g., `float-array-md` → `float-array-1/2/3/6`), the base page explains general structure; specialisation pages note their fixed width and typical use case.

### Missing FlatProperties workaround

The documentation generator does not always produce flatmd files for schemas that use pure `allOf` composition with no additional properties. When a generated flatmd file does not exist:

1. Remove the `FlatProperties` import line entirely.
2. Replace the `<FlatProperties />` tag with a prose note.

```mdx
## Properties

Properties are inherited from [integer-array-md](integer-array-md.md) with `width` constrained to 2.
```

## Cross-referencing conventions

### "See also" — peer-level cross-references

Link schemas that share a common relationship:

| Relationship type | Wording pattern |
|---|---|
| Sibling (shared base) | `(categorical counterpart)` / `(continuous counterpart)` |
| 2D/3D variant | `(3D counterpart)` / `(2D counterpart)` |
| Single ↔ collection | `(spatially varying collection)` / `(single definition)` |
| Absolute ↔ relative | `(drillhole-relative variant)` / `(absolute variant)` |
| Cell type family | `(other cell types)` |
| Width family | `(width W specialisation)` / `(base type)` / `(other widths)` |
| Single ↔ array | `(array form)` / `(single value)` |

Format: `**See also:** [component-a](component-a.md) (relationship), [component-b](component-b.md).`

### "Used by" — consumer cross-references

Link a schema to its direct consumers one tier up (elements → components, components → objects).

Format: `**Used by:** [object-a](../objects/object-a.md), [object-b](../objects/object-b.md).`

Rules:
- Only list **direct** references — not indirect consumers through other components.
- **Skip ubiquitous schemas** where listing adds noise: `base-spatial-data-properties`, `base-object-properties`, `attribute-list-property`, `one-of-attribute`, `locations`, `rotation`.
- For elements, the ubiquity threshold is higher — only include "Used by" for elements with ≤5 direct consumers.
- If a consuming schema does not yet have a documentation page, omit it from the list.
- Link to the latest documented version for multi-version objects.

### Cross-reference ordering

When a schema has multiple cross-reference types:

```markdown
**Key components:**
- [comp-a](../components/comp-a.md) — Brief role description

**Used by:** [object-a](../objects/object-a.md), [object-b](../objects/object-b.md).

**See also:** [peer-a](peer-a.md) (relationship), [peer-b](peer-b.md).

## Properties
```

Order: **Key components** (objects only) → **Used by** (components/elements only) → **See also** → `## Properties`.

### Bidirectional consistency

Every "Key components" entry on an object page must have a corresponding "Used by" on the target component page, and vice versa. Quick verification: `grep -r "schema-name" docs/schemas/`.

## Deprecation notices

When a component or element is deprecated:

1. Import `Alert from '@mui/material/Alert'`.
2. Place the alert immediately after `<SchemaUri>`, before the description.
3. Use `severity="warning"`.
4. Keep the message factual and actionable. Do not reference unreleased services or internal infrastructure.
5. Annotate the entry in `index.md` with `(deprecated)`.

```mdx
import Alert from '@mui/material/Alert';

<Alert severity="warning">
The lineage component is deprecated and will be removed in a future schema version. New integrations should not rely on this component.
</Alert>
```

## Index page organisation

All three index pages organise schemas by **functional domain**, not alphabetically. This aids discoverability — users looking for drilling-related schemas find all drilling components together.

### Shared index conventions

- **Functional grouping over alphabetical** — organise by concept, not by name.
- **Section summaries** — every section gets a 1–2 sentence introduction before its bullet list, written for geoscientists, not schema engineers.
- **Entry format** — `* [Display name](file.md) — brief description`. Annotations like `(deprecated)` are appended.
- **Ordering within sections** — general/abstract before specific/concrete.
- **Cross-listing** — when a schema serves two audiences, list it in both sections.
- **Tier links** — each index page links to adjacent tiers in its introductory paragraph.

### Multi-version objects in indexes

Use sub-bullets for version links:

```markdown
* Gravity — potential-field gravity survey data
  * [1.2.0](gravity-1.2.0.md)
  * [2.0.0](gravity-2.0.0.md)
```

## Technical accuracy conventions

### Specificity in standards references

Prefer specific standard names: ✅ "A [WKT2](https://www.ogc.org/standards/wkt-crs) string representation" over ❌ "A Well-Known Text (WKT) string representation".

### Array shape precision

Array width and spatial dimensionality are distinct:

- **Array shape**: N×W notation (e.g., "N×3 array"). Do not use "3D array" for width 3.
- **Spatial dimensions**: "2D" and "3D" for physical space (e.g., "3D coordinates").
- In index pages and "See also" labels, use `(width W)` notation: ✅ `(width 1)` not ❌ `(1D)`.

### Schema terminology

- Use `allOf` for inheritance/composition.
- Use `oneOf` for discriminated unions.
- Reference `attribute_type` as the discriminator field name.

## Documentation expansion principles

- **Additive, not rewriting**: Preserve existing human-authored content. Expansions add context.
- **When-to-use guidance**: For families of related schemas, each member should explain when it is the appropriate choice relative to siblings.
- **Inline jargon definitions**: Technical terms unfamiliar to non-specialists (e.g., "quadrature", "chargeability", "sill") should get brief parenthetical definitions on first use.
- **Version change notes**: For schemas with multiple documented major versions, the newer version should include a brief note on what changed.

## What NOT to document

- **Generated files** (`docs/schemas/generated/`): Never edit manually.
- **Internal infrastructure**: No private repos, internal tooling, CI/CD, or unreleased services.
- **Transitive relationships**: "Used by" lists only direct consumers.
- **Ubiquitous schemas in "Used by"**: Don't list every consumer of foundational components.

## Cross-reference maintenance checklist

| Action | Updates required |
|---|---|
| **New object** | Add "Key components" for specialised components. Update each listed component's "Used by". Add "See also" to domain peers. |
| **New component** | Add "Used by" listing consumers. If consumer has "Key components", add entry there. Add "See also" to siblings. |
| **New element** | Add "Used by" if ≤5 direct consumers. |
| **Rename/remove** | Search `docs/schemas/` for all references and update or remove. |
| **Version bump** | Update doc page imports and cross-reference links with version-specific paths. |
| **Refactor composition** | Update both object's "Key components" and component's "Used by" if composition changes. |
