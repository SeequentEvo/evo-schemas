### lines-3d-indices (v1.0.1)
This component describes line endpoints for 3D lines. It has two columns (start,end), which are indices into vertices_3D for the line endpoint. Unlike 2D, curved segments in 3D would use a 2D segment with a transform, or be represented via a BREP

| Property | Type | Description | Flags |
|---|---|---|---|
| indices | index-array-2 | 0-based indices into the vertices. Columns: start, end. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

