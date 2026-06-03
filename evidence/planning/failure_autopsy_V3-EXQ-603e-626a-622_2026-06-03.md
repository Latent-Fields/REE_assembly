# Failure Autopsy (cluster) -- V3-EXQ-603e / 626a / 622

**Generated:** 2026-06-03T05:40:09Z
**Session:** failure-autopsy-goalstream-603e-626a-622-20260603T054009Z
**Scope:** cluster (SD-054 scaffolded-onboarding / goal-stream / goal-pipeline z_goal=0 family)
**Status:** confirmed (interactive Step 8 gate passed; user-confirmed routing + 626a disposition 2026-06-03)
**Primary targets:** V3-EXQ-603e, V3-EXQ-626a, V3-EXQ-622
**Lineage/context:** V3-EXQ-603d, V3-EXQ-626, V3-EXQ-621a
**Appendix/background:** 603a/b/c, 590a, 591, 540-series SD-054/goal-stream predecessors
**Routing (user-confirmed):** implement-substrate AMEND on `scaffolded_sd054_onboarding` (survival/foraging-competence prerequisite, NOT the now-closed goal-wiring); 626a -> non_contributory + diagnostic note.

---

## 0. Why a cluster, and what is new

All three primaries share one shape: **z_goal stays at its zero-init for the measured window**, in the SD-054 scaffolded-onboarding / goal-stream / goal-pipeline family (claims Q-045, MECH-313, MECH-260 for the 603 chain; `claim_ids=[]` diagnostics for 626/626a/622). The load-bearing new content of this autopsy is that the cluster has now **burned through three independent wiring/config/budget bugs and exposed a fourth, structural layer** that none of the prior autopsies (603, 603b, 603a-b-c-604-605, 603d, 626, 622) could see because they were dominated by the earlier layers.

This artifact supersedes the *framing* of the 603d autopsy ("wire `update_z_goal`, then re-issue at restored budget"): that wiring + budget fix landed (AMEND `deb24cc`; 603e at P0/P1=100/50) and was validated by 603e/626a as **necessary but insufficient**. The remaining gap is upstream of the goal pipeline.

---

## 1. Facts reconstruction (manifests + scripts + scheduler verbatim)

### 1a. The three primaries

| Run | run_id timestamp | purpose | outcome | claim_ids | z_goal result |
|---|---|---|---|---|---|
| V3-EXQ-622 | 20260531T223804Z | staged goal-stream decomposition diagnostic | FAIL | [] | z_goal=0; already **superseded** by 621a PASS (2026-06-01); autopsy `failure_autopsy_V3-EXQ-622_2026-06-01` exists |
| V3-EXQ-626a | 20260601T201354Z | goal-pipeline developmental-window diagnostic (re-run of 626 harness fix) | FAIL | [] | P0 positive-control: z_goal forms on **1/3 seeds** -- `arm_a_p0_z_goal_peak_per_seed=[0.0, 0.0, 0.19174]` (only seed 44); **untriaged** (`evidence_direction: null`) |
| V3-EXQ-603e | 20260603T040310Z | Q-045/MECH-313/MECH-260 4-arm + FP-2 matched-noise on scaffolded substrate (re-issue of 603d on hook-fixed scheduler) | FAIL | [Q-045, MECH-313, MECH-260] | `z_goal_norm_peak = 0.0` on **all 15 cells** incl. the 5 surviving seed-43 cells; `c4_z_goal_engaged=false`; non_contributory / SUBSTRATE_FAILURE |

### 1b. 603e detail (the decisive run)

