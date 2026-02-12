# Summary

Seequent Geoscience Objects Schemas define metadata and data serialisation of various geoscience objects. The goals include:
* Facilitate interoperabilities between various applications and services that produce and consume geoscience data.
* A data interchange specification to facilitate interoperabilities between various industry/segment standards.

:::info
This documentation is authored in the [`SeequentEvo/evo-schemas`](https://github.com/SeequentEvo/evo-schemas) repository and rendered on the [Seequent Developer Portal](https://developer.seequent.com/docs/data-structures/geoscience-objects). To contribute to these docs, submit a pull request to the repository — changes will be reflected on the Developer Portal once merged.
:::

## Concepts

The schemas are divided into the following categories:
* Elements
* Objects
* Components

### Elements

Elements are primitives that can exist on their own, or be composed into more complex objects, such as lines, point, etc.

### Objects

Objects are composed of a range of elements and their own unique metadata, with their own semantics and structure.

### Components

Components are common/standard snippets of information that are used across Elements and Objects.
