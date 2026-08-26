# `/thought-digestion v3-closure` -- PILOT WAVE 1, drafts for review

**Date:** 2026-08-26 · **Session:** `thoughtdig-grouping-7fd98a-wave1`
**Status:** STAGED ONLY -- **no `claims.yaml` write has been made and none will be made by
this session.** `claims.yaml` is held by the concurrent live session
`insights-7fd98a-digestion`; this pilot is deliberately draft-only and read-only on the
registry. Dispositions are the user's call.

**Mode under test:** grouped (wave-of-groups), `cap=5 floor=3.0`, edge-first agglomerative,
scope = closure-core + 1 hop. One agent per GROUP, three groups in parallel.
**Design + measurements:** `thought_digestion_wave_grouping_design_20260826.md`.

**Wave 1 = 3 groups / 12 claims** (of the 31-claim scope; wave 2 = the remaining 19 in 9
groups, worklist already built). All 12 verified undigested (`what_would_answer` absent,
no `digestion_note`) and disjoint from the concurrent live session's own wave 1/2 claims.

| group | claims | closure-core | why grouped |
|---|---|---|---|
| G1 | MECH-312b, MECH-312c, MECH-316, MECH-317, MECH-318 | 5/5 | `subject: policy.arbitration*` + shared registration batch + `depends_on` |
| G2 | MECH-263, SD-033b, ARC-113, MECH-298 | 2/4 | MECH-263's title NAMES SD-033b; `pfc.*`; ARC-113/MECH-298 one `depends_on` hop |
| G3 | MECH-254, SD-027, SD-064 | 2/3 | SD-064 is the organising concept both instantiate; pulled in by the hop |

---

## PILOT FINDINGS -- mechanism defects found while ASSEMBLING the wave

These are findings about the grouped mode itself, independent of what the agents return.

### P1. `cap=5` splits lettered claim families -- CONFIRMED, and the fix is free
`MECH-312a` <-> `MECH-312b` = **6.00** and `MECH-312a` <-> `MECH-312c` = **6.00**, yet
312a was stranded as a **solo in a different wave**. Mechanism: edge-first agglomeration
consumes the strongest edges first (`316`<->`318` = 8.00, `317`<->`318` = 8.00,
`312b`<->`317` = 7.00), filling the group to cap=5 as {316,317,318,312b,312c}; 312a then
cannot join a full group.

Measured across the full backlog: **4 lettered families have >=2 undigested members, and 2
of the 4 (50%) are split** (`MECH-312a/b/c/d` across two groups; `SD-033b`/`SD-033c` across
two). **No family exceeds cap=5 on its own**, so the fix costs nothing:

> **Proposed refinement (not yet applied to SKILL.md):** pre-merge lettered families
> (same numeric stem, e.g. `MECH-312a..d`) into an ATOMIC unit before clustering, and let
> the cap flex to accommodate a family. Never split a family across groups or waves.

Confidence: the fix is free and clearly right in direction, but n=4 families is a small
base. Flagged rather than shipped.

### P2. The scope filter itself splits a family
`MECH-312d` is `MECH-312a`'s joint-top partner (**6.00**) and is **outside** the
closure-core+1hop scope, so the scoped run sees only 312a/b/c of a 4-member family. The
`depends_on` hop does not close over lettered families.

> **Proposed refinement:** when any member of a lettered family is in scope, pull the whole
> family into scope (a "family closure" rule alongside the `depends_on` hop), OR admit the
> absent members as read-only CONTEXT MEMBERS (design doc 7b.4) so the agent at least sees
> them.

### P3. Deviation from the skill text, deliberate, for evaluation
Step 4/G3 says embed each claim's full YAML block **verbatim in the agent prompt**. Here
the blocks were pre-extracted to a file the agent reads instead (G1 425 lines, G2 547, G3
239 -- 1211 lines total). Rationale: identical information, no 86,000-line registry search,
and prompts stay readable. **Whether this weakens the "extract before inventing"
instruction is an open question this pilot should answer** -- if agents drift toward
inventing, embed verbatim next time.

---

## Wave timing

- dispatched 2026-08-26T20:14:45Z

---

## GROUP RESULTS

*(agents in flight -- results appended on completion)*

---

## GROUP G2 -- MECH-263, SD-033b, ARC-113, MECH-298  (returned 20:22Z, ~7.8 min)

### Dispositions
| claim | disposition |
|---|---|
| MECH-263 | **(c) substrate-blocked -- `substrate_ceiling`, NOT `substrate_conditional`** (see FLAG 1), with an (a)-testable representation-plane carve-out |
| SD-033b | **(a) testable now** -- mint a REPRESENTATION-PLANE SD-033b-vs-SD-033c distinguishability proposal |
| ARC-113 | **(f) defer with a durable marker** -- but a CORRECTED gate + the stage-implementation audit the claim owes |
| MECH-298 | **(a) testable now** -- the only claim in the group neither competence-floor-blocked nor substrate-blocked |

### What the GROUPED view produced that per-claim dispatch could not

