# Substrate Defect Gate — Plan of Record

Status: **proposed** (design only — no schema or skill edits landed yet)
Opened: 2026-08-07T20:09:22Z, session `substrate-fixes-governance-gap-58b073`
Owner: user-initiated design conversation; no chip spawned yet (see Next step)

## Status table (resume primitive)

| Step | State | Note |
|---|---|---|
| 1. Confirm the gap is real, not already covered | DONE | see "What already exists" below |
| 2. Design `substrate_paths` + `severity` fields | DRAFTED (this doc) | not yet in `substrate_queue.json`'s schema notes |
| 3. Design the `/queue-experiment` consumer gate | DRAFTED (this doc) | not yet in SKILL.md |
| 4. Design the `/failure-autopsy` producer-side fill | DRAFTED (this doc) | not yet in SKILL.md |
| 5. Backfill existing 145 entries with `substrate_paths` | NOT STARTED | scoping question below |
| 6. Land schema + skill edits | NOT STARTED | needs user sign-off on this doc first |
| 7. Write `check_substrate_path_overlap.py` standing scan | NOT STARTED | mirrors GOV-CEIL-1 / GOV-DIAG-1 shape |

## The observation that triggered this

User, in conversation: `/governance` and `/failure-autopsy` routinely surface substrate
defects that need fixing, and those defects have dependency and priority structure much
like `claims.yaml` itself — but nothing stops a *new, unrelated* experiment from being
queued and run against substrate that a prior autopsy already flagged as broken. That
reads as a governance gap: known-bad substrate should gate new work on it, not just
retests of the specific claim that happened to surface the defect.

## What already exists (do not rebuild)

This is not a greenfield problem. `substrate_queue.json` (145 entries) already carries:

- `sd_id`, `title`, `node_class` (work-graph debt token — buildability)
- `priority` (1 high / 2 med / 3 low), **derived** at governance Step 6a-ii.6:
  `1` if ≥1 fresh failure record OR blocks ≥3 claims; `2` if blocks 1-2 claims; `3` otherwise
- `unblocks_claims` — which claims become testable once this SD lands
- `depends_on_unresolved` — dependency graph, same shape as `claims.yaml depends_on`
- `ready` / `ready_blocked_by` — whether the entry itself is unblocked
- `failure_record[]` — run_ids that hit this gap, with the metric and threshold

And there are already forward gates that stop experiments from running against known-bad
substrate:

- `/queue-experiment` Step 2.5 — blocks queuing if the target claim's own SD isn't marked
  IMPLEMENTED in `ree-v3/CLAUDE.md`.
- `/queue-experiment` Step 2.5a — empirical probe, catches doc-says-done /
  runtime-says-otherwise drift for the target claim's own feature.
- `/queue-experiment` Step 2.5b (re-derive brake) — refuses a same-claim, same-granularity
  re-queue once that claim has hit a `substrate_ceiling` reading ≥2 times, until the named
  upstream substrate is BUILT.
- Governance GOV-CEIL-1 / GOV-DIAG-1 — detect claim-keyed and diagnostic-chain recurrence
  against a ceiling and recommend demotion / refuse re-queue.
- IGW workset generator `_priority_score` — already blends substrate_queue priority into
  the same sorted worklist as new experiment proposals, so substrate work isn't invisible
  next to fresh experiment proposals.

Priority-derivation and dependency-tracking, which is what the user asked to think through,
**already exist** for substrate_queue entries. The granularity question is not "do we need
a priority field" — it's "what is priority computed *over*, and what does it *gate*."

## The actual gap (confirmed, not assumed)

Every one of the mechanisms above is **keyed to the claim/SD the current experiment is
testing**. Governance SKILL.md says this explicitly of the two claim-level recurrence
detectors: *"The re-derive brake and GOV-CEIL-1 (6a-v-bis) are BOTH claim-keyed."* The same
is true of `/queue-experiment` Step 2.5/2.5b: they check whether *this experiment's own
target SD* is built and clean — never whether the experiment's driver script imports or
exercises a code path that some *other, unrelated* claim's autopsy already flagged as
broken.

Concretely: if MECH-457's autopsy finds a bug in `ree_core/predictors/e3_selector.py` and
writes a `substrate_queue` entry for it, nothing stops a brand-new experiment for a
completely different claim (say, a Q-series curiosity question) from being queued and run
against that same broken `e3_selector.py` path tomorrow. The defect is recorded, it has a
priority, it blocks the claims that were on the autopsy at the time — but it does not gate
*anything else that happens to touch the same file*. `unblocks_claims` is claim-scoped, not
code-scoped, so there is no way to ask "does entry X's defect intersect the code this new
experiment will run" at all.

