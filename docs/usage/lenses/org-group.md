# :material-office-building-outline: org-group

The corporate group around an organization: its ultimate parent and every
subsidiary and unit, from stored control relationships, with each one's
jurisdiction and registration number. From a domain, the group of its main
organization. Part of [`amass lens`](../lenses.md).

```bash
amass lens org-group -org "Example Corp"
amass lens org-group -d owasp.org
```

## What you get

An indented tree of the group — ultimate parent at the top, subsidiaries and
organizational units beneath — each with its jurisdiction and registration
number. The links are **stored control relationships** (such as GLEIF
parent/child records), never inferred from a shared name.

## Example

Run against `owasp.org` (its main organization resolves to the host here):

```text
Corporate group of cloudflare, the main organization of owasp.org
(1 organization(s)), from stored org_unit and subsidiary relationships.

  cloudflare  (US-DE, reg 4710875)

No parent, subsidiary or unit of cloudflare is stored. GLEIF records parents
and subsidiaries for organizations with an LEI, and reviewed department
proposals add units.
```

## Reading it

- **A single-node group** means no control relationships are stored yet — not
  that the company has none. The footer names how they get populated: GLEIF
  (by LEI) for parents/subsidiaries, and reviewed proposals for units.
- **Jurisdiction and registration** (`US-DE, reg 4710875`) come from the stored
  organization record and are the strong keys that distinguish same-named
  companies.
- Group structure powers the [`group-funding`](group-funding.md) and
  [`group-vendors`](group-vendors.md) roll-ups.
- **Units its own documents name** follows the tree when a
  [document model](../../ai/documents.md) has read the organization's
  documents: the offices, departments, campuses and programs they name, each
  marked stored or not stored, with the number of documents and an example.
  This list is read-only. A unit that isn't stored can be added by approving
  its proposal with [`amass review`](../review.md).

## See also

- [`family`](family.md) · [`group-funding`](group-funding.md) ·
  [`group-vendors`](group-vendors.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
