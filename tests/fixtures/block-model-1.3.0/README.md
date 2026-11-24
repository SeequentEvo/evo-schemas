# Block-model validation fixtures

Each file in `payloads/` is a complete JSON instance validated against the
block-model 1.3.0 schema, regardless of its `schema` property. `index.json` maps
each filename to `null` for a valid instance or to an expected validation error:

- `keyword`: JSON Schema keyword that fails.
- `path`: JSON instance path as an array of property names and array indices.
- `message_contains`: optional substring to distinguish errors at the same path.
- `schema_prefix`: optional schema path prefix identifying a particular
  `oneOf` branch.

The test collects nested errors as well as top-level errors. A failed geometry
alternative can also cause an outer `unevaluatedProperties` error, so the error
in the index is not necessarily the single error selected by `jsonschema.validate`.

The test matches the repository's example validator: it resolves local
references, enables the installed `FormatChecker` checks and adds
`unevaluatedProperties` checks to referenced components. This is stricter than
the unmodified component schemas, but does not reject every unknown property:
the `valid-attribute-extra-property` fixture records the current behavior of
the composed attribute schema. Available format checks depend on installed
optional dependencies; the test dependencies include a date-time checker.

Cases exercise validation keywords, required fields, types and boundaries across
the object and its referenced components. They do not enumerate every possible
invalid JSON value or every unit enum, and cannot test prose-only or
service-side constraints such as group-reference integrity.

Run with `pytest tests/test_block_model_validation.py`.
