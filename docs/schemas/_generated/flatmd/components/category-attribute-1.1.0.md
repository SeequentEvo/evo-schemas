### category-attribute (v1.1.0)
An attribute that describes a category.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the attribute | ⬆️ ✅ |
| key | String | An identifier of the attribute, used to keep track of the attribute when it is renamed.
The identifier must be unique within an attribute list. | ⬆️ ✅ |
| attribute_type | String | Type of the attribute. | ⬆️ ✅ |
| attribute_description | category-attribute-description | The attribute description record. | ⬆️ |
| table | lookup-table | Lookup table associated with the attributes. | ⬆️ ✅ |
| values | integer-array-1 | The index values of the attributes. | ⬆️ ✅ |
| attribute_type | String |  | ✅ |
| nan_description | nan-categorical | Describes the values used to designate not-a-number. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

