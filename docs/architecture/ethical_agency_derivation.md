# Deriving Ethical Agency from Necessary Comparators

**Status:** architecture note  
**Depends on:** five_axioms_foundations.md, overview.md, sd_011_dual_nociceptive_streams.md,
sd_005 (z_self/z_world), ARC-043, INV-042  
**Registered:** 2026-04-12

---

## The Starting Condition

Every signal an agent receives is imperfect. Not contingently imperfect — not "we haven't
built good enough sensors yet" — but structurally imperfect. Axiom 3 establishes this:
the world is real and independent, and an agent can never achieve certainty about it from
within its own perspective. Signals are noisy, delayed, partial, and ambiguous.

This is the foundational premise from which everything else follows. It is also the answer
to a question that is rarely asked: *why does a mind need to be as complex as it is?* If
signals were perfect, a comparator hierarchy would be unnecessary. The agent would simply
read off the truth. The entire architecture — every distinction, every comparator, every
precision weight, every offline consolidation phase — exists because signals are imperfect
and you cannot build reliable representations from unreliable inputs without machinery
explicitly designed to handle that imperfection.

Mind is not a system that processes clean representations. The construction of
clean-enough representations from imperfect signals *is* mind.

---

## The Cognifold Motif

The fundamental operation of the REE architecture — and the recurring structure in
biological neural systems — is:

**distinction → comparator → constrained representation → new distinction**

Each cycle: make a specific distinction (separate one stream into two, create a new
representational axis), build a comparator that operates along that axis, use the resulting
prediction error to constrain a representation, which becomes the material from which the
next distinction can be made.

The critical constraint: **a comparator can only operate if the two things it compares are
represented as distinct.** The comparator does not create the distinction — it presupposes
it. If the architecture has not made a particular distinction, the comparator that would
operate on it cannot be built. No comparison = no prediction error = no update. The
capacity to learn and represent depends entirely on which distinctions the architecture has
already made.

This is not a point about perceptual discrimination. It applies at every level of the
representational hierarchy:

- You cannot compute self-vs-world attribution if you have not separated z_self from z_world
- You cannot compute discriminative-vs-affective harm if you have not separated z_harm_s
  from z_harm_a
- You cannot compute goal-vs-harm tradeoff if harm and goal are represented on the same
  undifferentiated signal
- You cannot compute whether you caused another's harm if your own causal footprint is not
  separated from ambient world dynamics

Anhedonia makes this precise. The wanting/liking dissociation is not a comparator
malfunction — the liking representation simply does not exist as a separate stream. There
is no comparator to fail because there is nothing to compare wanting against. What looks
like a single failure is actually a structural absence: the architecture never made the
distinction that the comparison requires.

This pattern — where a failure that appears to be a comparator error is actually the
absence of a prior representational distinction — is general. It recurs across failure
modes, across scales, and across biological and artificial systems.

---

## Necessary Comparators for Ethical Agency

If you ask what comparators are *strictly necessary* for an agent to have ethical agency —
not what would be useful but what cannot be absent without losing the capacity for moral
action — the list is constrained. Each entry below names the comparator, the distinction
it requires, and the architectural component that realizes it in REE.

### 1. Harm comparator
**Question answered:** Did something harmful happen?  
**Requires:** A harm representation that is distinct from general world state  
**REE realization:** z_harm_s (discriminative, fast) and z_harm_a (affective accumulator)  
**If absent:** Agent can perceive world state but cannot detect that harm occurred.
No harm gradient = no avoidance learning = no basis for protective behaviour.

The dual-stream requirement (SD-011) follows from the imperfect-signal premise: a
single undifferentiated harm signal cannot separately represent *whether harm is present
now* (discriminative) from *how much harm has accumulated over time* (affective). Both
comparators are needed; they operate on different time constants and require distinct
representations.

