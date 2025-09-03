### vector-attribute (v1.0.0)
An attribute containing an N-dimensional vector.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the attribute | ⬆️ ✅ |
| key | String | An identifier of the attribute, used to keep track of the attribute when it is renamed.
The identifier must be unique within an attribute list. | ⬆️ ✅ |
| attribute_type | String | Type of the attribute. | ⬆️ ✅ |
| attribute_description | attribute-description | The attribute description record. | ⬆️ |
| attribute_type | String |  | ✅ |
| nan_description | nan-continuous | Describes the values used to designate not-a-number. | ✅ |
| values | float-array-md | The vector array, where each row is a vector. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

