import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/attribute-description-1.0.1.md';

# attribute-description

<SchemaUri uri="schema/components/attribute-description/1.0.1/attribute-description.schema.json" />

The `attribute-description` component provides general metadata for a continuous attribute:

* `discipline` — The scientific discipline (e.g., geology, geophysics).
* `type` — The type of measurement or property.
* `unit` — An optional unit of measurement.
* `scale` — An optional measurement scale.
* `extensions` — An optional map for application-specific metadata.
* `tags` — An optional list of tags.

**Used by:** [non-parametric-continuous-cumulative-distribution](../objects/non-parametric-continuous-cumulative-distribution.md).

## Properties

<FlatProperties />
