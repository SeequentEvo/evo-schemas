### drilling-campaign (v1.0.0)
The path taken by the planned drillhole using both natural and directed deviations.

| Property | Type | Description | Flags |
|---|---|---|---|
| attributes | [one-of-attribute](../components/one-of-attribute-1.2.0.md) | Attribute data. | [⬆️](../components/attribute-list-property-1.2.0.md) |
| deviation_type | String | Type of deviation | ✅ |
| segment_type | [string-array](../elements/string-array-1.0.1.md) | Type of segment deviation, 'natural' or 'directed' | ✅ |
| segment_properties | [drilling-campaign](../objects/drilling-campaign-1.0.0-planned-path-mixed_deviation-segment_properties.md) | The path taken by the planned drillhole using both natural and directed deviations. Columns: distance, azimuth, dip, lift rate, drift rate, deviation rate distance, toolface angle, dogleg severity | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

