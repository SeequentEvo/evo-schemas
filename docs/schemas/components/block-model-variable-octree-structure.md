import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/block-model-variable-octree-structure-1.0.0.md';

# block-model-variable-octree-structure

<SchemaUri uri="schema/components/block-model-variable-octree-structure/1.0.0/block-model-variable-octree-structure.schema.json" />

The `block-model-variable-octree-structure` component defines the structure of a variable-octree subblocked model.

Subblocking repeatedly splits blocks along each axis until there are a maximum of `n_subblocks_per_parent`
subblocks. The number of splits can differ per axis, allowing anisotropic refinement.

## Properties

<FlatProperties />
