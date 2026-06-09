# Thought intake: inference, belief-state construction, and inferred affordance fields

**Date:** 2026-06-09  
**Status:** thought intake / architecture-pressure note; not yet a registered claim cluster  
**Proposed location:** `evidence/planning/thought_intake_2026-06-09_inference_belief_state_affordance_layer.md`  
**Primary trigger:** V3-EXQ-603k harm-pathway validation, especially the emerging split between `ARM_HARM_ON_NAV` and `ARM_HARM_ON_MIDLINE`  
**Related work:** state definition, hippocampal map primitives, hippocampal systems, rule apprehension, cue ecology / cue-recall, SD-059 escape-affordance bridge, Q-044 epistemic value / curiosity, V3-EXQ-603i/603j/603k/653/654/655

---

## 1. Immediate trigger

V3-EXQ-603k appears to show that the harm pathway is becoming behaviourally live.

The headline arm pattern, as currently observed in runner heartbeat state, is:

```text
ARM_HARM_OFF_NAV: 0/3 pass
ARM_HARM_ON_NAV: 2/3 pass
```

This supports the reading that training the previously untrained harm-avoidance valuation pathway can lift survival when the safety/navigation setup is favourable.

However, the harder informational arm, `ARM_HARM_ON_MIDLINE`, exposes a further issue. Seed 42 failed Stage-H despite strong early survival and active harm training:

```text
ARM_HARM_ON_MIDLINE seed 42:
  P0 mean_len high
  harm pathway active
  Stage-H G_H fail
  P1 survival gate pass
  final verdict fail
```

This should not automatically be read as weakening the harm-pathway fix. It may instead indicate that the midline arm is asking for a different competence:

> not merely “can the creature value danger?”,  
> but “can the creature infer a route to safety from partial map/cue/gradient evidence?”

That competence is not currently named as a first-class REE layer.

---

## 2. Core insight

REE already contains many of the ingredients of inference:

```text
state abstraction
uncertainty structure
hippocampal indexing
pattern completion
counterfactual rollout
E2 action-consequence prediction
E3 trajectory evaluation
cue recall
rule apprehension
candidate trajectories
control-plane precision/gating
```

But the architecture does not yet appear to name **inference** as a distinct integrative function.

The missing name is something like:

> **Inference = construction of latent state hypotheses and inferred affordances from partial observations, memory, cues, rules, affective gradients, and predicted transitions.**

This is not a new organ ex nihilo. It is a bridge function between organs that already exist or are already planned.

---

## 3. Distinction: rule apprehension versus inference

Rule apprehension goes some of the way, but it is not the whole thing.

Rule apprehension:

```text
This kind of context follows this regularity.
This room has this rule.
This cue usually means this policy regime should be available.
```

Inference:

```text
Given this partial evidence, which situation am I probably in?
Which hidden structure is likely present?
Which rule, if any, applies here?
What unobserved affordances probably exist?
Which action would test or exploit that hypothesis?
```

Rule apprehension supplies candidate regularities. Inference selects, combines, and applies them under uncertainty.

Rule-goblin knows cave customs.  
Map-goblin remembers tunnels.  
Cue-goblin smells reef.  
Inference-goblin says: “Given smoke, slope, old reef-smell, and the remembered left turn, the safe path is probably there.”  
Commitment-goblin then has something intelligent to choose.

---

## 4. Relationship to existing REE architecture

### 4.1 State

REE already defines state as:

```text
State = situation as navigable from here.
```

A state is not raw perception. It is a compressed relational package linking inferred world structure, agent condition, temporal position, goal relation, antigoal relation, constraints, uncertainty, and transition readiness.

This is already inference-ready, but the architecture still needs to specify how the state is inferred when observation is partial, ambiguous, misleading, or insufficient.

Current architecture answers:

```text
What is a valid REE state?
```

The missing inference layer asks:

```text
How does REE construct a valid state from incomplete evidence?
```

### 4.2 Hippocampal systems

The hippocampal system already provides:

```text
path memory
episodic traces
pattern completion
counterfactual rollout
hypothesis injection
viability mapping
```

This is directly inference-adjacent. Pattern completion reconstructs plausible trajectories from sparse cues. Hypothesis injection lets remembered or imagined trajectories speak into the present. Viability mapping labels action-consequence coordinates with harm/goal outcomes.

