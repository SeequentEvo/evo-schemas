### volumetric-model-meshes (v1.0.0)
A surface that is part of the model but is none of the other kinds. Intended for meshes carried alongside a model for context, such as a topography or an imported wireframe, where no threshold, category or extent face applies. A consumer can display it but can draw no inference from it, so prefer a more specific kind wherever one fits.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| parts | Array[[reversible-index](../elements/reversible-index-1.0.0.md)] | A list of parts and whether they are reversed. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| material_key | String | Key of the entry in 'materials' that describes how this surface should be presented. A surface carries a single material, so a surface that separates two differently presented regions takes its appearance from that one entry. | [⬆️](../objects/volumetric-model-meshes-1.0.0-surfaces-vmm_isosurface-vmm_embedded_surface.md) |
| surface_type | String | Identifies this surface as none of the other kinds. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

