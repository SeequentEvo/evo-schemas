import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/block-model-category-attribute-2.0.0.md';

# block-model-category-attribute

<SchemaUri uri="schema/components/block-model-category-attribute/2.0.0/block-model-category-attribute.schema.json" />

A block model category attribute extends the categorical attribute system for use with block model data.

This component composes [base-category-attribute](base-category-attribute.md) and [category-data](category-data.md)
with block-model-specific value storage. Its `attribute_class` is always `category`, which discriminates it from
[block-model-attribute](block-model-attribute.md) when both share the same `attribute_type`.

**Used by:** block-model.

**See also:** [block-model-attribute](block-model-attribute.md) (continuous counterpart).

## Properties

<FlatProperties />
