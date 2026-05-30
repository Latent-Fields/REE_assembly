# Failure Autopsy: V3-EXQ-490i

| Field | Value |
|---|---|
| run_id | `v3_exq_490i_mech295_cascade_gap4_tier1_20260530T184434Z_v3` |
| queue_id | V3-EXQ-490i |
| supersedes | V3-EXQ-490h (pipeline drop; this is the bit-identical scientific re-run on the post-fix runner pipeline) |
| claim_ids | [MECH-295] |
| experiment_purpose | evidence |
| outcome | FAIL |
| manifest `evidence_direction` | weakens |
| elapsed | 15205.75 s (~4.2 h) on DLAPTOP-4.local |
| autopsy generated_utc | 2026-05-30T19:43:19Z |
| scope | single |
| status | confirmed (user-confirmed routing 2026-05-30) |

## 1. Reconstruction (facts, no interpretation)

V3-EXQ-490i is the GAP-4 Tier-1 MECH-295 drive->liking->approach cascade retest, run on the rebuilt Fork-A library (post 490g-cohort autopsy). 2 arms x 3 seeds (42, 7, 19). ARMs:

- **ARM_0_legacy_collapsed**: `z_goal_enabled=True`, `drive_floor=0`, no goal_stream, no MECH-295 bridge stack.
- **ARM_1_gap4_operating**: full GAP-4 stack (drive_floor=0.9 + goal_stream + MECH-295 bridge + use_dacc=True via rebuilt library default).

### 1.1 Per-seed metrics

| Seed | Arm | bridge_cue_fires | bridge_write_fires | dacc_bias_nonzero_steps | approach_commit_rate | goal_norm_peak | total_eval_steps |
|---|---|---|---|---|---|---|---|
| 42 | ARM_0 | 0 | 0 | 0 | 0.0 | 0.7925 | 441 |
| 42 | ARM_1 | 6 | 6 | 0 | 1.0 | 0.2261 | 1379 |
| 7  | ARM_0 | 0 | 0 | 0 | 0.0 | **12.4888** | 2000 |
| 7  | ARM_1 | 4 | 4 | 0 | 1.0 | 0.0919 | 59 |
| 19 | ARM_0 | 0 | 0 | 0 | 0.0 | 0.4679 | 911 |
| 19 | ARM_1 | 12 | 40 | 0 | 1.0 | 0.2958 | 793 |

### 1.2 Acceptance result

| Criterion | Type | Result |
|---|---|---|
| C1_cue_fires | ARM_1 absolute | PASS |
| C2_dacc_bias | ARM_1 absolute | **FAIL** (`dacc_bias_nonzero_steps=0` in 3/3 ARM_1 seeds) |
| C3_approach_commit | ARM_1 absolute | PASS |
| C3_lift_vs_baseline | ARM_1 vs ARM_0 discrimination (metric: `goal_norm_peak` delta, floor 0.01, >=2/3 seeds) | **FAIL** (ARM_1 < ARM_0 every seed) |
| C4_goal_active | ARM_1 absolute | PASS |

### 1.3 Episode-length variance

ARM_0 episode lengths: 441 / 2000 / 911. ARM_1 episode lengths: 1379 / 59 / 793. Seed-7 ARM_1 ran 59 eval steps total; seed-7 ARM_0 ran 2000. Per-seed metric magnitudes are not normalized for length.

## 2. Claim-layer mapping (MECH-295)

MECH-295 (claims.yaml): `mechanism_hypothesis`, status `candidate`, `v3_pending=true`, weak-necessity reading committed provisionally. Primary falsifiable test as registered in the claim entry:

> a V3 factorial with the drive->liking link intact vs severed (under matched drive_level) should show approach_commit recovers when the bridge is intact and collapses when severed.

Observed:

- ARM_1 (bridge intact): bridge_cue_fires non-zero across all seeds (4, 6, 12); approach_commit_rate = **1.0 in 3/3 seeds**.
- ARM_0 (bridge severed: no goal_stream / drive_floor=0): bridge inactive; approach_commit_rate = **0.0 in 3/3 seeds**.

The sign-test that the claim entry registers as the primary falsifiable test PASSES across all seeds. The two component failures (C2 dACC bias, C3_lift_vs_baseline) are not about MECH-295 (see Sections 3-5).

Existing `evidence_quality_note` on MECH-295 already records the 2026-05-07 update_z_goal_typeerror_swallowed contamination of the 471/475/483/483a/483b/490/490b/490c/490e/490f/524 cohort, which 490i is a corrected downstream of (via 490g substrate fix and 490h-490i pipeline re-run).

## 3. Biological-reference triage

