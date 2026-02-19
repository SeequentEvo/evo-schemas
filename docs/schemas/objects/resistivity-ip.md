import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/resistivity-ip-1.1.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# resistivity-ip

<SchemaUri uri="schema/objects/regular-masked-3d-grid/1.3.0/regular-masked-3d-grid.schema.json" />

**Key components:**
- [resistivity-ip-line](../components/resistivity-ip-line.md) — Survey line with electrode positions and measurements
- [resistivity-ip-dcip-survey-properties](../components/resistivity-ip-dcip-survey-properties.md) — DC induced polarization survey properties
- [resistivity-ip-phaseip-survey-properties](../components/resistivity-ip-phaseip-survey-properties.md) — Phase induced polarization survey properties
- [resistivity-ip-sip-survey-properties](../components/resistivity-ip-sip-survey-properties.md) — Spectral induced polarization survey properties
- [resistivity-ip-pldp-configuration-properties](../components/resistivity-ip-pldp-configuration-properties.md) — Pole-dipole electrode configuration
- [resistivity-ip-plpl-configuration-properties](../components/resistivity-ip-plpl-configuration-properties.md) — Pole-pole electrode configuration

**See also:** [geophysical-records-1d](geophysical-records-1d.md) (1D geophysical data).

## Overview

A resistivity-IP object represents geolocated, time-stamped resistivity and induced polarization (IP) survey data. This data is used extensively in exploration for mineral resources, environmental investigations, and other fields where the electrical properties of subsurface materials provide insight.

The `number_of_dimensions` parameter describes the survey dimension and can take one of the values "1D", "2D", or "3D".

The `number_contributing_electrodes` parameter indicates the number of contributing electrodes, excluding remote electrodes.

The `survey` object includes details about the survey type, which can be one of the following:
- DCIP (Direct Current Induced Polarization): Includes timing information, duty cycle, and number of pulses per recording
- SIP (Spectral Induced Polarization): Specifies a list of frequencies used during measurement
- PHASEIP (Phased Induced Polarization): Specifies a list of frequencies used during measurement
- DCRES (Direct Current Resistivity)

The `configuration` object includes details about the survey configuration, as well as location information for the remote survey elements in the case of Pole-Dipole (transmitter) or Pole-Pole (transmitter and receiver).

The `line_list` array includes one or more resistivity-IP line definitions, including the `group_number`, `date`, `station`, `number_of_electrodes`, and `channel_attributes`.

## Properties

<FlatProperties />

::mermaid[../generated/uml/resistivity-ip-1.1.0.mmd]
