# Failure autopsy -- MECH-341 cluster (V3-EXQ-608 + V3-EXQ-611)

- **Date (UTC):** 2026-05-29T16:56:17Z
- **Scope:** cluster (2 diagnostic runs sharing claim_ids=[MECH-341])
- **Status:** confirmed (user-confirmed at Step 8 gate 2026-05-29)
- **Routing:** implement-substrate (action=amend on existing MECH-341 substrate_queue entry; documentary close)

## 1. Cluster scoping

Two diagnostic runs sharing claim_ids=[MECH-341] with evidence_direction=non_contributory were
walked together because both carry `experiment_purpose: diagnostic` and the second
(substrate-readiness) sequentially follows the first (collapse probe) in the
behavioral_diversity_isolation_plan.md Phase P2 -> P3 routing.

| Run                                                                | Date       | Outcome | evidence_direction | Diagnostic role                                          |
|--------------------------------------------------------------------|------------|---------|--------------------|----------------------------------------------------------|
| v3_exq_608_mech341_e3_score_collapse_diagnostic_20260526T025832Z_v3 | 2026-05-26 | PASS    | non_contributory   | P2 collapse probe (substrate OFF)                        |
| v3_exq_611_mech341_substrate_readiness_4arm_20260527T130213Z_v3    | 2026-05-27 | FAIL    | non_contributory   | P3 4-arm substrate v1 readiness (substrate OFF / 3 ON arms) |

The brief described both as "FAILs"; V3-EXQ-608 is in fact outcome=PASS -- a diagnostic PASS
that confirmed the score-collapse hypothesis under test. The two share non_contributory
direction because the indexer never weights diagnostics, not because they failed criteria.

## 2. Facts (per target)

### V3-EXQ-608 (P2 collapse probe, substrate OFF)

Acceptance: cross_seed majority_label == R2a (e3_collapse_confirmed_large_gap) -> route to
substrate landing.

Per-seed labels: R2a / R2a / inconclusive_resample_heavier. Majority 2/3 = R2a, unanimous=false.

- seed 42: frac_pre_ge2=1.0; mean_top2_class_gap=0.41; score_gap_epsilon=0.078;
  frac_e3_collapse_above_eps=0.84 -> R2a
- seed 43: frac_pre_ge2=1.0; mean_top2_class_gap=0.28; epsilon=0.029;
  frac_e3_collapse_above_eps=0.98 -> R2a
- seed 44: frac_pre_ge2=1.0; mean_top2_class_gap=1.97; epsilon=1.33;
  frac_e3_collapse_above_eps=0.28; frac_near_tie_below_eps=0.72;
  n_p1_ticks=139 -> inconclusive (low n + high near-tie fraction)

PASS: routing rule applied 2026-05-27 -- substrate Options 1 (entropy_bonus) + 2
(stratified_select) landed via /implement-substrate as togglable master under MECH-341
substrate module ree-v3/ree_core/predictors/e3_score_diversity.py.

### V3-EXQ-611 (P3 substrate v1 readiness, 4-arm)

Acceptance: PASS = >= 15/18 seeds AND C1 AND (C2 OR C3). 12/12 seeds completed.

Criterion outcomes:
- C1_substrate_fires_in_on_arms: **FALSE**
- C2_arm0_reproduces_exq608_r2a: true
- C3_single_option_arm_produces_diversity: true
- C4_arm0_le_arm2_entropy: true; C4_arm2_le_arm3_entropy: true
- R2c_readiness: true

Overall FAIL because C1 (the substrate-readiness criterion specifically) failed.

Per-arm shape:

- **ARM_0 ALL_OFF** (baseline): mean_selected_class_entropy_nats=0.563; cross_seed labels
  R2a / R2a / R2b. Reproduces V3-EXQ-608 R2a finding. Substrate-OFF baseline already exceeds
  the R2c_readiness threshold (0.3) -- see process note section 7.
