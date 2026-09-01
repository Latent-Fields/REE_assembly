---
nav_exclude: true
---

Status: processed
Intake: evidence/planning/thought_intake_2026-08-31_play_as_developmental_information_hunger.md
Claims registered: MECH-528, ARC-136


# Play as developmental information hunger across expanding affordance spaces

**Date:** 2026-08-31
**Status:** exploratory thought intake; full REE lineage

## Core thought

Play may be understood, at least in part, as **intrinsically motivated exploration of learnable affordances under conditions where immediate instrumental success is not the sole objective**.

In early development, the most valuable unknowns are often close to the body. A developing organism must discover what its current body can reach, climb, arrest, carry, squeeze through, balance on, throw, survive, and manipulate. Running, jumping, climbing, spinning, falling, balancing, throwing and repeatedly attempting marginal actions may therefore provide a dense stream of experiments on the coupled **self-world-action model**.

This is particularly important because the plant being controlled is changing. Growth changes limb lengths, strength, centre of mass, reach, momentum, balance, locomotor strategy and energetic cost. Yesterday's calibration of an affordance can therefore become obsolete even when the external environment has not changed.

The relevant model is not simply:

`P(outcome | world-state, action)`

but something closer to:

`P(outcome | self-state, world-state, action)`.

Developmental motor research supports this general framing: locomotor development requires continual calibration of action against both environmental properties and changing bodily capabilities, and affordance perception is central to that process. Mobility itself creates new opportunities for exploration and cascades into perceptual, cognitive and social development.

## It does not come before play: it may be play

The first intuition was that bodily information-hunger might be what comes *before* play. On reflection, that division may be wrong. This sort of low-stakes, intrinsically rewarding experimentation may already be one of the most basic forms of play.

Exploratory play can be sensitive to information value. Children preferentially intervene where evidence is ambiguous and can choose actions that discriminate between competing possibilities. Intrinsic-motivation and developmental-robotics work likewise shows how curiosity, prediction improvement, competence gain or learning progress can organise exploration without requiring an external task reward.

A better hypothesis is therefore:

> **Play is one expression of a developmental information-hunger system that preferentially explores regions of action space in which useful learning remains possible.**

This need not imply explicit metacognitive curiosity. The exploration process itself can be rewarding.

## The moving frontier of play

The important extension is that the information hunger need not disappear when bodily affordances become comparatively well calibrated. Instead, the **frontier at which play is rewarding may migrate**.

A tentative progression is:

**bodily affordances**  
→ **object affordances**  
→ **compositional and causal affordances**  
→ **other agents and social affordances**  
→ **symbolic and counterfactual affordances**  
→ **cultural, conceptual and abstract affordances**

This should not be treated as a rigid sequence. These spaces overlap and recursively enable one another. But there is a plausible bootstrapping logic.

Reliable bodily agency allows controlled interventions on objects. Object manipulation reveals causal regularities. Other agents introduce partially observable causal systems whose responses depend on belief, intention, relationship and history. Language makes absent, hypothetical and abstract states manipulable. Culture exposes the learner to enormous inherited possibility spaces that no individual could discover alone.

The object of play can therefore become progressively less obviously physical without requiring a fundamental discontinuity in the exploratory process.

A child tests whether she can jump from a wall.

Later she tests what two objects can be made to do together.

Later she tests what another child will do in response to a social move.

Later she tests what happens if everyone agrees that the sofa is a ship.

Much later, an adult may test a mathematical conjecture, improvise music, construct a fictional society, modify a software architecture, or build an artificial organism.

The outward behaviours are radically different. The computational motif may remain recognisable:

**generate intervention → observe consequence → update model → seek another tractable uncertainty.**

## Human neoteny

This provides a potentially useful interpretation of human neoteny.

Play is not exclusively human, and adult play occurs in other species, especially social mammals. But humans combine prolonged development with unusually extended plasticity and cultural learning. The relevant possibility is not merely that adult humans still play. Human neoteny may help preserve a **developmental mode of information-seeking after basic sensorimotor competence has been achieved**.

Rather than terminating, exploration is repeatedly redirected toward whatever newly reachable space still contains structured uncertainty.

What changes with maturation may therefore be not the presence of play, but **where the edge of play lives**.

