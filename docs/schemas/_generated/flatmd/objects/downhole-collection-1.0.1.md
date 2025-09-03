### downhole-collection (v1.0.1)
A collection of downhole locations.

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
| type | String | The type of the collection. | ✅ |
| distance_unit | unit-length | Distance unit. |  |
| desurvey | String | The desurvey algorithm. |  |
| location | downhole-collection | The locations of the downholes in the collection. | ✅ |
| collections | Array[downhole-collection] | The collections of data associated with the downhole collection. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

