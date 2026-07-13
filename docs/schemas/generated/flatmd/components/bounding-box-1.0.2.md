### bounding-box (v1.0.2)
Defines the geographic bounds of the dataset as an axis-aligned box. Each min_*/max_* pair gives the extent along the corresponding axis of the object's coordinate_reference_system (min_x/max_x is the first axis, min_y/max_y the second, min_z/max_z the third). The x, y, z labels denote the CRS axes in order.

| Property | Type | Description | Flags |
|---|---|---|---|
| min_x | Number | Minimum value along the first axis (x) of the object's coordinate reference system. | ✅ |
| max_x | Number | Maximum value along the first axis (x) of the object's coordinate reference system. | ✅ |
| min_y | Number | Minimum value along the second axis (y) of the object's coordinate reference system. | ✅ |
| max_y | Number | Maximum value along the second axis (y) of the object's coordinate reference system. | ✅ |
| min_z | Number | Minimum value along the third axis (z) of the object's coordinate reference system. | ✅ |
| max_z | Number | Maximum value along the third axis (z) of the object's coordinate reference system. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

