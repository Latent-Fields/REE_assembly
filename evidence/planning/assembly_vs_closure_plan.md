---
closure_plan:
  id: assembly_vs_closure
  title: "Assembly-vs-closure: stop the machinery forcing closure before substrate is ready"
  generation: meta
  last_updated: 2026-06-21
  owner: machinery
  summary: >
    Give substrate ASSEMBLY a first-class lifecycle parallel to claim
    ADJUDICATION, so the machinery stops biasing every node toward closure.
    generation: meta -> excluded from the V3 closure % (this is machinery work,
    not V3 substrate). Not scanned by check_closure_drift (no owner_exq).
  nodes:
    - id: MOVE-1
      title: "Keystone: first-class `assembling` / `open_by_design` node state"
      status: done
      severity: load-bearing
      last_updated: 2026-06-21
      note: >
        Landed 2026-06-21. serve.py CLOSURE_STATUS_WEIGHTS +
        generate_closure_snapshot.py + check_closure_drift.py. Credited on its
        own assembly-frontier axis (weight None -> never punishes the %), held
        out of `remaining`, restful in drift (no recurring re-stamp), opt-in
        `revisit_after` resume trigger. Non-disruptive (79.0% unchanged);
        self-test + functional smoke green.
    - id: MOVE-2
      title: "Assembly-chip path mirroring the closure-chip path (session-land)"
      status: done
      severity: high
      awaiting: null
      last_updated: 2026-06-21
      note: >
        Landed 2026-06-21. session-land Phase 3 rule 3 split into rule 3 (still
        skip work blocked on a pending run -- correctly in-flight) + new rule 3a
        (chip an UNBUILT critical-path substrate as a BUILD task routed to
        /implement-substrate when all four hold: on critical path, not built, in
        no build queue, nobody constructing it -- verified against the queue /
        substrate_queue / TASK_CLAIMS / plan-of-record status tables). Chip must
        name the substrate id + critical-path + no-active-builder. Report-line
        example reconciled to match. Edited BOTH skill copies (.claude/ +
        .agents/) byte-identically. PROMOTES NOTHING.
    - id: MOVE-3
      title: "Hard brake on the re-derive loop (failure-autopsy granularity hook gates the queue)"
      status: done
      severity: load-bearing
      last_updated: 2026-06-21
      note: >
        Landed 2026-06-21. The granularity-debt recurrence hook now GATES, not
        just detects. PRODUCER half (/failure-autopsy): on the Nth
        (RE_DERIVE_BRAKE_THRESHOLD, default 2) substrate_ceiling/non_contributory
        autopsy for the same claim, recommended routing is forced to
        /implement-substrate on the named upstream substrate and a same-claim
        test re-queue is explicitly REFUSED; the firing is recorded on the
        autopsy target via a new re_derive_brake{} field (fired/threshold/
        prior_substrate_ceiling_autopsies/refused_requeue/route_to/
        upstream_substrate). CONSUMER half (/queue-experiment Step 2.5b): refuses
        to queue a new same-granularity test of a claim with >=2
        substrate_ceiling autopsies on record (scans
        failure_autopsy_*.json targets[].claim_ids) UNLESS the named upstream
        substrate now shows IMPLEMENTED/VALIDATED in ree-v3/CLAUDE.md; mirrors the
        blocked_substrate stop-gate and points the user at /implement-substrate.
        Redesigns of a DIFFERENT mechanism (new EXQ number / different claim_ids)
        and commitment-free reads are exempt. Both skill copies (.claude/ +
        .agents/) edited byte-identically. Dry walk-through vs the SD-033b/MECH-263
        485-series: brake fires (count=9 each), names upstream substrate
        f_dominance_conversion_ceiling / MECH-449 constitution, correctly HOLDS
        (MECH-448/ARC-107 built but MECH-449 still under construction) -> route to
        build, not another 485-letter. Matches the documented first-migration
        candidate commitment_closure:GAP-8. PROMOTES NOTHING. Direct fix for the
        7-12x lettered re-runs circling one ceiling.
    - id: MOVE-4
      title: "Assembly/maturity portfolio view (the missing broad-overview altitude)"
      status: done
      severity: medium
      last_updated: 2026-06-21
      note: >
        Closure-plan-node version landed 2026-06-21. The broad-overview altitude
        now exists: serve.py /api/closure carries an `assembly` block
        (`_closure_assembly_view`) bucketing the V3 nodes by maturity /
        assembly-state -- mature(done) / mid_construction(assembling,in_progress)
        / awaiting_construction(assembling,queued|unset) /
        genuinely_blocked(blocked|upstream_blocked|blocked_pending_substrate) /
        remaining(open|partial|in_progress|tracked); deferred-family parked out.
        It also computes assembly-frontier health live from the MOVE-1 node
        fields (awaiting/assembly_status/revisit_after now passed through
        read_closure's node_record), with `revisit_due` evaluated against today.
        closure.html (CLOSURE_VERSION 2026-06-21.1) renders an "Assembly
        maturity" strip below the closure bar: a TWO-number headline (closure %
        AND frontier count + revisit-due, never one burndown), a segmented
        maturity bar, a per-bucket legend, and click-to-highlight frontier
        chips. Verified end-to-end (synthetic-node bucketing + live render on
        :8011: 79.0% closure unchanged, frontier 0/empty honestly -- no live
        node tagged assembling yet; populated-path render confirmed via
        injection). REMAINING FOLLOW-ON (larger, claims-layer, still open):
        consolidate the 6 scattered substrate-blocked conventions
        (substrate_conditional / substrate_ceiling / v3_pending /
        implementation_phase>=v4 / two pending_* booleans) into one canonical,
        machine-readable field with an `awaiting:` pointer -- see Open
        follow-ons.
