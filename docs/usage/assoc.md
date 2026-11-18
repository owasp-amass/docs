# :material-vector-polyline: Association walks

`amass assoc` queries the [Asset Database](../asset_db/index.md) directly, by
walking a path of **triples** you give it. Where a [lens](lenses.md) answers a
fixed question, `assoc` lets you express an arbitrary traversal — "from this
name, follow these relationships, and show me what you reach." It is the
command-line face of the [triples query language](../asset_db/triples.md).

## A single-hop walk

Each `-t<n>` flag is one triple: a subject, a predicate, and an object.

```bash
amass assoc -t1 '<fqdn:owasp.org> - <*:node> -> <*>'
```

This starts at the FQDN `owasp.org`, follows every `node` relationship, and
returns whatever it reaches.

## Chaining hops

The object of one triple feeds the subject of the next, so a walk can cross
several relationships. Up to ten triples (`-t1` … `-t10`) can be chained:

```bash
amass assoc \
  -t1 '<fqdn:owasp.org> - <*:node> -> <*>' \
  -t2 '<fqdn:*> - <*:dns_record> -> <ipaddress:*>'
```

The first triple gathers the names under `owasp.org`; the second takes those
names and returns the IP addresses their DNS records point to.

For a long or reused walk, keep the triples in a file and pass it with `-tf`:

```bash
amass assoc -tf owasp-walk.txt
```

## Options

| Flag | Meaning |
| :--- | :--- |
| `-t1` … `-t10` | The triples of the walk, in order |
| `-tf <file>` | Read the triples from a file, one per line |
| `-config <file>` / `-dir <path>` | Configuration file and data directory |
| `-nocolor` / `-silent` | Plain or no output |

## Reading the output

`assoc` prints the assets each triple reached and the full walk that connected
them, so you can see not just the endpoints but the path of evidence between
them. The entire walk — every node and the properties along it — is available
as JSON for further processing.

See [Triples](../asset_db/triples.md) for the full syntax: constants,
wildcards (`*`), regular expressions (`#/.../#`), and property filters such as
`prop:[sourceproperty:...,since:...,confidence:...]`.

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
