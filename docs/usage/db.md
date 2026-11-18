# :material-broom: Database hygiene

`amass db` scans the whole [Asset Database](../asset_db/index.md) for records
that should be corrected and records each as a **proposal** — it never changes
the database itself. A person applies or rejects the proposals with
[`amass review`](review.md). Unlike a [lens](lenses.md), these commands are not
read-only views of one subject; they walk the entire database.

```bash
amass db duplicates     # organizations stored more than once
amass db identity       # legal identities that contradict the evidence
amass db person-named   # organizations that are really a person
```

| Command | What it records |
| :--- | :--- |
| `amass db duplicates` | Duplicated organizations (merge proposals) |
| `amass db identity` | Contradicted legal identities (correction proposals) |
| `amass db person-named` | An organization that is really a person (removal) |

Each scan writes to the review journal; nothing is applied until a reviewer
approves it. See [Review](review.md) for how to list, approve, reject and undo
proposals, and why a matching name alone is never enough to merge two
organizations.

These scans are also reachable through [`amass ai`](../ai/index.md) in plain
language — the model picks the right one and summarizes what it found.

---

*© 2026 Jeff Foley — Licensed under Apache 2.0.*
