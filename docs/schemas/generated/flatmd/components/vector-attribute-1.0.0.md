### vector-attribute (v1.0.0)
An attribute containing an N-dimensional vector.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the attribute | [⬆️](../components/base-attribute-1.0.0.md) ✅ |
| key | String | An identifier of the attribute, used to keep track of the attribute when it is renamed.
The identifier must be unique within an attribute list. | [⬆️](../components/base-attribute-1.0.0.md) ✅ |
| attribute_type | String | Type of the attribute. | [⬆️](../components/base-attribute-1.0.0.md) ✅ |
| attribute_description | [attribute-description](../components/attribute-description-1.0.1.md) | The attribute description record. | [⬆️](../components/base-continuous-attribute-1.0.0.md) |
| attribute_type | String |  | ✅ |
| nan_description | [nan-continuous](../components/nan-continuous-1.0.1.md) | Describes the values used to designate not-a-number. | ✅ |
| values | [float-array-md](../elements/float-array-md-1.0.1.md) | The vector array, where each row is a vector. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

