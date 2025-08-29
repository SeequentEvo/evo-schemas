import CheckIcon from '@mui/icons-material/Check';
import Chip from '@mui/material/Chip';
import Grid from '@mui/material/Grid';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/regular-2d-grid-1.3.0.md';

<Grid container>
# regular-2d-grid
<Chip color="info" icon={<CheckIcon />} label="Supported" style={{margin: '0.75em'}} />
</Grid>
<SchemaUri uri="schema/objects/regular-2d-grid/1.3.0/regular-2d-grid.schema.json" />

Represents a regularly-sampled two-dimensional grid (i.e., image) and data attached to the cells and vertices.

The grid implements spatial properties including a coordinate reference system and bounding box in world coordinates.

The grid origin is defined in three dimensions, along with `rotation` (defined per the Rotation schema component).

The size of the grid is specified in cells (see `size`), each of which has the same rectangular dimensions (see `cell_size`) throughout the grid.

Fields `cell_attributes` and `vertex_attributes` accept a variety of scalar values (see One of Attribute component), attached to either the cells (of length `grid_size_x * grid_size_y`) or vertices (of length `[grid_size_x + 1] * [grid_size_y + 1]`).

See also:

- For a 3D grid, see [`regular-3d-grid`](regular-3d-grid.md).
- For a 2D grid with variable cell sizes, see [`tensor-2d-grid`](tensor-2d-grid.md).

## Properties

<FlatProperties />

::mermaid[_generated/uml/regular-2d-grid-1.3.0.mmd]
