import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/design-geometry-1.1.0.md';

# design-geometry

<SchemaUri uri="schema/objects/design-geometry/1.1.0/design-geometry.schema.json" />

A design geometry describes either a 2D planar or 3D geometry suitable for use in a numerical model. Design geometry objects can contain both geology and engineering objects like a plates or anchors.
- A 3D geometry can contain 2D parts with an associated transform to place them in 3D space.
- A 2D geometry does not support 3D parts. All parts of a 2D geometry should be on the same plane.

Geometries are decomposed into Parts, each part describes one "thing" - a soil volume, a plate, an anchor, etc. Parts optionally reference a material. The same material can be used in multiple parts.

The design-geometry representation encourages using connected parts for common objects. (e.g. adjacent polygons share common vertices instead of using duplicate overlapping vertices). The intent is support of lossless data transfer for numerical models allowing consumers to avoid non-deterministic numerical tests using a tolerance to detect adjacent (touching) parts.

## `parts` *array*

 A collection of geometry-part, each part describes a “thing” in the geometry. It could be a soil volume, a plate, an anchor, etc. We expect design geometries to be made of many small "parts" that when combined describe the geometry as a whole.

 A part can even be composed from other parts for templating. That is we can stamp out the same part multiple times at different locations in space. e.g. stamp out multiple instances of a soil anchor at different locations along a retaining wall.

A part has a unique id (its “key”).

Parts may or may not be connected. When connected, they share vertices with other parts.

Fields:

* `key`: unique identifier for the part. No two parts in a design-geometry share the same key.

* `name`: user friendly name for the part. The name is not guaranteed to be unique from other geometry-part’s.

* `data_source`: If a BRep/mesh is generated from another Evo object, the data source link is useful to support automation workflows. Placing the data_source in the part extends this concept to other objects.

  Example use cases:
  - auto update a model on change to bore hole logs
  - auto update cross section when leap-frog pushes new cross sections to Evo.

* `feature`: We use the feature as an identifier for the kind of 'thing' represented by the part. The feature is one of:
  - "Void"
  - "Soil"
  - "GMV"
  - "Discontinuity"
  - "Plate"
  - "Geogrid"
  - "Beam"
  - "EmbeddedBeam"
  - "Cable"
- "Anchor"

* `material_key`: unique identifier to a material stored in the design-geometry.

* `transform`: In 3D, both 2D & 3D constituent parts can be combined, where the 2D part is transformed to a location in 3D space. The transform is an affine change of basis represented as a 4x4 transformation matrix flattened in row-major order. The transform is used to map objects described in 2D into 3D space.

    The transformation matrix must be constructed so that [ Transform Matrix ]  *  [ 2D coordinate matrix ] = [3D coordinate matrix ]

    i.e.

    |  Transform Matrix   | *      | 2D col matrix | =      | 3D col matrix |
    | :----:              | :----: | :----:        | :----: | :----:        |
    | tr11 tr12 tr13 tr14 |        |    x          |        | x'            |
    | tr21 tr22 tr23 tr24 |   *    |    y          |   =    | y'            |
    | tr31 tr32 tr33 tr34 |        |    0          |        | z'            |
    | tr41 tr42 tr43 tr44 |        |    1          |        | 1             |

* `bounding_box`: Bounding box of this part.

* `layer`: The layer concept comes from 2D CAD products that often store geometry on multiple layers. A layer lets us easily represent a tunnel or hole without intersecting it with the surrounding domain. Another idea is to use layers to represent staged construction sequences. The intention is that separate layers do not connect with each other - they overlap in space.

* `color`: Default color if not otherwise overridden. The color normally comes from the associated material, the part color is only used if no material is assigned.

