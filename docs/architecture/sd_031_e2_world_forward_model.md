---
nav_exclude: true
---

# SD-031: E2_world Causal-Footprint Forward Model Comparator

**Claim ID:** SD-031
**Subject:** self_attribution.comparator_z_world
**Status:** CANDIDATE (V4-scoped)
**Registered:** 2026-04-18
**Depends on:** SD-005 (self/world latent split), SD-010 (harm-stream separation), MECH-256 (general comparator mechanism)
**Instantiates:** MECH-256 on the z_world stream
**Parent roadmap:** [self_attribution_per_stream.md](self_attribution_per_stream.md)

## Problem

V3 tracks world-state changes caused by the agent through ResidueField: each
action leaves a trace in z_world space, and downstream valuation reads the
terrain of accumulated residues. The residue mechanism answers "where did I
go" and "what did I affect," but it does not, by itself, distinguish
agent-caused world changes from externally-caused world changes happening in
the same region of state space.

That distinction is the foundation of moral attribution for non-harm
consequences. If I push a block and it knocks over a vase, the vase-falling
belongs to me. If I walk past a shelf and someone else pushes a different
block that topples the vase, the vase-falling does not belong to me -- even
though I am physically present in the same z_world neighbourhood. V3 has no
comparator-structured signal for this; z_world attribution is implicit in
where the agent is, not in what the agent did.

SD-031 exists to make z_world attribution an explicit comparator signal:

```
predicted_z_world = E2_world(z_world_{t-1}, a_actual)
residual_z_world  = z_world_observed - predicted_z_world
causal_sig_world  = f(residual_z_world, context)
```

A self-caused world change is one the agent's own action predicted. An
externally-caused world change is one the agent's action did not predict.
Residual magnitude is the agency signal on this stream.

V3 does not run SD-031 because V3 does not have a dedicated E2_world forward
model. E2FastPredictor operates on z_gamma (combined self-world); with SD-005
separating z_self and z_world, the natural split is to have dedicated forward
models per stream. E2_world exists in V3 only implicitly through
E2FastPredictor.world_forward (the world-component of the combined model), and
the V3 SD-003 validation on z_world (EXQ-030b) used a two-pass counterfactual
against that implicit substrate. SD-031 re-specifies the mechanism as a
single-pass comparator on a dedicated E2_world after the SD-005 expansion is
complete.

## Solution

E2WorldForward: a dedicated learnable forward model
f(z_world_t, a_t) -> z_world_{t+1}. Same architectural pattern as ARC-033 and
SD-030: residual-delta, stop-gradient on z_world inputs during training,
phased training.

Single-pass comparator at inference:

```
predicted_z_world = E2WorldForward(z_world_{t-1}, a_actual)
residual_z_world  = z_world_observed - predicted_z_world
causal_sig_world  = f(residual_z_world, context)
```

Continuity with SD-003: SD-003 on z_world was validated pre-SD-010 using a
two-pass counterfactual (EXQ-030b PASS, world_forward_r2=0.947). SD-031
supersedes that design by asserting the single-pass comparator is sufficient
on z_world, mirroring MECH-256. The EXQ-030b substrate (E2.world_forward)
would be adequate for SD-031 evaluation; the retirement of SD-003 on z_world
in favour of SD-031 is a bookkeeping change, not a mechanism change, once the
comparator is read single-pass.

## Architecture Context

E2WorldForward is the third of three parallel forward models in V4:

- E2HarmSForward (ARC-033) -- on z_harm_s, V3-active
- E2SelfForward (SD-030) -- on z_self, V4
- E2WorldForward (SD-031) -- on z_world, V4

MECH-257 applies: each forward model is read in two modes. The evaluator
mode of E2WorldForward is what V3 already does when E3 scores candidate
trajectories (rollout through E2 on z_world-like latents); SD-031 adds the
comparator mode -- running the same forward model retrospectively on the
action actually taken, computing the residual against the observed world
state.

Training protocol (phased):
- P0: z_world encoder warmup (event-contrastive supervision per SD-009,
  resource proximity per SD-018, already V3-established)
- P1: E2WorldForward trains on frozen z_world (stop-gradient on z_world_t
  inputs). Metric: world_forward_r2 > 0.9 (baseline from EXQ-030b already
  0.947, so this threshold is achievable).
- P2: Attribution evaluation via scripted perturbation trials (see
  Validation Experiment below).

## What This Enables

