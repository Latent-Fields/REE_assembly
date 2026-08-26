---
title: "Offline Representational Reindexing & Counterfactual Model Comparison"
parent: "Sleep & Offline Integration"
grandparent: Architecture
nav_order: 5
status: candidate
status_asof: 2026-08-25
status_claim: MECH-514
---

# Offline Representational Reindexing & Counterfactual Model Comparison

**Claim IDs:** ARC-132 (attractor-property differentiation), MECH-513 (representation-version
reindexing), MECH-514 (counterfactual replay for attractor testing)
**Origin:** thought-intake [thought_intake_2026-08-24_offline-representational-reindexing-counterfactual-model-comparison.md](../../evidence/planning/thought_intake_2026-08-24_offline-representational-reindexing-counterfactual-model-comparison.md),
from raw thought `docs/thoughts/2026-08-24_offline-representational-reindexing-counterfactual-model-comparison.md`
**Status:** candidate / substrate_conditional / implementation_phase v4. Promote/demote-suppressed.
Not a V3 build target.

> This is a **control-plane / memory-lifecycle compass doc**, not a V3 implementation target. All
> three claims registered here are `substrate_conditional` / `implementation_phase: v4` -- they
> extend and combine already-built or already-planned V3/V4 machinery (MECH-269, MECH-094,
> MECH-392, INV-080, MECH-496, ARC-014, ARC-115) rather than proposing standalone new V3 substrate.
> Do not build any of this in V3 or queue a V3 experiment from this doc without an explicit
> version-routing decision.

---

## 1. What already exists (do not duplicate)

The raw thought itself is unusually careful to note that REE already contains many of the pieces
it is asking for; this section names them so later readers do not re-derive or re-register them.

- **MECH-496 (2026-08-23)** -- representational dimensionality (the number/granularity of memory
  "buckets") is an OUTCOME of a developmental plasticity schedule, not a fixed architectural
  constant. This is the closest existing claim to the thought's "buckets... their number,
  granularity and organisation may change through experience" framing, and is the CHANGE DRIVER
  MECH-513 below assumes without re-asserting.
- **INV-080 / MECH-392 (2026-06-10, V4 memory-lifecycle cluster)** -- raw-episode preservation and
  a provenance + contradiction-flag + rollback layer over CONSOLIDATION (abstraction/summarisation
  of episodic content). The planned 6-state memory-lifecycle store
  (retained/indexed/summarised/consolidated/contested/retired,
  `evidence/planning/memory_lifecycle_v4_plan.md` MEM-5) already gives REE a `contested` state and
  a "never silently overwrite the evidence base" discipline. This is the nearest sibling to the
  thought's "no rewriting history... versioning and rollback" requirement, but scoped to
  abstraction faults, not to the addressing SCHEME changing (see MECH-513 below for the
  distinction).
- **MECH-269** -- V3-live hippocampal proposer anchor selection and anchor-reset against a
  regional-verisimilitude threshold, including a minority probe channel (strengthened MECH-094
  hypothesis tag, inverted gate for low-verisimilitude/high-PE regions, no viability-map update
  until validated). This is REE's existing single-model anchor/probe substrate; MECH-514 below
  proposes comparing evidence ACROSS several bounded alternative models, an extension in kind.
- **MECH-094** -- the categorical hypothesis tag / one-way sim-vs-real write gate. Necessary
  substrate for any counterfactual-replay proposal, but not by itself sufficient for cross-model
  comparison (it distinguishes simulated from real; it says nothing about comparing two
  simulations of the same evidence against each other).
- **MECH-264 / MECH-265 (SD-033e, frontopolar)** -- counterfactual-VALUE tracking for unchosen
  ACTION alternatives and relative-importance monitoring across goals, driving behavioural
  switching. This is REE's existing "counterfactual" machinery, but for action-value arbitration,
  not for comparing explanatory models of past evidence.
- **ARC-014** -- Default Mode / DMN permits imagination without commitment; the substrate locus
  where alternative-model construction and replay would run.
- **ARC-115** -- confidence readouts are non-collapsible across a specific axis set (propositional
  confidence, attractor stability, cross-subsystem agreement, conflict pressure, action-readiness,
  socially-supplied agreement). Adjacent to but a different cut from ARC-132 below (see 2a).
