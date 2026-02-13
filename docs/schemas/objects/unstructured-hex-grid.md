import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/unstructured-hex-grid-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# unstructured-hex-grid

<SchemaUri uri="schema/objects/unstructured-hex-grid/1.3.0/unstructured-hex-grid.schema.json" />

Represents an unstructured hexahedral grid where cells are hexahedrons.

The grid implements spatial properties including a coordinate reference system and bounding box in world coordinates.

The grid's data are all stored on the `hexahedrons` attribute, which defines the spatial layout of the grid, including the coordinates of the vertices and the connectivity between them to form hexahedral cells.

See also:

- For an unstructured grid with arbitrary shapes, see [`unstructured-grid`](unstructured-grid.md).
- For an unstructured quadrilateral grid, see [`unstructured-quad-grid`](unstructured-quad-grid.md).
- For an unstructured tetrahedral grid, see [`unstructured-tet-grid`](unstructured-tet-grid.md).

## Properties

<FlatProperties />

::mermaid[../generated/uml/unstructured-hex-grid-1.3.0.mmd]
