# Thought intake -- Hippocampal relational continuity: campaign adjudication and evidence matrix

**Date processed:** 2026-09-15
**Raw thought:** `docs/thoughts/2026-09-09_hippocampal_campaign_adjudication.md` (308 lines)
**Session:** thought-pipeline-20260915
**Family:** FAMILY D hub. **The full family novelty table is section 2 of this file**; the four sibling
intakes carry a short table plus "see hub".

Siblings: `thought_intake_2026-09-09_exq1010_substrate_readiness_audit.md` (carries the family's
implementation-gap audit in full), `..._hippocampal_replay_interface_maintenance_supplement.md`,
`..._hippocampal_translation_interface_archaeology.md`,
`..._hippocampal_translation_maps_ree_archaeology.md`.

**Status of the raw file, honoured:** "literature synthesis and assay design; no claim registration,
promotion, substrate change, or queue mutation." Its own section 5 closes: "No new scientific claim is
registered. The matrix is non-scoring: it is not a substitute for governed literature intake."
**This intake registers nothing from this file.** Everything it adds is cross-reference, currency
finding, or a literature debt routed onward.

**Already-consumed check (done before drafting, per the brief).** Most of this file's operational
content has already landed in `evidence/planning/`, in six commits between 2026-09-09 and 2026-09-10:
its assay A/B designs into `hippocampal_campaign_assay_specifications_20260910.md`, its assay C into
`hippocampal_developmental_assay_c_specification_20260910.md`, its tranche-3 pointer and Butola
publication status into the tranche-3 file (`2bf877f1c81`). The intake therefore concentrates on what
those documents did NOT absorb.

---

## 1. Verbatim core proposal

> The strongest surviving account is a **distributed relational-memory system with selective
> reinstatement and state-dependent routing**. ... **None of these results requires a general
> hippocampal translator.**

> There is a serious, testable stronger hypothesis: offline activity may maintain access between
> representations as their codes change. This has a close computational precedent in Kali and Dayan
> (2004), rather than being a new theoretical invention. The missing biological discriminator is
> **replay-dependent rescue of cross-system use after controlled representational change, with memory
> strength and local information availability held constant**.

> The interface product `content x communication subspace x reference frame x receiver context x
> temporal gate` is a useful experimental decomposition, **not an established biological
> multiplicative law**. The factors can interact, correlate, or be implemented by the same circuit.

---

## 2. Novelty table (FAMILY D, full)

Method: for each substantive thread, `grep -n -iE` over `docs/claims/claims.yaml` (1126 claims) on
several plain-language synonyms, plus `docs/architecture/` and `evidence/planning/`. Counts below are
title/subject matches unless stated. **Default assumption applied: REE probably already owns most of
it, and finding the precise existing match is the success.** It owns most of the INTERFACE space and
almost none of the RIVAL space.

### 2a. Already owned -- cross-reference only

