### global-ellipsoid (v1.2.0)
Global ellipsoid.

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
| ellipsoid_ranges | ellipsoid | An ellipsoid as defined by three lengths, for the major, semi-major and minor axes rotated in space as defined by the rotation. | ⬆️ ✅ |
| rotation | rotation | Rotation of the ellipsoid | ⬆️ ✅ |
| schema | String |  | ✅ |
| domain | String | The domain the ellipsoid is modelled for | ✅ |
| attribute | String | The attribute the ellipsoid is modelled for | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

