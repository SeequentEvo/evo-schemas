### downhole-attributes (v1.0.0)

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the table. | [⬆️](../components/relative-planar-data-table-1.2.0.md) ✅ |
| collection_type | String | The type of the collection. | [⬆️](../components/relative-planar-data-table-1.2.0.md) ✅ |
| distance | [relative-planar-data-table](../components/relative-planar-data-table-1.2.0-distance.md) | The distance down the drillhole. | [⬆️](../components/relative-planar-data-table-1.2.0.md) ✅ |
| relative_plane_angles | [float-array-2](../elements/float-array-2-1.0.1.md) | Planar measurements relative to the drillhole. Columns: alpha, beta | [⬆️](../components/relative-planar-data-table-1.2.0.md) ✅ |
| plane_polarity | [bool-array-1](../elements/bool-array-1-1.0.1.md) | Polarity of the planar measurements. Column: has_positive_polarity | [⬆️](../components/relative-planar-data-table-1.2.0.md) |
| holes | [hole-chunks](../components/hole-chunks-1.0.0.md) | The data describing the holes. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

