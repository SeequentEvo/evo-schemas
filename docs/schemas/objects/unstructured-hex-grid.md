import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/unstructured-hex-grid-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# unstructured-hex-grid

<SchemaUri uri="schema/objects/unstructured-hex-grid/1.3.0/unstructured-hex-grid.schema.json" />

**Key components:**
- [hexahedrons](../components/hexahedrons.md) — Hexahedral cell vertices and connectivity

**See also:** [unstructured-grid](unstructured-grid.md) (arbitrary cell shapes), [unstructured-quad-grid](unstructured-quad-grid.md) (quadrilateral cells), [unstructured-tet-grid](unstructured-tet-grid.md) (tetrahedral cells).

## Overview

Represents an unstructured hexahedral grid where cells are hexahedrons.

The grid implements spatial properties including a coordinate reference system and bounding box in world coordinates.

The grid's data are all stored on the `hexahedrons` attribute, which defines the spatial layout of the grid, including the coordinates of the vertices and the connectivity between them to form hexahedral cells.

## Properties

<FlatProperties />

::mermaid[../generated/uml/unstructured-hex-grid-1.3.0.mmd]