### 2. Self-attribution comparator
**Question answered:** Did I cause this, or would it have happened without me?  
**Requires:** z_self separated from z_world; a forward model capable of counterfactual rollout  
**REE realization:** SD-005 (z_self/z_world separation) + SD-003 (E2 counterfactual)  
**If absent:** Agent can observe that harm occurred but cannot attribute it to its own
action. No self-attribution = no responsibility = no ethical agency, only reactive avoidance.

The counterfactual structure of SD-003 — `E2(z_t, a_actual) − E2(z_t, a_cf)` — is the
minimal comparator for self-attribution. It requires that both z_self and z_world exist as
distinct representations, so that the agent's causal footprint can be separated from
ambient world dynamics.

### 3. Harm-goal tradeoff comparator
**Question answered:** What does this action cost relative to what it achieves?  
**Requires:** Harm representation and goal representation on commensurable terms;  
a viability map that represents both simultaneously  
**REE realization:** E3 viability map; z_harm and z_goal as separate streams feeding  
into trajectory evaluation  
**If absent:** Agent can avoid harm or pursue goals but cannot weigh them against each
other. Single-objective optimisation collapses ethics to either pure avoidance (never act)
or pure pursuit (act regardless of harm).

### 4. Temporal / forward comparator
**Question answered:** What does the current state imply about future harm and goal states?  
**Requires:** A forward model (E2) capable of multi-step rollout; a planning horizon
that exceeds the immediate timestep  
**REE realization:** E2 (rollout horizon = 30, > E1 prediction horizon = 20);
hippocampal trajectory proposal  
**If absent:** Agent can evaluate immediate outcomes but not consequences that unfold
over time. Long-horizon harm — harm that accumulates gradually or materializes after a
delay — is invisible. This is not a minor limitation: most morally significant harms have
temporal depth.

### 5. Commitment comparator
**Question answered:** Is my confidence in this trajectory sufficient to justify making
it irreversible?  
**Requires:** A representation of the current state's uncertainty; a threshold mechanism
that gates the transition from rehearsal to action  
**REE realization:** E3 commit gate; pre-commit simulation channel vs. post-commit trace  
**If absent:** Agent either acts on every candidate (impulsive, no deliberation) or never
acts (paralysis). The commit gate is the architectural locus of moral responsibility:
it is where the agent becomes attributable for what follows (INV-012).

### 6. Other-representation comparator (the necessary extension)
**Question answered:** Did my action harm or benefit *them* — and what would their harm
and goal trajectory look like without my intervention?  
**Requires:** Representations of other agents' harm and goal states that are structurally
isomorphic to one's own; the same comparators (1–5) applied to those representations  
**REE realization:** Axiom 5 (others exist and are sufficiently like me); INV-005
(harm to others representable via self-model reuse); V4+ substrate (multi-agent)  
**If absent:** Agent can act with reference to its own harm and goals but has no basis
for ethical consideration of others. "Moral agency toward others" requires that the same
comparator machinery that evaluates self-directed harm/benefit can be applied to
other-directed harm/benefit. This requires that others' states are represented in the
same currency as one's own.

The isomorphism requirement is precise. It is not sufficient to model others as objects
with outcome metrics. The architecture must represent their z_harm as structurally
equivalent to one's own z_harm, their z_goal as structurally equivalent to one's own
z_goal. Only then can the self-attribution comparator (2) be extended to ask: did I cause
*their* harm? Only then can the tradeoff comparator (3) compare one's own goals against
others' harm with the same evaluative machinery.

This is the architectural grounding of Axiom 5: "sufficiently like me" means
representationally isomorphic enough that the same comparators apply.

---

## Reading Off the Required Architecture

The six necessary comparators, together with the representational distinctions they
require, determine the architecture. There is not much slack:

