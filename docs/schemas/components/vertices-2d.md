import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/vertices-2d-1.0.1.md';

# vertices-2d

<SchemaUri uri="schema/components/vertices-2d/1.0.1/vertices-2d.schema.json" />

The `vertices-2d` component stores a set of 2D vertex coordinates.

* `vertices` — An N×2 array of (x, y) coordinates, stored as a [float-array-2](../elements/float-array-2.md) element. Vertex ordering is significant — other components (e.g., segment indices, polyline indices) reference vertices by their 0-based position in this array.

**Used by:** [design-geometry](../objects/design-geometry.md).

**See also:** [vertices-3d](vertices-3d.md) (3D counterpart).

## Properties

<FlatProperties />
