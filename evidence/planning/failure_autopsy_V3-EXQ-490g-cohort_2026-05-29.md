# Failure Autopsy: V3-EXQ-490g cohort cluster (483c / 524a / 603c)

**Generated:** 2026-05-29T16:49:51Z
**Scope:** cluster (3 FAILs) — two-fork disposition
**Status:** confirmed (user sign-off 2026-05-29)
**Autopsy session:** failure-autopsy-490g-cohort-20260529T164951Z
**Owner of record:** goal_pipeline:GAP-4 / V3-EXQ-490g cohort

---

## 1. Targets

| Field | V3-EXQ-483c | V3-EXQ-524a | V3-EXQ-603c |
|---|---|---|---|
| run_id | `v3_exq_483c_sd037_broadcast_gap4_tier1_20260521T064444Z_v3` | `v3_exq_524a_reef_showcase_gap4_tier1_20260521T060220Z_v3` | `v3_exq_603c_q045_mech313_mech260_phased_training_20260527T113805Z_v3` |
| claim_ids | SD-037, MECH-280, MECH-281 | (diagnostic, no claim_ids) | Q-045, MECH-313, MECH-260 |
| outcome | FAIL | FAIL | FAIL (manifest values empty) |
| experiment_purpose | evidence | diagnostic | evidence |
| evidence_direction (manifest) | mixed (SD-037: weakens, MECH-280/281: unknown) | non_contributory | non_contributory (per-claim all non_contributory) |
| ran 2026-05- | 21T06:44 | 21T06:02 | 27T11:38 |

The 490g letter itself was **never queued**. The cohort plan named it (with 471a / 475a / 483c / 524a) as the Tier-1 StepHarness retest set for `goal_pipeline:GAP-4` MECH-295 cascade behavioural validation; only 483c and 524a got as far as a manifest, and 603c is the substrate-prereq #2 test from the 591 autopsy that the cohort needed cleared first.

---

## 2. Facts — what each FAIL actually showed

### 2a. V3-EXQ-483c (3 seeds × 4 arms, 12 runs)

Pass/fail criteria observed (every run):

| Criterion | Result |
|---|---|
| C1_cue_fires | PASS (bridge_cue_fires > 0 every run) |
| C2_dacc_bias | **FAIL — dacc_bias_nonzero_steps = 0 in ALL 12 runs** |
| C3_approach_commit | PASS (approach_commit_rate = 1.0 every run) |
| C3_lift_vs_baseline | **FAIL — OFF_OFF baseline already at 1.0, no headroom** |
| C4_goal_active | PASS (goal_active_fraction = 1.0 every run) |

Per-arm metrics (seeds 42 / 7 / 19):

| Arm | goal_norm_peak | bridge_cue_fires | dacc_bias_nz | approach_commit_rate |
|---|---|---|---|---|
| OFF_OFF | 0.193 / 0.092 / 0.296 | 26 / 4 / 12 | 0 / 0 / 0 | 1.0 / 1.0 / 1.0 |
| ON_OFF  | 0.189 / 0.092 / 0.310 | 29 / 3 / 29 | 0 / 0 / 0 | 1.0 / 1.0 / 1.0 |
| OFF_ON  | 0.193 / 0.092 / 0.296 | 26 / 4 / 12 | 0 / 0 / 0 | 1.0 / 1.0 / 1.0 |
| ON_ON   | 0.189 / 0.092 / 0.310 | 29 / 3 / 29 | 0 / 0 / 0 | 1.0 / 1.0 / 1.0 |

Per-seed **OFF_OFF = OFF_ON and ON_OFF = ON_ON byte-identical** — the broadcast-override flag had zero behavioural effect on any observable. SD-037 was wired correctly per [V3-EXQ-483b PAG release ratio 1.875x] but invisible to this experiment's instrumentation.

**Critical observation: goal_norm_peak is non-zero (0.09–0.31) in every run.** This is NOT the 591 substrate-uniform z_goal-zero signature. The goal pipeline is firing.

### 2b. V3-EXQ-524a (3 seeds × 1 arm, reef-showcase diagnostic)

