# Failure Autopsy — V3-EXQ-701 (INV-050 MEL-measurability diagnostic)

- **run_id:** `v3_exq_701_inv050_mel_measurability_diagnostic_20260622T231121Z_v3`
- **queue_id:** V3-EXQ-701
- **claim:** INV-050 (MEL = the third / model-error-load sleep drive; the directly-testable IV precondition: is accumulated waking prediction-error a measurable, graded, manipulable quantity?)
- **experiment_purpose:** diagnostic (excluded from governance confidence/conflict scoring)
- **outcome:** FAIL — self-route `substrate_not_ready_requeue`, `evidence_direction: non_contributory`
- **scope:** single (lineage: 677 MECH-180 sleep-side -> 701 INV-050 IV-precondition, no-sleep)
- **generated_utc:** 2026-06-23T04:16:33Z
- **status:** confirmed (user interactive gate, 2026-06-23)
- **routing:** queue-experiment (re-queue with a CONVERGED P0; gate R2 before R1/C1). No substrate_queue entry. Re-derive brake does NOT fire.

---

## 1. Facts (no interpretation)

Pre-registered readiness gates (the diagnostic's own grid: "R1 or R2 unmet -> substrate_not_ready_requeue ... NOT a verdict on INV-050"):

- **R2 `world_model_converged_p0` = -2.60** (threshold >= 0.10, direction higher-is-converged): the P0 world-forward model's relative PE drop `(pe_init - pe_final)/pe_init` is strongly NEGATIVE -- PE *rose* ~260% over the CONV_EPISODES=20 P0 budget on the stable base env. The SD-056 online-contrastive world-forward model **diverged**, it did not converge. **UNMET.**
- **R1 `pe_response_range_to_novelty_shock` = -0.005** (threshold >= 0.25): on the frozen model, PE under a max-novelty shock is *not* above PE on the stable env (slightly below). **UNMET.**
- **C1 `mel_measurable_monotonic` (load-bearing) = FAIL:** `mel_none=0.019230`, `mel_high=0.019055` (HIGH is marginally BELOW NONE); `rel_spread_ok=false`, `abs_spread_ok=false`. The per-arm MEL means are flat across novelty (0.01923 / 0.01938 / 0.01920 / 0.01906). The per-group structure (0.0152 / 0.0174 / 0.0253) is essentially identical across all 4 arms -- the 3 groups dominate, novelty exposure contributes nothing.
- **C2 `non_degenerate` = PASS** (cross-seed/group spread present; the run is not vacuous-by-construction).

**Which criterion failed:** two readiness preconditions (R1 + R2). No claim-bearing criterion was ever reached. Clean readiness self-route, not a claim test.

## 2. Claim-layer mapping

INV-050 is the architectural/invariant claim that sleep is regulated by a THIRD (MEL) drive proportional to accumulated waking prediction error. 701 tests ONLY the IV precondition (is MEL measurable + graded?), commitment-free, NO sleep machinery touched. The DV never spoke to INV-050 because the readiness gates failed. Correctly `non_contributory`; **INV-050 is not weakened.** Promotion held by INV-050's existing v3_pending / substrate-blocked status regardless.

## 3. Biological-reference triage

- Closest reference: sleep as homeostatic model-consolidation pressure scaling with the day's learning load (synaptic-homeostasis / SHY; Tononi-Cirelli). The IV here (accumulated prediction error as a proxy for model-error load) is a faithful functional translation, not a formal-definition import. `lit_status: present` (sleep-consolidation literature).
- The failure does NOT implicate the biological mechanism. It is upstream of any MEL claim: the diagnostic's *own world model never converged*, so there is no valid frozen base against which a novelty-driven PE rise could be read.

## 4. The convergence confound (the central move)

The DOMINANT unmet precondition is **R2 (P0 world model diverged, conv_rel_drop -2.60)**, and R1/C1 are downstream of it:

- If the world-forward model never learned the base env (PE rose over P0), the frozen model is an invalid base. Its per-step prediction error is dominated by un-learned base-env structure (the stable per-group pattern 0.015/0.017/0.025), which swamps any novelty transient.
- So R1 ("PE rises under a novelty shock") and C1 ("MEL grows monotonically with novelty") **cannot be interpreted** as evidence about the novelty->PE channel while R2 is unmet. A flat MEL on a diverged model is uninterpretable, not a demonstration that novelty fails to move PE.

This is the **V3-EXQ-642 canonical incident** in a new guise: the manifest self-routed substrate_not_ready (correctly), but the reason is an UNTRAINED/diverged substrate, so the correct response is **re-queue with a converged P0**, NOT a substrate-ceiling reclassification. Reclassifying a convergence-confounded run as a MEL ceiling is exactly the "illusory conflict resolution" the autopsy rules warn against.

CONV_EPISODES=20 is a small convergence budget for the SD-056 world-forward model, and conv_rel_drop=-2.60 is a *divergence* (not merely insufficient convergence) -- so the re-queue must both (a) raise the P0 budget and (b) verify *why* the world-forward model diverges on the stable env at this budget (instability / LR / regime), gating so R2 passes before R1/C1 are read.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | INV-050 IV precondition never reached; DV gated out by R1+R2. Correctly non_contributory, never a weakens. |
| Biological reference | clear | Sleep-as-model-consolidation (SHY). Not the failing layer; failure is upstream of any MEL claim. |
| Prerequisites | missing (diagnostic-internal) | A CONVERGED P0 world-forward model -- the valid frozen base the whole probe depends on. It diverged (conv -2.60). |
| Implementation | partial | The raw per-step e3 prediction_error read + frozen-window accumulation is the right instrument (it fixes 677's batch-loss wash-out bug); the gap is the P0 training that feeds it. |
| Environment | adequate | CausalGridWorldV2 graded-drift novelty arms are well-formed; matched-activity NONE control present. |
| Measurement | under-instrumented for convergence | The MEL readout is sound, but the P0 budget/regime does not produce a converged base, so the readout has nothing valid to measure. |
| Integration | n/a | Single-module diagnostic. |
| Scale / capacity | likely insufficient (P0 budget) | CONV_EPISODES=20 with a diverging trend -> needs a larger / stabilised P0. |

Recommended epistemic_category: **n/a (diagnostic, no claim status change).** evidence_direction `non_contributory`.

## 6. Lineage / re-derive brake

- INV-050: **0** prior substrate_ceiling/non_contributory autopsies under this tag. 677 (2026-06-14) tagged the sibling corollary **MECH-180** (sleep-side: sleep counts scheduler-pinned + novelty never moved PE 8.8e-7), routed implement-substrate (deferred adaptive-sleep-cadence) + a re-queue redesign, and explicitly flagged the IV-validation gap that 701 was built to close.
- **Brake does NOT fire.** A strict claim_ids count is 1 (INV-050's first). More importantly, 701 is **confounded by P0 non-convergence**, so it has NOT cleanly hit a MEL ceiling -- firing the brake here would reclassify a confounded run as a ceiling (illusory resolution).

**Recurrence flag (for the successor, NOT a brake firing now):** 677 (sleep-side) and 701 (no-sleep IV) BOTH show novelty failing to move PE -- but each under a confound (677 batch-loss wash-out + scheduler-pinned DV; 701 diverged P0). The **converged-P0 re-run is the decisive test**: if R1/C1 still show a flat MEL once R2 passes, THAT is the genuine "MEL not measurable on V3" confirmation, and a substrate-ceiling routing (enrich the world model / a stronger MEL manipulation: causal-structure or reward-structure shift, finer PE instrumentation) becomes correct -- and the brake should fire on that clean reading. The script's own grid already names that branch (`C1 FAIL with substrate ready -> mel_not_modulated_by_novelty`).

## 7. Learning extracted

1. 701's dominant blocker is R2 (P0 world-forward model DIVERGED, conv -2.60), not the novelty channel. The R1/C1 flatness is a downstream consequence of an invalid frozen base and is uninterpretable as INV-050 evidence -- the V3-EXQ-642 confound.
2. The MEL readout instrument is correct (raw per-step e3 prediction_error, frozen-window accumulation -- it fixes 677's batch-training-loss wash-out). The gap is the P0 that feeds it: CONV_EPISODES=20 yields divergence, not convergence, on the SD-056 world-forward model.
3. The converged-P0 re-run is the decisive MEL-measurability test. 677 + 701 are a recurrence (novelty not moving PE) but each is confounded; only an R2-passing run can cleanly answer whether MEL is manipulable on V3.

## 8. Routing decision (user-confirmed)

- `evidence_direction: non_contributory` CONFIRMED for INV-050 (NOT weakened; diagnostic, scoring-excluded). Self-route `substrate_not_ready_requeue` is correct per the pre-registered grid.
- **Routing: queue-experiment** -- re-queue the MEL-measurability diagnostic (new letter, e.g. V3-EXQ-701a) with: a larger / stabilised P0 so R2 (`world_model_converged`, conv_rel_drop >= 0.10) PASSES; a hard gate so R1/C1 are only interpreted on R2-passing seeds; and a diagnosis of why the SD-056 world-forward model diverges on the stable env at CONV_EPISODES=20 (budget vs instability/LR/regime).
- `recommended_substrate_queue_entry.action = none` -- no missing mechanism; the fix is the diagnostic's P0 convergence (test-bed construction), not substrate enrichment.
- Re-derive brake NOT fired; recurrence flagged for the successor (a converged-P0 flat MEL would be the decisive ceiling reading).

### Draft `evidence_quality_note` (for governance to write — diagnostic, no claim status change)

> V3-EXQ-701 (2026-06-23, failure-autopsy): INV-050 MEL-measurability diagnostic, non_contributory CONFIRMED (NOT a verdict on INV-050; diagnostic, scoring-excluded). Self-route substrate_not_ready_requeue is correct per the pre-registered grid: BOTH readiness gates unmet -- R2 world_model_converged=-2.60 (the SD-056 P0 world-forward model DIVERGED, PE rose ~260% over 20 ep) and R1 pe_response=-0.005. The R2 divergence is a V3-EXQ-642-style untrained-substrate confound: with an invalid frozen base, the R1/C1 novelty-flatness is uninterpretable as a MEL ceiling. Route: re-queue (new letter) with a converged/stabilised P0, gated so R2 passes before R1/C1 are read; no substrate_queue entry; no re-derive brake. Recurrence note: 677 (MECH-180, sleep-side) + 701 (INV-050, no-sleep IV) both show novelty not moving PE, each under a confound -- the converged-P0 re-run is the decisive MEL-measurability test; a flat MEL there would be the genuine ceiling and route to substrate enrichment / a stronger MEL manipulation.
