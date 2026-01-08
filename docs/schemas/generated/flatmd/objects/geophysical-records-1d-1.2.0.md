### geophysical-records-1d (v1.2.0)
1D geophysical records.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/base-object-properties-1.0.1.md) ✅ |
| uuid | [base-object-properties](../components/base-object-properties-1.0.1-uuid.md) | Identifier of the object. | [⬆️](../components/base-object-properties-1.0.1.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/base-object-properties-1.0.1.md) |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | [⬆️](../components/base-object-properties-1.0.1.md) |
| tags | Object | Key-value pairs of user-defined metadata | [⬆️](../components/base-object-properties-1.0.1.md) |
| bounding_box | [bounding-box](../components/bounding-box-1.0.1.md) | Bounding box of the spatial data. | [⬆️](../components/base-spatial-data-properties-1.0.1.md) ✅ |
| coordinate_reference_system | [crs](../components/crs-1.0.1.md) | Coordinate system of the spatial data | [⬆️](../components/base-spatial-data-properties-1.0.1.md) ✅ |
| schema | String |  | ✅ |
| number_of_layers | Integer | Number of layers. | ✅ |
| locations | [geophysical-records-1d](../objects/geophysical-records-1d-1.2.0-locations.md) | Array of locations. | ✅ |
| depths | [geophysical-records-1d](../objects/geophysical-records-1d-1.2.0-depths.md) | Array of depths. | ✅ |
| line_numbers | [category-data](../components/category-data-1.0.1.md) | Line numbers. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

