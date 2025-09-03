### downhole-collection (v1.0.1)
The locations of the downholes in the collection.

| Property | Type | Description | Flags |
|---|---|---|---|
| coordinates | float-array-3 | Coordinates. Columns: x, y, z. | ⬆️ ✅ |
| attributes | one-of-attribute | Attribute data. | ⬆️ |
| distances | float-array-3 | The distances stored in columns final, target, current. | ✅ |
| holes | downhole-collection | The data describing the holes. | ✅ |
| hole_id | category-data | Hole IDs. | ✅ |
| path | downhole-collection | The path taken by the downhole location. Columns: distance, azimuth, dip. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

