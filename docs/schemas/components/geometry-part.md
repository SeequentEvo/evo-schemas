import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/geometry-part-1.0.1.md';

# geometry-part

<SchemaUri uri="schema/components/geometry-part/1.0.1/geometry-part.schema.json" />

The `geometry-part` component describes a named part within a composite geometry, associating a section of
shared geometry with metadata.

* `key` — A unique identifier for the part.
* `name` — A display name.
* `data_source` — An optional link to a related geoscience object.
* `feature` — The geological feature type.
* `transform` — An optional spatial transform.
* `bounding_box` — The [bounding box](bounding-box.md) of this part.
* `layer` — An optional layer index.
* `color` — An optional display colour.
* `geometry` — Indices defining which elements of the parent geometry belong to this part.

See [Understanding parts](../../understanding-schemas/understanding-parts.md) for more context.

## Properties

<FlatProperties />
