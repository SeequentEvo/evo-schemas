### geological-sections (v1.1.0)
A closed polyline defining the external ring of the polygon.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | ⬆️ ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | ⬆️ |
| parts | Array[reversible-index] | A list of parts and whether they are reversed. | ⬆️ ✅ |
| material_key | String | Unique identifier of the material. |  |
| feature | String | Kind of feature. | ✅ |
| layer | String | Optional identifier for the layer containing the polygon. Polygons in the same layer should not overlap. Polygons in different layers can overlap. Layer precidence may matters s follow a layer precidence where defined |  |
| internal_rings | Array[embedded-polyline-object] | Optional field representing internal rings (holes) inside the volume. When multiple inner_ring's exist they can touch but should not overlap. There may or may not be another volume whose external ring overlaps an inner ring |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

