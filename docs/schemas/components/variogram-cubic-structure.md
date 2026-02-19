import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/variogram-cubic-structure-1.1.0.md';

# variogram-cubic-structure

<SchemaUri uri="schema/components/variogram-cubic-structure/1.1.0/variogram-cubic-structure.schema.json" />

A cubic variogram model structure, used as a component of the [variogram](../objects/variogram.md) object.
The cubic model provides a smooth, parabolic transition from the origin — similar to the Gaussian model
in its near-origin behaviour — but reaches the sill at a finite range. This makes it a useful
alternative to the Gaussian model when a smooth interpolation is desired without the numerical
instability that can accompany asymptotic models.

**Used by:** [variogram](../objects/variogram.md).

**See also:** other variogram models: [spherical](variogram-spherical-structure.md), [exponential](variogram-exponential-structure.md), [Gaussian](variogram-gaussian-structure.md), [linear](variogram-linear-structure.md), [generalised Cauchy](variogram-generalisedcauchy-structure.md), [spheroidal](variogram-spheroidal-structure.md).

## Properties

<FlatProperties />
