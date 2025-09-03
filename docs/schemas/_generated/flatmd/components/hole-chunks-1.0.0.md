### hole-chunks (v1.0.0)
Used to indicate which rows of the segment and attribute tables are associated with a specific drillhole. The indices, counts, and offsets into locations and attribute tables of each hole. Columns: hole_index, offset, count.

| Property | Type | Description | Flags |
|---|---|---|---|
| data | binary-blob | The binary data for the holes. Columns: hole_index, offset, count. | ✅ |
| length | Integer | length of array | ✅ |
| width | Integer | number of columns | ✅ |
| data_type | String | Data type for the columns. 1st column is of type int32, 2nd is uint64 and 3rd is uint64. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

