### geological-sections (v1.0.0)

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the section. | ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. |  |
| origin | Array[Number] | The coordinates of the section origin. [x, y, z] | ✅ |
| rotation | rotation | The orientation of the section. | ✅ |
| volumes | geological-sections | The consecutive group of volumes in the volumes list. |  |
| surfaces | geological-sections | The consecutive group of surfaces in the surface list. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

