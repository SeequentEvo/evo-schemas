# Coordinate reference systems and axis order

The Coordinate Reference System (CRS) for spatial / geoscience data is critical to uniquely locate each datapoint relative to the Earth and to other datasets. Evo takes a strict approach to CRS, consistent with other leading implementations (e.g., PROJ > v6.0; see below).

Every spatial Geoscience Object carries a `coordinate_reference_system` as part of its
[base-spatial-data-properties](../schemas/components/base-spatial-data-properties.md). The CRS is
the single source of truth for how the object's coordinates should be interpreted: it defines the
**order**, **direction**, and **meaning** of each coordinate axis.

The schema field labels `x`, `y`, and `z` (and the bounding-box fields `min_x`, `max_x`, `min_y`,
`max_y`, `min_z`, `max_z`) are **positional labels for the first, second, and third CRS axes**.
They do **not** imply easting, northing, and elevation or any other inferred coordinate ordering. To interpret a coordinate correctly, read the object's CRS first.

## CRS representations

The [crs](../schemas/components/crs.md) component supports three representations, exactly one of which must be provided:

* `epsg_code` — An integer EPSG code from the [EPSG Geodetic Parameter Dataset](https://epsg.org/).
* `ogc_wkt` — A [WKT2](https://www.ogc.org/standards/wkt-crs) string. Axis order is declared explicitly in the WKT2 `AXIS` clauses.
* An unspecified CRS (no properties), used when the coordinate reference system is unknown or not applicable.

For both `epsg_code` and `ogc_wkt`, the axis order, direction, and meaning are those declared in the CRS definition — not an assumption made by the schema or by consuming software.

## The rule

> The order, direction, and meaning of the coordinate axes are defined by the object's `coordinate_reference_system`, following the axis order declared in the CRS (its WKT2 / EPSG definition). The labels `x`, `y`, and `z` denote the **first, second, and third CRS axes** — consumers must **not** infer the meanings of these labels.

This mirrors the modern [PROJ](https://proj.org/) (version 6 and later) philosophy of being strict about CRS-declared axis order rather than silently assuming an easting-first ordering. See the PROJ
FAQ, [Why is the axis ordering in PROJ not consistent?](https://proj.org/en/stable/faq.html#why-is-the-axis-ordering-in-proj-not-consistent), for a clear rationale.

## Worked example: axis order matters

Consider a point whose first two coordinate values are `(500000, 400000)`.

**EPSG:2180** ([ETRF2000-PL / CS92, Poland](https://epsg.io/2180)) declares its axis order as **(northing, easting)** — the first axis points North, the second points East. **A UTM zone** such
as [EPSG:32633](https://epsg.io/32633) declares the opposite order, **(easting, northing)**. The same pair of numbers therefore describes two different ground positions depending on the CRS.

The transformation below uses [pyproj](https://pyproj4.github.io/pyproj/stable/) to convert the point from EPSG:2180 to [EPSG:4326](https://epsg.io/4326) (WGS 84 geographic, axis order latitude, longitude). The `always_xy` flag on [`Transformer`](https://pyproj4.github.io/pyproj/stable/api/transformer.html) controls whether the
CRS axis order is honoured. **`always_xy=False` (the default) honours the CRS-declared axis order and is the correct setting here**. The use of `always_xy=True` forces an easting/longitude-first ordering and silently swaps the coordinates in many CRS configurations, e.g.:

```python
import pyproj

epsg_4326_gps    = pyproj.CRS.from_epsg(4326)   # WGS 84 geographic, axis order (lat, lon)
epsg_2180_poland = pyproj.CRS.from_epsg(2180)   # axis order (northing, easting)

# Honours the CRS axis order — always_xy=False is the default (CORRECT):
t = pyproj.Transformer.from_crs(epsg_2180_poland, epsg_4326_gps, always_xy=False)
print(t.transform(500000, 400000, 0))
# -> (52.356819022127155, 17.531162579943917, 0.0)   # (lat, lon, z)

# Forces easting/longitude-first, ignoring the CRS axis order (WRONG for this CRS):
t = pyproj.Transformer.from_crs(epsg_2180_poland, epsg_4326_gps, always_xy=True)
print(t.transform(500000, 400000, 0))
# -> (19.0, 51.466568940540256, 0.0)                 # (lon, lat, z) — swapped, wrong location
```

Interpreting the coordinates as easting-first, when the CRS declares northing-first, places the point in the wrong location. The only generally-correct approach is to defer to the CRS.

## Non-cardinal and reversed axes

Deferring to the CRS is necessary because axis order is not the only variable — axes can also point in non-cardinal directions or increase in the "wrong" direction. For example,
[EPSG:2065](https://epsg.io/2065) (S-JTSK / Krovak, Czechia) is a Křovák projection whose first axis points **South** and whose second axis points **West**. Increasing the first coordinate moves a point
*south* (latitude decreases); increasing the second coordinate moves it *west* (longitude decreases).

You cannot infer axis order, direction, or meaning from the field names `x`, `y`, `z`. Always read them from the CRS.

## Bounding box

The [bounding-box](../schemas/components/bounding-box.md) `min_*`/`max_*` fields give the extent along the corresponding **CRS axis**, not necessarily easting, northing, or elevation:

* `min_x`/`max_x` — extent along the first CRS axis.
* `min_y`/`max_y` — extent along the second CRS axis.
* `min_z`/`max_z` — extent along the third CRS axis.

## Contrast with GeoJSON

Readers coming from a [GeoJSON](https://www.rfc-editor.org/rfc/rfc7946) background should note an important difference. GeoJSON fixes its coordinate reference system to WGS 84 ([RFC 7946, §4](https://www.rfc-editor.org/rfc/rfc7946#section-4)) and always orders coordinates longitude, then latitude, then elevation ([§3.1.1 "Position"](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.1)). This fixed longitude-first ordering (equivalent to `urn:ogc:def:crs:OGC::CRS84`) is why GeoJSON differs even from EPSG:4326, which uses the same WGS 84 datum but is latitude-first. Geoscience Objects do **not** pin a CRS this way — they defer to the object's `coordinate_reference_system`, so both the CRS and the coordinate order can differ from GeoJSON.

## Producer and consumer guidance

* **Producers** should write coordinates (and bounding-box extents) in the CRS's native axis order, and set `coordinate_reference_system` to describe exactly that ordering.
* **Consumers** should read the CRS *before* interpreting any coordinate. A consumer that natively supports arbitrary CRSs can use the coordinates directly in their declared order; one that transforms to another CRS should use a library that honours CRS-declared axis order (for example, PROJ ≥ 6 / pyproj with the default `always_xy=False`). Be flexible on read: do not assume easting-first.

## References

* PROJ FAQ — [Why is the axis ordering in PROJ not consistent?](https://proj.org/en/stable/faq.html#why-is-the-axis-ordering-in-proj-not-consistent)
* pyproj — [`Transformer` API and `always_xy`](https://pyproj4.github.io/pyproj/stable/api/transformer.html)
* [EPSG:2180 — ETRF2000-PL / CS92 (axis order northing, easting)](https://epsg.io/2180)
* [EPSG:2065 — S-JTSK / Krovak (South, West axes)](https://epsg.io/2065)
* [EPSG:4326 — WGS 84 geographic (axis order latitude, longitude)](https://epsg.io/4326)
* [EPSG Geodetic Parameter Dataset](https://epsg.org/)
* OGC — [WKT-CRS (WKT2) standard](https://www.ogc.org/standards/wkt-crs)
* [GeoJSON — RFC 7946, §3.1.1 "Position"](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.1)
* Seequent Developer Portal — [coordinate reference systems (common data types)](https://developer.seequent.com/docs/api/fundamentals/common-data-types/#coordinate-reference-systems)
