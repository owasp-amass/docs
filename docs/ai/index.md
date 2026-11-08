# AI-powered investigations (development preview)

!!! warning "Unreleased feature"
    This page describes the `feature/ai-investigation-inference` implementation branches. It is not yet available in a published Amass release, and the functionality must not be treated as production-ready.

OWASP Amass is adding optional, model-independent reasoning over the Open Asset Model (OAM). The two initial workflows are:

1. **Investigations:** read-only graph tools allow a model to inspect OAM assets, edges, and evidence, then explain observed findings.
2. **Inference proposals:** deterministic candidate selection and optional local classification precede generative analysis. Proposals remain in a separate review journal; they do not automatically change OAM relationships.

The implementation uses the existing Asset Database, keeping SQLite and PostgreSQL support. The Amass client and MCP server share a restricted graph tool layer.

## Read-only graph tools

- `get_asset`: retrieve an OAM entity by database ID
- `find_assets`: find a limited number of assets by type
- `walk_relations`: traverse a bounded graph neighborhood
- `get_evidence`: retrieve evidence tags and source properties
- `render_graph`: produce a Mermaid graph from a bounded result

The bounded graph reader is being developed in `owasp-amass/asset-db`. AI graph walks now **fail closed** if the deployed database implementation lacks server-side limits. The released `asset-db` dependency may need to be updated before these features can run.

## CLI example (feature branch only)

```console
amass ai -config /path/to/config.yaml \
  -provider compatible \
  -model YOUR_MODEL \
  -endpoint https://MODEL_HOST/v1/chat/completions \
  -question "What evidence connects these assets?" ask
```

Use `amass ai infer` with an evidence-backed candidate JSON file and a proposal journal path. See [classification and triage](classification.md).

## Model independence

The current prototype includes native OpenAI-compatible and Anthropic provider adapters. A locally hosted compatible endpoint can be used if configured securely. The `Classifier` abstraction is separate from the generative model interface, allowing CPU-only deterministic or statistical models to triage candidates without a hosted LLM call.

## Security boundaries

- Existing OAM facts and probabilistic inferences remain distinct.
- Candidate evidence IDs are verified against the Asset Database.
- The agent has no raw SQL, arbitrary shell, or network tool.
- Bounded graph queries have depth, row-count, output-size, and call budgets.
- Untrusted internet data must never be treated as instructions.
- Source IDs are deduplicated; counting different names does not guarantee genuine independence.
- The MCP stdio endpoint and Compose support are development features. No public network endpoint is required.

See the [classification](classification.md) and [synthetic fixtures](fixtures.md) pages.
