# Cell type geometry

All binary blobs that store cell geometry such as tetrahedrons and hexahedrons should follow the convention taken in the VTK library for vertex ordering. This ensures that all consumers of the binary blob will know the vertex ordering and can transform it to fit their needs.

See the VTK book, [chapter 5](https://kitware.github.io/vtk-examples/site/VTKBook/05Chapter5/) for all cell types and their vertex ordering. The images linked below are from the VTK book.

It is especially important to note the vertex ordering of the cells in the images below.

## Linear cell types

These are linear cell types in the VTK library, taken from chapter 5 of the VTK book. Note that there may be some cell types that Evo does not support, such as VTK_VOXEL.

See [Linear cell types](https://raw.githubusercontent.com/Kitware/vtk-examples/gh-pages/src/VTKBook/Figures/Figure5-2.png) from the VTK book.

## Non-linear cell types

These are non-linear cell types in the VTK library, taken from chapter 5 of the VTK book. Note that there may be some cell types that Evo does not support.

See [Non-linear cell types](https://raw.githubusercontent.com/Kitware/vtk-examples/gh-pages/src/VTKBook/Figures/Figure5-4.png) from the VTK book.

## Supported cell types

The following table shows the cell types and a corresponding integer which should be stored in the Parquet tables in the appropriate column.

### Basic cell types

| Type | Numeric value |
| ---- | --------------|
| Point | 0 |
| Line  | 1 |
| Triangle | 2 |
| Quadrilateral | 3 |
| Tetrahedron | 4 |
| Hexahedron | 5 |
| Wedge | 6 |
| Pyramid | 7 |
