# Failure Autopsy: V3-EXQ-592d (MECH-090 R-c 4-arm readiness conjunction validation)

**Generated:** 2026-06-01T05:52:37Z
**Resolved (Step 8 user gate):** 2026-06-01T05:55:00Z
**Scope:** single
**Status:** confirmed
**Autopsy session:** failure-autopsy-v3-exq-592d-20260601T055237Z
**Routing decision:** `/queue-experiment` for a V3-EXQ-592e redesign of the C1 baseline criterion. NOT a substrate falsification.

---

## 1. Target and the failure mode

| Field | Value |
|---|---|
| Script | `ree-v3/experiments/v3_exq_592d_mech090_readiness_conjunction_validation.py` |
| Run manifest | `REE_assembly/evidence/experiments/v3_exq_592d_mech090_readiness_conjunction_validation_20260531T213852Z_v3.json` |
| claim_ids (script) | `["MECH-090"]` |
| experiment_purpose | `diagnostic` |
| supersedes | V3-EXQ-592c (FAILed on ree-cloud-3 2026-05-30) |
| outcome (manifest) | `FAIL` |
| failed criterion class | all four (C1 + C2 + C3 + C4) |

**Acceptance rule (from script):** `PASS = C1 AND (C2 OR C3) AND C4`.

**Arm matrix:** 4 arms x 3 seeds (42 / 43 / 44):
- ARM_0 BASELINE_BOTH_OFF -- legacy rv-only commit entry; no gates.
- ARM_1 SCORE_MARGIN_ONLY -- within-tick decisiveness (Hanes & Schall 1996 reading) at floor=0.05.
- ARM_2 NAV_COMPETENCE_ONLY -- across-tick motor-program readiness (Cisek & Kalaska 2010 + Roesch / Calu / Schoenbaum 2007) at floor=0.3, initial=0.0 fail-closed.
- ARM_3 BOTH_GATES_ON -- full R-c conjunction (AND-composed at both elevate sites).

## 2. Facts (manifest, no interpretation)

Per-arm aggregates across 3 seeds:

| Arm | total_p2_steps | total_commits | total_committed_steps (sum of seeds, P2) | n_commit_entries | score-margin blocks | nav-competence blocks | hold_rate (per-seed) |
|---|---|---|---|---|---|---|---|
| ARM_0 BOTH_OFF | 18729 | **0** | 18729 (P2 hold_rate=1.0) | **0** | 0 | 0 | 1.0 across all 3 seeds |
| ARM_1 SCORE_MARGIN_ONLY | 16443 | **0** | 2513 (seed 42) | **0** | **2005** | 0 | 0.0 across all 3 seeds |
| ARM_2 NAV_COMPETENCE_ONLY | 15204 | **0** | varies | **0** | 0 | **150** | 0.0 across all 3 seeds |
| ARM_3 BOTH_ON | 15987 | **0** | varies | **0** | **1949** | **150** | 0.0 across all 3 seeds |

Acceptance criteria from manifest `acceptance` block:

| Criterion | Predicate | Observed | Verdict |
|---|---|---|---|
| C1 BASELINE_FIRES | ARM_0 commit_rate > 0.001 | 0.0 | FAIL |
| C2 SCORE_MARGIN_DISCRIMINATES | ARM_1 false_commit_rate < ARM_0 * 0.7 | 0 vs 0 (note: "baseline false_commit_rate=0; cannot demonstrate reduction") | FAIL |
| C3 NAV_COMPETENCE_FIRES | ARM_2 nav_blocks >= 1 AND ARM_2 commit_rate < ARM_0 commit_rate | nav_blocks=150 (PASS half) AND 0.0 NOT-strictly-less-than 0.0 (FAIL half) | FAIL |
| C4 CONJUNCTION_SUPPRESSES_DEGENERATE | ARM_3 false_commit_rate < 0.10 AND ARM_3 commit_rate > 0 | 0.0 (PASS half) AND 0.0 (FAIL half) | FAIL |

ARM_0 P0 outcomes: rv converged in all 3 seeds (final rv 2.72e-5 / 1.94e-6 / 3.67e-6 -- all well below `commit_threshold=0.4`).

P2 hold rates (rv-only ARM_0): 1.0 across all 3 seeds -- the agent is in committed state every single tick of P2 under ARM_0.

## 3. Claim-layer mapping

