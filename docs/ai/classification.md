# Cost-aware classification and review

!!! warning "Experimental"
    The CPU classifier has no production-calibrated weights.
    Accuracy, cost savings, and false-negative rates have not been
    measured on a representative corpus.

Deterministic candidate selection is the default. With adequate
verified provenance, an optional local classifier routes candidates:

- **`review`:** Record a review-only triage event without an LLM call
  or trusted OAM edge.
- **`escalate`:** Send bounded evidence to the generative provider.
- **`skip`:** Reject a candidate locally only under an explicit,
  calibrated policy. This is not an ownership conclusion.

**An uncalibrated skip never suppresses generative analysis.**
The Go API permits calibrated skipping only with an explicit policy;
the CLI does not enable that behavior.

## Provenance-aware features

The initial `oam-provenance-v1` extractor uses bounded counts of
distinct source identities, evidence records, the fraction of source
properties, and the fraction of unattributed evidence. It requires
at least two attributed source IDs before classification.

These features test routing and costs. They do not establish legal
ownership from name similarity or shared infrastructure, and cannot
replace evidence-based relationship assessment.

## Evaluation

The `classify.Evaluate` API reports label correctness, escalations,
review decisions, and unsafe skips (known positives wrongly skipped).
Tests include shared-CDN and similar-name negative examples.

Do not enable automatic negative skipping until an independently
adjudicated, held-out evaluation set demonstrates acceptable recall
and false-negative behavior for each relationship category.

## Audit and review

Classification-only decisions use `triage` journal events.
Generative proposals use `proposal` events and must pass evidence ID
and OAM taxonomy validation. Neither writes trusted OAM edges.

The local JSONL journal is suitable for development. An unattended
worker requires durable queueing, idempotency, concurrency controls,
and authorization before production use.
