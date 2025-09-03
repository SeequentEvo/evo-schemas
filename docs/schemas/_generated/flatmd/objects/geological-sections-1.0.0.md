### geological-sections (v1.0.0)
A collection of cross-sections made up from multiple polygons/polylines.

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
| folders | Array[geological-sections] | A recursive list of folders containing indices into the sections list. | ✅ |
| line_geometry | embedded-line-geometry | The embedded line geometry, defining vertices, segments and parts. | ✅ |
| materials | Array[material] | Materials used by this planar geology collection. |  |
| sections | Array[geological-sections] | A list of cross-sections. | ✅ |
| section_attributes | one-of-attribute | Attributes associated with each section. The attribute tables have one row per section. |  |
| volumes | Array[geological-sections] | A list of embedded polygon volumes. Each volume consists of a number of parts. | ✅ |
| volume_attributes | one-of-attribute | Attributes associated with each polygon volume. The attribute tables have one row per volume. |  |
| surfaces | Array[geological-sections] | A list of embedded polyline surfaces. Each surface consists of a number of parts. | ✅ |
| surface_attributes | one-of-attribute | Attributes associated with each polyline surface. The attribute tables have one row per surface. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

