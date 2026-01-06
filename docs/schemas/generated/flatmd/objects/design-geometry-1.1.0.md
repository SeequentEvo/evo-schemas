### design-geometry (v1.1.0)
2D/3D Geometry

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/base-object-properties-1.1.0.md) ✅ |
| uuid | [base-object-properties](../components/base-object-properties-1.1.0-uuid.md) | Identifier of the object. | [⬆️](../components/base-object-properties-1.1.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/base-object-properties-1.1.0.md) |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | [⬆️](../components/base-object-properties-1.1.0.md) |
| tags | Object | Key-value pairs of user-defined metadata | [⬆️](../components/base-object-properties-1.1.0.md) |
| lineage | [lineage](../components/lineage-1.0.0.md) | Information about the history of the object | [⬆️](../components/base-object-properties-1.1.0.md) |
| bounding_box | [bounding-box](../components/bounding-box-1.0.1.md) | Bounding box of the spatial data. | [⬆️](../components/base-spatial-data-properties-1.1.0.md) ✅ |
| coordinate_reference_system | [crs](../components/crs-1.0.1.md) | Coordinate system of the spatial data | [⬆️](../components/base-spatial-data-properties-1.1.0.md) ✅ |
| schema | String |  | ✅ |
| kind | String | The kind of geometry. | ✅ |
| distance_unit | [unit-length](../elements/unit-length-1.0.1-unit_categories.md) | Distance unit. |  |
| materials | Array[[material](../components/material-1.0.1.md)] | Materials for this geometry. | ✅ |
| vertices_2d | [vertices-2d](../components/vertices-2d-1.0.1.md) | Vertex coordinates in 2D space. |  |
| vertices_3d | [vertices-3d](../components/vertices-3d-1.0.1.md) | Vertex coordinates in 3D space. |  |
| lines_2d | [lines-2d-indices](../components/lines-2d-indices-1.0.1.md) | 2D line indices. |  |
| lines_3d | [lines-3d-indices](../components/lines-3d-indices-1.0.1.md) | 3D line indices. |  |
| parts | Array[[geometry-part](../components/geometry-part-1.0.1.md)] | List of geometry parts. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

