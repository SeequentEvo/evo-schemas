### resistivity-ip (v1.1.0)
Resistivity-IP data.

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
| number_of_dimensions | String | Survey dimension. |  |
| number_contributing_electrodes | Integer | Number of contributing electrodes. Not including remote electrodes. |  |
| survey | [resistivity-ip](../objects/resistivity-ip-1.1.0-survey.md) | Survey information. |  |
| configuration | [resistivity-ip](../objects/resistivity-ip-1.1.0-configuration.md) | Configuration information. |  |
| line_list | Array[[resistivity-ip-line](../components/resistivity-ip-line-1.1.0.md)] | Line list. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

