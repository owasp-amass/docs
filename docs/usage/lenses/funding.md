# :material-cash-multiple: funding

The funding a domain's or organization's company has received, from stored
`FundsTransfer` records: each round or award with its amount, date and the
investor or agency behind it, and a total when the rounds share a currency.
Part of [`amass lens`](../lenses.md).

```bash
amass lens funding -d owasp.org
amass lens funding -org "Example Corp"
```

## What you get

One line per funding event — amount, date, and the funder (investor, agency or
contracting body) — with a total per currency. Funding comes from keyless
public sources: US federal awards and grants (USAspending, NSF, NIH, SBIR), US
nonprofit and securities filings (ProPublica, SEC EDGAR), and public
procurement (TED, Open Contracting / OCDS).

## Example

Run against `owasp.org`:

```text
Funding of owasp.org and open web application security project:
0 round(s), 0 investor(s).

No funding record is stored.
```

Nothing matched here — the public funding sources did not return a record tied
to this organization in this run. A populated result looks like:

```text
Funding of Example Labs: 3 round(s), total $12,500,000.
  2024-06-01  $8,000,000   Series A   led by Example Ventures
  2022-03-15  $3,500,000   Seed       led by Angel Fund LLC
  2021-09-01  $1,000,000   Grant      National Science Foundation
```

## Reading it

- **The funder on each line** is a strong signal of an organization's backers,
  partners and grantors — modelled as `FundsTransfer --third_party-->
  Organization`.
- **An empty result is not proof of no funding** — only that the keyless
  sources stored nothing for it. Coverage depends on which sources apply (a US
  nonprofit shows up via ProPublica's 990 data; a European supplier via TED).
- See [Funding and procurement data](../../ai/funding.md) for the full source
  list and how a transfer is modelled.

## See also

- [`group-funding`](group-funding.md) ·
  [Funding and procurement](../../ai/funding.md)

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
