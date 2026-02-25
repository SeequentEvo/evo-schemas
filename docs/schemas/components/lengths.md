import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/lengths-1.0.1.md';

# lengths

<SchemaUri uri="schema/components/lengths/1.0.1/lengths.schema.json" />

The `lengths` component stores an array of scalar length values representing layer thicknesses. In a
1D layered-earth model, each value gives the thickness of a single layer; cumulating these thicknesses
from the surface yields depth to each layer boundary. Each entry is stored as a
[float-array-1](../elements/float-array-1.md) element.

**Used by:** [geophysical-records-1d](../objects/geophysical-records-1d.md) (as layer thicknesses in the `depths` property).

**See also:** [intervals](intervals.md), [from-to](from-to.md).

## Properties

<FlatProperties />
