import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/base-category-attribute-1.0.0.md';

# base-category-attribute

<SchemaUri uri="schema/components/base-category-attribute/1.0.0/base-category-attribute.schema.json" />

The `base-category-attribute` component extends [base-attribute](base-attribute.md) with an optional
`attribute_description` property (via [category-attribute-description](category-attribute-description.md))
that provides metadata such as discipline and type.

This is the base for categorical attribute types including [category-attribute](category-attribute.md)
and [bool-attribute](bool-attribute.md).

## Properties

<FlatProperties />
