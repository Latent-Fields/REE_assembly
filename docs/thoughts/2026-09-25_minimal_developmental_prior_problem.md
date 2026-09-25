Status: raw / unprocessed

# The Minimal Developmental Prior Problem: What Must an Organism Know Before It Can Learn?

**Date:** 2026-09-25  
**Status:** thought document / architectural hypothesis / experimental programme; not a claim promotion, build authorisation, experiment commission, or fixed minimal-prior specification.  
**Scope:** developmental priors, viability, structured babbling, self-action contingency, reflexive survival, developmental accelerators, replay and freeze/unfreeze, chunking/splitting, axiom-to-necessity mapping, ablation/minimality testing.  
**Origin:** discussion prompted by the September 25 REE Phase-0 babbling result and the observation that a near-monostrategy developmental phase can make the downstream E2→E3→valuation chain appear flat.  
**Epistemic caution:** the candidate minimum below is deliberately provisional. The purpose of the document is to preserve uncertainty about necessity, sufficiency, reducibility and environment-specificity while defining a programme capable of testing them.

## Status and purpose

The purpose of this thought is **not** to specify a canonical innate repertoire for REE. It is to identify candidate structures that may be necessary for an artificial organism to begin learning at all, distinguish them from structures that merely make development substantially easier, and make both classes experimentally reducible.

The central question is:

> **How little inherited structure is enough for an organism to become learnable, and how much additional general structure makes development reliably tractable without smuggling in solutions to its environment?**

This distinction matters. A mechanism may be unnecessary in principle yet improve developmental speed, robustness or survivability by orders of magnitude. Conversely, something necessary in one hostile environment may reveal more about that environment than about organisms in general.

The appropriate objective is therefore not to decide the minimal set in advance. It is to construct candidate sets and allow REE to determine, through development, ablation and environmental transfer, which structures are necessary, which are accelerators, which can emerge from others, and which are merely ecological scaffolds.

---

## 1. The observation that motivates the problem

A recent REE developmental probe exposed a deceptively simple failure.

Phase 0 was intended to provide something analogous to motor babbling: early behaviour through which an initially ignorant organism generates experience of how its actions alter its world. In practice, the native Phase-0 behaviour became near-monostrategy on most tested seeds.

This created a potentially profound interpretive trap.

If early behaviour contains very little action diversity, E2 receives little information from which to learn differential action consequences. If E2 cannot distinguish what different actions do, predicted trajectories become similar. If trajectories are insufficiently differentiated, E3 has little meaningful structure upon which valuation, effort, harm and other comparators can act. The downstream cognitive chain can therefore appear flat even when its individual components are capable of contributing.

Structured action-diverse babbling substantially improved world-model action discrimination. More importantly, a one-off developmental exposure was insufficiently durable: later narrow experience could overwrite what had been learned. Retaining a minority of structured developmental replay preserved the advantage across the tested seeds.

This suggests that an organism cannot simply be supplied with learning machinery and expected to bootstrap cognition from whatever behaviour happens to occur.

**The organism must first generate experience from which useful distinctions can be learned.**

The question then becomes unavoidable: what, if anything, must already exist before learning can do the rest?

---

## 2. Biology does not appear to begin from behavioural white noise

Early spontaneous movement is variable, but the available evidence does not support treating it as unrestricted random actuator noise.

Recent work on spontaneous infant arm movement found structured exploration of limb dynamics before mature goal-directed reaching. Early movement appears capable of sampling informative regions of the body's dynamics without already encoding the later task solution.

Longitudinal work on infant locomotion provides an especially useful possible principle. Neonates can generate very high behavioural variability from a **small number of motor primitives whose activation is itself highly variable**. With development, more differentiated primitives appear while their recruitment becomes more regular. The result is not development from randomness to structure, but development from **a small structured vocabulary used very variably toward a larger, more specialised vocabulary**.

Motor-primitives research more generally suggests that such primitives can bootstrap action construction while remaining recombinable and extensible; importantly, an initial primitive repertoire can both facilitate and constrain later behaviour, making augmentation and reorganisation necessary as novel skills develop.

