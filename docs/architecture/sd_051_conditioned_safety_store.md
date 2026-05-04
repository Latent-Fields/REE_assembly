# SD-051: safety_prediction.cue_specific_conditioned_inhibition_substrate

**Claim ID:** SD-051
**Subject:** safety_prediction.cue_specific_conditioned_inhibition_substrate
**Status:** IMPLEMENTED
**Registered:** 2026-05-04
**Depends on:** SD-011 (z_harm_a affective stream), SD-050 / MECH-302 (relief-completion teaching signal), MECH-094 (categorical tag write gate), MECH-057a (commitment-release pipeline)
**Blocks:** MECH-304 (cue-specific conditioned safety prediction substrate)

## Problem

REE agents learn to avoid harm but have no mechanism for learning that specific features of
the world predict the *absence* of harm — the conditioned inhibition substrate. Without this,
avoidance commitments cannot be released by safety cues; only harm cessation (MECH-302) or
goal attainment (MECH-057a) close avoidance loops.

This is the architectural gap measured by the conditioned-inhibition discriminative-pair
protocol (Andreatta 2012; Ng & Sangha 2023): a learned safety cue should suppress ongoing
avoidance commitment even when a threat cue is concurrently present. Without SD-051, an
REE agent cannot produce this behavioural signature.

## Solution

A non-trainable `ConditionedSafetyStore` module that maintains a prototype representation
of the world state at MECH-302 relief-completion event times (the EMA of z_world across
all waking ticks when relief fires). At each step, it computes the cosine similarity of the
current z_world to the stored prototype and returns a `safety_prediction` scalar.

**Encoding (dorsal striatum / dlPFC analog):** EMA prototype update on MECH-302 event ticks.
  `z_safe_prototype = (1 - alpha) * z_safe_prototype + alpha * normalize(z_world)`
  The prototype is the slowly-accumulated average of the z_world states that co-occurred
  with relief — the V3 analog of the dorsal striatal / dlPFC associative encoding identified
  in Laing et al. 2022 (conditioned inhibitor encoding, distinct from standard safety signal).

**Per-step decay:** `z_safe_prototype *= (1 - decay_rate)` (forgetting without reinforcement).
  Biologically motivated: conditioned inhibitors extinguish without continued pairing.

**Expression pathway query (IL-to-CeA analog):** cosine similarity between current z_world
  and z_safe_prototype is passed through a sigmoid with a gain parameter.
  `safety_prediction = sigmoid(cosine_sim * gain)` when `||z_safe_prototype|| > min_norm`.
  Returns 0.0 when the store is empty (no events yet).

**MECH-094 compliance:** `update()` returns 0.0 and does NOT advance the prototype when
  `sim_mode=True`. Simulation and replay content cannot contribute to safety-cue learning
  or trigger safety-signal gates.

## Data Flow

```
CausalGridWorldV2.step() -> obs_dict
-> agent.sense() -> LatentStack.encode() -> latent.z_world [1, world_dim]
-> ConditionedSafetyStore.update(z_world[0], relief_event=_relief_completion_event, sim_mode=hypothesis_tag)
-> agent._conditioned_safety_signal: float (ephemeral, not in LatentState)

agent.select_action():
    # IL->CeA expression: lower avoidance commitment threshold when safety cue recognized
    if conditioned_safety_store and beta_gate.is_elevated:
        if _conditioned_safety_signal > safety_store_threshold:
            beta_gate.release(); _committed_step_idx = 0
            if valence_liking_enabled and not hypothesis_tag:
                residue_field.update_valence(z_world, VALENCE_LIKING,
                                             safety_store_commitment_weight, hypothesis_tag=False)
    _conditioned_safety_signal = 0.0  (cleared each tick)
```

## Config Parameters

All gated by `use_conditioned_safety_store=False` (default, no-op):

| Parameter | Default | Purpose |
|-----------|---------|---------|
| `use_conditioned_safety_store` | `False` | master switch |
| `safety_store_ema_alpha` | `0.1` | prototype update rate per MECH-302 event |
| `safety_store_decay_rate` | `0.001` | per-step prototype decay (forgetting) |
| `safety_store_min_norm` | `0.1` | prototype L2 norm below which query returns 0 |
| `safety_store_threshold` | `0.5` | cosine similarity threshold for commitment release |
| `safety_store_commitment_weight` | `1.0` | VALENCE_LIKING write magnitude on release |

All parameters wired through `REEConfig.from_dims()`.

## Architecture Context

SD-051 is the encoding + expression substrate for MECH-304 (cue-specific conditioned
inhibition). It parallels but does not duplicate MECH-303 (contextual passive safety
representation, vmPFC/hippocampal substrate):

