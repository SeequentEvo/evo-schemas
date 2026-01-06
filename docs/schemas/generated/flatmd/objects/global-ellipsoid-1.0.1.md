### global-ellipsoid (v1.0.1)
Global ellipsoid.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/base-object-properties-1.0.1.md) ✅ |
| uuid | [base-object-properties](../components/base-object-properties-1.0.1-uuid.md) | Identifier of the object. | [⬆️](../components/base-object-properties-1.0.1.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/base-object-properties-1.0.1.md) |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | [⬆️](../components/base-object-properties-1.0.1.md) |
| tags | Object | Key-value pairs of user-defined metadata | [⬆️](../components/base-object-properties-1.0.1.md) |
| bounding_box | [bounding-box](../components/bounding-box-1.0.1.md) | Bounding box of the spatial data. | [⬆️](../components/base-spatial-data-properties-1.0.1.md) ✅ |
| coordinate_reference_system | [crs](../components/crs-1.0.1.md) | Coordinate system of the spatial data | [⬆️](../components/base-spatial-data-properties-1.0.1.md) ✅ |
| ellipsoid_ranges | [ellipsoid](../components/ellipsoid-1.0.1-ellipsoid_ranges.md) | An ellipsoid as defined by three lengths, for the major, semi-major and minor axes rotated in space as defined by the rotation. | [⬆️](../components/ellipsoid-1.0.1.md) ✅ |
| rotation | [rotation](../components/rotation-1.0.1.md) | Rotation of the ellipsoid | [⬆️](../components/ellipsoid-1.0.1.md) ✅ |
| schema | String |  | ✅ |
| domain | String | The domain the ellipsoid is modelled for | ✅ |
| attribute | String | The attribute the ellipsoid is modelled for | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

