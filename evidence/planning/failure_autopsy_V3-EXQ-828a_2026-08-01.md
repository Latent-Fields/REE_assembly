# Failure Autopsy: V3-EXQ-828a (INV-091 cross-stream similarity band, null-validated re-run)

**Generated:** 2026-08-01T12:54:47Z
**Run:** `v3_exq_828a_inv091_cross_stream_similarity_band_null_validated_20260801T073417Z_v3`
**Queue ID:** V3-EXQ-828a
**Claim IDs:** INV-091
**Status:** confirmed
**Successor of:** V3-EXQ-828 (`null_validation_successor_of`) · **Complements:** V3-EXQ-827a, V3-EXQ-828

## 1. Facts

**Design.** Byte-for-byte identical six-arm ablation design to V3-EXQ-828 (intact, broadcast_off, mode_decorrelated, residue_off, rate_randomized, harm_collapse). The **only** change: eval-phase budget raised from 828's 1500 steps to 3600 steps (`INV091_EVAL_EPISODES=24`), via the `INV091-NULL-VALIDATION-RUN-LENGTH` substrate fix (IGW-20260730-192), specifically to let the Q-081 surrogate null-validation check finally run (it had failed to run in 827/827a/828, all undersized).

**Outcome:** FAIL. `non_degenerate: true`. Label: `cross_stream_similarity_band_not_supported`.

**Criteria:**
- C1 (non-degeneracy, at least one ablation moves similarity): **PASS**
- C2 (peak-composite arm interior AND beats both extremes by ≥0.15 margin): **FAIL** — peak arm `residue_off` is interior, `margin_vs_min=0.232`, `margin_vs_max=0.148` (just **0.002 short** of the 0.15 threshold), `monotonic_direction='none'`.

**Null validation:** `checked: false` — **again**. The surrogate refused to run: *"the slowest stream needs blocks of at least 761–1831 steps (2x tau_max) but only 761–2018 steps were supplied... need at least 6088-14648 steps."* The worst-case requirement (14,648 steps) is roughly **4x** what the 3600-step budget supplied, and roughly **5x** the 2848-step deficit the IGW-20260730-192 fix was sized against.

## 2. Claim-layer mapping

INV-091 (candidate, `epistemic_category: standard`). Per claims.yaml's existing evidence_quality_note, 827 (non_contributory, confound), 827a (non_contributory, clean FAIL after fixing the confound), 828 (**weakens** — intact does not distinguish itself, residue_off has best composite reward). Governance already established (2026-07-29) that the null-validation gap does not block the weakens verdict for this cluster — "the ablation-contrast is treated as the sufficient discriminator... standing design note, not a blocker."

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | C1/C2 correctly evaluated |
| Biological reference | not assessed here | unchanged from 827/827a/828 |
| Prerequisites | present | shared warmed-up substrate, all arms ran correctly |
| Implementation | complete | design unchanged and correctly executed |
| Environment | adequate for C1/C2, **inadequate for this run's own null-validation purpose** | run length still ~4x short of the worst-case requirement |
| Measurement | the surrogate correctly REFUSED rather than silently shortening blocks | good failure mode, but the intended upgrade wasn't achieved |
| Integration | n/a | |
| Scale | the fix needs a structural change, not another static guess | tau_max is empirically variable per seed/run |

## 4. Why this is a recurring infrastructure defect, not a new claim finding

This is the **second consecutive miscalibration** of the same run-length estimate:
1. 827/828's original hardcoded budget (1500 steps) was undersized — the first diagnosed gap.
2. The IGW-20260730-192 fix computed "2848-step worst-case deficit + 26% margin = 3600 steps" **from V3-EXQ-828's own shortfall message** — but 828a's actual worst-case seed/stream needed 14,648 steps, ~5x that deficit estimate.

The pattern suggests tau_max (the autocorrelation timescale the block length must exceed) is genuinely variable across seeds/runs — a margin computed from one run's observed worst case does not reliably bound a different run's. Bumping the number a third time risks a third failure of the same kind.

## 5. The C1/C2 verdict stands independently

Per standing governance precedent for this cluster (2026-07-29), the missing null-validation does not block the weakens verdict — the ablation-contrast is the accepted discriminator on its own terms. This run's C1/C2 result (peak interior, margin_vs_max just 0.002 short of threshold) is informationally consistent with 828's own already-scored weakens and does not retract or supersede it — it is a fresh, higher-seed-count corroborating data point at the same read.

Note the margin: 0.148 vs a 0.15 threshold is razor-thin — exactly the kind of result where a working null validation would matter most for distinguishing genuine structure from measurement noise, which is precisely why the recurring null-validation gap deserves a real fix rather than continued acceptance as a standing note.

## 6. Learning extracted

1. A static run-length margin computed from one run's worst case does not generalize — this is now confirmed twice.
2. The surrogate's refuse-rather-than-silently-shorten behavior is correct and should be preserved in any fix.
3. The C1/C2 ablation-contrast reading remains valid and informative independent of the null-validation gap, per standing precedent.
4. The razor-thin C2 margin (0.148 vs 0.15) is a strong argument for actually fixing the null-validation infrastructure rather than accepting the gap indefinitely.

## 7. Routing

**Evidence direction: `weakens`** (confirmed, consistent with 828).

**Routing: `/implement-substrate`** — amend the existing `INV091-NULL-VALIDATION-RUN-LENGTH` substrate_queue.json entry (not a third `/queue-experiment` guess-and-bump). Recommend either a much larger static margin (3–5x headroom over the newly observed 14,648-step worst case) or, better, a per-run dynamic pilot pass that measures actual tau_max before committing to a fixed eval-phase budget. `pending_retest_after_substrate: true`.

Re-derive brake: 0 prior `substrate_ceiling` autopsies for INV-091 (this cluster's category is `standard`, not `substrate_ceiling`) — does not fire. Granularity-debt trigger: not checked separately here — this run does not introduce a new failure signature relative to 828, it corroborates the existing one.
