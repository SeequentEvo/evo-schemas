### unstructured-grid-geometry (v1.2.0)
Cell descriptions which consists of an array of triples. The first item in the triple represents the shape, second item is an offset to the indices array and the third item is the number of vertices for the shape. Columns: shape, offset, num_vertices.

| Property | Type | Description | Flags |
|---|---|---|---|
| attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attribute data. | [⬆️](../components/attribute-list-property-1.2.0.md) |
| data | [binary-blob](../elements/binary-blob-1.0.1.md) | Data stored as a binary blob. | ✅ |
| length | Integer | length of array | ✅ |
| width | Integer | number of columns | ✅ |
| data_type | String | Data type for the columns. 1st column is of type int32, 2nd is uint64 and 3rd is int32. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

