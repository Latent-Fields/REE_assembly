# Failure Autopsy: V3-EXQ-671a (MECH-025b, precision-responsibility attribution, corrected retest)

**Generated:** 2026-08-02T10:14:48Z
**Run:** `v3_exq_671a_mech025b_precision_responsibility_20260802T035128Z_v3`
**Queue ID:** V3-EXQ-671a
**Claim IDs:** MECH-025b
**Status:** confirmed
**Supersedes:** V3-EXQ-671 (`failure_autopsy_batch9_2026-06-12`, degenerate — residue never accumulated)

## 1. Facts

**Design.** Single-seed (seed=0) retest of MECH-025b ("high-precision action mode carries responsibility attribution: actions committed at higher precision should accumulate proportionally more residue than low-precision actions"). The driver's own docstring documents a careful, code-verified root-cause fix of 671's degenerate result: (1) 671 never called `agent.update_residue(...)`, so `total_residue` was mathematically guaranteed to stay 0.0 regardless of precision/harm dynamics; (2) 671's `is_committed` check read a stale multi-rate candidate cache (`_committed_candidates`), not the actual commitment signal (`SelectionResult.committed`); (3) 671's sample filter pooled benefit ticks (which can never produce a residue delta) in with harm ticks, diluting the correlation sample; (4) a new `owned=` parameter sources "agent-caused" from the environment's `transition_type == "agent_caused_hazard"` ground truth. A new positive-control precondition (`residue_accumulates_under_committed_harm`) gates on residue actually moving before the C1/C2 read is trusted.

**Outcome:** FAIL. `non_degenerate: True`. Label: `precision_does_not_modulate_residue_responsibility_weight`.

**Readiness precondition:** `residue_accumulates_under_committed_harm` — measured 1.86 vs floor 1e-6 — **PASSED cleanly**, confirming the instrument fixes worked (residue genuinely accumulates now, unlike 671).

**Results (n=29 committed harm-events, single seed):**
- C1 `precision_residue_correlation > 0.15`: measured **0.0505** — FAIL
- C2 `high_precision_residue_ratio > 1.1`: measured **0.9214** — FAIL (below 1.0: high-precision commits carried *slightly less* residue than low-precision ones, not more)
- C3–C6 (sample size, world-model quality, harm-prediction variance, no fatal errors): all PASS

Confirmed non-dry via `check_dry_run_citations.py`.

## 2. This is a real, careful retest — but it has an asymmetric gap in its own positive-control logic

