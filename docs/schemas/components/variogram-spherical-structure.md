import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/variogram-spherical-structure-1.1.0.md';

# variogram-spherical-structure

<SchemaUri uri="schema/components/variogram-spherical-structure/1.1.0/variogram-spherical-structure.schema.json" />

A spherical variogram model structure, used as a component of the [variogram](../objects/variogram.md) object.
The spherical model is one of the most commonly used variogram models in geostatistics. It increases
steadily from the origin and reaches the sill at a finite range, beyond which the semivariance remains
constant. Its well-defined range makes it a natural first choice when fitting experimental variograms
to data with a clear spatial correlation limit.

**Used by:** [variogram](../objects/variogram.md).

**See also:** other variogram models: [exponential](variogram-exponential-structure.md), [Gaussian](variogram-gaussian-structure.md), [cubic](variogram-cubic-structure.md), [linear](variogram-linear-structure.md), [generalised Cauchy](variogram-generalisedcauchy-structure.md), [spheroidal](variogram-spheroidal-structure.md).

## Properties

<FlatProperties />
