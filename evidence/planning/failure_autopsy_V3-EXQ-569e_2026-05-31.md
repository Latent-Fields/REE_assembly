# Failure Autopsy: V3-EXQ-569e

**Date:** 2026-05-31T10:45:00Z
**Scope:** single target
**Status:** confirmed
**Target:** V3-EXQ-569e (SD-056 Pathway A vs Pathway B mechanism probe; ARC-065 / MECH-341)
**Run ID:** v3_exq_569e_sd056_mechanism_probe_pathway_a_vs_b_20260531T004944Z_v3
**Manifest:** REE_assembly/evidence/experiments/v3_exq_569e_sd056_mechanism_probe_pathway_a_vs_b_20260531T004944Z_v3.json
**Script:** ree-v3/experiments/v3_exq_569e_sd056_mechanism_probe_pathway_a_vs_b.py
**Predecessor / parallel sibling:** V3-EXQ-569c (failure_autopsy_V3-EXQ-569c_2026-05-30) and V3-EXQ-569d (floor-recalibrated falsifier; queued alongside 569e same session 2026-05-30T17:00Z)
**Routing (user-confirmed 2026-05-31):** `/implement-substrate` amend SD-056 for numerical stability + three script-side acceptance-criteria fixes; per-claim direction stays mixed (diagnostic, non-weighting); 569c headline remains the load-bearing finding

---

## 1. Facts (no interpretation)

### Verdict-cell short-circuit fired

```
verdict_cell: INSTRUMENTATION_FAILURE
overall_pass: false
m3_max_nan_fraction_on_arms: 0.8915    (ceiling: 0.4)   --> triggered
```

### Acceptance criteria as reported (versus what the numbers actually say)

| Criterion | Reported | What the numbers say | Disagreement? |
|---|---|---|---|
| C1 (M3 NaN-fix instrumentation) | **PASS** | At least 3 seeds per ON arm had at least 1 finite top2_gap value. But across-tick `top2_class_gap_nan_fraction` is 0.72-1.00 on most ON-arm seeds (ARM_1 seed 43 = 1.0; ARM_2 seed 43 = 1.0; ARM_3 seed 43 = 1.0; ARM_4 seed 43 = 1.0). NaN is endemic, not fixed. | **Yes** -- the C1 gate is too weak |
| C2 (M4 frozen-vs-live discriminative) | **FAIL** | abs(c3_live - c3_frozen) = 0.033 (floor 0.05); frozen_pres delta from unity = 0.099 (floor 0.25). M4 axis cannot discriminate because both live AND frozen arms inherit the same E2 pathology from P0 training. | No |
| C3 (M1 rollout-divergence operative) | **PASS** | rollout_ratio_on_vs_off = 3.793881119125856e+16; rollout_amp_ratio_live = 2.490806312828144e+17. ARM_0 OFF baseline = 0.523 (clean). ON-arm rollout means are 1.98e+16 (ARM_1) and far higher in spikes. These are **numeric overflow**, not large divergences. | **Yes** -- the C3 gate has no sanity ceiling |
| C4 (verdict definite) | **FAIL** | verdict_cell short-circuit correctly fires INSTRUMENTATION_FAILURE | No |

### Per-arm rollout magnitudes (mean pairwise L2 over candidate trajectories)

| Arm | Category | mean rollout dist | rollout_skipped_nonfinite (typical seed) |
|---|---|---|---|
| ARM_0 OFF | off | 0.392 - 0.774 | 0 |
| ARM_1 W=0.05 LIVE | live | 0 to 6.06e+16 | 1950 - 3478 |
| ARM_2 W=0.20 LIVE | live | 0 to 9.87e+16 | 863 - 3496 |
| ARM_3 W=0.05 FROZEN | frozen | 1.39e+16 - 1.49e+16 | 0 - 3478 |
| ARM_4 W=0.20 FROZEN | frozen | 8.78e+14 - 1.39e+16 | 0 - 3496 |
| ARM_5/6 ARGMIN | argmin | 0 / 1e+16 spread | 2860 - 3478 |
| ARM_7 NOISE | noise | 0.522 | 0 |