The driver added exactly one positive-control gate: residue must demonstrably move (fixing 671's degenerate failure mode). **It did not add the mirror-image gate on the independent variable — precision itself.** `precision_samples` are collected (`agent.e3.current_precision` at each committed step) and fed directly into the Pearson correlation and median-split ratio, but the driver never checks whether those 29 values have meaningful spread before trusting the correlation/ratio read. This matters because MECH-025's own documented V2 history (its only recorded evidence, cited directly in claims.yaml) is: *"Fundamental blocker: action-doing mode requires self-attribution... action_precision_lift = 0.0 across all seeds/conditions — E3 precision hardcoded, no dynamic channel."* That is the exact failure signature (a near-constant independent variable defeating a correlation test) the driver already fixed on the dependent-variable side for residue, but left unchecked on the independent-variable side for precision.

**Mitigating evidence:** ARC-016 (dynamic, E3-derived precision) is `stable` with real V3 confirmation (V3-EXQ-018b PASS: precision 718 in a stable env vs 426 in a perturbed env — genuine, substantial dynamic range). This makes "precision is still hardcoded" unlikely as a *global* substrate property. But ARC-016's evidence is cross-environment-condition variance, not within-a-single-eval-run variance across 29 committed steps in one seed — the specific quantity this correlation test actually needs to have spread. Whether precision varies enough *within this run* to give the C1/C2 test power is not directly checked or ruled out.

**MECH-025 itself (the direct prerequisite — "doing mode produces distinct internal signatures") has `evidence: None` in claims.yaml** — no recorded V3 confirmation at all, only the V2 FAIL cited above and a note that "V3 gate cleared (2026-03-28)... V3 action-doing mode experiments can now proceed" (permission to test, not confirmation the test would succeed).

## 3. Biological-reference note

MECH-025b's own registration notes are candid that this is **not** a pure neuroscience claim: precision modulation of motor control is grounded (Friston 2013 active inference; Wen & Haggard 2020 agency prediction error), but "the responsibility linkage — where high precision IMPLIES ethical accountability — is a philosophical bridge, not a neuroscience finding," explicitly mapped onto the legal/philosophical negligence-vs-deliberate-action distinction. No literature entry specifically addresses whether precision-at-commitment correlates with post-hoc moral/responsibility weighting in any biological or cognitive-science sense (the two literature hits found under similar search terms, `targeted_review_paper_fm4_precision_staleness` and `targeted_review_rem_precision_recalibration_timing`, are about unrelated precision-recalibration topics). Per this skill's own guidance, a formal/philosophical import with no biology lit backing should not be treated as fairly falsified by a single FAIL without first checking whether the test itself was fair.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | precondition cleared, but the independent variable's own adequacy was never checked |
| Biological reference | philosophical-bridge, no direct lit backing | precision modulation (MECH-025) is grounded; the responsibility-linkage half is explicitly a philosophical construct per the claim's own notes |
| Prerequisites | **unconfirmed** | MECH-025 (precision produces a distinct signature) has no recorded V3 evidence; only a V2 FAIL and a "gate cleared to test" note |
| Implementation | genuinely improved | 4 real instrument fixes over 671, well-documented and code-verified |
| Environment | n/a | |
| Measurement | **asymmetric positive-control gap** | residue-side gate added; no equivalent precision-variance gate added, despite this being the exact historical failure signature for this substrate |
| Integration | n/a | |
| Scale | **underpowered** | single seed, n=29 samples — thin for a Pearson correlation and a median-split ratio |

## 5. Learning extracted

1. When fixing a degenerate instrument defect on one side of a correlation test (here: residue), check whether the same defect class could exist on the other side (precision) before trusting the corrected read.
2. A prerequisite claim (MECH-025) being "gate cleared to test" is not the same as "confirmed operative" — claims.yaml's `evidence: None` on MECH-025 is a real gap worth closing before treating a downstream test's null result as decisive.
3. Single-seed correlational tests on philosophical-bridge claims (no direct biological literature) warrant a higher evidentiary bar before being read as claim pressure, given the skill's own guidance on formal-import divergence.

## 6. Routing (user-confirmed 2026-08-02)

**User confirmed:** treat as inconclusive pending a precision-variance positive control and more seeds — not yet claim pressure.

**Recommended `epistemic_category`:** `measurement_gap` (missing positive control on the independent variable, mirroring the one already added for the dependent variable).
**Recommended `evidence_direction`:** `non_contributory` (informative about instrumentation, not yet a fair test of MECH-025b).

**Routing: `/queue-experiment`** — low/medium priority `V3-EXQ-671b`, same design, adding: (a) a positive-control precondition on precision spread (e.g. `precision_samples` std or range must clear a floor, mirroring `residue_accumulates_under_committed_harm`), and (b) 3–5 seeds instead of 1, to give the correlation/ratio tests real statistical power. Consider also recording a direct V3 confirmation of MECH-025's own signature (or citing an existing one, if a session finds this was covered elsewhere) alongside this retest.

Re-derive brake: 1 prior autopsy for MECH-025b (`failure_autopsy_batch9_2026-06-12`), category `n/a (degenerate)`, not `substrate_ceiling`. This autopsy's own recommended category (`measurement_gap`) is also not `substrate_ceiling`. Does not fire.

Granularity-debt recurrence trigger: checked via `granularity_debt_cluster.py MECH-025b` — 1 prior target, `claim_alignment: intact (not tested)`, no target reads `weakened`. Does not fire.
