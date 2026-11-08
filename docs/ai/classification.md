# Cost-aware classification and review

!!! warning "Experimental"
    The included CPU classifier has no production-calibrated weights. Accuracy, cost savings, and false-negative rates have not been measured on a representative corpus.

The default inference path uses deterministic candidate selection. When evidence has adequate verified provenance, an optional local classifier may route a candidate to:

| Decision | Meaning |
|---|---|
| `review` | Store a review-only triage event without a generative call or trusted OAM edge |
| `escalate` | Send the evidence-bounded candidate to the configured generative provider |
| `skip` | A **policy-gated** locally rejected candidate; not an ownership conclusion |

An **uncalibrated skip never suppresses generative analysis**. The Go routing API permits calibrated skipping only with an explicit policy; it is not enabled by the CLI.

## Provenance-aware features

The initial `oam-provenance-v1` feature extractor is deliberately simple, with bounded counts of distinct source identities, tagged evidence records, the proportion of source properties, and the proportion of unattributed evidence. It does not determine legal ownership from name similarity or shared infrastructure. For each candidate it checks that at least two attributed source IDs are available before classification.

These features are intended to test model routing and costs, not to replace evidence-based relationship assessment.

## Evaluation

The `classify.Evaluate` API reports label correctness, abstentions/escalations, review decisions, and unsafe skips (a known positive relationship incorrectly skipped). Tests include hard negatives such as shared CDNs and similar organization names.

Do not enable automatic negative skipping until a sufficiently large, independently adjudicated, held-out evaluation set demonstrates acceptable recall and false-negative behavior across different asset and relation classes.

## Audit and review

Classification-only events use the `triage` journal type. Generative proposals use the `proposal` type and must pass evidence ID and taxonomy validation. Neither writes a trusted OAM edge automatically.

The local JSONL journal is suitable for development. An unattended inference worker requires a durable queue, idempotent persistence, concurrency controls, and authorization before production use.
