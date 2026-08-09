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

**See also:** [geological-model-meshes](geological-model-meshes.md) (the same structural pattern with geological semantics), [triangle-mesh](triangle-mesh.md) (a single surface on its own).

## Overview

A mesh-based volumetric model: a collection of surfaces and volumes composed from the parts of one shared triangulated mesh. Because every surface and volume references parts of the same mesh, adjacent volumes are conformal — they abut exactly and share their bounding geometry rather than each carrying its own copy of it.

The schema is deliberately generic. Its first use is isosurfacing output — grade shells at a series of thresholds and the volumes between them — but the same object represents categorical domain models, and is intended to grow to cover combined models by adding optional properties and enum values only.

Use [triangle-mesh](triangle-mesh.md) instead when a single surface is all that is needed. Use [geological-model-meshes](geological-model-meshes.md) when the content is geological interpretation with materials and geological feature types.

## `triangle_geometry`

The single shared mesh. See [Understanding parts](../../understanding-schemas/understanding-parts.md) for the semantics of chunks, indices, and the reversal flag.

* `triangles`: The vertices and triangle indices of the mesh.

* `parts`: Chunks of triangles that surfaces and volumes are composed from. `parts` is required on this object.

Parts must be split finely enough that every part is wholly inside or wholly outside every volume. A part is never partially used — partial use is expressed by having more, smaller parts.

## Orientation and winding

Several properties refer to the front and back of a surface. `evo-schemas` does not define a library-wide winding convention, so this object states one explicitly:

* The **front** of a triangle is the side from which its three vertices appear in **counter-clockwise** order. Equivalently, its outward normal is `(v1 - v0) × (v2 - v0)` under the right-hand rule, and points away from the front face.

* A part referenced with [`reversed`](../elements/reversible-index.md) set to `true` has the front and back of its triangles swapped for that reference. The same part can therefore be used front-out by one volume and back-out by the adjacent one, which is what makes the pair conformal.

* A closed volume's parts are oriented so that every triangle's front faces **outwards**, away from the enclosed region.

So for a surface separating two volumes, the normal points out of the volume behind it and into the volume in front of it. This is what `surfaces[].categories` order and `boundary_face` are defined against.

## `surfaces` *array*

Open or closed surfaces in the model. May be empty. Each surface contains:

* `name`: Object name.

* `description`: Optional additional description of this surface.

* `quality`: Optional hint about mesh [quality](../components/mesh-quality.md) characteristics.

* `parts`: The mesh parts that make up this surface, and whether traversal order within each part is reversed.

* `surface_type`: Optional kind of surface. One of
  - `"Isosurface"` — extracted at a scalar threshold
  - `"CategoryBoundary"` — a contact between two categories
  - `"ModelBoundary"` — lies on the boundary of the model extent
  - `"NoData"` — introduced where the source data was absent, so geometrically part of the model hull but not a real contact
  - `"Generic"`

  The set of values is closed in this version and may be extended in a later minor version. A consumer that encounters a value it does not recognise should treat it as `"Generic"` rather than rejecting the surface, so that a model written against a later minor version remains usable.

* `bound`: Optional scalar value the surface was extracted at, in the model's [`bounds_unit`](#bounds_unit). A surface is extracted at a single threshold, so it carries one value rather than a range. Absent for surfaces that are not extracted at a threshold, such as model extent faces and category boundaries.

