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

---

## Missing Pieces (registered 2026-03-17)

A neuroanatomical review of the SD-005 design against known cortical architecture identified
four gaps. Three are registered as candidate claims (v3); one is a design constraint only.

### 1. TPJ Agency-Detection Comparator (MECH-095)

Separating z_self from z_world is necessary but not sufficient for SD-003 attribution.
A comparator mechanism is also required: at the z_self/z_world interface, the
efference-copy-predicted z_self change must be compared against the observed z_self change.
Match → self-caused (no residue). Mismatch → world-contributed cause (residue candidate).

Neural basis: temporoparietal junction (TPJ) computes forward-model prediction vs sensory
outcome mismatch for agency attribution. Blakemore, Wolpert & Frith (2002): the sense of
agency arises from exactly this comparator; failure produces schizophrenic passivity
phenomena (self-generated actions experienced as externally caused).

SD-003's causal_delta `||E2(z, a_actual) - E2(z, a_cf)||` approximates the counterfactual
mode of this comparator. Without MECH-095, the delta conflates proprioceptive self-effects
with world-directed footprint — the V2 EXQ-027/028 failure mechanism.

Literature: `evidence/literature/targeted_review_connectome_mech_095/`

### 2. Dual-Stream Observation Encoder (MECH-096)

SD-005's phrase "observation encoder routes sensory channels to the appropriate stream"
underspecifies the required architecture. A single encoder with a learned routing gate
will re-merge z_self and z_world toward z_gamma conflation under end-to-end gradient
pressure. The encoder must implement two architecturally separate output heads:

- **Dorsal-equivalent head** → z_self: egocentric, action-relevant, high temporal resolution
- **Ventral-equivalent head** → z_world: allocentric, object-identity, sustained representation

Neural basis: Goodale & Milner (1992) dorsal/ventral visual stream distinction. The dorsal
stream (V1→MT→PPC) and ventral stream (V1→V4→IT) remain anatomically separate throughout
the cortical hierarchy — their separation is an architectural commitment, not a learned
emergent property. Patient DF (visual form agnosia) demonstrates functional dissociation:
she cannot recognize objects she can accurately grasp.

The two-head requirement is not specific to visual modalities: the structural principle
(egocentric/action-relevant and allocentric/identity-relevant processing must be
architecturally separate) generalises to arbitrary observation spaces.

Literature: `evidence/literature/targeted_review_connectome_mech_096/`

### 3. Peripersonal Space as Commit Locus (MECH-097)

SD-005 lacks spatial grounding for where self ends and world begins. Without a
peripersonal space (PPS) representation, the encoder has no principled basis for
routing observations to z_self vs z_world — the routing decision degenerates to a
fixed threshold or heuristic.

PPS is the dynamically maintained near-body region where motor-action execution meets
world-directed consequence. In CausalGridWorld, contamination occurs exactly at the
PPS boundary: agent position (z_self) contacts cell state (z_world). PPS is not fixed:
it scales with motor reach, tool use, and attentional state — in REE terms, z_beta
modulates the effective PPS boundary, consistent with ARC-016 (z_beta-gated commitment
precision) and MECH-093 (z_beta modulates E3 heartbeat rate).

Neural basis: Rizzolatti, Fogassi & Gallese (1997) — premotor F4 and parietal 7b/VIP
encode near-body space in body-part-centered egocentric coordinates.

Literature: `evidence/literature/targeted_review_connectome_mech_097/`

### 4. Temporal Asymmetry in Update Dynamics (design constraint — no separate claim)

z_self and z_world operate on structurally different consolidation timescales:

- z_self: cerebellar forward model updates ~100ms (online, continuous)
- z_world: hippocampal SWR-equivalent consolidation during quiescent cycles (MECH-092)

SD-005 treats them as symmetric latent splits. V3 implementation must not apply
symmetric update dynamics: z_self requires fast online updating (motor-sensory loop
frequency); z_world requires replay-based consolidation (MECH-092 quiescent cycles).
Applying the same update schedule to both would either over-update z_world (instability)
or under-update z_self (motor error accumulation).

No separate claim registered — too underspecified for a testable mechanism candidate
at this stage. Revisit when V3 encoder architecture is designed.
