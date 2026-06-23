### embedded-triangulated-mesh (v2.0.0)
A structure defining chunks the mesh is composed of.

| Property | Type | Description | Flags |
|---|---|---|---|
| attributes | [one-of-attribute](../components/one-of-attribute-1.1.0.md) | Attribute data. | [⬆️](../components/attribute-list-property-1.1.0.md) |
| chunks | [index-array-2](../elements/index-array-2-1.0.1.md) | A tuple defining the first index and the length of a chunk.<br>If triangle_indices is defined, the chunk refers to a segment of the triangle_indices array.<br>Otherwise, the chunk refers to a segment of the triangles array.<br>Chunks do not have to include all triangles, and chunks can overlap.<br>Columns: offset, count | ✅ |
| triangle_indices | [index-array-1](../elements/index-array-1-1.0.1.md) | An optional index array into the triangle indices set.<br>This is used to define chunks if the mesh triangle indices do not contain contiguous chunks. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