MECH-090 `control_plane.commitment_gated_policy_output`: `claim_type=mechanism_hypothesis`, `status=active`, `implementation_phase=v3`, `claim_level=mechanistic`. R-c amendment substrate (within-tick decisiveness axis) landed 2026-05-28 + R-c continuation (across-tick motor-program readiness axis) landed 2026-05-29. claims.yaml carries a comprehensive `evidence_quality_note` block tracking the 592 lineage history.

**Did the experiment let the claim express itself?**

NO -- the test design has an instrumentation defect on the C1 baseline criterion that renders all four acceptance criteria structurally unmeetable, INDEPENDENT of substrate behaviour. The substrate IS firing as predicted (2005 score-margin blocks on ARM_1; 150 nav-competence blocks on ARMs 2 + 3) -- but the script's chosen "commit entry" count predicate is unmeasurable under the rv-only baseline semantic at hand.

`claim_ids=["MECH-090"]` is accurate -- the script does directly test MECH-090's commit-entry predicate. The issue is not tag accuracy; it is the predicate chosen for the C1 baseline.

## 4. Biological-reference triage

R-c amendment cluster anchored on three load-bearing biological readings (per `REE_assembly/evidence/literature/targeted_review_connectome_mech_090/synthesis.md` commit 9e68c5ca8a):

| Axis | Anchor | Implementation |
|---|---|---|
| Within-tick decisiveness | Hanes & Schall 1996 (FEF accumulator-to-threshold) | `BetaGate.should_admit_elevation(margin, K)` -- 2005 blocks ARM_1 confirms firing |
| Across-tick motor-program readiness | Cisek & Kalaska 2010 (affordance preparation) + Roesch / Calu / Schoenbaum 2007 (dopaminergic readiness) | `CommitReadiness.is_above_floor` EMA -- 150 blocks ARM_2/3 confirms firing |

Substrate is NOT a formal-definition import -- it is a biology-faithful translation. Both gates demonstrably fire at the elevate sites at the expected rates. The biological reference does not require the implementation to fail; the test predicate is the problem.

`lit_status: present` -- the connectome lit-pull synthesis is current and load-bearing.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact -- claim NOT tested | C1 baseline unmeasurable under rv-only ARM_0 entry semantic; gates 2/3 nav-blocks firing as predicted; C3 ARM_2-commit_rate-less-than-ARM_0 fails ONLY because ARM_0 baseline is also 0 (the test design's flaw, not the substrate's). |
| Biological reference | clear | Three R-c anchors load-bearing; no biology divergence; both axes wired and firing. |
| Prerequisites / dependencies | present | R-c within-tick (2026-05-28) + across-tick (2026-05-29) substrates both landed; `notify_outcome()` harness-push seam exercised correctly (150 nav blocks confirm reading the per-tick proxy push). |
| Implementation completeness | substrate COMPLETE; SCRIPT has measurement defect | `n_commit_entries = beta_gate.mech090_n_elevation_admitted` is a TRANSITION-EDGE counter. Under ARM_0 the agent enters P2 already committed (P0 trained rv to ~1e-5 / 1e-6 / 1e-6 across seeds, well below `commit_threshold=0.4`) and stays continuously committed (hold_rate=1.0, beta_elevated_steps == committed_steps). No fresh entry transitions during the measurement window -> n_commit_entries = 0 *unconditionally* on ARM_0 regardless of gate state. |
| Environment | adequate | committed_mode_curriculum standard P0/P1/P2; same env as 592b/c. |
| Measurement | UNDER-INSTRUMENTED / MISLEADING | C1's `commit_rate > 0.001` is structurally unmeetable under the actual ARM_0 semantic (continuous-committed-from-tick-0). C2/C3/C4 inherit the defect via cross-arm comparison against ARM_0. The script's interpretation grid says "C1 FAIL -> /diagnose-errors on curriculum harness, NOT the gate" -- but the curriculum harness is working as designed; the predicate is wrong. |
| Integration | ok | Harness push pattern via `commit_readiness.notify_outcome()` correctly advances the across-tick EMA (150 nav blocks). AND-composition at both elevate sites visible in ARM_3's 1949 score + 150 nav blocks. |
| Scale / capacity | adequate | 3 seeds x 4 arms x ~50 episodes; P0 convergence robust across all 12 cells. |

**Recommended `epistemic_category`:** `non_contributory` -- test-design measurement gap; substrate not falsified, claim not tested under conditions where it could express itself at the chosen acceptance predicate.

