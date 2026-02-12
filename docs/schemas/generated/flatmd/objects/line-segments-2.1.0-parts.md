### line-segments (v2.1.0)
A structure defining chunks the line collection is composed of.
Attributes are associated with each chunk.

| Property | Type | Description | Flags |
|---|---|---|---|
| attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attribute data. | [⬆️](../components/attribute-list-property-1.2.0.md) |
| chunks | [index-array-2](../elements/index-array-2-1.0.1.md) | A list of chunks of segments.
A chunk consists of consecutive segments, defined by the index of the first segment and the number of segments.
Chunks do not have to include all segments, and chunks can overlap.
Columns: offset, count |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

