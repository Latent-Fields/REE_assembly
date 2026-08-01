# Failure Autopsy: V3-EXQ-836e (MECH-476 interval-dependent consolidation, THIRD and final falsifier leg)

**Generated:** 2026-08-01T14:08:00Z
**Run:** `v3_exq_836e_mech476_interval_dependent_consolidation_redesign_20260801T124230Z_v3`
**Queue ID:** V3-EXQ-836e
**Claim IDs:** MECH-476
**Status:** confirmed
**Supersedes:** V3-EXQ-836b
**Read alongside:** `failure_autopsy_V3-EXQ-836-cluster_2026-08-01.md` (836a dose + 836d novelty-tagging, both already confirmed `weakens`, held pending this exact leg)

## 1. Facts

**Design.** Third leg of the noise-scaled MECH-476 falsifier redesign (same convention as 836a/836d: `effective_margin = max(1.5 * sd_delta, 0.05)`, 10 seeds, leave-one-out diagnostics). Varies the A→B offline interval (window_steps: 0/150/400/900) between BC-install and RL-refinement interference, holding install dose fixed. Tests whether resistance to interference grows with the consolidation window (Krakauer, Ghez & Ghilardi 2005 retrograde-interference design).

**Outcome:** FAIL. `non_degenerate: true`. Label: `retention_invariant_to_interval_no_process`.

**Readiness:** all 4 window arms (n0/n150/n400/n900) pass `install_took_strict_majority` at 100%.

**Interval response:**
| window_steps | 0 | 150 | 400 | 900 |
|---|---|---|---|---|
| retained_fraction_mean | 0.712 | 0.707 | 0.860 | 0.723 |

Spread 0.153, **non-monotone** (peaks at n400, does not grow steadily with interval). `mean_paired_delta = 0.0106` vs `effective_interval_margin = 0.893` (noise-scaled, `sd_delta=0.595`) — the effect is roughly **84x smaller** than the margin required to call retention interval-dependent.

**Leave-one-out:** all **10/10 folds** (dropping each seed 42–51) read `weakened` — fully robust, matching 836d's own 10/10 result.

## 2. Claim-layer mapping — this is the completing leg

MECH-476's own pre-registered `what_would_answer` text (claims.yaml) states the exact disposition this cycle is meant to settle:

> "WEAKENED if retained fraction is INVARIANT to both [install dose and the A→B interval] and tracks only the concurrent constraint coefficient — there is then no consolidation process **and this claim is withdrawn into MECH-459/460**."

Status of all three pre-registered arms after this run:

| Arm | Run | Result | Robustness |
|---|---|---|---|
| Dose | V3-EXQ-836a | **weakens** — retained_fraction non-monotone across dose (0.712→0.430→0.512), effect well inside noise-scaled margin | confirmed |
| Novelty-tagging (the claim's own "sharpest discrimination") | V3-EXQ-836d | **weakens** — paired retention LOWER than unpaired (0.834 vs 0.950), reversed from Moncada & Viola's prediction | 10/10 leave-one-out folds |
| Interval | V3-EXQ-836e (this run) | **weakens** — non-monotone across interval (0.712/0.707/0.860/0.723), effect ~84x inside margin | 10/10 leave-one-out folds |

**All three legs now independently satisfy the claim's own pre-registered WEAKENED condition**, each with clean readiness gates and (for the two most recent) full leave-one-out robustness.

## 3. Biological-reference triage

Unchanged from the cluster autopsy — Krakauer 2005 (consolidation-as-resistance-to-interference, the direct source of this leg's design), Walker et al. 2003 (dissociable consolidation stages), Moncada & Viola 2007 (behavioral tagging, tested by the sibling 836d leg). All three arms are fair, well-instrumented tests of the biological predictions, not translation gaps — the biology is clear and the substrate prerequisites (SD-083 offline EWC-anchor window, distributional critic V3-EXQ-788, KL anchor V3-EXQ-792) are all landed and confirmed engaging.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | third and final pre-registered arm, tested fairly under the fixed measurement convention |
| Biological reference | clear | Krakauer 2005 directly on-point; unchanged from siblings |
| Prerequisites | present | all 4 window arms readiness-gated at 100% |
| Implementation | complete | same noise-scaled gate as 836a/836d |
| Environment | adequate | offline window length is a cleanly manipulable parameter |
| Measurement | now adequate | effect ~84x smaller than the noise-scaled margin — not a close call |
| Integration | coupled | same substrate (offline EWC-anchor window) as siblings |
| Scale | adequate | 10 seeds, 10/10 leave-one-out robust |

## 5. Why this is claim-level ripe, not just another leg

This autopsy is not simply "one more weakens data point." The claim's own pre-registration names an exact three-part falsifier and an exact withdrawal criterion, and — as of this run — all three parts are in, all three read the same direction, and the two most recent are leave-one-out-robust at 10/10. This is a rare case where a claim wrote its own falsification condition in advance and that condition has now been cleanly met by fair, well-powered tests across every arm it named. Per this skill's routing table, "tested fairly + biology supports the mechanism + still fails" is the highest-threshold case for recommending demotion — and here it applies with the additional strength that the claim itself specifies exactly what should happen next (withdrawal into MECH-459/460, not merely a status/confidence change).

## 6. Learning extracted

1. All three independently-designed falsifier arms now converge on the same finding: retention in REE is invariant to dose, interval, and novelty-pairing alike — consistent with a constant regulariser (the distributional critic + KL anchor), not a consolidation process.
2. The noise-scaled effect-size-gate redesign (replacing the 2026-07-29 cycle's fixed-0.15-margin defect) has now produced three clean, well-powered, mutually-reinforcing verdicts — the redesign methodology itself is vindicated.
3. A claim pre-registering its own exact withdrawal criterion, later cleanly satisfied, is the strongest possible position for applying that pre-registered disposition rather than open-ended re-litigation.

## 7. Routing

**Evidence direction: `weakens`** (confirmed, matches self-route).

**Routing: `governance-demotion`** — specifically, recommend `/governance` apply MECH-476's own pre-registered disposition: **withdraw the claim, folding its content into MECH-459/460** (return_scale_invariance_blocks_actor_bootstrap and transient_behavioral_prior_bootstrap respectively), per the exact text in the claim's `what_would_answer` field. This is a recommendation for the normal `/governance` interactive confirmation, not applied here (out of this skill's scope).

Re-derive brake: 0 prior `substrate_ceiling` autopsies for MECH-476 (this cluster's category is `standard`, not `substrate_ceiling`) — does not fire. This is a completion of a pre-registered falsifier, not a re-derive loop.
