### frequency-domain-electromagnetic (v1.0.0)
Frequency Domain Electromagnetic data.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | ⬆️ ✅ |
| uuid | base-object-properties | Identifier of the object. | ⬆️ ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | ⬆️ |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | ⬆️ |
| tags | Object | Key-value pairs of user-defined metadata | ⬆️ |
| bounding_box | bounding-box | Bounding box of the spatial data. | ⬆️ ✅ |
| coordinate_reference_system | crs | Coordinate system of the spatial data | ⬆️ ✅ |
| schema | String |  | ✅ |
| survey | frequency-domain-electromagnetic | Survey information. | ✅ |
| data_type | String | Data type. |  |
| channels | Array[frequency-domain-electromagnetic-channel] | Channel information. | ✅ |
| line_list | Array[survey-line] | Line list. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

