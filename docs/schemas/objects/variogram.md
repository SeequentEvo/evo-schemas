import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/variogram-1.2.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.2.0" badge="supported" />

# variogram

<SchemaUri uri="schema/objects/variogram/1.2.0/variogram.schema.json" />

**Key components:**
- [variogram-spherical-structure](../components/variogram-spherical-structure.md) — Spherical model reaching sill at finite range
- [variogram-exponential-structure](../components/variogram-exponential-structure.md) — Exponential model approaching sill asymptotically
- [variogram-gaussian-structure](../components/variogram-gaussian-structure.md) — Gaussian model with parabolic origin behaviour
- [variogram-cubic-structure](../components/variogram-cubic-structure.md) — Cubic model with smooth transition
- [variogram-linear-structure](../components/variogram-linear-structure.md) — Linear model increasing with distance
- [variogram-spheroidal-structure](../components/variogram-spheroidal-structure.md) — Spheroidal model for geostatistical analysis
- [variogram-generalisedcauchy-structure](../components/variogram-generalisedcauchy-structure.md) — Generalised Cauchy model with flexible shape parameters

**See also:** [experimental-variogram](experimental-variogram.md) (experimental counterpart), [local-ellipsoids](local-ellipsoids.md) (anisotropy ellipsoids).

## Overview

The variogram object captures the parameters of variogram models as used in geostatistical analysis and modelling. A variogram describes the degree of spatial dependence of properties such as mineral grades, porosity, or petrophysical properties. It is used to quantify how data points are related to each other based on their spatial separation and direction.

A variogram is required anytime one uses the Kriging family of algorithms, including most geostatistical conditional simulations and non-linear estimation methods such as LUC and MIK.

The variogram model object can be composed of several structures. Each structure is independently composed of a type (e.g., spherical, exponential) and an anisotropy (ranges, sill and rotation angles).

The anisotropy of the variogram is described as an ellipsoid. An ellipsoid is defined by three lengths for the major, semi-major, and minor axes, rotated in space as defined by the rotation and perpendicularlly related. Rotation in 3D is described by three angles—azimuth, dip, and pitch—applied sequentially: first around the Z-axis, then the X-axis, and finally the Z-axis again to determine the plunge direction (major axis). All angles must be positive values in degrees, within the defined bounds for each rotation. In the XY plane, a dip azimuth of 0° points North.

This object also captures additional context of the data underlying the model and can be associated with:

- Modelling space: data (raw) space or normal score space.
- Domain: the name of the domain that is represented by this variogram model.
- Attribute: the name of the data property that was used to model this variogram.
- Declustering: Using or not the declustering weight.

This object can be used when performing kriging, conditional simulations, and change of support analysis. It is typically created from a variogram modeling application.

## Properties

<FlatProperties />

::mermaid[../generated/uml/variogram-1.2.0.mmd]
