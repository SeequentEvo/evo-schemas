### drilling-campaign (v1.0.0)
A planned drillholes and interim drillhole data for a drilling campaign.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/base-object-properties-1.1.0.md) |
| uuid | [base-object-properties](../components/base-object-properties-1.1.0-uuid.md) | Identifier of the object. | [⬆️](../components/base-object-properties-1.1.0.md) |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/base-object-properties-1.1.0.md) |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | [⬆️](../components/base-object-properties-1.1.0.md) |
| tags | Object | Key-value pairs of user-defined metadata | [⬆️](../components/base-object-properties-1.1.0.md) |
| lineage | [lineage](../components/lineage-1.0.0.md) | Information about the history of the object | [⬆️](../components/base-object-properties-1.1.0.md) |
| bounding_box | [bounding-box](../components/bounding-box-1.0.1.md) | Bounding box of the spatial data. | [⬆️](../components/base-spatial-data-properties-1.1.0.md) |
| coordinate_reference_system | [crs](../components/crs-1.0.1.md) | Coordinate system of the spatial data | [⬆️](../components/base-spatial-data-properties-1.1.0.md) |
| schema | String |  |  |
| type | String | The type of the planned drillholes. |  |
| distance_unit | [unit-length](../elements/unit-length-1.0.1-unit_categories.md) | The units of depth for the drillholes. |  |
| hole_id | [category-data](../components/category-data-1.0.1.md) | Hole IDs. |  |
| planned | [drilling-campaign](../objects/drilling-campaign-1.0.0-planned.md) | Planned data for the drilling campaign. |  |
| interim | [drilling-campaign](../objects/drilling-campaign-1.0.0-interim.md) | Interim drillhole data for the drilling campaign. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

