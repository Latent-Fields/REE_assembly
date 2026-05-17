# Failure Autopsy — V3-EXQ-575 (ISEF-001 Harm-Gradient Warm-Start Gate)

- **Generated (UTC):** 2026-05-17T00:19:25Z
- **Scope:** single
- **Status:** confirmed (interactive gate completed; user confirmed routing + evidence note)
- **Target run_id:** `v3_exq_575_isef001_harm_gradient_baseline_20260516T223727Z_v3`
- **Queue id:** V3-EXQ-575
- **claim_ids:** [] (pure diagnostic — DEV-NEED-029 warm-start gate)
- **Outcome:** FAIL (ran to completion; C2 not met) — autopsy applies, not /diagnose-errors

## 1. Facts (no interpretation)

Diagnostic gate. 5 seeds (42-46), 200 episodes x 200 steps/ep, 32 RBF basis
functions. ARM_0 (control) `proximity_harm_scale=0.05`; ARM_1 (treatment)
`proximity_harm_scale=0.30`. Metric:
`coverage = residue_field.get_statistics()["active_centers"] / 32`.

| Criterion | Definition | Result |
|---|---|---|
| C1 | ARM_1 mean coverage >= 0.15 | **PASS** (1.0) |
| C2 | ARM_1 mean > ARM_0 mean | **FAIL** (both = exactly 1.0) |

Every seed, both arms: `final_coverage = 1.0`; `mean_coverage` 0.973-0.996
(rises to 1.0 within the first ~50 episodes and stays). Failed criterion =
**discrimination**; the absolute floor (C1) passes trivially. This is the
ceiling fingerprint — here the ceiling is in the **metric**, not the substrate.

## 2. Mechanism — root cause: blind instrument

- `get_statistics()["active_centers"] = rbf_field.active_mask.sum()`
  (`ree-v3/ree_core/residue/field.py:644`).
- `active_mask[idx]` is set True **permanently** by `RBFLayer.add_residue`
  (`field.py:131`), reached via `ResidueField.accumulate` (`field.py:334`)
  from `agent.update_residue` whenever `harm_signal < 0` (`agent.py:3757`).
- Center allocation is a **32-slot ring buffer**:
  `next_center_idx = (next_center_idx + 1) % num_centers` (`field.py:132`).
- `harm_scale` modulates residue **weight magnitude** only
  (`weights.data[idx] += intensity`, intensity ~ harm_magnitude *
  accumulation_rate). It does **not** change *which* centers are flipped
  active — even an infinitesimal harm flips the bit.
- Over 40,000 steps/episode, >=32 harm events accumulate within the first
  episode in **both** arms; `active_mask.sum()` pins at 32, coverage at 1.0,
  and `active_mask` is a persistent buffer that never resets across the 200
  episodes. The metric is **structurally incapable** of expressing C2.

This is a measurement-design flaw, not a tuning problem and not substrate or
claim pressure.

## 3. Claim-layer mapping

`claim_ids: []`. No MECH/ARC/Q/SD/INV claim is tagged, falsified, or weakened.
EXQ-575 is a substrate-readiness *gate* for downstream work (ARC-065 diversity
sweeps, Q-043/044/045, INV-049 retests), not evidence weighing any claim.
There is no conflict ratio or "supports" set to re-check (the
illusory-conflict-resolution rule is satisfied vacuously — no claim affected).

## 4. Biological-reference triage

Mechanism under test: persistent residue field phi(z_world) — the REE
aversive-trace analogue (hippocampal/amygdalar accumulated nociceptive value
map). Biological aversive memory is **intensity-graded**, not present/absent.
Biology therefore *predicts* the corrected instrument: a low- vs high-intensity
harm field should differ in **weight magnitude / extent above a salience
threshold**, not in the binary count of ever-touched locations. Biology is
**clear** and points directly at the fix. This is not a formal-definition
import; **no lit-pull is warranted**.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (n/a) | no claim tagged; nothing falsified |
| Biological reference | clear | aversive trace is intensity-graded; biology predicts the GAP-6 metric |
| Prerequisites | present | residue accumulation path confirmed LIVE (coverage->1.0 = accumulate fired both arms) |
| Implementation completeness | substrate complete; **metric is the gap** | `get_statistics().active_centers` is a ring-buffer saturation counter, wrong instrument |
| Environment adequacy | adequate | harm generated in both arms (centers fill) |
| Measurement adequacy | **misleading — dominant diagnosis** | binary active_mask count saturates 32/32 regardless of harm_scale |
| Integration adequacy | coupled | accumulate->active_mask->get_statistics path works as coded |
| Scale / capacity | the ceiling itself | 32-center ring buffer fills within episode 1; metric pinned for 200 episodes |

