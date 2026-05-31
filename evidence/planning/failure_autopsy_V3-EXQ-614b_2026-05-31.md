# Failure autopsy -- V3-EXQ-614b (MECH-341 P3 behavioural falsifier on SD-056-amended substrate)

- **Date (UTC):** 2026-05-31T18:35:08Z
- **Scope:** single (one FAIL); cluster context with predecessors V3-EXQ-614 / V3-EXQ-614a / V3-EXQ-611 / V3-EXQ-608 (MECH-341 lineage)
- **Status:** confirmed (user-verdict 2026-05-31T18:35Z at Step 8 gate)
- **Routing:** governance reclassification (no /diagnose-errors loop; no new substrate_queue entry; V3-EXQ-616 already queued)
- **Predecessor autopsy:** failure_autopsy_MECH-341-cluster_2026-05-29.{md,json}
- **Predecessor autopsy (substrate enabler):** failure_autopsy_V3-EXQ-569e_2026-05-31.{md,json} (routed the SD-056 multi-step rollout stability amend that 614b runs on)

## 1. Target and scope

V3-EXQ-614b is the substrate-amended re-run of V3-EXQ-614a (PASS_C2_C3_only, 2026-05-30T19:32Z), executing the same 3-arm MECH-341 Phase-P3 behavioural falsifier under the SD-056 amend that landed 2026-05-31T11:25Z (ree-v3 main d327b89; substrate-readiness V3-EXQ-617 PASS 11:31Z).

Single-target scope. The cluster context (614 / 614a / 611 / 608 lineage and the parallel 569e / 569d substrate work) is summarised below for routing, but this autopsy's recommendations apply only to the V3-EXQ-614b manifest. The MECH-341 cluster autopsy 2026-05-29 covered the 608 + 611 substrate-readiness pass; V3-EXQ-614b is the third entry in that lineage at the behavioural-validation layer.

## 2. Facts (manifest reconstruction)

Manifest: `evidence/experiments/v3_exq_614b_mech341_p3_behavioural_falsifier_3arm_sd056_amended_20260531T182040Z_v3.json`.

