# Morning Agenda — 2026-09-24

Generated: 2026-09-24T05:16:27Z

*Tier 1 full run. No live claims when this run started, so `governance.sh` ran. It **stopped
at Step 4b** (the backward-traceability gate, exit 1), so Steps 5-7 did not run: the
claim-dependency dashboard data, the contributor ledger, and the `governance_agenda.v1.json`
timestamps. Everything this agenda reads was produced before 4b and is current:
`pending_review.md`, `promotion_demotion_recommendations.md`, `closure_status.md`, and
`claims.json`. See Blocked Items.*

---

## Headlines — Positive Results & Live Decisions

Six diagnostics finished overnight: 4 PASS, 2 FAIL. **None of them has a confirmed
`/failure-autopsy` yet**, so every reading below is the run's own self-route. Treat each one
as a hypothesis until it is adjudicated.

- **V3-EXQ-1080 — `contamination_truncation_prevalence_probe` — PASS** (decision-flipping
  diagnostic, `non_contributory`, reported here under the 723 rule)
  - **Moves:** label `contamination_truncation_present_verdicts_robust_no_reruns_owed`.
    Contamination truncation is real: a random walker on the 669c nursery died of it in 100% of
    episodes at stock settings and in 0% with the gate on. But it **did not change any
    verdict**. On 669c, 939a, 904 and 888, the stock-vs-opt-out verdict matched and the stock
    death fraction stayed below the material threshold.
  - **Makes live / unblocks:** **no re-runs are owed** for the 7 directly measured claims:
    ARC-070, MECH-074, MECH-074a, MECH-074b, MECH-189, MECH-303, MECH-329. This closes a
    re-run backlog before anyone starts it.
  - **Gate on acting:** the caveat still stands for **MECH-074d, SD-077 and SD-079**
    (family claims, not cleared). Three claims were not covered at all, each needing its own
    env: MECH-106 (231a), INV-054 (278/435), MECH-427 (883). Needs `/failure-autopsy` before
    `/governance` uses it.

- **V3-EXQ-1012c — `e3_commensurability_eligibility_stage_validation` — PASS** (diagnostic,
  `non_contributory`, MECH-439)
  - **Moves:** label `commensurate_at_eligibility_both_regimes`. At the eligibility stage, the
    E3 channels are commensurate with the operator fed and with it starved. Preconditions were
    met: 201 genuine P1 selections (floor 60), the operator engaged, and the clamp config
    landed.
  - **Makes live / unblocks:** bears on `behavioral_diversity_isolation:GAP-I` (the MECH-439
    F-dominance node, in_progress, load-bearing). If commensurability holds at eligibility,
    the F-monopoly is not an eligibility-stage scale artefact. That points the next MECH-439
    probe downstream of eligibility.
  - **Gate on acting:** the run's own `prior_note` says PASS is the **expected** reading under
    Gaussian or sparse-HIGH channel shapes. It would fail only for sparse-LOW shapes, for
    r >= 3, or for a channel at 5x or more of its EMA. Read R against the recorded shape
    quantiles before treating this as informative. MECH-439 has no experimental evidence yet
    (0 exp / 7 lit, confidence 0.796). Needs autopsy.

- **V3-EXQ-1081 — `sdppb1_world_forward_ranking_reach_probe` — PASS** (diagnostic,
  `non_contributory`, **indexer flag `precondition_unmet`**)
  - **Moves:** label `sleep_head_change_reaches_e3_ranking__rollout_yes__curiosity_undetermined`.
    C1 passed: a sleep-induced head change reaches the E3 ranking on all 3 ready seeds. C2
    passed: it reaches through the rollout route.
  - **Makes live / unblocks:** SD-PP-B1's canonical-consumer question. The world-forward
    change does reach action selection through rollout.
  - **Gate on acting:** the curiosity-route positive control failed on all 3 seeds, so C3 is
    undetermined. That is what raised the flag. **Also, C6 passed:** a norm-matched *random*
    direction also reaches the ranking (3/3). "Reaches" may therefore be generic
    sensitivity, not something specific to sleep. The autopsy should settle this before
    anything is built on it.

