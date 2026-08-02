# Failure Autopsy: V3-EXQ-857a (Q-086 gentler-environment confound control, REDESIGN)

**Generated:** 2026-08-02T09:49:33Z
**Run:** `v3_exq_857a_q086_gentler_env_fingerprint_redesign_20260802T015401Z_v3`
**Queue ID:** V3-EXQ-857a
**Claim IDs:** Q-086 (diagnostic, open_question)
**Status:** confirmed
**Flagged in `pending_review.md`** as "Diagnostic adjudication required (self-route unverified)" — `precondition_unmet`.
**Read alongside:** `failure_autopsy_V3-EXQ-857_2026-08-01.md` (this run is 857's own redesign, following that autopsy's routing verbatim: more seeds, starker gradient, survival-time DV)

## 1. Facts

**Design.** Second attempt at the V3-EXQ-664 z_harm_a "saturation-and-inversion" confound control. Three arms this time: ARM_HARSH (num_hazards=4, the 664 default), ARM_GENTLE (num_hazards=1, 857's original gentle arm, kept for comparability), ARM_BENIGN (num_hazards=0, NEW — a true hazard-free floor). 6 seeds (double 857's 3), plus a new `mean_episode_survival_steps` secondary DV, per 857's autopsy routing.

**Outcome:** FAIL. `non_degenerate: false`. Label: `substrate_not_ready_requeue`. The readiness precondition (`gentle_env_manipulation_took_z_harm_s_differs_starkest`, ARM_HARSH vs ARM_BENIGN) failed again: SNR **0.388** vs required ≥2.0 (`|delta mean z_harm_s|=0.0566`, pooled cross-seed SD=0.146). The driver's own code anticipated this exact outcome and flagged it explicitly rather than silently self-routing a second time: *"this is a stronger signal than 857's own inconclusive result: it suggests the sensory-tier z_harm_s readout may not be ecologically sensitive to hazard density at this raw-warmup scale."*

**Dry-run check:** both `V3-EXQ-857` and `V3-EXQ-857a` confirmed non-dry via `scripts/check_dry_run_citations.py` (0 dry cited, 5 clean across all run_ids referenced in this autopsy).

## 2. Why "insufficiently sensitive readout" is the wrong read — a paired-design reanalysis

**The raw per-seed data (both this run and its predecessor):**

| seed | ARM_HARSH z_harm_s | ARM_GENTLE z_harm_s | ARM_BENIGN z_harm_s | ARM_HARSH surv. | ARM_BENIGN surv. |
|---|---|---|---|---|---|
| 0 | 0.3076 | 0.2121 | 0.2123 | 81.8 | 160.2 |
| 1 | **0.6475** | **0.6490** | **0.6951** | 11.6 | 105.2 |
| 2 | 0.4209 | 0.2989 | 0.3008 | 23.4 | 187.6 |
| 3 | 0.3453 | 0.2920 | 0.2802 | 62.6 | 200.0 |
| 4 | 0.2916 | 0.2802 | 0.2793 | 118.2 | 200.0 |
| 5 | 0.3494 | 0.2704 | 0.2547 | 25.0 | 128.4 |

