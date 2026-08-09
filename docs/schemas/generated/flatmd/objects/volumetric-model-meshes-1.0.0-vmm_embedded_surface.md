### volumetric-model-meshes (v1.0.0)

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| parts | Array[[reversible-index](../elements/reversible-index-1.0.0.md)] | A list of parts and whether they are reversed. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| material_key | String | Key of the entry in 'materials' that describes how this surface should be presented. |  |
| surface_type | String | Kind of surface. The set of values is closed in this version of the schema and may be extended in a later minor version; a consumer that encounters a value it does not recognise should treat it as 'Generic' rather than rejecting the surface. |  |
| bound | Number | The scalar value the surface was extracted at, in the model's 'bounds_unit'. Present for a surface extracted at a threshold; absent otherwise, such as for a model extent face or a category boundary. |  |
| categories | Array[Integer] | Keys into 'category_lookup' identifying the categories the surface separates, ordered so that the triangle normals point from 'categories[0]' towards 'categories[1]'. Two entries for a contact between two categories, where the first is the category behind the surface and the second is the category in front of it. One entry for a category against unassigned or out-of-model space, where the normals point away from that category. The front of a triangle is the side from which its three vertices appear in counter-clockwise order, which is the side its normal points towards; a part referenced with 'reversed' set to true has its front and back swapped. |  |
| boundary_face | String | For a surface lying on the boundary of the model extent, which face of the extent it lies on, named by the axis and direction that face points along. The axes are those of the extent itself, so for a rotated extent they are the rotated axes rather than those of the coordinate reference system. For example 'NegativeX' is the face at the extent's minimum X, whose outward normal points along negative X. Absent on a boundary surface that spans more than one face, or that the producer cannot attribute to a single face. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

