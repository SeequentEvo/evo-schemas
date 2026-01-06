### downhole-collection (v1.0.1)
The locations of the downholes in the collection.

| Property | Type | Description | Flags |
|---|---|---|---|
| coordinates | [float-array-3](../elements/float-array-3-1.0.1.md) | Coordinates. Columns: x, y, z. | [⬆️](../components/locations-1.0.1.md) ✅ |
| attributes | [one-of-attribute](../components/one-of-attribute-1.0.1.md) | Attribute data. | [⬆️](../components/attribute-list-property-1.0.1.md) |
| distances | [float-array-3](../elements/float-array-3-1.0.1.md) | The distances stored in columns final, target, current. | ✅ |
| holes | [downhole-collection](../objects/downhole-collection-1.0.1-location-holes.md) | The data describing the holes. | ✅ |
| hole_id | [category-data](../components/category-data-1.0.1.md) | Hole IDs. | ✅ |
| path | [downhole-collection](../objects/downhole-collection-1.0.1-location-path.md) | The path taken by the downhole location. Columns: distance, azimuth, dip. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

