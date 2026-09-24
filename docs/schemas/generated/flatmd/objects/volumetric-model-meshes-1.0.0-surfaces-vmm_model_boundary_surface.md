### volumetric-model-meshes (v1.0.0)
A surface lying on the boundary of the model extent, introduced where the model was clipped rather than where the data changes.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| parts | Array[[reversible-index](../elements/reversible-index-1.0.0.md)] | A list of parts and whether they are reversed. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| material_key | String | Key of the entry in 'materials' that describes how this surface should be presented. A surface carries a single material, so a surface that separates two differently presented regions takes its appearance from that one entry. | [⬆️](../objects/volumetric-model-meshes-1.0.0-surfaces-vmm_isosurface-vmm_embedded_surface.md) |
| surface_type | String | Identifies this surface as part of the model extent boundary. | ✅ |
| boundary_face | String | Which face of the model extent this surface lies on, named by the axis and direction its outward normal points along. The axes are those of the extent: rotated by the model's 'extent_rotation' if present, otherwise those of the coordinate reference system. For example 'NegativeX' is the face at the extent's minimum X, whose outward normal points along negative X. Absent if the surface spans more than one face or the producer cannot attribute it to a single face. |  |
| category | Integer | Key into 'category_lookup' identifying the category whose region this surface closes, for a categorical model clipped by its extent. Absent if the surface closes no single category, as in a model without categories. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