`e3_top2_class_gap` mean values on ON arms range from 4.7e+32 to 1.08e+36 with NaN-fractions 0.72 to 1.00; on OFF / NOISE arms the values are O(1) with NaN-fraction 0.

### Per-arm selected-action entropy (the C3 axis 569c headline pointed at)

| Arm | selected_action_class_entropy |
|---|---|
| ARM_0 OFF (T=1.0) | 0.432 |
| ARM_1 W=0.05 LIVE | 0.711 |
| ARM_2 W=0.20 LIVE | 0.829 |
| ARM_3 W=0.05 FROZEN | 0.786 |
| ARM_4 W=0.20 FROZEN | 0.821 |
| ARM_5 W=0.05 ARGMIN | 0.711 |
| ARM_6 W=0.20 ARGMIN | 0.829 |
| ARM_7 NOISE (T=2.5) | 0.432 |

`on_c3_lift_above_noise = 0.337` (floor 0.30). The C3 signal exists in selected-entropy, but the **mechanism** (Pathway A per-candidate variance vs Pathway B rollout-landscape shift) cannot be read off the data because the M1/M4/M5 channels that distinguish them are saturated/NaN.

### Operational notes

- Contrastive_loss across ON arms means 1.93 - 1.98 (range 1.51 - 5.52); ln(K=8) = 2.08. Head sits just below random baseline.
- `frozen_at_p1_event = true` on ARM_3 / ARM_4 all seeds (the frozen-at-P1 ablation fired as designed).
- The script's `_evaluate` block's gate at line 1110 correctly catches the failure mode: `(not c1_pass) OR (m3_max_nan_frac_on >= M3_NAN_FRAC_CEIL) OR (not c3_pass) OR (on_c3_lift < ON_LIFT_C3_FLOOR) -> INSTRUMENTATION_FAILURE`. The second clause (max-NaN gate at 0.4) is what fires; C1 and C3 nominally PASS but the short-circuit overrides them. This means **the script knew** the experiment was broken; the contradiction is only in the surfaced `acceptance_criteria` dict.

---

## 2. Claim-layer mapping

### ARC-065 (parent architectural commitment; candidate; v3_pending=true)

`behavioral_diversity_generation_pathway`. The 569 family tests SD-056 (Layer A; E2 action-conditional contrastive next-state divergence preservation) as a child substrate within ARC-065. 569e was designed as a parallel diagnostic to 569c that dissociates **Pathway A** (per-candidate z_world variance propagation through E3 softmax routing) from **Pathway B** (E2 rollout dynamics shift producing a different scoring landscape) as the source of 569c's ~2.4x C3 lift over the matched-noise control.

- Conditions to express: SP-CEM main-path ON, MECH-341 OFF, MECH-313 OFF, MECH-269 default. Confirmed by per-arm config.
- **The substrate had a fair chance to express.** The probe did not. The reason the probe didn't express is **substrate-implementation** (SD-056 numerical instability at behavioural-runtime episode lengths), not claim falsification.
- 569c's C3 finding (~2.4x lift) stands as the load-bearing reading on this surface; 569e cannot add to or subtract from it.

### MECH-341 (Layer-B child; candidate; v3_pending=true)

`e3_scoring_preserves_trajectory_class_diversity`. Tagged on 569e because the M3 / M5 channels were designed to dissociate "E3 aggregation collapsed upstream variance" (a MECH-341 weak-reading consequence) from per-candidate variance propagation. Same conclusion as ARC-065: the probe did not dissociate; 569c's substrate-readiness on this axis (retune validated 2026-05-29 V3-EXQ-611c) is what currently grounds MECH-341 substrate-side.

### claim_ids accuracy check

claim_ids = [ARC-065, MECH-341] inherited from 569c (the script docstring documents this explicitly and the autopsy of 569c confirmed the inheritance was appropriate for the matched-entropy falsifier design). 569e is a parallel diagnostic in the same family; the inheritance carries.

---

## 3. Biological-reference triage

### SD-056 closest mechanism

