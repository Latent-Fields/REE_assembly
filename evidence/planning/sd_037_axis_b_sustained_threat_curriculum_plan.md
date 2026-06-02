---
nav_exclude: true
---

# SD-037 Axis (b): Sustained-Threat Env Curriculum Plan

**Owner SD:** SD-037 (`broadcast.override_regulator`) -- substrate-ceiling at the consumer-input-threshold layer per V3-EXQ-483e autopsy + V3-EXQ-620 Phase 1 zero-distribution outcome.
**Sibling claims:** MECH-280 (PAG LH-override projection), MECH-281 (orexin drive-arousal coupling).
**Routing source:** Axis (a) consumer-input-threshold recalibration ruled empirically unmeetable on fishtank baseline (per `sd_037_axis_a_phase2_recalibration_block.md`, 2026-06-01). V3-EXQ-620 returned pooled n=2939 identically-zero distributions across all six consumer-input quantities; the deterministic p70 rule could not produce any per-knob override.
**Authored:** 2026-06-01. Plan is REE_assembly-only; no ree-v3 code in this session; no claims.yaml edits; no experiment_queue.json edits.
**Companion artefacts:**
- `evidence/planning/sd_037_axis_a_consumer_input_recalibration_plan.md` -- axis (a) plan-of-record (4 phases; §8 "axis (b) fallback" trigger conditions).
- `evidence/planning/sd_037_axis_a_phase2_recalibration_block.md` -- 2026-06-01 verdict: axis (a) empirically unmeetable; override block inert; route to axis (b).
- `evidence/planning/failure_autopsy_V3-EXQ-483e_2026-05-31.{md,json}` -- substrate-ceiling diagnosis that opened the two-axis fork.
- `docs/architecture/self_attribution_per_stream.md` -- SD-029 design doc (the existing `scheduled_external_hazard` curriculum mechanism in `CausalGridWorldV2`).
- `evidence/planning/substrate_queue.json` SD-037 entry (this plan referenced from `metric_trajectory.next_step` + new `implementation_log` line).

---

## 1. Headline routing decision: LIGHTER (env-kwargs-only)

**Decision: LIGHTER path -- env-kwargs-only on existing `CausalGridWorldV2` surface. No new ree-v3 module.**

### 1.1 Why lighter is feasible

The "heavier" framing in the activation prompt anticipated authoring a SD-029-style scheduler de novo. Inspection of `ree-v3/ree_core/environment/causal_grid_world.py` (lines 153-176, 1941-1988, 3669-3700) and `ree-v3/CLAUDE.md` §"SD-029: Balanced Hazard-Event Curriculum (2026-04-21)" confirms that **the SD-029-style scheduler already exists** in the substrate. It landed 2026-04-21 as part of the SD-029 self-attribution comparator implementation. The mechanism:

- `CausalGridWorldV2.__init__` kwargs (already present, defaults are no-op):
  - `scheduled_external_hazard_enabled: bool = False` -- master switch.
  - `scheduled_external_hazard_interval: int = 50` -- every N steps.
  - `scheduled_external_hazard_prob: float = 0.5` -- per-eligible-tick injection probability.
  - `scheduled_external_hazard_adjacent_only: bool = True` -- if True, requires an empty cell adjacent to agent; if no adjacency, that tick is skipped.
- Mechanism: when enabled, every `interval` steps with probability `prob`, an existing hazard is relocated (or a new one spawned) to a cell adjacent to the agent. The agent did not initiate the encounter, so subsequent harm is externally-caused.
- Env state and info keys already wired: `info["external_hazard_injected"]`, `info["external_hazard_event_count"]`, `self._external_hazard_event_count` per-episode counter.

There is therefore no new ree-v3 module to author for Phase 1b. The axis (b) deliverable is a tuned `ENV_FISHTANK_KWARGS` overlay that turns SD-029's curriculum on (plus, if needed, lifts `hazard_harm` above its tiny default of 0.05). Phase 1b is a re-run of V3-EXQ-620's measurement protocol against the new env config.

