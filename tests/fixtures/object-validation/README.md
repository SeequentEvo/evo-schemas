# Object validation fixtures

These fixtures complement the block-model cases with representative validation
behaviors from other object schemas. Each file in `payloads/` is a complete JSON
object; `index.json` maps its filename to the object schema ID and either
`null` for a valid instance or an expected error. Error fields have the same
meaning as in the [block-model fixtures](../block-model-1.3.0/README.md).

The test uses the repository's strict component-property transformation,
filesystem reference resolver and `Draft202012Validator.FORMAT_CHECKER`.
The test dependencies include the optional RFC 3339 checker so invalid
`date-time` values are rejected. This suite covers representative validation
logic, not every property, enum value or schema version. JSON Schema cannot
enforce rules expressed only in descriptions or the contents of binary blobs.

The cases include binary-blob formats and array metadata, related-object
versions, attribute and time-series alternatives, lineage facets, recursive
folders, mesh uniqueness, grid and rotation boundaries, CDF alternatives,
drilling collections and deviations, resistivity surveys and variograms.
Where several alternatives report the same error, the index identifies the
intended branch with `schema_prefix`.

Run with `pytest tests/test_object_validation.py tests/test_block_model_validation.py`.
