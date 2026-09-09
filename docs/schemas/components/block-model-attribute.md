---
seoTitle: block-model-attribute Component for Evo Schemas | Seequent Developer
description: Review the block model attribute component schema for Geoscience Objects, supporting consistent data structures and reliable Seequent Evo workflows.
---

import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/block-model-attribute-1.2.0.md';

# block-model-attribute

<SchemaUri uri="schema/components/block-model-attribute/1.2.0/block-model-attribute.schema.json" />

A block model attribute extends the standard attribute system for use with block model data. Block model
attributes accommodate the variable-length sub-block structure of block models.

This component composes [base-continuous-attribute](base-continuous-attribute.md) and adds block-model-specific
value storage. As of 1.2.0 it is the single attribute type used by the block-model object, covering both
continuous and categorical attributes via its `attribute_type` (`Boolean` and `Utf8` alongside the numeric,
date, and timestamp types).

**Used by:** block-model.

**See also:** [block-model-category-attribute](block-model-category-attribute.md) (separate categorical
attribute used by block-model 1.1.0 and earlier).

## Properties

<FlatProperties />
