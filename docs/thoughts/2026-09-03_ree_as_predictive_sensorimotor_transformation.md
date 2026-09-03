# Thought: REE as a Predictive Sensorimotor Transformation

## A different representation of the same architecture

Status: conceptual reframing / architectural lens — explicitly not a new REE claim

Date: 2026-09-03

## 1. The simplest possible description

At the end of the day, a nervous system converts sensed state into action.

In that extremely broad sense, the brain can be understood as a **super-complex reflex**.

This does not mean cognition is simple, feed-forward or stimulus-bound. The transformation from sensation to action can depend on internal bodily state, previous experience, predictions, remembered events, current context, uncertainty, other organisms, anticipated consequences and the actions currently under consideration.

Nevertheless, underneath that complexity remains a closed sensorimotor loop:

```text
S_t -> A_t -> S_(t+1) -> A_(t+1)
```

The organism senses. Its internal machinery transforms what is sensed. It acts. Its action changes what is subsequently sensed.

Cognition exists inside this loop rather than outside it.

---

## 2. REE makes the reflex temporally deep

The important REE proposition is not merely that sensory information causes action. It is that the transformation is mediated by predictions of how the world and organism unfold through time.

A crude reflex approximates:

```text
S_t -> A_t
```

A predictive organism instead performs something closer to:

```text
S_t -> predicted S_(t+1:t+n) -> A_t
```

REE makes this richer because predicted futures depend on what the organism itself might do:

```text
S_t, B_t
   -> predicted W_(t+1:t+n | A), predicted B_(t+1:t+n | A)
   -> A_t
```

where `W` is relevant world state, `B` organism/body state, and `A` candidate action or trajectory.

The essential computation becomes:

> Given what appears to be happening, how might the world and organism change if different actions occur?

The resulting behaviour can become organized around trajectories compatible with continued viable interaction and away from trajectories associated with ending, severe harm or catastrophic loss of viability.

That is still a sensorimotor transformation. It is simply a sensorimotor transformation that has acquired a model of time, self and intervention.

---

## 3. Familiar modules can be understood as contributors to one transformation

REE is naturally described using functional nouns:

- world model;
- memory;
- goals;
- planner;
- trajectory generator;
- selector;
- control system.

These descriptions remain useful, but nouns can make processes look more separable than they really are.

The same architecture can instead be represented as one recurrent transformation whose dynamics are altered by different subsystems.

### E1

E1 does not merely hold a world representation. It contributes temporal continuity and learned predictive structure to the sensory–action transformation.

### E2

E2 does not merely "predict futures". It allows contemplated actions to perturb the transformation prospectively:

> If this action is propagated forward, what sensory and organism state would follow?

### Hippocampal-like memory

The hippocampal component need not be conceptualized simply as a map or memory database. Its crucial contribution may include the ability to **chain transformations across states that are not currently sensed**.

It can permit:

```text
here -> remembered intermediate state -> possible later state
```

Memory therefore extends the sensorimotor transformation across absent space, absent time and previously experienced contingencies.

### Frontal-like systems

Frontal systems need not primarily be repositories of goals or executive instructions. They may instead alter the **mapping between representation and action** according to context.

A maintained frontal-like state can make one sensory distinction behaviourally important while another becomes irrelevant. It may therefore be better viewed, at this explanatory level, as configuring, stabilizing or transforming the current sensorimotor mapping rather than simply storing a destination that another system pursues.

### Basal-ganglia-like / E3 machinery

Basal-ganglia-like machinery need not be understood only as a final selector receiving completed plans.

Selection may be the macroscopic description of what happens when competing predictive sensorimotor transformations are differentially amplified, suppressed, prolonged or committed.

What looks from above like:

> choose trajectory A

may mechanistically resemble:

> the dynamics associated with trajectory A increasingly dominate the recurrent transformation until behaviour follows them.

This thought does not claim that this is a complete biological description of frontal cortex, hippocampus or basal ganglia. These are alternative functional interpretations that may help REE engineering.

---

## 4. The modules may be verbs disguised as nouns

This distinction may matter more than it first appears.

"Memory", "goal", "map", "planner" and "selector" sound like objects or boxes. Many underlying functions may be better understood as operations:

