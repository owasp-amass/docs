# :material-auto-fix: Asset Transformations Configuration

The `transformations` section of the OWASP Amass `config.yaml` file is one of
the most powerful parts of the collection engine. It controls **how data flows
through the system**, defines **which types of assets can be transformed into
others**, and sets **constraints like freshness (TTL), trustworthiness
(confidence), and urgency (priority)** on those transformations.

This section empowers users to **customize and optimize their data collection
workflows** based on their goals, risk tolerance, and update requirements.

## :material-help-circle-outline: What Are Transformations?

In Amass, the data collection process is modeled as a pipeline of **asset
transformations**. Each asset observed (like an IP address, domain, ASN, etc.)
can trigger **handlers**, which attempt to enrich, correlate, or expand on that
asset type by transforming it into new assets.

For example:

- A discovered `FQDN` might trigger a handler to look up its DNS records
  (`FQDN -> DNS`)
- A known `AutonomousSystem` could be transformed into its RDAP metadata
  (`AutonomousSystem -> RDAP`)
- A `Product` seen on a web service might lead to discovery of its
  `ProductRelease` metadata

The `transformations` section defines:

- **Which transformations are allowed**
- **How frequently** each transformation should be retried (`ttl`)
- **How much confidence** the system should have in the results (`confidence`)
- **How important** the transformation is (`priority`)

## :material-cog-outline: Configuration Overview

Here's the structure of a typical configuration:

```yaml
transformations:
  default:
    ttl: 1440         # in minutes (default is 1 day)
    confidence: 50    # default confidence threshold (0–100%)
    priority: 5       # default priority level (1=low, 10=high)
  FQDN->DNS:
    ttl: 1440
  AutonomousSystem->RDAP:
    ttl: 43200        # 30 days
  Identifier->GLEIF:
    ttl: 43200
  Product->ALL:
    ttl: 10080        # 7 days
```

### :gear: `default`

The `default` entry, the one key in `transformations` that isn't
`<from>-><to>`, defines fallback values used when no custom values are given
for a transformation. A transformation that leaves out `ttl` or `confidence` takes
the value from its type's `->ALL` transformation first (`FQDN->DomainRecord`
takes `FQDN->ALL`'s), then from these defaults.

| Key          | Type    | Description                                                                                                                 |
| ------------ | ------- | --------------------------------------------------------------------------------------------------------------------------- |
| `ttl`        | integer | Time-to-live (in minutes) for data freshness. If expired, the data will be fetched again from the source instead of reused. |
| `confidence` | integer | Evidence (0–100) needed before an asset reached through the transformation is admitted into scope. |
| `priority`   | integer | Priority score (1=lowest, 10=highest) that may influence queue ordering in some future extensions.                          |
| `reach`      | string  | Expansion policy: `scope`, `footprint` (default), `connected` or `any`. See "What is `reach`?" below. |
| `hops`       | integer | With `reach: connected`, how many relations from the footprint (default 1). |

## :hammer_and_wrench: Defining Transformations

Each transformation follows this format:

```yaml
<SourceAssetType>-><TargetAssetType|Plugin Name>:
  ttl: <int>           # Optional override of default
  confidence: <int>    # Optional override
  priority: <int>      # Optional override
  reach: <scope|footprint|connected|any>  # Optional expansion policy
  hops: <int>          # With reach: connected
```

Use `->ALL` as a wildcard to enable **all available transformations from a given
source asset type**.

Example:

```yaml
FQDN->ALL:
```

This enables all known FQDN transformations (e.g., `FQDN->IPAddress`,
`FQDN->DomainRecord`, etc.).

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

### Explanation

- **FQDN->DNS**: Amass will try to resolve DNS for fully qualified domain names
  once per day.
- **FQDN->DomainRecord**: Domain ownership records are more stable, so these are
  refreshed every 30 days.
- **IPAddress->ALL**: All available transformations for IPs are enabled (e.g.,
  geolocation, RDAP, reverse DNS).
- **TLSCertificate->ALL**: Certificates fetched from services are checked weekly.

## :material-refresh: What is `ttl`?

`ttl` (Time To Live) controls **how often a transformation can be retried** from
the original source:

- If the data is **still fresh** (within TTL), Amass will use the previously
  stored result from the database.
- If the TTL has **expired**, the handler will attempt to **re-run the
  transformation**, such as querying the data source again.

This ensures the system avoids unnecessary queries and controls bandwidth/load.

## :material-shield-check: What is `confidence`?

`confidence` is how strong the evidence must be before an asset reached
through the transformation is **admitted into the enumeration's scope**. When
evidence ties another domain, network or organization to the one you're
investigating, Amass scores it. With strong evidence, it's admitted only if
that score meets the transformation's `confidence`.

