# Failure Autopsy: V3-EXQ-848 (ARC-005 precision-only decoupled ladder, TRACK A)

**Generated:** 2026-08-01T14:08:00Z
**Run:** `v3_exq_848_arc005_precision_only_decoupled_ladder_20260801T134855Z_v3`
**Queue ID:** V3-EXQ-848
**Claim IDs:** ARC-005
**Status:** confirmed
**Successor of:** V3-EXQ-802 (confounded joint-ladder design)

## 1. Facts

**Design.** Successor to V3-EXQ-802, which moved all four control-plane channels together and landed FAIL/mixed (clean occupancy dissociation, but log10-precision bit-identical across levels — rho=0.0 exactly, for every unit). Root-cause diagnosis (chip-20260731-arc005-802-precision-anomaly) found channels 3/4 never reach E3's precision readout at all (occupancy-only, correctly excluded a priori here), and pre-registered specific reasons channels 1/2 were ALSO expected to show weak/no effect even after decoupling:
- **Channel 1 (5-HT rigidity):** a real substrate bug (SD-057 L7 dACC-consume reading the collapsed proposer starting state) was found and **fixed this session**. This run is the first to exercise the fix. However, quantified diagnosis showed `dacc_adapter`'s response to a genuine post-fix `goal_proximity` signal is ~1e-8 — 4-7 orders of magnitude below the ~0.87 scale of other score_bias components — because `dacc_adapter` has never been trained on non-degenerate values of this input.
- **Channel 2 (phasic-burst temperature):** architecturally argmax-invariant under normal committed operation (measured ~97% committed in a matched-RNG probe) — temperature only matters in the rare uncommitted stochastic branch this experiment doesn't exercise.

This run (TRACK A) decouples the ladder to vary **only** channels 1+2, holding 3+4 at L0 defaults in every cell (6 cells × 5 seeds = 30 cells, matching 802's cell count).

**Outcome:** FAIL. `non_degenerate: true`. Label: `precision_channel_authority_weak`. `evidence_direction: mixed`.

**Criterion:** `C_precision_monotonicity` (load-bearing) — `|Spearman rho(log10-precision, level)| ≥ 0.60`, required in ≥7/10 (content×seed) units. **Only 4/10 satisfied.**

**Per-unit rho values:** Content A: [0.866, 0.0, -0.5, 0.866, 0.5]. Content B: [0.0, 0.866, 0.866, 0.5, 0.0]. Scattered across the full range — **not** a clean near-zero null (802's own finding was bit-identical rho=0.0 for every unit).

**Readiness:** all preconditions pass across all 6 cells (`precision_cross_seed_sd`, `n_salience_ticks ≥150`, `channel_state_delta_vs_L0 >0.05` for perturbed cells).

## 2. Claim-layer mapping

ARC-005 tests whether the control plane routes precision, decoupled from occupancy. This run is scoped to precision ONLY (occupancy dissociation was already clean and strong in 802's own C1/C3, not retested here; GAP-B/V3-EXQ-846 covers per-channel occupancy attribution separately).

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | correctly-scoped successor to a confounded design |
| Biological reference | not load-bearing | control-plane wiring/authority question |
| Prerequisites | present | all readiness gates green across all 6 cells |
| Implementation | complete, pre-explained | channel 1 fix landed and exercised; both channels' expected weakness pre-registered with specific mechanisms |
| Environment | adequate | same family as 802 |
| Measurement | **coarse statistic** | Spearman rho over only 3 ladder levels is high-variance; worth a redesign note |
| Integration | coupled | channel 1 wired correctly but consumer untrained |
| Scale | likely under-powered for the noise-vs-signal question | 10 units at 3 levels each |

## 4. Why "mixed" is the right label, and why it's subtly different from what was pre-registered

The driver's own docstring pre-registered the EXPECTATION of a clean null (matching 802's own bit-identical rho=0.0 finding) and explained why via two independent, already-diagnosed mechanisms (channel 1's untrained consumer, channel 2's architectural argmax-invariance). The actual result is **not** that clean null — it's a noisy, scattered pattern (rho ranging -0.5 to 0.866) that the driver's own outcome map correctly buckets separately ("FAIL, otherwise (some real but sub-threshold trend) → mixed") rather than forcing into the expected non_contributory bucket. This distinction matters: the pre-registered mechanistic explanations (untrained dacc_adapter at ~1e-8 scale; architectural temperature-invariance under commitment) predict a signal too small to detect as *anything*, which would look like scattered noise around zero just as easily as a clean flat zero. With only 3 ladder levels per unit, Spearman rho is a coarse statistic — under pure noise (zero true effect), a 3-point correlation can easily land at |rho|≥0.6 by chance, since there are few possible values it can take. So this run's scattered pattern is **consistent with, not contradictory to**, the pre-registered mechanistic story — but it's worth being honest that a 3-point correlation can't cleanly distinguish "weak real effect" from "pure sampling noise at low resolution," which a future redesign (more ladder levels, not just more seeds) could resolve.

## 5. A new substrate gap, quantified but not yet tracked

Channel 1's `dacc_adapter` untrained-consumer gap (Track C in the driver's docstring) is quantified precisely (~1e-8 vs ~0.87 scale, 4-7 orders of magnitude) but had no `substrate_queue.json` entry. This autopsy recommends creating one (`arc005_dacc_adapter_goal_proximity_training`).

## 6. Learning extracted

1. Decoupling a confounded joint-ladder design into only the mechanistically-relevant channels converted an uninterpretable 802 confound into a clean, mechanistically-grounded result — a good general pattern.
2. A driver pre-registering *why* a null is expected makes the eventual result more interpretable, but the actual outcome (scattered, not clean-zero) deserves its own honest read rather than being smoothed into the pre-registered expectation.
3. Per-unit Spearman rho at only 3 ladder levels is a coarse, high-variance statistic — a future redesign wanting a cleaner discrimination should add ladder levels rather than only seeds.
4. The dacc_adapter undertraining gap was diagnosed with a specific quantified magnitude but had no substrate_queue entry — now created.

## 7. Routing

**Evidence direction: `mixed`** (confirmed, matches self-route).

**Routing: `/implement-substrate`** — create `arc005_dacc_adapter_goal_proximity_training` (channel 1's untrained-consumer gap, quantified at ~1e-8 vs ~0.87 scale). Track B (channel 2 under an uncommitted-only regime) remains a separately-noted future candidate per the driver's own docstring, not built here.

Re-derive brake: 0 prior `substrate_ceiling` autopsies for ARC-005 in this category (`standard`, not `substrate_ceiling`) — does not fire.
