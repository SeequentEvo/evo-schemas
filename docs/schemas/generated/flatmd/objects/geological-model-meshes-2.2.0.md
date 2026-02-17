### geological-model-meshes (v2.2.0)
A collection of geological volumes and surfaces.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/base-object-properties-1.1.0.md) ✅ |
| uuid | [base-object-properties](../components/base-object-properties-1.1.0-uuid.md) | Identifier of the object. | [⬆️](../components/base-object-properties-1.1.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/base-object-properties-1.1.0.md) |
| extensions | Object | Extended properties that may be associated to the object, but not specified in the schema | [⬆️](../components/base-object-properties-1.1.0.md) |
| tags | Object | Key-value pairs of user-defined metadata | [⬆️](../components/base-object-properties-1.1.0.md) |
| lineage | [lineage](../components/lineage-1.0.0.md) | Information about the history of the object | [⬆️](../components/base-object-properties-1.1.0.md) |
| bounding_box | [bounding-box](../components/bounding-box-1.0.1.md) | Bounding box of the spatial data. | [⬆️](../components/base-spatial-data-properties-1.1.0.md) ✅ |
| coordinate_reference_system | [crs](../components/crs-1.0.1.md) | Coordinate system of the spatial data | [⬆️](../components/base-spatial-data-properties-1.1.0.md) ✅ |
| schema | String |  | ✅ |
| folders | Array[[geological-model-meshes](../objects/geological-model-meshes-2.2.0-folder.md)] | A recursive list of folders containing indices into the volume and surface lists. | ✅ |
| triangle_geometry | [geological-model-meshes](../objects/geological-model-meshes-2.2.0-triangle_geometry.md) | The embedded mesh, defining vertices, triangles and parts. | ✅ |
| materials | Array[[material](../components/material-1.0.1.md)] | Materials used by this mesh collection. |  |
| volumes | Array[[geological-model-meshes](../objects/geological-model-meshes-2.2.0-gm_embedded_volume.md)] | A list of embedded volumes. Each volume consists of a number of parts. | ✅ |
| volume_attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attributes associated with each volume. The attribute tables have one row per volume. |  |
| surfaces | Array[[geological-model-meshes](../objects/geological-model-meshes-2.2.0-gm_embedded_surface.md)] | A list of embedded surfaces. Each surface consists of a number of parts. | ✅ |
| surface_attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attributes associated with each surface. The attribute tables have one row per surface. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

