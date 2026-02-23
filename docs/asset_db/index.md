# :simple-owasp: Asset Database

The **Asset Database** is the persistent store for all
entities and relations discovered during an Amass
enumeration. It is backed by the
[`owasp-amass/asset-db`][asset-db] library, which
provides a unified repository interface over multiple
storage backends.

[asset-db]: https://github.com/owasp-amass/asset-db

Every Amass **Session** receives its own database
connection. Assets are stored as typed entities
following the [Open Asset Model][oam]; the connections
between them are stored as directed edges (relations)
with optional properties attached to both entities
and edges.

[oam]: ../open_asset_model/index.md

## :material-database: Supported Backends

| Backend | Connection String | Best For |
| :--- | :--- | :--- |
| **SQLite** | Auto-created | Dev, quick scans |
| **PostgreSQL** | `postgres://u:p@host:5432/db` | Production |
| **Neo4j** | `neo4j://u:p@host:7687/db` | Graph queries |

If no database is configured, Amass automatically
creates a local SQLite database in its configuration
directory.

## :material-cog: Configuring the Database

Set the connection string in `config.yaml`:

```yaml
options:
  database: "postgres://amass:amass4OWASP@host:5432/db"
```

You can also configure the database via environment
variables, which take precedence over the config file:

```text
AMASS_DB_USER      database username
AMASS_DB_PASSWORD  database password
AMASS_DB_HOST      database host
AMASS_DB_PORT      database port
AMASS_DB_NAME      database name
```

## :material-graph-outline: How It Fits Together

The asset database sits at the center of the data
model. The Amass engine writes every discovered asset
into the database during enumeration. Assets are
stored once and referenced many times — the same IP
address discovered by multiple data sources is a
single entity with multiple `SourceProperty`
annotations.

Relations between assets (e.g., an FQDN resolving to
an IP address via a `dns_record` relation) are stored
as directed edges. This graph structure is what makes
the [Triples Query Language](triples.md) possible.

## :material-page-next: Next Steps

- [PostgreSQL Setup](postgres.md) — production
  PostgreSQL setup guide
- [Triples Query Language](triples.md) — traverse
  the asset graph with subject-predicate-object queries

---

*© 2025 Jeff Foley — Licensed under Apache 2.0.*
