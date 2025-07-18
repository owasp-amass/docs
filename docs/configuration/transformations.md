# :material-auto-fix: Asset Transformations Configuration

The `transformations` section of the OWASP Amass `config.yaml` file is one of the most powerful parts of the collection engine. It controls **how data flows through the system**, defines **which types of assets can be transformed into others**, and sets **constraints like freshness (TTL), trustworthiness (confidence), and urgency (priority)** on those transformations.

This section empowers users to **customize and optimize their data collection workflows** based on their goals, risk tolerance, and update requirements.

## :material-help-circle-outline: What Are Transformations?

In Amass, the data collection process is modeled as a pipeline of **asset transformations**. Each asset observed (like an IP address, domain, ASN, etc.) can trigger **handlers**, which attempt to enrich, correlate, or expand on that asset type by transforming it into new assets.

For example:
- A discovered `FQDN` might trigger a handler to look up its DNS records (`FQDN -> DNS`)
- A known `AutonomousSystem` could be transformed into its RDAP metadata (`AutonomousSystem -> RDAP`)
- A `Product` seen on a web service might lead to discovery of its `ProductRelease` metadata

The `transformations` section defines:
- **Which transformations are allowed**
- **How frequently** each transformation should be retried (`ttl`)
- **How much confidence** the system should have in the results (`confidence`)
- **How important** the transformation is (`priority`)

## :material-cog-outline: Configuration Overview

Here's the structure of a typical configuration:

```yaml
options:
  default_transform_values:
    ttl: 1440         # in minutes (default is 1 day)
    confidence: 50    # default confidence threshold (0–100%)
    priority: 5       # default priority level (1=low, 10=high)

transformations:
  FQDN->DNS:
    ttl: 1440
  AutonomousSystem->RDAP:
    ttl: 43200        # 30 days
  Identifier->GLEIF:
    ttl: 43200
  Product->ALL:
    ttl: 10080        # 7 days
```

### :gear: `default_transform_values`

This section defines fallback values used when no custom values are given for a transformation.

| Key          | Type    | Description                                                                                                                 |
| ------------ | ------- | --------------------------------------------------------------------------------------------------------------------------- |
| `ttl`        | integer | Time-to-live (in minutes) for data freshness. If expired, the data will be fetched again from the source instead of reused. |
| `confidence` | integer | Minimum confidence (0–100%) required to accept the result of a transformation.                                              |
| `priority`   | integer | Priority score (1=lowest, 10=highest) that may influence queue ordering in some future extensions.                          |

## :hammer_and_wrench: Defining Transformations

Each transformation follows this format:

```yaml
<SourceAssetType>-><TargetAssetType|Plugin Name>:
  ttl: <int>           # Optional override of default
  confidence: <int>    # Optional override
  priority: <int>      # Optional override
```

Use `->ALL` as a wildcard to enable **all available transformations from a given source asset type**.

Example:

```yaml
FQDN->ALL:
```

This enables all known FQDN transformations (e.g., `FQDN->IPAddress`, `FQDN->DomainRecord`, etc.).

## :page_facing_up: Example Config Breakdown

```yaml
transformations:
  FQDN->DNS:
    ttl: 1440  # 1 day
  FQDN->DomainRecord:
    ttl: 43200  # 30 days
  IPAddress->ALL:
  TLSCertificate->ALL:
    ttl: 10080  # 7 days
```

### Explanation:

* **FQDN->DNS**: Amass will try to resolve DNS for fully qualified domain names once per day.
* **FQDN->DomainRecord**: Domain ownership records are more stable, so these are refreshed every 30 days.
* **IPAddress->ALL**: All available transformations for IPs are enabled (e.g., geolocation, RDAP, reverse DNS).
* **TLSCertificate->ALL**: Certificates fetched from services are checked weekly.

## :material-refresh: What is `ttl`?

`ttl` (Time To Live) controls **how often a transformation can be retried** from the original source:

* If the data is **still fresh** (within TTL), Amass will use the previously stored result from the database.
* If the TTL has **expired**, the handler will attempt to **re-run the transformation**, such as querying the data source again.

This ensures the system avoids unnecessary queries and controls bandwidth/load.

## :material-shield-check: What is `confidence`?

`confidence` helps Amass **filter out noisy or speculative results**. Some plugins or handlers may return results with associated confidence scores.

* If a handler returns a transformation with `confidence: 40`, and your threshold is `50`, **it will be ignored**.
* Use this to reduce false positives or to tune behavior in environments where high data quality is crucial.

## :material-star: What is `priority`?

The `priority` value is a **relative score (1–10)** that can help inform which transformations are more important. While not strictly enforced in the engine today, this allows **future prioritization of more urgent or valuable tasks**—like scanning attack surfaces or refreshing high-risk domains.

## :material-clipboard-list-outline: Tips and Best Practices

* ✅ Use `->ALL` to simplify enabling all known transformations for an asset type.
* ✅ Use higher TTLs (e.g., 30+ days) for records that rarely change (e.g., `RDAP`, `GLEIF`, `DomainRecord`).
* ⚠️ Keep `ttl` low (e.g., 60–1440 min) for time-sensitive records like DNS, services, or IP geolocation.
* ✅ Set `confidence` thresholds higher (e.g., 70–90) in production pipelines where trust is critical.
* ✅ Consider adjusting `priority` for critical infrastructure or high-value assets.

## :material-rocket-launch: Summary

The `transformations` section of the Amass configuration lets users **shape the intelligence collection process**, optimize for **freshness vs. efficiency**, and **control data quality** through TTLs and confidence scoring.

It is a key part of how Amass turns passive and active discoveries into structured asset graphs that can drive attack surface monitoring, red teaming, or asset attribution.

---

For a full list of supported asset types, refer to the [Open Asset Model documentation](../open_asset_model/index.md).

*© 2025 Jeff Foley — Licensed under Apache 2.0.*
