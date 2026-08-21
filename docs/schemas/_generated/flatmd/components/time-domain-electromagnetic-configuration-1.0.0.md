### time-domain-electromagnetic-configuration (v1.0.0)
Time domain electromagnetic configuration.

| Property | Type | Description | Flags |
|---|---|---|---|
| name | String | The name of the configuration. | ✅ |
| key | String | An identifier of the configuration. Must be unique within a list of configurations. | ✅ |
| zero_time | Number | Current turn off time (msec) relative to start of cycle. | ✅ |
| start_time | Number | Time (msec) delay of first gate relative to turn off time. | ✅ |
| transmitter_id | Integer | Transmitter Id. | ✅ |
| receiver_id | Integer | Receiver Id. | ✅ |
| waveform_id | Integer | Waveform Id. | ✅ |
| gates_id | Integer | Gates Id. | ✅ |
| inclinometers_transmitter_position | Array[coordinates-3d] | Inclinometers transmitter position. |  |
| inclinometers_receiver_position | Array[coordinates-3d] | Inclinometers receiver position. |  |
| gates_factor | Number | Gate factor (calibrations factor). |  |
| gates_time_shift | Number | Gate time shift (calibration factor). |  |
| uniform_standard_deviation | Number | Uniform data standard deviation. |  |
| number_of_transmitter_turns | Number | Number of transmitter loop turns. | ✅ |
| base_transmitter_frequency | Number | Base frequency (Hz) at the transmitter. |  |
| peak_transmitter_current | Number | Peak current (Amp). | ✅ |
| primary_field_damping_factor | Number | Primary field damping factor. |  |
| front_gate_filter | time-domain-electromagnetic-configuration | Front gate filter. |  |
| front_gate_time | Number | Front gate time (sec). |  |
| front_gate_slope_low_pass_filter | time-domain-electromagnetic-configuration | Slope low pass filter before front gate. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

