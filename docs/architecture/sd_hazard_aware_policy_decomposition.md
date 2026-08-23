---
title: "SD-hazard-aware-policy-decomposition: policy.harm_aware_decomposition_selection"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 25
status: implemented/v3_pending
status_asof: 2026-08-01
status_claim: MECH-321
---

# SD-hazard-aware-policy-decomposition: policy.harm_aware_decomposition_selection

**Claim ID:** SD-hazard-aware-policy-decomposition (substrate) + MECH-321 (mechanism)
**Subject:** `policy.decomposition_via_event_segmenter.harm_aware_selection`
**Status:** IMPLEMENTED 2026-08-01
**Registered:** 2026-08-01
**Depends on:** ARC-070 / MECH-321 (policy_decomposition_via_event_segmenter substrate), SD-014
(residue-field valence channels, specifically `VALENCE_HARM_DISCRIMINATIVE`), SD-011 (`z_harm_a`
affective harm accumulator)
**Blocks:** none directly; unblocks further MECH-321 behavioural-effect validation
(`unblocks_claims: [MECH-321]`)

---

## Problem

`V3-EXQ-844` (`failure_autopsy_V3-EXQ-844_2026-08-01`) tested MECH-321's mid-execution
policy-decomposition abort mechanism on a task-outcome criterion. Readiness was green on both
arms; C2 (mechanistic corroboration) PASSED -- aborting a stale macro measurably lowers
forward-prediction-error post-abort, confirming the abort mechanism engages exactly as designed
informationally. C1 (task-outcome improvement, load-bearing) FAILED: -0.003262, wrong direction,
using a paired post-divergence-window statistic built specifically to avoid the whole-run-mean
dilution problem the prior V3-EXQ-839 diagnostic had flagged.

