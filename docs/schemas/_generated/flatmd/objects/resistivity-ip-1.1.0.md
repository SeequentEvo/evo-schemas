### resistivity-ip (v1.1.0)
Resistivity-IP data.

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
| number_of_dimensions | String | Survey dimension. | ✅ |
| number_contributing_electrodes | Integer | Number of contributing electrodes. Not including remote electrodes. | ✅ |
| survey | resistivity-ip | Survey information. | ✅ |
| configuration | resistivity-ip | Configuration information. | ✅ |
| line_list | Array[resistivity-ip-line] | Line list. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

