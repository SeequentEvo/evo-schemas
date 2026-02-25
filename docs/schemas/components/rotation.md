import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/rotation-1.1.0.md';

# rotation

<SchemaUri uri="schema/components/rotation/1.1.0/rotation.schema.json" />

Rotation in 3D space described by 3 in-plane rotations, all rotating clockwise about the Z, then X, and finally Z axes. All angles must be positive values, specified in degrees, within the bounds defined for each rotation. 0 degrees in the xy plane (dip azimuth) is 90 degrees East of North.

- `Dip Azimuth` [0-360]: The angle to the dip. The angle is measured clockwise in degrees with respect to North.

- `Dip` [0-180]: The angle measured downwards from the horizontal at the steepest line in the plane. Use a dip of 90 for a vertical section.

- `Pitch` [0-360]: The angle, measured on the inclined plane, between the strike (horizontal line within the plane) and any other line that lies in the plane

**Used by:** [geological-sections](../objects/geological-sections.md), [non-parametric-continuous-cumulative-distribution](../objects/non-parametric-continuous-cumulative-distribution.md), [regular-2d-grid](../objects/regular-2d-grid.md), [regular-3d-grid](../objects/regular-3d-grid.md), [regular-masked-3d-grid](../objects/regular-masked-3d-grid.md), [tensor-2d-grid](../objects/tensor-2d-grid.md), [tensor-3d-grid](../objects/tensor-3d-grid.md).

## Properties

<FlatProperties />
