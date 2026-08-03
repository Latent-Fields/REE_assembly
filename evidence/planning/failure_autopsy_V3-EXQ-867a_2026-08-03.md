# Failure Autopsy: V3-EXQ-867a (MECH-321 harm-aware selection, hazard-tuned retest)

**Generated:** 2026-08-03T08:42:37Z | **Status:** confirmed | **Scope:** single

## Facts

- Run: `v3_exq_867a_mech321_harm_aware_selection_hazard_tuned_20260802T203309Z_v3`, FAIL, claim MECH-321, supersedes V3-EXQ-867. Not a dry run (`check_dry_run_citations.py`: 1 clean). `non_degenerate: true`. `per_arm_gate.all_green: true` (both ARM_SELECTION_OFF and ARM_SELECTION_ON green, no red/vacuous arms).
- Successor to `failure_autopsy_V3-EXQ-867_2026-08-02` (confirmed `environment_adequacy_defect`): 867's `harm_bias_engages` precondition failed on every seed/arm because the run used the default (untuned) baseline env with no hazard-density overlay, so `z_harm_a_norm` never cleared the engagement floor.
- **867a's own docstring (code-verified, not just asserted) documents THREE additional structural fixes found this same session beyond the recommended SD-029 env overlay alone**, each confirmed necessary by direct instrumentation before this run was queued: (1) `use_affective_harm_stream=True` + passing `obs_harm_a` into `agent.sense()` -- `z_harm_a` was structurally `None` throughout the entire 844/867 lineage, so no env tuning alone could move `z_harm_a_norm`; (2) `use_harm_stream=True` + passing `obs_harm` -- Stage 1's graded `harm_bias()` also needs the RBF-sourced `harm_penalty`, which requires this second, separate SD-010 channel; (3) `valence_harm_enabled=True` -- gates whether the RBF's `VALENCE_HARM_DISCRIMINATIVE` channel writes at all. All three plus the SD-029 hazard-density overlay were needed together; applying the overlay alone (measured this session) still left `decomp_n_harm_bias_nonzero=0`.
- **Readiness precondition `harm_bias_engages` now MET** (ARM_SELECTION_ON, measured 972 nonzero calls, threshold 0) -- the manipulation is genuinely engaged for the first time in this lineage, unlike 867's total inertness.
- **Load-bearing criterion `C1_TASK_OUTCOME_IMPROVES` FAILS**: measured mean paired delta -0.0139 vs threshold 0.0 (positive = ARM_SELECTION_ON less harmful). Restricted, by design, to the `both_decompose` seed tier (seeds where mid-execution decomposition independently fired in BOTH arms) -- **exactly 2 seeds qualified (11, 23)**, the driver's own stated `MIN_DECOMPOSING_SEEDS=2` floor, out of 6 total seeds run (2 `both_decompose`, 1 `on_only_decompose`, 2 `neither_decompose` -- unusual four-way tiering unchanged in shape from 867).
- **The two matched seeds disagree in direction**: seed 11's fresh-window harm delta (off-minus-on) = -0.0402 -- ARM_SELECTION_ON was MORE harmful than OFF in this seed. Seed 23's delta = +0.0125 -- ON was slightly LESS harmful. Net mean -0.0139 fails the (already weak) 1xSE bar.
- **Non-load-bearing corroboration `C2_FORWARD_PE_CORROBORATES` PASSES** (forward-PE also lower in ON than OFF on the same matched window) -- consistent with 844's established finding, but non-gating.
- **Excluded (unmatched, informational) seed 47** (`on_only_decompose` -- only ON's decomposition fired mid-execution, not OFF's, so it is correctly excluded from the paired statistic by design): fresh-window delta = **+0.127**, a substantially larger beneficial effect in the intended direction than either matched seed shows. Correctly excluded (the pairing requirement is not optional), but the magnitude and direction are a material covariate against reading 867a as a clean, confident null.

## Claim-layer mapping

MECH-321 `depends_on: [ARC-070, MECH-288, MECH-269, MECH-094]`, `status: candidate`, `v3_pending: true`. Granularity-debt cluster (`granularity_debt_cluster.py MECH-321`): 4 prior targets, alignment distribution `intact=2, unclear=1, weakened=1` (V3-EXQ-844 reads `weakened` for the harm-outcome-specifically axis; V3-EXQ-867 reads `unclear`, manipulation never engaged). 867a is now the first run where the manipulation genuinely engages AND a scored direction is possible -- but the sample the load-bearing statistic can draw on (n=2 matched seeds, opposite-signed) is too thin to treat the negative mean as a confident test of the claim.

## Biological-reference triage

