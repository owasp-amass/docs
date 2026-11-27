# :material-history: Collection Runs

A **collection run** is one run of a tool that collected
data into the asset database: an Amass enumeration, an
import, or another scanner. Each run records what it was
asked to collect, when it started and ended, and how it
ended.

Runs let a reader tell two things apart that timestamps
alone cannot: something that a run looked for and did
not find, and something that nothing looked for. An
asset inside a finished run's scope that was last seen
before that run started was not found by the run.

Runs describe collection, not the assets themselves.
They are stored beside the graph, and the
[Open Asset Model][oam] is unchanged.

[oam]: ../open_asset_model/index.md

## :material-account-group: Any Tool Can Record Runs

The table is not specific to Amass. Any tool that writes
assets into the database can record its own runs, so
readers such as the Amass lenses can use runs from every
tool that contributed to the database.

- **Amass** records every enumeration session as a run
  with the tool name `amass`. Nothing needs to be
  configured.
- **Go tools** use the `RunRecorder` interface of the
  [`owasp-amass/asset-db`][asset-db] library, which works
  with PostgreSQL, SQLite and Neo4j.
- **Tools in other languages** write the
  `collection_run` table (PostgreSQL and SQLite) or
  `CollectionRun` nodes (Neo4j) directly, as shown below.

[asset-db]: https://github.com/owasp-amass/asset-db

## :material-table: Fields

| Field | Meaning |
| :--- | :--- |
| `run_id` | Unique ID of the run, such as a UUID |
| `tool` | Name of the tool, such as `amass` (required) |
| `tool_version` | Version of the tool |
| `external_id` | The tool's own ID for the run |
| `status` | `running`, `finished`, `stopped` or `failed` |
| `started_at` | When the run started, in UTC |
| `finished_at` | When the run ended, in UTC; empty while running |
| `scope` | JSON list of what the run was asked to collect |
| `metadata` | JSON object describing how the run collected |

PostgreSQL and SQLite also keep `created_at` and
`updated_at` on each row.

### Status

| Status | Meaning |
| :--- | :--- |
| `running` | The run has not ended |
| `finished` | The run ended with all of its work done |
| `stopped` | The run ended early, with work left |
| `failed` | The run ended because of an error |

Only a `finished` run should be read as complete. A run
that stopped or failed may have missed anything in its
scope. A run is finished at most once: the status of a
run that has ended does not change.

### Scope

The scope lists the targets a run was asked to collect.
Each target is an Open Asset Model asset type and the
key of that asset, written as it is stored:

```json
[
  {"type": "FQDN", "key": "example.com"},
  {"type": "IPAddress", "key": "198.51.100.7"},
  {"type": "Netblock", "key": "192.0.2.0/24"},
  {"type": "AutonomousSystem", "key": "64496"}
]
```

Amass reads a domain name in a run's scope as covering
the names beneath it.

### Metadata

Metadata is a free-form JSON object for how a run
collected. Amass records these keys:

| Key | Meaning |
| :--- | :--- |
| `mode` | `active`, `passive` or `default` |
| `widens` | Whether the expansion policy let the scope widen during the run |
| `brute_forcing` | Whether names were brute forced |
| `alterations` | Whether name alterations were tried |

Amass records its session ID as `external_id` and its
version as `tool_version`.

## :material-language-go: Recording Runs from Go

```go
import (
    "context"
    "time"

    "github.com/owasp-amass/asset-db/repository"
    "github.com/owasp-amass/asset-db/types"
    oam "github.com/owasp-amass/open-asset-model"
)

func collect(ctx context.Context, repo repository.Repository) error {
    runs, ok := repo.(repository.RunRecorder)
    if !ok {
        return collectWithoutRun(ctx, repo)
    }

    run, err := runs.StartRun(ctx, &types.CollectionRun{
        Tool:        "my-scanner",
        ToolVersion: "1.2.0",
        StartedAt:   time.Now().UTC(),
        Scope:       []types.RunTarget{{Type: oam.FQDN, Key: "example.com"}},
        Metadata:    map[string]any{"mode": "passive"},
    })
    if err != nil {
        return err
    }

    status := types.RunFinished
    if err := collectWithoutRun(ctx, repo); err != nil {
        status = types.RunFailed
    }

    // A zero time records the current time.
    _, err = runs.FinishRun(ctx, run.ID, status, time.Time{})
    return err
}
```

