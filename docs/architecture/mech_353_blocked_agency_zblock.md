---
title: "MECH-353: affect.blocked_agency_control_failure_stream (z_block)"
parent: "Affect, Harm & Nociception"
grandparent: Architecture
nav_order: 8
---

# MECH-353: affect.blocked_agency_control_failure_stream (z_block)

**Claim ID:** MECH-353
**Subject:** affect.blocked_agency_control_failure_stream
**Status:** IMPLEMENTED 2026-06-06 (substrate; v3_pending until the discriminative experiment PASSes)
**Registered:** 2026-06-05 (lit-pull `targeted_review_blocked_agency_anger_stream`, chip `task_64c2e558`)
**Depends on:** SD-029 (agency comparator), MECH-112 (z_goal / wanting), MECH-320 (tonic vigor / assert pole), MECH-342 (decommit actuator), ARC-016 (commitment-threshold gate), SD-011 (differentiated-from: harm), SD-019b (differentiated-from: suffering). Detector discrimination additionally requires **SD-056** (action-conditional `world_forward`) trained.
**Blocks:** the smallest-V3 blocked-action discriminative experiment; clears its own `v3_pending` on PASS.

This doc records the V3 substrate implementation. The affect-register framing (the
"why", the full neighbour-differentiation grid, and the literature) lives in
`docs/architecture/affect_primitives.md` (Extension Register, `blocked_agency`).
This file is the implementation contract.

## Problem

REE represents harm (SD-011, `z_harm_*`), suffering (SD-019b `z_harm_a` + Q-036
escapability — the **capacity-collapsed withdraw** pole), residue (MECH-056), and
licit self-imposed commitment-holds (MECH-090). It does **not** represent the
affect that arises when an intended, predicted-to-succeed action is repeatedly
**BLOCKED** while the goal and the agent's **capacity-belief are retained** — the
energised "assert / restore" pole. The lit-pull verdict (Davis & Montag 2019 RAGE
as a distinct primary-process system; Papini 2024 frustrative non-reward, zero
noxious input; Bertsch 2020 reactive-aggression assert channel under prefrontal
gating; Carruthers 2012 comparator model) establishes this is a distinct stream,
not reducible to harm + residue + frustration. Folding it into the harm register
would repeat the SD-010 -> SD-011 *philosophy-right / mechanism-wrong* error
(`feedback_biology_before_formal_definitions`).

## Solution

`z_block` is a **derived affect readout** — a pure-arithmetic regulator
(`ree_core/affect/blocked_agency.py`, mirroring the MECH-313 / MECH-320 / MECH-342
pattern), NOT an encoder output. It is also surfaced as `LatentState.z_block`
(`[batch, 1]`) for downstream consumers / instrumentation.

**Detector / antecedent (computed in `REEAgent._update_blocked_agency`, called from
`sense()` right after the MECH-095 TPJ update):**

1. **Action-outcome comparator (SD-029 on the z_world channel; Carruthers 2012).**
   `zw_pred = E2.world_forward(z_world_prev, last_action)`;
   `pred_mag = ||zw_pred - z_world_prev||` (the intended effect size);
   `outcome_mismatch = ||zw_pred - z_world_now|| / (pred_mag + eps)`.
   Gated by a **predicted-effect floor**: when `pred_mag < floor` the action was
   not predicted to produce an effect, so there is nothing to be blocked from
   (`outcome_mismatch = 0`; this also fails safe on an untrained `world_forward`).
   Calibration with a trained, action-conditional `world_forward`: blocked ->
   `z_world` unchanged -> `outcome_mismatch ~ 1.0`; success -> `z_world` reaches
   the prediction -> `outcome_mismatch ~ 0.0`. This is FNR's expected-minus-obtained
   (Papini 2024) generalised from reward-omission to action-effect-omission.

2. **Expectation (MECH-112).** The goal-retained gate (`goal_state.is_active()`)
   supplies "there is an intended outcome" the block frustrates.

3. **Motor-agency / external-attribution comparator (z_self channel).**
   `motor_agency = 1 / (1 + ||E2.predict_next_self(z_self_prev, last_action) -
   z_self_now||)`. High = the motor command executed as predicted -> the mismatch
   is **external**, not the agent's own motor error. (`predict_next_self` is E2's
   primary trained objective, so this gate is reliable even when `world_forward`
   is weak.) This is the load-bearing distinction the verdict emphasises.

**Integration (`BlockedAgency.update`).** `z_block` accumulates the comparator
mismatch over a window **only when** `motor_agency >= attribution_motor_floor`
(external) **and** `outcome_mismatch >= outcome_mismatch_floor` (genuinely blocked)
**and** the goal is retained; it leaks on success. Capacity-gated split:
`z_block_assert = z_block * capacity_belief`,
`withdraw_handoff = z_block * (1 - capacity_belief)`, where
`capacity_belief = clip(1 - w * ||z_harm_a||, 0, 1)` (suffering collapses
capacity-belief, so the assert pole yields to the existing withdraw pole).

