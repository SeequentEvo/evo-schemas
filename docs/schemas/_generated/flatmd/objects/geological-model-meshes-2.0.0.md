### geological-model-meshes (v2.0.0)
A collection of geological volumes and surfaces.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | ⬆️ ✅ |
| uuid | base-object-properties | Identifier of the object. | ⬆️ ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | ⬆️ |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | ⬆️ |
| tags | Object | Key-value pairs of user-defined metadata | ⬆️ |
| bounding_box | bounding-box | Bounding box of the spatial data. | ⬆️ ✅ |
| coordinate_reference_system | crs | Coordinate system of the spatial data | ⬆️ ✅ |
| schema | String |  | ✅ |
| folders | Array[geological-model-meshes] | A recursive list of folders containing indices into the volume and surface lists. | ✅ |
| triangle_geometry | geological-model-meshes | The embedded mesh, defining vertices, triangles and parts. | ✅ |
| materials | Array[material] | Materials used by this mesh collection. |  |
| volumes | Array[geological-model-meshes] | A list of embedded volumes. Each volume consists of a number of parts. | ✅ |
| volume_attributes | one-of-attribute | Attributes associated with each volume. The attribute tables have one row per volume. |  |
| surfaces | Array[geological-model-meshes] | A list of embedded surfaces. Each surface consists of a number of parts. | ✅ |
| surface_attributes | one-of-attribute | Attributes associated with each surface. The attribute tables have one row per surface. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

