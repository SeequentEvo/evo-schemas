### hole-collars (v1.0.0)
Hole collars represent the surface locations where drillholes begin. Contains the 3D coordinates (x, y, z), depth information, hole indices, and attributes for the collars of drillholes.

| Property | Type | Description | Flags |
|---|---|---|---|
| coordinates | float-array-3 | Coordinates. Columns: x, y, z. | ⬆️ ✅ |
| attributes | one-of-attribute | Attribute data. | ⬆️ |
| distances | float-array-3 | The depth values for each drillhole. Columns: final, target, current. | ✅ |
| holes | hole-chunks | The data describing the hole paths. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

