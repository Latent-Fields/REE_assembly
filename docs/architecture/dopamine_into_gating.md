---
title: Learned dopamine-gated E3 selection (ARC-108 JOB-1 steps 1 + 2)
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 6
---

# Learned dopamine-gated E3 selection (ARC-108 JOB-1 steps 1 + 2)

**Claim:** ARC-108 (candidate / substrate_conditional / implementation_phase v3)
**Coupled:** MECH-450 (the recurrent-settling step — factor 2, **IMPLEMENTED 2026-06-22**)
**Status:** IMPLEMENTED 2026-06-22 — step 1 (`w_chan` + signed-RPE) + step 2 (the
MECH-450 learned-`W_lat` settling step) both landed; the two compose as the
learned-gating 2×2 the sec-7 falsifier exercises.
**Module:** `ree-v3/ree_core/predictors/e3_selector.py`
**Design-of-record:**
`REE_assembly/evidence/planning/dopamine_into_gating_design_2026-06-22.md` (secs 2-4) +
`REE_assembly/evidence/planning/unified_dopamine_substrate_design_2026-06-22.md` (sec 1, sec 10).

## Problem

The ARC-107 arbitration layer (MECH-447 conflict-grade, MECH-448 F→eligibility
demotion, MECH-449 Go/No-Go, the modulatory-authority rescale) is **pure
arithmetic with no learned parameters**. Learning exists only at the *valuation*
layer (`harm_eval_head`, `benefit_eval_head`); the *arbitration* does not learn.
In biology the cortico-striatal weights that decide which channel wins selection
authority are themselves learned by three-factor plasticity (Hebbian
co-activation × dopaminergic RPE) with a D1-LTP / D2-LTD asymmetry. F monopolises
88–89% of E3 committed-selection variance (V3-EXQ-571 / MECH-439) precisely
because there is **no learned striatal weighting that can re-weight channels
through experience** — every diversity channel is a fixed-magnitude bias
competing against a fixed primary score. The campaign's own failure history
(structural bounding works, parametric tuning does not, each structural lever
needs hand-calibration per channel) is the signature of a system that needs a
selection rule that *learns its weights*. This is the next MECH-439 attack:
**learned, not arithmetic.**

## What this build lands (JOB 1, step 1)

A single **learned per-channel selection-weight vector `w_chan`** over the
modulatory channels feeding the E3 selector's `_modulatory_accum`:

```
_modulatory_accum = sum_c  softplus(w_chan[c]) * channel_bias_c     # was the unweighted sum
```

- **Channels.** At the `_modulatory_accum` composition site the genuinely-separable
  constituents are the three add-terms already tracked there: `score_bias` (the
  composed dACC + lPFC + OFC + MECH-295 + MECH-314 + MECH-320 chain, summed
  *upstream* in `agent.py`), the MECH-341 entropy bonus, and the route bias. So the
  minimal registry is `("score_bias", "mech341", "route")` (C=3), indexed by name —
  a channel absent on a tick simply does not contribute, so `w_chan` stays a stable
  learned object. A finer per-head split is a documented follow-on (those biases are
  summed upstream before reaching `select()`).
- **No-op default.** `w_chan` is a `register_buffer` (NOT an `nn.Parameter` — the
  three-factor rule is a *local* update, never touched by an optimizer/autograd),
  init `w_chan[c] = ln(e−1)` so `softplus(w_chan[c]) == 1.0` exactly in float32 →
  the recompose reproduces the unweighted accumulator bit-for-bit (`1.0*x==x`,
  matching add order).
- **Composes inside the F-bounded eligible set.** Only `_modulatory_accum` is
  re-weighted; raw `scores` / F (the MECH-448 envelope + the commit decision) are
  untouched. So learning re-weights the *within-eligible* arbitration and **a learned
  weight can never re-admit a No-Go-suppressed candidate** — safety is inherited from
  the MECH-448/449 envelope.

### The teaching signal: a signed RPE (distinct from ARC-016 — divergence B5)

In `post_action_update(actual_z_world)` (the waking post-step hook):

```
R_t     = (benefit_eval_head - harm_eval_head)(actual_z_world)   # realised outcome valence, reuse trained heads, detached
V-hat_t = slow EMA leaky-integrator baseline of R                # the "expected" term
delta_t = R_t - V-hat_t                                          # SIGNED
```

