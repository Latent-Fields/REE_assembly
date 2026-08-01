# Failure Autopsy: V3-EXQ-859 (ARC-062 lateral-PFC route MECH-448/449 ablation, short-budget diagnostic)

**Generated:** 2026-08-01T18:17:37Z
**Run:** `v3_exq_859_arc062_lateral_pfc_route_mech448_449_ablation_20260801T151524Z_v3`
**Queue ID:** V3-EXQ-859
**Claim IDs:** none (by design)
**Status:** confirmed
**Read alongside:** `failure_autopsy_V3-EXQ-851_2026-08-01.md` (the finding this diagnostic was built to isolate)
**Blocks:** V3-EXQ-858 (ARC-062 GOV-FANOUT-1 Leg P-B), currently suspended pending this result

## 1. Facts

**Design.** Per the chip commissioned from V3-EXQ-851's autopsy: a cheap, short-budget (~45min) 2-arm comparison at V3-EXQ-851's exact seeds (42/43/44), varying **only** `modulatory_channel_route_source` (`'lateral_pfc'` vs `'none'`), tracking **only** MECH-448 (`f_eligibility_demotion_active_frac` + mean excluded_count) and MECH-449 (`go_nogo_active_frac` + mean suppressions) engagement — not the full committed-class-entropy falsifier.

**Outcome:** PASS (readiness). `evidence_direction: non_contributory`. Label: `mixed_partial_result_needs_full_replication`.

**Readiness:** `p2_fresh_select_sample_adequate_both_arms` — 220 vs 100 floor, passed.

**Result:**
| | MECH-448 live seeds | MECH-449 live seeds |
|---|---|---|
| ARM_LPFC (`lateral_pfc`) | 3/3 (majority) | 0/3 |
| ARM_NONE (`none`) | 3/3 (majority) | 0/3 |

`criteria_non_degenerate`: `mech448_ablation_discriminates: false`, `mech449_ablation_discriminates: false` — **neither mechanism's engagement differs by route_source at all.**

## 2. Why this doesn't reproduce V3-EXQ-851's finding — and why that's informative, not contradictory

V3-EXQ-851 (the full ~7.7-hour design, same seeds) found MECH-448 completely **dead** (measured 0.0) under `lateral_pfc` routing, versus robustly **live** (17.76) under `cand_world_summary` in the matched-stack template V3-EXQ-654j. This short probe finds MECH-448 **alive in both arms** — it does not reproduce 851's collapse at all, under either route_source value.

Two readings are live, and this run does not distinguish between them:

- **(a) Route_source has no causal effect at all**, and 851's own diagnosis (route_source → MECH-448/449 suppression) has some other explanation entirely.
- **(b) Route_source's suppressive effect is training-duration-dependent** — it accumulates or emerges only over a longer run, and a ~45-minute probe simply doesn't run long enough to show it.

A cheap short-budget scale-down is not automatically a safe cost-reduction for reproducing a *training-dynamics-dependent* effect — this is exactly that failure mode, if reading (b) is correct.

**Separately:** MECH-449 is dead in BOTH arms here, matching its deadness in 851. This suggests MECH-449's suppression is **not** route_source-dependent at all — it may simply need more training exposure to engage, a distinct question from MECH-448's apparently route-dependent collapse in the full run.

## 3. Claim-layer mapping

`claim_ids=[]` by design — this run exists purely to route GOV-FANOUT-1 Leg P-A follow-on work and the suspended V3-EXQ-858 allocation, not to score MECH-309/ARC-062 evidence.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | pure routing diagnostic |
| Biological reference | not load-bearing | |
| Prerequisites | present | sample-adequacy precondition passed |
| Implementation | correct, built to spec | same seeds, short budget as commissioned |
| Environment | same family as 851/654j | |
| Measurement | clean but negative | neither mechanism discriminates by route_source |
| Integration | **the short-budget scale-down itself may be the problem** | doesn't reproduce 851's full-length finding |
| Scale | insufficient to answer the causal question | can't distinguish "no effect" from "duration-dependent effect" |

## 5. What should happen to V3-EXQ-858

V3-EXQ-858 (ARC-062 Leg P-B, F-dominance) presupposes MECH-448/449 are active under the `lateral_pfc`-routed matched-stack config — the exact presupposition 851 called into question. This run neither confirms nor refutes that presupposition (it's inconclusive), so **V3-EXQ-858 should remain suspended** rather than being unblocked on an ambiguous result.

## 6. Learning extracted

1. A cheap short-budget probe built to isolate a causal factor from a full-length run can fail to reproduce the original finding entirely — informative, but not evidence the original finding was spurious, if the effect is training-duration-dependent.
2. MECH-449's deadness appears route_source-independent (dead in both arms here and in 851) — a distinct question from MECH-448's route-dependent-looking collapse, worth separating in any follow-up design.
3. The self-route's own honest "needs full replication" label is well-calibrated here — this autopsy concurs rather than pushing toward a stronger reading than the data supports.

## 7. Routing

**Evidence direction: `non_contributory`** (confirmed, correct — claim_ids=[] by design).

**Routing: `/queue-experiment`** — a full-training-budget version of this same ablation (lateral_pfc vs none, same seeds, ~7.7h duration matching 851) is the only design that can actually discriminate reading (a) from (b). Flagging the compute-cost tradeoff for governance to weigh, given V3-EXQ-858 is already sitting suspended on exactly this question.

Re-derive brake: n/a (claim_ids=[], no claim to brake against).