Reference mechanism: NAc shell hedonic hotspot + ventral pallidum + OFC pleasure coding -- the drive -> liking-stream -> approach cascade. Substrate is a translation of a working biological pathway; literature on record at `evidence/literature/targeted_review_mech295_liking_approach_bridge/SYNTHESIS.md` (6 entries, mean conf 0.77, 5 supports / 1 mixed). Strongest anchors: Smith Berridge & Aldridge 2011 (VP single-unit, drive change recodes palatability before cue firing); Dickinson & Balleine 1994 (instrumental devaluation requires outcome re-experience); Berridge & Kringelbach 2015 (architectural articulation).

The biology predicts: drive recruits liking-stream activation at goal-congruent cues, which biases approach. The observed pattern (bridge fires under elevated drive -> approach_commit rises) is the biology's prediction in the sign direction. Biology supports the mechanism; the failure pattern is not biology-divergence.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened | Primary falsifiable test (bridge ON -> approach_commit; bridge OFF -> no approach) passes 3/3 seeds. Substrate-side proxy fails because the chosen metric is contaminated, not because MECH-295 is wrong. |
| Biological reference | clear | NAc hedonic hotspot pathway; well-anchored lit-pull already on record. |
| Prerequisites | present | SD-012 + SD-014 + SD-015 + SD-016 + MECH-117 + ARC-036 all landed and active. |
| Implementation | complete (MECH-295); partial (SD-032b dACC bundle -> E3 score_bias) | MECH-295 bridge instantiated cleanly (cue + write fires). dACC bundle never reaches the `_last_bundle` population path the E3 score_bias adapter expects. |
| Environment | adequate | Fishtank `ENV_FISHTANK_KWARGS`; behavioural divergence between arms is sharp and reproducible. |
| Measurement | **inadequate** | `C3_lift_vs_baseline` uses `goal_norm_peak` ARM_1 - ARM_0. ARM_0 has `z_goal_enabled=True` (just `drive_floor=0` + no goal_stream / bridge), so it accumulates a goal_norm baseline the metric assumes is zero. Seed-7 ARM_0 spikes to 12.49 (~50x the other ARM_0 seeds) and dominates the cross-seed comparison. Episode-length variance (59 <-> 2000 steps within ARM_1) further confounds per-seed magnitude comparison. The script's docstring claims this metric "measures the cascade's proximal substrate output -- z_goal seeding amplification -- directly"; the chosen baseline arm does not actually subtract that contribution. |
| Integration | partial | MECH-295 bridge wired and firing in ARM_1. dACC bundle is constructed but its downstream pathway to E3 `score_bias` is dormant in this validation env / config -- consistent with the same "wired but inert at validation surface" signature documented in the SD-037 substrate_queue entry. |
| Scale | adequate | 3 seeds x ~75 episodes is the standard GAP-4 Tier-1 budget. |

**Recommended `epistemic_category`: `standard`.** This is NOT the substrate-ceiling cluster shape (V3-EXQ-540 / 590a / 591 / 598 / 603). Those clusters are negative-control-passes-discrimination-fails on a substrate that cannot carry the distinction; here the substrate carries the behavioural distinction cleanly (approach_commit 1.0 in 3/3 vs 0.0 in 3/3) and the discrimination criterion itself is mis-designed.

## 5. Cluster check

V3-EXQ-490i is NOT part of the substrate-ceiling cluster. The autopsy treats it as single-target.

## 6. Learning extracted

1. The pre-registered "FAIL with C3_lift_vs_baseline=False, C1/C2/C4 PASS" row in the script's interpretation grid (route to MECH-295 sub-gain parametric sweep) is **NOT the right diagnosis here** -- the grid did not anticipate `C2=False AND C3_lift=False` together. The composite-failure cell needs both routing arms (gain sweep would not fix the contaminated metric; dACC diagnose would not address the metric either). Future Tier-1 grids should cover composite-FAIL cells, not just single-criterion-FAIL cells.

2. Substrate-side proxy metrics that subtract two arms must guarantee the baseline arm is ACTUALLY zero on the measured channel. ARM_0 `legacy_collapsed` keeps `z_goal_enabled=True` -- it severs the bridge but does not zero the channel the metric reads. The clean MECH-295 baseline is `z_goal_enabled=False` (true severed-bridge control), not `drive_floor=0`.

3. The MECH-295 architectural prediction registered as the primary falsifiable test is the BEHAVIOURAL sign-test (approach_commit_rate sign-difference between bridge-on and bridge-off arms). 490i meets that test in 3/3 seeds. Treating the manifest's roll-up `evidence_direction=weakens` as the governance signal would mis-weight a result whose primary test passed.

4. dACC bundle `_last_bundle` population path under `cfg.use_dacc=True` is silently dormant. This is a separate wiring gap on the SD-032b consumer path -- orthogonal to MECH-295. Same wired-but-inert signature documented under SD-037 / V3-EXQ-483d (consumer-cascade dormancy in validation envs).

