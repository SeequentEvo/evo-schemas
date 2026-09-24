### volumetric-model-meshes (v1.0.0)
A surface closing the model where the source data was absent, so geometrically part of the model hull but not a real contact. Arises where a scalar field is undefined over part of the extent; a categorical model represents absent data as a category of its own instead.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| parts | Array[[reversible-index](../elements/reversible-index-1.0.0.md)] | A list of parts and whether they are reversed. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| material_key | String | Key of the entry in 'materials' that describes how this surface should be presented. A surface carries a single material, so a surface that separates two differently presented regions takes its appearance from that one entry. | [⬆️](../objects/volumetric-model-meshes-1.0.0-surfaces-vmm_isosurface-vmm_embedded_surface.md) |
| surface_type | String | Identifies this surface as the edge of the region where data was available. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

