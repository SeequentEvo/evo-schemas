import CheckIcon from '@mui/icons-material/Check';
import Chip from '@mui/material/Chip';
import Grid from '@mui/material/Grid';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/radiometric-1.2.0.md';

<Grid container>
# radiometric
<Chip color="info" icon={<CheckIcon />} label="Supported" style={{margin: '0.75em'}} />
</Grid>
<SchemaUri uri="schema/objects/radiometric/1.2.0/radiometric.schema.json" />

A radiometric object represents geolocated, time stamped radiometric survey data. Radiometric surveys measure naturally occurring radioactivity in the form of gamma-rays, which mostly originate from mineral species containing radioactive isotopes of Potassium (K), Uranium (U), and Thorium (Th). The gamma-rays emitted by different elements have different energy levels, and the number of counts at each energy level indicates the presence of that element. This type of survey is most often carried out alongside other geophysical methods (e.g., aeromagnetic surveys) to provide additional information about naturally occurring radioactive mineral species in the area.

The `survey` object includes details about the survey type, which can be either "GROUND" or "AIR".

The `dead_time`, `live_time`, and `idle_time` parameters describe the timing characteristics of the survey measurements in milliseconds.

The `array_dimension` and `energy_level` (in meV) parameters describe the characteristics of the array.

The `line_list` array includes one or more survey-line definitions, including the `line_number`, `date`, `version`, and `group` of the survey. Each survey-line definition indicates the type of survey line (the geometry and intended use), location channels, and the associated channel attribute data.

## Properties

<FlatProperties />

::mermaid[_generated/uml/radiometric-1.2.0.mmd]
