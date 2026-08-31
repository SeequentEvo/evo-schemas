import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/block-model-attribute-group-1.0.0.md';

# block-model-attribute-group

<SchemaUri uri="schema/components/block-model-attribute-group/1.0.0/block-model-attribute-group.schema.json" />

A block-model-attribute-group defines metadata for a logical column group in a block model. Groups can form a hierarchy using `parent_group_uuid`; attributes join a group through their `block_model_group_uuid`. Groups without a `parent_group_uuid` are root groups.


**See also:** [block-model-attribute](block-model-attribute.md) (block-model attribute metadata).

## Constraints

The Block Model API enforces additional constraints which aren't represented in the schema. The key constraints are:
* Each groups `parent_group_uuid` and each attribute's `block_model_group_uuid` must reference a declared group.
* Parent group references must not form a cycle.

## Properties

<FlatProperties />