| Thread | Existing owner | What it already says |
|---|---|---|
| Specialised systems coordinate without representational convergence; federation not homogenisation | **ARC-139** | The architectural principle, registered 2026-09-08, with `ARC-121` kept alive as the explicit rival (shared epistemic-state object). Neither is prejudged |
| A variable can be encoded in the full sender yet absent from the consumer-facing subspace; RRR from sender to the ACTUAL consumer input tensor | **MECH-537** | The mechanism *and* its operationalisation, verbatim. Now implemented -- `interface_probe.communication_subspace` |
| Minimum bridge complexity as the legibility measure; the native -> Procrustes -> affine -> low-rank -> nonlinear -> high-capacity ladder; a high-capacity bridge that succeeds is evidence about the BRIDGE | **MECH-538** | `L(A -> B)` between FROZEN endpoints, plus the two-axis anti-degeneracy guard (local competence AND legibility) that stops "falling L" being read as progress when one system simply lost its specialisation |
| A bridge can succeed pointwise and destroy transition geometry; map-initial-only versus re-map-each-step | **MECH-539** | Dynamic interface compatibility, `receiver_transition(T(x_t), a_t)` vs `T(x_{t+1})` |
| Sleep adjusts or stabilises the interface as a third offline job; the strongest test compares TWO interfaces with different predicted plasticity | **MECH-540** | Exactly this, including the two-interface requirement the supplement independently re-derives, and the S1-S4 post-sleep signature set with S4 (maladaptive homogenisation) registered as an ADVERSE signature that must be measured |
| The same sender should expose different content to different receivers; `T(sender, receiver, context)` | **MECH-547** | Receiver-conditioned translation, with the exposure-not-solving constraint and the receiver-permutation discriminator |
| Repeated interface use is a separate property from one-step utility; off-manifold compounding vs semantic double-counting; cumulative vs clean-base | **MECH-548** | Recurrent interface stability. The adjudication's "Add recurrent stability as a separate requirement" IS MECH-548, arrived at independently |
| `encoded != decodable != natively accessible != bridgeable != pairing-specific != causally used != behaviourally useful`; correct/mismatched/zero/moment-matched-random controls | **INV-105** | The seven-rung ladder verbatim, with the two controls stated as REQUIREMENTS, plus the random-projection-floor clause |
| Sender-side preservation: what must survive the observation boundary | **INV-104** | The complement of INV-105; INV-105's own notes state the pairing |
| Developmental over-connected -> pruned -> sparse structured trajectory; pruning need not mean deletion | **MECH-362 / Q-057** | Registered June 2026 off the same Vargas-Barroso anchor the dossier rediscovers as E24. The dossier says so itself and is right: "**direct genealogy**, not new evidence intake" |
| Replay reorganises the representational scheme (split/merge/reweight of equivalence classes) and re-indexes episodic traces | **MECH-529** | The two offline jobs MECH-540 adds a third to |
| Offline integration is a family of TYPED transformations with distinct write targets, provenance classes and distal readouts | **ARC-137** | Registered 2026-09-03 from the sleep-as-deferred-reorganisation thought. Partitions by OUTCOME: retention, reorganisation, recalibration, behavioural-access repair |
| Retrospective linking / provenance: descendants must not be counted as independent witnesses | 31 claims carry provenance/ancestry/independent-witness in title or subject; the owning artifact is `evidence/planning/provenance_false_evidence_multiplication_experiment_ladder.md` P1/P3 | The dossier's own section 8 routes its extension there and says it "should not become a duplicate experiment family". **Agreed; not registered** |
| E2 supplies action-consequence objects, not sensory-state transitions, across the hippocampal handoff | **MECH-033** (`active`), **ARC-018**, **ARC-007** | The February/March lineage both archaeologies trace |

### 2b. Adjacent but distinct -- named, not registered

