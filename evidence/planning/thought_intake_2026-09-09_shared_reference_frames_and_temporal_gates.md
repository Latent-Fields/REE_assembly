# Thought intake -- Shared reference frames and temporal gates in cross-system mutual legibility

**Date processed:** 2026-09-15
**Raw thought:** `docs/thoughts/2026-09-09_shared_reference_frames_and_temporal_gates.md` (471 lines)
**Session:** thought-pipeline-20260915 (family F)
**Parent (already ingested, not re-derived):** `evidence/planning/thought_intake_2026-09-07_mutual_legibility.md`
(ARC-139, MECH-537, MECH-538, MECH-539, MECH-540, INV-105)
**Sibling (already ingested, not re-derived):** `evidence/planning/thought_intake_2026-09-08_receiver_conditioned_translation_and_recurrent_interface_stability.md`
(MECH-547, MECH-548)
**Implementation companion:** `docs/thoughts/2026-09-07_mutual_legibility_implementation_assays.md`
**Read for currency (both POSTDATE the raw thought and both already carry its threads):**
`evidence/planning/hippocampal_translation_maps_biology_campaign_20260909.md`,
`evidence/planning/hippocampal_campaign_assay_specifications_20260910.md`,
`evidence/planning/hippocampal_translation_maps_literature_tranche_3_receiver_conditioning_temporal.md`,
`docs/thoughts/2026-09-09_hippocampal_translation_maps_ree_archaeology.md` (its section 9 IS this thought).

---

## 0. The finding that shapes this whole pass

This thought was written on 2026-09-09 and has been overtaken, operationally, by work landed on
2026-09-09 and 2026-09-10. The hippocampal-translation-maps campaign scaffold names it in its
"Related REE work" line; the campaign's own research question **R2 -- reference-frame mediation** is
this thought's first half; the campaign's section-5 assay table already carries the rows
*"Does a relational frame matter? | reference-frame permutation"* and
*"Does phase matter? | target/early/late/shuffled temporal gate"*; and the 2026-09-10 assay
specification operationalises both **in more detail than this thought proposes** (assay A's five
frame levels, `A3_frame_cond` arm, shuffled-frame-label control and Gate A3 frame x receiver
factorial; assay B's Gate B2 timing manipulation with matched event count, phase occupancy and total
weight change). The instrument those assays need --
`ree-v3/experiments/_lib/interface_probe.py` -- is BUILT and contract-tested.

So the thought's section 13 request ("Extend the existing interface-analysis plan with
reference-frame metadata, frame-preserving versus frame-scrambled controls, temporal-phase
identifiers, synchronous versus displaced interventions") is **already discharged** except for one
gap (frame metadata in `CaptureRecord`). What is NOT discharged is the claim question the thought
asks in the same section, and the campaign deliberately deferred it (scaffold section 7, deliverable
6: "only after that, a decision on whether any claim/intake update is justified").

**This intake answers that deferred question and nothing else.** It registers two narrow claims whose
entire purpose is to give already-specified assay arms something to attach evidence to, and it
explicitly authorises no work.

---

## 1. Verbatim core proposal

> `effective interface = content x communication subspace x reference frame x receiver context x temporal gate`
>
> with recurrent stability constraining repeated use over time.

> **A cross-system mapping can be representationally adequate yet functionally ineffective if the
> interface is opened at the wrong moment.**

> The result is a new distinction between **having a compatible interface** and **engaging that
> interface at the phase in which its content can actually alter another system**.

---

## 2. Novelty table

Default assumption applied throughout: REE probably already owns it. Nine of thirteen threads are
already owned, and two of the remaining four are owned *operationally* (as assays) but not as claims.

