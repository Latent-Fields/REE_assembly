# Failure Autopsy -- GAP-A candidate-diversity cluster (V3-EXQ-604b / 648a / 649)

- **Generated:** 2026-06-07T14:20:26Z
- **Scope:** cluster (3 runs, one structural property)
- **Status:** confirmed (user-adjudicated via AskUserQuestion, 2026-06-07)
- **Routed from:** governance cycle `governance-cycle-20260607T1346Z` (commit 80c8335256), which walked 6 pending and deferred 604b/648a/649 to /failure-autopsy.
- **Sibling autopsy:** `failure_autopsy_V3-EXQ-651_2026-06-07` (ARC-060, independent -- not part of this cluster).

## TL;DR

All three runs revolve around ONE substrate fact: before 2026-06-07 ~13:14, every CEM
candidate produced an identical `z_world` after one E2 world-forward step
(`cand_world_pairwise_dist ~ 0`) despite differing first actions. Every E3-side
modulatory bias channel therefore reads a **class-uniform pool** -- a bias can have
*magnitude* but ~zero *cross-candidate range*, so it cannot move the argmin.

- **604b** is a **pre-fix null** (ran 11:01, before the GAP-A fix validated at 13:14) -> `non_contributory`, **do NOT weaken** MECH-314 family, retest as 604c.
- **648a** confirms the **curiosity channel** is now load-bearing-ready (C2 PASS); its overall FAIL is driven only by non-load-bearing C1/C3.
- **649** confirms the **shared bias channel** (GAP-A) is now ready (C2 PASS) -> the unblocker for the whole retest set.

This cluster is the **resolution** of the four-instance candidate-pool-collapse confound
(604a / 624a / 614d / 614e), not four independent bugs.

---

## Facts (no interpretation)

### V3-EXQ-604b -- MECH-314/314a/314b/314c, Q-044 (FAIL, self-emitted "mixed"/weakens)
- Ran **2026-06-07T11:01Z** on ree-cloud. Supersedes 604a.
- Preconditions: `curiosity_bias_supra_floor` last_bias_max_abs=**0.0177** >= 1e-4 (MET); `primary_scores_bounded` 1.0 >= 0.9 (MET).
- Load-bearing criterion **C1_mech314_parent_effect_authority_on passed=FALSE** -- with the validated modulatory selection authority ON, the curiosity sub-flavours did not change the selected candidate.
- The GAP-A action-conditional candidate-diversity fix validated **2026-06-07T13:14Z** (V3-EXQ-649) -- i.e. **after** this run.

### V3-EXQ-648a -- MECH-314a Phase-2 substrate-readiness (FAIL, claim_ids=[], flagged precondition_unmet)
- Readiness floors all MET: consumed candidate z_world spread **0.149** >= 0.05; consumed curiosity bias range **0.0206** >= 1e-4; rolled-out magnitude **0.315** <= 1e6 (upper bound).
- Criteria: **C2 (LOAD-BEARING) PASSED** -- visitation source -> per-candidate-varying curiosity bias. C1 (baseline collapsed) passed=FALSE; C3 (augmentation engages-when-needed) passed=FALSE + degenerate (off-engage minus on-engage = 0); C4 (MECH-094 sim gate) passed=TRUE.
- Label logic: `readiness OK + any of C1..C4 fails -> phase2_wiring_does_not_support (FAIL)`. So the FAIL is driven by the two non-load-bearing legs.

### V3-EXQ-649 -- ARC-065 GAP-A shared candidate-summary source (PASS, claim_ids=[], flagged precondition_unmet)
- Load-bearing **C2 (e2_world_forward lifts consumed spread over proposer) PASSED**; ARM_1 consumed-summary spread **0.090** >= 0.05; bounded **0.190** <= 1e6 (direction:upper, comparator:<=).
- Self-route label `gapa_shared_channel_ready`.

### Both precondition_unmet flags are FALSE POSITIVES
The indexer's `_compute_adjudication` (3a) recompute treated every numeric
measured/threshold precondition as a lower-bound floor (`m < t -> precondition_unmet`),
false-flagging the upper-bound `rolled_out_zworld_*_bounded` ceilings (measured ~0.2/0.3
vs threshold 1e6). **Fixed and pushed this morning** (REE_assembly `4cad6af514` +
`639e9e0a59`): a direction-aware recompute + manifest `direction:upper`/`comparator:<=`
tags. The on-origin `pending_review.md` (generated 14:03:47Z) predates the fix and will
clear on the next governance regen.

