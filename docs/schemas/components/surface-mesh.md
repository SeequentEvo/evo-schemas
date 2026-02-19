import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/surface-mesh-1.0.1.md';

# surface-mesh

<SchemaUri uri="schema/components/surface-mesh/1.0.1/surface-mesh.schema.json" />

The `surface-mesh` component describes a triangulated surface mesh.

* `kind` — Whether the mesh is `"Open"` (a surface with boundaries) or `"Closed"` (a watertight volume boundary).
* `quality` — An optional [mesh-quality](mesh-quality.md) component specifying quality guarantees.
* `triangles` — An index array of vertex triplets defining the mesh triangles (0-based indices).

**Used by:** [brep-container](brep-container.md), [geometry-composite](geometry-composite.md).

## Properties

<FlatProperties />
