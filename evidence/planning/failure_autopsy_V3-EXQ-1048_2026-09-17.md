# Failure autopsy -- V3-EXQ-1048 (MECH-017)

Status: confirmed (user gate 2026-09-17)
Generated: 2026-09-17T17:57:22Z
Run: `v3_exq_1048_mech017_reality_consolidation_replay_vs_budget_matched_20260917T102244Z_v3`
Purpose: evidence | Outcome: FAIL | Direction: mixed (STANDS as stamped)

## 1. Facts

Dry-run gate: CLEAN. Recording: `validate_recording.py` OK, 0 always-core gaps.
substrate_hash `fa1ae059...`, machine `ree-cloud-2`, 5 seeds [42,123,456,2026,45],
elapsed 406.1 s. `degenerate_metrics` empty, `non_degenerate` true.
All **12** readiness preconditions met.

Three arms, identical agent construction: **A** whole-life-buffer offline replay,
**B** budget-matched recent-window (last 90 steps), **C** no extra training.
Budget matched exactly: 192 extra gradient steps in every A and B cell,
`gradient_budget_delta_a_minus_b` = 0.0. C gets 0.

| criterion | load-bearing | threshold | measured | result |
|---|---|---|---|---|
| C1 replay beats budget-matched on EARLY probes | YES | 4 seeds | 5 | PASS |
| C2 no cost on LATE probes | YES | 4 seeds | 1 | **FAIL** |
| C3 early effect size clears floor | YES | > 0.05 | 0.4542 | PASS |

`combination_rule`: PASS iff ALL of C1, C2, C3 (plain AND). `c1 and c3 and not c2` takes the
dedicated trade-off branch -> label `replay_counters_forgetting_at_a_recency_cost`,
direction `mixed`.

**Which criterion failed:** C2, a discrimination criterion (between-arm, second probe stratum).
The design's two negative controls -- ARM_C via `forgetting_present_in_control` (2.4854 vs a
1.1 floor) and `manipulation_reaches_dv` (5/5) -- are readiness preconditions and both passed.

## 2. The central question, and a draft claim WITHDRAWN

This autopsy's first draft argued C2 was mis-specified: that it compared A against a stratum
specialist instead of against ARM_C, so the 41% late deficit was a foregone benefit under a
fixed budget rather than damage. **That argument is withdrawn.** Recorded rather than deleted.

MECH-017's own `what_would_answer`, verbatim:

> CONFIRMING if A < B on the EARLY-state probes (replay counters forgetting) with **A <= B on
> late-state probes (no cost to recency)**, and calibration improves in A, sign-consistent
> across >=3 seeds.

The late-probe comparator is pre-registered **in the claim itself, against B**. ARM_C appears
in the claim only in the arm list and in NON-DEGENERACY PRECONDITION (i) as a readiness control
-- which is exactly and only how the manifest uses it. **C2 transcribes the claim's own
confirming clause.** Proposing to swap the comparator after that comparator failed is a
post-hoc decision-rule change on the axis that failed.

It would not even have rescued C2: recomputed, `late_A <= 1.1 * late_C` holds on
{42, 123, 456} = **3 of 5** against a threshold of 4 -- still a FAIL. Flipping it needs a second
undisclosed relaxation (sign-consistency 4 -> 3).

And "a wash" was wrong. Paired mean(A - C) on late probes is **+9.17e-06 (A 9.63% worse)**,
median +2.0%, and it **replicates on the untouched second DV** (E2 self-forward late, A 11.9%
worse) -- 6 of 10 late cells have A worse than C.

## 3. What the run actually establishes

| late probe, per seed | 42 | 123 | 456 | 2026 | 45 |
|---|---|---|---|---|---|
| (A/B) - 1 | +13.62% | +41.86% | +9.25% | +95.13% | +47.06% |

**A > B on late probes on 5 of 5 seeds**, mean +41.4%, replicated on the second DV.
MECH-017's FALSIFYING clause reads: "A > B (replaying stale traces DEGRADES the model against
the online comparator -- the anti-prediction, a genuine weakening)" -- stated **without a probe
stratum**. It is triggered.

