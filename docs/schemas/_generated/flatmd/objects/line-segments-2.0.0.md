### line-segments (v2.0.0)
A collection of lines composed of straight segments.
Optionally, consecutive chunks of segments can be grouped and attributed.

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
| segments | segments | Vertices and segments. | ✅ |
| parts | line-segments | An optional structure defining segment chunks the line collection is composed of. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

