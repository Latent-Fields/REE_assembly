# Morning Agenda — 2026-09-25

Generated: 2026-09-25T04:14:30Z

> **DEGRADED RUN — `governance.sh` was NOT run.** Live sessions at generation time:
> `IGW-20260925-229 MECH-284 MECH-287 implement-substrate STAGED`
> (`igw-auto-igw-229-substrate-ready-staleness-within-20260925T031644Z`, age 0.9h, holds
> `claims.yaml`); `MECH-287 readout: DV decision applied` (`metaworker-science-20260925-orchc-mech287-readout-build-p2`, 1.4h);
> `V3-EXQ-1099 apply B+D, queue` (`metaworker-science-20260925-orchc-contamination-probe-r2`, 1.1h);
> plus the orchestrator claims `orchestrate-20260924-1707` (3.0h), `orchestrate-20260924-breakthrough` (1.0h),
> `orchc0925-comments-2` (1.1h), `orchc0925-mmskew` (0.7h). The Governance Agenda, Experiments Awaiting
> Review, and granularity/category audit sections below reflect the **last** pipeline run, not
> today's state. Re-run `/morning-digest` manually once sessions are clear to refresh them.
>
> In practice the drift is small today. `pending_review.md` was regenerated at 01:08Z by the
> nightly `/update-docs`, and `promotion_demotion_recommendations.md` was regenerated at 04:07Z by
> a lit-pull reindex. Both post-date every run listed below.

---

## Headlines — Positive Results & Live Decisions

Five runs finished since the 2026-09-24 digest: 3 PASS, 2 FAIL. One is a genuine evidence
PASS. The other two PASSes are diagnostics that need a confirmed `/failure-autopsy` before
anything acts on them.

- **V3-EXQ-1085 — `mech365_provenance_gate_boundary_lesion` — PASS** (evidence, `supports`)
  - **Moves:** MECH-365 (candidate), the provenance-bearing one-way commit-status gate.
    This is its **first experimental entry**: exp confidence 0.773, overall 0.759, quadrant now
    `confirmed_established`. All four load-bearing criteria passed on 5/5 seeds, with
    non-degenerate criteria. With the gate intact, imagined content reaching the committed map
    was exactly 0 (C1a), and the committed map was bit-identical with and without imagined
    input (C1b). Lesioning the boundary contaminated imagined-sourced content (C2 = 1.76 vs
    floor 0.05). The sham lesion was inert (C3 = 0).
  - **Makes live / unblocks:** MECH-365 sat in yesterday's governance agenda as
    `hold_pending_v3_substrate` with 0 experimental evidence. That hold premise is now stale:
    the substrate exists and the claim has its first PASS. The next `/governance` cycle should
    re-read MECH-365's disposition with this run in hand. Its phase-locked v4 parent **ARC-085**
    has also dropped out of the CONFLICT list since yesterday (see Governance Agenda).
  - **Gate on acting:** none on the result itself. It is one experiment, so it counts toward the
    promotion threshold rather than crossing it. The S4 selectivity audit is recorded as
    degenerate and was not gated, by design.

- **V3-EXQ-1093 — `mech428_parent_stat_ess_sweep` — PASS** (diagnostic, `non_contributory`, reported under the 723 rule)
  - **Moves:** label `parent_statistic_achievable_range_exists`. A sub-ceiling cell of the
    MECH-428 parent-goal statistic separates on every in-set cell (C1 = 1.0, 15 cells, best
    `a0.025_d0.0_N1600`). ESS orders separation (C3 = 0.96). The 884c default cell also
    separates (0.8), which suggests the 884c at-chance reading was a parameter-range issue.
  - **Makes live / unblocks:** answers `chip-20260917-mech428-parent-goal-alpha-sweep`. It
    gives MECH-428's subgoal-seeding line a parameter range where the parent statistic can carry
    signal, so a consumer experiment can be designed against it. That design would be
    `/queue-experiment` work once the autopsy confirms.
  - **Gate on acting:** needs `/failure-autopsy`. MECH-428 is also the #4 P1 granularity
    recurrence (7 hits / 6 signatures). No `weakened` alignment, so it still reads as
    measurement debt, which is consistent with this finding.

