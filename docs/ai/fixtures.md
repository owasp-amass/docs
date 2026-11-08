# Reproducible AI fixture databases

Synthetic OAM fixture inputs live in the [Asset Database repository](https://github.com/owasp-amass/asset-db/tree/feature/ai-investigation-inference/testdata/ai) under `testdata/ai`.

The current fixture has 15 assets, 12 directed relations, and six properties. It exercises subsidiaries, websites, DNS names, source provenance, and unrelated organizations. Additional scenario JSON describes ambiguity and negative attribution cases.

The seeder under `asset-db/cmd/ai-fixture-seed` writes only to explicitly selected disposable SQLite or PostgreSQL test databases. Never point it at a customer database or the existing Compose `assetdb` service. The test data is synthetic; binary databases are generated in disposable locations and are not committed.

The initiative CI validates SQLite and PostgreSQL fixture creation and checks bounded edge queries against both backends.

For larger benchmarks, use a generated private or disposable test database and separately labeled, representative holdout data. Synthetic fixtures establish regression behavior but cannot establish the accuracy of real-world corporate attribution.