- Three fixes vs 603d: (1) restored budget P0/P1 = 30/30 -> **100/50**; (2) config fix `z_goal_enabled=True` + `drive_weight=2.0`; (3) bespoke P2 loop now calls `agent.update_z_goal(benefit, drive)` after each `env.step` (matching the scheduler AMEND `deb24cc` + the `goal_stream_stages_sd054` reference runner).
- Result: `z_goal_norm_peak_ARM_3_max = 0.0`; **all 15 `arm_results` rows** `z_goal_norm_peak=0.0`. `p2_cell_count=5`, `aborted_cells=10` -> only seed 43 cleared the P1 survival gate (the 603-chain N=1 fragility, **reproduced at restored budget**).
- Surviving-cell diagnostics (seed 42 ARM_1, representative of the aborting seeds): P0 `mean_episode_length=24.2` on the *easy* goal-frozen P0 env, `final_running_variance=1.2e-5`; P1 `median_last_window_episode_length=18.0` < `p1_survival_gate_steps=75` -> `p1_survival_gate_failed`. The agent never develops a survival-competent policy even on the easy env at 100 P0 episodes.
- Selection-entropy ARM_2/ARM_3 = 0.70 (non-zero); ARM_0/ARM_1/ARM_4 ~ 0.002-0.006. `reef_fraction_ARM_3=0.0`; `fifo_temporal_gate_ok_all=false`.

### 1c. 626a detail (the adjudication run)

- `harness_fix_note`: "626 omitted `agent.update_z_goal()`; z_goal stayed at zero-init. 626a feeds the pipeline every step (body_state[11] benefit, 1-energy drive) in train+eval and adds a P0 positive control on ARM_A formation."
- P0 positive control was designed to adjudicate: **PASS -> 626 failure was the missing call; FAIL -> genuine formation regression contradicting 622 S0.** It **FAILED** -- `frac_seeds_clearing=0.333`, z_goal forms only on seed 44 (0.19). C1 formation-regression guard `frac_seeds_clearing=0.0`. C5 consumer-readout `dacc_per_episode_mean_per_seed=[0,0,0]`. `axis_criteria_trusted=false`.
- Interpretation: the harness fix **did** take effect (seed 44 formed z_goal where 626 had zero everywhere), but ecological formation is **gated on foraging contact** and fails on the seeds that do not forage.

### 1d. The contract that closes the wiring question

`tests/contracts/test_scaffolded_sd054_onboarding.py::test_c6_stage0_positive_control_p2_seeds_zgoal` PASSES: with a `z_goal_enabled` agent and **forced supra-threshold** benefit+drive (monkeypatched `_benefit_and_drive`), the scheduler P2 produces `z_goal_norm_peak_max > 0.0`. So the pipeline **forms z_goal under adequate input**. The ecological FAIL is an input-starvation problem, not a pipeline defect.

### 1e. Which criterion failed

PASS gate = C2 AND C4 AND C5 AND FP2. Failed class: **absolute** (C4 z_goal-engagement gate `z_goal_norm_peak_max(ARM_3) > 0.4` is 0.0), but the failure is upstream of the substrate-under-test -- a survival/foraging-competence + benefit-input prerequisite. Discrimination criteria (C2 mutually-load-bearing, FP-2 dissociation) are additionally untestable at effective N=1.

---

## 2. Claim-layer mapping

| Claim | Type | Status | Did the test let it express? |
|---|---|---|---|
| Q-045 | open_question | open, v3_pending, pending_retest_after_substrate, substrate_ceiling | NO -- coupling/independence untestable at effective N=1; z_goal never formed |
| MECH-313 | mechanism_hypothesis | candidate_substrate_landed, v3_pending, pending_retest_after_redesign | NO -- the goal-rich regime the LC-NE noise floor is meant to diversify never existed (z_goal=0); ARM_1 vs ARM_0 only readable at N=1 |
| MECH-260 | mechanism_hypothesis | candidate, v3_pending, pending_retest_after_substrate | NO -- dACC FIFO/suppression operative in surviving cells but behavioural effect unmeasurable at N=1 + z_goal=0 |

626/626a/622 carry `claim_ids=[]` -> no claim weighting either way. `claim_ids` accuracy: the 603-chain tags are correct and consistently inherited; the FAIL weighs against none of the three (it never tested them). EXQ-445h remains the sole valid MECH-260 support. **This autopsy adds a failure_record, not a reclassification.**

---

## 3. Biological-reference triage

