### embedded-triangulated-mesh (v1.0.1)
A mesh made up of triangles, which is part of an object.

| Property | Type | Description | Flags |
|---|---|---|---|
| vertices | [triangles](../components/triangles-1.0.1-vertices.md) | Vertex coordinates. Columns: x, y, z. | [⬆️](../components/triangles-1.0.1.md) ✅ |
| indices | [triangles](../components/triangles-1.0.1-indices.md) | 0-based indices into the vertices. Each triple is a triangle. Columns: n0, n1, n2. | [⬆️](../components/triangles-1.0.1.md) ✅ |
| kind | String | The kind of mesh. | ✅ |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. |  |
| name | String | Name of the object. | ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. |  |
| material_key | String | Unique identifier of the material. |  |
| feature | String | Kind of feature. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

