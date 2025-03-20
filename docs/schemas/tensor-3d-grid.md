import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/tensor-3d-grid-1.3.0.md';

# tensor-3d-grid

<SchemaUri uri="schema/objects/tensor-3d-grid/1.3.0/tensor-3d-grid.schema.json" />

Represents a three-dimensional tensor grid where cells may have different sizes.

The grid implements spatial properties including a coordinate reference system and bounding box in world coordinates.

The grid origin is defined in three dimensions, along with `rotation` (defined per the Rotation schema component).

The size of the grid is specified in cells (see `size`), with each cell potentially having different dimensions along the x, y, and z axes (see `grid_cells_3d`).

Fields `cell_attributes` and `vertex_attributes` accept a variety of scalar values (see One of Attribute component), attached to either the cells (of length `grid_size_x * grid_size_y * grid_size_z`) or vertices (of length `[grid_size_x + 1] * [grid_size_y + 1] * [grid_size_z + 1]`).

See also:

- For a 2D tensor grid, see [`tensor-2d-grid`](tensor-2d-grid.md).
- For a 3D grid with equal cell sizes, see [`regular-3d-grid`](regular-3d-grid.md).

## Properties

<FlatProperties />

::mermaid[_generated/uml/tensor-3d-grid-1.3.0.mmd]