- **MECH-313 (LC-NE tonic noise floor)** -- clear (Aston-Jones & Cohen 2005; Haarnoja 2018 SAC). Untestable here: with z_goal=0 there is no goal-directed behaviour for a noise floor to diversify away from.
- **MECH-260 (dACC anti-recency)** -- clear (Scholl & Kolling 2015; Kennerley 2006). Biology intact; fires in surviving cells.
- **Q-045 (LC-NE / dACC independence)** -- biology says coupled-not-collapsed (Tervo 2014); needs a non-degenerate, goal-engaged substrate to test.
- **The structural gap (goal-formation requires reward-contact history):** vmPFC/OFC goal/incentive representations form from the animal actually contacting/consuming rewards (Berridge wanting/liking; `benefit_exposure` is the consummatory-contact analog feeding `GoalState.update`). An agent that cannot survive/forage never accrues the reward-contact history that forms a goal representation. **The FAIL resembles exactly what happens biologically when a known developmental dependency (competent foraging / reward contact) is absent** -> a *discovered prerequisite*, not a falsification, and arguably positive evidence for the dependency.
- **Biology divergence: none.** No formal-definition import implicated; **no `/lit-pull` commission warranted** -- the biology is clear; this is a curriculum/competence gap.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | none of Q-045/MECH-313/MECH-260 under fair test; FAIL weighs against none |
| Biological reference | clear | all three mechanisms well-anchored; goal-formation-needs-reward-contact dependency well-anchored; no divergence |
| Developmental / dependency prerequisites | **missing (competence + input)** | survival/foraging competence not reached by 2/3 seeds even at restored budget; benefit_exposure stays sub-threshold for the non-foraging surviving policy in the hard P2 env -> `update_z_goal` has nothing to seed |
| Implementation completeness | **complete (this layer now closed)** | `update_z_goal` wired (scheduler P1/P2 + bespoke P2, AMEND deb24cc); `z_goal_enabled=True`; contract `test_c6` proves z_goal forms under forced input. The three prior wiring/config bugs are fixed and verified. |
| Environment adequacy | **wrong pressures for the measurement** | P2 target env `hazard_food_attraction=0.7` + food-attracted hazards suppress foraging-contact even for the surviving frozen policy -> benefit_exposure ~ 0 -> z_goal=0 |
| Measurement adequacy | partial | C4 cannot measure substrate engagement when the agent never forages; no foraging-contact-rate guard on the z_goal read |
| Integration adequacy | isolated | goal stream never integrated into behaviour because the policy never reaches the foraging-competent stage that drives it |
| Scale / capacity | **adequate (budget ruled out)** | restored P0/P1=100/50 did NOT fix survival (seed 42 P0 mean ep len 24.2; P1 median 18 < 75) -> survival fragility is a genuine curriculum/substrate property, not a budget artifact |

**Dominant diagnosis:** survival/foraging-competence + benefit-input prerequisite gap in the SD-054 scaffolded onboarding curriculum, upstream of the now-closed goal-pipeline wiring. **Recommended `epistemic_category`:** `substrate_ceiling` (unchanged; the claims already carry it -- the right response is substrate/curriculum enrichment, not more experiments on the existing substrate).

---

## 5. Cluster pattern (the load-bearing output)

| Experiment | Claim(s) | Negative-control / absolute criterion | Discrimination criteria | Read |
|---|---|---|---|---|
| V3-EXQ-603e | Q-045/MECH-313/MECH-260 | P0 builds *some* episode length for seed 43; selection entropy ARM_2/3 = 0.70 (non-zero) | C4 z_goal=0 (all 15 cells); C2 mutually-LB false; FP-2 untestable; survival 1/3 | substrate-ceiling fingerprint; absolute C4 itself fails for an upstream input-starvation reason |
| V3-EXQ-626a | none (`claim_ids=[]`) | P0 positive control fires on the foraging seed (seed 44 z_goal=0.19) | formation fails 2/3 seeds; consumer readout (dACC) = 0 | harness fix confirmed effective; ecological formation foraging-gated |
| V3-EXQ-622 | none | (superseded by 621a PASS) | -- | superseded; recorded here for cluster shape only |

