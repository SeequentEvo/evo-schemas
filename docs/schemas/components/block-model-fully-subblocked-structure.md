import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/block-model-fully-subblocked-structure-1.0.0.md';

# block-model-fully-subblocked-structure

<SchemaUri uri="schema/components/block-model-fully-subblocked-structure/1.0.0/block-model-fully-subblocked-structure.schema.json" />

The `block-model-fully-subblocked-structure` component defines the structure of a fully-subblocked block model.

Each parent block is either split into exactly the grid defined by `n_subblocks_per_parent`, or left whole.
There is no partial subblocking — a block is either fully subdivided or not subdivided at all.

## Properties

<FlatProperties />
