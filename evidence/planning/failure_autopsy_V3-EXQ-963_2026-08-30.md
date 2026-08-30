# Failure autopsy -- V3-EXQ-963 (MECH-063 sub-claim (ii) tonic/phasic dissociation retest)

- **Status:** `awaiting_human_confirmation` (staging mode -- non-interactive session; routing NOT finalised)
- **Generated:** 2026-08-30T06:34:18Z
- **Run:** `v3_exq_963_mech063ii_tonic_phasic_dissociation_retest_20260830T023012Z_v3`
- **Purpose:** `evidence`, `claim_ids: ["MECH-063", "SD-069"]`
- **Predecessors:** V3-EXQ-779 / 779a / 779b (new number, correctly, per the 779b re-derive brake)
- **Dry-run gate:** clean (`dry_run: false`)

## 1. What the manifest already got right

This is the most self-aware of the five manifests reviewed today. It emits `evidence_direction: non_contributory` for **both** claims, sets `non_degenerate: false` with reason *"substrate capability precondition unmet: tonic_axis_live"*, and carries a `sampling_shortfall` block that explicitly warns: *"This is a SAMPLING failure, not a substrate capability failure -- do not route to substrate_not_ready_requeue without an independent capability check."* The direction needs no correction. What this autopsy adds is **why**, and a correction to the route.

## 2. The decisive finding -- the tonic axis was inert

`tonic_axis_live` measured **0.0** against a floor of 0.5. `noise_floor_temp_lift_mean` is exactly **0.0 on all 20 cells** -- including `T1P0` and `T1P1`, where `use_noise_floor` is correctly `True`.

`NoiseFloor.compute_effective_temperature` (`ree_core/policy/noise_floor.py:191-193`) is **unconditional**:

```
self._n_waking_calls += 1
lifted    = float(baseline_temperature) + float(self.config.noise_floor_alpha)
effective = max(lifted, float(self.config.noise_floor_min_temperature))
```

There is no gate. `tonic_noise_floor.alpha = 1.0` in this run's config. So **a lift of exactly 0.0 means the regulator was never called on the waking path** -- this is a wiring fault, not a tuning result and not a ceiling.

### Comparison with V3-EXQ-779a (whose C1/C2 computation this run states is UNCHANGED)

| | 779a (2026-07-18) | 963 (2026-08-30) |
|---|---|---|
| `noise_floor_temp_lift_mean`, TONIC-ON cells | **1.0** (== alpha) | **0.0** |
| `mean_dS_tonic` | **+0.2654** (robust, 4/5 seeds) | **+0.0053** |
| `S_sustained_entropy` range | 0.29 - 0.76 | 0.023 - 0.166 |
| cells meeting sample floors | **3 / 20** | **4 / 20** |

**Sampling starvation is refuted as the explanation.** The two runs are essentially *equally* starved (3/20 vs 4/20 cells meeting floors), yet the outcome differs 50-fold. A confound held constant across both arms of the comparison cannot be the discriminating variable. The starvation is real and worth fixing on its own account; it does not explain this.

## 3. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | unclear | the tonic manipulation was never applied |
| Biological reference | partial | LC-NE tonic/phasic gain control well-anchored; not reached |
| Prerequisites | **present** | SD-075 implemented (`4a5139838b`); V3-EXQ-952 confirmed the config; brake legitimately released |
| Implementation | partial | regulator configured on, never invoked |
| Environment | adequate | same env as 779a, which produced a large clean effect |
| Measurement | **under-instrumented** | the two counters that would identify the cause exist and were not recorded |
| Integration | **isolated** | tonic axis configured on, no downstream effect |
| Scale | adequate for the comparison | starvation matched to 779a |

**Failure-location (GOV-FAILLOC-1): `MECHANISM` (wiring) + `MEASURES`.** Implementation is not complete and measurement is not adequate, so **REE FAILED is not reachable** and is not asserted. MECH-063 sub-claim (ii) is untouched by this run.

## 4. Arguments raised and withdrawn

1. **"Sampling starvation explains the collapse."** *Refuted* by the 779a comparison above (3/20 vs 4/20 -- matched).
2. **"The SD-074 warmup cache fails to restore the NoiseFloor regulator's warmed state."** *Refuted by code read*: NoiseFloor is documented "stateless across ticks" and the lift is computed unconditionally, so a cold regulator lifts identically to a warmed one. **The underlying blind spot is nonetheless real and is reported separately** (section 6) -- it just is not this failure's cause.
3. **"`noise_floor_alpha` is 0."** *Refuted*: `alpha = 1.0`. Note 779a's measured lift was exactly `1.0` -- i.e. the regulator fired on **every** tick there and on **zero** ticks here.

## 5. Learning extracted

