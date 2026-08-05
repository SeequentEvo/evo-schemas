### volumetric-model-meshes (v1.0.0)

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| parts | Array[[reversible-index](../elements/reversible-index-1.0.0.md)] | A list of parts and whether they are reversed. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| material_key | String | Key of the entry in 'materials' that describes how this volume should be presented. |  |
| volume_type | String | Kind of volume. Consumers that do not recognise a value should treat it as 'Generic'. |  |
| lower_bound | Number | Inclusive lower bound of the scalar range the volume encloses, in the model's 'bounds_unit'. Absent if the volume is unbounded below. |  |
| upper_bound | Number | Exclusive upper bound of the scalar range the volume encloses, in the model's 'bounds_unit'. Absent if the volume is unbounded above. |  |
| categories | Array[Integer] | Keys into 'category_lookup' identifying the categories the volume encloses. More than one entry means several source categories have been merged into a single domain. Unordered. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

