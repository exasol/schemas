# Schema Collection

This repository contains a collection of XML and JSON schemas, used for validators and IDEs that support auto-completion.

## Exasol Document Mapping Language (EDML)

The EDML is a JSON-based domain specific language.
You can use it to configure the mapping of document data to Exasol tables when using a [document virtual schema](https://github.com/exasol/virtual-schema-common-document).

* [1.0.0 (current)](edml-1.0.0.json) ([reference](https://exasol.github.io/dynamodb-virtual-schema/schema_doc/index.html))

## Information for Contributors

This repository is automatically served as as a website under https://schemas.exasol.com.
You can contribute using the [GitHub  repository](https://github.com/exasol/schemas).

If you change this `README.md` file also regenerate the `index.html` using the following command:

```shell script
pandoc README.md > index.html
```