* `categories`: Optional keys into `category_lookup`, ordered so that the triangle normals point **from `categories[0]` towards `categories[1]`** — the first entry is the category behind the surface, the second the category in front of it, as defined under [Orientation and winding](#orientation-and-winding). One entry for a category against unassigned or out-of-model space, where the normals point away from that category and out of the model.

* `boundary_face`: For a surface on the model extent, which face it lies on, named by the axis and direction that face points along: `"NegativeX"`, `"PositiveX"`, `"NegativeY"`, `"PositiveY"`, `"NegativeZ"` or `"PositiveZ"`. The axes are those of the extent itself, so for a rotated extent they are the rotated axes rather than those of the coordinate reference system. `"NegativeX"` is the face at the extent's minimum X, whose outward normal points along negative X. Omit it on a boundary surface that spans more than one face, or that the producer cannot attribute to a single face — a `"NoData"` patch, for instance, never carries one.

* `material_key`: Optional key of an entry in `materials`, matching [geological-model-meshes](geological-model-meshes.md), where surfaces carry a material as well as volumes. Isosurfacing output normally omits it; interpreted models use it to preserve a surface's appearance.

### `surface_attributes`

Attributes associated with each surface. Attribute tables have one row per surface.

## `volumes` *array*

Closed volumes in the model. May be empty. A volume's parts must together form a closed hull. Each volume contains:

* `name`, `description`, `quality`, `parts`: As for surfaces.

* `volume_type`: Optional kind of volume. One of `"IsoVolume"`, `"CategoryRegion"`, `"ModelBoundary"` or `"Generic"`. As for `surface_type`, the set is closed in this version and a consumer should treat an unrecognised value as `"Generic"`.

* `lower_bound`: Optional inclusive lower bound of the scalar range enclosed, in the model's [`bounds_unit`](#bounds_unit). Absent if unbounded below.

* `upper_bound`: Optional exclusive upper bound of the scalar range enclosed, in the model's [`bounds_unit`](#bounds_unit). Absent if unbounded above.

* `category`: Optional key into `category_lookup` for the category enclosed. A volume encloses exactly one category. A domain that merges several source categories is represented as a category of its own, added to `category_lookup`, rather than as a list.

* `material_key`: Optional key of an entry in `materials`.

Because the bounds are inclusive below and exclusive above, adjacent volumes tile the scalar range without overlap. The kind of iso-volume follows from which bounds are present:

| `lower_bound` | `upper_bound` | Meaning |
|---|---|---|
| absent | present | Everything below the upper bound |
| present | present | Between two thresholds |
| present | absent | Everything above the lower bound |
| absent | absent | Unbounded in the scalar dimension — for example the model extent |

### `volume_attributes`

Attributes associated with each volume. Attribute tables have one row per volume.

## Relating surfaces to volumes

Parts are the only linkage between a surface and a volume — there are no index references from one to the other. A surface and a volume are related exactly when their sets of part indices intersect.

That intersection may be partial. A volume does **not** necessarily contain a whole surface: a model-extent surface is typically cut into patches by the isosurfaces crossing it, and each volume uses only the patches that bound it. An isosurface, by contrast, is normally shared in full by exactly two volumes with opposite `reversed` flags — which is what makes the volumes watertight where they meet.

## `bounds_unit`

The [unit](../elements/unit.md) of measure of every `bound`, `lower_bound` and `upper_bound` in the model — for example `"g/t"` for grade shells, `"ohm.m"` for a resistivity model, or `"m"` for an elevation cut.

A single model-level unit is sufficient because all bounds derive from one scalar field. Omit it when the bounds are dimensionless, or when the producer does not know the unit — in which case a consumer must treat the bounds as opaque numbers and must not convert or label them.

A purely categorical model has no bounds and omits this property.

## `category_lookup`

Maps the integer keys used by `categories` and `category` to their names. Required if any surface specifies `categories` or any volume specifies `category`.

The keys are those of the categorical attribute the model was built from, carried through unchanged, so that a consumer can join the model back to its source grid or block model. The table may contain keys that no surface or volume references — a category present in the source data but absent from this model extent.

## `materials`

Optional [materials](../components/material.md) describing how surfaces and volumes should be presented — a `key`, a `name` and a `color`. Surfaces and volumes reference an entry by its `material_key`. Keys must be unique within the array.

Materials are presentation metadata and carry no geometric or analytical meaning. Isosurfacing output typically omits them; interpreted and combined models use them to preserve a model's appearance across applications.

## `folders`

An optional recursive tree organising the model for presentation. Each folder has a `name` and an `items` array, where each item is either a nested folder, a `{ "volume_index": n }` reference, or a `{ "surface_index": n }` reference.

Folders hold indices only, never geometry. They need not cover every surface and volume, and a surface or volume may appear in more than one folder. Consumers that do not present a tree can ignore them entirely.

## Index groupings

Six optional properties provide named, ordered access into `surfaces` and `volumes`. They hold indices only — no geometry and no metadata of their own.

* `isosurfaces`: Indices into `surfaces` of the surfaces with `surface_type` of `"Isosurface"`, ordered by `bound` ascending.

* `boundary_surfaces`: Indices into `surfaces` of the surfaces with `surface_type` of `"ModelBoundary"` or `"NoData"` — together, the model hull.

* `volumes_below`: Indices into `volumes` of the volumes that specify `upper_bound` and not `lower_bound`, ordered by `upper_bound` ascending.

* `volumes_between`: Indices into `volumes` of the volumes that specify both bounds, ordered by `lower_bound` ascending.

* `volumes_above`: Indices into `volumes` of the volumes that specify `lower_bound` and not `upper_bound`, ordered by `lower_bound` ascending.

* `boundary_volume`: Index into `volumes` of the closed hull of the model extent.

The per-item metadata — `surface_type`, `boundary_face`, and the presence of `bound`, `lower_bound` and `upper_bound` — is the single normative source. Each grouping is a **derived index** over it: a producer may omit a grouping entirely, but a grouping that is present must be **exhaustive** — it must list every item matching its criterion and no others.

Note that `volumes_between` covers only volumes with **both** bounds. A volume unbounded below belongs in `volumes_below` and one unbounded above in `volumes_above`, however the producer happened to generate it.

That rule is what keeps the two routes to the same answer in agreement. A consumer that reads a grouping and a consumer that filters `surfaces` or `volumes` directly always obtain the same set; the grouping adds only the producer's ordering. If exhaustiveness were optional the two routes could disagree, and since JSON Schema cannot enforce cross-property invariants there would be no way to tell which was intended.

## Properties

<FlatProperties />

::mermaid[../generated/uml/volumetric-model-meshes-1.0.0.mmd]
