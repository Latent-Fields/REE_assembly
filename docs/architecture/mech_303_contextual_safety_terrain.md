---
title: "MECH-303: Contextual Passive Safety Terrain"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 8
status: active
status_asof: 2026-08-23
status_claim: MECH-303
---

# MECH-303: Contextual Passive Safety Terrain

**Claim ID:** MECH-303
**Subject:** safety_prediction.contextual_passive_substrate
**Status:** IMPLEMENTED 2026-05-04
**Registered:** 2026-05-03
**Revised:** 2026-05-04 (split from original MECH-303; cue-specific pathway moved to MECH-304 / SD-051)
**Depends on:** SD-011, SD-012, ARC-007, MECH-304 (sister claim)
**Blocks:** context-conditioned-vs-cue-conditioned safety extinction discriminative-pair experiment

## Problem

The agent has no substrate for learning that an environment is generally safe. Without a
contextual safety representation, avoidance commitments persist in familiar harmless
environments, producing chronic vigilance that cannot be extinguished by passive exposure
alone. This is distinct from MECH-304 (cue-specific conditioned safety), which requires
explicit discrete relief events to update.

Biological grounding: Laing et al. 2022 (J Neurosci, 7T fMRI) dissociates two safety-
learning systems -- a standard safety signal pathway (contextual, passive accumulation,
vmPFC + hippocampus) from a conditioned inhibitor pathway (cue-specific, event-driven,
dorsal striatum + dlPFC). MECH-303 covers the vmPFC/hippocampal pathway. Kreutzmann
2020 (Psychopharmacology) shows IL is required for safety-signal expression. Meyer 2019
(PNAS) localises the contextual store to a vHipp-to-PL circuit, cross-species.

## Solution

A parallel RBF field (`safety_terrain_rbf_field`) in ResidueField accumulates small
per-step increments at the current z_world location whenever z_harm_a.norm() is below
the quiescent threshold. Over repeated exposure to a harmless context, the safety terrain
builds up a spatially-localised attractor at that context's z_world signature.

In select_action(), the safety terrain is evaluated at the current z_world. When the
scalar prediction exceeds `contextual_safety_release_threshold` AND the beta gate is
elevated, the gate is released -- lowering background avoidance commitment in familiar
safe contexts.

### Update rule (harm-absence accumulation)

```
sense() each step:
    harm_norm = z_harm_a.norm()   (SD-011 affective stream)
    if harm_norm < contextual_safety_harm_threshold   (harm is absent)
    AND hypothesis_tag == False                        (waking only, MECH-094)
        residue_field.accumulate_safety(z_world, contextual_safety_accum_weight)
```

The increment per step is small (default 0.01) so safety builds slowly, consistent
with the slow/diffuse update rule of contextual safety learning (contrasted with the
fast event-driven MECH-304).

### Background vigilance gate

```
select_action() when beta_gate.is_elevated:
    safety_pred = residue_field.evaluate_safety(z_world)  [batch scalar]
    if float(safety_pred.mean()) >= contextual_safety_release_threshold:
        beta_gate.release()
        _committed_step_idx = 0
        _committed_anchor_keys = None
```

## Architecture context

MECH-303 is the contextual/passive complement to MECH-304 (cue-specific conditioned
inhibition, SD-051). The two systems dissociate behaviourally:

- MECH-303: builds up over repeated safe context exposure (no discrete event needed);
  outputs a tonic reduction in background vigilance in that context.
- MECH-304: updates on discrete MECH-302 relief-completion events; outputs a phasic
  commitment release when the stored safety cue is recognised.

The safety terrain follows the same RBF architecture as `benefit_terrain` (ARC-030)
and the residue field itself, but uses a separate `safety_terrain_rbf_field` with its
own accumulators -- no sharing with VALENCE_LIKING or benefit_terrain.

## Implementation surface

**New module file:** None -- extension to `ree_core/residue/field.py`.

**ResidueField changes:**
- `safety_terrain_enabled` attribute from `ResidueConfig.safety_terrain_enabled`
- `safety_terrain_rbf_field: RBFLayer` instantiated when enabled
- `total_safety: Tensor` buffer (total accumulated safety)
- `num_safety_steps: Tensor` buffer (count of harm-absent steps accumulated)
- `accumulate_safety(z_world, magnitude, hypothesis_tag)` -- write path
- `evaluate_safety(z_world)` -- read path, returns [batch] scalar

