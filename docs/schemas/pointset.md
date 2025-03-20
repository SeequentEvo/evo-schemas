import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/pointset-1.3.0.md';

# pointset

<SchemaUri uri="schema/objects/pointset/1.3.0/pointset.schema.json" />

The pointset object captures a set of points in space and their associated attributes. This object is widely used in earth sciences for various applications such as geological mapping, geostatistical analysis, and environmental monitoring.

A pointset can represent different types of spatial data, including:
* Sampling locations for mineral exploration
* Monitoring stations for environmental studies
* Observation points for geological surveys

Each point in the pointset is defined by its spatial coordinates and can have multiple associated attributes, such as:
* Mineral grade
* Contaminant concentration
* Temperature

## Locations

To define a pointset, the object requires a `locations` property.

This property has two sub-properties

* `coordinates` - an array property with the coordinates (xyz) of each point.
* An optional [attribute list.](../understanding-schemas/understanding-attributes.md)


See also:

There are two derived schema for storing specific data at the locations.

- For a pointset with lineation measurements, see [lineations-data-pointset](lineations-data-pointset.md).
- For a pointset with planar orientation measurements, see [planar-data-pointset](planar-data-pointset.md).

## Properties

<FlatProperties />

::mermaid[_generated/uml/pointset-1.3.0.mmd]
