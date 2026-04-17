import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/unstructured-quad-grid-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# unstructured-quad-grid

<SchemaUri uri="schema/objects/unstructured-quad-grid/1.3.0/unstructured-quad-grid.schema.json" />

**Key components:**
- [quadrilaterals](../components/quadrilaterals.md) — Quadrilateral cell vertices and connectivity

**See also:** [unstructured-grid](unstructured-grid.md) (arbitrary cell shapes), [unstructured-hex-grid](unstructured-hex-grid.md) (hexahedral cells), [unstructured-tet-grid](unstructured-tet-grid.md) (tetrahedral cells).

## Overview

Represents an unstructured grid where cells are quadrilaterals.

The grid implements spatial properties including a coordinate reference system and bounding box in world coordinates.

The grid's data are all stored on the `quadrilaterals` attribute, which defines the spatial layout of the grid, including the coordinates of the vertices and the connectivity between them to form quadrilateral cells.

## Properties

<FlatProperties />

::mermaid[../generated/uml/unstructured-quad-grid-1.3.0.mmd]
