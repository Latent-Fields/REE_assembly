Thought intake: trainable relief/safety affordance learners

Date: 2026-06-08
Status: processed
Phase: post-603i successor candidate (V3-narrow minimal trainable bridge; V4/V5-rich tier off the V3 path)
Related: SD-059, MECH-358, MECH-302, MECH-303, MECH-304, SD-058, MECH-357, V3-EXQ-603h, V3-EXQ-603i
Proposed follow-up: if V3-EXQ-603i is partial/fails, route to a trainable relief/safety affordance learner successor rather than treating the bridge concept as wrong.

Processed in:
- MECH-375 (trainable relief critic Q_relief(state, action, threat_context) -- learned parametric negative-reinforcement credit-assignment head) -- docs/claims/claims.yaml
- MECH-376 (trainable prospective safety predictor P_safety(state, cue, action, context) -- learned threat-absence / conditioned-inhibition head, distinct from z_goal) -- docs/claims/claims.yaml
- Q-067 (relief-only vs safety-only vs both-required decomposition; which component to train first per the V3-EXQ-603i outcome) -- docs/claims/claims.yaml
- docs/architecture/trainable_relief_safety_affordance_learners.md (home doc)
- Reaped 2026-06-09. ALREADY-OWNED cross-refs (depends_on, not duplicated): SD-050, MECH-302/303/304, SD-058/SD-059, MECH-357/358. All three new claims candidate / substrate_conditional / implementation_phase:v3.

Core thought

The escape-affordance bridge should not ultimately remain a fixed arithmetic table. Relief and safety both need to be trainable.

603h showed the missing structure clearly: the agent could suppress freezing and act under threat, but it did not learn that a specific action/location/policy was the way out. Scalar avoidance efficacy was insufficient because it did not bind relief to an escape direction.

603i is a valid minimal diagnostic bridge: it tests whether binding relief/safety credit to first-action classes is enough to rescue Stage-H survival. But even if it helps, it should be treated as the V3-minimal scaffold of a richer system, not the mature architecture.

Biological/computational interpretation

Relief is not ordinary pleasure and not ordinary wanting. It is an aversive-offset reinforcement signal: “this action reduced suffering / terminated harm.” It can reuse reward/goal machinery, but its function is negative-reinforcement credit assignment, not generic appetite.

Safety is not relief and not mere low harm. It is a prospective learned predictor: “this cue/context/action means threat is absent or likely to remain absent.” It licenses commitment-release, approach, and recovery, but should remain distinct from z_goal.

Therefore REE needs two trainable heads:

Q_relief(state, action, threat_context)
    learns expected harm/suffering reduction after action

and

P_safety(state, cue, action, context)
    learns threat-absence / response-produced safety / conditioned inhibition

These should feed E3 as bounded, threat-gated score-biases rather than becoming global reward.

Proposed architecture direction

1. Trainable relief critic

Input candidates:

* current z_world
* z_self
* current threat/harm streams, especially z_harm_a
* action class / candidate first action
* possibly local trajectory features from E3

Training target:

* positive target when a directed action under threat is followed by a drop in z_harm_a
* stronger target when the drop is temporally close, action-contingent, and not explained by passive environmental drift
* negative / extinction target when the expected relief action fails to reduce harm

Functional role:

* under future threat, bias E3 toward actions predicted to reduce harm/suffering
* do not fire when safe
* do not credit no-op/freeze unless explicitly modelling passive safety

2. Trainable safety predictor

Input candidates:

* current z_world
* cue/context features
* action class / recent action
* threat history
* time since threat offset
* possibly hippocampal context slot / rule representation

Training target:

* positive target when a cue/context/action predicts threat absence or response-produced safety
* negative target when “safe” cues are followed by threat recurrence
* contrastive target to prevent overgeneralising safety to stable background features that merely co-occurred with relief

Functional role:

* support commitment release
* permit approach to safety affordances
* stabilise recovery after threat
* prevent persistent defensive mode when threat is genuinely absent

Why both are needed

Relief alone can teach “that action reduced harm,” but may not produce a stable prospective safety model.

Safety alone can teach “this context/cue is safe,” but may not solve action-specific escape under active threat.

The mature avoidance system needs both:

* action-contingent relief learning for escape;
* cue/context-contingent safety learning for recovery, inhibition of defensive mode, and future approach.

Relation to 603i

603i should be allowed to complete as the minimal bridge test. It should not be reinterpreted mid-run.

If 603i passes:

* SD-059 / MECH-358 can be treated as V3-minimal validated.
* A trainable relief/safety learner can be logged as a V3-enrichment or V4-bridge candidate, depending on closure pressure.

If 603i partially passes:

* inspect whether relief-only, safety-only, or both-required pattern emerged.
* successor should train only the missing/weak component first.

If 603i fails but non-vacuity fires:

* do not conclude “relief/safety bridge wrong.”
* likely conclusion: fixed first-action-class table is too crude; trainable state-action/context-cue learner required.

If 603i fails because bridge credit does not fire:

* route back to substrate readiness: harm derivative, trained encoder, threat detector, or action-contingency detection.

Design guardrails

The trainable system must remain:

* bounded: cannot dominate E3 scoring;
* threat-gated: no global approach bias when safe;
* extinguishable: failed relief/safety predictions decay;
* contrastive: safety cannot simply mean “low harm” or “recent relief”;
* action-bound: relief must credit the action/policy that produced harm reduction;
* cue/context-bound: safety must credit the cue/context/action that predicts threat absence;
* MECH-094-safe: simulated relief/safety in hypothesis mode must not train the waking learner unless explicitly authorised as play/training.

Provisional conclusion

The fixed 603i escape-affordance bridge is a useful V3 diagnostic scaffold. The biologically stronger architecture is a pair of trainable relief/safety affordance learners:

relief = action-contingent aversive-offset reinforcement
safety = prospective threat-absence / conditioned-inhibition prediction

Together they convert “I can stop freezing” into “I know what action gets me out, and I can recognise when I am safe.”
