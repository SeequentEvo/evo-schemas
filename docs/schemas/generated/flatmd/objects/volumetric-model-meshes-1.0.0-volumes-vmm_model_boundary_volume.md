### volumetric-model-meshes (v1.0.0)
The volume whose hull is the boundary of the model extent. A model has at most one, referenced by the model's 'boundary_volume'. Its hull may include inner shells, which enclose interior voids that lie outside the model.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| parts | Array[[reversible-index](../elements/reversible-index-1.0.0.md)] | A list of parts and whether they are reversed. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| material_key | String | Key of the entry in 'materials' that describes how this volume should be presented. | [⬆️](../objects/volumetric-model-meshes-1.0.0-volumes-vmm_iso_volume-vmm_embedded_volume.md) |
| volume_type | String | Identifies this volume as the extent of the model. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