*V3-EXQ-1087 (MECH-321) also returned PASS, but the indexer flagged it `vacuous_pass`. Its
label is `stage2_discriminative_anti_harm_tracking__stage1_clamp_saturated`: C1 passed
(Stage-2 tie rate 0.078, so discriminative) and C2 harm-tracking failed. Stage 1 was clamp-saturated.
It is not a positive result for MECH-321. See below.*

---

## Decisions Waiting on You (1)

## Decisions waiting on you

1 decision(s) recorded as awaiting your answer, oldest first. These do NOT block any session -- they are recorded requests, so nothing is stalled while they sit. Answer any of them in the explorer's Paper view (each has a form there), with the command in its block, or by reopening the asking session.

### MECH-268 -- waiting 33h

**The claim:** dACC conflict saturation: the dACC-analog (SD-032b) prediction-error / conflict signal caps and habituates under repeated identical outcomes; it does not grow unboundedly as conflict persists. Without saturation, a stuck governance loop can generate unbounded pe signal that never triggers a mode change, which is the control-theory signature of persistent rumination. (status `provisional`, mechanism_hypothesis)

**Claim detail:** Mechanism hypothesis. The dACC prediction-error / conflict signal in SD-032b is currently unsaturated. Biological dACC error signals habituate under repeated identical outcomes (Bryden et al 2019); the EVC framework (Shenhav et al 2016) predicts saturation dynamics under sustained demand; repeated-identical-outcome adaptation is a general feature of cortical error coding. ...

**Evidence on record now:** 1 experimental / 8 literature entries; directions: supports 5, weakens 0, mixed 4; runs PASS 1 / FAIL 0; overall confidence 0.75; latest entry `v3_exq_463b_mech268_dacc_conflict_saturation_behavioural_20260604T030903Z_v3`

**Question:** Which calibration route should MECH-268's dACC saturation use so it actually releases the SD-032a mode register? Decide AFTER the closure-cadence successor experiment (chip-20260917-mech268-closure-cadence-dose) has replicated the strength-0.5 effect across seeds.

**Recommendation:** Wait for multi-seed replication at dacc_saturation_strength >= 0.5, then choose; do not change the fleet-wide default on one seed (user decision 2026-09-23, GFLAG-0330).

**Context:** MECH-268 says the dACC conflict signal saturates so a stuck governance loop does not run away. The saturation factor f_sat only affects behaviour through its FLOOR, and at today's default strength 0.3 the floor (0.357) sits just above what the mode register needs (~0.275). Single-seed trained-agent measurement: the saturation changes argmax(operating_mode) on 7/195 ticks at 0.3 vs 151/195 at 0.5. The mismatch exists because dacc_pe's scale drifts with training (~1 untrained, ~3.6 after warmup, ~16 on the 464d/467d config) while the floor is a fixed function of (strength, window, grace). Source: docs/architecture/mech_268_dacc_saturation_form.md (REE_assembly 588c844333e + c12a11eafb9).

**Options** (or answer in your own words):

1. Raise the production default dacc_saturation_strength to 0.5 (cheapest; changes every run using the default, so needs a regression check on runs that relied on 0.3).
2. Leave the default at 0.3 and normalise dacc_pe instead, fixing the scale drift at its source (needs a design and a substrate_queue entry).
3. Make the f_sat floor track external_task_bias dynamically (most principled, least specified, most build).

**What answering does:** Your answer is appended to `evidence/decisions/decision_log.v1.jsonl` as `approved` (or `rejected`/`withdrawn`), committed and pushed. It does NOT edit claims.yaml or any plan by itself: session `governance-flags-20260923b` applies it when resumed, otherwise the next `/governance` cycle does. Until then it is listed under 'Answered -- awaiting application'.

**Read more:** `REE_assembly/evidence/planning/sd033_governance_plan.md`

- decision_id: `dec-20260923T185804-MECH-268`
- asked by: `dgolden` (session `governance-flags-20260923b`)
- status: `proposed`

**Answer it here** (records your decision; the asking session picks it up on resume):

```bash
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/pending_decisions.py resolve \
  --decision-id dec-20260923T185804-MECH-268 \
  --selected-option '<your answer>' \
  --rationale '<why, one line -- optional but worth it>'
```

**Or reopen the session that asked:**

