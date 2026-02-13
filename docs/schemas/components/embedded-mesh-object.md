import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/embedded-mesh-object-1.0.0.md';

# embedded-mesh-object

<SchemaUri uri="schema/components/embedded-mesh-object/1.0.0/embedded-mesh-object.schema.json" />

The `embedded-mesh-object` component represents a named mesh object that references parts within an
[embedded-triangulated-mesh](embedded-triangulated-mesh.md).

* `name` — The name of the mesh object.
* `description` — An optional description.
* `quality` — An optional [mesh-quality](mesh-quality.md) specification.
* `parts` — A list of part references into the parent mesh.

**See also:** [embedded-polyline-object](embedded-polyline-object.md) (polyline equivalent).

**Used by:** [geological-model-meshes](../objects/geological-model-meshes.md).

## Properties

<FlatProperties />
