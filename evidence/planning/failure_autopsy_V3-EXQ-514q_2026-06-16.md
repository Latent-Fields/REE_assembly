# Failure Autopsy — V3-EXQ-514q (MECH-229 drive-coupled wanting/liking)

- **Generated:** 2026-06-16T19:28:56Z
- **Scope:** single (4th autopsy on the MECH-229 / 514 lineage)
- **Status:** confirmed (user-adjudicated 2026-06-16)
- **Run:** `v3_exq_514q_sd049_phase2_mech229_drive_coupled_wanting_liking_20260616T020619Z_v3`
- **Verdict:** the self-stamped `weakens` is **NOT genuine → `non_contributory`**; `substrate_ceiling`; MECH-229 core untouched. Route to `/queue-experiment` (514r disambiguator) + `/claim-synthesis` (split MECH-229).

## 1. Facts (no interpretation)

The load-bearing criterion `C_WL_DRIVE_coupled_dissociation` is `mean(WL_drive − WL_nodrive) ≥ max(1.0·pstdev(delta), 0.15)`. Observed:

- `mean_delta = 0.0`, `sd_delta = 0.0`, per-seed delta `[0.0, 0.0, 0.0, 0.0, 0.0]` → fails the 0.15 floor → self-stamped `weakens`, label `drive_delta_below_effect_size_genuine_weakens_run_offarm_overshoot`.
- The zero is **exact**: `mean_wl_drive == mean_wl_nodrive == 0.7021327829377364` (16 sig figs). Per seed, `object_bound_wl_dissoc_fraction == wl_nodrive_dissoc_fraction` identically (e.g. seed 42: 0.6667/0.6667; seed 43: 0.8235/0.8235).
- **`drive_spread_max ≈ 0.0055–0.0085` on every seed.** The bank held 3 distinct token *types* (`distinct_tokens_max = 3`, `run_bank_populated = true`), but the per-axis *drive* across them spans only ~0.006.
- Readiness "passed": `pc_separation_frac = 1.0` (a *constructed* positive-control bank with large drive separation flips the argmax), `run_bank_populated_frac = 1.0`, per-seed `drive_spread_max > DRIVE_SPREAD_FLOOR = 1e-3`. Guard 5/6 seeds; n=78 scored WL steps.
- `most_wanted = argmax_k base_value[k]·(1 + κ·per_axis_drive[k])`.

**Failed criterion class:** discrimination.

## 2. The mechanism of the zero

`wl_readiness_met = pc_ok AND run_populated_ok` (script line 673) verifies that the machinery *can* respond to drive (the constructed control separates) and that *some* spread exists (>1e-3). It never verifies that the **in-run** spread (~0.006) is large enough to flip an object-score-dominated argmax. With `κ·0.006` swamped by cross-object `base_value` (liking) differences, the drive-favoured and drive-uniform argmax pick the **same** token on every scored step → delta is structurally 0.0. This is the "off-arm overshoot" gap named in the label: capability was proven (positive control), in-run expressibility was not, and the overshoot arm that would settle it was never run.

## 3. Claim-layer map

MECH-229 (`provisional`, `implementation_phase: v3`, `pending_retest_after_substrate: true`, `epistemic_category: standard`) bundles two sub-mechanisms:

- **(a) wanting ≠ liking** (object-bound dissociation) — **ESTABLISHED**: V3-EXQ-514o PASSed at 0.80, which lifted MECH-229 `substrate_ceiling → standard` / `confirmed_established`. 514q's `object_bound` fraction is 0.70, consistent.
- **(b) wanting is drive-state-MODULATED** (the drive-coupling delta) — the **only** thing 514q tested, and the only thing that failed.

The FAIL bears on (b) alone. It must not be allowed to weaken (a).

## 4. Biological-reference triage

Closest mechanism: **incentive salience** — drive/state-modulated cue attraction (Berridge 2006; Smith/Berridge/Aldridge 2011; DiFeliceantonio/Berridge 2016 — the `targeted_review_connectome_mech_347` entries written *this same session*). Drive modulation is the biologically load-bearing part: hunger amplifies cue-triggered wanting. Not a formal-definition import.

The divergence is **environmental/substrate, not conceptual**: the V3 P2-foraging ecology produces near-flat per-axis homeostatic drive (spread ~0.006), so the drive-coupling cannot express. This matches a known-dependency-absent signature (no differential depletion pressure), which is precisely the script's own pre-registered "V4-1 multi-agent-ecology dependency" off-ramp — a discovered prerequisite, not a falsification.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | core (a) established by 514o; only drive-coupling (b) untested-fairly |
| Biological reference | clear | incentive salience is drive-modulated; near-flat drive = missing differential-depletion dependency |
| Prerequisites | missing | env does not generate argmax-relevant per-axis drive spread |
| Implementation | partial | `most_wanted` responds to drive (control flips); κ·0.006 sub-threshold vs base_value |
| Environment | too sparse | CausalGridWorldV2 P2 → drive_spread ~0.006 |
| Measurement | misleading | readiness gate green-lit a vacuous comparison (spread>1e-3, not argmax-relevant); no overshoot control |
| Integration | coupled | drive channel reaches `most_wanted` |
| Scale | adequate | 6 seeds, 78 scored steps, 30 eval episodes |

