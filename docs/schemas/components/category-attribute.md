import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/category-attribute-1.1.0.md';

# category-attribute

<SchemaUri uri="schema/components/category-attribute/1.1.0/category-attribute.schema.json" />

A category attribute assigns categorical labels to geometric elements. It uses `attribute_type = "category"`.

Values are stored as integers that index into a lookup table (via [category-data](category-data.md)):

* `table` — A lookup table mapping integer indices to category names.
* `values` — Integer indices into the lookup table, one per geometric element.
* `nan_description` — A [nan-categorical](nan-categorical.md) component defining how NaN values are interpreted.

See [Understanding attributes](../../understanding-schemas/understanding-attributes.md) for more detail.

**Used by:** [channel-attribute](channel-attribute.md), [one-of-attribute](one-of-attribute.md).

## Properties

<FlatProperties />