`delta_t` is signed by construction and is **explicitly NOT** the unsigned ARC-016
prediction-error *variance* (`e3._running_variance`). They are kept separate
(divergence B5): an unsigned magnitude cannot supply the directional Go-up /
No-Go-down credit a learned gate needs. R_t reuses the already-trained valuation
heads — **no new encoder, no phased training.**

### Three-factor update (Hebbian × signed RPE × D1/D2 asym)

```
eligibility_c = |channel_bias_c[selected]|         # decayed last-K-ticks Hebbian co-activation trace (recorded in select())
Delta w_chan[c] = eta * delta_t * eligibility_c * asym(delta_t)
```

`asym` renders the D1-LTP / D2-LTD asymmetry as a single asymmetric gain
(potentiation on `delta_t ≥ 0` faster than depression on `delta_t < 0`) — the V3
single-vector rendering; the D1/D2 opponent-population split is **ARC-109 (deferred
V4)**. Applied in-place under `no_grad`.

### Waking-only gate (MECH-094)

`select()` gains a keyword-only `simulation_mode` (default `False`); eligibility is
recorded only when `not simulation_mode`, and `post_action_update` updates `w_chan`
only when a fresh waking eligibility trace is pending. A replay/DMN tick forms no
`delta_t` and writes no `w_chan`. Per-episode `agent.reset()` clears the
within-episode credit window (`e3.clear_learned_channel_eligibility()`); `w_chan`
and `V-hat_t` persist across episodes as the learned state.

## What this build lands (JOB 1, step 2 — MECH-450)

The SECOND factor of the learned-gating 2×2: a bounded recurrent **lateral-inhibition
settling step** over the F-bounded eligible set, parametrised by a LEARNED inhibition
matrix `W_lat`, sharing the SAME signed-RPE `delta_t` / `V-hat_t` / D1–D2 asym built in
step 1.

- **The settling step.** Runs at the within-eligible arbitration site (on
  `mod_eligible = _modulatory_accum[eligible_idx]`) BEFORE the commit:
  ```
  accum = _modulatory_accum[eligible_idx]
  for r in range(R):                       # R = learned_settling_rounds, default 3
      a       = softmax(-accum / T)        # support over eligible (low cost -> high)
      a_class = onehot.T @ a               # per-action-class aggregated support
      accum   = accum + onehot @ (W_lat @ a_class)   # learned lateral inhibition
  commit = argmin(settled accum)  (committed)  /  sample(softmax(-settled accum/T))  (uncommitted)
  ```
  Fixes divergence **B1** (one-shot argmin → recurrent settling) AND **B3-blend**
  (additive `_modulatory_accum` blend → competitive winner-take-most) together.
- **`W_lat` is over candidate first-action CLASSES**, not per-candidate `[K, K]`: the
  candidate set is variable-size with no stable identity, so the inhibition is
  parametrised by action class — a stable `[C, C]` learned object (the BG
  surround-inhibition between competing motor programs; Mink 1996, the opponency
  MECH-449 already grounds). `register_buffer` (NOT `nn.Parameter` — local plasticity,
  never an optimizer/autograd target). Init `W_lat = 0` → the settling step is a
  no-op → **bit-identical OFF and at init**.
- **Learned by the SAME three-factor rule** as `w_chan`, off one shared signed RPE:
  `post_action_update` computes `delta_t = R_t − V-hat_t` ONCE and applies
  `Delta W_lat ~ eta_w * delta_t * asym(delta_t) * coact_trace`, where `coact_trace` is
  the decayed Hebbian co-activation of the per-round settling-step class activations
  (recorded in `_lateral_settle`). One dopaminergic RPE drives both `w_chan` and `W_lat`.
- **Composes INSIDE the F-bounded eligible set.** The settling transforms ONLY
  `_modulatory_accum[eligible_idx]`; raw scores / F are untouched, so a learned `W_lat`
  can never re-admit a No-Go-excluded candidate — safety inherited from the MECH-448/449
  envelope, exactly as for `w_chan`.
