import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/quadrilaterals-1.2.1.md';

# quadrilaterals

<SchemaUri uri="schema/components/quadrilaterals/1.2.1/quadrilaterals.schema.json" />

The `quadrilaterals` component defines a set of quadrilateral cells by their vertices and connectivity.

* `vertices` — An array of 3D coordinates.
* `indices` — An index array of vertex quadruplets, each defining a quadrilateral face. Indices are 0-based.

The vertex coordinate columns follow the axis order declared in the object's `coordinate_reference_system` — see [Coordinate reference systems and axis order](../../understanding-schemas/coordinate-reference-systems.md).

**Used by:** [unstructured-quad-grid](../objects/unstructured-quad-grid.md).

**See also:** [triangles](triangles.md), [hexahedrons](hexahedrons.md), [tetrahedra](tetrahedra.md), [segments](segments.md) (other cell types).

## Properties

<FlatProperties />
