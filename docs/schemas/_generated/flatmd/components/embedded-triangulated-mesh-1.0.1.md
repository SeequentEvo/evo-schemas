### embedded-triangulated-mesh (v1.0.1)
A mesh made up of triangles, which is part of an object.

| Property | Type | Description | Flags |
|---|---|---|---|
| vertices | triangles | Vertex coordinates. Columns: x, y, z. | ⬆️ ✅ |
| indices | triangles | 0-based indices into the vertices. Each triple is a triangle. Columns: n0, n1, n2. | ⬆️ ✅ |
| kind | String | The kind of mesh. | ✅ |
| quality | mesh-quality | Mesh quality. |  |
| name | String | Name of the object. | ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. |  |
| material_key | String | Unique identifier of the material. |  |
| feature | String | Kind of feature. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

