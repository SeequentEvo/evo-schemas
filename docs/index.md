# Geoscience Objects

Geoscience Objects is Seequent's open schema standard for geoscience data. It defines how geoscience datasets — point clouds, drillhole campaigns, geological models, geophysical surveys, and more — are structured and serialised for exchange between applications and services.

The schemas are written in [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/json-schema-core) and organised into a three-tier hierarchy of [objects, components, and elements](schemas/index.md). New schemas follow an open [RFC process](https://github.com/SeequentEvo/evo-schemas/labels/rfc) and progress through a defined [development lifecycle](versioning-and-release-process/schema-development-lifecycle.md) from proposal to supported status.

:::info
This documentation is authored in the [`SeequentEvo/evo-schemas`](https://github.com/SeequentEvo/evo-schemas) repository and rendered on the [Seequent Developer Portal](https://developer.seequent.com/docs/data-structures/geoscience-objects). To contribute to these docs, submit a pull request to the repository — changes will be reflected on the Developer Portal once merged.
:::

## Understanding these docs

[Evo schemas](schemas/index.md) — the schema catalogue, organised by tier:

- [Object schemas](schemas/objects/index.md) — top-level geoscience datasets: points and surfaces, grids, drilling, geological modelling, structural geology, geophysics, and geostatistics
- [Component schemas](schemas/components/index.md) — reusable building blocks: identity, attributes, geometry primitives, and domain-specific structures
- [Element schemas](schemas/elements/index.md) — primitive data types: typed arrays, colours, coordinates, lookup tables, and units

[Understanding schemas](understanding-schemas/blob-storage.md) — conceptual guides covering blob storage, attributes, parts, and cell-type geometry.

[Versioning & release process](versioning-and-release-process/schema-versioning-policy.md) — the schema versioning policy and development lifecycle.
