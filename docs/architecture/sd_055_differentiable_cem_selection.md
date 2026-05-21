---
nav_exclude: true
---

# SD-055: Differentiable CEM Selection Approximation

**Claim ID:** SD-055
**Subject:** `hippocampal.differentiable_cem_selection`
**Status:** IMPLEMENTED 2026-05-15 (substrate-readiness PASS V3-EXQ-568 20260515T204931Z)
**Registered:** 2026-05-15
**Depends on:** SD-016 (frontal cue integration -- cue_action_proj consumer)
**Blocks:** ARC-072 (gap 2 V3 staging), MECH-326 (differentiable PFC-to-retrieval path prerequisite)

---

## Problem

EXP-0155 and V3-EXQ-449 established that `cue_action_proj` receives zero gradient under
default HippocampalModule CEM: elite selection uses `argsort` on trajectory scores, and
`agent.py` detaches `action_bias` before rollouts. The structural hook from SD-016 is
present but the selection operator is not differentiable.

Failure signature: `cue_action_proj.weight` grad norm = 0.0; `action_bias_divergence` ~ 0.0
in SD-016-enabled experiments.

---

## Solution

Opt-in softmax-weighted mean over **all** candidate action-object sequences when
`use_differentiable_cem=True`:

```
weights = softmax(-scores / temperature)   # lower score -> higher weight
ao_mean = sum_i weights[i] * ao_seq[i]
```

Legacy path (`use_differentiable_cem=False`, default): argsort elite indices + indexed mean
unchanged.

**Module:** `ree_core/hippocampal/module.py` (post-elite refit distribution block).

**Config:** `HippocampalConfig.use_differentiable_cem` (bool, default False);
`HippocampalConfig.differentiable_cem_temperature` (float, default 1.0).
Surfaced via `REEConfig.from_dims(...)`.

ARC-007 STRICT preserved: scoring still uses `_score_trajectory` over residue terrain;
no value head added in hippocampal module.

---

## Architecture Context

- SD-016 `cue_action_proj` injects PFC affordance bias into E2 rollouts inside CEM.
- SD-055 restores gradient flow **when the flag is ON**; it does not implement
  MECH-325 trajectory library or MECH-326 context-sensitive retrieval gate.
- Complements ARC-065 support-preserving CEM (within-tick diversity) but addresses a
  different failure mode (cross-tick cue learning, ARC-072 gap 2).

---

## What This SD Enables

| Downstream | Scope |
|------------|-------|
| ARC-072 gap 2 | V3 staging: gradient can reach cue_action_proj under differentiable CEM |
| MECH-326 | Prerequisite for V3 staging path in claims.yaml (full routing still V4) |
| SD-016 experiments | May enable supervised / joint training paths previously blocked |

Behavioural claim (cue-conditioned candidate divergence on goal-rich env) is **not**
validated by substrate-readiness; requires a separate training experiment.

---

## Related Claims

MECH-326, ARC-072, SD-016, INV-073, MECH-325

**Validation:** V3-EXQ-568 (diagnostic, non_contributory, PASS 5/5 UC, grad_max=372).

**Smoke:** `ree-v3/smoke_sd055_differentiable_cem.py` (4/4 PASS).
