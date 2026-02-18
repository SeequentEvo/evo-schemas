import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/elements/float-array-md-1.0.1.md';

# float-array-md

<SchemaUri uri="schema/elements/float-array-md/1.0.1/float-array-md.schema.json" />

Multi-dimensional array of 64-bit floating-point values. The base type for all float array specialisations. Each row stores `width` float64 values, with `length` rows total. Binary data is encoded as float64.

The float array family uses a width specialisation pattern: `float-array-md` defines the general case with a variable `width`, while fixed-width variants (`float-array-1`, `float-array-2`, `float-array-3`, `float-array-6`) constrain `width` to a constant value for specific use cases.

**See also:** [float-array-1](float-array-1.md) (width 1), [float-array-2](float-array-2.md) (width 2), [float-array-3](float-array-3.md) (width 3), [float-array-6](float-array-6.md) (width 6) — width specialisations.

## Properties

<FlatProperties />