This suggests a different interpretation of "babbling" for REE.

The primitive requirement may not be:

> produce random actions.

It may instead be:

> **possess a small generative basis from which varied, temporally structured actions can be produced before their consequences are understood.**

That is much less environment-specific.

---

## 3. Development may manufacture its own later priors

Kanazawa's account of early behavioural development is particularly compatible with this interpretation. Spontaneous fetal and infant activity is proposed to progressively structure sensorimotor information through interaction among body, environment and developing nervous system. Behaviour that initially lacks explicit external goals can thereby contribute to the organisation upon which later intentional behaviour depends.

This suggests that early action may do more than populate a training buffer.

It may construct the first useful representational coordinate system.

Before an organism can know that:

> action A causes outcome X,

it may first have to discover regularities corresponding to:

- something changed;
- this change followed my action;
- some changes recur after similar actions;
- some dimensions of observation are controllable;
- some consequences concern my own state;
- some action sequences behave as coherent units;
- some distinctions matter to prediction while others can be compressed.

Early developmental behaviour therefore potentially participates in constructing **self, action, consequence and controllability** as useful representational categories.

That interpretation makes the developmental problem deeply relevant to REE rather than a peripheral training concern.

---

## 4. A provisional taxonomy: necessity must not be confused with usefulness

Candidate developmental mechanisms should be classified along at least two independent axes.

| | **General / environment-independent** | **Environment-specific** |
|---|---|---|
| **Candidate necessary** | Structures that may be required for a broad class of organisms to bootstrap learning | Structures required because a particular ecological niche is otherwise unlearnable or unsurvivable |
| **Developmental accelerator** | General mechanisms that improve efficiency, stability or robustness but may be derivable or dispensable in principle | Domain-specific shortcuts that make a particular task or world easier |

There is also a fifth category orthogonal to this table:

### Enabling architecture

Some structures are not meaningfully "priors" at all. An agent cannot test developmental hypotheses without machinery such as:

- plasticity;
- memory;
- temporal representation;
- an action interface;
- mechanisms capable of representing self-generated events;
- some persistent world/self state;
- capacity for learned representations to influence subsequent behaviour.

These are properties of the experimental organism rather than hypotheses about what it innately knows.

This distinction should remain explicit in REE.

---

## 5. Candidate general necessities

The current evidence suggests several **candidate** necessities, but none should yet be canonised as the unique minimum.

### 5.1 A valued self-state

Some states of the organism must matter before ordinary environmental goals have been learned.

Homeostatic reinforcement-learning work demonstrates how behavioural policies can subsequently be learned when changes in internal state provide primary value. In such models, preservation or restoration of viable internal conditions can ground learned anticipatory and motivated behaviour without specifying the environmental policy in advance.

This maps suspiciously well onto the existing REE ethical foundation.

A1 establishes a self or locus to which states, action and responsibility apply.

A2 states that existence has value.

A4 establishes both causal power and vulnerability.

D1 derives self-preservation.

From the developmental direction, we appear to reach something structurally similar: if there is no valued condition of the organism, there may be no non-arbitrary grounding from which "better" and "worse" consequences can first acquire behavioural force.

This convergence is interesting but is **not proof that the axiomatisation is uniquely necessary**. REE should be capable of showing that some different grounding is sufficient or that an apparently necessary axiom can be reduced to another structure.

Nevertheless, the developmental question gives A2 and D1 an empirical role: they may be prerequisites for bootstrapping motivated behaviour rather than propositions layered onto an otherwise complete cognitive agent.

### 5.2 Structured endogenous action

Learning action consequences requires actions to occur before their consequences are known.

A developmental organism therefore plausibly needs some source of endogenous behaviour which:

- spans the available action basis sufficiently;
- contains temporal structure rather than independent white noise;
- permits variable combinations and durations;
- does not encode the solution to the environment;
- remains capable of producing alternatives before the world model can recommend them.

The infant motor literature suggests that high behavioural variability can be obtained from a surprisingly small primitive basis.

