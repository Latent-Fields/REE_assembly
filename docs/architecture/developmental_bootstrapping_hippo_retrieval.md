---
nav_exclude: true
---

# Developmental Bootstrapping and Hippocampal Cue-Indexed Trajectory Retrieval

**Date:** 2026-05-15
**Session:** design-doc-dev-bootstrap-hippo-retrieval-2026-05-15T201135Z
**Status:** Draft -- claims INV-073, MECH-325, MECH-326, ARC-072 registered (candidate)
**Lit source:** evidence/literature/targeted_review_developmental_exploration_hippocampal_retrieval/

---

## 1. The Problem This Document Addresses

REE's monostrategy problem (MECH-269, EXQ-561 cluster) is not a runtime diversity failure.
It is a map-population failure: the hippocampal trajectory store has not been populated with
sufficiently diverse options for the policy to switch between them at inference time.

This document synthesises the literature establishing (a) WHY this happens
(developmental bootstrapping gap), (b) WHAT the correct architecture looks like
(hippocampal cue-indexed trajectory retrieval + PFC context gating), and (c) WHERE
REE's current substrate diverges from it.

---

## 2. Developmental Bootstrapping (INV-073)

### 2.1 The biological argument

All motor-competent vertebrates studied so far require a dedicated developmental epoch --
babbling in humans, subsong in songbirds -- in which the motor system produces
high-variability output before reinforcement learning narrows the repertoire. The function
of this epoch is not noise production but trajectory library population.

Three lines of evidence converge:

**Causal necessity (Doupe & Kuhl 1999, Annual Review of Neuroscience)**
Silencing LMAN -- the BG-driven variability generator in juvenile songbirds -- during
subsong arrests repertoire formation and produces a permanently impoverished, stereotyped
song. The monostrategy signature is irreversible in adults if the developmental window is
missed. The BG-driven variability epoch is not incidental to learning; it is the mechanism
that populates the option library before reinforcement begins to select from it.

**Motor exploration opens sensory learning (Leitao & Gahr 2024, PNAS)**
Administering testosterone to juvenile zebra finches induced premature motor vocal
exploration; these birds memorised the tutor song earlier and more faithfully than
controls. Motor exploration is causally upstream of perceptual template formation, not
downstream of it. An agent that skips or abbreviates the exploration epoch does not
merely have a thin option store -- it also fails to form the perceptual templates that
later serve as retrieval cues.

**Severed feedback loop --> single attractor (Warlaumont & Finnegan 2016, PLoS ONE)**
A spiking-network computational model of babbling acquisition: when own-voice auditory
feedback was blocked (simulating deafness or tracheostomy), the model collapsed to a
single low-diversity attractor instead of developing canonical babbling. The motor
exploration epoch converges to a diverse repertoire ONLY when the intrinsic
reward signal (auditory salience of own output) remains closed.

### 2.2 The claim (INV-073)

> Any model-building agent that must flexibly select from multiple behavioral options
> requires a dedicated developmental exploration phase in which diverse behavioral
> candidates are executed and evaluated via closed-loop sensory feedback. An exploration
> epoch that is too short, too narrow, or that has its feedback loop severed permanently
> restricts the option library available at inference time.

Invariant type: emergent (follows from optimization dynamics + closed-loop feedback
requirement; not derivable from ethics axioms or from physics alone).

lit_conf: 0.76. Primary anchors: Doupe & Kuhl 1999 (conf 0.78), Leitao & Gahr 2024
(conf 0.76), Warlaumont & Finnegan 2016 (conf 0.70).

**Li et al. 2007 (Behavioural Pharmacology)** provides the outcome-side prediction: rats
reared in social isolation performed normally on initial visual discrimination acquisition
but showed a specific deficit in reversal learning -- they could learn one strategy but
could not switch to another when contingencies changed. The developmental impoverishment
(insufficient post-weaning exploration) produced permanent behavioral rigidity. Initial
acquisition unimpaired; update failure is the diagnostic signature.

**Wang et al. 2017 (Behavioural Brain Research)** provides the dissociation: novelty
enrichment (varied sensory-motor challenges) specifically reduced the "never tried this
option" failure mode; social enrichment alone did not expand the option store in the same
way and in some conditions increased perseveration. The type of early experience matters --
the relevant variable is motor-sensory option diversity, not social contact.

---

## 3. Hippocampus as Cue-Indexed Trajectory Library (MECH-325)

