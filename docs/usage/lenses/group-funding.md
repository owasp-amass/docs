# :material-cash-sync: group-funding

The funding of a whole corporate group rolled up — the organization and every
parent, subsidiary and unit — merged, noting which group organization received
each round, with a group total. Part of [`amass lens`](../lenses.md).

```bash
amass lens group-funding -org "Example Corp"
amass lens group-funding -d owasp.org
```

## What you get

The same funding records as [`funding`](funding.md), merged across the
[group](org-group.md). One institution's funding is often split across records
that name different parts of it (a parent and a subsidiary, a university system
and a campus); this shows the whole picture when those records are linked.

## Example

Run against `owasp.org`:

```text
Funding across the corporate group of owasp.org:
0 round(s), 0 investor(s) across 0 organization(s).

No funding record is stored for the group.
```

With a funded group, each round is attributed to the member that received it,
and a group total is given:

```text
Funding across the corporate group of Example Holdings:
5 round(s), total $47,000,000 across 3 organization(s).
  Example Labs (subsidiary)   Series A   $8,000,000   2024-06-01
  Example EU GmbH (subsidiary) Grant (TED) €2,000,000  2023-11-20
  … 
```

## Reading it

- **The per-member attribution** shows where the money actually landed — useful
  when a parent's public profile hides funding that went to a subsidiary.
- **The group total** only sums rounds that share a currency; mixed-currency
  groups are listed without a single total.
- The group is built from stored control relationships (see
  [`org-group`](org-group.md)); if the group is a single node, this equals
  [`funding`](funding.md).

## See also

- [`funding`](funding.md) · [`org-group`](org-group.md) ·
  [Funding and procurement](../../ai/funding.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
