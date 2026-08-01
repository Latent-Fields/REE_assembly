# Failure Autopsy: V3-EXQ-847 (ARC-062 GOV-FANOUT-1 Leg P-D, H4 context-modeswitch divergence)

**Generated:** 2026-08-01T21:02:08Z
**Run:** `v3_exq_847_arc062_pd_context_modeswitch_committed_class_divergence_20260801T191410Z_v3`
**Queue ID:** V3-EXQ-847
**Claim IDs:** none (`claim_ids=[]`, diagnostic by design — matches sibling V3-EXQ-859's precedent)
**Status:** confirmed (interactive gate completed with user)
**Read alongside:** `failure_autopsy_V3-EXQ-851_2026-08-01.md` (Leg P-A, the finding this portfolio traces back to), `failure_autopsy_V3-EXQ-859_2026-08-01.md` (Leg P-A follow-up, MECH-448/449 short-budget ablation)
**Machine/elapsed:** ree-worker-3, 41988.9s (~11.7h)

## 1. Facts

**Design.** GOV-FANOUT-1 portfolio Leg P-D (H4: measurement aliasing). Tests whether the 654-lineage's pooled-marginal committed-class-entropy DV is blind to a narrower, context-CONDITIONED effect: does the CRF-differentiated rule_state shift WHICH class is committed differently by context (reef vs. open) while leaving the pooled marginal roughly unchanged? Matched stack identical to V3-EXQ-654j (`modulatory_channel_route_source='cand_world_summary'`, NOT `lateral_pfc` — the P-A erratum this leg explicitly does not depend on), MECH-448 (rank-preserving F->eligibility demotion) and MECH-449 (Go/No-Go) both ARMED on both arms, sole swept variable `use_candidate_rule_field` (ARM_OFF/ARM_ON), seeds 42/43/44. Primary DV: paired-by-seed TV distance between reef-context and open-context committed-class distributions, ARM_ON vs ARM_OFF.

**Dry-run check:** clean (0 dry-run citations; `check_dry_run_citations.py` confirms).

**Outcome:** FAIL. `non_degenerate: null` (not explicitly set; effectively degenerate per the self-route). Label: `substrate_not_ready_requeue`.

**The two readiness preconditions that failed:**

| Precondition | Measured | Threshold | Comparator | Met |
|---|---|---|---|---|
| `mech448_demotion_lever_live_and_excluding_both_arms` | 0.0 | 2.0 | `>=` | ❌ |
| `mech449_active_nogo_live_and_suppressing_both_arms` | 0.0 | 2.0 | `>=` | ❌ |

Both preconditions require ≥2 (of 6 arm×seed cells) to clear `active_frac >= 0.8`. Per-cell `f_eligibility_demotion_active_frac` / `go_nogo_active_frac` ranged 0.145–0.606 — well under 0.8 on every cell — so the count of clearing cells was 0, and the run self-routed as if MECH-448/449 were not engaging.

## 2. The bug — this is a false negative, not a substrate finding

Reading the driver (`ree-v3/experiments/v3_exq_847_arc062_pd_context_modeswitch_committed_class_divergence.py`): the active-tick numerator (`demotion_active_ticks` / `nogo_active_ticks`) is correctly latch-guarded — it only increments when `agent.e3.last_score_diagnostics` is non-`None`, i.e. on a genuine fresh `E3.select()` tick (the driver's own comment cites this as "the V3-EXQ-785 ~9x pseudo-replication fix"). But the **denominator** used to compute `active_frac` is `n_p2_ticks` — every P2 env tick, including ticks where the E3 diagnostics latch was `None` (a held/replayed commitment, not a fresh selection). At MECH-093's E3 reselection cadence, only ~10–60% of P2 ticks are genuine fresh selections (varies by seed/arm — see below), so `active_frac` is deflated by the exact fraction of held ticks, independent of whether the mechanism is actually engaging.

The manifest already records both `n_p2_ticks` and `n_latched_ticks` per cell. Recomputing `active_frac` against the correct denominator (`n_p2_ticks - n_latched_ticks`, i.e. genuine fresh-selection ticks only):

| Arm | Seed | n_p2_ticks | n_latched | fresh | reported active_frac | **corrected active_frac** |
|---|---|---|---|---|---|---|
| OFF | 42 | 1255 | 504 | 751 | 0.598 | **1.000** |
| OFF | 43 | 11212 | 9585 | 1627 | 0.145 | **1.000** |
| OFF | 44 | 999 | 451 | 548 | 0.549 | **1.000** |
| ON | 42 | 1349 | 584 | 765 | 0.567 | **1.000** |
| ON | 43 | 11212 | 9585 | 1627 | 0.145 | **1.000** |
| ON | 44 | 938 | 370 | 568 | 0.606 | **1.000** |

Every cell corrects to exactly 1.0 — MECH-448 and MECH-449 fire on **100% of genuine fresh selections**, on both arms, every seed. `demotion_active_frac` and `nogo_active_frac` are numerically identical per row because both mechanisms' "active" counters are effectively counting the same thing (fresh-selection ticks) at this substrate operating point. This is unambiguously a measurement-precondition bug, not a substrate collapse: the raw ingredients needed to see this were already in the manifest.

**The H4 primary DV was computed anyway** (the gate blocks interpretation, not computation) and is fully present in `arm_results[].tv_context_divergence`:

| Seed | OFF (reef/open ticks) | ON (reef/open ticks) | TV divergence OFF | TV divergence ON |
|---|---|---|---|---|
| 42 | 428/827 | 548/801 | 0.0852 | 0.0460 |
| 43 | 10975/237 | 10975/237 | 0.0635 | 0.0635 |
| 44 | 0/999 | 0/938 | 0.0 | 0.0 |

Seed 43's reef/open tick counts and committed-class counts are bit-identical between arms — the CRF manipulation produced zero detectable trajectory difference for that seed. Seed 44 never visits the reef half in either arm (`n_reef_ticks=0`) — the same environmental-degeneracy signature already documented for this seed in `failure_autopsy_V3-EXQ-690_2026-06-20.md` ("R3 environmental-degeneracy lesson"). Seed 42 is the only cell where the manipulation produced any divergence at all, and it runs the *opposite* direction from H4's hypothesis: CRF-ON (differentiated rule_state) **reduces** context-divergence (0.046 vs 0.085), not increases it.

## 3. Claim-layer mapping

`claim_ids=[]` by design. This diagnostic cannot support or weaken MECH-309/ARC-062 directly — it exists to test whether the 654-lineage's pooled-marginal DV is measurement-blind to a context-conditioned effect (H4). MECH-309/ARC-062's most recent note (2026-08-01, V3-EXQ-851) already documents the P-A erratum this leg is a sibling to; MECH-448/MECH-449 (both `candidate`/`provisional`, own independent validation gates 689d/689i and 689g) are unaffected either way — the readiness preconditions were about *this run's* diagnostic gate, not a re-test of their own claims.

## 4. Biological-reference triage

Not load-bearing — this is a measurement-instrumentation question (does the pooled DV alias a context-conditioned effect), not a mechanism test. No biology triage needed.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | `claim_ids=[]`, pure measurement-aliasing probe |
| Biological reference | not load-bearing | |
| Prerequisites | present, but MIS-MEASURED | MECH-448/449 are actually 100% live on fresh ticks; the readiness check itself is broken |
| Implementation | correct except one gate | latch-guarding on the numerator is right; the denominator wasn't updated to match |
| Environment | adequate except seed 44 | reef geometry is a real, working primitive (690); seed 44 is a known-degenerate seed for this specific env config |
| Measurement | **the defect** | `active_frac` denominator uses all P2 ticks instead of fresh-selection ticks only |
| Integration | coupled | offline nothing — same live substrate as 654j |
| Scale | only 1/3 seeds informative | seed 43 shows zero manipulation effect, seed 44 is environmentally degenerate |

## 6. Learning extracted

1. **Recording gap, recoverable by reanalysis, not a re-run.** `n_p2_ticks` and `n_latched_ticks` were both recorded; the correct `active_frac` (and hence the correct readiness verdict) can be recomputed from the existing manifest without spending any more compute.
2. **The denominator bug is a reusable pattern risk.** Any driver that latch-guards its numerator against held/replayed E3 ticks but computes `active_frac` against `n_p2_ticks` (not `n_p2_ticks - n_latched_ticks`) will systematically under-read active_frac by the held-tick fraction — which varies 40–86% across these six cells, so the deflation is not even a fixed discount. Sibling script V3-EXQ-859 gets this right (divides by `n_p2_fresh_select`); this driver does not. Worth a corpus-wide grep for the same anti-pattern before it recurs in a future MECH-448/449-tracking script.
3. **H4 itself remains untested in any real sense.** Of 3 seeds, only 1 (seed 42) produced a non-degenerate, arm-differentiated observation, and it points against H4's hypothesis (CRF-differentiation *reduces* context-divergence rather than increasing it). n=1 cannot support or refute H4.

## 7. Recommended routing

**Recommended `epistemic_category`:** `measurement_test_design_defect` (the precondition's denominator, not the substrate).

**Recommended `evidence_direction`:** `non_contributory` — only 1 of 3 seeds is informative (seed 43 shows no arm effect at all; seed 44 is environmentally degenerate), which is not enough to score H4 in either direction. Do NOT read seed 42's single against-hypothesis observation as `weakens` on its own.

**Recommended `evidence_quality_note`** (draft text for governance):
> [2026-08-01 failure-autopsy, V3-EXQ-847, confirmed]: self-routed `substrate_not_ready_requeue` is a FALSE NEGATIVE — the driver's `mech448_demotion_lever_live_and_excluding_both_arms` / `mech449_active_nogo_live_and_suppressing_both_arms` preconditions compute `active_frac` against `n_p2_ticks` (all P2 env ticks) rather than genuine fresh-E3-selection ticks (`n_p2_ticks - n_latched_ticks`, both already recorded). Recomputed with the correct denominator, MECH-448/449 are 100% active on every seed×arm — fully live, not dead. The H4 primary DV (`tv_context_divergence`, paired reef/open by seed) was computed regardless and is fully recoverable from this manifest without a re-run: seed 43 is bit-identical across arms (no detected CRF effect), seed 44 never visits the reef half (known-degenerate seed per V3-EXQ-690), and seed 42 (the only informative cell) shows CRF-ON *reducing* context-divergence — opposite H4's predicted direction. n=1 usable seed cannot support or refute H4. `evidence_direction: non_contributory`.

**Routing:** `/queue-experiment` — a same-question redesigned re-run (new letter, e.g. V3-EXQ-847a) with (a) the corrected `active_frac` denominator so the readiness gate reflects reality, and (b) either more seeds or a seed set pre-verified to visit both reef and open regions in adequate volume for both arms (690's own seeds 42/43 are documented-good; avoid 44 for this specific env geometry, or accept it will always self-exclude). This is a recording/measurement-gate fix, not a substrate rebuild — per Step 7's routing table, the repair is *fixing the gate*, and reanalysis of the H4 DV itself from the existing manifest can proceed in parallel without waiting on a re-run.

**Also recommend:** the same denominator-bug check be run against any other driver in this GOV-FANOUT-1 portfolio (P-A/P-B/P-C) that reused this precondition pattern, since the bug is silent (produces a plausible-looking sub-1.0 fraction rather than an obvious error).

Re-derive brake: n/a (`claim_ids=[]`, no claim to brake against — matches V3-EXQ-859's own precedent).

Granularity-debt recurrence trigger: n/a (`claim_ids=[]`).
