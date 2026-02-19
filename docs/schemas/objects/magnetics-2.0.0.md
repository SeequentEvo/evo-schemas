import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/magnetics-2.0.0.md';

<OverlineWithVersion title="Geoscience Objects" version="2.0.0" badge="techPreview" />

# magnetics

<SchemaUri uri="schema/objects/magnetics/2.0.0/magnetics.schema.json" />

**Key components:**
- [survey-collection](../components/survey-collection.md) — Logical grouping of survey measurements
- [survey-attribute-definition](../components/survey-attribute-definition.md) — Common properties for survey measurement attributes

**See also:** [gravity-2.0.0](gravity-2.0.0.md) (gravity surveys), [radiometric-2.0.0](radiometric-2.0.0.md) (radiometric surveys).

## Overview

A magnetics object represents geolocated, time stamped geomagnetic survey data. This data is used extensively in exploration for mineral resources, environmental investigations, fundamental earth science mapping, and other fields where the magnetic properties of subsurface materials provide insight.

The `type` parameter describes the survey mode (i.e., how the acquisition was carried out), and must take one of the values "GROUND", "AIR" or "MARINE".

The `survey_type` parameter describes the type of measurement:

- "TMI" indicates Total Magnetic Intensity measurements
- "VMG" stands for Vector Magnitude, a 3-component (triaxial) vector measurement
- "MGRM" stands for Magnetic Gradiometry, a 3D tensor representation with 5 unique components

The `gradient_magnetic` object includes details about gradient magnetic measurements, including the number of sensors and their offsets.

The `base_stations` array includes at least one base station definition, comprising `name`, `location`, `survey_type` and a list of magnetic lines for which it is associated. In this case, `survey_type` in the sub-object refers to the survey type of the base station measurements.

The `collections` array includes one or more `survey-collection` components. Each collection will reference a `survey-attribute-definition` from the `attribute-definition-list`. The definition includes information such as the `name`, spatial `offset`, and `attribute-description`. Individual collections will include the `date`, `identifier`, `version`, `group`, `type` (the geometry and intended use), `locations`, and associated `survey_attributes` (collection data).

The `qaqc_magnetic_azimuth_test_list` array includes QA/QC information describing the magnetic asimuth tests done at the beginning of the survey in a non-magnetically responsive location.

The `qaqc_noise_test_list` array includes QA/QC information measuring ambient noise. This is typically acquired at multiple elevations at the beginning of the survey.

## Properties

<FlatProperties />

::mermaid[../generated/uml/magnetics-2.0.0.mmd]
