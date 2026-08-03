# Failure Autopsy: V3-EXQ-866a (INV-034/Q-021 goal-maintenance-necessary-for-agency, onboarded re-run)

**Generated:** 2026-08-03T10:34:50Z | **Status:** confirmed | **Scope:** single

## Facts

- Run: `v3_exq_866a_inv034_q021_goal_maintenance_agency_onboarded_20260803T075813Z_v3`, FAIL, `non_contributory`, claims INV-034/Q-021. Supersedes V3-EXQ-866 (`failure_autopsy_V3-EXQ-866_2026-08-02`, confirmed, user-approved).
- `dry_run_checked: true` -- confirmed real run.
- Gate table (own driver, `experiments/v3_exq_866a_inv034_q021_goal_maintenance_agency_onboarded.py`): G0 non-degeneracy 0/3 FAIL, C1 harm parity 2/3 PASS, C2 survival parity 2/3 PASS, C3 quiescence 3/3 PASS, C4 approach-restored 0/3 FAIL, C5 entropy signature 0/3 FAIL, C6 z_goal mechanistic check 0/3 FAIL.
- G0 (same signature as 866): `resource_visit_rate_mean_FULL=0.0033` is **below** `resource_visit_rate_mean_RANDOM=0.0103` -- the trained FULL agent forages worse than random action selection, on the SECOND-generation (scaffolded_sd054_onboarding) curriculum that 866's own autopsy prescribed as the fix for exactly this failure mode.
- The driver's own `summary_markdown`/`interpretation` already states: *"G0 non-degeneracy gate FAILED on the second-generation (scaffolded) harness. This is a genuine escalation-exhausted finding, not a routine re-queue... Still NOT evidence against INV-034/Q-021 -- it means the ceiling is deeper than the 866-diagnosed harness gap. Route to a fresh substrate-readiness diagnostic on this exact configuration before a further lettered iteration."*

## Configuration-parity check (ruling out a config-mismatch explanation)

Compared 866a's `build_scaffold_cfg`/`build_agent_config` line-by-line against its cited validated reference, V3-EXQ-603q (`v3_exq_603q_sd059_mech358_escape_affordance_bridge_evidence.py`, ARM_BASE_IA_ONLY arm):
- Curriculum stage order identical: `run_stage0_nursery -> run_stage0b_consolidation -> run_p0 -> run_hazard_avoidance -> run_p1` in both.
- Stage-H parameters identical: `HAZARD_STAGE_NUM_HAZARDS=6`, `NUM_RESOURCES=2`, `HFA=0.0`, `PROXIMITY_HARM=0.10`, `SURVIVAL_GATE_STEPS=75`, `STABILITY_WINDOW=10`, `BUDGET=40`.
- Curriculum budgets identical: `STAGE0=20, STAGE0B=10, P0=100, P1=50` (866a P2=30 vs 603q P2=15 -- eval-only, does not affect training).
- Agent config identical on every checked flag: `z_goal_enabled=True`, `drive_weight`, MECH-295/307, incentive-token-bank, cue-recall, PAG freeze gate, instrumental avoidance, escape-affordance-bridge=False (both).
- Same seeds: `[42, 43, 44]` in both.
- **No config difference found that would explain a performance gap.**

Yet observed Stage-H performance is drastically worse than the cited reference: `hazard_median_last_window` = 5.5 (seed 42), 4.0 (seed 43) out of a 75-step survival gate, vs 603q's own reported `base_mean_survival=37.725` (confirmed by reading 603q's own manifest, `v3_exq_603q_..._20260617T042830Z_v3.json`) -- a ~7x shortfall.

**Recording gap in the cited reference**: 603q's manifest (2026-06-17) predates the recording standard and carries `substrate_commit: None`, `substrate_hash: None` -- there is no way to confirm 603q ran against the same substrate state as 866a (2026-08-03, 47 days later). The citation of "the validated 603q-lineage configuration" as an expected-performance target is therefore commit-unverifiable; substrate drift over that 47-day window cannot be ruled in or out directly.

## Secondary finding: z_goal decay across the curriculum

FULL arm's `stage0_z_goal_norm_peak` is healthy (0.499 seed42, 0.429 seed43) -- z_goal forms correctly during Stage-0. But `zgoal_norm_mean_FULL` at P2 measurement is only **0.120** -- well under the C6 floor of 0.4. z_goal is not surviving the intervening Stage-H (hazard-only, no resource-approach reinforcement) and P1 curriculum phases into the measurement window. This independently explains C6's failure and likely contributes to C4/C5 (the FULL arm may no longer be meaningfully goal-engaged by the time it is measured, eroding its advantage over AVOIDANCE_ONLY before the ablation comparison even happens).

## Claim-layer mapping

