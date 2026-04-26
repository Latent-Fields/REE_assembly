---
nav_exclude: true
---

# D_V Temporal-Depth Verisimilitude — V3 Synaptic Form (ARC-054 V3 promotion)

**Claim cluster:** ARC-054 (D_V trajectory selection -- promoted v4 -> v3 in rollout-horizon
synaptic-EMA form), INV-068 (temporal depth requirement), MECH-269 (per-region V_s),
MECH-284 (staleness accumulator).
**Registered:** 2026-04-26
**Status:** candidate, implementation_phase: v3, v3_pending: true (V3 form);
ARC-054 V4 form (with full ARC-053 TCL substrate + MECH-225 oscillatory multiplexing +
MECH-228 ephaptic field-coherence) remains v4-deferred.
**Origin:** thought_intake_2026-04-09_verisimilitude_ethics.md Thread A.
**Architectural commitment:** the V3 working-model needs a temporal-depth signal that
hippocampal rollout evaluation can integrate over its planning horizon. The V4 form
requires phase-coherent substrate (TCL); the V3 form approximates this with a synaptic
EMA over a content-similarity proxy. The V3 form is sufficient to close the temporal-depth
gap that surfaced in EXQ-074b/076b path collapse and the EXQ-471/478/480/483/483a freeze-
recommit oscillations. The V4 form refines, not replaces, the V3 form.

---

## Why promote now (the gap)

ARC-054 in its full V4 form (J(pi) = sum_k gamma^k * V_hat_pi(t+k) over a phase-coherent
TCL) is correctly v4-deferred -- the substrate it depends on (ARC-053 distributed phase
loop, MECH-225 oscillatory multiplexing, MECH-228 ephaptic field-level coherence) is not
in V3 scope.

But MECH-269 V_s as currently implemented is *instantaneous*. The waking-arm circuit
(MECH-287 broadcast trigger + MECH-284 staleness accumulator + MECH-269 anchor-reset
hysteresis) tells E3 *that* an anchor's verisimilitude has degraded; it does not tell E3
how the predicted future verisimilitude trajectory of a candidate rollout compares to the
predicted future verisimilitude of an alternative. Several V3 failure modes implicate this
missing horizon-integration signal:

- **EXQ-471/478/480/483/483a freeze-recommit cycles**: SD-036 GABA decay releases the
  freeze gate, but E3 has no signal that the candidate trajectory drawn from the original
  avoid-anchor will *predictably* re-stoke z_harm_a within ~80 steps. Instantaneous V_s
  doesn't carry the projection.
- **EXQ-074b/076b path collapse** (MECH-124 z_goal salience diagnostic): z_goal salience
  is not competitive with harm salience because the rollout cost is instantaneous; a
  trajectory with high anticipated future D_V (sustained coupling to a goal-relevant
  schema) is not preferred over a trajectory with high instantaneous V but predicted
  collapse.
- **SD-029 monostrategy lock-in** (V_s_baseline-monostrategy diagnostic EXQ-482):
  rollout evaluation cannot compare alternative operating modes when each mode's
  verisimilitude is read at a single timestep.

The V3 D_V form closes this gap synaptically.

---

## V3 form (rollout-horizon synaptic-EMA D_V)

### Variables

For each candidate rollout `pi` proposed by the hippocampal proposer (MECH-269 anchored
draw + MECH-285 sleep-priority probe draw, both already implemented), and for each step
`k = 0, 1, ..., H` of the rollout (`H` = current planning horizon):

- `V_hat_pi(t+k)` -- predicted regional verisimilitude at step k of rollout pi.
- `D_V_pi(t+k)` -- predicted temporal-depth verisimilitude at step k.

### Computation (V3 form, no phase substrate)

`V_hat_pi(t+k)` is the **per-region V_s readout** (already implemented as MECH-269 Phase 2
iii T4 `per_region_vs[(scale, segment_id)][stream]`) read at the predicted future region
(scale, segment_id) that pi visits at step k. Source: the `BoundaryEvent` segmenter
(MECH-288) projects predicted segment_ids forward over the rollout. For steps where the
projected region is not in the AnchorSet, `V_hat_pi(t+k)` falls back to the per-stream V_s
EMA (MECH-269 Phase 1) at the upstream anchor's stream mixture.

`D_V_pi(t+k)` is an EMA over the rollout step:

```
D_V_pi(t+0) = V_hat_pi(t+0)
D_V_pi(t+k) = lambda * D_V_pi(t+k-1) + (1 - lambda) * V_hat_pi(t+k)   for k >= 1
```

with `lambda` configurable (`arc054_dv_lambda`, default 0.85 to match the typical
hippocampal rollout horizon of ~10-30 steps).

### Trajectory cost