### 3.1 The biological argument

The hippocampus is not a passive archive indexed by past-event timestamps. It is a
content-addressable system where context/goal cues pattern-complete to retrieve stored
trajectory templates.

**Hippocampus as imagination system (Buckner 2010, Annual Review of Psychology)**
Hippocampus and associated cortex activate when people envision future events; hippocampal
damage specifically impairs future-event imagination, not just past-event recall. In rats,
hippocampal ensembles preplay event sequences before goal-directed navigation -- sequences
that, if combined in novel ways, provide planning building blocks. The hippocampus is a
generator of possible sequences indexed by context, not an archive indexed by time.

**Forward/reverse replay learning gradient (Shin, Tang & Jadhav 2019, Neuron)**
Simultaneous recording from 200+ CA1 and mPFC neurons during spatial alternation task
acquisition. During inter-lap pauses, hippocampal replay performs an internal search.
Reverse replay (evaluating past paths) peaks early in learning; forward replay (planning
future paths) peaks as proficiency develops. By the end of learning, forward replay
specifically discriminated correct future paths from alternative choices. PFC theta
coherence during forward replay predicted subsequent correct choice. This is the
cue-indexed retrieval signature: hippocampus is not replaying the recent past but
retrieving trajectory templates appropriate for the upcoming context.

**Imagination beyond recall (Comrie, Frank & Kay 2022, Phil Trans R Soc B)**
Hippocampal firing patterns regularly correspond to paths not taken, locations not
currently occupied, and novel path combinations -- not merely replays of actual past
paths. The hippocampus generates hypothetical-trajectory events during active behaviour,
rest, and at decision points. Episodic memory and spatial navigation are special cases of
a more general cue-queryable imagination system.

### 3.2 The claim (MECH-325)

> In the REE architecture, the hippocampal module should function as a content-addressable
> trajectory store: PFC context/goal cues pattern-complete against the stored library to
> retrieve trajectory templates appropriate for the current context. Different PFC context
> states should retrieve different trajectory subsets, enabling context-differentiated
> behavioral option selection without regenerating trajectories from scratch each tick.

Note: this claim is at the implementation_phase: v4 boundary. The current V3
HippocampalModule (ARC-007 STRICT) is a CEM generator that produces value-flat proposals
fresh each tick by navigating residue-field terrain. MECH-325 describes the architectural
upgrade required for full cue-indexed retrieval.

lit_conf: 0.82. Primary anchors: Shin/Jadhav 2019 (conf 0.84), Buckner 2010 (conf 0.82),
Comrie/Frank 2022 (conf 0.77).

---

## 4. PFC Top-Down Bias as Hippocampal Retrieval Gate (MECH-326)

### 4.1 The biological argument

The PFC does not compute responses directly. It maintains active representations of goals
and task rules that send top-down bias signals to downstream regions, shaping which
input-output mappings are active for a given context. In the hippocampal context, this
bias signal determines which trajectory templates are retrieved or replayed.

**PFC bias mechanism (Miller & Cohen 2001, Annual Review of Neuroscience)**
PFC neurons fire selectively for task rules -- not sensory features -- and maintain this
activity across delay periods. This maintained representation sends top-down projections
to posterior cortex, motor cortex, and subcortical structures, biasing activity toward
context-appropriate mappings. Working memory, attention, inhibitory control, and task
switching are all instances of the same underlying bias mechanism. The same circuit
architecture that gates sensory-motor cortex routing applies to hippocampal retrieval:
different PFC context states should produce different hippocampal retrieval content.

**PFC gates hippocampal replay content (Zielinski, Tang & Jadhav 2018, Hippocampus)**
Review from the Jadhav lab explicitly framing hippocampal-PFC interaction as the mechanism
for context-dependent memory retrieval and behavioral flexibility. The paper documents that
coordinated hippocampal-PFC SWR activity during inter-trial pauses predicts upcoming
correct choices, and proposes that PFC context state gates which hippocampal sequences
are replayed. Forward/reverse replay dissociation mirrors REE planning horizon: theta
sequences handle local deliberation (which immediate step); forward SWR replay handles
longer trajectory retrieval (which full path to goal).