- **ARM_1 OPT1_only** (entropy_bonus on): mech341_n_entropy_bonus_fired equals
  n_calls_total in all 3 seeds (fires every call), BUT
  `mech341_last_entropy_bonus_max_abs` 0.023 / 0.038 / 0.044 across seeds, dwarfed by
  per-seed mean_top2_class_gap 0.41 / 0.27 / 1.96. Bonus is 1-2 orders of magnitude smaller
  than the score gap it needs to traverse. Cross-seed labels and entropy values identical to
  ARM_0 to three decimal places.
- **ARM_2 OPT2_only** (stratified_select on): mech341_n_stratified_fired=0 across all 3
  seeds despite mech341_n_calls_total in {1, 2, 20}. The substrate is called but the
  stratified_select pathway never triggers. Cross-seed labels and entropy values identical
  to ARM_0.
- **ARM_3 BOTH_ON**: composite of ARM_1 (entropy bonus too small) and ARM_2
  (stratified never fires). Cross-seed labels and entropy values identical to ARM_1.

## 3. Claim-layer map

**MECH-341** -- e3_scoring_preserves_trajectory_class_diversity. claim_type=mechanism_hypothesis,
status=candidate, v3_pending=true, implementation_phase=v3. depends_on=[ARC-065, ARC-033,
SD-003, INV-076]. Layer-B in behavioral_diversity_isolation_plan.md four-layer model.

Both diagnostics tested the claim at conditions where it could express itself
(`frac_pre_ge2=1.0` in every seed of both runs -- CEM always supplies >=2 candidate
classes, the precondition for E3 to be able to express a diversity-preserving choice).

claim_ids accuracy: both runs correctly tagged only [MECH-341]; no inherited or
companion-claim contamination. Neither run touches ARC-065 / SD-003 / INV-076 directly.

## 4. Biological-reference triage

Closest mammalian / connectome analogue: BG / cortico-striatal-thalamic loop winner-take-all
selection with downstream-action bias. The "options collapse to single deterministic ranking
under near-equal value" phenomenon is well-attested (basal ganglia indirect-pathway dynamics,
deep-RL replication of the same brittleness). But the specific "preserve diversity at the
*scoring* step rather than at proposal or action-selection" mechanism is REE-novel -- the
ARC-065 acceptance-criteria doc names this as the Layer-B gap and MECH-341 closes it.

Not a formal-definition import (no Pearl / Shannon / Bayesian-decision artifact). No targeted
biology lit-pull exists for MECH-341 specifically; this is acceptable here because the
proposed mechanisms (entropy bonus over candidate classes; class-stratified selection) are
algorithmic regulators rather than translations of a named biological mechanism. They are
analogous to LC-NE / striatal-novelty bias at the *function* level (broaden the choice
distribution) without claiming a specific cell-type substrate.

is_formal_import: false. divergence: n/a. lit_status: absent (acceptable for an algorithmic
regulator).

## 5. Four-layer diagnosis

### V3-EXQ-608 (diagnostic PASS)

| Layer                | Status            | Note                                                                                              |
|----------------------|-------------------|---------------------------------------------------------------------------------------------------|
| Claim alignment      | strengthened      | Layer-B collapse confirmed empirically -- the gap MECH-341 was registered to fill is real         |
| Biological reference | partial           | BG analogue at the function level; mechanism specifics are REE-novel                              |
| Prerequisites        | present           | CEM, per-stream V_s, anchor_sets, support-preserving CEM all in place                             |
| Implementation       | complete          | probe-only, no substrate path under test                                                          |
| Environment          | adequate          | bipartite-reef supplies spatially-distinct candidate classes                                      |
| Measurement          | adequate          | per-tick mech341 diagnostic block; frac_pre_ge2 / score_gap_epsilon thresholds correctly applied  |
| Integration          | isolated by design | probe                                                                                             |
| Scale                | adequate          | 3 seeds x (60 P0 + 40 P1) ep                                                                      |

### V3-EXQ-611 (substrate-readiness FAIL)

