# Evo schemas

Geoscience object schemas define the data structures used in the Evo platform. The schema hierarchy is organised into three tiers — objects, components, and elements — each documented in its own section below.

## [Object schemas](objects/index.md)

Objects are the top-level data structures — the entities that consumers create, read, and exchange. Each object describes a complete geoscience dataset, organised into the following categories:

- [Points and surfaces](objects/index.md#points-and-surfaces) — point clouds, triangulated surfaces, and line geometries
- [Grids and block models](objects/index.md#grids-and-block-models) — regular, tensor, and unstructured grid geometries
- [Drilling and downhole data](objects/index.md#drilling-and-downhole-data) — drillhole survey campaigns and downhole measurements
- [Geological modelling](objects/index.md#geological-modelling) — model surfaces, cross-sections, and design geometries
- [Structural geology](objects/index.md#structural-geology) — lineation and planar orientation measurements
- [Survey and geophysics](objects/index.md#survey-and-geophysics) — potential fields, electromagnetic, and resistivity-IP surveys
- [Geostatistics](objects/index.md#geostatistics) — variogram models, distribution functions, and anisotropy ellipsoids

## [Component schemas](components/index.md)

Components are reusable building blocks that objects compose via `allOf`. They define shared structures such as coordinate systems, attribute lists, geometry primitives, and domain-specific data formats.

- [Foundational](components/index.md#foundational) — identity, spatial context, and shared metadata inherited by all objects
- [Attributes](components/index.md#attributes) — typed data arrays, ensembles, and time series
- [Geometry](components/index.md#geometry) — vertices, meshes, lines, polylines, and composite geometry
- [Geoscience disciplines](components/index.md#geoscience-disciplines) — drilling, geological modelling, orientation, block models, geophysics, and geostatistics

## [Element schemas](elements/index.md)

Elements are the lowest-level primitives — typed binary arrays, colour values, spatial coordinates, lookup tables, and the unit system. Components are built from elements.

- [Binary storage](elements/index.md#binary-storage) — binary blob references
- [Typed arrays](elements/index.md#floating-point-arrays) — floating-point, integer, index, boolean, string, and date-time arrays
- [Colour](elements/index.md#colour) — colour values and colour arrays
- [Spatial primitives](elements/index.md#spatial-primitives) — 3D coordinates and reversible index mappings
- [Lookup and categorisation](elements/index.md#lookup-and-categorisation) — lookup tables for categorical data
- [Units](elements/index.md#units) — physical measurement unit definitions
