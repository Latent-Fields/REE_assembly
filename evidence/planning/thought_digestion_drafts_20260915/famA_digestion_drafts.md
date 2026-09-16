# Digestion drafts -- family A (candidate cognitive invariants)

**NOT part of the intake.** Drafts for `/thought-digestion` / `/governance` to consider; nothing here is
proposed for direct application, and no existing claim field is touched.

**Source thought:** `docs/thoughts/2026-09-08_candidate_cognitive_invariants.md`
**Date drafted:** 2026-09-15 | **Session:** thought-pipeline-20260915

**Extraction-before-invention note.** Almost every falsifier below is the thought's own language (its
section 16 lists ten programme falsifiers, section 14 the crossed design, section 15 the failure
signatures) or is already present in
`evidence/planning/cognitive_contract_narrowing_stack_preregistration_2026-09-08.md` (arms A-E, gates
G0-G5, the pre-results prediction table) or in the ledger's per-record `lesion_prediction` and
`alternative_explanation` fields. Where a falsifier is invented rather than extracted it is marked
**[drafted]**.

**Currency check performed.** For every cited blocker or run: `ree-v3/experiment_queue.json` holds 1 item
and none is a cognitive-contract entry; `REE_assembly/evidence/experiments/` contains no matching run; and
`evidence/planning/substrate_queue.json` contains zero occurrences of `cognitive_contract`, `ARC-142` or
`MECH-545`. Nothing in this programme has been run, queued or given a substrate owner. No cited blocker
has resolved since 2026-09-08 except the three "missing planned artefacts" (see intake s.7.2), all of
which had in fact landed before the thought was written.

---

## Part 1 -- proposed new claims

### NEW-ARC-1 -- boundary-indexed contract obligations

- **NON-DEGENERACY PRECONDITION.** At least two heterogeneous interfaces have been instrumented with the
  SAME candidate relation and the SAME receiver-accessible recoverability measure, and the relation is
  measurably present at at least one of them. If one boundary is instrumented, or the relation is absent
  everywhere, the claim is untestable rather than false: a single-boundary programme cannot distinguish
  "boundary-indexed" from "universal".
- **CONFIRMING.** A relation is shown obligatory at one boundary (nuisance-controlled lesion produces the
  predicted deficit, MECH-545) and NOT obligatory at another -- the receiver at the second boundary
  reconstructs it locally within its own compute/latency budget with no behavioural cost -- with the
  dissociation replicating across seeds. Plus, over several boundaries, a measured OVERLAP set that is
  non-empty and smaller than the union: obligations differ, and a core exists.
- **FALSIFYING.** Two outcomes, in opposite directions, both count. (i) **Universality**: every
  instrumented boundary requires the same obligation set, with no relation ever locally reconstructable --
  the flat ARC-142 reading was right and the indexing is bookkeeping. (ii) **Falsifier 10** (the thought's
  own): useful obligations exist per boundary but their OVERLAP across the cognitive graph is negligible
  -- there is no shared core, and the contract is a set of interface specifications rather than an
  architecture of cognition. NEW-ARC-1 survives only the middle.
- **DISPOSITION: (c) substrate-blocked -- `substrate_conditional`.** Never exercised: multi-boundary
  instrumentation does not exist, and MECH-545's lesion pattern is itself unbuilt. Not a ceiling -- the
  code is absent, not absorbing signal.
- **Justification.** The claim is about a comparison across boundaries, and REE currently has no
  instrument that measures the same thing at two of them.

### NEW-GOV-1 -- promotion ladder

- **NON-DEGENERACY PRECONDITION.** At least one candidate has reached a stage above 1, so the ladder has
  discriminated something. Until then the rule is a refusal rule only, and "no candidate has been
  registered" is consistent with both the rule working and the programme being stalled.
- **CONFIRMING.** [drafted] The ladder gives a DIFFERENT answer from the prior wording on a real case,
  and the different answer turns out to be the right one in hindsight -- e.g. a candidate registered under
  the old "ledger record + lesion prediction" test is later shown reducible or boundary-local, and would
  have been held at Stage 1-3 by this ladder. Evidence of use, not of formalisation (same promotion
  discipline as GOV-PATHVALID-1 / GOV-INTERVENE-1).
