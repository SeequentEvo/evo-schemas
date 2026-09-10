---
seoTitle: float-array-3 Element for Evo Schemas | Seequent Developer
description: Review the float array 3 element schema for Geoscience Objects, supporting consistent data structures and reliable Seequent Evo workflows.
---

import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/elements/float-array-3-1.0.1.md';

# float-array-3

<SchemaUri uri="schema/elements/float-array-3/1.0.1/float-array-3.schema.json" />

Array of 64-bit floating-point values with three values per row (N×3). Extends [float-array-md](float-array-md.md) with a fixed width of 3. The most widely used element — stores 3D vertex coordinates, direction vectors, and RGB colour data across geometry and attribute components.

When the three columns hold coordinates, their order follows the axis order declared in the object's
`coordinate_reference_system` rather than a fixed easting/northing/elevation ordering. See
[Coordinate reference systems and axis order](../../understanding-schemas/coordinate-reference-systems.md).

**See also:** [float-array-md](float-array-md.md) (base type), [float-array-1](float-array-1.md), [float-array-2](float-array-2.md), [float-array-6](float-array-6.md) (other widths).

## Properties

<FlatProperties />
