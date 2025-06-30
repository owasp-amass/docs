# :simple-owasp: SimpleProperty

The `SimpleProperty` is one of the foundational data types used in the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model) (OAM) to describe metadata associated with an asset or relation. As its name suggests, a `SimpleProperty` represents a basic key-value pair that conveys a single, scalar piece of information about an asset or relation—such as a name, identifier, timestamp, or descriptive attribute.

This property type is designed for flexibility and broad applicability. It is not limited to a fixed schema or controlled vocabulary, making it well-suited for capturing diverse details across many different asset and relation types. For example, a `SimpleProperty` might describe the version of a software component, the date a DNS name was last resolved, or a flag indicating whether a host has a JARM fingerprint.

Each `SimpleProperty` includes the following core components:

- **Name** – A string that identifies the nature or role of the property (e.g., `last_monitored`).
- **Value** – A string-encoded representation of the property's actual value (e.g., `"DNS-IP"`).

By standardizing on this minimal structure, `SimpleProperty` allows assets and relations in the model to be richly annotated without enforcing strict typing or domain-specific schemas up front. This supports extensibility, integration with heterogeneous data sources, and future evolution of the model.

In practice, `SimpleProperty` entries are often used when importing information from external tools, integrating OSINT data, or performing enrichment tasks across discovered assets and relations. The model treats them as first-class citizens in the graph, enabling reasoning, filtering, and correlation based on any attached properties.

## :fontawesome-solid-tags: SimpleProperty Attributes

| Attributes | Type | Required | Description |
| :--------: | :----: | :--------: | :----------- |
| `property_name` | string | :material-check-decagram: | A string that identifies the nature or role of the property |
| `property_value` | string | :material-check-decagram: | A string-encoded representation of the property's actual value |
