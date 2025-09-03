### downhole-collection (v1.3.1)
The locations of the downholes in the collection.

| Property | Type | Description | Flags |
|---|---|---|---|
| coordinates | float-array-3 | Coordinates. Columns: x, y, z. | ⬆️ ✅ |
| attributes | one-of-attribute | Attribute data. | ⬆️ |
| distances | float-array-3 | The depth values for each drillhole. Columns: final, target, current. | ⬆️ ✅ |
| holes | hole-chunks | The data describing the hole paths. | ⬆️ ✅ |
| hole_id | category-data | Hole IDs. | ✅ |
| path | downhole-direction-vector | The path taken by the downhole location. Columns: distance, azimuth, dip. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

