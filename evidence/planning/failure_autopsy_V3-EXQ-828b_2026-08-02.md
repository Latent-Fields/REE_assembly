# Failure Autopsy: V3-EXQ-828b (INV-091, cross-stream similarity band, dynamic-budget re-run)

**Generated:** 2026-08-02T10:14:48Z
**Run:** `v3_exq_828b_inv091_cross_stream_similarity_band_dynamic_budget_20260802T073924Z_v3`
**Queue ID:** V3-EXQ-828b
**Claim IDs:** INV-091
**Status:** confirmed
**Lineage:** V3-EXQ-827 → 827a → 828 → 828a → **828b**. Read alongside `failure_autopsy_V3-EXQ-828a_2026-08-01.md` (immediate predecessor, which recommended the dynamic-budget mechanism this run implements) and `failure_autopsy_batch-822a-826-817a-827_2026-07-26.md`.

## 1. Facts

**Design.** Six-arm ablation (intact, broadcast_off, mode_decorrelated, residue_off, rate_randomized, harm_collapse) — same six-arm design as 828/828a. The change from 828a: eval-phase budget is now determined by a **per-arm-per-seed dynamic pilot** (6 pilot episodes, 2.0x margin multiplier, 1.5x extra margin if the pilot itself is unreliable, 2848-step floor), implementing 828a's own autopsy recommendation ("a per-run dynamic pilot pass that measures actual tau_max before committing to a fixed eval-phase budget") rather than another static guess.

**Outcome:** FAIL. Label: `cross_stream_similarity_band_not_supported`.

- **C1** (at least one ablation moves similarity): PASS
- **C2** (peak-composite arm interior, beats both extremes by ≥0.15 margin): FAIL — peak-composite arm is `harm_collapse`, which is *also* the similarity-maximum arm (`sim_max_arm='harm_collapse'`) — i.e. the empirically best-composite-reward arm sits **at an extreme of the similarity axis**, not in the interior a "band" hypothesis predicts. `margin_vs_min=0.101`, `margin_vs_max=0.000` (comparing the arm to itself), `peak_is_interior=False`, `monotonic_direction='none'`.
- **Null validation:** `checked: false` — again.

Confirmed non-dry via `check_dry_run_citations.py`.

## 2. The C1/C2 read: a third corroborating data point, with a notably different specific pattern

828 found `residue_off` as best-composite (interior). 828a found `residue_off` again as best-composite, interior, with a razor-thin margin miss (0.148 vs 0.15 threshold). **828b finds `harm_collapse`** — a different arm — as best-composite, and this time it is *not* interior at all (it sits at the similarity extreme). All three runs share the same top-line verdict (the interior-band hypothesis is not supported by any of them), but the *specific arm* identified as best-composite has now varied across two of three runs (`residue_off` in 828/828a, `harm_collapse` in 828b). This run-to-run instability in which specific ablation "wins" is itself worth noting as corroborating evidence against a robust interior band: if a genuine, reproducible band structure existed, the winning arm should be more stable across independently-seeded runs of the same design.

## 3. This is the THIRD consecutive failed attempt to fix the same infrastructure gap

