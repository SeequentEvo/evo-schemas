# Component schemas

Components are reusable building blocks composed into [geoscience object schemas](../index.md). They define shared structures such as coordinate systems, attributes, geometry primitives, and domain-specific data formats.

## Foundational

* [Base object properties](base-object-properties.md) — common fields for all objects (name, uuid, description)
* [Base spatial data properties](base-spatial-data-properties.md) — adds bounding box and CRS to base properties
* [Coordinate reference system](crs.md) — EPSG code or WKT spatial reference
* [Bounding box](bounding-box.md) — axis-aligned geographic extents
* [Lineage](lineage.md) — provenance and processing history
* [Locations](locations.md) — 3D point coordinates

## Attributes

### Core

* [One-of-attribute](one-of-attribute.md) — discriminated union of all attribute types
* [Attribute list property](attribute-list-property.md) — attribute list container
* [Base attribute](base-attribute.md) — common attribute fields (name, key, type)
* [Base continuous attribute](base-continuous-attribute.md) — base for continuous-valued attributes
* [Base category attribute](base-category-attribute.md) — base for categorical attributes
* [Attribute description](attribute-description.md) — metadata for continuous attributes
* [Category attribute description](category-attribute-description.md) — metadata for categorical attributes
* [Category data](category-data.md) — lookup table for categorical values
* [NaN (continuous)](nan-continuous.md) — NaN definitions for floating-point data
* [NaN (categorical)](nan-categorical.md) — NaN definitions for integral data

### Scalar types

* [Continuous attribute](continuous-attribute.md) — floating-point values
* [Integer attribute](integer-attribute.md) — integer values
* [Bool attribute](bool-attribute.md) — boolean values
* [String attribute](string-attribute.md) — string values
* [Color attribute](color-attribute.md) — ABGR colour values
* [Date-time attribute](date-time-attribute.md) — timestamp values
* [Vector attribute](vector-attribute.md) — N-dimensional vectors
* [Indices attribute](indices-attribute.md) — index references to related objects
* [Category attribute](category-attribute.md) — categorical values with lookup table

### Ensembles and time series

* [Continuous ensemble](continuous-ensemble.md) — ensemble of continuous realisations
* [Category ensemble](category-ensemble.md) — ensemble of categorical realisations
* [Continuous time series](continuous-time-series.md) — continuous values over time
* [Category time series](category-time-series.md) — categorical values over time
* [Bool time series](bool-time-series.md) — boolean values over time
* [Time-step attribute](time-step-attribute.md) — time step (date or elapsed)
* [Time-step continuous](time-step-continuous-attribute.md) — elapsed-time continuous values
* [Time-step date-time](time-step-date-time-attribute.md) — timestamped date-time values
* [Channel attribute](channel-attribute.md) — multi-channel survey data

## Geometry

### Vertices and meshes

* [Vertices 2D](vertices-2d.md) — 2D vertex coordinates
* [Vertices 3D](vertices-3d.md) — 3D vertex coordinates
* [Triangles](triangles.md) — triangle connectivity and vertices
* [Quadrilaterals](quadrilaterals.md) — quadrilateral cells
* [Hexahedrons](hexahedrons.md) — hexahedral (brick) cells
* [Tetrahedra](tetrahedra.md) — tetrahedral cells
* [Segments](segments.md) — line segments
* [Surface mesh](surface-mesh.md) — triangulated surface (open or closed)
* [Mesh quality](mesh-quality.md) — quality guarantees for meshes
* [Unstructured grid geometry](unstructured-grid-geometry.md) — vertices, cells, and connectivity

### Lines and polylines

* [Polyline 2D](polyline-2d.md) — 2D polyline
* [Polyline 3D](polyline-3d.md) — 3D polyline
* [2D line indices](lines-2d-indices.md) — 2D line endpoints with arc support
* [3D line indices](lines-3d-indices.md) — 3D line endpoints

### Composite and embedded geometry

