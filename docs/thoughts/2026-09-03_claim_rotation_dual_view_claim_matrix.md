# Thought: Claim Rotation and Dual-View Claim Matrices

Status: processed
Intake: evidence/planning/thought_intake_2026-09-03_claim_rotation_dual_view_claim_matrix.md
Claims registered: GOV-ROTATE-1

Original status line: epistemic/governance tooling thought — not a new scientific claim and not a second independent evidence ledger

Date: 2026-09-03

## 1. Trigger

The preceding two thoughts suggest that the same REE machinery can be represented in more than one useful coordinate system.

One representation emphasizes architecture and named mechanisms:

```text
observation -> z_world -> E1/E2 -> E3 -> action
```

Another emphasizes the transformation of behaviourally meaningful distinctions:

```text
sensed distinction
    -> internal transformation
    -> predicted consequence distinction
    -> action distinction
```

These may describe substantially the same underlying scientific commitments while making different experimental questions obvious.

This raises a governance possibility: REE's claim system may benefit from holding **multiple explicit representations of the same canonical claim-space**.

The purpose would not be to generate duplicate truths. It would be to make difficult claims easier to reason about and easier to turn into experiments.

---

## 2. Two coordinate systems over the same claim-space

The current REE claim matrix is naturally architectural and functional. Claims concern things such as:

- E1;
- E2;
- E3;
- world representations;
- memory;
- goals;
- residue;
- control;
- developmental mechanisms;
- and relations among those components.

That is useful because implementation is organized around these systems.

A second view could represent many of the same commitments in transformation coordinates:

```text
sensory distinction
    -> represented distinction
    -> predicted consequence distinction
    -> candidate/action distinction
    -> behavioural effect
```

Neither view is intrinsically more true. They foreground different relationships.

A rough mapping might look like this:

| Architectural / functional view | Transformation view |
| --- | --- |
| `z_world` preserves directional information | Resource-direction distinctions remain behaviourally discriminable after encoding |
| E1 predicts future state | A current distinction propagates into temporally extended consequence distinctions |
| E2 evaluates action-conditioned futures | Changing the candidate action changes the predicted transformation appropriately |
| Hippocampal memory supports planning | Absent or intermediate states can be chained into the current sensorimotor transformation |
| E3 selects trajectories | Appropriate candidate distinctions acquire differential behavioural control |
| Goal machinery represents wanting | Persistent internal state biases which sensory -> future -> action relationships dominate |
| Residue alters candidate evaluation | Prior consequences modify subsequent propagation through the transformation |

The right-hand column does not automatically add scientific content. It often simply restates what the left-hand claim would have to mean in terms of information becoming behaviour.

---

## 3. V3-EXQ-978 as an example of claim rotation

The recent directional-resource experiments show why this could help.

One architectural representation of the foraging failure was approximately:

> Perhaps observation contains directional resource information, but `z_world` discards it before downstream systems can use it.

That representation naturally suggested SD-018: directly supervise a directional resource-field head and test whether strengthening that information in `z_world` improves competence.

V3-EXQ-978 then found that directional resource information was already substantially linearly decodable from `z_world` even in the OFF condition, while the extra supervision did not materially change `z_world` or behaviour at that operating point. The formal result was mixed and did not identify the actual bottleneck.

Rotate the same problem into transformation coordinates:

> Does changing the sensed resource direction ultimately cause the appropriate change in action tendency, and where in the transformation does that relationship disappear?

That representation immediately suggests a different family of experiments:

```text
resource left vs right
    -> z_world difference
    -> E1/E2 difference
    -> predicted candidate consequence difference
    -> E3 difference
    -> action-probability difference
```

The scientific object has not necessarily changed.

The representation has changed, and with it the obvious next action.

---

## 4. The crucial governance rule: one canonical truth state

A dual-view matrix must **not** become two independent claim matrices with separate truth states.

That would create several risks:

- the same evidence could be counted twice;
- two representations of one proposition could acquire contradictory promotion states;
- apparent claim support could grow merely because the same idea had been reworded;
- uncertainty could be hidden by moving between formulations;
- and the claim registry could multiply without adding empirical content.

A safer structure is:

```text
C_i <-> R_i1, R_i2, R_i3, ...
```

where:

- `C_i` is the canonical scientific claim;
- each `R_ij` is an alternative representation or operational view of that claim;
- evidence and claim status remain attached to the canonical claim and its actual experiments;
- representations help generate diagnostics and interventions but do not independently become "supported" unless they introduce genuinely new propositions.

The representation layer is therefore epistemic tooling, not an evidence multiplier.

---

## 5. What an alternative representation could carry

An alternative view could be useful even without its own truth value.

For example, each representation could carry:

- **view name** — architectural, transformation, behavioural, developmental, biological analogue, etc.;
- **statement** — the claim expressed in those coordinates;
- **diagnostic question** — what would we ask if reasoning from this view?;
- **operational observables** — what measurable differences should appear?;
- **intervention points** — where can the system be perturbed?;
- **expected signatures** — what pattern would be informative?;
- **falsifier or failure pattern** — what would make this representation unhelpful or reveal an extra assumption?;
- **related claims** — which canonical claims become adjacent in this view.

A lightweight schema could look like:

```yaml
canonical_claim_id: MECH-XYZ
representations:
  - view: architectural
    statement: ...
    diagnostic_question: ...
    observables: [...]
    intervention_points: [...]
    falsifier: ...
  - view: transformation
    statement: ...
    diagnostic_question: ...
    observables: [...]
    intervention_points: [...]
    falsifier: ...
```

