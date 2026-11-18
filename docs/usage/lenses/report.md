# :material-file-document-outline: report

The attack surface report: the key findings first, then a section from each
posture lens below. Start here. Part of [`amass lens`](../lenses.md).

```bash
amass lens report -d owasp.org
amass lens report -org "Example Corp"
```

## What you get

A single document: a **Key findings** list that pulls the most important items
to the top (takeovers, exposed services, unsupported software, expired domains
and certificates, email spoofing, mail-receiving lookalikes), then one section
per posture lens — exposure, dangling, certificates, domains, email,
disclosure, identifiers (with breach exposure), headers, lookalikes, services,
vulnerable, network, concentration, changes and coverage — each the same output
that lens produces on its own.

## Example

Run against `owasp.org` (heavily abridged):

```text
# Attack surface report: owasp.org
_Computed 2026-11-17 from the Amass Asset Database: what past enumerations
stored, not a live scan._

## Key findings
- Lookalike domains not tied to it that receive mail (8): 0wasp.org;
  owasp.co; owasp.com; …
- Lookalike domains not tied to it (7): iwasp.org; oasp.org; …

## What it exposes
  … exposure section …
## Dangling DNS
  … dangling section …
## Certificates
  … certificates section …
## Services
  … services section …
## Recent changes
  … changes section …
```

## Reading it

- **Breach exposure rises to the top.** If any collected email identifier
  appears in a known data breach, it is a priority-1 key finding
  ("Identifiers exposed in a known data breach") — the breach names only,
  never a secret. Enable a breach source (see [`identifiers`](identifiers.md))
  to populate it.
- **Read Key findings first.** It is the triage layer — each item is drawn from
  a lens below and ordered by priority, so you can act before reading the full
  sections. For owasp.org the top items are mail-receiving lookalike domains.
- **Each section is a full lens result**, so the per-lens pages in this
  reference explain how to read every part of the report.
- **Bound large targets** with `-max-assets` / `-max-reads`; the report says
  when a section is partial.
- For a graph instead of text, run [`amass viz`](../viz.md) over the same data.

## See also

Every lens it includes has its own page — start with
[`exposure`](exposure.md), [`dangling`](dangling.md),
[`certificates`](certificates.md) and [`vulnerable`](vulnerable.md).

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
