import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/elements/reversible-index-1.0.0.md';

# reversible-index

<SchemaUri uri="schema/elements/reversible-index/1.0.0/reversible-index.schema.json" />

An index reference to a geometry part with an optional reversal flag. The `index` identifies a part within a composite geometry, and the `reversed` boolean (default `false`) indicates whether the part's orientation should be flipped. Used by embedded geometry objects to reference parts that may need normal reversal for consistent winding order.

**Used by:** [embedded-mesh-object](../components/embedded-mesh-object.md), [embedded-polyline-object](../components/embedded-polyline-object.md).

## Properties

<FlatProperties />
