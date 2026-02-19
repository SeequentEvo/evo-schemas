import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/unstructured-grid-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# unstructured-grid

<SchemaUri uri="schema/objects/unstructured-grid/1.3.0/unstructured-grid.schema.json" />

**Key components:**
- [unstructured-grid-geometry](../components/unstructured-grid-geometry.md) — Vertices, cells, and connectivity indices

**See also:** [unstructured-hex-grid](unstructured-hex-grid.md) (hexahedral cells), [unstructured-quad-grid](unstructured-quad-grid.md) (quadrilateral cells), [unstructured-tet-grid](unstructured-tet-grid.md) (tetrahedral cells).

## Overview

Represents an unstructured grid where cells can have arbitrary shapes and sizes.

The grid implements spatial properties including a coordinate reference system and bounding box in world coordinates.

The grid's data are all stored on the `geometry` attribute, which defines the spatial layout of the grid, including the coordinates of the vertices and the connectivity between them to form cells.

`vertices` - Table of 3D coordinates (x,y,z)
`cells`- Table of cell descriptions. Each entry is an array of triples. The first item in the triple represents the shape, second item is an offset to the indices array and the third item is the number of vertices for the shape. Columns: shape, offset, num_vertices.". See [Cell Type Geometry](../../understanding-schemas/cell-type-geometry.md).

## Properties

<FlatProperties />

::mermaid[../generated/uml/unstructured-grid-1.3.0.mmd]