There's a second, quieter half of the same gap: nothing captures whether a defect
*silently corrupts* results (evidence that looks clean but isn't — the class of incident
this repo's CLAUDE.md documents extensively elsewhere: the E3 diagnostics staleness lint,
the SD-081 hold-weighted-readout pseudo-replication, the multinomial cross-machine
divergence) versus *degrades* (known limitation, weakens confidence but doesn't invalidate)
versus is purely cosmetic. `node_class` answers "can we build the fix"; `priority` answers
"how urgently should we build it." Neither answers "how dangerous is it to keep running
experiments against this substrate while it's still open" — which is the actual question
behind "should this block new work."

## Proposed design

Two axes, kept separate on purpose (conflating them was the mistake to avoid, per the
earlier conversation):

### Axis 1 — `severity` (new field, orthogonal to `node_class` and `priority`)

One of three values, set by whoever files the entry (governance Step 6a-iii /
`/failure-autopsy` Step 7):

- `corrupting` — produces evidence that looks valid but isn't (silent). Forward: new
  experiments against the affected paths should be **blocked**, not just warned.
- `degrading` — known limitation; weakens confidence in results but doesn't invalidate
  them outright. Forward: **warn**, don't block.
- `cosmetic` — no evidence impact (a lint gap, a naming issue, dead code). No gate.

This is the field that decides *whether the entry should be able to stop other work at
all* — most substrate_queue entries today are ordinary missing-feature backlog and would
default to a fourth implicit bucket, `not-yet-run` (nothing has been tested against it, so
there's no evidence-corruption risk to gate on — this covers the large majority of the 145
existing entries and needs no severity stamp).

### Axis 2 — `substrate_paths` (new field, code-scoped, distinct from `unblocks_claims`)

A list of repo-relative path globs the defect actually lives in or corrupts —
e.g. `["ree_core/predictors/e3_selector.py"]` or `["ree_core/predictors/e3_selector.py::compute_harm_cost_fallback"]`
when the defect is scoped to one function. This is what makes the entry queryable by *code
footprint* instead of only by *claim*. `unblocks_claims` stays as-is (it answers "which
claims does fixing this help"); `substrate_paths` answers "what does an experiment need to
avoid touching while this is open."

Populated by whoever fills `recommended_substrate_queue_entry` (`/failure-autopsy` Step 7)
— they've already read the source to diagnose the failure, so naming the path(s) is nearly
free at that point, unlike trying to reconstruct it later from prose.

### Priority stays as-is, with one addition

The existing 1/2/3 derivation (fresh failure record OR blocks ≥3 claims) is fine for
*build-ordering* — sorting `/implement-substrate` work. It's a poor proxy for *blast
radius* on the gate, though: a defect in a narrow, single-experiment-type module and a
defect in a widely-shared module like `e3_selector.py` (used across dozens of experiment
types) can have the same claim-blocking count today but very different gate consequences.
Add `path_breadth` as a derived-not-stored signal — computed at gate time by counting how
many experiment driver scripts under `ree-v3/experiments/` import the flagged path — rather
than a new stored field, so it can't drift stale the way a hand-maintained count would.

### The gate itself (`/queue-experiment`, new Step 2.5c — after 2.5b, before Step 3)

For the experiment script being written, resolve the set of `ree_core`/`coordinator`
modules its driver imports. Cross-reference against every OPEN (`status` not
`implemented`/`wontfix`) `substrate_queue` entry's `substrate_paths`:

- **Any overlap with a `severity: corrupting` entry** → same stop-gate shape as Step 2.5:
  do not write the script, do not queue, report the defect + its `sd_id` to the user, route
  to `/implement-substrate` if not already in flight. This is the actual "block new
  experiments before fixing known-bad substrate" behavior the user asked about.
- **Any overlap with a `severity: degrading` entry** → do not block; append a note to the
  queue entry's `note` field naming the open defect, so the eventual result manifest and
  any later autopsy can see the run happened under a known limitation.
- **`cosmetic` or unset severity** → no action.

This is the consumer half; `/failure-autopsy` Step 7 (producer half) is where
`substrate_paths` + `severity` actually get written, symmetric with how Step 2.5b
(consumer) / the re-derive brake (producer) already split across the same two skills.

### Governance-side standing scan (mirrors GOV-CEIL-1 / GOV-DIAG-1's shape)

A `check_substrate_path_overlap.py`, run at governance Step 3g/3h alongside the existing
warn-only scans: for every `severity: corrupting` entry that's still open, list any
*already-completed* run (via `git log`/experiment index, not just the originating claim's
own results) whose driver script touches one of its `substrate_paths` and that completed
**after** the defect's `added_utc`. This is the backward half — surfacing evidence that may
need re-review because it ran against substrate later found to be silently wrong, even when
that evidence belongs to a claim the original autopsy never mentioned. Warn-only, same as
its siblings; a human decides whether to re-review, this only surfaces the candidates.

## Explicitly out of scope for this doc

- Backfilling `substrate_paths` onto all 145 existing entries in one pass — most are
  `complicated (buildable)` missing-feature backlog with no evidence-corruption risk, so
  blanket backfill is wasted effort. Fill it going forward, and retroactively only for
  entries whose `failure_record` suggests a `corrupting`-severity defect.
- A brand-new registry file. Everything above is additive fields on `substrate_queue.json`
  plus one new consumer check and one new standing scan — reusing the dependency/priority
  machinery that already exists rather than duplicating it, per the granularity discussion.
- Auto-blocking based on `priority` (1/2/3) alone. Priority orders *build* work; only
  `severity: corrupting` should ever gate *experiment-queuing* work. A priority-1,
  `degrading`-severity entry should not stop anyone from running experiments — it just
  needs the fix scheduled soon.

## Next step

This is a design doc, not yet actioned. Per CLAUDE.md's chip-everything-else rule, once the
user confirms the design, the schema + skill edits (Steps 5-7 in the status table above)
should be chipped as `/implement-substrate`-adjacent work — this doc is exactly the kind of
follow-on that gets spawned as its own session rather than done inline, since it touches two
skill files and a shared schema under active governance use.
