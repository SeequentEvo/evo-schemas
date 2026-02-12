### magnetics (v1.1.0)
Magnetics survey data.

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
| type | String | Survey mode. |  |
| survey_type | String | Type of survey. |  |
| gradient_magnetic | [magnetics](../objects/magnetics-1.1.0-gradient_magnetic.md) | Gradient magnetic details. |  |
| base_stations | Array[[magnetics](../objects/magnetics-1.1.0-base_stations.md)] | Base stations. |  |
| magnetic_line_list | Array[[survey-line](../components/survey-line-1.1.0.md)] | Magnetic line list. |  |
| qaqc_magnetic_azimuth_test_list | Array[[survey-line](../components/survey-line-1.1.0.md)] | QA/QC Magnetic azimuth test list. |  |
| qaqc_noise_test_list | Array[[survey-line](../components/survey-line-1.1.0.md)] | QA/QC Magnetic noise test list. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

