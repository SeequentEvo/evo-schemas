import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/radiometric-2.0.0.md';

<OverlineWithVersion title="Geoscience Objects" version="2.0.0" badge="techPreview" />

# radiometric

<SchemaUri uri="schema/objects/radiometric/2.0.0/radiometric.schema.json" />

A radiometric object represents geolocated, time stamped radiometric survey data. Radiometric surveys measure naturally occurring radioactivity in the form of gamma-rays, which mostly originate from mineral species containing radioactive isotopes of Potassium (K), Uranium (U), and Thorium (Th). The gamma-rays emitted by different elements have different energy levels, and the number of counts at each energy level indicates the presence of that element. This type of survey is most often carried out alongside other geophysical methods (e.g., aeromagnetic surveys) to provide additional information about naturally occurring radioactive mineral species in the area.

The `survey` object includes details about the survey type, which can be either "GROUND" or "AIR".

The `sample_time` parameter describes the timing characteristics of the survey measurements in milliseconds.

The `array_dimension` and `energy_level` (in meV) parameters describe the characteristics of the array.

The `collections` array includes one or more `survey-collection` components. Each collection will reference a `survey-attribute-definition` from the `attribute-definition-list`. The definition includes information such as the `name`, spatial `offset`, and `attribute-description`. Individual collections will include the `date`, `identifier`, `version`, `group`, `type` (the geometry and intended use), `locations`, and associated `survey_attributes` (collection data).

## Properties

<FlatProperties />

::mermaid[../generated/uml/radiometric-2.0.0.mmd]
