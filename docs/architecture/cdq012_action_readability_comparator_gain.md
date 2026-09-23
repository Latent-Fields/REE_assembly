---
status: candidate/v3_pending
status_asof: 2026-09-23
status_claim: MECH-581
---

# Action Readability at Small Displacement: Comparator Gain, Encoder Consistency, Harm-PE Attribution (CDQ-012)

**Status:** architecture stub. Registered by the CDQ-012 Register pass of the Convergence Demand
Pipeline on 2026-09-23, session `cdq012-register-20260923`.
**Claims:** MECH-581, MECH-582, MECH-583 / MECH-584 (a competing pair), and MECH-585. All are
`candidate`, `implementation_phase: v3`, `v3_pending: true`.
**Substrate entries:** `SD-PP-B10-zworld-encoder-action-displacement` (`complex (probe-gated)`) and
`SD-PP-B11-harm-stream-predictor-reliability-producer` (`complicated (buildable)`), both in
`evidence/planning/substrate_queue.json`.
**Row:** CDQ-012, `evidence/planning/convergence_demand_queue.v1.json`. `satisfied` is NOT set.
GFLAG-0432 routes the correction of the row's criterion (i) to `/governance`.
**Inputs:** biology lit-pull `evidence/literature/targeted_review_efference_copy_small_signal_gain/`
(REE_assembly 04554d0fd17), plus two intakes in REE_convergence 8d5534d:
`sources/dreamer-v3/action_readability_small_displacement.md` and
`sources/muzero/action_readability_small_displacement.md`.
**Registration is not build authorisation.** No experiment has been queued.

---

## 1. What the row asked, and what has changed

CDQ-012 asks how an action-conditioned latent dynamics model keeps its action readable when one step
moves z_world by only ~3e-3 RMS per dim. Two premise corrections have landed since the row was
written.

1. **The head already reads its action (GFLAG-0432).** On this battery, 1.0 is the random-init null,
   not the action-blind null. The copy-the-input blind null measures 0.56 / 0.58 / 0.51. The trained
   OFF head sits at 0.83 / 0.88 / 0.71, which is 0.20-0.30 above the blind null on 3/3 seeds. A ratio
   that drifts toward 1.0 is decay toward initialisation. The real gap is **poseability**: is the
   action-driven difference big enough, against z_world's small per-step movement, for a
   contradiction to be scored?
2. **The small displacement is mostly an operating-point property.** V3-EXQ-1073 and V3-EXQ-1075
   never set `alpha_world`, so both inherited the `from_dims` default of 0.3 (`config.py:7562`). SD-008
   is **stable** and requires >= 0.9, and ~820 experiment files set 0.9. The intake probe shows that
   per-step displacement is ~3x larger at 0.9 or 1.0. The environment step itself is large: ~0.69 of it
   is action-attributable at the observation, against ~0.22-0.38 in z_world. The action information is
   lost **between world_obs and z_world**, in two places: the action-blind EMA and an encoder that never
   receives a transition gradient.

**Unit note.** The lit summaries quote the 1075a displacement as "0.013-0.016 RMS/dim". That figure is
`sqrt(WORLD_DIM * identity_mse)`, an L2 norm over 16 dims, so it is ~3.2-4.1e-3 per dim.

## 2. What biology says (the precondition, discharged)

Corollary discharge is a **family** of strategies: subtraction, gain modulation and gating (Crapse &
Sommer 2008). SD-007's ReafferencePredictor implements only **subtraction**. The function of
subtraction is to raise the detectability of **small external residuals** (Enikolopov, Abbott &
Sawtell 2018). **Gain modulation scaled to the predicted consequence** is a separate strategy, and REE
does not have it (Poulet & Hedwig 2006, in the opposite large-self-signal regime). A comparator is only
as informative as its prediction is accurate **at the signal's own scale** (Keller et al. 2012).

## 3. The claims

<a id="mech-581"></a>
### MECH-581: comparator gain scaled to the predicted action consequence

This is the missing corollary-discharge strategy, placed at the **comparator** rather than the head.
The world-forward PE is read through a gain calibrated to the magnitude of the predicted consequence.
A rule inversion that reverses a small predicted displacement then yields a PE that is large relative
to the prediction. The claim does not touch reconstruction, so CDQ-012 criterion (ii) is met by
construction (this is stated, not counted as evidence). Its control is a **global** min-max rescale
(MuZero MZ2), which leaves the displacement/spread ratio unchanged.