REE should therefore ask whether a tiny action generator can bootstrap everything else.

In the current gridworld, this need not mean a repertoire of "go north", "avoid hazard" or "seek food" reflexes. It could mean little more than availability of every action class, including non-action where relevant, combined into short persistent and varied motifs.

The distinction is important:

**the prior should preferably specify how to explore an action space, not what the actions mean.**

### 5.3 Self-action contingency sensitivity

An organism receives many changes in sensory state. Only some result from its own actions.

Some initial bias toward temporal and causal contingency may therefore be necessary if the organism is to discover agency efficiently.

The infant mobile-paradigm literature demonstrates remarkably early learning and retention of sensorimotor contingencies, and embodied interpretations of that literature treat contingency learning as an important basis for active exploration of body and environment.

For REE, the relevant primitive need not encode any particular environmental causal relationship. It may be as weak as:

> **changes occurring with an appropriate temporal relationship to self-generated action deserve preferential consideration as possible action consequences.**

This could provide an initial bridge between A1 and A4: there is a self, and that self discovers that it has causal power by identifying reliable contingencies between its actions and subsequent state changes.

Whether even this must be innate should remain experimentally open.

---

## 6. Candidate innate survival mechanisms

There is an important special case in which ordinary learning may be insufficient.

If a first encounter with some state destroys the agent, "learn after experiencing the consequence" is impossible.

Biological organisms contain fast regulatory and defensive systems operating beneath deliberative learning. Homeostatic control likewise includes both immediate regulation and learned anticipatory behaviour.

REE may therefore require primitive survival responses.

But their content should be kept as general as possible.

An innate survival mechanism need not mean:

> hazard tile -> move LEFT.

It could instead mean:

> **extreme deterioration in the valued self-state interrupts the current behavioural trajectory and temporarily changes action selection away from its continuation.**

The environmental solution remains to be learned.

This provides a useful distinction between **primitive preservation** and **learned avoidance**.

The first prevents development from terminating before learning can occur. The second discovers how this particular environment should be navigated.

---

## 7. General developmental accelerators

Several mechanisms may greatly improve development without being strictly necessary.

They should therefore remain candidates rather than silently becoming innate requirements.

### Prediction-error-driven orienting

Infants presented with violations of prior expectations subsequently preferentially explore and learn about the surprising objects involved. Their exploration can be specifically related to the nature of the violated expectation rather than merely reflecting undirected arousal.

REE may therefore eventually derive:

> high prediction error -> acquire additional relevant information.

But this does not imply that "orient toward novelty" must be hard-coded.

Once a world model exists, prediction error already identifies situations in which that model is inadequate. Orienting may emerge as a learned information-gathering response.

The distinction can be tested.

### Learning-progress-driven exploration

Novelty alone creates obvious failure modes: an irreducibly noisy stimulus remains perpetually novel.

Computational intrinsic-motivation work distinguishes novelty from progress in learning, allowing exploration to preferentially target regions in which uncertainty is actually reducible.

This could be an extraordinarily useful developmental accelerator for REE.

But it requires a history long enough to estimate whether prediction is improving. It therefore seems more naturally a **later developmental achievement** than a birth-level primitive.

A plausible progression is:

> spontaneous exploration -> contingency discovery -> prediction -> surprise-guided exploration -> learning-progress-guided exploration.

### Primitive persistence

An action may have to continue long enough for its consequences to become observable.

This probably does not require an independent reflex. It may simply be a property of the endogenous action generator: actions occur in temporally extended motifs rather than instantaneous independent draws.

### Developmental replay and protected retention

The REE babbling results make this particularly salient.

Broad developmental experience can create useful distinctions and then be erased by later narrow behaviour.

Retaining representative developmental experience is therefore likely to be a powerful accelerator and may ultimately prove necessary in some learning regimes.

Motor-babbling work in robotics already supports the usefulness of moving from broad early exploration toward later specialisation. The general-to-particular approach, for example, begins with motor babbling to establish a broad approximate inverse map and subsequently refines task-relevant regions through reinforcement.

For REE, however, retained developmental information should not simply become immutable.

