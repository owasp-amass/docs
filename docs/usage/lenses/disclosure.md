# :material-bug-check-outline: disclosure

How a domain or organization invites vulnerability reports: the `security.txt`
security contacts, policy and encryption links, and which files have expired.
Part of [`amass lens`](../lenses.md).

```bash
amass lens disclosure -d owasp.org
amass lens disclosure -org "Example Corp"
```

## What you get

For each host that publishes a `security.txt`, the security contacts it lists,
the policy / acknowledgments / encryption links, and the file's expiry — with
expired files flagged, since an expired `security.txt` is considered invalid.

## Example

Run against `owasp.org`:

```text
Vulnerability-disclosure posture of owasp.org and open web application
security project.

owasp.org (expires 2027-12-31)
  contacts: support@owasp.org
  acknowledgments: https://owasp.org/security
```

## Reading it

- **Contacts** are where to send a report — the `Contact:` fields from the
  published `security.txt` (RFC 9116).
- **The expiry** matters: `security.txt` carries a mandatory `Expires` field,
  and a file past it should be treated as stale. The lens flags expired files so
  you can tell a maintained disclosure process from an abandoned one.
- A host with **no `security.txt`** simply does not appear — its absence is
  itself a finding if you expected one.

## See also

- [`exposure`](exposure.md) · [`contacts`](contacts.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
