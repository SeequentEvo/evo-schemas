import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/locations-1.0.1.md';

# locations

<SchemaUri uri="schema/components/locations/1.0.1/locations.schema.json" />

The `locations` component represents a set of point coordinates in 3D space. It is used by objects such as
[pointset](../objects/pointset.md) and others that need to define spatial positions.

* `coordinates` — An array of 3D coordinates (x, y, z), stored as a `float-array-3` element.

Attributes can be associated with locations via the optional attribute list (see
[Understanding attributes](../../understanding-schemas/understanding-attributes.md)).

**Used by:** [downhole-collection](../objects/downhole-collection.md), [downhole-intervals](../objects/downhole-intervals.md), [geophysical-records-1d](../objects/geophysical-records-1d.md), [lineations-data-pointset](../objects/lineations-data-pointset.md), [local-ellipsoids](../objects/local-ellipsoids.md), [planar-data-pointset](../objects/planar-data-pointset.md), [pointset](../objects/pointset.md).

## Properties

<FlatProperties />
