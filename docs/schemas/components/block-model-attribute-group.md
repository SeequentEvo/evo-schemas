import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/block-model-attribute-group-1.0.0.md';

# block-model-attribute-group

<SchemaUri uri="schema/components/block-model-attribute-group/1.0.0/block-model-attribute-group.schema.json" />

A block-model attribute group defines metadata for a logical grouping of block-model attributes. Groups can
form a hierarchy using `parent_group_uuid`; attributes join a group through their `block_model_group_uuid`.
A group whose `parent_group_uuid` is null or absent is a top-level group.

Groups are declared on the block-model object in its `groups` array. Membership is not recorded in the group
itself -- it is expressed by the pointer held on each attribute -- so a group can be declared before any
attribute references it.

The Block Model Service stores attribute values column-wise, so its API refers to an attribute as a *column*.
The two terms denote the same thing: `missing_column_policy` governs the attributes that are members of the
group, and `block_model_column_uuid` on [block-model-attribute](block-model-attribute.md) identifies the
column backing that attribute.

**Used by:** block-model.

**See also:** [block-model-attribute](block-model-attribute.md) (the attributes that groups organise).

## Constraints

The Block Model API enforces additional constraints which aren't represented in the schema. The key constraints are:

* Each group's `parent_group_uuid`, and each attribute's `block_model_group_uuid`, must reference a declared group.
* Parent group references must not form a cycle.
* `title` must be unique among sibling groups sharing a parent, and among top-level groups.

## Properties

<FlatProperties />