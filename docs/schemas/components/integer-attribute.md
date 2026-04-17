import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/integer-attribute-1.1.0.md';

# integer-attribute

<SchemaUri uri="schema/components/integer-attribute/1.1.0/integer-attribute.schema.json" />

An integer attribute stores a range of integer values. It uses `attribute_type = "integer"`.

* `values` — An array of integer values, one per geometric element.
* `nan_description` — A [nan-continuous](nan-continuous.md) component defining how NaN values are interpreted.
* Inherits from [base-continuous-attribute](base-continuous-attribute.md).

**Used by:** [one-of-attribute](one-of-attribute.md).

## Properties

<FlatProperties />