| Arm | seed | goal_norm_peak | bridge_cue_fires | dacc_bias_nz | approach_commit_rate | total_eval_steps |
|---|---|---|---|---|---|---|
| ARM_gap4_reef | 42 | 0.356 | 10 | 0 | 1.000 | 211 |
| ARM_gap4_reef | 7  | 0.234 | 34 | 0 | 1.000 | 824 |
| ARM_gap4_reef | 19 | 0.261 | 4  | 0 | 1.000 | 276 |

Same shape as 483c: C2 zero (use_dacc gap), C3 saturated, but goal pipeline **firing at goal_norm 0.23–0.36** with the MECH-295 bridge actively writing cues.

### 2c. V3-EXQ-603c (3 seeds × 4 arms, Q-045 phased-training)

Manifest `metrics.json: values = {}` and `status: FAIL` with `outcome: None`. The script implemented Fix C (P0 + P1 phased training) and Fix D (end-of-P1 survival gate `median episode length >= 75`) per the 603b autopsy 2026-05-25 routing. The empty metrics indicate the script reached the "less than half the cells produced P2 data" branch in `_evidence_direction_per_claim`, which routes all three claims to `non_contributory` and emits no quantitative summary.

This is the structurally-underpowered branch the script was designed to detect — `n_p2_cells < total_cells / 2` means most (arm, seed) cells aborted at P0 (running_variance not converging) or failed the Fix D survival gate (`median episode length < 75`). The 591 autopsy enumerated 603c as the third member of the substrate-uniform z_goal-zero family (with V3-EXQ-540 series, 590a, 591 itself).

---

## 3. Claim-layer map

### SD-037 (broadcast_override regulator, candidate, v3_pending)
EXQ-483c tested SD-037 under conditions where the C2 criterion **could not fire regardless of SD-037 state** (use_dacc was off in every arm). The "weakens" tag was auto-generated from binary PASS/FAIL and carries no scientific signal. SD-037 implementation already validated by EXQ-483b (PAG release ratio 1.875x). **Recommendation: SD-037 → non_contributory + pending_retest_after_substrate=true** (reaffirms the 2026-05-24 autopsy).

### MECH-280 (LH→PAG override projection), MECH-281 (orexin-analog gain modulation)
Both candidate, v3_pending. C2/C3 failures say nothing about either claim. Evidence direction "unknown" is appropriate; no change.

### Q-045 / MECH-313 / MECH-260 (in 603c)
All three already `non_contributory` per the script's structurally-underpowered branch. No revision needed; the 591 autopsy's substrate-uniform reading absorbs the 603c result.

### 524a (no claim_ids)
Diagnostic experiment; nothing to weigh in either direction.

---

## 4. Biological-reference triage

### 483c / 524a (Tier-1 library cluster)
The biology is not the bottleneck. SD-037 is an orexin-analog with strong biological grounding (two lit-pulls: orexin_kinetics + homeostatic_override, 13 papers); MECH-295 is the drive→liking→approach bridge with NAcc/VP grounding (Pecina & Berridge 2005, Smith Berridge & Aldridge 2011). The substrate IS producing the architecturally-expected signal (goal_norm 0.09–0.36, bridge cues 3–34, approach saturated). The failure is in the test harness — `use_dacc=True` omission + degenerate C3 baseline.

### 603c (591 cluster member)
ARC-046's biological reading already triaged in the 591 autopsy 2026-05-27 (developmental-protection mechanism, faithful biological translation, no lit-pull required). Q-045 + MECH-313 + MECH-260 are all anchored to LC-NE adaptive-gain (Aston-Jones & Cohen 2005) and dACC anti-recency (Scholl/Kolling 2015) — sound biology, blocked by the substrate-side z_goal-development gap not by mechanism specification.

---

## 5. Four-layer diagnosis

