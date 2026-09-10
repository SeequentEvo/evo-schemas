---
seoTitle: tetrahedra Component for Evo Schemas | Seequent Developer
description: Review the tetrahedra component schema for Geoscience Objects, supporting consistent data structures and reliable Seequent Evo workflows.
---

import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/tetrahedra-1.2.0.md';

# tetrahedra

<SchemaUri uri="schema/components/tetrahedra/1.2.0/tetrahedra.schema.json" />

The `tetrahedra` component defines a set of tetrahedral cells by their vertices and connectivity.

* `vertices` — An array of 3D coordinates.
* `indices` — An index array of vertex quadruplets, each defining a tetrahedron. Indices are 0-based.

The vertex coordinate columns follow the axis order declared in the object's `coordinate_reference_system` — see [Coordinate reference systems and axis order](../../understanding-schemas/coordinate-reference-systems.md).

**Used by:** [unstructured-tet-grid](../objects/unstructured-tet-grid.md).

**See also:** [triangles](triangles.md), [quadrilaterals](quadrilaterals.md), [hexahedrons](hexahedrons.md), [segments](segments.md) (other cell types).

## Properties

<FlatProperties />
