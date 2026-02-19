import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/brep-container-1.0.1.md';

# brep-container

<SchemaUri uri="schema/components/brep-container/1.0.1/brep-container.schema.json" />

The `brep-container` component stores a Boundary Representation (BRep) model along with its discretised form.

* `format` — The format of the BRep data.
* `producer` — The software that produced the BRep.
* `brep` — The BRep data (as blob storage).
* `discretized_brep` — An optional discretised (triangulated) representation of the BRep.

**Used by:** [geometry-composite](geometry-composite.md).

## Properties

<FlatProperties />