| Layer                | Status              | Note                                                                                              |
|----------------------|---------------------|---------------------------------------------------------------------------------------------------|
| Claim alignment      | intact              | v1-implementation check, not falsification of MECH-341                                            |
| Biological reference | partial             | same as 608                                                                                       |
| Prerequisites        | present             | 608 R2a routing applied; substrate landed before queueing                                         |
| Implementation       | partial / stub      | v1 had two distinct first-pass gaps -- see section 6                                              |
| Environment          | adequate            | same env as 608                                                                                   |
| Measurement          | adequate            | instrumentation correctly surfaced both bug shapes (entropy_bonus_max_abs + n_stratified_fired)   |
| Integration          | partially coupled   | stratified_select wiring incomplete vs uncommitted path                                           |
| Scale                | adequate            | 12 seeds x 4 arms                                                                                 |

Dominant diagnosis layer: Implementation (v1 substrate had two first-pass bugs). Recommended
`epistemic_category`: none (both runs stay non_contributory per experiment_purpose=diagnostic).

## 6. Cluster pattern (convergent table)

| Arm / Run                       | Substrate state         | Negative-control / absolute criterion         | Discrimination criterion                                                                                       | Read                                                                                                       |
|---------------------------------|-------------------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| V3-EXQ-608 (full run)           | OFF (probe)             | n/a (diagnostic)                              | R2a majority across seeds                                                                                      | **Diagnostic PASS**: collapse confirmed -> routed substrate Options 1+2                                    |
| V3-EXQ-611 ARM_0 ALL_OFF        | OFF                     | C2_arm0_reproduces_exq608_r2a PASS            | n/a (baseline)                                                                                                 | substrate-OFF reproduces 608 collapse; measurement valid                                                   |
| V3-EXQ-611 ARM_1 OPT1_only      | entropy_bonus ON        | substrate fires every call                    | C1 FAIL -- bonus_max_abs 0.023-0.044 << score_gap 0.27-1.96                                                    | **Calibration bug**: default scale=0.1 is 1-2 orders of magnitude too small for measured gap regime         |
| V3-EXQ-611 ARM_2 OPT2_only      | stratified ON           | substrate is called (n_calls_total > 0)       | C1 FAIL -- n_stratified_fired=0 x 3 seeds                                                                      | **Gating-path bug**: stratified_select gated to committed branch; P1 measurement traverses uncommitted    |
| V3-EXQ-611 ARM_3 BOTH_ON        | both ON                 | both substrate paths exercised                | C1 FAIL -- composite of ARM_1 + ARM_2                                                                          | both v1 bugs visible simultaneously                                                                        |

### Independent bugs or one structural property?

**Two independent first-pass implementation bugs in MECH-341 substrate v1**, exposed by the
same V3-EXQ-611 instrumentation. Not a single structural property of the MECH-341 claim:

1. **Calibration bug** (ARM_1, ARM_3): `e3_diversity_entropy_bias_scale=0.1` is too small
   for the measured `mean_top2_class_gap` regime. Addressed 2026-05-28 by the V3-EXQ-611b
   6-arm factorial sweep at scales {1.0, 2.0}.
2. **Gating-path bug** (ARM_2, ARM_3): `stratified_select` was gated to the committed
   branch in `e3_selector.py`; the P1 measurement window predominantly traverses the
   uncommitted path. Addressed 2026-05-28 by module change to call `stratified_select`
   on both branches (commit on ree-v3 main; 506/506 contracts PASS post-edit).

The Layer-B claim itself remains intact. V3-EXQ-608 demonstrated the collapse it predicts;
V3-EXQ-611 demonstrated that the v1 instantiation of the fix didn't actually do anything
in the measured regime. The retune addressed both. V3-EXQ-611b runner-cache reports PASS
(C1=True C3=True R2c=True, 18/18) but the manifest was lost to heartbeat autostash;
V3-EXQ-611c is the bit-identical recovery re-run already queued.

Two readings considered and rejected:
- "structural property of MECH-341" -- rejected because the bugs are at distinct call
  sites (loss-sum and selection-branch) with no shared upstream cause. Each could exist
  without the other.
- "the readiness test itself is wrong" -- partially correct (see section 7 on R2c
  threshold) but the C1 criterion correctly surfaced both bugs at the right granularity.

## 7. Process / measurement note (R2c threshold)

