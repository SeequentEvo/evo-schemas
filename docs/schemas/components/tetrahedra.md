import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/tetrahedra-1.2.0.md';

# tetrahedra

<SchemaUri uri="schema/components/tetrahedra/1.2.0/tetrahedra.schema.json" />

The `tetrahedra` component defines a set of tetrahedral cells by their vertices and connectivity.

* `vertices` — An array of 3D coordinates.
* `indices` — An index array of vertex quadruplets, each defining a tetrahedron. Indices are 0-based.

**See also:** [triangles](triangles.md), [quadrilaterals](quadrilaterals.md), [hexahedrons](hexahedrons.md), [segments](segments.md) (other cell types).

**Used by:** [unstructured-tet-grid](../unstructured-tet-grid.md).

## Properties

<FlatProperties />
