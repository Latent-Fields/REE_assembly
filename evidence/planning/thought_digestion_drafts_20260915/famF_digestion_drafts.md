# Digestion drafts -- FAMILY F

**Source thought:** `docs/thoughts/2026-09-09_shared_reference_frames_and_temporal_gates.md`
**Date:** 2026-09-15 -- **NOT part of the intake.** These are `/thought-digestion` drafts
(`what_would_answer` candidates + disposition recommendations), offered for a later hardening pass.
Nothing here was written into `claims.yaml`.

Method note: falsifier language is EXTRACTED from the thought (sections 7, 8, 11) and from the
already-written assay specification
(`evidence/planning/hippocampal_campaign_assay_specifications_20260910.md`) wherever it exists, rather
than invented. Where an existing sibling's wording covers a condition, it is reused verbatim.

**Currency check performed (2026-09-15):** V3-EXQ-1010 has RUN and RESOLVED -- manifest
`v3_exq_1010_zworld_overcapacity_decoder_sweep_20260909T195348Z_v3.json`, outcome PASS,
`hypothesis_verdict: H-F-confirmed`, "the decision-relevant content is DESTROYED AT ENCODE TIME: no
decoder in the capacity ladder recovers the oracle above the bar from the frozen latent ... The repair
is at the ENCODER'S OBJECTIVE, not at the consumer", with the `rawfield_ceiling` positive control at
0.9735 worst-seed. It is `evidence_direction: non_contributory`, `claim_ids: []`, and already in
`review_tracker.json`. **This bounds the whole family and every draft below is written against it.**
`docs/CURRENT_FRONT.md` (generated 2026-09-14 from a 2026-09-08 insights report) still describes 1010
as "queued and running" -- a generated-doc staleness, not a claim error.

---

## D1. NEW-MECH-1 -- reference-frame mediation

**NON-DEGENERACY PRECONDITION (this is the gate; check it before anything else).** Three conditions,
all failing today:

1. **An adequate source.** V3-EXQ-1010 CONFIRMED H-F at `observation -> z_world`: the decision-relevant
   content is destroyed at encode, so at THAT locus there is nothing mis-framed to detect and a frame
   permutation would measure noise. A frame assay is only interpretable at an interface whose source
   passes an adequacy check first -- `rawfield25` (0.9735 worst-seed) or a post-SD-106 encoder, not
   the shipped P0 latent. Running RF-1..RF-4 on an inadequate source cannot distinguish RF-F from F1
   (target absent from sender) and would produce a false RF-F-eliminated.
2. **At least two candidate frames that are distinguishable in V3.** Zero matches in `ree_core/` for
   `egocentric`, `allocentric`, `reference_frame`, `ref_frame`, `frame_id`, so the frames must be
   supplied by the experiment layer. The assay spec already does this (five frame levels, assay A
   section 2.2) -- but note level (ii), the invertible 90/180/270 rotation, is a CONSTRUCTED frame,
   not one REE learned, so it tests the instrument's sensitivity, not whether REE spontaneously
   preserves a shared index.
3. **The G4 instrument gate.** "Known invertible frame transform with its exact inverse. If this does
   not restore the consumer, the instrument cannot detect any transformation effect and the run is
   refused." Reused verbatim from the assay spec.

**CONFIRMING.** On a source that passed adequacy, at frozen endpoints and matched capacity, data,
optimisation and conditioning-channel width: held-out consumer use under the intact frame is
**substantially greater** than under a within-stratum frame permutation, **while the task target
remains decodable at the same level in both** (the permutation preserved content and marginal
difficulty), AND `A3_frame_cond` clears `A1_source_only` on the compositional holdout cells (frame
level x query level unseen in fitting). A frame permutation that disrupts **only one** downstream
consumer confirms the weaker, consumer-specific reading and MUST be reported as such rather than as
a shared global frame.