`J(pi) = sum_{k=0}^{H} gamma^k * D_V_pi(t+k)` is added as an additive bias to the existing
E3 trajectory selection score (which already incorporates MECH-014 harm-cost, MECH-016
goal-attainment, etc.). `J(pi)` is exposed as `arc054_dv_score` in the rollout metadata so
governance experiments can measure the contribution.

### Wiring

- E3Selector reads `per_region_vs` via the existing HippocampalModule API.
- HippocampalModule grows a small helper `predict_rollout_vs(rollout) -> List[float]` that
  walks the rollout and reads `V_hat_pi(t+k)` per step using the MECH-288 segmenter
  projections.
- Master flag `use_arc054_dv` (default False, bit-identical-when-OFF preserved per the
  V3 substrate-flag convention).
- Sub-knobs: `arc054_dv_lambda` (EMA decay), `arc054_dv_gamma` (rollout discount, default
  matches `e3_planning_gamma`), `arc054_dv_score_weight` (scalar coefficient on additive
  bias, default 1.0), `arc054_dv_horizon_cap` (truncate at min(H, cap), default 30).

### What V3 deliberately does NOT include

- **No phase-channel projection** (MECH-225 oscillatory multiplexing). V3 reads V_s as a
  scalar per (region, stream); V4 will read phase-aligned V(t) components.
- **No TCL phase-coherence substrate** (ARC-053). V3 uses synaptic readout; V4 reads
  cross-frequency-coupled multiplexed signals.
- **No ephaptic field-level coherence support** (MECH-228). V3 treats V_s changes as
  discrete EMA updates; V4 will treat them as continuous field-level coupling magnitude.
- **No D_self computation** as a separate variable (INV-069 self-as-coherence-trajectory).
  V3 D_V is computed over the per-stream V_s readout, of which `z_self` is one stream;
  D_self is implicitly `D_V` restricted to `stream = z_self`. V4 may promote D_self to its
  own first-class signal.
- **No multi-agent extension** (β_j coefficients, ARC-056 ethics-as-coherence). V3 D_V is
  self-only; V4 social systems extend to D_{V,j} for represented others.

These deferrals are deliberate (see `v3_v4_phase_substrate_boundary.md`).

---

## Validation experiment (queue after implement-mech269b lock releases)

`V3-EXQ-491` (proposed): ARC-054 V3 D_V rollout-horizon validation, 4-arm factorial
{use_arc054_dv} x {EXQ-074b condition (z_goal salience contest), EXQ-481 condition
(V_s commit-release)}. Acceptance:

- C1 (EXQ-074b condition, ON arm): z_goal salience competitive with harm salience
  (`goal_action_share / harm_avoid_action_share >= 0.30` mean across 3 seeds; current
  baseline ~0.0).
- C2 (EXQ-481 condition, ON arm): freeze-recommit cycle count drops by `>=50%` vs OFF
  baseline (current ON_OFF mean = 5.3 releases / 12 recommits per release).
- C3 (bit-identical OFF): with master flag OFF, all metrics within 1e-9 of pre-flag
  baseline -- enforced by contracts test as standard for V3 substrate landings.
- C4 (instrumentation sanity): `arc054_dv_score` non-zero in all 3 seeds when ON;
  `mean(D_V_pi)` over evaluated rollouts in the expected range [0.0, 1.0].

Failure on C1 OR C2 with C3 + C4 PASS = V3 D_V form is a true-negative; consider whether
the V4 phase form is required (see Section "What V3 does NOT include"). Failure on C3 or
C4 = implementation bug, fix and retry.

---

## Lit-pull (deferred until promotion is committed)

Tagged `targeted_review_arc054_dv_rollout_horizon/`. Targets: rollout-horizon evaluation
in hippocampal replay (Pfeiffer & Foster 2013, Mattar & Daw 2018), persistence-of-coupling
signals in long-horizon planning (Schuck & Niv 2019), distinction between instantaneous
and integrated belief signals in non-stationary environments (Yu & Dayan 2005). Deferred
until claim status flip lands cleanly (avoid lit-pull-then-revert churn).

---

## Cross-references

- **V_s invalidation runtime** (`v_s_invalidation_runtime.md`): MECH-269 / MECH-284 /
  MECH-287 substrate that ARC-054 V3 reads from.
- **V3/V4 phase substrate boundary** (`v3_v4_phase_substrate_boundary.md`): the explicit
  architectural commitment that V3 working-model uses synaptic V_s + EMA D_V, and that
  ARC-053 / MECH-225 / MECH-226 / MECH-228 stay v4 as refinements.
- **Verisimilitude intake** (`evidence/planning/thought_intake_2026-04-09_verisimilitude_ethics.md`)
  Thread A: original formal definition of V(t), D_V, and the TCL.
- **MECH-269b** (`mech_269b_vs_rollout_gating.md`): the parallel session's symmetric V_s
  gating on E1/E2 forward predictions. ARC-054 V3 reads downstream of MECH-269b's gated
  predictions; the two land as compatible substrate refinements with the same OFF-default
  contract.
