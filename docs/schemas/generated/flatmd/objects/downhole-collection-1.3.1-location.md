### downhole-collection (v1.3.1)
The locations of the downholes in the collection.

| Property | Type | Description | Flags |
|---|---|---|---|
| coordinates | [float-array-3](../elements/float-array-3-1.0.1.md) | Coordinates. Columns: x, y, z. | [⬆️](../components/locations-1.0.1.md) ✅ |
| attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attribute data. | [⬆️](../components/attribute-list-property-1.2.0.md) |
| distances | [float-array-3](../elements/float-array-3-1.0.1.md) | The depth values for each drillhole. Columns: final, target, current. | [⬆️](../components/hole-collars-1.0.0.md) ✅ |
| holes | [hole-chunks](../components/hole-chunks-1.0.0.md) | The data describing the hole paths. | [⬆️](../components/hole-collars-1.0.0.md) ✅ |
| hole_id | [category-data](../components/category-data-1.0.1.md) | Hole IDs. | ✅ |
| path | [downhole-direction-vector](../components/downhole-direction-vector-1.0.0.md) | The path taken by the downhole location. Columns: distance, azimuth, dip. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

