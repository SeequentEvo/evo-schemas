### block-model-variable-octree-structure (v1.0.0)
The structure of a variable-octree subblocked model. Subblocking is carried out by repeatedly splitting blocks along each axis, until there are a maximum of n_subblocks_per_parent subblocks. This number can be different per axis.

| Property | Type | Description | Flags |
|---|---|---|---|
| model_type | String | The model geometry type. |  |
| n_parent_blocks | Array[Integer] | The number of parent blocks in the model. [nx, ny, nz] |  |
| parent_block_size | Array[Number] | The size of each parent block in the model. [dx, dy, dz] |  |
| n_subblocks_per_parent | Array[Integer] | The maximum number of subblocks in each parent block in the model in each axis. [nx, ny, nz] |  |
| origin | Array[Number] | The coordinates of the model origin. [x, y, z] |  |
| rotation | [rotation](../components/rotation-1.1.0.md) | The orientation of the model. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

