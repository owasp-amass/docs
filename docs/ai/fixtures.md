# Reproducible AI fixture databases

Synthetic OAM fixture inputs live in the
[Asset Database repository](https://github.com/owasp-amass/asset-db),
under `testdata/ai` on the `feature/ai-investigation-inference` branch.

The fixture contains 15 assets, 12 directed relationships, and six
properties. It covers subsidiaries, websites, DNS names, provenance,
and unrelated organizations. Other scenarios describe ambiguity and
negative attribution cases.

The `asset-db/cmd/ai-fixture-seed` utility writes only to explicitly
selected disposable SQLite or PostgreSQL databases. **Never seed a
customer database or the existing Compose `assetdb` service.**

The input data is synthetic. Generated binary databases remain in
temporary locations and are not committed.

Initiative CI validates SQLite and PostgreSQL fixture creation and
bounded edge queries against both backends.

For larger benchmarks, use a disposable database and separately
reviewed, representative holdout data. Synthetic fixtures establish
regression behavior but cannot establish real-world attribution accuracy.
