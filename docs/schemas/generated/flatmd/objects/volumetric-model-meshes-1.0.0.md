### volumetric-model-meshes (v1.0.0)
A mesh-based volumetric model: a collection of surfaces and volumes composed from the parts of a single shared triangulated mesh. Because every surface and volume references parts of the same mesh, adjacent volumes are conformal and share their bounding geometry exactly. Typical uses are isosurfacing output such as grade shells and the volumes between them, and categorical domain models.

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
| triangle_geometry | [volumetric-model-meshes](../objects/volumetric-model-meshes-1.0.0-triangle_geometry.md) | The embedded mesh, defining the vertices, triangles and parts that all surfaces and volumes are composed from. | ✅ |
| surfaces | Array[[volumetric-model-meshes](../objects/volumetric-model-meshes-1.0.0-vmm_embedded_surface.md)] | A list of embedded surfaces, each composed of a number of parts. May be empty. | ✅ |
| surface_attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attributes associated with each surface. The attribute tables have one row per surface. |  |
| volumes | Array[[volumetric-model-meshes](../objects/volumetric-model-meshes-1.0.0-vmm_embedded_volume.md)] | A list of embedded volumes, each composed of a number of parts that together form a closed hull. May be empty. | ✅ |
| volume_attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attributes associated with each volume. The attribute tables have one row per volume. |  |
| bounds_unit | [unit](../elements/unit-1.0.1.md) | Unit of measure of the 'bound' value of every surface and the 'lower_bound' and 'upper_bound' values of every volume in this model. All bounds are expressed in this unit, as they are all derived from a single scalar field. Absent if the unit is unknown or the bounds are dimensionless. |  |
| category_lookup | [lookup-table](../elements/lookup-table-1.0.1.md) | Lookup table resolving the integer keys used by the 'categories' property of surfaces and the 'category' property of volumes to their names. The keys are those of the categorical attribute the model was built from, carried through unchanged. Must be present if any surface specifies 'categories' or any volume specifies 'category'. |  |
| materials | Array[[material](../components/material-1.0.1.md)] | Materials used by the surfaces and volumes of this model, referenced by 'material_key'. Keys must be unique within the array. |  |
| folders | Array[[volumetric-model-meshes](../objects/volumetric-model-meshes-1.0.0-vmm_folder.md)] | A recursive list of folders organising the model for presentation. Folders hold indices into 'surfaces' and 'volumes', not geometry, and need not cover every surface or volume. |  |
| isosurfaces | Array[Integer] | Indices into 'surfaces' of the surfaces that were extracted at a scalar threshold, ordered by threshold ascending. A derived index: if present it must list every surface with 'surface_type' of 'Isosurface' and no others, so that a consumer that ignores it and filters 'surfaces' itself obtains the same set. |  |
| boundary_surfaces | Array[Integer] | Indices into 'surfaces' of the surfaces that lie on the boundary of the model extent, being those with a 'surface_type' of 'ModelBoundary' or 'NoData'. A derived index: if present it must list every such surface and no others. Together these surfaces cover the model hull, which is the same geometry as 'boundary_volume'. |  |
| volumes_below | Array[Integer] | Indices into 'volumes' of the volumes that are bounded above only, ordered by 'upper_bound' ascending. A derived index: if present it must list every volume that specifies 'upper_bound' and not 'lower_bound', and no others. |  |
| volumes_between | Array[Integer] | Indices into 'volumes' of the volumes that are bounded both above and below, ordered by 'lower_bound' ascending. A derived index: if present it must list every volume that specifies both 'lower_bound' and 'upper_bound', and no others. |  |
| volumes_above | Array[Integer] | Indices into 'volumes' of the volumes that are bounded below only, ordered by 'lower_bound' ascending. A derived index: if present it must list every volume that specifies 'lower_bound' and not 'upper_bound', and no others. |  |
| boundary_volume | Integer | Index into 'volumes' of the volume that is the closed hull of the model extent. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

