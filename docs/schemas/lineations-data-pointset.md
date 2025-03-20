import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/lineations-data-pointset-1.3.0.md';

# lineations-data-pointset

<SchemaUri uri="schema/objects/lineations-data-pointset/1.3.0/lineations-data-pointset.schema.json" />

The `lineations-data-pointset` schema is a variant of the generic [pointset](pointset.md) schema. See that schema for general information.

It enhances the base pointset by allowing lineation data to be associated with each point.

## Lineation data

 The lineation data is specified using two angles.

 * *trend* angle. The azimuth of the lineation direction.
 * *plunge* angle. The angle below the horizontal that the lineation plunges at.

The angles are similar to the first two used for specifying [rotations](components/rotation.md).  The *dip_azimuth* and *dip* pair correspond to the *trend* and plunge of the down-dip direction (itself a lineation) on the rotated xy plane.

## Locations

To define a pointset, the object requires a `locations` property.

This property has three sub-properties, one with the lineation data and two from the generic pointset schema.

* `lineations` - a two column float array with the *trend* and *plunge* angles.
* `coordinates` - an array property with the coordinates (xyz) of each point.
* An optional [attribute list.](../understanding-schemas/understanding-attributes.md)

See also:
- The base [pointset](pointset.md) documentation.
- For a pointset with planar orientation measurements, see [planar-data-pointset](planar-data-pointset.md).

## Properties

<FlatProperties />

::mermaid[_generated/uml/lineations-data-pointset-1.3.0.mmd]
