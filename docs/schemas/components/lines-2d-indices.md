---
seoTitle: lines-2d-indices Component for Evo Schemas | Seequent Developer
description: Review the lines 2d indices component schema for Geoscience Objects, supporting consistent data structures and reliable Seequent Evo workflows.
---

import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/lines-2d-indices-1.0.1.md';

# lines-2d-indices

<SchemaUri uri="schema/components/lines-2d-indices/1.0.1/lines-2d-indices.schema.json" />

The `lines-2d-indices` component describes endpoints for 2D line segments. Each entry has three columns:

* `start` — Index into the 2D vertices for the line start.
* `end` — Index into the 2D vertices for the line end.
* `arcCenter` — The counter-clockwise signed distance from the line centre to the arc edge, enabling curved segments.

**Used by:** [design-geometry](../objects/design-geometry.md).

**See also:** [lines-3d-indices](lines-3d-indices.md) (3D counterpart).

## Properties

<FlatProperties />
