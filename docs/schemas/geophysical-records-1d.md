import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './generated/flatmd/objects/geophysical-records-1d-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# geophysical-records-1d

<SchemaUri uri="schema/objects/geophysical-records-1d/1.3.0/geophysical-records-1d.schema.json" />

The geophysical-records-1d object captures physical properties related to 1D geophysical records. These records are the product of geophysical inversion. These are composed of a series of 1D, vertical (columnar) datasets, each of which contains records (or dummy values) for a series of layers.

To define the geophysical-records-1d object, the following properties are required:

- The number of layers (integer; this is consistent for all records)
- An array of locations
- An array of depths
- The standard required information for a Geoscience Object

Each location entry contains information about the:

- Coordinates (x, y, z).

Each depth entry contains:

- Length values.

Additionally, the object can include:

- Line numbers.

## Properties

<FlatProperties />

::mermaid[generated/uml/geophysical-records-1d-1.3.0.mmd]