- **FALSIFYING.** The ladder is applied and every candidate either passes all six stages trivially (the
  stages do not discriminate) or none ever passes Stage 2 over a long programme while the candidates are
  nevertheless independently shown load-bearing by other routes (the ladder is measuring instrument
  availability rather than candidate quality). Either outcome says the stages are the wrong cuts.
- **DISPOSITION: (b) derivational**, with a use-gated promotion condition. It is a governance rule with no
  substrate dependency; its status should not move to `provisional` until it has been *applied* in a live
  `/governance` pass, per the GOV-INTERVENE-1 / GOV-PATHVALID-1 precedent ("promote only after live use,
  not merely after formalisation").
- **Justification.** Nothing in V3 bears on whether the ladder is the right ladder; only governance
  practice does.

### NEW-GOV-2 -- reduction admissibility

- **NON-DEGENERACY PRECONDITION.** A concrete merge proposal exists with an explicit before/after basis,
  and the cost terms are at least coarsely estimable for both. NEW-MECH-1 is that proposal; without it the
  rule has nothing to score.
- **CONFIRMING.** [drafted] A proposed merge that looks compelling on relabelling grounds is REFUSED by
  the relocation checklist -- the lost distinction is found in the decoder, a context tag or a side
  channel -- and the refusal is later vindicated (the merged basis fails a discriminating-prediction test
  the unmerged basis passes). One such case establishes the rule catches something the naive criterion
  does not.
- **FALSIFYING.** Every merge proposal fails the cost test for reasons that turn out to be measurement
  artefacts (cost terms not estimable at the available precision), so the rule blocks all reduction and
  the basis grows monotonically -- the thought's own falsifier 8 ("The basis continually expands ... total
  description cost fails to fall"). Alternatively, the symmetry clause is never exercised -- no retention
  is ever argued for, only reductions policed -- in which case the rule is one-sided in practice whatever
  its text says.
- **DISPOSITION: (b) derivational.**
- **Justification.** Same as NEW-GOV-1; the rule's correctness is a question about governance practice
  and cost-accounting, not about V3.

### NEW-MECH-1 -- the 3 + 2 reduction hypothesis

- **NON-DEGENERACY PRECONDITION.** The crossed design of the thought's section 14 can actually be
  instantiated: structure and weighting must be independently manipulable. Concretely, there must exist a
  manipulation that changes confidence at FIXED structural content, and one that changes structural
  content at FIXED confidence -- and a positive control showing each manipulation moves its own target.
  If the two cannot be varied independently at all, the experiment cannot test the model and returns
  "assay invalid", not "model wrong" (prereg gate G1's role).
- **CONFIRMING.** All five crossed contrasts dissociate along the structure/field boundary: structural
  families (correspondence, event/trajectory, lineage) survive object/world remapping when the world
  relation is preserved despite altered surface features, while epistemic and regulatory weights vary
  strongly with uncertainty, need, goal, physiology and task regime at fixed structure. Plus: the absorbed
  candidates' failure signatures collapse onto the five reduced signatures of section 15 rather than
  remaining fourteen-way distinct, AND the merge passes NEW-GOV-2's three collapse requirements (lower
  total cost, discriminating predictions preserved, transfer improved).
- **FALSIFYING.** Four distinct routes, all extracted: (i) structural and weighting variables **cannot be
  dissociated** by the crossed design -- the thought's own stated refutation ("the 3 + 2 model is wrong or
  too simple"); (ii) a held-out residue survives -- intervention/control residue (passive prediction
  preserved with selective loss of action-effect learning and controllability attribution) or
  expected-absence residue (inability to represent omitted expected events despite intact raw surprise) --
  showing the families do not absorb CCI-004 or CCI-011; (iii) the reduction succeeds only by decoder
  inflation (falsifier 9), caught by NEW-GOV-2; (iv) the fourteen candidates' failure signatures remain
  mutually distinguishable under nuisance-controlled perturbation, i.e. the merges destroy discriminating
  predictions.
