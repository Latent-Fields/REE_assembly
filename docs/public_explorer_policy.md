---
nav_exclude: true
---

# Public Explorer — what it exposes and what it withholds

The **[Lab Window](public_explorer/)** is a static, read-only view onto REE's
claim-governed evidence trail, built for people who are not the maintainer. This
note is the design statement and the safety boundary: what was added, why it is
safe, what it exposes, and what it deliberately does not.

## What was added

- A static export pipeline (`scripts/export_public_explorer.py`) that reads the
  canonical registry and evidence index and emits a **curated** subset of JSON.
- A static front-end (`docs/public_explorer/`) — four modes: Orientation,
  Evidence explorer, Mechanism map, and Contribute.
- This data is generated from canonical sources, never hand-duplicated, so it
  cannot silently drift from the registry it summarises.

## Relationship to the internal tool

REE has an internal cockpit (`serve.py` + `explorer.html`) used by the
maintainer. That tool is API-driven, can start and stop experiment runners,
issue commands to machines, and shows live fleet telemetry. **It is not part of
this site and is never served by GitHub Pages.** The Lab Window is a separate,
read-only export — it has no backend, controls nothing, and mutates nothing.

## What it exposes

- **Settled, V3-relevant claims** — id, title, type, subject, status,
  cognitive-function grouping, dependency links, and a reviewed-evidence summary
  (supported / weakened / mixed / unresolved / superseded).
- **Reviewed experiments** — a short summary, outcome (pass / fail / error /
  superseded), the claims they bear on, caveats (e.g. excluded-from-scoring),
  and date.
- **An aggregate count** of experiments awaiting review — a number only.
- **Safe contribution paths** via GitHub issue templates.

## What it deliberately withholds

By design, and enforced in code (allowlist + sensitive-pattern scrub):

- **Operational detail** — runner controls, machine names, IP addresses,
  WireGuard topology, ports, file paths, SSH/systemd config, tokens or secrets.
  None of this is read by the exporter, and any value that matches a sensitive
  pattern is dropped and flagged for review.
- **Future-sensitive material** — claims tagged for V4/V5/V6, claims whose
  `epistemic_category` is `substrate_conditional` (depend on substrate not yet
  built), and any roadmap ordering or "what we will test next". Publicising
  these could steer or contaminate the work.
- **Pending-test framing** — `what_would_answer` falsification targets and the
  list of not-yet-reviewed runs. Pending work is shown only as a count, so
  outsiders can inspect *reviewed evidence* without being handed optimisation
  targets for open tests.
- **Internal prose** — claim `notes`, `evidence_quality_note`,
  `implementation_note`, source paths; experiment per-seed/per-arm metrics,
  configs, and timing. Output records are built from an explicit field
  allowlist, so unlisted fields can never leak.

## Why it is safe

1. **Scope filter** restricts to settled claims and withholds future-stage and
   substrate-conditional material.
2. **Allowlist** means each published field is named explicitly; everything else
   is dropped unconditionally.
3. **Sensitive-pattern scrub** is a second layer over the survivors, dropping
   anything that looks like an IP, host, path, or secret.
4. **Human gate** — every export writes a `redaction_report` (kept out of the
   published site) that the maintainer reviews before publishing.

The result lets an outsider understand what REE is, what V3 is trying to prove,
and what the reviewed evidence says — without operational access and without the
ability to steer pending governance. Suggestions are welcome through the
Contribute tab, but they do not change any claim's standing until reviewed.