---

## Claim-layer map

| Claim | Type | Status | v3_pending | Reading |
|---|---|---|---|---|
| MECH-314 / 314a / 314b / 314c | mechanism_hypothesis | candidate_substrate_landed | yes | **intact** -- not tested fairly (candidate pool collapsed pre-GAP-A) |
| Q-044 | open_question | open | -- | **unanswered** -- the ablation could not produce interpretable evidence |
| ARC-065 | architectural_commitment | provisional | no | substrate slot; GAP-A shared channel now validated ready |
| MECH-341 | mechanism_hypothesis | candidate | yes | downstream retest unblocked by 649 |

A `weakens` against the MECH-314 family from 604b would be a **false weakening** of
v3_pending claims that were never given a differentiable candidate pool to act on.

---

## Four-layer diagnosis

| Layer | 604b | 648a | 649 |
|---|---|---|---|
| Claim alignment | intact (not tested fairly) | n/a (claim_ids=[]) | n/a (claim_ids=[]) |
| Biological reference | frontopolar exploration bonus; failure = upstream option-differentiation deficit | novelty/visitation curiosity signature | shared option-evaluation representation |
| Prerequisites | **missing at run time** (GAP-A not yet validated) | present (Phase-2 amend landed) | present (GAP-A re-source landed) |
| Implementation | authority complete; consumed pool collapsed | **load-bearing-ready** (C2 PASS) | **verified ready** (C2 PASS) |
| Environment | adequate | adequate | adequate |
| Measurement | precondition checked magnitude not range (same-statistic confound) | label over-FAILs on non-load-bearing legs | precondition_unmet false-positive (fixed) |
| Integration | partially coupled (upstream collapse) | coupled | coupled |
| Scale | adequate | adequate | adequate |

## Cluster pattern

**Shape:** candidate-pool collapse -- identical post-E2 candidate representations -> bias
has magnitude but ~zero cross-candidate range -> argmin unmoved. Magnitude readiness gates
pass while the range-routed discrimination criterion fails.

**One structural property, not three bugs:** a single upstream substrate property
(action-conditional candidate diversity) gated the entire MECH-314 / ARC-065 / MECH-341
family. 604b is the pre-fix null; 648a (curiosity channel) and 649 (shared channel) are the
two readiness probes confirming the fix is in place. This cluster **resolves** the
four-instance candidate-collapse confound (604a/624a/614d/614e).

---

## Learning extracted

1. A modulatory bias's readiness gate must check **cross-candidate RANGE** (the statistic the selection criterion routes on), not magnitude -- magnitude floors pass under candidate-pool collapse. (Same-statistic confound, cf. 642/648.)
2. A readiness diagnostic whose overall label FAILs on **any** criterion will over-FAIL when a secondary contrast leg fails; the **load-bearing** leg is the verdict-bearing signal (648a C2).
3. The GAP-A fix (validated by 649) is the substrate that finally makes the MECH-314 family testable; the curiosity channel (648a C2) and shared channel (649 C2) are both confirmed action-conditional.
4. C3's auto-augmentation engage-when-needed gate (648a) is **not yet demonstrated** -- a real secondary open item, separable from the Phase-2 readiness verdict.

---

## Routing (user-confirmed)

| Run | evidence_direction | epistemic_category | routing | substrate action |
|---|---|---|---|---|
| 604b | non_contributory | substrate_ceiling | implement-substrate (retest 604c on ready GAP-A); **do NOT weaken** MECH-314 family | amend ARC-065 (append 604b failure_record) |
| 648a | non_contributory | substrate_ceiling (load-bearing PASS) | queue-experiment (optional 648b for C3 augmentation gate); substrate ready | none (Phase-2 landed) |
| 649 | non_contributory | substrate_ready | governance (verified PASS; clears GAP-A blocked_by) | amend ARC-065 (mark GAP-A READY) |

Draft `evidence_quality_note` text for each run is in the companion JSON
(`recommended_evidence_quality_note`). This skill does NOT write claims.yaml, manifests,
review_tracker, or substrate_queue -- /governance applies these.

**Next:** /governance applies the three notes + the ARC-065 substrate amends, marks GAP-A
READY, and (per user) the GAP-A-gated retests can then be queued: V3-EXQ-604c
(MECH-314 family), MECH-341 committed-class diversity, and the ARC-062/063 GAP-B falsifier.
