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
| surfaces | Array[[volumetric-model-meshes](../objects/volumetric-model-meshes-1.0.0-surfaces.md)] | A list of embedded surfaces, each composed of a number of parts. Every surface declares its kind in 'surface_type', which selects the data it carries. May be empty, but a model with no surfaces and no volumes carries no content. | ✅ |
| surface_attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attributes associated with each surface. The attribute tables have one row per surface. |  |
| volumes | Array[[volumetric-model-meshes](../objects/volumetric-model-meshes-1.0.0-volumes.md)] | A list of embedded volumes, each composed of a number of parts that together form a closed hull. Every volume declares its kind in 'volume_type', which selects the data it carries. May be empty, but a model with no surfaces and no volumes carries no content. | ✅ |
| volume_attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attributes associated with each volume. The attribute tables have one row per volume. |  |
| bounds_unit | [unit](../elements/unit-1.0.1.md) | Unit of measure of the 'bound' value of every isosurface and the 'lower_bound' and 'upper_bound' values of every iso-volume in this model. All bounds are expressed in this unit, as they are all derived from a single scalar field. Absent if the unit is unknown or the bounds are dimensionless. |  |
| bounds_attribute | String | Name of the scalar attribute the bounds are measured on, such as 'Au'. Absent if the model has no bounds or the name is unknown. |  |
| category_lookup | [lookup-table](../elements/lookup-table-1.0.1.md) | Lookup table resolving the integer keys used by the 'categories' property of category boundary surfaces, the 'category' property of category regions, and the 'category' property of model boundary surfaces to their names. Must be present if any surface or volume specifies a category. |  |
| category_attribute | String | Name of the categorical attribute the model was built from, such as 'Lithology', whose keys 'category_lookup' resolves. Absent if the model has no categories or the name is unknown. |  |
| materials | Array[[material](../components/material-1.0.1.md)] | Materials used by the surfaces and volumes of this model, referenced by 'material_key'. Keys must be unique within the array. |  |
| folders | Array[[volumetric-model-meshes](../objects/volumetric-model-meshes-1.0.0-vmm_folder.md)] | A recursive list of folders organising the model for presentation. Folders hold indices into 'surfaces' and 'volumes', not geometry, and need not cover every surface or volume. |  |
| extent_rotation | [rotation](../components/rotation-1.1.0.md) | Orientation of the axes of the model extent, for a model built on a rotated grid. Only 'boundary_face' is interpreted against these axes; vertices remain in the coordinate reference system. Absent if the extent is aligned with the axes of the coordinate reference system. |  |
| boundary_volume | Integer | Index into 'volumes' of the volume whose hull is the boundary of the model extent. That volume has a 'volume_type' of 'ModelBoundary'. Absent if the model does not include its extent as a volume. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