But the current documents keep hippocampus deliberately orthogonal to valuation and commitment. That is correct. The missing layer is not “make hippocampus decide.” It is:

```text
hippocampus proposes / completes / replays
E2 predicts action consequences
rules constrain possible futures
cue systems retrieve relevant traces
control plane gates precision
E3 evaluates and commits
```

Inference is the integrative loop by which these proposals become state hypotheses and inferred affordance fields.

### 4.3 Cue ecology

The cue-recall work already exposed a key distinction:

```text
cue formation: does the cue have anything to recall?
cue authority: does a fired cue change behaviour?
```

638a showed that cues could fire without lifting contact, and might even displace stronger wild-seeded attractors. This forced a measurement-only post-cue action diagnostic.

That same structure likely applies to safety cues and harm escape:

```text
danger cue fires
harm valuation rises
but does the cue orient action?
does it retrieve a safety route?
does it bias candidate trajectories?
does selected action reduce distance to refuge?
```

This is a cue-to-inference-to-action gap, not merely a cue-firing gap.

### 4.4 Rule apprehension

The rule-apprehension layer already states a strong architecture:

```text
regularity detection
→ tolerance-gated rule availability
→ hippocampal rollout biasing
→ approach/avoid goal weighting
→ basal ganglia commitment
→ action
→ evidence record
→ waking and sleep/offline refinement
```

Inference should sit alongside this pipeline, not replace it.

Rules bias the hypothesis space. Inference uses those rules, plus map/cue/memory/evidence, to infer the current latent situation and likely transitions.

### 4.5 SD-059 / MECH-358 escape-affordance bridge

The escape-affordance bridge is highly relevant because it moves beyond scalar harm avoidance. It asks whether relief/safety credit becomes action-specific and future-biasing.

This is likely one of the first behavioural expressions of inference:

```text
not merely “harm is bad”
but “this kind of action, in this kind of state, tends to lead toward safety”
```

The bridge converts undirected avoidance into directed escape affordance.

---

## 5. Biological grounding

The biological picture strongly supports a distinct inference framing.

### 5.1 Hippocampal-prefrontal replay

Awake hippocampal replay is not only sleep consolidation. It appears during pauses, decision points, and learning, and can represent possible or remembered trajectories. Hippocampal-prefrontal coordination can distinguish correct upcoming paths from incorrect alternatives, and disrupted coordination precedes errors.

REE mapping:

```text
hippocampal replay / completion
→ candidate future hypotheses
→ prefrontal / E3-like selection context
→ better or worse action commitment
```

This supports the idea that hippocampal output is not merely memory retrieval. It is a source of prospective hypotheses.

### 5.2 Cognitive maps and relational inference

The hippocampal-entorhinal system is increasingly understood as a general relational mapping system, not only a spatial mapper. A cognitive map can encode abstract relations, conceptual spaces, and latent structure. This supports REE’s state-as-navigable framing.

Inference is what happens when the system uses such a map to answer:

```text
where am I in this relational space?
what unseen relation follows?
which transition is likely viable?
```

### 5.3 Pattern completion and preplay

Pattern completion allows partial cues to reconstruct plausible full trajectories. This is powerful but dangerous: completed trajectories are hypotheses, not perceptions and not commitments.

REE already has the correct safety principle here:

```text
completed trajectory = hypothesis
not perception overwrite
not automatic commitment
```

Inference should preserve this. It should propose state hypotheses and inferred affordances without collapsing uncertainty too early.

---

## 6. Machine-learning grounding

### 6.1 Partially Observable Markov Decision Processes

In a Partially Observable Markov Decision Process, the agent cannot directly observe the true world state. It must maintain a belief state over possible hidden states, updated through action and observation history. The policy is therefore not simply observation → action. It is belief/history → action.

REE does not need to copy the full Partially Observable Markov Decision Process formalism, but the functional point is essential:

```text
under partial observability, action must be selected from inferred state, not raw observation
```

### 6.2 Latent world models

World-model agents such as Dreamer learn compact latent dynamics and use imagined trajectories to train behaviour. This is a machine-learning analogue of REE’s E2/hippocampal rollout structure:

```text
latent model
→ imagined trajectories
→ value / policy learning
→ action without direct trial-and-error for every situation
```