---

## 8. Freeze, destabilise, revise

A developmental organism faces a stability-plasticity problem.

If early broad knowledge remains maximally plastic, later narrow experience can erase it.

If it becomes permanently fixed, the organism cannot adapt when its environment genuinely changes.

The useful solution is therefore not permanent freezing but **conditional reopening**.

Memory-reconsolidation research provides a relevant biological analogy. Previously stable memories can become labile again under particular conditions, with prediction error repeatedly implicated in destabilisation and subsequent updating. Dopamine, norepinephrine and acetylcholine have all been implicated in memory-labilisation processes, although the biological mechanisms are considerably richer than any simple one-neuromodulator mapping.

For REE this suggests a candidate developmental principle:

> **knowledge that has become reliable should become resistant to incidental overwrite, but persistent prediction failure should permit its internal structure to become plastic again.**

This aligns with the developing acetylcholine (ACh)-mediated freeze/unfreeze hypothesis, but the mapping should remain provisional rather than treating acetylcholine as a predetermined software variable with a single biological meaning.

---

## 9. Development requires changing primitives, not merely learning values over fixed primitives

The developmental-prior problem connects directly to REE's existing interest in chunking and splitting.

A useful organism should not retain the same behavioural vocabulary throughout its development.

Early experience might begin with atomic or near-atomic primitives:

> action A  
> action B  
> action C

Repeated reliable structure may support chunking:

> A-A-A -> persistent movement motif

then:

> A-A-B -> manoeuvre

and eventually:

> approach -> inspect -> interact.

Motor-skill learning in humans is hierarchical. With practice, individual elements become organised into chunks and reusable higher-level representations rather than remaining permanently flat action sequences.

But chunking alone is dangerous.

Suppose REE compresses repeated successful behaviour into:

> APPROACH-SALIENT-OBJECT.

Later it encounters two previously conflated classes of salient object whose consequences differ.

The appropriate response is not merely to lower the value of the entire chunk. Prediction failure should be capable of reopening its internal representation:

> APPROACH-SALIENT-OBJECT  
> ↓  
> distinguish object/context dimension  
> ↓  
> APPROACH-class-A / INVESTIGATE-class-B

Development therefore needs two complementary operations:

> **chunk when distinctions cease to predict meaningful differences; split when previously ignored distinctions acquire predictive or evaluative importance.**

This applies not only to motor behaviour.

It potentially governs:

- perceptual categories;
- action primitives;
- E1/E2 transition schemas;
- hippocampal episodes and maps;
- strategies;
- goals;
- social categories;
- concepts;
- eventually ethical and relational abstractions.

The result is an expanding and contracting representational vocabulary.

---

## 10. Three meanings of "primitive"

The word primitive should therefore be used carefully.

REE may contain at least three distinct forms.

### Innate primitives

Structures available before relevant environmental learning.

These are the proper subject of the minimal-prior question.

### Developmental primitives

Learned structures that have become sufficiently reliable that higher layers can temporarily treat them as atomic.

A complex skill can therefore function as a primitive at a higher level without having been innate.

### Contextually reopened primitives

When a mature chunk begins producing systematic prediction error, its hidden components can be made available again for revision.

Thus a representation can alternate between:

> internally complex but functionally atomic

and

> explicitly decomposed and plastic.

This may be central to lifelong adaptation.

---

## 11. The axioms viewed as developmental necessities

This framework reveals an unexpected correspondence between the REE axioms and problems encountered when asking what a developmental organism requires.

### A1 — Self exists

Contingency learning requires some locus to which action and consequence can be attributed.

### A2 — Existence has value

A valued self-state supplies a non-arbitrary initial direction before learned environmental goals exist.

### A3 — Uncertainty and modelling

If the organism acts only through imperfect models, discrepancy between prediction and experience acquires functional significance. Model refinement becomes necessary rather than optional.

### A4 — Causal power and vulnerability

The organism can alter the world, discover that its actions have consequences, and itself suffer consequences. This creates both agency and the possibility of self-preservation.