*V3-EXQ-1078 (INV-069) also returned PASS, but the indexer flagged it `vacuous_pass`: none of
its three criteria was non-degenerate, and its label reads `inv069_undetermined`. It is not a
positive result. See below.*

---

## Decisions Waiting on You (1)

## Decisions waiting on you

1 decision(s) recorded as awaiting your answer, oldest first. These do NOT block any session -- they are recorded requests, so nothing is stalled while they sit. Answer any of them in the explorer's Paper view (each has a form there), with the command in its block, or by reopening the asking session.

### MECH-268 -- waiting 10h

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

## Queue Status

- **Total pending: 0** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0). 1 claimed.
- **ALERT: QUEUE EMPTY (threshold 3), for the second morning running.** The refill chip from
  yesterday, `chip-20260923-queue-refill-empty`, is still `open` and **unclaimed**. No new chip
  has been spawned; that chip is the one to click. The 2026-09-18 refill chip went five days
  unactioned too. The recurring failure is that nobody claims the refill chip, not that the
  digest misses the empty queue.
- **The one claimed item looks stranded:** `V3-EXQ-1067` is claimed by **DLAPTOP** and has
  been since 2026-09-20T02:07:22Z (**about 4 days**). The Mac runner is deliberately off, so
  this claim has no executor. It sits under the coordinator's 6h stale floor only because
  recovery keys on telemetry absence. Releasing it is an operator decision.
- **Fleet-idle watcher** (snapshot `2026-09-24T04:18:05Z`, `status: OK`): `idle_risk=true`,
  claimable backlog **0** (threshold 3). The one ready-SD validation candidate is still
  **SD-106 → V3-EXQ-1023** (leverage 6; it unblocks SD-015, ARC-030, MECH-117, MECH-457,
  ARC-065 and the EXQ-085h..o goal-directed cluster). Exclusions: 40 already ran, 46 have no
  queueable validation, 4 known-churn. Past SD-106, refilling needs a fresh
  `/queue-experiment` design, not a re-queue.
- **Owed successors: none.** All four plan `owner_exq` ids (V3-EXQ-1047, 445h, 910b, 938)
  have landed manifests, so they ran (Step 7c check (b)). No phantoms, and no
  declared-never-minted ids.

---

## Experiments Awaiting Review (6 indexed / 0 runner-only, + 1 ERROR manifest)

`pending_review.md` (generated 2026-09-24T05:10:22Z): 7 items. **All 6 indexed runs are
`experiment_purpose: diagnostic` with no confirmed autopsy.** Each needs `/failure-autopsy`
before `/governance` can mark it reviewed. 1078 and 1081 are additionally flagged
untrustworthy by the indexer.

### V3-EXQ-1080 — contamination_truncation_prevalence_probe — PASS
- **Claims tested:** none tagged (measures ARC-070, MECH-074/074a/074b, MECH-189, MECH-303, MECH-329 indirectly)
- **Key metrics:** stock death fraction 1.0 vs gated 0.0 (control); verdict unchanged stock-vs-opt-out on 669c / 939a / 904 / 888
- **Classification:** diagnostic
- **Governance impact if confirmed:** no re-runs owed for 7 claims; the caveat stays on MECH-074d / SD-077 / SD-079

### V3-EXQ-1012c — e3_commensurability_eligibility_stage_validation — PASS
- **Claims tested:** MECH-439 (candidate; 0 exp / 7 lit; lit confidence 0.796; 5 mixed / 2 supports)
- **Key metrics:** 201 genuine P1 selections (floor 60); operator engaged 1.0; both regimes commensurate
- **Classification:** diagnostic
- **Governance impact if confirmed:** would localise MECH-439's F-dominance downstream of the eligibility stage; scores nothing either way (`non_contributory`)
- **Supersedes:** lineage 1012 → 1012c (no `supersedes` field in the queue; the queue is empty)