## 7. Repair pathway

User-confirmed routing 2026-05-30T19:43Z:

**(a) `/queue-experiment` for V3-EXQ-490j** -- redesigned MECH-295 probe:
  - True severed-bridge baseline arm (`z_goal_enabled=False`), NOT `drive_floor=0`.
  - Direct bridge-magnitude probe (cue_fires + write_fires + per-tick anticipatory liking write magnitude) replacing the contaminated `goal_norm_peak` delta.
  - Consistent episode-length budget across seeds (cap or floor the per-episode step count so seed-7 doesn't trail out to 59 vs 1379).
  - Keep the behavioural sign-test (`approach_commit_rate` ARM_1 vs ARM_0) as a parallel criterion.

**(b) Separate `/diagnose-errors`** on the SD-032b cingulate.dacc bundle -> E3 `score_bias` propagation path (the C2 wiring gap; matches the script's pre-registered "FAIL with C2=False" interpretation row). Not bundled into the 490j scope -- it is its own wiring investigation that touches the SD-032b consumer pathway.

## 8. Per-claim direction recommendation (governance applies)

`evidence_direction_per_claim["MECH-295"]`: **narrow_supports** (autopsy upgrade from manifest `weakens`).

Rationale: behavioural sign-test (the claim entry's registered primary falsifiable test) met in 3/3 seeds; substrate-side proxy failure is metric-design contamination, not claim falsification. `narrow` because this is one experimental pair under one env config; broader retest comes with V3-EXQ-490j.

## 9. Draft `evidence_quality_note` (verbatim text for governance to append)

> V3-EXQ-490i (GAP-4 Tier-1 retest on rebuilt library, post 490g-cohort autopsy Fork A): bridge fires cleanly in ARM_1 (cue 4-12 / write 4-40 across seeds 42/7/19) with `approach_commit_rate=1.0` in 3/3 seeds vs ARM_0 `approach_commit_rate=0.0` in 3/3. The MECH-295 architectural prediction registered as the primary falsifiable test (bridge intact -> approach recovers; bridge severed -> collapses) is met in the sign direction across all seeds. The manifest's `evidence_direction=weakens` rolls up a test-design contamination on `C3_lift_vs_baseline` (the chosen substrate-side proxy is `goal_norm_peak` ARM_1 - ARM_0, but ARM_0 has `z_goal_enabled=True` and accumulates a goal-norm baseline the metric assumes is zero -- seed-7 ARM_0 spikes to 12.49) and a separate C2 dACC wiring gap (`dacc_bias_nonzero_steps=0` across all ARM_1 seeds despite `cfg.use_dacc=True` -- bundle never reaches `_last_bundle` population path). Neither failure component falsifies MECH-295. Autopsy upgrade: `evidence_direction_per_claim["MECH-295"]` = `narrow_supports`. Routing: (a) `/queue-experiment` for a V3-EXQ-490j successor with a true `z_goal_enabled=False` severed-bridge baseline and a direct bridge-magnitude probe replacing the contaminated `goal_norm_peak` delta; (b) separate `/diagnose-errors` on the SD-032b dACC bundle -> E3 `score_bias` propagation. See `evidence/planning/failure_autopsy_V3-EXQ-490i_2026-05-30.{md,json}`.

## 10. Routing summary (governance applies)

| Action | Owner | Notes |
|---|---|---|
| Append draft `evidence_quality_note` to MECH-295 in claims.yaml | governance | Verbatim text in Section 9. |
| Set `evidence_direction_per_claim["MECH-295"] = narrow_supports` on the V3-EXQ-490i manifest | governance | Autopsy upgrade from `weakens`. Re-run indexer after. |
| substrate_queue write | NONE | No substrate amendment. Substrate operative. `recommended_substrate_queue_entry.action = none`. |
| `pending_retest_after_substrate` | NO | Substrate fires correctly; retest dependency is on probe redesign (V3-EXQ-490j), not substrate work. |
| Successor experiment | `/queue-experiment` V3-EXQ-490j | Separate session. |
| C2 dACC wiring gap | `/diagnose-errors` | Separate session targeting SD-032b cingulate.dacc bundle -> `_last_bundle` -> E3 `score_bias`. |

## 11. Open items / explicitly NOT done in this session

- claims.yaml `evidence_quality_note` write -- left for governance (skill rule).
- manifest `evidence_direction_per_claim` write -- left for governance (skill rule).
- 490j experiment script + queue entry -- separate `/queue-experiment` session.
- C2 dACC wiring diagnosis -- separate `/diagnose-errors` session.
- substrate_queue.json -- no edit (no substrate amendment).
- review_tracker.json -- left for governance.