Cerebellar internal model preserving action-specificity (Tanaka et al. 2020); prefrontal counterfactual rollout (Miyamoto / Rushworth / Shea 2023); vestibular cerebellum corollary discharge (Cullen 2023). Mammalian forward models preserve action-conditional discriminability at the prediction step through structural mechanisms (cerebellar microcircuits, PFC counterfactual rollouts, corollary-discharge cancellation). REE's SD-056 is a **faithful biological translation** of this prerequisite, not a formal-definition import.

**lit_status: present** (REE_assembly/evidence/literature/targeted_review_e2_forward_model_action_divergence/SYNTHESIS.md; conf 0.78-0.82; SD-056 substrate landed 2026-05-29).

**Biology comment on numerical instability:** the cerebellum / PFC counterfactual circuitry doesn't simply scale up contrastive contribution magnitudes -- there are gain-control loops (climbing-fibre PE normalisation, dopaminergic modulation, neuromodulator-mediated learning-rate decay) that keep the next-state prediction in a bounded operating regime. REE's SD-056, as implemented, lacks the analogous arithmetic guards (gradient clipping, output norm clamping, contrastive weight scheduling) and is structurally vulnerable to the explosion observed here. This is the missing-prerequisite signature the autopsy reads on.

### MECH-341 closest mechanism

Mixed selectivity in PFC (Rigotti et al. 2013); OFC value comparison preserving option-distinct value signals (Padoa-Schioppa & Conen 2017). Biology preserves trajectory-class diversity through dedicated structural circuits at the scoring step. Substrate-readiness already validated (V3-EXQ-611c PASS).

### Verdict

**Biology supports the architectural class of mechanism SD-056 instantiates.** It does NOT support the current implementation's lack of arithmetic stability guards. Failing this probe IS evidence the implementation is incomplete; it is NOT evidence the architectural claim is wrong.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | Probe could not express; the 569c headline (~2.4x C3 lift) remains the load-bearing finding |
| Biological reference | clear | Cerebellar / PFC forward-model preservation; lit-pull complete |
| Prerequisites | present | SP-CEM main-path landed (2026-05-15); MECH-341 substrate landed + retune-validated (2026-05-27 / 2026-05-29); SD-056 substrate landed (2026-05-29) |
| Implementation | **partial / unstable** | SD-056 contrastive training, as implemented, produces numerically explosive `E2.world_forward` rollouts on most ON-arm seeds over the behavioural-runtime episode budget. Substrate-readiness V3-EXQ-613 PASSed at short-scale training-only; instability emerges at longer episode lengths |
| Environment | adequate | CausalGridWorldV2 12x12 + 4 hazards + 5 resources + reef substrate is the validated env for this family |
| Measurement | **inadequate** | Every measurement channel (M1 rollout, M3 NaN-fix, M4 frozen-vs-live, M5 argmin) depends on finite E2/E3 outputs. Substrate explosion saturates all four. Plus: C1 acceptance gate is too weak; C3 acceptance has no sanity ceiling; acceptance_criteria dict surface contradicts the (correct) verdict_cell short-circuit |
| Integration | partial | Substrate operates cleanly alone short-scale; breaks at the integration point of (sustained P1 training + long-horizon rollout for M1 measurement) |
| Scale | likely insufficient | Substrate-readiness validated at short-tick counts only; instability is scale-dependent |

**Recommended epistemic_category:** `standard` with `substrate_action=amend`. NOT `substrate_ceiling` -- this is implementation pathology (numerical instability), not a flat substrate ceiling. NOT `substrate_conditional` -- the substrate exists and works at short-scale.

---

## 5. Cluster note (single autopsy, but cross-cluster comparison)

569e is **distinct in shape** from the substrate-uniform cluster (V3-EXQ-540a/b/c/e + 603/603b/603c + 590a + 591 + 598/598b) named by the EXQ-591 + EXQ-598 autopsies. That cluster has the "negative-control passes, discrimination fails on every criterion" substrate-ceiling shape: substrate carries information, just not at the granularity the claims require. The 569e shape is different: substrate is **numerically explosive**, OFF baseline is clean, ON arms produce 1e16+ overflow. This is implementation pathology, not a substrate ceiling.

