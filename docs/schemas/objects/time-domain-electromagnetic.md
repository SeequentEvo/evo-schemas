import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/time-domain-electromagnetic-1.1.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.1.0" badge="supported" />

# time-domain-electromagnetic

<SchemaUri uri="schema/objects/time-domain-electromagnetic/1.1.0/time-domain-electromagnetic.schema.json" />

A time-domain electromagnetic (TDEM) object represents geolocated, time-stamped TDEM survey data. This data is used extensively in exploration for mineral resources, groundwater investigations, and other fields where the electrical conductivity of subsurface materials provides insight.

Electromagnetic (EM) methods do not require direct contact with the ground.  EM methods use the phenomenon of electromagnetic induction to create a subsurface current flow, then measure its dissipation.  This provides information about the electrical conductivity/chargeability of the subsurface, by measuring the ease with which induced electrical currents flow in the subsurface and the rate at which the electrical chargeability discharges at rock unit boundaries. Rather than the rock units, it is the porosity and the content in the pores space that influence the conductivity of the rock. EM methods provide a measure of the geometry, dimension and electrical characteristics of the source of the anomalous response.

Electromagnetic (EM) methods do not require direct contact with the ground.  EM methods use the phenomenon of electromagnetic induction to create a subsurface current flow, then measure its dissipation.  EM methods provide information about the electrical conductivity/chargeability of the subsurface, by measuring the ease with which induced electrical currents flow in the subsurface and the rate at which the electrical chargeability discharges at rock unit boundaries. Rather than the rock units, it is the porosity and the content in the pores space that influence the conductivity of the rock.  EM methods provide a measure of the geometry, dimension and electrical characteristics of the source of the anomalous response.

The `survey` object includes details about the survey type, which can be one of the following:
- GROUND
- AIR
- MOVING_GROUND
- DAGCAP (stands for DoD Advanced Geophysical Classification Accreditation Program)

The `geometry_category` property is a string value taking one of the following forms describing the transmitter (Tx) and receiver (Rx) geometry:
- STXMRX: The Tx is stationary on the ground and the Rx is towed either on the ground or airborne
- FGTXRX: The Tx and Rx are on the same fixed geometry frame and moving together
- MTXMRX: The Tx is built into the vehicle and the Rx is towed on a separate frame
- STXSRX: The Txs and Rxs are in a fixed geometry and stationary, and frequencies are changed

The `gps` field indicates the location of a GPS relative to a point of reference.

The `channels` array includes one or more time-domain-electromagnetic-channel objects. Each channel has properties including the channel index, timing information for the transmissions, IDs for the transmitter and receiver, waveform and gates configuration, loop configuration, statistics, filter parameters, etc.

The `line_list` array includes one or more survey-line definitions, including the `line_number`, `date`, `version`, and `group` of the survey. Each survey-line definition indicates the type of survey line (the geometry and intended use), location channels, and the associated channel attribute data.

## Properties

<FlatProperties />

::mermaid[../generated/uml/time-domain-electromagnetic-1.1.0.mmd]