* `geometry`: The geometry definition for this part. The number of constituent shapes in any given part are typically small as the part represents a single “thing” (e.g. a single soil layer)

    A geometry is composed of one of :

  - part_key: String used to lookup another part by its key. Having a part reference to another part allows parts to be built from simpler constituents, and templating of parts allows the same part can be stamped out in multiple locations.
  - [brep__container](#brep-container): A Brep stored in a well known Brep form.
  - [mesh](#surface-mesh): A surface mesh (triangulated mesh in 3D space). the mesh can either be open (a surface) or closed (a volume)
  - points_2d: list of points in 2D space, represented using an array of 0-based indices into the vertices_2d table.
  - [polylines_2d](#polyline-2d): connected list of line segments in 2D space.
  - points_3d: list of points in 3D space, represented using an array of 0-based indices into the vertices_3d table.
  - [polylines_3d](#polyline-3d): connected list of line segments in 3D space.

### brep-container

A 3D object represented in a Brep form. Brep is short for Boundary representation . The Brep is stored as a blob using the supplied format.

Fields:

* `format`: The BRep storage format used. (e.g. ‘RAW’, ‘STEP’, ‘DWG’, etc.).

    There is no "lossless" format that interop's with all geometry kernels. This makes designing a common format challenging.

    Even "STEP", an ISO-standard format whose entire reason for existence is interop between various geometry kernels may require a data transformation to convert to another BRep representation. Numerical artifacts from the transformation can result. STEP is also missing a structure to represent modern "convergent" models that merge parametric and discretized objects together. Each kernel seems to do this in its own way.

    Instead of trying to support generic BRep interop, the "RAW" format is intended to hold BReps with a format native to some kernel (the producer).

* `producer`: The Kernel is identified with the producer field. E.g. if producer = ‘PLAXIS' we know the blob is in the PLAXIS native format shared by Plaxis and GeoStudio. We wish to support other workflows however, and thus consider other formats that can be consumed using 3rd party API’s. Many kernels (e.g. Autodesk, Parasolid, Rhino, MicroStation) are consumable using common library support.

* `brep`: Brep stored as a blob in the specified format.

* `discretized_brep`: brep blobs cannot be generically consumed without a compatible kernel, so the publisher of the component can also provide a discretized version of the same geometry as in the brep. Information/accuracy is lost, but a discretized representation is more generally consumable (e.g. for visualization).

### surface-mesh

Triangulated “connected” surface mesh in 3D space. A surface can be closed or open, and a closed surface mesh represents a volumetric hull.

Mesh elements can share vertices with other surface-mesh components in the same object.  We do this to encourage conformal meshes that exactly abut adjacent meshes. Using shared vertices makes it easier to validate if a set of meshes are conformal.

Fields:

* `kind`: One of ‘open’ or ‘closed’. If ‘closed’, the mesh represents a volumetric hull. If ‘open’, the mesh is a surface.

* `quality` : Optional hint about mesh [quality](components/mesh-quality.md) characteristics that provide guarantees about the mesh.

* `triangles`: blob containing tuples of 0-based indices used to represent each mesh element. Column names are i, j, k.

### polyline-2d

A 2D object made from a collection of connected line segments. Each entry in the polyline is an index into the lines_2d table. Lines may be straight or curved.

The lines_2d table has three columns (Start, End, ArcCenter). Start/End are indices into vertices_2D for the line endpoints. ArcCenter is the counter-clockwise signed distance from the line center to the arc edge. ArcCenter is optional - typically its NaN or 0.0 for straight lines. Note that because ArcCenter is given counter-clockwise to the line, line endpoint orientation matters to describe the arc.

Fields:

* `begin`: Index of the first line segment in lines__2d.

* `count`: The number of line segments in the polyline.

* `closed`: ‘Closed’ or ‘Open’. ‘Open’ is a polyline, ‘Closed’ is a closed polygon where the first line segment touches the last line segment.

* `shape`: ‘Straight’ or ‘Curved’. Shape is ‘Curved’ if any line segment used in the polyline is curved.

### polyline-3d

A 3D object made of a collection of connected line segments. Line segments are stored in the lines_3d table.

The lines_3d table describes 3D lines. Unlike 2D, 3D lines are never curved. This table has two columns (Start/End) that are indices into vertices_3D for the line endpoints.

In a design-geometry, 3D curved segments are not directly supported, but they can be created using a planar lines-2d-indices with a transform into 3D space, or alternatively be represented as a Brep.

Fields:

* `begin`: Index of the first line segment in lines-3d.

* `count`: The number of line segments in the polyline.

* `closed`: ‘Closed’ or ‘Open’. ‘Open’ is a polyline, ‘Closed’ is a closed polygon where the first line segment touches the last line segment.

## `materials` *array*
 [Materials](components/material.md) referenced by volumes and surfaces.

## Properties

<FlatProperties />

::mermaid[_generated/uml/design-geometry-1.1.0.mmd]
