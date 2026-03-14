# Self vs World Latent Split — SD-003 Limitation and V3 Direction

**Date:** 2026-03-14
**Status:** unprocessed
**Connects to:** SD-003, SD-004, MECH-071, MECH-072, E2, E3, z_gamma

---

## The Observation

SD-003 as designed (EXQ-027, EXQ-028) tests whether E2 can discriminate agent-caused from
environment-caused harm using E2.predict_harm(z_t, a_actual). But there is a deeper problem
that V2's architecture cannot address:

**z_gamma conflates what the agent IS with what the agent DOES.**

When E2 predicts `z_{t+1}` from `(z_t, a_t)`, the predicted change includes:

1. **Self-directed effects** — consequences of the action on the agent's OWN sensory streams:
   - Proprioceptive: body position changed, limb moved
   - Interoceptive: energy expenditure, fatigue accumulation, internal state shift
   - These are IMMEDIATE, DIRECT, action-determined

2. **World-directed effects** — consequences of the action on the EXTERNAL world:
   - First-order: I contaminated the cell I stepped on (immediate)
   - Second-order: that contamination will harm me when I return (delayed)
   - These involve TEMPORAL DISTANCE and CAUSAL CHAINS

In V2, both kinds of effect live in z_gamma. E2 cannot know whether its prediction delta
reflects "my body state changed" or "the world state changed due to my action."

---

## Why This Matters for Attribution

Moral residue should accumulate on WORLD-DIRECTED harm, not on self-directed state change.

- "I expended energy walking" → z_self change → self-preservation signal, not moral residue
- "I contaminated the path behind me" → z_world change → moral footprint, should drive residue
- "I walked into an env hazard" → z_world provided the hazard; my action provided the entry
  → partial responsibility, requires decomposition

The causal_delta as computed in SD-003 (`||E2(z, a_actual) - E2(z, a_cf)||`) conflates
the proprioceptive delta (how my body moved differently) with the world delta (what my
action did to the environment). These two components may not have the same magnitude
relationship to moral responsibility.

---

## The E2 vs E3 Asymmetry

This maps naturally onto E2 vs E3:

| | E2 domain | E3 domain |
|---|---|---|
| **Latent** | z_self (body state) | z_world (environment) |
| **Effects** | Direct motor-sensory | Delayed, consequence-bearing |
| **Error signal** | Motor-sensory prediction error | Harm + goal error |
| **Horizon** | Medium (rollout_horizon=30) | Long (planning, hippocampal map) |
| **Moral weight** | Low (self-preservation, not residue) | High (world footprint, residue) |

E2's job is: "given I took this action, what happened to MY body?" — updating the agent's
self-model. E3's job is: "what happened to the WORLD, and what should I do about it?"

The self-directed / world-directed split is not currently reflected in the architecture.

---

## V3 Design Sketch

Split z_gamma into:
- `z_self` — proprioceptive + interoceptive channel. Continuously updated from body-state
  observations. E2 operates here. Motor-sensory error = prediction error on z_self_{t+1}.
- `z_world` — exteroceptive world model. Updated from environment observations.
  E3 plans over this. Harm/goal error lives here.

The SD-003 causal signature then decomposes:
```
self_delta  = ||E2(z_self, a_actual)  - E2(z_self, a_cf)||   # body state change
world_delta = ||E3_world(z_world, a_actual) - E3_world(z_world, a_cf)||  # world change
```

Residue accumulates on world_delta, not self_delta.

Claim: `world_delta` discriminates agent_caused_hazard from env_caused_hazard better than
the current conflated causal_delta, because env hazards are in z_world but are NOT caused
by the agent's action (low world_delta) while contamination IS caused by the agent's visits
(high world_delta over the full trajectory).

This would also integrate cleanly with SD-004 (action objects): action objects encode
`(z_world_{t} → z_world_{t+1})` under action `a_t` — the action's world-model footprint,
compressed. This is exactly the z_world delta.

---

## Effect on SD-003 as Designed

The V2 SD-003 experiments (EXQ-027, EXQ-028) remain valid as a first approximation:
- CausalGridWorld's contamination is visible in the observation → encoded in z_gamma
- E2 may learn to use contamination features even within the conflated z_gamma
- The discrimination result (MECH-071) will measure whether this works in practice

If EXQ-027 shows weak discrimination (calibration_gap close to threshold), the self/world
conflation is a likely explanation: E2's causal_delta is noisy because proprioceptive
self-effects (moving, energy) are swamping the contamination signal in the latent delta.

If EXQ-027 shows strong discrimination, z_gamma is learnable enough that E2 can implicitly
factor out the self-effects — useful to know before adding the architectural complexity.

---

## V3 Consideration: SD-005?

Possible design decision to document for V3:

**SD-005 — Self/World Latent Split**
- z_gamma split into z_self (E2's domain) and z_world (E3's domain)
- E2 becomes a pure body-state predictor: f(z_self_t, a_t) → z_self_{t+1}
- E3/Hippocampus plans over z_world; residue field operates over z_world
- Observation encoder routes sensory channels to the appropriate stream
- Motor-sensory error = z_self prediction error (clean proprioceptive signal)
- Harm/goal error = z_world consequence prediction error (clean world signal)

This would also clarify MECH-069 (error signal incommensurability): the incommensurability
is not just about learning rates — it's about the ONTOLOGICAL CATEGORIES being different.
Self-state prediction error and world-consequence error are different kinds of thing.

---

## The Philosophical Point

"What I am" vs "what I do" is a fundamental distinction in moral psychology.
The current architecture doesn't make this cut.

- z_self = what the agent IS at each moment (body, energy, internal state)
- z_world = what the agent is DOING TO the world (its causal footprint)

REE's residue field should track z_world changes, not z_self changes. An agent that
exhausts itself doing nothing harmful has high self-state change and zero world-change.
An agent that causes contamination has high world-change. Currently both look the same
to the residue field if harm_signal is the same magnitude.

The self/world split would ground the residue field in the right causal substrate.
