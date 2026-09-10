---
seoTitle: survey-attribute-definition Component for Evo Schemas | Seequent Developer
description: Review the survey attribute definition component schema for Geoscience Objects, supporting consistent data structures and reliable Seequent Evo workflows.
---

import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/survey-attribute-definition-1.0.1.md';

# survey-attribute-definition

<SchemaUri uri="schema/components/survey-attribute-definition/1.0.1/survey-attribute-definition.schema.json" />

The `survey-attribute-definition` component defines common properties for attributes in survey data, including
the attribute name, spatial offset, and description.

This is used by geophysical survey schemas (e.g., [gravity](../objects/gravity-2.0.0.md), [magnetics](../objects/magnetics-2.0.0.md))
to describe the measurements collected.

**Used by:** [drilling-campaign](../objects/drilling-campaign.md), [gravity](../objects/gravity-2.0.0.md), [magnetics](../objects/magnetics-2.0.0.md), [radiometric](../objects/radiometric-2.0.0.md).

**See also:** [survey-attribute](survey-attribute.md).

## Properties

<FlatProperties />
