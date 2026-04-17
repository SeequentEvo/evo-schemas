import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/elements/lookup-table-1.0.1.md';

# lookup-table

<SchemaUri uri="schema/elements/lookup-table/1.0.1/lookup-table.schema.json" />

A key-value mapping from integer keys to string values, stored as binary data. Used by categorical attributes to map integer codes to human-readable category names. Supports int32 and int64 key encoding.

**Used by:** [category-data](../components/category-data.md), [category-ensemble](../components/category-ensemble.md), [category-time-series](../components/category-time-series.md).

**See also:** [integer-array-1](integer-array-1.md) (integer key storage), [string-array](string-array.md) (string value storage), [binary-blob](binary-blob.md) (underlying data reference).

## Properties

<FlatProperties />