```bash
# session 'governance-flags-20260923b' not in the worktree registry (ended, or a non-Mac box)
/opt/local/bin/python3 /Users/dgolden/REE_Working/scripts/sync_worktree_session_registry.py --why
```

---

**Context for the MECH-268 decision above:** the successor experiment it waits on has now
run. **V3-EXQ-1089** (`mech268_closure_cadence_mode_register`, from
`chip-20260917-mech268-closure-cadence-dose`) returned **FAIL, `substrate_not_ready_requeue`**.
Only **2 of 4** intended seeds met readiness, and none of C1-C3 cleared its effect-size bar (C1
reset-bracket delta 0.088 vs 0.176; per-seed 0.176 / 0.0). So the multi-seed replication at
strength 0.5 that the recommendation says to wait for **has not happened yet**. That is a
reason the decision stays open, not an answer to it. Whether 1089 gets a re-queue under a new
letter is `/failure-autopsy` work.

## Queue Status

- **Total pending: 0** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0). 2 claimed.
- **ALERT: QUEUE EMPTY (threshold 3), for the third morning running.** The refill chip
  `chip-20260923-queue-refill-empty` is still `open` and **unclaimed**, two days after it was
  spawned. No new chip was spawned; that chip is still the one to click. One live session
  (`metaworker-science-20260925-orchc-contamination-probe-r2`) is preparing **V3-EXQ-1099** for
  the queue, so at most one item is about to land.
- **Running:** `V3-EXQ-1090` (MECH-449 endogenous safety-veto producer validation) on
  **ree-cloud-2**, claimed 2026-09-24T17:26:05Z (~11h).
- **Still stranded:** `V3-EXQ-1067` (MECH-266/SD-032a squash-vs-clamp) has been claimed by
  **DLAPTOP** since 2026-09-20T02:07:22Z, **about 5 days**. The Mac runner is deliberately off,
  so this claim has no executor. Releasing it is an operator decision (third digest to report it).
- **Fleet-idle watcher** (snapshot `2026-09-25T03:21:35Z`, `status: OK`): `idle_risk=true`,
  claimable backlog **0** (threshold 3). The one ready-SD validation candidate is still
  **SD-106 → V3-EXQ-1023** (leverage 6). Exclusions: 40 already ran, 50 have no queueable
  validation (46 yesterday), 4 known-churn. Past SD-106, refilling needs a fresh
  `/queue-experiment` design, not a re-queue.
- **Owed successors: none.** All four plan `owner_exq` ids (V3-EXQ-1047, 445h, 910b, 938)
  have landed manifests, so they ran (Step 7c check (b)). No phantoms, and no
  declared-never-minted ids.

---

## Experiments Awaiting Review (5 indexed / 0 runner-only)

`pending_review.md` (generated 2026-09-25T01:08:12Z): 5 items, 3 PASS and 2 FAIL. Yesterday's
six diagnostics have all cleared. **1087 and 1093 are diagnostics with no confirmed autopsy.**
1087 is additionally flagged `vacuous_pass`. None of the five carries a `supersedes` field, and
none of their EXQ ids is in the queue.

### V3-EXQ-1085 — mech365_provenance_gate_boundary_lesion — PASS
- **Claims tested:** MECH-365 (candidate; now 1 exp / 2 lit; exp 0.773, overall 0.759)
- **Key metrics:** C1a imagined-to-committed leakage 0.0 (5/5 seeds); C1b committed-map diff 0.0; C2 boundary-lesion contamination 1.76 (floor 0.05); C3 sham 0.0
- **Classification:** evidence
- **Governance impact if confirmed:** first experimental support for MECH-365. It undercuts yesterday's `hold_pending_v3_substrate` premise, and moves the claim toward the promotion threshold

### V3-EXQ-1093 — mech428_parent_stat_ess_sweep — PASS
- **Claims tested:** MECH-428 (candidate; 0 exp / 3 lit; lit 0.737)
- **Key metrics:** C1 sub-ceiling separation 1.0 over 15 cells; C2 884c default cell 0.8; C3 ESS-orders-separation 0.96; sense path equals act path (PR0 diff 0.0)
- **Classification:** diagnostic
- **Governance impact if confirmed:** scores nothing (`non_contributory`). It establishes that the parent statistic has an achievable operating range, so the 884c null was about parameters, not a ceiling

