# Failure autopsy: V3-EXQ-1073 (diagnostic PASS) -- precision-provenance-conditioned consolidation gain

**Generated:** 2026-09-22T18:39:38Z, session `compassionate-pike-fe9174` (the session that designed, built and queued the run; adjudicated against its own preregistration section 12 and freeze record section 15).
**Run:** `v3_exq_1073_mech572_precision_provenance_gain_20260922T182856Z_v3`, ree-cloud-2, 73.1 min, seeds 42/123/456, 72 cells.
**Self-route label:** `confidently_wrong_condition_unposeable_on_this_head` (outcome PASS on validity G1-G7).
**Claims:** MECH-572. **Purpose:** diagnostic, `non_contributory` by design (preregistration section 14).
**Status:** CONFIRMED at the Step 8 gate (2026-09-22T19:01:15Z). User decision: routing confirmed AND SD-PP-B5 escalated to /implement-substrate now.

## 1. Facts (Step 2)

Dry-run gate: `check_dry_run_citations.py` over the run_id and queue_id -- 0 dry cited, 1 clean. Recording provenance: `validate_recording.py` OK (always-core complete, substrate_hash present). Coverage: no prior autopsy covers V3-EXQ-1073.

Validity gates (all route PASS/FAIL, all passed): G1 liveness 5/5 rungs increasing; G2 arms bit-identical pre-sleep (world buffer, world-head params, action buffer, RNG state, all six arms, all cells); G3 evidence channel varies (noise ratio 0.0022/0.0084/0.050 < 0.25; sigma_obs equal at the floor between clean conditions); G4 pi_hist varies (sd min 4.76); G5 pi_cur converged/underfit 4628x/887x/3518x; G6 baseline displaces 0.00794; G7 readouts vary.
Non-degeneracy markers: G1b consumer live (ARM C step scale deviates from unity by 0.94); G3b kappa alias 0.58/0.07/0.28 (<= 2.0) pass; **G4b FAIL** (cond-3 early surprise fraction 0.033 vs >= 0.5); **G8 FAIL** (skill vs identity predictor -0.071/+0.227/-0.007, 1/3 seeds > 0); **G9 FAIL** (cond-3 waking PE / converged residual 0.745/0.677/0.674 vs > 2.0).

Per-cell retention (post/pre - 1 on the R0 battery; A == B bitwise in every cell):

| condition | A/B | C provenance | C-nohist | D-global (c_seed 0.45/0.34/0.52) | D-residual |
|---|---|---|---|---|---|
| converged clean | 9.72 / 61.9 / 52.6 | 0.47 / 1.31 / 0.82 | 0.38 / 0.81 / 0.04 | 3.78 / 8.23 / 16.3 | 0.13 / 1.01 / 0.20 |
| underfit | -0.39 / 0.05 / -0.44 | -0.25 / -0.11 / -0.67 | -0.14 / -0.16 / -0.67 | -0.28 / 0.01 / -0.33 | -0.55 / -0.08 / -0.66 |
| confidently wrong (R0) | 45.6 / 39.1 / 48.1 | 0.46 / 0.29 / 0.44 | 0.44 / 0.25 / 0.94 | 8.4 / 6.5 / 15.3 | 3.47 / 0.40 / 0.25 |
| noisy contradiction | 4.62 / 20.6 / 97.2 | -0.01 / 0.19 / 1.06 | -0.02 / 0.13 / 1.00 | 7.66 / 5.61 / 25.3 | 0.22 / 0.26 / 0.65 |

Correction on the inverted-rule battery (cond 3, (pre - post)/pre): A/B -62/-46/-54; C -1.12/-0.46/-0.62; D-global -11.9/-8.0/-17.1; D-residual -5.0/-0.66/-0.36. The inverted-rule battery's PRE-sleep MSE is LOWER than the original rule's on every seed (G9 ratios above): the head does not read the action.

Realised gains: A/B 1.0 (displacement 0.0079-0.0081 = the 8*lr Adam bound, 12/12 cells); C 0.043-0.083 (converged / cond 3 / cond 4), 1.22-1.87 (underfit); D-residual 0.040-0.098 and 1.02-1.58; D-global 0.34-0.52 uniform. Budget ratios D-global/C: 5.9-10.6x (converged), 6.3-7.2x (cond 3), 8.8-16.7x (cond 4), 0.27-0.28x (underfit). D-residual/C: 0.68-1.09 (converged), 0.54-1.40 (cond 3), 0.99-1.91 (cond 4).

