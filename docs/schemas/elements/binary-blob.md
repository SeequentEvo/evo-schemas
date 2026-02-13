import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/elements/binary-blob-1.0.1.md';

# binary-blob

<SchemaUri uri="schema/elements/binary-blob/1.0.1/binary-blob.schema.json" />

Reference to binary data storage. Accepts a file hash (64-character hex string), a UUID, or null (no data). This is the foundational storage primitive — all array elements reference a `binary-blob` for their `data` property.

## Properties

<FlatProperties />
