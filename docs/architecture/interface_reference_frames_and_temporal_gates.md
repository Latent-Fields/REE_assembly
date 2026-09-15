---
title: "Interface Reference Frames and Temporal Gates (MECH-555, MECH-556)"
parent: "Core Engines & Forward Models"
grandparent: Architecture
nav_order: 19
status: candidate
status_asof: 2026-09-15
status_claim: MECH-555
---

# Interface Reference Frames and Temporal Gates

**Status:** candidate, registered 2026-09-15 from
`docs/thoughts/2026-09-09_shared_reference_frames_and_temporal_gates.md`
(intake: `evidence/planning/thought_intake_2026-09-09_shared_reference_frames_and_temporal_gates.md`).
Child of [Mutual Legibility and Communication Subspaces](mutual_legibility_communication_subspaces.md)
(ARC-139, MECH-537..540, INV-105); sibling of
[Receiver-Conditioned Translation and Recurrent Interface Stability](receiver_conditioned_translation.md)
(MECH-547, MECH-548) and of [The Cognitive Contract](cognitive_contract.md) (ARC-142).

Nothing here is a build instruction. Both claims are `candidate`, `substrate_conditional`, and carry a
"do not build in V3, do not queue" caveat. Neither authorises new instrument work: the assays that
would test them were specified independently in
`evidence/planning/hippocampal_campaign_assay_specifications_20260910.md` (assay A frame levels and
`A3_frame_cond`; assay B Gate B2 timing) and the primitives are already built in
`ree-v3/experiments/_lib/interface_probe.py`.

**Working principle (verbatim from the thought):**

> Mutual legibility may depend not only on what information is present and how it is geometrically
> exposed, but on whether sender and receiver refer that information to a compatible relational frame
> and whether the interface is opened at the moment when the receiver can use it. Specialised systems
> can therefore remain globally different while becoming locally, relationally, and temporally
> coordinated.

## The interface-factor decomposition

