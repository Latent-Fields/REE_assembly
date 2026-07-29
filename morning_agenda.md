# Morning Agenda — 2026-07-29

Generated: 2026-07-29T04:24:30Z

> **DEGRADED RUN — `governance.sh` was NOT run.** Live sessions at generation time:
> `IGW-20260728-192 MECH-217 implement-substrate STAGED`
> (`igw-auto-igw-192-substrate-ready-mech-217-20260728T221941Z`, age `6`h). The Governance
> Agenda, Experiments Awaiting Review, and granularity/category audit sections below reflect the
> **last** pipeline run (2026-07-28T20:22Z), not today's state. Re-run `/morning-digest` manually
> once sessions are clear to refresh them.

**Second staleness note (not the standard banner).** `REE_assembly` is diverged locally
(ahead 3 / behind 5) with 1227 dirty files, so no pull was performed — pulling or resetting a
shared dirty checkout is the documented skew/autostash hazard. Three runs that completed **after**
the last pipeline run are therefore absent from `pending_review.md` below and are surfaced
separately: **V3-EXQ-835 (PASS)**, **V3-EXQ-810a (PASS)**, **V3-EXQ-834 (FAIL)**.

---

## Headlines — Positive Results & Live Decisions

Covering 2026-07-21 (last digest) → 2026-07-29. Twelve PASSes landed in that window; the six
below are the ones that change what to do next. **The two newest are not yet in
`pending_review.md` and are not in `review_tracker.json` — they are brand-new and undiscussed.**

- **V3-EXQ-810a — `arc071_chunk_accumulator_readiness` — PASS** (decision-flipping diagnostic;
  per-claim direction emitted, all three `supports`)
  - **Moves:** ARC-071, MECH-323, MECH-324 — all three `supports`. ARC-071 and MECH-323/324 are
    all `v3_pending: true`; ARC-071 sits at `exp_conf=0.0` (lit 0.826, `plausible_unproven`) with
    **no experimental evidence at all**, so this is its first experimental signal.
  - **Makes live / unblocks:** `chunk_accumulator_fires` directly reverses
    `chunk_accumulator_silent` (V3-EXQ-810, 2026-07-23, FAIL) — the readiness gate that blocked
    the whole ARC-071 chunk-accumulator line is now clear.
  - **Gate on acting:** the very next consumer already ran and did **not** clear —
    **V3-EXQ-834** (`arc071_mech323_budget_coupled_ceilings`, 2026-07-29T00:23Z) is FAIL
    `substrate_not_ready_requeue` with `chunks_formed = False` on **all five arms** (`STATIC_H50`,
    `BOTH_H30`, `SIZE_H50`, `DEPTH_H50`, `BOTH_H50`), despite outcome-spread and symbol-buffer
    preconditions all met. So the accumulator *fires* in the 810a readiness harness but *forms no
    chunks* in the 834 ceiling harness — that discrepancy is the first thing to adjudicate.
    Also `DEPTH_H50`/`BOTH_H50` report `depth_gain_evaluable_trials = False`.

- **V3-EXQ-835 — `mech068_consolidation_selectivity_ablation` — PASS / `supports`** (evidence)
  - **Moves:** MECH-068 — `exp_conf=0.0` → first experimental support (lit 0.668,
    `plausible_unproven`, 1 supporting entry, 0 opposing).
  - **Makes live / unblocks:** `consolidation_operator_has_selection_authority` — establishes the
    consolidation operator is selective rather than uniform, i.e. an authority result, not a
    throughput one.
  - **Gate on acting:** none identified; unreviewed, so route through `/governance` before it
    weighs.

