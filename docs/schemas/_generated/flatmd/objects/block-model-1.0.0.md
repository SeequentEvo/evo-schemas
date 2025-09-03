### block-model (v1.0.0)
A reference to a block model stored in the Block Model Service.

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
| block_model_uuid | String | The unique ID of the block model in the Block Model Service. | ✅ |
| block_model_version_uuid | String | The unique ID of this version of the block model in the Block Model Service. |  |
| geometry | block-model | The geometry (including subblocking parameters, if applicable) of the block model. | ✅ |
| attributes | Array[block-model] | The attributes found on this version of the block model. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

