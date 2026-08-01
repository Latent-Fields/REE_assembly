# Failure Autopsy: V3-EXQ-857 (Q-086 gentler-environment confound control)

**Generated:** 2026-08-01T14:08:00Z
**Run:** `v3_exq_857_q086_gentler_env_fingerprint_20260801T134757Z_v3`
**Queue ID:** V3-EXQ-857
**Claim IDs:** Q-086 (diagnostic)
**Status:** confirmed
**Flagged in `pending_review.md`** as "Diagnostic adjudication required (self-route unverified)" — `precondition_unmet`.
**Read alongside:** `failure_autopsy_V3-EXQ-856_2026-08-01.md` (this run is 856's driver-designated follow-up)

## 1. Facts

**Design.** Environment-confound control for the V3-EXQ-664 z_harm_a saturation observation. Two arms: ARM_HARSH (num_hazards=4, hazard_food_attraction=0.7, the 664 default) vs ARM_GENTLE (num_hazards=1, hazard_food_attraction=0.2). Tests whether z_harm_a's saturation is a REPRESENTATIONAL/CALIBRATION pathology (stays pegged regardless of ecology) or FAITHFUL CHRONIC SUFFERING (level/range genuinely track hazard density).

**Outcome:** FAIL. `non_degenerate: false`. Label: `substrate_not_ready_requeue`.

**Readiness precondition:** `gentle_env_manipulation_took_z_harm_s_differs` — measured SNR **0.42** vs required **≥2.0**. `|delta mean z_harm_s| = 0.072`, `seed_noise_sd = 0.171`. **FAILED**: the environment was not measurably made gentler by this metric.

**Per-seed z_harm_s** (the sensory harm tier used for the readiness check):
| | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| ARM_HARSH | 0.308 | 0.647 | 0.421 |
| ARM_GENTLE | 0.212 | 0.649 | 0.299 |

Note ARM_GENTLE's highest seed (0.649) nearly matches ARM_HARSH's highest (0.647) — heavy overlap despite a 4x reduction in hazard count.

**Secondary, uncounted observation:** `min_eval_steps` differs sharply between arms — ARM_HARSH=58, ARM_GENTLE=125. This suggests some harsh-arm episodes are ending much earlier (plausibly hazard-driven), a signal the per-step z_harm_s average does not directly capture.

## 2. Why this looks like a power problem, not a design-logic flaw

The manipulated parameters are substantively large on paper (num_hazards cut 75%, hazard_food_attraction cut 71%), yet the effect on z_harm_s is small (0.072) relative to seed-to-seed noise (SD 0.171, a ~42% coefficient of variation on a ~0.4 mean). With only 3 seeds, clearing an SNR≥2.0 bar against this much per-seed variance is a demanding requirement. This reads as under-powered rather than a wrong hypothesis about what drives z_harm_s.

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | readiness gate failed, no discrimination possible |
| Biological reference | not load-bearing | diagnostic |
| Prerequisites | n/a | this run's own manipulation is what failed to take |
| Implementation | manipulation large on paper, small in effect | |
| Environment | genuinely didn't move z_harm_s beyond noise | SNR 0.42 vs 2.0 required |
| Measurement | likely a power problem | 3 seeds vs high per-seed variance is a demanding bar |
| Integration | n/a | |
| Scale | insufficient | more seeds and/or a starker gradient needed |

## 4. The uncounted signal worth instrumenting directly

`min_eval_steps` (58 harsh vs 125 gentle) suggests the harsh environment IS doing something — plausibly causing earlier episode termination (hazard collisions/mortality) — that the chosen readout (per-step average z_harm_s) doesn't capture, since an episode that ends early contributes fewer, possibly systematically different, harm-tier samples to the average. A redesign should consider episode survival time as an explicit secondary DV rather than relying solely on the per-step average.

## 5. Connection to V3-EXQ-856

This run is the driver-designated follow-up to V3-EXQ-856 (SD-087), which weakened the hypothesis that the SD-020 PE-target flag explains the 664 saturation signature. This run was meant to test the alternative (environment/ecology) explanation, but its own readiness gate never cleared. **Net result of the 856→857 chain: the underlying question (what explains the 664 saturation-and-inversion signature?) remains open on both candidate explanations.** Neither is confirmed or eliminated.

## 6. Learning extracted

1. A large-on-paper parameter change can still fail an SNR-based readiness gate if the underlying metric is noisy — worth checking observed variance before assuming a manipulation of this size will clear a fixed SNR bar.
2. `min_eval_steps` divergence between arms is informative and currently uncounted — instrument episode survival time directly in a redesign.
3. The 856/857 diagnostic chain has now run both legs without resolving the shared question; it remains genuinely open, not defaulted toward either hypothesis.

## 7. Routing

**Evidence direction: `non_contributory`** (confirmed — no discrimination was possible).

**Routing: `/queue-experiment`** — a redesigned re-run with either (a) more seeds (5–10) to gain power against the observed noise, or (b) a starker environmental gradient (e.g. num_hazards 4 vs 0), or both, plus consider adding episode-survival-time as an explicit secondary DV to capture the signal `min_eval_steps` hints at.

Re-derive brake: 0 prior `substrate_ceiling` autopsies for Q-086 (first-ever run) — does not fire.
