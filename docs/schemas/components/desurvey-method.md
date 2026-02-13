import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/desurvey-method-1.0.0.md';

# desurvey-method

<SchemaUri uri="schema/components/desurvey-method/1.0.0/desurvey-method.schema.json" />

The `desurvey-method` component specifies the algorithm used to calculate 3D drillhole paths from survey
measurements (azimuth and dip readings at measured depths).

The method determines how the path between survey stations is interpolated — common methods include
minimum curvature and tangential approaches.

## Properties

<FlatProperties />
