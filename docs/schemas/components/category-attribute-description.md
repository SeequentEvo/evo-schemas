import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/category-attribute-description-1.0.1.md';

# category-attribute-description

<SchemaUri uri="schema/components/category-attribute-description/1.0.1/category-attribute-description.schema.json" />

The `category-attribute-description` component provides general metadata for a categorical attribute:

* `discipline` — The scientific discipline.
* `type` — The type of categorisation.
* `extensions` — An optional map for application-specific metadata.
* `tags` — An optional list of tags.

This is the categorical counterpart to [attribute-description](attribute-description.md), without `unit`
and `scale` fields (which are not meaningful for categories).

## Properties

<FlatProperties />
