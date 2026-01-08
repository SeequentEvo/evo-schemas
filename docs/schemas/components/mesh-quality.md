import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/mesh-quality-1.0.1.md';

# mesh-quality

<SchemaUri uri="schema/components/mesh-quality/1.0.1/mesh-quality.schema.json" />

A set of quality guarantees associated with a mesh.

When consuming a mesh, optional guarantees of mesh quality allow us to avoid expensive post processing if provided. Often the producer knows a set of guarantees about the mesh it creates.

---

The quality can be one or more of:

- "Manifold": every edge has 1 - 2 adjacent elements.
- "ConsistentWinding": element nodes are always CW or CCW.
- "NonDegenerate": all triangle coordinates are unique resulting in a non-zero area for the element.
- "NonSelfIntersecting": No element in a mesh intersects another.
- "Continuous": Adjacent elements share nodes.

## Properties

<FlatProperties />
