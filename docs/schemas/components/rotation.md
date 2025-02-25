import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../_generated/flatmd/components/rotation-1.1.0.md';

# rotation

<SchemaUri uri="schema/components/rotation/1.1.0/rotation.schema.json" />

Rotation in 3D space described by 3 in-plane rotations, all rotating clockwise about the Z, then X, and finally Z axes. All angles must be positive values, specified in degrees, within the bounds defined for each rotation. 0 degrees in the xy plane (dip azimuth) is 90 degrees East of North.

- `Dip Azimuth` [0-360]: The angle to the dip. The angle is measured clockwise in degrees with respect to North.

- `Dip` [0-180]: The angle measured downwards from the horizontal at the steepest line in the plane. Use a dip of 90 for a vertical section.

- `Pitch` [0-360]: The angle, measured on the inclined plane, between the strike (horizontal line within the plane) and any other line that lies in the plane

## Properties

<FlatProperties />
