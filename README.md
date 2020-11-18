# Schema Collection

This repository contains a collection of XML and JSON schemas, used for validators and IDEs that support auto-completion.

## Exasol Document Mapping Language (EDML)

The EDML is a JSON-based domain specific language.
You can use it to configure the mapping of document data to Exasol tables when using a [document virtual schema](https://github.com/exasol/virtual-schema-common-document).

* [1.2.0 (current)](edml-1.2.0.json) ([reference](https://exasol.github.io/virtual-schema-common-document/schema_doc/edml_1.2.0/index.html))
* [1.1.0](edml-1.1.0.json) ([reference](https://exasol.github.io/virtual-schema-common-document/schema_doc/edml_1.1.0/index.html))
* [1.0.0](edml-1.0.0.json) ([reference](https://exasol.github.io/virtual-schema-common-document/schema_doc/edml_1.0.0/index.html))

## Exasol Error Code Report

The Exasol error code report is a JSON report that is generated by local crawlers from the source code.
It lists all error codes defined in the project together with some metadata.
The report format is standardized by this JSON-Schema.

* [0.1.0 (current)](error_code_report-0.1.0.json) ([reference](https://exasol.github.io/schemas/error_code_report-0.1.0/index.html)) ([example](error_code_report-0.1.0_example.json))
## Information for Contributors

This repository is automatically served as as a website under https://schemas.exasol.com.
You can contribute using the [GitHub  repository](https://github.com/exasol/schemas).

If you change this `README.md` file also regenerate the `index.html` using the following command:

```shell script
pandoc README.md > index.html
```
