import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/category-data-1.0.1.md';

# category-data

<SchemaUri uri="schema/components/category-data/1.0.1/category-data.schema.json" />

The `category-data` component defines the lookup-table structure used by [category-attribute](category-attribute.md):

* `table` — A lookup table (using the `lookup-table` element) mapping integer keys to category names.
* `values` — An integer array storing the category index for each geometric element.

## Properties

<FlatProperties />