| Thread | Nearest owner | Why it is not registered here |
|---|---|---|
| Hippocampal INDEXING THEORY (Teyler and Rudy): an index triggers distributed cortical completion, and cortical pattern completion after a hippocampal trigger does not require detailed hippocampal reconstruction | **No owner.** `grep -iE "index(ing)? (theory|lookup|reinstat)"` over 1126 claims returns exactly ONE incidental hit (Q-020). `reinstat` has 3 title/subject hits, none about indexing theory. `MECH-513` (representation-version reindexing for episodic memory) is the closest and is about keeping an index valid across representation versions, not about index-triggered completion | **A genuine registry gap, and it is NOT this file's to fill.** The dossier treats indexing as the strongest SIMPLER RIVAL to be beaten (its section 4, row 1; its assay A arm "episode-index lookup plus native reinstatement"). A rival that must be implemented as a working comparator is an assay arm, and the assay spec owns it. Flagged to `/governance` as a coverage gap |
| REFERENCE FRAMES: egocentric / allocentric / route-relative / object-vector; frame selection vs coordinate transformation vs inverse reconstruction as three different operations | **No owner.** `grep -iE "reference frame|allocentric|egocentric"` returns **ZERO** title/subject matches across the registry and 4 incidental prose hits (MECH-096, MECH-098, MECH-384, GOV-DIAG-1) | **Genuine gap, and the primary owner is a DIFFERENT raw thought** -- `docs/thoughts/2026-09-09_shared_reference_frames_and_temporal_gates.md`, which has no Stage-2 intake either. Registering it from the adjudication would pre-empt that file's own pass. **Reported in concerns, deliberately not registered.** See section 8 |
| TEMPORAL GATES: a correct mapping fails if engaged outside the phase in which the receiver is receptive, plastic, or evaluating the relevant candidate | **No owner** as an interface factor. The sleep/offline cluster is large (115 title/subject) but is about phase-indexed PROCESSES, not about an interface being gated by receiver phase | Same disposition as reference frames -- same owning thought, same reason |
| REPRESENTATIONAL DRIFT as a named phenomenon (unit-level change with preserved population geometry) | **No owner.** `drift` has 9 title/subject hits and **every one is parameter, environmental or confidence drift** (MECH-142, SD-047, SD-048, SD-054, MECH-375, SD-076, MECH-444, MECH-494, GOV-SUBIMG-1) | Owned in the supplement's intake instead, where it is load-bearing (MECH-562, Q-107). Not duplicated here |
| Hippocampal anchor SELECTION for proposals (which start state a rollout begins from) | **MECH-269** (`candidate`, `v3_pending`, `what_would_answer` PRESENT) | Genuinely adjacent and genuinely different: MECH-269 is about the proposer choosing an anchor inside ONE system's own map; R1 is about two systems referring to the same event without shared coordinates. No merge |
| Hippocampal anchor TOPOLOGY carries functional information; relation types are not collapsible to one adjacency | **MECH-468 / MECH-469 / MECH-470**, plus **MECH-495** (relational appropriateness, not maximal pattern separation) | These are REE's existing R1-adjacent cluster and the dossier does not cite them. Not a duplicate -- they are about the structure of the hippocampal map itself, not about cross-system reference -- but a session registering an R1 claim later must distinguish from all four. **Recorded so the distinction is available** |
| CA3 sparse -> CA1 dense coding transformation (E05) as reformatting | `MECH-149` (CA1 mismatch between E1-predicted and CA3-retrieved `z_world` gates trajectory injection); `ARC-039` (hippocampal-entorhinal loop) | The dossier's own caution is the right disposition: "**Code transformation, frame selection, and inverse reconstruction are different operations.** A sparse-to-dense population transformation does not show that CA1 reconstructs the original cortical pattern" |
| "When does invariant-preserving translation between cognitive systems constitute one mind or two?" | **Q-104** (cognifold versus braidling) | Registered; the dossier does not reach this question but a reader of both should know it exists |

### 2c. Genuinely new -- and where it went

| Thread | Verdict |
|---|---|
| The six-gate completed-chain standard; Gate 0 interface-lesion proof; the `D > max(E,F,G)` estimand; prospective local-memory equating by equivalence test | **NEW.** Registered from the SUPPLEMENT (which states it in full) as **INV-110**, not from this file, which states only the one-line version ("with memory strength and local information availability held constant") |
| Receiver-local self-healing as the standing rival | **NEW.** Registered from the supplement as **MECH-562**. This file names Rule and O'Leary (E30) as "Essential matched comparator in B" but does not develop it |
| Code-change vs world-change indistinguishability | **NEW.** Registered from the supplement as **Q-107**. Absent from this file |
| A reproduced recipe is not a frozen endpoint | **NEW.** Registered from the exq1010 audit as **INV-109** |
| The non-multiplicativity caveat: the five-factor interface product is a decomposition, not a law; factors can interact, correlate, or be implemented by one circuit | **NEW to this file, and NOT registered.** It is a caveat on a decomposition that is itself unregistered (two of its five factors have no owner, per 2b). Registering a caveat before its subject inverts the order. **Carry it forward** to whichever pass registers the decomposition |
| The four-way classification survive / narrow R1 / split R2 into four / split R3 into three / split R4 into five / split R5 into three | **Not a claim.** A research-programme decomposition. Its most useful residue is the R4 five-way split -- memory strengthening, local retuning, index maintenance, stable output scaffolds, active interface repair -- which is the shape INV-110 exists to adjudicate between. Recorded in INV-110's notes |
| Genealogy classification (earlier precursor / direct genealogy / independent convergence / experimental convergence) applied to 9 connections | **Not a claim**; it is the archaeologies' method. See their intakes |