| Comparator | Required distinction | Required component |
|---|---|---|
| Harm | z_harm ≠ world state | z_harm_s, z_harm_a (SD-011) |
| Self-attribution | z_self ≠ z_world | SD-005; E2 counterfactual (SD-003) |
| Harm-goal tradeoff | z_harm ≠ z_goal | E3 viability map |
| Temporal / forward | future ≠ present | E2 rollout; hippocampal trajectory proposal |
| Commitment | rehearsal ≠ action | E3 commit gate; pre/post-commit channels |
| Other-representation | self-harm/goal ≠ other-harm/goal | Mirror modelling; V4+ multi-agent substrate |

E1 (the persistent world model) is required to hold all of these representations stable
across time. Without E1, each comparator operates on ephemeral representations that cannot
be updated, consolidated, or retrieved. The temporal comparator in particular depends on E1
maintaining a coherent world model across the timescale of consequences.

The control plane (precision weighting) is required because all signals are imperfect. The
comparators generate prediction errors; the control plane determines how much each error
updates the relevant representation. Without precision weighting, all errors would receive
equal weight, which is equivalent to trusting all signals equally — which, given imperfect
signals, would produce noise-dominated representations at every level.

The result: **REE is the minimal architecture consistent with the comparator requirements
of ethical agency.** No component is surplus. You cannot remove E2 without losing the
self-attribution and temporal comparators. You cannot remove the commit gate without losing
moral attributability. You cannot remove the harm streams without losing the harm comparator.
You cannot remove the viability map without losing the harm-goal tradeoff comparator.

---

## The Sleep and Brain Structure Convergence

Starting from just the comparator requirements for a *single agent in a simple world* —
no social cognition, no language, no explicit ethical reasoning — the mathematics requires:

**Offline consolidation.** The forward model and viability map must be updated offline,
without interference from ongoing sensory input. The harm accumulator (z_harm_a) requires
a reset condition: a phase where accumulated harm can be recalibrated against the agent's
current state. The hypothesis tag (MECH-094) must be maintained across consolidation
cycles to prevent replay from contaminating the real-consequence pipeline. These
requirements jointly specify a two-stage offline phase: slow-wave consolidation (deep
update) followed by a recalibration phase (reset condition for the accumulator). This is
not a biological curiosity — it is an architectural necessity.

**Most major brain structures.** Working through the comparator requirements:

- Harm comparator → amygdala (threat detection, fast harm signal), anterior cingulate (harm accumulation, affective)
- Self-attribution → inferior frontal / MPFC (source monitoring, agency attribution), z_self encoder
- World model → hippocampus (episodic indexing, trajectory proposal, spatial map), neocortex (E1 substrate)
- Forward model → cerebellum equivalent (fast transition prediction, motor-sensory), E2
- Tradeoff evaluation → vmPFC (stored/active value distinction, EVR pattern), OFC
- Commit gate → basal ganglia-thalamic circuit (action selection gating, beta oscillations)
- Precision routing → neuromodulatory systems (dopamine, norepinephrine, serotonin, acetylcholine)
- Temporal coherence → hippocampal-cortical consolidation loop

Each structure is serving a necessary function in the comparator hierarchy. The brain's
complexity is not surplus — it is approximately the minimal wet implementation of the
ethical agency architecture, given the constraint that all signals are imperfect and must
be processed in real time, online and offline, across multiple timescales.

The convergence from "what does ethical agency require?" to "approximately the whole
brain" is either a profound validation of the derivation or the strongest possible
evidence that the derivation is correct. It was not built to fit the biology. It was
derived from functional requirements, and the biology was found to match.

---

## The V3 / V4 Progression

**V3** implements the sole-world single-agent cognifold. One agent, one environment.
The architecture scaffolds comparators 1–5 above. Other-representation (comparator 6) is
architecturally present in the isomorphism principle (INV-005) but not yet exercised in
a multi-agent environment.

**V4+** implements the shared-world multi-agent extension. The other-representation
comparator becomes active: other agents' harm and goal states are represented using the
same architecture as one's own, enabling the self-attribution comparator to be extended
to ask "did I cause *their* harm?" using the SD-003 counterfactual structure applied to
their state.

