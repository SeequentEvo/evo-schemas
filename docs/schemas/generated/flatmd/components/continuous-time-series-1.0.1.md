### continuous-time-series (v1.0.1)
An attribute that describes a continuous time series.

| Property | Type | Description | Flags |
|---|---|---|---|
| key | String | The key |  |
| attribute_type | String | Type of the attribute. |  |
| nan_description | [nan-continuous](../components/nan-continuous-1.0.1.md) | Describes the values used to designate not-a-number. |  |
| num_time_steps | Integer | Number of time steps. |  |
| time_step | [time-step-attribute](../components/time-step-attribute-1.0.1.md) | Time step attribute component. |  |
| values | [float-array-md](../elements/float-array-md-1.0.1.md) | The values of the series where 'num_time_steps' is the width of the array. |  |
| attribute_description | [attribute-description](../components/attribute-description-1.0.1.md) | The attribute description record. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

