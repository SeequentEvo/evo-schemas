import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/polyline-2d-1.0.1.md';

# polyline-2d

<SchemaUri uri="schema/components/polyline-2d/1.0.1/polyline-2d.schema.json" />

The `polyline-2d` component describes a 2D polyline, defined as a contiguous sequence of vertices.

* `begin` — The starting index into the parent vertex array.
* `count` — The number of vertices in the polyline.
* `closed` — Whether the polyline forms a closed loop.
* `shape` — The shape type of the polyline.

**Used by:** [geometry-composite](geometry-composite.md).

**See also:** [polyline-3d](polyline-3d.md) (3D counterpart).

## Properties

<FlatProperties />
