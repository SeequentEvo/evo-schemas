### category-attribute (v1.1.0)
An attribute that describes a category.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the attribute | [⬆️](../components/base-attribute-1.0.0.md) ✅ |
| key | String | An identifier of the attribute, used to keep track of the attribute when it is renamed.
The identifier must be unique within an attribute list. | [⬆️](../components/base-attribute-1.0.0.md) ✅ |
| attribute_type | String | Type of the attribute. | [⬆️](../components/base-attribute-1.0.0.md) ✅ |
| attribute_description | [category-attribute-description](../components/category-attribute-description-1.0.1.md) | The attribute description record. | [⬆️](../components/base-category-attribute-1.0.0.md) |
| table | [lookup-table](../elements/lookup-table-1.0.1.md) | Lookup table associated with the attributes. | [⬆️](../components/category-data-1.0.1.md) ✅ |
| values | [integer-array-1](../elements/integer-array-1-1.0.1.md) | The index values of the attributes. | [⬆️](../components/category-data-1.0.1.md) ✅ |
| attribute_type | String |  | ✅ |
| nan_description | [nan-categorical](../components/nan-categorical-1.0.1.md) | Describes the values used to designate not-a-number. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