Evidence would remain attached to the canonical claim and experiment records, not copied into each representation.

This schema is illustrative only. It should not be implemented merely because the thought exists.

---

## 6. When a translation reveals a genuinely new claim

There is an important exception.

Sometimes translating a claim into another representation exposes an assumption that was hidden in the original wording.

For example:

> E3 uses `z_world` to select trajectories.

might be rotated into:

> A behaviourally relevant directional distinction in `z_world` is preserved through candidate prediction and reverses the corresponding action preference when the sensory direction reverses.

That second statement may contain additional empirical commitments that were not actually entailed by the first claim.

If so, it should **not** be treated as merely another phrasing.

The translation has discovered a new proposition, and that proposition may deserve its own canonical claim or explicit subclaim.

The governance rule should therefore be:

> Alternative representations may restate a claim, but they may not smuggle additional empirical content into the same truth state.

Claim rotation is useful partly because it can reveal these hidden assumptions.

---

## 7. A forge heuristic: when a claim stalls, rotate it

This suggests a simple scientific heuristic for the forge:

> **When a claim stalls, rotate it.**

Do not immediately spawn more variants of the same experiment in the same conceptual coordinates.

Instead ask whether the claim can be represented from another useful perspective.

Possible views include:

### Architectural view

Which component, interface or mechanism is supposed to perform the function?

### Transformation view

Which behaviourally relevant distinction should propagate from input to consequence to action, and where does it cease to do so?

### Behavioural view

What controlled environmental perturbation should reliably change the creature's behaviour if the claim matters?

### Developmental view

What experience should cause the competence to appear, stabilize or reorganize over development?

### Biological-analogue view

What computational role does the biological analogue suggest, and does that expose a missing mechanism or a misleading decomposition?

These are not mandatory views and need not all exist for every claim.

The purpose is not to create a larger ontology. It is to find a representation in which the next discriminating experiment becomes clearer.

---

## 8. Claim rotation as experiment generation rather than claim generation

This distinction is important.

The forge should not interpret "rotate the claim" as:

> produce five semantically similar claims and test all five.

It should instead mean:

> hold the canonical scientific uncertainty fixed while changing the representation used to search for a useful intervention or observable.

A successful rotation should ideally reduce experimental branching.

For example, an architectural problem that suggests ten possible broken modules may become a transformation-tracing problem with a sequential localization strategy. Conversely, a vague transformation failure may become easy to intervene on once rotated back into a specific module/interface representation.

The views can therefore constrain one another.

---

## 9. Relation to temporary coordinated representational transformations

There is a useful recursion here.

The accompanying scientific thought proposes that REE itself may sometimes need to transform the representation of available information so that the relationships required for a current decision become accessible.

The scientific process studying REE may face the same abstract problem.

The claim registry contains information.

Experiments contain information.

The architecture contains information.

Yet the next scientific action may remain unclear because the current representation does not expose the useful relationship.

REE science can therefore deliberately transform its representation of the same evidence until a discriminating experiment becomes easier to see.

This does not imply that scientific reasoning and REE cognition are mechanistically identical. The analogy is methodological:

> changing representation can change which actions become easy to derive without changing the underlying information.

---

## 10. A possible workflow

If this thought survives digestion, a conservative workflow might be:

1. Keep the existing canonical claim matrix unchanged as the authority for evidence state.
2. Permit claims to acquire one or more explicitly labelled alternative representations.
3. Generate those representations only when they improve diagnosis, experiment design or interpretation.
4. Never duplicate evidence simply because it supports two representations of the same claim.
5. During rotation, check whether the new wording adds an empirical assumption.
6. If it does, split that assumption into a genuine subclaim rather than silently inheriting the parent's evidence.
7. Record which representation generated an experiment so later archaeology can show why that experiment existed.
8. Evaluate whether claim rotation actually reduces stalled claims or experimental branching before expanding the machinery.

This is deliberately lighter than constructing a second governance stack.

---

## 11. What would make this idea unhelpful

The proposal should not be retained merely because the recursion is elegant.

It is unhelpful if:

- alternative views merely paraphrase claims without changing experimental reasoning;
- maintaining the mappings creates more governance overhead than useful science;
- the existing claim system already supports equivalent diagnostic decompositions cleanly;
- alternative representations create ambiguity about canonical evidence state;
- or the forge begins generating representation variants as paperwork rather than using them selectively to resolve uncertainty.

The success criterion is practical:

> Does rotating a stalled claim produce a clearer, smaller or more discriminating next experiment?

If not, the machinery is unnecessary.

---

## 12. Concise formulation

> **REE may benefit from maintaining multiple explicit representations of the same canonical scientific claims. The canonical claim retains a single evidence and promotion state, while alternative architectural, transformation, behavioural, developmental or biological views expose different observables and interventions. When a claim stalls, rotating its representation may reveal a simpler next experiment without multiplying claims or evidence.**

The safeguard is equally important:

> **Same claim, multiple views, one truth state. If a new view introduces new empirical content, that content becomes a new claim rather than inheriting the old claim's evidence.**

---

## 13. Closing thought

The scientific process may need to do to REE's own claims what REE may be doing to the world:

> change the representation until an appropriate action becomes possible.

Or, as a compact forge rule:

> **When a claim stalls, rotate it.**

This is currently a governance and scientific-reasoning thought only. It should not create a second evidence ledger or any new claim automatically.