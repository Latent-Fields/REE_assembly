# Thought intake: body-as-owned-object, selfhood binding, and bounded other-self projection

**Date:** 2026-07-31  
**Status:** thought intake / cross-plan integration audit; not yet a registered claim cluster  
**Proposed location:** `evidence/planning/thought_intake_2026-07-31_body_owned_object_selfhood_other_projection.md`  
**Primary trigger:** audit of inspectable models across V3–V6 and clarification that the body should be represented through the general object substrate, with selfhood and other-self modelling layered through typed relations rather than separate body-specific machinery  
**Related work:** object representation V4, object persistence, part–whole binding, action objects, self-model V4, reafference comparator family, z_self / z_world separation, agency attribution, mirror modelling V5, multi-agent ecology V5, theory of mind, ethics-as-coherence, agent-indexed harm and goal terrain, tool use, affordance inference

---

## 1. Immediate trigger

REE’s forward architecture already provides the likely ingredients for embodiment and social modelling:

```text
persistent object representation
object parts and relations
object permanence
object-to-action affordance binding
self/world separation
reafferent prediction
interoceptive and harm streams
stateful self-model
other-agent slots
mirror modelling
agent-indexed welfare and goal inference
```

A separate body-schema module would risk duplicating this machinery.

The more coherent architecture is:

> The body is one persistent object among others, but it is bound to selfhood through privileged ownership, controllability, reafference, interoception, action-origin and autobiographical-continuity relations.

Other agents begin as persistent objects and may become represented as possible selves through a bounded application of the same selfhood model.

The genuine architectural issue is therefore not whether REE needs a separate body model. It is whether the planned object, self and other systems explicitly represent the binding relations that distinguish:

```text
my body
an external object
a controlled tool
another embodied agent
a represented other self
```

---

## 2. Core insight

The body need not be a different ontological category from other objects.

It can share the general object substrate:

```text
identity
persistence
parts
part relations
pose
dynamics
damage
affordances
causal transitions
```

What makes a persistent object the agent’s body is a set of privileged, dynamically maintained relations:

```text
owned_by_self
directly_controllable
source_of_reafference
source_of_interoception
origin_of_action
boundary_of_direct_harm
coupled_to_autobiographical_continuity
```

This yields the factorisation:

```text
body representation
    =
persistent object representation
    +
self-binding relations
    +
privileged access channels
```

Similarly, another agent need not require a wholly separate representational architecture.

A persistent embodied object may support an `OtherSelfHypothesis` when evidence suggests that it possesses:

```text
private state
goals
harm gradients
beliefs
memory
controllability
perspective
commitments
```

The selfhood model can therefore act as a structural generative template for modelling others.

However, self and other must remain epistemically asymmetric.

---

## 3. Body as a privileged object

### 3.1 Shared object structure

The body should use ordinary object primitives wherever possible:

```text
persistent identity
part–whole hierarchy
spatial relations
dynamics
state changes
damage
interaction history
```

A limb, sensor, actuator or body region is therefore an object part rather than a separate self-specific primitive.

This allows the same relational machinery to represent:

```text
a hand
a wheel
a gripper
a damaged limb
a tool
another agent’s limb
```

### 3.2 Self-binding relations

The body becomes self-specific through relations rather than object type.

A possible structure is:

```text
SelfBinding:
    self_id
    object_id
    ownership_confidence
    controllability_by_part
    reafference_match
    interoceptive_source_strength
    action_origin_confidence
    direct_harm_source
    autobiographical_continuity
    temporal_stability
    uncertainty
    provenance
```

These relations should be learned and updateable.

They must not be permanently hard-coded merely because a sensor channel was initially designated “self.”

### 3.3 Multiple candidate bindings

Under ambiguity or perturbation, REE may need to maintain competing hypotheses:

```text
this object is part of me
this object is controlled by me but not part of me
this sensory consequence was externally caused
this apparent body part is visually correlated but not controllable
```

This suggests that ownership and embodiment should be graded and evidence-sensitive.

The architecture should not collapse immediately to one body boundary when evidence is incomplete.

---

## 4. Affordances as body-relative object relations

An affordance is not solely a property of an external object.

It is a relation among:

```text
object
current body
available tools
goal
environment
skill
uncertainty
```

For example:

