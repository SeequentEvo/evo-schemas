# Element schemas

Elements are the lowest-level building blocks in the schema hierarchy — primitive data types that [components](../components/index.md) compose into higher-order structures. They define binary array formats, colour values, spatial coordinates, lookup tables, and the unit system.

## Binary storage

The foundational storage reference used by all array elements to point to binary data.

* [Binary blob](binary-blob.md) — file hash, UUID, or null reference for binary data

## Floating-point arrays

64-bit floating-point arrays for continuous numeric data. The base type ([float-array-md](float-array-md.md)) supports arbitrary width; fixed-width specialisations constrain `width` to match specific geometric or physical use cases.

* [Float array (multi-dimensional)](float-array-md.md) — base type with variable width
* [Float array (1D)](float-array-1.md) — scalar values (width = 1)
* [Float array (2D)](float-array-2.md) — paired values such as 2D coordinates (width = 2)
* [Float array (3D)](float-array-3.md) — 3D coordinates and vectors (width = 3)
* [Float array (6D)](float-array-6.md) — symmetric tensor components (width = 6)

## Integer arrays

Integer arrays supporting int32 and int64 encoding. Follows the same base-plus-specialisation pattern as floating-point arrays.

* [Integer array (multi-dimensional)](integer-array-md.md) — base type with variable width
* [Integer array (1D)](integer-array-1.md) — scalar integer values (width = 1)
* [Integer array (2D)](integer-array-2.md) — paired integer values (width = 2)
* [Integer array (3D)](integer-array-3.md) — triple integer values (width = 3)

## Index arrays

Unsigned 64-bit integer arrays for topology and connectivity. Each width corresponds to a geometric primitive — pairs for line segments, triplets for triangles, and so on.

* [Index array (1)](index-array-1.md) — single indices (width = 1)
* [Index array (2)](index-array-2.md) — line segment connectivity (width = 2)
* [Index array (3)](index-array-3.md) — triangle connectivity (width = 3)
* [Index array (4)](index-array-4.md) — quadrilateral connectivity (width = 4)
* [Index array (8)](index-array-8.md) — hexahedral connectivity (width = 8)

## Boolean arrays

Boolean data arrays for flags, masks, and binary-state attributes.

* [Bool array (1D)](bool-array-1.md) — single boolean per element
* [Bool array (multi-dimensional)](bool-array-md.md) — multiple booleans per element

## String and date-time arrays

Non-numeric array types for text and temporal data.

* [String array](string-array.md) — variable-length string values
* [Date-time array](date-time-array.md) — timestamp values

## Colour

Colour values using 32-bit ABGR packing (alpha, blue, green, red).

* [Color](color.md) — single colour value
* [Color array](color-array.md) — per-element colour data

## Spatial primitives

Standalone geometric primitives for point positions and part references.

* [Coordinates 3D](coordinates-3d.md) — single point in 3D space (x, y, z)
* [Reversible index](reversible-index.md) — part index with optional orientation reversal

## Lookup and categorisation

Key-value mappings for categorical data.

* [Lookup table](lookup-table.md) — integer-to-string mapping for category names

## Units

Physical measurement units organised by dimension.

* [Unit](unit.md) — 125+ unit categories organised by physical dimension
