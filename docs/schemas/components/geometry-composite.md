import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/geometry-composite-1.0.1.md';

# geometry-composite

<SchemaUri uri="schema/components/geometry-composite/1.0.1/geometry-composite.schema.json" />

The `geometry-composite` component groups multiple geometry types into a single composite:

* `brep_container` — An optional [brep-container](brep-container.md).
* `mesh` — An optional [embedded-triangulated-mesh](embedded-triangulated-mesh.md).
* `points_2d` — Optional 2D point coordinates.
* `polylines_2d` — Optional 2D polylines.
* `points_3d` — Optional 3D point coordinates.
* `polylines_3d` — Optional 3D polylines.

## Properties

<FlatProperties />
