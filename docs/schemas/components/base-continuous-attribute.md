import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/base-continuous-attribute-1.0.0.md';

# base-continuous-attribute

<SchemaUri uri="schema/components/base-continuous-attribute/1.0.0/base-continuous-attribute.schema.json" />

The `base-continuous-attribute` component extends [base-attribute](base-attribute.md) with an optional
`attribute_description` property (via [attribute-description](attribute-description.md)) that provides
metadata such as discipline, unit, and scale.

This is the base for continuous-valued attribute types including [continuous-attribute](continuous-attribute.md),
[color-attribute](color-attribute.md), [string-attribute](string-attribute.md),
[integer-attribute](integer-attribute.md), [date-time-attribute](date-time-attribute.md),
[vector-attribute](vector-attribute.md), and [indices-attribute](indices-attribute.md).

## Properties

<FlatProperties />