### V3-EXQ-1081 — sdppb1_world_forward_ranking_reach_probe — PASS (`precondition_unmet`)
- **Claims tested:** none tagged (SD-PP-B1)
- **Key metrics:** C1 3/3 ready seeds; C2 rollout 2/2 bar passed; C3 curiosity undetermined (positive control failed 3/3); C6 noise-matched random direction also reaches (3/3)
- **Classification:** diagnostic
- **Governance impact if confirmed:** a sleep-head change reaches the E3 ranking through rollout; specificity is open (C6)

### V3-EXQ-1078 — inv069_zself_coherence_unsettled — PASS (`vacuous_pass`)
- **Claims tested:** INV-069 (candidate; no experimental evidence on record)
- **Key metrics:** recurrence live (0.865, floor 0.001). All three criteria degenerate (A1, A2, B). Arm (b) was scoped out: its DV is fixed by the manipulation, in closed form
- **Classification:** diagnostic
- **Governance impact if confirmed:** none. Its own label is `inv069_undetermined`, with arm (b) `non_contributory`. This is the INV-069 arm-(b) degeneracy the done chip `chip-20260923-inv069-armb-degenerate` already routed

### V3-EXQ-1077 — sdppb9_harm_head_undertrain_probe — FAIL
- **Claims tested:** none tagged (SD-PP-B9 / the MECH-055 harm-head line)
- **Key metrics:** C1 converged-head-ready 0/2; label `active_error_removed_AMBIGUOUS`. On 3 eligible seeds the converged head was `cannot_determine`, aliased across under-training, representation ceiling and PE source
- **Classification:** diagnostic
- **Governance impact if confirmed:** the under-training hypothesis for the MECH-055 harm head is **neither confirmed nor refuted**. The run explicitly says this is not a ceiling verdict. A third MECH-055 run has now failed to decide

### V3-EXQ-1082 — sdppb5_alpha09_live_battery_revalidation — FAIL
- **Claims tested:** none tagged (SD-PP-B5)
- **Key metrics:** C1 0/2; C3 "lift excluded on every rung" 3/2 → FAIL-a, label `margin_lowers_action_read`. At alpha_world=0.9 on a live 512-row battery, the margin *lowers* the action read
- **Classification:** diagnostic
- **Governance impact if confirmed:** backs the 2026-09-23 governance ruling that SD-PP-B5 does not validate (1075 autopsy), now at alpha_world ≥ 0.9 and on a live-agent battery. This answers the `chip-20260923-sdppb5-revalidate-alpha09` question. SD-PP-B5 does not recover at the SD-008 stable floor
- **Supersedes:** revalidates V3-EXQ-1075 under a corrected alpha_world and a live battery

---

## Errors to Diagnose (0 new)

- **V3-EXQ-1066** (`arc029_commitment_mode_harm_variance_bar`, ERROR, ree-cloud-3) is still in
  `pending_review`, but it **has been diagnosed** and deliberately not re-queued. It stays
  listed only because `/diagnose-errors` Step 11 has no "no successor owed" terminal branch.
  That gap is already chipped (`chip-20260923-diagnose-errors-no-successor-terminal`, open).
  No new action.
- Fleet ERROR rate: **1.5%** (2/134) over 30 days, 0 unexplained phantoms, 0 operator
  cancellations.

---

## Governance Agenda (4 recommendations)

From `promotion_demotion_recommendations.md` (regenerated 2026-09-24T05:09:57Z). All four are
**`hold_pending_v3_substrate`** on `candidate` claims, and all four are **new**:

- **ARC-084** (candidate) — Hold — 0 exp / 4 lit (3 supports, 1 mixed); lit confidence 0.767
- **ARC-139** (candidate) — Hold — 0 exp / 7 lit (3 supports, 3 mixed, 1 unknown); lit confidence 0.746
- **MECH-147** (candidate) — Hold — 0 exp / 3 lit (3 supports); lit confidence 0.807
- **MECH-365** (candidate) — Hold — 0 exp / 2 lit (2 supports); lit confidence 0.752

