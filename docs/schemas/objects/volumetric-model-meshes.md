import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/volumetric-model-meshes-1.0.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.0.0" badge="techPreview" />

# volumetric-model-meshes

<SchemaUri uri="schema/objects/volumetric-model-meshes/1.0.0/volumetric-model-meshes.schema.json" />

**Key components:**
- [embedded-triangulated-mesh](../components/embedded-triangulated-mesh.md) — The single shared mesh, decomposed into parts
- [embedded-mesh-object](../components/embedded-mesh-object.md) — Base for both surfaces and volumes
- [material](../components/material.md) — Presentation metadata referenced by `material_key`
- [lookup-table](../elements/lookup-table.md) — Resolves the integer category keys to names
- [rotation](../components/rotation.md) — Orientation of a rotated model extent, referenced by `extent_rotation`

**See also:** [geological-model-meshes](geological-model-meshes.md) (the same structural pattern with geological semantics), [triangle-mesh](triangle-mesh.md) (a single surface on its own).

## Overview

A mesh-based volumetric model: a collection of surfaces and volumes composed from the parts of one shared triangulated mesh. Because every surface and volume references parts of the same mesh, adjacent volumes are conformal — they abut exactly and share their bounding geometry rather than each carrying its own copy of it.

The schema is deliberately generic. Its first use is isosurfacing output — grade shells at a series of thresholds and the volumes between them — but the same object represents categorical domain models. A single model may carry both: a combined model in which domains are cut by grade shells has isosurfaces and category boundaries side by side, and the object is designed to hold that without a second schema.

Use [triangle-mesh](triangle-mesh.md) instead when a single surface is all that is needed. Use [geological-model-meshes](geological-model-meshes.md) when the content is geological interpretation with materials and geological feature types.

### Kinds of surface and volume

Every entry in `surfaces` declares a `surface_type`, and every entry in `volumes` a `volume_type`. Both are **required**, and each value selects the data that entry carries:

| `surface_type` | Carries | Meaning |
|---|---|---|
| `"Isosurface"` | `bound` *(required)* | Extracted from a scalar field at a single threshold |
| `"CategoryBoundary"` | `categories` *(required)* | A contact between two categories, or one category against unassigned space |
| `"ModelBoundary"` | `boundary_face`, `category` *(both optional)* | Lies on the boundary of the model extent |
| `"NoData"` | — | Closes the model where the source data was absent |
| `"Generic"` | — | None of the above |

| `volume_type` | Carries | Meaning |
|---|---|---|
| `"IsoVolume"` | `lower_bound`, `upper_bound` | A band of the scalar field between consecutive thresholds |
| `"CategoryRegion"` | `category` *(required)* | The region occupied by one category |
| `"ModelBoundary"` | — | The extent of the model itself |
| `"Generic"` | — | None of the above |

The type is not a label attached to an otherwise uniform object — it chooses between distinct shapes. An isosurface without a `bound` is not valid, and a category region without a `category` is not valid; both are rejected by the schema rather than left to a consumer to discover. Equally, a `"Generic"` surface cannot carry a `bound`, because a threshold on something that is not an isosurface has no meaning.

Adding a further kind in a later minor version means adding a variant here. A document using a new kind will not validate against this version of the schema, which is the same as it would have been had the types been a plain enumeration.

### Orientation and winding

Several properties refer to the front and back of a surface. `evo-schemas` does not define a platform-wide winding convention, so this object states one explicitly:

* The **front** of a triangle is the side from which its three vertices appear in **counter-clockwise** order. Equivalently, its normal is `(v1 - v0) × (v2 - v0)` under the right-hand rule, and points **out of the front face**.

* A part referenced with [`reversed`](../elements/reversible-index.md) set to `true` has the front and back of its triangles swapped for that reference. The same part can therefore be used front-out by one volume and back-out by the adjacent one, which is what makes the pair conformal.

* A closed volume's parts are oriented so that every triangle's front faces **outwards**, away from the enclosed region.

* A producer whose triangulation uses the opposite winding must correct it before publishing. Inverting the `reversed` flag of every part reference is sufficient; no geometry needs rewriting.

A surface and the volumes that use it are oriented independently, which is worth working through. Take a contact with category A in front of it and category B behind it: the surface's own triangles have their fronts facing A. The volume enclosing B uses those parts unchanged, because their fronts already face out of B. The volume enclosing A uses the *same* parts with `reversed` set to `true`, so that its view of them faces out of A. Both volumes are outward-facing as required, no geometry is duplicated, and the two fit together exactly. The consequence for consumers is that a part's orientation must be read from the reference that uses it, never from the surface alone.

