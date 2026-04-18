---
nav_exclude: true
---

# SD-030: E2_self Motor-Proprioceptive Forward Model Comparator

**Claim ID:** SD-030
**Subject:** self_attribution.comparator_z_self
**Status:** CANDIDATE (V4-scoped)
**Registered:** 2026-04-18
**Depends on:** SD-005 (self/world latent split), MECH-256 (general comparator mechanism)
**Instantiates:** MECH-256 on the z_self stream
**Parent roadmap:** [self_attribution_per_stream.md](self_attribution_per_stream.md)

## Problem

V3 operates a single forward-model comparator on z_harm_s (SD-029, ARC-033).
That instantiation addresses agency attribution for nociceptive consequences --
"did I cause this pain?" -- which is the highest-priority stream for moral
attribution and the one where biology most clearly demands a working comparator
(descending pain modulation, self-inflicted pain attenuation).

It does not address the two other reafferent streams on which the biological
forward-model architecture is at least as well-established:

- **z_self (motor-proprioceptive)** -- "did I cause the movement I just felt?"
  The cerebellar internal-model loop. Attenuation of self-generated tactile
  input (Blakemore 1998), force-matching underestimation (Shergill 2003),
  saccadic corollary discharge (Sommer & Wurtz).
- **z_world (causal-footprint)** -- "did I cause the world-state change I just
  observed?" Covered by SD-031.

SD-030 exists to make the topology explicit: the comparator mechanism
(MECH-256) applies uniformly across streams; z_self is the stream with the
strongest biological grounding for forward-model machinery. Without SD-030 on
the roadmap, motor-proprioceptive self-attribution would have no substrate
claim, and the cerebellar internal-model loop -- the canonical forward-model
system in neuroscience -- would have no home in the REE architecture.

V3 does not run SD-030 because V3 does not yet have a first-class z_self stream
with its own forward model. E2 currently operates on z_gamma (combined
self-world), with a split into z_self and z_world per SD-005 that has not yet
been instantiated with dedicated stream-specific E2 substrates. SD-030 is
deferred to V4 alongside the z_self substrate materialisation.

## Solution

E2SelfForward: a dedicated learnable forward model
f(z_self_t, a_t) -> z_self_{t+1}. Structural analogue of E2HarmSForward
(ARC-033): residual-delta architecture, stop-gradient on z_self inputs during
forward-model training, small learning rate, phased training (encoder warmup
-> frozen-encoder forward model).

Single-pass comparator at inference:

```
predicted_z_self = E2SelfForward(z_self_{t-1}, a_actual)
residual_z_self  = z_self_observed - predicted_z_self
causal_sig_self  = f(residual_z_self, context)
```

No counterfactual query. The prediction on the actually-taken action is the
reference; the residual is the agency signal.

**Why the structure mirrors ARC-033 rather than adding a new mechanism class.**
MECH-256 asserts that the comparator is stream-agnostic computationally. SD-030
is therefore an instance, not a variant. The engineering differences from
ARC-033 are parameter-level (z_self has different dimensionality, different
autocorrelation profile, different action-conditional structure), not
architectural.

## Architecture Context

E2SelfForward is distinct from E2FastPredictor in the same way E2HarmSForward
is: it operates on its own latent stream, trained with its own loss, with
stop-gradient on the input latent to prevent encoder drift. In V4, three
parallel forward models coexist:

- E2HarmSForward (ARC-033) -- on z_harm_s, V3-active
- E2SelfForward (SD-030) -- on z_self, V4
- E2WorldForward (SD-031) -- on z_world, V4

MECH-257 asserts that each of these substrates is read in two modes:
retrospective comparator (attribution) and prospective rollout-scoring
(evaluation). SD-030 inherits the dual-mode reading. The V3 evaluator on
z_world (score_trajectory in E3) is the prospective mode of a not-yet-existing
E2WorldForward; the same pattern applies to E2SelfForward.

Training protocol (phased, inherited from ARC-033):
- P0: z_self encoder warmup (body-state supervision; currently a single-layer
  MLP per SD-005, DR-13 flagged this for expansion in V4)
- P1: E2SelfForward trains on frozen z_self (stop-gradient on z_self_t inputs)
- P2: Evaluation (forward_r2, self_causal_gap on scripted self-vs-external
  perturbation trials)

## What This Enables

