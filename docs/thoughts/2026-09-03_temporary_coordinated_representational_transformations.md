# Thought: Temporary Coordinated Representational Transformations

Status: processed
Intake: evidence/planning/thought_intake_2026-09-03_temporary_coordinated_representational_transformations.md
Claims registered: none (already owned by MECH-517/518, MECH-359, ARC-065 GAP-A; experimental content routed to the V3-EXQ-978 autopsy)

Original status line: exploratory architectural thought / conceptual reframing — not an implementation decision or promoted REE claim

Date: 2026-09-03

## Trigger

This thought arose while interpreting V3-EXQ-978 and asking why competent foraging remains poor even when directional resource information is substantially recoverable from the current world representation.

V3-EXQ-978 is important here as a diagnostic trigger, not as proof of the proposal below. At the tested operating point, the dedicated directional resource-field supervision head learned its own target, but enabling that supervision did not materially change `z_world` decoding or foraging competence. Directional resource information was already strongly linearly decodable from `z_world` with the field loss OFF (roughly R² 0.71 at sense time and 0.858 on the encoder path). The formal experiment nevertheless remained mixed, with the associated claim support unknown. It therefore weakens a simple story in which observation contains direction, `z_world` discards it, and behaviour fails for that reason; it does not establish where the remaining bottleneck lies.

The useful distinction is:

> Information being present in a representation is not the same as that information being present in the form required by the computation currently being performed.

A creature may therefore contain the information required for an action while still being unable to act appropriately from it.

---

## 1. The problem with treating one latent as the decision representation

A rich world representation has to preserve enough information to support many possible future computations. A decision, by contrast, needs only a small subset of those relationships, and it may need them expressed in a very particular geometry.

The same scene may need to be represented differently when the organism is:

- eating;
- escaping;
- exploring;
- returning to a remembered location;
- checking an uncertainty;
- protecting another agent;
- or deciding whether to persist with a costly trajectory.

A universal `z_world` that is required to make every useful variable immediately readable by every downstream process risks becoming an increasingly near-lossless vector rather than a useful predictive substrate.

A different possibility is:

1. sensory and internal information is preserved in a rich substrate;
2. current context, organism state, memory and candidate action temporarily reorganize that information;
3. the resulting representation makes the relationships needed for the present computation especially accessible;
4. action selection operates over these temporary decision-relevant transformations rather than over a single fixed world representation.

This is not necessarily a proposal for another module. It is a different way of understanding how the existing predictive machinery may have to interact.

---

## 2. Temporary coordinated representational transformations

The phrase **temporary coordinated representational transformations** seems preferable to the earlier image of a discrete "theta package".

A package sounds like an object assembled in one place and handed to another. That may be too literal and too sequential. The biologically and computationally plausible process is more likely distributed and recurrent: current task state alters gain and retrieval; memory changes prediction; candidate simulation changes what is relevant; conflict changes control state; the altered state drives another representational pass.

Theta-band coordination may eventually be relevant to how some such processes are synchronized, but this thought does not require a literal theta packet and should not hard-code theta as a universal carrier.

A minimal conceptual notation is:

```text
R_(t,a) = T(S_t, D_t, a)
```

where:

- `S_t` is the rich currently available substrate: sensory state, predictive state, body state, memory, learned structure and other available information;
- `D_t` is the currently active configuration of structures that bias how that substrate is used;
- `a` is a candidate action or trajectory where candidate conditioning is relevant;
- `T` is the coordinated transformation produced by the current system dynamics;
- `R_(t,a)` is a temporary decision-relevant representation.

`R_(t,a)` is not intended to be a miniature reconstruction of the world. It is the representation of the organism–world relationship that makes the distinctions relevant to this candidate or decision easy to use.

---

## 3. Goals participate, but "goal" is probably too narrow

The original intuition was that goals might query the machinery so that the information arriving at action selection was represented in the right form.

That remains useful, but "goal" may be too narrow and too agent-like as the organizing concept.

A system may contain persistent or transient structures that systematically alter:

- what is represented;
- what is retrieved;
- what is predicted;
- what is compared;
- what becomes salient;
- which candidates are generated;
- which representational dimensions become separable;
- which consequences are admissible;
- and when commitment becomes possible.

A desired state is only one kind of thing that can do this.

For discussion, call the broader class **directive structures**.

