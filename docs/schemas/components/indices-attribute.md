---
seoTitle: indices-attribute Component for Evo Schemas | Seequent Developer
description: Review the indices attribute component schema for Geoscience Objects, supporting consistent data structures and reliable Seequent Evo workflows.
---

import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/indices-attribute-1.1.0.md';

# indices-attribute

<SchemaUri uri="schema/components/indices-attribute/1.1.0/indices-attribute.schema.json" />

An indices attribute stores index references to elements of a related object. It uses `attribute_type = "indices"`.

* `values` — An array of index values.
* `related_object` — A reference to the object whose elements are indexed.
* Inherits from [base-continuous-attribute](base-continuous-attribute.md).

**Used by:** [one-of-attribute](one-of-attribute.md).

## Properties

<FlatProperties />
