import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/regular-3d-grid-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# regular-3d-grid

<SchemaUri uri="schema/objects/regular-3d-grid/1.3.0/regular-3d-grid.schema.json" />

Represents a regularly-sampled three-dimensional grid (i.e., image) and data attached to the cells and vertices.

The grid implements spatial properties including a coordinate reference system and bounding box in world coordinates.

The grid origin is defined in three dimensions, along with `rotation` (defined per the Rotation schema component).

The size of the grid is specified in cells (see `size`), each of which has the same length, width and height (see `cell_size`) throughout the grid.

Fields `cell_attributes` and `vertex_attributes` provide an optional [attribute list](../understanding-schemas/understanding-attributes.md) attached to either the cells (of length `grid_size_x * grid_size_y * grid_size_z`) or vertices (of length `[grid_size_x + 1] * [grid_size_y + 1] * [grid_size_z + 1]`).

See also:

- For a 2D grid, see [`regular-2d-grid`](regular-2d-grid.md).
- For a 3D grid with data defined on only some cells, see [`regular-masked-3d-grid`](regular-masked-3d-grid.md).
- For a 3D grid with variable cell sizes, see [`tensor-3d-grid`](tensor-3d-grid.md).

## Properties

<FlatProperties />

::mermaid[_generated/uml/regular-3d-grid-1.3.0.mmd]
