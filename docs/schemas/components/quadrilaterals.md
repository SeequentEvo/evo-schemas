import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/quadrilaterals-1.2.0.md';

# quadrilaterals

<SchemaUri uri="schema/components/quadrilaterals/1.2.0/quadrilaterals.schema.json" />

The `quadrilaterals` component defines a set of quadrilateral cells by their vertices and connectivity.

* `vertices` — An array of 3D coordinates.
* `indices` — An index array of vertex quadruplets, each defining a quadrilateral face. Indices are 0-based.

**See also:** [triangles](triangles.md), [hexahedrons](hexahedrons.md), [tetrahedra](tetrahedra.md), [segments](segments.md) (other cell types).

**Used by:** [unstructured-quad-grid](../unstructured-quad-grid.md).

## Properties

<FlatProperties />
