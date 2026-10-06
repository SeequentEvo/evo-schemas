### volumetric-model-meshes (v1.0.0)
A volume enclosing the region occupied by one category of a categorical model, such as a lithological domain.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| parts | Array[[reversible-index](../elements/reversible-index-1.0.0.md)] | A list of parts and whether they are reversed. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| material_key | String | Key of the entry in 'materials' that describes how this volume should be presented. | [⬆️](../objects/volumetric-model-meshes-1.0.0-volumes-vmm_iso_volume-vmm_embedded_volume.md) |
| volume_type | String | Identifies this volume as the region occupied by a single category. | ✅ |
| category | Integer | Key into 'category_lookup' identifying the category the volume encloses. A volume encloses exactly one category, so a domain that groups several source categories is published as a single category with its own key and name. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

