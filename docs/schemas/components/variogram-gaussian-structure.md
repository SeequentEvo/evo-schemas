import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/variogram-gaussian-structure-1.1.0.md';

# variogram-gaussian-structure

<SchemaUri uri="schema/components/variogram-gaussian-structure/1.1.0/variogram-gaussian-structure.schema.json" />

A Gaussian variogram model structure, used as a component of the [variogram](../objects/variogram.md) object.
The Gaussian model is characterised by a parabolic behaviour near the origin, producing very smooth
interpolated fields. Like the exponential model, it approaches the sill asymptotically. It is
appropriate when the underlying property varies smoothly in space; however, it can cause numerical
instability in Kriging systems and should be used with care.

**Used by:** [variogram](../objects/variogram.md).

**See also:** other variogram models: [spherical](variogram-spherical-structure.md), [exponential](variogram-exponential-structure.md), [cubic](variogram-cubic-structure.md), [linear](variogram-linear-structure.md), [generalised Cauchy](variogram-generalisedcauchy-structure.md), [spheroidal](variogram-spheroidal-structure.md).

## Properties

<FlatProperties />
