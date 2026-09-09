---
seoTitle: date-time-attribute Component for Evo Schemas | Seequent Developer
description: Review the date time attribute component schema for Geoscience Objects, supporting consistent data structures and reliable Seequent Evo workflows.
---

import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/date-time-attribute-1.1.0.md';

# date-time-attribute

<SchemaUri uri="schema/components/date-time-attribute/1.1.0/date-time-attribute.schema.json" />

A date-time attribute stores a range of timestamps. It uses `attribute_type = "date_time"`.

* `values` — An array of timestamp values, one per geometric element.
* `nan_description` — A [nan-continuous](nan-continuous.md) component defining how NaN values are interpreted.
* Inherits from [base-continuous-attribute](base-continuous-attribute.md).

**Used by:** [channel-attribute](channel-attribute.md), [one-of-attribute](one-of-attribute.md).

## Properties

<FlatProperties />
