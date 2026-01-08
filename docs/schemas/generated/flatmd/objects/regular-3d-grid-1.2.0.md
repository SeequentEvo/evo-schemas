### regular-3d-grid (v1.2.0)
A 3D regular grid (all cells are equal size).

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/base-object-properties-1.0.1.md) ✅ |
| uuid | [base-object-properties](../components/base-object-properties-1.0.1-uuid.md) | Identifier of the object. | [⬆️](../components/base-object-properties-1.0.1.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/base-object-properties-1.0.1.md) |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | [⬆️](../components/base-object-properties-1.0.1.md) |
| tags | Object | Key-value pairs of user-defined metadata | [⬆️](../components/base-object-properties-1.0.1.md) |
| bounding_box | [bounding-box](../components/bounding-box-1.0.1.md) | Bounding box of the spatial data. | [⬆️](../components/base-spatial-data-properties-1.0.1.md) ✅ |
| coordinate_reference_system | [crs](../components/crs-1.0.1.md) | Coordinate system of the spatial data | [⬆️](../components/base-spatial-data-properties-1.0.1.md) ✅ |
| schema | String |  | ✅ |
| origin | Array[Number] | The coordinates of the origin [x,y,z] | ✅ |
| size | Array[Integer] | The size of the entire grid. [grid_size_x, grid_size_y, grid_size_z] | ✅ |
| cell_size | Array[Number] | The size of each cell in the grid. [cell_size_x, cell_size_y, cell_size_z] | ✅ |
| rotation | [rotation](../components/rotation-1.1.0.md) | Orientation of the grid. |  |
| cell_attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attributes associated with the cells. |  |
| vertex_attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attributes associated with the vertices. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