- INV-034, Q-021: both claims never fairly tested for a second time -- the SAME structural non-degeneracy problem (FULL below RANDOM) recurred despite a full harness escalation.
- `granularity_debt_cluster.py`: not run against a compound cluster query here since 866/866a form a supersession chain (single lineage), not independent claim-tagging targets in the corpus sense -- but note this IS the second autopsy circling this claim pair with two different (though related) failure signatures: 866 = below-random foraging on a lightweight harness; 866a = below-random foraging AGAIN on the heavy harness, PLUS a newly-visible Stage-H survival shortfall and z_goal decay. Per the re-derive brake's R3 convention, 866's own category (`substrate_not_ready_requeue`) does not count as a `substrate_ceiling` hit, so this autopsy is the first to recommend `substrate_ceiling` proper for this claim pair (count=1, threshold=2 not yet met).

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | claim never fairly tested; substrate readiness has now failed on two successive harness generations |
| Biological reference | unchanged | mechanism (D1/D2 Go/NoGo, Bariselli 2018; wanting vs liking, Barch & Dowd 2010) not yet tested |
| Prerequisites | **missing/immature** | Stage-H hazard-avoidance training does not reproduce its own cited validated precedent (~7x shortfall) despite confirmed config parity |
| Implementation completeness | unclear | z_goal FORMS correctly (Stage-0 peak healthy) but does not survive the curriculum to the measurement window (P2 mean 0.12 vs 0.4 floor) |
| Environment adequacy | possibly inadequate | hazard-only curriculum stages (Stage-H, most of P1) offer no resource-approach reinforcement to sustain z_goal, if decay-during-distraction is a genuine substrate property rather than a bug |
| Measurement adequacy | **compromised for the reference, not this run** | 603q's own manifest lacks substrate_hash/commit -- the performance target this escalation was built against is not commit-verifiable |
| Integration adequacy | unclear pending diagnostic | cannot yet separate substrate drift from one-off variance without re-running 603q's own script fresh |
| Scale/capacity | adequate on paper | curriculum budgets match the validated reference exactly |

## Learning extracted

1. The driver's own self-diagnosis was already correct and complete -- this autopsy confirms and extends it rather than re-deriving it.
2. Configuration parity with the cited reference is confirmed line-by-line; the shortfall is not explained by a hyperparameter or curriculum-order mismatch.
3. The cited reference (V3-EXQ-603q) is itself commit-unverifiable (pre-recording-standard manifest) -- citing an old, unverifiable run as a validated performance target is a real methodological gap, independent of whether substrate drift turns out to be the actual cause here.
4. z_goal maintenance itself appears fragile across a curriculum with an extended no-goal-relevant-stimuli stretch (Stage-H + most of P1) -- worth probing directly, since (ironically) a real z_goal-decay-under-distraction phenomenon would be thematically adjacent to INV-034's own subject matter, though as currently designed it shows up as a confound inside the FULL arm rather than a clean ablation result.

## Routing (user-confirmed 2026-08-03)

**epistemic_category:** `substrate_ceiling` | **evidence_direction:** `non_contributory` (both claims) | **routing:** `/queue-experiment` a targeted **substrate-regression diagnostic**, NOT a third lettered iteration (866b) on INV-034/Q-021 itself. Concretely: (a) re-run V3-EXQ-603q's own script fresh, unmodified, on current substrate to check whether it still reproduces `base_mean_survival~37.7` today -- this isolates substrate drift from one-off seed variance without touching the INV-034/Q-021 design at all; (b) if 603q no longer reproduces its own figure, bisect the Stage-H/harm-pathway-training code path between the two dates. Per the re-derive brake: this is the first `substrate_ceiling`-stamped reading for this claim pair (count=1); if the diagnostic confirms a persistent ceiling and a further attempt on INV-034/Q-021 later routes to `substrate_ceiling` again, the brake fires and a same-claim re-queue must be refused in favour of a substrate build.

**Draft `evidence_quality_note` for governance:**
> EXQ-866a FAIL (2026-08-03), supersedes EXQ-866: G0 non-degeneracy failed AGAIN on the scaffolded_sd054_onboarding curriculum that 866's own autopsy prescribed (FULL resource_visit_rate 0.0033 < RANDOM 0.0103). Configuration verified line-by-line identical to the cited reference V3-EXQ-603q (ARM_BASE_IA_ONLY) -- same seeds, same curriculum order/budgets, same agent flags -- yet Stage-H hazard-avoidance survival (median 4-5.5/200 steps) is ~7x below 603q's cited base_mean_survival=37.7. 603q's own manifest predates the recording standard (no substrate_hash/commit), so the reference is commit-unverifiable across the 47-day gap; substrate drift is plausible but not confirmed. Separately, z_goal decays from a healthy Stage-0 peak (~0.5) to a P2 mean of only 0.12 (floor 0.4), so goal maintenance itself may not be surviving the intervening hazard-only curriculum stages. Still NOT evidence against INV-034/Q-021. Routed to a substrate-regression diagnostic (re-run 603q fresh) rather than a third lettered iteration -- v3_pending KEPT.

**User gate (2026-08-03):** Confirmed substrate-regression diagnostic as sole routing.
