import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/attribute-list-property-1.2.0.md';

# attribute-list-property

<SchemaUri uri="schema/components/attribute-list-property/1.2.0/attribute-list-property.schema.json" />

The `attribute-list-property` component wraps the [one-of-attribute](one-of-attribute.md) array into a named
`attributes` property. This component is used by geometric sub-components (such as vertices and indices)
to attach optional attribute data.

See [Understanding attributes](../../understanding-schemas/understanding-attributes.md) for how attribute lists
work in practice.

## Properties

<FlatProperties />