Contrasts (P1-P7 route no verdict): P1 pass (exact zero); P2 relative pass 3/3 (C ret below B by 40.5 +/- 27.4) -- marked non-degenerate=False by G8; P2b (absolute 10% bar) fails 3/3 (0.47/1.31/0.82); P3 pass 3/3 (C learns at least as well on the underfit base); P4 fail and non-degenerate=False (unposeable); P5 fail (C vs D-residual on the noisy channel: +0.03 +/- 0.33) and non-degenerate=False; P6 protection leg pass 2/3, correction leg degenerate, marked non-degenerate=False; P7 fail (C vs C-nohist 0.10 +/- 0.26) and non-degenerate=False.

## 2. Claim layer (Step 3)

MECH-572 (candidate, v3_pending, standard, no epistemic_category field, depends_on SD-017): asserts the across-sleep sign is governed by the displacement-to-residual ratio; CONFIRMING requires a non-negative delta on >= 2/3 seeds at conv_rel_drop >= 0.99 with the head above the trivial predictor; P-FAIL converts to substrate_conditional if no such setting exists. This run REPRODUCES the mechanism (displacement pinned at the bound on 12/12 baseline cells; the worsening scales monotonically with the step scale across 1.0 -> ~0.45 -> ~0.05 on 3/3 seeds) but reaches NO non-negative delta and the base clears the trivial predictor on 1/3 seeds only. Claim alignment: intact; direction non_contributory by design; no verdict. The claim_ids tag is accurate (the run exercised exactly MECH-572's mechanism). The intake's three candidate formulations are NOT registered claims and this run does not support registering them.

## 3. Biological-reference triage (Step 4)

Closest mechanisms: confidence-weighted belief updating (Meyniel & Dehaene 2017), CA1 mismatch scaled by prediction strength (Chen 2015), tagging/eligibility (Takeuchi 2016), sleep as a separate gain regime (Swift 2018, Feher 2026). Literature: present (intake 2026-09-22, 15 references; targeted_review_inv_063 entries 2026-09-22). The Kalman-form K_i is a formal import standing in for precision-weighted PE; the run shows it acts (K ~0.44 under noise vs ~1.0 elsewhere) but that acting bought no retention advantage over a current-residual scheduler at this operating point. The failure signature -- nothing to reopen because the model never held a falsifiable belief -- is the missing-dependency shape: the reference mechanism presupposes a world model that predicts the consequences of action, which this head does not (B5).

## 4. Four-layer diagnosis (Step 5)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | mechanism reproduced; CONFIRMING not reachable on this base |
| Biological reference | partial | class supported; load-bearing half untestable here |
| Prerequisites | missing | B5 (head ignores the action; copy-the-input), B1 (no behavioural consumer) |
| Implementation | complete | SD-PP-1..4 live, A/B neutral, consumer live, rule factor-by-factor as pre-registered |
| Environment | too sparse | one-cell moves -> identity MSE ~1e-5; no reliable contradiction available |
| Measurement | adequate | all pre-registered readouts recorded; markers flagged the unreadable contrasts |
| Integration | coupled but inert BY DESIGN (reopen factor; behavioural path) | r_i ~1 because surprise ~1; no E3 consumer of e2.world_forward |
| Scale | representation-range insufficient (B5) | training budget adequate |

Failure-location (GOV-FAILLOC-1): MECHANISM established, MEASURES established, ENVIRONMENT not established (plus a prerequisite gap) -> **not chargeable to REE**; net ENVIRONMENT + PREREQUISITE. The inert reopen factor is inert by DESIGN at this operating point (no contradiction to interpret), so Implementation stays `complete`.

Recommended `epistemic_category`: **standard** (the run says nothing suppressive about MECH-572; the diagnosis lives in the note). `recommended_diagnostic_evidence_adjudicated: true`. `pending_retest_after_substrate: true` (B5, B1).

## 5. Learning extracted (Step 7)

1. MECH-572's phenotype and mechanism reproduce on 3 seeds; the worsening tracks the step scale monotonically.
2. Storing provenance is bitwise neutral (SD-PP-3 validated).
3. Provenance NOT shown to add information beyond a current-residual scheduler at this operating point (R2-shaped): prefer the simpler mechanism until a use case demonstrates provenance value.
4. Historical precision inert because no contradiction existed; the reopen factor is only testable where one does.
5. Condition 3 is unposeable on this head (B5), measured on 3 seeds -- an instrument record, not a null; it blocks the intake's hardest test and MECH-572's own CONFIRMING clause.
6. The pre-freeze channel probe caught three warm-up/statistic gate failures before the run; calibration window + estimator state are now substrate.
7. No recording gap: budget ratios, per-step gains and packet distributions are in the manifest.

Granularity-debt trigger: does NOT fire (0 tagging targets for MECH-572). Re-derive brake: 0 prior counting hits; this target is `standard` with an instrument/prerequisite marker and does not count.

Node class: `complicated (buildable)` for B5's remedy (a world head that reads its action / an action-sensitivity readiness gate) and B1 (a canonical behavioural consumer); `complex (probe-gated) / mystery (known data)` for whether provenance can add value at all -- the data exist, the frame (an action-blind head) is wrong, more runs on this head will not settle it.

## 6. Routing (Step 7) -- proposed, pending the Step 8 gate

**governance**, no re-queue at this granularity. `recommended_substrate_queue_entry`: **amend SD-PP-B5** with this run's failure record (G9 0.745/0.677/0.674; G4b 0.033; inverted-rule battery MSE below the original's on 3/3 seeds), severity `degrading`, paths `e2_fast.py::world_forward`, `latent/stack.py`. Governance also owes: apply the MECH-572 per-claim recommendation; mark SD-PP-1..4 validated (this run is their Step 8 validation); resolve GFLAG-0413; do not register the intake's candidate claims; the organism-level follow-up on B1 is governance's chip.

