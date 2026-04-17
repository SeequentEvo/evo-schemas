import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/continuous-ensemble-1.1.0.md';

# continuous-ensemble

<SchemaUri uri="schema/components/continuous-ensemble/1.1.0/continuous-ensemble.schema.json" />

The `continuous-ensemble` component stores an ensemble of continuous-valued realisations. Each realisation
is a separate set of values over the same geometric elements, enabling uncertainty quantification and
probabilistic analysis.

**Used by:** [channel-attribute](channel-attribute.md), [one-of-attribute](one-of-attribute.md).

**See also:** [category-ensemble](category-ensemble.md) (categorical counterpart).

## Properties

<FlatProperties />
