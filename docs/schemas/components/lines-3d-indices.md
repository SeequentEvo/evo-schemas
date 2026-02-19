import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/lines-3d-indices-1.0.1.md';

# lines-3d-indices

<SchemaUri uri="schema/components/lines-3d-indices/1.0.1/lines-3d-indices.schema.json" />

The `lines-3d-indices` component describes endpoints for 3D line segments. Each entry has two columns:

* `start` — Index into the 3D vertices for the line start.
* `end` — Index into the 3D vertices for the line end.

Unlike 2D lines, curved segments in 3D are represented via a 2D segment with a transform, or via a BREP.

**Used by:** [design-geometry](../objects/design-geometry.md).

**See also:** [lines-2d-indices](lines-2d-indices.md) (2D counterpart).

## Properties

<FlatProperties />
