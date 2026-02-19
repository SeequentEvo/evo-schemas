import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/data-table-1.2.0.md';

# data-table

<SchemaUri uri="schema/components/data-table/1.2.0/data-table.schema.json" />

The `data-table` component represents a named table of attribute data. It is used to store supplementary data
that does not correspond directly to a geometric property.

* `name` — The name of the table.
* `collection_type` — Always `"data"` (a constant discriminator).
* `attributes` — An optional list of attributes (via [one-of-attribute](one-of-attribute.md)).

**Used by:** [downhole-collection](../objects/downhole-collection.md).

**See also:** [interval-table](interval-table.md), [distance-table](distance-table.md) (specialised table types), [downhole-attributes](downhole-attributes.md) (drilling context).

## Properties

<FlatProperties />
