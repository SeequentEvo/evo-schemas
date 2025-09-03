### design-geometry (v1.0.1)
2D/3D Geometry

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
| kind | String | The kind of geometry. | ✅ |
| distance_unit | unit-length | Distance unit. |  |
| materials | Array[material] | Materials for this geometry. | ✅ |
| vertices_2d | vertices-2d | Vertex coordinates in 2D space. |  |
| vertices_3d | vertices-3d | Vertex coordinates in 3D space. |  |
| lines_2d | lines-2d-indices | 2D line indices. |  |
| lines_3d | lines-3d-indices | 3D line indices. |  |
| parts | Array[geometry-part] | List of geometry parts. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

