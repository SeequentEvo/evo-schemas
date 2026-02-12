### geological-sections (v1.1.0)
A collection of cross-sections made up from multiple polygons/polylines.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/base-object-properties-1.1.0.md) |
| uuid | [base-object-properties](../components/base-object-properties-1.1.0-uuid.md) | Identifier of the object. | [⬆️](../components/base-object-properties-1.1.0.md) |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/base-object-properties-1.1.0.md) |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | [⬆️](../components/base-object-properties-1.1.0.md) |
| tags | Object | Key-value pairs of user-defined metadata | [⬆️](../components/base-object-properties-1.1.0.md) |
| lineage | [lineage](../components/lineage-1.0.0.md) | Information about the history of the object | [⬆️](../components/base-object-properties-1.1.0.md) |
| bounding_box | [bounding-box](../components/bounding-box-1.0.1.md) | Bounding box of the spatial data. | [⬆️](../components/base-spatial-data-properties-1.1.0.md) |
| coordinate_reference_system | [crs](../components/crs-1.0.1.md) | Coordinate system of the spatial data | [⬆️](../components/base-spatial-data-properties-1.1.0.md) |
| schema | String |  |  |
| folders | Array[[geological-sections](../objects/geological-sections-1.1.0-folder.md)] | A recursive list of folders containing indices into the sections list. |  |
| line_geometry | [embedded-line-geometry](../components/embedded-line-geometry-1.0.0.md) | The embedded line geometry, defining vertices, segments and parts. |  |
| materials | Array[[material](../components/material-1.0.1.md)] | Materials used by this planar geology collection. |  |
| sections | Array[[geological-sections](../objects/geological-sections-1.1.0-section.md)] | A list of cross-sections. |  |
| section_attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attributes associated with each section. The attribute tables have one row per section. |  |
| volumes | Array[[geological-sections](../objects/geological-sections-1.1.0-gm_embedded_polygon_volume.md)] | A list of embedded polygon volumes. Each volume consists of a number of parts. |  |
| volume_attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attributes associated with each polygon volume. The attribute tables have one row per volume. |  |
| surfaces | Array[[geological-sections](../objects/geological-sections-1.1.0-gm_embedded_polyline_surface.md)] | A list of embedded polyline surfaces. Each surface consists of a number of parts. |  |
| surface_attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attributes associated with each polyline surface. The attribute tables have one row per surface. |  |
| layer_order | Array[String] | An optional list of layers used when stacking volumes on top of each other. The first entry represents the topmost layer, while the last entry represents the bottommost. Layers are occluded sequentially from top to bottom. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

