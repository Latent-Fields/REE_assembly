# Targeted Review: REM-phase precision recalibration timing — SYNTHESIS

**Created:** 2026-05-09
**Claims:** MECH-204 (primary), MECH-203, SD-017
**Question:** does biology specifically support cross-cycle EMA-tracked persistent reference (F1, just landed in ree-v3 commit 966c47e) vs broadcast read at action-selection consuming the captured precision_at_rem_entry directly (F3 / Phase 7 / Option B) for REM-driven precision recalibration? Does the answer differ from the general waking precision-update timing covered by Q-042?

## Entries

| Entry | Direction | Confidence | Primary contribution |
|---|---|---|---|
| Hobson, Hong & Friston 2014 ([DOI](https://doi.org/10.3389/fpsyg.2014.01133)) | supports | 0.82 | F1-sufficient: REM refines generative model; waking consumes the refined model passively via parameter updates. No separate broadcast arm needed in their architectural commitment. |
| Hong, Fallon, Friston & Harris 2018 ([DOI](https://doi.org/10.3389/fpsyg.2018.02087)) | supports | 0.68 | REMs as active-inference probes. Reinforces 2014 Hobson-Friston framework with empirical fMRI anchor. Indirect support for F1-sufficient. |
| Sakai & Crochet 2001 ([DOI](https://doi.org/10.1016/s0306-4522(01)00103-8)) | supports | 0.78 | Substrate evidence: 88% of presumed serotonergic DR neurons go silent at REM entry. Grounds MECH-203 quiescence + MECH-204 capture moment. Necessary substrate for both F1 and F3; does not arbitrate between them. |
| Walker & Stickgold 2006 ([DOI](https://doi.org/10.1146/annurev.psych.56.091103.070307)) | supports | 0.74 | Cumulative-across-cycles dose-response pattern of sleep-dependent memory consolidation. By architectural analogy, supports F1's EMA-tracked persistent reference over snapshot-only architectures. Does not directly arbitrate F1 vs F3. |
| Laukkonen, Friston & Chandaria 2025 ([DOI](https://doi.org/10.1016/j.neubiorev.2025.106296)) | mixed | 0.62 | Proposes "hyper-model for precision-control" that broadcasts global precision preferences through inference hierarchy. Tilts reading toward F3 / Option B as a candidate dual-arm complement to F1. Does not directly establish that the hyper-model consumes REM-captured zero-points. |

According to PubMed.

## Verdict

**The dominant biological pattern for REM-driven precision recalibration is option (a) cross-cycle slow-EMA reference accumulation that downstream consumers read passively via the refined generative model -- F1, just landed in ree-v3.** The Hobson-Hong-Friston 2014 architectural commitment, reinforced by Hong et al 2018 and the cumulative-across-cycles Walker-Stickgold 2006 pattern, points to F1 as the dominant pattern. The 5-HT zero-point during REM (Sakai & Crochet 2001 substrate) creates the capture moment; the cumulative refinement across cycles produces the persistent reference; waking inference consumes the refined model parameters passively in the normal course of choice.

**However, option (c) dual-arm pattern is also defensible** based on the Laukkonen-Friston-Chandaria 2025 hyper-model proposal. Biology may run BOTH F1 (cumulative parameter refinement) AND F3 (live broadcast read of the captured precision at action selection), as a sleep-extension of the Q-042 dual-arm finding for general waking precision-update timing. The hyper-model is the active-inference framing of F3; it has not been directly tied to REM-captured zero-points in the literature, but the architectural pattern is plausible.

**Option (b) F3-only is NOT supported.** No paper in this lit pull argues that biology runs F3 exclusively without an underlying F1-style cumulative refinement. The Sakai 2001 substrate makes F1 architecturally necessary -- the captured zero-point at REM entry IS read by something downstream, and the Hobson-Friston framework says that something is the refined generative model accessed by waking inference.

**Option (d) -- no explicit consumer, purely passive parameter drift -- is also NOT supported.** All five papers point at REM as an active recalibration phase with downstream behavioural consequence; none describe REM-driven changes as accidental passive drift.

## Phase 7 implications

For REE's `sleep_substrate_plan.md` Phase 7 / Option B decision:

1. **If V3-EXQ-541b's step-size sweep clears C3 in a defensible step band (0.05 / 0.10 / 0.25):** Phase 7 / Option B implementation is **not needed in V3**. The Hobson-Hong-Friston 2014 + Walker-Stickgold 2006 F1-sufficient reading is the operative architecture; F1 + tuned step is a complete MECH-204 closure. EXP-MECH204-STEP-SWEEP becomes the validation experiment for that closure.

2. **If V3-EXQ-541b fails C3 across the defensible band (0.05 / 0.10 / 0.25) but ARM_4_step_0_50 clears it:** The result indicates F1 with the step-size cranked to a biologically borderline value is barely sufficient. Phase 7 / Option B remains optional but deprioritised; the dual-arm reading is preserved as a follow-on if subsequent behavioural evidence accumulates pointing at MECH-204 as the bottleneck for downstream recalibration-dependent claims.

3. **If V3-EXQ-541b fails C3 across all step-size arms including 0.50:** F1 + step-tuning alone is insufficient. The Laukkonen-Friston-Chandaria 2025 hyper-model reading becomes load-bearing and Phase 7 / Option B implementation is justified. The implementation should:
   - Read `serotonin._persistent_zero_point` (the F1 cumulative reference) at action-selection time, NOT `serotonin._precision_at_rem_entry` (the moment-snapshot). Reasoning: Hobson-Hong-Friston 2014 + Walker-Stickgold 2006 establish that the cumulative reference is the biologically meaningful target, not the most-recent snapshot.
   - Apply the broadcast as an additive bias to E3 score, scaled by some gain analogous to `rem_precision_recalibration_step` (a `rem_precision_broadcast_gain` knob).
   - Run alongside F1 (NOT replace it) -- the dual-arm pattern. This matches both Q-042's general dual-arm finding and Laukkonen-Friston-Chandaria 2025's hyper-model + parameter-update architecture.

4. **F2 (apply-before-recapture) remains discarded** -- no paper in this lit pull supports a "recalibrate then re-snapshot" pattern. The architectural shape has no biological referent. This confirms the F2-discarded decision recorded in sleep_substrate_plan.md decision-log entry 2026-05-09.

## What this lit pull does NOT settle

- **The exact gain / scaling of an F3 broadcast.** Phase 7 / Option B's `rem_precision_broadcast_gain` parameter has no direct biological analogue in this lit pull; tuning would be empirical.
- **The cumulative-vs-snapshot question for the broadcast arm specifically.** F1 vs snapshot is settled (Walker & Stickgold 2006); F1 vs F3 (assuming both are cumulative) is not directly resolved.
- **Whether the 12% atypical DR neurons (firing during REM, per Sakai & Crochet 2001) carry any precision-relevant signal that REE's binary `tonic_5ht=0.0` during REM ignores.** This is a V4-or-later refinement; for V3 the I-A / I-B canonical pattern is the operative substrate.
- **The interaction with NREM / SWS spindle-mediated consolidation** (Manoach & Stickgold 2019, schizophrenia / spindle deficit literature). REE's MECH-120 SHY normalisation lives in SWS; whether SWS recalibration interacts with REM-driven precision recalibration in a load-bearing way is a separate substrate question.

## Recommended next action

Wait for V3-EXQ-541b result (currently running on DLAPTOP-4.local). Apply the dispatch table above based on outcome.

If V3-EXQ-541b clears C3, mark MECH-204 V3 closure on F1 + tuned step. Phase 7 deferred to V4 or later; this lit pull becomes the architectural reference if Phase 7 is ever revisited.

If V3-EXQ-541b fails C3 across defensible band but clears at 0.5, queue a Phase 7 implementation as a follow-on (V3-EXQ-542 family) but flag it as architectural insurance rather than urgent.

If V3-EXQ-541b fails C3 across all arms, Phase 7 / Option B becomes the next implementation work. The lit-pull-supported design: read `serotonin._persistent_zero_point` at `select_action()` time, scale by a tunable gain, broadcast as additive bias on E3 score, run alongside F1.