- **DISPOSITION: (c) substrate-blocked -- `substrate_conditional`**, and specifically
  **substrate_conditional, NOT substrate_ceiling**: the mechanisms are absent, not built-and-absorbed.
  Family C's V3 analogue is a binary `Trajectory.hypothesis_tag` with injector-only source metadata
  (`ree-v3/ree_core/predictors/e2_fast.py:41-70`, `ree_core/hippocampal/module.py:833-843`) rather than a
  lineage structure; field D's translation-confidence subcase has zero substrate representation
  (`grep -rln "translation_confidence\|bridge_confidence" ree_core experiments` -> 0).
- **Justification.** Testing it needs a rate-constrained multi-consumer bottleneck that does not exist
  (no KL/variational, quantisation, noise-injection, sparsity or rate-regularisation machinery anywhere in
  `ree_core`) plus generative-lineage structure that does not exist.
- **Additional routing note.** The prereg's pre-results prediction table already contains two rows that
  bear on this claim ("factorial status axes transfer better than coarse mode labels" -> supports the
  representation-of-representation-system account; "viability basis transfers better than signed value" ->
  supports value-as-derived H2). Those are NEW-MECH-1's family-C and field-E predictions written a week
  early; whoever digests this claim should reuse that wording rather than redraft it.

---

## Part 2 -- existing claims this thought materially bears on

All five contract claims and two of their neighbours were checked: **none has a `what_would_answer`
field** (verified by loading `claims.yaml`; `GOV-INTERVENE-1` is the only claim in this neighbourhood that
does). Drafts follow for the five the thought bears on most directly.

### ARC-142 (candidate, `substrate_conditional`, v4) -- the cognitive contract

- **NON-DEGENERACY PRECONDITION.** At least one inter-engine boundary is instrumented well enough that a
  relation can be shown recoverable at it by the RECEIVER (INV-105 rung 3), not merely by an external
  probe. Without that, both "contract preserved" and "contract failed" are unobservable and every result
  is about the probe.
- **CONFIRMING.** Engines maintain measurably DIFFERENT representational geometries (global similarity
  flat or falling) while a small, stable set of relations remains receiver-recoverable across their
  boundaries, and behavioural coherence tracks the relations rather than the geometry -- the thought's
  falsifiable claims 4-5, and the non-redundant developmental prediction MECH-538 already registers
  (specialisation and legibility rising together).
- **FALSIFYING.** The thought's section 16 supplies ten; four falsify ARC-142 rather than the method.
  (1) **No reusable compact structure exists** -- different consumers repeatedly require unrelated
  task-specific exchange variables, with no set recurring across boundaries. (2) **Ordinary latent
  geometry is operationally enough** -- actual receiving modules cheaply reconstruct every required
  distinction locally, so nothing must be preserved. (3) **Probe-only invariants dominate** -- candidate
  information is externally decodable but unavailable to or unused by receivers (INV-105 rungs 2 but not
  3/6). (10) **Boundary-specificity defeats a shared core** -- see NEW-ARC-1.
- **DISPOSITION: (c) substrate-blocked, `substrate_conditional`.** Unchanged from registration.
- **Justification.** No boundary in V3 is instrumented for receiver-side recoverability; the mutual-
  legibility instruments (ML-10..ML-15) that would supply it are themselves owed.

### GOV-CONTRACT-1 (candidate, `governance_rule`, v3) -- admissibility

- **NON-DEGENERACY PRECONDITION.** The ledger has entries whose classification the rule actually
  determines. Satisfied since 2026-09-08 -- which is itself the point: the rule's own notes still say
  "THE TWELVE-FIELD LEDGER IS NOT BUILT ... until it exists the rule is warn-only". **That note is stale
  and should be corrected before any `what_would_answer` is attached**, or the precondition will be read
  as unmet.
- **CONFIRMING.** [drafted] The four-way classification and the >= 2-of-6 quorum give a different answer
  from an unclassified reading on a real candidate, and the different answer survives a later independent
  pull. The 2026-09-14 Session-B reconciliation is the first live instance: CCI-003's linguistic cell was
  graded `supports` by Session A and `s` (areal/cultural-leaning) by Session B, and the rule is what forces
  that disagreement to be recorded per-record rather than silently averaged.
