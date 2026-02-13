import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/elements/integer-array-md-1.0.1.md';

# integer-array-md

<SchemaUri uri="schema/elements/integer-array-md/1.0.1/integer-array-md.schema.json" />

Multi-dimensional array of integer values. The base type for all integer array specialisations. Each row stores `width` values, with `length` rows total. Supports both int32 and int64 encoding via the `data_type` property.

The integer array family uses a width specialisation pattern: `integer-array-md` defines the general case with a variable `width`, while fixed-width variants (`integer-array-1`, `integer-array-2`, `integer-array-3`) constrain `width` to a constant value for specific use cases.

**See also:** [integer-array-1](integer-array-1.md) (1D), [integer-array-2](integer-array-2.md) (2D), [integer-array-3](integer-array-3.md) (3D) — width specialisations.

## Properties

<FlatProperties />
