### volumetric-model-meshes (v1.0.0)

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| parts | Array[[reversible-index](../elements/reversible-index-1.0.0.md)] | A list of parts and whether they are reversed. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| material_key | String | Key of the entry in 'materials' that describes how this volume should be presented. |  |
| volume_type | String | Kind of volume. The set of values is closed in this version of the schema and may be extended in a later minor version; a consumer that encounters a value it does not recognise should treat it as 'Generic' rather than rejecting the volume. |  |
| lower_bound | Number | Inclusive lower bound of the scalar range the volume encloses, in the model's 'bounds_unit'. Absent if the volume is unbounded below. |  |
| upper_bound | Number | Exclusive upper bound of the scalar range the volume encloses, in the model's 'bounds_unit'. Absent if the volume is unbounded above. |  |
| category | Integer | Key into 'category_lookup' identifying the category the volume encloses. A volume encloses exactly one category; a domain merging several source categories is represented as one category of its own, added to 'category_lookup'. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

