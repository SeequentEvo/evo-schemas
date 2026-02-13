import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/lineage-1.0.0.md';

# lineage

<SchemaUri uri="schema/components/lineage/1.0.0/lineage.schema.json" />

The lineage component records provenance information for a Geoscience Object, describing how the object was created
and what data sources contributed to it. The schema is based on a subset of the
[OpenLineage](https://openlineage.io/) specification (v2.0.2).

* `self_link` — An optional self-referencing link for the object.
* `events` — A list of run events describing segments of the input lineage graph.

## Properties

<FlatProperties />
