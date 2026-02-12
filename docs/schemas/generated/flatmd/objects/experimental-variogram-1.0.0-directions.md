### experimental-variogram (v1.0.0)
A data-table defining the parameters for each variogram direction.

| Property | Type | Description | Flags |
|---|---|---|---|
| attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attribute data. | [⬆️](../components/attribute-list-property-1.2.0.md) |
| data | [binary-blob](../elements/binary-blob-1.0.1.md) | Binary blob reference for the directions data table. Columns: offset, count, direction_type, azimuth, dip, azimuth_tolerance, dip_tolerance, bandwidth, bandheight. |  |
| length | Integer | Number of directions. |  |
| width | Integer | Number of columns in the core directions data table. |  |
| data_type | String | Data types for the core directions columns. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

