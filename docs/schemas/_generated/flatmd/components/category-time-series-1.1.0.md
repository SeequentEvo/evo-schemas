### category-time-series (v1.1.0)
An attribute that describes a category time series.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the attribute | ⬆️ ✅ |
| key | String | An identifier of the attribute, used to keep track of the attribute when it is renamed.
The identifier must be unique within an attribute list. | ⬆️ ✅ |
| attribute_type | String | Type of the attribute. | ⬆️ ✅ |
| attribute_description | category-attribute-description | The attribute description record. | ⬆️ |
| attribute_type | String |  | ✅ |
| nan_description | nan-categorical | Describes the values used to designate not-a-number. | ✅ |
| num_time_steps | Integer | Number of time steps. | ✅ |
| time_step | time-step-attribute | Time step attribute component. | ✅ |
| values | integer-array-md | The values of the series where 'num_time_steps' is the width of the array. | ✅ |
| table | lookup-table | Lookup table associated with the attributes. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