### V3-EXQ-1087 — mech321_perleaf_harm_discriminability — PASS (`vacuous_pass`)
- **Claims tested:** MECH-321 (candidate; 2 exp / 14 lit; exp 0.277, overall 0.593; 2 FAIL runs)
- **Key metrics:** probe non-perturbing (0 differing actions); C1 Stage-2 tie rate 0.078 over 243 calls (discriminative, ≤ 0.20); C2 harm tracking FAILED (anti-tracking); Stage 1 clamp-saturated
- **Classification:** diagnostic
- **Governance impact if confirmed:** Stage 2 discriminates, but it does not track harm in the intended direction. Per the run's combination rule, this bears on whether V3-EXQ-919's MECH-321 reading stays conditional. It must be adjudicated before it moves anything

### V3-EXQ-1083 — sd081_adaptive_vs_fixed_allocation — FAIL
- **Claims tested:** SD-081 (candidate; 0 exp / 1 lit; lit 0.698)
- **Key metrics:** C1 allocation tracks model uncertainty 0.131 (thr 0.02, 7 seeds +) PASS; C2 committed recruitment 0.139 PASS; C4 reach beyond shuffled 0.140 PASS; **C3 benefit over fixed 0.0 (no scored cells), degenerate**; C4-benefit degenerate
- **Classification:** evidence (outcome `non_contributory`, label `reach_confirmed_benefit_untestable`)
- **Governance impact if confirmed:** the arbitration mechanism is live: allocation tracks uncertainty and recruits planning beyond fixed and shuffled controls. The *benefit* criterion had no scorable cells, so the payoff half is untested. Needs `/failure-autopsy`, not a demotion

### V3-EXQ-1089 — mech268_closure_cadence_mode_register — FAIL
- **Claims tested:** MECH-268 (provisional; 1 exp / 8 lit; overall 0.754)
- **Key metrics:** ready seeds 2/4 (precondition unmet); C1 0.088 vs 0.176; C2 0.070 vs 0.140; C3 0.119 vs 0.239
- **Classification:** evidence (outcome `non_contributory`, label `substrate_not_ready_requeue`)
- **Governance impact if confirmed:** none on MECH-268's standing. The run could not test the closure-cadence dose. It is the run the pending MECH-268 decision waits on (see above)

---

## Errors to Diagnose (0)

- Fleet ERROR rate: **1.5%** (2/135) over 30 days (coordinator DB). 0 unexplained phantoms,
  0 operator cancellations, and no new ERROR rows since yesterday.

---

## Governance Agenda (10 recommendations)

From `promotion_demotion_recommendations.md` (regenerated 2026-09-25T04:07:00Z by a lit-pull
reindex, not by `governance.sh`). 10 items are `pending_user`:

- **SD-050** (provisional) — **Demotion review: provisional → candidate** (`demote_to_candidate`).
  This is the one item with status consequences. Note that `IGW-20260924-224` (SD-050 / MECH-302
  implement-substrate) is staged and has not run (see Stale Claims).
- **MECH-479** (candidate) — `hold_candidate_resolve_conflict` (literature conflict; stays gated pending an upstream probe or substrate)
- **Eight `hold_pending_v3_substrate` holds:** ARC-109, ARC-111, ARC-139, ARC-144,
  GOV-CONTRACT-3, MECH-308, MECH-452, MECH-585. Recording these is routine `/governance`
  bookkeeping, and it stops them re-flagging.
- **MECH-365** was one of yesterday's four holds. It is recorded as applied now, but V3-EXQ-1085
  above gives it its first PASS. Worth revisiting with the new evidence.

**Granularity-debt recurrence (GOV-GRAN-1):** P0 `dropped_handoff` = **0**. P1
`unflagged_recurrence` = **54** (unchanged) across 230 claims with hits (222 yesterday). The
top of the list is unchanged, and **none of the top eight carries a `weakened` alignment**:
- **INV-050** — 13 hits / 9 sigs — unclear=8 intact=4 n/a=1: no weakened, likely measurement debt
- **MECH-180** — 12 hits / 8 sigs — unclear=8 intact=2 other=1 n/a=1: no weakened
- **SD-082** — 9 hits / 6 sigs — unclear=9: no weakened
- **MECH-428** — 7 hits / 6 sigs — other=3 unclear=3 intact=1: no weakened (consistent with V3-EXQ-1093 above)
- **SD-078** — 7 hits / 6 sigs — unclear=7: no weakened

