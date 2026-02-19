import SchemaUri from '@theme/SchemaUri';
import FlatProperties from '../generated/flatmd/components/one-of-attribute-1.2.0.md';

# one-of-attribute

<SchemaUri uri="schema/components/one-of-attribute/1.2.0/one-of-attribute.schema.json" />

The `one-of-attribute` component is a discriminated union defining the set of attribute types that can be used
within an attribute list. Each item in the array must match exactly one of the supported attribute schemas,
distinguished by the `attribute_type` field.

The supported attribute types are:

| Attribute type | `attribute_type` value | Description |
|---|---|---|
| [continuous-attribute](continuous-attribute.md) | `"scalar"` | Floating-point values |
| [category-attribute](category-attribute.md) | `"category"` | Categorical values with a lookup table |
| [bool-attribute](bool-attribute.md) | `"bool"` | Boolean values |
| [color-attribute](color-attribute.md) | `"color"` | ABGR colour values |
| [string-attribute](string-attribute.md) | `"string"` | String values |
| [integer-attribute](integer-attribute.md) | `"integer"` | Integer values |
| [date-time-attribute](date-time-attribute.md) | `"date_time"` | Timestamp values |
| [vector-attribute](vector-attribute.md) | `"vector"` | N-dimensional vectors |
| [indices-attribute](indices-attribute.md) | `"indices"` | Index references to related objects |
| [continuous-ensemble](continuous-ensemble.md) | — | Ensemble of continuous realisations |
| [category-ensemble](category-ensemble.md) | — | Ensemble of categorical realisations |
| [bool-time-series](bool-time-series.md) | — | Boolean values over time |
| [continuous-time-series](continuous-time-series.md) | — | Continuous values over time |
| [category-time-series](category-time-series.md) | — | Categorical values over time |

See [Understanding attributes](../../understanding-schemas/understanding-attributes.md) for guidance on how
attributes are associated with geometry.

**Used by:** [geological-model-meshes](../objects/geological-model-meshes.md), [geological-sections](../objects/geological-sections.md), [regular-2d-grid](../objects/regular-2d-grid.md), [regular-3d-grid](../objects/regular-3d-grid.md), [regular-masked-3d-grid](../objects/regular-masked-3d-grid.md), [tensor-2d-grid](../objects/tensor-2d-grid.md), [tensor-3d-grid](../objects/tensor-3d-grid.md).

## Properties

<FlatProperties />
