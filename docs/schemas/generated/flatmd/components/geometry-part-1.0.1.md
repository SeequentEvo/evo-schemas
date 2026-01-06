### geometry-part (v1.0.1)
This component describes a geometry part.

| Property | Type | Description | Flags |
|---|---|---|---|
| key | String | Unique identifier of the geometry part. | ✅ |
| name | String | Name. | ✅ |
| data_source | String | Data source. |  |
| feature | [geometry-part](../components/geometry-part-1.0.1-feature.md) | Geometry part feature. | ✅ |
| transform | Array[Number] | 4x4 transformation matrix flattened in row-major order. |  |
| bounding_box | [bounding-box](../components/bounding-box-1.0.1.md) | Bounding box of the geometry part. | ✅ |
| layer | String | Geometry part layer. |  |
| color | [color](../elements/color-1.0.1.md) | Geometry part color. |  |
| geometry | [geometry-part](../components/geometry-part-1.0.1-geometry.md) | Another part in the geometry or a geometry composite. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

