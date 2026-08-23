---
title: "SD-059 / MECH-358: Relief/Safety Escape-Affordance Bridge"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 17
status: candidate/v3_pending
status_asof: 2026-07-10
status_claim: SD-059
---

# SD-059 / MECH-358: Relief/Safety Escape-Affordance Bridge

**Claim ID:** SD-059 (architecture) / MECH-358 (mechanism)
**Subject:** `defensive_action.escape_affordance_bridge`
**Status:** IMPLEMENTED 2026-06-08 (substrate; v3_pending until the 4-arm validation EXQ PASSes)
**Registered:** 2026-06-08
**Depends on:** SD-058 / MECH-357 (instrumental-avoidance gate), MECH-302 / SD-050 (relief comparator), MECH-303 / SD-052 + MECH-304 / SD-051 (safety prediction), SD-011 (z_harm_a), MECH-279 (PAG freeze), SD-056 (e2 action-conditional divergence -- the relief detector reads z_harm_a/world-forward), scaffolded_sd054_onboarding Stage-H driver
**Blocks (unblocks on PASS):** SD-058, MECH-357, ARC-060, MECH-320, ARC-068, SD-054-readiness; goal_pipeline GAP-2 survival-leg cohort

## Problem

The V3-EXQ-603h Stage-H validation FAIL (2026-06-08; failure_autopsy_V3-EXQ-603h_2026-06-08)
adjudicated **engaged-but-insufficient**: the SD-058/MECH-357 ilPFC gate engaged
and suppressed the MECH-279 PAG freeze on all INTACT seeds (`readiness_met=true`),
but `G_H_INTACT` was 0/3 and did not beat LESION. The disambiguator read straight
off `ree_core/pfc/infralimbic_avoidance_gate.py`:

1. **Freeze-suppression works; relief credit starves.** `n_freeze_suppressed`
   65/268/75 across seeds, but the efficacy-credit event (a *directed* action under
   threat that *drops* z_harm_a) almost never fired (`n_credit` 6/0 on 2/3 seeds vs
   `n_decay` ~15.5k), so `avoidance_efficacy` collapsed to ~0.
2. **Where efficacy DID accumulate, it bought no survival.** Seed-43 reached
   efficacy 0.633 and survived **worst** (11.0). Structural reason:
   `compute_action_bias` only **penalises the no-op/freeze class** proportional to a
   **scalar** efficacy and by design *"does NOT compute the escape direction"*. A
   high scalar efficacy un-freezes the agent and biases it to act, but binds no
   **specific** action/direction to relief. There is no escape *affordance*, only a
   global "avoidance works" scalar.

The agent learned to **twitch away from freeze without learning that a particular
action/direction is a relief/safety affordance** -- the user's Section 3 prediction
verbatim.

## Biological reference

Moscarello & LeDoux 2013 active avoidance = ilPFC suppresses CeA/PAG freezing **AND**
an LA/BA -> **NAcc** action pathway where CS-termination / response-produced safety
positively reinforces a *specific* avoidance response. The modern literature
(LeDoux/Moscarello/Sears & Campese 2017; Boeke/Phelps/Hartley 2017) frames the
reinforcer as circuit-level threat-removal + safety acquisition -- complementary
contributors, NOT subjective relief. REE built the **suppression** half (MECH-357);
the **NAcc relief/safety-credit -> approachable-affordance** half is the missing
dependency the 603h FAIL signatures. REE already owns relief (MECH-302) and safety
(MECH-303/304) primitives but they are **unwired to avoidance**.

## Solution

`ree_core/pfc/escape_affordance_bridge.py` (`EscapeAffordanceBridge` +
`EscapeAffordanceBridgeConfig` + `EscapeAffordanceBridgeOutput`). Pure-arithmetic
regulator (no `nn.Module`, no trained params, no gradient flow); sibling to the
SD-058/MECH-357 gate in `ree_core/pfc/`. Extends MECH-357's **scalar**
`avoidance_efficacy` into a **per-first-action-class credit table** -- the directed
escape (the discrete-action-space rendering of `escape_affordance[action]`).

**Two independently-toggleable halves** (so the 4-arm validation dissociates):

- **RELIEF half (MECH-302-consistent):** a directed action under threat that drops
  z_harm_a (`delta = prev - now > relief_reward_floor`) credits
  `relief_affordance[action_class]` (EMA toward 1) -- the same `d(z_harm_a)/dt < 0`
  signal MECH-302 fires on, attributed to the specific action that produced it.
- **SAFETY half (MECH-303/304-consistent):** a directed action after which threat is
  absent (`threat_scale <= 0`) credits `safety_affordance[action_class]`
  (response-produced safety / conditioned inhibition).

