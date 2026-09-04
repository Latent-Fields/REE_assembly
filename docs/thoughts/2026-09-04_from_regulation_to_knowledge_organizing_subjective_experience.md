# From Regulation to Knowledge: Organizing Subjective Experience

Status: thought / organising hypothesis  
Date: 2026-09-04

## Core question

A major current frontier in REE is the organization of `z_world`: how continuous, partial, uncertain experience becomes an internal representation that can support prediction, memory, planning, agency, development, and later social understanding.

The usual framing asks: **how should an agent represent the external world?**

This thought proposes a different starting point:

> **How does a machine organize experience according to its own enduring regulatory constraints?**

The claim is not that the external world is unreal or secondary in ontology. It is that, for an organism, knowledge of the world may be developmentally downstream of regulation.

## Proposed developmental ordering

A compact version is:

**machine → regulation → interaction → organized experience → knowledge**

The machine comes first. Before it can know, it already has structure, limits, needs, vulnerabilities, effectors, sensors, and regulatory dynamics. It functions before it knows that it functions.

This is visible in infants: physiological and behavioural regulation precede explicit knowledge, reflective self-models, and conceptual world models. The infant acts, is soothed, is distressed, orients, feeds, withdraws, approaches, and gradually differentiates regularities from these interactions.

On this view, a mature world model is not the primitive. It is an achievement of development.

## What, then, are the invariants?

An initial intuition was that the relevant invariants might be emotions, harm, safety, agency, attachment, and related self-relevant variables. A refinement is needed: emotions may be better treated as reports, regulators, or compressed signals concerning deeper organismic constraints rather than as the ultimate invariants themselves.

Candidate deeper constraints include:

- continued existence;
- bodily or structural integrity;
- regulation of internal state;
- vulnerability to harm;
- ability to effect change;
- preservation of agency or control;
- attachment or dependence relations;
- uncertainty about the causes of important outcomes.

The internal world may become organized around relations between external regularities and these enduring constraints.

## World model as relation-to-self rather than detached map

This does **not** imply that every representation explicitly encodes “me”. A useful world model can become increasingly abstract, objective, and portable.

The proposal is developmental: the machine has no route to a detached world model except through interaction generated and constrained by what matters to the machine. The organism does not begin by learning an objective universe and later discover relevance. Relevance is present from the beginning because the machine is already a regulated physical system.

Thus the earliest useful distinction may not be “what exists?” but something closer to:

- what changes me;
- what I can change;
- what predicts harm or benefit;
- what is controllable;
- what persists;
- what belongs together;
- what should be preserved, avoided, approached, or investigated.

Over development, those distinctions can support progressively less self-bound knowledge.

## Why this matters for `z_world`

The `z_world` problem may therefore be mis-specified if treated primarily as a compression or feature-learning problem.

A good latent representation is not merely one that reconstructs observations. It must retain the distinctions that matter for the organism's ability to predict and regulate itself across time.

This gives a possible interpretation of recent REE difficulties around the observation → `z_world` → E1/E2 interface: failures may arise because the representation is technically compact yet discards distinctions that are behaviourally or regulatorily meaningful.

The recent need to preserve directional resource information is a concrete example of this general class of failure. If information relevant to action, harm, benefit, opportunity, or controllability is collapsed too early, later prediction cannot recover it.

## Clinical clue: common ground under divergent world models

A suggestive clinical observation comes from communication with people who are severely psychotic. Shared agreement about external facts can become fragile, yet communication often remains possible through more basic anchors such as:

- fear;
- safety;
- harm;
- agency;
- loss of control;
- attachment;
- threat;
- relief.

This is not evidence that psychosis proves the hypothesis. It is, however, compatible with the idea that self-regulatory variables form a deeper common computational ground than explicit propositional world models.

If so, very divergent high-level beliefs may remain intelligible because they are still organized around relatively conserved organism-level concerns.

## Red-team challenges

### 1. The universe comes before the self

True ontologically. But the claim concerns representation and development, not metaphysics. The universe can pre-exist the organism while the organism's access to it is necessarily conditioned by its own sensors, actuators, needs, and regulatory structure.

### 2. Infants do not possess sophisticated selves

Also true, and this strengthens the refined version. A narrative or conceptual self need not come first. The machine's regulatory organization can precede explicit self-representation. The “self” may initially be nothing more than the persistent pattern of constraints and controllable consequences around which experience becomes organized.

### 3. Mathematics and abstract knowledge are not reducible to self-interest

The hypothesis need not claim that mature knowledge remains reducible to its developmental origin. Once learned, abstractions can become detached from immediate organismic regulation. The question is how a learner gets to the point where such abstraction is possible.

### 4. Perhaps control variables, not the self, are primary

This is probably a stronger formulation rather than a refutation. The machine's regulatory variables come first; an enduring self-model may emerge from modelling the persistent structure that those variables define.

### 5. Compression alone might explain representation

This is an important competing hypothesis. If unsupervised compression plus generic predictive learning reliably preserves all behaviourally relevant distinctions without explicit regulatory anchoring, the regulation-first account becomes less necessary.

