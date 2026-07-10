---
title: "Status/History Plane Separation"
nav_exclude: true
---

# Status / History Plane Separation — Plan of Record

**Pipeline id:** `status_history_plane`
**Registered:** 2026-07-10
**Last updated:** 2026-07-10
**Owner session:** ree-audit-review-26e305 (doc-accuracy audit)
**Promotes/demotes:** NOTHING — this is documentation/tooling infrastructure, not a claim.

> **Deliberately carries NO `closure_plan:` frontmatter.** This is a tooling/governance
> build, not a v3-substrate closure plan; it must not be auto-discovered by
> `generate_closure_snapshot.py` or counted toward the v3 closure %.

---

## 1. Problem (the doc-accuracy audit that motivated this)

The "true front of progress" is **not missing** from the repo — as of 2026-07-10 it is
recorded, correctly and redundantly, in at least four places:

| Artifact | Currency | Owner (generator) |
|---|---|---|
| `insights_report.md` | today | `/insights` skill |
| `docs/roadmap.md` "Status Snapshot" (top of an 859 KB / 4120-line file) | today | `/update-docs` nightly |
| `evidence/planning/closure_status.md` + `closure_drift.md` | today | `governance.sh` |
| autopsies `failure_autopsy_*.json` + the `closure_plan` frontmatter of each `*_plan.md` | today | hand-written / `/failure-autopsy` |

Yet a cold-start reader (human or agent) following the Session Startup Protocol
(`CLAUDE.md` -> `NEW_AGENT_START_HERE.md` -> `WORKSPACE_STATE.md` -> `TASK_CLAIMS.json`
-> `pending_review.md`) is **routed to none of them**, and a grep of `README.md`,
`START_HERE_HOW_REE_DEVELOPS.md`, `index.md`, `NEW_AGENT_START_HERE.md` for
`insight|competence|policy-learning|current front|724|737` returns **zero hits**.

Two distinct failures, not one:

- **Failure A — routing.** The entry docs were built for *rules* (how to work), never for
  *state* (where we are). `WORKSPACE_STATE.md` (6631 lines) is used as the de-facto state
  surface but its newest entry is instrumentation minutiae, not the scientific front.
- **Failure B — signal-to-noise at the terminal.** Where the truth *is* recorded, the live
  line is co-mingled with its entire superseded history in the same append-only prose field.
  The `conversion_ceiling_campaign:CAMPAIGN` node's `phase:` field is a single ~500-word
  paragraph; `closure_drift.md` "Suppressed" rows are 500+ words *each*. Extracting "the one
  live line" requires reading everything it superseded.

Compounding confounds:
- **git-mtime is a misleading currency signal.** ~150 architecture docs share a `2026-06-13`
  git date from a bulk nav-frontmatter stamp (`apply_nav_frontmatter.py`); their content
  currency is unrelated to that date.
- **Two doc populations, unlabelled.** *Generated* docs stay current because a script owns
  them; *manually-maintained* docs (`GOVERNANCE_STATE.md` last touched 2026-03-02;
  `REE_overview.md` Apr; `index.md` May; the 184 architecture-doc `**Status:**` body lines)
  rot silently with no owner. Nothing marks which is which.

**Root cause:** current status and history are *fused into one prose field* with *one*
maintenance model, when they are two different kinds of thing with *opposite* maintenance
models.

---

## 2. Principle (the design razor)

**Derivability decides the plane.** If a value can be recomputed from other records, it is
*current status* -> **derive it**, let it be blown away and rebuilt. If it can only be
recorded once at the moment it happened, it is *history* -> **append-only**, authoritative,
never regenerated.

- A judgement ("724 showed the deficit is diffuse") is a fact-at-a-timestamp you cannot
  re-derive -> **history plane**.
- "The front is the competence wall" is a *projection over* those judgements you can and
  should recompute -> **status plane**.

The two planes are **separate but intimately co-operable**: history is an *input* to the
projection, and each projection *contributes back* to history (below).

---

## 3. The event-sourced contract (settled 2026-07-10)

```
events (append-only, authoritative)
   |  autopsy/v1 JSON  +  result manifests  +  decision_log
   v
projector  =  pure fn over an EVENT SLICE (not just the newest event)
   |
   +--> live   (regenerable status-plane field; overwritten each run)
   +--> status_snapshot/v1  (APPENDED back into the event log -> the status
   |                         timeline becomes history too)
   v
views (Q2 = BOTH)
   +--> query API  (serve.py; tools)
   +--> generated *_history.md sidecar  (humans, server-free)
```

**Contract terms:**

1. **Full projection.** The `live` head is machine-projected for every node/claim each
   `governance.sh` run; all hand-written prose is removed from status fields. *Constraint
   from the owner:* projection must **not destroy history bits** — see the non-destructive
   razor (§5).