**Approach bonus (the directed escape):** under FUTURE threat (`threat_scale > 0`),
E3 receives a per-candidate **negative** score-bias (REE lower-is-better, so negative
= favoured) toward each candidate whose first-action class carries combined
affordance credit: `-clamp(approach_gain * threat_scale * combined_affordance[class],
0, bias_scale)`. The no-op/freeze class never gets a bonus.

**Three guards** (thought-intake design discipline):
1. clamped to `bias_scale` (mirrors the MECH-357/curiosity/vigor scale -> cannot
   dominate the additive score-bias chain);
2. **threat-context-gated** -- exactly zero when safe, so it never globally swamps
   food/goal approach;
3. per-tick **leak** on both tables (forgetting -> no pathological avoidance/habit
   loop).

**Distinct from** reflexive escape (SD-037 orexin raises PAG exit threshold; MECH-281
lowers the MECH-091 urgency-interrupt -- both threat/arousal reflexes) and from the
generic relief/safety rows (MECH-302/303/304 fire on the *current* state): this is
learned-efficacy-gated **directed approach** binding an action to relief/safety for
use under future threat.

### Config (REEConfig + from_dims; all no-op default, bit-identical OFF)

`use_escape_affordance_bridge` (False, master), `use_escape_relief_credit` (True),
`use_escape_safety_credit` (True), `escape_relief_learn_rate` (0.1),
`escape_safety_learn_rate` (0.1), `escape_bridge_leak_rate` (0.01),
`escape_relief_reward_floor` (1e-4), `escape_threat_floor` (0.1),
`escape_threat_ref` (0.5), `escape_approach_gain` (0.1), `escape_bias_scale` (0.1),
`escape_noop_class` (0). `n_action_classes` set from `config.e2.action_dim` at agent
build.

### Data flow

```
sense(): z_harm_a -> escape_affordance_bridge.update(z_harm_a_norm,
  last_action_class, ...) [one-tick lag; relief + safety credit; MECH-094 no-op
  under hypothesis_tag]  (after the MECH-357 eligibility update)
select_action(): per-candidate first-action classes + current z_harm_a ->
  escape_affordance_bridge.compute_approach_bias(...) -> negative bias on
  credited classes -> composed into dacc_score_bias AFTER the MECH-357 action-bias
select_action() end: cache _eab_last_action_class = argmax(action)
reset(): bridge.reset() clears within-episode trace; affordance tables persist
```

### Curriculum wiring

The bridge runs automatically inside the existing Stage-H training loop
(`scaffolded_sd054_onboarding.run_hazard_avoidance`) once the agent is built with
`use_escape_affordance_bridge=True`. `HazardAvoidanceResult.escape_bridge_state`
surfaces `bridge.get_state()` so the validation manifest can gate non-vacuity
(relief/safety credit actually incremented) before scoring G_H.

## What this SD enables

Closes the V3-EXQ-603h directed-escape gap: with the bridge ON, the agent acquires a
specific escape direction (relief/safety-credited action class) and approaches it
under future threat, rather than only un-freezing. Unblocks the goal_pipeline GAP-2
survival-leg retest cohort and the `pending_retest_after_substrate` claims
(ARC-060 / MECH-320 / ARC-068 / SD-054-readiness).

## MECH-094

Both compute methods and the eligibility update accept `simulation_mode` and are
no-ops when True (replay / DMN content must not credit escape affordances or bias
action selection on imagined outcomes). Call-site: `sense()` and `select_action()`
are waking-only; the bridge has no replay/memory write surface.

## Phased training

Not required at the substrate level (pure-arithmetic regulator; no learned params).
But the relief-credit detector reads z_harm_a / the world-forward, so it depends on a
trained encoder. The **validation experiment** keeps the SD-056 e2 contrastive warmup
in P0 + a relief-credit non-vacuity readiness gate -- without a trained encoder the
relief event re-starves the way it did on 603h (n_credit 6/0 on 2/3 seeds).

## Validation experiment

`V3-EXQ-603i` -- thought-intake Section 5 4-arm discriminative diagnostic
(`claim_ids=[]`):

- `ARM_BASE_IA_ONLY` (SD-058/MECH-357 as 603h INTACT)
- `ARM_RELIEF_BRIDGE` (IA + relief half)
- `ARM_SAFETY_BRIDGE` (IA + safety half)
- `ARM_RELIEF_SAFETY_BRIDGE` (both)
- plus a **nav-competence positive control** (oracle/hand-shaped escape gradient or
  reef-refuge reachability under threat) so a flat G_H across all bridge arms is
  attributable to a survival/navigation ceiling rather than the bridge being wrong.

