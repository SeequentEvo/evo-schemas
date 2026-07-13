import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/hexahedrons-1.2.0.md';

# hexahedrons

<SchemaUri uri="schema/components/hexahedrons/1.2.0/hexahedrons.schema.json" />

The `hexahedrons` component defines a set of hexahedral (brick) cells by their vertices and connectivity.

* `vertices` — An array of 3D coordinates.
* `indices` — An index array of 8-tuples defining hexahedral cells. Indices are 0-based.

The vertex coordinate columns follow the axis order declared in the object's `coordinate_reference_system` — see [Coordinate reference systems and axis order](../../understanding-schemas/coordinate-reference-systems.md).

**Used by:** [unstructured-hex-grid](../objects/unstructured-hex-grid.md).

**See also:** [triangles](triangles.md), [quadrilaterals](quadrilaterals.md), [tetrahedra](tetrahedra.md), [segments](segments.md) (other cell types).

## Properties

<FlatProperties />
