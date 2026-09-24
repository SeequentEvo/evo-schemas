### volumetric-model-meshes (v1.0.0)
A surface extracted from a scalar field at a single threshold, such as a grade shell. Triangle normals point towards increasing values of the field, so the region above the threshold lies in front of the surface and the region below it lies behind.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| parts | Array[[reversible-index](../elements/reversible-index-1.0.0.md)] | A list of parts and whether they are reversed. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| material_key | String | Key of the entry in 'materials' that describes how this surface should be presented. A surface carries a single material, so a surface that separates two differently presented regions takes its appearance from that one entry. | [⬆️](../objects/volumetric-model-meshes-1.0.0-surfaces-vmm_isosurface-vmm_embedded_surface.md) |
| surface_type | String | Identifies this surface as an isosurface. | ✅ |
| bound | Number | The scalar value the surface was extracted at, in the model's 'bounds_unit'. A surface is extracted at a single threshold, so it carries one value rather than a range. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

