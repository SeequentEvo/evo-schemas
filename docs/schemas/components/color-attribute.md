import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/color-attribute-1.1.0.md';

# color-attribute

<SchemaUri uri="schema/components/color-attribute/1.1.0/color-attribute.schema.json" />

A colour attribute stores colour values encoded as ABGR integers. It uses `attribute_type = "color"`.

* `values` — An array of ABGR-encoded integer colour values, one per geometric element.
* Inherits from [base-continuous-attribute](base-continuous-attribute.md).

**Used by:** [one-of-attribute](one-of-attribute.md).

## Properties

<FlatProperties />
