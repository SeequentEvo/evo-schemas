import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/geophysical-records-1d-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# geophysical-records-1d

<SchemaUri uri="schema/objects/geophysical-records-1d/1.3.0/geophysical-records-1d.schema.json" />

**Key components:**
- [category-data](../components/category-data.md) — Lookup table mapping integer keys to category names
- [lengths](../components/lengths.md) — Layer thickness values

**See also:** [resistivity-ip](resistivity-ip.md) (resistivity/IP surveys).

## Overview

The geophysical-records-1d object captures physical properties related to 1D geophysical records. These records are typically the product of geophysical inversion (the process of estimating subsurface physical properties from measured geophysical data). They are composed of a series of 1D, vertical columnar datasets — each column represents a stack of layers at a single surface location, with a property value (e.g., resistivity, density, susceptibility) assigned to each layer.

To define the geophysical-records-1d object, the following properties are required:

- The number of layers (integer; this is consistent for all records)
- An array of locations
- An array of depths (layer thicknesses)
- The standard required information for a Geoscience Object

Each location entry contains information about the:

- Coordinates (x, y, z).

Each depth entry contains:

- Layer thickness values. The `depths` property uses the [lengths](../components/lengths.md) component to store the thickness of each layer. Cumulating these thicknesses from the surface yields the depth to each layer boundary.

Additionally, the object can include:

- Line numbers.

## Properties

<FlatProperties />

::mermaid[../generated/uml/geophysical-records-1d-1.3.0.mmd]