Unchanged from 844/867: threat-modulated defensive path-selection (Fanselow/Mobbs, per 844's lit-pull) is the reference mechanism; no new biology question is raised here. This autopsy's finding is a measurement/sampling-design issue, not a biological-reference gap.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (underpowered, not weighted) | negative mean driven by 2 opposite-signed matched seeds; not a confident test either direction |
| Biological reference | clear | unchanged from 844/867 |
| Prerequisites | present | SD-hazard-aware-policy-decomposition implemented+ready (unchanged from 867) |
| Implementation | complete | three-flag substrate fix (affective/sensory harm streams, valence-harm-enabled) + SD-029 overlay confirmed engaging (972 nonzero calls) |
| Environment | adequate now | hazard-density overlay + affective-stream wiring both confirmed live this run |
| Measurement | **underpowered -- the load-bearing gap** | `both_decompose` matched-pair tier is set by CHANCE (whether decomposition happens to fire mid-execution independently in both arms per seed), not by design control; only 2/6 seeds landed in it |
| Integration | n/a | |
| Scale | n/a | |

## Learning extracted

1. Fixing 867's environment-adequacy defect (SD-029 overlay) alone was NOT sufficient -- three further structural wiring gaps (two separate harm-sensory channels plus a valence-write gate) had to be fixed together before the manipulation could engage at all. This is now confirmed and load-bearing for any future MECH-321 harm-aware-selection run: the three-flag fix is a genuine substrate prerequisite, not an 867a-specific config quirk.
2. The manipulation now genuinely engages (unlike 867's total inertness) -- environment-adequacy and substrate-wiring are both closed. What remains open is a SAMPLING problem: the `both_decompose` matched-pair design tier depends on stochastic mid-execution behaviour rather than being under direct experimental control, so the effective sample size for the load-bearing statistic (n=2) is set by seed luck, not by the experimenter.
3. The excluded unmatched seed's large beneficial-direction effect (+0.127, vs the matched seeds' -0.040/+0.0125) is a meaningful signal that the true effect may be larger and more consistently positive than the underpowered matched comparison can currently detect -- it should motivate growing the matched-tier sample, not be read as noise to discard.

## Re-derive brake (Step 7)

MECH-321 re-derive-brake count (R1-R3 recipe, confirmed corpus): **0** prior `substrate_ceiling` hits. This target is recommended `epistemic_category: measurement_test_design_defect`, not `substrate_ceiling` -- brake stays at 0, does not fire. Consistent with routing to a re-queue rather than `/implement-substrate`.

**Granularity-debt check** (`granularity_debt_cluster.py MECH-321`): alignment distribution across the 4-target cluster is `intact=2, unclear=1(867), weakened=1(844)`. Adding this target as `unclear` (underpowered, per the user-confirmed reading) does not add a second `weakened` -- the trigger's own bar (>=1 target reading `weakened`, AND structurally differing signatures) is not newly crossed by this target. Does not fire.

## Routing

**epistemic_category:** `measurement_test_design_defect` | **evidence_direction:** `non_contributory` (underpowered, not scored as a confident weakens) | **routing:** `/queue-experiment` 867b -- same question, redesigned specifically to grow the `both_decompose` matched-seed pool: either (a) run substantially more seeds from the already-characterized `HAZARD_TUNED_SEED_POOL` candidate scan (10-candidate table already measured this session per the 867a driver module), or (b) retune the hazard-density / decomposition-trigger schedule to raise the probability that BOTH arms independently decompose mid-execution per seed (removing the current dependence on chance alignment), rather than accepting whichever seeds happen to qualify. `recommended_substrate_queue_entry.action: "none"` -- no substrate build needed; this is a sampling/design question, not an implementation gap.

**Draft `evidence_quality_note`** (governance to write, MECH-321):

> [failure_autopsy_V3-EXQ-867a_2026-08-03] V3-EXQ-867a confirms the manipulation now genuinely engages (867's three additional structural gaps -- affective/sensory harm streams + valence-harm-enabled -- fixed alongside the SD-029 hazard overlay; `harm_bias_engages` precondition met, 972 nonzero calls). The load-bearing task-outcome test is underpowered: only 2 seeds qualified for the matched-pair (`both_decompose`) design tier, with opposite-signed deltas (-0.040, +0.0125), netting a small negative mean (-0.0139) that fails the (already weak) 1xSE bar. A third, correctly-excluded unmatched seed shows a substantially larger beneficial effect (+0.127) in the intended direction. Read as `measurement_test_design_defect` / non_contributory rather than a confident weakens -- the matched-seed sample size is set by chance (whether decomposition independently fires mid-execution in both arms), not by design control. Routed to `/queue-experiment` 867b to grow the matched-seed pool or retune the trigger schedule; no substrate build needed.

**User gate (2026-08-03):** Confirmed via `AskUserQuestion` -- scored as underpowered null (`measurement_test_design_defect` / non_contributory) with a re-queue recommendation, rather than letting the negative mean stand as a confident `weakens`.
