# Organization identity and geography (development preview)

!!! warning "Unreleased feature"
    This page describes the `feature/ai-investigation-inference` branches.
    These capabilities are not yet published or production-ready.

Much of what Amass reasons about hangs off an `Organization`: its funding, its
geography, its related entities, and whether two records are the same company.
That only works if the organization exists in the Asset Database. For a company
that hosts its web presence in the cloud, it often did not.

## The cloud-hosted gap

Amass has long created an `Organization` from three places, all of which fail
for a cloud-hosted company:

- the **netblock registrant** (RDAP/WHOIS) — this names the *host* (a CDN or
  cloud provider), not the company;
- the **TLS certificate subject** (`O=`) — empty on the Domain-Validated
  certificates that CDN and cloud front ends serve;
- the **domain WHOIS registrant** — redacted under privacy/GDPR for most gTLDs.

So a company behind a DV certificate and a privacy-protected domain produced no
organization of its own, and everything downstream had nothing to attach to.

## Identifying the company from the domain

Three sources now look the company up from the registered domain itself. Each is
**keyless and on by default**, rate-limited and TTL-cadenced, and can be turned
off per session through the `transformations` configuration (each is its own
named source).

| Source | Confidence | Mode | What it does |
| :--- | :--- | :--- | :--- |
| **Wikidata** | 85 | any | Reverse-looks-up the entity whose official website (P856) is the domain; stores its official name (P1448), country (P17) and LEI (P1278). |
| **GLEIF** | 100 | any | Enriches from an **exact LEI** (never a name search): legal name, jurisdiction, registration ID, addresses, related entities. |
| **schema.org homepage** | 50 | active | Reads the `Organization` a site publishes about itself (JSON-LD). Self-asserted, so lowest confidence; mainly corroborates and bootstraps the others via `sameAs`/`leiCode`. |

The sources are designed to chain. Wikidata (or the homepage markup) supplies an
**LEI**, which GLEIF then resolves to an authoritative record. A GLEIF *name*
search is deliberately not used to create organizations — it is too easily
wrong; only an exact LEI lookup is trusted. A name-only lead, if ever acted on,
would go through the reviewed proposal workflow, not direct collection.

### How the company attaches to the domain

A looked-up company is linked with relations the Open Asset Model already
defines, so no new ownership relation is introduced and the existing lenses
reason over it unchanged:

```
Organization --website--> URL --domain--> FQDN
```

Only one organization is created per domain: before creating, each source reuses
an organization already linked to the domain through that chain, so several
sources enrich one record rather than making duplicates. A rare simultaneous
race is reconciled by the attribution/duplicates merge.

Every asset and relation a source writes carries that source's provenance (a
`SourceProperty` with its name and confidence), so the Asset Database records
exactly which source asserted each fact and how much to trust it. Agreement
between sources raises confidence.

## Country inference

An organization's country is needed for geography, for distinguishing
same-named companies in different jurisdictions, and for gating country-specific
collectors (such as the on-demand procurement exports). It is inferred from
stored evidence by a shared, read-only helper, most credible first, each with
the strongest contributing signal and a confidence:

| Signal | Confidence | Source |
| :--- | :--- | :--- |
| Legal jurisdiction | 95 | ISO 3166 (GLEIF, registration) |
| Registration/contact address country | 75 | ISO 3166-1 alpha-2 (RDAP/WHOIS) |
| Registrant phone country | 55 | ITU-T E.164 calling code |

The signals, their paths and confidences are data
(`internal/semantics/org_country.json`), not code, and only valid two-letter
codes are accepted. A country found by several signals is raised by agreement.
The [`geography`](../usage/lenses.md#geography) lens reports this as an inferred
country for an organization, alongside the per-address counts.

## Related pages

- [Funding and procurement data](funding.md) — what attaches to an organization
  once it exists.
- [Lenses](../usage/lenses.md) — `geography`, `funding`, `family` and the rest.