- outcome: FAIL
- evidence_direction (run-level): weakens
- evidence_direction_per_claim: {MECH-341: weakens, ARC-065: weakens}
- interpretation_label: FAIL_no_criterion_routes_to_diagnose_errors (the script's hard-coded route)
- machine: DLAPTOP-4.local
- p0_episodes=30, p1_episodes=60, steps_per_episode=200, seeds=[42, 43, 44]
- claim_ids_tested: [MECH-341, ARC-065]
- experiment_purpose: evidence
- supersedes: V3-EXQ-614a

Acceptance criteria evaluation:
- **C1** (R2.c: ARM_0 B_only Rung-1 majority): **False**
- **C2** (B necessity entropy delta >= 0.1): **False** -- observed delta = 0.087 (just below threshold)
- **C3** (ARM_2 ALL_ON Rung-1 majority): **True**

The script's decision rule `_classify_outcome(c1=False, c2=False, c3=True)` hard-routes the (False, False, True) cell to `FAIL_no_criterion_routes_to_diagnose_errors` with evidence_direction=weakens.

Per-arm shape:

| Arm | substrate axes | mean_selected_class_entropy_nats | mean_n_unique_selected | seeds_passing_rung1 | frac_pre_ge2 |
|---|---|---|---|---|---|
| ARM_0 B_only (A off, B on, C off, D off) | -- only MECH-341 on -- | **0.000** | 1.000 | 0/3 | 0.000 |
| ARM_1 ablate_B (A on, B off, C on, D on) | -- no MECH-341 -- | 0.713 | 3.000 | 3/3 | 1.000 |
| ARM_2 ALL_ON (A on, B on, C on, D on) | -- full stack -- | **0.800** | 3.333 | 3/3 | 1.000 |

ARM_0 B_only seed-level: every seed's P1 measurement window has n_p1_pre_ge2=0 (frac_pre_ge2=0.0) -- the CEM proposer collapses to single-class candidate pools every tick. With single-class pools MECH-341 has no class-level diversity to preserve (entropy_bonus is uniform across one class; stratified_select falls through to argmin under min_classes_for_stratification=2). seeds 42 / 43 / 44 lock onto first-action class 0 / 2 / 4 respectively (different lock-in classes but same monomodal-collapse signature).

ARM_1 ablate_B (no MECH-341, full upstream stack on): clean Rung-1 across all 3 seeds. mean_top2_class_gap range 0.27-1.51.

ARM_2 ALL_ON: highest absolute entropy of any 614-lineage run on record (0.800 vs 0.684 in 614a). 3/3 seeds Rung-1 PASS.

## 3. Claim-layer map

**MECH-341** -- `ethics_engine_3.scoring_trajectory_class_diversity_preservation`. claim_type=mechanism_hypothesis, status=candidate, v3_pending=true, implementation_phase=v3. depends_on=[ARC-065, ARC-033, SD-003, INV-076]. Layer-B in behavioral_diversity_isolation_plan.md.

**ARC-065** -- `architectural_commitment.behavioural_diversity_generation_pathway`. The parent distributed-diversity-generation architecture; status=candidate per the 2026-05-30 governance walk after V3-EXQ-569c matched-entropy clearance.

claim_ids accuracy: both tagged correctly. No inherited / contaminated tags. The test discriminates substrate-axis ablations, which is the right surface for both claims.

**Did the experiment test the claim under conditions where it could express itself?** Mostly yes, with one structural caveat:

- C2 + C3 (full-stack and necessity-delta) tests are valid: both arms ran cleanly, P1 measurement windows were adequate (n_p1_logged in {1288, 1268, 11806, 11423, 10676, 1739, 9383, 10009, 358, 404, 395, 1632}), and the diversity-of-action measurement is the right behavioural signal for ARC-065.
- C1 (B_only isolation) is structurally degenerate **independent of SD-056 amend**: without SP-CEM (A axis) the CEM proposer collapses to single-class candidate pools, leaving MECH-341 (a *score-layer preserver*) with no class-level diversity to act on. This is a substrate-coupling fact, not a falsification of MECH-341's claim text. Q-054 entropy_bias_scale sweep (V3-EXQ-616) tests whether higher scales can pull additional candidate classes into the pool through E3 selection feedback; pre-registered floor=8.0 as the upper end of the sweep.

## 4. Biological-reference triage

Closest mammalian analogue: BG / cortico-striatal-thalamic winner-take-all selection with downstream entropy-regulating modulation. Mnih 2016 A3C entropy regulariser at the function level for OPT1 (entropy_bonus); Rigotti et al. 2013 mixed-selectivity preservation + Padoa-Schioppa & Conen 2017 OFC value-comparison categorical preservation at the function level for OPT2 (stratified_select).

- is_formal_import: **false** (algorithmic regulators, not translations of a named biological mechanism)
- divergence: n/a
- lit_status: absent for MECH-341-specific synthesis (acceptable for an algorithmic regulator -- see MECH-341 cluster autopsy 2026-05-29 section 4)

The "FAIL" reading is not a biology-divergence finding. Both OPT1 and OPT2 are functioning as designed; what changed is the substrate's diversity-generation capacity in the *upstream* (SD-056 amend on E2 action-conditional divergence preservation) which masks MECH-341's marginal contribution at the *score* layer.

## 5. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | intact | ALL_ON cleared Rung-1 3/3 at the highest absolute entropy of any 614-lineage run (0.800 nats). C2 missed threshold by 0.013 nats. Not a falsification reading. |
| Biological reference | partial | BG analogue at function level; algorithmic regulator; no biology divergence at play |
| Prerequisites | present | SD-056 amend landed substrate-readiness 2026-05-31T11:31Z; substrate v1 retune landed 2026-05-28 |
| Implementation | complete | substrate code unchanged from 614a (only configuration: SD-056 amend levers now ON uniformly across all 3 arms) |
| Environment | adequate-but-coupling-changed | SD-054 bipartite-reef env identical to 614a / 611c / 611. The coupling change is at the substrate layer: SD-056 amend lifted upstream candidate-diversity capacity. |
| Measurement | adequate-but-threshold-stale | n_p1_ticks adequate across all arms; mech341 diagnostics fired correctly. C2 necessity_delta_threshold=0.1 was calibrated against the pre-SD-056-amend substrate and is now too tight for the amended regime. |
| Integration | coupled-and-stable | Full stack PASSes C3 at higher absolute entropy than 614a. No NaN/Inf rollouts (positive substrate-readiness evidence for SD-056 amend levers). |
| Scale | adequate | 3 arms x 3 seeds x 90 ep x 200 steps = same budget as 614a |

**Dominant diagnosis layer:** Measurement-and-environment coupling (test-design threshold + substrate-amend coupling). C2 necessity_delta_threshold=0.1 is calibrated against the pre-amend substrate; under the SD-056-amended substrate the no-MECH-341 baseline (ARM_1 ablate_B) is lifted more than the full stack, shrinking MECH-341's marginal contribution to the full stack from 0.158 to 0.087 nats. ARM_0 structural degeneracy is a separately-tracked Q-054-routed concern (V3-EXQ-616 already queued).

**Recommended `epistemic_category`:** none (manifest stays per-claim non_contributory; not a substrate_ceiling or substrate_conditional case -- the claims are V3-tractable and have already been validated at the C3 ALL_ON level on the same substrate).

## 6. Cluster pattern (lineage table)

| Run | Date | C1 | C2 | C3 | substrate config | Mean ALL_ON entropy | Read |
|---|---|---|---|---|---|---|---|
| V3-EXQ-608 (P2 collapse probe) | 2026-05-26 | n/a | n/a | n/a | substrate OFF baseline | n/a (probe) | R2a collapse confirmed -> route Options 1+2 to land |
| V3-EXQ-611 (P3 readiness v1, 4-arm) | 2026-05-27 | False | n/a | True | substrate v1 (entropy_bonus calibration too low + stratified_select gated to committed branch only) | 0.563 ARM_0 OFF | substrate v1 had two implementation bugs; retune 2026-05-28 |
| V3-EXQ-611c (P3 readiness retune recovery) | 2026-05-28 | True | True | True | substrate v2 + scale 2.0 | n/a (PASS) | retune validated; behavioural successor unblocked |
| V3-EXQ-614a (P3 behavioural falsifier) | 2026-05-30 | False | True (0.158) | True | substrate v2 + scale 2.0 | 0.684 | PASS_C2_C3_only -- MECH-341 supports + load-bearing-in-stack-only |
| **V3-EXQ-614b (P3 behavioural falsifier, SD-056 amend)** | **2026-05-31** | **False** | **False (0.087)** | **True** | **substrate v2 + scale 2.0 + SD-056 multi-step contrastive h=5 + per-step output norm clamp ratio=2.0** | **0.800** | **substrate-stable-but-isolation-still-not-clearing; near-miss against C2 by 0.013 nats** |

### Independent bugs or one structural property?

**One structural property: MECH-341 marginal contribution scales inversely with upstream diversity-generation capacity.** Across the 614-lineage:

- 614a: pre-amend substrate. Upstream stack delivers ARM_1 ablate_B at 0.526 nats. MECH-341 contribution (ARM_2 - ARM_1) = 0.158 nats. C2 PASSes.
- 614b: SD-056-amended substrate. Upstream stack delivers ARM_1 ablate_B at 0.713 nats (+0.187 nats). MECH-341 contribution (ARM_2 - ARM_1) = 0.087 nats (-0.071 nats). C2 fails the 0.1 threshold by 0.013 nats.

The SD-056 amend genuinely improves E2's action-conditional divergence preservation at the rollout horizon (the substrate-readiness it was registered to deliver per V3-EXQ-617 PASS 2026-05-31T11:31Z). That improvement reaches downstream consumers (cand_world_summaries -> SP-CEM proposer -> first-action diversity at the candidate-pool level), lifting upstream contribution to behavioural-runtime diversity. MECH-341 lives at the *score-layer* of the same diversity pipeline; when upstream supplies more raw class diversity to the pool, MECH-341 has less left to add at the scoring step. The full-stack ALL_ON value still rises (0.684 -> 0.800), but MECH-341's *marginal* contribution at the necessity-delta level shrinks.

This is a substrate-coupling reading, not a falsification of MECH-341. The full-stack diversity-generation pathway (ARC-065) still requires multiple substrates working together; ARM_1 ablate_B Rung-1 PASS shows the rest of the stack is operative, ARM_2 ALL_ON higher entropy shows MECH-341 still adds value, but the necessity-delta criterion calibrated for the pre-amend regime no longer fires.

### Two readings considered and rejected

- **"MECH-341 weakens at the behavioural layer" (the script's hard-coded reading).** Rejected: ALL_ON entropy is the highest of any 614-lineage run; the script's grid was authored before SD-056 amend landed; the 614a header_note already anticipated this cell.
- **"Substrate amend was the bug -- revert SD-056 amend levers."** Rejected: SD-056 amend's lit-anchored design (Dreamer / PlaNet / Srivastava 2021 contrastive RSSM) is architecturally correct; V3-EXQ-617 substrate-readiness PASS confirms the substrate operates as designed at its training horizon; the behavioural-layer signal (ARM_2 ALL_ON 0.800 nats) is positive evidence for the amend's downstream impact.

## 7. Learning extracted

1. **Substrate amends that benefit upstream of a tested mechanism reduce its marginal necessity-delta.** Necessity-delta tests are calibrated for a specific substrate baseline; when the substrate improves the no-mechanism arm faster than the with-mechanism arm, the delta shrinks. This is information about substrate-coupling, not about the mechanism's claim text.
2. **C2 necessity_delta_threshold=0.1 nats** in `v3_exq_614b_mech341_p3_behavioural_falsifier_3arm_sd056_amended.py` (and identical in 614a) was calibrated pre-SD-056-amend. The threshold should be revisited before any V3-EXQ-614c-type re-run on the amended substrate. The autopsy does not propose a specific new value (Q-054 sweep returns will inform the right floor); the recommendation is that successor scripts MUST not inherit the 0.1 threshold without recalibration.
3. **ARM_0 B_only structural degeneracy is a 614-lineage constant.** frac_pre_ge2=0.0 across all seeds in BOTH 614a AND 614b confirms the SP-CEM-off configuration produces single-class candidate pools every tick regardless of SD-056 amend. Q-054 entropy_bias_scale sweep V3-EXQ-616 (priority 100, already queued, scales {1.0, 2.0, 4.0, 8.0}) is the appropriate routing for the C1-isolation question; not part of this autopsy's scope.
4. **SD-056 amend behavioural-layer signal: positive substrate-readiness evidence.** ARM_2 ALL_ON delivered 0.800 nats entropy (vs 0.684 pre-amend) with zero NaN/Inf rollouts across 162k steps. This corroborates the V3-EXQ-617 substrate-readiness PASS at a different measurement horizon.
5. **Cluster lineage pattern (614a + 614b together)**: under both substrate regimes, MECH-341 contributes to the full stack but is not sufficient in isolation. The contribution shrinks as the upstream improves -- which is what a score-layer preserver should do.

## 8. Repair pathway and routing decision (user-confirmed at Step 8)

User-confirmed 2026-05-31T18:35Z via AskUserQuestion (two-question gate; both Recommended options chosen):
1. Routing: **Reclassify non_contributory, route to Q-054 sweep (V3-EXQ-616 already queued)**. Per-claim direction overrides: MECH-341=non_contributory, ARC-065=non_contributory. `pending_retest_after_substrate=true` for both, gated on V3-EXQ-616 (entropy_bias_scale sweep) AND V3-EXQ-615 (matched-entropy control) returning contributory results.
2. C2 threshold: **Flag for recalibration in evidence_quality_note**. Surface the C2 necessity_delta_threshold=0.1 calibration-drift observation in the recommended evidence_quality_note. Do not propose a specific new value; Q-054 sweep returns + ARM_0 root-cause analysis will inform the right floor.

Repair pathway: **measurement / environment / test-design adjustment** (C2 threshold recalibration) **coupled with** substrate-coupling reading (MECH-341 marginal contribution masked by upstream SD-056 amend). Routing skill is governance reclassification (not /queue-experiment -- V3-EXQ-616 already covers the Q-054 scale sweep). No new substrate_queue entry; no new EXQ; no /diagnose-errors loop.

## 9. Recommended `evidence_quality_note` (governance to write, not this skill)

> "2026-05-31 autopsy (failure_autopsy_V3-EXQ-614b_2026-05-31): V3-EXQ-614b ran the V3-EXQ-614a P3 falsifier (3 arms: B_only / ablate_B / ALL_ON; SD-054 bipartite reef env) on the SD-056-amended substrate (multi-step contrastive h=5 + per-step output norm clamp ratio=2.0, ree-v3 main d327b89). Outcome FAIL per the script's hard-coded grid: C1=False (ARM_0 B_only frac_pre_ge2=0.0 across all 3 seeds -- structural CEM proposer collapse without SP-CEM upstream, identical to 614a), C2=False at observed delta 0.087 vs 0.1 threshold (entropy_delta value just below the criterion), C3=True at 3/3 seeds Rung-1 PASS with mean entropy 0.800 nats (highest of any 614-lineage run on record vs 0.684 pre-amend). Diagnosis: SD-056 amend lifted ARM_1 ablate_B baseline by +0.187 nats (0.526 -> 0.713) vs +0.116 nats lift on ARM_2 ALL_ON (0.684 -> 0.800); MECH-341 marginal contribution shrank from 0.158 to 0.087 nats because the SD-056-amended upstream cluster (SP-CEM + V_s + noise_floor + amended E2 action-conditional divergence) is now doing more of the diversity work at the candidate-pool layer, masking MECH-341's score-layer preservation contribution. Not a falsification: ARM_2 ALL_ON ran cleanly with no NaN/Inf rollouts and the highest absolute entropy of any 614-lineage run, providing positive substrate-readiness evidence at the behavioural runtime horizon for the SD-056 amend in addition to the V3-EXQ-617 substrate-readiness PASS 2026-05-31T11:31Z. Per-claim direction override: MECH-341=non_contributory (substrate-stable-but-isolation-still-not-clearing); ARC-065=non_contributory (full-stack diversity preserved at higher absolute entropy; necessity-delta near-miss does not falsify the architectural commitment). pending_retest_after_substrate=true for both, gated on V3-EXQ-616 entropy_bias_scale sweep (priority 100, already queued, scales {1.0, 2.0, 4.0, 8.0} on B_only isolation) AND V3-EXQ-615 matched-entropy control. Process note: C2 necessity_delta_threshold=0.1 was calibrated against the pre-SD-056-amend substrate; under the amended substrate the absolute entropy values are higher and the marginal delta range is smaller. Threshold MUST be revisited before any V3-EXQ-614c successor on the amended substrate (autopsy does not pin a specific new value; Q-054 sweep returns + ARM_0 root-cause will inform). ARM_0 B_only structural degeneracy (frac_pre_ge2=0.0 across all seeds, identical to 614a) is a substrate-coupling fact at the SP-CEM-OFF configuration -- MECH-341 (score-layer preserver) cannot create pool-level diversity from a single-class CEM proposer output; Q-054 entropy_bias_scale sweep V3-EXQ-616 covers the appropriate test of whether higher scales can pull additional classes into the pool through E3 selection feedback."

## 10. Routing field for `/governance`

- **routing:** `governance-reclassification`
- **target claims:** [MECH-341, ARC-065]
- **per-claim evidence_direction overrides:** {MECH-341: non_contributory, ARC-065: non_contributory}
- **pending_retest_after_substrate:** true (both claims). Retest gated on V3-EXQ-616 AND V3-EXQ-615 returns.
- **narrow_supports_flag:** false. ALL_ON 3/3 seeds Rung-1 PASS at 0.800 nats is broad evidence, not narrow / single-pathway support.
- **no new substrate_queue entry:** V3-EXQ-616 already queued under EVB-0284 / EXP-0273 (Q-054 entropy_bias_scale sweep on B_only isolation). V3-EXQ-615 (matched-entropy control) also already queued. No new substrate gap surfaced.
- **no /diagnose-errors loop:** the FAIL is a substrate-coupling + test-design-threshold artifact, not an instrumentation bug.
