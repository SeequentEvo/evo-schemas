import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/global-ellipsoid-1.2.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.2.0" badge="supported" />

# global-ellipsoid

<SchemaUri uri="schema/objects/global-ellipsoid/1.2.0/global-ellipsoid.schema.json" />

**Key components:**
- [ellipsoid](../components/ellipsoid.md) — Single ellipsoid definition for anisotropy

**See also:** [local-ellipsoids](local-ellipsoids.md) (per-element ellipsoids).

## Overview

The global-ellipsoid object captures the parameters of an ellipsoid. Such an object is typically used to represent the anisotropy or the main direction of continuity of spatial geological properties such as mineral grades, petrophysical properties, or lithology.

An ellipsoid is defined by three lengths for the major, semi-major, and minor axes, rotated in space as defined by the rotation.

The rotation in 3D space is described by three angles (azimuth, dip, and pitch), all rotating clockwise about the Z, then X, and finally Z axes. All angles must be positive values, specified in degrees, within the bounds defined for each rotation. 0 degrees in the xy plane (dip azimuth) is 90 degrees East of North.

This object is related to [the variogram object](variogram.md) as both can be used to describe anisotropy.

## Properties

<FlatProperties />

::mermaid[../generated/uml/global-ellipsoid-1.2.0.mmd]