2. **The projector consumes a slice, not the newest event.** Proven necessary on real data
   (§6): the newest event can be a measurement-instrument autopsy whose routing is not the
   node's live head. Reconciliation rule: **prefer the newest event carrying a *forward*
   routing** (`recommended_substrate_queue_entry` present, or `routing` in
   {`queue-experiment`, `implement-substrate`} with a target); treat instrument/measurement
   autopsies (`routing: governance`, category `test_design_ceiling`/observability) as
   *modifiers*, not the head.
3. **`needs_review` flag (the full-projection safety valve).** When the slice is ambiguous
   (e.g. newest forward-routing event predates a later non-forward event, or children
   disagree at an umbrella), the projector still emits `live` **and** sets
   `live.needs_review: true` so a human glances rather than the head silently mis-projecting.
   This preserves full projection without reverting to hybrid hand-authoring.
4. **Projections are events.** Each run appends a `status_snapshot/v1` record (the derived
   `live` per node at that timestamp) to an append-only log, so "what did we believe the
   front was on DATE" is answerable.
5. **Join = union.** `join(node) = events where (bears_on ∋ token) UNION (claim_ids ∩ scope_claims)`.
   `bears_on` was formalized recently (GOV-DIAG-1); older events join only via `claim_ids`
   and get an **additive `bears_on` backfill** (append-only, non-destructive).
6. **Brake state is derived** from the slice (`count(substrate_ceiling events) >= threshold`),
   not hand-asserted.

---

## 4. Schema (before -> after)

### 4a. Closure-plan node

**Before** (fused; the live line buried in ~500 words of superseded history):
```yaml
- id: "conversion_ceiling_campaign:CAMPAIGN"
  phase: "<~500-word paragraph mixing the live head with 714/715a/717/689a/654-lineage history>"
  status: assembling
  owner_exq: "null -- umbrella; the live path is the brake-EXEMPT ... <+ history>"
  awaiting: "<another live+history blob>"
```

**After** (two planes, one join key):
```yaml
- id: "conversion_ceiling_campaign:CAMPAIGN"
  status: assembling                 # derived
  severity: load-bearing
  live:                              # STATUS PLANE -- projected, regenerable
    as_of: 2026-07-08
    from: failure_autopsy_V3-EXQ-719a_2026-07-08   # provenance = one event id
    verdict: non_contributory/substrate_ceiling
    next: "brake-EXEMPT competence-localization diagnostic V3-EXQ-737/734; then /implement-substrate on localized gap"
    brake: fired
    needs_review: false
  join:                              # HISTORY PLANE -- queried, not stored inline
    bears_on: [f_dominance_conversion_ceiling, "ree_ai_design_critique_plan:WS-1"]
    scope_claims: [MECH-439, MECH-309, ARC-062, MECH-445, MECH-446, MECH-448, MECH-449]
```
History is reached by the join into the append-only autopsy/manifest files — never
re-pasted into the plan file.

### 4b. Claims registry (`claims.yaml`) — Phase 2

Add a derived `live_status` block (projected from the same event stream) alongside the
existing append-only fields; add per-claim `last_reviewed` so "recently-moved truth" is
sortable. `status:` stays the human-set epistemic category; `live_status` carries the
*derived* current reading + `as_of` + `from`.

### 4c. Architecture-doc `**Status:**` lines — Phase 2

The 184 hand-typed `**Status:**` body lines (71 say `candidate`/`v3_pending`) are replaced
by a value **derived from `claims.yaml`** and moved into machine-checkable YAML frontmatter
(`status:` + `status_asof:`), stamped by an `apply_status_frontmatter.py` companion to the
existing nav stamper. A `claims_doc_drift.py` (mirror of `closure_drift.py`) fails when a
doc's status != claims.yaml. (Confirmed live drift example today: `sd_063_*.md` still says
"v3_pending until V3-EXQ-716 scores" though SD-063 was promoted provisional 2026-07-09.)

---

## 5. Non-destructive migration razor (the owner's hard constraint)

Before any hand-written blob is collapsed:

1. **Diff** the blob against the structured events it should derive from.
2. **Any residual** — content in the blob not present in any event (e.g. a cross-face
   reconciliation written directly into the plan, never captured as an event) — is **lifted
   into the log first** (a backfilled autopsy note / decision_log / snapshot entry).
3. Only then collapse the blob to `live:` + `join:`.

The projector only ever **writes the regenerable field and appends**; it never edits or
deletes an event. The Phase-0 diff report *is* the audit of "history bits at risk."

---

## 6. Proof-of-concept result (read-only, run 2026-07-10)

A read-only projector (scratchpad `project_head.py`) run on the campaign node
(join `bears_on='f_dominance_conversion_ceiling'`) produced a correct history index —
`719a -> 724 -> 732 -> 732a`, the real competence-floor chain — and **immediately proved two
contract terms on real data**:

- **Newest-event != live head.** The newest event (732a) is the measurement-instrument
  autopsy (`test_design_ceiling`, `routing: governance`, blank detail); the node's true head
  ("run H1/H2 discriminator 737/734") lives in 719a/724. => the projector MUST reconcile
  across the slice (contract term 2) and flag ambiguity (term 3). "History is needed to
  compute status," proven.
