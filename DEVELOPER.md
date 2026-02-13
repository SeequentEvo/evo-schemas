# Developer documentation

## Pre-requisites

* Python >= 3.10

## Set up your environment

Bootstrap your development environment by completing the following steps:

1. Clone the repository.
2. Create a Python virtual environment.
3. Install the project's dependencies:
   - `pip install .[test]` to install development dependencies.
   - `pip install .[examples]` to install dependencies for running the provided examples.

## Install pre-commit hooks

This project uses [pre-commit hooks](https://pre-commit.com).  To install the hooks, simply run `pre-commit install` (assumes the dev dependencies have been installed).

Every commit to the repository will now run the same pre-commit hooks for linting and formatting as every other developer on the project. The CI builds also run the same hooks.

## Setup examples/.env

The examples in the [service](./examples/service) folder require some shared secrets to access the Geoscience Object Service.

1. Create a copy of [.env.default](./examples/.env.default) and name it [.env](./examples/.env)
2. Open [.env](./examples/.env) and fill in all items
   - `HOST` is the full URL of the Seequent Geoscience Object API, e.g. https://your-hub-code.api.seequent.com/geoscience-object
   - `ID_TOKEN` is your long-lived access token. This will be used to get a fresh authentication token from `ID_API_HOST`.

3. Ensure that you enter those details into [.env](./examples/.env) - this file is excluded from source control to avoid getting committed by accident.

## Schema composition

[JSON schema](https://json-schema.org/draft/2020-12/json-schema-core.html) draft 2019-09 added the [oneOf, anyOf, allOf](https://json-schema.org/understanding-json-schema/reference/combining.html) keywords to allow schema composition.
This repository makes use of the oneOf and allOf keywords.

### allOf

The `allOf` keyword is used for inheritance, e.g. the [base-spatial-data-properties](schema/components/base-spatial-data-properties/1.0.1/base-spatial-data-properties.schema.json) schema inherits the [base-object-properties](schema/components/base-object-properties/1.0.1/base-object-properties.schema.json) schema. As the name suggests, a JSON object must validate against all schemas nested under the allOf keyword.
An alternative solution would be to define a property of type 'baseclass' on the 'subclass', however, this would create an unintuitive level of nesting in the JSON object, e.g. accessing the `uuid` of a [pointset](schema/objects/pointset/1.0.1/pointset.schema.json) would be possible via `pointset.base_spatial_data.base_object.uuid` instead of the much cleaner `pointset.uuid`.

### oneOf

The `oneOf` keyword is used to select exactly one of several options. One example is the [one-of-attribute](schema/components/one-of-attribute/1.0.1/one-of-attribute.schema.json), which is used to define an attribute of an object. The schema validation fails if more than one subschema successfully validates the JSON data. To avoid this, all subschemas have a unique identifier - in the above example it is the `attribute_type` property, which is set to a constant value in the JSON data.

### Validation errors

This repository is using [jsonschema](https://pypi.org/project/jsonschema/) to validate the examples. Note that the error messages produced by this library are sometimes misleading. For example in a subschema, instead of reporting a problem in the `allOf`/`oneOf` validation, it often reports missing attributes which are present in the JSON data.

## Writing schemas

The schemas are written according to the JSON Schema Draft 2020-12. See [JSON schema](https://json-schema.org/draft/2020-12/json-schema-core.html) for more information. The JSON Schema book (Understanding JSON Schema)[https://json-schema.org/understanding-json-schema/index.html] is a great place to start. 

The schemas in this repository make heavy use of composition to create complex objects. The schemas are broken into elements, components, and objects. See the [README.md](README.md) for the differences.

The easiest way to write a new schema is to use some of the simpler objects as examples or templates. [Pointsets](schema/objects/pointset/1.0.1/pointset.schema.json) are one of the simpler schemas. If you are looking for a schema that also has properties as well as references to components, then a good starting point is [Regular 2D grid](schema/objects/regular-2d-grid/1.0.1/regular-2d-grid.schema.json). In both of these schemas, notice how components are shared and referenced.

There is also a Python function to help get started with an empty template. See `generate_json_schema()` in [tools/schemas.py](tools/schemas.py). This function generates a new JSON schema at the appropriate path with the required meta-schema version.

### Standards

The unit tests will catch all the set standards, however, listed below are a few that may not be obvious.

#### Unevaluated properties

Unevaluated properties should only be set to false on *objects*. When unevaluated properties are used on elements or components it prohibits schema composition.

#### Schema property

Every object requires a `schema` property that is a constant containing the path of that schema. This allows consumers to know which schema the JSON follows. The unit tests will fail if an object does not have the `schema` property or if the `schema` property does not contain the path of the schema. There is also a unit test that ensures the folder name matches the schema name.

#### Latest schema version

If a schema is the latest version then all schemas it references must also be of the latest version. This ensures that all schemas are kept up-to-date appropriately.

#### Property names

Property names must be snake case. This makes it easier for automatic tools to parse. The unit tests will fail if a property name is not snake case.

#### Coordinates

2D coordinates are represented as a pair of X, Y values. When coordinates come from a vertical plane, Y is elevation, otherwise X and Y depend on the CRS in use.
3D coordinates are represented as a tuple X, Y, Z values, where Z is elevation. No other fixed convention exists on the direction for 'X' and 'Y' as it depends on the CRS in use.

### Unit tests

The unit tests enforce the set standards such as snake case for property names and directory structure. They will also catch some of the common mistakes made while creating new schemas.
