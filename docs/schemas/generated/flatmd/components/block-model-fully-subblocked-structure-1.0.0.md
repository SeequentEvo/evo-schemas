### block-model-fully-subblocked-structure (v1.0.0)
The structure of a fully-subblocked block model. Subblocking is carried out by either splitting a parent block into exactly the grid defined by n_subblocks_per_parent, or leaving it whole.

| Property | Type | Description | Flags |
|---|---|---|---|
| model_type | String | The model geometry type. |  |
| n_parent_blocks | Array[Integer] | The number of parent blocks in the model. [nx, ny, nz] |  |
| parent_block_size | Array[Number] | The size of each parent block in the model. [dx, dy, dz] |  |
| n_subblocks_per_parent | Array[Integer] | The number of subblocks in each subblocked parent block in the model in each axis. [nx, ny, nz] |  |
| origin | Array[Number] | The coordinates of the model origin. [x, y, z] |  |
| rotation | [rotation](../components/rotation-1.1.0.md) | The orientation of the model. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