## 6. Cluster pattern

Single target. The 592 lineage:
- V3-EXQ-592 (2026-05-21): rv-only-predicate degeneracy reproduction (seed 42 substrate-readiness motivating signal for R-c amendment). NOT governance evidence against MECH-090.
- V3-EXQ-592b: manifest-pipeline silent-drop (2026-05-29 cluster autopsy with V3-EXQ-490h + V3-EXQ-614).
- V3-EXQ-592c: FAILed on ree-cloud-3 2026-05-30.
- V3-EXQ-592d (this autopsy): 4-arm extension adding the nav-competence axis to the prior 2-arm structure.

No cross-claim cluster -- the 592 lineage is single-claim (MECH-090). The convergent pattern across this lineage is "the rv-only baseline is the load-bearing measurement problem" -- 592 surfaced it as the degeneracy that motivated R-c; 592d reveals that the same regime makes the C1 baseline predicate structurally unmeetable. The biological substrate is sound across both observations.

## 7. Learning extracted

- The R-c amendment cluster (both axes) is wired correctly and demonstrably active: score-margin gate fires 2005 times on ARM_1; nav-competence gate fires 150 times on ARM_2/3; AND-composition at both elevate sites visible in ARM_3.
- The test script's C1 baseline predicate (`commit_rate > 0.001` where `commit_rate = sum(n_commit_entries) / total_p2_steps`) is structurally unmeetable under the rv-only-baseline semantic where the agent enters P2 already committed. `n_commit_entries` is a transition-edge counter; the agent has no transitions to count.
- The script's interpretation-grid routing for C1 FAIL is wrong: it says "C1 FAIL -> /diagnose-errors on curriculum harness, NOT the gate." But the curriculum harness is working as designed (P0 convergence robust; P2 hold_rate=1.0 on ARM_0 is the CORRECT rv-only behaviour). The defect is in the script's choice of C1 predicate.
- A V3-EXQ-592e successor needs structural rethink of C1 -- either (a) force the agent into uncommitted state at P2 entry (rv reset / variance perturbation / brief committed_threshold raise pre-measurement) so every elevation IS a transition, OR (b) replace C1 with a hold-rate-based baseline criterion (`ARM_0 hold_rate >= 0.5 over committed_steps`) so the predicate matches the actual rv-only semantic.
- The 2026-05-21 V3-EXQ-592 seed-42 degeneracy signature (running_variance=2.7e-5 with nav_competence=0.0 satisfying rv-only) that motivated the R-c amendment is REPRODUCED here at ARM_0 across all 3 seeds (final rv 2.72e-5 / 1.94e-6 / 3.67e-6). This is positive substrate-side evidence that the rv-only entry semantic IS the degenerate basin the R-c amendment was designed to gate.

## 8. User decision (interactive gate, satisfied 2026-06-01T05:55Z)

User confirmed via AskUserQuestion two-question gate:

**Q1 -- MECH-090 verdict:** "non_contributory + queue 592e redesign (Recommended)" -- reclassify V3-EXQ-592d `evidence_direction` non_contributory for MECH-090; route to `/queue-experiment` for V3-EXQ-592e fixing the C1 baseline predicate. R-c substrate (both 2026-05-28 + 2026-05-29 landings) remains pending behavioural validation. `claim_ids=[MECH-090]` unchanged. `pending_retest_after_substrate=false` (substrate is sound; the test needs redesign, not the substrate).

**Q2 -- Process flags (multi-select):** (a) "C1 baseline criterion needs structural rethink for any 592e (Recommended)" + (b) "Note the script's interpretation-grid C1 FAIL routing is wrong (Recommended)". Lit-anchor revisit NOT required -- R-c synthesis remains current.

## 9. Recommended writes (governance / queue handoff -- NOT applied this session)

