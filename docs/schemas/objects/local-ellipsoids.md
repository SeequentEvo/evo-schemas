import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/local-ellipsoids-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# local-ellipsoids

<SchemaUri uri="schema/objects/local-ellipsoids/1.3.0/local-ellipsoids.schema.json" />

The local-ellipsoids object captures a set of spatially located ellipsoids. Each ellipsoid is assigned a 3D location. This object is used to model spatially varying anisotropy. It is useful for exploring the spatial continuity of geological structures or as a locally-varying field in geostatistical workflows.

To define the ellipsoids, the object requires:

- A table of 3D locations.
- A table that has the six ellipsoid parameters (major, semi-major, minor, azimuth, dip, and pitch) for each location.

The object can also capture additional context such as the domain and the attribute that were used to compute the local ellipsoids.

This object is related to the global-ellipsoid and the variogram objects as each one of them can be used to measure spatial anisotropy.

## Properties

<FlatProperties />

::mermaid[../generated/uml/local-ellipsoids-1.3.0.mmd]