---

## 3. Key formulations (verbatim)

- "None of these results requires a general hippocampal translator."
- "**replay-dependent rescue of cross-system use after controlled representational change, with memory strength and local information availability held constant**."
- "a receiver-conditioned bridge can recover performance by introducing missing information from the receiver. Such a result does **not** prove the sender retained that information."
- "**Code transformation, frame selection, and inverse reconstruction are different operations.**"
- "projection identity is not receiver-state conditioning; a fixed projection can select different signals without constructing `T(A,B)`."
- "Anatomical direction, temporal precedence, decoding direction and causal influence should each receive a separate label."
- "Neither lag nor the word 'communication' upgrades a representational result to perturbational evidence."
- "Do not conflate (i) fewer recurrent synapses, (ii) fewer active neurons per memory, and (iii) a lower-dimensional interareal communication surface."
- "'Not demonstrated' is not a negative experimental result."
- "Treating repeated descendants as independent observations is epistemically invalid."
- "recurrence inside one research programme is not independent empirical evidence." (archaeology, quoted approvingly here)
- "The strongest rival ... must be a **working executable comparator**, not a weak 'no bridge' straw man."
- "Its strongest falsifier is successful matched local co-adaptation with no additional benefit of correct interareal replay."

---

## 4. Affected existing claims

Cross-reference only. **No status, confidence, evidence record or field of any existing claim is
touched.** Three CURRENCY findings are reported for `/governance`; none is fixed here.

| Claim | Relation | Finding |
|---|---|---|
| ARC-139, MECH-537, MECH-538, MECH-539, MECH-540, MECH-547, MECH-548, INV-105 | the space the dossier inventories | The dossier's conclusion is verified correct: "ARC-139, MECH-537-540 and INV-105 already cover mutual legibility, communication subspaces, bridge complexity, dynamics and maintenance. MECH-547/548 already cover receiver conditioning and recurrent stability. **No duplicate claims are warranted.**" |
| **All eight of the above** | -- | **CURRENCY FINDING 1: every one has NO `what_would_answer` field**, while every one also carries "DO NOT queue an experiment from this entry". The family has no registered falsification handle anywhere. See `digestion_drafts.md`, which drafts one for each |
| **MECH-537, MECH-538** | -- | **CURRENCY FINDING 2: their notes have been overtaken by V3-EXQ-1010.** MECH-537's notes say it "supplies the mechanism that would explain the 1002 result *without requiring information loss*"; H-F (content discarded at encode) was CONFIRMED 2026-09-11, three days after MECH-537 was registered, with the trained latent at or BELOW its own random-init control on 3/3 seeds. Neither claim is refuted -- routing failure remains a real third category and `L(A->B)` remains well defined -- but the motivating example no longer supports the sentence. Re-word; do not demote |
| **MECH-362 / Q-057** | the developmental lineage | Unchanged and correctly routed. The assay C spec adds a **material adverse finding neither claim records**: the matched-final-topology question has a substantial published ML literature (Liu et al. 2019; Frankle and Carbin 2019; Frankle et al. 2020; Renda et al. 2020; Blalock et al. 2020; Hooker et al. 2019) whose weight is **against** MECH-362's strong form, and none of it is in REE's tree. **Already owned by `LIT-1003`** (`proposed`, `targeted_review_mech_362`) -- do not raise a second pull |
| **ARC-121** | ARC-139's registered rival | Has an experiment proposal (`EXP-0267`, `blocked_substrate`); ARC-139 does not. Noted, not acted on |
| **SD-080** | the one pending substrate item on this critical path | **CURRENCY FINDING 3:** `unblocks_claims` lists MECH-516/517/518/523/532 but **not MECH-537**, which `depends_on` SD-080. One-line fix at `/governance` |
| INV-088, MECH-457 | `bears_on` targets of the 978-1010 autopsy chain | Unchanged |

