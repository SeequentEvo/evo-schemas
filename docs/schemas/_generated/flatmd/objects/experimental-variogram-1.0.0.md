### experimental-variogram (v1.0.0)
An experimental variogram object representing spatial continuity statistics for a single variable, grouped by direction and lag distance.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | ⬆️ ✅ |
| uuid | base-object-properties | Identifier of the object. | ⬆️ ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | ⬆️ |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | ⬆️ |
| tags | Object | Key-value pairs of user-defined metadata | ⬆️ |
| lineage | lineage | Information about the history of the object | ⬆️ |
| schema | String |  | ✅ |
| domain | String | The domain the experimental variogram is calculated for. |  |
| attribute | String | The attribute the experimental variogram is calculated for. |  |
| data_variance | Number | The variance of the source data, often used as the expected sill of the variogram. | ✅ |
| variogram_type | String | The type of calculation performed (e.g., variogram, semi-variogram, covariance, correlogram). |  |
| distance_unit | unit-length | Distance unit. |  |
| attribute_unit | unit | Attribute unit |  |
| directions | experimental-variogram | A data-table defining the parameters for each variogram direction. | ✅ |
| lags | experimental-variogram | A data-table containing the calculated values for each lag bin. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

