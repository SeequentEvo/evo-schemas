### block-model-regular-structure (v1.0.0)
The structure of a regular, non-subblocked block model.

| Property | Type | Description | Flags |
|---|---|---|---|
| model_type | String | The model geometry type. | ✅ |
| n_blocks | Array[Integer] | The number of blocks in the model. [nx, ny, nz] | ✅ |
| block_size | Array[Number] | The size of each block in the model. [dx, dy, dz] | ✅ |
| origin | Array[Number] | The coordinates of the model origin. [x, y, z] | ✅ |
| rotation | [rotation](../components/rotation-1.1.0.md) | The orientation of the model. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