**Consumers (in `select_action`):**

- **ASSERT / escalate-effort / alternative-action search** (the new behavioural
  pole REE lacks; the "raise MECH-320 vigor" effect). A self-emitted per-candidate
  score-bias composed into `dacc_score_bias` after the tonic_vigor block: NEGATIVE
  on action-trajectories (favour acting), POSITIVE on no-op (penalise passivity),
  extra POSITIVE on the just-blocked first-action class (try a *different* action).
  Scaled by `z_block_assert`; zero when there is no asserting block this tick
  (so OFF / no-block ticks add nothing — bit-identical).
- **DECOMMIT (MECH-342) gated by ARC-016.** When assertion fails across the window
  (`z_block_assert` sustained above `decommit_bound` for
  `decommit_consecutive_ticks`), `update()` emits a `decommit_signal`. `select_action`
  consumes it — beside the MECH-342 maintenance-release site — to `beta_gate.release()`,
  gated by the ARC-016 commitment-threshold (`e3.current_precision <=
  blocked_agency_decommit_arc016_precision_max`; `<= 0` disables the gate). Releases
  the blocked commitment rather than escalate unboundedly (Bertsch 2020 prefrontal
  inhibition of reactive aggression).
- **HANDOFF to suffering.** As `capacity_belief` falls the assert share decays and
  `withdraw_handoff` rises; the existing SD-019b / `z_harm_a` / Q-036 withdraw
  machinery takes over. No forced `z_harm_a` write — the assert pole simply yields.

## Config (all no-op default; bit-identical OFF)

`REEConfig` + `from_dims`: `use_blocked_agency` (master) plus
`blocked_agency_{accumulation_rate, leak_rate, outcome_mismatch_floor,
attribution_motor_floor, capacity_collapse_weight, require_goal_active,
z_block_cap, assert_action_weight, assert_passive_weight, assert_alt_action_weight,
assert_bias_scale, decommit_bound, decommit_consecutive_ticks,
decommit_arc016_precision_max, predicted_effect_floor, noop_class}`.

**Env manipulation** (`CausalGridWorldV2`, SD-029 / SD-022 env-curriculum precedent;
env-only kwargs, not surfaced through `from_dims`): `scheduled_action_block_enabled`
(+ `_interval`, `_prob`). On fire, the agent's chosen move is externally cancelled
(the agent stays put) for that tick with **no damage and no layout change** —
`transition_type="action_blocked"`, info tags `action_blocked_this_step` /
`action_block_event_count`. This is the clean external-block antecedent (motor
intact -> the attribution gate reads it as external), distinct from SD-022
limb-damage movement failure (own-motor error coupled to damage).

## Backward compatibility / training notes

- `use_blocked_agency=False` -> `agent.blocked_agency is None`, `LatentState.z_block`
  stays `None`, no consumer fires; verified bit-identical action stream (the
  regulator uses no torch RNG and adds zero bias when `z_block~0`). 803/803 ree-v3
  contracts pass with the master OFF; 9/9 new MECH-353 contracts pass.
- **No phased training** (pure-arithmetic regulator; no learned parameters).
- **MECH-094:** `update()` is a no-op under `simulation_mode` / `hypothesis_tag`
  (replay must not accumulate blocked-agency on imagined outcomes); `z_block` is
  left `None` on hypothesis-tagged latents.
- **Detector discrimination requires a trained substrate.** At smoke / untrained
  scale, `z_world` deltas do not track single-cell moves (the encoder is random;
  realised effect is uninformative), so the action-outcome comparator is
  uninformative — expected. The validation experiment trains the encoder
  (representing scene/position in `z_world`) and the action-conditional
  `world_forward` (SD-056) in P0, then measures block-vs-control discrimination in
  P1. If a trained substrate still cannot make the comparator discriminate, that is
  an informative substrate-ceiling finding routing to encoder / `world_forward`
  enrichment — NOT a falsification of MECH-353's affective claim.

## What this enables

The smallest-V3 blocked-action discriminative experiment: an env that repeatedly
blocks an intended, predicted-to-succeed action while harm and goal-value are held
constant; measure whether `z_block` rises, whether it drives assert/persist (effort
escalation / alternative-action search) **distinct from the withdraw signature**,
and whether it **dissociates from `z_harm_a`** under a matched controllability
manipulation. PASS clears `v3_pending` on MECH-353.

## Scope

This is **Stream A** (V3-tractable, single-agent). **Stream B** (coercion /
domination / injustice) needs a model of an other-agent coercer (psychological
reactance; Steindl 2015) and is **V4-social, deferred** — NOT implemented here.

## Related claims

SD-029, MECH-112, MECH-320, MECH-342, ARC-016, SD-011, SD-019b, Q-036, MECH-056
(residue, differentiated-from), MECH-090 (commitment-hold, differentiated-from),
MECH-095 (TPJ comparator, sibling agency signal on z_self), SD-056 (action-conditional
world_forward, detector prerequisite), MECH-094 (simulation gate).
