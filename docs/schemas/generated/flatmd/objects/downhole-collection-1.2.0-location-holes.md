### downhole-collection (v1.2.0)
The indices, counts, and offsets into locations of each hole. Columns: hole_index, offset, count.

| Property | Type | Description | Flags |
|---|---|---|---|
| data | [binary-blob](../elements/binary-blob-1.0.1.md) | The binary data for the holes. Columns: hole_index, offset, count. |  |
| length | Integer | length of array |  |
| width | Integer | number of columns |  |
| data_type | String | Data type for the columns. 1st column is of type int32, 2nd is uint64 and 3rd is uint64. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

