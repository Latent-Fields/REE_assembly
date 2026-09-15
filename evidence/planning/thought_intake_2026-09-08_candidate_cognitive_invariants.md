# Thought intake -- Candidate Cognitive Invariants (red-team revision)

**Date processed:** 2026-09-15
**Raw thought:** `docs/thoughts/2026-09-08_candidate_cognitive_invariants.md` (827 lines, 23 sections)
**Session:** thought-pipeline-20260915 (family A)
**Parent (already ingested -- read the intake, not re-derived):**
`evidence/planning/thought_intake_2026-09-08_deriving_the_cognitive_contract.md`
(registered ARC-142, GOV-CONTRACT-1, MECH-545, MECH-546, Q-104; all five blocks read in full).
**Canonical ledger read in full:** `evidence/planning/cognitive_contract_invariant_ledger.v1.json`
(schema 1.1, 14 records, `updated_utc` 2026-09-14).
**Architecture doc read in full:** `docs/architecture/cognitive_contract.md`.
**Prior programme artefacts read this pass:** `cognitive_contract_literature_pull_2026-09-08.md`,
`..._tranche2_...`, `..._tranche3_...`, `cognitive_contract_invariant_ledger_tranche3_amendment_2026-09-08.md`,
`cognitive_contract_narrowing_stack_preregistration_2026-09-08.md`,
`cognitive_contract_stage0_substrate_audit_2026-09-08.md`,
`evidence/literature/targeted_review_cognitive_contract_invariants/SYNTHESIS.md` (outline + reconciled cells).

**READ-ONLY PASS.** No repository file was created, edited or committed by this agent. Everything below is
a proposal for the orchestrating session.

---

## 0. The special question, answered first

> *Are candidate invariants meant to be registered as `INV-` claims at all, only once "admitted", or never
> (ledger-only)?*

**Verdict: LEDGER-ONLY for now. Register none of the fourteen -- not even the four marked `admitted`.**
Four independent primary sources agree, and one secondary source is loosely worded enough to mislead a
later session. All five are quoted here because the loose one is the live hazard.

1. **GOV-CONTRACT-1's own text** makes the quorum a bar on *standing*, not on *registration*: a candidate
   "acquires ARCHITECTURAL standing only by consilience -- independent support from at least two of six
   evidence domains". Its `functional_restatement` lists four triggers -- add a relation, implement a
   contract dimension in a bridge, read a linguistic/LLM/registry universal as an REE requirement, prune a
   candidate -- and for each REQUIRES "the >= 2-of-6-domain quorum, the four-way classification with
   alternative explanation, and the twelve-field ledger record". The required artefact is **the ledger
   record**. Nowhere does the rule mention a `claims.yaml` entry per candidate.

2. **The ledger's own `notes` field** defines the term the question turns on:
   > "'Admitted' means the candidate currently clears the GOV-CONTRACT-1 multi-domain admissibility bar,
   > **not that its encoding or primitive status is fixed**. Composite candidates remain candidate even
   > when recurrence is strong."
   So `admitted` is a statement about evidence quorum, not about architectural status. Registering an
   `admitted` record as an `INV-` claim would convert a quorum result into an architectural commitment --
   exactly the move the sentence forbids.

3. **The raw thought under ingestion says so explicitly, twice.** s.20.1: "No candidate should be promoted
   from this red-team pass. This document is doing ontology destruction, not architecture declaration."
   s.21: "No candidate is promoted by this revision." s.19 supplies the reason in structural form: the
   GOV-CONTRACT-1 quorum is **Stage 1 of a six-stage promotion hierarchy** (Stage 0 named candidate;
   1 cross-domain recurrence; 2 transferable receiver-accessible recoverability; 3 causal handoff
   dependence; 4 irreducibility under constrained reconstruction; 5 adaptation-aware characterisation;
   6 boundary scope established) -- "Only then should a candidate be considered for stronger architectural
   treatment." All fourteen records sit at Stage 1 or below.

4. **The tranche-3 amendment names the owed action on this ingestion, and it is not claim registration.**
   `cognitive_contract_invariant_ledger_tranche3_amendment_2026-09-08.md` s.13 "Next canonical-ledger
   action" opens: *"When Thought 2 is authored/ingested, rewrite the canonical JSON ledger so that ..."*
   -- seven ledger edits, zero claims. This pass **is** the ingestion of Thought 2. See s.7.1 below: that
   rewrite is still unapplied.

5. **The loose wording -- flag it, do not act on it.** `docs/architecture/cognitive_contract.md`, under
   "What is deliberately NOT registered", says: *"The candidate inventory as individual claims. Each
   becomes claim-shaped only when it has a ledger record and at least one lesion prediction."* Written
   2026-09-08 when the ledger had five seeded records, that read as a distant condition. It is now
   **satisfied by all fourteen records** -- every record carries a `lesion_prediction` string. Read
   literally today it licenses fourteen `INV-` registrations, which sources 1-4 all forbid. This is a live
   over-registration hazard for the next session that reads the doc without the ledger. **Recommended
   (not applied): tighten that sentence to cite the s.19 ladder -- "claim-shaped only at Stage 4
   (irreducibility under constrained reconstruction), not at Stage 1 (ledger record + quorum)".**