REE differs because it separates harm, goal, residue, commitment, and ethical texture rather than collapsing everything into reward. But the shared insight is that intelligent action depends on latent prediction, not just reactive mapping.

### 6.3 Active inference and epistemic value

Active inference frames action as serving both pragmatic and epistemic value. Actions may be selected not only to obtain reward or avoid harm, but to reduce uncertainty about hidden causes or future outcomes.

REE already has Q-044 novelty / uncertainty / learning-progress machinery. However, that machinery currently lives mainly under curiosity and exploration. The inference layer would generalise the same idea:

```text
epistemic action is not only curiosity
it is also survival-relevant uncertainty reduction
```

In a dangerous midline state, the intelligent action may be one that tests where safety is, not merely one that maximises immediate harm avoidance.

---

## 7. Proposed architecture slot

### Proposed ARC-0xx: Inference / Belief-State Affordance Layer

**Type:** architectural_commitment  
**Status:** candidate / thought-intake proposed  
**Phase:** likely V4 full implementation; V3 should name and route, and may add limited diagnostics if exposed by 603k  
**Depends on:** ARC-004 L-space, ARC-007 hippocampal systems, ARC-018 hippocampal rollout / viability mapping, MECH-022 hypothesis injection, MECH-033 E2 kernel to rollout interface, ARC-062/063 rule apprehension, SD-057 cue recall, SD-059 escape-affordance bridge, E3 trajectory commitment, control-plane precision routing

**Claim text:**

> REE requires an inference layer that constructs latent state hypotheses and inferred affordance fields from partial observations, memory, cue traces, candidate rules, affective gradients, uncertainty, and E2 action-consequence rollouts, so that E3 can select trajectories under partial observability without requiring direct perception or oracle-like prior knowledge.

**Rationale:**

A state cannot be treated as the current observation. A valid REE state is a navigable situation model. When sensory evidence is incomplete, REE must infer the state before it can evaluate trajectories.

---

## 8. Proposed candidate claims

### Candidate INV-0xx: Inferred state must not collapse to perceived observation

**Type:** invariant  
**Proposed text:**

> A REE state is valid only if it can integrate observation with memory, temporal context, self-state, cue context, rule context, and uncertainty. Under partial observability, the current perceived scene is evidence for state, not identical to state.

**Depends on:** INV-035, INV-036, ARC-004, ARC-007, ARC-018

**Why needed:**

The existing state invariants already say state is not raw perception. This candidate makes explicit that state must sometimes be inferred.

---

### Candidate MECH-0xx: Belief-state hypothesis set

**Type:** mechanism_hypothesis  
**Proposed text:**

> When observations are ambiguous or incomplete, REE maintains a bounded set of competing latent-state hypotheses, each carrying confidence/precision, predicted transitions, goal/antigoal relations, and uncertainty. E3 evaluates candidate trajectories over this hypothesis set rather than over a single collapsed state.

**V3 minimal form:**

```text
top-k state hypotheses
confidence weights
uncertainty flags
candidate transition costs
```

**V4 fuller form:**

```text
structured belief-state distribution
hypothesis generation from hippocampal completion
hypothesis updating from action/outcome evidence
epistemic action selection
```

---

### Candidate MECH-0xx: Inferred affordance field

**Type:** mechanism_hypothesis  
**Proposed text:**

> REE can infer affordances that are not directly perceived by combining current cues, hippocampal traces, E2 action-consequence predictions, CandidateRuleField content, affective gradients, and control-plane precision. These inferred affordances bias E3 candidate trajectories without overwriting perception.

**Example:**

```text
danger gradient + remembered reef cue + previous safe trajectory
→ inferred safety direction
→ higher rollout eligibility for refuge-seeking actions
```

**Design constraint:**

Inferred affordances are hypotheses, not facts. They must carry uncertainty and be corrigible by action outcome.

---

### Candidate MECH-0xx: Safety-route inference

**Type:** mechanism_hypothesis / substrate-development target  
**Proposed text:**

> Under threat, REE can infer a likely route to safety from partial map, cue, gradient, and prior trajectory evidence, rather than requiring safety to be directly visible or navigation-handed.

**Motivation from V3-EXQ-603k:**

