import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/base-object-properties-1.1.0.md';

# base-object-properties

<SchemaUri uri="schema/components/base-object-properties/1.1.0/base-object-properties.schema.json" />

The `base-object-properties` component defines properties common to all Geoscience Objects. Every object schema
composes this component (either directly or via `base-spatial-data-properties`) using `allOf`.

The core fields are:

* `name` — A human-readable name for the object.
* `uuid` — A universally unique identifier for the object. May be `null` for new objects that have not yet been assigned an identifier.
* `description` — An optional description of the object.
* `extensions` — An optional map for application-specific extensions.
* `tags` — An optional list of tags for categorisation.
* `lineage` — An optional [lineage](lineage.md) component recording the provenance of the object.

## Properties

<FlatProperties />
