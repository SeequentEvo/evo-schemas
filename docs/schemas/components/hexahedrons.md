import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/hexahedrons-1.2.0.md';

# hexahedrons

<SchemaUri uri="schema/components/hexahedrons/1.2.0/hexahedrons.schema.json" />

The `hexahedrons` component defines a set of hexahedral (brick) cells by their vertices and connectivity.

* `vertices` — An array of 3D coordinates.
* `indices` — An index array of 8-tuples defining hexahedral cells. Indices are 0-based.

**See also:** [triangles](triangles.md), [quadrilaterals](quadrilaterals.md), [tetrahedra](tetrahedra.md), [segments](segments.md) (other cell types).

**Used by:** [unstructured-hex-grid](../unstructured-hex-grid.md).

## Properties

<FlatProperties />
