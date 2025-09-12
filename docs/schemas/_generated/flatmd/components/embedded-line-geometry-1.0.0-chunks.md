### embedded-line-geometry (v1.0.0)
A tuple defining the first index and the length of a chunk of vertices, forming a polyline/polygon.
If indices is defined, the chunk refers to a segment of the indices array.
Otherwise, the chunk refers to a segment of the vertices array.
Chunks can overlap.
Columns: offset, count

| Property | Type | Description | Flags |
|---|---|---|---|
| data | binary-blob | Data stored as a binary blob. | ⬆️ ✅ |
| length | Integer | length of array | ⬆️ ✅ |
| width | Integer | number of columns | ⬆️ ✅ |
| data_type | String | data type | ⬆️ ✅ |
| attributes | one-of-attribute | Attribute data. | ⬆️ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