`StartRun` assigns the run's ID and sets its status to
`running`. `FinishRun` accepts `finished`, `stopped` or
`failed`, and fails when the run is not running.
`FindRunById` reads one run, and `FindRuns` reads the
runs started since a time, newest first, optionally
limited to some tools.

## :material-database-edit: Recording Runs Directly

Run the asset-db migrations first; Amass runs them when
it opens the database. Store every time in UTC.

### PostgreSQL

```sql
-- Start a run (PostgreSQL 13 or later for gen_random_uuid).
INSERT INTO public.collection_run
  (run_id, tool, tool_version, status, started_at, scope, metadata)
VALUES
  (gen_random_uuid()::text, 'my-scanner', '1.2.0', 'running',
   now() AT TIME ZONE 'UTC',
   '[{"type": "FQDN", "key": "example.com"}]'::jsonb,
   '{"mode": "passive"}'::jsonb)
RETURNING run_id;

-- Finish it.
UPDATE public.collection_run
SET status = 'finished',
    finished_at = now() AT TIME ZONE 'UTC',
    updated_at = now()
WHERE run_id = $1 AND status = 'running';
```

### SQLite

SQLite stores times as text in the fixed form
`YYYY-MM-DD HH:MM:SS.SSS`, in UTC, so that they sort
correctly. `scope` and `metadata` must be valid JSON.

```sql
INSERT INTO collection_run
  (run_id, tool, tool_version, status, started_at, scope, metadata)
VALUES
  (:id, 'my-scanner', '1.2.0', 'running',
   strftime('%Y-%m-%d %H:%M:%f', 'now'),
   '[{"type": "FQDN", "key": "example.com"}]',
   '{"mode": "passive"}');

UPDATE collection_run
SET status = 'finished',
    finished_at = strftime('%Y-%m-%d %H:%M:%f', 'now'),
    updated_at = strftime('%Y-%m-%d %H:%M:%f', 'now')
WHERE run_id = :id AND status = 'running';
```

### Neo4j

A run is a `CollectionRun` node, apart from the asset
graph. Times are `LocalDateTime` values in UTC, and
`scope` and `metadata` are JSON strings.

```cypher
CREATE (r:CollectionRun {
  run_id: $id, tool: 'my-scanner', tool_version: '1.2.0',
  external_id: '', status: 'running',
  started_at: localdatetime({timezone: 'UTC'}),
  scope: '[{"type": "FQDN", "key": "example.com"}]',
  metadata: '{"mode": "passive"}'
});

MATCH (r:CollectionRun {run_id: $id, status: 'running'})
SET r.status = 'finished',
    r.finished_at = localdatetime({timezone: 'UTC'});
```

## :material-magnify: Reading Runs

```sql
-- The latest finished runs whose scope names example.com
-- (PostgreSQL).
SELECT run_id, tool, started_at, finished_at
FROM public.collection_run
WHERE status = 'finished'
  AND scope @> '[{"type": "FQDN", "key": "example.com"}]'
ORDER BY started_at DESC
LIMIT 10;
```

The Amass `changes` lens uses runs this way: it compares
a domain or organization with the latest finished run
whose scope covered it, and reports what that run did
not see.

## :material-ip-network: Address Ranges

The asset database can also answer two range questions
directly, which the Amass network lenses use:

- which stored IP addresses fall inside a netblock, and
- which stored netblocks contain an address, the most
  specific first.

Go tools use the `IPRangeReader` interface
(`FindAddressesInRange` and `FindNetblocksContaining`).
PostgreSQL answers with GiST indexes on its `inet` and
`cidr` columns. SQLite and Neo4j keep fixed-width range
keys beside each address and netblock; asset-db fills
them in for existing data when the database is opened.

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
