### regular-3d-grid (v1.3.0)
A 3D regular grid (all cells are equal size).

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | ⬆️ ✅ |
| uuid | base-object-properties | Identifier of the object. | ⬆️ ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | ⬆️ |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | ⬆️ |
| tags | Object | Key-value pairs of user-defined metadata | ⬆️ |
| lineage | lineage | Information about the history of the object | ⬆️ |
| bounding_box | bounding-box | Bounding box of the spatial data. | ⬆️ ✅ |
| coordinate_reference_system | crs | Coordinate system of the spatial data | ⬆️ ✅ |
| schema | String |  | ✅ |
| origin | Array[Number] | The coordinates of the origin [x,y,z] | ✅ |
| size | Array[Integer] | The size of the entire grid. [grid_size_x, grid_size_y, grid_size_z] | ✅ |
| cell_size | Array[Number] | The size of each cell in the grid. [cell_size_x, cell_size_y, cell_size_z] | ✅ |
| rotation | rotation | Orientation of the grid. |  |
| cell_attributes | one-of-attribute | Attributes associated with the cells. |  |
| vertex_attributes | one-of-attribute | Attributes associated with the vertices. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

