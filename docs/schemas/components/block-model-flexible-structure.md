import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/block-model-flexible-structure-1.0.0.md';

# block-model-flexible-structure

<SchemaUri uri="schema/components/block-model-flexible-structure/1.0.0/block-model-flexible-structure.schema.json" />

The `block-model-flexible-structure` component defines the structure of a flexibly-subblocked block model.

Subblocking divides each parent block into a fixed grid defined by `n_subblocks_per_parent`, then recombines
subblocks into larger chunks. The resulting subblocks can have different sizes within the same parent block,
but must remain cuboid and completely fill the parent block.

## Properties

<FlatProperties />