The parent package's ladder (`encoded -> decodable -> natively accessible -> bridgeable ->
pairing-specific -> causally used -> behaviourally useful`, INV-105, plus MECH-548's proposed eighth
rung `recurrently stable`) answers *what a measurement establishes*. A second and separate
decomposition answers *what must be jointly correct for causal communication to occur at all*:

| Factor | Question it answers | Owning claim |
|---|---|---|
| content | does the sender contain the distinction? | INV-104 (sender-side preservation) |
| communication subspace | is the distinction inside the directions the consumer reads? | MECH-537 |
| **reference frame** | **relative to what relation is it indexed?** | **MECH-555** |
| receiver context | is the receiver in a state where it is interpretable? | MECH-547 |
| **temporal gate** | **is it delivered when the receiver can use or learn from it?** | **MECH-556** |
| recurrent stability | does repeated use stay on-manifold and calibrated? | MECH-548 |

Both decompositions are retained; they are not rungs of one another.

## MECH-555 -- reference-frame mediation {#mech-555}

A communication subspace says *which directions* of a sender matter to a receiver. A reference frame
says *what relation those directions are indexed against*. Two systems can use very different local
codes and still interoperate if they preserve a common relational coordinate -- self-relative
direction, allocentric position, temporal order, object or episode identity, action candidate, causal
source. The frame need not be symbolic or hand-written; it can be learned.

The registered failure class is **RF-F**: a probe succeeds on sender *and* receiver, nothing is
missing and no subspace is collapsed, yet native cross-system use fails because the two index the
content against incompatible coordinates -- one allocentric and one egocentric, one
current-position-relative and one trajectory-origin-relative, one at observation time and one at
predicted action time. The repair is relational re-indexing, not more capacity.

The discriminator is a **content-preserving frame permutation**: permute frame labels or anchors
between episodes or positions while holding the sender-state distribution, marginal difficulty and
content statistics fixed.

- intact >> frame-permuted, target still decodable in both -> shared indexing is functionally load-bearing;
- intact ~= frame-permuted -> the frame is incidental at that interface;
- frame preserved but content permuted performs poorly -> content specificity remains necessary (INV-105 rung 5);
- frame permutation disrupts only one downstream consumer -> frames are consumer-specific, not globally shared.

**Architectural caution, part of the claim.** Do not prescribe a universal coordinate vocabulary; look
for relational invariants already emerging in trained systems; prefer low-complexity frame
transformations; keep the frame separate from the content indexed by it; allow different interfaces
to use different frames; and do **not** infer one global workspace or one shared object merely because
several consumers share an indexing relation.

## MECH-556 -- temporal-gate adequacy {#mech-556}

A bridge says *how* content could cross. A temporal gate says *when crossing is allowed to matter*.
The same content through the same pathway can have different effects depending on whether it arrives
before, during or after a prediction update, a replay event, or an action-selection window.

The registered failure class is **TG-F**: source content present, receiver-facing geometry adequate,
bridge low-complexity, correct-pair specificity satisfied, receiver on-manifold -- and still no
downstream effect, because the information arrived outside the phase in which the receiver is
plastic, receptive, or using that quantity.

The binding evidential consequence, deliberately shaped like INV-105's two: **a null measured at an
interface whose engagement phase was not a controlled variable does not license "the interface is
semantically useless" or "the information was lost"** until the same correctly paired content has
been delivered at a target phase versus early-shifted, versus late-shifted, versus phase-shuffled, at
**matched communication energy, event count and update magnitude** -- so that timing, not quantity, is
the manipulated variable.

**Do not add a gate mechanism to make the test runnable.** REE's existing wake/sleep/control-plane
substrate is expected to express the manipulation, and a demonstration that it cannot is itself the
finding.

## Failure-class routing -- proposed extension

The parent doc's routing table runs F1-F7. These two classes extend it; the extension is proposed
here rather than edited into the parent, on the GFLAG-0235 precedent (an extension stays on the claim
that carries it until it matures).

| Class | Signature | Routes to |
|---|---|---|
| F8 = RF-F | probe succeeds on both endpoints, native use fails, frame permutation is destructive | relational re-indexing (MECH-555) |
| F9 = TG-F | interface adequate on every static criterion, no downstream effect, phase uncontrolled | timing control before any content verdict (MECH-556) |

## Where this already exists in V3

Recorded so that neither claim is read as a build proposal. Verified against `ree-v3` 2026-09-15.

| Thing the thought treats as needed | V3 status |
|---|---|
| shared latent read by several engines | `z_world` (1457 references across `ree_core/`) -- shared representation, not a shared *frame* |
| a frame distinction between the core latents | MECH-096 *specifies* z_self egocentric / z_world allocentric; zero matches for egocentric, allocentric, reference_frame, ref_frame, frame_id anywhere in `ree_core/` |
| learned shared relational binding between two streams | `ree_core/latent/cross_stream_binder.py` -- learned contrastive conjunction between z_self and z_world, theta-gated, with a shuffle control; measured ceiling at V3-EXQ-641a/720/725 |
| temporal gating of an inter-engine read | built at three grains: MECH-089 `ThetaBuffer`, MECH-272 `ree_core/sleep/routing_gate.py`, MECH-122 spindle content packaging |
| a lever to shift engagement phase | MECH-091 `phase_reset`, `MultiRateClock` (ARC-023 / MECH-093 / MECH-108), `force_sleep_cycle_at_eval_boundary` |
| interface instrument (subspace, ladder, causal replacement) | `ree-v3/experiments/_lib/interface_probe.py`, contract-tested |
| phase recorded in interface telemetry | `CaptureRecord.phase` and `active_gates` exist; nothing treats phase as a factor |
| frame recorded in interface telemetry | absent -- no frame field |

## Evidence status

No experiment has been run against either claim. Both external anchors (Steel et al. eLife reviewed
preprint 110234; Okyere et al. bioRxiv 10.64898/2026.09.02.748628) are taken from the source thought's
reference list, are **not independently verified**, and per `feedback_lit_exp_decoupled` raise no
claim's confidence. The section-9 conjunction hypothesis -- that replay opens transient,
frame-aligned communication windows -- is deliberately unregistered: the thought itself states the
biology supports the two halves separately and not their conjunction.