**Motor-proprioceptive self-attribution.** The REE analogue of the question
"did my body just move because I willed it, or was I pushed?" The residual
distinguishes self-generated from externally-imposed body-state changes.

**Extends descending modulation beyond the harm stream.** V3's SD-021 pathway
attenuates z_harm_s during commitment because the comparator expects cancellation
(self-inflicted pain attenuation). The z_self stream has an even stronger case
for the same pattern: voluntary movement produces predictable proprioceptive
input, which is attenuated relative to externally-induced movement. The
cerebellar-S1/S2 cancellation (Blakemore 1998) is the canonical biological
signature.

**Precondition for MECH-215 capacity estimation.** DR-12 in the V3/V4 boundary
notes that E3 currently trusts E2's rollout unconditionally. When the forward
model on the agent's body is degraded -- injury, fatigue, reduced motor capacity
-- the residual should increase (the prediction fails even though the action was
self-generated). A working E2SelfForward is the substrate through which E3 can
learn "this self-transition is unreliable" and discount trajectories accordingly.

**Precondition for z_self-domain goals.** DR-11 flags z_self-domain goal
representation ("I want my energy restored", "I want to not be in pain") as
structurally inaccessible to V3. A working E2SelfForward is required before
E3 can plan trajectories in z_self space -- the evaluator mode of MECH-257 on
this substrate is the mechanism that scores candidate action sequences by
their predicted self-state trajectories.

## Module Location (V4 target)

```python
# Planned location (mirrors ARC-033 pattern):
# from ree_core.predictors.e2_self import E2SelfForward, E2SelfConfig
#
# Enabled via LatentStackConfig.use_e2_self_forward (False default).
# Config dataclass E2SelfConfig standalone in e2_self.py.
#
# Integration point in agent.py:
#   latent_state.z_self_pred = e2_self(latent_state.z_self_prev, action_onehot)
#   self_residual = latent_state.z_self - latent_state.z_self_pred
```

No V3 implementation exists. V4 milestone: following SD-005 z_self expansion
(DR-13: recurrent z_self encoder or E1 feedback into z_self), register a
dedicated `ree_core/predictors/e2_self.py` module.

## ML Engineering Notes

Inherited from ARC-033 pattern:

- **Stop-gradient** on z_self inputs to forward model during P1 (prevent encoder
  drift -- identity collapse is the default failure mode on autocorrelated
  streams).
- **Residual-delta architecture** (not direct next-state prediction). z_self is
  strongly autocorrelated (body state changes slowly relative to observation
  cadence); a direct predictor collapses to identity. Predicting the delta forces
  the network to learn change structure.
- **Small learning rate** (5e-4 initial, matching E2HarmSForward; may need
  tuning for the z_self dim and typical motion-induced delta magnitude).
- **Phased training** required: P0 encoder warmup with body-state supervision,
  P1 frozen-encoder forward model training, P2 evaluation.
- **Interventional training** (SD-013 analogue): once P1 baseline works,
  consider margin loss forcing ||E2_self(z_self, a_i) - E2_self(z_self, a_j)||
  >= margin for a_i != a_j. Prevents observational confound where ambient
  correlations let the model predict z_self_{t+1} without using the action.
- **MECH-094:** not applicable (waking forward model, not replay content).

New to SD-030 relative to ARC-033:

- **Temporal depth constraint (DR-13).** If V4 z_self encoder is still a
  single-layer MLP, the forward model inherits a flat input. Recurrence in z_self
  (LSTM or E1-feedback into z_self enrichment) should precede SD-030
  implementation. Otherwise E2_self has nothing to predict from.
- **Body-frame action encoding.** Actions in CausalGridWorldV2 are 4-direction
  one-hot. For z_self, the relevant representation is the motor command in
  body frame (which limb, which direction, what force). V4 environment
  extension may need richer action encoding before E2_self can saturate its
  capacity.

## Biological Grounding

**Cerebellar internal models (Wolpert, Miall, Ito).** The canonical forward-model
locus. Wolpert & Miall 1996 (Neural Networks): the cerebellum maintains an
internal forward model of the body that predicts sensory consequences of motor
commands. Ito 2008 (Nat Rev Neurosci): cerebellar microcomplexes as learned
forward models.

**Self-generated tactile attenuation (Blakemore 1998, Nat Neurosci).** When
subjects self-tickle vs are tickled by another, the self-generated input is
perceived as less intense. fMRI shows reduced S1/S2 activation for self-generated
tactile input. The attenuation requires predictability -- delayed or
trajectory-perturbed self-touch reinstates the full response. This IS the
E2_self comparator running on the tactile substream of z_self.