**Why these four appeared:** all four were **V3-necessity ROOT leaks in yesterday's digest**,
and all four have now **cleared** as leaks (see below). They were relabelled v4 → v3, and a
v3 claim with no substrate lands in the hold queue. Recording the four holds is routine
`/governance` bookkeeping, and it stops them re-flagging. Yesterday's 16 holds have all been
applied.

**Granularity-debt recurrence (GOV-GRAN-1):** P0 `dropped_handoff` = **0**. P1
`unflagged_recurrence` = **54** (53 yesterday) across 222 claims with hits. Only **6** carry
any `weakened` alignment and lean toward granularity debt. The set is unchanged:
- **Q-034** — 6 hits / 2 sigs — other=3 **weakened=3**
- **ARC-038** — 3 hits / 1 sig — **weakened=3**
- **SD-005** — 3 hits / 1 sig — **weakened=3**
- **INV-054** — 4 hits / 2 sigs — other=2 **weakened=2**
- **MECH-111** — 5 hits / 3 sigs — other=4 **weakened=1**
- **ARC-018** — 2 hits / 2 sigs — unclear=1 **weakened=1**

The other 48 have no `weakened` reading. They look like measurement or implementation debt.
List-only, no chips.

**Epistemic-category completeness (GOV-CAT-1):** **clean.** `missing_category` 0,
`invalid_category` 0, `malformed_markers` 0. P1 only: 10 `unkeyed_schema` and 2
`claimless_missing`. The baseline holds 208 artifacts and 674 excluded invalids.

**V3-necessity phase leaks:** 5 ROOT / 2 CONFLICT / 0 stale provenance, down from 18 / 5 / 0.
18 cleared and 5 are new.
- **Cleared:** ARC-084, ARC-092, ARC-125, ARC-139, INV-098, MECH-147, MECH-228, MECH-278,
  MECH-359, MECH-363, MECH-365, MECH-499, MECH-500, MECH-507, MECH-508, MECH-512, Q-077, Q-104
  (CONFLICT cleared: ARC-092, MECH-278, MECH-359)
- **NEW** ARC-053 (v4, RECLASSIFY) — needed by V3 MECH-228
- **NEW** MECH-225 (v4, RECLASSIFY) — needed by V3 MECH-228
- **NEW** INV-099 (v4, RECLASSIFY) — needed by V3 ARC-125
- **NEW** MECH-510 (v4, RECLASSIFY) — needed by V3 MECH-512
- **NEW** ARC-085 (v4, **CONFLICT**, `phase_locked`) — needed by V3 MECH-365; only a human can resolve this one
- These look like a **cascade**, not fresh leaks. Each new root is the v4 parent of a claim
  that was relabelled v3 yesterday (MECH-228, ARC-125, MECH-512, MECH-365). Relabelling a
  child moves the leak up one level, so each relabel hands the next level to `/governance`.
- `/governance` Step 3 walks these; they are not adjudicated here.

---

## Active Plans Heartbeat (18 plans with closure frontmatter)

No change from yesterday. Weighted progress is **72.3%** across 98 non-deferred nodes, with
**34** remaining, 64 done, 10 deferred, and 11 on the assembly frontier (exempt). Status
tally: assembling=11, blocked=13, blocked_pending_substrate=3, in_progress=9, open=4,
partial=3, upstream_blocked=2. `check_closure_drift.py` finds **0 drifted and 0 stale** rows.
4 are suppressed as legitimately non-terminal.

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

**13 of 18 plans are non-done.**

**Owner-EXQ status (Step 7c):** V3-EXQ-1047 (ORNT-2), 445h (self_attribution:GAP-1), 910b
(ORNT-6, confirmed-autopsied) and 938 (policy_decomposition_trigger:REPOSE) all have
manifests, so they **ran**, and none of them is owed. Several rows carry `owner_exq: TBD`.
That is a bookkeeping gap, not an unqueued run.

**Link to today's results:** V3-EXQ-1012c bears on `behavioral_diversity_isolation:GAP-I`
(MECH-439), and V3-EXQ-1080 relieves the re-run pressure on ARC-070 behind
`policy_decomposition_trigger:REPOSE`. Neither node moves until `/failure-autopsy` +
`/governance` act.

