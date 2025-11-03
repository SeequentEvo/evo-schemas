### radiometric (v2.0.0)
Radiometric survey data.

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
| survey | radiometric | Survey information. | ✅ |
| sample_time | Number | Total time that elapses between each record (msec). Required for idle/live time corrections. |  |
| array_dimension | Integer | Array dimension. | ✅ |
| energy_level | Number | Energy level (meV) of array elements. |  |
| attribute_definition_list | Array[survey-attribute-definition] | List of attribute definitions. These will be referenced in survey collections. | ✅ |
| collections | Array[survey-collection] | Survey collections. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