- With `confidence: 80`, a domain the evidence scores at 70 isn't admitted.
  It's still recorded, and waits for review.
- Raise it to widen the scope only on stronger evidence; lower it to widen
  more readily.

## :material-map-marker-radius: What is `reach`? (expansion policy)

`reach` decides **how far the enumeration investigates** beyond what you asked
about. It's set per transformation, like `ttl`, so you choose how much
expansion you're comfortable with, and for which kinds of work:

| `reach` | A transformation runs on an asset that is… |
|:--|:--|
| `scope` | within the scope the enumeration was given: the seed and the `scope` section |
| `footprint` | in scope, including what the run admitted into it on the evidence (the default) |
| `connected` | linked to the footprint within `hops` relations (1 to 5, default 1) |
| `any` | anything |

An asset that falls outside a transformation's reach is still stored. If the
scope later grows to take it in, it's investigated then. Assets the scope
can't judge by themselves take the standing of what they belong to: an
address that of the names resolving to it (through aliases too), a service
that of the name or address it runs on, a file that of its URL, a contact
record that of the domain registration or organization it belongs to, a phone
or street address that of whoever holds it. A vendor's identifiers and
contact details take the vendor's standing, so identifying every organization
doesn't spread the rest of the work to vendors.

Probing is held tighter: the port, banner and SSH probes, and HTTP probes of
names and addresses, run only on an address or name the scope takes in by
itself, whatever the `reach`. An address that only an in-scope name resolves
to can be a provider's shared host, so it isn't probed. A policy can narrow
this (`reach: scope` keeps probes off admitted assets) but not widen it.

A transformation without a `reach` takes its type's `->ALL` reach, then
`default`'s, then `footprint`. One setting can set the policy
for the whole configuration. A configuration that sets no `reach` anywhere
gets the footprint policy, and `amass enum` and the engine log say so:

```yaml
transformations:
  default:
    reach: footprint
  FQDN->DNS:
    reach: connected    # resolve names one step from the footprint
    hops: 1
  Organization->GLEIF:
    reach: any          # identify every organization, investigate only the target's
  Netblock->RDAP:
    reach: any          # look up who registered every network
  AutonomousSystem->RDAP:
    reach: any
  IPNetRecord->RDAP:
    reach: any          # the registration's registrant and contacts
  AutnumRecord->RDAP:
    reach: any
```

A network's registration, with its registrant and contacts, has to be read
before the network can be attributed to the organization and admitted into
the footprint, so the default configuration and the example policies look up
every netblock's and autonomous system's registration (RDAP) whatever the
`reach`. Nothing else is collected for a network outside the footprint.

Ready-made policies are in the `examples` directory beside the default
configuration (`resources/examples` in the Amass repository, `config/examples`
in the Docker Compose project):

| Policy | What it does |
|:--|:--|
| `policy-strict.yaml` | Investigates only the scope you gave. |
| `policy-footprint.yaml` | Recommended. Investigates the footprint, and resolves names linked to it to see whether they tie back. |
| `policy-horizontal-discovery.yaml` | Finds the organization's other domains and networks, widening on strong evidence. |
| `policy-third-party-mapping.yaml` | Identifies every vendor and provider, but investigates only the organization's own assets. |
| `policy-broad-passive.yaml` | Passive sources for everything, active probing and document reading only on the footprint. |

Merge one into your `config.yaml`: its transformations replace yours with the
same key, `default` included.

## :material-star: What is `priority`?

The `priority` value is a **relative score (1–10)** that can help inform which
transformations are more important. While not strictly enforced in the engine
today, this allows **future prioritization of more urgent or valuable
tasks**—like scanning attack surfaces or refreshing high-risk domains.

## :material-clipboard-list-outline: Tips and Best Practices

- ✅ Use `->ALL` to simplify enabling all known transformations for an asset type.
- ✅ Use higher TTLs (e.g., 30+ days) for records that rarely change (e.g.,
  `RDAP`, `GLEIF`, `DomainRecord`).
- ⚠️ Keep `ttl` low (e.g., 60–1440 min) for time-sensitive records like DNS,
  services, or IP geolocation.
- ✅ Set `confidence` thresholds higher (e.g., 70–90) in production pipelines
  where trust is critical.
- ✅ Consider adjusting `priority` for critical infrastructure or high-value assets.

## :material-rocket-launch: Summary

The `transformations` section of the Amass configuration lets users **shape the
intelligence collection process**, optimize for **freshness vs. efficiency**,
and **control data quality** through TTLs and confidence scoring.

It is a key part of how Amass turns passive and active discoveries into
structured asset graphs that can drive attack surface monitoring, red teaming,
or asset attribution.

---

For a full list of supported asset types, refer to the [Open Asset Model documentation](../open_asset_model/index.md).

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
