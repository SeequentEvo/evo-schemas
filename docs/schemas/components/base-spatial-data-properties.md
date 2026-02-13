import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/base-spatial-data-properties-1.1.0.md';

# base-spatial-data-properties

<SchemaUri uri="schema/components/base-spatial-data-properties/1.1.0/base-spatial-data-properties.schema.json" />

The `base-spatial-data-properties` component extends [base-object-properties](base-object-properties.md) with
fields required by all spatial data objects. Most object schemas compose this component via `allOf`.

In addition to the inherited fields (name, uuid, description, etc.), it adds:

* `bounding_box` — The geographic [bounding box](bounding-box.md) of the spatial data.
* `coordinate_reference_system` — The [coordinate reference system](crs.md) in which the object's spatial data is defined.

## Properties

<FlatProperties />
