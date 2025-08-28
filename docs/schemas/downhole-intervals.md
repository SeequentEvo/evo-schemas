import CheckIcon from '@mui/icons-material/Check';
import Chip from '@mui/material/Chip';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/downhole-intervals-1.3.0.md';

# downhole-intervals

<Chip color="info" icon={<CheckIcon />} label="Supported" />
<SchemaUri uri="schema/objects/downhole-intervals/1.3.0/downhole-intervals.schema.json" />

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

::mermaid[_generated/uml/downhole-intervals-1.3.0.mmd]