7b pre-routing checks: one fire, C7 (`conv_rel_drop` bit-identical across arms within a seed) -- DISMISSED: it is a property of the cached P0 base the pairing design asserts equal across arms, not a discrimination criterion; the discrimination criteria are the P contrasts and they vary across arms in every cell.

7c red-team (Opus, cross-model; session on Fable): **CONTESTED**, all findings accepted -- see the JSON `red_team.dispositions`. The load-bearing one: the driver bound the flat readout flags p3..p7 by position after P2b was inserted, so the LANDED manifest's `readout.p3..p7` and its `evidence_direction_note` counts are shifted by one (published P4 3/3, true P4 0/3; published P3 0/3, true 3/3; P6 2/3 true; P7 1/3 true). `interpretation.criteria[]` and the label are unaffected. Driver fixed at source (bind by name) the same day; no re-run needed. Corrections applied: the battery statistic (inverted-rule pre-sleep MSE 0.760/0.901/0.881x the original; G9 0.745/0.677/0.674 is waking pe / residual); P5/P7 no longer cited (non-degenerate); P3 3/3 cited; K under noise 0.525/0.588/0.570 (0.44 was the pre-run probe); displacement linear but retention non-monotone above scale 0.5; MECH-572 already carries epistemic_category standard, so the change tail is diagnostic_evidence_adjudicated: true; MECH-572's CONFIRMING needs no contradiction and P-FAIL is NOT triggered (seed 123 readable; ladder reached ret -0.044 at scale 0.02) -- a readable-seed step-scale ladder, optionally with SD-PP-B8, is the cheap next MECH-572 test; failure-location net MIXED (4/6 degenerate contrasts charge to G8, the head's readability).

**Corrected reading of the science:** the intake's causal question is UNANSWERED at this operating point, not answered negatively. The readable yield is P1 (storage neutral), P3 (still learns on an underfit base) and the mechanism descriptives; R1/R2/R3/R7 are not reached.

**Step 8 user decision:** routing confirmed; **SD-PP-B5 escalated to /implement-substrate now** (a world-forward head that reads its action / action-sensitivity readiness gate). Chip spawned by this session on that instruction; the B5 substrate_queue row set ready:true citing the decision.

## 7. Hypothesis ledger (Step 9b) -- proposed

Existing question `inv063_legb_sleep_worsens_converged_dv` (no growth restriction): resolve H-step-scale and H-dv-headroom as `alive` with this run as a resolving run and a basis (supported directionally; not confirmed because the P2 contrast is non-degenerate=False under G8). New question `precision_provenance_consolidation_gain` (claims MECH-572), pre-registered 2026-09-22T15:xx by the preregistration commit and resolved by this run: H-provenance-beyond-generic (R1) alive (P6 non-degenerate=False; P5 fails), H-generic-gain-sufficient (R2) alive with basis (Dr matches C where readable; G8), H-self-sealing (R3) alive (unposeable). Observation bottleneck: B5 + MECH-573 readability + B1.
