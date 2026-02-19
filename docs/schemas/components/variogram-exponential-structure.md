import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/variogram-exponential-structure-1.1.0.md';

# variogram-exponential-structure

<SchemaUri uri="schema/components/variogram-exponential-structure/1.1.0/variogram-exponential-structure.schema.json" />

An exponential variogram model structure, used as a component of the [variogram](../objects/variogram.md) object.
The exponential model approaches the sill asymptotically — unlike the spherical model, it never fully
reaches the sill but gets arbitrarily close. The practical range (where it reaches ~95% of the sill)
is about three times the range parameter. This model is well suited to phenomena with a gradual
decay in spatial correlation.

**Used by:** [variogram](../objects/variogram.md).

**See also:** other variogram models: [spherical](variogram-spherical-structure.md), [Gaussian](variogram-gaussian-structure.md), [cubic](variogram-cubic-structure.md), [linear](variogram-linear-structure.md), [generalised Cauchy](variogram-generalisedcauchy-structure.md), [spheroidal](variogram-spheroidal-structure.md).

## Properties

<FlatProperties />
