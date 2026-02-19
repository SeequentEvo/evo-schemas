import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/frequency-domain-electromagnetic-1.1.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.1.0" badge="supported" />

# frequency-domain-electromagnetic

<SchemaUri uri="schema/objects/frequency-domain-electromagnetic/1.1.0/frequency-domain-electromagnetic.schema.json" />

**Key components:**
- [survey-line](../components/survey-line.md) — Survey line spatial path with location data
- [frequency-domain-electromagnetic-channel](../components/frequency-domain-electromagnetic-channel.md) — Single frequency channel definition

**See also:** [time-domain-electromagnetic](time-domain-electromagnetic.md) (time-domain counterpart).

## Overview

The frequency-domain-electromagnetic object captures the properties and measurements related to frequency domain electromagnetic surveys. This object is used to represent the data collected during such surveys, including the configuration of the equipment and the resulting measurements.

This object is particularly useful in geophysical analysis where the electromagnetic properties of the subsurface are studied. It provides a standardized way to store and share the data collected during frequency domain electromagnetic surveys.

To define the frequency domain electromagnetic object, the following properties are required:

- The standard required information for a Geoscience Object.
- The survey type ("GROUND" or "AIR").
- The data type (string)
- One or more entries in the `channels` array
- One or more entries in the `line_list` array

Each channel entry contains information about the:

- Channel ID (integer)
- The standard deviations for quadrature and in-phase measurements (the two components of the complex electromagnetic response: in-phase is the component in sync with the transmitted signal, quadrature is the 90°-shifted component)
- The configuration of the coils used in the survey.
- The GPS location of the survey.

The coil configuration includes details about the frequency, geometry, and separation of the coils. The GPS location provides the spatial reference for the survey data.

Each line list entry contains:

- Line number (string; can be alphanumeric)
- Survey date
- Version
- Group
- Survey type; from: ["Line", "Base", "Tie", "Trend", "Special", "Random", "Test"]
- Location channels; mappings indicating which channel attribute corresponds to each of the x, y and z axes
- An array of channel attributes

## Properties

<FlatProperties />

::mermaid[../generated/uml/frequency-domain-electromagnetic-1.1.0.mmd]
