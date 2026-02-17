### relative-planar-data-table (v1.0.1)
A table of planar data relative to a drillhole

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the table. | ✅ |
| collection_type | String | The type of the collection. | ✅ |
| distance | [relative-planar-data-table](../components/relative-planar-data-table-1.0.1-distance.md) | The distance down the drillhole. | ✅ |
| relative_plane_angles | [float-array-2](../elements/float-array-2-1.0.1.md) | Planar measurements relative to the drillhole. Columns: alpha, beta | ✅ |
| plane_polarity | [bool-array-1](../elements/bool-array-1-1.0.1.md) | Polarity of the planar measurements. Column: has_positive_polarity |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

