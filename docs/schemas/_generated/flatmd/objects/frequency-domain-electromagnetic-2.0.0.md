### frequency-domain-electromagnetic (v2.0.0)
Frequency Domain Electromagnetic data.

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
| survey | frequency-domain-electromagnetic | Survey information. | ✅ |
| data_type | String | Data type. |  |
| configurations | Array[frequency-domain-electromagnetic-configuration] | Frequency domain electromagnetic configurations. |  |
| attribute_definition_list | Array[frequency-domain-electromagnetic] | List of attribute definitions. These will be referenced in survey collections. | ✅ |
| collections | Array[survey-collection] | Survey collections. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