- **Waking-only gate (MECH-094).** No settling and no `W_lat` write on a simulation
  tick (the within-eligible site gates the settling on `not simulation_mode`; the
  three-factor update fires only on a pending waking trace). `agent.reset()` clears the
  within-episode settling trace via `clear_learned_channel_eligibility()`; `W_lat` and
  `V-hat_t` persist across episodes.

## What is OFF / deferred

- **JOB-2 control-plane pair** (ρ_t maintenance ramp + habenula negative-`delta_t`
  de-commit on the `closure_exclusive_decommit_eval` substrate) — separate chip.
- **The sec-7 selection falsifier** (2×2 learned-`w_chan` × learned-`W_lat` on the
  GAP-A divergent pool; committed-class entropy strict-above the envelope-only arm
  AND a matched-noise control, growing with training, with the signed-vs-unsigned-RPE
  ablation) — `/queue-experiment` chip, sequenced after the settling step lands.

## Config (all no-op default → bit-identical OFF)

`E3Config` + `REEConfig.from_dims`:

- **Step 1 (`w_chan`):** `use_learned_channel_gating` (False, master),
  `learned_channel_gating_eta` (0.01), `learned_channel_gating_elig_decay` (0.9),
  `learned_channel_value_baseline_beta` (0.05), `learned_channel_asym_potentiation`
  (1.0), `learned_channel_asym_depression` (0.5).
- **Step 2 (MECH-450 `W_lat` settling):** `use_learned_settling_step` (False, master),
  `learned_settling_rounds` (3, R), `learned_settling_temperature` (1.0, T),
  `learned_settling_eta` (0.01, the `W_lat` learning rate), `learned_settling_elig_decay`
  (0.9, cross-tick co-activation decay), `learned_settling_n_action_classes` (8, the
  `W_lat` dimension = first-action class count, clamped). The settling reuses the step-1
  `delta_t` / `V-hat_t` / asym (one shared signed RPE).

## Validation

- **Step 1** — `tests/contracts/test_arc108_learned_channel_gating.py` (9 contracts):
  C1 config defaults + from_dims + softplus-unity init; C2 OFF == ON-at-init exact
  scores+selection, OFF writes no `w_chan`; C3 `w_chan` moves under a non-flat `delta_t`
  when ON / stays at init when OFF; C4 simulation tick writes no `w_chan`; C5 signed-RPE
  potentiate-vs-depress load-bearing (guards B5); C6 envelope intact.
- **Step 2 (MECH-450)** — `tests/contracts/test_mech450_learned_settling_step.py`
  (10 contracts): C1 config defaults + from_dims + `W_lat` zero-init; C2 OFF ==
  ON-at-init exact scores+selection, settling pass a no-op (round_delta 0), OFF writes no
  `W_lat`; C3 `W_lat` moves under a non-flat `delta_t` when ON (w_chan OFF — the settling
  learns independently) / stays at init when OFF; C4 simulation tick writes no `W_lat`;
  C5 non-degeneracy — a non-zero `W_lat` MOVES the field across rounds (round_delta > 0),
  no-op at init; C6 envelope intact — a strong `W_lat` cannot re-admit an F-excluded
  candidate; C7 shared `delta_t` — both `w_chan` and `W_lat` move off init under one RPE.

Preflight 8/8 + 74 e3-cluster contracts PASS. Selector activation: `W_lat` range moved
0.0 → 4.23 over 13 updates with a non-flat `delta_t`; the settling MOVES the field
(round_delta 6.16); OFF == ON-at-init bit-identical (exact scores + selection). Agent
env-loop smoke: the settling engaged 60/60 ticks ON, 0 OFF (wiring engages end-to-end).

## What remains

- The **sec-7 selection 2×2 falsifier** (learned-`w_chan` × learned-`W_lat` on the GAP-A
  divergent pool; committed-class entropy strict-above the envelope-only arm AND a
  matched-noise control, growing with training, with the signed-vs-unsigned-RPE ablation)
  is now fully runnable — both factors are built. A separate `/queue-experiment` chip.
- **JOB-2 control-plane pair** (ρ_t maintenance ramp + internal-habenula de-commit) — a
  separate chip.

**PROMOTES NOTHING.** ARC-108 stays candidate / substrate_conditional / v3; MECH-450
stays candidate / substrate_conditional / v3; the falsifier is a later step.
