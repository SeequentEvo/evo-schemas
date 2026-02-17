### triangle-mesh (v2.0.0)
A mesh composed of triangles.
The triangles are defined by triplets of indices into a vertex list.
Optionally, parts and edges can be defined.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/base-object-properties-1.0.1.md) ✅ |
| uuid | [base-object-properties](../components/base-object-properties-1.0.1-uuid.md) | Identifier of the object. | [⬆️](../components/base-object-properties-1.0.1.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/base-object-properties-1.0.1.md) |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | [⬆️](../components/base-object-properties-1.0.1.md) |
| tags | Object | Key-value pairs of user-defined metadata | [⬆️](../components/base-object-properties-1.0.1.md) |
| bounding_box | [bounding-box](../components/bounding-box-1.0.1.md) | Bounding box of the spatial data. | [⬆️](../components/base-spatial-data-properties-1.0.1.md) ✅ |
| coordinate_reference_system | [crs](../components/crs-1.0.1.md) | Coordinate system of the spatial data | [⬆️](../components/base-spatial-data-properties-1.0.1.md) ✅ |
| triangles | [triangles](../components/triangles-1.1.0.md) | The vertices and triangle indices of the mesh. | [⬆️](../components/embedded-triangulated-mesh-2.0.0.md) ✅ |
| parts | [embedded-triangulated-mesh](../components/embedded-triangulated-mesh-2.0.0-parts.md) | A structure defining triangle chunks the mesh is composed of. | [⬆️](../components/embedded-triangulated-mesh-2.0.0.md) |
| schema | String |  | ✅ |
| edges | [triangle-mesh](../objects/triangle-mesh-2.0.0-edges.md) | An optional structure defining edges and edge chunks of the mesh. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

