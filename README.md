# Schema Collection

This repository hosts an collection of XML and JSON schemas.These schemas are primarily designed for validators and Integrated Development Environments (IDEs) that support auto-completion, enhancing the development experience.

## Schemas

The repository includes various schemas such as:

- **Exasol Document Mapping Language (EDML):** A schema for mapping documents in Exasol.
- **Exasol Error Code Report (error_code_report):** Used as common error reporting format within Exasol.
- **Exasol Project Metrics (project-metrics):** A schema for tracking project metrics within Exasol.

For detailed information on these schemas, visit [schemas.exasol.com](https://schemas.exasol.com). To explore the most current local versions, refer to the Developers Guide section.

## Developers Guide

The contents of this repository are automatically published as a website accessible at [schemas.exasol.com](https://schemas.exasol.com). Contributions are welcome!
To contribute, please create a pull request in the [GitHub repository](https://github.com/exasol/schemas).

## Overview & Structure

This repository adheres to the principle of "convention over configuration", with a structure outlined as follows:

- **Schemas Directory:** `schemas/<name>/<version>` - Contains different versions of each schema.
    ```
      schemas
        ├── schema                    
        │ ├── MAJOR.MINOR.PATCH.json
        ...
      
      e.g.:
      schemas
        ├── edml
        │ ├── 1.0.0.json
        │ ├── 1.1.0.json
        │ ├── 1.2.0.json
        │ ├── 1.3.0.json
        │ ├── 1.4.0.json
        │ ├── 1.5.0.json
        │ └── 2.0.0.json
        ├── error_code_report
        │ ├── 0.1.0.json
        │ ├── 0.2.0.json
        │ └── 1.0.0.json
        └── project-metrics
            └── 0.1.0.json
        ...
    ```
- **Examples Directory:** `examples/<name>/<version>` - Provides example instances for each schema version.
    ```
      examples
        ├── schema                    
        │ ├── MAJOR.MINOR.PATCH.json
        ...
      
      e.g.:
      examples
        ├── error_code_report
        │ ├── 0.1.0.json
        │ ├── 0.2.0.json
        │ └── 1.0.0.json
        ...
    ```

## Deployment

Deployment is managed through a cron job that automatically updates from the `gh-pages` branch every 5 minutes. The updated content is then published on [schemas.exasol.com](https://schemas.exasol.com).

## Setting up the Project / Development Environment

### Prerequisites

- Python >= 3.10
- Poetry

### Setting up Poetry

To set up Poetry, execute the following commands:

```shell
poetry shell
poetry install
```

## Adding a New Schema

Guidelines for introducing a new schema to the collection:

### New Schema Version
To add a new version of an existing schema:

1. Create and add files following the conventions mentioned in the Overview and Structure section.
2. Create a Pull Request (PR).
3. Once the PR is merged, the system will automatically pick it up and publish it. 

**Note:** There may be a delay of up to ~5 minutes.

### Adding the First Schema Version
To add a completely new schema:

1. Create files according to the conventions mentioned in Overview and Structure.
2. Add the new schema to the schemas section of this README.
3. Add a new section to the index.jinja template, located in src/exasol/schemas/templates/index.jinja.

Example HTML snippet for the new schema:

```html
<h2>schema-name</h2>
{# Include details about the schema here. You can add helpful information, links, etc., as long as it's HTML/jinja compatible. #}
{{ schema_list(schemas['schema-name'], examples) }}
```
**Attention:** Make sure to replace `schema-name` in the template with the actual name of your schema.