---

## Literature Pull Candidates (Top 5)

457 backlog items need literature: 449 `medium`, 8 `low`, and none `high`. So this is the
head of the list, not a ranking. ARC-103 and ARC-105 have left the head since yesterday.

| # | Claim | Priority | Existing entries |
|---|---|---|---|
| 1 | ARC-109 | medium | 0 |
| 2 | ARC-111 | medium | 0 |
| 3 | ARC-114 | medium | 0 |
| 4 | ARC-115 | medium | 0 |
| 5 | ARC-116 | medium | 0 |

(Coverage was checked against `claim_ids_tested` in each `record.json`, not by directory-name
globbing.)

---

## Fleet Git Health

- `DLAPTOP-4` (local) — REE_assembly OK, ree-v3 OK (5 `--dry-run` smoke manifests present; they self-clear and are not evidence)
- `ree-cloud-1` (hub) — REE_assembly OK, ree-v3 OK
- `ree-cloud-2` (worker) — UNREACHABLE (ssh timeout; probably powered off, which is not a fault). It produced V3-EXQ-1082 at 04:50Z, so it was up recently
- `ree-cloud-3` (worker) — UNREACHABLE (ssh timeout). Yesterday's REE_assembly wedge on this box
  was repaired (`chip-20260923-cloud3-wedge-repair`, done). **Repair not re-verified today**
  because the box is off. Check it the next time it is powered on.
- `ree-cloud-4` (worker) — REE_assembly OK, ree-v3 OK

63 untracked paths were graded against origin: 0 stranded run manifests and 0 stranded
literature entries.

---

## Stale Claims (2 active > 6h)

- Buckets: A 0 | B 0 | C 0 | D 0 | U 0 | **S(staged-never-ran) 2**
- **[S]** `igw-auto-igw-222-substrate-ready-sd032b-candidate-20260923T195937Z` (9.2h) —
  *IGW-20260923-222 SD-032b implement-substrate STAGED*. Staged, never ran.
  - warn: directory-scoped `ree-v3/ree_core/`; shared file `REE_assembly/docs/claims/claims.yaml`
- **[S]** `igw-auto-igw-219-substrate-ready-sd105-frozen-sha-20260923T185150Z` (10.4h) —
  *IGW-20260923-219 SD-105 MECH-063 implement-substrate STAGED*. Staged, never ran.
  - warn: same two

Yesterday's two MECH-572 staged claims (IGW-216, IGW-228) and both no-trace claims have
cleared. Note that SD-032b is the dACC-analog that the pending **MECH-268** decision is about.

---

## Serve.py Status

- **RUNNING** on port 8000 (PID 42900)

---

## Blocked Items

- **`governance.sh` exited 1 at Step 4b (backward-traceability gate G2).** ARC-083 is now
  flagged developmental but is not referenced in
  `docs/architecture/developmental_needs_register.md`. The cause is yesterday's ARC-083
  rewording: "REQUIRES" became "TYPICALLY DEVELOPS AFTER" (commit `9606fb86fe`, GFLAG-0309), and
  the ARC-150 follow-on landed in `20792df26dc`. DEV-NEED-021 ("Otherness inference after
  self-stability") is the natural row. Steps 5-7 (process dashboard, contributor ledger,
  `governance_agenda.v1.json` timestamps) did not run and will not run until this is fixed.
  **Chip spawned** (`chip-20260924-arc083-devneed-register`). It overlaps the open
  `chip-20260923-devneed021-weaken-requires`, which edits the same row.
- **Regen outputs left uncommitted:** besides the four files this digest commits, the pipeline
  dirtied ~65 derived files in REE_assembly: the index, planning snapshots, status history,
  and six new `experiment.md`/`INDEX.md` pairs for 1012c/1077/1078/1080/1081/1082. They are
  left in the working tree for the next governance cycle, following the skill's
  commit-set rule. `evidence/experiments/substrate_status_snapshot.json` was already dirty
  before the regen and is not this run's output.
- **Queue empty, second day.** See Queue Status. The refill chip is unclaimed.
