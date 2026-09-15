---
title: "Dynamic Information Governance (ARC-145, MECH-560, MECH-561, Q-106)"
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 20
status: candidate
status_asof: 2026-09-15
status_claim: ARC-145
---

# Dynamic Information Governance

> **Placeholder ids.** `ARC-145`, `MECH-560`..`MECH-561` and `Q-106` are placeholders
> assigned by the 2026-09-15 thought-ingestion pass. The orchestrating session substitutes the
> real ids in the frontmatter, the anchors below and every cross-reference.

> **Status: candidate, substrate-conditional, diagnosis-only.** Nothing on this page is built, and
> nothing on this page authorises a `ree_core` change or a queue entry. The source thoughts are
> explicit that the first deliverable is a companion *specification* for the existing
> communication-subspace / bridge instrument, not an implementation. The one entry with
> `implementation_phase: v3` (`MECH-561`) is v3 because its **diagnostic** is runnable read-only
> over recorded trajectories, not because any mechanism should be added.

Placed under *Core Engines & Forward Models* alongside its three nearest neighbours --
[`l_space_authority_field.md`](l_space_authority_field.md) (MECH-534, Q-103),
[`mutual_legibility_communication_subspaces.md`](mutual_legibility_communication_subspaces.md)
(ARC-139, MECH-537..540, INV-105) and
[`receiver_conditioned_translation.md`](receiver_conditioned_translation.md) (MECH-547, MECH-548) --
because every claim here is an addition to that lineage rather than to the control-plane docs.

## Why a separate page

The mutual-legibility lineage asks two questions about an inter-engine interface: does the content
survive the sender's encoding, and can the receiver interpret it. This page adds a third, which the
existing pages do not carry: **when is the interpreted message allowed to matter?**

Three levels, kept apart on purpose:

| Level | Question | Owning claims |
|---|---|---|
| Content | What does this subsystem represent? | INV-104, MECH-532, V3-EXQ-1010's H-F verdict |
| Legibility | If delivered, in what form can the receiver use it? | ARC-139, MECH-537, MECH-538, MECH-539, MECH-547 |
| Jurisdiction | At this moment, how much authority does the sender have over the receiver? | **ARC-145** (this page), realised by MECH-534 |

A representation can be intact but causally silent; a transformation can be correct but unavailable
at the wrong time; a high-volume channel can be behaviourally useless if it is not selectively
coordinated with the rest of the organism.

## Three levels of claim, and what is deliberately absent

The source family insists on a separation this page enforces:

1. **Biological claim** -- travelling waves, informational tuning, anaesthetic mechanism, ephaptic
   coupling. **Out of domain for REE. Not registered.** The anchors (Misawa et al. 2026;
   Bhattacharya et al. 2022; Luo & Ester 2025; Mohanta et al. 2024 preprint; Anastassiou et al.
   2011; Buzsaki, Anastassiou & Koch 2012) are **unverified** -- no `/lit-pull` has been run on any
   of them, and per `feedback_lit_exp_decoupled` a paper resembling REE raises no claim's
   confidence. They are motivation.
2. **Architectural principle** -- ARC-145.
3. **REE-testable mechanism** -- MECH-560..4 and Q-106.

Also absent by design: the consciousness inference. `routing field present => consciousness` and
`informational tuning present => consciousness` are both refused. SENT-0 stands; SENT-1 owns the
indicator matrix.

---

## ARC-145

A complete inter-engine interface requires three properties, not two: content survives the sender's
encoding; sender and receiver are mutually legible; and the exchange occurs under a routing state
that grants the sender causal privilege over that receiver at that moment. The third property --
jurisdiction, or temporal/state access -- is a separate organisational level, with its own repair
class: an encoder fix addresses level 1, a bridge addresses level 2, and neither addresses level 3.
The architectural consequence is that REE's effective interface graph is *constructed* rather than
possessed: `G_eff(t) = f(wiring, representational geometry, control state, phase, history)`, so the
same substrate can belong to different effective networks at different times.

This is deliberately **not** MECH-539. MECH-539's third requirement is that a mapping preserve
action-conditioned transition geometry -- a property of the map, checkable with the channel
continuously open. ARC-145's is a property of the *occasion*: the same map, with intact transition
geometry, used at the wrong moment. Their failure signatures separate cleanly (`good static + bad
dynamic` versus `good static and good dynamic, but only in the right routing state`).

**Separability falsifier.** If a static bridge between frozen endpoints restores the full
behavioural phenotype irrespective of when the message is made available, level 3 is unnecessary and
this commitment should be withdrawn in favour of ARC-139 plus MECH-539.

## MECH-560

Competence tracks the selectivity, stability, repertoire and causal timing of directed influence
between engines rather than the amount transferred. The decisive signature is a dissociation at
matched traffic: endpoint content still decodable, endpoint competence intact, total inter-module
transfer matched or *increased*, integrated behaviour nonetheless degraded in proportion to lost
directional selectivity, route stability or motif repertoire. Three degradation modes are predicted
to be distinguishable -- flattening, domination by one slow global mode, and fragmentation.

**Instruments live here, not in `claims.yaml`.** The routing-fidelity `RF(t)` and tuning-index
`TI(t)` metrics, the six discriminating quantities (amount / selectivity / stability / repertoire /
behavioural appropriateness / causal necessity), and the lesion families (FLAT, SHUFFLE-TIME,
SHUFFLE-EDGE, DOMINANT-SLOW, FRAGMENT, FEEDBACK-CUT; and the sibling note's gain flattening,
direction shuffle, phase shuffle, propagation break, stereotyped slow-mode lock, top-down removal)
are instruments. They belong in the mutual-legibility work programme, following the 2026-09-07
precedent that an instrument becomes claim-shaped only when it asserts something about REE.

