import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/triangle-mesh-2.2.0.md';

<OverlineWithVersion title="Geoscience Objects" version="2.2.0" badge="supported" />

# triangle-mesh

<SchemaUri uri="schema/objects/triangle-mesh/2.2.0/triangle-mesh.schema.json" />

A discretization of a 3D domain into triangles. The triangles are defined by triplets of indices into a vertex list. Optionally, parts and edges can be specified.

## `triangles`
The vertices and triangle indices of the mesh.

`vertices` : Table of vertex coordinates. Columns: x, y, z.

- An optional [attribute list](../understanding-schemas/understanding-attributes.md) can be associated with the vertices.

`indices` : Table of 0-based indices into vertices. Each triple is a triangle. Columns: n0, n1, n2.

- An optional [attribute list](../understanding-schemas/understanding-attributes.md) can be associated with the triangles.

## `parts`

A structure defining triangle chunks the mesh is composed of. [Parts](../understanding-schemas/understanding-parts.md) allow us to share common sections of one volume or surface with another. Parts are made up from chunks of triangle indices.

`chunks`
Each chunk is a tuple defining the first index and the length of a chunk of vertices. If triangle_indices is defined, the chunk refers to a segment of the triangle_indices array, Otherwise, the chunk refers to a segment of the triangles array. Chunks do not have to include all triangles, and chunks can overlap. Columns: offset, count.

`attributes` — the parts can have an optional [attribute list](../understanding-schemas/understanding-attributes.md) in the standard manner.

`triangle_indices`
An optional index array into the triangle indices set. This is used to define chunks if the mesh triangle indices do not contain contiguous chunks.

### edges
An optional structure defining edges and edge chunks of the mesh. An optional attribute can be associated with each edge.

`indices` : Edges defined by tuples of indices into the vertex list. Columns: start, end.

`parts` : An optional structure defining edge [chunks](#parts-1) the mesh is composed of.

#### `parts`

`chunks`: Tuple defining the first index and the length of a chunk of edges. The chunk refers to a segment of the edges array. Chunks do not have to include all edges, and chunks can overlap. Columns: offset, count

## Properties

<FlatProperties />

::mermaid[_generated/uml/triangle-mesh-2.2.0.mmd]