- remembering;
- conditioning;
- predicting;
- chaining;
- suppressing;
- amplifying;
- comparing;
- stabilizing;
- committing.

A hippocampal map may be useful because it enables **chaining**.

A goal representation may be useful because it **biases transformation**.

A basal-ganglia selection signal may matter because it **changes propagation through competing action pathways**.

A frontal representation may matter because it **changes which relationship between sensation and action is currently expressed**.

This is not merely linguistic. If REE is engineered around the nouns too literally, it risks imposing artificial interfaces between processes that should remain dynamically coupled.

---

## 5. Goals become less fundamental under this representation

Consider hunger.

One perfectly valid behavioural description is:

> The organism has a goal to obtain food.

But the underlying machinery need not contain a single symbolic or latent object equivalent to:

```text
GOAL = FOOD
```

Hunger might instead alter the entire transformation:

- food-related sensory structure becomes more salient;
- food-associated memories become easier to retrieve;
- predictions involving successful ingestion acquire different significance;
- candidate trajectories leading toward food propagate differently;
- costs that were previously unacceptable may become tolerable;
- actions associated with food acquisition become more likely.

From outside the system this looks like pursuit of a goal. Internally, the "goal" may partly be an emergent property of how the sensorimotor transformation has been reconfigured.

This does **not** mean explicit goal representations cannot exist. REE already contains such machinery, and explicit representations may be computationally useful.

It means only that goal-directed behaviour does not require GOAL to be the fundamental explanatory unit.

---

## 6. Continuation can be represented similarly

The same reasoning may apply to one of REE's deepest commitments: continuation.

It is possible to describe the organism as possessing a goal:

> continue existing.

Another formulation may be closer to the intended developmental architecture.

Through development and learning, the organism's predictive dynamics become shaped such that trajectories associated with bodily destruction, severe harm, loss of control, unrecoverable states or inability to continue interacting produce very different internal dynamics from trajectories associated with viable continuation.

Continuation then need not exist only as a proposition evaluated at the end of planning. It can become a **distributed property of the perception–prediction–action transformation**.

The organism need not always reason:

> I wish to continue existing, therefore I will avoid this.

Its learned architecture can instead increasingly map states predictive of ending away from commitment and states compatible with continued viable interaction toward it.

The behavioural description remains "the organism seeks continuation". The mechanistic description becomes "continuation is embedded in the transformation by which prediction becomes action".

---

## 7. This may matter for later ethical development

The same distinction applies when other organisms enter the system.

A simple engineered ethics system might add another term to trajectory scoring:

```text
U = U_self + lambda * U_other
```

REE's developmental aspiration is deeper than merely attaching another utility term.

If another organism becomes sufficiently integrated into predictive and relational modelling, then another's state may alter the transformation by which possible futures become behaviour.

A distressed other could change:

- attention;
- prediction;
- memory retrieval;
- candidate generation;
- trajectory evaluation;
- commitment;
- action.

A promise could alter those dynamics differently. Trust, responsibility, attachment and dependence could become durable structures that continuously reshape what futures are behaviourally available.

Ethical behaviour would then not merely result from **consulting an ethical objective**. It could become part of the organism's learned sensorimotor organization.

The other organism's continuation would matter because the machinery by which the world is transformed into action has learned that it matters.

This remains an architectural aspiration, not evidence that REE has already achieved it.

---

## 8. Temporary coordinated representational transformations fit inside this model

The accompanying thought on **Temporary Coordinated Representational Transformations** can be understood as describing one mechanism by which the predictive sensorimotor reflex acquires flexibility.

The organism does not need one fixed representation of the world that supports every possible behaviour. Instead, the recurrent transformation can temporarily reorganize available information according to context, bodily condition, prediction, candidate action, remembered history, active constraints and other directive structures.

The two thoughts therefore occupy different explanatory levels.

### Predictive sensorimotor transformation

Describes **what the overall organism is doing**:

```text
sensation -> predictively mediated transformation -> action
```

### Temporary coordinated representational transformation

Describes **one possible way the transformation becomes context-sensitive and computationally tractable**.

