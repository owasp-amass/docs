# :material-card-account-details-outline: contacts

The contact details of a domain or organization: phone numbers, email
addresses, contact people and postal addresses, from stored contact records.
Part of [`amass lens`](../lenses.md).

```bash
amass lens contacts -d owasp.org
amass lens contacts -org "Example Corp"
```

## What you get

A count of each kind of contact detail, then the details themselves, drawn from
registration (RDAP/WHOIS) and other contact records. When nothing is stored,
the lens says so plainly rather than inventing anything.

## Example

Run against `owasp.org`:

```text
Contacts for owasp.org and open web application security project:
0 phone(s), 0 email(s), 0 person(s), 0 address(es).

No contact details are stored.
```

An empty result like this is itself informative: it means the registration and
contact sources either returned nothing (many registries redact contacts) or
have not been collected yet. A populated result lists each phone, email,
contact person and postal address with the record it came from — for example a
registrant phone or an RDAP abuse address, which the
[`geography`](geography.md) lens also uses to infer an organization's country.

## Reading it

- **Treat contact data as sensitive.** It often contains personal information;
  handle it accordingly and only for authorized assessment.
- To populate it, enable the registration (RDAP/WHOIS) data sources and
  re-enumerate (see [`coverage`](coverage.md)).

## See also

- [`disclosure`](disclosure.md) · [`identifiers`](identifiers.md) ·
  [`geography`](geography.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
