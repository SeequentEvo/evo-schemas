import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/hole-chunks-1.0.0.md';

# hole-chunks

<SchemaUri uri="schema/components/hole-chunks/1.0.0/hole-chunks.schema.json" />

The `hole-chunks` component associates rows of segment and attribute tables with specific drillholes. It stores
the indices, counts, and offsets into locations and attribute tables for each hole.

Columns: `hole_index`, `offset`, `count`.

This component is used by the [drilling-campaign](../objects/drilling-campaign.md) schema.

**Used by:** [downhole-attributes](downhole-attributes.md), [hole-collars](hole-collars.md).

**See also:** [hole-collars](hole-collars.md), [downhole-attributes](downhole-attributes.md), [data-table](data-table.md), [interval-table](interval-table.md), [distance-table](distance-table.md).

## Properties

<FlatProperties />
