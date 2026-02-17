### experimental-variogram (v1.0.0)
An experimental variogram object representing spatial continuity statistics for a single variable, grouped by direction and lag distance.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/base-object-properties-1.1.0.md) ✅ |
| uuid | [base-object-properties](../components/base-object-properties-1.1.0-uuid.md) | Identifier of the object. | [⬆️](../components/base-object-properties-1.1.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/base-object-properties-1.1.0.md) |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | [⬆️](../components/base-object-properties-1.1.0.md) |
| tags | Object | Key-value pairs of user-defined metadata | [⬆️](../components/base-object-properties-1.1.0.md) |
| lineage | [lineage](../components/lineage-1.0.0.md) | Information about the history of the object | [⬆️](../components/base-object-properties-1.1.0.md) |
| schema | String |  | ✅ |
| domain | String | The domain the experimental variogram is calculated for. |  |
| attribute | String | The attribute the experimental variogram is calculated for. |  |
| data_variance | Number | The variance of the source data, often used as the expected sill of the variogram. | ✅ |
| variogram_type | String | The type of calculation performed (e.g., variogram, semi-variogram, covariance, correlogram). |  |
| distance_unit | [unit-length](../elements/unit-length-1.0.1-unit_categories.md) | Distance unit. |  |
| attribute_unit | [unit](../elements/unit-1.0.1.md) | Attribute unit |  |
| directions | [experimental-variogram](../objects/experimental-variogram-1.0.0-directions.md) | A data-table defining the parameters for each variogram direction. | ✅ |
| lags | [experimental-variogram](../objects/experimental-variogram-1.0.0-lags.md) | A data-table containing the calculated values for each lag bin. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

