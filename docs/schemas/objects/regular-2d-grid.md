---
seoTitle: regular-2d-grid Object for Evo Schemas | Seequent Developer
description: Review the regular 2d grid object schema for Geoscience Objects, supporting consistent data structures and reliable Seequent Evo workflows.
---

import OverlineWithVersion from '@theme/OverlineWithVersion';
import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/objects/regular-2d-grid-1.3.0.md';

<OverlineWithVersion title="Geoscience Objects" version="1.3.0" badge="supported" />

# regular-2d-grid

<SchemaUri uri="schema/objects/regular-2d-grid/1.3.0/regular-2d-grid.schema.json" />

Represents a regularly-sampled two-dimensional grid (i.e., image) and data attached to the cells and vertices. Regular grids have uniform cell dimensions throughout — use a [tensor-2d-grid](tensor-2d-grid.md) when variable cell sizes are needed (e.g., for local refinement or stretched grids).

The grid implements spatial properties including a coordinate reference system and bounding box in world coordinates.

The grid origin is defined in three dimensions, along with `rotation` (defined per the Rotation schema component). The origin coordinates are expressed in the axes of the object's `coordinate_reference_system`, following that CRS's declared axis order — see [Coordinate reference systems and axis order](../../understanding-schemas/coordinate-reference-systems.md).

The size of the grid is specified in cells (see `size`), each of which has the same rectangular dimensions (see `cell_size`) throughout the grid.

Fields `cell_attributes` and `vertex_attributes` accept a variety of scalar values (see One of Attribute component), attached to either the cells (of length `grid_size_x * grid_size_y`) or vertices (of length `[grid_size_x + 1] * [grid_size_y + 1]`).

**See also:** [regular-3d-grid](regular-3d-grid.md) (3D counterpart), [tensor-2d-grid](tensor-2d-grid.md) (variable cell sizes).

## Properties

<FlatProperties />

::mermaid[../generated/uml/regular-2d-grid-1.3.0.mmd]
