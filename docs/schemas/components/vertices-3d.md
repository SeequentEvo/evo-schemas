import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/vertices-3d-1.0.2.md';

# vertices-3d

<SchemaUri uri="schema/components/vertices-3d/1.0.2/vertices-3d.schema.json" />

The `vertices-3d` component stores a set of 3D vertex coordinates.

* `vertices` — An N×3 array of (x, y, z) coordinates, stored as a [float-array-3](../elements/float-array-3.md) element. Vertex ordering is significant — other components (e.g., segment indices, triangle indices) reference vertices by their 0-based position in this array.

The `x`, `y`, `z` columns follow the axis order declared in the object's `coordinate_reference_system` — see [Coordinate reference systems and axis order](../../understanding-schemas/coordinate-reference-systems.md).

**Used by:** [design-geometry](../objects/design-geometry.md).

**See also:** [vertices-2d](vertices-2d.md) (2D counterpart).

## Properties

<FlatProperties />
