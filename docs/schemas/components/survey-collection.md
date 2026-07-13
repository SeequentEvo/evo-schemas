import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/survey-collection-1.0.2.md';

# survey-collection

<SchemaUri uri="schema/components/survey-collection/1.0.2/survey-collection.schema.json" />

The `survey-collection` component groups survey data into a collection with a collection number, type,
identifier, and associated survey attributes.

Collections represent a logical grouping of measurements — for example, all data collected along a single
flight line or traverse.

**Used by:** [gravity](../objects/gravity-2.0.1.md), [magnetics](../objects/magnetics-2.0.1.md), [radiometric](../objects/radiometric-2.0.1.md).

**See also:** [survey-line](survey-line.md), [survey-attribute](survey-attribute.md).

## Properties

<FlatProperties />