- **MECH-430** -- multi-dimensional provenance SOURCE vector (perceived-vs-imagined,
  self-vs-other-generated, source identity, temporal source, modality). Adjacent to but a
  different cut from ARC-132 below.

None of the above is re-asserted below. The claims here name the gap that remains once all of it
is accounted for.

## 2. The gap: three distinct novel threads

### 2a. Attractor-property differentiation (ARC-132)

The raw thought lists eight quantities an attractor may carry (predictive reliability, epistemic
confidence, familiarity, affective valence, salience, action urgency, self-relevance, source
confidence) and argues that their conflation is what turns a hypothesis into a perceptual lens --
determining what is noticed, how ambiguity is resolved, which memories are retrieved, which
experiences are replayed, how replay is interpreted, and which interpretations are stored as
further evidence. This is a different axis set and a different problem from ARC-115 (which
dissociates internally-derived confidence from externally/socially-supplied agreement) and from
MECH-430 (which decomposes SOURCE attribution specifically). ARC-132 is about what an attractor
itself carries once formed, independent of both.

### 2b. Representation-version reindexing (MECH-513)

MECH-392/INV-080 already cover what happens when consolidation ABSTRACTS over episodic content
without silently overwriting it. Nothing in the registry covers the case the raw thought actually
leads with: the representational primitives an episode was INDEXED under (the "buckets") can
themselves change -- split, merge, or crystallise to a different count per MECH-496 -- while the
episode's content is untouched. This is REE's version of the latent-replay representation-drift
problem from continual learning (Pellegrini et al. 2019, cited but not verified in this pass):
stored intermediate activations are only valid while the encoder that produced them stays stable.
MECH-513 proposes that a change in indexing scheme require an explicit, additive, versioned
reindex -- never an overwrite -- with the episode remaining interpretable under both its
historical and its current representation.

### 2c. Counterfactual replay for attractor testing (MECH-514)

MECH-269 already lets a single rollout reset an anchor or run a strengthened-tag probe against a
verisimilitude threshold. MECH-264/265 already track the VALUE of unchosen actions. Neither
compares MULTIPLE EXPLANATORY MODELS of the same preserved evidence to generate discriminating
predictions and decide whether a different model organisation should be adopted. MECH-514
proposes that protocol: preserve evidence, temporarily de-weight the dominant attractor, construct
bounded alternatives, replay the same anchored evidence through all of them, and validate any
resulting change against held-out or subsequent waking evidence before granting it authority --
with the anti-circularity requirement (every derived item provenance-linked to its origin;
replay-selector independence from the attractor under test) treated as load-bearing rather than
optional, since without it the process could manufacture its own confirming evidence.

## 3. Explicitly out of scope here

- **Psychosis-as-mechanism claims.** The raw thought's own evidential-boundary section explicitly
  declines to assert that psychosis is one unitary precision failure, that axis-conflation (2a) is
  a demonstrated mechanism of it, or that counter-attractor replay (2c) is a demonstrated function
  of dreaming, or that sleep reindexing is a specific defence against psychosis. None of ARC-132,
  MECH-513, or MECH-514 asserts any of this; the clinical material (Jardri & Deneve 2013,
  Powers/Mathys/Corlett 2017, Howes et al. 2011, MECH-244, ARC-086) is cited only as failure-mode
  inspiration, exactly as the raw thought frames it.
- **Reconciling the raw thought's proposed handoff states** (`contested`, `pending_reindex`,
  `under_offline_review`, `provisionally_reindexed`, `validated`, `rollback_required`) against the
  existing 6-state memory-lifecycle model. `contested` already exists in both; the other four
  states named in the raw thought are not yet in the existing model. This reconciliation is real
  work for a future V4 build pass; the design question itself (fold-in vs. distinct state
  machine) is resolved in Section 5 below.
- **NREM-vs-REM architectural placement.** The raw thought suggests NREM-like phases for
  evidence-anchored consolidation and speculates REM-like phases could be useful for looser
  recombination and alternative generation, while flagging that the REM half is speculative. Not
  registered as a claim; left as a note for whichever future pass builds MECH-514's substrate.

## 4. Literature to mine before any of this hardens

