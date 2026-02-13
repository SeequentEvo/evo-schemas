import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/embedded-line-geometry-1.0.0.md';

# embedded-line-geometry

<SchemaUri uri="schema/components/embedded-line-geometry/1.0.0/embedded-line-geometry.schema.json" />

The `embedded-line-geometry` component represents a set of polylines composed of straight line segments.

* `vertices` — An array of 3D coordinates defining the polyline vertices.
* `chunks` — Offset and count information defining individual polylines within the vertex array.
* `indices` — Optional connectivity indices.

**See also:** [embedded-triangulated-mesh](embedded-triangulated-mesh.md) (mesh equivalent), [embedded-polyline-object](embedded-polyline-object.md).

**Used by:** [geological-sections](../objects/geological-sections.md).

## Properties

<FlatProperties />
