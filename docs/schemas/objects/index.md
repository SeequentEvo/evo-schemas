# Geoscience object schemas

Object schemas are the top-level data structures in the schema hierarchy. Each object composes reusable [components](../components/index.md), which are in turn built from primitive [elements](../elements/index.md).

## Points and surfaces

Fundamental spatial objects — point clouds, triangulated surfaces, and line geometries.

* [Pointset](pointset.md) — a set of points in space with attributes
* [Triangle mesh](triangle-mesh.md) — a triangulated surface with optional parts and edges
* [Line segments](line-segments.md) — a collection of lines composed of straight segments

## Grids and block models

Regular, tensor, and unstructured grid geometries for spatial discretisation and property modelling.

### Regular grids

* [Regular 2D grid](regular-2d-grid.md) — uniform-cell 2D grid
* [Regular 3D grid](regular-3d-grid.md) — uniform-cell 3D grid
* [Regular masked 3D grid](regular-masked-3d-grid.md) — uniform-cell 3D grid with a cell mask

### Tensor grids

* [Tensor 2D grid](tensor-2d-grid.md) — variable-cell-size 2D grid
* [Tensor 3D grid](tensor-3d-grid.md) — variable-cell-size 3D grid

### Unstructured grids

* [Unstructured grid](unstructured-grid.md) — general unstructured grid
* [Unstructured hex grid](unstructured-hex-grid.md) — hexahedral cells
* [Unstructured quad grid](unstructured-quad-grid.md) — quadrilateral cells
* [Unstructured tet grid](unstructured-tet-grid.md) — tetrahedral cells

## Drilling and downhole data

Drillhole survey campaigns and the data collected along drillhole traces.

* [Drilling campaign](drilling-campaign.md) — planned and interim drillhole data
* [Downhole collection](downhole-collection.md) — a collection of downhole locations
* [Downhole intervals](downhole-intervals.md) — interval data along drillholes

## Geological modelling

Model surfaces, cross-sections, and design geometries used in geological interpretation.

* [Geological model meshes](geological-model-meshes.md) — a collection of geological volumes and surfaces
* [Geological sections](geological-sections.md) — cross-sections composed of polygons and polylines
* [Design geometry](design-geometry.md) — 2D/3D design geometry

## Structural geology

Orientation measurements at point locations — lineation and planar data for structural analysis.

* [Lineations data pointset](lineations-data-pointset.md) — structural lineation measurements
* [Planar data pointset](planar-data-pointset.md) — structural planar measurements

## Survey and geophysics

Geophysical survey data across multiple measurement types — potential fields, electromagnetic, and resistivity-IP.

* Gravity — potential-field gravity survey data
  * [1.2.0](gravity-1.2.0.md)
  * [2.0.0](gravity-2.0.0.md)
* Magnetics — magnetic field survey data
  * [1.2.0](magnetics-1.2.0.md)
  * [2.0.0](magnetics-2.0.0.md)
* Radiometric — radiometric survey data
  * [1.2.0](radiometric-1.2.0.md)
  * [2.0.0](radiometric-2.0.0.md)
* [Resistivity-IP](resistivity-ip.md) — resistivity and induced polarisation data
* [Frequency-domain electromagnetic](frequency-domain-electromagnetic.md) — FDEM survey data
* [Time-domain electromagnetic](time-domain-electromagnetic.md) — TDEM survey data
* [Geophysical records 1D](geophysical-records-1d.md) — 1D geophysical records

## Geostatistics

Variogram models, experimental variograms, distribution functions, and ellipsoid definitions for spatial modelling and uncertainty quantification.

* [Variogram](variogram.md) — variogram model with nugget and structures
* [Experimental variogram](experimental-variogram.md) — spatial continuity statistics by direction and lag
* [Non-parametric continuous cumulative distribution](non-parametric-continuous-cumulative-distribution.md) — empirical CDF
* [Global ellipsoid](global-ellipsoid.md) — single anisotropy ellipsoid
* [Local ellipsoids](local-ellipsoids.md) — spatially varying anisotropy ellipsoids
