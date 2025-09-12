### bool-time-series (v1.1.0)
An attribute that describes a bool time series.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the attribute | ⬆️ ✅ |
| key | String | An identifier of the attribute, used to keep track of the attribute when it is renamed.
The identifier must be unique within an attribute list. | ⬆️ ✅ |
| attribute_type | String | Type of the attribute. | ⬆️ ✅ |
| attribute_description | attribute-description | The attribute description record. | ⬆️ |
| attribute_type | String |  | ✅ |
| num_time_steps | Integer | Number of time steps. | ✅ |
| time_step | time-step-attribute | Time step attribute component. | ✅ |
| values | bool-array-md | The values of the series where 'num_time_steps' is the width of the array. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