**Theta sequence encoding of alternatives (Tang, Shin & Jadhav 2021, eLife)**
First demonstration of theta-timescale prospective coding in PFC. At decision points,
hippocampal theta sequences encoded alternatives for deliberation -- not just the current
path. PFC theta sequences simultaneously predicted upcoming choices and were coordinated
with hippocampal alternatives. This is the cue-differentiation mechanism at neural
implementation level: PFC provides a bias that steers which hippocampal theta sweep is
selected. Inter-trial replay impairment before error trials supports the claim that
retrieval quality gates behavioral flexibility.

### 4.2 The claim (MECH-326)

> REE's E3 planner must implement a PFC-analog top-down bias signal that gates which
> trajectory templates are retrieved from the hippocampal store. The bias signal is derived
> from the current goal representation (z_goal) and task context, and it steers retrieval
> toward templates appropriate for that context. Without this routing, the hippocampal
> trajectory library is queried uniformly regardless of goal state -- producing the same
> option set in all contexts and leaving the diversity gap unaddressed.

implementation_phase: v4. Depends on MECH-325 (the store must exist before it can be
gated).

lit_conf: 0.82. Primary anchors: Miller & Cohen 2001 (conf 0.84), Zielinski/Jadhav 2018
(conf 0.79), Tang/Jadhav 2021 (conf 0.82).

---

## 5. REE's Current Architecture: Two Inter-Dependent Gaps (ARC-072)

### 5.1 Gap 1: No diversity-bootstrapping phase

REE's HippocampalModule (V3) is a CEM generator. It produces K trajectory candidates
each tick by iterative refit of a Gaussian in action-object space, guided by the terrain
prior (residue_val, z_world, e1_prior -> action_object_mean). The CEM collapses to
one dominant action class per seed (EXQ-561 cluster) because it re-uses the same
distribution each tick from the same starting point and re-fits toward the same terrain
gradient. There is no mechanism to populate a diverse trajectory store during an early
exploration epoch; there is no intrinsic diversity reward that would prevent repertoire
collapse during that epoch.

The monostrategy experiments (MECH-269, EXQ-561 cluster) are the diagnostic signature
of Gap 1. The EXQ-563 series (support-preserving CEM) is addressing the symptom --
keeping candidate set diverse within each tick -- but does not address the root cause:
a trajectory library that was never populated with diverse options in the first place.

### 5.2 Gap 2: No cue-indexed retrieval

SD-016 introduced `cue_action_proj` as the PFC-to-hippocampus affordance bias route.
The path is broken: EXP-0155 confirmed zero gradient through the CEM argmax. PFC goal
cues cannot steer action generation because CEM candidate selection is non-differentiable.
The architecture has the structural hook (`cue_action_proj` weight) but the computational
route is severed.

MECH-292/293 (ghost-goal bank and probes) is the closest V3 approximation to cue-indexed
retrieval: it seeds CEM from past goal-location anchor z_world representations. But the
retrieval is by goal-location proximity in the current observation, not by an arbitrary
PFC context cue. This is spatial-context-indexed, not general cue-indexed.

### 5.3 Why the gaps are inter-dependent

Gap 2 (broken cue routing) implies Gap 1 (thin library): the feedback loop that would
populate the trajectory store with diverse options is the same closed loop that is severed
in Gap 2. An agent cannot populate a diverse library via CEM if CEM ignores the cue
signal that should diversify what it generates. The Warlaumont & Finnegan (2016) analogy
is direct: severed auditory feedback -> single attractor; severed PFC cue gradient ->
CEM collapses to same action class regardless of context.

### 5.4 The claim (ARC-072)

> REE lacks two inter-dependent architectural components for behavioral diversity:
> (1) a dedicated developmental exploration epoch with an intrinsic diversity reward
> that populates the hippocampal trajectory store before reinforcement narrows the
> repertoire; and (2) a differentiable cue-indexed retrieval path from PFC context
> representation to trajectory generation, so that different goal states retrieve
> different candidate sets. The monostrategy findings (MECH-269, EXQ-561 cluster) are
> diagnostic of gap (1); EXP-0155 zero-gradient cue_action_proj is diagnostic of gap (2).
> Addressing gap (2) alone (support-preserving CEM, EXQ-563 series) treats the symptom
> but does not resolve the root cause.

implementation_phase: v4. This claim sets the V4 architectural scope for the diversity
cluster and scopes the required V3-diagnostic experiments for the two gaps.

lit_conf: 0.74. Convergent from Doupe/Kuhl 1999, Warlaumont/Finnegan 2016,
Shin/Jadhav 2019.

---