This term is deliberately provisional. It should not yet become an ontology, module class or implementation requirement. It means only: an internal structure whose current activation or persistence systematically biases the representation-to-action transformation.

Possible examples include:

- an attractive state or object;
- a threat;
- a rule;
- an obligation;
- uncertainty;
- a social commitment;
- learned task context;
- an active model of another agent;
- a hypothesis under examination;
- prediction error;
- an affordance;
- a prohibition;
- a self-model constraint;
- a developmental prior;
- information hunger or exploratory pressure.

Some of these may eventually prove to be different computational species. Some may reduce to the same machinery. The point is not to classify them prematurely. The point is that **desired outcomes are unlikely to be the only persistent structures capable of organizing representation and action**.

---

## 4. A goal need not have one representation

Even where a recognizable goal exists, it need not have a single canonical form.

"Get food" might appear at different moments as:

- a homeostatic drive;
- an incentive value attached to an object class;
- a remembered resource location;
- a spatial or latent attractor;
- a current subgoal;
- a superordinate continuation requirement;
- an episodic cue;
- or a relational structure such as "food available after passing this obstacle".

There is no obvious need for a meta-controller that asks, "What form shall my goal take now?"

A more natural possibility is that several reusable structures coexist and the current organism/world state changes which of them gains functional influence. The world representation helps select the useful expression of the directive state, while the directive state changes which relationships in the world representation become useful.

Schematically:

```text
world/context -> directive retrieval and gating
directive state -> world retrieval and gating
candidate simulation -> modifies both
```

The relevant representation can therefore emerge from mutual constraint rather than from a fixed goal querying a fixed world model.

---

## 5. The deeper represented object may be a relationship

This suggests that "world representation" and "goal representation" may themselves sometimes be the wrong primitive decomposition.

For choice, the important object may be a relation among:

- organism state;
- world state;
- history;
- candidate action;
- predicted trajectory;
- current constraints;
- and active directive structures.

A decision is not usually about the world alone or the desired state alone. It is about what this organism can do, from this state, through this possible trajectory, under these constraints, with these consequences.

Temporary coordinated transformation may therefore construct a useful representation of **the current organism–world–candidate relationship**, not simply combine two static vectors labelled WORLD and GOAL.

---

## 6. Avoiding a representational combinatorial explosion

This framing opens an obvious can of worms. If every task could have its own representation, REE could degenerate into an unlimited collection of bespoke representational types.

That is not the proposal.

The more plausible constraint is compositional reuse:

- maintain rich reusable latent structure;
- maintain reusable contextual, motivational, relational and control structures;
- temporarily compose, rotate, gate or reweight those structures;
- allow the current computation to expose the dimensions that matter now.

Mixed representations are therefore a feature, not necessarily a failure. A representation need not have one variable per semantic concept. What matters is whether the geometry can be temporarily transformed so that the required distinction becomes usable by a sufficiently simple downstream computation.

The useful target may not be maximal universal decodability. It may be **conditional behavioural accessibility**.

---

## 7. Protected channels are still needed

Task- or goal-conditioned representation creates a danger: the system could make inconvenient information disappear whenever it conflicts with what it currently wants.

A robust architecture therefore probably needs a distinction between transformable content and signals that retain privileged access to control or veto machinery.

Candidate protected channels may include:

- harm or nociceptive signals;
- basic homeostatic viability signals;
- hard safety/veto pathways;
- severe uncertainty;
- large prediction mismatch;
- possibly agency/control loss signals;
- and, at later developmental stages, sufficiently entrenched social or constitutional constraints.

This is not yet a claim that these exact channels require a particular implementation. It is a design warning: representational flexibility must not become motivated blindness.

---

## 8. What V3-EXQ-978 now permits us to ask

V3-EXQ-978 leaves at least three broad explanations open.

### A. Information loss

The needed directional information is absent from the relevant internal representation.

The experiment weakens the simplest form of this hypothesis because directional resource information was already substantially linearly decodable from `z_world`.

### B. Consumer/readout/learning failure

The information is in an adequately usable form, but the current downstream consumer has simply failed to learn the appropriate mapping from that representation to action.

This is the most important simple alternative and should be tested before introducing richer architecture.

### C. Representational mismatch

The information is technically recoverable, but the current geometry does not make the relationships needed by prediction and action selection sufficiently accessible under the actual learning dynamics. A task-, context- or candidate-conditioned transformation could improve behavioural accessibility without increasing total information content.

