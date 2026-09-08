---
title: "Receiver-Conditioned Translation and Recurrent Interface Stability (MECH-547, MECH-548)"
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 18
status: candidate
status_asof: 2026-09-08
status_claim: MECH-547
---

# Receiver-Conditioned Translation and Recurrent Interface Stability

**Status:** candidate, registered 2026-09-08 from
`docs/thoughts/2026-09-08_receiver_conditioned_translation_and_recurrent_interface_stability.md`
(intake: `evidence/planning/thought_intake_2026-09-08_receiver_conditioned_translation_and_recurrent_interface_stability.md`).
Child of [Mutual Legibility and Communication Subspaces](mutual_legibility_communication_subspaces.md)
(ARC-139, MECH-537..540, INV-105); sibling of [The Cognitive Contract](cognitive_contract.md) (ARC-142).

Nothing here is a build instruction. Both claims are `candidate`, `substrate_conditional`, and carry a
"do not build in V3, do not queue" caveat. What they justify is a **diagnostic** over frozen endpoints.

**Working principle (verbatim from the thought):**

> Mutual legibility may be relational rather than fixed: what a sender should expose can depend on the
> receiver's current state. But an interface that is useful once is not necessarily safe to use
> repeatedly. In a recurrent cognitive system, translation must be both content-specific and
> dynamically self-consistent over time.

---

## MECH-547 -- receiver-conditioned translation {#mech-547}

The parent package framed translation as `sender state -> bridge -> receiver-readable state`. The
sharper abstraction is

```text
translated content = T(sender state, receiver state, receiver position / context)
```

so the communication subspace (MECH-537) may be **context-indexed**: the sender supports several read
surfaces and which is active depends on receiver mode, goal / task-loop context, uncertainty, the
candidate under evaluation, retrieved episodic context, temporal phase and predicted state.

**The constraint that keeps this honest:** receiver-conditioning decides *which part* of already-present
sender information is exposed and *how* it is expressed. It must not let the bridge solve the task
independently. A high-capacity `T(A, B)` can compute an arbitrary joint function of both systems and
become a hidden cognitive module, so the evidence burden is stricter than for a linear bridge:

- frozen endpoints during diagnosis;
- explicit parameter / capacity reporting;
- a sender-only matched-capacity baseline `T(A)`;
- a **receiver-state permutation** control (the discriminator: if permutation barely changes the gain,
  the gain is capacity, not conditioning);
- correct-vs-mismatched sender control (INV-105);
- off-manifold and recurrence-stability checks (MECH-548);
- held-out environments / tasks;
- a demonstration that the bridge exposes or aligns existing content rather than learning the task.

**Candidate REE loci** (diagnostic targets, not build sites): `z_world -> E1` vs `z_world -> E2`
(different read surfaces of one sender); `E1 <-> E2` conditioned on the candidate action / horizon;
hippocampal retrieval -> consumer conditioned on the consumer's query state; `ContextMemory` -> reader
expressed relative to current context; waking vs offline interface geometry.

---

## MECH-548 -- recurrent interface stability {#mech-548}

> **An interface can be statically useful yet recurrently unstable.**

A bridge with `one-step utility > 0` can fail `repeated closed-loop stability`. Two mechanisms, to be
separated experimentally:

| Mechanism | What happens | Separating measure |
|---|---|---|
| (a) off-manifold compounding | `B_0 -> T(A_0,B_0) = B_1' -> T(A_1,B_1') = B_2'`; each step lands slightly off the native receiver distribution and the next treats it as ordinary input | receiver-manifold distance / drift over steps |
| (b) semantic double-counting | already-injected content is not recognised as present and is re-amplified | bridge output norm / gain over time; redundant re-injection of transmitted content |

**Clean-base versus cumulative translation.**

