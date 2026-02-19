import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/lengths-1.0.1.md';

# lengths

<SchemaUri uri="schema/components/lengths/1.0.1/lengths.schema.json" />

The `lengths` component stores an array of length values, typically representing the lengths of segments,
intervals, or measurement stations along a profile. Each entry is a scalar distance value stored as a
[float-array-1](../elements/float-array-1.md) element.

**Used by:** [geophysical-records-1d](../objects/geophysical-records-1d.md).

**See also:** [intervals](intervals.md), [from-to](from-to.md).

## Properties

<FlatProperties />