| Thread in the thought | Existing REE coverage | Verdict |
|---|---|---|
| Interfaces decompose into factors that must be jointly correct | ARC-139 + MECH-537 + MECH-547 + MECH-548 already supply four of the six factors | **Already owned in pieces**; the decomposition itself is a framing, not a claim |
| Which sender directions are exposed to a consumer | **MECH-537** communication-subspace routing | **Already owned** -- cross-ref only |
| Which read surface the receiver's own state selects | **MECH-547** receiver-conditioned translation | **Already owned** -- cross-ref only |
| Repeated use can destabilise a statically useful interface | **MECH-548** | **Already owned** -- cross-ref only |
| Sleep adjusts / maintains interfaces | **MECH-540** (S1-S4 signatures) | **Already owned**; the thought's section 10.5 questions are MECH-540's own reporting requirements |
| Simpler bridges are stronger evidence; frame alignment should lower the rung | **MECH-538** L(A->B) ladder | **Already owned**; "frame alignment lowers L" is registered as a prediction ON the new claim, not a new meter |
| Transition geometry must survive the map; action/horizon frame | **MECH-539** dynamic interface compatibility | **Already owned**; action-conditioned frame is explicitly one of MECH-539's objects |
| A null must be read against controls before it means information loss | **INV-105** consequences (1) mismatched-pair, (2) random-projection floor | **Already owned as a pattern**; TG-F is a third instance, registered on its own claim per the GFLAG-0235 precedent |
| Relations must be recoverable across a lossy boundary, however differently encoded | **ARC-142** cognitive contract | **Adjacent and the closest rival** -- see section 2.1 |
| Shared reference frame for cross-*modal* co-registration | **ARC-087** (Ernst & Banks precision-weighted shared-reference-frame fusion, within the thalamocortical family) | **Adjacent, different object** -- perception-side fusion before world-model entry, not an inter-engine interface |
| REE's two core latents sit in different frames | **MECH-096** notes: "Dorsal-equivalent head: egocentric ... -> z_self. Ventral-equivalent head: allocentric ... -> z_world" | **Already asserted, never implemented** (zero `egocentric`/`allocentric` matches in `ree_core/`) -- this is the sharpest internal instance, and it is a gap, not coverage |
| Timing controls whether coupling between subsystems is possible | **ARC-053** TCL ("enables or prevents coupling between prediction and input"; "modulates integration windows based on task demands and mode"), **MECH-089** theta packaging, **MECH-122** spindle transmission window, **MECH-272** state-gated routing, **MECH-294** phase-aligned joint binding | **Mechanism already owned AND largely built** -- do not register the mechanism |
| Reference frame as a separable interface factor + RF-F failure class + content-preserving frame permutation | none registered (`grep -icE "reference frame\|relational coordinate\|shared basis\|canonical frame"` -> 2 hits, both ARC-087/MECH-432 and neither this) | **NEW (narrowly) -> MECH-555** |
| Temporal gate as an interface factor + TG-F false-negative rule (phase-controlled null) | none registered; `grep -icE "temporal gate\|timing window"` -> 4 hits, all critical-period (MECH-333/334/Q-052) or run-defect prose | **NEW (narrowly) -> MECH-556** |
| Section 9: replay opens transient *frame-aligned* communication windows | MECH-540 (offline interface maintenance) + the two new claims | **NOT registered** -- the thought itself says the conjunction is unsupported |
| RF-1..RF-4 and the five-condition timing assay | `hippocampal_campaign_assay_specifications_20260910.md` sections 2 and 3 (more complete) | **Instrument, already specified** -- not a claim, not chipped |

### 2.1 The hardest call: MECH-555 versus ARC-142

ARC-142 says a heterogeneous mind needs an invariant-preserving contract -- a small set of relations
`I` such that `I(x_A) ~ I(x'_B)` across a lossy translation -- and that each engine may encode an
invariant differently "(explicit scalar, trajectory position, recurrent-state relation, geometric
direction, ordering relation) so long as the relation is recoverable at the boundary when needed".
Its candidate inventory already includes *spatial relation* and *temporal relation*.

The strongest case for "already owned" is: a frame mismatch simply IS a contract relation that failed
to be recoverable, so ARC-142 covers it.

The case for registering anyway, which this pass accepts, is **operational, not verbal**:

- ARC-142's test is recoverability at the boundary. RF-F's test is a permutation that leaves
  recoverability **at both endpoints untouched** and destroys cross-system use anyway. A claim whose
  confirming signature cannot be produced by the other claim's test is doing separate work.
