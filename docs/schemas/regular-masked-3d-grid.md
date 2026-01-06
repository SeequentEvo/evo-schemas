import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './generated/flatmd/objects/regular-masked-3d-grid-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# regular-masked-3d-grid

<SchemaUri uri="schema/objects/regular-masked-3d-grid/1.3.0/regular-masked-3d-grid.schema.json" />

The regular-masked-3d-grid object captures the geometry and attributes of a regular grid with inactive cells. This object is used to represent a 3D grid where only active cells are considered for attribute properties. As a result, the size of the attribute data can be much smaller than the underlying regular grid.

This object is particularly useful in geological and geostatistical analysis when working with a sub-space of a regular grid, such as a domain or a mining pit. It eliminates the need to externally track which cells are inside or outside the region of interest.

To define the regular masked 3D grid, the object requires:

- The dimensions of the grid in number of cells.
- The coordinates of the origin [x, y, z].
- The size of each cell in the grid [cell_size_x, cell_size_y, cell_size_z].
- A mask (boolean array) indicating active and inactive cells.
- The number of active cells, which corresponds to the number of true elements in the mask.
- The orientation of the grid (defined per the Rotation schema component).

The grid origin is defined in three dimensions, along with rotation. The origin is set at the corner of the grid.

The size of the cells in the grid corresponds to the number of true elements in the boolean mask array. Each cell has the same length, width, and height, as defined by the cell size, throughout the grid.

The cell_attributes field accepts a variety of scalar values (see One of Attribute component), defined for number_of_active_cells (number of true elements in the mask array).

As with all objects, this grid implements spatial properties including a coordinate reference system and bounding box in world coordinates.

See also:

- For a 3D grid with data defined on all cells or vertices, see [`regular-3d-grid`](regular-3d-grid.md).
- For a 3D grid with tensor values, see [`tensor-3d-grid`](tensor-3d-grid.md).

## Properties

<FlatProperties />

::mermaid[generated/uml/regular-masked-3d-grid-1.3.0.mmd]
