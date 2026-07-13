import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/hole-collars-1.0.0.md';

# hole-collars

<SchemaUri uri="schema/components/hole-collars/1.0.0/hole-collars.schema.json" />

The `hole-collars` component represents the surface locations where drillholes begin. It contains:

* 3D coordinates (x, y, z) of collar locations.
* Depth information for each hole.
* Hole indices and associated attributes.

The `x`, `y`, `z` columns denote the first, second, and third axes of the object's
`coordinate_reference_system` and follow that CRS's declared axis order, not necessarily
easting/northing/elevation. See
[Coordinate reference systems and axis order](../../understanding-schemas/coordinate-reference-systems.md).

This component is used by the [drilling-campaign](../objects/drilling-campaign.md) schema.

**Used by:** [drilling-campaign](../objects/drilling-campaign.md), [downhole-collection](../objects/downhole-collection.md).

**See also:** [hole-chunks](hole-chunks.md), [desurvey-method](desurvey-method.md).

## Properties

<FlatProperties />
