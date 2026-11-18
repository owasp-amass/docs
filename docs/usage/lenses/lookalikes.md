# :material-content-duplicate: lookalikes

Registered domains one typing mistake from the subject's, or under another
suffix, and whether each looks like the subject's own or another party's. Part
of [`amass lens`](../lenses.md).

```bash
amass lens lookalikes -d owasp.org
amass lens lookalikes -org "Example Corp"
```

## What you get

The stored lookalike domains, split by whether they appear to belong to the
subject or to someone else, each with signals that help you judge risk: whether
it **receives mail** (can be used for phishing) and its name servers.

## Example

Run against `owasp.org` (excerpt of 15 found):

```text
Lookalike domains of owasp.org and open web application security project:
15 stored of 107 checked; 15 not tied to it.

Not tied to it (15):
  0wasp.org  (like owasp.org): receives mail; ns: *.ns.cloudflare.com
  owasp.com  (like owasp.org): receives mail; ns: fay/west.ns.cloudflare.com
  owasp.net  (like owasp.org): receives mail; ns: *.ns.cloudflare.com
  owasp.co   (like owasp.org): receives mail; ns: *.domaincontrol.com
  owsap.org  (like owasp.org): receives mail; ns: *.klczy.com
  owas.org   (like owasp.org): ns: ns1/ns2.afternic.com
  owasp.io   (like owasp.org): ns: *.domaincontrol.com
  … 
```

## Reading it

- **"receives mail" is the risk multiplier.** A lookalike with MX records can
  send and receive mail as a near-twin of the real domain — the basis of
  business-email-compromise phishing. `0wasp.org` (zero for O) and `owasp.com`
  receiving mail are the ones to watch.
- **Name servers hint at intent.** Parking hosts (`afternic.com`) suggest a
  for-sale squat; a real mail/DNS setup suggests active use.
- **A lookalike is not automatically hostile** — many are defensive
  registrations or unrelated names. The lens surfaces candidates; you judge.
  Typo models follow Moore & Edelman (insertion, deletion, substitution,
  transposition, alternate suffix).

## See also

- [`domains`](domains.md) · [`email`](email.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