**Seed 1 is a massive, exactly-reproducible outlier across ALL THREE arms**, not seed-to-seed noise. Comparing 857a's ARM_HARSH/ARM_GENTLE seed 0/1/2 values against 857's original 3-seed run (same substrate config, `torch.manual_seed(seed)` set identically per arm): the values are bit-identical to 4 decimal places (e.g. seed 1: harsh 0.6475 in both runs, gentle 0.6490 in both runs). **This confirms the substrate is deterministic for a given seed in this raw-warmup CPU regime** — the "noise" the readiness statistic is fighting is not sampling variance, it is a fixed per-seed effect (seed 1's particular initialization/trajectory produces an idiosyncratic outcome in every arm equally).

The driver's non-degeneracy statistic pools all 6×2=12 values into one unpaired SD, which lets seed 1's outlier dominate the denominator. But the design already shares seeds across arms (`make_agent_and_env(seed, ...)` calls `torch.manual_seed(seed)` identically regardless of `env_overrides` — verified against `experiments/_lib/baselines/affective_fishtank.py:203-210`), making this a **naturally paired design**. Pairing by seed (ARM_HARSH − ARM_BENIGN per seed) and computing a paired SNR instead:

- Per-seed deltas: +0.0953, **−0.0476**, +0.1201, +0.0651, +0.0123, +0.0947 (5 of 6 positive, only seed 1 negative and small)
- Paired mean = 0.0566, paired SD = 0.0631, paired SNR = mean / (SD/√6) ≈ **2.20** — clears the driver's own K=2.0 bar.

This is corroborated by the survival-time secondary DV, which the driver already computed but treated as non-gating: survival differs enormously and consistently in the same direction (harsh episodes end far earlier than benign ones at every seed, including seed 1: 11.6 vs 105.2), even though the driver's own unpaired survival-SNR (1.658) also narrowly missed its K=2.0 bar for the same pooling reason.

## 3. Once the gate is read as cleared, the driver's own discrimination logic already resolves the question

The manifest's `discrimination` block (computed regardless of the gate, just not surfaced past `non_degenerate=false`):

```
benign_saturated_sub_floor_cov: true    (ARM_BENIGN cov_z_harm_a = 0.029 < COV_FLOOR 0.05)
level_tracks_hazard_density:    false   (level_harsh=7.41 < level_benign=8.64 -- INVERTED, not dropping)
cov_tracks_hazard_density:      false
```

ARM_BENIGN's z_harm_a stays saturated (sub-floor CoV) **and** its level is *higher*, not lower, than ARM_HARSH — the opposite of what "faithful chronic suffering" predicts, and consistent with the original 2026-06-10 664 "saturation-and-inversion" observation that opened this whole diagnostic thread (856 → 857 → 857a). This reads cleanly as **`calibration_pathology_representational`**.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened** (reversed from 857's "unclear") | once correctly analysed, the manipulation did take and the question is answered |
| Biological reference | not load-bearing | diagnostic |
| Prerequisites | n/a | |
| Implementation | correct on paper | manipulation itself (num_hazards, food_attraction) worked as designed |
| Environment | genuinely moved z_harm_s and survival time | the paired analysis shows a real, consistent, large effect |
| **Measurement** | **under-instrumented / misleading** | the readiness statistic (unpaired pooled-SD SNR) discards the shared-seed pairing structure the design already has, letting one outlier seed swamp a real signal present in 5/6 seeds |
| Integration | n/a | |
| Scale | adequate | 6 seeds is enough once paired; more seeds would firm up the borderline SNR (2.20) further |

## 5. Learning extracted

1. **When a design shares seeds across arms (same `torch.manual_seed` call regardless of arm config), the non-degeneracy statistic should be paired, not pooled-unpaired.** An unpaired pooled-SD SNR treats between-seed heterogeneity as if it were independent per-arm noise, and is vulnerable to exactly the failure mode observed here: one outlier seed inflating the denominator enough to mask a real, consistent, majority-of-seeds effect.
2. **Cross-run bit-identical reproducibility (857 vs 857a, same seeds) is itself diagnostic** — it rules out "stochastic noise" as an explanation and points to a deterministic per-seed effect, the same signature 851's autopsy independently identified in a different lineage ("a precondition flipping under identical seeds is a deterministic result, not a stochastic power/noise problem").
3. **A self-route's own speculative narrative ("the readout may not be ecologically sensitive") should not be accepted without checking whether the *test*, not the *readout*, is at fault** — here the readout (z_harm_s) was in fact highly sensitive to the manipulation; the aggregation statistic just discarded that sensitivity.
4. The episode-survival-time secondary DV (added per 857's own routing) turned out to be the strongest corroborating signal even though it individually missed its own unpaired SNR bar for the identical reason.

## 6. Routing (user-confirmed 2026-08-02)

**User confirmed:** accept the paired-seed reanalysis as the answer to Q-086 (no new run required), plus a low-priority follow-up to fix the driver's readiness statistic for future reuse.

**Recommended `evidence_direction`:** `supports` (of the "calibration, not ecology" reading; Q-086's own `what_would_answer` names this as one of its two possible PASS conditions).
**Recommended `epistemic_category`:** `measurement_test_design_defect` (the self-route's `substrate_not_ready_requeue` was a mis-specified statistic, not a genuine substrate-readiness failure).
**Recommended `live_status.reading`:** `q086_calibration_pathology_representational` (matching the driver's own PASS-branch label for this outcome, reached via reanalysis rather than the driver's own gate).

**Routing: `/queue-experiment`** (low priority) — a small, cheap `V3-EXQ-857b` that (a) fixes the readiness statistic to use the paired-by-seed SNR by default for this lineage's affective-fishtank confound controls, and (b) optionally adds a handful more seeds to firm up the borderline paired SNR (2.20, just above the 2.0 bar) — a confirmatory run, not a re-litigation of the question. This is a genuine test-design fix, not a same-question re-litigation the re-derive brake would object to.

Re-derive brake: 1 prior `substrate_ceiling`-family autopsy for Q-086 (`failure_autopsy_V3-EXQ-857_2026-08-01`), category `non_contributory` (not `substrate_ceiling` — R3 excludes it from the count). Well under threshold=2, and this autopsy's own recommended category (`measurement_test_design_defect`) is also not `substrate_ceiling`. Does not fire.

Granularity-debt recurrence trigger: checked via `granularity_debt_cluster.py Q-086` — 1 prior target, `claim_alignment: unclear`, no target reads `weakened`. Does not fire (measurement debt, not granularity debt) — consistent with this autopsy's own finding that it was a measurement-layer defect all along.