- **Join must be a union; older events need backfill.** Only 4 events carried the `bears_on`
  token; the campaign's full history (714/715a/717/689a/654-lineage) joins via `claim_ids`
  (ARC-062/MECH-309). The naive brake count read 1 instead of 20+. => contract term 5 + the
  `bears_on` backfill.

Both findings are *good news*: the projector is feasible, and the two things needing care
are now precisely scoped.

---

## 7. Phasing + status table (resume primitive)

| id | title | status | notes |
|----|-------|--------|-------|
| `status_history_plane:SHP-0` | Audit + contract + PoC | **done** 2026-07-10 | this doc; PoC in scratchpad `project_head.py` |
| `status_history_plane:SHP-1` | Harden projector -> fleet-wide **shadow** | **done** (shadow) 2026-07-10 | Landed `REE_assembly/scripts/project_status_head.py` (read-only; PROMOTES/DEMOTES NOTHING, edits no `*_plan.md`). Reconcile rule (newest-forward head + measurement-autopsy modifier override) + union join (claim_ids UNION harvested substrate-token bears_on) + narrow `needs_review` (later-non-forward-than-head, or umbrella children disagree) + `no_events`/`head_forward` split so the flag stays a signal. Emits shadow `live:`+`join:` (`status_head.shadow.{yaml,md}`), per-plan `*_history.md` sidecars (pointer index, newest last), and the **diff-vs-blob report** (`diff_vs_blob.md`, the SHP-2 input) to `scratch/status_history_shadow/` (git-ignored). Sample run 2026-07-10: 42 plans / 316 nodes / 270 autopsy + 293 PASS-manifest + 349 decision events; 111 ambiguous-head, 71 at-risk history refs. Reproduces both PoC findings on the campaign node (732a modifier != live head; union join needed). |
| `status_history_plane:SHP-2` | Collapse closure-plan blobs -> `live:` + `join:` | blocked on SHP-1 | per-plan: lift residuals to log (razor §5), then collapse; extend `closure_drift.py` with a status-plane drift check (projected `live` == stored `live`) |
| `status_history_plane:SHP-3` | `status_snapshot/v1` append log + both views | blocked on SHP-2 | wire snapshot-append + sidecar-gen into `governance.sh`; add query API to `serve.py` (Q2=both) |
| `status_history_plane:SHP-4` | Port to `claims.yaml` (`live_status` + `last_reviewed`) | open | derive `live_status`; add per-claim `last_reviewed`; drift-gated |
| `status_history_plane:SHP-5` | Derive architecture-doc `**Status:**` from claims.yaml | open | `apply_status_frontmatter.py` + `claims_doc_drift.py`; retire the 184 hand lines |
| `status_history_plane:SHP-6` | Entry-doc routing (`CURRENT_FRONT.md`) | open | generated short live-only front doc; one-line pointer from `CLAUDE.md` startup, `START_HERE` "Where detail lives", top of `WORKSPACE_STATE.md`. Fixes Failure A. Can ship independently of SHP-1..5 |
| `status_history_plane:SHP-7` | Retire/auto-stamp abandoned manual docs | **done** 2026-07-10 | Landed `scripts/generate_status_stubs.py` (owner of all 3; wired `governance.sh` Step 3c-bis-3, before the nav stamper). `GOVERNANCE_STATE.md` (V1/V2-era) -> live-source pointer stub; `REE_overview.md` (IMPL-004 `status:legacy`) -> canonical-sources pointer stub (keeps `#impl-004` anchor + `nav_exclude`); `index.md` public Home page regenerated (timeless narrative preserved + owned + stamped; rotting "Latest result" 2026-04-03 block -> live `CURRENT_FRONT.md` pointer; stays `title:Home`). Non-destructive (Sec.5): closed SD-001/002/003 register + Q-019 hypothesis survive in architecture docs + claims.yaml + git. Idempotent; nav-stamper co-operates. REE_assembly master c36a5c3e2e. Ships independently of SHP-1..6. |

**Suggested order:** SHP-6 (cheapest, fixes the felt problem) can go first or in parallel;
SHP-1 -> SHP-2 -> SHP-3 is the structural spine; SHP-4/5 port the pattern; SHP-7 mops up.

---

## 8. Open items / risks

- **Umbrella reconciliation** is the hardest projection case (a node spanning many children's
  events). `needs_review` is the backstop; if too many umbrellas trip it, revisit the
  reconcile heuristic rather than hand-authoring.
- **`bears_on` backfill breadth.** How far back to normalize old autopsies is a bounded
  judgement; join-via-`claim_ids` already covers most, so backfill is an accuracy refinement,
  not a blocker.
- **decision_log / manifest event types.** Full projection must union over autopsies *and*
  PASS manifests *and* decision_log promotions (a build landing / a promotion is also a
  status-moving event, not only autopsies).
- **Concurrency.** Collapsing plan frontmatter (SHP-2) touches high-contention `evidence/`
  files; each plan collapse is a small, claimed, single-plan edit, per the concurrency rules.
