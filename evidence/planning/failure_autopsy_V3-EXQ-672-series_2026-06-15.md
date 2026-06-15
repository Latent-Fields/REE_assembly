# Failure Autopsy -- V3-EXQ-672 series (MECH-057b trajectory promotion gate)

- **Generated (UTC):** 2026-06-15T04:20:05Z
- **Scope:** cluster (V3-EXQ-672 / 672a / 672b)
- **Status:** confirmed (user-adjudicated 2026-06-15)
- **Claim:** MECH-057b -- "Hippocampal sequence completion must be verified before candidates are eligible for E3 selection." (mechanism_hypothesis, candidate, conf 0.0, v3_pending, zero genuine prior evidence)
- **Routing:** non_contributory (672b) + pending_retest_after_substrate; implement-substrate **amend** on ARC-065 (candidate-pool divergence track)

---

## 1. Facts (no interpretation)

The experiment installs a proxy completion gate at the harness candidate->E3 seam
(`_filter_trajectories_by_completion`), ranking candidates by
`hippocampal._score_trajectory` (residue-completion cost, lower = more complete),
comparing ARM_0_NO_GATE vs ARM_1_COMPLETION_GATE. The series is **progressive
instrumentation-peeling**, not three independent bugs:

| Run | Machine | Fix introduced | C3 gate fires | C6 baseline forages | C1 harm / C2 completion | Recorded |
|---|---|---|---|---|---|---|
| **672** (2026-06-12) | cloud-3 | -- | **No** (absolute threshold 2.0 above the whole score distribution; filtered_fraction 0.0) | No (goal_succ 0.0) | n/a | `superseded` (scoring-excluded) |
| **672a** (2026-06-13) | cloud-1 | relative-quantile gate | **Yes** (40.6%) | **No** -- eval read `info["resource_collected"]`, a key `CausalGridWorldV2.step()` never emits -> goal_succ structurally 0.0 in **both** arms | vacuous (no functional baseline) | `non_contributory` (governance-applied 2026-06-14) |
| **672b** (2026-06-15) | cloud-1 | read `transition_type=="resource"` + `num_resources 1->3` | **Yes** (40.6%) | **Yes** (goal_succ ARM_0 = 0.26) | **C1 FAIL** (harm ARM_1 0.343 > ARM_0 0.311), **C2 FAIL** (completion 0.34386 vs 0.34388) | `weakens` -> **adjudicated here** |

672b criteria: C1 FAIL, C2 FAIL, C3 PASS, C4 PASS, C5 PASS, C6 PASS, C7 PASS;
`non_degenerate=true` (the check_degeneracy net passed -- C1/C2 channels move across seeds).

**Load-bearing measurements (672b):**
- `mean_candidate_score_spread_ARM_1 = 0.009035` -- the residue-completion scores across the 8 CEM candidates are near-identical.
- `mean_completion_signal_ARM_0 = 0.343979`, `mean_completion_signal_ARM_1 = 0.343859` -- **pinned ~0.3439 regardless of the gate** (delta ~1.2e-4).
- `mean_filtered_fraction_ARM_1 = 0.4062` -- the gate mechanically drops the bottom 40% by quantile.

So the gate filters 40% of candidates, but the dropped candidates are
indistinguishable from those kept (spread 0.009). Filtering a flat distribution
cannot improve harm/completion; ARM_1 harm even rises slightly, exactly as random
candidate removal would.

## 2. Claim-layer map

MECH-057b is V3-scoped with **zero genuine experimental evidence**: the historical
EXQ-048/048b/059/060 tags were corrected away in 2026-03-22 (they tested MECH-090,
not the hippocampal candidacy gate). 672b would have been the first genuine counted
experiment. The claim's note states the actual mechanism -- a HippocampalModule
feedback path suppressing partial trajectories before E3 -- **is not yet implemented**;
672 installs a harness quantile **proxy**.

