Status: processed
Intake: evidence/planning/thought_intake_2026-08-31_replay_rebucketing_decision_relevance.md
Claims registered: MECH-529

# Replay-driven rebucketing: decision relevance as pressure on E1 representation

**Date:** 2026-08-31  
**Status:** thought / architectural pressure only  
**Scope:** full REE lineage; may create version-placement pressure on current v4-labelled claims  
**Governance note:** this document does **not** promote, demote, or edit claims. It identifies relationships that should be checked against the claims registry and implementation plan.

## Core thought

E1 eventually needs more than persistent predictive content. It needs a way for experience to teach it **which distinctions in that content are worth preserving**.

Objects and episodes provide two related but different representational problems:

- **Object encoding:** what recurring structure should count as a persistent entity, which features belong to it, which relations and affordances are stable, and when two observations should be treated as the same object or as different objects.
- **Episode encoding:** which temporally extended experiences belong together, where event boundaries fall, which objects/relations/commitments matter within the episode, and which parts of the episode are worth sparse retention.

The downstream test of representational adequacy is not whether E1 can reconstruct sensory detail. It is whether the representation preserves distinctions that matter for predicting consequentially different futures while allowing compression of distinctions that do not.

This gives a principled reason for downstream decision systems to exert **learning pressure** on E1 without becoming oracular teachers of E1 content.

A distinction that repeatedly changes viable transitions, consequences, harm, goal progress, uncertainty, or commitment outcome should become easier for E1 to preserve or separate. A distinction that repeatedly fails to alter consequential predictions may become compressible.

The decision system should not say, "this is the correct category." It should provide evidence that the current category structure was or was not sufficient for action and prediction.

## Existing REE pieces that already point toward this

This thought appears to connect mechanisms already present in REE rather than requiring an entirely new subsystem.

### E1 as persistent associative structure

ARC-001 and MECH-154 already frame E1 as a persistent perception-association substrate / addressable associative manifold rather than a declarative database. MECH-507 further proposes explicit compression/decompression in which high-dimensional situations may become functionally equivalent when they imply sufficiently similar action-relevant consequences.

This already contains much of the right principle, but the consequence for **object and episodic category structure** is not yet explicit.

### State as decision-usable binding

The state architecture already distinguishes broad E1 representation from a decision-usable state. A state binds world configuration, self, temporal position, goal relation, antigoal relation, constraints, uncertainty and transition readiness into a navigable unit.

This means REE already has an important separation:

`representation != state prepared for transition search`.

The present thought extends that distinction backward: the representational substrate itself should be shaped over time by whether its distinctions proved sufficient for building useful states.

### Hippocampal episodic sparsity and segmentation

ARC-007 already treats hippocampal traces as sparse episodic trajectories rather than continuous recordings. Existing segmentation pressure includes commitment boundaries, prediction-error or precision changes, and contextual/motivational shifts. Sparse indexing favours decision points, surprising transitions and high-curvature regions.

This is already a primitive form of decision-relevant episodic encoding.

### E3 / basal-ganglia-like extraction and commitment

E3 already receives or constructs bounded task-loop objects containing object identity/index, valence, transition operators, error, stop, time, provenance and optional path structure. E3 is also explicitly the basal-ganglia-like comparison/commitment system rather than another world model.

Therefore REE already has much of the forward path:

`rich representation -> bound state / episodic context -> decision-facing task object -> comparison and commitment`.

The underspecified path is the **slow return path**:

`decision consequences -> evidence about representational sufficiency -> later E1 reorganisation`.

## Endogenous object grain is a prerequisite, not a cosmetic improvement

Recent ARC-134 / MECH-521 work already exposes a deeper problem: current object-like populations can inherit their grain from caller/environment-provided `EntityObservation` structures. The missing P0 is an endogenous merge/split or grain operator capable of deciding when sensory structure should be treated as one object, multiple objects, part-whole structure, or a persistent entity across change.

This matters more under the present framing.

