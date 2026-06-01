---
nav_exclude: true
---

# SD-037 Axis (a) Phase 2 — Consumer-Input-Threshold Recalibration Block

**Plan-of-record:** `evidence/planning/sd_037_axis_a_consumer_input_recalibration_plan.md` (4-phase plan; this doc is the Phase 2 output).
**Input manifest:** `evidence/experiments/v3_exq_620_sd037_axis_a_phase1_consumer_input_distributions_20260531T175254Z_v3.json` (V3-EXQ-620, PASS at manifest gate, 2026-05-31T17:52:54Z).
**Authored:** 2026-06-01. Planning-only landing; no ree-v3 code edits; no claims.yaml edits; no experiment queue edits.
**Sibling claims:** SD-037 (`broadcast.override_regulator`), MECH-280 (PAG LH-override projection), MECH-281 (orexin drive-arousal coupling).

---

## 1. Headline finding

**Phase 1 returned six identically-zero distributions.** Pooled across 3 seeds (n=2939 eval-window steps post-warmup, fishtank baseline, broadcast OFF, all consumer cascade gains 0.0), every measured quantity that feeds a consumer-input gate is bit-zero at every percentile. `zero_fraction = 1.0` for all six quantities; `min = max = mean = std = 0.0` per seed and pooled.

The deterministic p70 recalibration rule (plan-doc §5) is **unmeetable across all four knobs** because the distribution it would map against has no upper tail — it has no signal at all. Lowering any threshold to p70 = 0.0 violates the plan-doc floor (0.05 / 0.05 / 0.05 / 0.1 / non-zero scale) and would produce always-on consumers detached from biological gating.

**Recommendation (this Phase 2):** Hold all four current defaults unchanged; route to axis (b) SD-029-style sustained-threat env curriculum (plan-doc §8, reserved fallback). Axis (a) cannot succeed on fishtank-baseline data because fishtank baseline produces no consumer-input signal whatsoever.

---

## 2. Source distributions (Phase 1 manifest, pooled across seeds 42, 7, 19)

All six quantities show identical statistics — pooled across the eval window for the three seeds (1514 + 76 + 1349 = 2939 steps).

| Quantity | n | min | median (p50) | mean | p70 | max | zero_fraction |
|---|---:|---:|---:|---:|---:|---:|---:|
| `z_harm_a_norm` | 2939 | 0.0 | 0.0 | 0.0 | **0.0** | 0.0 | **1.000** |
| `cea_low_freq_magnitude` | 2939 | 0.0 | 0.0 | 0.0 | **0.0** | 0.0 | **1.000** |
| `z_harm_a_instant_val` | 2939 | 0.0 | 0.0 | 0.0 | **0.0** | 0.0 | **1.000** |
| `pag_sustained_product` | 2939 | 0.0 | 0.0 | 0.0 | **0.0** | 0.0 | **1.000** |
| `bla_pe_magnitude` | 2939 | 0.0 | 0.0 | 0.0 | **0.0** | 0.0 | **1.000** |
| `dacc_pe` | 2939 | 0.0 | 0.0 | 0.0 | **0.0** | 0.0 | **1.000** |

Per-seed view is identical: seed 42 / 7 / 19 each have `zero_fraction = 1.0` on each quantity, and every reported percentile (p10, p25, p50, p70, p80, p90, p95, p99) is 0.0. The 20-bin histogram in the manifest deposits the entire mass in the central bin around zero. No tail. No nonzero observation in any of the 17 634 (2939 × 6) sample points.

This is not a sampling artefact at the upper percentiles — there is no nonzero observation anywhere in the distribution.

---

## 3. Per-knob computed thresholds

Plan-doc §5 specifies: primary value = p70 pooled; floors and ceilings as given; if p70 falls below the floor, leave default unchanged and flag for axis (b). All four knobs hit the floor-violation path.

### 3.1 `BLAConfig.arousal_threshold_on`

| | value |
|---|---|
| Source distribution | pooled `z_harm_a_norm` (primary per plan-doc; `bla_pe_magnitude` was the named secondary) |
| Source stats | n=2939, min=0.0, median=0.0, mean=0.0, **p70=0.0**, max=0.0, zero_fraction=1.0 |
| p60 sensitivity | 0.0 |
| p80 sensitivity | 0.0 |
| Plan-doc floor | 0.05 |
| Plan-doc ceiling | 0.4 (current default) |
| **Recommended override** | **none — hold default 0.4; flag for axis (b)** |
| Plan-doc-side note | Primary distribution chosen: `z_harm_a_norm`. The plan-doc names `z_harm_a_norm OR bla_pe_magnitude` as the BLA gate input; both are identically 0.0 in Phase 1, so the choice does not affect the computed threshold. `z_harm_a_norm` is the more direct biological input (Roozendaal inverted-U on-threshold reads arousal level, not PE), so we treat it as primary and `bla_pe_magnitude` as the cross-check. |

### 3.2 `CeAConfig.fast_route_threshold`

