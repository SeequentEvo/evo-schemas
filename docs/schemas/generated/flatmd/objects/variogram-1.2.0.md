### variogram (v1.2.0)
Variogram model and associated metadata. The variogram model is defined by the nugget, and multiple structures using the leapfrog-convention rotation. See struture and rotation components for additional details.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/base-object-properties-1.1.0.md) |
| uuid | [base-object-properties](../components/base-object-properties-1.1.0-uuid.md) | Identifier of the object. | [⬆️](../components/base-object-properties-1.1.0.md) |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/base-object-properties-1.1.0.md) |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | [⬆️](../components/base-object-properties-1.1.0.md) |
| tags | Object | Key-value pairs of user-defined metadata | [⬆️](../components/base-object-properties-1.1.0.md) |
| lineage | [lineage](../components/lineage-1.0.0.md) | Information about the history of the object | [⬆️](../components/base-object-properties-1.1.0.md) |
| schema | String |  |  |
| nugget | Number | The variance between two samples separated by near-zero lag distance, representing the randomness present. When plotted, this value is the y-intercept. |  |
| sill | Number | The variance of the variogram. This must be within a very small tolerance of the nugget plus the sum of all structure's contributions. |  |
| data_variance | Number | The variance of the data, if different from the sill value, this is used for normalising or rescaling the variogram |  |
| is_rotation_fixed | Boolean | Boolean value specifying whether all structure's rotations are the same. |  |
| structures | Array[[variogram](../objects/variogram-1.2.0-structures.md)] | A list of at least one mathematical model, which are parameterised to represent the spatial structure of the variogram model. |  |
| modelling_space | String | The modelling space the variogram model was fitted in either data for original units or normalscore for gaussian space. |  |
| domain | String | The domain the variogram is modelled for |  |
| attribute | String | The attribute the variogram is modelled for |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

