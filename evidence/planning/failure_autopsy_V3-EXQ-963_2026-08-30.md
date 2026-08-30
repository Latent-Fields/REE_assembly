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
| `S_sustained_entropy` range | 0.146 - 0.849 | 0.023 - 0.166 |
| cells meeting sample floors | **3 / 20** | **4 / 20** |

**Sampling starvation is refuted as the explanation -- and more strongly than first stated.** The two runs are not merely equally starved: 963's per-cell sampling is **equal-or-better** than 779a's (min `n_e3_selects` 334 vs 280; min phasic event ticks 95 vs 6; comparable totals ~11.2k). The 120-vs-2400 `max_episodes_per_cell` difference is inert, because the 2400-env-step cap binds in both. A confound held constant -- here, held *favourably* -- cannot be the discriminating variable.

**One caveat on the headline ratio, added after red-team.** The 50x `mean_dS_tonic` collapse is contaminated by a roughly 5x warmup-driven compression of the entropy scale itself, so it overstates the effect size. **The clean, scale-free statement is the lift: 1.0 -> 0.0**, which is what this diagnosis actually leans on.

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

## 6. CAUSE CONFIRMED -- and this section previously asserted the opposite

> **The first revision of this section was wrong.** It described the warmup-cache blind spot as *"Harmless for this failure"* and said `NoiseFloor` is *"invisible to `_restore_cached_surface`"*. Both are false: that machinery **is the cause**, and the restore does not fail to see the regulator -- it **overwrites** it.

The chain, verified in source and reproduced with the real functions:

1. `_warmup_key` excludes the arm's runtime flags, so one warmup blob is shared across the whole 2x2 within a seed.
2. **`T0P0` is always the cache MISS** and therefore always mints the blob -- and `T0P0` has `use_noise_floor=False`, so `agent.noise_floor` is `None` in the captured surface (`agent.py:1159` declares `self.noise_floor: Optional[NoiseFloor] = None`; it is constructed only when the flag is set, `:1166`).
3. On every cache HIT, `_restore_cached_surface` does `object.__setattr__(module, name, value)` across that surface, **writing the mint arm's `None` over the live `NoiseFloor` instance** the TONIC-ON arm had just constructed.
4. The guarded call site `if self.noise_floor is not None` (`agent.py:3444`) is then skipped. No lift is ever computed, so `noise_floor_temp_lift = tonic_T - baseline = 0.0`.

Nothing raises and nothing logs it: `assert_state_dict_shareable` passes because these regulators are zero-parameter and non-`nn.Module` (its docstring cites exactly that property as *what licenses* the sharing), and the restore's missing-module logging covers only cached paths **absent here**, never the reverse.

**The clincher is the asymmetry, and it was in the cells all along.** The driver's `_fresh_regulator` (line 502) reinstalls **only** `agent.phasic_burst` after warmup -- never `agent.noise_floor`. So the phasic axis survived the restore and the tonic axis did not. Confirmed: `R_transient` is non-zero on **10/10** PHASIC-ON cells and exactly `0.0` on all 10 PHASIC-OFF cells, while the tonic lift is `0.0` everywhere. **No other hypothesis explains that split.**

**`ree_core` is healthy.** This is an experiment-harness defect.

## 7. Routing (proposed -- awaiting confirmation)

**`implement-substrate`**, new entry `sd_tonic_noise_floor_call_path_integrity`, priority 1, severity **`corrupting`** (the run produced a claim-tagged manifest that looks valid while the manipulation was silently absent).

**Re-derive brake -- read carefully.** MECH-063 carries **3** prior `substrate_ceiling` hits under the R1-R3 convention (`20260329-legacy-cluster`, `MECH-063-777a-779a-cluster`, `V3-EXQ-779b`), above the threshold of 2. **This autopsy does not add a fourth** -- the reading is `standard` (instrument wiring), not `substrate_ceiling`. The brake therefore does not fire here and a same-question re-test is *not* refused. But it is **gated on the wiring repair plus the recording addition** below -- not permitted as another blind letter.

