---
seoTitle: float-array-2 Element for Evo Schemas | Seequent Developer
description: Review the float array 2 element schema for Geoscience Objects, supporting consistent data structures and reliable Seequent Evo workflows.
---

import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/elements/float-array-2-1.0.1.md';

# float-array-2

<SchemaUri uri="schema/elements/float-array-2/1.0.1/float-array-2.schema.json" />

Array of 64-bit floating-point values with two values per row (N×2). Extends [float-array-md](float-array-md.md) with a fixed width of 2. Used for paired values such as 2D coordinates and from-to depth ranges.

When the two columns hold coordinates, their order follows the axis order declared in the object's
`coordinate_reference_system` rather than a fixed easting/northing ordering. See
[Coordinate reference systems and axis order](../../understanding-schemas/coordinate-reference-systems.md).

**See also:** [float-array-md](float-array-md.md) (base type), [float-array-1](float-array-1.md), [float-array-3](float-array-3.md), [float-array-6](float-array-6.md) (other widths).

## Properties

<FlatProperties />
