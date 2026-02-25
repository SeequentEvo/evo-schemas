import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/continuous-attribute-1.1.0.md';

# continuous-attribute

<SchemaUri uri="schema/components/continuous-attribute/1.1.0/continuous-attribute.schema.json" />

A continuous attribute stores a range of floating-point values. It uses `attribute_type = "scalar"`.

* `values` — A data array of floating-point values, one per geometric element.
* `nan_description` — A [nan-continuous](nan-continuous.md) component defining how NaN values are interpreted.
* Inherits `name`, `key`, and optional `attribute_description` from [base-continuous-attribute](base-continuous-attribute.md).

**Used by:** [channel-attribute](channel-attribute.md), [one-of-attribute](one-of-attribute.md).

## Properties

<FlatProperties />
