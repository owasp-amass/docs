# AI-powered investigations (development preview)

!!! warning "Unreleased feature"
    This page describes the `feature/ai-investigation-inference` branches.
    These capabilities are not yet published or production-ready.

OWASP Amass is adding optional, model-independent reasoning over the
Open Asset Model (OAM). The initial workflows are:

1. **Investigations:** Read-only tools inspect OAM assets, relationships,
   and evidence before a model explains findings.
2. **Inference proposals:** Deterministic candidate selection and optional
   local classification precede generative analysis. Proposals remain in
   a review journal and never automatically change trusted OAM edges.

The implementation uses the Asset Database (SQLite or PostgreSQL).
The Amass CLI and MCP server share a restricted graph-tool layer.

## Read-only graph tools

- `get_asset`: Retrieve an entity by database ID.
- `find_assets`: Find a bounded number of assets by type.
- `walk_relations`: Traverse a bounded graph neighborhood.
- `get_evidence`: Retrieve evidence tags and source properties.
- `render_graph`: Render a bounded result as a Mermaid graph.

Query-side limits are being developed in `owasp-amass/asset-db`.
AI graph walks fail closed if the deployed backend lacks those limits.
The published database dependency may require an update.

## CLI example (feature branch only)

```console
amass ai -config /path/to/config.yaml \
  -provider compatible \
  -model YOUR_MODEL \
  -endpoint https://MODEL_HOST/v1/chat/completions \
  -question "What evidence connects these assets?" ask
```

Use `amass ai infer` with an evidence-backed candidate JSON file and a
proposal journal. See [classification and triage](classification.md).

## Configuration assistant

The assistant can also help with the Amass configuration itself. Because
the MCP server runs no model of its own — the connected assistant is the
model — the server exposes the schema and the checks, and the assistant
does the drafting:

- `describe_config`: the configuration schema (every section and field
  with its type, default, description and an example), the current
  settings with data source credentials masked, and a commented template
  to start a new file from.
- `validate_config`: check a complete draft with the real Amass loader
  and show a credential-masked diff, without changing anything.
- `apply_config`: write a validated draft to the configuration file,
  after the user approves it and sees the exact masked diff. This is an
  operator-mode tool; read-only connections can describe and validate but
  not apply.

A terminal user gets the same help from the locally configured model:

```console
amass ai -config /path/to/config.yaml \
  -provider compatible -model YOUR_MODEL \
  -endpoint https://MODEL_HOST/v1/chat/completions \
  -question "Set up a passive enumeration of example.com" config
```

It prints the proposed configuration and a masked diff, and writes it
only on approval — at an interactive prompt, or ahead of time with
`-approve-config`.

Data source credentials never pass through the model: they are masked in
what `describe_config` returns and in every diff, and a draft that sets
any is refused. Keys are entered by the operator through a one-time local
link (`data_source_key_link`), never written by the assistant.

## Learning from review

Ownership-gap proposals go to a review journal, where a person approves or
rejects them. Those decisions train a small, local ownership model that
replaces the hand-set signal weights with weights learned from the
reviewer's choices:

```bash
# Train (or retrain) from the journal's reviewed decisions.
amass ai -config /path/to/config.yaml train-attribution

# Report whether a model is trained, what it decides with, and how much
# reviewed data is on hand to retrain.
amass ai -config /path/to/config.yaml attribution-status
```

A trained model is written beside the journal and is used everywhere
ownership is decided: the engine's automatic attribution from the next
enumeration, the `amass ai` ownership-gap answers, and the MCP ownership-gap
tool. The model only ever ranks and decides candidates the rules already
found attributable; weak and ambiguous candidates stay with the rules, and
until a model is trained the static signal weights decide. The threshold for
an automatic write is set above the highest score any rejected proposal
received, so the model writes nothing a reviewer turned down.

## Model independence

The prototype includes OpenAI-compatible and Anthropic model adapters.
Approved local endpoints can also be used. The `Classifier` interface
is separate from generative models, allowing inexpensive CPU-based
triage without a hosted LLM call.

## Security boundaries

- Trusted OAM facts remain separate from probabilistic inferences.
- Candidate evidence identifiers are verified against the database.
- The agent has no raw SQL, shell, or arbitrary network tool.
- Graph queries enforce depth, row-count, output-size, and call budgets.
- Internet-derived content is untrusted data, never instructions.
- Source IDs are deduplicated, but matching names alone do not establish
  independence.
- MCP stdio and Compose support remain development features.

See [classification](classification.md) and [synthetic fixtures](fixtures.md).