This gives a possible continuity between childhood running-around and adult science, engineering, art, fiction, games, conversation and hobby research. These can remain playful in the deep sense: bounded interventions into a possibility space where the immediate reward includes discovering what happens.

## Important qualification

The evolutionary and psychological relationship between curiosity, exploration and play should not be collapsed into a single construct. Play also serves social bonding, practice, affect regulation, competition, creativity, signalling and probably multiple other functions.

Therefore REE should not encode the strong equation:

`play = information gain`.

A more defensible hypothesis is:

> **An intrinsic drive toward learnable uncertainty may be one important generative substrate from which substantial classes of play emerge.**

## Relevance to REE

REE already contains several unusually appropriate ingredients.

REE version 3 defines E2 around self-relevant forward modelling, affordances and action-conditioned consequences. Hippocampal and residue systems preserve experience and support trajectory proposals, while offline integration is already architecturally explicit.

The current v3 specification also contains a hippocampal curiosity drive (`SD-025 / ARC-057`) built around representational density and unfamiliarity, with familiarity raised on waking visits and an anti-perseveration role. Thus this thought does **not** imply that REE needs a generic curiosity variable invented from scratch.

What may be missing is the developmental interpretation and the machinery that lets exploration migrate across affordance spaces.

### 1. Curiosity should be self-relative

Information value should concern the coupled self-world system rather than the external environment alone. A change in the self can make previously learned environmental relations uncertain again.

This suggests that E1/E2 may eventually need uncertainty over action consequences conditional on current self-state, not merely novelty or uncertainty about places.

### 2. Development should be capable of generating its own curriculum

The agent need not necessarily be told:

> first learn movement, then objects, then agents.

Intrinsic-motivation work suggests that learning progress can generate ordered developmental transitions as currently learnable domains become mastered and attention migrates elsewhere.

For REE this is especially attractive because externally imposed developmental stages risk becoming hidden oracles. Progression may instead emerge because new capacities alter which parts of the possibility space are reachable, uncertain, learnable, safe enough to investigate, and consequential enough to retain.

### 3. Play may emerge without a play module

REE may not require an explicit command called `PLAY`.

Play-like behaviour could arise when:

- basic viability is sufficiently secure;
- no urgent commitment dominates action selection;
- spare behavioural capacity is available;
- reachable states contain model uncertainty;
- exploration is predicted to produce learning;
- repetition loses value when useful information is exhausted.

Under those circumstances an agent should sometimes select an action principally because **the resulting observation will teach it something**.

That would be a stronger result than programming play behaviour directly.

### 4. Mastery should move, not extinguish, curiosity

Pure novelty seeking easily degenerates into random wandering. Pure uncertainty seeking can repeatedly select impossible or inherently stochastic situations.

Learning progress or reducible uncertainty may be a better target. Once one affordance class becomes predictable, its intrinsic value should decline and exploration should migrate toward adjacent possibilities whose uncertainty has recently become tractable.

This supplies a computational interpretation of the moving frontier of play.

### 5. Objects and other agents expand the affordance landscape

An object's affordances depend on body capability, goal, context, other objects, learned tool use, other agents and shared conventions.

Social agents enlarge the space more dramatically because their behaviour changes in response to the learner. Social play may therefore become a particularly information-rich regime: actions probe not only physics but **conditional models of other minds**.

This provides a possible developmental bridge between embodied affordance learning and later REE social cognition.

### 6. Counterfactual play may internalise exploration

Once a sufficiently capable forward model exists, every information-seeking intervention need not be physically executed.

The system can begin to play internally:

- recombine objects;
- simulate alternate trajectories;
- rehearse social encounters;
- perturb assumptions;
- invent situations;
- test counterfactual outcomes.

Pretend play may be especially interesting as a developmental transition in which affordance exploration begins operating over decoupled representations rather than only the immediately present world. Later abstract reasoning may represent a further expansion of the same capability.

### 7. Sleep and replay may metabolise play

A large amount of exploratory experience need not produce immediate explicit learning. Spontaneous activity can generate a rich experiential corpus from which later replay or offline integration extracts regularities, reorganises representations, updates confidence and recombines trajectories.

REE already contains substantial sleep/replay machinery, making it possible eventually to test a two-stage process:

