### downhole-collection (v1.0.1)

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the table. | ⬆️ ✅ |
| collection_type | String | The type of the collection. | ⬆️ ✅ |
| distance | relative-planar-data-table | The distance down the drillhole. | ⬆️ ✅ |
| relative_plane_angles | float-array-2 | Planar measurements relative to the drillhole. Columns: alpha, beta | ⬆️ ✅ |
| plane_polarity | bool-array-1 | Polarity of the planar measurements. Column: has_positive_polarity | ⬆️ |
| holes | downhole-collection | The data describing the holes. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