1. **`depends_on` CYCLE between MECH-263 and SD-033b** -- each declares the other its ground.
   Neither can be topologically ordered; a governance move on either has no defined
   propagation direction. Only visible reading both blocks together.
2. **Their `functional_restatement` blocks are ~90% identical prose and their `falsifiable`
   clauses are THE SAME falsifier** ("collapses back into SD-033c"). **This explains a
   16-run, zero-evidence trail**: 16 manifests (485 x4, 485a-485m, 696 x2), every one
   adjudicated `non_contributory`, `genuine_exp_count: 0`,
   `experimental_confidence: 0.0` on BOTH claims. The two claims have been tested sixteen
   times and have zero evidence in either direction, because they were being asked the
   same question.
3. **The fix is DIFFERENTIATION, not merge** -- and the agent explicitly declined (g),
   correctly: a `design_decision` and a `mechanism_hypothesis` can each survive the other
   being wrong. SD-033b now takes the *substrate-distinguishability* falsifier; MECH-263
   takes the *functional-signature* falsifier. Different experiments, different
   preconditions, and **only one is competence-floor-blocked.**
4. **MECH-263 fuses ARC-113's `representation` and `prediction` stages** and says so
   explicitly. This hands ARC-113 a **pre-registered prediction it did not have**: the
   representation/prediction seam is the most likely non-dissociable pair, so ARC-113's
   ablation must either find a locus where they separate (`OFCConfig.use_outcome_oracle`,
   verified live) or report the pair as fused and accept a partial refutation at that seam.
5. **MECH-298 is a ready-made ON/OFF lesion for ARC-113's apprehension->representation
   seam** -- already designed, representational readout, so ARC-113 should reuse it rather
   than design a stage-lesion from scratch.
6. **ONE shared falsification condition** (the competence-floor non-degeneracy
   precondition) that MECH-263, SD-033b and ARC-113 should all POINT AT rather than
   re-derive -- 16+ manifests have independently rediscovered it -- **and MECH-298 is
   identified as the one claim that ESCAPES it** (representational DV, not committed
   behaviour).
7. **Cross-cutting finding:** the group is uniformly **mis-planed** -- every registered
   falsifier is on the BEHAVIOURAL plane while every claim's actual evidence, substrate
   maturity and tractability sit on the REPRESENTATION plane. 16 runs of confirming that
   the readout plane is wrong is enough signal to change the plane rather than the gain.

### Governance flags raised (5)
- **FLAG 1** -- `epistemic_category` on MECH-263 + SD-033b appears silently DOWNGRADED
  `substrate_ceiling` -> `substrate_conditional`, contradicting their own notes which say
  `substrate_ceiling` six times incl. *"11th substrate_ceiling reading"* (2026-06-22).
  Flipped between 2026-06-22 and 2026-07-11. **Agent deliberately did NOT decide** --
  both readings defensible, no artifact records the decision. Governance call.
- **FLAG 2** -- V3-EXQ-696 (2 runs, reviewed, adjudicated, `weakens` OVERTURNED to
  `non_contributory`, cleared SD-033b's `hold_candidate_resolve_conflict` agenda item) is
  recorded in **neither** claim's `evidence_quality_note`.
- **FLAG 3** -- SD-033b note cites `ree_core/pfc_analogs/ofc_analog.py`; **that directory
  does not exist** (correct path `ree_core/pfc/ofc_analog.py`). Isolated stale path.
- **FLAG 4** -- both notes terminate on *"next test is the co-armed full-stack arm"*, which
  RAN as V3-EXQ-714 (2026-07-07), terminal FAIL, readiness abort, C2 never scored, brake
  FIRED, re-queue REFUSED. **Following the note's instruction today attempts an
  already-REFUSED re-queue.**
- **FLAG 5** -- ARC-113's gate cites a release condition **already discharged**
  (V3-EXQ-654g, 2026-06-19, a month BEFORE ARC-113 was registered 2026-07-22); the real
  surviving blocker is the conversion ceiling, which binds only its behavioural route.
- **Registry defect** -- the MECH-263 <-> SD-033b `depends_on` cycle (item 1 above).

### Currency verified live in `ree-v3` (2026-08-26)
`ofc_analog.py` state_bias_head / devaluation_bias_head / `use_outcome_oracle` all LIVE
as described; `GoalState.is_active()` exists; MECH-288 `EventSegmenter` slow scale IS a
BOCPD-Gaussian on `z_goal` (= MECH-298's stated trigger); gate-modulated EMA confirmed on
both MECH-298 write targets; **no MECH-298 implementation exists anywhere** (note correct).
ARC-113 and MECH-298 are **absent from `claim_evidence.v1.json` entirely**.

### Agent's own stated uncertainty (kept, not smoothed)
- FLAG 1 left undecided on purpose.
- The MECH-263 outcome-oracle identity-decoding route is a **design sketch**: it was NOT
  verified that `E2HarmSForward` emits anything from which outcome IDENTITY (vs scalar
  harm magnitude) is decodable. **The single assumption most worth checking before minting.**
- ARC-113's representation-plane route is plausible but unproven -- depends on the
  unbuilt stage audit; this is why (f) not (a).