**Force-matching underestimation (Shergill 2003, Science).** Subjects asked to
match a force applied to their finger systematically over-apply force when
generating it themselves. The forward model cancels the expected sensory
consequence of self-generated force, so the self-generated force feels weaker
than the external reference at the same physical magnitude. Schizophrenia
patients with passivity experiences show reduced attenuation (Shergill 2005,
Am J Psychiatry) -- consistent with Frith 2000's comparator-failure framing.

**Saccadic corollary discharge (Sommer & Wurtz).** Superior colliculus -> MD
thalamus -> parietal cortex corollary discharge pathway. Parietal neurons
remap receptive fields in anticipation of each saccade; the remapping IS the
forward prediction. Lesions to MD thalamus disrupt remapping, producing
behavioural deficits in saccade-target-directed tasks. Oculomotor is a
sub-domain of z_self in the REE mapping.

**Songbird HVC corollary discharge (Crapse & Sommer 2008 review).** During
singing, efference-copy from HVC-RA motor path projects to auditory cortex and
cancels expected auditory feedback. Birds with lesioned corollary discharge
cannot maintain song quality because they cannot distinguish self-generated
from external sound. Self-vocalization is a distinct z_self sub-stream.

**Electrosensory cancellation (Bell, ELL).** Weakly electric fish cancel the
reafferent signal from their own electric organ discharge via granule-cell
negative images in the electrosensory lobe. The cancellation is adaptive
(learned) and disrupted by transecting the corollary-discharge input.
Perfect-model-organism demonstration of the comparator pattern on a sensory
stream with an agent-generated reafferent signal.

Biological grounding for SD-030 is the strongest of the three per-stream
instantiations. ARC-033 has good nociceptive-agency evidence (ACC/insula); SD-031
has moderate evidence (parietal outcome-attribution, MD thalamus); SD-030 has
five distinct preparations across mammals, birds, and fish all converging on
the same mechanism. This is the core of why the comparator was generalised
from SD-003 (z_world-only, counterfactual) to MECH-256 (stream-agnostic,
single-pass).

## Validation Experiment (V4)

Proposed design (not queued for V3):

**Phase P0:** z_self encoder warmup. Supervised on body-state targets from the
environment (energy, limb_damage, residual_pain per SD-022). Verify
z_self stream is discriminative before forward-model training.

**Phase P1:** E2SelfForward training. Frozen z_self encoder, stop-gradient on
z_self_t inputs. Metric: self_forward_r2 > 0.85 on held-out trajectories.
Identity-collapse check: r2 on action-shuffled control must drop below 0.3
(i.e., the model is using the action, not just autocorrelation).

**Phase P2:** Attribution evaluation. Scripted trials with self-initiated
movement vs externally-imposed perturbation (environment extension: a
"pushed" condition that modifies body state independently of the agent's
action). Residual magnitude must be substantially lower for self-initiated
than for pushed. Metric: self_causal_gap = mean(||residual||_pushed) -
mean(||residual||_self) > 0.1.

**Interventional extension (SD-013 analogue):** after P1 baseline, enable
margin loss and retest. Prediction: ambient correlations in body state compress
the causal signal under pure observational training; interventional training
restores it.

**Ablation:** with SD-030 disabled, trajectory selection in E3 cannot
distinguish "reliable body transition" from "unreliable body transition".
V4 experiment is a goal-directed task where fatigue/injury degrades a subset
of actions; agents with working E2SelfForward + DR-12 confidence modulation
should avoid the degraded actions; ablated agents should not.

## Related Claims

- MECH-256: general comparator mechanism (parent)
- MECH-257: dual-function gated readout (comparator + evaluator on same substrate)
- SD-005: self/world latent split (prerequisite -- z_self must exist as a
  first-class stream)
- SD-029: z_harm_s comparator (V3-active sibling)
- SD-031: z_world comparator (V4-deferred sibling)
- ARC-033: E2_harm_s forward model (reference implementation template)
- SD-013: interventional training extension (applied later)
- DR-11, DR-12, DR-13: V4 boundary items this SD unblocks
- MECH-215: self-model prerequisite for agentive prediction (downstream)
- MECH-214: goal-referent E1-representability for z_self domain (downstream)
