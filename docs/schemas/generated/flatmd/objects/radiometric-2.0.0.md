### radiometric (v2.0.0)
Radiometric survey data.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/base-object-properties-1.1.0.md) ✅ |
| uuid | [base-object-properties](../components/base-object-properties-1.1.0-uuid.md) | Identifier of the object. | [⬆️](../components/base-object-properties-1.1.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/base-object-properties-1.1.0.md) |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | [⬆️](../components/base-object-properties-1.1.0.md) |
| tags | Object | Key-value pairs of user-defined metadata | [⬆️](../components/base-object-properties-1.1.0.md) |
| lineage | [lineage](../components/lineage-1.0.0.md) | Information about the history of the object | [⬆️](../components/base-object-properties-1.1.0.md) |
| bounding_box | [bounding-box](../components/bounding-box-1.0.1.md) | Bounding box of the spatial data. | [⬆️](../components/base-spatial-data-properties-1.1.0.md) ✅ |
| coordinate_reference_system | [crs](../components/crs-1.0.1.md) | Coordinate system of the spatial data | [⬆️](../components/base-spatial-data-properties-1.1.0.md) ✅ |
| schema | String |  | ✅ |
| survey | [radiometric](../objects/radiometric-2.0.0-survey.md) | Survey information. | ✅ |
| sample_time | Number | Total time that elapses between each record (msec). Required for idle/live time corrections. |  |
| array_dimension | Integer | Array dimension. | ✅ |
| energy_level | Number | Energy level (meV) of array elements. |  |
| attribute_definition_list | Array[[survey-attribute-definition](../components/survey-attribute-definition-1.0.1.md)] | List of attribute definitions. These will be referenced in survey collections. | ✅ |
| collections | Array[[survey-collection](../components/survey-collection-1.0.1.md)] | Survey collections. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

