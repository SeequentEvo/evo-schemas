### triangle-mesh (v2.2.0)
A structure defining edge chunks of the mesh.

| Property | Type | Description | Flags |
|---|---|---|---|
| attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attribute data. | [⬆️](../components/attribute-list-property-1.2.0.md) |
| chunks | [index-array-2](../elements/index-array-2-1.0.1.md) | A tuple defining the first index and the length of a chunk.
The chunk refers to a segment of the edges array.
Chunks do not have to include all edges, and chunks can overlap.
Columns: offset, count | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

