### category-time-series (v1.0.1)
An attribute that describes a category time series.

| Property | Type | Description | Flags |
|---|---|---|---|
| key | String | The key | ✅ |
| attribute_type | String | Type of the attribute. | ✅ |
| nan_description | nan-categorical | Describes the values used to designate not-a-number. | ✅ |
| num_time_steps | Integer | Number of time steps. | ✅ |
| time_step | time-step-attribute | Time step attribute component. | ✅ |
| values | integer-array-md | The values of the series where 'num_time_steps' is the width of the array. | ✅ |
| table | lookup-table | Lookup table associated with the attributes. | ✅ |
| attribute_description | category-attribute-description | The attribute description record. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

