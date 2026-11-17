# Funding and procurement data (development preview)

!!! warning "Unreleased feature"
    This page describes the `feature/ai-investigation-inference` branches.
    These capabilities are not yet published or production-ready.

Amass collects the public funding an organization has received — venture
rounds, government grants, contracts and procurement awards — and stores each
as a `FundsTransfer` in the Open Asset Model. The [`funding`](../usage/lenses.md#funding)
and [`group-funding`](../usage/lenses.md#group-funding) lenses surface it. A
funder named on a transfer is a strong signal of an organization's backers,
partners, suppliers and grantees.

## How a transfer is modelled

Each award or round is one `FundsTransfer` (its amount, currency and date). It
is linked:

- `FundsTransfer --recipient--> Account` — a checking `Account` the recipient
  organization controls, so the organization's funding is reachable from the
  organization.
- `FundsTransfer --third_party--> Organization` — the funder (investor, agency
  or contracting body).

The Asset Database rejects a transfer with a non-positive amount, so a record
with no monetary value is skipped rather than stored.

## Sources

All of the collectors below are **keyless and on by default** — no API key or
setup. Each applies only where it has coverage (a US source matches nothing for
a non-US organization, and stores nothing), requests are rate-limited, and
collection follows the normal TTL cadence. Any source can be turned off per
session through the `transformations` section of the configuration (see
[Transformations](../configuration/transformations.md)); each grant source is
its own named source so they can be excluded individually.

| Source | Region | What it adds |
| :--- | :--- | :--- |
| USAspending | US | Federal contracts and assistance |
| NSF, NIH-RePORTER, SBIR | US | Federal research grants |
| ProPublica | US | Nonprofit 990 data (EIN, address, contributions) |
| SEC-EDGAR | US | CIK, Form D raises, business phone and address |
| TED | EU | European public procurement |
| OCDS publishers | International | Public procurement (see below) |

## Open Contracting (OCDS)

The Open Contracting Data Standard normalizes procurement data, so one parser
reads every publisher; what differs is each publisher's access method, recorded
as data in the publisher catalog. A publisher is used only after its endpoint
and response shape are validated against a real sample.

- **Supplier-search publishers** expose an API that can be queried by supplier
  name; the collector queries it per organization.
- **Bulk publishers** publish only a full export (newline-delimited compiled
  releases, optionally gzipped). Bulk ingestion is **on-demand**: the export is
  downloaded (once per day, then streamed and matched by supplier) only when an
  organization from that publisher's own country is enumerated, so a run that
  touches no organizations from a country never downloads it. This covers a
  country with no supplier-search API without pulling every country's data. The
  amount is read from the award, or, when the award omits it, from the matching
  contract or the tender value.

Currently enabled publishers include Mexico (Nuevo León), the United Kingdom
(Find a Tender), Rwanda, the Dominican Republic, Honduras and Paraguay. To add
one, set its `bulk_url` (or a supplier-search `query_url`) in the catalog and
enable it after validating a sample from that publisher.

## Signals and inference

Government and registry identifiers collected alongside funding feed
correlation: a shared registry identifier (LEI, D-U-N-S, EIN, SEC CIK, …) is a
strong signal that two stored organizations are the same company, and shared
funders are a signal that two organizations are affiliated. These remain
[review](../usage/review.md) proposals; funding itself is a stored observation,
and the lenses compute their conclusions each time without writing them back.
