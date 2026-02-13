import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/vector-attribute-1.0.0.md';

# vector-attribute

<SchemaUri uri="schema/components/vector-attribute/1.0.0/vector-attribute.schema.json" />

A vector attribute stores N-dimensional vectors. It uses `attribute_type = "vector"`.

* `values` — A data array of vector values, one per geometric element.
* `nan_description` — A [nan-continuous](nan-continuous.md) component defining how NaN values are interpreted.
* Inherits from [base-continuous-attribute](base-continuous-attribute.md).

## Properties

<FlatProperties />
