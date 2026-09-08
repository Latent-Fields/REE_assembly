---
title: "Culture as a Distributed Precommit System (ARC-141, MECH-542..544)"
parent: "Modes, Agency & Default Mode"
grandparent: Architecture
nav_order: 14
status: candidate
status_asof: 2026-09-08
status_claim: ARC-141
---

# Culture as a Distributed Precommit System

Registered 2026-09-08 from the two-document package
`docs/thoughts/2026-09-07_culture_as_distributed_precommit_system.md` and its evidence
companion `..._evidence.md`, via
`evidence/planning/thought_intake_2026-09-07_culture_distributed_precommit.md`.

The architectural foothold already exists: REE's commitment boundary already distinguishes
hypothetical cognition from committed action, and INV-011 (*imagination without belief update*,
status `active`) protects it. **This package does not propose a new "fiction module."** Its
natural implementation is an extension of source tagging, generative mode, hippocampal rollout,
E1 representation and E3 commitment/precision machinery.

---

## MECH-542 -- Source-sensitive selective permeability (the load-bearing claim)

This is the narrow, falsifiable core of the package, and the one that carries architectural
consequence. Everything else on this page is downstream of it.

INV-011 must not be read as `hypothetical -> learning OFF`. Human cultural learning suggests
"belief update" is too unitary a category if applied literally across every representational
layer. The proposal is:

> **hypothetical -> source-sensitive selective permeability**

The hypothesis tag protects particular kinds of commitment while permitting useful
representational learning elsewhere.

| Should ordinarily NOT update from fictional/hypothetical source | May legitimately update |
|---|---|
| autobiographical occurrence (*this happened to me*) | possibility estimates |
| historical occurrence (*this event actually occurred*) | causal expectations |
| source truth (*the narrator's proposition describes reality*) | representations of other agents, possible motivations |
| responsibility attribution (*I performed this action*) | policy repertoire; harm/benefit expectations |
| responsibility-bearing residue | social contingencies; counterfactual vocabulary; the range of trajectories available for later simulation |

Three properties that are otherwise conflated must be allowed to dissociate:
**representability** (can this state enter the generative system at all?), **epistemic
commitment** (does the system treat it as describing the actual world?), and **behavioural
commitment** (has an action been selected and owned on its basis?). A fictional state may have
high representability, zero epistemic commitment and zero behavioural commitment while still
modifying the future space available to the system.

### Registered falsifier -- update fingerprints

The prediction is explicitly **NOT** "fiction causes no update". It is:

> **Epistemic framing determines which components of the model are authorised to update.**

Inject semantically identical event content under different source frames -- direct observation,
testimony, fiction, counterfactual, prediction, joke, memory, committed experience -- and
measure *differential* change across world-state belief, source confidence, E1 expectations, E2
predictions, other-agent models, harm/benefit expectations, policy availability, hippocampal
trajectory repertoire, E3 evaluation, precision allocation, residue, and subsequent behaviour.

**The claim is wrong in both directions, which is what makes it a claim:** if REE learns equally
from fiction and observation across *every* model component, the source-sensitive architecture
is wrong; if REE learns *nothing* transferable from fiction or counterfactual trajectories, it is
also wrong. The predicted regime lies strictly between those extremes.

## ARC-141 -- Culture as a distributed precommit workspace

The organising conjecture:

> **Culture functions partly as a distributed precommit workspace in which minds collectively
> generate, exchange and evaluate candidate beliefs, identities, norms and futures before those
> representations acquire full epistemic or behavioural commitment.**

Candidate trajectories need not originate within the individual organism -- another mind can
construct a trajectory and transmit enough of its structure for my predictive system to
instantiate it. Search is much cheaper than commitment, so a population that can exchange
possible worlds explores far more of possibility space than one that must pay for knowledge with
real consequences.

The proposed cultural progression (explicitly **not** assumed universal or monotonic):

> unrepresentable -> representable only under protection -> hypothetically discussable ->
> socially negotiable -> propositionally credible -> behaviourally actionable -> committed

Science fiction is the clearest instance: a technological trajectory can be instantiated in
narrative space, mutated by many authors and evaluated by many readers, *before society commits
to constructing it* -- externally generated long-horizon candidate trajectories reaching
E1/E3-like evaluation before the corresponding state has been directly sampled.

**Falsifiability guard, carried verbatim from the evidence companion:** the largest conceptual
danger is treating every beneficial effect of fiction as evidence for the hypothesis, which would
make it unfalsifiable. ARC-141 is a framing whose empirical content is discharged through
MECH-542; it must not be cited as independently confirmed by any pleasant result about fiction.

## MECH-543 -- Drama runs own machinery under another's boundary conditions

A proposed distinction between two modes of hypothetical engagement:

> **Fiction:** simulate another agent's trajectory.
>
> **Drama / role enactment:** partially run one's OWN generative machinery under another agent's
> identity or situational boundary conditions.

If correct, enacted role-play should produce **different** effects on other-model formation,
policy availability or affective prediction than semantically equivalent descriptive narrative --
partially overlapping but distinguishable update fingerprints. Speculative, but experimentally
tractable, and it dissociates cleanly from MECH-542 (which concerns *which variables* update, not
*by what route* the material is instantiated).

## MECH-544 -- Permeability pathology and source-tag decay

The same permeability that enables cultural learning creates its failure modes, and this is
**not an accidental weakness** -- it may be the unavoidable price of learning from counterfactual
experience. A fully impermeable hypothetical system learns nothing from imagination; a fully
permeable one cannot distinguish imagination from reality.

Predicted failure routes: repeated fictional trajectories distorting perceived likelihood;
emotionally powerful narratives acquiring inappropriate precision; propaganda altering
other-models without adequate evidence; humour gradually reducing the effective cost of
prohibited representations; imagined threats modifying expectations of groups never encountered;
cultural availability mistaken for environmental frequency.

**Registered signature -- source-tag decay:** source information degrades while narrative
structure is retained, producing characteristic errors in which retained narrative becomes
progressively harder to distinguish from experienced or testified information. This connects to
REE's existing "spurious residue from narrative contamination" analysis in
`architecture/language/language_failure_modes.md`.

The architectural problem is therefore **not** to prevent hypothetical material from influencing
cognition, but to ensure that *the kind and magnitude of update remain appropriate to the
epistemic status of the representation*.

---

## Already owned -- humour (SOC-HUM-1)

Sections 7-8 of the source thought (humour as controlled norm violation; humour as a low-cost
social probe of commitment) are **already owned by SOC-HUM-1**, which registers humour's
"low-commitment, deniable PROBE that re-opens gridlocked norm conflicts ... because a joke floats
a heterodox interpretation without committing anyone to it." No new humour claim was minted.

One thread is deliberately left **unregistered pending a closer check**: the source thought's
*interpersonal* reading -- humour as an assay of a specific other agent's tolerance boundary and
of shared interpretive-community membership -- is a different *use* (measurement of another mind)
from SOC-HUM-1's societal norm-unblocking *mechanism*. Whether that is a distinct claim or a
consequence of SOC-HUM-1 is a `/thought-digestion` question, not an ingestion one.
