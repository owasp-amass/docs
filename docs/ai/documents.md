# :simple-owasp: Documents and the document model (development preview)

Amass collects the PDF and Office documents an organization publishes and
records what their metadata and content reveal: authors, the software that
made them, user directory names, email addresses, host names, phone numbers
and the GPS position of embedded photos. See the
[`File`](../open_asset_model/assets/file.md) asset for everything stored.

With a **document model** configured, Amass can also read the text of those
documents and learn from what they say: the organization's units and parent
companies, its suppliers and partners, the systems it runs, its addresses, and
hosts or networks the rest of the enumeration hasn't found yet.

## What is kept, and what is not

The Asset Database keeps a document's metadata, the assets it links to and a
hash of its content, but **no copy of its content**. When the document model
reads a document, Amass fetches it again (from the web archive copy, when the
engine read one, so the target isn't contacted again), reads its text in
memory and remembers which version it read. Each version of a document is read
once; a document that changes is read again.

## What the document model finds

The model reads the whole document and reports, in
[Open Asset Model](../open_asset_model/index.md) terms:

- **things the text names:** organizations, people, host and domain names, IP
  addresses and networks, URLs, email addresses, phone numbers, street
  addresses, products and more;
- **relationships between them:** a unit and its parent, a subsidiary, a
  funder, a supplier, a partner, a person's role, a product in use, an
  address, a former name;
- **details about them:** an organization's founding date or industry, a
  product's type;
- **what kind of document it is:** an annual report, policy, staff directory,
  contract and so on.

Amass checks every finding against the text before keeping it. The quote must
appear word for word in the document. Names and values must be written near
it, and must be real values of their kind: a real host name, a valid address
range, a proper name rather than a phrase like "third parties". A building,
a law or a course isn't kept as an organization, and a job title isn't kept
as a person ("Boyd Hall", "the Clery Act", "CS 101", "Dean of Students").
Statements the
text denies ("no longer", "not") are dropped. A finding records what the
document says, not that it is true.

## During an enumeration

When the MCP server starts an enumeration and the document model is enabled,
the model reads the run's documents as they're collected.

### Leads

Anything a document names that Amass hasn't seen yet, and that the engine can
look up, is handed to the running enumeration as a **lead**. That covers host
and domain names, IP addresses, networks, organizations, addresses, phone
numbers, email addresses and URLs. The engine checks a lead like anything else
it finds, in DNS, the registries and by attribution, and a lead joins your
scope only if that evidence ties it to your target. People and products are
kept as findings but aren't leads.

An organization is a lead only when a document ties it to something the engine
can look up: a domain, address, phone number or network beside its name. An
organization named on its own is kept as a finding, because a name alone gives
the engine little to search and rarely leads anywhere; it becomes a lead if a
later document ties it to one of those. Generic units of the publisher ("Office
of Events"), names made only of generic office or service words ("Counseling",
"Health Center", "Rapid Response") and the target's own abbreviation are never
leads: the registries match such names to unrelated organizations. How many
leads a run receives adapts to how many the engine confirms, and to the size of
the run. Use `max_leads` to cap it (`-1` turns leads off).

### Units of the organization

The model is told which site published the document, and reports the offices,
departments, campuses and programs it names as units of the organization
behind that site. Agencies, contractors, vendors and partners stay separate
organizations. These units:

- are listed under "Units its own documents name" by the
  [`org-group`](../usage/lenses/org-group.md) lens;
- become review proposals: approving one adds the unit as an organization
  under its parent, and undoing the approval removes it again. A unit's record
  belongs to its parent, so offices of one name at two organizations
  ("Counseling") stay separate and are never proposed as one;
- are never leads for the enumeration.

A unit is implied by where a document is published, so a budget or directory
line can name a fund or a committee rather than an office. That's why every
unit waits for a person's approval.

### Old documents

Organizations publish documents for years and rarely remove them. A
document whose own dates are more than five years old is still read, and what
it says is kept, but it gives no leads, no proposals and no evidence for the
AI's decisions: offices, staff, parent organizations and suppliers change. The
one exception is history, such as a former name or a merger, which an old
document records as well as a new one. Current documents are read first.

When the engine has finished, the run stays open for up to 15 minutes while
the model reads the documents found last.

### How leads are settled

When the run ends, every lead it was given is settled:

- **Confirmed:** the engine tied it to your target: the lead is one of the
  target's own hosts, addresses or networks that the engine resolved or linked,
  or what the engine found connects it to the target within a few steps (a phone
  on the target's contact record, an office under the target organization). An
  organization the engine only collected records of its own for, such as its
  funding or registrations, isn't confirmed. The lead stays, and what it led to
  (often much more than the lead itself: an in-scope host brings its addresses,
  networks, certificates and services) cites the document.
- **Expired:** nothing tied it to the target. The lead and its asset are
  removed; if other collectors stored records about it, those stay. The
  finding stays with the document, so a later run can raise it again.

Leads are listed with the other changes the AI made on its own:

```bash
amass review applied
```

To see everything one confirmed lead led to:

```bash
amass review lead -proposal doclead:<run>:<entity>
```

To take one back:

```bash
amass review retract -proposal doclead:<run>:<entity> -reviewer <your name>
```

Retracting removes the lead's marks, and the asset itself if the engine linked
nothing to it. What the engine collected from a confirmed lead stays, because
DNS, the registries and other sources back it, not the document. Over MCP, use
`list_proposals` with `applied` or `lead`, and `review_proposal`.

### Watching a run

`enumeration_status` shows how many documents and parts of documents have been
read, the findings, the leads (and those waiting), and any documents that
couldn't be read, by reason:

| Reason | Meaning |
|:--|:--|
| `fetch` | The download failed (an HTTP error, a network error or a timeout) |
| `too_large` | The document is too long to read |
| `unsupported` | Amass doesn't read documents of this type |
| `extract` | Its text couldn't be extracted |
| `model_timeout` | The document model took too long to answer |
| `model` | The document model returned an error |

A download or model failure is tried once more; the others aren't retried in
the same run.

## Reading documents on demand

```bash
amass ai read-documents -d example.com
```

reads the stored documents of a domain (or `-org "Example University"`) that
haven't been read yet, at most 25 at a time (`-max-documents`). `-dry-run` reads
and checks without storing anything, and `-reread` reads documents again,
replacing their earlier findings. Each reading can be undone:

```bash
amass ai read-documents -undo doc:<file id>:<time>
```

The documents lens (`amass lens documents -d example.com`) shows how many
findings each document has.

An assistant connected to the Amass MCP server as an operator can do the same
with the `read_documents` tool, after you approve each call.

## Findings as evidence

What documents say also counts as **evidence** in the conclusions Amass draws.
It's always treated as supporting evidence, never as strong evidence: a model
read the text, and documents can be out of date. It counts for a bit more when
the document is the organization's own, and when several documents agree.

**Relationships for you to review.** When a document states a relationship
between two things already in the database, Amass proposes it for review:

| The document says | Proposed |
|:--|:--|
| A is a unit (division, department, campus) of B | B has unit A |
| A is a subsidiary of, was acquired by, or is owned by B | B has subsidiary A |
| A is funded by B | A's funding source is B |
| A person holds a role at B | the person is a member of B |
| A is located at, or headquartered at, an address already stored | A's address or headquarters |

Names must match exactly one stored organization, person or address, so a
finding never attaches to the wrong one. Proposals are recorded when an
enumeration the MCP server started ends, and on demand:

```bash
amass db doc-relations -d example.com
```

They appear with the other proposals (`amass review proposals`), each citing
the documents that state it, and you accept or reject them like any other
proposal. See [Review](../usage/review.md).

**In Amass's other conclusions.**

- **Duplicate organizations:** a document saying one organization was formerly
  known as, or merged with, another supports merging their records, even when
  the two share nothing else (a complete rename). A document calling one the
  parent, subsidiary or unit of the other counts *against* merging them.
- **Ownership:** a document saying the organization operates a stored host or
  URL supports attributing it to the organization.
- **Vendors:** the [`vendors`](../usage/lenses/vendors.md) lens lists the
  suppliers and products a domain's own documents name, with the documents
  cited.
- **Affiliation:** the [`affiliation`](../usage/lenses/affiliation.md) lens
  counts a membership or partnership a domain's own documents state.

!!! note "Document evidence never changes the database on its own"
    It can bring something to your attention and strengthen a case, but
    a merge, an ownership relationship or a proposed relationship is never
    applied automatically because of a document. Anything Amass applies
    without review must qualify on other evidence alone.

## Choosing the model

Documents can hold personal or internal details, so you choose the one model
allowed to read them, separately from the model used for questions. Nothing
falls back to the question model: without an `options.ai.documents` section, no
model reads documents.

```yaml
options:
  ai:
    documents:
      enabled: true
      # The containerized Ollama started by amass-docker-compose:
      provider: ollama
      endpoint: http://ollama:11434
      model: qwen3:30b          # or qwen3:4b on a machine with less memory
      allow_http: true          # trusted private Compose network only
      model_timeout: 4m
      share_with_assistants: false
```

An Ollama running directly on the host uses
`endpoint: http://host.docker.internal:11434` from a container, or
`http://127.0.0.1:11434` outside one. On a Mac, Ollama installed on the host
uses the GPU, which Ollama inside Docker Desktop can't, so it reads documents
several times faster.

A hosted model takes the work off your machine. Use one only if you're
comfortable sending your targets' documents to it:

```yaml
options:
  ai:
    documents:
      enabled: true
      provider: anthropic       # or compatible, for an OpenAI-compatible API
      model: claude-haiku-5-5   # the fastest and least costly
      api_key_env: ANTHROPIC_API_KEY   # the key is read from this variable
      max_chunks: 20            # bounds what one reading of a document costs
```

The key needs to be exported in the shell that starts Amass, and passed into
the container: `docker compose run --rm -e ANTHROPIC_API_KEY ...`. It's a
Messages API key from the Anthropic Console, which is billed separately from a
Claude subscription.

Any OpenAI-compatible API works too, hosted (such as OpenAI) or local (vLLM,
LM Studio, llama.cpp or Ollama's `/v1` API), with `provider: compatible` and
`endpoint` set to the full `/v1/chat/completions` URL. Nothing else needs to
change for a particular model:

- A model that refuses a setting, as newer models do with `temperature` or
  `max_tokens`, is asked again without it, and Amass remembers that for the
  rest of the run.
- Replies are held to the findings' JSON format when the provider supports
  it, and a provider that doesn't is asked with the instructions alone.
- A provider that limits how fast you can send requests is waited out for the
  time it asks for, a few times, before that part of the document fails.
- An error shows the reason the provider gave, never the key.

With Ollama, `amass ai read-documents` and the MCP server's log check at
startup that the model has room for one request (the instructions, a chunk and
the reply), and that `context_tokens` isn't larger than the window the model
was trained with. If either doesn't fit, they name the setting to change.

### Which model to use

How much a model finds, how much of it is right, and how long it takes all
differ widely. One comparison, of six documents from one university (a 2012
course catalog, a faculty contract, a policy and a call for papers). The local
models ran on an Apple silicon Mac with Ollama on the GPU, and Haiku through
the Anthropic API:

| Model | Catalog parts read in 10 minutes | What it found |
|:------|:--------------------------------:|:--------------|
| `qwen3:4b` | 14 | The most findings, with the most noise: real people with their roles and the accrediting body, but also made-up details and contradictory relations |
| `qwen3:30b` | 10 | Fewer, steadier findings, such as the university's institutes and partner schools, but buildings recorded as organizations and job titles as people |
| `qwen3:8b` | 7 | The fewest useful findings on the catalog: course codes and learning goals recorded as organizations |
| `claude-haiku-5-5` | All 44 | The most accurate: the university's institutes with the years they were founded and their place in the university, outside partners, and people with their roles. Still a few errors, such as a law recorded as an organization and one organization under two names |

`qwen3:30b` is a mixture-of-experts model: about 19 GB to hold, but only a
small part of it works on each word, so it reads faster than its size
suggests. `qwen3:4b` suits a machine with less memory. In this sample the
hosted model was both the fastest and the most accurate; what it costs is
money per token and sending the documents' text off your machine. A small
sample like this one is a starting point, not a ranking: compare models on
documents from your own targets (below).

Every model also reports findings that don't fit, so findings are checked
against the text before they're stored, and you review what an enumeration
applied. Documents whose text can't be extracted give nothing to any model.

Scanned documents hold pictures of their pages instead of text. When the
document model can read pictures, it's shown each page and writes out the
text. Otherwise Tesseract reads the pages; it's included in the Compose
images. `options.ai.documents.vision` says whether the model can read
pictures. Left at `auto`, Anthropic models can, Ollama models can when Ollama
reports it (vision models such as `qwen3-vl`), and other models can't. Set it
to `off` to use Tesseract even with a model that can.

### Keeping the work in bounds

Long documents, such as course catalogs and handbooks, can run to dozens of
parts. Three settings keep one enumeration from spending hours on them, and
none of them skips anything: what isn't read now is read later.

- `document_timeout` (default `10m`) ends one reading of one document after
  that long. The next reading continues where it stopped: later in the same
  enumeration if `hold` allows, otherwise in the next one.
- `max_chunks` caps the parts one reading takes. With a hosted model, it
  bounds the cost of each reading.
- `hold` (default `15m`) is how long a finished enumeration waits for
  documents still being read.

### Comparing models on your own documents

`read-documents` with `-reread` and `-dry-run` reads documents again with the
model a configuration names, and stores nothing, so you can try a model before
using it. Make a copy of your configuration for each model to compare, change
its `options.ai.documents` section, set `document_timeout: 0` so each model
reads whole documents, and run each one over the same documents:

```bash
docker compose run --rm --entrypoint /bin/amass ai ai read-documents \
  -config /.config/amass/doc-qwen3-30b.yaml -domain example.com \
  -max-documents 6 -reread -dry-run > doc-qwen3-30b.txt 2>&1
```

Each document's line gives the parts read and the findings kept and rejected,
and a dry run lists every finding with its quote, so you can judge what's
right.

| Setting | Default | Meaning |
|:--------|:-------:|:--------|
| `enabled` | `false` | Turns the document model on |
| `provider` | | `ollama`, `compatible` or `anthropic` |
| `endpoint` | provider default | The model's address |
| `model` | | The model's name; required when enabled |
| `api_key_env` | | Environment variable holding a hosted provider's key |
| `allow_http` | `false` | Allows plain HTTP, for a trusted private network only |
| `model_timeout` | | Time allowed for one request, 5s to 15m |
| `context_tokens` | `16384` | An Ollama model's context window |
| `chunk_chars` | `12000` | How much of a document one request reads |
| `max_tokens` | `4096` | Longest reply the model may give to one request |
| `vision` | `auto` | Whether the model can read pictures, for scanned documents: `auto`, `on` or `off`. A model that can't gets Tesseract's reading of the pages |
| `share_with_assistants` | `false` | Lets other models read the findings |
| `max_leads` | `0` (adaptive) | Caps the leads one enumeration receives; `-1` turns leads off |
| `hold` | `15m` | How long a finished enumeration stays open while documents are still being read, so their leads reach it; `0` ends it as soon as collection is done. It ends sooner when the documents left could not be read in time, and the next run reads them |
| `document_timeout` | `10m` | The longest one reading spends on one document. A long document read past it is continued where it stopped by the next reading, so nothing is skipped; `0` sets no limit |
| `max_chunks` | `0` (no cap) | The most parts of one document one reading takes; mainly bounds what a hosted model costs. The rest is read by the next reading |

### How often documents are collected again

Amass doesn't download a document again while its stored copy is recent. You
set how recent in the `transformations` section of the config, with the
`URL->File` entry's `ttl` in minutes:

```yaml
transformations:
  URL->File:
    ttl: 43200 # 30 days
```

`URL->File` applies to every collector that stores files from URLs. To set it
for the document collector alone, name it instead: `URL->Documents`. When both
are present, `URL->Documents` wins.

A shorter `ttl` refreshes documents more often; a longer one spends each
enumeration on documents it hasn't collected yet. Each enumeration collects at
most 250 documents per domain, and the next enumeration continues with the rest.

## Who else sees the findings

Findings quote the documents. By default, other models (the question model,
and assistants connected over MCP) see only how many findings a document has,
not their text. Set `share_with_assistants: true` to let them read the
findings.