- **FALSIFYING.** (5) **Cross-domain convergence evaporates** -- linguistic, developmental, neural,
  comparative and artificial-system evidence support mutually incompatible structures, so the quorum is
  aggregating noise. Or: the quorum is met by every candidate ever proposed, making it non-discriminating
  (a bar nothing fails is not a bar). Currently 4 of 14 records are `admitted` and 0 are `not_required`,
  which is closer to discriminating than not -- but **zero `not_required` records after three literature
  tranches is worth watching**, because the rule's most valuable clause is the one that preserves negative
  findings, and it has never once fired.
- **DISPOSITION: (b) derivational**, use-gated promotion as for NEW-GOV-1.

### MECH-545 (candidate, `substrate_conditional`, v4) -- contract-lesion assays

- **NON-DEGENERACY PRECONDITION.** A within-boundary content-preserving CONTROL exists and works -- the
  lesion must be shown to delete the relation while leaving content intact, distinguished from MECH-537's
  encoded-but-not-exposed phenotype (INV-105 rung 3 vs rung 2). Without that control every lesion result
  is generic information loss.
- **CONFIRMING.** Each of the five lesions, applied at ONE inter-engine boundary, produces a signature
  distinct from the other four AND from a dimensionality-matched random-projection floor, replicating
  across seeds, with acute-frozen-weights and adapted phases separated per ARC-140.
- **FALSIFYING.** (4) **Lesion specificity disappears** -- controlled corruption produces only generic
  information loss, no five-way dissociation. Also, per the thought's section 12, two asymmetric failure
  routes that must be excluded before either verdict: an **off-manifold** lesion damaging unrelated
  computations (false positive: the candidate looks necessary) and **compensation** through an alternative
  pathway (false negative: the mechanism looks unnecessary if only post-adaptation behaviour is examined).
- **MERGE / DEPENDENCY PROPOSAL, not a merge of claims.** MECH-545's `depends_on` should gain **ARC-140**
  and **GOV-INTERVENE-1**. The thought's section 12 causal standard is almost entirely those two claims
  (ARC-140: acute vs adapted, altered causal-importance distribution, selective re-ablation, restoration,
  four-arm design; GOV-INTERVENE-1: the explicit on-/near-/off-manifold construction axis and the
  intervention-attribution rule). No survivor, no absorption -- two edges. Reverse-deps unaffected.
- **DISPOSITION: (c) substrate-blocked, `substrate_conditional`.** The reality-status lesion remains the
  cheapest V3-buildable cousin, but see the currency note below.
- **Currency correction on that cousin.** Both the parent intake and MECH-545's own notes say
  "force-dropping `committed_vs_imagined` at the replay -> consolidation boundary is a small edit". Verified
  2026-09-15: `grep -rn "committed_vs_imagined\|source_status" ree_core experiments` -> **0 hits**. The
  MECH-365 token structure is unbuilt; what exists is `hypothesis_tag` used as a boolean **write gate** at
  that boundary (`ree_core/sleep/mel_consumer.py:46,178`, `ree_core/sleep/phase_manager.py:255`). The
  lesion is still cheap -- forcing the gate open is a small edit -- but it perturbs a *gate*, not a
  *status carried across the boundary*, which is a weaker instance of the assay pattern than the notes
  imply. Whoever routes this should say which of the two they mean.

### MECH-546 (candidate, `substrate_conditional`, v6) -- grammar inherits the contract

- **NON-DEGENERACY PRECONDITION.** The two directions can disagree. If the set of "invariants derived from
  cognition" is read off grammar in the first place, direction (a) is guaranteed and the test is circular
  -- which is exactly the contamination GOV-CONTRACT-1 and the prereg's language firewall exist to
  prevent, so the precondition is: the candidate set was frozen BEFORE the typological comparison.
- **CONFIRMING.** Agreement across both directions: contract-derived invariants over-represented among
  recurrently grammaticalised distinctions, AND recurrently grammaticalised distinctions lacking
  developmental/comparative/computational support classifying as embodied or cultural. Plus the
  emergent-communication prediction: agents transmitting invariant-rich states over a low-cost channel
  develop grammar-like structure for contract relations and not for schema content.
