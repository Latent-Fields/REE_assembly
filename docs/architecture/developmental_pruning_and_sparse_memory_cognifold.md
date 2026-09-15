---
title: Developmental pruning and sparse memory cognifold
parent: "Development & Curriculum"
grandparent: Architecture
nav_order: 7
status: candidate
status_asof: 2026-09-15
status_claim: MECH-362
---

# Developmental pruning and sparse memory cognifold

**Date:** 2026-06-09
**Status:** Compass (V4/V5; off the V3 critical path)
**Claims:** MECH-362, Q-057
**Origin:** thought-intake [thought_intake_2026-06-06_ca3_development_sparse_structured_connectivity.md](../../evidence/planning/thought_intake_2026-06-06_ca3_development_sparse_structured_connectivity.md)

> This is a **developmental architecture compass**, not a V3 implementation target. The two
> claims registered here are `substrate_conditional` / `implementation_phase: v4` -- they are
> promote/demote-suppressed and do **not** imply an experiment is owed on the current substrate.
> Do not build a developmental pruning substrate or queue an experiment from this doc without an
> explicit decision routing it onto a version's critical path.

---

## 1. Empirical anchor (verified)

Vargas-Barroso V., Watson J. F., Navas-Olive A., Schlogl A., Jonas P. "Developmental emergence of
sparse and structured synaptic connectivity in the hippocampal CA3 memory circuit." *Nature
Communications* (2026), article `s41467-026-71914-x` (ISTA).
https://www.nature.com/articles/s41467-026-71914-x

- Multicellular patch-clamp circuit mapping of up to 8 CA3 pyramidal neurons at three postnatal
  stages: P7-8 (early), P18-25 (adolescent), P45-50 (adult).
- CA3 recurrent connectivity transforms **local / dense / strong / near-random -> distributed /
  sparse / structured**.
- **Early:** a single synaptic event can be sufficient to trigger a postsynaptic spike.
- **Mature:** spatial summation of several (weaker) inputs is required to drive a spike.
- Authors' framing: **"tabula plena"** -- a full, over-connected starting substrate refined by
  pruning -- rather than tabula rasa; the sparse/structured endpoint may emerge via
  experience-dependent mechanisms.

Cross-species corroboration that the mature endpoint is *structured* (not random): Tang et al.,
"Human hippocampal CA3 uses specific functional connectivity rules for efficient associative
memory," *Cell* (2024).

---

## 2. The two registered claims

### MECH-362 -- Subtractive developmental sparsification

Mature sparse/structured memory connectivity emerges by **pruning / down-weighting an initially
over-connected, dense, near-random substrate** ("tabula plena"), not by additively growing
connections onto a sparse skeleton. The corollary at the recall stage: **mature recall requires
convergent summation of several weak inputs rather than a single strong cue.**

**Distinct from MECH-120 (SWS synaptic homeostasis / Tononi SHY).** MECH-120 is *nightly
homeostatic down-scaling* of synaptic weight to restore signal-to-noise; MECH-362 is a *one-way
developmental* trajectory of recurrent connectivity from dense-random to sparse-structured. They
may share machinery (down-weighting), but the timescale, directionality, and function differ.

**Relation to ARC-019 (staged developmental curriculum).** REE's developmental claims (ARC-019,
IMPL-019) are currently *additive* -- capability is added stage by stage. MECH-362 proposes a
*subtractive* stage: an over-connected exploratory phase that is pruned. If adopted, MECH-362
most naturally **amends ARC-019** rather than standing fully alone.

**Pruning is not (only) deletion.** Down-weighting, gating, or residue-tagged de-authorization are
plausible computational analogues -- see Q-057.

### Q-057 -- Exploratory-overconnected vs mature-sparse substrate

Should REE distinguish an **early over-connected exploratory developmental substrate** from a
**mature sparse/structured substrate** -- and is developmental sparsification best modelled as
deletion, down-weighting, gating, or residue-tagged de-authorization? Sub-questions:

- Does REE-v3's cue-authority problem partly reflect *immature single-cue authority* rather than
  mature convergent-weak-input recall?
- Can offline integration act as **pruning / contextualisation** rather than merely consolidation?
- What developmental gates should exist before a memory trace can influence action release?

---

## 2b. Claims registered 2026-09-15 from the developmental-overcapacity thought

Source: `docs/thoughts/2026-09-08_developmental_overcapacity_pruning_sparse_interfaces.md`
(intake: `evidence/planning/thought_intake_2026-09-08_developmental_overcapacity_pruning_sparse_interfaces.md`).
All four are `candidate`, `substrate_conditional`, `v4` / `v4_v5`, and carry a "do not build in V3,
do not queue" caveat. The thought's own section-6 fork (over-capacity decoder as an upper-bound assay)
has already been RUN in REE -- V3-EXQ-1010 swept decoder capacity ~77,000x with 0/3 seeds at the bar --
and REE's confirmed routing ("the repair site is the encoder's objective, not the consumer", SD-018
amend, SD-106) matches the thought's own prescription for that branch. The audit also found that
`ree_core/` holds NO structural pruning, sparsification, retention criterion or capacity schedule; the
one developmental capacity manipulation that exists, `GatedPolicy.crystallize()`, runs the OPPOSITE
way (freezes established heads, ADDS a plastic channel).

### ARC-143 -- developmental vs mature capacity envelope {#arc-143}