---

# Assembly vs closure: making the machinery assemble, not just finish

**Status:** MOVE-1 (keystone) + MOVE-2 (assembly-chip path) + MOVE-3 (re-derive
brake) + MOVE-4 (assembly/maturity portfolio view) all landed 2026-06-21. The
four-move mechanism is complete; the only open item is the larger claims-layer
consolidation of the 6 scattered substrate-blocked conventions (see Open
follow-ons).
**Origin:** user observation 2026-06-21 — "the machinery gets stuck in myopic
attempts to force closure before substrate is ready. We are meant to be
assembling, not tying off loose ends." Diagnosis below grounded in a 3-sweep
review of the governance / closure / work-rhythm machinery (see WORKSPACE_STATE
entry of the same date).

## Diagnosis: one mode where it needs two

REE runs on an **adjudication engine** — every experiment outcome injects a
mandatory closure pipeline (autopsy -> governance walk -> mark-reviewed ->
reconcile docs -> land -> spawn closure-chips). That engine is genuinely good:
per-claim promotion gates are hard, vacuous FAILs are defanged
(`non_degenerate`, `precondition_unmet`, scoring exclusions), a not-yet-diagnosed
FAIL is denied an evidence stamp. Strong protection against forcing a *verdict*.

The problem: **assembly is not a first-class mode** — it is treated as the
absence of closure. Measured evidence:

- **Work rhythm ~65-70% closure/cleanup, ~15-20% assembly.** Assembly is never
  a starting move: the only path into `/implement-substrate` is a failure
  autopsy emitting `recommended_substrate_queue_entry`. You build substrate only
  as a *consequence of a failure*, never because you decided to.
- **74% of failure autopsies (111/151) conclude `substrate_ceiling`** — "the
  substrate isn't rich enough." Zero conclude claim falsification. The modal
  output of the whole machine is the *same finding re-derived*: EXQ families
  603 (x12), 654/514/460 (x7 each) — lettered iterations circling one claim.