Acceptance: readiness (PAG freezes; IA gate engages; each enabled bridge half fires
non-vacuously) -> primary `G_H >= 2/3` AND improves over `ARM_BASE_IA_ONLY` ->
secondary P1 survival transfer improves without over-avoidance/starvation. Interpretation
grid: relief-only / safety-only / both-required / neither-helps-AND-nav-control-fails
(route to a navigation/competence substrate, NOT the bridge).

## Safety-half trained-signal amend (V3-EXQ-603i secondary gap, 2026-06-09)

The 2026-06-08 landing wired the SAFETY half structurally but left it **starved**.
On **V3-EXQ-603i** the safety half credited **0/3 in every arm** (relief half 2/3,
functional) because its credit condition -- raw threat-absence `threat_scale(z_now)
<= 0` (i.e. `z_harm_a` norm below `threat_floor`) -- almost never fires under
Stage-H: the threat does not go fully absent after a single directed action. This is
the **symbol-of-mechanism-without-functional-input** gap named in
`failure_autopsy_V3-EXQ-603i_2026-06-08` (Section 4 Prerequisites (b), Section 6
Learning #2). REE already owns the trained threat-absence predictors -- **MECH-303**
(`ResidueField.evaluate_safety`, contextual RBF terrain) and **MECH-304**
(`ConditionedSafetyStore`, EMA-prototype cosine->sigmoid) -- but they were unwired to
the bridge.

**The fix (no-op default, bit-identical OFF; the bridge itself stays OFF by default):**

- `EscapeAffordanceBridgeConfig` gains `use_trained_safety_signal` (False) +
  `safety_signal_threshold` (0.5). `EscapeAffordanceBridge.update()` gains
  `safety_signal: Optional[float] = None`. The safety credit now fires on raw
  threat-absence **OR** (when `use_trained_safety_signal`) a trained
  `safety_signal >= safety_signal_threshold`. OR-composed -> the original raw
  mechanism is retained as a fallback; the trained path stays **inside** the existing
  under-threat (`prev > threat_floor`) + directed-action gate, so it credits genuine
  **response-produced** safety, not generic safe-context. New diagnostic
  `mech358_n_safety_credit_trained` attributes credits to the trained predictor (the
  non-vacuity readout).
- `ConditionedSafetyStore.predict(z_world)` -- a read-only cosine->sigmoid query (no
  decay/EMA mutation), additive and never called by existing paths -> zero behaviour
  change. Lets the agent read the MECH-304 prediction for the **current post-action**
  state at the bridge-update site (the store's own `update()` runs later in the same
  `sense()`, so the cached `_conditioned_safety_signal` is one tick stale).
- `agent.py`: at the bridge-`update` site, when `escape_use_trained_safety_signal` is
  on and not simulation, `_eab_safety_signal = max` over enabled trained predictors
  (MECH-304 `predict` + MECH-303 `evaluate_safety(...).mean()`, both pure reads) ->
  passed as `bridge.update(safety_signal=...)`. `None` when the flag is off ->
  bit-identical.
- `REEConfig.escape_use_trained_safety_signal` (False) +
  `escape_safety_signal_threshold` (0.5), wired through `from_dims`.

**Verification:** 7/7 preflight + 951 contracts PASS (2 new C9/C10 +
the prior 8). Activation smoke (bridge + MECH-304 + flag ON, retained threat): the
agent feeds a real trained signal (~0.375 on an untrained encoder), the under-threat
gate opens, and the safety half credits 5x via the trained signal
(`mech358_n_safety_credit_trained=5`); flag OFF reproduces the 603i 0/0.

**Governance:** SD-059 / MECH-358 are **neither validated nor weakened** by this amend
(stay `candidate` / `v3_pending` / `pending_retest_after_substrate`). V3-EXQ-603i
state is untouched; `claims.yaml` not modified. Validation: **V3-EXQ-603j** claim-free
safety-half-credit readiness microdiagnostic (OFF reproduces 603i `safety_credit~0`;
ON -> `mech358_n_safety_credit_trained > 0` on >=2/3 seeds). The full 4-arm G_H
behavioural retest stays gated on the **PRIMARY** nav/survival-competence ceiling
(scaffolded_sd054_onboarding Stage-H leg / separate chip) -- a retest can only score
G_H once nav competence clears too.

## Related claims

SD-058 / MECH-357 (parent gate), MECH-302 / SD-050 (relief), MECH-303/304 /
SD-052/SD-051 (safety), MECH-279 (PAG freeze), SD-011 (z_harm_a), SD-037 / MECH-281
(reflexive escape -- distinct), SD-056 (action-conditional divergence; relief-detector
prerequisite), ARC-060 / MECH-320 / ARC-068 (unblocked), MECH-094 (call-site scoping),
scaffolded_sd054_onboarding (Stage-H driver), goal_pipeline:GAP-2.