## 6. Relationship to Existing Claims

| New claim | Primary relationship | Key existing claims |
|-----------|---------------------|---------------------|
| INV-073 | upstream cause of MECH-269 monostrategy | MECH-269 (V_s monostrategy), ARC-065 (diversity stack) |
| MECH-325 | architectural upgrade target for ARC-007 | ARC-007 (value-flat proposals), MECH-292/293 (ghost probes) |
| MECH-326 | architectural upgrade for SD-016 cue routing | SD-016 (cue_terrain_proj / cue_action_proj), ARC-016 (dynamic precision), MECH-025 |
| ARC-072 | names the gap cluster; scopes V4 diversity work | ARC-065, MECH-269, SD-016, EXQ-563 series |

The EXQ-563 series (support-preserving CEM) and EXQ-567 (natural entropy measurement)
are valid V3 diagnostic experiments that quantify Gap 1 severity. They do not close
Gap 2, but they establish whether Gap 1 alone is sufficient to explain the monostrategy
finding, or whether Gap 2 also contributes independently.

---

## 7. V4 Architectural Requirements (derived from ARC-072)

These are design-level requirements, not yet substrate decisions. They establish what V4
must implement to address both gaps.

**R1 -- Trajectory library structure (MECH-325)**
A persistent data structure (e.g., episodic buffer with cue-indexed access) that stores
(trajectory, context-cue, outcome-value) tuples accumulated during an explicit exploration
epoch. The cue-key must be a representation that allows pattern-completion from a novel
partial cue (content-addressable, not exact-match).

**R2 -- Diversity-bootstrapping epoch (INV-073)**
An early training phase with elevated intrinsic diversity reward (e.g., action-type
entropy bonus, trajectory dissimilarity reward) that populates R1 before task-reward
begins to narrow the repertoire. The epoch must last long enough that diverse options
are self-sustaining (the Warlaumont & Finnegan stability criterion).

**R3 -- Differentiable PFC-to-retrieval path (MECH-326)**
Replace or supplement CEM argmax with a differentiable retrieval operation: e.g.,
attention over the trajectory library keyed by z_goal, or a differentiable sampling
step (Gumbel-softmax) over stored trajectory indices. This restores the gradient path
from SD-016's cue_action_proj to actual trajectory generation.

**R4 -- Context-sensitive retrieval gate**
Different z_goal representations should pattern-complete to different trajectory subsets.
This is the MECH-326 requirement: the gate must be learnable, not just a static bias.
Implementation candidates: transformer attention, learned key-query retrieval, or
hippocampal context-key compression learned alongside the exploration epoch.

---

## 8. Literature Anchors

All 12 entries referenced here are in:
`evidence/literature/targeted_review_developmental_exploration_hippocampal_retrieval/entries/`

| Entry key | Claim anchored | lit_conf |
|-----------|---------------|---------|
| topic1_birdsong_babbling_doupe_kuhl1999 | INV-073 (bootstrapping necessity) | 0.78 |
| topic1_babbling_sensorimotor_leitao_gahr2024 | INV-073 (motor opens sensory phase) | 0.76 |
| topic1_canonical_babbling_warlaumont_finnegan2016 | INV-073, ARC-072 (severed feedback) | 0.70 |
| topic1_respiratory_rhythm_babbling_fuchs2026 | INV-073 (cross-modal calibration) | 0.68 |
| topic2_hippo_prediction_imagination_buckner2010 | MECH-325 (cue-indexed library) | 0.82 |
| topic2_hippo_pfc_replay_decision_shin_jadhav2019 | MECH-325, MECH-326 (forward replay + PFC coherence) | 0.84 |
| topic2_hippo_pfc_theta_sequences_tang_jadhav2021 | MECH-326 (theta-sequence alternatives) | 0.82 |
| topic2_hippo_imagination_comrie_frank2022 | MECH-325 (imagination beyond recall) | 0.77 |
| topic3_pfc_cognitive_control_miller_cohen2001 | MECH-326 (PFC bias mechanism) | 0.84 |
| topic3_pfc_hippo_context_replay_zielinski_jadhav2018 | MECH-326 (PFC gates replay) | 0.79 |
| topic4_isolation_rearing_reversal_li2007 | INV-073, ARC-072 (reversal learning deficit) | 0.68 |
| topic4_enrichment_behavioral_flexibility_wang2017 | INV-073 (novelty type matters) | 0.64 |
