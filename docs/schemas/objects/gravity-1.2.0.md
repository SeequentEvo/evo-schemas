import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/gravity-1.2.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.2.0" badge="supported" />

# gravity

<SchemaUri uri="schema/objects/gravity/1.2.0/gravity.schema.json" />

**Key components:**
- [survey-collection](../components/survey-collection.md) — Logical grouping of survey measurements
- [survey-attribute-definition](../components/survey-attribute-definition.md) — Common properties for survey measurement attributes

**See also:** [magnetics-1.2.0](magnetics-1.2.0.md) (magnetic surveys), [radiometric-1.2.0](radiometric-1.2.0.md) (radiometric surveys).

## Overview

A gravity object represents geolocated, time stamped gravity survey data. This is generally, but not exclusively, collected along nearly parallel lines. This type of data is used extensively in exploration for mineral resources, fundamental earth science mapping and other fields where the density of subsurface materials provides insight.

The `type` parameter describes the survey mode (i.e., how the acquisition was carried out), and must take one of the values "GROUND", "AIR" or "MARINE".

The `survey_type` parameter describes the type of measurement:

- "GRAV" indicates single-component absolute or relative gradiometry measurements
- "FTG" stands for "Full Tensor Gradiometry"
- "AGG" stands for "Airborne Gravity Gradiometry"

Both "FTG" and "AGG" modes include multi-component measurements of the gravity variation tensor field (of which up to 5 components are unique).

The `base_stations` array includes at least one base station definition, comprising `name`, `location` and a list of gravity lines for which it is associated.

The `gravity_line_list` array includes one or more survey-line definitions, including the `date`, `version` and `group` of the survey. Each survey-line definition indicates the type of survey line (the geometry and intended use), channel mappings and the associated channel attribute data.

## Properties

<FlatProperties />

::mermaid[../generated/uml/gravity-1.2.0.mmd]
