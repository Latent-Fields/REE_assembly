# Mutual legibility: implications and next moves

**Date:** 2026-09-07  
Status: processed
Intake: evidence/planning/thought_intake_2026-09-07_mutual_legibility.md
Claims registered: ARC-139, MECH-537, MECH-538, MECH-539, MECH-540, INV-105

**Document type:** synthesis / next-step thought; not a claim registration, not an experiment queue mutation
**Parent thought:** `2026-09-07_mutual_legibility_communication_subspaces.md`  
**Implementation companion:** `2026-09-07_mutual_legibility_implementation_assays.md`  
**Detailed work programme:** `../../evidence/planning/mutual_legibility_work_program_20260907.md`

## Why this companion exists

The mutual-legibility idea now has enough external evidence, internal REE convergence, and implementation detail that the next steps are themselves part of the thought.

They should not live only as an operational tail in a planning file, because the **ordering of the next investigations is conceptually load-bearing**. The order determines what REE will be entitled to conclude.

The central danger is to see an exciting literature on latent bridges and immediately add a bridge to REE. That would be backwards. The strongest present use of the idea is diagnostic: distinguish information loss from routing failure, coordinate mismatch, consumer collapse, generic channel effects, and dynamic incompatibility.

The next moves therefore follow from the thesis itself:

> **First measure mutual legibility. Then locate the failure. Only then decide whether any architectural change is justified.**

---

## 1. What is now sufficiently established to act on

Several propositions are strong enough to guide investigation without being promoted to architectural axioms.

### 1.1 Representation adequacy and consumer adequacy are separable

REE already has direct internal evidence for this separation. The SD-004 / SD-080 / V3-EXQ-817a lineage showed that making the action-object representation more consequence-structured did not improve behaviour when the downstream path remained collapsing.

The lesson is not merely historical. It changes experimental interpretation:

- a representation-side success with a behavioural null is not automatically evidence that the represented information is irrelevant;
- a consumer-side failure can mask a real representational improvement;
- a ceiling measured through an untrained or collapsing readout may be a ceiling of the interface rather than of the representation.

### 1.2 Severe compression does not imply severe information loss

The waypoint probe on 2026-09-07 showed that a random 275 -> 32 projection retained roughly 78% of the measured directional lift. Therefore dimensionality alone is not an adequate explanation for current `z_world` failures.

The relevant null is no longer simply "information is absent after compression". It must be compared against a dimensionality-matched random-projection floor and then followed through the actual consumer.

### 1.3 Communication can occupy a selective subspace

The communication-subspace literature provides a plausible mechanism by which a rich sender representation can contain information that the actual consumer does not see. High-dimensional local representations can coexist with lower-dimensional, consumer-specific channels.

For REE this creates an experimentally useful middle category between:

- information absent from the sender; and
- information successfully used by the receiver.

That middle category is:

> **information present in the sender but poorly exposed through the consumer-facing communication subspace.**

### 1.4 Low-complexity translation is stronger evidence than arbitrary rescue

Mostik, Interlat, StateBridge, model stitching, and related work collectively motivate asking whether frozen systems can be made mutually legible. But the evidential value depends on bridge complexity.

A rotation or low-rank map rescuing a frozen interface suggests a shallow geometry mismatch. A large nonlinear bridge can become a second computational system and therefore supplies much weaker evidence about the original sender and receiver.

### 1.5 Channel dependence is not content dependence

Correct-pair, mismatched-pair, zero, and distribution-matched random controls are not optional decorations. They distinguish a receiver that uses the **specific transmitted content** from one that merely benefits from activation, gain, regularisation, or some generic statistical property of the channel.

This distinction should become standard experimental hygiene for internal communication claims in REE.

---

## 2. What remains hypothesis rather than established fact

Several attractive extensions must remain explicitly provisional.

### 2.1 REE does not yet know that communication-subspace failure is the current dominant V3 problem

The external literature makes it plausible. V3-EXQ-817a makes it locally credible. The current `z_world` work makes it timely. None of those establish that the present waypoint/resource/ContextMemory failures are caused by the same mechanism.

That is why the next step is a diagnostic instrument rather than an architectural amendment.

### 2.2 REE does not yet know that development reduces translation complexity

A useful developmental hypothesis is that specialised systems can become more internally distinct while becoming easier for one another to use.