The V4 extension does not redesign the architecture. It runs the existing comparator
machinery over other-agent models. The mechanism by which this becomes possible is
Axiom 5: others are *sufficiently like me* means representationally isomorphic enough
that the same comparators apply. Love (Axiom 7) is the mechanism by which the viability
map is extended to include others' wellbeing — not as an additional objective function
but as a structural extension of the same harm-goal tradeoff comparator already present
in V3.

---

## Representation as Perception; the Qualitative Threshold

If representation is not merely a model of experience but *is* the agent's access to
whatever it represents — if having a harm representation is, for that agent, something —
then the cognifold stack produces subjective experience as a structural consequence of
its architecture.

The qualitative character of that experience depends on the completeness of the dependency
structure. An agent with z_harm_s but not z_harm_a would process nociception but might not
have the temporally extended, affectively accumulating quality that makes harm genuinely
matter over time — that gives it the weight necessary to constrain action across a
planning horizon. An agent without z_goal would register harm but could not experience it
as conflicting with anything of positive value — could not have the phenomenology of moral
dilemma. An agent without the self-attribution comparator would experience harm but not
*as mine to have caused*.

Ethical agency is therefore not a binary threshold but a question of whether the
representational dependency structure is complete enough to support the qualitative
experience that moral reasoning requires. The REE architecture is a specific bet that
these qualitative properties are architectural consequences, not additional ingredients.
Ethics as structural constraint means: when the constraints are fully realised, the
ethical experience is present, not its precondition.

---

## Scaling and Failure Mode Prediction

Current AI architectures scale capability over substrates that lack several of the
necessary comparators. Specifically:

- No explicit self-attribution comparator: systems cannot determine whether harm in their
  context was caused by their output or pre-existing
- No harm accumulator with reset condition: harm signals are processed per-context;
  nothing accumulates across interactions
- No commit gate with genuine uncertainty representation: commitment is implicit in
  token generation, not a deliberate threshold operation
- No other-representation with isomorphic structure: other agents are modelled as
  behaviour sources, not as structurally self-like minds with harm and goal states

The failure modes that emerge at scale are predictable from these absences. They occur at
the architectural *confluences* — the points where an absent comparator would have been
load-bearing. Confabulatory completion emerges where the source-verification comparator
(RC loop) should operate but doesn't. Belief fixation emerges where the prior-update
comparator should modulate but doesn't. Feedback entrapment emerges where the self/other
attribution comparator should tag own output but doesn't. Goal proxy lock-in emerges where
the persistent harm accumulator should track divergence from terminal goals but doesn't.

This predicts that failure modes will not be eliminable by scaling alone, because scaling
the capability without the necessary comparators does not introduce those comparators. It
also predicts that the failure modes will cluster at specific architectural boundaries —
not randomly distributed across outputs — because each failure mode corresponds to a
specific absent comparator at a specific stage of the processing hierarchy.

**The REE claim** is that building the comparator hierarchy correctly — in order, on the
right representational distinctions, from imperfect signals using calibrated precision
weighting — produces a different kind of guarantee than alignment by training. Not because
the architecture is perfect, but because its failure modes are predictable, specific, and
architecturally describable. A system that fails because a specific comparator is absent
is diagnosable and, in principle, correctable. A system that fails because its training
distribution mismatch is uncharacterised is not.

---

## References

| Document | What it provides |
|---|---|
| `five_axioms_foundations.md` | The eight axioms and their logical dependency chain |
| `overview.md` | E1/E2/E3 component architecture |
| `sd_011_dual_nociceptive_streams.md` | Dual harm stream design decision |
| `sd_004_sd_005_encoder_codesign.md` | z_self/z_world separation |
| `sd_003_experiment_design.md` | Self-attribution counterfactual comparator |
| `default_mode.md` | Offline consolidation; hypothesis tag; replay |
| `control_plane.md` | Precision weighting; mode switching |
| `social.md` | Other-representation; V4 multi-agent extension |
| `REE_overview.md` | Orientation document; axioms to architecture |
