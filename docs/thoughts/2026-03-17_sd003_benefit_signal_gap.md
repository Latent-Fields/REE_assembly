# SD-003 Attribution Gap — Benefit Signal Missing from E3 Evaluator

**Date:** 2026-03-17
**Status:** unprocessed
**Connects to:** SD-003, MECH-095, MECH-071, V3-EXQ-002 through EXQ-010

---

## Observation

SD-003 V3 calibration_gap has plateaued at ~0.027 across all variants (EXQ-002r1–r6,
EXQ-007–010). The E2+E3 joint pipeline is:

```
causal_sig = E3.harm_eval(E2.world_forward(z_world, a_actual))
           - E3.harm_eval(E2.world_forward(z_world, a_cf))
```

`harm_eval` is trained as a **binary classifier**: harm states (label=1) vs
no-harm states (label=0). This has a structural problem: it creates zero
contrast between *beneficial* z_world states and *neutral* z_world states.
Both are labelled 0.

CausalGridWorld's `harm_signal` is already **signed**:
- `agent_caused_hazard` → -0.4
- `env_caused_hazard`   → -0.5
- `resource`            → +0.3
- `none`                → 0.0

The environment provides a full net_eval signal. We are discarding half of it.

---

## Why This Causes Low Calibration Gap

The probe evaluation places the agent adjacent to a hazard and computes
`causal_sig = harm_eval(z_world_actual) - harm_eval(z_world_cf)`. For this
to be positive, `harm_eval(z_world_actual)` must reliably exceed
`harm_eval(z_world_cf)`.

With binary classification:
- z_world_actual (agent enters hazard): scored based on similarity to
  known harm-state z_worlds — noisy, because z_world is a compressed
  representation where adjacent-to-hazard looks similar to in-hazard
- z_world_cf (agent takes different action): scored similarly, because
  the nearby cells are also in the harm-neighborhood the classifier learned

The classifier learns the **neighborhood** of hazards as generally harmful,
not the sharp action-conditional boundary between entering and not entering.

With **signed regression** (net_eval regresses against actual harm_signal):
- E3 learns: resource cells → +0.3, hazard cells → -0.5, contaminated → -0.4, empty → 0
- The contrast between z_world_actual (just entered hazard, -0.5) and
  z_world_cf (safe cell, 0.0 or +0.3 if near resource) is exact and unambiguous
- E2.world_forward only needs to learn that different actions produce
  different z_world states — the evaluator provides the valence gradient

Additionally, training on harm-only (RANDOM policy) means:
- E3 sees sparse positive training signal (resources are collected occasionally
  by a random walk but not reliably)
- The net_eval function is calibrated mostly around neutral→harm, not neutral→benefit
- A **goal-seeking policy** would generate dense resource collection trajectories,
  giving E3 strong positive signal examples alongside harm examples

---

## The Analogy to Reinforcement Learning

The current setup is equivalent to training a value function only on negative
rewards. A zero-centered value function (benefit - harm) provides sharper
gradients because the contrast between chosen and counterfactual trajectories
is amplified: instead of (harm_high - harm_low), the contrast is
(benefit_high - harm_low), which is a larger and more consistent signal.

---

## Proposed Fix

**Minimal change (V3-EXQ-012):** Replace binary `harm_eval` BCE with a
**signed regression `net_eval` head** trained on actual `harm_signal` values.
Keep RANDOM policy. Include resource benefit steps in training.

Expected effect: net_eval learns the sharp ±0.3–0.5 value boundaries.
`causal_sig` = `net_eval(z_world_actual) - net_eval(z_world_cf)` will have
stronger contrast for near-hazard probes.

**Extended (V3-EXQ-013, if EXQ-012 fails):** Add a **resource-seeking policy**
during warmup (epsilon-greedy toward nearest resource). Dense benefit events
improve net_eval training. Agent-caused contamination now arises from
purposive trajectories (moving toward resource across contaminated cells),
making the causal signature sharper: the agent's path choice is the
discriminating factor.

---

## Architectural Note

This gap connects to the MECH-069 incommensurability claim: E3 trains on
**harm/goal error**, not just harm error. "Goal error" = failure to achieve
benefit (resource collection, waypoint completion). The current E3 has no
goal representation — only harm avoidance. The full incommensurability test
(MECH-069 strong form, V3-EXQ-004 partial FAIL) cannot be validated until E3
has a benefit/goal signal alongside harm.

This is also relevant to MECH-060 (dual error channels): the pre-commit
simulation error should evaluate both harm AND benefit; the current pipeline
only down-weights harmful trajectories without up-weighting beneficial ones.