---

## 5. Candidate claims -- REGISTERED this pass

**None from this file.** The dossier's own boundary is correct and is upheld: every mechanism thread
it develops is already owned by ARC-139 / MECH-537-540 / MECH-547-548 / INV-105 / MECH-362 / Q-057,
and its genuinely-new content is literature adjudication rather than claim content.

The family's four new claims are registered from its two other files and are listed in
`proposed_claims.yaml`: **INV-109** (exq1010 audit), **INV-110**, **MECH-562**, **Q-107**
(all supplement).

---

## 6. Deliberately NOT registered

- **The 43-source evidence matrix.** Explicitly non-scoring by its own declaration, and not governed
  literature intake. Routing it to `/lit-pull` is section 8 item 2 -- registering it is not an option.
- **R1-R5 as five claims.** Three are already owned (R1 partially by the anchor-topology cluster, R3
  by MECH-547, R4 by MECH-540), one has no owner but belongs to a different thought (R2), and one is
  MECH-362/Q-057 (R5). Registering the set would duplicate four owners to acquire one.
- **The "indexed associative reinstatement plus distributed frame processing and adaptive routing"
  rival model.** It is an ASSAY ARM ("a **working executable comparator**"), and the assay spec owns
  the arm list. A comparator registered as a claim is a comparator nobody builds.
- **Assays A, B and C.** Designs, and all three are already specified in `evidence/planning/`
  (`hippocampal_campaign_assay_specifications_20260910.md` for A and B;
  `hippocampal_developmental_assay_c_specification_20260910.md` for C).
- **The provenance extension.** Routed by the dossier itself to the existing provenance ladder P1/P3.
- **Any biological finding as REE evidence.** The dossier's own three-layer separation (established
  result / computational inference / REE hypothesis) is the correct discipline and forbids it.

---

## 7. Implementation-gap audit (this file's share)

The full family audit, re-measured 2026-09-15, is section 7 of
`thought_intake_2026-09-09_exq1010_substrate_readiness_audit.md`. Two rows belong specifically to the
assay designs in THIS file's section 7, and both are new findings that the readiness audit could not
have made:

