### volumetric-model-meshes (v1.0.0)
A band of a scalar field: the region where the field lies between two consecutive thresholds, below the lowest threshold, or above the highest. The iso-volumes of a model partition its extent without overlap, so cumulative volumes, such as everything below a threshold other than the lowest, are not published; a consumer builds them from the bands. At least one of 'lower_bound' and 'upper_bound' must be present, otherwise the volume constrains nothing.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | Name of the object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| description | String | Optional field for adding additional description to uniquely identify this object. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| quality | [mesh-quality](../components/mesh-quality-1.0.1.md) | Mesh quality. | [⬆️](../components/embedded-mesh-object-1.0.0.md) |
| parts | Array[[reversible-index](../elements/reversible-index-1.0.0.md)] | A list of parts and whether they are reversed. | [⬆️](../components/embedded-mesh-object-1.0.0.md) ✅ |
| material_key | String | Key of the entry in 'materials' that describes how this volume should be presented. | [⬆️](../objects/volumetric-model-meshes-1.0.0-volumes-vmm_iso_volume-vmm_embedded_volume.md) |
| volume_type | String | Identifies this volume as the region between two scalar thresholds. | ✅ |
| lower_bound | Number | Inclusive lower bound of the scalar range the volume encloses, in the model's 'bounds_unit'. Absent if the volume is unbounded below. |  |
| upper_bound | Number | Exclusive upper bound of the scalar range the volume encloses, in the model's 'bounds_unit'. Absent if the volume is unbounded above. The range is half-open so that adjacent iso-volumes tile the scalar range without overlap; the threshold itself is the shared bounding surface, which has no volume of its own. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