```text
reachable(object_A, self_body)
graspable(object_B, left_effector)
liftable(object_C, current_strength)
safe_to_cross(gap_D, current_balance)
```

This does not require a separate body-schema object if the general object model can represent parts, kinematics, controllability, capability, damage and tool relations.

The key requirement is that object affordances be conditioned on the object currently bound as the body.

A generic affordance such as `graspable(object)` is insufficient. The architecture needs something closer to:

```text
graspable(object, agent_body_state, tool_state, skill_state)
```

---

## 5. Tool use and graded incorporation

A tool is initially an external object.

Through use, REE may learn relations such as:

```text
hand controls tool
tool extends reach
tool transmits action consequence
tool produces predictable reafference
tool modifies available affordances
```

This need not mean that the tool literally becomes part of the self.

Tool incorporation can be represented as graded functional coupling:

```text
control reliability
reafferent predictability
causal dependence
capability extension
temporal attachment
```

A possible relation is:

```text
FunctionalExtension:
    self_bound_part
    external_object
    control_coupling
    sensory_coupling
    capability_delta
    reliability
    attachment_state
```

This prevents two errors:

1. treating every controlled object as part of the self;
2. treating tools as ordinary detached objects after they have changed the agent’s effective action space.

---

## 6. Other agents as self-structured hypotheses

### 6.1 From object to possible agent

An observed entity begins as a persistent object:

```text
identity
body parts
trajectory
actions
effects
interaction history
```

REE may infer that the object is an agent when its behaviour is better explained by:

```text
internally organised goals
selective controllability
persistent preferences
belief-dependent action
harm avoidance
memory
commitment
```

The transition is therefore:

```text
PersistentObject
    -> AgentHypothesis
    -> OtherSelfHypothesis
```

These should remain distinguishable.

An object may be agent-like without yet supporting a rich model of selfhood.

### 6.2 Selfhood as a generative template

The self-model supplies a structured hypothesis space for others:

```text
this other may have goals
this other may experience harm
this other may hold beliefs
this other may remember
this other may control its body
this other may have a perspective different from mine
```

This is not direct access to the other’s state. It is an inference using structural analogy.

A possible object is:

```text
OtherSelfHypothesis:
    object_id
    agent_probability
    inferred_body_binding
    inferred_goal_state
    inferred_harm_state
    inferred_belief_state
    inferred_memory_state
    inferred_controllability
    inferred_perspective
    inferred_commitments
    similarity_to_self
    uncertainty_by_field
    evidence_provenance
```

### 6.3 Epistemic asymmetry

For the self, REE may possess:

```text
direct interoception
direct motor-command access
efference copy
first-person memory provenance
high-confidence ownership evidence
```

For another, REE possesses:

```text
observed behaviour
observed body
environmental effects
communication
inferred hidden state
```

Therefore the same structural model must operate under different access conditions.

The architecture must preserve source, perspective, uncertainty and access boundary at every stage.

The other-self model must never acquire the epistemic authority of direct self access merely because it uses the same structural template.

---

## 7. Self–other homology without identity

The intended relation is:

```text
self and other are structurally comparable
but not informationally interchangeable
```

This supports later REE claims concerning mirror modelling, empathy, agent-indexed harm, agent-indexed goal terrain, responsibility, shared commitments, love and repair without requiring a separate architecture for each other agent.

The same selfhood variables may be instantiated in different indexed slots:

```text
SelfModel[self]
SelfModel[other_A]
SelfModel[other_B]
```

But their update rules differ.

For `self`:

```text
direct sensory and motor evidence
```

For `other_A`:

```text
behavioural and communicative inference
```

This indexed homology is likely the cleanest path from V4 selfhood to V5 social cognition.

---

## 8. Critical guardrails

### 8.1 No self–other state leakage

The system must not write another agent’s inferred state into the self’s direct state channels. Likewise, the self’s state must not be projected onto another without evidence.

### 8.2 No false interoceptive access

REE must not treat inferred other-harm as if it were direct nociception. The two may affect common downstream ethical machinery, but provenance must remain distinct.

### 8.3 No egocentric completion without uncertainty

The self-model provides priors, not truth. Differences in body, goals, history, culture, competence and perspective must remain representable.

### 8.4 No body ownership from controllability alone

A remotely controlled object may be highly controllable without being part of the body.

