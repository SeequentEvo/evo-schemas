### category-ensemble (v1.1.0)
Category ensemble.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the attribute | [⬆️](../components/base-attribute-1.0.0.md) ✅ |
| key | String | An identifier of the attribute, used to keep track of the attribute when it is renamed.
The identifier must be unique within an attribute list. | [⬆️](../components/base-attribute-1.0.0.md) ✅ |
| attribute_type | String | Type of the attribute. | [⬆️](../components/base-attribute-1.0.0.md) ✅ |
| attribute_description | [category-attribute-description](../components/category-attribute-description-1.0.1.md) | The attribute description record. | [⬆️](../components/base-category-attribute-1.0.0.md) |
| attribute_type | String |  | ✅ |
| nan_description | [nan-categorical](../components/nan-categorical-1.0.1.md) | Describes the values used to designate not-a-number. | ✅ |
| table | [lookup-table](../elements/lookup-table-1.0.1.md) | Lookup table associated with the attributes. | ✅ |
| values | [integer-array-md](../elements/integer-array-md-1.0.1.md) | The values of the attributes. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