- **The closure metric punishes correct patience.** `generate_closure_snapshot`
  scored a legitimately parked-pending-substrate node at **0.1** — about the
  same as a neglected one. The drift detector flags every non-terminal node
  every cycle; staying open cost a recurring manual `last_updated` re-stamp
  while closing is a one-time write. Least-friction path: close it, or
  reclassify it away.
- **The chip rule drops forward-assembly work by construction.** session-land
  Phase 3 skips "anything blocked on upstream — a planned substrate, a pending
  run." New substrate work is almost always blocked on upstream substrate, so
  the build work that would relieve the ceiling falls on the floor every session.

**Root cause.** "This node is waiting on substrate still being assembled" is not
a first-class, machine-readable, *restful* state. At the claims layer it is
scattered across 6+ overlapping conventions (`substrate_conditional` x155,
`substrate_ceiling` x28, `v3_pending` x218, `implementation_phase >= v4` x170,
two `pending_*` booleans). At the closure-plan layer it had no penalty-free,
low-maintenance representation at all — so the only portfolio-altitude tool
(`closure.html`) is a *burndown*, and the broad-overview altitude the user wants
(what is being built vs mature vs blocked) structurally did not exist.

## The fix: give Assembly its own lifecycle, parallel to Adjudication

Four moves, ordered by leverage. Each serves both altitudes (drill-down +
overview): the state change enables the overview; the queue change enables the
drill-down.

### MOVE-1 — first-class `assembling` state (the keystone). DONE 2026-06-21.

A node may declare `status: assembling` (alias `open_by_design`): *required for
v3, actively or intentionally under construction — substrate being built, not a
stalled gap.* It is:

- **Credited on its own axis, never punishing the %.** `CLOSURE_STATUS_WEIGHTS`
  maps it to `None` — excluded from the closure-% denominator (like `deferred`),
  but unlike `deferred` it is *required* for closure, so it is surfaced
  separately as the **assembly frontier**, not hidden.
- **Held out of the `remaining` backlog.** It is on the frontier, not the
  to-close list, so it never inflates "what is left to close v3."
- **Restful in drift.** `check_closure_drift` deliberately keeps it OUT of
  `NON_TERMINAL_STATUSES`, so it is never flagged drifted/stale and needs no
  recurring Case-3 re-stamp to stay quiet — the maintenance asymmetry that made
  "keep assembling" the most effortful choice is gone. It is still listed,
  auditably, in an "Assembly frontier — resting, not drift" report section.
- **Has an opt-in resume trigger.** `revisit_after: YYYY-MM-DD` is the *only*
  thing that disturbs its rest: once the date passes, the node is flagged
  `revisit_due` for review. No date == rests indefinitely.

**Node fields (canonical spec):**

| field | meaning |
|-------|---------|
| `status: assembling` | required-for-v3, under construction (alias `open_by_design`) |
| `awaiting:` | the substrate being built (claim/SD/MECH id or short phrase) |
| `assembly_status:` | build state of that substrate: `queued` / `in_progress` / `built` |
| `revisit_after:` | optional `YYYY-MM-DD`; past-date -> `revisit_due` flag |

**Where it lives in code:** `serve.py:CLOSURE_STATUS_WEIGHTS` (single source of
truth) + byte-identical fallback in `scripts/generate_closure_snapshot.py`;
bucket + "Assembly frontier" section in `generate_closure_snapshot.py`;
`ASSEMBLING_STATUSES` + `assembly_frontier_record()` + report section + JSON
sidecar in `scripts/check_closure_drift.py` (self-test fixtures included).

**Validation at landing:** closure % unchanged at 79.0% (no real node uses the
status yet — non-disruptive); drift counts unchanged; `--self-test` green
including 5 new fixtures; functional smoke (a temp plan with one `open` + one
`assembling` node) confirmed the open node dragged the % and joined `remaining`
while the assembling node sat in the frontier bucket and moved neither.

### MOVE-2 — assembly-chip path mirroring the closure-chip path. DONE 2026-06-21.