- **The decisive move was comparing the predecessor's per-cell *instrument* reading, not its headline result.** `lift_mean 1.0 -> 0.0` identifies an inert manipulation at once; `mean_dS_tonic 0.265 -> 0.005` alone reads as a weak or negative result.
- **A matched confound is a free control.** Near-equal starvation across the two runs converts starvation from a candidate explanation into a held-constant nuisance variable, refuted in one line.
- **RECORDING GAP.** `NoiseFloor.get_state()` already exposes `n_waking_calls` and `last_n_simulation_skips` -- together they separate "never called" from "called under `simulation_mode`". Neither was recorded, so a re-run is currently needed to answer a question the substrate was *already computing*.
- `baseline_entropy_headroom` passed (`met: True`) while **all four arms** appear in `saturating_arms` with `worst_margin` 0.0037 against a `warn_margin` of 0.15. The gate tests membership of the band `[0.02, 0.98]`, not the margin to its edge, so it admits a run with effectively no headroom.
- The `tonic_axis_live` capability gate, evaluated worst-cell, **worked** -- it is why this manifest's `evidence_direction` is already correct.

## 6. Cross-cutting finding (bears on, not adjudicated here)

`NoiseFloor` is zero-parameter and **not** an `nn.Module`. That places it in a double blind spot of the warmup cache: invisible to `assert_state_dict_shareable` (which compares `state_dict` key/shape parity, and whose docstring cites exactly this zero-parameter property as *what licenses* cache sharing across the 2x2), and invisible to `_restore_cached_surface` (which walks `agent.named_modules()`). The guard also logs cached module paths *absent on this substrate* but not the reverse -- a module present here and absent from the cache passes silently. Harmless for this failure; worth closing before a stateful non-Module regulator is added.

## 7. Routing (proposed -- awaiting confirmation)

**`implement-substrate`**, new entry `sd_tonic_noise_floor_call_path_integrity`, priority 1, severity **`corrupting`** (the run produced a claim-tagged manifest that looks valid while the manipulation was silently absent).

**Re-derive brake -- read carefully.** MECH-063 carries **3** prior `substrate_ceiling` hits under the R1-R3 convention (`20260329-legacy-cluster`, `MECH-063-777a-779a-cluster`, `V3-EXQ-779b`), above the threshold of 2. **This autopsy does not add a fourth** -- the reading is `standard` (instrument wiring), not `substrate_ceiling`. The brake therefore does not fire here and a same-question re-test is *not* refused. But it is **gated on the wiring repair plus the recording addition** below -- not permitted as another blind letter.

### Fan-out (GOV-FANOUT-1) -- three live explanations, different axes

| # | Hypothesis | Axis | Probe |
|---|---|---|---|
| H2 | The noise-floor call site is not reached on the tonic path (only all-cell change vs 779a is the SD-074 shared cached warmup) | instrumentation | record `n_waking_calls` per cell; `0` confirms |
| H3 | Scored selections ran with `simulation_mode=True`, which returns baseline unchanged by contract | instrumentation | record `last_n_simulation_skips`; `>0` with `n_waking_calls==0` confirms |
| H2 | (behavioural check) | process | run one cell with SD-074 warmup DISABLED; restored `lift_mean 1.0` isolates the warmup |
| H5 | Substrate drift 2026-07-18 -> 2026-08-30 changed the call path independently | representation | replay the 779a driver unchanged against today's substrate |

**The first two probes are pure instrumentation and cost nothing. Run them before spending any behavioural budget.**

## 8. Recommended per-claim disposition

| Claim | Direction | `epistemic_category` | Status |
|---|---|---|---|
| **MECH-063** | `non_contributory` | currently carries **no** category field -- set one -> `standard` | stays `provisional` |
| **SD-069** | `non_contributory` | already `standard`; **must not move** -- the change is the `evidence_quality_note` | stays `candidate` |

Explicitly: **do not record `substrate_ceiling` from this run.**

## 9. Mechanical pre-routing checks (Step 7b)

**1 fire, acted on (not dismissed).**

**C2** -- `action: "create"` was recommended for MECH-063/SD-069 while `SD-PROBE-WARMUP` and `sd_phasic_ema_episode_continuity` already unblock those claims and went unmentioned.

Both are now named in the artifact. The new entry is **retained**: `sd_phasic_ema_episode_continuity` (SD-075) is the entry the 779b brake routed to and is implemented (`4a5139838b`, confirmed by V3-EXQ-952) -- which is exactly what licensed this run; `SD-PROBE-WARMUP` covers the SD-074 warmup this run consumed. **Neither concerns the tonic noise-floor call path**, which is the defect diagnosed here.

One consequence worth flagging at apply time: fan-out **H2 implicates the SD-074 shared cached warmup as a possible route to the fault**. If H2 is confirmed, the repair may belong against `SD-PROBE-WARMUP` rather than in a new entry -- governance's call.

## Adversarial red-team pass (Step 7c) -- NOT RUN

**No independent verifier ran, and no CONFIRMED verdict is claimed.** Step 7c calls for spawning a separate agent (preferably on a different model) to attack the conclusion. This session operates under a standing instruction not to invoke the Agent tool unless the user requests it, and the user did not.

The adversarial discipline was applied in-context instead, and it did change conclusions rather than rubber-stamping them -- six arguments were raised and withdrawn on direct code or docstring reads, each recorded under `arguments_withdrawn`. That is explicitly **weaker** than an independent pass: it shares the drafter's priors by construction, which is the exact property the pass exists to break.

**For governance:** treat every routing recommendation here as unverified by a second reader. The two highest-value targets for an independent check are V3-EXQ-963's claim that sampling starvation is refuted by the 779a comparison, and V3-EXQ-964's claim that C2 was mathematically unsatisfiable at `n_targets == 1`.
