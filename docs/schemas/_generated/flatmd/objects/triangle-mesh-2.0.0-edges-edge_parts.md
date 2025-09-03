### triangle-mesh (v2.0.0)
A structure defining edge chunks of the mesh.

| Property | Type | Description | Flags |
|---|---|---|---|
| attributes | one-of-attribute | Attribute data. | ⬆️ |
| chunks | index-array-2 | A tuple defining the first index and the length of a chunk.
The chunk refers to a segment of the edges array.
Chunks do not have to include all edges, and chunks can overlap.
Columns: offset, count | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