Code-verified root cause: `_apply_policy_decomposition`
(`ree-v3/ree_core/hippocampal/module.py:896-983`) and `PolicyDecomposition.evaluate()` /
`decompose_sequence()` (`ree-v3/ree_core/policy/policy_decomposition.py:471-747`) read only
`z_self`/`z_world`/`z_goal` -- no harm-valence signal (`z_harm_a`) reaches this step -- **and**
the step performs no ranked selection among candidate re-tilings at all: a binary decompose/keep
test per candidate, with every surviving leaf tile additively recombined into the pool. MECH-288
(this claim's own trigger) is pure predictive-surprise, unrelated to hazard proximity; REE's
actual fear/threat pathway (BLA/CeA, MECH-357/SD-058) biases action selection elsewhere (E3
scoring, the separate MECH-091 urgency-interrupt abort) but was not connected here. So a
withheld chunk that decomposes near a hazard offers ALL of its re-tilings -- high-harm and
low-harm alike -- to E3 with no differentiation, and the abort mechanism (which fires correctly)
has nothing downstream biasing the replan toward a lower-harm continuation.

A targeted lit-pull was commissioned before fixing the exact functional form, per
biology-before-formal-definitions
(`evidence/literature/targeted_review_threat_modulated_defensive_path_selection/SYNTHESIS.md`,
9 entries: Fanselow's Predatory Imminence Continuum x4, Mobbs 2007 *Science* + Mobbs 2020 *TICS*,
Evans et al. 2018 *Nature*, Cooper 2016, Blanchard & Blanchard 1989).

## Lit-pull verdict (Form B, two-stage regime-sensitive)

The literature does not support a pure single-threshold design or a pure smooth-linear-weighting
design in isolation. Five entries converge on a dual-coding structure: (a) a continuously graded
harm signal, (b) feeding a threshold-crossing categorical decision about HOW to select, which (c)
also continuously scales the magnitude of whatever is selected, and (d) is more reliably
triggered by a CHANGE in the harm signal than by absolute level alone (deferred here -- see
"What this SD does NOT do" below).

Recommended default (**Form B**), applied per withheld chunk to its own candidate re-tilings:

1. **Graded bias term (always active).** `score_total(tile) = score_structural(tile) -
   w(h) * harm_penalty(tile)`, where `h` is a function of `z_harm_a` and `w(h)` is monotonically
   increasing, gain-scaled and clamped (Cooper 2016's sigmoidal-not-linear finding argues against
   an unbounded linear weight; the clamp is what makes this saturating rather than literally
   linear).
2. **Threshold-gated categorical override**, active only above a high-imminence boundary: restrict
   the candidate set to the single lowest-harm-penalty tile, overriding ordinary structural-cost
   scoring (Mobbs 2007's categorical vmPFC->PAG shift; Evans 2018's synaptic-threshold escape-choice
   mechanism).
3. **Preserve the existing harm-blind additive recombination as the below-threshold default**
   (Evans 2018's freeze-as-fallback finding) -- this is an addition, not a rewrite.

Escapability (Cooper 2016) and predictability/certainty (Fanselow 2022 BST; Blanchard & Blanchard
1989) are real, lit-pull-confirmed secondary gaps -- deferred, not blocking this first buildable
version (see "What this SD does NOT do").

## Solution

### Data flow

```
Withheld chunk candidate (ARC-070 R1 trigger fires)
  -> _recursive_leaf_tiles()  [existing, unchanged -- produces N candidate re-tilings]
  -> for each leaf: _rollout_tile() [existing, unchanged -- E2 rollout -> Trajectory.world_states]
  -> NEW: _decomposition_harm_penalty(leaf_traj)
         = mean(residue_field.evaluate_valence(leaf_traj.world_states)[..., VALENCE_HARM_DISCRIMINATIVE])
  -> NEW: leaf_traj.metadata["decomposition_harm_penalty"] = harm_penalty   (provenance)
  -> NEW: leaf_traj.metadata["decomposition_harm_bias"]
         = PolicyDecomposition.harm_bias(harm_penalty, z_harm_a_norm)      (Stage 1, graded)
  -> NEW: PolicyDecomposition.select_harm_aware_leaves(leaves_with_penalty, z_harm_a_norm)
         -- Stage 2 (categorical): below harm_override_w_threshold, returns all leaves
            unchanged; at/above it, returns only the lowest-penalty leaf.
  -> decomposed_out (spliced into the CEM candidate pool, as before)
  ...
  -> REEAgent.select_action(): NEW score_bias-chain block gathers
     candidate.metadata["decomposition_harm_bias"] into the SAME additive score_bias
     tensor InstrumentalAvoidanceGate / EscapeAffordanceBridge / dACC compose into.
     E3 supplies all other value; PolicyDecomposition never scores a trajectory itself.
```

`harm_penalty(tile)` is sourced from the residue field's `VALENCE_HARM_DISCRIMINATIVE` channel
(SD-014) read at the candidate's OWN predicted `world_states` -- the same per-location valence
readout `HippocampalModule.build_goal_payload` already uses for `VALENCE_WANTING` (SD-039),
applied here to each decomposition candidate's own rollout instead of the agent's current
position, so distinct re-tilings of the same withheld chunk carry independently-estimated hazard
along each of their own predicted paths. `z_harm_a` (SD-011) is threaded through
`propose_trajectories(..., z_harm_a=latent_state.z_harm_a)` -> `_apply_policy_decomposition`,
mirroring exactly how `InstrumentalAvoidanceGate.compute_action_bias` /
`EscapeAffordanceBridge.compute_approach_bias` already read `z_harm_a_norm` at the
`REEAgent.select_action` composition site.

`w(h)` is `PolicyDecomposition.harm_threat_scale(z_harm_a_norm)`: a linear ramp from 0 at
`harm_threat_floor` to 1 at `harm_threat_ref`, reused verbatim (not re-derived) from
`InstrumentalAvoidanceGate.threat_scale` / `EscapeAffordanceBridge.threat_scale` -- the same
`z_harm_a`-norm-to-`[0,1]` convention already shared across this codebase's PFC threat-response
modules (biology-before-formal-definitions: an engineering primitive, not a fresh claim).

### Why the graded term is a score_bias contribution, not a value head

ARC-007 strict value-flatness: `HippocampalModule._score_trajectory` and the ARC-071 chunk
candidates it injects are explicitly "value-flat -- value_tag rides in metadata as provenance
only, and E3 supplies value at selection time." `PolicyDecomposition` never computes a
trajectory's value; Stage 1 only contributes one more ADDITIVE term to the SAME `score_bias`
chain every other threat-response module in this codebase already composes into
(`InstrumentalAvoidanceGate`, `EscapeAffordanceBridge`, `TrainableEscapeAffordanceLearner`,
dACC). E3 remains the sole value-supplying authority.

### Why the categorical override is pool admission, not an oversized bias

Every existing score_bias source in this codebase is clamped (`bias_scale`) specifically so no
single channel can dominate the additive chain ("Clamped to bias_scale so the gate cannot
dominate the score_bias chain" -- `InstrumentalAvoidanceGate` module docstring). A literal
oversized override bias would violate that discipline. Instead, Stage 2 exercises the SAME
pool-admission authority `_apply_policy_decomposition` already has (it already excludes a
depth-capped or irreducible candidate rather than offering it blind): at/above threshold, it
simply removes the competing re-tilings for THIS withheld chunk from the candidate pool, leaving
only the lowest-harm one. It does not force E3 to select that tile -- other trajectory sources
(flat-grain CEM candidates, other untriggered chunks) remain independently available -- but it
does remove the alternative high-harm re-tilings of this one chunk from consideration, which is
exactly MECH-321's pre-existing scope of authority (which candidates to offer), extended by a
ranking criterion rather than a bare binary test.

### Config surface

All new knobs live on `PolicyDecompositionConfig` (`ree-v3/ree_core/policy/policy_decomposition.py`)
and mirror onto `REEConfig` with the SAME "no hippocampal sub-config mirror" shape as
`use_policy_decomposition` itself (`PolicyDecomposition` reads its own config object, constructed
once at `REEAgent.__init__` from `REEConfig` via `getattr`):

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `decomposition_use_harm_aware_selection` | bool | `False` | master switch |
| `decomposition_harm_bias_gain` | float | `0.1` | Stage 1 gain (mirrors `InstrumentalAvoidanceGateConfig.action_bias_gain`) |
| `decomposition_harm_bias_scale` | float | `0.1` | Stage 1 clamp (mirrors `bias_scale`) |
| `decomposition_harm_threat_floor` | float | `0.1` | `w(h)` ramp start (mirrors `threat_floor`) |
| `decomposition_harm_threat_ref` | float | `0.5` | `w(h)` ramp end / saturation (mirrors `threat_ref`) |
| `decomposition_harm_override_w_threshold` | float | `0.9` | Stage 2 categorical-override threshold on `w(h)` |

All defaults are no-op: `decomposition_use_harm_aware_selection=False` means
`_apply_policy_decomposition` never computes `harm_penalty`, never touches
`self.residue_field.evaluate_valence` for this purpose, never tags metadata, and
`select_harm_aware_leaves`/`harm_bias` are unconditional early-returns -- bit-identical to
pre-existing MECH-321 behaviour. With the flag on and `z_harm_a` at rest (norm at or below
`harm_threat_floor`), `w(h)=0`, so the graded bias is 0 and every leaf is kept: the below-threshold
behaviour is *also* bit-identical to pre-existing behaviour at rest.

### Backward compatibility

Confirmed by the full pre-existing `test_arc070_policy_decomposition.py` contract suite (32
tests) passing unmodified, plus a new `test_c10`-style pin (metadata carries no
`decomposition_harm_*` keys when the flag is off). Existing experiment scripts run unchanged with
default config.

### Phased training

Not applicable -- `PolicyDecomposition` (including the new methods) is pure arithmetic, no
learned parameters, mirroring `ChunkAccumulator`/`ChunkLibrary`/`InstrumentalAvoidanceGate`. No
phased-training protocol is needed.

### MECH-094

Not applicable in a new way -- `_apply_policy_decomposition` already fires under
`hypothesis_tag=True` during rollout deliberation as its primary phase (this is unchanged by this
SD; see `policy_decomposition.py`'s "asymmetry with ARC-071" module docstring). The new harm-aware
selection reads `z_harm_a` and the residue field, both pure reads with no residue-write side
effect, so it inherits MECH-321's existing write-refusal-free posture unchanged.

### What this SD does NOT do (explicitly deferred, per the lit-pull)

- **Escapability** (Cooper 2016: distance-to-refuge / relative speed / path angle) -- a candidate
  input structurally separate from `z_harm_a`, requiring a new signal (e.g. a tile's own predicted
  reachability of a low-harm completion). Not built here.
- **Predictability/certainty** of the harm-predicting cue (Fanselow 2022 BST; Blanchard &
  Blanchard 1989) -- a candidate companion signal that would govern whether the override should
  widen or narrow selection under ambiguous vs. confirmed threat. Not built here.
- **Rate-of-change triggering** (Fanselow 2019: mode transitions are more reliably triggered by a
  CHANGE in threat state than by absolute level). The current `w(h)` ramp is level-based, matching
  the pre-existing `threat_scale` convention used across this codebase; a change-detector variant
  is a natural follow-on, not built here.
- **Sustained-threat disengagement failure mode** (Fanselow 2022): a selection step that, once
  triggered, never disengages even after the harm-predicting condition resolves. `w(h)` is
  recomputed fresh every `_apply_policy_decomposition` call from the CURRENT `z_harm_a`, so this
  substrate has no persistent state to get stuck in -- but this should be an explicit
  negative-control acceptance criterion for the eventual validation experiment, not assumed away.

These are real, lit-pull-confirmed gaps, flagged explicitly per the lit-pull's own instruction so
a later iteration is not mistaken for scope creep on this first one.

## Architecture Context

Extends ARC-070/MECH-321 (policy_decomposition_via_event_segmenter) with a harm-valence-weighted
selection stage over its own candidate re-tilings. Reuses SD-039's per-location valence-read
pattern (`build_goal_payload`'s `VALENCE_WANTING` readout), SD-014's residue-field valence
channels (`VALENCE_HARM_DISCRIMINATIVE`), and the score_bias composition chain established by
SD-058/MECH-357 (`InstrumentalAvoidanceGate`) and SD-059/MECH-358 (`EscapeAffordanceBridge`).
Does NOT extend `AnchorGoalPayload`/`build_goal_payload` (SD-039) directly, despite the originating
`substrate_queue.json` `implementation_hint` suggesting that as one option: `AnchorGoalPayload` is
scoped to hippocampal *anchors* (a single payload per anchor-write tick, shared across all anchors
written that tick), not to policy-decomposition *candidates* (which need an independent per-tile
estimate). Reusing the residue field's `VALENCE_HARM_DISCRIMINATIVE` channel directly, read at each
candidate's own predicted `world_states`, is the more architecturally faithful choice and avoids
threading a hippocampal-anchor-scoped payload through an unrelated proposal-time code path.

## What This SD Enables

Gives MECH-321's mid-execution abort mechanism (which V3-EXQ-844 confirmed engages correctly
informationally) a downstream replanning step that can actually prefer lower-harm continuations,
closing the gap V3-EXQ-844 identified between "abort fires" and "task harm improves." Enables a
future MECH-321 behavioural-effect validation experiment measuring whether harm-aware selection
(this SD) improves the C1 task-outcome statistic V3-EXQ-844 used, ON vs OFF, at matched abort
rates.

## Related Claims

MECH-321 (`unblocks_claims`), ARC-070, SD-014, SD-039, SD-011, MECH-357/SD-058, MECH-358/SD-059.