**Consequence for section 5 of this intake: zero candidate invariants are proposed as claims.** The four
claims proposed are all *second-order* -- about the shape of the contract, the admission ladder, what
counts as a valid reduction, and a falsifiable reduction hypothesis over the candidate set. None of them
adds a relation to the contract, so none of them fires GOV-CONTRACT-1 trigger (a).

---

## 1. Verbatim core proposal

> A cognitive invariant is not a universal symbol, concept, feature, or shared latent coordinate. It is a
> relation whose recoverability across some representational transformation is required for heterogeneous
> cognitive processes to continue referring coherently to the same world, history, alternatives, and
> possible actions.

> The phrase **the cognitive contract** risks suggesting a universal packet header that every subsystem
> must transmit at every handoff. That is probably too strong. ... `I_AB = relations required by B that B
> cannot cheaply and reliably reconstruct locally` ... A **deep shared core**, if one exists, should emerge
> as the relations repeatedly required across many heterogeneous interfaces -- not be assumed beforehand.

> The cognitive contract should contain no distinction merely because humans can name it, and no reduction
> should count merely because humans can rename it. A relation belongs only when a real receiving system
> repeatedly needs it, cannot reconstruct it cheaply and robustly from a smaller basis, and fails in a
> specific way when it is lost.

---

## 2. Novelty table

