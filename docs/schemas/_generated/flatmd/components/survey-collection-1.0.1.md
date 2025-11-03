### survey-collection (v1.0.1)
A survey collection containing a collection number, type, and attributes.

| Property | Type | Description | Flags |
|---|---|---|---|
| identifier | String | The collection identifier. In line-based surveys, this will typically be the line number. | ✅ |
| date | String | The date the survey collection was conducted. |  |
| version | Integer | The version of the survey collection. |  |
| group | Integer | The group of the survey collection. |  |
| type | String | Survey collection type. | ✅ |
| locations | survey-collection | Survey collection locations. |  |
| survey_attributes | Array[survey-attribute] | List of survey attributes. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

