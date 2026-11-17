# AI-powered investigations (development preview)

!!! warning "Unreleased feature"
    This page describes the `feature/ai-investigation-inference` branches.
    These capabilities are not yet published or production-ready.

OWASP Amass is adding optional, model-independent reasoning over the
[Open Asset Model](../open_asset_model/index.md). You can ask plain-language
questions about what has been collected and get **evidence-backed** answers, and
Amass can **propose** correlations — such as which organizations are really the
same company — for you to review. Collected facts and AI inferences are kept
separate, and nothing an AI suggests changes the database until you accept it.

```mermaid
flowchart LR
  Q["Your question"] --> AG["AI agent"]
  AG <-->|read-only tools| DB[("Asset Database")]
  AG --> ANS["Evidence-backed answer"]
  DB --> INF["Inference"] --> PROP["Review proposal"] --> YOU["You confirm or reject"]
```

## Two workflows

1. **Investigations** — read-only tools inspect assets, relationships and
   evidence, and a model explains the findings. Nothing is changed.
2. **Inference proposals** — Amass proposes correlations backed by evidence.
   They stay in a [review](../usage/review.md) journal and never change the
   database until you accept them.

## Asking a question

```console
amass ai -config /path/to/config.yaml \
  -provider compatible \
  -model YOUR_MODEL \
  -endpoint https://MODEL_HOST/v1/chat/completions \
  -question "What evidence connects these assets?" ask
```

Amass can also run inference over an evidence-backed candidate file with
`amass ai infer`; see [classification and triage](classification.md).

## Using it through an assistant (MCP)

Amass exposes a restricted, read-only set of graph tools through an MCP server,
so an AI assistant can explore the Asset Database on your behalf:

- `get_asset` — retrieve an entity by its database ID.
- `find_assets` — find a bounded number of assets by type.
- `walk_relations` — traverse a bounded neighborhood of the graph.
- `get_evidence` — read the evidence and source behind a fact.
- `render_graph` — draw a bounded result as a diagram.

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

Amass is not tied to one model. It ships OpenAI-compatible and Anthropic
adapters, and approved local endpoints can be used instead — so inexpensive,
CPU-based triage can run without a hosted model call.

## What stays trustworthy

- Collected facts stay separate from AI inferences.
- Evidence is verified against the database before it is used.
- The agent has no raw SQL, shell, or arbitrary network access.
- Graph queries are bounded (depth, row count, output size, number of calls).
- Content from the internet is treated as data, never as instructions.
- A matching name alone never establishes that two organizations are the same.

See [classification and triage](classification.md).