**Did the experiment let the claim express itself?** No. The gate can only express
MECH-057b if candidates differ in completion quality. The substrate presented spread
0.009 and a completion_signal pinned across arms, so the C1/C2 cross-arm contrast is
vacuous *about the claim* (though the run is non-degenerate by the indexer's net).

## 3. Biological-reference triage (the core move)

Closest reference: hippocampal sequence-completion verification gating commitment --
CA3 autoassociative pattern completion; Lisman & Grace 2005 subiculum->NAc->VP->VTA
completion-to-dopamine loop; Foster & Wilson reverse replay. REE already partly
implements the coupling (ARC-028 / MECH-105 completion-signal -> BetaGate). The biology
is an existence proof for the **class** of mechanism.

**Does the failure match a missing dependency of the reference mechanism?** Yes. The
reference mechanism requires partial-vs-completed candidates to discriminate between.
The REE substrate has the *symbol* of completion-verification (a quantile filter on a
completion score) but not the *functional role*: `_score_trajectory` carries no
cross-candidate discriminative information (spread 0.009), so ranking on it is ranking
on noise. This is a **faithful-translation gap / substrate ceiling**, not a falsification.

## 4. Four-layer diagnosis (672b)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact / not-yet-tested | the gate never saw a discriminable spread; weakens unwarranted |
| Biological reference | clear | CA3 pattern-completion -> commitment; reference mechanism exists |
| Prerequisites / dependency | missing | needs candidates differing in completion quality; spread 0.009, completion_signal flat 0.3439 |
| Implementation completeness | partial / proxy | claimed HippocampalModule promotion policy unbuilt; harness quantile proxy ranks on a flat score |
| Environment adequacy | adequate (672b) | num_resources 1->3 + correct readout -> functional baseline (goal_succ 0.26) |
| Measurement adequacy | adequate (672b) | 672a `resource_collected` bug fixed; FAIL is genuine, not instrumentation |
| Integration adequacy | coupled but inert | gate fires (40.6%) but acts on a non-discriminative signal |
| Scale / capacity | unknown | candidate-pool collapse may reflect an under-discriminative substrate at test scale |

Recommended `epistemic_category`: **substrate_ceiling**.

## 5. Cluster pattern

| Experiment | Claim | Negative-control / absolute criterion | Discrimination criteria | Read |
|---|---|---|---|---|
| 672 | MECH-057b | C6 FAIL (baseline 0.0), C3 FAIL (filtered 0%) | -- | gate mis-scaled; superseded |
| 672a | MECH-057b | C6 FAIL (resource_collected key bug; both arms 0.0) | C3 PASS (40.6%) but no baseline | instrumentation; non_contributory |
| 672b | MECH-057b | **C6 PASS** (0.26), **C3 PASS** (40.6%) | **C1/C2 FAIL** on flat completion score (spread 0.009) | substrate ceiling |

**Independent bugs or one structural property?** One structural property. The series
peels instrumentation (mis-scaled threshold -> resource-readout bug + baseline collapse)
and converges at 672b on: *the substrate has the wiring MECH-057b asserts but does not
carry the information at the granularity the claim asserts*. The CEM candidate pool is
monostrategy-collapsed, so `hippocampal._score_trajectory` has negligible cross-candidate
spread -- the same collapse documented for z_world (ARC-065 GAP-A `cand_world_pairwise_dist=0`;
V3-EXQ-543e first-action spread 1e-4; V3-EXQ-614e). Two live readings: substrate
enrichment (make the pool discriminable) vs test-design ceiling (the harness proxy can
never be better than the score it ranks on). Both force the same next step: gate the
MECH-057b retest on candidate-pool completion-score discriminability.

## 6. Learning extracted

- The MECH-057b completion gate ranks on `hippocampal._score_trajectory`; under candidate-pool collapse that score has ~0.009 cross-candidate spread, so the gate filters indistinguishable candidates and cannot help -- substrate ceiling, not falsification.
- The 672 series converges on one structural property at 672b, not three independent bugs.
- The flat completion-score channel is the same candidate-pool collapse as ARC-065 GAP-A (z_world) / SD-056; any per-candidate ranking gate inherits it.
- MECH-057b's actual mechanism (HippocampalModule promotion policy) is unbuilt; the experiment tests a harness quantile proxy.
- A future retest (672c) must carry a `mean_candidate_score_spread` non-vacuity precondition before scoring C1/C2 -- the explicit guard against re-running the same vacuous contrast (cf. the V3-EXQ-672 degeneracy guard the 672b script already added for filtered_fraction).

## 7. Repair pathway (routing)

**672b: `weakens` -> `non_contributory` + `pending_retest_after_substrate`** (user-adjudicated).
Returns MECH-057b to zero genuine evidence (no illusory conflict; it had none).
**672a: no change** (already non_contributory; cluster autopsy confirms the readout-bug diagnosis).
**672: no change** (superseded).

**implement-substrate `amend` on ARC-065** (candidate-pool divergence track / GAP-A
`cand_world_pairwise_dist`): append the 672b failure record (see JSON
`recommended_substrate_queue_entry`). Once the ARC-065 GAP-A route-range / SD-056 work
lands divergent per-candidate predictions on a trained substrate, re-check that
`mean_candidate_score_spread` rises, then re-queue the MECH-057b gate as **672c** with
a `mean_candidate_score_spread` non-vacuity precondition. (No `/claim-synthesis`: this is
the first autopsy on the MECH-057b `bears_on` target -- 677/669a only mention it in
passing -- so the granularity-debt recurrence trigger does not fire.)

Draft `evidence_quality_note` for governance to write on the 672b manifest: see the JSON
`recommended_evidence_quality_note`.

## 8. Routing decision confirmed (Step 8 gate)

User selected (AskUserQuestion 2026-06-15):
1. **non_contributory + pending_retest_after_substrate** for 672b.
2. **implement-substrate: amend** the ARC-065 candidate-divergence entry; gate the retest on cand-pool divergence readiness with a `mean_candidate_score_spread` non-vacuity precondition.
