# Failure autopsy -- V3-EXQ-610a (INV-074 crystallization-necessity discriminative pair)

- **Date (UTC):** 2026-06-01T16:46:43Z
- **Scope:** single (one FAIL)
- **Status:** confirmed (user verdict at Step 8 gate 2026-06-01: scope=both -> full 610a autopsy)
- **Routing:** governance reclassification (correct the rescue session's conservative read). No /diagnose-errors loop -- the `emit_outcome(experiment_type=...)` crash that caused the original misclassification is already fixed in the lineage (see Section 5b). No new EXQ unless governance wants an enriched-environment retest.
- **Prior handling:** rescue-v3-exq-610a-manifest-20260530T190400Z recovered the manifest from ree-cloud-3 and set a conservative per-claim read; governance marked the dir discussed (review_tracker). No prior deep autopsy artifact existed -- this is it.

## 1. Target and scope

V3-EXQ-610a is the INV-074 crystallization-necessity discriminative pair (supersedes V3-EXQ-610, which was SIGTERMed after ~13.25h on an under-estimate; no code change). It tests whether plasticity crystallization is *necessary* for diversity persistence after Phase 3.

claim_ids = [INV-074 (primary), MECH-334, MECH-333, MECH-341]. experiment_purpose = evidence. backlog_id = EVB-0270.

Manifest: `evidence/experiments/v3_exq_610a_inv074_crystallization_necessity_20260529T224419Z_v3.json` (ran ree-cloud-3 2026-05-29T22:44:19Z; recovered 2026-05-30T19:04Z).

## 2. Facts (manifest reconstruction -- facts only)

2-arm design, 3 matched seeds [42,43,44], 4-phase infant curriculum, 2500 episodes/arm, 200 steps/ep:
- ARM_0 control: `crystallize_at_phase3 = False`
- ARM_1 test: `crystallize_at_phase3 = True`
- Both arms: MECH-313 noise_floor + MECH-260 dACC + MECH-341 E3 diversity + gated_policy/differential_heads ON.

Primary observable: Shannon entropy of the selected-action distribution at end_phase_2 (peak window) and end_phase_3 (post-closure).

Pre-registered acceptance:
- **D1** (crystallization preserves diversity): ARM_1.end_phase_3 - ARM_0.end_phase_3 >= +0.10
- **D2** (control shows collapse): ARM_0.end_phase_2 - ARM_0.end_phase_3 >= +0.10
- **D3** (sanity, both arms diverse at Phase 2): ARM_0 & ARM_1 end_phase_2 > 0.4
- PASS = D1 AND D2 AND D3

Recorded result (`acceptance` block):
- D1 = **False**; d1_delta = **-0.0123** (ARM_1 end_phase_3 1.1011 vs ARM_0 end_phase_3 1.1133 -- crystallization arm slightly LOWER, not +0.10 higher)
- D2 = **False**; d2_delta = **-0.0062** (ARM_0 end_phase_2 1.1071 vs end_phase_3 1.1133 -- entropy did NOT drop; it rose slightly)
- D3 = **True**; both arms end_phase_2 entropy ~1.107 (> 0.4)
- verdict = FAIL

Per-seed end-phase entropies (arm_results) hover ~0.90-1.28 across both arms in both phases -- the two arms track each other closely in every seed.

## 3. Claim-layer map

- **INV-074** -- invariant, invariant_type=universal, status=candidate, epistemic_category=**substrate_ceiling** already set, pending_retest_after_substrate. The crystallization-necessity claim.
- **MECH-333 / MECH-334** -- mechanism_hypothesis, candidate, v3_pending, implementation_phase=v3 (MECH-334 also already epistemic_category=substrate_ceiling). The closure-side mechanisms (plasticity injection + residue EWC).
- **MECH-341** -- as in the 614c autopsy; here only a diversity-establishment dependency, not under direct test.

claim_ids accuracy: INV-074/MECH-333/MECH-334 are the right surface for a crystallization-necessity test. MECH-341 is correctly a *background dependency* (it establishes Phase 0-2 diversity), not a claim this design discriminates -- the rescue session's `non_contributory` read for MECH-341 is correct.

**Did the experiment test INV-074 under conditions where it could express itself? NO -- the negative control did not produce the failure mode the claim addresses.** INV-074 predicts diversity *collapses post-Phase-3 without crystallization*. D2 measures exactly that collapse in the control arm, and D2 = False: the control did NOT collapse (entropy was flat/slightly rising from Phase 2 to Phase 3). When the control never degrades, the crystallization arm having no marginal advantage (D1 = False) is *expected and uninformative* -- there is nothing for crystallization to protect against in this environment.

## 4. Biological-reference triage

Closest mechanism: critical-period crystallization / closure of plasticity windows (Hensch 2005 PV/GABA critical period; the closure side REE instantiates via INV-074 + MECH-333/MECH-334 + EWC). The reference mechanism's protective benefit is only observable when there is an ongoing destabilising pressure (continued learning / forward-model consolidation) that would otherwise overwrite established discrimination.

- is_formal_import: false (a biologically-motivated closure mechanism, not a formal-definition import)
- divergence: n/a
- lit_status: present-adjacent (critical_period_crystallization.md design doc; Hensch/Bear anchors referenced in the 2026-06-01 plasticity-window thoughts doc)

**Does the failure resemble a missing-dependency signature?** Yes: it matches the biological case where the *opening/destabilising pressure is absent*. If the CausalGridWorldV2 fishtank does not drive post-Phase-3 forward-model consolidation hard enough to overwrite Phase-2 discrimination, then neither arm degrades and the protective mechanism cannot show its effect. This is an environment-pressure / test-bed-adequacy gap, consistent with INV-074's existing substrate_ceiling categorization -- not a falsification of the crystallization-necessity claim.

## 5a. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | unclear (not weakened) | INV-074 cannot be weakened by a run where the predicted control collapse never occurred. The conservative `weakens` rescue read overshoots. |
| Biological reference | partial | Closure mechanism; benefit observable only under a destabilising post-closure pressure that this env did not supply. |
| Prerequisites | present-but-inert | MECH-341 diversity established (D3 PASS, both arms ~1.107 at Phase 2), but no Phase-3 degradation pressure to make crystallization matter. |
| Implementation | complete | Crystallization + residue EWC wired (ARM_1 ran the closure path); no crash in the science (manifest written normally). |
| Environment | **too benign / wrong pressures (dominant)** | Control did not collapse (D2 delta -0.006). CausalGridWorldV2 fishtank does not drive the post-Phase-3 forward-model consolidation that would overwrite discrimination. |
| Measurement | adequate | Entropy at Phase 2/3 boundaries is the right observable; D3 sanity confirms the instrument captured diversity. |
| Integration | coupled-and-stable | Both arms ran 2500 ep x 3 seeds; arms track each other. |
| Scale | adequate-or-more | 2500 ep/arm is a long horizon; the absence of collapse is not a too-short-training artifact (D2 note (ii) in the script grid is the alternative, but 2500 ep makes (i) -- signals more robust than predicted / env too benign -- the stronger reading). |

**Dominant diagnosis layer:** Environment adequacy. The negative control did not exhibit the predicted post-Phase-3 diversity collapse, so the test is **non-discriminative**. This is the substrate/test-bed-ceiling fingerprint and is already INV-074's recorded epistemic_category.

**Recommended `epistemic_category`:** substrate_ceiling (specifically, test-bed / environment-pressure ceiling -- the destabilising post-closure pressure that crystallization protects against is not present in the current env).

## 5b. The crash (why this was an ERROR, and why /diagnose-errors does NOT apply now)

The original run wrote its manifest normally, then crashed at the script tail on `TypeError: emit_outcome() got an unexpected keyword argument 'experiment_type'` (a copy-paste bug; `emit_outcome` in `experiment_protocol.py` has never had that parameter). The runner saw a non-zero exit + missing sentinel and classified ERROR, so the Phase-3 writer never ingested the (already-written) manifest. The rescue session recovered it.

**This crash is already remediated lineage-wide.** As of 2026-06-01 the sibling scripts the rescue note flagged as "still present" are clean:
- `ree-v3/experiments/v3_exq_540g_mech307_criterion_fix.py:772` -> `emit_outcome(outcome=..., run_id=..., queue_id=...)` (no `experiment_type`)
- `ree-v3/experiments/v3_exq_610_inv074_crystallization_necessity.py:788` -> `emit_outcome(outcome=..., manifest_path=..., run_id=..., queue_id=...)` (no `experiment_type`)
Both match the current `emit_outcome` signature (`experiment_protocol.py:109`). There is no live crash to fix. **/diagnose-errors is therefore not invoked.** (599/600 were already fixed via 599a/600a per the rescue note.) The science of 610a is intact in the recovered manifest, so no re-run is required to recover the result.

## 6. Cluster pattern

Single target. (Note: this FAIL shares the "negative control does not collapse -> non-discriminative" shape with several prior substrate-ceiling readings on INV-074 / MECH-262 lineage -- the recurring REE fingerprint where the env is too benign to surface the failure mode a closure/persistence claim addresses. Not run as a formal cluster here.)

## 7. Learning extracted

1. **The rescue session's conservative `weakens` read overshoots the pre-registered grid.** The script's own interpretation grid row (c) maps D2 FAIL (control does not collapse) to **non_contributory** ("control does not exhibit the predicted failure mode; either the diversity signals are more robust than predicted, or insufficient training epochs"). With both D1 and D2 failing, D2-FAIL governs: you cannot read D1-FAIL as evidence against INV-074 when the control never degraded. Recommended correction: INV-074/MECH-333/MECH-334 -> **non_contributory** (not weakens).
2. **A crystallization-necessity test needs an environment that drives post-closure degradation.** A retest must introduce a destabilising Phase-3 pressure (continued forward-model consolidation / distribution shift) strong enough that the *control* arm measurably collapses; otherwise the necessity claim cannot express itself. This is a test-bed-construction gap.
3. **2500 episodes makes the "too benign env" reading stronger than the "too short" reading.** With this much training and no control collapse, the more likely cause is that the env supplies no overwriting pressure, not that the collapse needs more epochs.
4. **MECH-341 = non_contributory here is correct** -- it is a Phase-0-2 diversity-establishment dependency, not a claim this 2-arm crystallization design discriminates.

## 8. Repair pathway and routing decision (user-confirmed at Step 8)

Routing: **governance reclassification**. Recommended per-claim overrides on the 610a manifest: INV-074 = non_contributory, MECH-333 = non_contributory, MECH-334 = non_contributory, MECH-341 = non_contributory (correcting the rescue session's conservative weakens to match the pre-registered grid row (c) and the substrate/test-bed-ceiling diagnosis). Set/retain epistemic_category=substrate_ceiling and pending_retest_after_substrate=true on INV-074/MECH-334 (already present). Optionally surface to /implement-substrate or /queue-experiment a *test-bed enrichment* (a Phase-3 destabilising-pressure env) as the precondition for any future crystallization-necessity retest -- recommended as `amend` discipline, not created here.

No /diagnose-errors (crash already remediated lineage-wide). No re-run required to recover the science.

## 9. Recommended evidence_quality_note (governance to write, not this skill)

> "2026-06-01 autopsy (failure_autopsy_V3-EXQ-610a_2026-06-01): V3-EXQ-610a (2-arm crystallization-necessity discriminative pair, 2500 ep x 3 seeds, 4-phase curriculum) is reclassified non_contributory for INV-074/MECH-333/MECH-334 (correcting the 2026-05-30 rescue session's conservative `weakens` read). The run FAILed D1 (d1_delta -0.012) and D2 (d2_delta -0.006) with D3 (sanity) PASS. The governing failure is D2: the no-crystallization control arm did NOT exhibit the predicted post-Phase-3 diversity collapse (ARM_0 end_phase_2 entropy 1.107 ~= end_phase_3 1.113). Per the script's own pre-registered interpretation grid, D2 FAIL = non_contributory (control does not exhibit the predicted failure mode). With the control never degrading, ARM_1's lack of marginal advantage (D1 FAIL) is expected and carries no information against the crystallization-necessity claim. Diagnosis: environment/test-bed ceiling -- CausalGridWorldV2 does not drive the post-Phase-3 forward-model consolidation that would overwrite Phase-2 discrimination, so the protective benefit of crystallization cannot express itself (consistent with INV-074's existing epistemic_category=substrate_ceiling). MECH-341 non_contributory retained (background Phase-0-2 diversity dependency, not under direct test). pending_retest_after_substrate=true: a retest requires a test-bed enrichment introducing a destabilising Phase-3 pressure strong enough that the control arm measurably collapses. The original run's emit_outcome(experiment_type=...) crash that caused the ERROR misclassification is already fixed lineage-wide (540g, 610 clean as of 2026-06-01); the recovered manifest's science is intact, so no /diagnose-errors loop and no re-run is needed to recover the result."

## 10. Routing field for /governance

- routing: governance-reclassification
- target claims: [INV-074, MECH-333, MECH-334, MECH-341]
- per-claim evidence_direction overrides: {INV-074: non_contributory, MECH-333: non_contributory, MECH-334: non_contributory, MECH-341: non_contributory}
- pending_retest_after_substrate: true (INV-074, MECH-333, MECH-334) -- gated on a test-bed enrichment (destabilising Phase-3 pressure)
- narrow_supports_flag: false
- recommended_substrate_queue_entry.action: amend (optional) -- test-bed enrichment env that drives post-Phase-3 diversity collapse in the control arm; governance to decide whether to materialise now or defer
- no /diagnose-errors loop: the emit_outcome(experiment_type=...) crash is already fixed lineage-wide; recovered manifest science intact
