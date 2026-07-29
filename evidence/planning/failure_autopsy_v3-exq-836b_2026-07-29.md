# Failure Autopsy — V3-EXQ-836b (MECH-476, interval-dependent consolidation)

- **Generated (UTC):** 2026-07-29T21:57:54Z
- **Scope:** single (straggler sibling of the confirmed `failure_autopsy_mech476-mech475-cluster_2026-07-29`)
- **Status:** confirmed
- **Run:** `v3_exq_836b_mech476_interval_dependent_consolidation_20260729T210911Z_v3`
- **Queue id:** V3-EXQ-836b · **Purpose:** evidence · **Claim:** MECH-476
- **Outcome:** FAIL · self-route `non_monotone_interval_response` · `evidence_direction: mixed` · `non_degenerate: true`
- **Dry-run gate:** clean (top-level `dry_run` absent; `check_dry_run_citations.py` → 0 dry). **Recording:** `validate_recording.py` OK (always-core complete).

## 1. Facts (no interpretation)

Four interval arms — offline consolidation window = 0 / 150 / 400 / 900 steps — n=6 seeds each (seeds 42-47), rung `D3_hazard_free`. **Every arm installed above the competence floor** (`install_took_fraction = 1.0` on all four; all four per-arm gates green; `post_bc_foraging_competence_mean = 9.71` identical across arms because BC install is pre-consolidation and shared).

Decision variable = `retained_fraction` (terminal ÷ peak foraging competence). Interval-response axis:

| window steps | 0 | 150 | 400 | 900 |
|---|---|---|---|---|
| retained_fraction mean | 0.389 | 0.536 | 0.749 | **0.592** |
| per-arm SD | 0.241 | 0.345 | 0.359 | 0.295 |
| per-arm SEM (n=6) | 0.098 | 0.141 | 0.147 | 0.120 |

Load-bearing criterion `resistance_grows_with_interval` = *monotone non-decreasing in N* **AND** *(mean[max_N] − mean[min_N]) ≥ 0.15 (fixed `RESISTANCE_INTERVAL_MARGIN`)*. **FAILED** — the axis rises to n400 then **drops** at n900, so it is non-monotone (`monotone_non_decreasing: false`, `spread: 0.360`, `non_monotone: true`). Failed criterion = **discrimination** (every readiness/install precondition passed).

## 2. Why the verdict is non_contributory, not "mixed"

- **Between-arm deltas sit inside per-arm noise.** Deltas = [+0.147, +0.213, **−0.157**]; per-arm SEMs are 0.098-0.147. Every step is ≤ ~1 SEM, and the fixed 0.15 margin is *not scaled to observed noise* — identical defect to siblings 836 (dose) and 836c (novelty).
- **Single-seed sensitivity.** The non-monotone peak at n400 is driven by one extreme seed (`retained_fraction = 1.285` vs siblings 0.202-0.934). Leave-one-out on that seed pulls n400's mean 0.749 → 0.642, collapsing the peak that makes the axis non-monotone. The load-bearing verdict does not survive a leave-one-out check — same as 836/836c.
- The `mech476-mech475-cluster` autopsy explicitly named 836b as the propagation risk ("interval arm, still running on ree-cloud-3 … shares the same script family and likely the same fixed-margin pattern"). It does.

## 3. Claim-layer map (MECH-476)

MECH-476 (interval/dose/novelty-dependent consolidation) is **neither strengthened nor weakened**: nothing here bears on whether consolidation is genuinely interval-dependent, because the instrument cannot discriminate a real interval effect from n=6 ratio-DV noise at a fixed 0.15 margin. The FAIL is entirely about test-design validity.

## 4. Biological-reference triage

Closest reference: Müller-Pilzecker / Krakauer et al. 2005 time-dependent (retrograde-interference) consolidation — a genuine biological existence proof for the *class*. The design is agnostic to REE's known divergence (awake/online/undifferentiated protection vs the biology's sleep/replay-dependent, trace-selective mechanisms) and does not resolve it either way. Not a formal-definition import; `lit_status: partial`. No biology-divergence finding is load-bearing here — the block is measurement, upstream of the biology question.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | instrument cannot discriminate; MECH-476 untouched |
| Biological reference | clear | Müller-Pilzecker/Krakauer time-dependent consolidation |
| Prerequisites | present | install took on all arms, all gates green |
| Implementation | complete | consolidation window machinery ran as specified |
| Environment | adequate | D3_hazard_free rung as designed |
| Measurement | **misleading** | fixed 0.15 margin < per-arm noise floor at n=6; ratio-DV single-seed sensitive |
| Integration | isolated | — |
| Scale | **likely insufficient n** | n=6 seeds cannot resolve a <0.2 interval effect against this per-seed variance |

**Recommended `epistemic_category`: `measurement_test_design_defect`** (do not write — governance applies).

## 6. Learning extracted

- The fixed (non-noise-scaled) 0.15 discrimination margin at n=6 is the same defect that felled 836 and 836c; the `retained_fraction` ratio DV is highly sensitive to single-seed RL-trajectory variance across the whole 836 family.
- Existing dependency neither strengthened nor weakened — nothing here bears on whether consolidation is interval-dependent.
- The three arms of the 836 family (dose / interval / novelty) share one instrument and one flaw; a redo should adopt a **noise-scaled discrimination rule** (margin scaled to the SD of the between-arm delta, plus an absolute floor) uniformly, not a per-arm fixed constant.

## 7. Repair pathway — routing

Node class: `complex (probe-gated) / mystery (known data)` at the measurement level — we already have the data to see the instrument is too coarse; the fix is a measurement redesign, not more runs of the same design.

**Routing: `/queue-experiment` — 836b redo under a noise-scaled discrimination rule** (same route the cluster gave 836/836c). New alphabetic-suffix iteration (same scientific question, corrected instrument). Mark this run `evidence_direction: superseded` once the redo lands. **Not** `/implement-substrate` (substrate is fine), **not** demotion (claim untested).

### Draft `evidence_quality_note` (governance to write — do NOT write here)

> V3-EXQ-836b (2026-07-29, INTERVAL arm) self-routed non_monotone_interval_response, but is non_contributory, not mixed: the retained-fraction interval axis [0.389, 0.536, 0.749, 0.592] over windows [0,150,400,900] is non-monotone only because of the drop at n900, and every between-arm delta (+0.147/+0.213/−0.157) sits inside the per-arm SEM (0.098-0.147) against a fixed, non-noise-scaled 0.15 margin; the n400 peak does not survive leave-one-out on its single extreme seed (retained_fraction=1.285, mean 0.749→0.642) (failure_autopsy_v3-exq-836b_2026-07-29). Same measurement_test_design_defect as siblings 836/836c. Superseded pending a 836b redo under a noise-scaled discrimination rule.

## 8. Granularity-debt / re-derive brake

- **Re-derive brake:** does **not** fire — R3 counts only `substrate_ceiling`; this is `measurement_test_design_defect`. No refusal recorded.
- **Granularity-debt trigger:** does **not** fire — MECH-476's autopsy cluster is measurement/instrument debt (no target reads `claim_alignment: weakened`), not granularity debt; the coarse-claim decomposition signal is absent.

## 9. Cluster consistency

Routed **consistently** with the confirmed `failure_autopsy_mech476-mech475-cluster_2026-07-29`: 836 (dose) and 836c (novelty) both → `measurement_test_design_defect` / `non_contributory` / redo-under-noise-scaled-rule. 836b (interval) is the fourth member of the same fixed-margin ratio-DV signature and receives the same verdict. Kept as a separate straggler file (per user judgment) rather than folded into the cluster artifact.
