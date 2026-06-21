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
      status: open
      severity: load-bearing
      note: >
        On the 2nd substrate_ceiling autopsy for the same claim family, BLOCK
        re-queuing tests of that claim and force the work into the build queue.
        The granularity-debt recurrence hook already DETECTS the loop; make it
        GATE. Direct fix for 7-12x lettered re-runs circling one ceiling.
    - id: MOVE-4
      title: "Assembly/maturity portfolio view (the missing broad-overview altitude)"
      status: open
      severity: medium
      note: >
        A dashboard (or closure.html mode) showing the whole assembly by
        maturity + assembly-state: mature / mid-construction / awaiting
        construction / genuinely blocked. Headline = TWO numbers (closure % AND
        assembly-frontier health), not one burndown %. Depends on MOVE-1's
        queryable state + consolidating the 6 scattered substrate-blocked
        conventions (claims-layer follow-on).
---

# Assembly vs closure: making the machinery assemble, not just finish

**Status:** MOVE-1 (keystone) + MOVE-2 (assembly-chip path) landed 2026-06-21.
MOVES 3-4 open.
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

### MOVE-3 — hard brake on the re-derive loop. OPEN.

`/failure-autopsy` already has a granularity-debt recurrence hook that *detects*
the Nth circling of a claim but does not *gate the queue*. Make it gate: on the
2nd `substrate_ceiling` for the same claim family, block re-queuing tests of that
claim and route the work into the build queue (MOVE-2). Stops the 7-12x
lettered-iteration burn before it starts. Edit: `.claude/skills/failure-autopsy/`
+ a check in `/queue-experiment` substrate-readiness Step 2.5.

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

- MOVE-3, MOVE-4 (above). MOVE-2 done 2026-06-21.
- Claims-layer consolidation of the 6 substrate-blocked conventions into one
  canonical `assembling`-equivalent with a machine-readable `awaiting:` edge
  (prerequisite for MOVE-4's full portfolio view).
- Decide whether meta-generation plans should ever be drift-scanned (currently
  not; they have no owner_exq experiments).
