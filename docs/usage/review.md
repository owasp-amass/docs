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
| `amass review approve -proposal <id> -as <kind> -reviewer <name>` | Say whether a name is a `person` or an `organization` |
| `amass review reject -proposal <id> -reviewer <name>` | Decline a proposal |
| `amass review retract -proposal <id> -reviewer <name>` | Undo an applied one |
| `amass review signals` | Why each ownership signal counts |
| `amass review duplicate-signals` | Why each duplicate signal counts |
| `amass review import-journal -journal <file>` | Move a journal file into the Asset Database, once |

Review shares `-format`, `-dir` and `-config` with the other subcommands,
and takes `-journal <file>` to choose the journal (by default the one
automatic attribution uses, set by `AMASS_AI_JOURNAL`).

### Where the journal lives

When the Asset Database is PostgreSQL or SQLite, the review journal is kept
in the database itself. Every engine, MCP server and `amass` command that
uses the same database shares one set of proposals, decisions and undo
records. A proposal rejected on one machine stays rejected on the others,
and any of them can undo what another applied. With another database, or
none, the journal is the file named by `-journal`.

A journal file kept from before is not read once the database holds the
journal. `amass review` says so, and the file can be moved in once:

```bash
amass review import-journal -journal /path/to/review.jsonl
```

Importing the same file again does nothing. The file stays where it is, as a
backup. Trained models are still written beside the file.

## :material-source-branch: What produces proposals

- **`db duplicates`** proposes merging organizations stored more than
  once. Approving moves the duplicate's relationships and properties onto the
  record with more evidence, fills that record's empty fields, and deletes
  the duplicate. No name is lost: the merged record shows the more complete
  name (the full name rather than its acronym) and keeps every other name
  either record had as another name it's known by. People merge the same
  way, their other names kept on the person's own record.
- **`db identity`** proposes correcting a legal identity that contradicts
  the evidence. Approving removes what only an enrichment source recorded and
  clears the legal fields.
- **`db person-named`** proposes removing an organization that is really a
  person. Approving deletes the organization and keeps the person.
- **`db org-named`** proposes converting a person that is really an
  organization, such as a company name stored in a contact's person field.
  Approving turns the person into an organization (reusing the one its
  contact record already names, if any) and moves its relationships there.
  A relationship an organization can't have, such as a phone number, is set
  aside, and retracting brings the person back with all of it.
- **Enumeration** proposes widening its scope to a domain, netblock or
  autonomous system tied to the organization by supporting evidence only.
  Approving lets the next enumeration that finds it admit it into scope;
  rejecting keeps every later one away from it; retracting an approved or
  automatic expansion does the same from then on. When the main model was
  asked and didn't admit it, its answer is shown as advice: that it would
  reject the domain, or admit it below the confidence the policy asks for.
- **Enumeration** asks about a name it cannot place. A contact or a
  document sometimes gives an organization's name where a person's belongs,
  and when the words and what is already stored don't settle which it is,
  the name is kept on its record and proposed for review. Approve it with
  `-as person` or `-as organization` to record it as one; rejecting leaves
  the name on its record. The same name in the same field, such as one login
  as the author of several files, is listed once and decided together; add
  `-only` to decide just the one proposal. With a main model, its answer is
  shown as advice, or applied on its own when it's confident (see
  [Person or organization?](../ai/index.md#person-or-organization)).

- **An assistant** connected in operator mode can add what it found
  elsewhere, such as in a search or a document, with the `contribute` tool:
  assets, relationships between them and properties, each with where it came
  from. You approve the whole list before anything is written, so a
  contribution (`ctb-`) is listed as already applied, under the assistant's
  name (`amass-ai:<client>`). Retracting it removes what only it recorded;
  anything an enumeration also found stays. Unless
  `options.ai.contributions.strong_evidence` is set, a contribution is
  supporting evidence only: it can't by itself lead to an automatic
  ownership relationship, scope expansion or merge.

Each decision is reversible. Retracting a merge restores the duplicate and
removes what the merge added, giving the record its own name back;
retracting a correction restores the cleared fields; retracting a removal
recreates the organization with its relationships; retracting a name's
decision keeps the name on its record again.

A merge never strands other proposals. A pending proposal that named the
merged-away record now names the record that holds it. One whose two sides
became the same record, or that asks for what an older proposal already
asks, is marked superseded by the merge, and retracting the merge makes it
pending again.

Merges applied before merges kept every name can get theirs back once, with
`amass review keep-merged-names`.

## :material-scale-balance: Why a proposal, not an automatic edit

A matching organization name is never treated as strong evidence, because
companies in different jurisdictions often share a name and are different
companies. Companies also genuinely rename and relocate. So identity corrections
and person-name removals are never applied automatically, and merges are applied
on their own only during an enumeration explicitly run with
`AMASS_AI_ATTRIBUTION=auto`, and only when the evidence includes a registry
identifier (an LEI, a jurisdiction and registration number, or a network handle)
or a shared domain contact record together with the same name. A contact record
with only an address beside it often joins a parent and its subsidiary, so that
merge waits for a person. People's decisions are the only training labels the
ownership model learns from.

## :material-robot-outline: Model-assisted review

[`amass ai review`](../ai/index.md) can add a language model's advice to a
proposal — a second opinion with its reasoning and the evidence it rests on.
The decision is still a person's, made with `amass review`.