| | value |
|---|---|
| Source distribution | pooled `cea_low_freq_magnitude` |
| Source stats | n=2939, min=0.0, median=0.0, mean=0.0, **p70=0.0**, max=0.0, zero_fraction=1.0 |
| p60 sensitivity | 0.0 |
| p80 sensitivity | 0.0 |
| Plan-doc floor | 0.05 |
| Plan-doc ceiling | 0.5 (current default) |
| **Recommended override** | **none — hold default 0.5; flag for axis (b)** |

### 3.3 `PAGFreezeGateConfig.duration_input_threshold` (lower of PAG's two thresholds)

| | value |
|---|---|
| Source distribution | pooled `z_harm_a_instant_val` |
| Source stats | n=2939, min=0.0, median=0.0, mean=0.0, **p70=0.0**, max=0.0, zero_fraction=1.0 |
| p60 sensitivity | 0.0 |
| p80 sensitivity | 0.0 |
| Plan-doc floor | 0.05 |
| Plan-doc ceiling | 0.4 (current default) |
| **Recommended override** | **none — hold default 0.4; flag for axis (b)** |

### 3.4 `PAGFreezeGateConfig.theta_freeze` (upper of PAG's two thresholds; duration-integral commit condition)

| | value |
|---|---|
| Source distribution | pooled `pag_sustained_product` (the running `z_harm_a * duration_above_duration_input_threshold` integral PAG accumulates) |
| Source stats | n=2939, min=0.0, median=0.0, mean=0.0, **p70=0.0**, max=0.0, zero_fraction=1.0 |
| p60 sensitivity | 0.0 |
| p80 sensitivity | 0.0 |
| Plan-doc floor | 0.1 |
| Plan-doc ceiling | 2.0 (current default) |
| **Recommended override** | **none — hold default 2.0; flag for axis (b)** |
| Plan-doc-side note | Plan-doc §5 also calls for recomputing `theta_freeze` against the running product under the **recalibrated** `duration_input_threshold`. Because the underlying per-tick `z_harm_a` is identically 0.0, no choice of `duration_input_threshold` (including zero) produces a nonzero running product — the multiplicand is zero. The PAG channel is exactly the case the plan-doc anticipated in §6 FAIL-route prose: "duration above threshold may genuinely be zero in steady-state fishtank". |

### 3.5 `DACCConfig.dacc_precision_scale` (rescale, not threshold)