V3-EXQ-978 does **not** distinguish B from C.

That distinction is now experimentally valuable.

---

## 9. Minimal experiments suggested by the reframing

### Experiment 1: frozen-latent simple action reader

Freeze the existing `z_world` and train the simplest sensible supervised/oracle action adapter on a tightly controlled directional task.

Question:

> Can an uncomplicated consumer turn the existing representation into competent directional behaviour?

If yes, the current V3 bottleneck may be ordinary downstream training/readout rather than a need for representational transformation.

If no, despite strong generic decoding, representational mismatch becomes more interesting.

### Experiment 2: goal- or task-conditioned geometry

Present equivalent sensory scenes under two different task or directive conditions.

Measure whether conditioning changes action-relevant separability while preserving the same underlying sensory information.

The key outcome is not merely whether the latent changes, but whether the distinction required by the current action becomes easier to read and use.

### Experiment 3: candidate-conditioned representation

For the same current state, condition the predictive representation separately on candidate actions.

Ask whether candidate-specific transformation produces clearer differences in predicted consequences than evaluating candidates against a single shared static representation.

### Experiment 4: geometry change without information gain

Construct or learn a transformation that preserves approximately the same recoverable information while rotating/reweighting the geometry.

Test whether competence tracks decision-relevant separability rather than global decoding score.

If behaviour improves without meaningful information gain, that would be particularly informative.

### Experiment 5: conflict-triggered representational revision

When candidate actions remain closely matched, allow another recurrent pass in which conflict changes retrieval/gain/representation before commitment.

Test whether the second pass improves decisions specifically in ambiguous states rather than merely adding computation indiscriminately.

---

## 10. Ways this thought could be wrong

This framing should be allowed to disappear if simpler explanations win.

It is weakened if:

- a fixed simple reader from current `z_world` immediately solves the competence problem;
- ordinary training, scaling or objective correction solves the bottleneck;
- conditioning changes representations but does not improve action-relevant separability or competence;
- candidate-conditioned representations offer no useful distinction beyond the existing pipeline;
- recurrent conflict-triggered re-representation adds no benefit;
- or the same behaviour is explained more parsimoniously by a local implementation defect.

In particular, a successful simple reader would be a useful result, not a disappointment. This thought is intended to expose experiments, not to demand architectural complexity.

---

## 11. Relationship to current REE machinery

REE already contains much of the machinery from which such transformations could emerge:

- a predictive world representation;
- E1 temporal dynamics;
- E2 action-conditioned prediction;
- hippocampal/path memory;
- explicit and latent goal machinery;
- residue;
- body and viability signals;
- E3 trajectory dynamics;
- control/gain/precision mechanisms;
- developmental state;
- and eventually richer social representations.

The thought therefore does not require adding a foreign executive that assembles a decision packet.

Its architectural implication is primarily about **interfaces and dynamics**: do these systems jointly transform what the organism already represents into a form in which the current decision becomes easy enough to learn and express?

---

## 12. Candidate hypothesis for later digestion

The following is a candidate formulation only. It should not be promoted merely because this thought has been saved:

> REE decision competence depends not only on preservation of relevant information in its predictive representations, but on temporary coordinated transformations that make task-, context- and candidate-relevant relationships readily usable by action-selection machinery. Goal representations are one subset of a broader class of directive structures capable of biasing these transformations.

A stronger extension is:

> Persistent directive structures need not encode desired outcomes. They may encode rules, threats, contexts, uncertainties, commitments or relational constraints that alter what information is retrieved, emphasized, simulated or admitted into candidate evaluation.

The central V3 prediction worth testing is narrower:

> Poor behaviour despite strong generic decoding may track failure of decision-time behavioural separability more closely than failure of raw information preservation.

That prediction should compete directly with the simpler fixed-reader explanation.

---

## 13. Final formulation

REE need not decide from a fixed representation of a fixed goal in a fixed representation of the world.

Persistent and transient directive structures may interact with predictive state, memory, bodily condition and candidate actions to produce **temporary coordinated representational transformations**. These transformations make particular relationships salient and computationally accessible for the decision currently being made. Selection and conflict can feed back into that process until sufficient commitment is reached.

The important diagnostic question then becomes:

> Not merely: does the creature contain the information?
>
> But: can the creature temporarily bring what it contains into the form in which this decision can be made?

This is currently a conceptual reframing and experiment-generating lens, not an additional REE claim.