- `claim_evidence.v1.json` / indexer: V3-EXQ-592d entry should carry `evidence_direction: non_contributory` for MECH-090 (`evidence_direction_per_claim` field not needed -- single-claim experiment; the run-level `evidence_direction` override is sufficient).
- claims.yaml MECH-090 `evidence_quality_note`: append a paragraph documenting V3-EXQ-592d test-design defect (exact text in `recommended_evidence_quality_note` field of the JSON artifact).
- `review_tracker.json`: V3-EXQ-592d run_id and dir name added to `reviewed_run_ids` / `discussed_experiment_dirs` after `/governance` walks this.
- `substrate_queue.json`: NO new entry, NO amendment. R-c substrate (both axes) was already landed pre-592d; commitment_closure:GAP-4 remains substrate_landed_pending_validation; the gap is closure-plan-side (a new validation EXQ), not substrate-queue-side.
- `experiment_proposals.v1.json`: no entry to mark executed (592d was a substrate-readiness retest of the R-c amendment; no governance-side proposal).
- `/queue-experiment`: V3-EXQ-592e queued in a separate session after this autopsy lands. Script options (decision left to the /queue-experiment skill author):
  - **Option (a) -- force-uncommitted P2 entry:** at P0 -> P2 transition, raise committed_threshold briefly OR inject rv perturbation so the agent starts P2 in uncommitted state. Every commit during P2 measurement IS then a fresh entry transition; n_commit_entries becomes a meaningful counter.
  - **Option (b) -- hold-rate-based C1:** replace `commit_rate = n_commit_entries / total_p2_steps > 0.001` with `ARM_0 mean P2 hold_rate >= 0.5` (or similar). This matches the actual rv-only-baseline semantic. C2/C3/C4 also need redesign on the same logic -- compare hold_rate / gate-block fraction across arms rather than commit-entry counts.
  - The interpretation grid in 592e must update the "C1 FAIL" row to route to `/queue-experiment` (script redesign) rather than `/diagnose-errors` (curriculum harness).

## 10. Provenance

| Source | What it told us |
|---|---|
| `REE_assembly/evidence/experiments/v3_exq_592d_mech090_readiness_conjunction_validation_20260531T213852Z_v3.json` | 4-arm x 3-seed arm aggregates + acceptance block + per-cell P0 / P2 metrics |
| `ree-v3/experiments/v3_exq_592d_mech090_readiness_conjunction_validation.py` | Script docstring (acceptance rule + interpretation grid + arm matrix); per-tick nav_competence push pattern; supersession lineage 592 / 592b / 592c |
| `REE_assembly/docs/claims/claims.yaml` lines 4785-4980 | MECH-090 `evidence_quality_note` block tracking 592 lineage; R-c amendment implementation_note documenting both 2026-05-28 + 2026-05-29 substrate landings |
| `REE_assembly/evidence/planning/failure_autopsy_V3-EXQ-490h-V3-EXQ-592b_2026-05-30.md` | Predecessor cluster autopsy (manifest-pipeline silent-drop bug fixed at ree-v3 commit 41c3411); confirms V3-EXQ-592b was NOT a substrate failure |
| `REE_assembly/evidence/literature/targeted_review_connectome_mech_090/synthesis.md` commit 9e68c5ca8a | R-c reading anchors (Cisek & Kalaska 2010 + Hanes & Schall 1996 + Roesch / Calu / Schoenbaum 2007); R-b Tandetnik 2021 fallback |
| `ree-v3/CLAUDE.md` MECH-090 R-c sections (2026-05-28 + 2026-05-29) | Substrate-side wiring narrative; contract test pass counts; backward-compatibility guarantee |

---

## Process flags surfaced for governance

(a) **C1 baseline criterion needs structural rethink for any 592e successor.** The current `commit_rate > 0.001` predicate is structurally unmeetable under the rv-only ARM_0 entry semantic (continuous-committed-from-tick-0). Successor must redesign via force-uncommitted P2 entry OR hold-rate-based baseline. Add to claims.yaml MECH-090 `evidence_quality_note`.

(b) **Script interpretation-grid routing is wrong on C1 FAIL.** The script says "C1 FAIL -> /diagnose-errors on curriculum harness, NOT the gate." The curriculum harness is working as designed (P0 convergence robust; P2 hold_rate=1.0 on ARM_0 is the correct rv-only semantic). The defect is in the script's chosen C1 predicate. The 592e interpretation grid must update this routing row.

## Routing summary

- `evidence_direction` recommended: `non_contributory` (MECH-090)
- `epistemic_category` recommended: `non_contributory`
- `pending_retest_after_substrate`: `false` (substrate is sound; the test needs redesign)
- `narrow_supports_flag`: `false`
- Routing: `/queue-experiment` for V3-EXQ-592e C1 redesign (separate session)
- No new substrate_queue entry; no /diagnose-errors loop; no claims.yaml status change beyond the recommended `evidence_quality_note` append