### Fan-out (GOV-FANOUT-1) -- RESOLVED BEFORE QUEUING, do not fan out

The first revision proposed a three-hypothesis portfolio (H2 wiring / H3 `simulation_mode` / H5 substrate drift) and noted that the first two probes were pure instrumentation and free. **The red-team pass ran them, as source reads, and H2 is confirmed** (section 6). H3 and H5 are refuted or unnecessary: both drivers read the identical `_last_control_vector["G_vigor"]["noise_floor_temp_lift"]` field, and `T1P0` alone carries the 1.0 -> 0.0 contrast even under a worst-case SD-069 recording-semantics change; and no drift hypothesis explains phasic surviving while tonic died.

This is recorded rather than deleted, because it is what a GOV-FANOUT-1 portfolio is *for*: enumerating the rivals and noticing two probes cost nothing is what collapsed a three-way discrimination to a confirmed single cause **before any compute was spent**. The hypothesis-space ledger append is withdrawn accordingly -- registering a frozen 3-hypothesis set for an already-answered question would inflate the denominator with legs that were not live at registration time, which the ledger invariants forbid.

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

## Adversarial red-team pass (Step 7c) -- VERDICT: CONTESTED

An independent verifier (different model, reasoning withheld until it had recomputed from the raw cells) attacked this diagnosis. **The conclusion survived every attack. The repair did not.**

**Verified exhaustively, not sampled:** all 20 cells of 963 at lift exactly 0.0 (including all 10 `use_noise_floor=True` cells); all 10 TONIC-ON cells of 779a at exactly 1.0 (== alpha). No dissenting cell in either run. Per-seed and mean `dS_tonic` recomputed from the raw `S_sustained_entropy` cells, matching both manifests to <1e-9.

**Attacks that failed:**
- *Is it the same quantity in both runs?* Yes -- both drivers read the identical `_last_control_vector["G_vigor"]["noise_floor_temp_lift"]` field, and even under a worst-case SD-069 recording-semantics change, `T1P0` (phasic-off) alone carries the 1.0 -> 0.0 contrast. The recording-artifact hypothesis is refuted.
- *Is "C1/C2 unchanged from 779a" actually true?* Yes -- `_seed_effects` is **line-for-line identical** across the two drivers.
- *Is the starvation refutation fair?* Yes, and understated -- see section 2.

**What was contested, and it changes the repair.** The verifier confirmed fan-out **H2** in source and reproduced it with the real functions, at zero behavioural cost. Consequences, all applied above:

1. **Section 6 asserted the opposite of the truth** -- "harmless for this failure", "invisible to `_restore_cached_surface`". The warmup machinery *is* the cause, and the restore *overwrites* the regulator rather than failing to see it. Rewritten.
2. **`substrate_paths` cited a symbol that does not exist** (`agent.py::_curiosity_noise_floor_temperature` -- `grep` exit 1) and pointed a priority-1 `corrupting` repair at **healthy `ree_core` code**. The fault is in `experiments/_lib/probe_warmup.py` plus the driver, which is where the entry now points -- and, per this artifact's own pre-registered contingency, governance should prefer **amending SD-PROBE-WARMUP** over creating a new SD.
3. **The fan-out is withdrawn** as resolved-before-queuing, and with it the hypothesis-ledger append.
4. **A withdrawn argument was withdrawn for a locally-correct but incomplete reason** -- see `arguments_withdrawn[1].withdrawal_CORRECTED_after_red_team`. "NoiseFloor is stateless, so a cold regulator lifts identically" is true and does refute the stated hypothesis; what it missed is that the restore does not leave the regulator cold, it writes `None` over it.

**Hygiene corrections applied:** the 779a `S_sustained_entropy` range was quoted as 0.29-0.76; the actual range is **0.146-0.849**. And the headline "50x" collapse is contaminated by a ~5x warmup-driven compression of the entropy scale -- the clean, scale-free statement is the lift, 1.0 -> 0.0.

**Not checked by either party:** no real-experiment re-run (the confirmation is a synthetic reproduction plus source reads); the prior ceiling-autopsy files were taken at face value.
