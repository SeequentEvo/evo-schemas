---
seoTitle: bool-attribute Component for Evo Schemas | Seequent Developer
description: Review the bool attribute component schema for Geoscience Objects, supporting consistent data structures and reliable Seequent Evo workflows.
---

import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/bool-attribute-1.1.0.md';

# bool-attribute

<SchemaUri uri="schema/components/bool-attribute/1.1.0/bool-attribute.schema.json" />

A boolean attribute stores true/false values. It uses `attribute_type = "bool"`.

* `values` — An array of boolean values, one per geometric element.
* Inherits from [base-category-attribute](base-category-attribute.md).

**Used by:** [regular-masked-3d-grid](../objects/regular-masked-3d-grid.md).

## Properties

<FlatProperties />
