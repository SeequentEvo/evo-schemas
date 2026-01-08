### unstructured-grid-geometry (v1.1.0)
This component describes a set of vertices, indices and cell information.

| Property | Type | Description | Flags |
|---|---|---|---|
| vertices | [unstructured-grid-geometry](../components/unstructured-grid-geometry-1.1.0-vertices.md) | Vertex coordinates. Columns: x, y, z. | ✅ |
| cells | [unstructured-grid-geometry](../components/unstructured-grid-geometry-1.1.0-cells.md) | Cell descriptions which consists of an array of triples. The first item in the triple represents the shape, second item is an offset to the indices array and the third item is the number of vertices for the shape. Columns: shape, offset, num_vertices. | ✅ |
| indices | [index-array-1](../elements/index-array-1-1.0.1.md) | 0-based indices into the vertices. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