This is testable, but it is not yet demonstrated in REE.

### 2.3 REE does not yet know that sleep improves mutual legibility

The neuroscience supports replay, representational transformation, selective communication, and different plasticity/stability regimes across interfaces. It does **not** yet establish the stronger statement that sleep reduces the formal mapping complexity between independently specialised representational systems.

Therefore the sleep experiment belongs late in the sequence, after the waking metric has been validated.

---

## 3. The sensible immediate sequence is part of the hypothesis

The recommended next sequence is:

1. **ML-00 — evidence completeness and provenance review.**  
   Ensure the Mostik/Interlat/StateBridge/model-stitching/causal-audit/communication-subspace/NoMAD/compression-reconstruction evidence is represented with the correct epistemic status: peer reviewed, preprint, or company reported.

2. **ML-01 — claim-overlap and contradiction review.**  
   Check whether mutual legibility is already substantially owned by MECH-532, MECH-507, ARC-121, INV-088 lineage, SD-080/MECH-517/518, and relevant sleep/replay claims. The default should be reinterpretation or refinement before creating a new claim.

3. **ML-10/11 — build read-only interface telemetry and an offline dataset.**  
   Capture aligned sender states, actual consumer inputs/preactivations, task variables, actions/candidates, outcomes, phase, provenance and hashes without changing behaviour or the random-number stream.

4. **ML-12 — implement communication-subspace analysis with synthetic falsifiers.**  
   Reduced Rank Regression, rank sweeps, held-out receiver prediction, orthogonal complements, principal angles, task-information overlap, and planted-subspace controls should work before touching a live REE claim.

5. **ML-13/14/15 — implement the bridge ladder, causal replacement controls, and dynamic-compatibility tests.**  
   These instruments belong together because a static behavioural rescue without causal-pairing and dynamics checks is too easy to misread.

6. **ML-20 — run the first live diagnosis at the waypoint `z_world -> consumer` locus.**  
   This is the best first site because the sender-side information range has already been characterised and the random-projection floor is known.

7. **Adjudicate before expanding.**  
   Do not immediately repeat the new assay across every REE boundary. First decide which failure class ML-20 actually supports.

8. **ML-30 — revisit V3-EXQ-817a using the validated communication-subspace instrument.**  
   This is the strongest historical negative case and therefore the best independent test of whether the new vocabulary adds explanatory power rather than merely redescribing today's problem.

9. **Only after those results should developmental and sleep assays become live work.**

The detailed engineering forms of these tasks are kept in `evidence/planning/mutual_legibility_work_program_20260907.md` so this document can preserve their conceptual rationale.

---

## 4. Why ML-20 should be first

A useful first experiment should maximise discrimination among rival explanations while minimising architectural novelty.

The current waypoint locus already supplies:

- a task-relevant variable;
- raw-observation decodability;
- a severe random-projection comparison;
- an existing `z_world` representation;
- an actual downstream consumer;
- a current science question rather than an artificial benchmark created for this thought.

Therefore the experiment can ask, in order:

1. Is waypoint information present in trained `z_world` above the justified floor?
2. Which low-rank directions of `z_world` actually predict the native consumer?
3. How much waypoint information overlaps that consumer-facing subspace?
4. Is relevant information concentrated instead in the orthogonal/private space?
5. Can an orthogonal, affine, or low-rank frozen bridge improve native use?
6. Does any improvement depend on the **correct paired state**?
7. Does the bridge preserve transition dynamics?

The resulting categories are meaningfully different:

- **information loss**;
- **routing/subspace mismatch**;
- **shallow coordinate mismatch**;
- **consumer computation failure**;
- **generic channel effect**;
- **dynamic mismatch**.

A single well-designed assay can therefore close more hypothesis space than several ad hoc architecture changes.

---

## 5. Why the 817a revisit matters

The 817a result predates the present Mostik-triggered campaign. That makes it especially valuable.

If the new framework can explain an already-landed negative result that was not designed around communication subspaces, it has stronger standing than if it only explains the case that inspired it.

The key retrospective questions are:

- Did consequence information become encoded in the grounded action-object space?
- Did that information overlap the dimensions actually used by the decoder/planner?
- Was the downstream map effectively rank-deficient or decision-boundary collapsed?
- Would a deliberately non-collapsing low-complexity readout make the already-grounded information behaviourally visible?