**Recommended `epistemic_category`: `measurement_artifact`.** The FAIL is an
artifact of the chosen instrument, not a property of the substrate or any
claim. Contributory: it tells us precisely how the warm-start gate must be
measured, and it validated the residue path is live.

## 6. Cluster pattern

Single. `pending_review.md` shows no co-pending FAIL sharing this
run_id / substrate / shape. The *shape* (floor passes, discrimination fails by
saturation) is in the substrate-ceiling family, but the *cause* here is a
metric ceiling, not a substrate ceiling — kept distinct, not folded into the
cross-claim substrate-ceiling pattern doc.

## 7. Learning extracted

1. **Measurement gap discovered.** `get_statistics()["active_centers"]` is a
   ring-buffer saturation counter — blind to harm *intensity*. Any
   harm-intensity discrimination must use magnitude-thresholded coverage.
2. **Positive signal.** The residue accumulation path is confirmed LIVE
   end-to-end (update_residue -> accumulate -> add_residue -> active_mask fired
   in both arms). Not a null / dead-path result.
3. **The corrected instrument already exists** and landed ~13 min post-run:
   `ResidueField.get_coverage_telemetry()` (GAP-6, `field.py:652`),
   `coverage_pct = (active_mask & |weight| > 0.02*rsf) / n`. EXQ-575 is the
   empirical motivation for GAP-6.
4. **Downstream implication.** ARC-065 diversity sweeps / Q-043/044/045 /
   INV-049 warm-start gating must re-spec on `get_coverage_telemetry`, never
   the binary count. DEV-NEED-029 gate remains UNVALIDATED until 575a passes.

## 8. Repair pathway / routing (user-confirmed)

- **Routing:** `/queue-experiment` -> **V3-EXQ-575a** (alphabetic suffix,
  same scientific question, instrument fix only). `supersedes: V3-EXQ-575`.
- **575a redesign spec:**
  - Replace `get_statistics()["active_centers"]/32` with
    `agent.residue_field.get_coverage_telemetry()["residue_coverage_pct"]`.
  - Keep arms (0.05 vs 0.30), seeds (42-46), 200 ep x 200 steps, 32 bases.
  - Keep C1 (ARM_1 thresholded coverage >= 0.15) and C2 (ARM_1 > ARM_0) —
    both now able to express, since the threshold separates the magnitude
    regimes.
  - Add a secondary metric: `harm_total` and `mean_weight` (from
    `get_statistics()` / `get_coverage_telemetry`) so the magnitude
    separation is visible even if thresholded coverage co-saturates at high
    `proximity_harm_scale`.
  - Update the interpretation grid: an ARM_1 == ARM_0 co-saturation on
    thresholded coverage routes to lowering the contrast (e.g. ARM_0 -> 0.0)
    or raising the threshold, not to a substrate conclusion.
- **No claims.yaml / manifest / review_tracker / substrate_queue edits** by
  this skill — `/governance` applies the note; `/queue-experiment` writes 575a.

## 9. Draft `evidence_quality_note` (governance to write verbatim — user-accepted)

> V3-EXQ-575 non_contributory: C2 FAIL is a measurement artifact, not
> substrate/claim pressure. get_statistics().active_centers is a 32-slot
> ring-buffer saturation counter blind to harm intensity; both arms pin at
> 1.0. Residue accumulation path confirmed LIVE end-to-end (positive signal).
> DEV-NEED-029 warm-start gate remains UNVALIDATED; downstream ARC-065 /
> Q-043/044/045 / INV-049 stay blocked pending V3-EXQ-575a on
> get_coverage_telemetry().

`evidence_direction` stays `non_contributory` (correct — no claim tagged); the
interpretable signal at the measurement/substrate-readiness layer is recorded
above, so this is not a force-mapped value.