The second sits inside the first.

Neither necessarily adds a new architectural claim. They provide alternative representations of machinery REE already contains or intends to contain.

---

## 9. Why this representation may help with the current V3 problem

The reframing produces a practical diagnostic question.

Suppose resource direction is substantially recoverable from `z_world`, as V3-EXQ-978 found at its tested operating point, but the organism still fails to forage competently.

A module-oriented description asks:

> Which component is broken?

- encoder?
- world model?
- E1?
- E2?
- E3?
- goal system?

The transformation-oriented description asks instead:

> **At what point does a difference in sensory state that ought to produce a difference in action cease producing that difference?**

That gives a continuous experimental chain:

```text
resource left vs right
        ↓
Delta z_world
        ↓
Delta E1/E2
        ↓
Delta predicted candidate consequences
        ↓
Delta E3 dynamics
        ↓
Delta P(action)
```

If food being left rather than right is represented in `z_world`, the next question is whether it produces appropriately different predicted futures.

If it does, examine whether those differences reach E3.

If they reach E3, examine whether they produce appropriately different candidate dynamics.

If they do, examine why the resulting action probabilities remain wrong.

The diagnostic target becomes the **transfer of behavioural discrimination through the transformation**, rather than the independent quality of each named module.

This may be a productive way to interrogate the current observation -> `z_world` -> E1/E2 -> E3 difficulty.

---

## 10. A candidate experimental primitive: transformation tracing

This suggests a reusable REE diagnostic.

Choose two conditions that should produce different actions while controlling everything possible except the relevant distinction.

For example:

```text
S^L = resource left
S^R = resource right
```

Then trace the distinction through successive stages:

```text
D0 = d(S^L, S^R)
D1 = d(z_world^L, z_world^R)
D2 = d(E1^L, E1^R)
D3 = d(predicted trajectories^L, predicted trajectories^R)
D4 = d(E3^L, E3^R)
D5 = d(P(A|L), P(A|R))
```

The important quantity is not necessarily absolute representational distance.

It is whether the distinction continues to point in a **behaviourally appropriate direction**.

The diagnostic question becomes:

> At which transformation does the sign, ordering or usefulness of the sensory distinction disappear?

This may provide a more direct route to competence than repeatedly increasing latent supervision.

---

## 11. The super-complex reflex is recurrent, not feed-forward

The word "reflex" is misleading if it implies one pass.

REE's reflex would be recurrent.

Candidate actions modify predictions. Predictions modify representational state. Memory modifies predictions. Conflict changes how long processing continues. Control state changes gain and eligibility. The resulting changed state alters which action is now favoured.

Schematically:

```text
S -> R1 -> P1 -> C1 -> R2 -> P2 -> C2 -> ... -> A
```

where `R` is transformed internal state, `P` predictive development and `C` competition/control state.

The system can therefore "think" without requiring thought to be a fundamentally different event from perception and action.

Thinking is what happens when the reflex becomes sufficiently recurrent, predictive and internally simulatory that substantial transformations occur before overt action.

---

## 12. Planning may be internalized action

Planning need not be a wholly separate cognitive faculty.

It can be understood as allowing the sensorimotor transformation to operate on **predicted sensory consequences rather than immediately acting on the external world**.

Ordinary action:

```text
S_t -> A_t -> S_(t+1)
```

Planning:

```text
S_t -> predicted A1 -> predicted S1 -> predicted A2 -> predicted S2 -> ...
```

before an overt `A_t` is committed.

A sufficiently capable predictive system can therefore turn the sensorimotor loop inward temporarily.

This is not different in kind from the loop. It is the loop recursively applied to internally generated possibilities.

E1/E2 naturally occupy part of this role in REE.

---

## 13. Intelligence may be depth and flexibility of transformation

This perspective also offers a useful description of increasing intelligence.

A simple reflex has:

- shallow temporal depth;
- little contextual modulation;
- minimal internal state;
- a relatively fixed transformation.

A more capable organism has:

- deeper prediction;
- richer internal state;
- memory-dependent transformations;
- candidate counterfactuals;
- context-sensitive representations;
- uncertainty-sensitive processing;
- reusable learned structure;
- increasingly complex models of self and others.