* [Embedded triangulated mesh](embedded-triangulated-mesh.md) — mesh with optional parts
* [Geometry composite](geometry-composite.md) — grouped geometry types
* [Geometry part](geometry-part.md) — named part within a composite
* [Embedded line geometry](embedded-line-geometry.md) — polylines from line segments
* [Embedded mesh object](embedded-mesh-object.md) — named mesh referencing parts
* [Embedded polyline object](embedded-polyline-object.md) — named polyline referencing parts
* [BRep container](brep-container.md) — boundary representation model

## Tabular data

* [Data table](data-table.md) — named table of attributes
* [Interval table](interval-table.md) — interval data with attributes
* [Distance table](distance-table.md) — distance-based data
* [Intervals](intervals.md) — depth or distance ranges
* [From-to](from-to.md) — from-to depth ranges
* [Lengths](lengths.md) — segment or interval lengths

## Drilling

* [Hole collars](hole-collars.md) — drillhole surface locations
* [Hole chunks](hole-chunks.md) — row associations for drillhole data
* [Desurvey method](desurvey-method.md) — drillhole path interpolation algorithm
* [Downhole attributes](downhole-attributes.md) — attributes along drillhole traces
* [Downhole direction vector](downhole-direction-vector.md) — segment direction and length

## Orientation data

* [Rotation](rotation.md) — 3D rotation (dip azimuth, dip, pitch)
* [Lineation data](lineation-data.md) — lineation measurements at locations
* [Planar data](planar-data.md) — planar orientation measurements at locations
* [Relative lineation data table](relative-lineation-data-table.md) — lineation data relative to drillholes
* [Relative planar data table](relative-planar-data-table.md) — planar data relative to drillholes
* [Ellipsoid](ellipsoid.md) — single ellipsoid (anisotropy)
* [Ellipsoids](ellipsoids.md) — spatially varying ellipsoids
* [Material](material.md) — material identity and colour

## Block model structures

* [Block model attribute](block-model-attribute.md) — continuous attribute for block models
* [Block model category attribute](block-model-category-attribute.md) — categorical attribute for block models
* [Regular structure](block-model-regular-structure.md) — uniform grid, no subblocking
* [Flexible structure](block-model-flexible-structure.md) — variable-size subblocks within parent blocks
* [Fully subblocked structure](block-model-fully-subblocked-structure.md) — all-or-nothing subblocking
* [Variable octree structure](block-model-variable-octree-structure.md) — octree-based anisotropic refinement

## Survey and geophysics

* [Survey line](survey-line.md) — spatial path of survey measurements
* [Survey collection](survey-collection.md) — grouped survey data
* [Survey attribute](survey-attribute.md) — survey data values
* [Survey attribute definition](survey-attribute-definition.md) — survey attribute metadata
* [Fiducial description](fiducial-description.md) — spatial reference markers
* [Resistivity-IP line](resistivity-ip-line.md) — resistivity-IP survey line
* [Resistivity-IP DCIP properties](resistivity-ip-dcip-survey-properties.md) — DC induced polarization
* [Resistivity-IP Phase IP properties](resistivity-ip-phaseip-survey-properties.md) — phase induced polarization
* [Resistivity-IP SIP properties](resistivity-ip-sip-survey-properties.md) — spectral induced polarization
* [Resistivity-IP pole-dipole config](resistivity-ip-pldp-configuration-properties.md) — pole-dipole electrodes
* [Resistivity-IP pole-pole config](resistivity-ip-plpl-configuration-properties.md) — pole-pole electrodes
* [FDEM channel](frequency-domain-electromagnetic-channel.md) — frequency-domain EM channel
* [TDEM channel](time-domain-electromagnetic-channel.md) — time-domain EM channel

## Statistics

* [Cumulative distribution function](cumulative-distribution-function.md) — empirical CDF
* [Spherical variogram](variogram-spherical-structure.md) — spherical model
* [Exponential variogram](variogram-exponential-structure.md) — exponential model
* [Gaussian variogram](variogram-gaussian-structure.md) — Gaussian model
* [Cubic variogram](variogram-cubic-structure.md) — cubic model
* [Linear variogram](variogram-linear-structure.md) — linear model
* [Generalised Cauchy variogram](variogram-generalisedcauchy-structure.md) — generalised Cauchy model
* [Spheroidal variogram](variogram-spheroidal-structure.md) — spheroidal model