The DEVELOPMENTAL capacity envelope is a design variable distinct from the MATURE envelope, and REE
must not infer the first from the second: the connection count, candidate mappings, accessible
transformation repertoire and interface permissiveness a developing organism needs in order to
DISCOVER a useful organisation may each exceed what the mature organism retains. Generalises
MECH-362's subtractive trajectory from recurrent memory connectivity to every locus the thought
names (z_world, E1/E2 interfaces, replay pathways, goal/directive influence, E3 selection) and
supplies the missing claim-graph edge between the developmental-pruning lineage (MECH-362, Q-057)
and the mutual-legibility lineage (ARC-139, MECH-537, MECH-538, MECH-540, INV-105). It licenses
DECLARING a developmental envelope per locus; it does not assert bigger is better.

### MECH-549 -- developmental-history irreducibility at matched final capacity {#mech-549}

Some mature organisations may be historically inaccessible from their own final architecture. The
confirming contrast is the four-arm design's arm D: (A) mature size throughout, (B) overcapacity
progressively reduced, (C) overcapacity retained, (D) arm B's final architecture, mask and
interfaces REINITIALISED and trained from the start. B > A is consistent with "pruning found a
better small architecture"; only B > D establishes the claim. Distinguished from Q-101 (the same
counterfactual at cross-version grain) and from knowledge distillation (a distillation-only account
weakens, not confirms, the claim).

### MECH-550 -- functional persistence as the retention criterion {#mech-550}

What survives a developmental reduction should be decided by repeated demonstrated usefulness under
prediction, action, regulation and replay -- not by weight magnitude. Named rival control:
indiscriminate magnitude pruning at matched final capacity (MECH-120 is approximately that rule at
another timescale and must not be cited as support). Distinct from Q-057, which asks what pruning IS,
not what it selects on. Constrained by INV-104: a present-tense-only criterion would prune exactly the
not-yet-relevant distinctions INV-104 protects.

### MECH-551 -- replay-coupled capacity reduction as the coordination site {#mech-551}

Reduction concurrent with representational change is a coordination problem (a route can look
unnecessary only because its consumer has not yet adapted; a useful-looking route can be preserving an
obsolete convention), so the retention decision read online is unreliable in both directions and
offline replay is the proposed site. Of the thought's six offline items, four are already owned
(MECH-529, MECH-513, MECH-540); the residue is weakening redundant ROUTES and verifying a reduction
destroyed no counterfactual or regulatory distinction. Prediction: at matched reduction and matched
update count, replay-coupled reduction preserves more transfer and causal structure than
online-only. Governance may prefer this as a fifth signature on MECH-540; that is a governance call.

---

## 3. Three-phase developmental schedule (hypothesis)

1. **Over-connected exploratory phase** -- many weakly-constrained associations, high plasticity,
   broad coupling, **low action authority**.
2. **Pruning / selection phase** -- repeated offline + waking experience down-weights unstable /
   non-useful pathways.
3. **Sparse structured retrieval phase** -- mature recall requires coordinated multi-cue
   activation rather than single-cue domination.

Recall formulation (from the intake):

```
mature_recall_activation = f(convergent_weak_inputs, context_match, residue_state,
                             goal_state, self_world_tag, precision_gate)
```
rather than `max(single_strong_cue)`.

---

## 4. Where the V3-relevant strand already lives

The **convergent-weak-input vs single-strong-cue** corollary is the one strand with present-day
V3 relevance (REE-v3 currently exhibits single-representative over-authority). It is folded in as a
**diagnostic lens** -- NOT a separate V3 claim -- in the selection-authority plan-of-record:
[modulatory_bias_selection_authority_design.md](../../evidence/planning/modulatory_bias_selection_authority_design.md)
"Developmental framing (compass)". Registering it as its own V3 claim would duplicate the active
selection-authority / rule-apprehension claims (MECH-314/341, ARC-062).

---

## 5. Related claims

- **ARC-006** -- entities are sparse, persistent, bindable structures (the sparse *endpoint*).
- **ARC-007** -- hippocampal map substrate (biological locus is the CA3 recurrent circuit).
- **ARC-019 / IMPL-019** -- staged developmental curriculum (currently additive; MECH-362 would add a subtractive stage).
- **MECH-120** -- SWS synaptic homeostasis (SHY); closest existing down-scaling analog (V4).
- **ARC-139 / MECH-537 / MECH-538 / MECH-540 / INV-105** -- mutual-legibility lineage; ARC-143 (above) is the edge
  between it and this doc's pruning lineage; MECH-538's falling minimum-bridge-rank prediction is the
  interface-side readout of MECH-549.
- **Q-101** -- ontogenetic-vs-architectural ancestry; the same counterfactual as MECH-549 at cross-version grain, not merged.
- **MECH-094** -- provenance / hypothesis tagging (failure mode: confabulatory completion from un-pruned over-connection).
- **MECH-076** -- attractor lock-in (failure mode: belief fixation / un-pruned early attractor).
- **Play-mode cluster (ARC-049/050, MECH-194-199, INV-058/059/060)** -- the natural home for an
  "exploratory over-connected phase," but **substrate-blocked in V3** (no `play_frame_tag`); do
  not queue against it.

---

## 6. Cautions (carried from the intake)

- Do not overgeneralise mouse CA3 development to human cognition or REE design.
- Do not treat dense early connectivity as automatically good/bad.
- Do not assume pruning = deletion only.
- Do not make this a V3 implementation target without a specific substrate gap.
- **Guardrail:** if a future agent tries to convert this into "add more connections" or "delete
  weak connections," stop and reframe. The correct extraction is: *mature sparse structured memory
  may emerge through developmental pruning of an initially over-connected substrate.*