Hub table for family A (this thought is the family's only raw file).
`grep` counts are over `docs/claims/claims.yaml` (1126 claims) unless stated.

| # | Thread in the thought | Existing REE coverage | Verdict |
|---|---|---|---|
| 1 | A cognitive invariant is a recoverable *relation*, not a shared coordinate (s.1) | **ARC-142** states exactly this; **ARC-139** is the legibility-not-sameness half | **Already owned** -- cross-ref only |
| 2 | Contract is **boundary-specific**: `I_AB`, typed obligations `{A->B: I_AB, tolerated distortion, receiver capability, fallback behaviour}`; a shared core must EMERGE as overlap (s.2, falsifier 10) | `boundary-specific` 0 hits, `per-boundary` 0, `typed obligation` 0, `each boundary` 0, `shared core` 0, `receiver capability` 0, `fallback behaviour` 0. **MECH-547** is receiver-*state*-conditioned exposure within one boundary; **MECH-540** gives interfaces different *plasticity*, not different *obligations*; **INV-104** is one path | **NEW -> ARC-144** |
| 3 | Counting primitives is not minimality; anti-cheating **contract cost** (rate + encoder/decoder complexity + context/side-channel + distortion + compute/latency + robustness); three requirements for a valid collapse (s.3, s.11); four-way reducibility ladder logical / information-theoretic / computational / **operational** (s.5.8) | `rate-distortion` 0, `minimal sufficient` 0, `total description` 0, `decoder inflation` 0, `operational reducib` 0. **MECH-538** measures minimum *bridge* complexity between two frozen endpoints -- a different object from the *cost of a proposed reduction of the candidate set*. GOV-CONTRACT-1 trigger (d) governs *pruning* but says only that the negative result is kept; it has no test for when a MERGE is valid | **NEW -> GOV-CONTRACT-3** |
| 4 | Decodability != recoverability: latent-present != researcher-decodable != receiver-recoverable != causally used; use the receiver as decoder, receiver-matched probe class, nuisance-matched baselines (s.6) | **INV-105** seven-rung ladder: encoded / decodable / natively accessible / bridgeable / pairing-specific / causally used / behaviourally beneficial, plus the random-projection-floor consequence | **Already owned** -- the thought's four-way chain is INV-105 rungs 1, 2, 3, 6. Cross-ref only. The *resource-bound* reading (compute / latency / sample / robustness) is the one piece INV-105 lacks; folded into GOV-CONTRACT-3, not registered separately |
| 5 | Eight survival challenges for a candidate: handoff relevance, recoverability-not-coordinate-identity, consumer relevance, irreducibility, transfer, causal use, nuisance resistance, computational availability (s.5) | 5.2 = ARC-142/ARC-139; 5.6 = MECH-545; 5.7 + 5.3 = INV-105; 5.1 = ARC-142 | **Mostly owned**; 5.4 + 5.8 are the residue -> GOV-CONTRACT-3 |
| 6 | **3 + 2 compression hypothesis**: structural families A correspondence/binding, B directed event/trajectory structure, C generative context/anchoring/lineage; attached fields D epistemic weight, E regulatory/viability weight; crossed dissociation test (s.7, s.14); post-compression failure signatures (s.15) | `structural skeleton` 0, `structural famil` 0, `weighting field` 0, `epistemic weight` 0, `regulatory weight` 0, `generative lineage` 0. Nearest prior art is the **tranche-3 amendment** s.12 tier list and s.5 factorial mode basis -- which is a *tier ordering*, not a *typed structural-vs-field distinction* and carries no transfer prediction | **NEW -> MECH-557** (partly anticipated by the tranche-3 amendment; distinguished in the block's notes) |
| 7 | Six-stage promotion hierarchy Stage 0..6 (s.19); candidates stay ledger-only until Stage 4+ | `promotion hierarchy` 0, `promotion ladder` 0. **GOV-CONTRACT-1** supplies Stage 1 only; **INV-105** is the evidence ladder for one rung of Stage 2/3 | **NEW -> GOV-CONTRACT-2** (this is the answer to the special question, written down) |
| 8 | Familiar modes (perception / memory / imagination / prediction / counterfactual) are composites over lineage + trajectory position + branch + epistemic weight + control state; mode labels may be removable (s.9) | **Tranche-3 amendment s.5** already demotes the four coarse modes and gives the same factorial basis with a pre-registered cross-context test. **MECH-094 / MECH-365 / ARC-092 / MECH-271** own the content-level mode distinction | **Already owned by the amendment** (a planning artefact, unapplied to the ledger). Folded into MECH-557 family C + field D; not separately registered |
| 9 | Agency / goal / negation / salience as vulnerable composites (s.10) | **Ledger** CCI-004/010/011/014 `alternative_explanation` fields already state each decomposition almost verbatim; **tranche-3 amendment** s.6, s.7, s.10 already adjudicate them | **Already owned at ledger level** -- cross-ref by record id, no claim |
| 10 | Lesion standard: off-manifold lesion false-positive; matched random/subspace controls; within-manifold counterfactual replacement not zeroing; nuisance-matched energy/rate; receiver-side recoverability; acute-frozen then adapted; alternative-pathway recruitment; rescue; five-way interpretation (s.12) | **GOV-INTERVENE-1** `functional_restatement` names "on-manifold / near-manifold / deliberately off-manifold" as an explicit axis and requires intervention-attribution. **ARC-140** (compensatory realizability) owns acute-vs-adapted, altered causal-importance distribution, selective re-ablation and restoration, with a four-arm design. **INV-105** owns the random-projection floor. **MECH-545** owns the lesion pattern. **Prereg** s.17 + gate G5 already operationalise it | **Fully owned across four claims** -- the strongest cross-reference result of this pass. See s.4: MECH-545 cites *neither* ARC-140 *nor* GOV-INTERVENE-1 |
| 11 | Narrowing stack as a discovery experiment; conditions A-F; **width alone is not an information bottleneck** -- needs finite precision / noise / quantisation / sparsity / entropy or rate regularisation / variational-KL / explicit rate-distortion budget; condition D (rate-constrained multi-consumer, labels sealed) is the important one (s.13, s.20.6) | **Prereg** already has A/B/C/D/E, label sealing, nuisance probes, cross-seed convergence. But prereg s.5 "Width schedule" operationalises capacity as **width only** (`1.00, 0.75, 0.50, 0.25, 0.125`); no rate, precision, noise or KL term anywhere in it (`grep -iE "rate.distortion|quantis|KL|noise inject|sparsity"` -> 0 relevant hits) | **Adjacent -- a genuine correction to a frozen pre-registration, not a claim.** Routed as a timestamped prereg amendment in s.8. Nearest claim is **MECH-523** (capacity measured at untrained compression sites is uninterpretable) -- different failure, cross-ref |
| 12 | Warning against the vacuous "one typed graph" solution (s.11) | none | Folded into GOV-CONTRACT-3's three collapse requirements |
| 13 | Cognifold need not share one flat contract; unity is a property of the *transformation network*; cognifold-vs-braidling severance reading (s.18) | **Q-104** owns the severance criterion; the "unity from overlapping transformations among many latent spaces" reading is already recorded on `docs/architecture/cognitive_contract.md` under "A sharper reading of the cognifold" | **Already owned** -- cross-ref. ARC-144 sharpens the *contract* side and is listed in Q-104's natural dependants |
| 14 | Developmental/linguistic predictions; language firewall; grammar asymmetry (s.17, s.20.9) | **MECH-546**, **ARC-100**, **GOV-CONTRACT-1** linguistic-universality clause, prereg s.3 "Language remains sealed" | **Already owned** -- cross-ref only |
| 15 | Ten strong falsifiers of the programme (s.16) | ARC-142 / GOV-CONTRACT-1 / MECH-545 all have **no `what_would_answer`** (verified) | **Digestion material, not claims** -- drafted in `digestion_drafts.md` |
| 16 | Two failure poles implicit in s.2/s.11 (collapse vs fragmentation) | **ARC-142** states both poles; **INV-091** states the same as a *measurable viable band* of cross-stream similarity | **Already owned** -- but ARC-142 does not cite INV-091; flagged in s.4 |
| 17 | CCI-011 expected-absence: `absence ~= expected event + context/time window + failure to obtain` (s.10) | **MECH-303 / MECH-304 / SD-051 / MECH-376** own omission-of-harm (conditioned safety) only; no general expected-absence relation (`expected absence` 0 hits, `non-occurrence` only in the safety cluster). **Ledger CCI-011** + tranche-3 amendment s.7 already own it as a candidate | **Ledger-owned** -- cross-ref. The harm-only scope of the existing V3 claims is recorded in the gap audit (s.7) |

### The strongest extraction

It is not a new invariant. It is that **the red-team pass and the tranche-3 amendment, written 58 minutes
apart on 2026-09-08 by different sessions, independently converged on the same decomposition** -- lineage
splitting off reality-status (amendment CCI-015/CCI-016; thought family C), value reducing to viability
(amendment CCI-017; thought field E), agency as composite, modes as factorial composites, priority as
control metadata. The thought reached it destructively from first principles; the amendment reached it
from three literature tranches. That convergence is the kind of consilience GOV-CONTRACT-1 asks for --
and it is currently invisible, because **the amendment was never applied to the canonical ledger** (s.7.1).

---

## 3. Key formulations (verbatim)

- "`I_AB = relations required by B that B cannot cheaply and reliably reconstruct locally`"
- "A **deep shared core**, if one exists, should emerge as the relations repeatedly required across many
  heterogeneous interfaces -- not be assumed beforehand."
- "Declaring that everything has been reduced to 'one typed graph' or 'one latent' would therefore be
  formally compact and scientifically empty."
- "The relevant notion of minimality is therefore closer to **minimal sufficient transferable information
  under constrained encoders and receivers**, not 'fewest English nouns'."
- "A relation may be derivable in principle but unavailable to the actual receiver within its compute,
  latency, sample and robustness constraints."
- "A relation that is recoverable only by a large external probe should not be promoted as a cognitive
  contract invariant."
- "'Actual' may then be a relation to the currently sensory-anchored worldline rather than a primitive
  category."
- "confusion may arise because lineage/anchoring information is degraded, not because a dedicated REALITY
  neuron or symbol has been lost."
- "**fewer nodes is not by itself an information bottleneck**."
- "A powerful result would be that mode labels can be removed entirely while downstream systems continue
  to distinguish these cases from the lower-dimensional relational structure."
- "A compensated system may show that the *function* is important while the original *mechanism* is not
  unique."
- "Even **3 + 2 is not a target answer**."
- "Unity could therefore be a property of the transformation network rather than of any one
  representation."
- "The goal is not the shortest vocabulary. It is the **smallest causally and computationally sufficient
  transferable structure that lets heterogeneous representations remain parts of one coherent cognition**."

---

## 4. Affected existing claims

Cross-referenced via `depends_on` only. **No status, confidence, evidence record or any other field of any
existing claim is touched or proposed to be touched by this pass.** Four observations are raised for
`/governance` rather than applied:

1. **MECH-545 `depends_on` is missing two claims that already own half its causal standard.** Its list is
   `ARC-142, GOV-CONTRACT-1, INV-105, ARC-086, MECH-094, MECH-365, MECH-271, ARC-092, ARC-080, MECH-256,
   INV-035, INV-104, MECH-539` -- it cites neither **ARC-140** (compensatory realizability: acute vs
   adapted, altered causal-importance distribution, selective re-ablation, four-arm design) nor
   **GOV-INTERVENE-1** (the on-/near-/off-manifold construction axis and the intervention-attribution
   rule). The raw thought's s.12 is almost entirely those two claims. Adding the two edges is a
   `/governance` edit, not an ingestion edit.

2. **ARC-142 does not cite INV-091.** ARC-142's "two failure poles" (representation collapse vs cognitive
   fragmentation) is INV-091's "viable band" stated without the measurable quantity. INV-091 is the
   V3-phase, `standard`-epistemic-category sibling of a `substrate_conditional` v4 claim; the edge is
   worth having in the other direction too.

3. **GOV-CONTRACT-1 is still marked "warn-only until the ledger exists" in its own notes** ("THE
   TWELVE-FIELD LEDGER IS NOT BUILT: proposed home evidence/planning/...json"). The ledger has existed
   since 2026-09-08 (`db990ff2c10`) and has 14 populated records. The notes field is stale; the rule is no
   longer warn-only by its own terms. Report only.

4. **`docs/architecture/cognitive_contract.md` says the ledger was "seeded 2026-09-08 with five records"**
   and describes GOV-CONTRACT-1 as the gate on a not-yet-populated ledger. It now has fourteen. The
   "claim-shaped only when it has a ledger record and at least one lesion prediction" sentence is the
   over-registration hazard analysed in s.0 item 5.

---

## 5. Candidate claims -- REGISTERED this pass

**No candidate cognitive invariant is proposed as a claim** (s.0). Four second-order claims are proposed.
Full blocks in `proposed_claims.yaml`. All `status: candidate` / `open`, `registered_utc: '2026-09-15'`,
`source_thought: docs/thoughts/2026-09-08_candidate_cognitive_invariants.md`, anchors on the **existing**
`docs/architecture/cognitive_contract.md` (no new stub needed -- the doc is the programme's own page and
already carries all five sibling anchors).

| Id | Type | Phase | One line |
|---|---|---|---|
| **ARC-144** | architectural_commitment | v4 | The contract is a family of BOUNDARY-INDEXED obligations `I_AB`, not one flat universal header; a deep shared core is an empirical overlap to be measured, never a premise. |
| **GOV-CONTRACT-2** | governance_rule | v3 | Six-stage contract-invariant promotion ladder; GOV-CONTRACT-1's quorum is Stage 1; a ledger record confers NO `claims.yaml` entry before Stage 4. |
| **GOV-CONTRACT-3** | governance_rule | v3 | Reduction admissibility: a merge counts only if it lowers total contract cost, preserves discriminating predictions and improves transfer -- under the operational (not logical or information-theoretic) reducibility standard. |
| **MECH-557** | mechanism_hypothesis | v4 | The 3+2 hypothesis: the fourteen candidates may generate from three structural families plus two attached weighting fields, with structure and fields dissociating under a crossed transfer design. |

**Judgement calls flagged for the orchestrator:**

- **GOV-CONTRACT-2 and GOV-CONTRACT-3 could reasonably be ONE claim.** They extend the same rule and interlock
  (GOV-CONTRACT-2's Stage 4 *is* GOV-CONTRACT-3's test). They are split because their triggers differ -- promotion
  vs merge -- and the registry has precedent for finely-split governance rules (GOV-ROTATE-1 /
  GOV-SHARPEN-1 / GOV-EQUIV-1; GOV-CEIL-1 / GOV-CEIL-2 amendment). Merging them is defensible; the
  orchestrator should decide.
- **MECH-557 could be an `open_question` (Q-) instead.** The thought calls 3+2 "a destructive model to
  test against the ledger" and says it "is not a target answer", which reads Q-shaped. It is proposed as
  `mechanism_hypothesis` because s.14 makes a *directional* prediction (structural families survive
  remapping; attached fields covary with uncertainty/need at fixed structure; failure to dissociate
  refutes the model), and a `candidate` mechanism_hypothesis is exactly "a hypothesis to be attacked". If
  `/governance` prefers Q-, the crossed-design prediction must survive the conversion.
- **ARC-144 sits in mild tension with ARC-142's flat reading** ("a small set of relations `I`"). It is
  registered narrowly and distinguished rather than proposed as an amendment to ARC-142, per the standing
  no-silent-amendment discipline. `/governance` may prefer to fold it into ARC-142 instead.

---

## 6. Deliberately NOT registered

- **All fourteen ledger candidates**, including the four `admitted` (CCI-001 identity, CCI-002 temporal
  relation, CCI-006 equivalence/similarity, CCI-007 relational topology). Reason in s.0. Each already has
  a canonical home: the ledger record id.
- **The three "new" structural families and two fields as contract relations.** MECH-557 registers the
  *reduction hypothesis*, not the five relations. Registering correspondence / event-structure / lineage /
  epistemic weight / regulatory weight as relations would fire GOV-CONTRACT-1 trigger (a) and would need
  their own ledger records and quorum first. The thought forbids it explicitly (s.4: "New decomposition
  terms remain unnumbered hypotheses unless and until governance explicitly adds them to the ledger").
- **The rate-vs-width correction (s.13).** It is an amendment to a frozen pre-registration, not a claim.
  Routed in s.8.1. Registering "width is not capacity" as an REE claim would be registering a
  methodological truism.
- **The four-way reducibility ladder as a standalone claim.** Folded into GOV-CONTRACT-3's notes; INV-105
  already owns the access half and a second ladder claim would invite collapse with it.
- **The lesion/compensation standard (s.12).** Owned by GOV-INTERVENE-1 + ARC-140 + INV-105 + MECH-545.
  The only action is the two missing `depends_on` edges (s.4 item 1).
- **Mode-composite reduction (s.9) as its own claim.** Already adjudicated by the tranche-3 amendment s.5;
  folded into MECH-557.
- **The ten programme falsifiers (s.16).** `what_would_answer` material -> `digestion_drafts.md`.
- **Any edit to CCI-\* record content.** The ledger rewrite owed by the tranche-3 amendment (s.7.1) is a
  `/governance` action under GOV-CONTRACT-1 trigger (a)/(d), not an ingestion action.

---

## 7. Currency and bookkeeping findings

These are reported for a later session to act on. **Nothing was fixed.**

### 7.1 The tranche-3 ledger amendment has never been applied -- and this pass is its stated trigger

`evidence/planning/cognitive_contract_invariant_ledger_tranche3_amendment_2026-09-08.md` s.13 opens:
*"When Thought 2 is authored/ingested, rewrite the canonical JSON ledger so that:"* and lists seven edits:

| # | Owed ledger edit | State in `cognitive_contract_invariant_ledger.v1.json` (`updated_utc` 2026-09-14) |
|---|---|---|
| 1 | CCI-003 becomes a historical composite parent | NOT DONE -- still a first-class `candidate` record |
| 2 | **CCI-015 provenance/source** becomes first-class | NOT DONE -- record absent |
| 3 | **CCI-016 branch/obtaining/update status** becomes first-class | NOT DONE -- record absent |
| 4 | CCI-011 renamed non-obtaining/expected absence | NOT DONE -- still `negation_absence` |
| 5 | **CCI-017 viability/preference** added as rival to scalar value | NOT DONE -- record absent |
| 6 | causal/control gets its own record out of CCI-004 | NOT DONE |
| 7 | CCI-014 marked not-yet-required / control metadata | NOT DONE -- still `candidate`, `uncertain` |

Two ledger-writing sessions have run since (`7e906c7a84e` populate 2026-09-08 21:15, `0981e20ea14`
reconcile 2026-09-15 00:39 for `updated_utc` 2026-09-14) and neither applied it. The reconcile pass
touched only CCI-001..005 -- the five records overlapping the Session-B lit-pull -- and its `notes` do not
mention the amendment.

**This is the drift the raw thought was trying to prevent, arriving from the opposite direction.** The
thought's s.4 red-team note apologises for having collided `CCI-*` identifiers and rules that "New
decomposition terms remain unnumbered hypotheses unless and until governance explicitly adds them to the
ledger" -- while CCI-015/016/017 had *already been explicitly proposed by governance* 58 minutes earlier
and were simply never written. The thought's s.7.3 statement that provenance is "not currently represented
as a canonical CCI record" is therefore **true of the file and false of the programme's intent.**

**Recommended (not applied):** `/governance` applies the tranche-3 amendment s.13 rewrite as a versioned
ledger edit under GOV-CONTRACT-1, and records in the ledger `notes` that the red-team thought independently
converged on items 2, 3, 5 and 7. That convergence is admissible consilience evidence *about the
decomposition* under GOV-CONTRACT-1's own rules, and it is currently unrecorded.

### 7.2 The raw thought's red-team note is factually stale

The thought's header note says three planning artefacts "are not present on the repository default branch
at this revision" and must be "treated here as planned artefacts/checks, not completed evidence". All three
were on `master` **and in the thought commit's own ancestry** before the revision was written:

| Artefact the note calls missing | Actual path | Commit | Committed | Ancestor of the red-team commit `3494ef72278`? |
|---|---|---|---|---|
| "an evidence pull" | `evidence/planning/cognitive_contract_literature_pull_2026-09-08.md` (+ tranche2, tranche3) | `1f629769720` | 2026-09-08 21:02 | YES |
| "a narrowing preregistration" | `evidence/planning/cognitive_contract_narrowing_stack_preregistration_2026-09-08.md` | `fd912a58fd2` | 2026-09-08 21:24 | YES |
| "a Stage-0 V3 substrate audit" | `evidence/planning/cognitive_contract_stage0_substrate_audit_2026-09-08.md` | `aaaafab275d` | 2026-09-08 21:33 | YES |

(The red-team revision itself is `3494ef72278`, 2026-09-08 22:24; the first draft `353c86b971c`, 22:00.
`git merge-base --is-ancestor` confirms all three for both `master` and `3494ef72278`.)

Consequence: **every "planned artefact" hedge in the thought can be discharged**, and s.20.3 ("Materialise
the missing planned artefacts before citing them as evidence") is already satisfied. This matters because
the hedge is what makes the thought's s.13 read as new design work when it is in fact a *correction to an
existing frozen pre-registration* (s.8.1).

### 7.3 Two stale notes on registered claims

- **GOV-CONTRACT-1 notes**: "THE TWELVE-FIELD LEDGER IS NOT BUILT ... until it exists the rule is
  warn-only". The ledger exists and is populated. Rule is no longer warn-only by its own terms.
- **`docs/architecture/cognitive_contract.md`**: "seeded 2026-09-08 with five records" -- now fourteen.

---

## 8. Implementation-gap audit

Method: each row verified directly against `ree-v3` at `9d3a7a4` (2026-09-15) by reading code, not by
trusting the thought or the 2026-09-08 Stage-0 audit (pinned at `8e57e473`). `substrate_queue.json` and
`experiment_queue.json` checked for queued work.

| # | Mechanism the thought treats as needed / missing | Thought's assertion | Verified status | Evidence |
|---|---|---|---|---|
| 1 | Monotonically narrowing latent hierarchy | s.13 treats narrowing as the hypothesis, not as built | **CONFIRMED NOT BUILT, unchanged since the Stage-0 audit.** Widths are `concat(z_self 32, z_world 32) = 64` -> `z_beta` **64** -> `z_theta` 32 -> `z_delta` 32. The first shared stage therefore applies NO width reduction at all (64 in, 64 out) before the step down to 32; the stack is not monotonically narrowing, and the live dimensions must not be retro-read as the narrowing hypothesis' implementation | `ree-v3/ree_core/utils/config.py:67-73` (`self_dim=32, world_dim=32, beta_dim=64, theta_dim=32, delta_dim=32`); `ree_core/latent/stack.py:5-16` |
| 2 | **True capacity/rate pressure** -- finite precision, injected noise, quantisation, sparsity/activity budget, entropy or rate regularisation, variational/KL, explicit rate-distortion budget (s.13) | s.13: "fewer nodes is not by itself an information bottleneck"; conditions C and D require it | **GENUINE GAP -- in the substrate AND in the pre-registration.** Searched `ree_core/` for `kl_div`, `KL(`, `variational`, `logvar`, `quantiz/quantis`, `vector_quant`, `sparsity`, `l1_penalty`, `activity_budget`, `rate_penalty`, `entropy_reg`, `add_noise`, `noise_std`, `gaussian_noise`: **zero latent-capacity hits**. The only `quantis` hit is a fixed, unlearned region-code discretisation of `z_world` for policy decomposition (a different purpose); the only `sparsity` hits are comments in an amygdala attribution head recording that a sparsity penalty was **removed** for outweighing the objective ~100x. The prereg's s.5 width schedule contains no rate term either | `ree_core/policy/policy_decomposition.py:127,218,502,664`; `ree_core/amygdala/attribution_head.py:220,228`; `cognitive_contract_narrowing_stack_preregistration_2026-09-08.md` s.5 |
| 3 | Structural family C -- generative lineage / anchoring beyond a binary reality bit (s.7.3) | s.7.3: "Instead of a binary REALITY bit, a system may preserve relations such as: current sensory-anchored lineage / past reconstructed / future predicted branch / internally generated hypothetical / counterfactual conditioned on altered premise / externally communicated" | **PARTIAL, and the thought's diagnosis is correct about V3.** V3 has exactly the binary bit the thought attacks: `Trajectory.hypothesis_tag: bool` plus an OPTIONAL `metadata["source"]` set **only by injectors** -- the accessor's own docstring states "Untagged trajectories are ordinary proposal-distribution samples ... a None here must NEVER be treated as synthetic", i.e. there is no positive lineage record for ordinary content. No branch relation, no sensory-worldline anchoring, no predicted-vs-counterfactual distinction | `ree_core/predictors/e2_fast.py:41-70` (`hypothesis_tag`, `metadata`); `ree_core/hippocampal/module.py:833-843` (`_trajectory_source` docstring) |
| 4 | MECH-365's `committed_vs_imagined` / `source_status` provenance-bearing event token -- the parent intake flagged this as "the cheapest V3-buildable lesion cousin" for MECH-545 | not asserted by this thought; inherited from the parent intake s.7 | **GENUINE GAP, still open.** `grep -rn "committed_vs_imagined\|source_status" ree_core experiments` -> **0 hits**. The MECH-365 token structure is unbuilt. What V3 does have is `hypothesis_tag` used as a **write gate** at the consolidation boundary (imagined content is blocked from writing) rather than as content that crosses it with a status -- which is a *different* mechanism from the one MECH-545's reality-status lesion would perturb, though it is still the cheapest place to build the lesion | `ree_core/sleep/mel_consumer.py:46,178`; `ree_core/sleep/phase_manager.py:255`; `ree_core/hippocampal/module.py:29` |
| 5 | Attached field D -- **translation confidence** distinct from content confidence (s.7.4: "confidence in a translation itself") | s.7.4 lists it as a subcase that must not be collapsed; parent intake s.7.2 already recorded it as "a genuine substrate gap" | **GENUINE GAP, confirmed still open.** `grep -rln "translation_confidence\|bridge_confidence"` over `ree_core` + `experiments` -> **0 hits**. Content precision exists (E3 `dynamic_precision`, `current_precision`); nothing represents confidence *in a translation*. Note the Session-B reconciliation on ledger CCI-005 independently proposes splitting the record into `confidence_flag` / `confidence_weight`, a third axis again distinct from translation confidence | `ree_core/predictors/e3_selector.py:4420` (`dynamic_precision`), `:4691` (`get_commitment_state`); ledger CCI-005 `session_b_reconciliation` |
| 6 | Structural family B -- event/token instances, partial order, reachable transitions (s.7.2) | s.7.2: "The relevant representation may need event tokens, a partial order, interval relations, or a trajectory structure rather than a scalar clock" | **BUILT (partially), better than the thought assumes.** MECH-288 `EventSegmenter` emits monotonic hierarchical segment IDs in nested `outer.inner` form from a fast PE-threshold detector plus a slow BOCPD over `z_goal`, with **fully isolated per-stream detectors** for `"observation"` vs `"rollout"` -- exactly the token/stream separation family B needs. What is NOT built is an explicit partial order or interval relations over those tokens (`partial order` -> 0 hits in `claims.yaml` and no `interval` relation type in the segmenter) | `ree-v3/ree_core/hippocampal/event_segmenter.py:1-34` |
| 7 | Multi-consumer bottleneck requires proof that each consumer genuinely couples | s.13: "no hidden side channel carrying the discarded detail"; Stage-0 audit s.12 requires it | **BUILT.** `shared_latent_probe.py` (107 lines) measures whether multiple module losses couple to a shared latent and whether gradients conflict -- the readiness check the E-arm needs | `ree-v3/ree_core/utils/shared_latent_probe.py` |
| 8 | Full-width latent recording (vectors, not norms) with freshness metadata -- prerequisite for any receiver-access measurement | not asserted by the thought; load-bearing for s.6 and s.13 | **BUILT.** `StreamTraceRecorder`, 667 lines, stores fixed-width float32 vectors per stream with `<name>__fresh` / `<name>__valid` flags and a declared freshness derivation. Canonical harness and Q-081 profile both present | `ree-v3/experiments/_lib/stream_recorder.py`; `experiments/_harness.py` (467 lines); `experiments/_lib/q081_profile.py` (229 lines) |
| 9 | CCI-011 general expected-absence representation | s.10: `absence-like representation ~= expected event + defined context/time window + failure to obtain` | **PARTIAL, harm-scoped only.** V3's non-occurrence machinery is entirely safety-learning: MECH-303 (context-bound "this environment predicts absence of suffering"), MECH-304 (cue-specific "suffering will be omitted"), SD-051 conditioned safety store, MECH-376 `P_safety` head. Nothing represents a *general* omitted expected event outside the harm domain | `claims.yaml` MECH-303 / MECH-304 / SD-051 / MECH-376 |

**Nothing in this programme is queued anywhere.** `ree-v3/experiment_queue.json` holds 1 item and none
mentions the contract, narrowing or `CCI-*`; `evidence/experiments/` has no matching run (the two
`*contract*` / `*narrow*` directory hits are unrelated -- V3-EXQ-155 commit-boundary and V3-EXQ-810b narrow
repertoire probe); and `evidence/planning/substrate_queue.json` contains **zero** occurrences of
`cognitive_contract`, `ARC-142` or `MECH-545`, so **no SD- entry owns any row above**. Rows 2, 4 and 5 are
therefore unowned gaps, not queued work -- which is consistent with the programme's own "do not build in
V3" posture and is recorded here so a later session does not read the silence as coverage.

**Two corrections to the 2026-09-08 Stage-0 substrate audit**, offered for the record:

- The audit's s.8 says "E2 trajectories already carry a `hypothesis_tag`" and calls branch/commitment
  status "one of the cleanest places to test whether represented content can retain 'what status does
  this representation have?'". Verified: the tag is a **boolean write-gate flag**, and `metadata["source"]`
  is set only by injectors with untagged explicitly meaning "not synthetic". It is a control-plane gate,
  not a status carried in the representation across a boundary. The audit's green verdict for that probe
  is optimistic; the label exists but the *thing to be preserved* does not.
- Everything else in the audit's G0 checklist re-verified as still true at `9d3a7a4`, one week on.

---

## 9. Next steps

### 9.1 Amend the narrowing-stack pre-registration (highest-value routing from this thought)

The prereg's own s.23 freeze statement allows amendment "if timestamped and justified **before the
affected result is inspected**". **No arm has been run** (`experiment_queue.json` has no
cognitive-contract entry; `evidence/experiments/` has no matching run). The window is open, and closing it
correctly is the single most actionable output of this thought.

Amendment owed, from thought s.13 and s.20.6:
- Replace the width-only independent variable (prereg s.5) with an explicit **capacity/rate** variable:
  finite numerical precision, injected noise, quantisation, sparsity/activity budget, entropy or rate
  regularisation, variational/KL, or an explicit rate-distortion budget -- at least one, declared before
  runs, with width retained as a *separate* factor so the two do not confound.
- Re-label the arms so the thought's condition **F (capacity-matched nuisance/random-relation control)** is
  explicit; the prereg has nuisance *probes* (s.11) but no capacity-matched nuisance *arm*.
- Record in the amendment that the substrate supplies **no** rate machinery today (gap-audit row 2), so an
  auxiliary-harness implementation is mandatory, not optional.

### 9.2 Apply the tranche-3 ledger rewrite (s.7.1) under `/governance`

Seven edits, plus a `notes` entry recording the red-team convergence as consilience evidence about the
decomposition. This is the action the amendment itself names for this ingestion.

### 9.3 Tighten the architecture doc's registration sentence (s.0 item 5)

One sentence, to remove the standing licence to register fourteen `INV-` claims.

### 9.4 Literature owed before any external citation is used as SUPPORT

The thought names no papers. Its two literature-shaped assertions are **unverified** and must not be cited
until pulled: (a) that a rate/description-length or rate-distortion objective is the right formalism for
contract cost (s.3) -- the information-bottleneck and rate-distortion-theory literature, and the
minimum-description-length model-selection literature; (b) that lineage/anchoring degradation rather than a
lost reality tag explains source-monitoring failure (s.7.3) -- this contradicts nothing in the ledger but
sharpens CCI-003's `session_b_reconciliation`, which already records Dijkstra & Fleming's
graded-signal-reconstruction dissent. Existing pulls (`cognitive_contract_literature_pull_2026-09-08.md`,
tranches 2-3, `targeted_review_cognitive_contract_invariants/`) cover neither.

### 9.5 Version routing belongs to `/governance`

ARC-144 and MECH-557 default to v4 / `v4_v5` following ARC-142 and MECH-545. GOV-CONTRACT-2 and GOV-CONTRACT-3
are v3 / `v3` following GOV-CONTRACT-1, because governance rules apply now. None is V3-buildable and all
four carry the "DO NOT build in V3. DO NOT queue an experiment from this entry." caveat.

### 9.6 Hardening deferred by design

No `what_would_answer` is proposed for any claim here. Drafts for all four new claims and for the five
existing contract claims (none of which has one) are in `digestion_drafts.md` for `/thought-digestion`.
