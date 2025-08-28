import CheckIcon from '@mui/icons-material/Check';
import Chip from '@mui/material/Chip';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/line-segments-2.2.0.md';

# line-segments

<Chip color="info" icon={<CheckIcon />} label="Supported" />
<SchemaUri uri="schema/objects/line-segments/2.2.0/line-segments.schema.json" />

A collection of lines composed of straight segments.
Often the collection will be broken down into connected linear structures called *strings* or *polylines*.  The [Parts](../understanding-schemas/understanding-parts.md) mechanism can be used for capturing the details of that additional structure.

## `segments`

The vertices and indices of the segments.

`vertices` : Table of vertex coordinates. Columns: x, y, z.

 - An optional [attribute list](../understanding-schemas/understanding-attributes.md) can be associated with the vertices.

`indices` : Table of 0-based indices into vertices. Each pair is a segment. Columns: n0, n1.

- An optional [attribute list](../understanding-schemas/understanding-attributes.md) can be associated with the segments.

If the segments are organised into *strings* or *polylines* then adjacent segments will usually share an index.  In those cases the indices are also often sequential.  An example of the indices for four connected segments might be `[(0, 1), (1, 2), (2, 3), (3, 4)]`. If the segments formed a closed loop then your last pair could be `(3, 0)` indicating that the last vertex in the segment chain was the same as the first.

## `parts`

A structure defining chunks A structure defining chunks of segments in the line collection. Parts allow us to combine individual segments into longer elements.

`chunks` -
Each chunk is a tuple defining the first index and the length of a chunk of vertices. The chunk refers to a contiguous piece of the segment array. Chunks do not have to include all segments, and chunks can overlap. Columns: offset, count

`attributes` — the parts can have an optional [attribute list](../understanding-schemas/understanding-attributes.md) in the standard manner.

## Properties

<FlatProperties />

::mermaid[_generated/uml/line-segments-2.2.0.mmd]
