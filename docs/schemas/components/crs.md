import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/crs-1.0.1.md';

# crs

<SchemaUri uri="schema/components/crs/1.0.1/crs.schema.json" />

The coordinate reference system (CRS) component specifies the spatial reference for an object's coordinate data.
It supports three representations, exactly one of which must be provided:

* `epsg_code` — An integer EPSG code (between 1024 and 32767) from the [EPSG Geodetic Parameter Dataset](https://epsg.org/).
* `ogc_wkt` — A [WKT2](https://www.ogc.org/standards/wkt-crs) string representation of the CRS.
* An unspecified CRS (no properties), used when the coordinate reference system is unknown or not applicable.

**Used by:** [base-spatial-data-properties](base-spatial-data-properties.md).

## Properties

<FlatProperties />
