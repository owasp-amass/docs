# :material-clipboard-check: Review

The [`amass db`](db.md) scans find changes that would improve the Asset
Database: two records of one organization that should be merged, a legal
identity that contradicts its own evidence, or an organization stored under a
person's name. A scan never makes such a change itself. It records a
**proposal** in the review journal, and `amass review` is how a person
approves, rejects or undoes it. Every proposal keeps enough to be reversed,
and every decision records who made it.

```bash
amass db duplicates                                    # record proposals
amass review proposals                                 # see them
amass review approve -proposal dup-1a2b -reviewer jeff # apply one
amass review retract -proposal dup-1a2b -reviewer jeff # undo it
```

## :material-format-list-checks: Commands

| Command | What it does |
| :--- | :--- |
| `amass review proposals` | List every proposal in the journal and its status |
| `amass review approve -proposal <id> -reviewer <name>` | Apply a proposal |
| `amass review reject -proposal <id> -reviewer <name>` | Decline a proposal |
| `amass review retract -proposal <id> -reviewer <name>` | Undo an applied one |
| `amass review signals` | Why each ownership signal counts |
| `amass review duplicate-signals` | Why each duplicate signal counts |

Review shares `-format`, `-dir` and `-config` with the other subcommands,
and takes `-journal <file>` to choose the journal (by default the one
automatic attribution uses, set by `AMASS_AI_JOURNAL`).

## :material-source-branch: What produces proposals

- **`db duplicates`** proposes merging organizations stored more than
  once. Approving moves the duplicate's relationships and properties onto the
  record with more evidence, fills that record's empty fields, and deletes
  the duplicate.
- **`db identity`** proposes correcting a legal identity that contradicts
  the evidence. Approving removes what only an enrichment source recorded and
  clears the legal fields.
- **`db person-named`** proposes removing an organization that is really a
  person. Approving deletes the organization and keeps the person.

Each decision is reversible. Retracting a merge restores the duplicate and
removes what the merge added; retracting a correction restores the cleared
fields; retracting a removal recreates the organization with its
relationships.

## :material-scale-balance: Why a proposal, not an automatic edit

A matching organization name is never treated as strong evidence, because
companies in different jurisdictions often share a name and are different
companies. Companies also genuinely rename and relocate. So identity
corrections and person-name removals are never applied automatically, and
merges are applied on their own only during an enumeration explicitly run
with `AMASS_AI_ATTRIBUTION=auto`. People's decisions are the only training
labels the ownership model learns from.

## :material-robot-outline: Model-assisted review

[`amass ai review`](../ai/index.md) can add a language model's advice to a
proposal — a second opinion with its reasoning and the evidence it rests on.
The decision is still a person's, made with `amass review`.
