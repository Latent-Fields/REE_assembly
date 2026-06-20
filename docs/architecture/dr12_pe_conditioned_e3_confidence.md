---
title: "DR-12: E2 forward prediction-error modulates E3 trajectory-scoring confidence"
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 4
---

# DR-12: E2 forward prediction-error modulates E3 trajectory-scoring confidence

**Claim ID:** (DR-12 audit item; v4_spec.md V4-2) -- owner node `self_model_v4:SELF-4`
**Unblocks:** MECH-215 (self-model prerequisite for agentive prediction -- the E2
self-transition-accuracy half)
**Subject:** ethics_engine_3.pe_conditioned_confidence_weighting
**Status:** IMPLEMENTED 2026-06-17
**Generation:** v4 (FIRST V4 substrate build; off the V3 critical path; promotes nothing in V3)
**Depends on:** SD-005 (z_world/z_self split, implemented), ARC-016 (E3 dynamic precision,
implemented), SD-056 (E2 action-conditional forward divergence -- the trained source of a
meaningful forward-PE, implemented)
**Blocks:** the DR-10+DR-12 pair that unblocks MECH-215; the V4 self-model cutover pattern

---

## Problem

DR-12 from `docs/architecture/v4_spec.md` V4-2: *"E3 trusts E2's rollout
unconditionally. When E2's capacity model is degraded (producing inflated or deflated
predictions), E3 inherits the error with no 'this rollout might be unreliable' signal.
V4 needs E2 PE magnitude to modulate E3's confidence in each trajectory's
self-transition feasibility, so that trajectories generated from unreliable E2
predictions are appropriately discounted."*

V3 today: `E3.score_trajectory()` scores `J(zeta) = F + lambda*M + rho*Phi - beta*B - goal`
purely from the E2-rolled-out `world_states`, trusting them as if E2 were perfectly
reliable everywhere. E3 already maintains two PE-magnitude signals it consumes for its
own dynamics -- `_running_variance` (ARC-016 EMA of the world-forward prediction error)
and `_novelty_ema` (MECH-111 EMA of E1 prediction error) -- but neither down-weights a
trajectory's viability as a function of how poorly E2 models *that trajectory's region*.

This is the **most V3-tractable** of the five DR cutover steps (v4_spec: "partly
addressable in V3"): it keys off PE magnitude, which is present in V3 today, and needs no
stateful z_self substrate. It is sequenced as the **cheapest cutover step and a natural
pilot** -- the first V4 experiment, proving the E2-PE -> E3-confidence wiring pattern for
the rest of the self-model roadmap.

## Solution

A **no-op-default monotone confidence-by-PE lever** in `E3TrajectorySelector`. The lever
adds, per trajectory, a penalty proportional to a monotone function of the E2-forward-PE
magnitude attributed to that trajectory's region. Because REE scoring is lower-is-better,
a higher PE raises the trajectory's cost -> the trajectory is discounted (its
viability/confidence is down-weighted). The lever is a NEW term on EXISTING machinery
(the same per-candidate score-composition path the modulatory channels already use); it
adds no learned parameters.

**Where the penalty is applied (the lever -- `score_trajectory`):**

```
score = F + lambda*M + rho*Phi - beta*B - goal_term            # unchanged J
if config.use_pe_confidence_weighting and e2_forward_pe is not None:
    score = score + config.pe_confidence_weight * penalty(e2_forward_pe)
```

`penalty(pe)` is monotone non-decreasing in PE magnitude:
- `mode = "linear"` (default): `penalty = pe`
- `mode = "saturating"`: `penalty = 1 - exp(-pe / pe_confidence_scale)` in `[0, 1)` -- a
  bounded confidence-deficit reading.

**Per-candidate threading (so it can change selection):** `select()` accepts an optional
`e2_forward_pe_per_candidate` `[K]` tensor and passes element `i` into candidate `i`'s
`score_trajectory` call. A per-candidate PE that varies across candidates can change the
committed argmin; a uniform scalar would be argmin-invariant (the V3-EXQ-571 deleted-
broadcast-novelty lesson), which is why the signal is per-candidate, not global.

