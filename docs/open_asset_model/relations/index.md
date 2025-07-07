# :simple-owasp: Relations

In the [OWASP](https://owasp.org) [Open Asset Model](https://github.com/owasp-amass/open-asset-model), a **relation** is a typed, directed connection between two assets that expresses how they are linked in the external world. Relations transform isolated observations into an **interconnected graph**, enabling reasoning over ownership, control, communication, service structure, and many other dimensions. Each relation carries contextual metadata such as discovery source, timestamps, and confidence, and is a first-class citizen in the data model—critical for building a coherent picture of an organization's external footprint.

## :material-graph-outline: Why *Relations* Matter

While *assets* are the atomic units of external exposure, **relations** are what make those atoms intelligible as systems. They represent the **structure**, **flow**, and **attribution logic** that connects seemingly disparate observations into a meaningful model.

Relations bring three core advantages to the OAM:

1. **Contextual Linking** – Relations encode meaningful semantics (e.g., *announces*, *contains*, *registration*) between assets.
2. **Graph Navigation** – They enable powerful queries such as tracing supply chain dependencies or resolving domain-to-IP mappings.
3. **Explainability** – Each relation retains source, timestamp, and confidence, making inferences and automated decisions transparent and reproducible.

## :material-graph-outline: Relation Definition

> **Relation**: *A typed, directional edge connecting two assets that captures a discoverable or inferred relationship between them.*

Each relation answers three questions:

1. **What is the connection?**
   The **label** (e.g., *dns_record*, *contains*, *owns*, *announces*).
2. **What assets are involved?**
   A **source asset** and a **target asset**, each uniquely identified.
3. **When was it discovered?**
   A timestamp for when it was first and most recently seen.

## :material-graph-outline: Core Relation Schema

```json
{
  "label": "contains",
  "source": "Netblock/192.0.2.0-24",
  "target": "IPAddress/192.0.2.4",
  "created_at": "2025-06-20T14:22:00Z",
  "last_seen": "2025-06-20T14:22:00Z",
}
```

## :material-graph-outline: Common Relation Labels (Partial)

| Relation Type        | From (Source Asset) | To (Target Asset)         | Meaning                      |
| -------------------- | ------------------- | ------------------------- | ---------------------------- |
| **dns_record**       | FQDN                | IPAddress                 | DNS resolved A/AAAA record   |
| **contains**         | Netblock            | IPAddress                 | IP belongs to CIDR range     |
| **announces**        | AutonomousSystem    | Netblock                  | AS BGP route announcement    |
| **registration**     | Netblock            | IPNetRecord               | Ownership or allocation data |

*The list is extensible—new relation types are added as threat models and data sources evolve.*

## :material-graph-outline: Directionality and Semantics

Relations are **directed**: a relation from *A → B* is not the same as *B → A*. For instance:

* *FQDN → IPAddress* via `dns_record` indicates resolution;
* *IPAddress → FQDN* is not automatically implied and may require reverse DNS (`ptr_record`).

Understanding directionality is key to constructing valid traversal paths and interpreting graph queries.

## :material-graph-outline: Role in Graph Queries

Relations are the **edges** that enable:

* Ownership traversal: *Domain → Organization → LegalName*
* Infrastructure mapping: *Service → IP → Netblock → AS*
* Contact pivoting: *TLSCertificate → ContactRecord → Organization*

The expressive power of the model arises from chaining these relations through triple-based queries.

Example:

> *“Which TLS certificates are served from IPs owned by ASNs linked to Acme Corp?”*

This query may walk:
`Organization → organization → ContactRecord → registrant → AutnumRecord → registration → AutonomousSystem → announces → Netblock → contains → IPAddress → port → Service → certificate → TLSCertificate`

## :material-graph-outline: Where to Go Next

Learn more about the structure and usage of the model:

- [Assets](../assets/index.md) – The core entities in the graph.
- [Properties](../properties/index.md) – Descriptive metadata that enrich assets.
- [Triples](../assetdb/triples.md) – Performing graph queries using SPARQL-style syntax.
- [Assoc Tool](../framework_tools/assoc.md) – Using the command-line tool that queries the graph.
---

*© 2025 Jeff Foley — Licensed under Apache 2.0.*