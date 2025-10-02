import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/unstructured-quad-grid-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# unstructured-quad-grid

<SchemaUri uri="schema/objects/unstructured-quad-grid/1.3.0/unstructured-quad-grid.schema.json" />

Represents an unstructured grid where cells are quadrilaterals.

The grid implements spatial properties including a coordinate reference system and bounding box in world coordinates.

The grid's data are all stored on the `quadrilaterals` attribute, which defines the spatial layout of the grid, including the coordinates of the vertices and the connectivity between them to form quadrilateral cells.

See also:

- For an unstructured grid with arbitrary shapes, see [`unstructured-grid`](unstructured-grid.md).
- For an unstructured hexahedral grid, see [`unstructured-hex-grid`](unstructured-hex-grid.md).
- For an unstructured tetrahedral grid, see [`unstructured-tet-grid`](unstructured-tet-grid.md).

## Properties

<FlatProperties />

::mermaid[_generated/uml/unstructured-quad-grid-1.3.0.mmd]