- ARC-142 has two failure *poles* (representation collapse, cognitive fragmentation). It has no
  failure *taxonomy* and does not route a diagnosis. RF-F is a routing class in the F1-F7 table's
  sense, and its routing verdict -- relational re-indexing rather than more sender capacity or a
  higher bridge rung -- is actionable in a way "contract failure" is not.
- The frame-permutation control is absent from INV-105's control set and from MECH-547's, and the
  2026-09-10 assay already runs it as a factor crossed with the receiver factor. A control that is
  already being run for an arm with no claim behind it is the specific reason to register.

**Recorded honestly:** if governance judges otherwise, the correct disposition is MERGE into ARC-142
naming MECH-555 as absorbed, with the RF-F routing class and the permutation control lifted into
ARC-142's notes. That option is written into the proposed claim's own `notes` so a later session
does not have to re-derive it.

---

## 3. Key formulations (verbatim)

- "Globally distinct systems can remain functionally integrated because selected activity in both systems is **indexed against the same underlying relational coordinate**."
- "A communication subspace says **which directions** of a sender matter to a receiver. A reference frame says **what relation those directions are indexed against**."
- "The reference frame need not be hand-written or symbolic. It can itself be learned."
- "A shared reference frame can provide coherence **without representational collapse**."
- "`content present + geometry adequate + wrong temporal gate -> no downstream effect`" -- "Such a result should not automatically be interpreted as evidence that the interface is semantically useless."
- "The problem is not missing information. It is **reference-frame incompatibility**."
- "Where possible preserve total communication energy/updates so that **timing, not quantity**, is the manipulated variable."
- "A directional signal is not fully specified without knowing its coordinate basis."
- "These should not be collapsed into one `z_world inadequate` diagnosis."
- "Do not add a new gate mechanism unless the existing sleep/wake/control substrate cannot express the required timing."
- On the section-9 conjunction: "This remains a hypothesis. The current biological evidence supports shared reference scaffolds and timing-sensitive consolidation **separately**; it does not directly demonstrate their conjunction."

---

## 4. Affected existing claims

Cross-referenced via `depends_on` only. **No status, confidence, evidence record, epistemic_category
or any other field of any existing claim was touched in this pass.** No governance flag was raised.

- **ARC-139 / MECH-537 / MECH-538 / MECH-539 / MECH-540 / INV-105** -- the parent package; extended
  by two factors, competed with by neither. INV-105 is explicitly **not** amended: the GFLAG-0235
  ruling of 2026-09-10 (option (b), forward reference only) already decided that an extension to the
  ladder or its consequence list stays on the claim that carries it until that claim matures, and
  TG-F's null-reading rule is exactly the shape of thing that ruling governs.
- **MECH-547 / MECH-548** -- the sibling pair. MECH-547's title already lists "temporal phase" among
  candidate receiver-state conditioners; MECH-556's notes distinguish that (phase selecting the
  exposed surface) from the temporal gate (phase determining whether the receiver can use what
  arrives). MECH-556 is a single-traversal claim; MECH-548 is a repeated-traversal claim.
- **ARC-142** -- see section 2.1. Registered as a dependency of MECH-555 with the merge option
  stated. No ARC-142 field touched.
- **ARC-087** -- cited and distinguished (multisensory co-registration, not an inter-engine
  interface). Untouched.
- **ARC-053, MECH-089, MECH-122, MECH-272, MECH-294, MECH-091, ARC-023** -- the temporal-gating
  lineage. All cited as *already owning the mechanism*, which is why no mechanism claim is proposed.
  ARC-053 in particular is distinguished at length: it asserts a loop must exist; MECH-556 asserts
  nothing about mechanism necessity and survives ARC-053's retirement.
- **MECH-096** -- named as the sharpest internal instance of an asserted-but-unimplemented frame
  distinction. Untouched; see the stale-note finding in section 7.
- **MECH-517 / MECH-532 / INV-104 / SD-080 / MECH-518** -- the inherited interface lineage, already
  cross-referenced by the parent claims. Not re-cited.

---

## 5. Candidate claims -- REGISTERED this pass