D1 — self-preservation — then acquires a potential developmental implementation through primitive viability protection plus subsequently learned anticipatory behaviour.

D2 — model refinement — may likewise require a **developmental behavioural manifestation**:

> act so as to obtain informative consequences; detect where the model fails; preserve useful regularities; reopen them when necessary; progressively build better primitives.

The significance of this correspondence is not that developmental science has proved the axioms.

Rather, a different question — *what machinery does an initially ignorant organism require to begin functioning?* — appears to regenerate structures resembling several of them.

That convergence is testable.

REE should be permitted to show that one is unnecessary, reducible, incorrectly formulated or functionally replaceable.

---

## 12. General versus environment-specific priors

A central experimental discipline should be:

> **prefer the least environment-specific intervention capable of restoring development.**

If ordinary development fails:

1. first test whether better structured endogenous exploration is sufficient;
2. then whether general contingency or information-seeking mechanisms are sufficient;
3. then whether memory/plasticity mechanisms are insufficient;
4. only then introduce environment-specific priors where necessary.

Examples:

**General**
- generate diverse temporally coherent actions;
- protect viability;
- detect self-action contingencies;
- attend to persistent model failure;
- preserve and revise learned regularities.

**Environment-specific**
- move toward food sprites;
- avoid red tiles;
- turn left after a particular visual pattern;
- prefer northward movement in this map.

Environment-specific mechanisms are not illegitimate. Biology contains enormous inherited ecological structure.

But when REE requires one, the scientific interpretation should be explicit:

> this environment could not be reliably developed into under the current general prior set without additional ecological information.

That is itself a useful result.

---

## 13. Proposed candidate register

Rather than declaring a minimal set, REE should maintain a developmental-prior candidate register.

Each entry should contain:

- **mechanism**
- **general or environment-specific**
- **candidate necessity / accelerator / scaffold / enabling architecture**
- **predicted developmental contribution**
- **mechanisms from which it might instead emerge**
- **earliest developmental stage at which it can operate**
- **cost of including it**
- **what would show it is unnecessary**
- **what would show it is merely accelerating development**
- **transfer expectation across environments**
- **ablation consequence**
- **current evidence**

Possible initial entries include:

**Candidate necessities**
- valued self-state / viability;
- structured endogenous action;
- self-action contingency sensitivity;
- perhaps a minimal catastrophic-harm interrupt.

**General accelerator candidates**
- prediction-error orienting;
- adaptive exploratory variability;
- learning-progress intrinsic motivation;
- primitive persistence;
- motor synergies;
- developmental replay;
- freeze/unfreeze plasticity;
- sleep consolidation;
- precision regulation;
- controllability-seeking;
- chunk formation;
- prediction-error-driven splitting.

**Enabling architecture**
- memory;
- plasticity;
- temporal ordering;
- self/world representation;
- action representation;
- capacity for learned models to alter action selection.

**Environment-specific scaffolds**
- left deliberately empty until an environment demonstrates their necessity.

---

## 14. Experimental programme: do not guess the minimum

The minimum should be discovered by **reduction and ablation**.

A useful starting architecture might deliberately contain somewhat more general developmental machinery than is ultimately necessary.

Then progressively remove components.

### Remove structured endogenous action

Retain all learning machinery, but allow only whatever behaviour emerges from the existing policy.

Does world-model action discrimination develop?

If not, restore structured babbling.

### Remove contingency bias

Retain diverse action but eliminate preferential learning of action-linked changes.

Does agency emerge anyway from generic prediction?

If yes, contingency sensitivity was an accelerator rather than a necessity.

### Remove viability grounding

Retain exploration and modelling.

Do stable goals or preservation behaviours emerge from another source?

If so, A2's implementation requires reconsideration.

### Remove developmental retention

Permit structured babbling but allow later on-policy learning to overwrite it.

Does development repeatedly collapse into mono-strategy?

The existing REE result provides an initial positive reason to test this seriously.

### Remove explicit orienting

Retain prediction error and action-contingency machinery.

Does targeted exploration emerge without an orienting reflex?

If so, orienting is derivable.

