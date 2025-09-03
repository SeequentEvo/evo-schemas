### magnetics (v1.2.0)
Magnetics survey data.

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
| type | String | Survey mode. | ✅ |
| survey_type | String | Type of survey. | ✅ |
| gradient_magnetic | magnetics | Gradient magnetic details. |  |
| base_stations | Array[magnetics] | Base stations. |  |
| magnetic_line_list | Array[survey-line] | Magnetic line list. | ✅ |
| qaqc_magnetic_azimuth_test_list | Array[survey-line] | QA/QC Magnetic azimuth test list. |  |
| qaqc_noise_test_list | Array[survey-line] | QA/QC Magnetic noise test list. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