The six `weakened`-leaning claims from yesterday (Q-034, ARC-038, SD-005, INV-054, MECH-111,
ARC-018) remain the discrimination candidates. List only, no chips.

**Epistemic-category completeness (GOV-CAT-1):** **clean (10 legacy-schema warns).**
`missing_category` 0, `invalid_category` 0, `malformed_markers` 0. P1: 10 `unkeyed_schema`,
2 `claimless_missing`. The baseline holds 208 artifacts and 674 excluded invalids.

**V3-necessity phase leaks:** 1 ROOT / 1 CONFLICT / 0 stale provenance, down from 5 / 2 / 0.
**None new**, and 4 roots have cleared.
- **Cleared ROOT:** ARC-053, ARC-085, INV-099, MECH-225 (CONFLICT cleared: ARC-085, the
  `phase_locked` parent of MECH-365)
- **Remaining ROOT:** MECH-510 (v4, RECLASSIFY) ← 1 V3 dependent (MECH-586). Yesterday it was
  needed by MECH-512. The dependent has changed, so the cascade has moved on by one level
- **Remaining CONFLICT:** MECH-095 (v5, cascade, `phase_locked`). Only a human can resolve it
- Walked by `/governance` Step 3; not adjudicated here.

---

## Active Plans Heartbeat (18 plans with closure frontmatter)

No change from yesterday. Weighted progress is **72.3%** across 98 non-deferred nodes, with
**34** remaining, 64 done, 10 deferred, and 11 on the assembly frontier (exempt). Status
tally: assembling=11, blocked=13, blocked_pending_substrate=3, in_progress=9, open=4,
partial=3, upstream_blocked=2. **13 of 18 plans are non-done.** `closure_drift.md`
(2026-09-24T10:27Z): **0 drifted**, **1 stale-since-update**:
`behavioral_diversity_isolation:GAP-I` (in-progress, last updated 2026-09-16). The
`failure_autopsy_V3-EXQ-1012c_2026-09-24` autopsy reclassified MECH-439 after that date, so the
node needs its frontmatter reconciled.

| Plan | In-flight | Blocked | Assembling | Progress | Last updated |
|---|---|---|---|---|---|
| conversion_ceiling_campaign | 0 | 0 | 7 | 0% | 2026-07-10 |
| global_workspace_jlens | 2 (open) | 2 | 0 | 5% | 2026-09-08 |
| policy_decomposition_trigger | 0 | 1 | 0 | 10% | 2026-08-21 |
| zworld_adequacy | 0 | 1 (upstream) | 1 | 10% | 2026-09-21 |
| sd_037_axis_b_sustained_threat_curriculum | 0 | 3 | 1 | 10% | 2026-06-23 |
| self_attribution | 0 | 4 | 0 | 28% | 2026-09-04 |
| orienting_epistemic_deficit_v3 | 2 + 2 open | 1 | 0 | 32% | 2026-09-17 |
| mech357_avoidance_efficacy | 1 (partial) | 0 | 0 | 50% | 2026-08-29 |
| arc_062_rule_apprehension | 2 + 1 partial | 1 + 2 substrate | 0 | 56% | 2026-09-01 |
| behavioral_diversity_isolation | 2 + 1 partial | 1 | 1 | 71% | 2026-09-16 |
| commitment_closure | 2 | 0 | 1 | 88% | 2026-09-16 |
| sleep_substrate | 0 | 1 (upstream) | 0 | 91% | 2026-08-14 |
| infant_substrate | 1 | 1 (substrate) | 0 | 91% | 2026-09-16 |
| arc_005_control_plane_routing | — | — | — | 100% | 2026-08-13 |
| goal_pipeline | — | — | — | 100% | 2026-06-15 |
| mech303_safety_threshold | — | — | — | 100% | 2026-08-16 |
| sd033_governance | — | — | — | 100% | 2026-05-29 |
| sd_037_axis_a_consumer_input_recalibration | — | — | — | 100% | 2026-06-16 |