The system cannot learn which **object distinctions** matter for action if the object boundaries themselves are externally fixed.

A plausible developmental ordering is therefore:

1. sensory regularities and temporal coherence;
2. provisional object individuation;
3. persistent identity across observation;
4. relational and affordance structure;
5. episodes binding objects, contexts, actions and consequences;
6. downstream decision use;
7. retrospective pressure to split, merge or reshape earlier representational buckets.

Object individuation should remain corrigible. The initial grain can be wrong and later experience should be able to revise it.

## Why replay becomes functionally necessary

Decision relevance is often only discoverable **after** the episode in which the relevant feature was experienced.

An organism may initially treat several experiences as equivalent because their important discriminating feature is not yet known. A later experience can reveal that an apparently incidental property predicted a consequential divergence.

For example, experiences A, B and C may initially occupy one bucket. Episode D later reveals that one feature shared by A and C but not B predicts harm, viability, trustworthiness, affordance or some other consequential outcome.

The system now needs to revisit earlier episodes and ask, in effect:

- Were A and C more alike than previously represented?
- Was B incorrectly grouped with them?
- Which feature or relation explains the consequential divergence?
- Does the apparent discriminator generalise across other episodes?
- Is a split warranted, or was the divergence incidental?

That cannot be done reliably from the currently active episode alone.

**Replay provides access to non-contiguous experiences under a common evaluative frame.**

Its role is therefore richer than repetition or predictor training. Replay can support **retrospective representation learning**.

## Replay as re-bucketing

A possible functional loop is:

```text
experience
   -> sparse episodic capture
   -> action / commitment
   -> observed consequences
   -> later related experiences
   -> replay of selected episodes
   -> compare invariants and discriminators
   -> evaluate whether current E1 equivalence classes remain sufficient
   -> candidate split / merge / feature reweighting / relation reorganisation
   -> gated consolidation into E1
```

The key operations are not limited to splitting categories.

Replay may support:

- **split:** experiences formerly treated as equivalent predict different consequential futures;
- **merge:** superficially different experiences repeatedly support the same consequential transition structure;
- **feature reweighting:** an already represented dimension becomes more or less important for future inference;
- **relation discovery:** the important predictor is not an object feature but a relation among object, self, context and time;
- **boundary revision:** event segmentation itself changes because a previously unnoticed transition became causally important;
- **abstraction change:** the useful unit moves from specific object to category, from category to relation, or from immediate event to longer episode.

This provides an architectural interpretation of hippocampal pattern separation and pattern completion:

- **Pattern separation:** this difference predicts sufficiently different futures; stop treating the experiences as equivalent.
- **Pattern completion:** these partial cues reliably identify a useful common structure; retrieve/generalise across the shared class.

This is not claimed as a complete biological account of dentate gyrus / CA3 function. It is a functional mapping useful for REE.

## Why sleep has a distinct role beyond replay itself

Some replay can occur during waking. REE already allows for waking and sleep-capable processing to overlap rather than assigning every replay function exclusively to sleep.

However, representational rebucketing supplies a strong reason why **some changes should preferentially complete during sleep or another decoupled mode**.

If E1 is the representational coordinate system currently being used to perceive, bind state, retrieve memories and choose actions, changing its category boundaries while simultaneously relying on those boundaries can create instability:

- active perceptions may change interpretation mid-action;
- pointers into object or state representations may become stale;
- episodic indices may no longer refer cleanly to the same representational neighbourhoods;
- downstream decision objects may change semantics during comparison;
- newly generated hypotheses can be mistaken for external evidence if provenance is not preserved;
- a salient single episode can trigger catastrophic over-splitting or over-merging.

A sleep-like mode can reduce these hazards by temporarily weakening the need for immediate sensorimotor consistency while allowing replay, comparison and controlled representational revision.

This suggests a useful distinction:

### Waking-capable operations

- capture a provisional episode;
- attach outcome / commitment information;
- retrieve similar episodes;
- perform limited replay;
- adjust local precision or eligibility;
- create provisional hypotheses that an existing bucket is inadequate.

