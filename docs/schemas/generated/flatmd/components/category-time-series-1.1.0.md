### category-time-series (v1.1.0)
An attribute that describes a category time series.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the attribute | [⬆️](../components/base-attribute-1.0.0.md) |
| key | String | An identifier of the attribute, used to keep track of the attribute when it is renamed.
The identifier must be unique within an attribute list. | [⬆️](../components/base-attribute-1.0.0.md) |
| attribute_type | String | Type of the attribute. | [⬆️](../components/base-attribute-1.0.0.md) |
| attribute_description | [category-attribute-description](../components/category-attribute-description-1.0.1.md) | The attribute description record. | [⬆️](../components/base-category-attribute-1.0.0.md) |
| attribute_type | String |  |  |
| nan_description | [nan-categorical](../components/nan-categorical-1.0.1.md) | Describes the values used to designate not-a-number. |  |
| num_time_steps | Integer | Number of time steps. |  |
| time_step | [time-step-attribute](../components/time-step-attribute-1.1.0.md) | Time step attribute component. |  |
| values | [integer-array-md](../elements/integer-array-md-1.0.1.md) | The values of the series where 'num_time_steps' is the width of the array. |  |
| table | [lookup-table](../elements/lookup-table-1.0.1.md) | Lookup table associated with the attributes. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

