### tensor-3d-grid (v1.2.0)
A 3D tensor grid (cells may have different sizes).

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
| origin | Array[Number] | The coordinates of the origin [x,y,z] | ✅ |
| size | Array[Integer] | Number of cells in each direction. [grid_size_x, grid_size_y, grid_size_z] | ✅ |
| grid_cells_3d | tensor-3d-grid | Grid cell sizes along the axes | ✅ |
| rotation | rotation | Orientation of the grid. |  |
| cell_attributes | one-of-attribute | Attributes associated with the cells. |  |
| vertex_attributes | one-of-attribute | Attributes associated with the vertices. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