### Sleep-favoured or decoupled operations

- broad comparison of non-contiguous episodes;
- merge/split evaluation across multiple memories;
- re-index episodic traces after representational change;
- remodel attractor boundaries;
- alter compression depth or category grain substantially;
- reconcile newly reorganised representations with older autobiographical structure;
- run counterfactual tests of proposed rebucketing before allowing it to affect waking inference.

This gives sleep a concrete computational purpose: **safe maintenance of the representational coordinate system itself**.

## Counterfactual replay as protection against bad rebucketing

Pure association is not enough. A salient outcome could otherwise cause the system to overfit one episode and split categories around incidental features.

Counterfactual replay provides a possible safeguard. If a candidate distinction is thought to matter, replay can test whether using that distinction changes predicted consequences across several remembered or simulated trajectories.

The question is not simply:

`Did feature X occur before harm?`

but:

`Does representing X as a distinct causal/contextual feature improve predictions of what would happen under relevant alternative actions and contexts?`

This remains non-oracular: simulated material must retain provenance and cannot count as independent external confirmation. Existing hypothesis/source tagging and non-oracular injection principles are therefore directly relevant.

## Biological convergence

The broad biological organisation appears compatible with this decomposition without requiring anatomical identity:

- perirhinal and related cortical systems contribute object/item representations;
- parahippocampal and entorhinal systems contribute contextual, spatial and relational structure;
- hippocampus binds object/context/time into episodic and navigable relational structures;
- hippocampal replay can reinstate non-current experience and support consolidation/generalisation;
- orbitofrontal/prefrontal systems represent task/state structure and context-conditioned outcome/value relationships;
- corticostriatal / basal-ganglia loops gate actions and cognitive transitions based on state- and consequence-relevant information;
- consolidation allows later experience and outcome structure to reshape cortical representations rather than storing a permanent copy of the initial episode.

The useful architectural lesson is not that REE needs exact replicas of these areas. It is that biological systems appear to preserve a distinction among:

1. rich persistent representation;
2. episodic relational binding;
3. context-conditioned decision relevance;
4. action/commitment selection;
5. slower representational reorganisation informed by accumulated experience.

REE already has all five functions in partial form, but the final loop connecting (4) and (5) is not yet explicit enough.

## The important constraint: E3 must not become E1's teacher

This thought should **not** be implemented as direct supervised category labels from E3 into E1.

E3 should be allowed to communicate that the current representation was consequentially insufficient, for example through typed signals such as:

- prediction/consequence mismatch;
- harm or goal error;
- repeated veto/conflict associated with a representation;
- alternative trajectories whose outcomes diverge despite apparently equivalent E1 states;
- unexpectedly different outcomes following apparently equivalent objects or contexts.

E1 / hippocampal / consolidation machinery can then use accumulated evidence to decide whether and how the representation should change.

This preserves the architectural principle that downstream selection changes the **learning conditions and evidence pressure**, not the truth content of E1 directly.

## Version-placement pressure: v4 mechanisms may contain v3 prerequisites

This thought creates a legitimate reason to re-examine some claims currently labelled for v4 or later.

The key question is not:

> Would richer object cognition be nice to have in v3?

It is:

> Can v3 be considered a coherent implementation of its own E1 -> hippocampus -> E3 architecture if the distinctions supplied to those systems cannot be formed and revised endogenously according to accumulated decision consequences?

If the answer is no, then at least a **minimal non-degenerate form** of some currently v4-labelled representational machinery may be necessary in v3.

The strongest pressure currently appears to fall on:

