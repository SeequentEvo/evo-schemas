### volumetric-model-meshes (v1.0.0)

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| parts | Array[[reversible-index](../elements/reversible-index-1.0.0.md)] | A list of parts and whether they are reversed. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| material_key | String | Key of the entry in 'materials' that describes how this surface should be presented. |  |
| surface_type | String | Kind of surface. Consumers that do not recognise a value should treat it as 'Generic'. |  |
| lower_bound | Number | The lowest scalar value the surface was extracted at, in the model's 'bounds_unit'. Equal to 'upper_bound' for a surface extracted at a single threshold. |  |
| upper_bound | Number | The highest scalar value the surface was extracted at, in the model's 'bounds_unit'. Equal to 'lower_bound' for a surface extracted at a single threshold. |  |
| categories | Array[Integer] | Keys into 'category_lookup' identifying the categories the surface separates. Two entries for a contact between two categories, where the first is the category in front of the triangles as wound and the second is the category behind. One entry for a category against unassigned or out-of-model space. |  |
| boundary_face | String | For a surface lying on the boundary of the model extent, which face of the extent it lies on. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

