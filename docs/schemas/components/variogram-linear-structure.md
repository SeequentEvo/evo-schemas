import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/variogram-linear-structure-1.1.0.md';

# variogram-linear-structure

<SchemaUri uri="schema/components/variogram-linear-structure/1.1.0/variogram-linear-structure.schema.json" />

A linear variogram model structure, used as a component of the [variogram](../objects/variogram.md) object.
The linear model increases linearly with distance up to the sill. It is the simplest bounded variogram
model and is typically used as one structure within a nested variogram rather than as a standalone
model.

**Used by:** [variogram](../objects/variogram.md).

**See also:** other variogram models: [spherical](variogram-spherical-structure.md), [exponential](variogram-exponential-structure.md), [Gaussian](variogram-gaussian-structure.md), [cubic](variogram-cubic-structure.md), [generalised Cauchy](variogram-generalisedcauchy-structure.md), [spheroidal](variogram-spheroidal-structure.md).

## Properties

<FlatProperties />
