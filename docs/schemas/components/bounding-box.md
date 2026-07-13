import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/bounding-box-1.0.1.md';

# bounding-box

<SchemaUri uri="schema/components/bounding-box/1.0.1/bounding-box.schema.json" />

The `bounding-box` component defines the geographic extents of a spatial dataset as an axis-aligned box:

* `min_x`, `max_x` — Extents along the first CRS axis.
* `min_y`, `max_y` — Extents along the second CRS axis.
* `min_z`, `max_z` — Extents along the third CRS axis.

All six fields are required.

Each `min_*`/`max_*` pair gives the extent along the corresponding **CRS axis** (`*_x` → first axis,
`*_y` → second axis, `*_z` → third axis), not necessarily easting/northing/elevation. The order,
direction, and meaning of the axes are defined by the object's `coordinate_reference_system`. See
[Coordinate reference systems and axis order](../../understanding-schemas/coordinate-reference-systems.md).

**Used by:** [base-spatial-data-properties](base-spatial-data-properties.md), [geometry-part](geometry-part.md).

## Properties

<FlatProperties />
