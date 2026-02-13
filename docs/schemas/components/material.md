import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/material-1.0.1.md';

# material

<SchemaUri uri="schema/components/material/1.0.1/material.schema.json" />

Material associated with volumes or surfaces. This component does not attempt to represent the full spectrum of information that can be associated with a material. A future shared Evo material object is envisioned; the material component only provides a placeholder sufficient to identify the material used and link to another object if one exists.

Materials have a name but are referenced uniquely by their key.

Each material contains:

* `name` - A user friendly (display) name for the material. It may or may not be unique in a list.

* `key` - unique identifier for the material.
 
* `color` - Display color associated with the material. Color value as an encoded ABGR integer.

* `data_source` - link to a separate geoscience object. We expect over time for a materials Evo object to exist. This field is optional; and it's intended as a link to a shared material object.

:::info
Multiple materials can have the same name because they can be sourced from different geological models. For example "material A" can show up in two geological models that are sourced from different borehole data, and they can have different colours. To deal with this, materials have a name (not unique) and a key identifier (unique).
:::

**Used by:** [design-geometry](../design-geometry.md), [geological-model-meshes](../geological-model-meshes.md), [geological-sections](../geological-sections.md).

## Properties

<FlatProperties />