| | value |
|---|---|
| Source distribution | pooled `dacc_pe` (PE magnitude `||z_harm_a(t) - E2_harm_a(z_harm_a(t-1), a(t-1))||`) |
| Source stats | n=2939, min=0.0, median=0.0, mean=0.0, **p70=0.0**, max=0.0, zero_fraction=1.0 |
| Plan-doc rescale rule | `dacc_precision_scale = (dacc_bias_max_abs / 2) / p70(dacc_pe_magnitude)` |
| **Recommended override** | **none — division by zero; hold default; flag for axis (b)** |
| Plan-doc-side note | The Phase 1 run set `dacc_bias_max_abs = 0.1` and `dacc_weight = 0.1` (per the script's diagnostic preset, plan-doc §10 risk item 3). Even with `dacc_bias_max_abs > 0` ensured at the experiment-config layer, the PE distribution itself is identically zero, so no `dacc_precision_scale` choice can map an upper-tail PE into a non-zero bias — the upper tail is zero. |

---

## 4. Override block (Python dict, ready to paste into Phase 3 / Phase 4 scripts)

Provided for **completeness of the Phase 2 contract** (the plan-doc §5 requires this block to exist). Under the empirically-derived recommendation, the per-experiment override block is **empty** — every knob is held at its current default. Phase 3 / Phase 4 should NOT consume this block as written; they should consume the axis (b) prerequisite instead (see §6).

```python
# SD-037 axis (a) Phase 2 recalibration overrides.
# AUTHORITATIVE STATE: axis (a) is empirically unmeetable on fishtank baseline.
# All four knobs hold their current ree_core defaults. Do NOT apply this block
# to Phase 3 / Phase 4 scripts without first running Phase 1b (hazard-engaging
# probe env). See substrate_queue.json SD-037.metric_trajectory.next_step.

SD037_AXIS_A_PHASE2_OVERRIDES = {
    # BLAConfig.arousal_threshold_on
    "bla_arousal_threshold_on": None,            # hold default 0.4
    # CeAConfig.fast_route_threshold
    "cea_fast_route_threshold": None,            # hold default 0.5
    # PAGFreezeGateConfig.duration_input_threshold (lower of PAG's two)
    "pag_duration_input_threshold": None,        # hold default 0.4
    # PAGFreezeGateConfig.theta_freeze (upper of PAG's two; duration integral)
    "pag_theta_freeze": None,                    # hold default 2.0
    # DACCConfig.dacc_precision_scale (rescale parameter, not threshold)
    "dacc_precision_scale": None,                # hold default
}

SD037_AXIS_A_PHASE2_FLAGS = {
    "axis_a_status": "empirically_unmeetable",
    "reason": (
        "Phase 1 V3-EXQ-620 pooled n=2939 zero across all six consumer-input "
        "quantities; p70 == 0.0 < plan-doc floor for every knob; recalibration "
        "would require always-on consumers (detached from biological gating)."
    ),
    "route_to": "axis_b_sustained_threat_env_curriculum",
    "prerequisite_for_phase2_retry": "phase_1b_hazard_engaging_probe_env",
}
```

For the contracted-but-unfilled case, the override dict semantics: `None` means "fall through to the consumer module's `ree_core` default at runtime"; the experiment script should not apply a kwarg override. The block is intentionally inert.

---

## 5. Per-knob caveats and which fallback path applies

| Knob | Phase 1 distribution character | Phase 2 caveat | Axis-(a) sensitivity sweep useful? | Axis-(b) routing recommended? |
|---|---|---|---|---|
| `BLAConfig.arousal_threshold_on` | pinned-zero, no tail | p60/p80 also zero — no within-axis-(a) recovery | No | Yes |
| `CeAConfig.fast_route_threshold` | pinned-zero, no tail | p60/p80 also zero | No | Yes |
| `PAGFreezeGateConfig.duration_input_threshold` | pinned-zero (z_harm_a_instant_val never nonzero) | p60/p80 also zero | No | Yes (cleanest case — plan-doc §6 explicitly flagged this for axis (b)) |
| `PAGFreezeGateConfig.theta_freeze` | pinned-zero (running product is multiplicand-of-zero) | Recomputing under any duration_input_threshold yields zero | No | Yes |
| `DACCConfig.dacc_precision_scale` | pinned-zero PE (division-by-zero rescale) | dacc_bias_max_abs setting at script layer is moot when PE is zero | No | Yes |

The **uniform** "pinned-zero" character across all four knobs is the load-bearing observation. The plan-doc anticipated PAG specifically as the most likely single-knob failure for axis (a); the empirical result is that ALL FOUR knobs share the same failure mode. This makes the routing decision unambiguous.

---

## 6. Routing decision and prerequisite for Phase 2 retry

**Axis (a) verdict:** Phase 2 cannot produce per-experiment override values from V3-EXQ-620's Phase 1 manifest. Routing to axis (b) per plan-doc §8 trigger condition "Phase 3 verification clears 0 of 4" is short-circuited at Phase 2 — we never need to queue Phase 3 because the override block contains no overrides to verify.

**Prerequisite for any Phase 2 retry under axis (a):** A hazard-engaging probe env (a Phase 1b re-run of V3-EXQ-620's measurement protocol on a substrate that drives `z_harm_a` above zero in a measurable fraction of eval-window ticks). Candidate env knobs include increased `hazard_field_decay`, lower `hazard_harm` floor coupled with sustained exposure windows, or a sustained-threat curriculum analogous to SD-029's `scheduled_external_hazard`. The substrate-side prerequisite is itself the work of axis (b) — there is no axis-(a)-internal recovery path.

**Concrete next step (out of scope for this Phase 2 session):** Authoring an axis (b) sketch — either as an addendum to the recalibration plan-doc (Phase 1b prerequisite section) or as a fresh `/implement-substrate` session producing `evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md`. The user's session-routing call (per plan-doc §8 and the substrate_queue `metric_trajectory.next_step` 2026-05-31T19:15Z observation) is to do axis (b) next.

---

## 7. Phase 4 (V3-EXQ-483f) status

**Reserved per plan-doc §7; remains reserved.** V3-EXQ-483f cannot be queued from this Phase 2 output. The Phase 3 verification diagnostic is also not queueable from this Phase 2 output — there is nothing to verify. Both wait on axis (b).

---

## 8. Cross-references

- `evidence/planning/sd_037_axis_a_consumer_input_recalibration_plan.md` — plan-of-record (§5 Phase 2 rule, §6 FAIL routes, §8 axis (b) trigger, §10 risks).
- `evidence/experiments/v3_exq_620_sd037_axis_a_phase1_consumer_input_distributions_20260531T175254Z_v3.json` — input manifest.
- `evidence/planning/substrate_queue.json` SD-037 entry — `metric_trajectory.observations` 2026-05-31T19:15Z already noted the zero-baseline outcome at governance pass; this Phase 2 block formalises the per-knob computation backing that observation and amends the `implementation_log` to point at this doc.
- `evidence/planning/failure_autopsy_V3-EXQ-483e_2026-05-31.{md,json}` — origin of the consumer-input-threshold layer hypothesis.
- `docs/architecture/sd_037_broadcast_override_regulator.md` — substrate design; consumer-cascade amend section (2026-05-30).

---

## 9. Provenance

Authored 2026-06-01 in session `sd037-axis-a-phase2-recalibration-block-20260601T073706Z`. No ree-v3 code touched; no claims.yaml edits; no experiment_queue.json edits. Pathspec-limited REE_assembly master commit covers `evidence/planning/sd_037_axis_a_phase2_recalibration_block.md` + `evidence/planning/substrate_queue.json` only.