Ownership should depend on convergent evidence:

```text
controllability
reafference
interoception
continuity
action origin
persistent coupling
```

### 8.5 No other-self attribution from motion alone

Stochastic or reactive systems may resemble agents. Agent and selfhood hypotheses should require discriminating evidence.

---

## 9. Cross-plan integration questions

This intake should be treated initially as an integration audit.

### Object representation V4

Does the object substrate support:

```text
articulated parts
changing capability
damage
controllability relations
agent-indexed affordances
```

### Self-model V4

Does the self-model bind to a persistent object token? Or does it risk becoming an independent narrative or latent structure without an embodied referent?

### Action-object and affordance plans

Are affordances explicitly body-relative? Can the same external object support different affordances for differently embodied agents?

### Mirror modelling V5

Does mirror modelling instantiate self-structured hypotheses over persistent object tokens? Does it preserve uncertainty and perspective boundaries?

### Multi-agent ecology V5

Can different agents have different bodies, capabilities and private state access?

### Ethics-as-coherence V5

Are other-indexed harm and goal gradients grounded in an identified other-object slot? Or can ethical variables float without a stable represented subject?

---

## 10. Strong competing explanations

A new claim cluster may be unnecessary if existing roadmaps already specify:

1. the body as a special self-indexed object;
2. typed self-binding relations;
3. body-relative affordances;
4. indexed homologous self/other models;
5. strict provenance and perspective separation.

The apparent gap may be only documentation fragmentation across object representation, self-model, reafference, affordance inference, mirror modelling and social ethics.

If so, the correct action is a cross-plan synthesis note and dependency map, not a new mechanism.

---

## 11. Proposed minimal experiments

### Experiment A: self-bound versus controlled object

Provide two objects:

```text
one physically coupled to the agent’s sensors and actuators
one remotely controlled with similar action reliability
```

Test whether REE distinguishes:

```text
part of my body
controlled by me
external object affected by me
```

### Experiment B: ownership under conflicting evidence

Create conflicts among visual continuity, motor controllability, reafference and interoceptive source.

Test whether REE maintains graded or competing body-binding hypotheses rather than using one cue absolutely.

### Experiment C: body-relative affordance

Present the same object to agents with different embodiment or damage.

Test whether affordance estimates differ appropriately while object identity remains stable.

### Experiment D: bounded other-self projection

Give another agent a goal, belief or harm state different from REE’s own.

Test whether REE uses the selfhood template to infer hidden state, preserves the difference from self, tracks uncertainty, and updates after contradictory evidence.

### Experiment E: provenance-preserving empathy

Allow inferred other-harm to influence E3.

Test that:

```text
other-harm changes action
other-harm remains labelled as inferred and other-indexed
self nociceptive state does not falsely change
```

---

## 12. Failure and falsification conditions

The integration proposal is weakened if:

```text
self-model functions without binding to any object token
body-relative affordance transfer does not improve behaviour
other-self modelling performs no better than generic trajectory prediction
self-structured priors cause persistent egocentric errors
ownership variables fail to track causal interventions
tool coupling is handled adequately by ordinary object relations without additional typing
```

A new architectural claim should not be registered if a synthesis of existing plans already fully owns these relations.

---

## 13. Proposed routing

1. Audit object representation V4 for body-object ownership.
2. Audit self-model V4 for explicit object-token binding.
3. Audit affordance plans for body-relative feasibility.
4. Audit mirror modelling V5 for self-structured but epistemically asymmetric other models.
5. Audit ethics-as-coherence for stable agent-indexed referents.
6. Produce a cross-plan dependency diagram:

```text
object
    -> self-bound body
    -> selfhood
    -> inferred other agent
    -> other-self model
    -> agent-indexed ethics
```

7. Register new claims only for relations that remain genuinely unowned.

**Provisional generation:** cross-generational integration spanning V4 object/self architecture and V5 social architecture. It should not be assigned to one generation until ownership is resolved.

---

## 14. Working conclusion

REE does not necessarily need a separate body-schema organ.

The cleaner architecture is:

> Bodies are persistent objects. One becomes my body through self-binding relations. Another becomes a possible other self when the selfhood model is applied as a bounded, uncertain and perspective-preserving generative template.

The unresolved work is to ensure those binding relations are explicit, inspectable and owned across the roadmap.
