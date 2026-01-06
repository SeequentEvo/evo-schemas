### survey-attribute-definition (v1.0.1)
Common properties for attributes in survey data.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the attribute. | ✅ |
| key | String | An identifier of the attribute. Must be unique within a list of attributes. | ✅ |
| offset | [coordinates-3d](../elements/coordinates-3d-1.0.0.md) | Offset of attribute measurements relative to the point of reference. |  |
| significant_digits | Integer | Significant digits. |  |
| description | [attribute-description](../components/attribute-description-1.0.1.md) | Attribute-specific properties for survey data. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

