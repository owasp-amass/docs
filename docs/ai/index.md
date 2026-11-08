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