Do **not** fold 569e into the substrate-uniform cluster. The corrective action is amend-the-implementation, not enrich-the-substrate.

(569d, sister floor-recalibrated falsifier queued alongside 569e same 2026-05-30 session, will likely show the same instability when its manifest lands -- in which case 569d should attach to this autopsy rather than spawn its own.)

---

## 6. Learning extracted

1. **SD-056 substrate-readiness must validate at behavioural-runtime episode length, not just short-scale training-only.** V3-EXQ-613 PASS was insufficient evidence the substrate would hold up at 200-step / 50-episode P1 measurement windows. Future contrastive-loss substrate landings should include a long-horizon rollout stability check in UC3.

2. **Contrastive training on `world_forward` lacks arithmetic guards.** Gradient clipping on `world_transition` / `world_action_encoder`, output norm clamping on `world_forward`, or a `contrastive_weight` decay schedule are standard ML/AI engineering complements to InfoNCE-style auxiliary losses. The SD-056 implementation went straight to the literature-default formulation without these guards (consistent with the substrate-readiness signal being clean at short-scale).

3. **Diagnostic-probe acceptance criteria need defensive design.** Three concrete fixes for the 569e script (and a template for future diagnostic probes in this family):
   - **C1 should gate on max-NaN-fraction directly**, not on count-of-seeds-with-any-finite-value. The current gate ("at least 3 seeds with at least 1 finite top2_gap") is too weak.
   - **C3 should sanity-cap rollout magnitudes** to FAIL on overflow. A "rollout ratio of 3.8e16" should never read as success; cap meaningful rollout amplitudes (e.g. fail when `rollout_traj_pairwise_dist_max > 100x` ARM_0 baseline).
   - **acceptance_criteria dict should mirror verdict_cell short-circuit logic.** The verdict_cell correctly classified INSTRUMENTATION_FAILURE but C1/C3 acceptance flags read PASS. Internal manifest contradiction; the consumer-facing acceptance fields should reflect the same conclusion as the verdict cell.

4. **The 569c autopsy routing needs revision.** 569c's routing proposed 569d + 569e to dissociate Pathway A vs B. 569e cannot do that on the unstable substrate. The correct sequence is: amend SD-056 first; then re-run a 569e-equivalent (call it 569f or 569e-prime) on the stable substrate; then read the Pathway A vs B verdict.

---

## 7. Repair pathway and routing recommendation

**Primary routing:** `/implement-substrate` **amend SD-056** for numerical stability under sustained contrastive training at behavioural-runtime episode lengths.

Concrete amendment shopping list (the implement-substrate skill will pick the right combination based on its lit-pull + R-verdicts):

| Lever | Where | What |
|---|---|---|
| Gradient clipping | `world_transition.parameters()` and `world_action_encoder.parameters()` in the E2 contrastive-loss training step | torch.nn.utils.clip_grad_norm_ with literature-default max_norm (1.0 is typical for InfoNCE; the lit-pull verdict will name the operating value) |
| Output norm clamping | `world_forward` output, post-residual-add | Clamp predicted z_world_1 norm to a multiple of z_world_0 norm (e.g. 5x) to prevent runaway delta predictions |
| Contrastive-weight schedule | `e2_action_contrastive_weight` in E2Config | Either anneal from 0.0 -> 0.01 over warmup, or decay to 0.0 after a fixed step count if NaN-rate climbs above a floor |
| Temperature floor | `e2_action_contrastive_temperature` | Raise from 0.1 to a higher floor (e.g. 0.5) to soften the InfoNCE logits and reduce gradient explosion sensitivity |

The lit-pull on the substrate amendment should look at the same SD-056 SYNTHESIS family (Srivastava 2021 contrastive RSSM training stability; Saanum / Dayan / Schulz 2024 PLSM failure modes; Qiu 2026 SWIRL gradient-clipping defaults) plus the cerebellar gain-control biology (climbing-fibre PE normalisation, dopaminergic learning-rate modulation) for the structural prerequisite.

