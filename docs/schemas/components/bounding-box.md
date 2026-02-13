import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/bounding-box-1.0.1.md';

# bounding-box

<SchemaUri uri="schema/components/bounding-box/1.0.1/bounding-box.schema.json" />

The `bounding-box` component defines the geographic extents of a spatial dataset as an axis-aligned box:

* `min_x`, `max_x` — Extents along the X axis.
* `min_y`, `max_y` — Extents along the Y axis.
* `min_z`, `max_z` — Extents along the Z axis.

All six fields are required.

## Properties

<FlatProperties />
