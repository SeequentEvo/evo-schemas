# Understanding attributes

Most objects can have generic attributes associated with some of their components.
These are organised using an attribute list.

## Attribute lists

The generic attributes are defined using the `one-of-attribute` component schema which is defined as a list where each item is one of the attribute components.

This is usually implemented using an optional `attributes` property on one or more of geometric components using the `attribute-list-property` component schema.

For instance the [triangle-mesh](../schemas/objects/triangle-mesh.md) schema can have attributes attached for both the `vertices` and `indices` properties of its `triangles` property. The dimension of the attribute array in each case corresponds with the length of the geometry property; i.e., one value per vertex in the case of an attribute attached to mesh vertices or one value per triangle in the case of an attribute attached to triangle indices.

In some cases where the geometry is implied the list will have a different name. An example of this is for the [regular-grid-3d](../schemas/objects/regular-3d-grid.md) schema where `cell_attributes` and `vertex_attributes` properties are used for attributes for the cells and vertices of the grid respectively.

## Attribute definitions

There many attribute types to choose from, depending on the data type (boolean, date, string, integer, etc.).

Most attributes are scalar values but there are also vector, ensemble and time-series values available for some scalar types.

### Base properties

The `base-attribute` component schema defines three required properties (`key`, `name` and `attribute_type`) for all attribute schemas. Each attribute schema will also have a `values` property with the specific data array for that attribute type.

Additionally, each attribute will typically be classified as a *category* or *continuous* attribute and so also have an optional `attribute_description` property.

Many attribute schemas will also have a required `nan_description` property to designate not-a-number (NaN) values.

### Extra details

Category attributes use the `category-attribute` schema have a required `table` property (specified in the `category-data` component schema).  This specifies a lookup table (using the `lookup-table` element schema) to convert the integer `values` to strings.