Possible outcomes matter in both directions.

If a simple adequate readout unmasks behavioural benefit, the interface-first interpretation gains strong support.

If grounded consequence information reaches a demonstrably adequate consumer and still produces no benefit, the interface-first interpretation is materially weakened.

That makes ML-30/31 a proper falsification opportunity, not a rescue programme.

---

## 6. Architectural consequences should remain conditional

The current thought does **not** imply that REE should permanently contain explicit bridges between every module.

Several outcomes are possible after diagnosis:

- the correct fix may be to train an existing readout;
- the sender objective may need to expose a currently private direction;
- a dead gradient or collapsing decoder may need repair;
- phased training may need to co-train compression and decompression;
- the native interface may already be adequate, moving the failure elsewhere;
- a small consumer-specific projection may genuinely be useful;
- no new architecture may be required at all.

Only repeated evidence across loci would justify a broader architectural principle such as explicit consumer-specific communication subspaces.

A particularly strong future result would be emergence of the same pattern independently across several REE boundaries:

> rich private representation + low-rank consumer-facing subspace + correct-pair-specific causal dependence + preserved local specialisation.

At that point the pattern would deserve architectural status rather than remaining merely an analytical description.

---

## 7. Developmental implication if the hypothesis survives

If waking interface assays validate the construct, development can be measured on two axes rather than one:

- **local competence/specialisation**;
- **cross-system mutual legibility**.

This allows a mature system to become more specialised without becoming fragmented.

One especially informative developmental signature would be:

- sender and receiver each improve their own task competence;
- global representational similarity stays flat or even falls;
- task-relevant information becomes more concentrated in the consumer-facing subspace;
- the minimum bridge class/rank needed for held-out functional transfer decreases;
- correct-vs-mismatched causal separation increases.

That would operationalise the idea that development improves **coordination without homogenisation**.

---

## 8. Sleep implication if the developmental construct survives

Only after waking mutual legibility can be measured reliably should sleep be asked to alter it.

The biologically better hypothesis is not global alignment. It is selective interface maintenance:

- some interfaces should reconfigure because recent learning demands plasticity;
- other interfaces should remain stable because continuity is more important;
- representational rebucketing may require re-indexing and interface recalibration together;
- successful sleep may therefore preserve or improve functional communication while allowing internal representations themselves to move.

The strongest sleep test would compare at least two interfaces with different predicted plasticity rather than asking whether all systems become more similar after sleep.

---

## 9. Package map

This thought is one part of a deliberately split package:

### Conceptual thesis
`docs/thoughts/2026-09-07_mutual_legibility_communication_subspaces.md`

Defines mutual legibility, communication subspaces, the evidence ladder, development/sleep implications, and the core falsifiable architectural hypothesis.

### Implementation and assay companion
`docs/thoughts/2026-09-07_mutual_legibility_implementation_assays.md`

Defines telemetry, Reduced Rank Regression, bridge complexity ladders, pairing controls, dynamic compatibility, anti-shortcut guards, and possible later implementation forms.

### This document
`docs/thoughts/2026-09-07_mutual_legibility_implications_and_next_moves.md`

Explains what follows from the thought now, why the investigation order matters, and what evidence would justify or weaken architectural expansion.

### Detailed staged work programme
`evidence/planning/mutual_legibility_work_program_20260907.md`

Contains the ML-00 through ML-61 work items and conditional ML-A architecture placeholders in operational form.

### Evidence base
- `evidence/planning/latent_interface_translation_campaign_20260907.md`
- `evidence/planning/latent_interface_translation_tranche2_20260907.md`
- `evidence/planning/latent_interface_translation_tranche3_20260907.md`

These retain the research provenance and should remain separate from the thought documents.

---

## 10. Working conclusion

The immediate opportunity is not to build a Mostik-like bridge inside REE.

It is to exploit the external convergence to ask a better question of the creature we already have:

> **When REE contains information but fails to behave as though it contains it, is the information lost, privately encoded, badly routed, badly translated, dynamically incompatible, or simply ignored by the consumer?**

The first responsibility of the new framework is to distinguish those cases.

If it succeeds, mutual legibility becomes a useful measurable property of REE development. If it repeatedly fails to explain live or historical loci, the idea should contract rather than becoming a new architectural fashion.
