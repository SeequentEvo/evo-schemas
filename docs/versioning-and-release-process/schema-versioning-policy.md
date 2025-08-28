# Schema Versioning Policy

Geoscience Data Objects in Evo are how we represent core geoscientific concepts in digital form. The schemas governing these Geoscience Data Objects are called “Geoscience Object Schemas” or Evo Schemas, and the authoritative version of this open source schema library may be found on the [Seequent Evo GitHub repository called evo-schemas](https://github.com/SeequentEvo/evo-schemas). Documentation for these schemas is available in the [Seequent Developer Portal section on Data structures](https://developer.seequent.com/docs/data-structures/geoscience-objects).

We sometimes add fields, change the details on an existing data model, or change how Evo stores and represents the data. These changes allow us to grow the capabilities of the Evo platform to support more of your workflows. We release a new version of the underlying Evo Schema (also known as Geoscience Object Schema) when these changes occur. We will expand on the versioning philosophy behind these below, but to make this document as useful as possible, we will start with what you need to know.

- Evo Schema versions are composed of three numbers and look like this: `1.2.1`

- For schemas in the **Tech Preview** state (as defined in [Schema Development Lifecycle](./schema-development-lifecycle.md)):
    - **Tech Preview** schemas have finished development, but are not yet supported by Seequent nor covered by any SLA (Service Level Agreement) or deprecation policy
    - **Tech Preview** schemas are merged into `main` with the final version number (e.g., `1.2.1`), but the status of the Preview or Supported state is listed in the Seequent Developer Portal
    - In the event that a **Tech Preview** schema is deprecated or does not enter **Supported** status, any future versions of that schema will carry updated version numbers per the policy below

- [Each schema is versioned independently](#individual-versioning)

In basic terms:

- Changes to the leftmost number mean incompatibility between versions, because the data model changed a lot.

- Changes to the middle number mean compatibility is guaranteed for old data, but data under a new schema will lose information if converted to an old one.

- Changes to the rightmost number mean that there were changes made that do not affect data validation (perhaps improvements to documentation, restructuring into components, etc.)

When transforming between data models, even in cases where not all information is available within the source data object, there are frequently sensible default values and/or additional information available to the application. This can improve the compatibility story greatly by filling in gaps in the source data, making the software more robust against varying schema standards.

## Schema versioning philosophy

Seequent Evo is a system designed to help manage and enable workflows around the world’s geoscientific data. As such, it is a growing platform, and capabilities of its clients will change over time. Geoscience Objects (and other Evo datatypes) support versioning, but an object revision written today and an object revision written five years from now are not guaranteed to be written with the same schema version. As such, backwards compatibility for reading data is a core design goal.

It is expected that Evo will contain data of various lineages, including data following old schemas – however, clients will continue to update and support the features of newer schema revisions. In the fullness of time, the system will tend towards old data (along with new) and new clients. Hence, how newer schemas process old data (especially on-read) is extremely important.

As discussed below, this compatibility is the primary differentiator between `MAJOR`, `MINOR` and `PATCH` changes to schemas.

## Geoscience objects versioning specification

Geoscience Objects in Evo follow SemVer (Semantic Versioning), modified to make sense for the schema versioning use case. As such, each schema has a version of the form `MAJOR`.`MINOR`.`PATCH`, separated by periods with the leftmost values carrying the most significance. Data stored in schema `1.2.0` and data stored in schema version `1.2.1` have very similar rules and are fully compatible. Neither is guaranteed to be broadly compatible with version `2.0.0` of the same schema, which we know is different in significant ways. Each part of the version has a different meaning, as described below. We aim to maintain the familiar structure of SemVer, as it is well-supported in many systems, but the following details aim to clarify the impact of SemVer concepts in a data schema context.

### Data model (`MAJOR`)

`MAJOR` changes are breaking changes, which *prevent interacting with historical data* without extra help. It may be possible to translate or interpret between Geoscience Objects with different `MAJOR` schema revisions. However, the translation will sometimes imply [lossiness](#lossiness) (some information doesn't translate fully), require additional information, or both.

For example, a totally new version of a mesh object could be created, with a different indexing scheme from previous data. In that case, data stored in the previous model wouldn't be directly interpretable using the new one while still preserving the same geoscientific meaning. This kind of change always triggers a new `MAJOR` version.

Seequent may provide guidance on how to convert data from one form to another, or tools to do so. Alternatively, it will be obvious from the data schemas themselves (which are open for review). Possibly this will require additional information (for example, if a field is now required where before it was optional).

#### Examples

- **Adding new, required properties**: Adding a new property that isn’t in data following a previous revision of the schema
- **Making optional properties required**: Previous data revisions aren’t guaranteed to pass validation
- **Changing data types of existing properties**: For example, changing a string to an integer
- **Changing the meaning of properties**: Using a property differently, resulting in errors if old data is processed under new assumptions
- **Renaming properties**: Changing the name of a field
- **Breaking changes to enum values**: Removing existing enum values or changing their meaning
- **Significant restructuring of the schema**: Moving fields, nesting objects differently, or fundamental changes to relationships
- **Changes to data formats or validation rules that would invalidate previously valid data**: For example, tightening the validation rules on a piece of metadata
- **Adding new referenced sub-schemas in an `allOf` reference**: For example, adding a new required set of parameters from a sub-schema

### Data model revision (`MINOR`)

`MINOR` changes mean that the new schema is “Backwards Compatible” – i.e., it *validates successfully against all historical data*, but any new optional fields will be absent or filled with default values. The fields in the new version are a strict superset of the fields in the previous version. The schema is not “Forwards Compatible” – data written to the new schema may contain fields that do not validate against the previous schema. There are exceptions to this (a given Geoscience Object may not make use of any of the new features), and therefore translation from the new schema to the old is sometimes possible by omitting/ignoring fields in the new schema that are unsupported.

For API clients, code written against an earlier version with the same `MAJOR` revision can often read data written in an updated version, simply ignoring fields it does not understand (this requires coding in a defensive, resilient manner). There are exceptions, where a new sub-schema uses features not present in the old schema. Data written in an earlier version can always be interpreted by code expecting the newest version with the same `MAJOR`, because anything that’s not present in the data is optional or has a sensible default. There will be no [lossiness](#lossiness) in interpreting earlier data with the new schema, but translating newer data to an earlier version will mean removing fields that are not supported.

You may think of this as a feature enhancement. `MINOR` updates change something meaningful about the data model without totally rethinking it. Frequently, updating to a new `MINOR` is something that implementers can do with little or no significant effort: for example, by applying default values to older data.

#### Examples

- **Adding new, optional properties**: New fields can be introduced without requiring existing data or clients to adapt (if clients written to older schema versions accept or ignore properties they do not understand)
- **Adding new enum values**: Expanding the allowed values for an existing enum field
- **Loosening restrictions on existing types**: For example, changing a `minLength` from 5 to 0
- **Adding new referenced sub-schemas in an `oneOf` reference**: For example, adding a new acceptable parameterization or structure alongside other existing parameterizations, without replacing or removing old ones

### Fixes and clarifications (`PATCH`)

`PATCH` changes mean schema changes that are *fully backwards-compatible* and *fully forwards-compatible* (i.e., all historical data with the same `MAJOR` and `MINOR` revision can be validated by the new schema, and vice versa).

This mainly represents changes that are done to improve quality, without impacting the data model.

#### Examples

- **Backwards-compatible bug fixes**: Correcting errors in schema definitions that do not change the meaning or structure of existing valid data
- **Clarifications**: Adding more precise descriptions or examples without altering validation rules
- **Shifting sub-schema definitions to or from a `$ref` block**: For example, moving a data structure to a component to enable reuse. As the “flattened” form of the schema is the same, data valid under one definition is valid under the other.

:::info
API clients may choose to ignore `PATCH` changes, as they make no difference to the data flowing over the wire.

There are types of consumers for whom `PATCH` changes are very important. This includes anything generating documentation (for example, our own [Developer Portal](https://developer.seequent.com/)), since changes to descriptions and examples are quite important for that use case.

Another consumer that may wish to track `PATCH` releases is anyone interacting with Evo via AI / LLM tools for code generation – updates to the documentation can have a profound effect on the usefulness of these tools.
:::

### Individual versioning

The JSON schemas for the Geoscience Objects and their components use *individual versioning* (see [`SeequentEvo/evo-schemas`](https://github.com/SeequentEvo/evo-schemas)). Each schema has its own version rather than all the schemas incrementing versions when a change is made to other, unrelated schemas. This means that a schema at version `2.0.0` can reference a higher or lower version of another schema, say `3.5.2` or `1.0.0` – it depends on how many changes the referenced schema has gone through.

The individual versioning reflects the broad range of geoscientific domains supported by Evo. For example, an application that focusses on geophysical data management may never use schemas related to geostatistical modelling. Individual versioning allows each application to address only the data models it uses, while not being affected by changes to unused schemas.

This means that `tensor-3d-grid` v`1.3.0` might be older than `block-model` v`1.0.0` (it is), and that publishing a change to `tensor-3d-grid` that moved it to v`1.3.1` doesn’t imply any change to any other schema.

:::info
#### Component versioning

Many schemas depend on “components” – i.e., sub-schemas that are referenced to implement shared functionality. For example, `base-object-properties` is referenced broadly because it implements all the common behaviours for Geoscience Objects; most object schemas reference it via a transitive reference in `base-spatial-data-properties`.

When the lineage component v`1.0.0` was introduced, it was referenced by `base-object-properties` v`1.1.0`, and this minor revision cascaded through all of the objects, incrementing their minor versions by 1 as well. In some objects, this took them from v`1.1.0` to v`1.2.0`; in others, it took them from v`1.2.0` to v`1.3.0`.

When a referenced schema changes and a schema that uses it incorporates that change, it will always be (at least) as significant a version increase as the referenced sub-schema. However, the exact number will depend on the history of the schema evolution for the schema that references it.
:::

### Multiple versions in use

Within a given Workspace or Evo Instance, there may be data that follow the same broad schema but that are written with different versions. In some cases, this reflects historical data (once data in the Geoscience Object Service are written, a given revision is *immutable*, and therefore tied to the schema it was written in). In others, brand new data may be entered by an application that writes an earlier specification (either because they have not upgraded, or because they wish to be backwards compatible).

Having multiple versions simultaneously in use adds some complexity. However, having multiple versions is fundamental to storing what *truly happened*. A common alternative would be to seamlessly "upgrade" data to a new schema, where possible. Seamlessly upgrading should be employed in many cases, but *the data is different*. In Evo, performing an update means either a new Object or a new Object Revision: both may be tracked by Audit Logs and Lineage where supported.

## Concepts and design concerns

### Designing for robustness

Seequent recommend applying the [Robustness Principle](https://en.wikipedia.org/wiki/Robustness_principle) for designs that rely on Evo. This principle allows as much flexibility in your software as possible, and to benefit from access to as much of the data in a given Workspace as possible. This means accepting data from Evo knowing that in the future there may be a *newer version* of a schema.

Be flexible when faced with fields you don't expect, if possible. Interpret data to extract the information your algorithm, report, or app needs to know—but no more. This ensures that you can tolerate newer versions with `PATCH`es, and often even `MINOR` changes.

Equally, if your application is able to interpret a range of data versions effectively, consider which ones are valuable to support. For example, there may be valuable historical data written to an earlier schema that your users or customers already have stored in Evo. If you are able to interpret a range of versions, you are less dependent on data conversion tools offered by the platform (or yet to be built by Seequent or other developers).

Please reach out to the Seequent Evo support team or Developer Community Champions if you'd like to discuss these best practices.

### Lossiness

Some data transformations (also known as “schema migrations”) imply lossiness. Lossiness happens when not all of the data in the original form make it through a transformation. The transformation cannot be reversed, and return the same result.

A simple example is saying, *"There are only red, blue and green balls in the ball pit"*. From that, we can also conclude, *"There are three colours of balls in the ball pit"*. If we have the former sentence, we have all the information we need to construct the latter sentence (we can count the colours). However, we cannot go from knowing how many colours there are to knowing which colours exist without more information. These are the kinds of incompatibilities that most often occur between data schemas.

A less trivial example exists when we convert between versions of the same Geoscience Data Object model – there may be fields that are expected in one schema that data written to another schema simply lacks. Sometimes, more information will allow us to do an acceptable conversion (for example, *"Ball pits can have red, blue or green balls"*).