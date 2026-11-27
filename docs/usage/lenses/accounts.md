# :material-account-multiple-outline: accounts

The platform accounts (code hosts, social media and the like) a domain or
organization has, computed from the profile URLs stored for it. Part of
[`amass lens`](../lenses.md).

```bash
amass lens accounts -d owasp.org
amass lens accounts -org "Example Corp"
```

## What you get

Each recognized account — the platform and the handle — inferred from profile
URLs in the database (a `github.com/<org>` link becomes a GitHub account, and
so on). When no profile URLs have been collected, the lens reports none.

## Example

Run against `owasp.org`:

```text
Platform accounts of owasp.org and open web application security project:
0 account(s) on 0 platform(s).

No platform account is recognizable from the stored URLs.
```

A populated result groups accounts by platform (GitHub, LinkedIn, X, Mastodon,
and so on), each with the handle and the URL it was derived from. OWASP's
public profiles exist on the web, but none had been collected as stored URLs in
this run — enumerating the project's pages, or its `web` surface more deeply,
would surface them.

## Reading it

- Accounts are **derived from stored profile URLs**, so the richer the web
  collection ([`web`](web.md)), the more this finds.
- Handles tie an organization to its presence on third-party platforms — useful
  for attribution and for spotting impersonation accounts.

## See also

- [`web`](web.md) · [`identifiers`](identifiers.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