**Secondary routing (queued AFTER the amend lands and a successor substrate-readiness EXQ PASSes at behavioural-runtime scale):** `/queue-experiment` for a 569e-equivalent Pathway A vs B probe on the stable substrate. The script body is reusable; only the substrate config needs updating to enable the amended SD-056 implementation.

**Tertiary routing (separate session, low priority):** `/queue-experiment` script-fix iteration of `v3_exq_569e_*` with the three acceptance-criteria fixes from Section 6. Could be bundled with the 569e-equivalent re-run.

### Draft `evidence_quality_note` for governance to apply (per claim)

**ARC-065:** "V3-EXQ-569e Pathway A vs Pathway B mechanism probe verdict INSTRUMENTATION_FAILURE 2026-05-31. SD-056 contrastive training produced numerically explosive E2 rollouts (1e16+) on most ON-arm seeds at the behavioural-runtime episode length; verdict cells M1/M3/M4/M5 all saturated. Probe could not dissociate. Substrate implementation pathology (lacks gradient clipping / output norm clamping / contrastive weight schedule), not architectural claim falsification. Routed to /implement-substrate amend SD-056 for numerical stability; ARC-065 reading from V3-EXQ-569c (~2.4x C3 lift over matched-noise control) remains the load-bearing finding pending the amend-and-re-run cycle."

**MECH-341:** "V3-EXQ-569e diagnostic INSTRUMENTATION_FAILURE 2026-05-31; M3 / M5 channels intended to dissociate E3-aggregation-collapsed-upstream-variance vs per-candidate variance propagation were saturated by SD-056 numerical instability. MECH-341 substrate-side reading from V3-EXQ-611c retune PASS (2026-05-29) remains valid; 569e adds no new MECH-341 evidence in either direction."

### Recommended substrate_queue write (action=amend)

`target_sd_id`: SD-056. The substrate_queue entry for SD-056 (or its in-flight follow-on if one exists) gets a `failure_record_entry` capturing:

- run_id: `v3_exq_569e_sd056_mechanism_probe_pathway_a_vs_b_20260531T004944Z_v3`
- experiment_type: `v3_exq_569e_sd056_mechanism_probe_pathway_a_vs_b`
- metric: SD-056 contrastive training numerical stability under sustained P1 (50 episode / 200 step) measurement. Observed: `world_forward` rollout magnitudes overflow to 1e16-1e18 on most ON-arm seeds; `e3_top2_class_gap` NaN-fraction 0.72-1.00 on ON arms; ARM_0 OFF baseline clean (0.39-0.77 rollout magnitudes, 0 NaN). M1 rollout-divergence ratio = 3.79e16 (overflow); M3 max NaN fraction = 0.89 (vs ceiling 0.40); M4 frozen-vs-live and M5 argmin discrimination axes both contaminated.
- target: amended SD-056 implementation produces clean (max-NaN-fraction < 0.05, rollout magnitudes within 2x of ARM_0 baseline) E2 rollouts on a 569e-equivalent 8-arm probe across 5 seeds at the same P1 measurement budget.

`priority_suggested`: 1 (substrate gap blocks the ARC-065 GAP-A behavioural diversity validation surface that the 569 family is the central probe for).

---

## 8. Routing decision (user-confirmed via AskUserQuestion 2026-05-31T10:45Z)

- Primary: `/implement-substrate` amend SD-056 for numerical stability. **(user confirmed Recommended option)**
- Script-side fixes flagged: all three (C1 too weak; C3 needs sanity ceiling; acceptance_criteria should mirror verdict_cell). **(user multi-selected all three)**
- 569e manifest evidence_direction stays mixed; `evidence_direction_per_claim={ARC-065: mixed, MECH-341: mixed}` unchanged (diagnostic, non-weighting).
- 569c headline (~2.4x C3 lift over matched-noise) remains the load-bearing finding on ARC-065 GAP-A.
- 569d (sister floor-recalibrated falsifier) manifest expected to show the same instability when it lands; attach to this autopsy rather than spawn its own.
- After SD-056 amend lands and a substrate-readiness EXQ PASSes at behavioural-runtime scale: queue a 569e-equivalent Pathway A vs B probe on the stable substrate. Bundle the three script-side acceptance-criteria fixes into the same successor.