### Relating surfaces to volumes

Parts are the only linkage between a surface and a volume — there are no index references from one to the other. A surface and a volume are related exactly when their sets of part indices intersect.

That intersection may be partial. A volume does **not** necessarily contain a whole surface: a model-extent surface is typically cut into patches by the isosurfaces crossing it, and each volume uses only the patches that bound it. An isosurface, by contrast, is normally shared in full by exactly two volumes with opposite `reversed` flags — which is what makes the volumes watertight where they meet.

### Finding items by kind

`surface_type` and `volume_type` are the single source of truth for classification, and this object carries no precomputed index lists alongside them. To collect the isosurfaces, filter `surfaces` on `surface_type` and sort by `bound`. To collect the iso-volume bands in order, filter `volumes` on `volume_type` and sort by bound: the band with no `lower_bound` comes first and the band with no `upper_bound` last. Cumulative views, such as everything below a given threshold, are built from the bands as described under [`"IsoVolume"`](#isovolume).

Deriving these on read is cheap, and it avoids a second copy of the classification that JSON Schema has no way to check against the first. `boundary_volume` is the one index the object does carry, because it picks out a single volume that a consumer must not mistake for model content, and it is a lone reference rather than a list with an exhaustiveness contract to break.

## `triangle_geometry`

The single shared mesh. See [Understanding parts](../../understanding-schemas/understanding-parts.md) for the semantics of chunks, indices, and the reversal flag.

* `triangles`: The vertices and triangle indices of the mesh.

* `parts`: Chunks of triangles that surfaces and volumes are composed from. `parts` is required on this object.

Parts must be split finely enough that every part is wholly inside or wholly outside every volume. A part is never partially used — partial use is expressed by having more, smaller parts.

## `surfaces` *array*

Open or closed surfaces in the model. May be empty, though a model with neither surfaces nor volumes carries no content and should not be published. Every surface has:

* `name`: Object name.

* `description`: Optional additional description of this surface.

* `quality`: Optional hint about mesh [quality](../components/mesh-quality.md) characteristics.

* `parts`: The mesh parts that make up this surface, and whether traversal order within each part is reversed.

* `surface_type`: Required kind of surface, which selects the properties below.

* `material_key`: Optional key of an entry in `materials`, matching [geological-model-meshes](geological-model-meshes.md), where surfaces carry a material as well as volumes. Isosurfacing output normally omits it; interpreted models use it to preserve a surface's appearance.

  A surface has one `material_key`, not one per side. Where a surface separates two differently presented regions, that single entry is its whole appearance; a consumer that wants to shade the two sides differently should take its colours from the volumes on either side instead. This is a known limitation, shared with [geological-model-meshes](geological-model-meshes.md).

### `"Isosurface"`

A surface extracted from a scalar field at a single threshold, such as a grade shell.

* `bound`: **Required.** The scalar value the surface was extracted at, in the model's [`bounds_unit`](#bounds_unit). A surface is extracted at one threshold, so it carries a single value rather than a range.

Triangle normals point towards **increasing** values of the scalar field: the region above `bound` lies in front of the surface, the region below it behind. Combined with the outward rule for volumes under [Orientation and winding](#orientation-and-winding), the iso-volume band just below the threshold uses the isosurface's parts as they are, and the band just above uses them with `reversed` set to `true`.

### `"CategoryBoundary"`

A contact between two categories, or between one category and unassigned space inside the model extent. Where a category meets the boundary of the extent, the surface is a [`"ModelBoundary"`](#modelboundary) surface carrying that `category` instead — it is where the model was clipped, not a contact in the data.

* `categories`: **Required.** Keys into [`category_lookup`](#category_lookup), ordered so that the triangle normals point **from `categories[0]` towards `categories[1]`** — the first entry is the category behind the surface, the second the category in front of it, as defined under [Orientation and winding](#orientation-and-winding). A single entry describes a category against unassigned space inside the model extent, where the normals point away from that category.

  This order is the one that keeps `categories` consistent with `boundary_face` and with volume orientation: in all three, the normal points *away from* the material being described and out into whatever lies beyond it. Reading it the other way would make the single-entry case read a little more naturally, at the cost of disagreeing with the outward convention used everywhere else in this object.

### `"ModelBoundary"`

A surface lying on the boundary of the model extent — introduced where the model was clipped, rather than where the data changes.

* `boundary_face`: Optional. Which face of the extent the surface lies on, named by the axis and direction its outward normal points along: `"NegativeX"`, `"PositiveX"`, `"NegativeY"`, `"PositiveY"`, `"NegativeZ"` or `"PositiveZ"`. `"NegativeX"` is the face at the extent's minimum X, whose outward normal points along negative X.

  The axes are those of the model extent. For a model built on a rotated grid they are given by [`extent_rotation`](#extent_rotation); otherwise they are the axes of the object's [coordinate reference system](../components/crs.md). Omit `boundary_face` when the surface spans more than one face or the producer cannot attribute it to one. A `"NoData"` surface never carries one, because it is not a `"ModelBoundary"` surface at all.

* `category`: Optional key into [`category_lookup`](#category_lookup) identifying the category whose region the surface closes. A categorical model clipped by its extent has one such closure per category per face, carrying both `category` and `boundary_face` — for example the part of the extent's minimum-X face that closes the granite region. Omit it in a model without categories.

Together the `"ModelBoundary"` and `"NoData"` surfaces cover the model hull, the same geometry as [`boundary_volume`](#boundary_volume), whichever kind of model it is. A consumer can therefore treat the extent of a scalar model and of a categorical model in the same way, and use `category` and `boundary_face` only to label the pieces.

### `"NoData"`

A surface closing the model where the source data was absent. It is geometrically part of the model hull but is not a real contact, and a consumer should not present it as one.

This arises where a scalar field is undefined over part of the extent — the usual case being isosurfacing output over sparse data. A categorical model does not normally need it, because absent data is naturally represented as a category of its own with an ordinary `"CategoryBoundary"` around it.

### `"Generic"`

A surface that is part of the model but is none of the kinds above. It carries no data beyond the common properties.

It is intended for meshes kept alongside a model for context — a topographic surface, or a wireframe imported from elsewhere — where no threshold, category or extent face applies. A consumer can display it, but can draw no inference from it, so prefer a more specific kind wherever one fits. It is a fallback, not a default.

### `surface_attributes`

Attributes associated with each surface. Attribute tables have one row per surface.

## `volumes` *array*

Closed volumes in the model. May be empty, subject to the same caveat as `surfaces`. A volume's parts must together form a closed hull. Every volume has:

* `name`, `description`, `quality`, `parts`, `material_key`: As for surfaces.

* `volume_type`: Required kind of volume, which selects the properties below.

### `"IsoVolume"`

A band of the scalar field — the material between two consecutive grade shells, for example.

The iso-volumes of a model are **bands that partition the extent without overlap**: at most one between each pair of consecutive thresholds, plus the open-ended bands below the lowest threshold and above the highest. A band that would enclose nothing is omitted.

* `lower_bound`: Optional inclusive lower bound of the range enclosed, in the model's [`bounds_unit`](#bounds_unit). Absent if unbounded below.

* `upper_bound`: Optional exclusive upper bound of the range enclosed, in the model's [`bounds_unit`](#bounds_unit). Absent if unbounded above.

At least one bound must be present; an iso-volume with neither constrains nothing. Which bounds are present gives the kind of volume:

| `lower_bound` | `upper_bound` | Meaning |
|---|---|---|
| absent | present | The lowest band — everything below the lowest threshold |
| present | present | The band between two consecutive thresholds |
| present | absent | The highest band — everything above the highest threshold |

Cumulative volumes are **not** published. "Everything below 1.0 g/t" in a model that also has a 0.5 g/t shell would overlap the bands, and "everything below 0.5 g/t" would duplicate the lowest band exactly, with nothing in the file to tell the copies apart. A consumer that needs a cumulative view builds it from the bands instead. Everything below threshold *t* is the union of the bands whose `upper_bound` is at most *t*: collect their part references and drop every part that appears once as it is and once reversed. Those are the isosurfaces between adjacent bands, now interior to the union, and what remains is a closed, outward-facing hull. Everything above *t* is built the same way from the bands whose `lower_bound` is at least *t*.

The range is **half-open** — inclusive below, exclusive above — so that the bands tile the scalar range with no gap and no overlap. One consequence is worth spelling out: a volume with an `upper_bound` of `5` does not formally include the value `5` itself. That value is the isosurface bounding the volume, and a surface encloses no volume, so nothing is actually lost. The alternative — letting a producer mark each bound inclusive or exclusive independently — would make the tiling property unenforceable and oblige every consumer to handle both conventions, for no gain in what can be expressed.

### `"CategoryRegion"`

The region occupied by one category of a categorical model, such as a lithological domain.

* `category`: **Required.** Key into [`category_lookup`](#category_lookup) for the category enclosed. A volume encloses exactly one category.

### `"ModelBoundary"`

The extent of the model itself, as a closed volume. A model has at most one, and it is the volume that [`boundary_volume`](#boundary_volume) points at. It carries no data beyond the common properties.

### `"Generic"`

A closed region that is part of the model but is none of the kinds above — an imported solid carried for context, for instance. As with a `"Generic"` surface, a consumer can display it but can infer nothing from it, so prefer a more specific kind wherever one fits.

### `volume_attributes`

Attributes associated with each volume. Attribute tables have one row per volume.

## `bounds_unit`

The [unit](../elements/unit.md) of measure of every `bound`, `lower_bound` and `upper_bound` in the model — for example `"g/t"` for grade shells, `"ohm.m"` for a resistivity model, or `"m"` for an elevation cut.

A single model-level unit is sufficient because all bounds derive from one scalar field. Omit it when the bounds are dimensionless, or when the producer does not know the unit — in which case a consumer must treat the bounds as opaque numbers and must not convert or label them.

A purely categorical model has no bounds and omits this property.

## `bounds_attribute`

Optional name of the scalar attribute the bounds are measured on — for example `"Au"`. `bounds_unit` says what the numbers are measured in; this says what is being measured, so that a consumer can label the model as "Au 0.5 g/t" rather than just "0.5 g/t". Use [`lineage`](../components/lineage.md) to link to the source object itself.

## `category_lookup`

Maps the integer keys used by `categories` and `category` to their names. Required if any surface or volume specifies a category — a `"CategoryBoundary"` surface, a `"CategoryRegion"` volume, or a `"ModelBoundary"` surface with a `category`.

Keys are normally those of the categorical attribute the model was built from, carried through unchanged, so that a consumer can join the model back to its source grid or block model. The table may contain keys that no surface or volume references — a category present in the source data but absent from this model extent.

A volume encloses exactly one category, never a list. Where a producer groups several source categories into a single published domain, that domain becomes a category in its own right, with its own key and name in this table, and the volume references that key. A consumer therefore cannot assume that every key here also exists in the source data. The alternative of listing several categories against one volume is ambiguous — there is no way to tell "all of these apply throughout this region" from "this region is those regions merged" — which is why a single key is the only form allowed.

## `category_attribute`

Optional name of the categorical attribute the model was built from — for example `"Lithology"` — whose keys [`category_lookup`](#category_lookup) resolves. It plays the same role for categories that [`bounds_attribute`](#bounds_attribute) plays for bounds; a combined model carries both.

## `materials`

Optional [materials](../components/material.md) describing how surfaces and volumes should be presented — a `key`, a `name` and a `color`. Surfaces and volumes reference an entry by its `material_key`. Keys must be unique within the array.

Materials are presentation metadata and carry no geometric or analytical meaning. Isosurfacing output typically omits them; interpreted and combined models use them to preserve a model's appearance across applications.

## `folders`

An optional recursive tree organising the model for presentation. Each folder has a `name` and an `items` array, where each item is either a nested folder, a `{ "volume_index": n }` reference, or a `{ "surface_index": n }` reference.

Folders hold indices only, never geometry. They need not cover every surface and volume, and a surface or volume may appear in more than one folder. Consumers that do not present a tree can ignore them entirely.

## `extent_rotation`

Optional [rotation](../components/rotation.md) giving the orientation of the model extent's axes, for a model built on a rotated grid. It uses the same `dip_azimuth`, `dip` and `pitch` convention as the grid objects, so a producer copies the source grid's rotation across unchanged.

It only defines the axes that [`boundary_face`](#modelboundary) names faces against. Vertices remain in the coordinate reference system and are never rotated by it. Omit it when the extent is aligned with the axes of the coordinate reference system.

## `boundary_volume`

Index into `volumes` of the volume whose hull is the boundary of the model extent. That volume has a `volume_type` of `"ModelBoundary"`. Omit it when the model does not publish its extent as a volume.

The hull need not be simply connected. Where the source data was absent over an interior region, the model has an interior void, and the boundary volume's hull then consists of an outer shell plus one inner shell per void. The inner shells follow the same rule as every other closed volume — fronts facing outwards, away from the enclosed region — which here means facing *into* the void, since the void lies outside the model. The surfaces making up those inner shells are `"NoData"` surfaces, not `"ModelBoundary"` ones: they mark the edge of the data, not the edge of the extent.

## Properties

<FlatProperties />

::mermaid[../generated/uml/volumetric-model-meshes-1.0.0.mmd]
