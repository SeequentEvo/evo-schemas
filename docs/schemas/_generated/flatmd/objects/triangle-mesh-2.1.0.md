### triangle-mesh (v2.1.0)
A mesh composed of triangles.
The triangles are defined by triplets of indices into a vertex list.
Optionally, parts and edges can be defined.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | ⬆️ ✅ |
| uuid | base-object-properties | Identifier of the object. | ⬆️ ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | ⬆️ |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | ⬆️ |
| tags | Object | Key-value pairs of user-defined metadata | ⬆️ |
| bounding_box | bounding-box | Bounding box of the spatial data. | ⬆️ ✅ |
| coordinate_reference_system | crs | Coordinate system of the spatial data | ⬆️ ✅ |
| triangles | triangles | The vertices and triangle indices of the mesh. | ⬆️ ✅ |
| parts | embedded-triangulated-mesh | A structure defining triangle chunks the mesh is composed of. | ⬆️ |
| schema | String |  | ✅ |
| edges | triangle-mesh | An optional structure defining edges and edge chunks of the mesh. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