**Owner-EXQ status (Step 7c):** V3-EXQ-1047 (ORNT-2), 445h (self_attribution:GAP-1), 910b
(ORNT-6) and 938 (policy_decomposition_trigger) all have manifests. They **ran**, and none is
owed. **Link to today's results:** V3-EXQ-1087 (MECH-321) bears on
`policy_decomposition_trigger` (ARC-070 / MECH-321). It moves nothing until it is autopsied.

---

## Literature Pull Candidates (Top 5)

439 backlog items need literature (457 yesterday): 431 `medium`, 8 `low`, none `high`. So this
is the head of the list, not a ranking. ARC-109 and ARC-111 have left the head since yesterday.

| # | Claim | Priority | Existing entries |
|---|---|---|---|
| 1 | ARC-114 | medium | 0 |
| 2 | ARC-115 | medium | 0 |
| 3 | ARC-116 | medium | 0 |
| 4 | ARC-117 | medium | 0 |
| 5 | ARC-118 | medium | 0 |

(Coverage was checked against `claim_ids_tested` in each `record.json`, not by directory-name
globbing.)

---

## Fleet Git Health

- `DLAPTOP-4` (local) — REE_assembly OK, ree-v3 OK (5 `--dry-run` smoke manifests present; they self-clear)
- `ree-cloud-1` (hub) — REE_assembly OK, ree-v3 OK
- `ree-cloud-2` (worker) — REE_assembly OK, ree-v3 OK (running V3-EXQ-1090)
- `ree-cloud-3` (worker) — UNREACHABLE (ssh timeout; probably powered off, which is not a
  fault). **Second day the 2026-09-23 wedge repair could not be re-verified.** Check it the next
  time the box is powered on.
- `ree-cloud-4` (worker) — REE_assembly OK, ree-v3 OK

64 untracked paths were graded against origin: 0 stranded run manifests and 0 stranded
literature entries.

---

## Stale Claims (5 active > 6h)

- Buckets: A 0 | B 0 | **C 1** | D 0 | **U 1** | **S(staged-never-ran) 3**
- **[S]** `igw-auto-igw-224-substrate-ready-suffering-deriva-20260924T133548Z` (14.6h) — *IGW-20260924-224 SD-050 MECH-302 implement-substrate STAGED*. Staged, never ran. This is relevant to the SD-050 demotion review above.
- **[S]** `igw-auto-igw-222-substrate-ready-sd032b-candidate-20260923T195937Z` (32.2h) — *IGW-20260923-222 SD-032b implement-substrate STAGED*. Staged, never ran.
- **[S]** `igw-auto-igw-219-substrate-ready-sd105-frozen-sha-20260923T185150Z` (33.4h) — *IGW-20260923-219 SD-105 MECH-063 implement-substrate STAGED*. Staged, never ran.
  - warn (all three S): directory-scoped `ree-v3/ree_core/`; shared file `REE_assembly/docs/claims/claims.yaml`
- **[U]** `metaworker-science-20260924-arc021-h2-merged-leg-a` (14.2h) — *ARC-021 H2 merged leg queue* — directory-scoped `ree-v3/experiments/`, `ree-v3/experiments/_scratch/`
  - warn: shared/directory resource is dirty, likely another live session: `ree-v3/experiments/`
- **[C]** `metaworker-science-20260924-orchb-inv063-1071-defects-c4-doc` (14.2h) — *V3-EXQ-1071 fix addendum note* — nothing landed, nothing dirty (abandoned OR wrong-direction — not distinguishable here). The claim lists no resources.

---

## Serve.py Status

- **RUNNING** on port 8000 (PID 42900)

---

## Blocked Items

- **Tier 2 degraded run.** `governance.sh` was skipped because
  `igw-auto-igw-229-substrate-ready-staleness-within-20260925T031644Z` holds a live claim on
  `claims.yaml`. As a result, this digest cannot confirm that yesterday's Step 4b
  backward-traceability failure (ARC-083 / DEV-NEED-021) is fixed. Its chip,
  `chip-20260924-arc083-devneed-register`, is marked `done`. The next full pipeline run will
  show whether Steps 5-7 run again.
- **Queue empty, third day.** See Queue Status. The refill chip is unclaimed.
- **V3-EXQ-1067 stranded on DLAPTOP for ~5 days.** Operator decision.
