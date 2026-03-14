# SD-003 Self-Attribution Experiment Design

**Status:** Active design — substrate ready, experiments pending (EXQ-027, EXQ-028)
**Date:** 2026-03-14
**Depends on:** EXQ-018 PASS (CausalGridWorld baseline — SD-003 substrate validation)

---

## Background

SD-003 (design_decisions.md §SD-003) opens the question: can the agent distinguish harm caused by
its own actions from harm caused by the environment? Without this, the residue field accumulates
moral weight regardless of whether the agent's policy was causally responsible.

The substrate is:
```
z_actual_next = e2.predict_next_state(z_t, a_actual)
z_cf_next     = e2.forward_counterfactual(z_t, a_cf)
causal_delta  = z_actual_next - z_cf_next   # agent's causal signature
```

`CausalGridWorld` provides ground truth: `transition_type ∈ {agent_caused_hazard, env_caused_hazard, resource, none}`.

---

## Critical Design Observation

In `CausalGridWorld`, **both** `agent_caused_hazard` and `env_caused_hazard` require the agent to
move into a hazardous cell:

- `agent_caused_hazard` — agent steps onto a cell it previously contaminated through visits
- `env_caused_hazard` — agent steps onto a cell with an environment-placed hazard

Because both types require voluntary movement, the raw action counterfactual
`||E2(z, a_actual) - E2(z, a_null)||` (null = stay) gives a **large delta for both** — it measures
action-dependence of the current step, not causal origin.

**The discriminating factor is in z_t, not in the action.** The contamination_view (5×5 float
grid) is part of the observation and thus encoded in z_gamma. If E2 has learned contamination
dynamics:
- For `agent_caused_hazard`: z_t encodes HIGH contamination at the target cell (agent placed it)
  → E2 can predict the harm from the contamination signal alone
- For `env_caused_hazard`: z_t encodes LOW contamination at the target cell (env hazard, not agent
  contamination) → E2 cannot "see" the hazard as clearly in the contamination view

**Testable hypothesis:** `E2.predict_harm(z_t, a_actual)` is better calibrated (higher) before
`agent_caused_hazard` transitions than before `env_caused_hazard` transitions, after sufficient
training — because contamination is visible in z_t while env hazards are not directly encoded there.

---

## Claim Structure

### MECH-071 — E2 Harm Prediction Calibration Asymmetry

**Claim:** After training, E2 predicts harm more reliably before agent-caused transitions than
before environment-caused transitions, because agent contamination is encoded in z_gamma while
environment hazard placement is not.

**Operationalisation:** `calibration_gap = mean(E2.predict_harm(z_t, a_actual) | agent_caused)
- mean(E2.predict_harm(z_t, a_actual) | env_caused) > 0` after training but not with random weights.

### MECH-072 — Foreseeable-Harm Residue Gating

**Claim:** Gating residue accumulation on E2 harm foreseeability (`E2.predict_harm(z_t, a_actual)
> threshold`) reduces false attribution (residue at env-caused events) versus naive accumulation.

**Operationalisation:** `false_attribution_rate = residue_at_env_caused / total_residue_events`
is lower under FORESEEABLE than NAIVE, without degrading harm avoidance.

---

## Experiment EXQ-027 — E2 Attribution Calibration

**Backlog:** EVB-0046
**Claim:** MECH-071

### Design

Two conditions:
- **TRAINED** — agent (including E2) trained for `WARMUP_EPISODES=200` then evaluated for
  `EVAL_EPISODES=50`
- **RANDOM** — no warmup; E2 at random initialisation; evaluated for `EVAL_EPISODES=50`

At each step during evaluation:
1. `action, log_prob = agent.act_with_log_prob(obs)` → updates z_t internally
2. `z_t = agent._current_latent.z_gamma.detach()` — latent state before env step
3. `predicted_harm = agent.e2.predict_harm(z_t, action).item()`
4. `obs_next, harm, done, info = env.step(action)`
5. Record `(predicted_harm, info['transition_type'])` when `harm < 0`

### Metrics

- `calibration_gap = mean_ph[agent_caused] - mean_ph[env_caused]` (ph = predicted harm)
- Both conditions reported

### Pass Criteria

- TRAINED `calibration_gap > 0.05` — E2 measurably foresees agent-caused harm better
- RANDOM `calibration_gap_abs < 0.1` — no spurious discrimination from random weights (control)

---

## Experiment EXQ-028 — Selective Residue Attribution

**Backlog:** EVB-0047
**Claim:** MECH-072

### Design

Three conditions run with full training (E1 + E2 + policy):

- **NAIVE** — `agent.update_residue(harm)` called on every `harm < 0` step (current behaviour)
- **FORESEEABLE** — `agent.update_residue(harm)` only when `predicted_harm > ATTRIBUTION_THRESHOLD`
  (threshold = 0.3, empirically chosen from EXQ-027 distribution)
- **ORACLE** — `agent.update_residue(harm)` only when `info['transition_type'] == "agent_caused_hazard"`
  (ground truth upper bound — cannot be implemented in production, only for analysis)

At each step where `harm < 0`:
- Compute `predicted_harm = agent.e2.predict_harm(z_t, action)` before `env.step()`
- Record: `(predicted_harm, transition_type, condition, residue_accumulated)`

### Metrics

- `false_attribution_rate = steps where (residue_accumulated AND transition_type == "env_caused") / total residue_accumulated steps`
- `true_attribution_rate = steps where (residue_accumulated AND transition_type == "agent_caused") / total agent_caused harm steps`
- `final_harm = mean harm last quartile of episodes`

### Pass Criteria

Both must hold:
1. `false_attribution_rate[FORESEEABLE] < false_attribution_rate[NAIVE]` — gating reduces false attribution
2. `final_harm[FORESEEABLE] <= final_harm[NAIVE] * 1.05` — harm avoidance does not degrade

ORACLE serves as an interpretive bound: if ORACLE is not substantially better than NAIVE,
the attribution distinction doesn't matter much for harm avoidance.

---

## Sequencing

```
EXQ-018 (CausalGridWorld Baseline)
    ↓ PASS required
EXQ-027 (E2 Attribution Calibration)   ← Does E2 actually discriminate?
    ↓ informs ATTRIBUTION_THRESHOLD for EXQ-028
EXQ-028 (Selective Residue Attribution) ← Does gating help?
```

If EXQ-027 shows `calibration_gap ≈ 0` (E2 cannot discriminate), EXQ-028 becomes moot.
In that case: SD-003 requires extending either the environment (give env hazards a latent signature)
or the E2 architecture (explicit contamination tracking).

---

## Future Extension (not in scope for V2)

If EXQ-027 PASSES, SD-003 can be extended to:
- Multi-step causal attribution: "which of my past actions created this contamination?"
- Policy counterfactual: "what harm would have occurred under a more cautious policy?"
- Integration with SD-004 action objects: action objects encode moral footprint directly

These would be V3 or late V2 experiments.
