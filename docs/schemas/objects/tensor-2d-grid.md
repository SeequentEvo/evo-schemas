import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/tensor-2d-grid-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# tensor-2d-grid

<SchemaUri uri="schema/objects/tensor-2d-grid/1.3.0/tensor-2d-grid.schema.json" />

Represents a two-dimensional tensor grid where cells may have different sizes. Tensor grids allow variable cell dimensions along each axis, making them suitable for problems that require local refinement (e.g., finer cells near a feature of interest) or stretched grids for geophysical modelling. For uniform cell sizes, use a [regular-2d-grid](regular-2d-grid.md) instead.

The grid implements spatial properties including a coordinate reference system and bounding box in world coordinates.

The grid origin is defined in three dimensions, along with `rotation` (defined per the Rotation schema component).

The size of the grid is specified in cells (see `size`), with each cell potentially having different dimensions along the x and y axes (see `grid_cells_2d`).

Fields `cell_attributes` and `vertex_attributes` accept a variety of scalar values (see One of Attribute component), attached to either the cells (of length `grid_size_x * grid_size_y`) or vertices (of length `[grid_size_x + 1] * [grid_size_y + 1]`).

**See also:** [tensor-3d-grid](tensor-3d-grid.md) (3D counterpart), [regular-2d-grid](regular-2d-grid.md) (equal cell sizes).

## Properties

<FlatProperties />

::mermaid[../generated/uml/tensor-2d-grid-1.3.0.mmd]