**waking:** generate diverse, informative experience  
**offline:** consolidate, re-bucket, compare, counterfactually recombine and update affordance models.

This links naturally with the broader REE idea that sleep is more than passive consolidation.

## REE itself as an example

There is a recursive observation worth preserving.

REE itself is being produced through an adult instance of the phenomenon under discussion. A mechanism is imagined, implemented, observed, perturbed and compared with alternatives. Unexpected behaviour opens another question. Biological literature supplies another affordance for thought. A newly constructed subsystem makes previously inaccessible questions investigable.

The frontier moves from prediction to agency, memory, commitment, harm, sleep, development, social inference, cooperation, language and increasingly abstract questions.

The activity remains recognisably playful despite becoming technically elaborate.

This is not evidence for the biological hypothesis. It is an analogy. But it makes the central idea tangible:

> **Human adulthood may preserve the exploratory developmental mode while allowing its objects to become increasingly abstract. REE is simultaneously a product of that process and an attempt to build an architecture in which an analogous process might occur.**

## Candidate architectural consequences and tests

These should be treated as questions for intake rather than prematurely promoted claims.

1. **Self-relative affordance uncertainty:** determine whether E1/E2 currently maintain enough uncertainty about action consequences conditional on changing self-state.
2. **Learning-progress signal:** compare the existing hippocampal curiosity drive with expected information gain, prediction-error reduction and competence-progress formulations. Density × unfamiliarity may be insufficient to generate a developmental curriculum.
3. **Intrinsic curriculum experiments:** construct environments in which bodily affordances become learnable before object affordances, and object affordances subsequently unlock richer causal possibilities. Test whether exploration migrates without stage-specific rewards.
4. **Play-without-play test:** ask whether a safe, satiated REE agent with spare capacity spontaneously performs informative actions with no immediate extrinsic payoff.
5. **Anti-randomness discriminator:** demonstrate that behaviour preferentially samples *learnable* uncertainties rather than merely novel or stochastic states.
6. **Recalibration experiment:** alter a stable property of the agent's body/action model after competence is established and test whether affordance exploration selectively returns to the affected region.
7. **Frontier migration metric:** measure whether intrinsic exploration shifts from bodily/action variables toward object, causal and eventually social variables as earlier prediction errors and learning progress saturate.
8. **Offline integration:** test whether exploratory waking experience produces improved affordance calibration after sleep/replay without additional waking reward.

These need not all belong to v3. The normal thought-intake process should decide which are prerequisites of the current architecture and which belong to later developmental, social or cognitive stages.

## Strongest formulation

The central proposition is not:

> Children run around because they have excess energy.

Nor simply:

> Children run around because they are practising movement.

It is:

> **A developing organism must discover what actions its changing body makes possible. Intrinsically rewarding exploration provides the data required to learn those self-relative affordances. This exploration is already a form of play. As bodily affordances become predictable and new representational capacities emerge, the informational frontier of play can migrate into objects, causal combinations, other agents, symbols and abstractions. Human neoteny may preserve this developmental exploratory regime unusually far into adulthood.**

For REE, the corresponding architectural proposition is:

> **Do not teach an artificial developing organism how to play. Give it a self whose capabilities can be uncertain, a world whose affordances can be learned, sufficient safety to explore, an intrinsic preference for reducible uncertainty or learning progress, memory and offline integration, and increasingly rich reachable domains. Then ask whether play—and the migration of its frontier—appears.**

## Literature anchors for later intake

The thought arose from a synthesis of several established literatures rather than from a single source. A formal intake should revisit and cite primary sources on:

- affordance learning and locomotor calibration in infancy, including work by Karen Adolph and colleagues;
- changes in perceived affordances as infant body dimensions and locomotor competence change;
- developmental cascades following self-produced locomotion;
- children's information-sensitive exploratory play and causal intervention;
- intrinsic motivation, curiosity, expected information gain, competence progress and learning progress;
- developmental robotics work showing self-organised curricula from intrinsic motivation;
- comparative and adult social play;
- prolonged human development, plasticity and behavioural neoteny.

The key synthesis to preserve during intake is the **migration of the play frontier**: bodily → object → social → symbolic/counterfactual → abstract affordance spaces, with a potentially conserved information-seeking mechanism operating over progressively richer representations.