Simultaneously, on early probes A < B on 5 of 5, mean relative gain **0.4542 against a 0.05
floor (9.1x)**, with A < B < C monotone on every seed.

**The claim bundles two predictions and this run separates them cleanly:** "replay counters
forgetting" is SUPPORTED; "at no cost to recency" is WEAKENED. `mixed` is exactly right.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | MIXED, faithfully | implements the claim's grid verbatim; one leg met, one falsified |
| Biological reference | clear | hippocampal-neocortical replay; translation faithful in kind, no load-bearing divergence |
| Prerequisites | present | 12/12 preconditions |
| Implementation | complete | budget matched exactly; consolidator updated E1 and E2 96x per cell |
| Environment | adequate | for the question as posed |
| Measurement | **incomplete against the claim** | 2 of 3 named readouts never measured (below) |
| Integration | coupled | -- |
| Scale | adequate | 5/5 sign-consistent on both DVs |

**Failure-location summary (GOV-FAILLOC-1): MIXED, not chargeable to REE alone.** Measurement
adequacy is not established (section 5), so REE FAILED is unavailable by the table's own
threshold.

## 5. Limits, stated rather than buried

- **E2 `world_forward` never measured** -- declared in the driver docstring; no trainer exists
  in `ree_core`.
- **`precision_error_corr` absent from driver and manifest entirely** -- the claim's third named
  readout. So the CONFIRMING conjunction was never fully evaluable.
- The run calls the consolidator **directly, outside any sleep cycle** (declared, driver:52-61).
- `LATE_TOL = 0.10` is an unanchored pre-registered constant -- no measured noise floor, no
  replicates, no variance estimate anywhere in driver or manifest. **Not load-bearing here:**
  C2 would need a tolerance >= 0.4706 to flip, and the A > B sign is consistent 5/5 on both DVs.
  Recorded as hygiene.
- 3 of the 5 seeds (42, 123, 45) were run at full scale before the recorded run with matching
  recorded directions, disclosed in the driver docstring and the queue note; the pre-run cells
  wrote no manifest.

## 6. Claim-granularity flag -- RECORDED, NOT ROUTED

MECH-017 conjoins two separable predictions and this run supports one at 9x its floor while
triggering the claim's own falsifier on the other, 5/5, on two independent DVs. That is a clean
structural split, not tuning noise.

**Not routed to `/claim-synthesis`.** The GOV-GRAN-1 recurrence trigger does not fire:
`granularity_debt_cluster.py MECH-017` reports **0 tagging targets** -- this is the claim's
first autopsy. Surfaced here so a second circling run makes the split actionable rather than
starting the count from scratch. (User decision, Step 8 gate 2026-09-17: record, do not route.)

## 7. Re-derive brake

**Does not fire.** MECH-017 literal count 0; zero prior autopsy targets. Direction `mixed` and
category `standard` also fail the R1-R3 first gate independently.

## 8. Step 7b / 7c

- **7b:** 0 fires. C5 `inapplicable`.
- **7c: CONTESTED.** Model `claude-opus-5` -- the SESSION model, **not** cross-model
  (`claude-fable-5-1` returned HTTP 429 monthly spend limit; re-spawned once per Step 7c).
  Same-model pass: shares the drafter's priors. Both load-bearing findings accepted in full and
  independently re-verified (section 2). The pass also caught a fact-pack error: the run's
  machine is `ree-cloud-2`, not `ree-worker-1` -- confirmed against the manifest.

## 9. Routing

`queue-experiment`, **new question and new EXQ number** -- is the recency deficit INTRINSIC to
replay, or an artefact of REALLOCATING a fixed budget? That needs an arm with ADDITIONAL rather
than reallocated budget. It is explicitly **not** a re-specification of C2, whose comparator is
the claim's own.

No substrate entry: `action: none`. The substrate performed as designed.

The `-> epistemic_category: standard` disposition (MECH-017 currently carries no
`epistemic_category` field at all) is in the companion `.json`. `/governance` applies it.
