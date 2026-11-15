# :material-tools: Other Subcommands

Beyond [enumeration](enum.md), [lenses](lenses.md) and [review](review.md),
the framework has a few focused subcommands.

## :material-vector-polyline: Associations { #associations }

`amass assoc` walks the Asset Database along a path you describe as a series
of triples (subject–predicate–object), the same graph structure the
[Triples Query Language](../asset_db/triples.md) uses.

```bash
amass assoc -t1 "FQDN,dns_record,IPAddress" -t2 "IPAddress,contains,Netblock"
```

| Flag | Meaning |
| :--- | :--- |
| `-t1 … -t10 <triple>` | Up to ten triples defining the walk |
| `-tf <file>` | A file of triples |

## :material-graph: Visualizations { #visualizations }

`amass viz` renders the stored graph for a domain in a format you can open
elsewhere.

```bash
amass viz -d3 -d example.com      # interactive D3 force graph (HTML)
amass viz -dot -d example.com     # Graphviz DOT
amass viz -gexf -d example.com    # GEXF for Gephi
```

| Flag | Meaning |
| :--- | :--- |
| `-d3` | D3 v4 force-simulation HTML |
| `-dot` | Graphviz DOT |
| `-gexf` | Gephi Graph Exchange XML (GEXF) |
| `-o <dir>` / `-oA <prefix>` | Output directory and file prefix |
| `-since <time>` | Include only assets validated after a time |

The AI subcommand can also render a graph through its tools; see
[AI](../ai/index.md).

## :material-shield-bug: Vulnerability data { #vulnerability-data }

`amass vuln-update` fetches or refreshes the vulnerability data the
[`vulnerable` lens](lenses.md#vulnerable) reads: NVD's CVE records and
CISA's Known Exploited Vulnerabilities catalog. Run it before the lens, and
periodically to keep the data current.

```bash
amass vuln-update
amass lens vulnerable -d example.com
```

It retries, saves partial progress, and honors a minimum interval between
NVD refreshes so it does not over-ask the source.

## :material-engine: Engine { #engine }

`amass engine` runs the collection engine as a standalone service that
`amass enum` can connect to with `-engine <url>`. Running enum without a
separate engine starts a local one automatically, so this is for setups that
share one engine across clients.
