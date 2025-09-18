### time-step-continuous-attribute (v1.1.0)
A component that represents elapsed time (sec, min, hours, months, etc.) since a start time.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the attribute | ⬆️ ✅ |
| key | String | An identifier of the attribute, used to keep track of the attribute when it is renamed.
The identifier must be unique within an attribute list. | ⬆️ ✅ |
| attribute_type | String | Type of the attribute. | ⬆️ ✅ |
| attribute_description | attribute-description | The attribute description record. | ⬆️ |
| attribute_type | String |  | ✅ |
| values | float-array-1 | The values of the attributes. | ✅ |
| unit | unit-time | Time step unit. | ✅ |
| start_time | String | start time |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