**FALSIFYING.** Any of: (a) intact ~= frame-permuted at matched decodability -- the frame is
incidental at this interface; (b) `A3_frame_cond ~= A1_source_only` on the holdout cells, i.e.
conditioning on the frame label buys nothing over an unconditional low-rank bridge; (c) the frame
effect disappears once marginal difficulty is equalised, i.e. the permutation was off-distribution
rather than frame-destroying (assay spec guard 6); (d) frame alignment does NOT lower the minimum
bridge rung `L(A -> B)` in any tested pair -- this falsifies the claim's second non-redundant
prediction specifically while leaving the first open, and should motivate a narrower successor rather
than a flat fail.

**Recommended disposition: (f) DEFER, with reason** -- and the reason is sequencing, not doubt.
Everything the claim needs exists except an adequate source at a named locus, and 1010 just
established that the primary locus does not have one. The claim should sit `candidate` until either
SD-106 validates or the assay runs on `rawfield25`. Secondary disposition if governance disagrees on
2.1: **(g) MERGE into ARC-142**, naming NEW-MECH-1 absorbed, RF-F and the frame-permutation control
lifted into ARC-142's notes, reverse-deps = none (nothing yet depends on it).

---

## D2. NEW-MECH-2 -- temporal-gate adequacy

**NON-DEGENERACY PRECONDITION.** The manipulated phase must be one the receiver's plasticity or read
actually tracks, and the comparison must hold quantity fixed. Extracted from the thought
("preserve total communication energy/updates so that timing, not quantity, is the manipulated
variable") and from Gate B2 verbatim: "Match event count, phase occupancy, activity magnitude and
total absolute weight change. Do **not** interpret a timing interaction if the shifted condition
changes data exposure or update magnitude." Additional precondition specific to REE: the interface
under test must have a receiver whose state can change as a result of the read at all -- note
`mech092-replay-consumer-missing` (substrate_queue, `proposed_REGISTRATION_ONLY`): `_do_replay`
computes replay trajectories and discards them, so the replay -> consumer interface has **no
consumer**, and a timing manipulation there is unfalsifiable by construction.

**CONFIRMING.** Correctly paired content delivered at the target phase produces a downstream change
(receiver parameter/state change, consumer-use gain, or post-sleep retention) that early-shifted,
late-shifted and phase-shuffled delivery do not, at matched event count, phase occupancy, activity
magnitude and total absolute weight change -- and the effect survives the pairing controls that
already bind (correct vs mismatched vs zero vs moment-matched random, INV-105). Per MECH-540's
two-interface requirement, the timing effect must be measured on **at least two interfaces with
different predicted plasticity**; a timing effect identical on both is generic plasticity scheduling,
not interface-specific gating.

**FALSIFYING.** Any of: (a) target-phase ~= shifted at matched energy -- timing is not a factor at
this interface, and TG-F may not be invoked to excuse its nulls; (b) the apparent timing effect
tracks total update magnitude or exposure rather than phase (the Gate B2 disqualifier); (c) the
effect appears at every phase offset, i.e. what varied was not phase; (d) **the strong falsifier for
the claim's evidential rule specifically:** a systematic re-measurement of interface nulls under a
phase-controlled protocol recovers none of them -- the phase control adds cost and changes no verdict,
which would make TG-F a distinction without a difference and argue for retiring it to a
documentation note rather than a claim.

**Recommended disposition: (a) TESTABLE NOW ON V3 SUBSTRATE, with one caveat** -- the levers are
built (MECH-089 `ThetaBuffer`, MECH-272 `routing_gate.py`, MECH-091 `phase_reset`, `MultiRateClock`,
`force_sleep_cycle_at_eval_boundary`), the instrument is built (`interface_probe.py`, whose
`CaptureRecord` already carries `phase`), and the manipulation is specified (Gate B2). The caveat is
that Gate B2 is explicitly staged "only after content specificity is established" at Gate B1, so this
is testable-but-sequenced, not testable-now-in-practice. Governance should consider routing
NEW-MECH-2 `implementation_phase: v3` on this basis -- the same reasoning that put MECH-537 and
INV-105 at v3 while their siblings defaulted to v4.

---

## D3. MECH-537 (candidate, substrate_conditional, no `what_would_answer`)

The thought materially bears on this claim: it argues the communication subspace is under-specified
without saying what its directions are indexed against, and that a fixed-subspace estimate can
under-read an interface that is healthy but differently framed (MECH-547 already makes the parallel
point for receiver state).

**NON-DEGENERACY PRECONDITION.** A source that passes adequacy (see D1.1 -- 1010's H-F-confirmed
verdict means the primary locus does not), and a `receiver_input` tensor that is the signal the LIVE
consumer actually reads, not a neighbouring tensor (the assay doc's own "critical rule", which
`interface_probe.CaptureRecord` explicitly cannot enforce).

**CONFIRMING.** `target decodable from X` AND `poorly decodable from P_comm X` on held-out data, with
the orthogonal complement carrying the decodability, cross-validated RRR rank selected on a held-out
block, and the consumer demonstrably insensitive to the complement.

**FALSIFYING.** The target is as decodable inside the estimated communication subspace as in the full
sender (no routing failure -- route to F3, consumer insensitivity, or F1), OR the subspace estimate is
unstable across frame or receiver-state strata, in which case the single-subspace premise fails and
the question belongs to MECH-547 / NEW-MECH-1 rather than here.

**Recommended disposition: (a) testable now**, unchanged from the parent intake's routing -- the RRR
estimator exists in `interface_probe.communication_subspace`. This draft adds only the stratification
caveat.

---

## D4. MECH-539 (candidate, substrate_conditional, no `what_would_answer`)

Bearing: the thought's section 10.3 asks the dynamic-compatibility assay to "report whether sender and
receiver transitions are being compared in the same action/time frame" -- a precondition MECH-539
does not currently state.

**NON-DEGENERACY PRECONDITION (the thought's addition).** Sender and receiver transitions must be
compared in the SAME action and horizon frame before any `good static + bad dynamic` reading is taken.
A transition-geometry null measured across a frame mismatch (one indexed at observation time, one at
predicted action time) is uninterpretable, and would be scored as F4 when it is F8/RF-F.

**CONFIRMING.** Map-initial-only (receiver evolves natively) preserves one-step and multi-step
compatibility while repeated re-mapping of sender rollout states does not -- or the reverse, each
routing differently -- with the frame correspondence asserted rather than assumed, and horizons
matched to those used to judge predictive competence (MECH-548's requirement).

**FALSIFYING.** Pointwise and transition compatibility move together across every bridge rung, i.e.
transition geometry adds no separable failure mode; or the `good static + bad dynamic` signature
disappears once the action/time frame correspondence is fixed, which would reassign the phenomenon to
NEW-MECH-1.

**Recommended disposition: (f) defer** -- MECH-539's own notes already say the diagnostic does not
yet exist; `interface_probe.dynamic_compatibility` now supplies the primitive, so the reason to defer
is the same adequacy-of-source gate as D1, not absence of an instrument.

---

## D5. MECH-540 (candidate, substrate_conditional, no `what_would_answer`)

Bearing: the thought's section 10.5 says the sleep programme "should no longer ask only whether an
interface changed before versus after sleep" but which replay event was active, what frame it
instantiated, which consumer was receptive, at what phase, which interface changed, and whether waking
recurrent stability improved.

**NON-DEGENERACY PRECONDITION.** Two interfaces with DIFFERENT predicted plasticity measured
simultaneously (MECH-540's own requirement, operationalised in the assay spec as `I_drift` and
`I_stable`), plus the parent package's sequencing bar: a waking interface metric must have
demonstrated range and stability at one locus first. `force_sleep_cycle_at_eval_boundary` exists,
which is exactly why the sequencing bar is stated -- cheapness is the trap.

**CONFIRMING.** S2 (interface recalibration): local competence stable at both endpoints by equivalence
test, communication-subspace rotation or bridge complexity improves on the plastic interface and not
on the stable one, and -- per MECH-548's corollary and this thought's section 10.5 -- closed-loop
waking stability is preserved or improved after the change.

**FALSIFYING.** S4 (maladaptive homogenisation): cross-system similarity rises while local competence
or task-specific differentiation falls -- registered as a FAILURE, not a partial success. Or both
interfaces move identically, which is generic plasticity. Or a static probe improves while the next
waking trajectory destabilises (MECH-548's S5, which GFLAG-0235 left on MECH-548).

**Recommended disposition: (c) substrate-blocked -- `substrate_conditional` (unchanged)**, plus a
note that the phase/event identifiers section 10.5 asks for are the SAME fields Gate B2 already
specifies, so no new instrument is owed.

---

## D6. MECH-547 (candidate, substrate_conditional, no `what_would_answer`)

Bearing: the thought's temporal-gate thread makes explicit an item MECH-547 lists in passing
("temporal phase" among receiver-state conditioners).

**Draft addition only** (the sibling intake deferred the full hardening): a `what_would_answer` for
MECH-547 should state that **the temporal-phase item in its conditioner list is NOT tested by the
receiver-state permutation control**, because permuting receiver state within a phase stratum leaves
phase intact. If a future result attributes a `T(A,B)` gain to "temporal phase", it is a NEW-MECH-2
result, not a MECH-547 result, and the two must be scored separately.

**Recommended disposition: (f) defer** the full draft to `/thought-digestion` per the sibling intake;
register only the separation note above so the ambiguity is not inherited.

---

## D7. MECH-096 (candidate, no `what_would_answer`, no `epistemic_category`)

Bearing: MECH-096's notes carry REE's ONLY registered reference-frame commitment -- "Dorsal-equivalent
head: egocentric, action-relevant, high temporal resolution -> z_self. Ventral-equivalent head:
allocentric, object-identity, sustained representation -> z_world" -- and it has never been
implemented (zero `egocentric`/`allocentric` matches in `ree_core/`).

**NON-DEGENERACY PRECONDITION.** Two structurally distinct encoder heads must exist with a testable
frame difference. V3 has a z_self/z_world split (SD-005 SplitEncoder) but nothing that makes one
egocentric and the other allocentric, and nothing that measures which frame either occupies. The
claim is currently untestable in the vacuous sense ARC-087 records for its own substrate gate.

**CONFIRMING.** With both heads live, a frame-diagnostic probe recovers self-relative coordinates from
z_self and agent-position-invariant coordinates from z_world at above-chance separation, AND removing
the architectural distinction (a single encoder with a learned routing gate, the alternative
MECH-096 explicitly rejects) degrades the separation and the downstream split -- the claim's own
stated failure mode, "the z_self/z_world split degrades back toward z_gamma conflation".

**FALSIFYING.** A single encoder with a learned routing gate produces the same downstream behaviour
and the same stream separation, i.e. the two-head architectural requirement is not load-bearing; or
the two heads exist and neither occupies a recoverable frame, in which case the egocentric/allocentric
language should be retired from the claim as biological motivation rather than architectural content.

**Recommended disposition: (c) substrate-blocked -- `substrate_conditional`, and a currency note that
the frame half was never built.** NOT (e) excrete: it is the only place REE records a frame
commitment, and NEW-MECH-1 now depends on it. A `/governance` pass should set
`epistemic_category: substrate_conditional` (currently absent) rather than leave the claim
surfaceable as ready experiment work.

---

## Summary of recommended dispositions

| Claim | Disposition | One-sentence justification |
|---|---|---|
| NEW-MECH-1 | (f) defer, secondary (g) merge into ARC-142 | Everything needed exists except an adequate source at a named locus, which V3-EXQ-1010 just showed the primary locus does not have. |
| NEW-MECH-2 | (a) testable now, sequenced behind Gate B1 | The levers, the instrument and the manipulation spec are all built; only the staging bar is unmet, which argues for a v3 routing. |
| MECH-537 | (a) testable now | `interface_probe.communication_subspace` supplies the RRR estimator the claim is operationalised on. |
| MECH-539 | (f) defer | The instrument now exists; the source-adequacy gate does not. |
| MECH-540 | (c) substrate-blocked, `substrate_conditional` unchanged | Two-interface plasticity comparison plus the waking-metric sequencing bar are both unmet. |
| MECH-547 | (f) defer full draft; record the phase/state separation note | A temporal-phase gain is a NEW-MECH-2 result and must not be scored as receiver conditioning. |
| MECH-096 | (c) substrate-blocked + currency note | Its egocentric/allocentric frame requirement is asserted and unimplemented, and it carries no `epistemic_category` to suppress surfacing. |
