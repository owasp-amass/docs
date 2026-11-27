# :material-alert-outline: exposure

What a domain or organization exposes that deserves attention: remote access,
databases, file sharing, management interfaces and login pages. Part of
[`amass lens`](../lenses.md).

```bash
amass lens exposure -d owasp.org
amass lens exposure -org "Example Corp"
```

## What you get

Findings grouped into classes, each with a short rationale for why it matters
and the services or URLs that fall into it. It is a triage view that points you
at the handful of things worth looking at first, drawn from stored probes.

## Example

Run against `owasp.org` (one class omitted — see note):

```text
Exposure of owasp.org and open web application security project:
154 service(s) and 1338 URL(s).

Login and administration pages (8): login and administration pages, found by
their path or page title, are targeted by credential stuffing and are often
left unprotected by mistake.
  dev.owasp.org:443  web-service  "Sign in ・ Cloudflare Access"
  labs.training.owasp.org:443  web-service (nginx)  "Sign in - Sourcegraph"
  … 
```

## Reading it

- **Each class leads with why it matters**, so the output doubles as an
  explanation you can hand to someone else. Login pages behind an SSO gate
  (Cloudflare Access here) are lower risk than an unauthenticated admin panel —
  exposure surfaces them; you judge them.
- Amass also flags a **credentials-in-URL** class (a password written into a
  link). Treat any such value as disclosed and rotate it — for that reason this
  guide does not reproduce the offending URLs.
- Exposure is a **summary**; the [`dangling`](dangling.md),
  [`certificates`](certificates.md) and [`vulnerable`](vulnerable.md) lenses go
  deeper on their own areas.

## See also

- [`services`](services.md) · [`headers`](headers.md) · [`dangling`](dangling.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
