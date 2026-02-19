import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/variogram-spheroidal-structure-1.1.0.md';

# variogram-spheroidal-structure

<SchemaUri uri="schema/components/variogram-spheroidal-structure/1.1.0/variogram-spheroidal-structure.schema.json" />

A spheroidal variogram model structure, used as a component of the [variogram](../objects/variogram.md) object.
The spheroidal model is closely related to the spherical model but uses a spheroidal (ellipsoidal)
transition function. Like the spherical model it reaches the sill at a finite range, and it is
typically used in nested variogram structures where subtle differences in transition shape matter.

**Used by:** [variogram](../objects/variogram.md).

**See also:** other variogram models: [spherical](variogram-spherical-structure.md), [exponential](variogram-exponential-structure.md), [Gaussian](variogram-gaussian-structure.md), [cubic](variogram-cubic-structure.md), [linear](variogram-linear-structure.md), [generalised Cauchy](variogram-generalisedcauchy-structure.md).

## Properties

<FlatProperties />
