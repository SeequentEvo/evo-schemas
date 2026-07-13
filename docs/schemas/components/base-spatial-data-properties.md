import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/base-spatial-data-properties-1.1.1.md';

# base-spatial-data-properties

<SchemaUri uri="schema/components/base-spatial-data-properties/1.1.1/base-spatial-data-properties.schema.json" />

The `base-spatial-data-properties` component extends [base-object-properties](base-object-properties.md) with
fields required by all spatial data objects. Most object schemas compose this component via `allOf`.

In addition to the inherited fields (name, uuid, description, etc.), it adds:

* `bounding_box` — The geographic [bounding box](bounding-box.md) of the spatial data.
* `coordinate_reference_system` — The [coordinate reference system](crs.md) in which the object's spatial data is defined.

**Axis order is defined by the CRS.** The order, direction, and meaning of the coordinate axes
(`x`/`y`/`z`, `min_x`/`min_y`/`min_z`, …) are determined by the object's
`coordinate_reference_system`, following the axis order declared in the CRS (its WKT2 / EPSG
definition). The labels `x`, `y`, and `z` denote the **first, second, and third CRS axes** — they do
**not** imply easting, northing, and elevation. See
[Coordinate reference systems and axis order](../../understanding-schemas/coordinate-reference-systems.md).

**Used by:** Most object schemas.

## Properties

<FlatProperties />