### 6. Evolution may pre-wire useful world structure

Yes. A machine can inherit useful priors. But those priors themselves reflect regulatory success in prior evolutionary history. In REE, built-in architecture and developmental learning should therefore be distinguished rather than conflated.

## Stronger formulation

The stronger and less anthropocentric formulation is:

> **Constraints come first; meaning follows.**

A machine is already a structured, vulnerable, acting system before it knows anything. Its earliest representational organization should therefore reflect what its structure makes consequential. A self-model and a world model can then co-develop from repeated prediction and control of those consequential interactions.

## Consequences for REE architecture

If this thought is right, several architectural implications follow.

### `z_world` should preserve regulatorily relevant distinctions

The representation should be tested not only for reconstruction or prediction but for whether it preserves variables needed to distinguish:

- harm from benefit;
- controllable from uncontrollable change;
- self-caused from externally caused outcomes;
- approach opportunities from threats;
- persistent resources from transient cues;
- relations that matter to future regulation.

### Development should shape representational ontology

Development may not merely fill a fixed representation with better estimates. It may alter what distinctions exist at all. Categories should be allowed to reorganize as the machine learns which distinctions are useful for regulation.

### Replay and sleep become representational reorganization

Replay is not only memory consolidation. It may be a mechanism by which experiences are reclassified, linked, and reweighted according to their consequences for the organism, allowing latent structure to change without immediate action demands.

### Agency becomes foundational

The distinction between what the machine caused, what it could have caused, and what happened independently may be central to organizing experience. Agency is therefore not an optional late feature of the world model; it may be one of the axes along which the model is first carved.

### Knowledge is selective incorporation

Not every observation should become durable knowledge. Enduring incorporation should depend on usefulness for prediction, regulation, causal understanding, or future action.

## Testable predictions in REE

1. Representations trained only for sensory reconstruction should underperform representations additionally constrained to preserve organism-relevant variables when evaluated on downstream adaptive behaviour.
2. Developmental curricula in which regulatory consequences are available before explicit task labels should produce more robust generalization than equivalent curricula built around arbitrary labels alone.
3. Perturbing or hiding variables that affect the agent but not the raw external scene should disproportionately disrupt later world-model organization if regulation is foundational.
4. Agency and controllability signals should become organizing axes in latent space even when not explicitly labelled, provided the developmental environment makes them consequential.
5. Replay that prioritizes surprising regulatory outcomes should change future categorization and prediction more than replay matched only for perceptual novelty.
6. Agents with equivalent sensory statistics but different vulnerabilities or affordances should develop systematically different internal organizations of the same environment.
7. If the hypothesis is wrong and objective scene structure is sufficient, differences in machine-level vulnerability should have little effect on learned latent organization once observations are matched.

## Experimental programme suggested by the thought

A minimal first programme would compare alternative `z_world` objectives while holding environment and downstream architecture as constant as possible:

1. **Perceptual baseline:** reconstruction/predictive objective only.
2. **Regulatory anchoring:** add preservation or prediction of harm, benefit, resource, internal-state, and controllability variables.
3. **Agency anchoring:** add self-caused versus externally caused outcome prediction.
4. **Developmental anchoring:** introduce the above progressively rather than simultaneously.

Evaluate not only loss but:

- downstream rollout accuracy;
- behavioural competence;
- recovery from perturbation;
- counterfactual discrimination;
- latent geometry;
- transfer to altered environments;
- whether useful distinctions persist after sleep/replay.

The crucial comparison is whether regulatory constraints produce better *general organizing structure*, not merely better performance on variables directly supervised.

## Relation to cortex

There is an obvious analogy to cerebral cortex: a large distributed system transforming sensory and internal signals into progressively structured representations capable of supporting prediction, action, memory, and abstraction.

The analogy should remain functional rather than anatomical. `z_world` is not “the cortex” and REE should not assume one-to-one brain-region mappings. But the scale and difficulty of the problem may be unsurprising if the engineering problem being encountered is a miniature version of the same general computational problem: organizing a continuous stream of organism-centred experience into a coherent, reusable world.

## Open questions

- Which regulatory variables must be architecturally primitive, and which should emerge?
- How much explicit supervision is appropriate without turning the organism into a hand-coded utility machine?
- What is the minimal representation of self before a richer self-model develops?
- When should representational categories be allowed to reorganize?
- How should waking updates differ from sleep/replay updates?
- How can REE preserve ambiguity when multiple world explanations are equally compatible with regulatory outcomes?
- At what point does knowledge become sufficiently abstract to detach from immediate self-relevance?

## Working conclusion

The current `z_world` difficulty may be more than an implementation bottleneck. It may expose one of REE's central scientific questions.

The machine does not begin with knowledge of a world. It begins as a constrained, vulnerable, acting system. Regulation and interaction occur before explicit knowledge. Repeated experience can then be organized according to what those interactions reveal about persistence, harm, benefit, control, uncertainty, and relation.

A concise statement is:

> **The machine constrains things first. It functions before it knows. Experience is organized through regulation, and knowledge is what that organized experience can become.**

This should be treated as a hypothesis to test, not an axiom to protect.