Intelligence may therefore partly consist in increasing the **depth, flexibility and conditionality of the sensorimotor transformation** while retaining the ability to collapse that complexity into timely coherent action.

The hard problem is not generating representations for their own sake. It is ensuring that rich internal structure continues ultimately to constrain behaviour.

---

## 14. A useful engineering warning

This reframing cautions against a recurring architectural temptation.

When behaviour is deficient, it is easy to create another explicit cognitive object:

- a better goal;
- another world latent;
- an explicit planner;
- a new memory type;
- another decision score;
- an additional supervisor.

Sometimes that is necessary.

But before adding machinery, REE should ask:

> **Is the relevant computation genuinely absent, or is existing information failing to transform appropriately into action?**

V3-EXQ-978 makes this question concrete. Additional directional resource supervision did not materially improve behaviour at the tested operating point even though directional information was already substantially represented.

The missing ingredient may therefore lie in the transformation from represented information to action rather than in another representation. That remains a hypothesis to test, not a conclusion already earned.

---

## 15. Relationship to REE's existing claims

This thought does not require claiming that:

- frontal cortex is literally a sensorimotor transformation matrix;
- hippocampus only chains trajectories;
- basal ganglia merely modulates gain;
- goals do not exist;
- cognition is reducible to a simple feed-forward reflex;
- or REE's current E1/E2/E3 implementation already realizes this account.

Those would be additional empirical claims.

The thought is instead an **equivalent or near-equivalent representation of the existing REE programme**.

The familiar decomposition remains useful. E1 can still be called a predictive substrate. E2 can still be called a forward predictor. E3 can still be described as trajectory selection. Hippocampal machinery can still be treated as memory. Goal machinery can still be implemented explicitly.

The reframing simply reminds us that, from the perspective of the whole organism, these mechanisms jointly implement:

> **the transformation of sensed organism/world state into adaptive action through temporally extended prediction.**

---

## 16. Why an equivalent representation can still produce scientific progress

A mathematical or computational system can become easier to solve when represented in different coordinates even though the underlying system has not changed.

The same may be true here.

The architectural representation foregrounds modules:

```text
representation -> prediction -> selection
```

The transformation representation foregrounds propagated distinctions:

```text
sensed distinction -> predicted consequence distinction -> action distinction
```

Nothing fundamental has necessarily been added, but different failure modes become visible.

If the reframing is useful, its success should not be measured by whether it generates another architectural component. Its success should be measured by whether it helps identify why the current organism fails and suggests cleaner experiments or simpler implementations.

A useful summary is:

> **Nothing new has necessarily been added to REE. We may simply have rotated it until the current failure becomes easier to see.**

---

## 17. Concise formulation

> **REE can be understood as a recurrent predictive sensorimotor transformation: sensed world and organism state are transformed through learned prediction, memory and counterfactual action into behaviour. E1, E2, hippocampal, frontal-like, control and E3/basal-ganglia-like machinery are specialized contributors to this transformation rather than necessarily independent cognitive stages. Goals, plans, maps and selections are useful higher-level descriptions of patterns within these dynamics.**

The diagnostic consequence is:

> **When behaviour fails despite the relevant information being represented, trace where the sensory distinction stops producing the appropriate difference in predicted consequences and action dynamics before adding another representation.**

---

## 18. Closing thought

Nothing in this reframing necessarily changes REE.

It changes the direction from which REE is viewed.

The brain begins with sensation and ends, repeatedly, in action.

Between them it has learned to insert time.

It predicts the world.

It predicts the organism inside the world.

It predicts how actions could change both.

Memory allows those predictions to cross what is absent.

Temporary representational transformations make different relationships available when different computations are required.

Competition and recurrent gating allow some predicted futures to acquire behavioural control.

The resulting system can accumulate enough depth that its behaviour looks very far removed from a reflex.

But perhaps the continuity remains:

> **Cognition is what happens when the sensory–action transformation learns to predict, remember and rehearse itself before it moves.**

REE may be an attempt to build that transformation deliberately.

This is saved as a conceptual lens, not as evidence for or automatic promotion of any new REE claim.