| Attempt | Mechanism | Result |
|---|---|---|
| 827/828 (original) | hardcoded 1500-step budget | undersized — surrogate never ran |
| 828a (IGW-20260730-192 fix) | static bump to 3600 steps (computed from 828's own observed 2848-step deficit + margin) | still ~4x short of the observed 14,648-step worst case |
| **828b (this run)** | dynamic per-arm-per-seed pilot (6 episodes, 2.0x margin, 2848-step floor) | **still refuses** — worst-case seed needs 138,600 steps (tau_max≈79 steps observed), vs the ~22,800–138,600-step range actually required across seeds |

The dynamic pilot is a genuinely more sophisticated fix than a static guess (828a's own recommendation, correctly implemented per its `dynamic_budget_policy` config: `mechanism: per_arm_per_seed_pilot`, `any_cap_hit: false` — meaning the pilot's own estimate, not a hard cap, determined the budget and was still insufficient). The tau_max estimate from a 6-episode pilot appears to systematically underestimate the true worst-case autocorrelation timescale by a wide, seed-dependent margin (observed range ~29–79+ steps from a short pilot, but the *actual* requirement implies a much longer true tau_max on at least one seed/stream). This is not a "pick a bigger number" problem anymore — a short pilot pass may be fundamentally unable to observe the slow-timescale behavior it needs to characterize, which is close to a sampling-paradox (you need a long run to correctly estimate how long a run you need).

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | C1/C2 correctly evaluated, consistent with 828/828a |
| Biological reference | not assessed here | unchanged from prior autopsies in this lineage |
| Prerequisites | present | shared warmed-up substrate, all arms ran correctly |
| Implementation | complete for C1/C2 design; genuinely improved for the null-validation mechanism (dynamic pilot, per 828a's own recommendation) | the improved mechanism still failed |
| Environment | inadequate for null-validation, for the third consecutive design | a short pilot may be structurally unable to characterize the slow-timescale tau_max it needs to bound |
| Measurement | surrogate correctly refuses rather than silently shortening blocks (preserved across all 3 attempts) | good failure mode, but the underlying goal (achieving null-validation within a bounded budget) may not be reachable at reasonable cost |
| Integration | n/a | |
| Scale | the required budget (up to ~138,600 steps on one seed) is now known to be large enough that "just run longer" is a real compute-cost decision, not a small tweak | |

## 5. Learning extracted

1. A short pilot pass to estimate a slow-timescale statistic (tau_max) can itself be systematically biased toward underestimation if the true autocorrelation timescale exceeds what the pilot can observe — this is a structural limitation of the dynamic-pilot approach, not an implementation bug in 828b's own pilot logic.
2. Three consecutive attempts (static-undersized, static-bumped, dynamic-pilot) at the same underlying infrastructure gap, each more sophisticated than the last, still failing, is itself diagnostic: the achievable-within-reasonable-budget null-validation for this specific design may not exist, or would require a budget large enough to warrant an explicit cost/benefit decision rather than another guess.
3. The run-to-run instability in which specific ablation arm "wins" the composite score (residue_off twice, harm_collapse once) is itself informative and worth surfacing as corroborating (not just neutral) evidence against a robust interior-band structure.

## 6. Routing (user-confirmed 2026-08-02)

**User confirmed:** stop attempting to fix null-validation for this design; rely on the ablation-contrast (C1/C2) alone, formalizing the existing 2026-07-29 governance precedent.

**Recommended `evidence_direction`:** `weakens` (confirmed, consistent with 828/828a — third independent corroborating data point).

**Routing for the C1/C2 result:** no further action needed — the ablation-contrast stands as sufficient evidence per standing precedent.

**Routing for the null-validation infrastructure gap:** **do not** queue a fourth attempt. Recommend governance formally close out further null-validation attempts for this specific design as **aleatoric (irreducible within a reasonable compute budget)**, per the CLAUDE.md work-graph debt vocabulary — three consecutive attempts of increasing sophistication have each failed by wide, seed-dependent margins (up to ~50x the achieved budget on one seed), and the underlying quantity (a short pilot's ability to bound a slow-timescale statistic) is structurally, not incidentally, hard to estimate cheaply. Recommend updating `INV091-NULL-VALIDATION-RUN-LENGTH`'s substrate_queue entry status to reflect this closure rather than leaving it open for a fourth guess-and-bump.

Re-derive brake: 0 prior `substrate_ceiling` autopsies for INV-091 in this cluster (827: `measurement_test_design_defect`; 827a/828/828a: `standard`) — does not fire. This autopsy's own recommended category (`standard`, consistent with the existing cluster) is also not `substrate_ceiling`.

Granularity-debt recurrence trigger: not applicable — this run corroborates the existing failure signature (interior-band hypothesis not supported), it does not introduce a new one.