| Mechanism this file's assays presuppose | Verified status 2026-09-15 |
|---|---|
| **Assay A's decisive arm: a receiver-state-conditioned bridge, compared at matched capacity against a frame-conditioned and a fixed-route bridge** | **GENUINE GAP.** `interface_probe.bridge_ladder` (`ree-v3/experiments/_lib/interface_probe.py:629`) fits L0 identity, L1 Procrustes, L2 affine, L3 low-rank affine, L4 constrained nonlinear, L5 high-capacity -- **all unconditionally, `X -> Y`**. There is no receiver-conditioned rung. The work programme flagged this: `mutual_legibility_work_program_20260907.md` ML-13 addendum ("Added 2026-09-08", the `T(A,B)` rung) is the one ML-13 item the P0 build did not deliver. **MECH-547 therefore has no instrument at all**, and assay A can run every arm except the one that discriminates |
| **Assay A's frame manipulation: "Manipulate reference frame and receiver query independently using the same episodes"** | **GENUINE GAP, and the claim layer is empty too.** No frame-conditioning instrument exists, and per section 2b no REE claim owns reference frames. The one adjacent substrate piece is `ree_core/hippocampal/event_segmenter.py` (`EventSegmenter`, `BoundaryEvent`), which the assay spec cites for "frame level iv only" |
| **Assay B's pairing arms D/E: correctly paired vs marginal-matched-permuted intersystem replay** | **GENUINE GAP.** `ree_core/sleep/replay_sampler.py`'s `SleepReplaySampler` is by its own docstring a NO-OP CONSUMER; `ree_core/sleep/cross_module_consolidation.py`'s `CrossModuleConsolidator` schedules module LOSSES and carries no `(sender_episode, receiver_episode)` pairing. The assay spec is explicit that the fix is **experiment-layer** and that `ree_core` must NOT grow a pairing mechanism |
| **Assay B's drift manipulation: known invertible drift of task-relevant coordinates vs drift confined to unused coordinates** | **PARTIAL.** `interface_probe.per_code_drift` (:1012) MEASURES drift separately in transfer-relevant and orthogonal directions. Nothing IMPOSES it. The pieces exist in `v3_exq_1008`'s LEG 2 invertible 32x32 re-basis |
| **Assay B's two-interface comparator (MECH-540's own requirement)** | **GENUINE GAP.** No two live REE interfaces have adequate native consumers and full controls |
| **Assay C's whole substrate** | **Blocked further out than this file implies.** `hippocampal_developmental_assay_c_specification_20260910.md` section 11: gate **G-LIFE is DECIDED AGAINST** the branch assay C needs -- the observational-life driver family runs entirely under `torch.no_grad()`, so cumulative learning updates are zero by construction and arms B and D0 are literally the same object. The gradient-learning branch is "a genuinely new, unscoped architecture project", and the 2026-08-12 decision memo sequences scoping it behind the MECH-357 fair test. The dossier's "later developmental substrate" routing reads as scheduling; the actual position is `complex (probe-gated)` on a MECH-357 verdict |
| **Assay A/B source adequacy** | **DISCHARGED.** `rawfield25` (0.9735 worst seed) and `ws250_pca32` (0.868 mean, 3/3) are both implemented and measured-adequate; the dossier's own section 7A V3 gate has fired and selected them |
| **The instrument generally** | **BUILT 2026-09-10** (`ree-v3` `a83f2fb`). See the sibling intake's section 7.1 |

---

## 8. Next steps

1. **`/governance`, three currency fixes named in section 4:** the missing `what_would_answer` on all
   eight interface claims (drafts supplied in `digestion_drafts.md`); MECH-537/538's overtaken notes;
   SD-080's `unblocks_claims` omission of MECH-537.
2. **`/lit-pull`, and this is the file's main outward debt.** The dossier is explicit that its
   43-source matrix is NOT governed intake. Ordered by its own debt list: (i) cross-system repair
   causality; (ii) receiver state versus cue identity; (iii) CA1->EC reconstruction versus
   trigger/comparison -- **version question CLOSED** (Butola et al., Nat Neurosci 2025;28(4):811-822,
   DOI 10.1038/s41593-025-01883-9, PMID 39966537; verified against PubMed and already landed in the
   tranche-3 file) but the **detailed-controls review is NOT**, so the debt stands at that rung;
   (iv) developmental historical necessity; (v) independent replication of E02/E05/E06/E28;
   (vi) a temporal-relations/time-cell tranche; (vii) provenance. **Do not raise a pull for the
   pruning/lottery-ticket family -- `LIT-1003` already owns it.**
3. **Registry coverage gaps, reported not filled:** hippocampal indexing theory, reference frames, and
   temporal gates have no REE claim. The last two belong to
   `docs/thoughts/2026-09-09_shared_reference_frames_and_temporal_gates.md`, which has no Stage-2
   intake; if that file is in another family's batch this pass, **leave it to them** -- a
   double-registration here is the exact collision the pipeline exists to avoid.
4. **Carry forward the non-multiplicativity caveat** to whichever pass registers the five-factor
   interface decomposition.
5. **Version routing:** nothing here is V3. The two assays are v3-runnable as DIAGNOSTICS once their
   three gaps close (section 7); assay C is v4/v5 and further out than the dossier says.
6. **Do NOT re-run the campaign.** Its stopping rule was discriminative coverage and it was met. The
   next step is assay selection under live substrate constraints, which is a different activity.
