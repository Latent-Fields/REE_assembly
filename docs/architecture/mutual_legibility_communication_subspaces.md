---
title: "Mutual Legibility and Communication Subspaces (ARC-139, MECH-537..540, INV-105; INV-109, INV-110, MECH-562, Q-107)"
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 16
status: candidate
status_asof: 2026-09-15
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

## Registered 2026-09-15 from the hippocampal campaign cluster {#hippocampal-campaign-2026-09-15}

Source thoughts: `docs/thoughts/2026-09-09_exq1010_substrate_readiness_audit.md` (INV-109) and
`docs/thoughts/2026-09-09_hippocampal_replay_interface_maintenance_supplement.md` (INV-110, MECH-562,
Q-107); intakes under `evidence/planning/thought_intake_2026-09-09_*`. The two archaeologies and the
campaign adjudication registered nothing. Implementation-gap audit at registration: the audit's
"assay A/B NO-GO, build the instrument first" verdict is SUPERSEDED -- `experiments/_lib/interface_probe.py`
landed in ree-v3 on 2026-09-10 (RRR subspace, principal angles, L0-L5 bridge ladder, causal replacement,
manifold guard, dynamic compatibility, TOST). Remaining genuine gaps: no receiver-conditioned `T(A,B)`
rung (MECH-547 has no instrument), no arm F (receiver-local self-repair), no native-consumer causal
replacement (caps every result at INV-105 rung 4).

### INV-109 -- a reproduced recipe is not a frozen endpoint {#inv-109}

Re-running a documented training recipe reconstitutes an operating REGIME and licenses a within-run
paired comparison, never a claim about the identity of the artifact a prior run measured. Naming an
earlier endpoint requires its weights and observations to have been persisted and loaded; a pinned
substrate commit constrains the code, not the realised weights. Discriminator: a recorded state hash at
both endpoints, re-verified at every evaluation boundary, mismatch aborting. Load-bearing for every
assay defined over "frozen endpoints" (MECH-538, MECH-547, MECH-548, MECH-540). Distinct from GOV-EQUIV-1
(equivalence of claim representations, not artifacts).

### INV-110 -- the interface-repair adjudication standard {#inv-110}

A repair claim is admissible only from one design (or one tightly integrated series) that closes all
six links itself: measured change in a transfer-relevant direction; local preservation at both
endpoints; access loss by a causal receiver-dependent output; pair-specific maintenance against a
within-context permutation; causal restoration on held-out episodes; rival exclusion at matched budgets.
A Gate-0 lesion proof (oracle-restorable, null-subspace-drift-insensitive) precedes every maintenance
arm, and the estimand is the paired arm beating the MAXIMUM of permuted-pair, receiver-local-adaptation
and local-rehearsal arms, never the unmaintained floor. Local-memory equivalence is a prospective
equivalence test, never a post-hoc covariate. Standalone rather than an INV-105 amendment, by the
GFLAG-0235 precedent.

### MECH-562 -- receiver-local self-healing as the standing rival {#mech-562}

A consumer can restore its use of a drifting sender with no pair identity, cross-system label or replay,
by adjusting afferent weights from sender activity and its own output under homeostatic error against
pre-drift output statistics. It yields the same observable as interface repair, so any replay-attributed
rescue must beat a faithful implementation of it at matched update budget. Its preconditions are its
predictions (redundant smooth tuning, incremental drift, plasticity at least as fast as drift, enough
sampling), so its advantage is a function of the drift-rate-to-maintenance-interval ratio; an unswept
timescale silently chooses the winner. Zero prior coverage in the registry. Rival to MECH-540.

### Q-107 -- code change versus world change {#q-107}

Can a system distinguish a change in its own code from a change in the world that code represents, and
if not, what is a maintenance mechanism entitled to preserve? A label-free adaptive readout can "correct"
a truthful update away and report it as stability. Any repair claim must show the pre-drift mapping was
still the correct one, which needs an anchor outside both endpoints that REE does not currently represent.
Whether such an anchor is necessary, or self-consistency plus behavioural adequacy is the only coherent
criterion for an embedded system, is open.

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