| | Cumulative | Clean-base (temporary overlay) |
|---|---|---|
| Each step operates on | the previously translated receiver state | an unmodified native receiver state; residual held as a gated overlay |
| Gains | fully recurrent; prior transmitted content shapes later interface behaviour | prevents recursive contamination; keeps a native reference frame; cleaner causal attribution |
| Risks | compounding drift, duplicated evidence, escalating gain, self-generated artefacts become new evidence | may block genuinely useful integration; needs an explicit state / overlay distinction; artificial if permanent |

The REE reading: this is the **state vs modulatory overlay** distinction at an interface. Test translated
information first as an overlay or gated read surface, never as an irreversible rewrite of the
receiver's core latent state. The overlay is a gated, gained coupling in ARC-084's vocabulary, and
escalating gain is MECH-363's all-cooperative runaway at one interface (an analogy across levels,
labelled as such).

**How MECH-548 differs from MECH-539.** Both produce `good one-step + degrading long-horizon`. MECH-539 is
the bridge being incompatible with the receiver's *native dynamics*; MECH-548 is the bridge's *own output
re-entering as its input*, which can happen with perfectly compatible dynamics and a fixed sender. The
clean-base arm separates them: if recomputing against the clean receiver state restores stability, the
failure is MECH-548.

**The eighth rung.** INV-105's ladder becomes

```text
encoded -> decodable -> natively accessible -> bridgeable -> pairing-specific
        -> causally used -> behaviourally useful -> recurrently stable
```

For dynamical systems, recurrence stability is assessed *before* behavioural usefulness is read as
architecturally meaningful. This is proposed to `/governance` as an amendment to INV-105 (governance
flag raised at registration), not applied here.

**Sleep corollary (MECH-540).** Offline interface recalibration must improve or preserve closed-loop
stability when waking dynamics resume. A sleep-induced change that improves a static probe but
destabilises the next waking trajectory is a failure, not consolidation. Future sleep metric: change in
multi-step interface stability and correct-pair-specific communication after offline consolidation.
A REE hypothesis, not a biological claim.

---

## The assay (diagnostic; extends work-programme ML-13 / ML-14)

Keep both endpoints frozen; match capacity where possible. Arms:

1. fixed sender-only bridge `T(A)`;
2. receiver-conditioned bridge `T(A, B)`;
3. receiver-conditioned bridge with receiver-state permutation;
4. cumulative repeated application;
5. clean-base / temporary-overlay application;
6. zero and moment-matched random controls;
7. correct-vs-mismatched sender-state controls.

Measures: one-step consumer performance; multi-step performance curve; receiver-manifold distance /
drift; task-information calibration; bridge output norm / gain over time; redundant re-injection of
previously transmitted content; dynamic compatibility with native receiver transitions (MECH-539);
correct-pair specificity.

| Reading | Interpretation |
|---|---|
| `T(A,B) > T(A)` held-out, permutation destroys the gain | receiver conditioning is genuinely useful |
| `T(A,B) > T(A)`, permutation barely matters | extra capacity, not conditioning |
| one-step rescue, cumulative collapse, clean-base stable | recurrent interface instability (MECH-548) |
| cumulative stable with correct-pair specificity | functionally coherent recurrent bridge |
| both bridges fail, richer source information succeeds | upstream representation deficiency more likely |

Any proposed E1/E2 interface repair is tested over the **same horizons** used to judge predictive
competence. Sequencing from the parent package stands: a waking metric with range and stability first,
then recurrence, then sleep.

## Evidence status

XKV (Liu et al., 2026) operates across frozen models differing in family, depth, key-value geometry and
tokenizer, which strengthens the heterogeneous-bridge motivation. The public `kvloom` implementation is
independent of the original authors and reproduces the broad ordering across a substantial grid, but its
checkpoints are exploratory (single seed, limited validation, short runs, no confidence intervals):
**early independent replication, not settled replication**. The repeated-application collapse appears
only in `kvloom`, not in the XKV paper, and is tracked as an emerging finding requiring replication.
None of this was independently verified in the registering pass, and none of it raises any claim's
confidence.
