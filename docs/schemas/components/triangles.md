import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/triangles-1.2.0.md';

# triangles

<SchemaUri uri="schema/components/triangles/1.2.0/triangles.schema.json" />

The `triangles` component defines a set of triangles by their vertices and connectivity.

* `vertices` — An array of 3D coordinates.
* `indices` — An index array of vertex triplets (i, j, k), each defining a triangle. Indices are 0-based.

An optional attribute list can be associated with both vertices and indices.

**See also:** [quadrilaterals](quadrilaterals.md), [hexahedrons](hexahedrons.md), [tetrahedra](tetrahedra.md), [segments](segments.md) (other cell types).

## Properties

<FlatProperties />