### Disable chunking

Force all behaviour to remain in the original action alphabet.

Does competent behaviour emerge but scale poorly?

Chunking may then be an accelerator rather than a minimal requirement.

### Disable splitting

Permit learned macro-actions and abstractions but prevent their decomposition.

Does adaptation fail specifically after environmental changes or category exceptions?

That would establish splitting as a maintenance requirement rather than an initial developmental requirement.

---

## 15. Measure development, not merely endpoint performance

The outcome should not simply be:

> did the agent eventually obtain reward?

Developmental trajectories matter.

Relevant measurements include:

- action-space coverage over developmental time;
- action→consequence mutual information;
- controllability estimates;
- world-model discrimination between actions;
- persistence of developmental knowledge;
- prediction error;
- prediction-error reduction;
- emergence and turnover of chunks;
- chunk depth;
- splitting events;
- time to first coherent model-based behaviour;
- survival duration;
- recovery after environmental change;
- behavioural diversity after competence emerges;
- dependence of E3 decisions on learned causal information;
- emergence of orienting or information-seeking without explicit rules.

For each supposedly emergent capacity, causal intervention should test whether the behaviour actually depends on the proposed machinery.

Ethical-looking, curious-looking or organism-like behaviour is insufficient if the causal path cannot be demonstrated.

---

## 16. The possible developmental sequence

The current hypothesis suggests a developmental sequence approximately like:

> **valued self**
>
> ↓
>
> **small innate action basis**
>
> ↓
>
> **structured spontaneous variation**
>
> ↓
>
> **self-action contingency discovery**
>
> ↓
>
> **sensorimotor regularities**
>
> ↓
>
> **primitive world/body models**
>
> ↓
>
> **prediction error becomes meaningful**
>
> ↓
>
> **targeted exploration**
>
> ↓
>
> **reliable contingencies become chunks**
>
> ↓
>
> **chunks become higher-level primitives**
>
> ↓
>
> **persistent errors reopen and split those primitives**
>
> ↓
>
> **increasingly hierarchical model-based behaviour**

Nothing requires the entire sequence to be explicitly programmed.

The scientific objective is to determine how much of it emerges once the earliest pieces exist.

---

## 17. A different interpretation of "innate"

Innate structure need not primarily consist of facts about the world.

It can consist of **procedures for discovering a world**.

Instead of:

> food looks like X; danger looks like Y; perform action Z,

the initial inheritance could be closer to:

> I have states that matter.  
> I can act.  
> Vary action enough to discover its consequences.  
> Changes following my action may be caused by me.  
> Preserve useful regularities.  
> Notice when they stop predicting.  
> Reopen them when necessary.

That is much closer to an **epistemic inheritance** than an ontological one.

It does not tell the organism what its environment contains.

It gives the organism machinery with which to find out.

---

## 18. Implication for REE

REE may currently possess much of the machinery required for sophisticated cognition while still lacking part of the machinery required to **develop into a creature capable of using it**.

The recent babbling result is important precisely because the apparent defect propagated down the entire chain.

The world model could not learn action distinctions that behaviour did not expose.

E3 could not use distinctions that E2 had never acquired.

Valuation could not meaningfully discriminate trajectories that the predictor rendered nearly equivalent.

The apparent downstream flatness therefore had a developmental upstream cause.

The resulting lesson is broader:

> **Before an organism can reason well, it may need machinery whose purpose is simply to make useful reasoning learnable.**

This is not a diversion from the REE ethical programme.

If A1–A4 and D1–D2 are to become causally operative rather than declarative, developmental machinery may be the mechanism through which they acquire behavioural content.

---

## 19. Core hypothesis

The strongest current hypothesis can be stated cautiously:

> **A minimally developmental REE may require a valued and vulnerable self-state, a small general basis for structured endogenous action, and sufficient sensitivity to self-action contingencies to construct initial sensorimotor models. Persistent but revisable memory may allow those models to become the substrate from which prediction-driven exploration, learned self-preservation, hierarchical behavioural primitives and increasingly deliberative control emerge.**

