### hole-collars (v1.0.0)
Hole collars represent the surface locations where drillholes begin. Contains the 3D coordinates (x, y, z), depth information, hole indices, and attributes for the collars of drillholes.

| Property | Type | Description | Flags |
|---|---|---|---|
| coordinates | [float-array-3](../elements/float-array-3-1.0.1.md) | Coordinates. Columns: x, y, z. | [⬆️](../components/locations-1.0.1.md) |
| attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attribute data. | [⬆️](../components/attribute-list-property-1.2.0.md) |
| distances | [float-array-3](../elements/float-array-3-1.0.1.md) | The depth values for each drillhole. Columns: final, target, current. |  |
| holes | [hole-chunks](../components/hole-chunks-1.0.0.md) | The data describing the hole paths. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

