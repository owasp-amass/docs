# :material-identifier: identifiers

The registered identifiers of a domain or organization — LEI, tax, company and
registry numbers and handles — attached to what it controls, grouped by type.
Part of [`amass lens`](../lenses.md).

```bash
amass lens identifiers -d owasp.org
amass lens identifiers -org "Example Corp"
```

## What you get

Each stored identifier with its type and the asset that holds it, then a count
by type. Identifiers are the strong signals Amass uses to tell two
organizations apart or recognize them as the same — a shared LEI or company
number means far more than a shared name.

## Example

Run against `owasp.org`:

```text
Registered identifiers of owasp.org and open web application security project:
2 identifier(s) in 2 type(s).

  LEGAL_NAME: Open Web Application Security Project
  ORG_NAME:   Open Web Application Security Project

By type:
  LEGAL_NAME: 1
  ORG_NAME: 1
```

## Reading it

- **Identifier types** range from names (`ORG_NAME`, `LEGAL_NAME`) to strong
  registry keys (`LEI`, `DUNS`, `EIN`, company and tax numbers). A registry key
  is what lets the [`db identity`](../db.md) and [`db duplicates`](../db.md)
  scans decide two records are the same company without relying on the name.
- Here only the names are on record. Enabling identity sources (GLEIF by LEI,
  registries) would add registry numbers — see
  [Organizations: identity and geography](../../ai/organizations.md).

## Breach exposure

For an **email** identifier, Amass can also record the known data breaches it
appears in — breach name, date and data classes, **never the leaked secret**
— collected from an opt-in source (XposedOrNot free, HIBP keyed). The lens
reports each exposed email and a count, and the [`report`](report.md) lens
raises it as a priority-1 key finding. Exposure is a stored observation from an
outside authority, so unlike the computed identifier list it is collected, not
derived.

## See also

- [`db` (database hygiene)](../db.md) · [`accounts`](accounts.md) ·
  [`contacts`](contacts.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
