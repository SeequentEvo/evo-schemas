import CheckIcon from '@mui/icons-material/Check';
import Chip from '@mui/material/Chip';
import Grid from '@mui/material/Grid';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from './_generated/flatmd/objects/unstructured-tet-grid-1.3.0.md';

<Grid container>
# unstructured-tet-grid
<Chip color="info" icon={<CheckIcon />} label="Supported" style={{margin: '0.75em'}} />
</Grid>
<SchemaUri uri="schema/objects/unstructured-tet-grid/1.3.0/unstructured-tet-grid.schema.json" />

Represents an unstructured tetrahedral grid where cells are tetrahedrons.

The grid implements spatial properties including a coordinate reference system and bounding box in world coordinates.

The grid's data are all stored on the `tetrahedra` attribute, which includes the coordinates and connectivity information between them to form tetrahedral cells.

See also:

- For an unstructured grid with arbitrary shapes, see [`unstructured-grid`](unstructured-grid.md).
- For an unstructured hexahedral grid, see [`unstructured-hex-grid`](unstructured-hex-grid.md).
- For an unstructured quadrilateral grid, see [`unstructured-quad-grid`](unstructured-quad-grid.md).

## Properties

<FlatProperties />

::mermaid[_generated/uml/unstructured-tet-grid-1.3.0.mmd]
