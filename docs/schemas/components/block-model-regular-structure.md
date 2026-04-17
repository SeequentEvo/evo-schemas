import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/block-model-regular-structure-1.0.0.md';

# block-model-regular-structure

<SchemaUri uri="schema/components/block-model-regular-structure/1.0.0/block-model-regular-structure.schema.json" />

The `block-model-regular-structure` component defines the structure of a regular (non-subblocked) block model.
All blocks have the same dimensions, arranged in a uniform grid. This is the simplest block model structure
and is appropriate when uniform resolution is sufficient — for example, when block sizes are chosen based
on selective mining unit dimensions or when the orebody geometry does not require variable resolution.

**Used by:** block-model.

**See also:** [block-model-flexible-structure](block-model-flexible-structure.md), [block-model-fully-subblocked-structure](block-model-fully-subblocked-structure.md), [block-model-variable-octree-structure](block-model-variable-octree-structure.md) (subblocked alternatives).

## Properties

<FlatProperties />