- **FALSIFYING.** Either direction alone (the claim says agreement is the evidence). Concretely: the
  grammaticalised set and the contract set are statistically independent; or agents develop grammar-like
  structure for schema content as readily as for relations. **Existing contrary evidence already in the
  corpus:** `evidence/literature/targeted_review_cognitive_contract_invariants/entries/` carries
  `2026-09-08_mech_546_compositionality_not_required_for_generalization_chaabouni2020` -- compositionality
  is not required for generalisation in emergent communication, which weakens the channel-converges-on-
  relational-structure half. That entry should be read before any confirming citation is attached.
- **DISPOSITION: (f) defer.** v6 per ARC-100's language phase; nothing in V3 or V4 exercises it, and the
  typological work is a `/lit-pull`, not an experiment.

### Q-104 (open, `substrate_conditional`, v4) -- cognifold vs braidling

- **NON-DEGENERACY PRECONDITION.** A severance is actually performable and reversible on both candidate
  configurations -- within-agent (E1/E2/E3/hippocampus) and between-agent -- and a coherence measure
  exists that is not simply task performance. Otherwise the criterion cannot be applied to either side.
- **CONFIRMING.** The severance assay places E1/E2/E3/hippocampus on the cognifold side (severance
  degrades coherence on BOTH sides, not merely coordination) and two communicating REE agents on the
  braidling side (each remains independently coherent), with the placement tracking a measurable
  contract-dimension dependency or MECH-538 bridge complexity rather than being stipulated.
- **FALSIFYING.** The criterion does not separate the two configurations -- either everything severs
  gracefully (no cognifold anywhere in REE) or nothing does (the distinction is not doing work). Also
  falsified if placement tracks task coupling strength alone, with no contract-dimension dependency
  signal: the question would then be answered by ordinary coupling measures and not need the contract.
- **NEW ROUTING FROM THIS THOUGHT.** Section 18 sharpens the cognifold side to "unity could be a property
  of the transformation NETWORK rather than of any one representation". Under NEW-ARC-1 that is directly
  operationalisable: the cognifold is the region of the interface graph whose boundary obligations
  OVERLAP, and the braidling boundary is where overlap goes to zero. If NEW-ARC-1 is registered, Q-104
  should gain it as a `depends_on` -- the overlap measurement NEW-ARC-1 demands is a candidate severance
  criterion.
- **DISPOSITION: (c) substrate-blocked, `substrate_conditional`**, with the severance assay
  `complex (probe-gated)`: a spike measuring obligation overlap at two boundaries would convert it to
  `puzzle (known rules)`.

---

## Part 3 -- dispositions summary

| Claim | Disposition | One-sentence justification |
|---|---|---|
| NEW-ARC-1 | (c) substrate-blocked, `substrate_conditional` | Requires the same recoverability measure at two boundaries; no boundary is instrumented. |
| NEW-GOV-1 | (b) derivational, use-gated promotion | A governance rule with no substrate dependency; promote only after live application. |
| NEW-GOV-2 | (b) derivational, use-gated promotion | Same; its correctness is a question about cost-accounting practice, not about V3. |
| NEW-MECH-1 | (c) substrate-blocked, `substrate_conditional` | Needs rate-constrained multi-consumer compression and a lineage structure; neither exists in `ree_core`. |
| ARC-142 | (c) substrate-blocked, `substrate_conditional` | No boundary instrumented for receiver-side recoverability. |
| GOV-CONTRACT-1 | (b) derivational | Applies now; stale "ledger not built" note should be corrected first. |
| MECH-545 | (c) substrate-blocked + two `depends_on` edges owed (ARC-140, GOV-INTERVENE-1) | Assay pattern unbuilt; its causal standard is already owned by two uncited claims. |
| MECH-546 | (f) defer | v6 language phase; the owed work is a typology `/lit-pull`, and contrary evidence is already filed. |
| Q-104 | (c) substrate-blocked; severance assay `complex (probe-gated)` | No severance is performable; an overlap spike would convert it to `puzzle (known rules)`. |

**No `(e) excrete` and no claim merge is proposed.** The only merge-shaped item is the MECH-545
`depends_on` addition, which is an edge, not an absorption. **No candidate cognitive invariant appears
anywhere in this file as a claim**, per the intake's section 0.