But this is explicitly a **candidate minimum**, not the minimum.

A richer set of general developmental mechanisms may be required.

Alternatively, one or more elements above may be derivable from still simpler machinery.

Both outcomes are scientifically valuable.

---

## 20. Falsification and refinement

This thought would be weakened if:

- unstructured behaviour reliably develops equally informative world models;
- explicit self-action contingency sensitivity proves unnecessary across diverse environments;
- preservation behaviour arises without any valued self-state or equivalent;
- structured developmental experience provides no benefit once other training defects are corrected;
- chunking produces no scaling or transfer benefit;
- splitting is unnecessary after environmental change;
- general developmental accelerators fail to transfer between environments;
- supposed necessities can be removed without developmental cost.

It would be strengthened if:

- the same small general prior set repeatedly bootstraps development in substantially different environments;
- environment-specific priors become unnecessary once general developmental machinery is present;
- supposedly higher-level behaviours such as orienting and curiosity emerge without being explicitly programmed;
- learned chunks progressively replace innate primitives as the functional action vocabulary;
- prediction error selectively reopens those chunks when their internal distinctions become relevant;
- ablating individual candidate necessities produces specific predicted developmental failures;
- restoring the missing mechanism repairs development without encoding the environmental solution.

---

## 21. The experimental ideal

The aim should not be to build a creature that begins life knowing how to survive the reef.

The more interesting achievement would be a creature that begins with very little, **discovers what kind of place the reef is, discovers what its own actions mean there, constructs progressively better primitives, and develops behaviour appropriate to that world because its inherited machinery made learning possible**.

If that succeeds, REE will have done more than acquire another competent policy.

It will have begun to demonstrate how an artificial organism can transform weak general inheritance into a specific lived competence.

And because the inherited assumptions are explicit and ablatable, it may also provide an experimental answer to a much older question:

> **What must already be present before experience can teach the rest?**

## Selected literature

- García-Guzmán JH, Ros E, Luque NR. *Infants’ spontaneous movements explore arm dynamics.* Communications Biology. 2026. DOI: 10.1038/s42003-026-09986-0.
- Kanazawa H. *Early behavioral development as the structuring of sensorimotor information.* Advances in Child Development and Behavior. 2026. PubMed PMID: 42252157.
- Hinnekens E, Barbu-Roth M, Do M-C, Berret B, Teulier C. *Generating variability from motor primitives during infant locomotor development.* eLife. 2023;12:e87463.
- Keramati M, Gutkin B. *Homeostatic reinforcement learning for integrating reward collection and physiological stability.* eLife. 2014;3:e04811.
- Sen U, Gredebäck G. *Making the World Behave: A New Embodied Account on Mobile Paradigm.* Frontiers in Systems Neuroscience. 2021.
- Stahl AE, Feigenson L. *Observing the unexpected enhances infants' learning and exploration.* Science. 2015.
- Oudeyer P-Y, Kaplan F. *What is intrinsic motivation? A typology of computational approaches.* Frontiers in Neurorobotics. 2007.
- Diedrichsen J, Kornysheva K. *Motor skill learning between selection and execution.* Trends in Cognitive Sciences. 2015.
- Giszter SF. *Motor primitives—new data and future questions.* Current Opinion in Neurobiology. 2015.
- Exton-McGuinness MTJ, Lee JLC, Reichelt AC. *Updating memories—the role of prediction errors in memory reconsolidation.* Behavioural Brain Research. 2015.
- *Autonomous functional movements in a tendon-driven limb via limited experience.* Nature Machine Intelligence. 2019.

## Internal evidence anchors

- REE_assembly: `evidence/planning/babbling_e2_action_coverage_probe_20260925.md`
- REE_assembly: `evidence/planning/breakthrough_pass_synthesis_20260925.md`
- REE_assembly: coupled loop-repair campaign plan
- REE v3: native WakingTrainer landing, default-OFF
- Related thought: `docs/thoughts/2026-09-25_error_as_information_error_as_threat.md`
- Related thought: `docs/thoughts/2026-09-24_from_components_to_functional_organism.md`

