### volumetric-model-meshes (v1.0.0)
A contact between two categories, or between one category and unassigned space inside the model extent. Where a category meets the boundary of the extent, the surface is a model boundary surface carrying that category instead.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| parts | Array[[reversible-index](../elements/reversible-index-1.0.0.md)] | A list of parts and whether they are reversed. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| material_key | String | Key of the entry in 'materials' that describes how this surface should be presented. A surface carries a single material, so a surface that separates two differently presented regions takes its appearance from that one entry. | [⬆️](../objects/volumetric-model-meshes-1.0.0-surfaces-vmm_isosurface-vmm_embedded_surface.md) |
| surface_type | String | Identifies this surface as a contact between categories. | ✅ |
| categories | Array[Integer] | Keys into 'category_lookup' identifying the categories the surface separates, ordered so that the triangle normals point from 'categories[0]' towards 'categories[1]'. Two entries for a contact between two categories, where the first is the category behind the surface and the second is the category in front of it. One entry for a category against unassigned space inside the model extent, where the normals point away from that category. The front of a triangle is the side from which its three vertices appear in counter-clockwise order, which is the side its normal points towards; a part referenced with 'reversed' set to true has its front and back swapped. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

