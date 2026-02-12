### radiometric (v1.1.0)
Radiometric survey data.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/base-object-properties-1.0.1.md) |
| uuid | [base-object-properties](../components/base-object-properties-1.0.1-uuid.md) | Identifier of the object. | [⬆️](../components/base-object-properties-1.0.1.md) |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/base-object-properties-1.0.1.md) |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | [⬆️](../components/base-object-properties-1.0.1.md) |
| tags | Object | Key-value pairs of user-defined metadata | [⬆️](../components/base-object-properties-1.0.1.md) |
| bounding_box | [bounding-box](../components/bounding-box-1.0.1.md) | Bounding box of the spatial data. | [⬆️](../components/base-spatial-data-properties-1.0.1.md) |
| coordinate_reference_system | [crs](../components/crs-1.0.1.md) | Coordinate system of the spatial data | [⬆️](../components/base-spatial-data-properties-1.0.1.md) |
| schema | String |  |  |
| survey | [radiometric](../objects/radiometric-1.1.0-survey.md) | Survey information. |  |
| dead_time | Number | Dead time (msec). |  |
| live_time | Number | Live time (msec). |  |
| idle_time | Number | Idle time (msec). |  |
| array_dimension | Integer | Array dimension. |  |
| energy_level | Number | Energy level (meV) of array elements. |  |
| line_list | Array[[survey-line](../components/survey-line-1.1.0.md)] | Line list. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

