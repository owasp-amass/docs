# :material-link-variant: affiliation

Organizations the subject is affiliated with — tied by a shared phone, person,
funder or address — each with the signals behind the link and a confidence. A
shared name alone is never enough. Part of [`amass lens`](../lenses.md).

```bash
amass lens affiliation -d owasp.org
amass lens affiliation -org "Example Corp"
```

## What you get

Candidate affiliations, each naming the shared attribute that links the two
organizations (a phone number, a contact person, a funder, or a postal
address) and a confidence. A membership or partnership the subject's own
documents state, read by the [document model](../../ai/documents.md), counts
too, as a weaker signal citing the document. These are leads to weigh, not
conclusions.

## Example

Run against `owasp.org`:

```text
Affiliations of owasp.org and open web application security project:
0 candidate(s).

No other organization shares a phone, person, funder or address with it.
```

A populated result names each candidate and its evidence:

```text
Affiliations of Example Labs: 2 candidate(s).
  Example Holdings — shares a registrant phone and a contact person (high)
  Partner Co — shares a funder: National Science Foundation (medium)
```

## Reading it

- **The shared attribute is the whole point** — an affiliation tied by a
  registrant phone and a named person is far stronger than one tied only by a
  shared grantor. The confidence reflects that.
- **Shared contact data requires stored contacts** ([`contacts`](contacts.md)),
  so an empty result often means the registration/contact sources returned
  nothing, not that no affiliation exists.
- Affiliation is a read-only view; to turn a judgment into a stored decision,
  use the review workflow ([`amass review`](../review.md)).

## See also

- [`family`](family.md) · [`contacts`](contacts.md) · [`funding`](funding.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
