import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/base-attribute-1.0.0.md';

# base-attribute

<SchemaUri uri="schema/components/base-attribute/1.0.0/base-attribute.schema.json" />

The `base-attribute` component defines the three properties common to all attribute types:

* `name` — A display name for the attribute.
* `key` — A unique key identifying the attribute within its parent list.
* `attribute_type` — A constant string discriminator identifying the specific attribute type (e.g., `"scalar"`, `"category"`, `"bool"`).

All attribute schemas compose this component via `allOf`.

## Properties

<FlatProperties />
