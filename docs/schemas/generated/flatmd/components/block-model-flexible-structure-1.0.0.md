### block-model-flexible-structure (v1.0.0)
The structure of a flexibly-subblocked block model. Subblocking is carried out by dividing each parent block into a fixed grid of subblocks defined by n_subblocks_per_parent, before recombining the subblocks into larger chunks. The resulting subblocks can have different sizes within the same parent block, but must remain cuboid and completely fill the parent block.

| Property | Type | Description | Flags |
|---|---|---|---|
| model_type | String | The model geometry type. | ✅ |
| n_parent_blocks | Array[Integer] | The number of parent blocks in the model. [nx, ny, nz] | ✅ |
| parent_block_size | Array[Number] | The size of each parent block in the model. [dx, dy, dz] | ✅ |
| n_subblocks_per_parent | Array[Integer] | The number of blocks per axis in the underlying subblock grid in each parent block in the model. [nx, ny, nz] | ✅ |
| origin | Array[Number] | The coordinates of the model origin. [x, y, z] | ✅ |
| rotation | [rotation](../components/rotation-1.1.0.md) | The orientation of the model. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