**Q-081's surrogate discipline is mandatory here and is adopted rather than re-derived**: a
constrained-realisation null preserving each stream's tick grid, marginal distribution and
*within-stream* autocorrelation while destroying only the between-stream relation; validation of the
surrogate against a deliberately-artefactual and a deliberately-injected statistic *before* it
adjudicates anything; and an a-priori ban on any statistic that is a function of the configured
update rates. REE's streams tick at 1, 3 and 10 steps, so the surrogate must be designed, not looked
up.

## Deferred (not registered 2026-09-15): propagation, and replay-maintained access

Two of the six drafted claims were deferred by the registering session rather than registered.
(a) PROPAGATING ROUTING STATE -- that the routing state spreads over the interface graph so adjacent
interfaces open in order, with a propagation-break lesion as falsifier. MECH-534 already owns the
coupling field as a state variable with its own dynamics; the source thought itself calls propagation
the family's most disposable idea and carries a disposal clause. Re-open if MECH-534 acquires graph
structure or a propagation-break assay is specified. (b) REPLAY MAINTAINS THE ACCESS CORRESPONDENCE,
not only the representational map (factorial representation x routing discriminator). This is the
same shape as MECH-548's proposed eighth rung and MECH-551's reduction job: an addition to MECH-540's
signature list, which is a /governance amendment decision -- flagged to governance rather than
registered beside MECH-540. Both drafts survive verbatim in the hub intake's `proposed_claims` record.

## MECH-561

The receiver-potent communication subspace is indexed by an endogenous cyclic coordinate belonging
to neither endpoint: `S_comm(A -> B | phi, c)`. A sender dimension can be inside the receiver-potent
subspace at one phase and outside it at another with no change in the sender's representation.

**Corollary, the sharper half:** temporal separability can substitute for geometric separability.
Two concurrently represented streams need not be near-orthogonal if they become receiver-effective
at different temporal addresses -- predicting a trade-off in which principal angle and
phase-conditioned overlap with `S_comm` move oppositely while behavioural intrusion stays flat.
Four-cell verdict grid: geometry-only / timing-only / joint / null.

**Distinguished from MECH-225** (phase separation of *streams* over shared capacity, whose V4
shared-capacity precondition does not bind this claim) **and from MECH-547** (conditioning on the
*receiver's* state). MECH-547's title already lists "temporal phase" among its candidate
conditioners, so a shared experiment must run a receiver-state permutation alongside a phase
permutation; if only the receiver permutation destroys the gain, MECH-547 owns the result.

**Not a new architectural option.** `2026-09-07_mutual_legibility_implementation_assays.md`
section 18 Option C ("context-gated communication subspaces") already names the design, and the
2026-09-07 intake deliberately left Options A-F unregistered pending diagnostics. Option C stays
unregistered and unbuilt; what is registered is the diagnostic proposition with its falsifiers.

## Q-106

Does closing the loop -- letting the routing state be generated partly by the aggregate activity of
the subsystems whose effective connectivity it sets -- confer any capability a matched open-loop
schedule cannot reproduce? Compared on robustness, reconfiguration speed after a context change,
adaptive routing in unseen contexts, and recovery after a transient lesion; never on raw task score,
which extra recurrence alone can move. Output marginal statistics, parameters and compute all
matched.

**Ephaptic coupling is a biological implementation clue, not part of the hypothesis.** No result here
may be described as evidence that REE has an ephaptic mechanism. This is the *last* stage of the
programme and should not be opened until the earlier stages have produced results.

---

## Staging (binding, from the source)

```
measurement
 -> descriptive routing motifs
 -> matched causal perturbation
 -> external routing overlay (experiment layer, frozen endpoints)
 -> anaesthesia-like lesion family at matched traffic
 -> replay / access-maintenance test
 -> only then endogenous field architecture
```

Diagnosis before changing the organism. The first concrete deliverable is a **dynamic-routing
companion specification** for the existing communication-subspace / bridge instrument.

## Binding substrate facts (verified 2026-09-15)

- **V3-EXQ-1010 disqualifies the obvious sender.** Trained `z_world` is not an admissible
  information-preserving source (decision-relevant content destroyed at encode time; PASS,
  `H-F-confirmed`, run `20260909T195348Z`). `rawfield25` is the primary source, `ws250_pca32` the
  replication source. Content absence must be excluded before any routing failure is claimed.
- **The P0 interface instrument now exists**: `ree-v3 experiments/_lib/interface_probe.py`
  (commit `a83f2fb`, 2026-09-10, on `origin/main`) -- `communication_subspace()`,
  `principal_angles()`, `bridge_ladder()` L0-L5, `causal_replacement()`, `manifold_guard()`,
  `dynamic_compatibility()`, `per_code_drift()`, plus `tost_equivalence`. It has no
  phase-conditioning argument, but a caller can stratify rows by phase bin and compare bases.
- **Endogenous cyclic coordinates already exist**: `ree_core/heartbeat/clock.py` carries
  `_e3_phase_step` with MECH-091's salient-event `phase_reset()`, `_breath_phase_step` over
  `[0, breath_period)` with a `sweep_active` window (MECH-108, `breath_period` defaults 0 = OFF),
  and the E1/E2/E3 multi-rate tick grid (ARC-023 / SD-006 phase 1). All readable via
  `MultiRateClock.get_state()`.
- **What does not exist**: any time-resolved directed-influence estimator between engine interfaces;
  any routing-motif discovery or repertoire measure; any per-directed-edge gain `g_ij(t)` with its
  own state; any propagation of routing state across the interface graph; any
  `(sender_episode, receiver_episode)` pairing in `ree_core`. Nothing in `substrate_queue.json`
  plans any of these.
