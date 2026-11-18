# :material-email-outline: email

The mail security of a domain or organization's domains: the mail providers,
the SPF and DMARC policies and DKIM selectors, and which domains can be spoofed
because the records are missing or weak. Part of [`amass lens`](../lenses.md).

```bash
amass lens email -d owasp.org
amass lens email -org "Example Corp"
```

## What you get

Per domain: who handles its mail, its SPF and DMARC policy, its DKIM selectors,
and a flag if the configuration leaves the domain spoofable. A summary groups
domains by mail provider.

## Example

Run against `owasp.org`:

```text
Mail security of owasp.org and open web application security project:
1 domain(s).

Mail handled by:
  Google Workspace: 1 domain(s), e.g. owasp.org

owasp.org
  SPF:   v=spf1 include:_spf.google.com include:servers.mcsv.net
         include:amazonses.com -all
  DMARC: p=quarantine
  DKIM:  selector "google"
```

## Reading it

- **SPF ending in `-all`** is a hard fail — only the listed senders (Google,
  Mailchimp's `servers.mcsv.net`, Amazon SES) may send as the domain. A `~all`
  (soft fail) or missing SPF is weaker and is flagged.
- **DMARC `p=quarantine`** tells receivers to quarantine messages that fail
  alignment; `p=reject` is stronger and `p=none` (or no DMARC) means the domain
  can be spoofed — which the lens calls out.
- **DKIM selectors** show which signing keys are published. Together these three
  decide whether mail from the domain can be forged.

Records are read from stored DNS, interpreted per SPF (RFC 7208) and DMARC
(RFC 7489).

## See also

- [`exposure`](exposure.md) · [`concentration`](concentration.md) ·
  [`domains`](domains.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
