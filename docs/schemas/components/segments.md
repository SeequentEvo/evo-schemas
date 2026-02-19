import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/segments-1.2.0.md';

# segments

<SchemaUri uri="schema/components/segments/1.2.0/segments.schema.json" />

The `segments` component defines a set of line segments by pairs of vertex indices.

* `vertices` — An N×3 array of 3D coordinates defining the vertex positions.
* `indices` — An M×2 [index-array-2](../elements/index-array-2.md) of (start, end) vertex pairs, each defining one segment. Indices are 0-based and reference positions in the `vertices` array.

An optional attribute list can be associated with both vertices and indices, allowing per-vertex and per-segment properties.

**Used by:** [line-segments](../objects/line-segments.md), [triangle-mesh](../objects/triangle-mesh.md).

**See also:** [triangles](triangles.md), [quadrilaterals](quadrilaterals.md), [hexahedrons](hexahedrons.md), [tetrahedra](tetrahedra.md) (other cell types).

## Properties

<FlatProperties />