- **MECH-303**: diffuse, context-level, no discrete teaching event. Accumulated non-harm
  in a context lowers background vigilance.
- **MECH-304 / SD-051**: cue-specific, event-driven, MECH-302 teaching signal required.
  A discrete safety cue that co-occurred with relief becomes a targeted commitment-release
  trigger.

Laing et al. 2022 (7T fMRI, n=49) provides the load-bearing dissociation: conditioned
inhibitors recruit dorsal striatum + dlPFC during encoding (SD-051 substrate); standard
safety signals recruit vmPFC + hippocampus (MECH-303 substrate). The two pathways are
anatomically distinct.

The IL-to-CeA expression pathway (Ng & Sangha 2023 Neuropsychopharmacol, Ng & Sangha 2023
Cereb Cortex) is the output gate: when the conditioned inhibitor is recognised, IL output
suppresses CeA fear/avoidance output. In REE, this is modelled as safety_prediction →
beta_gate release threshold.

## What This SD Enables

- MECH-304 substrate implementation (v3_pending cleared after V3-EXQ-519 validation)
- Classical conditioned inhibition behavioural signature: learned safety cue suppresses
  avoidance commitment even in presence of concurrent threat cue
- PTSD / chronic-avoidance failure mode prediction: if SD-051 is degraded but MECH-303
  is intact, the agent feels safe in familiar environments but cannot use specific safety
  signals to calm down on demand -- a substrate-level PTSD phenotype distinct from
  MECH-303 failure

## V4-Deferred Extensions

The V3 substrate is minimal by design. Two extensions are deferred to V4:

1. **Approach attractor toward safety-signaling cues**: V3 handles only commitment-release
   gating (output 1 of the MECH-304 spec). Output 2 — the safety cue becoming an approach
   attractor in its own right — requires V4 multi-step trajectory planning infrastructure
   (HippocampalModule completing V3 prerequisite gate, MECH-163). Without multi-step
   planning, a safety-cue approach attractor reduces to a step-wise proximity signal that
   cannot compete with harm avoidance commitments over trajectories. Registered in
   `v3_v4_transition_boundary.md` under V4 extensions.

2. **Contrastive cue-specific learning**: The V3 EMA prototype conflates any z_world
   co-occurring with MECH-302 events, including contextual features that happen to be
   stable at relief time. A contrastive store (learning what distinguishes safety events
   from non-safety events via contrastive pairs) would produce sharper cue specificity.
   This requires a trainable encoder head and the phased-training infrastructure it entails.
   Substrate ceiling: V3's non-parametric prototype may generalise the safety prediction
   too broadly in environments with stable non-safety features that happen to co-occur with
   relief. Registered in `v3_v4_transition_boundary.md`.

## Module and Files

- `ree_core/safety/__init__.py` -- new package
- `ree_core/safety/conditioned_safety_store.py` -- `ConditionedSafetyStore` class
  (non-trainable; no `nn.Module` inheritance; pure arithmetic)
- `ree_core/utils/config.py` -- 6 config params in `REEConfig`, wired through `from_dims()`
- `ree_core/agent.py` -- import, `__init__` instantiation, `sense()` tick,
  `select_action()` fire handler, `reset()` clear

## Backward Compatibility

`use_conditioned_safety_store=False` by default. With this default:
- `agent.conditioned_safety_store is None`
- `sense()` skips the store update entirely
- `select_action()` skips the safety-gate block entirely
- No change to any existing experiment output

## Biological Basis

Laing et al. 2022 (J Neurosci, 7T fMRI): conditioned inhibitors (safety cues learned via
relief pairing) encode in dorsal striatum + dlPFC, dissociating from standard safety signals
(vmPFC/hippocampus). Load-bearing dissociation supporting the two-system (MECH-303/304)
architecture.

Ng & Sangha 2023 (Neuropsychopharmacology): IL->CeA pathway (chemogenetic dissection)
is required for conditioned safety expression; IL->BLA is not required. Positions IL as the
expression gate, not the encoding site.

Ng & Sangha 2023 (Cereb Cortex): IL single-unit recordings show cells that encode
conditioned inhibitors specifically -- the expression substrate has dedicated
representational support.

## Related Claims

MECH-304 (cue-specific conditioned safety prediction -- the claim this SD implements),
MECH-303 (sister contextual pathway), MECH-302 / SD-050 (teaching signal source),
SD-011 (z_harm_a affective stream), MECH-057a (commitment-release pipeline reused),
MECH-094 (hypothesis-tag simulation gate)

## Validation Experiment

V3-EXQ-519 (4-arm substrate-readiness diagnostic, queued 2026-05-04).
See `experiments/v3_exq_519_sd051_conditioned_safety_store_readiness.py`.