- **ARC-134 / endogenous perceptual grain:** some minimal endogenous object individuation / merge-split capacity may be prerequisite if v3 is to learn useful object structure rather than consume environment-defined objects.
- **MECH-507 / compression-decompression:** the action-relevant equivalence principle may need a minimal operational form if v3's E1 representations are to generalise and differentiate for reasons tied to consequences.
- **MECH-512 / compression depth:** a full dynamic abstraction controller may remain later-stage, but v3 may need at least enough variable representational grain to demonstrate split/merge rather than fixed buckets.
- **MECH-508 / attractor-as-generative-disposition:** the full mature interpretation may remain later, but replay-driven rebucketing assumes attractor/category structure is revisable rather than immutable.
- **sleep / replay claims:** existing sleep and replay machinery may need to be evaluated not only for state change or trajectory rehearsal, but for whether it can actually reorganise representational equivalence classes and preserve/re-index episodic access afterward.

This is not yet an argument that all of these claims should be relabelled `v3`.

A plausible outcome is instead to separate each into:

- a **minimal v3 prerequisite** needed to make the architecture non-degenerate; and
- a **richer v4+ mechanism** needed for endogenous, multi-scale, developmentally mature representation.

This would fit REE's existing pattern of pulling only the load-bearing core of later mechanisms into an earlier version while leaving the richer implementation where originally planned.

## What would distinguish necessity from premature scope expansion?

Before changing version labels, ask whether a minimal v3 agent can demonstrate all of the following:

1. **Object correction:** two initially equivalent perceptual entities can become distinct representations because accumulated experience predicts different consequences.
2. **Object generalisation:** two initially distinct entities can become functionally grouped when their relevant relational/consequence structure is equivalent.
3. **Episode rebucketing:** later experience can change how earlier episodic traces are grouped or retrieved without erasing their provenance.
4. **Decision relevance:** the changed representation measurably improves state construction, trajectory discrimination or commitment quality.
5. **Non-oracular learning:** no downstream signal directly supplies the new category label.
6. **Replay contribution:** the reorganisation can depend on replay of non-contiguous episodes rather than only online incremental learning.
7. **Sleep/decoupling contribution:** at least one consequential representational revision can be performed more safely or completely in a decoupled phase than while the representation is being used online.
8. **Index continuity:** after rebucketing, hippocampal/autobiographical traces remain addressable rather than becoming invalid pointers into the old representation.

If v3 cannot even represent these questions because its object grain and category structure are fixed by the environment, that is evidence that the current version boundary is cutting through a load-bearing loop.

If a much simpler existing mechanism can already satisfy them, the richer v4 claims can remain v4.

## Architectural synthesis

The resulting loop is:

```text
E1 persistent associative representation
        |
        v
provisional objects / relations / context
        |
        v
hippocampal episodic binding and sparse indexing
        |
        v
state construction / replay / candidate trajectories
        |
        v
E2 consequence prediction + E3 comparison/commitment
        |
        v
observed consequential divergence / sufficiency error
        |
        v
replay of relevant non-contiguous episodes
        |
        v
counterfactual test of candidate representational changes
        |
        v
sleep-favoured split / merge / reweight / re-index
        |
        +-------------------------------> E1
```

The most important idea is that **representation is itself something the organism learns how to do**.

It does not merely learn facts inside a fixed representational vocabulary. It learns which distinctions constitute useful objects, useful episodes and useful equivalence classes because living with those representations reveals which distinctions actually change what can happen next.

Replay permits the system to apply later knowledge to earlier experience. Sleep provides a protected regime in which the coordinate system can be revised without simultaneously depending on it for immediate perception and action.

This may be one of the missing links between REE's existing object-grain work, E1 compression, hippocampal replay, sleep, state abstraction and basal-ganglia-like commitment machinery.

## Immediate follow-up

Do **not** promote claims from this thought automatically.

Recommended next step is a claims/version audit asking:

1. Which existing claims already encode parts of this loop?
2. Which required edges are genuinely absent?
3. Which absent edges are required for v3 non-degeneracy versus only for richer v4 cognition?
4. Can current v3 sleep/replay machinery alter representational grain, or only write/replay within a fixed grain?
5. Can current object representations be split/merged endogenously, or are they still environment-authored at the decisive boundary?
6. If a v3 prerequisite is found inside a v4 claim, should the claim be split rather than wholesale relabelled?
