# :material-earth: geography

Where a domain or organization is: the countries of its stored addresses and
registrations, and the countries its hosting providers are registered in, by
how many names each hosts. For an organization it also reports an **inferred
country**. Part of [`amass lens`](../lenses.md).

```bash
amass lens geography -d owasp.org
amass lens geography -org "Example Corp"
```

## What you get

Three things, when the evidence is present: the organization's own inferred
country (from its legal jurisdiction, a registration or contact address, or a
registrant phone); the countries of any stored postal addresses; and the
countries the parties hosting its names are registered in.

## Example

Run against `owasp.org`:

```text
Geography of owasp.org and open web application security project, from 1551
controlled asset(s).

No address of its own is stored.

Where the parties hosting its names are registered, by names hosted:
  US: 44 name(s), e.g. cloudflare, vercel
  unknown: 19 name(s), e.g. IP addresses with no recorded network owner, …

Registration addresses show where a party is registered, not where its
servers run.
```

## Reading it

- **Hosting country is about the provider, not the packets.** "US: 44 names,
  e.g. cloudflare, vercel" means those names are served by US-registered
  providers; a Cloudflare-fronted name may still be answered from an edge near
  the visitor. The lens is explicit about this distinction.
- **`unknown`** covers addresses with no stored network owner yet — a cue to
  enumerate further (see [`coverage`](coverage.md)).
- **For an organization**, the inferred country is Amass's best single
  determination and is labelled with the signal it came from. See
  [Organizations: identity and geography](../../ai/organizations.md) for how
  that inference works.

## See also

- [`network`](network.md) — the ASNs and netblocks behind the hosting
- [`cloud`](cloud.md) — which cloud/CDN providers host the names

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
