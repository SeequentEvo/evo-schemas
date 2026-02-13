import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/segments-1.2.0.md';

# segments

<SchemaUri uri="schema/components/segments/1.2.0/segments.schema.json" />

The `segments` component defines a set of line segments by pairs of vertex indices.

* `vertices` — An array of 3D coordinates.
* `indices` — An index array of vertex pairs (start, end), each defining a segment. Indices are 0-based.

## Properties

<FlatProperties />
