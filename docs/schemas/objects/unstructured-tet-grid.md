import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/unstructured-tet-grid-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# unstructured-tet-grid

<SchemaUri uri="schema/objects/unstructured-tet-grid/1.3.0/unstructured-tet-grid.schema.json" />

**Key components:**
- [tetrahedra](../components/tetrahedra.md) — Tetrahedral cell vertices and connectivity

**See also:** [unstructured-grid](unstructured-grid.md) (arbitrary cell shapes), [unstructured-hex-grid](unstructured-hex-grid.md) (hexahedral cells), [unstructured-quad-grid](unstructured-quad-grid.md) (quadrilateral cells).

## Overview

Represents an unstructured tetrahedral grid where cells are tetrahedrons.

The grid implements spatial properties including a coordinate reference system and bounding box in world coordinates.

The grid's data are all stored on the `tetrahedra` attribute, which includes the coordinates and connectivity information between them to form tetrahedral cells.

## Properties

<FlatProperties />

::mermaid[../generated/uml/unstructured-tet-grid-1.3.0.mmd]
