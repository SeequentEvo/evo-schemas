import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/variogram-generalisedcauchy-structure-1.1.0.md';

# variogram-generalisedcauchy-structure

<SchemaUri uri="schema/components/variogram-generalisedcauchy-structure/1.1.0/variogram-generalisedcauchy-structure.schema.json" />

A Generalised Cauchy variogram model structure, used as a component of the [variogram](../objects/variogram.md) object.
The Generalised Cauchy model offers flexibility through additional shape parameters that independently
control the behaviour near the origin and at large distances. This allows it to model both smooth
and rough spatial correlation structures, making it useful when standard models (spherical, exponential)
do not adequately fit the experimental variogram.

**Used by:** [variogram](../objects/variogram.md).

**See also:** other variogram models: [spherical](variogram-spherical-structure.md), [exponential](variogram-exponential-structure.md), [Gaussian](variogram-gaussian-structure.md), [cubic](variogram-cubic-structure.md), [linear](variogram-linear-structure.md), [spheroidal](variogram-spheroidal-structure.md).

## Properties

<FlatProperties />