R2c_readiness_entropy_threshold=0.3 was cleared on V3-EXQ-611 even on substrate-OFF
ARM_0 (mean_selected_class_entropy_nats=0.563). The post-E3 selected-class distribution
is multi-modal in the absence of MECH-341 too -- the 608 R2a finding is "majority" not
"unanimous" (seed 44 R2b'd naturally). R2c_readiness is therefore not a discriminative
test of MECH-341 doing useful work at the current threshold; it should be tightened or
replaced before V3-EXQ-611c interpretation, otherwise R2.c will fire spuriously on the
recovery manifest. This is an observation, not a routing escalation.

## 8. Learning extracted

1. Layer-B score collapse is empirically real in the bipartite-reef env at default V3
   config (V3-EXQ-608 R2a confirmed). MECH-341 substrate need is justified.
2. The v1 substrate landed 2026-05-27 had two distinct first-pass implementation gaps,
   both surfaced by V3-EXQ-611's instrumentation block. This is what substrate-readiness
   diagnostics are for.
3. The 2026-05-28 retune addressed both (module change + parameter sweep). V3-EXQ-611c
   recovers the manifest the heartbeat autostash silently dropped.
4. R2c_readiness_entropy_threshold=0.3 is not substrate-discriminative; tighten or
   replace before V3-EXQ-611c interpretation.
5. Meta-pattern: first-pass substrate implementations should run a single-seed
   instrumentation-only smoke before consuming a 12-seed readiness diagnostic, to
   catch calibration / wiring bugs before they cost a run. (Filed as an observation,
   not as an action item this autopsy owns.)

## 9. Routing (user-confirmed at Step 8)

User-confirmed: "Documentary close + amend existing substrate entry."

- routing: `implement-substrate` with `action: "amend"`
- target_sd_id: MECH-341 (existing substrate_queue entry at substrate_queue.json line ~3169)
- The existing entry already carries a failure_record for V3-EXQ-611. The amend
  recommendation is documentary -- this autopsy artifact is the cluster-level diagnosis
  the existing entry's `next_step` field points at via "Await V3-EXQ-611b manifest"
  language; no new substrate gap is being filed.
- No new failure_record entry is filed for V3-EXQ-608 (it was a PASS).
- pending_retest_after_substrate: false (substrate retune already landed 2026-05-28;
  V3-EXQ-611c is the validation gate, not a future retest after a yet-to-be-built
  substrate).
- narrow_supports_flag: false.

## 10. Recommended evidence_quality_note (governance to write, not this skill)

> "2026-05-29 cluster autopsy (V3-EXQ-608 + V3-EXQ-611, failure_autopsy_MECH-341-cluster_2026-05-29):
> V3-EXQ-608 was a diagnostic PASS confirming R2a_e3_collapse_confirmed_large_gap (majority 2/3
> seeds), correctly routing substrate Options 1+2 to land 2026-05-27. V3-EXQ-611 was a
> substrate-readiness FAIL revealing two independent first-pass implementation gaps in
> substrate v1: (a) calibration -- `e3_diversity_entropy_bias_scale=0.1` produced
> `entropy_bonus_max_abs` 0.023-0.044 against observed `mean_top2_class_gap` 0.27-1.96, so
> ARM_1 substrate fired every call but could not move selection ordering; (b) gating-path --
> `stratified_select` was gated to the committed branch in `e3_selector.py` while P1
> measurement traverses uncommitted, so ARM_2 `n_stratified_fired=0` across all 3 seeds.
> Both bugs addressed in 2026-05-28 retune (module change applying stratified_select on
> both branches + V3-EXQ-611b 6-arm parameter sweep at scales 1.0/2.0). V3-EXQ-611b runner-cache
> reports PASS C1=True C3=True R2c=True (18/18) but manifest was lost to heartbeat
> autostash; V3-EXQ-611c is the bit-identical recovery re-run. MECH-341 claim itself
> intact; both failures are implementation-layer, not claim falsification. Process note:
> R2c_readiness_entropy_threshold=0.3 cleared on substrate-OFF ARM_0 too -- tighten or
> replace the metric before V3-EXQ-611c interpretation."
