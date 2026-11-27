# :material-card-account-details-outline: contacts

The contact details of a domain or organization: phone numbers, email
addresses, contact people and postal addresses, from stored contact records,
mailboxes found at its domains, and its documents. Part of [`amass lens`](../lenses.md).

```bash
amass lens contacts -d owasp.org
amass lens contacts -org "Example Corp"
```

## What you get

A count of each kind of contact detail, then the details themselves, each with
where it was found:

- **contact record**: a registration (RDAP/WHOIS) or other contact record, an
  organization or a person names it.
- **document**: a document on one of its domains contains it, such as a
  phone number or email address in a published report.
- **collected**: an address at one of its domains that the enumeration found
  elsewhere, such as on a web page. It's shown only when nothing more specific
  names the address.

When nothing is stored, the lens says so plainly rather than inventing
anything.

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
contact person and postal address with where it was found — for example a
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
