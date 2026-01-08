### embedded-line-geometry (v1.0.0)
A tuple defining the first index and the length of a chunk of vertices, forming a polyline/polygon.
If indices is defined, the chunk refers to a segment of the indices array.
Otherwise, the chunk refers to a segment of the vertices array.
Chunks can overlap.
Columns: offset, count

| Property | Type | Description | Flags |
|---|---|---|---|
| data | [binary-blob](../elements/binary-blob-1.0.1.md) | Data stored as a binary blob. | [⬆️](../elements/index-array-2-1.0.1.md) ✅ |
| length | Integer | length of array | [⬆️](../elements/index-array-2-1.0.1.md) ✅ |
| width | Integer | number of columns | [⬆️](../elements/index-array-2-1.0.1.md) ✅ |
| data_type | String | data type | [⬆️](../elements/index-array-2-1.0.1.md) ✅ |
| attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attribute data. | [⬆️](../components/attribute-list-property-1.2.0.md) |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

