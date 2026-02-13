import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/hole-collars-1.0.0.md';

# hole-collars

<SchemaUri uri="schema/components/hole-collars/1.0.0/hole-collars.schema.json" />

The `hole-collars` component represents the surface locations where drillholes begin. It contains:

* 3D coordinates (x, y, z) of collar locations.
* Depth information for each hole.
* Hole indices and associated attributes.

This component is used by the [drilling-campaign](../drilling-campaign.md) schema.

**See also:** [hole-chunks](hole-chunks.md), [desurvey-method](desurvey-method.md).

## Properties

<FlatProperties />
