# :simple-owasp: SourceProperty

The `SourceProperty` is a specialized property type in the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM) that captures context about where that information came from. This makes `SourceProperty` especially valuable in scenarios where provenance, traceability, and confidence are essential.

The `SourceProperty` allows consumers of the model to understand *how* and *from where* a piece of data was obtained. This is particularly useful when integrating data from OSINT sources, third-party APIs, security tools, or historical archives.

Each `SourceProperty` includes the following components:

- **Name** – Name of the engine plugin that discovered the asset or relation (e.g., `DNS-IP`, `RDAP`, `GLIEF`).
- **Confidence** – A numerical value providing a percentage of confidence (e.g., `50`, `75`, `100`).

By coupling assets and relations with their origin, `SourceProperty` supports trust-aware decision-making and enables the model to be used in environments where data reliability and reproducibility are critical. Consumers can prioritize or filter information based on its source, aiding in validation and reducing false positives in automated analysis pipelines.

All Amass engine plugins mark discovered assets and associations between them with source information to build the breadcrumb trail and better understand how the discoveries were made during the enumeration process.

## :fontawesome-solid-tags: SourceProperty Attributes

| Attributes | Type | Required | Description |
| :--------: | :----: | :--------: | :----------- |
| `name` | string | :material-check-decagram: | Name of the engine plugin that discovered the asset or relation |
| `confidence` | number | :material-checkbox-blank-circle-outline: | A value 0 through 100 representing the confidence percentage |
