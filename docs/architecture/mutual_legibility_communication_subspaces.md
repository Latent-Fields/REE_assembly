---
title: "Mutual Legibility and Communication Subspaces (ARC-139, MECH-537..540, INV-105)"
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 16
status: candidate
status_asof: 2026-09-08
status_claim: ARC-139
---

# Mutual Legibility and Communication Subspaces

Registered 2026-09-08 from the three-document thought package of 2026-09-07
(`docs/thoughts/2026-09-07_mutual_legibility_communication_subspaces.md` and its
implementation/implications companions), via
`evidence/planning/thought_intake_2026-09-07_mutual_legibility.md`.

The operational work programme (ML-00 .. ML-61, plus conditional ML-A architecture
placeholders) lives in `evidence/planning/mutual_legibility_work_program_20260907.md`
and is deliberately NOT restated here. This document carries only the claim-bearing
content.

**Standing caveat for every claim on this page:** these are `substrate_conditional`
registrations. DO NOT build a `LatentBridge` module in `ree_core`, DO NOT train modules
toward global representational similarity, and DO NOT queue a sleep mutual-legibility
experiment. The sanctioned near-term work is a READ-ONLY diagnostic harness over frozen
checkpoints and recorded trajectories.

---

## ARC-139 -- Integration does not require representational sameness

The organising proposition. Specialised subsystems may preserve distinct, high-dimensional,
private internal representations while coordinating through low-dimensional, context-sensitive
communication subspaces and low-complexity transformations. Development can raise local
specialisation and cross-system legibility *at the same time*.

The architectural picture is a federation, not a convergence:

```text
rich specialised representation A
        |       private dimensions
        |\
        | \ communication subspace A->B
        |  \
        v   v
     consumer B ---- specialised local dynamics
        |
        | communication subspace B->C
        v
     consumer C
```

This is an explicit ALTERNATIVE to ARC-121's shared epistemic-state-object framing, not a
refutation of it. Four architectures remain live: (1) one common epistemic object consumed by
many systems; (2) specialised objects sharing a low-dimensional interface format; (3)
specialised objects joined by context-specific translations; (4) a hybrid invariant core plus
private dimensions. The communication-subspace evidence makes 2-4 credible enough that ARC-121
must not be used to prejudge the question. No change is made to ARC-121 here.

## MECH-537 -- Communication-subspace routing: encoded but not exposed

A task variable can be strongly encoded in the full sender latent while being weakly represented
in the *consumer-facing* subspace, producing the phenotype

`external probe succeeds -> native behaviour fails`

without any information having been destroyed. This is a third category between "information
absent from the sender" and "information used by the receiver".

It is distinct from MECH-517 (interface *collapse*, where the decoder is rank-deficient or
decision-boundary-collapsed) and from MECH-532 (a compression site lacking a trained
decompression stage). Routing failure needs neither a collapse nor a missing readout: the
consumer can read a perfectly healthy subspace that simply does not contain the distinction.

Estimated by cross-validated Reduced Rank Regression from sender activity to the *actual*
consumer input, then comparing task decodability in the full sender, in the communication
subspace, and in its orthogonal complement.

## INV-105 -- The latent-access evidence ladder

A variable's status in a latent space is not one property but seven, which must never be
collapsed:

1. **encoded** -- statistically present;
2. **decodable** -- recoverable by an external probe;
3. **natively accessible** -- usable by the system's existing consumer;
4. **bridgeable** -- usable through a constrained map between frozen endpoints;
5. **pairing-specific** -- useful specifically when the correct sender state is paired with the
   correct receiver situation;
6. **causally used** -- interventions on its content alter downstream computation;
7. **behaviourally beneficial** -- that causal use improves adaptive performance.

> **decodable != accessible != bridgeable != pairing-specific != causally used != behaviourally
> beneficial.**

Two evidential consequences are binding rather than advisory:

- **Correct-vs-mismatched-vs-zero controls are mandatory before any content-transmission
  claim.** A channel can be strongly load-bearing while its example-specific content is barely
  load-bearing. The interpretive categories are: `correct >> mismatched ~= random` (content
  use); `correct ~= mismatched >> zero` (generic channel effect); `correct ~= zero` (not
  load-bearing).
