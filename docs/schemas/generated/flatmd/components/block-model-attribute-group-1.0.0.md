### block-model-attribute-group (v1.0.0)
Column group metadata

| Property | Type | Description | Flags |
|---|---|---|---|
| group_uuid | String | Unique identifier for the group. |  |
| is_hidden | Boolean | When true, the group's direct member columns are excluded from wildcard queries (unless include_hidden is set in the query). |  |
| missing_column_policy | String | Defines the update behaviour, for all columns in the group, for columns that do not have a value provided. |  |
| parent_group_uuid | [block-model-attribute-group](../components/block-model-attribute-group-1.0.0-parent_group_uuid.md) | Identifier of the parent group. Null means the group is a 'top-level' group. |  |
| tags | Object | Publisher-supplied free-form metadata for the group, as a JSON object. Keys must be 1-100 chars and cannot contain leading whitespace or dot, or the characters `/ \ : > < \| ? " *`; keys are unique case-insensitively. Values may be any JSON-compatible type. A single `tags` object serialised as UTF-8 JSON must be at most 10 KiB. |  |
| title | String | 'Human-readable label for the group, unique across the parent group, or across top-level groups if no parent. They must be 1-100 chars and cannot contain leading whitespace or dot, or the characters `/ \ : > < \| ? " *`. Must not contain the qualified title separator `▸`.' |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