### 5a. V3-EXQ-483c

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | C2 measures a disabled substrate; SD-037's primary PAG pathway is not captured by any criterion |
| Biological reference | partial | Orexin→PAG strong; orexin→dACC coupling weaker; C2 doesn't test primary pathway anyway |
| Prerequisites | missing | SD-032b not in SD-037 `depends_on`; not enabled in any arm |
| Implementation | complete | SD-037 implemented 2026-04-25; PAG wiring confirmed EXQ-483b (1.875x) |
| Environment | adequate | drive_floor=0.9 + goal_stream; C3 ceiling is a metric choice |
| Measurement | **misleading** | C2 measures a disabled substrate; C3_lift measures ceiling; neither captures SD-037 |
| Integration | partial | SD-037 wired to PAG/SalienceCoordinator/GoalState; dACC integration not wired |
| Scale | adequate | seeds 42/19 ran 793–1849 steps |

**Dominant diagnosis: measurement_gap** (configuration + metric choice; substrate is firing).

### 5b. V3-EXQ-524a

Same four-layer signature as 483c — measurement_gap on the same Tier-1 library template (no `use_dacc=True`, drive_floor=0.9 + reef ceiling on C3).

### 5c. V3-EXQ-603c

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | Test would let Q-045/MECH-313/MECH-260 express themselves; substrate did not produce z_goal under default config |
| Biological reference | clear | LC-NE adaptive-gain + dACC anti-recency well-anchored |
| Prerequisites | **missing** | Goal-pipeline substrate does not produce non-trivial z_goal in default config (591 cluster reading) |
| Implementation | partial | Phased-training scaffold complete; P2 measurement unreached |
| Environment | inadequate for discrimination | Substrate-uniform z_goal-zero across all arms |
| Measurement | adequate | Script correctly emits the structurally-underpowered branch when n_p2_cells < total_cells/2 |
| Integration | isolated | Modules work in isolation; default-config training regime does not engage the goal-pipeline substrate |
| Scale | likely insufficient | Same training-regime gap V3-EXQ-603b autopsy flagged; random-policy training across 2000 episodes does not develop z_goal |

**Dominant diagnosis: substrate_ceiling** (matches the 591 autopsy reading).

---

## 6. Cluster pattern — **two structurally distinct clusters, not one**

### Cluster A: GAP-4 Tier-1 library measurement-gap (483c, 524a — and by inheritance 471a, 475a, 490g if ever run)

| Experiment | Claim(s) | Negative-control / absolute criterion | Discrimination criteria | Read |
|---|---|---|---|---|
| V3-EXQ-483c | SD-037, MECH-280, MECH-281 | C1 cue_fires PASS, C3 approach_commit PASS, C4 goal_active PASS | **C2_dacc_bias 0 in ALL 12 runs (use_dacc missing); C3_lift FAIL (baseline ceiling 1.0)** | Goal pipeline firing (goal_norm 0.09–0.31); test-harness gap, not substrate |
| V3-EXQ-524a | (diagnostic) | C1 PASS, C3 PASS, C4 PASS | **C2_dacc_bias 0 in all 3 seeds; same template gap** | Goal pipeline firing (goal_norm 0.23–0.36); same template gap |

**One structural property, not two independent bugs.** The shared `evaluate_tier1_cohort` library in `ree-v3/experiments/_lib/goal_pipeline_tier1.py` requires `use_dacc=True` for C2 to fire, but the GAP-4 arm-spec template does not include it. Every GAP-4 Tier-1 experiment that does not explicitly add `use_dacc=True` to its arm configs will produce C2=false unconditionally. Five experiments named in the 483c autopsy as members (471a, 475a, 483c, 490g, 524a); the 490g letter itself was never queued, and 471a/475a were never queued for this cohort either.

