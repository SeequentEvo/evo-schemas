### embedded-line-geometry (v1.0.0)
A set of polylines composed of straight line segments.

| Property | Type | Description | Flags |
|---|---|---|---|
| vertices | [embedded-line-geometry](../components/embedded-line-geometry-1.0.0-vertices.md) | Vertex coordinates in 2D space. Columns: u, v. | ✅ |
| chunks | [embedded-line-geometry](../components/embedded-line-geometry-1.0.0-chunks.md) | A tuple defining the first index and the length of a chunk of vertices, forming a polyline/polygon.<br>If indices is defined, the chunk refers to a segment of the indices array.<br>Otherwise, the chunk refers to a segment of the vertices array.<br>Chunks can overlap.<br>Columns: offset, count | ✅ |
| indices | [index-array-1](../elements/index-array-1-1.0.1.md) | An optional index array into the vertices.<br>This is used to define chunks if the vertices list do not contain contiguous chunks. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