<a id="mech-582"></a>
### MECH-582: encoder shaped through the dynamics

This is the **encoder** leg of the V3-EXQ-1075 fan-out, which had no owner. The world-forward loss
should reach the encoder through the online input `z_t`, with the target `z_{t+1}` held stop-gradient
(the EfficientZero asymmetry; DreamerV3's `L_dyn`/`L_rep`). SD-070's variance/covariance hinge serves
as the anti-collapse floor. Its first precondition is the alpha_world operating-point probe. If raising
alpha alone closes the gap, the premise dissolves.

MECH-581 and MECH-582 are **complementary and separable**. MECH-582 controls how much action
information reaches z_world. MECH-581 controls how the comparator reads the displacement that is there.
A 2x2 design separates them.

<a id="mech-583"></a><a id="mech-584"></a>
### MECH-583 vs MECH-584: the SD-007 tension (competing, deliberately not chosen)

- **(A) MECH-583.** z_world is self-cancelled by design. world_forward on the corrected stream predicts
  external dynamics, and action readability belongs in the separate predictor that produced the
  subtraction.
- **(B) MECH-584.** Cancellation happens on the perception side. The forward model predicts the
  **uncorrected** `z_world_raw`, which `stack.py:1513` retains before both the correction and the EMA.

These are registered as competing claims on the ARC-033 / ARC-058 precedent (`e2_harm_a.py`). **The
discriminating observation:** turn reafference ON with a trained predictor, match alpha_world, and
denominate every ratio on its own blind null. Apply a one-shot action-map inversion and measure the
contradiction PE at three loci: (i) the ReafferencePredictor's own comparison, (ii) world_forward on
corrected z_world, and (iii) world_forward on z_world_raw.

- Under (A), (i) carries the contradiction, (ii) does not, and corrected z_world detects external
  events better than raw (the Enikolopov signature).
- Under (B), (iii) carries it at least as well as (i).

`z_world_raw` is also pre-EMA, so alpha_world must be matched between arms or reading (B) is confounded
with removing the EMA. The tension is latent in the 1073/1075 lineage because reafference was off
there.

<a id="mech-585"></a>
### MECH-585: harm PE attributed to world surprise only from a competent, calibrated predictor

This claim was folded in at the user's request. The user's words: "we need to know if the error came
from the world being surprising or the predictor being bad."

`e2_harm_a` describes a precision-weighted PE, but the dACC call passes `e3.current_precision`, a
z_world-domain precision, and `_affective_pe` scales the PE **up** by it. Nothing in that path
estimates the harm predictor's own reliability, and V3-EXQ-1062a measured that predictor **below
persistence** in 6/6 cells (SD-PP-B9).

The contract: an error beyond the calibrated per-state expectation, **from** a predictor that beats
persistence (online `d > 0`, the persistence_skill_gate statistic), reads as world surprise. Every
other error reads as model error.

A targeted biology pull on how aversive-prediction circuits estimate their own reliability is
**owed** before SD-PP-B11 is designed beyond its two named ingredients.

## 4. Graph wiring

| New claim | depends_on | Wired into |
|---|---|---|
| MECH-581 | SD-005, SD-007, MECH-098, MECH-059 | INV-063, MECH-574 |
| MECH-582 | SD-005, SD-008, SD-070 | INV-063, MECH-574, MECH-573 |
| MECH-583 | SD-007, MECH-098, MECH-101 (competes_with MECH-584) | none (decides the target locus for 581/582 when SD-007 is on) |
| MECH-584 | SD-007, MECH-098, MECH-101 (competes_with MECH-583) | none (as above) |
| MECH-585 | MECH-258, MECH-059, ARC-033 | none (MECH-055 related, not edited) |

**MECH-572 is deliberately not wired.** Its CONFIRMING does not require a readable head (SD-PP-B5
implementation_hint).

## 5. Cheapest next measurement

Run SD-PP-B10's candidate test 1: re-run the 1073/1075 OFF arm at alpha_world 0.9 and 1.0 against 0.3.
It needs no substrate and may dissolve the premise, so it goes before any build.

## 6. Scope

This pass is registration only. It includes no substrate build, no experiment script and no queue
entry. It does not decide CDQ-012 criterion satisfaction; that decision belongs to `/governance`, with
GFLAG-0432.
