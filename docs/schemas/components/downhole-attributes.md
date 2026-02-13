import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/downhole-attributes-1.0.0.md';

# downhole-attributes

<SchemaUri uri="schema/components/downhole-attributes/1.0.0/downhole-attributes.schema.json" />

The `downhole-attributes` component represents attributes associated with downhole locations, including
the indices, counts, and offsets into locations and attribute tables.

This is used by schemas that store data along drillhole traces.

**See also:** [hole-chunks](hole-chunks.md), [downhole-direction-vector](downhole-direction-vector.md), [data-table](data-table.md), [interval-table](interval-table.md), [distance-table](distance-table.md).

**Used by:** [drilling-campaign](../drilling-campaign.md), [downhole-collection](../downhole-collection.md).

## Properties

<FlatProperties />