Per the raw thought, none of the following are independently verified in this intake pass:
Bakker et al. 2008 (DG/CA3 pattern separation); Hassabis et al. 2007 (hippocampal scene
construction); Duncan et al. 2012 (CA1 comparator / mismatch detection); Schuck et al. 2016
(orbitofrontal hidden-state representation); Boorman et al. 2009 (frontopolar forgone-alternative
tracking); Turner et al. 2008 and Schnider 2013 (source/reality monitoring); Tse et al. 2011
(schema-primed assimilation); Latchoumane et al. 2017 (closed-loop SWR-spindle-slow-oscillation
coupling); Diering et al. 2017 and de Vivo et al. 2017 (sleep synaptic renormalisation); the 2025
detour-remapping and 2026 macaque assembly-drift studies cited in the raw thought; Jadhav et al.
2012 and Gupta et al. 2010 (awake hippocampal replay); Jardri & Deneve 2013, Powers/Mathys/Corlett
2017, Howes et al. 2011 (psychosis failure-mode inspiration only, per Section 3 above); Pellegrini
et al. 2019 (latent replay representation drift); Shumailov et al. 2024 (model collapse).

## 5. Addendum (2026-08-26): reindex handoff-state reconciliation

Closes the reconciliation flagged in Section 3 above and in the original thought-intake's Next
Steps item 2 (`thought_intake_2026-08-24_offline-representational-reindexing-counterfactual-model-comparison.md`).
Run under chip `chip-20260825-mech513-lifecycle-reconcile`; a design-question resolution against
MECH-513 as already registered, not a new claim and not a change to any claim's status or
confidence.

**Verdict: a distinct, orthogonal sub-state-machine, not a fold-in.** The existing 6-state
memory-lifecycle model (`memory_lifecycle_v4_plan.md` MEM-5:
retained/indexed/summarised/consolidated/contested/retired) tracks a record's ABSTRACTION level --
how much a memory has been summarised or consolidated, and whether that abstraction conflicts
with its source. MECH-513's four proposed states (`pending_reindex`, `under_offline_review`,
`provisionally_reindexed`, `rollback_required`) track something orthogonal: whether the ADDRESSING
SCHEME currently applied to a record is up to date with the system's current representational
primitives. A record can be `consolidated` (fully abstracted) and simultaneously
`pending_reindex` (its index just went stale because a MECH-496 bucket split), or `retained`
(barely touched) and simultaneously `pending_reindex` -- the two axes are independent, and
folding the four states into MEM-5's single `lifecycle_state` field would force every reindex
event to also assert an abstraction-level transition it has no information about.

**Recommended shape (V4 build-time, not itself a claim):** a second field on the memory record,
e.g. `reindex_status`, taking values `none` (default) / `pending_reindex` / `under_offline_review`
/ `provisionally_reindexed` / `validated` (terminal success) / `rollback_required` (terminal
failure), read and written independently of `lifecycle_state`. `validated` is not a resting state
distinct from the others -- once the new index is accepted the field resets to `none` and the
ADDITIVE new indexing relationship MECH-513's title specifies simply becomes one more entry a
record carries, exactly as `transformation_history` already accumulates entries under MEM-5
without needing its own lifecycle slot.

**The one real coupling point:** `rollback_required` (a reindex attempt failed validation against
held-out/waking evidence) SHOULD set the record's existing `lifecycle_state` to `contested`,
reusing MEM-5's "flagged, not silently authoritative" discipline rather than inventing a second
contested-equivalent. `pending_reindex`, `under_offline_review`, and `provisionally_reindexed`
are purely internal to the reindex sub-state-machine and never touch `lifecycle_state`.

**Why `contested` is the one name shared with the raw thought's own 6-item list, and that is not
a coincidence:** the raw thought's full proposed list is `contested, pending_reindex,
under_offline_review, provisionally_reindexed, validated, rollback_required` -- six items, of
which only `contested` collides by name with MEM-5. Given the coupling point above, `contested`
was never a fifth reindex-native state needing its own slot; it is the raw thought correctly
reaching for MEM-5's existing failure-signal state rather than proposing a new one.

This resolves the design question; it does not authorise building MEM-5, `reindex_status`, or
MECH-513's substrate in V3 -- see Section header status and CLAUDE.md's V3-pending gate.
