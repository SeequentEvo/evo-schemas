### experimental-variogram (v1.0.0)
A data-table containing the calculated values for each lag bin.

| Property | Type | Description | Flags |
|---|---|---|---|
| attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attribute data. | [⬆️](../components/attribute-list-property-1.2.0.md) |
| data | [binary-blob](../elements/binary-blob-1.0.1.md) | Binary blob reference for the lag data table. The columns must be: start, end, centroid, value, num_pairs. | ✅ |
| length | Integer | Total number of lag bins across all directions. | ✅ |
| width | Integer | Number of columns in the core lag data table. | ✅ |
| data_type | String | Data types for the core lag data columns. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