**One structural property, not N independent bugs.** The three *wiring/config/budget* bugs (hook omission, `z_goal_enabled`, reduced budget) were genuinely N independent bugs and are now all fixed. What remains is a single structural property: **the SD-054 scaffolded onboarding does not bring the agent to a survival/foraging-competent policy, so neither balanced behaviour (Q-045) nor benefit-driven z_goal formation can occur.** Two live readings, both forcing the same planning decision (substrate/curriculum enrichment, not wiring and not demotion):

- **Reading A (substrate/curriculum formation gap):** the onboarding curriculum + hard P2 measurement env do not produce >=2/3 foraging-competent seeds; benefit_exposure stays sub-threshold; z_goal cannot be driven.
- **Reading B (measurement/test-design ceiling):** effective N=1 + hard measurement env make the z_goal/Q-045 read uninterpretable; a forced-benefit Stage-0 warmup + a gentler measurement env would expose whether formation is genuinely fragile.

The two are not mutually exclusive and the AMEND addresses both.

---

## 6. Learning extracted

1. **The goal-pipeline wiring layer is closed and verified.** `update_z_goal` is wired (deb24cc) and contract-proven (`test_c6` forms z_goal under forced input). The 603d/626 "Class-1 harness bug" framing no longer applies to 603e/626a.
2. **The restored budget ruled out the 603d-autopsy's budget confound.** Survival fragility (1/3 seeds) reproduces at P0/P1=100/50; it is a genuine curriculum/substrate property.
3. **z_goal=0 in 603e/626a is downstream of survival/foraging competence + benefit-input, not the pipeline.** Even the surviving seed forms z_goal=0 in the hard P2 env because a non-foraging frozen policy keeps benefit_exposure sub-threshold.
4. **Goal formation requires reward-contact history (biological prerequisite).** This is a *discovered prerequisite*, not a falsification of Q-045/MECH-313/MECH-260 -- none was under fair test.
5. **626a's P0 positive control is now informative diagnostic content:** it confirms the harness fix took effect (seed 44) AND that ecological formation is foraging-gated (2/3 fail). That answers the 626 adjudication question.
6. **A Stage-0 forced-benefit z_goal warmup that decouples formation from survival is the cheapest path to testing Q-045/MECH-313/MECH-260** at N>1 while the survival scaffold is separately strengthened.

---

## 7. Repair pathway and routing (user-confirmed Step 8 gate)

**Routing:** `implement-substrate` **AMEND** on `scaffolded_sd054_onboarding` (`action: amend`, `target_sd_id: scaffolded_sd054_onboarding`).

**Amend content (the survival/foraging-competence prerequisite -- NOT the wiring, which is done):**
- Strengthen the P0/P1 survival scaffold so >= 2/3 seeds reach a foraging-competent policy (e.g. gentler `hazard_food_attraction` anneal target during P1, longer/easier P0 foraging warm-up, or a foraging-contact reward shaping during P0) so that benefit_exposure is non-trivial and z_goal can be driven.
- Add a **forced-benefit Stage-0 z_goal warmup** that seeds z_goal independent of foraging competence, so the Q-045 / MECH-313 / MECH-260 discrimination is testable at N>1 even when survival is fragile -- and so the survival-failure and formation-failure modes are decoupled and separately diagnosable.
- For the measurement env: lower `hazard_food_attraction` during the P2 measurement window AND/OR add a foraging-contact-rate guard so a z_goal=0 read is interpretable (distinguishes "pipeline didn't fire" from "agent never foraged").
- Then re-issue 603e -> **603f** via `/queue-experiment` on the amended substrate.

**626a disposition (user-confirmed):** set `evidence_direction: non_contributory` (claim_ids=[] -> no claim-weight delta) with the diagnostic note in Section 9 JSON. Do not supersede (no 626b planned yet).

**622:** no new action -- already `superseded` by 621a; recorded here for cluster shape only.

**Draft `evidence_quality_note` for /governance (exact text; not applied here)** -- append to the `scaffolded_sd054_onboarding` substrate_queue implementation_log AND as a dated note on Q-045 / MECH-313 / MECH-260:

