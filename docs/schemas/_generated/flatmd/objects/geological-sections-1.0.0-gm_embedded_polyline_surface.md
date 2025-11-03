### geological-sections (v1.0.0)

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | ⬆️ ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | ⬆️ |
| parts | Array[reversible-index] | A list of parts and whether they are reversed. | ⬆️ ✅ |
| layer | String | Identifier for the layer containing the polyline. Polylines in the same layer should not overlap. Polylines in different layers can overlap. | ✅ |
| material_key | String | Unique identifier of the material. |  |
| feature | String | Kind of feature. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