- **A compressed representation must be scored against a dimensionality-matched RANDOM
  projection floor, not against zero.** The 2026-09-07 waypoint-field probe (`ree-v3`
  `f00402c9`) measured mean directional lift of +0.269 raw, +0.211 through a random 275 -> 32
  projection (~78% retention), +0.167 through an untrained SplitEncoder (~62%). A null measured
  without that floor cannot be read as "the dimension was too small" or "z_world discarded it".

INV-104 is the sender-side half (preserve organism-relevant distinctions). This is the
consumer/evidence-side half: preservation is necessary and not sufficient, and probe success
licenses only rung 2.

## MECH-538 -- Minimum bridge complexity as the measure of mutual legibility

For systems A and B and a family of constrained mappings `T_k` of increasing complexity,

`L(A -> B) = minimum bridge complexity achieving a predeclared held-out functional criterion`

over the ladder: native readout; orthogonal (Procrustes); affine; low-rank affine; constrained
nonlinear; high-capacity (upper bound only). Lower `L` means greater mutual legibility. **The
simpler the bridge that works, the stronger the evidence that the sender already held an
appropriately structured representation** -- a high-capacity bridge that succeeds may simply be
performing new cognition, and is evidence about the bridge rather than about the endpoints.

`L` must never be read alone: two systems that become identical because one lost its
specialisation would show falling `L` with worsening cognition. Development is therefore tracked
on two axes -- local specialisation/competence, and cross-system mutual legibility.

**Non-redundant developmental prediction:** sender and receiver each improve local competence,
global representational similarity stays flat or falls, task information concentrates in the
consumer-facing subspace, and minimum bridge rank falls. That signature -- *coordination without
homogenisation* -- is what would distinguish this claim from ordinary co-training.

## MECH-539 -- Dynamic interface compatibility

Between predictive systems (E1, E2), pointwise state correspondence is insufficient. A bridge
must also satisfy: `receiver_transition(T(x_t), a_t)` is compatible with `T(x_(t+1))` under the
relevant action/context. A map can succeed pointwise while destroying transition geometry.

Diagnostic separation: map only the initial state and let the receiver evolve natively, versus
repeatedly mapping sender rollout states. This distinguishes a bridge that supplies a compatible
starting condition from one that must continually correct incompatible dynamics. Failure
signature `good static + bad dynamic` routes to transition-geometry work, not to representation
work.

Related to but distinct from INV-088's rollout-consistency lineage, which concerns E1's own
multi-step transition fidelity rather than the geometry of an interface between two systems.

## MECH-540 -- Sleep as selective interface maintenance

MECH-529 gives offline consolidation two jobs: revise the representation (split/merge/reweight)
and re-index episodic traces so autobiographical addressability survives. This claim adds a
**third**: adjust or stabilise the *interface* -- the subspace through which another subsystem
reads the revised representation.

The prediction is explicitly NOT global alignment. It is a **plasticity/stability division of
labour**: some interfaces reconfigure because recent learning demands it, while others stay
stable because downstream continuity matters more. Four distinguishable post-sleep signatures:
S1 representational retuning (interface metrics move only because the sender moved); S2
interface recalibration (local competence stable, bridge complexity improves); S3 stable
scaffold (representations move, mapping holds); S4 maladaptive homogenisation (similarity rises,
differentiation worsens).

**No biological evidence currently establishes that sleep reduces a formal bridge-complexity
metric between two independently specialised systems.** That is the REE hypothesis, not an
imported finding. The sleep assay is therefore sequenced LAST, after a waking interface metric
has demonstrated range and stability -- otherwise it measures the instrument rather than the
organism.

---

## Failure-class routing

The diagnostic value of the package is that it partitions "REE contains the information but does
not behave as though it does" into distinguishable classes:

| Class | Signature | Routes to |
|---|---|---|
| F1 | target absent from sender | representation/training work; do NOT build a bridge |
| F2 | target in sender, absent from communication subspace | interface/routing (MECH-537) |
| F3 | target in subspace, receiver insensitive | consumer computation, valuation, candidate diversity, commitment |
| F4 | simple bridge rescues statics, not dynamics | transition geometry (MECH-539) |
| F5 | only a high-capacity bridge rescues | upper-bound evidence only; suspect new cognition |
| F6 | correct ~= mismatched >> zero | generic channel effect; no content claim (INV-105) |
| F7 | correct >> mismatched but states grossly off-manifold | causally informative, architecturally suspect |