### 1.2 Sensitivity rationale: does env-kwarg-only fishtank plausibly drive z_harm_a above the lowest gate (BLAConfig.arousal_threshold_on = 0.4)?

The current `ENV_FISHTANK_KWARGS` defaults (from `ree-v3/experiments/_lib/goal_pipeline_tier1.py:75-95`):

```
size=10, num_hazards=3, num_resources=5, hazard_harm=0.05,
proximity_harm_scale=0.1, hazard_field_decay=0.5,
env_drift_interval=5, env_drift_prob=0.1, ...
```

`hazard_harm=0.05` with `proximity_harm_scale=0.1` and a sparse 3-hazard layout on a 10x10 grid produces tiny harm signals -- consistent with V3-EXQ-620's pooled-zero distributions (catatonic-lock baseline + small per-contact harm + low contact rate). The axis-(b) lifting levers are all already exposed:

| Lever | Default | Plausible Phase 1b setting | Effect on z_harm_a |
|---|---|---|---|
| `scheduled_external_hazard_enabled` | False | **True** | Forces externally-caused agent-adjacent hazard placements on schedule; bypasses the "agent never navigates to a hazard" failure mode of the monomodal / catatonic-lock baseline. |
| `scheduled_external_hazard_interval` | 50 | 20-30 | Reduces inter-injection gap so duration-above-threshold has a chance to accumulate at PAG's cadence. |
| `scheduled_external_hazard_prob` | 0.5 | 0.7-1.0 | Higher per-eligible-tick fire probability raises sustained hazard density. |
| `scheduled_external_hazard_adjacent_only` | True | True (keep -- biological motivation for SD-029 is adjacency) | Adjacency keeps the encounter spatially well-defined. |
| `hazard_harm` | 0.05 | 0.15-0.3 | 3-6x lift per contact; brings per-tick harm signal into the range that can drive `z_harm_a_norm` past BLA's 0.4 gate when integrated through the affective stream. |
| `proximity_harm_scale` | 0.1 | 0.2-0.3 | Scales the proximity-mediated harm field, raising z_harm_a between contacts (smooths the signal so PAG's duration integral has non-zero multiplicand outside contact-step spikes). |
| `hazard_field_decay` | 0.5 | hold (0.5) | Decay rate of the per-cell proximity contribution; raising it would narrow the field; holding preserves the spatial extent SD-022 / SD-029 substrate runs were designed against. |

Plausibility of the lower bound: At `hazard_harm=0.05` and `proximity_harm_scale=0.1`, the per-step harm at contact is roughly `hazard_harm * (1 - d/r_outer)**2 * scale` -- a maximum of order 0.05 in the affective-stream input, and that maximum is rare (requires d=0 in proximity terms). The affective stream's normalised output `z_harm_a_norm` integrates this over the `harm_history_len=10` buffer; even continuous contact would saturate well below the 0.4 BLA gate at default magnitudes. Lifting `hazard_harm` to 0.2-0.3 (a 4-6x increase) brings the per-contact upper bound into the 0.2-0.3 range and lets the affective integrator carry the running norm into the 0.4-0.6 range on contact-heavy windows. The 0.5 CeA `fast_route_threshold` and the 0.4 PAG `duration_input_threshold` then become reachable with the scheduled-injection curriculum providing sustained windows of contact-adjacent harm.

PAG's `theta_freeze=2.0` is the duration-integral commit gate: `z_harm_a * duration_above_duration_input_threshold > 2.0`. With `duration_input_threshold=0.4` and a sustained injection window of order 10-20 ticks holding `z_harm_a ~ 0.5`, the running product reaches `0.5 * 10 = 5.0` to `0.5 * 20 = 10.0` -- comfortably above theta_freeze. PAG's freeze-commit channel becomes engageable on env-kwarg-only fishtank.

**Verdict: the existing env-kwarg surface is plausibly sufficient. The lighter path is the right route.**

### 1.3 Why the heavier path is not needed

The "heavier" framing -- authoring a fresh `ree_core/curriculum/` or `ree_core/environment/` scheduler -- would duplicate SD-029's already-landed mechanism. SD-029 was specifically designed to deliver this exact substrate property (forced adjacency-injected hazards on a deterministic schedule). The only reason axis (b) was reserved as the heavier-path fallback in the axis-(a) plan-doc §8 was that the planning author did not enumerate SD-029's env-kwarg surface at that time. Re-using SD-029 is the architecturally-coherent choice and avoids reimplementing a substrate primitive.

### 1.4 What this decision commits to

- Phase 1b is the same script structure as V3-EXQ-620 with a tuned `ENV_FISHTANK_KWARGS` overlay; the per-step measurement protocol is unchanged.
- No new ree-v3 module. No new claims.yaml entries. No SD-029 design-doc amendments (SD-029 already covers the mechanism; it does not need axis-(b)-specific framing because the use here is curriculum re-application, not a new substrate property).
- The override values in §2 are TARGETS, not commitments -- Phase 1b will measure the empirical distributions under the tuned env, and Phase 2 (re-application of the p70 rule from axis (a)) computes the actual recalibration values from those distributions.

---

## 2. Target env behaviour: z_harm_a windows that clear the four consumer-input gates jointly

Goal: a `z_harm_a` distribution under the tuned env that has measurable upper-tail mass crossing each of the four consumer-input gates **simultaneously enough** for the cascade to engage. The acceptance is not "every tick crosses every gate" -- biologically, the gates fire on different timescales (BLA on arousal level, CeA on low-frequency component, PAG on duration integral, dACC on PE magnitude). The acceptance is **non-zero distributions** at the relevant percentile under fishtank-baseline-but-curriculum-engaged.

### 2.1 Per-gate target ranges

Re-using the per-knob floor/ceiling table from `sd_037_axis_a_consumer_input_recalibration_plan.md` §5 inverted into env-side targets:

| Gate (knob default) | Quantity feeding the gate | Phase-1b target (pooled across seeds, eval-window) | Why this target |
|---|---|---|---|
| `BLAConfig.arousal_threshold_on = 0.4` | `z_harm_a_norm` | p70 of `z_harm_a_norm` distribution >= 0.05 (the plan-doc floor); p90 >= 0.4 (so the upper-tail crosses the BLA gate on a measurable minority of ticks) | The p70 floor satisfies the axis-(a) Phase 2 recalibration rule's lower bound; the p90 crossing the default 0.4 gate means even WITHOUT recalibration BLA fires on the upper 10% of ticks. |
| `CeAConfig.fast_route_threshold = 0.5` | `cea_low_freq_magnitude` (`|LowFreq(z_harm_a)|`) | p70 of `cea_low_freq_magnitude` >= 0.05; p80 >= 0.5 | Low-frequency component lags the raw signal; target slightly looser at p70 but the same p80 default-gate-crossing requirement. |
| `PAGFreezeGateConfig.duration_input_threshold = 0.4` (lower of PAG's two) | `z_harm_a_instant_val` | p70 of `z_harm_a_instant_val` >= 0.05; at least one sustained run (10+ consecutive ticks) per seed where `z_harm_a > 0.4` | Duration-integral commit requires a sustained window, not just upper-tail density. |
| `PAGFreezeGateConfig.theta_freeze = 2.0` (upper of PAG's two) | `pag_sustained_product` (`z_harm_a * duration_above_duration_input_threshold`) | p70 of the running product >= 0.1 (the plan-doc floor); p95 >= 2.0 in at least 2/3 seeds | Theta_freeze commit fires on rare upper-tail mass; a p95 crossing means PAG commits at least once per episode in the majority of seeds. |
| `dACCConfig.dacc_precision_scale` (rescale, not threshold) | `dacc_pe` (`||z_harm_a(t) - E2_harm_a(z_harm_a(t-1), a(t-1))||`) | p70 of `dacc_pe` >= 0.01 (well above the divide-by-zero floor) | Once PE is non-zero, the rescale rule from axis-(a) Phase 2 §3.5 can compute a finite `dacc_precision_scale = (dacc_bias_max_abs / 2) / p70(dacc_pe)`. |
| (cross-check) `bla_pe_magnitude` (BLA's own internal PE channel) | `bla_pe_magnitude` | p70 >= 0.01 | Cross-check on the BLA PE channel which is mathematically related to but routing-distinct from the dACC PE. |

### 2.2 Joint-clearance heuristic

A Phase 1b PASS (per §3.4 below) does NOT require all six quantities to clear their target percentiles simultaneously. The acceptance gate is **non-zero distributions in >=2/3 seeds with at least one sustained window per seed**. The p90 / p95 / p80 default-gate-crossing targets above are stretch goals that determine whether Phase 3 verification can be skipped (if the default gates are already cleared by the env-engagement alone, axis-(a) Phase 2 recalibration becomes unnecessary -- the consumer cascade can engage at current defaults).

### 2.3 What sustained means here

"Sustained" follows PAG's biological gating: a run of >=10 consecutive ticks where `z_harm_a > 0.4` (the default `duration_input_threshold`). This is the minimum window that makes the duration-integral commit pathway diagnostically interesting. Shorter windows still produce non-zero distributions in the other consumers (BLA / CeA / dACC) but fail to engage PAG -- which is the cleanest single-channel diagnostic for whether axis (b) succeeded at the duration-integral layer (per axis-(a) plan-doc §6 "PAG-specific failure mode" prose).

---

## 3. Phase 1b diagnostic design

### 3.1 Run shape

- **Script:** New experiment script under `ree-v3/experiments/` (filename TBD by the /queue-experiment session; suggested form `v3_exq_NNN_sd037_axis_b_phase1b_consumer_input_distributions_sustained_threat.py`).
- **Substrate flags:** Identical to V3-EXQ-620 -- SD-036 + MECH-279 ON, `use_pag_freeze_gate=True`, `use_gabaergic_decay=True`, `use_salience_coordinator=True`, `use_broadcast_override=False` (broadcast OFF for the measurement; broadcast ON is reserved for Phase 4 V3-EXQ-483f). Modules instantiated: BLA + CeA + dACC + PAGFreezeGate all enabled at CURRENT defaults (no recalibration overrides). `dacc_bias_max_abs=0.1` and `dacc_weight=0.1` (per V3-EXQ-620's diagnostic preset, axis-(a) plan-doc §10 risk item 3).
- **Env config:** TUNED `ENV_FISHTANK_KWARGS` overlay with SD-029 curriculum engaged. Suggested Phase-1b values:
  - `scheduled_external_hazard_enabled=True`
  - `scheduled_external_hazard_interval=20`  (every 20 steps eligible)
  - `scheduled_external_hazard_prob=0.7`     (high per-eligible-tick fire rate)
  - `scheduled_external_hazard_adjacent_only=True`  (biological motivation; SD-029 default)
  - `hazard_harm=0.2`  (4x lift over default 0.05)
  - `proximity_harm_scale=0.2`  (2x lift; smooths inter-contact baseline)
  - All other `ENV_FISHTANK_KWARGS` defaults unchanged.
- **Seeds:** 42, 7, 19 (matches V3-EXQ-620 for direct comparability).
- **Phasing + step counts:** identical to V3-EXQ-620 (same warmup + eval window). The Phase 1b script must NOT hard-code step counts; it reuses V3-EXQ-620's protocol exactly.

### 3.2 Quantities to log per step

**Identical to V3-EXQ-620**, lifted verbatim from axis-(a) plan-doc §4:

1. `z_harm_a_norm = torch.linalg.norm(z_harm_a)`
2. `lowfreq_z_harm_a_norm` (the rolling-window low-frequency component from `cea.py`'s internal smoothing)
3. `z_harm_a_instant_val` (per-tick scalar for the PAG `duration_above_threshold` accumulator)
4. `pag_sustained_product` (the running `z_harm_a * duration_above_duration_input_threshold` at PAG's update cadence)
5. `dacc_pe_magnitude` (recomputed in the diagnostic)
6. `bla_pe_magnitude` (BLAAnalog's own `_last_pe_magnitude`)

**Distributions emitted per quantity, per seed, and pooled across seeds:**
- min, max, mean, std.
- Percentiles: 10, 25, 50, 70, 80, 90, 95, 99.
- Histogram with 20 bins from min to max.
- Fraction of steps at exactly zero (the "dead-floor mass").

**Plus -- sustained-window summary (NEW for Phase 1b):**
- Per seed: number of runs of >=10 consecutive ticks where `z_harm_a_instant_val > 0.4`. Total duration of all such runs. Maximum single-run length.
- Per seed: `external_hazard_event_count` at end of eval window (sanity check that SD-029 curriculum fired as configured).

### 3.3 Output artefacts

- Standard V3 experiment manifest: `evidence/experiments/v3_exq_<NNN>_sd037_axis_b_phase1b_consumer_input_distributions_sustained_threat_<TS>_v3.json`. `claim_ids=[]`; `experiment_purpose=diagnostic`. PASS at manifest gate = manifest emitted with all six quantity distributions populated AND the sustained-window summary block.
- Plan-side summary at `evidence/planning/sd037_axis_b_consumer_input_distributions_<TS>.md` written by the diagnostic script's post-run analysis block (mirrors V3-EXQ-620's plan-side markdown summary).

### 3.4 Acceptance gate

**Substrate-readiness PASS:**
- `external_hazard_event_count > 0` in 3/3 seeds (SD-029 curriculum confirmed firing).
- `zero_fraction < 1.0` on `z_harm_a_norm` in >=2/3 seeds (non-zero distributions).
- At least one sustained run (>=10 consecutive ticks with `z_harm_a > 0.4`) per seed in >=2/3 seeds.

**Substrate-readiness FAIL routes:**
- `external_hazard_event_count = 0` in any seed -> SD-029 curriculum knob mis-applied; fix env config and re-run (not a substrate failure).
- `zero_fraction = 1.0` on `z_harm_a_norm` despite `external_hazard_event_count > 0` -> the SD-029 injection is firing but harm magnitudes are still below the affective-stream noise floor. Escalate to §5 (heavier env-kwarg sweep or escalation to a true heavier path).
- `zero_fraction < 1.0` but no sustained runs (all upper-tail mass is single-tick spikes) -> PAG-specific failure mode flagged in axis-(a) plan-doc §6; escalate to §5 fallback or accept that the PAG channel will need a separate substrate-level commitment.

---

## 4. Post-Phase-1b path: re-application of the Phase 2 / Phase 3 / Phase 4 chip sequence

Once Phase 1b PASSes its substrate-readiness gate, the entire axis-(a) Phase 2 / Phase 3 / Phase 4 sequence re-applies on the new substrate. The chip sequence is identical; only the input distributions change.

### 4.1 Phase 2 (recalibration block) re-application

Inputs:
- Phase 1b manifest (replacing V3-EXQ-620's).

Process: identical to axis-(a) Phase 2 -- compute p70 per knob against the new pooled distributions; apply floors and ceilings from the axis-(a) plan-doc §5 table; emit a per-experiment override block as `evidence/planning/sd_037_axis_b_recalibration_overrides_<TS>.json`.

Expected output: a non-empty override block (in contrast to axis-(a)'s inert block). The exact values depend on the empirical distributions, but with the §1.2 sensitivity rationale satisfied, the per-knob computed thresholds should fall in the 0.05-0.4 range for BLA / CeA / PAG duration and in the 0.05-2.0 range for `pag_sustained_product`. The `dacc_precision_scale` rescale becomes finite (no divide-by-zero).

**Sensitivity sweep (within axis (b)):** if Phase 3 verification fails with p70, re-apply the axis-(a) p60 / p80 sweep on the new Phase 1b distributions before escalating to §5.

### 4.2 Phase 3 (verification diagnostic) re-application

Identical to axis-(a) Phase 3: same metric set, same 4-arm-less single-arm config (broadcast OFF, recalibrated thresholds ON), same acceptance gate (4/4 consumers fire on >=2/3 seeds with peak > 0).

### 4.3 Phase 4 (V3-EXQ-483f) re-application

Reserved per axis-(a) plan-doc §7. The Phase 4 experiment design is identical to V3-EXQ-483e's 4-arm 2x2 factorial (OFF_OFF / ON_OFF / OFF_ON / ON_ON, 3 seeds), but on the axis-(b)-recalibrated substrate. Acceptance contract unchanged from 483e (C1 substrate-readiness + C2 cascade-engagement ratios + C3 PRIMARY goal_norm_peak lift + C4 action-counts TV divergence).

A V3-EXQ-483f PASS would resolve `pending_retest_after_substrate=true` on SD-037 / MECH-280 / MECH-281 and route to governance for promotion candidacy. A V3-EXQ-483f FAIL on the axis-(b) substrate would be a load-bearing falsification across BOTH axes: the cascade still cannot engage even with sustained-threat windows engaging the upstream signal AND the consumer-input thresholds cleared. That FAIL would route to MECH-295 axis or to env redesign at a level above current curriculum extensions.

---

## 5. Failure modes: what to do if Phase 1b still returns zeroes (or partial zeroes)

### 5.1 SD-029 injection fires but z_harm_a still pinned at zero

Diagnosis: the per-contact harm magnitude is too small even with `hazard_harm=0.2`. The affective stream may have its own filtering or normalisation that suppresses sub-threshold inputs.

Response (still env-kwarg-only):
- Lift `hazard_harm` further (0.3, 0.4, 0.5).
- Lift `proximity_harm_scale` to 0.3-0.4.
- Reduce `hazard_field_decay` to 0.3 (slower spatial falloff so cells further from the agent contribute more harm signal).
- If still zero after these tweaks, suspect upstream filtering in `affective_stream.py` or `harm_history_len`-based smoothing -- this becomes a substrate diagnostic question, not a curriculum question. Route to a separate /diagnose-errors session.

### 5.2 z_harm_a lifts but no sustained runs

Diagnosis: per-injection windows are too short (single-tick contact-spikes rather than sustained co-location).

Response (still env-kwarg-only):
- Reduce `env_drift_interval` from 5 to 2 or 1 so the hazard does not drift away as quickly after injection.
- Reduce `env_drift_prob` from 0.1 to 0.05 (suppresses spontaneous drift between injections).
- These two combined keep the SD-029-injected hazard adjacent to the agent for longer windows.

If still no sustained runs: this is the PAG-specific failure mode anticipated in axis-(a) plan-doc §6. Accept that the PAG channel may require a future heavier-path scheduler explicitly designed for sustained-threat windows (not just adjacency-injection). At that point, axis (c) -- a new SD-NNN sustained-threat scheduler distinct from SD-029's instantaneous adjacency-injection -- becomes the next move. THIS plan does not author it.

### 5.3 dACC PE remains zero even with non-zero z_harm_a

Diagnosis: E2_harm_a's forward-model prediction is tracking z_harm_a perfectly even on injection ticks (no novelty -> no PE). This is plausible because SD-029 injections are deterministic relative to the agent's location, so the forward-model can in principle learn to predict them given enough warmup.

Response:
- Increase `scheduled_external_hazard_prob` from 0.7 to a stochastic 0.3-0.5 with a non-uniform interval (e.g., randomise `scheduled_external_hazard_interval` per episode -- this would be a small Phase-1b script-level change, NOT a ree-v3 substrate change). Stochasticity in the curriculum maintains PE.
- If E2_harm_a's prediction is too tight regardless, this becomes an E2_harm_a forward-model investigation -- separate from axis (b).

### 5.4 Env-kwarg surface exhausted

Trigger: §5.1, §5.2, and §5.3 responses all fail in combination.

Routing: axis (c) -- a new SD-NNN sustained-threat scheduler authored under /implement-substrate as the actual heavier path. SD-029's adjacency-injection is necessary but not sufficient; a sustained-threat curriculum (deterministic threat windows of fixed duration over which `z_harm_a` is forced to remain elevated -- a temporal counterpart to SD-029's spatial mechanism) becomes the new substrate work. THIS plan does not author it. Document the failure mode in a Phase 1b failure autopsy and route to /implement-substrate for axis (c).

---

## 6. Cross-references

- `evidence/planning/sd_037_axis_a_consumer_input_recalibration_plan.md` -- axis (a) plan-of-record. §8 originally named this axis as the heavier fallback; this plan re-classifies it as the lighter path because SD-029 is already landed.
- `evidence/planning/sd_037_axis_a_phase2_recalibration_block.md` -- 2026-06-01 verdict that triggered this plan. §6 of that doc explicitly names a "Phase 1b hazard-engaging probe env" as the substrate-side prerequisite -- the present plan IS that prerequisite, made precise.
- `evidence/planning/failure_autopsy_V3-EXQ-483e_2026-05-31.{md,json}` -- the substrate-ceiling autopsy that opened the two-axis fork at the consumer-input-threshold layer.
- `docs/architecture/self_attribution_per_stream.md` -- SD-029 design doc (§"V3 Implementation Target (SD-029)", §"First Test for SD-029"). Confirms `scheduled_external_hazard_enabled` is the substrate-already-implemented mechanism the present plan re-uses.
- `ree-v3/ree_core/environment/causal_grid_world.py` -- SD-029 implementation (lines 153-176 config docstring; 1941-1988 step()-side injection gate; 3669-3700 `_inject_external_hazard` helper).
- `ree-v3/CLAUDE.md` §"SD-029: Balanced Hazard-Event Curriculum (2026-04-21)" -- substrate implementation log for SD-029.
- `ree-v3/experiments/_lib/goal_pipeline_tier1.py:75-95` -- `ENV_FISHTANK_KWARGS` definition the Phase 1b script overlays.
- `ree-v3/experiments/v3_exq_620_sd037_axis_a_phase1_consumer_input_distributions.py` -- the Phase 1 script that Phase 1b is a direct re-run of with a tuned env overlay.
- `evidence/planning/substrate_queue.json` SD-037 entry -- `metric_trajectory.next_step` (2026-05-31T19:15Z) and `current_blocker` updated to point at this plan + Phase 1b.

---

## 7. Out-of-scope for this plan

- No ree-v3 code edits in this session.
- No /queue-experiment call (Phase 1b script + queue entry are a separate follow-on session).
- No claims.yaml edits. SD-037 / MECH-280 / MECH-281 keep `pending_retest_after_substrate=true` and `epistemic_category=substrate_ceiling` from the 2026-05-31 governance pass.
- No SD-029 design-doc amendments (the use here is curriculum re-application, not a new substrate property).
- No new SD-NNN registration. Axis (c) (if needed per §5.4) would register its own SD in a future /implement-substrate session.
- No default-flip on `ENV_FISHTANK_KWARGS` defaults (the curriculum knobs stay False-by-default in the library; the Phase 1b script applies a per-experiment overlay).

---

## 8. Risks and dependencies

- **§1.2 sensitivity argument is plausibility, not measurement.** The actual z_harm_a distribution under the tuned env is empirical. If §5.1's first response (`hazard_harm=0.3`) is insufficient, that is a real possibility -- the affective stream may have downstream filtering that suppresses signals below an absolute threshold independent of magnitude. The Phase 1b run will distinguish.
- **PAG sustained-window engagement is the hardest gate.** Among the four consumers, PAG's duration-integral commit (`z_harm_a * duration > 2.0`) is the most sensitive to the temporal structure of the curriculum, not just signal magnitude. SD-029's adjacency-injection produces co-location, which in the presence of `env_drift_interval=5` may still produce only short windows. §5.2 anticipates this; §5.4 is the explicit escalation if §5.2 also fails.
- **MECH-295 bridge dominance remains a downstream risk for Phase 4 C3_lift.** Axis (b) addresses the upstream signal magnitude problem; it does NOT address the MECH-295-bridge-dominates-effective_drive observation from the 483d autopsy. A C2 PASS + C3 FAIL in Phase 4 on the axis-(b) substrate would route to MECH-295 axis, NOT re-open axis (b).
- **The dACC PE channel may need stochasticity.** §5.3 anticipates that deterministic injections become predictable to E2_harm_a; the Phase 1b script may need a small stochasticity layer (interval/prob randomisation per episode) to keep PE non-zero. This is a Phase-1b script-level concern, not a ree-v3 substrate concern.
- **Concurrent session siblings on substrate_queue.json.** This planning session edits one entry (SD-037). The substrate_queue file is high-contention; pathspec-limited commits + re-read-before-write keep us disjoint from other sessions editing other entries. Active claims at the time of this session: `igw-auto-igw-027-retest-after-substrate-mech-229-...` (no resource overlap), `queue-experiment-arc-068-mech-320-niv-salamone-...` (closed but recent; touched experiment_queue.json which this session does NOT).

---

## 9. Provenance

Authored 2026-06-01 in session `implement-substrate-sd037-axis-b-sustained-threat-curriculum-plan-20260601T074925Z`. No ree-v3 code touched; no claims.yaml edits; no experiment_queue.json edits. Pathspec-limited REE_assembly master commit covers `evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md` (NEW) + `evidence/planning/substrate_queue.json` (SD-037 entry amend) only. Next session: `/queue-experiment` for the Phase 1b diagnostic referencing this plan §3.

---

## 10. Phase 1b first-run result (V3-EXQ-625b, 2026-06-01)

**Status: §3.4 acceptance gate FAIL on C3 sustained-window axis (1/3 seeds).**

V3-EXQ-625b ran the Phase 1b diagnostic per §3 on `affective_harm_stream_enabled=True` (post-stream-off bug fix; supersedes V3-EXQ-625). `env_overlay_delta_vs_620`: `scheduled_external_hazard_enabled=True`, `interval=20`, `prob=0.7`, `adjacent_only=True`, `hazard_harm=0.2`, `proximity_harm_scale=0.2`. Sustained-window config: `z_threshold=0.4, min_run_len=10`.

- **C1 curriculum_firing** PASS 3/3 seeds (external_hazard_event_count seed 42=10, seed 7=45, seed 19=6).
- **C2 z_harm_a_nonzero** PASS 3/3 seeds (zero_fraction=0.0 per seed).
- **C3 sustained_window** FAIL 1/3 seeds: seed 42 `n_sustained_runs=0`, seed 7 `n_sustained_runs=1`, seed 19 `n_sustained_runs=0`. §3.4 requires ≥2/3 seeds with ≥1 sustained window.

Pooled z_harm_a_norm distribution: p70=0.43, p80=0.44, p90=0.44, p99=0.45. The upper tail clears the BLA arousal_threshold_on=0.4, but the signal does not stay above 0.4 for ≥10 consecutive ticks in 2/3 seeds. The `interval=20, prob=0.7` schedule produces isolated contact spikes rather than the sustained 10-20 tick windows §1.2 sensitivity-rationalised to drive PAG's `theta_freeze=2.0` duration-integral.

Routing (per §5 failure-mode ladder): both **§5.2 (interval shorter, prob higher)** and **§5.4 (relax sustained-window definition: lower z_threshold or shorter min_run_len)** are in scope. §5.1 magnitude lifts (`hazard_harm=0.3`) are not the primary lever because the magnitude floor IS being cleared at the per-tick level; the temporal-structure axis is the load-bearing one. Plan owner picks the §5.2/§5.4 axis when next-cycling the diagnostic. Manifest: `evidence/experiments/v3_exq_625b_sd037_axis_b_phase1b_consumer_input_distributions_sustained_threat_20260601T181233Z_v3.json`. Marked discussed in `review_tracker.json` 2026-06-02T05:23Z.