**Diagnostics** (`last_score_diagnostics`, for the pilot's non-vacuity gate):
`pe_confidence_active` (bool), `e2_forward_pe_range` (cross-candidate range of the supplied
PE), `pe_confidence_weight`, `pe_confidence_penalty_range` (cross-candidate range of the
applied penalty).

### Config (all no-op default; bit-identical OFF)

| Param | Type | Default | Purpose | Class |
|-------|------|---------|---------|-------|
| `use_pe_confidence_weighting` | bool | `False` | master switch | E3Config (+ REEConfig mirror) |
| `pe_confidence_weight` | float | `0.0` | monotone penalty gain | E3Config |
| `pe_confidence_mode` | str | `"linear"` | `linear` \| `saturating` | E3Config |
| `pe_confidence_scale` | float | `1.0` | saturating-mode scale | E3Config |

With `use_pe_confidence_weighting=False` (or `e2_forward_pe`/`e2_forward_pe_per_candidate`
absent), the lever is skipped entirely -> bit-identical to the pre-DR-12 selector.

### Per-candidate E2-forward-PE source (v1 scope decision)

v1 is **caller-supplied**: the lever consumes a per-candidate PE passed into `select()`
(the established `score_bias` / `channel_route_bias` threading precedent). The DR-12 pilot
is a **controlled substrate-readiness probe** (V4-EXQ-001) that assigns a known
per-candidate PE (high on the primary-best candidate, low elsewhere) and tests whether
the ON arm selects differently from the unconditional-trust (weight 0) baseline. This
matches the SELF-4 spec ("keys off PE magnitude present in V3 today; no stateful substrate
required").

`REEAgent.select_action` plumbs an optional injected per-candidate PE
(`agent._injected_e2_forward_pe`, default `None`) through to `e3.select(...)` so the lever
is reachable from the waking loop in future; absent injection it passes `None` ->
bit-identical.

**Documented follow-on (NOT v1):** an *ecological* region-PE auto-source -- extend E3's
existing global `_running_variance` EMA into a region-keyed E2-forward-PE reliability map
updated in `post_action_update`, looked up per-trajectory at score time -- so the lever is
driven automatically in a real run without probe injection. That is a separate evidence
experiment once the wiring's value is shown; it is the only piece that adds new state, and
it is deferred precisely to keep v1 a "lever on existing machinery."

## What this enables / the falsifier

**FALSIFIER (SELF-4 graduation decision):** *if PE-conditioned confidence weighting does
NOT change trajectory selection in high-PE (poorly-modelled) regions vs the
unconditional-trust baseline, DR-12 buys nothing and the wiring is inert.* The pilot
(V4-EXQ-001) pre-registers:
- a **non-vacuity precondition** (cross-candidate `e2_forward_pe_range` >= floor; else
  `substrate_not_ready_requeue`, never a false negative), and
- an **inert-wiring off-ramp** (range clears but ON==OFF selection -> DR-12 buys nothing).

PASS = the ON arm avoids the high-PE candidate the OFF arm selects, i.e. the
E2-PE -> E3-confidence cutover wiring is live and consequential. This is the DR-10+DR-12
pair's E2-self-transition-accuracy half that unblocks MECH-215.

## Architecture context

- **ARC-016** already derives E3 dynamic precision from E3's OWN running variance; DR-12
  extends precision-weighting to the **E2 forward** stream, per-region/per-candidate.
- **MECH-111** novelty (E1 PE) and **ARC-016** running-variance (world-forward PE) are the
  sibling PE-magnitude signals E3 already consumes; DR-12 adds the E2-forward-PE lever
  alongside them.
- **DR-10** (SELF-3, z_self in E3 viability scoring) is the other half of the MECH-215
  unblock; DR-12 is independently landable and does not require a stateful z_self.

## ML/AI engineering parallel (Layer 7)

Pessimism-under-model-uncertainty (MOReL / MOPO): in offline model-based RL the value is
penalized in proportion to the dynamics model's error/uncertainty so the policy avoids
regions the model predicts poorly. DR-12 is the same engineering move at the E3
trajectory-scoring locus, with two REE-specific adaptations: (a) the uncertainty signal is
the **observed E2 forward-PE magnitude**, not ensemble disagreement (REE has no ensemble);
(b) the locus and grounding are neuroscientific (precision-weighting of an internal forward
model, ARC-016 extended to the E2 stream), not RL value estimation. Hazard imported from
the modulatory-authority cluster: a PE penalty whose scale is mismatched to the primary
score range either vanishes or dominates -> the pilot pre-registers the PE-range
non-vacuity gate and calibrates `pe_confidence_weight`.

## Related claims

MECH-215 (unblocked, stays candidate/v4), ARC-016 (E3 dynamic precision -- extended),
MECH-111 (sibling E1-novelty PE), SD-056 (trained E2 forward divergence -- the source of a
meaningful forward-PE), DR-10/SELF-3 (the z_self-in-E3 half of the MECH-215 unblock),
MECH-094 (call-site scoping; N/A -- waking selection, no replay write surface).