Closure work pulls itself forward (chips); assembly did not. The session-land
Phase 3 chip rule dropped "anything blocked on upstream" by reflex, and new
substrate work is almost always blocked on upstream substrate — so the build
work that relieves the ceiling fell on the floor every session.

Fixed by splitting Phase 3 rule 3 into two:

- **rule 3** — still skip vague observations, trivial inline fixes, and work
  **blocked on a pending run** (an experiment is queued/running, correctly
  in-flight; let it finish).
- **rule 3a** — do **not** drop forward-assembly work. An **unbuilt** substrate
  is chipped as a **build task** (route to `/implement-substrate`) when all four
  hold: (a) on the critical path, (b) not built, (c) in no build queue, (d)
  nobody constructing it. Verify (b)-(d) against `ree-v3/experiment_queue.json`,
  `evidence/planning/substrate_queue.json`, `TASK_CLAIMS.json`, and
  plan-of-record `*_plan.md` status tables (the same not-already-in-flight
  discipline as rule 2). The chip names the substrate (claim/SD/MECH id) and
  states it is on the critical path with no active builder. Queued / in-progress
  / already-claimed substrate stays skipped (in-flight, not dropped).

The report-line example was reconciled to match. Edited both skill copies
(`.claude/skills/session-land/SKILL.md` + `.agents/` mirror) byte-identically.

### MOVE-3 — hard brake on the re-derive loop. DONE 2026-06-21.

`/failure-autopsy` already had a granularity-debt recurrence hook that *detected*
the Nth circling of a claim but did not *gate the queue*. It now gates, in two
halves that enforce each other:

- **Producer (`/failure-autopsy` Step 7).** On the Nth (`RE_DERIVE_BRAKE_THRESHOLD`,
  default 2) `substrate_ceiling` / `non_contributory` autopsy for the same claim
  (counted over `failure_autopsy_*.json` `targets[].claim_ids`), the brake fires:
  recommended routing is forced to `/implement-substrate` on the named upstream
  substrate, a same-claim test re-queue is **explicitly refused**, and the firing
  is stamped on the autopsy target via a new `re_derive_brake{}` field
  (`fired` / `threshold` / `prior_substrate_ceiling_autopsies` / `refused_requeue`
  / `route_to` / `upstream_substrate`). A redesign of a *different* mechanism or a
  commitment-free read is exempt.
- **Consumer (`/queue-experiment` Step 2.5b).** Refuses to queue a new
  same-granularity test of a claim that already has >=2 `substrate_ceiling`
  autopsies on record **unless** the named upstream substrate now shows
  `IMPLEMENTED` / `VALIDATED` in `ree-v3/CLAUDE.md` (brake released — the re-test
  is finally meaningful). Otherwise it mirrors the existing `blocked_substrate`
  stop-gate and points the user at `/implement-substrate`. This catches the case
  the producer half misses: a re-queue attempted without running an autopsy, or
  from a different session.

Stops the 7-12x lettered-iteration burn before it starts. Both skill copies
(`.claude/` + `.agents/`) edited byte-identically. **Validated** by a dry
walk-through against the SD-033b/MECH-263 485-series: brake fires (9 prior
substrate_ceiling autopsies on each claim), names upstream substrate
`f_dominance_conversion_ceiling` / the MECH-449 Go/No-Go constitution, and
correctly **HOLDS** (MECH-448/ARC-107 implemented but MECH-449 still under
construction) — routing the work to the build queue instead of a 13th 485-letter.
That is exactly the documented first-migration candidate (`commitment_closure:GAP-8`
awaiting MECH-449).

### MOVE-4 — assembly/maturity portfolio view (the missing altitude). OPEN.

