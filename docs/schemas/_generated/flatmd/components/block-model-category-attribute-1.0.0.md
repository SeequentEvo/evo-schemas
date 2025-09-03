### block-model-category-attribute (v1.0.0)
A block model category/string attribute stored by the Block Model Service.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the attribute | ⬆️ ✅ |
| key | String | An identifier of the attribute, used to keep track of the attribute when it is renamed.
The identifier must be unique within an attribute list. | ⬆️ ✅ |
| attribute_type | String | Type of the attribute. | ⬆️ ✅ |
| attribute_description | category-attribute-description | The attribute description record. | ⬆️ |
| attribute_type | String | The data type of the attribute as stored in the Block Model Service. | ✅ |
| block_model_column_uuid | String | The unique ID of the attribute on the block model. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

