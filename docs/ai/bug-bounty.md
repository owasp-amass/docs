# :simple-owasp: Bug-bounty programs (development preview)

Many organizations run a public bug-bounty or vulnerability disclosure program
on HackerOne, Bugcrowd, Intigriti or YesWeHack. Each program publishes its
**scope**: the domains, hosts and address ranges the organization invites
researchers to test. A scope is the organization's own public list of the
assets it is responsible for, which makes it some of the best evidence of
ownership there is.

## What Amass collects

When an enumeration finds a registered domain in scope, Amass looks it up in
the public program lists and records every program whose scope names a host
under that domain. Each program is stored as an
[`Account`](../open_asset_model/assets/account.md) of type
`bug_bounty_program`, linked to its page on the platform and to every asset its
scope lists. Hosts in your enumeration's scope that the program lists are
collected like any other discovery; the rest are recorded but not collected.

The program lists come from a public mirror that is updated many times a day.
Amass downloads them at most once a day and needs no API key.

Recording a program says nothing yet about who owns what it lists. Programs
sometimes include a vendor-hosted service or a partner's system, so a program
that merely mentions one of your target's names stays an observation.

## When a program counts as the organization's

A program's scope becomes ownership evidence only when the organization's own
records tie the program to it. Any one of these is enough:

- the organization's `security.txt` links the program's page (the security.txt
  collector reads it);
- the organization's domain has the platform's domain verification record (for
  Bugcrowd, a `bugcrowd-verification` TXT record);
- the program's website is one of the organization's domains;
- the program's name is exactly the organization's name.

## What it proposes

Once a program is tied to the organization:

- the other hosts and address ranges in its scope become **ownership
  proposals**, listed by `amass review proposals` with the program and what
  tied it shown as the evidence;
- the other registered domains it lists become candidates for widening the
  enumeration's scope.

Both are **always reviewed by a person**. They are never applied
automatically, even alongside other evidence, and they never expand an
enumeration's scope on their own. Names under cloud providers' hosting domains
(such as `azurewebsites.net`) and the platforms' own sites are ignored.

## Things to keep in mind

- A parent company's program can cover subsidiaries and acquisitions that are
  separate organizations. Approve those as the organization they belong to.
- Scopes can be out of date: a business that was sold may stay listed until
  the program is updated.
- Only public programs appear in the lists. Private programs are invisible to
  Amass.

## Related pages

- [Review](../usage/review.md): approving and rejecting proposals.
- [disclosure lens](../usage/lenses/disclosure.md): an organization's
  `security.txt` contacts and policy links.
