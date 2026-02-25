import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/block-model-fully-subblocked-structure-1.0.0.md';

# block-model-fully-subblocked-structure

<SchemaUri uri="schema/components/block-model-fully-subblocked-structure/1.0.0/block-model-fully-subblocked-structure.schema.json" />

The `block-model-fully-subblocked-structure` component defines the structure of a fully-subblocked block model.

Each parent block is either split into exactly the grid defined by `n_subblocks_per_parent`, or left whole.
There is no partial subblocking — a block is either fully subdivided or not subdivided at all. This
all-or-nothing approach is simpler to implement than flexible subblocking and is appropriate when uniform
subdivision within refined areas is acceptable.

**Used by:** block-model.

**See also:** [block-model-regular-structure](block-model-regular-structure.md), [block-model-flexible-structure](block-model-flexible-structure.md), [block-model-variable-octree-structure](block-model-variable-octree-structure.md) (alternative structures).

## Properties

<FlatProperties />
