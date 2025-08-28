import CheckIcon from '@mui/icons-material/Check';
import Chip from '@mui/material/Chip';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/resistivity-ip-1.1.0.md';

# resistivity-ip

<Chip color="info" icon={<CheckIcon />} label="Supported" />
<SchemaUri uri="schema/objects/resistivity-ip/1.1.0/resistivity-ip.schema.json" />

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

::mermaid[_generated/uml/resistivity-ip-1.1.0.mmd]
