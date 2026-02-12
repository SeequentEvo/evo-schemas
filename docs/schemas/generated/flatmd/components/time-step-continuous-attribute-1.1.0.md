### time-step-continuous-attribute (v1.1.0)
A component that represents elapsed time (sec, min, hours, months, etc.) since a start time.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the attribute | [⬆️](../components/base-attribute-1.0.0.md) |
| key | String | An identifier of the attribute, used to keep track of the attribute when it is renamed.
The identifier must be unique within an attribute list. | [⬆️](../components/base-attribute-1.0.0.md) |
| attribute_type | String | Type of the attribute. | [⬆️](../components/base-attribute-1.0.0.md) |
| attribute_description | [attribute-description](../components/attribute-description-1.0.1.md) | The attribute description record. | [⬆️](../components/base-continuous-attribute-1.0.0.md) |
| attribute_type | String |  |  |
| values | [float-array-1](../elements/float-array-1-1.0.1.md) | The values of the attributes. |  |
| unit | [unit-time](../elements/unit-time-1.0.1-unit_categories.md) | Time step unit. |  |
| start_time | String | start time |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