**Config params:**
| Param | Type | Default | Class |
|-------|------|---------|-------|
| `safety_terrain_enabled` | bool | False | ResidueConfig |
| `use_contextual_safety_terrain` | bool | False | REEConfig |
| `contextual_safety_accum_weight` | float | 0.01 | REEConfig |
| `contextual_safety_harm_threshold` | float | 0.05 | REEConfig |
| `contextual_safety_release_threshold` | float | 1.0 | REEConfig |

All defaults are no-op. `from_dims(use_contextual_safety_terrain=True)` auto-enables
`residue.safety_terrain_enabled`.

## What this enables

- V3-EXQ-520: 4-arm substrate-readiness diagnostic
  - ARM_0 OFF: bit-identical baseline
  - ARM_1 write-only (release_threshold=999): terrain accumulates, no gate fires
  - ARM_2 full MECH-303 (release_threshold=1.0): gate fires in harm-free contexts
  - ARM_3 gate-only (accum_weight=0): terrain empty, no gate -- equals ARM_0

- Future: context-conditioned-vs-cue-conditioned safety extinction discriminative-pair
  experiment (MECH-303 ablated: extinction slower for contextual safety;
  MECH-304 ablated: extinction slower for cue-specific safety)

## Anatomical enrichment (2026-06-05, Silva et al. 2021)

The `targeted_review_affect_stream_relief_safety_soothing` lit-pull (2026-06-05)
surfaced **Silva et al. 2021** (*Nat Neurosci* 24(7):964-974, DOI
[10.1038/s41593-021-00856-y](https://doi.org/10.1038/s41593-021-00856-y)),
which causally establishes a **midline-thalamic relay -- nucleus reuniens (NRe)
-> basolateral amygdala (BLA)** -- that registers and actively *transmits* safety
signals onto the fear circuit (NRe->BLA activity rises before freezing cessation;
pathway-specific inhibition impairs and activation facilitates extinction).

This is **enrichment, not contradiction**. Two points apply to MECH-303:

1. **Cluster-level anatomy.** The safety cluster's expression machinery is
   prefrontal-hippocampal-**thalamic**, not prefrontal-hippocampal alone. Silva's
   causal evidence bears most directly on the sister claim **MECH-304** (the
   active, cue-specific safety signal that acts *on* the fear circuit), so MECH-303
   carries only the lighter cluster-level note that the contextual safety
   representation's downstream expression shares this thalamo-amygdalar relay. The
   MECH-303 vHipp-to-PL contextual store + IL expression anatomy stands unchanged.

2. **Remote-vs-recent (time-since-encoding) dependence.** Silva's NRe->BLA relay is
   recruited for the extinction of **remote** (systems-consolidated, ~30-day)
   aversive memories and not recent (~1-day) ones. This indexes how *consolidated*
   the suppressed fear is -- a new axis orthogonal to the context-vs-cue axis that
   separates MECH-303 from MECH-304. It is tracked on **MECH-304** as a **candidate
   third safety sub-mechanism** (consolidation-age-conditional safety expression),
   deliberately not minted as a claim yet (single rodent anchor, off the V3 critical
   path, no consolidation-interface design). See MECH-304 `notes`.

Neither the thalamic relay nor the remote/recent axis is implemented in the SD-052
substrate -- this enrichment is documentation-only.

## Related claims

- MECH-303 (this claim): contextual_passive_substrate
- MECH-304 / SD-051: cue_specific_conditioned_inhibition_substrate (sister, already implemented)
- MECH-302 / SD-050: relief_completion_event (teaching signal for MECH-304; harm source for MECH-303)
- SD-011: dual nociceptive streams (z_harm_a is the harm stream MECH-303 monitors)
- SD-012: homeostatic drive (anchors "safety" as drive-baseline-not-rising)
- ARC-007: hippocampal path memory (contextual encoding substrate)
- ARC-030 / MECH-117: benefit terrain (parallel architecture; separate RBF field)
- MECH-094: hypothesis tag (blocks safety accumulation during simulation/replay)
