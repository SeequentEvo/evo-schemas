import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/embedded-triangulated-mesh-2.1.0.md';

# embedded-triangulated-mesh

<SchemaUri uri="schema/components/embedded-triangulated-mesh/2.1.0/embedded-triangulated-mesh.schema.json" />

The `embedded-triangulated-mesh` component represents a triangulated mesh that can be decomposed into
[parts](../../understanding-schemas/understanding-parts.md).

* `triangles` — A [triangles](triangles.md) component defining the mesh geometry.
* `parts` — An optional list of [geometry-part](geometry-part.md) components, each referencing a subset of the mesh.

**See also:** [embedded-line-geometry](embedded-line-geometry.md) (polyline equivalent), [embedded-mesh-object](embedded-mesh-object.md).

**Used by:** [triangle-mesh](../objects/triangle-mesh.md), [geological-model-meshes](../objects/geological-model-meshes.md).

## Properties

<FlatProperties />