`ARM_HARM_ON_NAV` appears to validate harm valuation under favourable navigation/safety setup. `ARM_HARM_ON_MIDLINE` may expose that danger-sense alone is insufficient when the creature lacks map/cue/safety-route inference.

**Important interpretation rule:**

Failure from a harder midline start should not be treated as harm-pathway falsification unless the design demonstrates that route inference was developmentally available and still unused.

---

### Candidate MECH-0xx: Epistemic action pressure

**Type:** mechanism_hypothesis  
**Proposed text:**

> When goal success or harm avoidance depends on hidden state, REE can assign action pressure to information-gathering transitions that reduce uncertainty, even when those actions are not immediately reward-maximising or harm-minimising.

**Examples:**

```text
sample a safer-looking direction to disambiguate map structure
pause/replay before commitment
approach a landmark cue to resolve route hypothesis
avoid immediate high-salience attractor until hidden-risk uncertainty decreases
```

**Relationship to Q-044:**

This generalises novelty / uncertainty / learning-progress curiosity into survival-relevant inference. Epistemic value is not merely play or curiosity; it is also a viability function under partial observability.

---

### Candidate MECH-0xx: Rule apprehension supplies priors for inference

**Type:** mechanism_hypothesis / clarification  
**Proposed text:**

> Candidate rules constrain and structure inference by shaping which state hypotheses and rollout branches are considered likely or usable. Rule apprehension does not replace inference; it supplies priors and availability gates for hypothesis construction and action evaluation.

**Example:**

```text
rule: “hazard bands usually separate unsafe midline from safer reef edge”
cue: harm gradient rising
memory: previous reef-safe trajectory
inference: likely safety route is away from hazard band toward reef edge
```

---

### Candidate INV-0xx: Inferred trajectories must remain provenance-tagged

**Type:** invariant  
**Proposed text:**

> Trajectories generated by pattern completion, replay, rule-guided inference, or cue-driven reconstruction must remain provenance-tagged as inferred/imagined until enacted and updated by committed outcome evidence.

**Why needed:**

This prevents inference from becoming hallucinated certainty. Hippocampal completion should propose possible futures, not overwrite perception or fabricate residue history.

---

## 9. Failure modes to track

Inference introduces powerful new failure modes. These should be tracked early.

```text
failure to infer hidden danger
  → harm exposure despite apparently adequate perception

failure to infer hidden safety
  → avoidant collapse / helplessness / narrow safe zone

overconfident wrong hypothesis
  → reckless commitment

hypothesis collapse too early
  → one bad explanation dominates

hypothesis proliferation
  → indecision, apophenia, paranoid or magical route construction

cue hijack
  → weak cue displaces stronger state evidence

rule overreach
  → candidate rule applies outside its context

map overgeneralisation
  → wrong route transferred from superficially similar state

map oversplitting
  → failure to transfer safe route across equivalent states

epistemic freezing
  → agent keeps gathering information and never commits

anti-epistemic panic
  → agent commits too fast under threat and cannot sample enough evidence
```

These map naturally onto existing REE state-abstraction failure modes: context loss, uncertainty collapse, valence mis-tagging, overmerge, oversplit, and threat spreading.

---

## 10. Relation to V3-EXQ-603k

The current likely interpretation of V3-EXQ-603k should be preserved carefully.

### What 603k appears to show

```text
harm pathway off → creature dies
harm pathway on with navigation/safety support → creature often survives
```

This supports trained harm valuation as behaviourally load-bearing.

### What 603k does not necessarily show

```text
the creature can infer safety routes from arbitrary dangerous starts
the creature has a full map
the creature can perform open-ended escape planning
the creature is generally intelligent across worlds
```

### If midline fails

If `ARM_HARM_ON_MIDLINE` fails while `ARM_HARM_ON_NAV` passes, the correct reading may be:

```text
harm valuation: supported
safety-route inference: not yet available / not yet developmentally fair
midline arm: exposed next missing intelligence layer
```

This would be a progress result, not a setback.

### Why the midline arm may be unfair

A creature dropped into danger without prior route-learning experience, map structure, safety landmarks, or graded exploration history should not be expected to infer escape like a prescient oracle.

A fair developmental version would teach or expose:

```text
reef/safety geography
landmarks
hazard gradients
safe route traces
low-threat exploration
cue-to-refuge association
escape-affordance credit
```