> "[2026-06-03 cluster autopsy V3-EXQ-603e/626a/622] The goal-pipeline WIRING layer is closed and verified: `update_z_goal` is wired into the scheduler P1/P2 (AMEND deb24cc) and 603e's bespoke P2, `z_goal_enabled=True` + `drive_weight=2.0` are set, and contract `test_c6_stage0_positive_control` confirms z_goal forms under forced supra-threshold benefit+drive. 603e (restored budget P0/P1=100/50) nonetheless FAILed with z_goal_norm_peak=0.0 on ALL 15 cells incl. the 5 surviving seed-43 cells; 626a's P0 positive control formed z_goal on only 1/3 seeds (seed 44 = 0.19). Diagnosis: z_goal=0 is now downstream of TWO coupled prerequisites upstream of the wiring -- (1) survival/foraging-competence (2/3 seeds never reach a survival-competent policy even on the easy P0 env at restored budget -> NOT a budget artifact, ruling out the 603d-autopsy confound), and (2) benefit-input starvation (a non-foraging frozen policy keeps benefit_exposure sub-threshold in the hard P2 env hazard_food_attraction=0.7, so update_z_goal has nothing to seed). Biologically a discovered developmental prerequisite (goal representations require reward-contact history; Berridge), NOT a falsification: Q-045/MECH-313/MECH-260 were never under fair test (z_goal=0 -> no goal-directed behaviour to diversify; effective N=1). non_contributory; all three stay pending_retest_after_substrate / substrate_ceiling; EXQ-445h remains the sole valid MECH-260 support. Routing: implement-substrate AMEND on scaffolded_sd054_onboarding -- strengthen the P0/P1 survival scaffold to >=2/3 foraging-competent seeds AND add a forced-benefit Stage-0 z_goal warmup that decouples formation from survival; lower P2 hazard_food_attraction / add a foraging-contact-rate guard so the z_goal read is interpretable; then re-issue 603e -> 603f."

---

## 8. Provenance

- Manifests: `evidence/experiments/v3_exq_603e_q045_mech313_mech260_scaffolded_sd054_20260603T040310Z_v3.json` (FAIL, non_contributory, SUBSTRATE_FAILURE, supersedes 603d); `v3_exq_626a_goal_pipeline_developmental_window_diagnostic_20260601T201354Z_v3.json` (FAIL, claim_ids=[], evidence_direction null, supersedes 626); `v3_exq_622_goal_stream_staged_sd054_20260531T223804Z_v3.json` (FAIL, superseded by 621a).
- Scripts: `ree-v3/experiments/v3_exq_603e_q045_mech313_mech260_scaffolded_sd054.py` (docstring lines 10-29 enumerate the three fixes; bespoke P2 z_goal seeding ~line 570).
- Substrate module: `ree-v3/experiments/scaffolded_sd054_onboarding.py` (`update_z_goal` wired at lines 668 P1 + 751 P2 via AMEND commit `deb24cc`).
- Contract: `ree-v3/tests/contracts/test_scaffolded_sd054_onboarding.py::test_c6_stage0_positive_control_p2_seeds_zgoal` (PASS under forced input).
- Substrate entry: `evidence/planning/substrate_queue.json` (`sd_id: scaffolded_sd054_onboarding`, status=implemented + AMEND `amend_implemented_pending_validation`).
- Predecessor autopsies: `failure_autopsy_V3-EXQ-603d_2026-06-01.{md,json}`, `failure_autopsy_V3-EXQ-626_2026-06-01.{md,json}`, `failure_autopsy_V3-EXQ-622_2026-06-01.{md,json}`, `failure_autopsy_V3-EXQ-603a-b-c-604-605_2026-05-29.{md,json}`, `failure_autopsy_V3-EXQ-603_2026-05-23.{md,json}`, `failure_autopsy_V3-EXQ-603b_2026-05-25.{md,json}`.
- Design/triage memos: `goal_stream_repair_diagnostic_ladder_2026-06-01.md`, `goal_pipeline_developmental_window_diagnostic_memo_2026-06-01.md`, `z_goal_collapse_triage_2026-05-31.md`.
- Substrate-readiness prior: V3-EXQ-621a PASS 2026-06-01T05:55Z (C2 z_goal floor unmet -- the early read of this same gap).
- Companion JSON: `failure_autopsy_V3-EXQ-603e-626a-622_2026-06-03.json`.
