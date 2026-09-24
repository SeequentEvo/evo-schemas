### volumetric-model-meshes (v1.0.0)
A volume that is part of the model but is none of the other kinds. Intended for closed regions carried alongside a model for context, such as an imported solid, where no scalar range, category or extent applies. A consumer can display it but can draw no inference from it, so prefer a more specific kind wherever one fits.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| parts | Array[[reversible-index](../elements/reversible-index-1.0.0.md)] | A list of parts and whether they are reversed. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| material_key | String | Key of the entry in 'materials' that describes how this volume should be presented. | [⬆️](../objects/volumetric-model-meshes-1.0.0-volumes-vmm_iso_volume-vmm_embedded_volume.md) |
| volume_type | String | Identifies this volume as none of the other kinds. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