**Recommended `epistemic_category`: `substrate_ceiling`** (environment-adequacy; drive-coupling leg).

## 6. Lineage (granularity-debt recurrence — 4th autopsy)

| Autopsy | Signature | Routing |
|---|---|---|
| 514l (06-03) | foraging-competence prerequisite | substrate_ceiling / implement-substrate |
| 514m (06-11) | disabled VALENCE write paths → vacuous C_WL=0.0 | test-design / queue-experiment |
| 514p (06-15) | raw-fraction criterion confounded by (N−1)/N baseline | test-design / queue-experiment |
| **514q (06-16)** | **sub-threshold drive magnitude (~0.006); criterion now fixed** | substrate_ceiling / queue-experiment + claim-synthesis |

Each autopsy fixed the prior test-design defect and surfaced the next layer; the core (a) was established at 514o in parallel. The recurrence *is* the granularity-debt signal: MECH-229 is coarse — it bundles an established dissociation with a substrate-blocked drive-coupling leg the claim does not separately name.

## 7. Learning extracted

1. A readiness gate that checks "positive control separates" + "some spread >1e-3" is insufficient — it must assert the **in-run signal magnitude is in the decision-moving regime** (argmax-relevant drive spread vs object `base_value`), else a structurally-vacuous zero delta is mis-stamped a genuine weakens. The constructed control proves *capability*, not *in-run expressibility*; an overshoot arm is the missing control.
2. MECH-229 separates into (a) wanting ≠ liking (established) and (b) drive-modulated wanting (substrate-blocked on differential per-axis depletion).
3. V3 P2 foraging produces near-flat per-axis drive (~0.006); drive-state-dependent mechanisms cannot express until the env generates differential depletion (the pre-registered V4-1 dependency).
4. Fourth autopsy on one target with a distinct signature each time = granularity debt.

## 8. Routing (user-confirmed 2026-06-16)

- **514q → `non_contributory`** (scoring-excluded), `substrate_ceiling`, `pending_retest_after_substrate: true`. MECH-229 status **unchanged** this cycle; core dissociation unaffected; `narrow_supports_flag: true` (the remaining MECH-229 support is the single 514o object-bound pathway).
- **`/queue-experiment` → 514r** (the pre-registered disambiguator): (i) **n=5 OVERSHOOT arm** (artificially large `per_axis_drive` — *must* flip `most_wanted`; if it does, the bottleneck is drive magnitude/environment; if it does *not* flip even at overshoot, *that* is the genuine weakens), (ii) **OFF/bank-disabled control** (wanting==liking floor), (iii) **recalibrated readiness gate** asserting argmax-relevant in-run drive spread (not merely >1e-3).
- **Substrate routing:** `amend` SD-049-PHASE-2 with the 514q failure record (env differential-depletion / κ-scaling gap; priority 2).
- **`/claim-synthesis`** (secondary): split MECH-229 into the established wanting≠liking dissociation and a distinct drive-coupled / state-modulated wanting child, proposal-first and lit-grounded (the MECH-347 incentive-salience entries apply directly).

## Draft `evidence_quality_note` for governance

> 2026-06-16 (failure_autopsy_V3-EXQ-514q, confirmed): the self-stamped MECH-229 weakens is reclassified non_contributory and scoring-excluded. C_WL_DRIVE = mean(WL_drive − WL_nodrive) returned exactly 0.0 on all 5 guard-passing seeds (WL_drive==WL_nodrive byte-identical, 0.7021) because the in-run per-axis drive spread (~0.0055–0.0085) is far below the magnitude that could flip an object-score-dominated most_wanted argmax. The readiness gate verified the machinery can separate (constructed positive control 1.0) and spread>1e-3, but NOT that the in-run spread is argmax-relevant, and no overshoot control was run — so a zero delta cannot be read as 'drive does not carve wanting' vs 'drive never varied enough to carve'. MECH-229's core wanting≠liking dissociation is UNAFFECTED (established by V3-EXQ-514o PASS 0.80; 514q object_bound 0.70 consistent). The drive-coupling sub-leg is substrate_ceiling (P2 foraging produces near-flat per-axis drive). pending_retest_after_substrate stays true; MECH-229 status unchanged. Disambiguator queued: V3-EXQ-514r (overshoot + OFF control + recalibrated readiness). Granularity-debt: routed to /claim-synthesis to split the established dissociation from the substrate-blocked drive-coupling leg.
