import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/downhole-intervals-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# downhole-intervals

<SchemaUri uri="schema/objects/downhole-intervals/1.3.0/downhole-intervals.schema.json" />

**Key components:**
- [from-to](../components/from-to.md) — Depth range intervals along drillhole traces
- [category-data](../components/category-data.md) — Lookup table mapping integer keys to category names

**See also:** [drilling-campaign](drilling-campaign.md) (campaign-level), [downhole-collection](downhole-collection.md) (per-hole data).

## Overview

The downhole-intervals object captures the downhole geometry and data once desurveyed and possibly composited into target length intervals. They are represented as a series of lines grouped by hole ID.

Note that a downhole-interval object is a derivative object from the source data. The desurveying process adds a series of assumptions on the locations of each resulting segment. Different desurveying algorithms will provide different geometries.

This object is particularly useful in geological and geostatistical analysis where the spatial distribution of properties along drillholes needs to be quantified and analyzed.

To define the downhole intervals, the object requires:

- A table of start locations for each interval.
- A table of end locations for each interval.
- A table of mid-point locations for each interval (note that the mid-point is not necessarily the average of the start and end points, depending on the desurveying method applied to the source data).
- A pair of values "from-to" that note the start and end depth of the interval down the hole.
- Hole IDs for each interval to group them.

The object can also capture additional context such as whether the intervals are composited.

## Properties

<FlatProperties />

::mermaid[../generated/uml/downhole-intervals-1.3.0.mmd]