- **V3-EXQ-819a — `mech457_inv088_zworld_trained_vs_random_gatefix` — PASS**
  (decision-flipping; `evidence_direction: unknown`, so it scores nothing but moves the plan)
  - **Moves:** MECH-457 (`v3_pending`, `exp_conf=0.361`, 16 supports / 3 weakens across 24
    entries, 0 PASS / 2 FAIL runs) and INV-088 (`exp_conf=0.289`).
  - **Makes live / unblocks:** `zworld_prediction_training_confers_advantage` **reverses**
    V3-EXQ-819's `zworld_advantage_grid_nondiscriminative`. Supersedes 819 as a
    `measurement_test_design_defect` fix, user-confirmed 2026-07-26 in
    `failure_autopsy_batch-793a-817-819_2026-07-26.md` target 3. Three fixes, all measurement —
    substrate and science unchanged; the headline one re-scores `post_bc_install_took` on the
    strict-majority install fraction, the identical predicate the router uses.
  - **Gate on acting:** MECH-457 is the cold-start competence-floor claim — the standing
    competence-floor observability confound (privileged global oracle vs the agent's local view)
    still applies to anything built downstream of it.

- **V3-EXQ-832 — `inv041_childhood_exposure_context_diff` — PASS / `supports`** (evidence)
  - **Moves:** INV-041 (`exp_conf=0.773`, `confirmed_established`, 2 supporting / 0 opposing) and
    MECH-153 (`exp_conf=0.617`).
  - **Makes live / unblocks:** C1 supports INV-041 — the childhood (balanced/forced) exposure
    regime differentiates ContextMemory while the avoidance-shaped regime does not, **despite
    identical supervised labelling**. So committed exposure is a *necessary prerequisite*, not
    merely the labelling objective (MECH-153). This is a direct hit on the ontogenetic-ordering
    thread (approach-before-avoidance as a candidate conversion-ceiling root): an avoidance-shaped
    schedule provably fails to differentiate where the childhood schedule succeeds.
  - **Gate on acting:** none identified; unreviewed.

- **V3-EXQ-825 — `mech245_generative_dominance_deafferentation` — PASS / `supports`** (evidence)
  - **Moves:** MECH-245 (`candidate`, `exp_conf=0.77`, `confirmed_established`, 3 supporting /
    0 opposing / 0 weakens).
  - **Makes live / unblocks:** generative-model dominance under deafferentation demonstrated on
    a GRU forward model standing in for the E1/E2 top-down generative pathway, rolled through a
    grounding phase then a deafferentation window against the real `E3TrajectorySelector`
    bottom-up-mismatch pathway.
  - **Gate on acting:** the generative pathway is a GRU stand-in, not E1/E2 itself — a
    substrate-native replication is the obvious follow-on before this carries full weight.

- **V3-EXQ-032d — `mech102_ttype_escalation_fixed` — PASS / `supports`** (evidence; supersedes
  V3-EXQ-032b)
  - **Moves:** MECH-102 (`active`, `exp_conf=0.63`, but a heavily contested record — 11 supports
    / 11 weakens / 12 mixed, 4 PASS / 21 FAIL), ARC-024 (`provisional`), SD-003 (`superseded`).
  - **Makes live / unblocks:** a PASS on a claim whose experimental record is an even split is
    disproportionately informative; worth reading against the 21 prior FAILs rather than in
    isolation. MECH-102 is one of the two claims Phase-3 lit/exp decoupling surfaced as
    demotion-eligible, so this cuts against that.
  - **Gate on acting:** SD-003 is already `superseded` — do not let this run re-weight it.

Also PASS/`supports` in the window, lower decision-leverage: **V3-EXQ-815** (MECH-321/ARC-070,
`policy_decomposition_fires`), **V3-EXQ-811a** (MECH-477/MECH-163,
`arbitration_produces_differential_recruitment`), **V3-EXQ-818** (ARC-016,
`eval_time_threshold_engages_and_tracks_precision_monotonically`), **V3-EXQ-806** (SD-078
centering), **V3-EXQ-807** + **V3-EXQ-823** (SD-079 centering / ghost-goal retrieval).

**Deliberately NOT headlined:** V3-EXQ-830 (`slow_never_fires_on_rollout`) is a PASS but the
indexer flagged it **`vacuous_pass`** — its label must not drive a governance action until
`/failure-autopsy` adjudicates it.

---

## Queue Status

- **Total pending: 0** — Mac: 0 | PC: 0 | EWIN: 0 | any: 0
- **ALERT: QUEUE EMPTY.** Zero pending items. Only 2 claimed items remain in flight:
  - `V3-EXQ-833` — claimed by `ree-cloud-1` at 2026-07-27T23:39:56Z (**~28.7h ago** — long for a
    claim; worth confirming it is genuinely running rather than stranded)
  - `V3-EXQ-798a` — claimed by `ree-cloud-3` at 2026-07-29T00:23:38Z (fresh, ~4h)
- **Fleet-idle watcher:** `idle_risk = true`, claimable backlog **0** (threshold 3), snapshot
  `2026-07-28T22:09:04Z`. `ready_sd_validation_candidates` is **EMPTY**, with
  `excluded_validation_already_ran = 32`, `excluded_no_queueable_validation = 21`,
  `excluded_known_churn = 3`. **Refill therefore needs a fresh `/queue-experiment` design, not a
  re-queue** — every built SD's validation has already been attempted.
- **Owed successors (passed all four Step 7c checks — script written, never queued, never ran,
  provenance confirmed):**
  - **V3-EXQ-490g** — `v3_exq_490g_mech295_cascade_gap4_tier1.py`
  - **V3-EXQ-471a** — `v3_exq_471a_catatonic_lock_gap4_tier1.py`
  - **V3-EXQ-475a** — `v3_exq_475a_sd036_decay_gap4_tier1.py`
  - All three belong to `goal_pipeline_plan` GAP-4 (`in-progress`), whose `Blocking on` names a
    2-fork precondition: *"(A) Tier-1 library rebuild + 483d/490g re-queue; (B) SD-XXX scaffolded
    SD-054 onboarding substrate."* **483d has since run**, so fork A is at least partly cleared —
    verify the Tier-1 library rebuild landed before queuing. With the queue at zero these are the
    cheapest available refill if that gate is clear.
- **Gated, not owed:**
  - **V3-EXQ-514g** — `v3_exq_514g_sd049_bg_gating_wider_seeds_stepharness.py` exists and never
    ran, but `goal_pipeline_plan` GAP-2 is status `blocked`, gate = **"Phase 1 PASS"**. Correctly
    waiting, not dropped.
- **Phantom Owner-EXQ ids — plan prose names an experiment that was never created; needs a
  plan-prose correction, NOT a queue run:**
  - **V3-EXQ-739** (`ree_ai_design_critique_plan`, WS-14 decision text) — the row describes "the
    737/738/739 portfolio (P-A representation / P-B measurement / P-C observation axes)".
    **737 and 738 both ran; 739 has no queue entry current or historical, no script, and no
    manifest.** The P-C observation axis was never minted. Fix the WS-14 prose (or mint P-C
    deliberately under a fresh id) — do not "re-queue" 739.
  - **V3-EXQ-732b** is also absent everywhere, but that is **correct**: the same plan records
    "REFUSED V3-EXQ-732b same-question power bump". No action.

---

## Experiments Awaiting Review (18 indexed / 0 runner-only, per the 2026-07-28T20:22Z pipeline run)

**Plus 3 more that completed after that run and are not yet listed there** (and are not in
`review_tracker.json`): V3-EXQ-835 (PASS), V3-EXQ-810a (PASS), V3-EXQ-834 (FAIL).

### PASS (5 listed + 2 new)

| EXQ | Type | Claims (status / exp_conf) | Direction | Note |
|---|---|---|---|---|
| **835** *(new)* | `mech068_consolidation_selectivity_ablation` | MECH-068 (candidate / 0.0) | supports | first experimental evidence for MECH-068 |
| **810a** *(new)* | `arc071_chunk_accumulator_readiness` | ARC-071 (candidate, v3_pending / 0.0), MECH-323 (0.752), MECH-324 (0.477) | supports x3 | reverses 810 `chunk_accumulator_silent`; but see 834 below |
| 825 | `mech245_generative_dominance_deafferentation` | MECH-245 (candidate / 0.77) | supports | GRU stand-in for E1/E2 |
| 032d | `mech102_ttype_escalation_fixed` | MECH-102 (active / 0.63), ARC-024 (provisional), SD-003 (superseded) | supports | supersedes 032b |
| 819a | `mech457_inv088_zworld_trained_vs_random_gatefix` | MECH-457 (candidate, v3_pending / 0.361), INV-088 (0.289) | unknown | supersedes 819; measurement fix |
| 830 | `mech321_scale_resolved_rollout_boundary` | (no claim tags) | non_contributory | **`vacuous_pass` — adjudication required** |
| 832 | `inv041_childhood_exposure_context_diff` | INV-041 (candidate / 0.773), MECH-153 (0.617) | supports | ontogenetic-ordering evidence |

### FAIL (13 listed + 1 new)

Dominated by one signature: **9 of 14 are `substrate_not_ready_requeue`** — those experiments are
not testing their hypotheses, they are bouncing off unbuilt substrate.

| EXQ | Claims | Direction | Self-route label |
|---|---|---|---|
| **834** *(new)* | ARC-071, MECH-323, MECH-324 | unknown | `substrate_not_ready_requeue` — `chunks_formed=False` on all 5 arms |
| 822a | SD-078 | unknown | `substrate_not_ready_requeue` (supersedes 822) |
| 826 | MECH-244 | non_contributory | `substrate_not_ready_requeue` |
| 826a | MECH-244 | non_contributory | `substrate_not_ready_requeue` (supersedes 826) |
| 827 | INV-091 | unknown | `substrate_not_ready_requeue` |
| 827a | INV-091 | unknown | `substrate_not_ready_requeue` (supersedes 827) |
| 824a | Q-081 | unknown | `substrate_not_ready_requeue` (supersedes 824) |
| 822b | SD-078, SD-082 | unknown | `substrate_not_ready_requeue` — **`precondition_unmet`, adjudication required** |
| 817a | SD-080, SD-004 | mixed | `grounding_real_but_not_load_bearing` (supersedes 817) |
| 824 | Q-081 | weakens | `wired_gates_only_landmark_invariant` |
| 829 | MECH-324, MECH-323 | mixed | `retention_real_but_rapid_reacquisition_falsified` |
| 831 | MECH-466 | weakens | `clock_relative_not_exceeded` |
| 828 | INV-091 | weakens | `cross_stream_similarity_band_not_supported` |
| 816d | (none) | non_contributory | `env_still_underdrives_uncertainty` |

**INV-091 has now failed three times** (827 → 827a → 828), ending in an explicit
`cross_stream_similarity_band_not_supported` `weakens`. That lineage reads as closed *against* the
claim rather than blocked — and INV-091 is simultaneously sitting in the governance queue as
`pending_user`, so the two should be resolved together.

### Diagnostic adjudication required (self-route flagged — must not drive governance)

- `v3_exq_822b_sd082_head_internals_diagnostic` — FAIL, `substrate_not_ready_requeue`,
  **`precondition_unmet`**
- `v3_exq_830_mech321_scale_resolved_rollout_boundary` — PASS, `slow_never_fires_on_rollout`,
  **`vacuous_pass`**

Both need `/failure-autopsy` before their labels are allowed to act.

---

## Errors to Diagnose (0)

The 2026-07-28 pipeline run reports **0 runner-only ERROR entries and 0 ERROR manifests**.
`runner_status.json` carries 87 historical ERROR rows, but the newest is 2026-05-31 and they are
already closed or superseded by the pipeline — nothing new to route to `/diagnose-errors`.
(Note `runner_status.json` lags under Phase 3; the coordinator DB is authoritative for ERROR rate.)

---

## Governance Agenda (5 pending_user recommendations)

All five are `hold_candidate_resolve_conflict` — conflicting evidence blocking promotion, not
promote/demote proposals.

| Claim | Status | Recommendation | exp_conf | supports / weakens / mixed | PASS / FAIL |
|---|---|---|---|---|---|
| `INV-091` | candidate | hold — resolve conflict | 0.423 | 3 / 3 / 2 | 0 / 3 |
| `MECH-095` | candidate | hold — literature conflict; gated pending upstream probe/substrate | — | — | — |
| `MECH-163` | candidate | hold — resolve conflict | 0.566 | 13 / 3 / 1 | 1 / 2 |
| `MECH-324` | candidate | hold — resolve conflict | 0.477 | 4 / 0 / 1 | 0 / 1 |
| `MECH-466` | candidate | hold — resolve conflict | 0.323 | 2 / 1 / 0 | 0 / 1 |

Three of the five (INV-091, MECH-324, MECH-466) received **new FAIL evidence in the last 48h**
(828, 829, 831 respectively) that is not reflected in these recommendations — the next full
pipeline run will move them.

**Granularity-debt recurrence (GOV-GRAN-1):** 84 claims with hits, 37 already metabolized,
**0 P0 dropped handoffs** (no chip needed), **3 P1 unflagged recurrences**:

- [P1] **SD-078** — 3 hits / 2 signatures — alignment `unclear=3`, **no `weakened`** → likely
  measurement or implementation debt, not granularity debt. Needs discrimination (coarse-claim →
  `/claim-synthesis` vs coherent substrate-build campaign); no action taken.
- [P1] **MECH-244** — 2 hits / 2 signatures — alignment `unclear=2`, **no `weakened`** → same
  reading. Both its runs (826, 826a) are `substrate_not_ready_requeue`, which is the signature of
  a build campaign, not a coarse claim.
- [P1] **Q-081** — 2 hits / 2 signatures — alignment `unclear=2`, **no `weakened`** → same
  reading; 824 did produce a `weakens`, but under a distinct label.

**Epistemic-category completeness (GOV-CAT-1):** **clean** — `missing_category = 0`,
`claimless_missing = 0`, 10 legacy `unkeyed_schema` warns (singular `claim_id` targets in
`failure_autopsy_V3-EXQ-455a_2026-05-25.json`). List-only; none can corrupt a ceiling count.

---

## Active Plans Heartbeat (9 plans with status tables)

| Plan | In-flight | Blocked | Paused | Stale rows | Last decision |
|---|---|---|---|---|---|
| `arc_062_rule_apprehension` | 4 | 0 | 0 | 6 | 2026-05-18 |
| `commitment_closure` | 3 | 0 | 0 | 3 | 2026-07-21 |
| `goal_pipeline` | 1 | 2 | 0 | 3 | 2026-06-15 |
| `self_attribution` | 0 | 3 | 0 | 3 | 2026-05-30 |
| `ree_ai_design_critique` | 1 | 0 | 0 | 11 | — (no dated decision log) |
| `sleep_substrate` | 0 | 1 | 0 | 1 | 2026-07-20 |
| `behavioral_diversity_isolation` | 0 | 0 | 0 | 1 | — |
| `infant_substrate` | 0 | 0 | 0 | 0 | 2026-05-21 |
| `e3_fresh_select_migration` | 0 | 0 | 0 | 0 | — |

**PLAN STALING flags** (no decision logged in >14 days AND rows in-flight):

- `arc_062_rule_apprehension` — no decisions since **2026-05-18** (72 days); 4 rows in-flight,
  6 stale. The most staled plan in the set.
- `self_attribution` — no decisions since **2026-05-30** (60 days); all 3 rows blocked on
  "post-substrate-gates", owner TBD.
- `goal_pipeline` — no decisions since **2026-06-15** (44 days); 1 in-flight, 2 blocked.
- `ree_ai_design_critique` — 11 stale rows, 1 in-flight (WS-1), no dated decision log.

**Stale rows with Owner-EXQ status (Step 7c-checked):**

- `goal_pipeline` **GAP-4** (in-progress, last updated 2026-05-29) — 490g / 471a / 475a →
  **owed** (see Queue Status; verify the fork-A Tier-1 gate first); 483c, 524a, 603c → **ran**.
- `goal_pipeline` **GAP-2** (blocked, 2026-05-08) — 514g → **gated** on "Phase 1 PASS".
- `goal_pipeline` **GAP-7** (blocked_pending_substrate, 2026-06-10) — 636, 637, 626b, 640a →
  **all ran**; the row is unreconciled, not owed.
- `commitment_closure` **GAP-1** (in-progress, 2026-05-20) — 598 → **ran**.
- `commitment_closure` **GAP-8** (in-progress, 2026-06-03) — 485b, 485c → **ran**. The row's own
  text still says "audited = NEVER ran", which is now out of date.
- `sleep_substrate` **GAP-2** (upstream-blocked) — the row lists 418c/436a/500a/503a as "STILL
  OUTSTANDING"; **436a, 500a, 503a all ran**, and **418c was superseded by 418d, which ran**. Row
  prose is stale; nothing owed.
- `arc_062` **GAP-D / GAP-H / GAP-K** — 598, 544/545/604/605/603, 546/628 → **all ran**. GAP-I and
  GAP-J owners are literal "TBD" — no id to check.

Net: of ~34 Owner-EXQ ids checked, **3 are genuinely owed** (490g, 471a, 475a), **1 is gated**
(514g), **1 is a phantom** (739), **1 was deliberately refused** (732b), and the rest have run.
Most of the "stale" signal here is **unreconciled plan prose, not undone work** — a docs-reconcile
pass over these six plans would retire most of the staleness without any experiment.

---

## Literature Pull Candidates (3 — the backlog is nearly empty)

| # | Claim | Priority | Next action | Existing entries |
|---|---|---|---|---|
| 1 | `SD-082` | medium | Run targeted literature extraction and claim linkage | 0 |
| 2 | `Q-019` | medium | (none recorded) | 0 |
| 3 | `Q-085` | low | Run paired experiment + literature cycle before status change | 0 |

Only 3 of the 380 backlog items call for literature; none has an existing `targeted_review_*`
directory. SD-082 is also a live experimental claim (822b FAIL, `precondition_unmet`), so the lit
pull and the autopsy would inform each other.

---

## Fleet Git Health

| Machine | Repo | State |
|---|---|---|
| `ree-cloud-1` (hub) | REE_assembly | OK |
| `ree-cloud-1` (hub) | ree-v3 | OK |
| `ree-cloud-2` | — | UNREACHABLE (likely powered off — `hcloud server list` is authority) |
| **`ree-cloud-3`** | **REE_assembly** | **GC-BLOCKED** — `gc.log` present (automatic gc DISABLED) + **11 stash entries** |
| `ree-cloud-3` | ree-v3 | OK |
| `ree-cloud-4` | — | UNREACHABLE (surge worker, manual start) |

**`ree-cloud-3` needs attention and is actively claiming work** (it holds `V3-EXQ-798a`).
11 stash entries may strand evidence — inspect before dropping anything, and establish containment
per `evidence/planning/ree_v3_orphaned_autostash_triage.md` first. Not repaired here: a wedge needs
the preserve-before-reset procedure, and stranded stashes have previously held the only surviving
copy of completed-run evidence.

---

## Stale Claims (2 active > 6h)

- Buckets: **A(auto-closable) 2** | B(vendor-sync) 0 | C(no-trace) 0 | D(dirty-unproven) 0 |
  U(undetermined) 0
- Both are bucket **A `landed_unclosed`** — clean tree, resources moved; `/session-land`
  auto-closes these. No action needed.
  - `igw-auto-igw-192-substrate-ready-mech-217-20260728T221941Z` (6h) — *IGW-20260728-192
    MECH-217 implement-substrate STAGED* — landed `09889e6077`.
    warn: directory-scoped (not attributable) `ree-v3/ree_core/`; high-contention shared file
    (not attributable) `REE_assembly/docs/claims/claims.yaml`.
  - `igw-211-proposal-for-inv-056` (11h) — *IGW-211 INV-056 substrate-readiness* — landed
    `24e51b2efa`.

Healthy steady state — no abandoned or unprovable claims.

---

## Serve.py Status

- **RUNNING** on port 8000 (PID 95553).

---

## Blocked Items

1. **`governance.sh` skipped (Tier 2).** One active non-stale claim
   (`igw-auto-igw-192-substrate-ready-mech-217-20260728T221941Z`, 6h) covers
   `REE_assembly/docs/claims/claims.yaml` — regenerating derived governance artifacts from a
   half-edited `claims.yaml` would commit inconsistent state. The Governance, pending-review and
   audit sections above are from the 2026-07-28T20:22Z run.
2. **`REE_assembly` not pulled.** Local `master` is ahead 3 / behind 5 of `origin/master` with
   1227 dirty files (shared multi-session checkout). Pulling, resetting, or `update-ref`-ing that
   tree is the documented HEAD/worktree-skew and autostash hazard, so it was left alone. The 5
   unadopted commits are 4 phase3 telemetry/result writes plus the nightly `/update-docs` commit;
   the one substantive item is the **V3-EXQ-834 result pack**, read directly from `origin/master`
   for this agenda.
3. **`WORKSPACE_STATE.md` append skipped** — Tier 2 rule (a whole-file read-modify-write would
   adopt live sessions' uncommitted edits).
4. **Queue is empty and the idle-watcher has no refill candidates.** The single most actionable
   item on this page: the fleet has nothing to claim, and the automated refill path is exhausted
   (32 built-SD validations already ran). Needs a human `/queue-experiment` design pass.