Then test whether harm valuation recruits that knowledge under threat.

---

## 11. Proposed experiment family

### V3-EXQ-xxx: Safety-route inference diagnostic

**Purpose:** distinguish harm valuation failure from inferred-route failure.

**Design sketch:**

Train / expose under low threat:

```text
reef location
hazard gradient
safe path
landmark cues
escape affordance
```

Then test under harder start:

```text
midline start
partial cue
hazard pressure
time-limited survival
```

**Ablation arms:**

```text
MAP_ON + CUE_ON + HARM_ON
MAP_OFF + CUE_ON + HARM_ON
MAP_ON + CUE_OFF + HARM_ON
MAP_ON + MISLEADING_CUE + HARM_ON
MAP_ON + CUE_ON + HARM_OFF
```

**Readouts:**

```text
distance-to-refuge delta after harm rise
post-harm selected action toward inferred safety
candidate trajectory harm-cost differentiation
reef/safety cue activation
E2 predicted relief/safety by action class
hippocampal trace retrieval count
hypothesis confidence / entropy
time-to-first-safety-improving move
survival gate
```

**Interpretation:**

```text
HARM_ON works only when MAP/CUE_ON:
  safety-route inference substrate is load-bearing

HARM_ON fails even with MAP/CUE_ON:
  deeper action-selection or escape-affordance problem

MAP_OFF fails while MAP_ON passes:
  hippocampal map substrate required

MISLEADING_CUE causes wrong route:
  cue authority too strong / provenance or uncertainty insufficient

HARM_OFF fails despite MAP/CUE_ON:
  harm valuation still necessary
```

---

## 12. Possible implementation shape

Minimal V3-adjacent implementation, if pursued:

```text
InferredStateHypothesis:
  state_id
  source_tags: observation | cue | hippocampal_completion | rule | E2_rollout
  confidence
  uncertainty
  predicted_harm
  predicted_benefit
  predicted_safety
  candidate_actions
  provenance

InferredAffordance:
  action_class
  target_relation: toward_safety | away_from_harm | toward_resource | information_gain
  confidence
  evidence_sources
  expected_harm_delta
  expected_goal_delta
  expected_uncertainty_delta
```

E3 would not commit to these directly. It would score candidate trajectories with these as additional inputs, preserving provenance and uncertainty.

---

## 13. Relationship to “actual intelligence”

This is the transition from reflex-like harm avoidance to situated intelligence.

Reflex-like harm avoidance:

```text
danger high → avoid / move away
```

Inference-mediated intelligence:

```text
danger high
+ partial map
+ cue memory
+ rule context
+ predicted transitions
+ uncertainty
→ infer likely route / test action
→ commit
→ update from consequence
```

This is the actual intelligence bit of artificial intelligence:

```text
not merely learning a policy
but constructing a situation
under uncertainty
and acting through a predicted future
```

---

## 14. V3 scope recommendation

Do not explode V3 scope.

Recommended V3 action:

```text
Name the inference layer.
Register candidate claims or an architecture note.
Use 603k midline only as routing pressure, not as a demand for immediate full implementation.
Prevent misinterpretation of midline failure as harm-pathway failure.
Add measurement-only diagnostics if the same gap recurs.
```

V3 can finish as:

```text
pre-social creature substrate
with goal-seeking
harm valuation
candidate trajectories
commitment
relief/safety scaffolding
proto-rule machinery
and a named route toward inference
```

Full inference can become a V4/V5 development arc unless a minimal safety-route diagnostic is needed to close V3 fairly.

---

## 15. Summary

The missing piece is not a new organ. It is a named integrative function.

REE already has:

```text
state
map
memory
cue
rule
prediction
valuation
commitment
```

What now needs naming is:

```text
belief-state and affordance inference under partial observability
```

This layer explains why `ARM_HARM_ON_NAV` can pass while `ARM_HARM_ON_MIDLINE` struggles. The creature can smell danger. It may not yet infer the cave exit.

That is not failure. That is the next intelligence layer becoming visible.

Goblin-status:

```text
harm-goblin: alive
map-goblin: partly awake
cue-goblin: needs authority
rule-goblin: exists but not yet loud enough
inference-goblin: unnamed but now knocking from inside the cave wall
```
