import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/unstructured-grid-geometry-1.2.0.md';

# unstructured-grid-geometry

<SchemaUri uri="schema/components/unstructured-grid-geometry/1.2.0/unstructured-grid-geometry.schema.json" />

The `unstructured-grid-geometry` component describes the geometry of an unstructured grid, composed of vertices,
cell definitions, and connectivity indices.

* `vertices` — An array of 3D coordinates.
* `cells` — Cell type and offset information.
* `indices` — Connectivity indices into the vertex array.

See [Cell-type geometry](../../understanding-schemas/cell-type-geometry.md) for details on how cell types are encoded.

**Used by:** [unstructured-grid](../unstructured-grid.md).

## Properties

<FlatProperties />