**Both readings live:** (a) test-design ceiling (these are independent test-design errors masked as substrate failures), (b) the broadcast-override flag genuinely had no behavioural effect at this substrate scale. (a) is clearly correct for C2 (the criterion couldn't fire); (b) cannot be assessed until C2 has a discriminating criterion. The right action is **rebuild the library + re-queue the cohort** — not re-classify the existing FAILs as evidence against SD-037 or any other claim.

### Cluster B: 591 substrate-uniform z_goal-zero family (603c, plus 540 series, 590a, 591 itself)

V3-EXQ-603c is the third member of the 591 cluster (as already enumerated in `failure_autopsy_V3-EXQ-591_2026-05-27.md` §6). The structural property is the V3 substrate at default config under standard random-policy training does not produce non-trivial z_goal in any arm. 603c attempted to break this by adding P0+P1 phased training (Fix C from the 603b autopsy); the empty metrics + Fix D abort indicate the agent could not survive the target env even under the extended training budget (most cells aborted at P0 RV-not-converging or P1 survival-gate).

---

## 7. Learning extracted

1. **Cluster A (483c, 524a)**: The `_lib/goal_pipeline_tier1.py` library template is the bottleneck for the GAP-4 Tier-1 cohort, not the substrate. `use_dacc=True` must become the default for any GAP-4 arm-spec built through `ENV_FISHTANK_KWARGS` or the shared arm factory. C3_lift_vs_baseline must change: `approach_commit_rate` saturates at 1.0 in the OFF_OFF baseline under drive_floor=0.9 + goal_stream + reef, so it has no headroom. Replace with a metric that varies — `override_signal_nonzero_steps` (SD-037-specific), `goal_norm_peak delta vs baseline` (cross-claim), or `dacc_bias magnitude` once C2 has a non-degenerate measurement.
2. **Cluster A → Cluster B causality**: The 483c/524a FAILs are NOT evidence that the substrate is broken. The substrate is producing goal_norm 0.09–0.36, MECH-295 bridge cues 3–34, and approach saturation under drive_floor=0.9. Recovering the C2 measurement and a non-saturating C3 may show the substrate IS sufficient for GAP-4 cascade validation in the fishtank environment — which would weaken the 591-cluster reading for THIS environment slice (591 itself uses CausalGridWorldV2 + infant_curriculum, not fishtank + drive_floor=0.9 + goal_stream).
3. **Cluster B (603c)**: Phased training alone (Fix C) is insufficient for the 591 family. Random-policy P0+P1 training on the target env (SD-054 reef + bipartite + hazard_food_attraction=0.7 + proximity_harm_scale=0.1) is structurally hostile to the agent at random-init; the agent dies before z_goal can develop. The substrate-design follow-on per the user's 2026-05-29 sub-lever choice is **scaffolded SD-054 onboarding** — use the SD-054 substrate (landed 2026-05-04, V3-EXQ-521/522 PASS) as a goal-rich start-state distribution so the trained policy inhabits states where z_goal becomes load-bearing. This is the (A2) lever from the parent session.
4. **Cluster split is load-bearing for governance**: Forcing 483c/524a into the 591-cluster substrate-uniform-zero framing would (a) waste the SD-054-onboarding substrate-design effort on a measurement gap it doesn't fix, and (b) understate the substrate's actual capability in the fishtank slice. The two clusters need different fixes; collapsing them is misleading.

---

## 8. Repair pathway — two forks

### Fork A (483c, 524a, and the rest of the Tier-1 cohort)

**Routing: `/queue-experiment` (Tier-1 library rebuild)** — same routing as the 2026-05-24 483c autopsy, now reaffirmed under the second-wave evidence from 524a.

Substrate-side gap: the Tier-1 library template `ree-v3/experiments/_lib/goal_pipeline_tier1.py` (and its consumers via `ENV_FISHTANK_KWARGS` / the shared arm-spec factory). This is an experiment-script library fix, not a `ree_core/` substrate change — it does not warrant a substrate_queue entry. **`recommended_substrate_queue_entry.action = none`** for both 483c and 524a; the library fix is the queue-experiment skill's responsibility when V3-EXQ-483d (or its successor) is queued.

What the cohort retest needs:

- Library default: `use_dacc=True` in the GAP-4 arm-spec template (one shared factory call site fix).
- Library default: C3 metric replacement. For SD-037-specific arms, prefer `override_signal_nonzero_steps` (ON arms vs OFF arms — measures the primary PAG pathway directly). For cross-claim Tier-1 arms, prefer `goal_norm_peak delta vs baseline` (substrate-side; cross-claim-comparable). dACC-coupled SD-037 metrics (the original C2_dacc_bias) become a secondary diagnostic only.
- Optional substrate-side fix: SD-037 `depends_on` audit (the 2026-05-24 autopsy flagged that SD-032b should be in SD-037's `depends_on` list if dACC-coupled behaviour is a claimed signature). Governance-side audit, not autopsy work.
- Re-queue cohort: V3-EXQ-483d (successor to 483c), and successors for 524a + the unrun 471a / 475a / 490g letters, all under the rebuilt library.

### Fork B (603c — 591 cluster member)

**Routing: `/implement-substrate` (scaffolded SD-054 onboarding)** — confirms the user's 2026-05-29 sub-lever choice (A2) at the parent session.

Substrate-side gap: the goal-pipeline training regime under V3 default config does not produce non-trivial z_goal in default config. **`recommended_substrate_queue_entry.action = create`** for a new SD-XXX (governance assigns the real ID) describing the SD-054-scaffolded-onboarding substrate.

Implementation hint (to be expanded into a substrate-design memo by a follow-on `/implement-substrate` session, sibling to `e2_action_divergence_substrate_design.md`):

- Use SD-054 reef + bipartite-horizontal substrate (landed 2026-05-04, V3-EXQ-521 + V3-EXQ-522 PASS) as the start-state distribution for P0+P1 training. The agent spawns inside the reef refuge band; the forage half + hazard_food_attraction stays as the target-env reward landscape.
- During P0, freeze the goal-pipeline writes (`use_mech307_conjunction=False`, `use_mech295_liking_bridge=False`) so the agent's encoder + E2 + E3 can warm up on the SD-054 spatial structure without the goal-pipeline gating its own training data.
- During P1, gradually unfreeze the goal-pipeline (anneal `mech295_min_drive_to_fire` from 1.0 → 0.01 over a curriculum window; same for `mech307_conjunction_z_beta_threshold`). The agent is now alive long enough to develop a z_goal because the SD-054 substrate is providing scaffolded survival.
- P2 measurement on the trained agent.

This substrate is NOT yet named in `substrate_queue.json` or `claims.yaml`. The autopsy recommends `recommended_substrate_queue_entry.action = create` with `sd_id_suggested = "SD-XXX-scaffolded-sd054-onboarding"` (governance picks the real ID); the substrate-design memo + design doc are a follow-on `/implement-substrate` session per the spawning session's directive.

The 2026-05-29 IGW-prereq-detection feature ensures any future `Implement substrate: SD-XXX (unblocks Q-045)` IGW that references this new entry will appear in the workset for human-visible review before auto-spawning. The 591 autopsy's substrate prereq #3 (InfantCurriculumScheduler exit-gate tuning) is unaffected — ARC-046 stays pending its own prereqs.

---

## 9. Per-claim direction overrides (recommendations to /governance)

Per [REE_assembly/CLAUDE.md] "Per-experiment evidence_direction with per-claim overrides", governance applies these — the autopsy does not edit the manifests.

### V3-EXQ-483c
- `SD-037`: weakens → **non_contributory** (reaffirms 2026-05-24 autopsy; `pending_retest_after_substrate=true`).
- `MECH-280`: unknown → no change.
- `MECH-281`: unknown → no change.

### V3-EXQ-524a
- No `claim_ids` (diagnostic); no per-claim overrides needed. Manifest already non_contributory.

### V3-EXQ-603c
- `Q-045`: non_contributory → no change (matches 591 cluster reading; `pending_retest_after_substrate=true` retained).
- `MECH-313`: non_contributory → no change.
- `MECH-260`: non_contributory → no change.

---

## 10. Draft `evidence_quality_note` text (governance applies)

For SD-037 (V3-EXQ-483c, reaffirmation under cluster-split):

> 2026-05-29 (V3-EXQ-490g cohort autopsy): cluster-split analysis confirms 2026-05-24 V3-EXQ-483c autopsy reading. SD-037 weakens tag is algorithm-generated from binary FAIL on a configuration omission (use_dacc=True missing from all 4 arm configs → agent.dacc is None → C2_dacc_bias=0 in every run regardless of SD-037 state). Goal pipeline is firing (goal_norm 0.09–0.31; bridge_cue_fires 3–29; approach_commit_rate 1.0). C3_lift FAIL is policy ceiling (baseline approach_commit_rate=1.0 in OFF_OFF arm), not SD-037 suppression. Same template gap drives V3-EXQ-524a per-seed (goal_norm 0.23–0.36; same C2 zero). Cluster = 5 GAP-4 Tier-1 experiments (471a / 475a / 483c / 490g / 524a) all share one tier-1 library template gap. evidence_direction → non_contributory. Pending retest after Tier-1 library rebuild (use_dacc=True default + C3 metric replacement). NOT in the 591 substrate-uniform z_goal-zero cluster.

For Q-045 / MECH-313 / MECH-260 (V3-EXQ-603c, cluster-absorb into 591 family):

> 2026-05-29 (V3-EXQ-490g cohort autopsy): cluster-absorb confirmed. V3-EXQ-603c routes into the 591 substrate-uniform z_goal-zero family per failure_autopsy_V3-EXQ-591_2026-05-27.md §6. P0+P1 phased training (Fix C from 603b autopsy) was insufficient: most (arm, seed) cells aborted at P0 (running_variance not converging) or failed the Fix D survival gate (median episode length < 75), producing the structurally-underpowered evidence_direction_per_claim non_contributory branch (n_p2_cells < total_cells/2). Substrate prereq #2 from the 591 autopsy ("goal-pipeline training regime produces non-trivial z_goal in default config") confirmed unmet. evidence_direction stays non_contributory. pending_retest_after_substrate retained. Recommended substrate-design follow-on per user 2026-05-29 routing: scaffolded SD-054 onboarding (substrate-design memo + /implement-substrate session, sibling pattern to e2_action_divergence_substrate_design.md).

---

## 11. Routing decisions (user-confirmed 2026-05-29)

| Target | Routing | Substrate queue action | Per-claim overrides |
|---|---|---|---|
| V3-EXQ-483c | `/queue-experiment` (Tier-1 library rebuild + 483d successor) | none (library fix, not ree_core substrate) | SD-037 → non_contributory + pending_retest_after_substrate |
| V3-EXQ-524a | `/queue-experiment` (Tier-1 library rebuild, no SD-037-specific successor needed; diagnostic only) | none | — (diagnostic, no claim_ids) |
| V3-EXQ-603c | `/implement-substrate` (scaffolded SD-054 onboarding substrate-design memo + design doc) | **create** new entry `SD-XXX-scaffolded-sd054-onboarding` (governance picks real ID) | Q-045/MECH-313/MECH-260 no change (already non_contributory + pending_retest_after_substrate) |

---

## 12. Concurrent-session notes

- No active claims on the cohort manifests or on `goal_pipeline_plan.md` at session start (16:49Z snapshot). The gap-d-r4b-stamp claim that was open earlier in this hour closed concurrently before this autopsy's claim was written.
- The autopsy does NOT modify the substrate_queue, claims.yaml, manifests, or `goal_pipeline_plan.md`. Governance + the follow-on `/implement-substrate` session apply the recommendations.
- The 2026-05-29 IGW-prereq-detection symmetric extension (commit `d8d1aa2707`) ensures the new SD-XXX substrate-queue entry, once created, will surface as a properly-gated `Implement substrate: SD-XXX (unblocks Q-045)` IGW item in the workset.

---

## See also

- `failure_autopsy_V3-EXQ-591_2026-05-27.md` — parent cluster autopsy (603c absorbed here)
- `failure_autopsy_V3-EXQ-483c_2026-05-23.md` — original Tier-1 library measurement-gap diagnosis (Cluster A predecessor)
- `failure_autopsy_V3-EXQ-603b_2026-05-25.md` — 603 chain predecessor (motivated Fix C / Fix D in 603c)
- `goal_pipeline_plan.md` — GAP-4 plan-of-record (owner: V3-EXQ-490g cohort)
- `e2_action_divergence_substrate_design.md` — canonical-shape memo precedent for the SD-054-onboarding follow-on
- `behavioral_diversity_isolation_plan.md` GAP-C — consumer plan whose unblock cascades from goal-pipeline GAP-4
- `substrate_queue.json` ARC-046 — whose `ready_blocked_by` includes the goal-pipeline / training-regime prereq this autopsy addresses for Cluster B
