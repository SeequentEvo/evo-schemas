### time-domain-electromagnetic (v1.0.0)
Time Domain Electromagnetic data.

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
| survey | [time-domain-electromagnetic](../objects/time-domain-electromagnetic-1.0.0-survey.md) | Survey information. |  |
| geometry_category | String | Geometry category. |  |
| gps | [coordinates-3d](../elements/coordinates-3d-1.0.0.md) | Location of GPS relative to point of reference. |  |
| channels | Array[[time-domain-electromagnetic-channel](../components/time-domain-electromagnetic-channel-1.0.0.md)] | Channel information. |  |
| line_list | Array[[survey-line](../components/survey-line-1.1.0.md)] | Line list. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

