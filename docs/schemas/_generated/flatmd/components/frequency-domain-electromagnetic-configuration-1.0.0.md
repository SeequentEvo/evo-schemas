### frequency-domain-electromagnetic-configuration (v1.0.0)
Frequency domain electromagnetic configuration.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the configuration. | ✅ |
| key | String | An identifier of the configuration. Must be unique within a list of configurations. | ✅ |
| relative_quadrature_standard_deviation | Integer | Relative (%) qaudrature standard deviation. | ✅ |
| relative_in_phase_standard_deviation | Integer | Relative (%) in-phase standard deviation. | ✅ |
| coil_configuration | Array[frequency-domain-electromagnetic-configuration] | Coil configuration. Frequency is provided in increasing order. | ✅ |
| gps | coordinates-3d | Location of GPS relative to point of reference. | ✅ |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

