import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/elements/coordinates-3d-1.0.1.md';

# coordinates-3d

<SchemaUri uri="schema/elements/coordinates-3d/1.0.1/coordinates-3d.schema.json" />

A single point in 3D space, defined by `x`, `y`, and `z` coordinates. Used for fixed spatial positions such as survey station locations and electromagnetic channel positions.

The labels `x`, `y`, and `z` denote the first, second, and third axes of the object's
`coordinate_reference_system` — they do **not** imply easting, northing, and elevation. See
[Coordinate reference systems and axis order](../../understanding-schemas/coordinate-reference-systems.md).

**Used by:** [survey-attribute-definition](../components/survey-attribute-definition.md), [frequency-domain-electromagnetic-channel](../components/frequency-domain-electromagnetic-channel.md), [time-domain-electromagnetic-channel](../components/time-domain-electromagnetic-channel.md).

## Properties

<FlatProperties />
