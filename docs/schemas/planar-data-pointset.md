import CheckIcon from '@mui/icons-material/Check';
import Chip from '@mui/material/Chip';
import Grid from '@mui/material/Grid';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/planar-data-pointset-1.3.0.md';

<Grid container>
# planar-data-pointset
<Chip color="info" icon={<CheckIcon />} label="Supported" style={{margin: '0.75em'}} />
</Grid>
<SchemaUri uri="schema/objects/planar-data-pointset/1.3.0/planar-data-pointset.schema.json" />

The `planar-data-pointset` schema is a variant of the generic [pointset](pointset.md) schema. See that schema for general information.

It enhances the base pointset by allowing planar data to be associated with each point.

## Planar data

The planar data is specified using two angles and a boolean flag.  The angles are the same as the first two used for specifying [rotations](components/rotation.md).

 * *dip_azimuth* angle.  The azimuth of the dip direction.
 * *dip* angle. The dip below horizontal.
 * *polarity*.  A boolean flag, `True` indicates positive polarity.

## Locations

To define a pointset, the object requires a `locations` property.

This property has four sub-properties, two for the planar data and two from the generic pointset schema.

* `plane_orientations` - a two column float array with the *dip_azimuth* and *dip* angles.
* `plane_polarity` - a boolean array with the *polarity* flags.
* `coordinates` - an array property with the coordinates (xyz) of each point.
* An optional [attribute list.](../understanding-schemas/understanding-attributes.md)

See also:
- The base [pointset](pointset.md) documentation.
- For a pointset with lineation measurements, see [lineations-data-pointset](lineations-data-pointset.md).

## Properties

<FlatProperties />

::mermaid[_generated/uml/planar-data-pointset-1.3.0.mmd]
