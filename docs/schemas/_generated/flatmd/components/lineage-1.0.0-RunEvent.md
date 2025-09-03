### lineage (v1.0.0)

| Property | Type | Description | Flags |
|---|---|---|---|
| eventTime | String | the time the event occurred at | ✅ |
| producer | String | URI identifying the producer of this metadata. For example this could be a git url with a given tag or sha | ✅ |
| schemaURL | String | URI identifying the corresponding version of the schema definition for this RunEvent | ✅ |
| eventType | String | the current transition of the run state. It is required to issue 1 START event and 1 of [ COMPLETE, ABORT, FAIL ] event per run. Additional events with OTHER eventType can be added to the same run. For example to send additional metadata after the run is complete |  |
| run | lineage |  | ✅ |
| job | lineage |  | ✅ |
| inputs | Array[lineage] | The set of **input** datasets. |  |
| outputs | Array[lineage] | The set of **output** datasets. |  |


#### Legend

| Flag | Description |
| --- | --- |
| ⬆️ | Inherited property |
| ✅ | Required property |

