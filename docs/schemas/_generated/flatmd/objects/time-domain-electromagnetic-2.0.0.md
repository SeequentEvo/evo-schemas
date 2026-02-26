### time-domain-electromagnetic (v2.0.0)
Time Domain Electromagnetic data.

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
| survey | time-domain-electromagnetic | Survey information. | ✅ |
| geometry_category | String | Geometry category. | ✅ |
| gps | coordinates-3d | Location of GPS relative to point of reference. | ✅ |
| waveforms | time-domain-electromagnetic-waveform | Waveform information. | ✅ |
| frame_geometry | time-domain-electromagnetic-frame-geometry | Frame geometry information. | ✅ |
| time_gates | time-domain-electromagnetic-time-gates | Time gate information. | ✅ |
| configurations | Array[time-domain-electromagnetic-configuration] | Time domain electromagnetic configurations. | ✅ |
| attribute_definition_list | Array[time-domain-electromagnetic] | List of attribute definitions. These will be referenced in survey collections. | ✅ |
| collections | Array[survey-collection] | Survey collections. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

