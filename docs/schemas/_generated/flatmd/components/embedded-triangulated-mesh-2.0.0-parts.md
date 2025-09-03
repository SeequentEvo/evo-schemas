### embedded-triangulated-mesh (v2.0.0)
A structure defining chunks the mesh is composed of.

| Property | Type | Description | Flags |
|---|---|---|---|
| attributes | one-of-attribute | Attribute data. | ⬆️ |
| chunks | index-array-2 | A tuple defining the first index and the length of a chunk.
If triangle_indices is defined, the chunk refers to a segment of the triangle_indices array.
Otherwise, the chunk refers to a segment of the triangles array.
Chunks do not have to include all triangles, and chunks can overlap.
Columns: offset, count | ✅ |
| triangle_indices | index-array-1 | An optional index array into the triangle indices set.
This is used to define chunks if the mesh triangle indices do not contain contiguous chunks. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