Both `status: candidate`, `epistemic_category: substrate_conditional`, `implementation_phase: v4`,
`version_relevance: v3_v4`, `registered_utc: 2026-09-15`, location
`docs/architecture/interface_reference_frames_and_temporal_gates.md` (new stub, parent
"Core Engines & Forward Models", nav_order 19 -- a new doc rather than an edit to the hub, on the
sibling pass's own precedent of staying off a file other sessions hold).

| Id | Type | One line |
|---|---|---|
| **MECH-555** | mechanism_hypothesis | Reference-frame mediation as a separable interface factor: failure class RF-F (probe succeeds on both endpoints, native use fails on incompatible relational coordinates) with a content-preserving frame permutation as the discriminator, and the consumer-specific-frames caution against inferring a global workspace. |
| **MECH-556** | mechanism_hypothesis | Temporal-gate adequacy as a separable interface factor: failure class TG-F, and the binding rule that a null measured at an interface whose engagement phase was uncontrolled licenses no information-loss reading until target/early/late/shuffled phases are compared at matched communication energy. |

Full blocks: `proposed_claims.yaml`. Stub doc: `docs_architecture_interface_reference_frames_and_temporal_gates.md`.

**Both are registered to receive evidence, not to authorise work.** `A3_frame_cond` (assay A) is at
present the only arm of an already-specified assay with no registered claim behind it, while its
neighbour `A4_receiver_state_cond` has MECH-547; Gate B2 (assay B) is in the same position.

---

## 6. Deliberately NOT registered

1. **The interface-factor decomposition itself** (`content x subspace x frame x receiver context x
   temporal gate x recurrent stability`). A framing that organises six claims, four of which already
   exist. It lives on the location doc as a table. Registering it would create a claim whose content
   is a list of other claims.
2. **The RF-1..RF-4 assay and the five-condition timing assay.** Instruments, and already specified
   more completely in `hippocampal_campaign_assay_specifications_20260910.md`. Per the parent and
   sibling passes: an instrument becomes claim-shaped only when it asserts something about REE. Not
   chipped either -- the work is already owned by the campaign.
3. **Any temporal-gating MECHANISM claim.** ARC-053 asserts the loop, MECH-089/122/272/294 assert and
   largely implement the gates. A new mechanism claim here would be a second, staler tracker of built
   substrate.
4. **The section-9 conjunction** -- "offline consolidation may open short-lived, reference-frame-aligned
   communication windows". The thought states the biology supports the two halves separately and not
   their conjunction; registering it would also overlap MECH-540. Recorded in MECH-556's notes as
   deliberately unregistered so a later session does not add it without new evidence.
5. **The candidate reference-frame inventory** (section 5 of the thought: spatial, temporal,
   action-conditioned, episodic, organismic/ethical). The thought says these are "examples to test
   for, not ontologies to hard-code", and ARC-142 already carries a research inventory of the same
   kind with the same caveat. Duplicating it would give the frame inventory an authority ARC-142's
   own inventory is explicitly denied.
6. **Section 11's proposal to "add two new diagnoses to the mutual-legibility taxonomy"** as an edit
   to the parent doc's F1-F7 table. Proposed as F8/F9 on the new location doc instead; amending the
   parent's registered taxonomy is a governance decision, exactly as the eighth-rung proposal was.
7. **Both external references as support.** Steel et al. (eLife reviewed preprint 110234) and Okyere
   et al. (bioRxiv 10.64898/2026.09.02.748628, single preprint, unreplicated) are motivation only,
   taken from the thought's reference list, not independently verified. Lit-pull owed.

---

## 7. Implementation-gap audit

Verified against `ree-v3` and `evidence/planning/substrate_queue.json` on 2026-09-15. The thought's
own assertions were treated as hypotheses; two of them are wrong in REE's favour.

| Mechanism the thought treats as needed/missing | Thought's assertion | Verified status | Evidence |
|---|---|---|---|
| A shared reference frame between engines | "Not established that REE presently contains such shared reference frames" | **CORRECT -- GENUINE GAP.** `z_world` is a shared *representation* read by ~40 modules, not a shared *frame*. Zero matches for `egocentric`, `allocentric`, `reference_frame`, `ref_frame`, `frame_id`, `procrustes`, `shared_basis` anywhere in `ree_core/`. Nothing labels, enforces or records the frame of any latent. | `/usr/bin/grep -rn --include='*.py'` over `ree-v3/ree_core/`; `z_world` 1457 hits across 40+ files |
| A frame distinction between REE's core latents | not raised | **ASSERTED, NOT BUILT.** MECH-096's notes specify z_self egocentric / z_world allocentric as an architectural requirement ("or the z_self/z_world split degrades back toward z_gamma conflation"). Nothing in V3 implements or checks it. | `claims.yaml` MECH-096 notes; grep above |
| A learned (not hand-written) shared relational binding between two streams | "The reference frame need not be hand-written or symbolic. It can itself be learned." | **PARTIAL, AND MEASURED.** `ree_core/latent/cross_stream_binder.py` installs a learned contrastive conjunction between the z_self and z_world rollout streams, theta-gated, with a shuffle control that destroys it. Its history is a measured ceiling: V3-EXQ-641a (unbound, no selection information), V3-EXQ-720 (fixed projection SYMBOL-COMPLETE but FUNCTION-PARTIAL, 3/6 vs a 4/6 gate, `n_rebind` 0), V3-EXQ-725 (cosine-InfoNCE convergence repair). | `cross_stream_binder.py` module docstring |
| Reference-frame metadata in interface telemetry | requested as an instrument addition | **GENUINE GAP, NARROW.** `interface_probe.CaptureRecord` has `phase`, `provenance`, `candidate_id`, `active_gates` -- no frame field. | `ree-v3/experiments/_lib/interface_probe.py:88-117` |
| Frame-preserving vs frame-scrambled controls | requested as an instrument addition | **ALREADY SPECIFIED.** Assay A: five frame levels (egocentric native; invertible 90/180/270 rotation with action labels rotated, its G4 positive control; allocentric region index; event/segment index; elapsed-tick), negative control 6 "shuffled frame label", Gate A3 frame x receiver factorial with compositional holdout. | `hippocampal_campaign_assay_specifications_20260910.md` sections 2.2, 2.5, 2.6 |
| Temporal gating of inter-engine reads | treated as a variable REE has not made explicit | **BUILT AT THREE GRAINS.** MECH-089 `ThetaBuffer` (E3 never reads raw E1; status `active`; SD-100 phase-weighted summary landed); MECH-272 `ree_core/sleep/routing_gate.py` (which consumer replay reaches is conditioned on WAKING/SWS/REM; `implemented`); MECH-122 content-packaging half (`use_mech122_spindle_content_selection`, wired into `run_sws_schema_pass`). | `theta_buffer.py`, `sleep/routing_gate.py`, `agent.py`; substrate_queue `MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION` = `implemented_validated_result_non_contributory` |
| A lever to shift engagement phase | "Do not add a new gate mechanism unless the existing substrate cannot express the required timing" | **CORRECT -- THE SUBSTRATE EXPRESSES IT.** `MultiRateClock` (ARC-023 rates, MECH-093 arousal-modulated E3 rate, MECH-108 BreathOscillator sweep windows), MECH-091 `phase_reset` (wired at 5 call sites; `MECH091-SALIENT-EVENT-TRIGGER-WIRING` = `implemented`), `force_sleep_cycle_at_eval_boundary`. | `ree_core/heartbeat/clock.py`; `agent.py:12759` |
| Phase as a *controlled variable* in an interface measurement | the thought's actual ask | **GENUINE GAP IN PRACTICE, SPECIFIED ON PAPER.** Nothing in `interface_probe.py` strata or manipulates by phase. Gate B2 of assay B specifies exactly the manipulation (effective window vs shifted vs shuffled, matched event count / phase occupancy / activity magnitude / total absolute weight change), with "matched event count at the wrong update phase" as a negative control. Not yet run. | `interface_probe.py`; assay spec section 3.3, 3.5 |
| A content-preserving permutation of binding structure | proposed as novel (RF-2) | **PRECEDENT ALREADY BUILT.** MECH-294 `MultiContentThetaPacket` exposes `joint` / `alternation` / `shuffled` modes so a discriminative experiment can "hold bandwidth and content identical and vary ONLY the binding structure". Claim is `substrate_ceiling` / `v3_pending`; its behavioural falsifier is OWED AGAIN after V3-EXQ-840b was re-dispositioned to `non_contributory` (2026-09-09, GFLAG-0183/0256) on a floor-clamped candidate pool. | `ree_core/latent/multi_content_theta_packet.py`; `claims.yaml` MECH-294 |
| Interface instrument (subspace, bridge ladder, causal replacement, manifold guard, dynamic compatibility) | the parent package's ML-10..ML-14 | **BUILT.** `ree-v3/experiments/_lib/interface_probe.py` (RRR communication subspace, principal angles, L0-L5 ladder incl. Procrustes, causal replacement, manifold guard, dynamic compatibility, per-code drift), `tests/contracts/test_interface_probe.py`, `--selftest`. Its own docstring records that before it, `ree-v3` had none of these. | that file |
| Substrate-queue holdings for interface/translation | ids to confirm | **CONFIRMED, all four exist in `claims.yaml`:** SD-056 (E2 world-forward action-conditional divergence, contrastive; `candidate`), SD-070 (z_world P0 anti-collapse encoder recipe; `candidate`, `epistemic_category: standard`), plus SD-080 (`pending_implementation`, frozen action-object projection) and SD-106 (`implemented_pending_validation`, generic bottleneck variance preservation -- the live encoder-side successor to SD-018). In `substrate_queue.json`, SD-070 appears via `sd_zworld_warmup_optimizer_group` (`validated`); **SD-056 has no substrate_queue entry** -- it is a claim with no queued build. No substrate_queue entry anywhere mentions reference frames or interface phase. | `claims.yaml`; `evidence/planning/substrate_queue.json` (182 entries) |

**Net:** the thought's two "REE may lack this" hypotheses split cleanly. *Reference frame* is a
genuine gap in the substrate **and** in the telemetry schema (though not in the assay design).
*Temporal gate* is the opposite -- built three times over, never varied as an independent variable,
and the thought's own instruction not to build a new gate is the correct call.

---

## 8. Next steps

1. **Lit-pull owed before either external reference is cited as SUPPORT.** Steel et al. (eLife
   reviewed preprint v2, DOI 10.7554/eLife.110234) and Okyere et al. (bioRxiv, DOI
   10.64898/2026.09.02.748628) are unverified, taken from the thought's reference list. The Okyere
   result is a single unreplicated preprint. Note that
   `hippocampal_translation_maps_literature_tranche_3_receiver_conditioning_temporal.md` (2026-09-10)
   has already closed much of the adjacent temporal literature and records debt 6 as
   "substantially closed for coding and causal necessity; **still open for temporal-frame
   mediation**" -- so a pull here should target temporal-frame *mediation* specifically rather than
   re-covering ground tranche 3 already holds.
2. **Version routing belongs to /governance.** Both default to `v4`. An argument exists for `v3` on
   MECH-556 (the manipulation is expressible with built levers over frozen endpoints and recorded
   trajectories, exactly as MECH-537 and INV-105 were routed `v3`); this pass does not decide it.
3. **Hardening deferred** -- no `what_would_answer` drafted on either new claim; that is
   `/thought-digestion` work and the drafts are in `digestion_drafts.md`.
4. **One narrow instrument gap worth a chip, if the orchestrator wants one:** add a `reference_frame`
   field to `interface_probe.CaptureRecord` alongside the existing `phase`, so assay A's frame levels
   are recorded rather than reconstructed. This is the only piece of the thought's section-13
   instrument list not already built or specified. It is a ~1-line schema addition to an
   experiment-layer module, not `ree_core` work.
5. **Currency flag for a later session, not fixed here:** MECH-096's egocentric/allocentric frame
   specification for z_self/z_world has never been implemented and nothing in the claim records that.
   See summary section 5.
