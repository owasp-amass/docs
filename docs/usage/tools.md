# :material-tools: Other Subcommands

Beyond [enumeration](enum.md), [lenses](lenses.md), [database hygiene](db.md)
and [review](review.md), the framework has a few focused subcommands, each with
its own page:

## :material-vector-polyline: Associations { #associations }

[`amass assoc`](assoc.md) walks the Asset Database along a path you describe as
a series of triples (subject–predicate–object) — the
[Triples Query Language](../asset_db/triples.md) on the command line. See
**[Association walks](assoc.md)**.

## :material-shield-bug: Vulnerability data { #vulnerability-data }

[`amass vuln-update`](vuln-update.md) fetches and refreshes the NVD CVE and
CISA KEV data that the [`vulnerable`](lenses/vulnerable.md) lens matches
against. See **[Vulnerability data](vuln-update.md)**.

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
