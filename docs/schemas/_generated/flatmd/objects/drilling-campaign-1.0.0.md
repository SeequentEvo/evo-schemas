### drilling-campaign (v1.0.0)
A planned drillholes and interim drillhole data for a drilling campaign.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | ⬆️ ✅ |
| uuid | base-object-properties | Identifier of the object. | ⬆️ ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | ⬆️ |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | ⬆️ |
| tags | Object | Key-value pairs of user-defined metadata | ⬆️ |
| lineage | lineage | Information about the history of the object | ⬆️ |
| bounding_box | bounding-box | Bounding box of the spatial data. | ⬆️ ✅ |
| coordinate_reference_system | crs | Coordinate system of the spatial data | ⬆️ ✅ |
| schema | String |  | ✅ |
| type | String | The type of the planned drillholes. |  |
| distance_unit | unit-length | The units of depth for the drillholes. |  |
| hole_id | category-data | Hole IDs. | ✅ |
| planned | drilling-campaign | Planned data for the drilling campaign. | ✅ |
| interim | drilling-campaign | Interim drillhole data for the drilling campaign. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

