import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/embedded-polyline-object-1.0.0.md';

# embedded-polyline-object

<SchemaUri uri="schema/components/embedded-polyline-object/1.0.0/embedded-polyline-object.schema.json" />

The `embedded-polyline-object` component represents a named polyline/polygon object that references parts
within an [embedded-line-geometry](embedded-line-geometry.md).

* `name` — The name of the polyline object.
* `description` — An optional description.
* `parts` — A list of part references into the parent line geometry.

## Properties

<FlatProperties />
