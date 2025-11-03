### embedded-line-geometry (v1.0.0)
A set of polylines composed of straight line segments.

| Property | Type | Description | Flags |
|---|---|---|---|
| vertices | embedded-line-geometry | Vertex coordinates in 2D space. Columns: u, v. | ✅ |
| chunks | embedded-line-geometry | A tuple defining the first index and the length of a chunk of vertices, forming a polyline/polygon.
If indices is defined, the chunk refers to a segment of the indices array.
Otherwise, the chunk refers to a segment of the vertices array.
Chunks can overlap.
Columns: offset, count | ✅ |
| indices | index-array-1 | An optional index array into the vertices.
This is used to define chunks if the vertices list do not contain contiguous chunks. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