**Moral attribution for non-harm consequences.** The agent can distinguish
world changes it caused from world changes that happened in its vicinity.
This is the substrate for ethical attribution of blameworthy actions that do
not produce direct harm -- property damage, theft, deception, promises broken.
In V4's social extension, it is the substrate for attributing positive
agent-caused world changes (building, giving, repairing).

**Explicit residue-attribution signal.** ResidueField currently integrates
everything the agent's z_world trajectory touches. SD-031 provides the signal
to weight residue writes by attribution strength -- residues from predicted
self-caused transitions contribute fully; residues from externally-caused
transitions happening during the agent's presence are downweighted. This
tightens the signal that downstream planning reads.

**Causal chain tracking.** The residual on z_world at time t conditions on
the agent's action at time t-1. Chaining comparators across time steps allows
the agent to attribute distal consequences to its own actions ("I pushed the
block at t, the block knocked the vase at t+1, the vase-falling at t+1 belongs
to me"). This is the mechanism for moral responsibility extending beyond
immediate action consequences.

**Decouples world attribution from harm attribution.** SD-003's original
design used z_world-to-z_harm projection (HarmBridge) to query counterfactual
harm from world counterfactuals. That design was architecturally infeasible
(EXQ-093/094, bridge_r2=0, z_world perp z_harm by SD-010). The post-SD-010
topology is that harm attribution (SD-029) and world attribution (SD-031)
are independent signals on independent streams. SD-031 makes that independence
explicit rather than implicit.

## Module Location (V4 target)

```python
# Planned location (mirrors ARC-033 pattern):
# from ree_core.predictors.e2_world import E2WorldForward, E2WorldConfig
#
# Enabled via LatentStackConfig.use_e2_world_forward (False default).
# Config dataclass E2WorldConfig standalone in e2_world.py.
#
# V3 temporary path: E2FastPredictor.world_forward is the implicit world
# forward model. V4 migration: lift world_forward out of E2FastPredictor
# into a dedicated E2WorldForward module with its own training loss and
# stop-gradient discipline.
```

V3 has the substrate (E2.world_forward worked in EXQ-030b) but not the module
structure. V4 milestone: factor E2.world_forward into a dedicated
`ree_core/predictors/e2_world.py` module and add the stop-gradient training
discipline that the SD-003 counterfactual did not require (because it was
read as a function, not trained in isolation).

## ML Engineering Notes

Inherited from ARC-033 pattern:

- **Stop-gradient** on z_world inputs to forward model during P1 (prevent
  encoder drift). Less critical for z_world than for z_harm_s because z_world
  already has strong supervisory signals (event CE, resource proximity) that
  anchor the encoder; but still good discipline.
- **Residual-delta** architecture. z_world has moderate autocorrelation (world
  state changes at the cadence of agent action, so less autocorrelated than
  z_self but more than z_harm_s in high-threat states). Delta prediction is
  the robust default.
- **Learning rate.** E2.world_forward in V3 uses 3e-4 (E2 LR); the dedicated
  E2WorldForward in V4 may use the same or slightly smaller. Baseline from
  EXQ-030b shows 3e-4 saturates world_forward_r2 near 0.95.
- **Interventional training (SD-013 analogue).** Higher priority for z_world
  than for z_self because world state has strong ambient correlations
  (landmarks, resources, hazards persist across steps). Margin loss forcing
  ||E2_world(z_world, a_i) - E2_world(z_world, a_j)|| >= margin for a_i != a_j
  is the standard extension.
- **MECH-094:** not applicable (waking forward model, not replay content).

New to SD-031 relative to ARC-033:

- **Scale.** z_world_dim is 32 in current REEConfig, matching z_harm_s_dim.
  The world stream carries more information than the harm stream (spatial
  structure, landmark gradients SD-023, resource fields). If V4 expands
  z_world_dim, E2WorldForward hidden capacity scales with it.
- **Temporal horizon.** z_harm_s comparator is immediate (proximity-local).
  z_world comparator may need multi-step horizon to attribute distal
  consequences; this is where MECH-257 evaluator-mode rollout converges with
  the comparator-mode single-step residual. Open design question: whether
  multi-step comparator is a chained-single-step residual or a dedicated
  multi-step model.

## Biological Grounding

**Parietal outcome-prediction circuits.** Parietal cortex integrates forward-
model predictions of action consequences with observed outcomes. Desmurget &
Sirigu 2009 (TiCS): parietal stimulation produces conscious intention without
movement; parietal lesions disrupt sense of agency specifically for action
outcomes (as opposed to action initiation).

**Posterior parietal / MD-thalamus / colliculus corollary discharge (Sommer &
Wurtz).** The same pathway grounding SD-030 saccadic attribution extends to
object-locked attribution when the action produces a visual consequence on
external objects. Parietal remapping tracks not just the visual field after
the saccade but object trajectories the agent-initiated action was expected
to produce.

**ACC / insula outcome attribution.** Anterior cingulate encodes the
prediction error for action outcomes; the magnitude of the ACC signal scales
with how unexpected the outcome was given the action (Holroyd & Coles 2002).
This is the biological analogue of the z_world residual: self-initiated
action produces a prediction the outcome matches (small ACC signal);
externally-caused deviation from the prediction produces a large ACC signal.

**Schizophrenia passivity experiences (Frith 2000).** When the comparator
fails for world consequences of action ("my body moved but it was not my
doing" extended to "the world changed but it was not my doing"), the patient
reports alien control of external events. This is the clinical signature of
E2_world comparator failure specifically -- distinct from z_self comparator
failure (passivity of movement) and distinct from auditory hallucinations
(z_self auditory substream comparator failure).

**Sense of agency binding (Haggard 2017).** Temporal binding between voluntary
action and its sensory consequence is an implicit measure of agency
attribution. Binding is strongest when the outcome matches the prediction
(small residual); binding is abolished when the outcome is random or
externally-perturbed (large residual). The binding signature is shared across
modalities -- a single underlying comparator reading mechanism weighted by
stream-specific precision (Haggard's cue-integration model), which is exactly
what MECH-256 + SD-029/030/031 instantiate.

Biological grounding for SD-031 is **moderate** -- stronger than SD-003's
original two-pass counterfactual formulation (no biological evidence for
counterfactual forward rollouts being run symmetrically against actual-action
rollouts), weaker than SD-030 (cerebellar literature is canonical and
cross-species). The parietal outcome-prediction literature is clear; the
specific substrate is less uniform than the cerebellar story for SD-030.

## Validation Experiment (V4)

Proposed design (not queued for V3):

**Phase P0:** z_world encoder already established (SD-009 event-CE, SD-018
resource proximity). No additional warmup needed beyond standard training.

**Phase P1:** E2WorldForward factor-out and training. Migrate
E2FastPredictor.world_forward into dedicated module; train with stop-gradient
discipline. Metric: world_forward_r2 > 0.9 (EXQ-030b baseline 0.947 confirms
achievable). Identity-collapse check: r2 on action-shuffled control must
drop substantially.

**Phase P2:** Attribution evaluation. Environment extension required: CausalGridWorldV3
needs a "perturbation" condition where an external event modifies world state
independently of the agent's action (e.g., a block moves without the agent
having pushed it, or a resource appears/disappears exogenously). Metric:
world_causal_gap = mean(||residual||_perturbed) - mean(||residual||_self) > 0.1.

**Interventional extension (SD-013 analogue):** margin loss forcing
E2_world outputs to diverge across actions from the same state. Prediction:
ambient correlations (same landmark, same hazard configuration across many
trials) compress the signal; interventional training restores identifiability.

**Causal chain test (V4+):** scripted trials where the agent's action at t-2
produces a consequence at t that requires chaining two forward predictions to
attribute. Residue-field integration with SD-031 attribution weights should
track multi-step credit better than a residue field without attribution
weights.

**Ablation:** with SD-031 disabled, the ResidueField integrates all z_world
transitions with equal weight. The agent cannot discount residues from
externally-caused events. V4 task: moral-attribution test where the agent
must avoid blame for events caused by other agents operating in the same
environment. Agents with working SD-031 should show selective avoidance;
ablated agents should not.

## Related Claims

- MECH-256: general comparator mechanism (parent)
- MECH-257: dual-function gated readout (comparator + evaluator on same substrate)
- SD-005: self/world latent split (prerequisite -- z_world must be first-class)
- SD-010: harm-stream separation (prerequisite -- ensures z_world is distinct
  from z_harm, so SD-031 comparator is unambiguous about which stream it reads)
- SD-029: z_harm_s comparator (V3-active sibling)
- SD-030: z_self comparator (V4-deferred sibling)
- SD-003: z_world counterfactual (superseded by SD-031 single-pass reading)
- ARC-033: E2_harm_s forward model (reference implementation template)
- SD-013: interventional training extension
- ARC-017 / MECH-096 / MECH-103: ResidueField downstream consumer
- MECH-094: replay-content gate (not applicable to waking comparator)