With MOVE-1 making the data queryable, add a dashboard (or `closure.html` mode)
showing the whole assembly by maturity + assembly-state, headlined by TWO
numbers — closure % (adjudication health) AND assembly-frontier health —
instead of one burndown %. Prerequisite for the full version: consolidate the 6
scattered claims-layer substrate-blocked conventions into one canonical,
machine-readable field with an `awaiting:` pointer (claims-layer follow-on,
larger than this doc's scope).

## Rollout (MOVE-1 is mechanism; tagging real nodes is separate)

The keystone adds the *capability*; it does not re-tag any live node. Re-tagging
is a governance judgment and must be done under a claim, not raced against a
live session. **First candidate: `commitment_closure:GAP-8`** — currently
`in-progress`, its `owner_exq` has cycled 485i -> 485j -> 485k (superseding
lettered re-runs circling the F-dominance conversion ceiling) while the honest
state is "awaiting the MECH-449 Go/No-Go constitution, which is under active
construction this session." That node is the textbook re-derive loop and the
natural first `status: assembling` / `awaiting: MECH-449` /
`assembly_status: in_progress` migration once the MECH-449 build settles.

Other candidates: any closure node whose `owner_exq` is on its 3rd+ letter with
repeated `non_contributory` / `substrate_ceiling` autopsies and a named upstream
substrate on the substrate_queue.

## Open follow-ons

- MOVE-2 + MOVE-3 + MOVE-4 done 2026-06-21 (all four moves landed).
- ~~Harden MOVE-3 from a skill-doc gate to a code gate: a `validate_queue.py` /
  indexer check that flags a queued same-granularity re-test of a claim with >=2
  `substrate_ceiling` autopsies whose upstream substrate is not yet built (the
  doc-level brake relies on the skill being followed; a validator backstop would
  catch a hand-edited queue append).~~ **DONE 2026-06-22.** Landed in
  `ree-v3/validate_queue.py` as a **warn-only** backstop (user-confirmed severity;
  mirrors `validate_claims.py`'s warn-only enum checks). It re-applies the EXACT
  `/queue-experiment` Step 2.5b + `/failure-autopsy` Step 7 counting logic
  (`substrate_ceiling` in `recommended_epistemic_category` OR `non_contributory` in
  `recommended_evidence_direction`, one hit per `failure_autopsy_*.json` per claim)
  at queue-validate time — which runs at the PreToolUse git-commit hook AND at
  runner startup, so a hand-edited queue append is caught even when the skill was
  bypassed. For every claim a queued item tags with >= `RE_DERIVE_BRAKE_THRESHOLD`
  (default 2) counted autopsies, it resolves the most-recent counted autopsy's named
  upstream substrate (`recommended_substrate_queue_entry.target_sd_id` /
  `sd_id_suggested` / `re_derive_brake.upstream_substrate`) and WARNs unless that
  substrate shows `IMPLEMENTED`/`VALIDATED` on a single `ree-v3/CLAUDE.md` line
  (same-line, token-boundary match — so a nearby unrelated `IMPLEMENTED` header
  cannot falsely release it). Warn-only (`_LAST_WARNINGS`), never blocks the commit
  hook or runner. Exemptions: claimless items, an item whose `note` documents a
  brake clearance, and (advised in the warning text, not auto-detected) redesigns of
  a different mechanism / commitment-free reads / diagnostics. Validated against the
  live queue (correctly fires on `V3-EXQ-654i` MECH-309/ARC-062 → unbuilt
  `f_dominance_conversion_ceiling`, exit 0) + a synthetic suppression/threshold/
  note-clearance/claimless/word-boundary test (all branches green). PROMOTES
  NOTHING; tooling backstop. The indexer was deliberately NOT chosen — it is
  derive-only and runs too late to catch a commit-time append.
- Claims-layer consolidation of the 6 substrate-blocked conventions into one
  canonical `assembling`-equivalent with a machine-readable `awaiting:` edge.
  MOVE-4's portfolio view landed over the closure-plan-node layer (which MOVE-1
  made queryable); this consolidation is the deferred claims-layer half that
  would let the same maturity buckets be drawn over the whole claims registry,
  not just the closure-plan nodes.
- Decide whether meta-generation plans should ever be drift-scanned (currently
  not; they have no owner_exq experiments).
