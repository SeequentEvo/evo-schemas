### downhole-intervals (v1.3.0)
A description for downhole intervals.

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
| attributes | one-of-attribute | Attribute data. | ⬆️ |
| schema | String |  | ✅ |
| is_composited | Boolean | Is composited? | ✅ |
| start | locations | Start locations. | ✅ |
| end | locations | End locations. | ✅ |
| mid_points | locations | Mid-point locations. | ✅ |
| from_to | from-to | From-to description. | ✅ |
| hole_id | category-data | Hole IDs. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

