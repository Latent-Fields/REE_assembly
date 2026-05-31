---
nav_exclude: true
---

# SD-037 Axis (a): Consumer-Input-Threshold Recalibration Plan

**Owner SD:** SD-037 (`broadcast.override_regulator`) — substrate-ceiling at the consumer-input-threshold layer per V3-EXQ-483e autopsy (2026-05-31).
**Sibling claims:** MECH-280 (PAG LH-override projection), MECH-281 (orexin drive-arousal coupling).
**Routing source:** IGW-20260531-001 (2026-05-31) selected axis (a) consumer-input-threshold recalibration as the next substrate work. Axis (b) SD-029-style sustained-threat env curriculum is reserved as fallback.
**Authored:** 2026-05-31. Plan is REE_assembly-only; no ree-v3 code in this session.
**Companion artefacts:**
- `evidence/planning/failure_autopsy_V3-EXQ-483e_2026-05-31.{md,json}`
- `docs/architecture/sd_037_broadcast_override_regulator.md`
- `evidence/planning/substrate_queue.json` (SD-037 entry, this plan referenced from `metric_trajectory.next_step` + new `recalibration_plan_doc` field)

---

## 1. Problem

V3-EXQ-483e (4-arm OFF_OFF / ON_OFF / OFF_ON / ON_ON, 3 seeds, PAG-engaging substrate via `use_gabaergic_decay=True` + `use_pag_freeze_gate=True` + `use_salience_coordinator=True`) FAILed all three discrimination criteria (C2_cascade_engagement, C3_lift_vs_baseline, C4_action_divergence). The SD-037 broadcast itself saturated correctly (`override_signal_nonzero_steps == total_eval_steps` in every ON_OFF / ON_ON seed). The four MECH-281 consumer cascade sites landed 2026-05-30 are fully wired (verified in activation-smoke). What did not fire:

- `bla_encoding_gain_peak = 0.0` across ALL 12 runs.
- `cea_mode_prior_peak = 0.0`, `cea_fast_prime_peak = 0.0` across ALL 12 runs.
- `pag_release_count_end = 0` across ALL 12 runs.
- `dacc_bias_nonzero_steps = 0` across ALL 12 runs.
- `beta_release_count = 0` across ALL 12 runs.
- `action_counts` bit-identical across all four arms within every seed.

`lateral_pfc_rule_state_norm_peak` was the only consumer that responded at all (1.08-1.18x across the cascade-engaged axis), but below the 1.5x C2 discrimination threshold. lateral_pfc is the only consumer site whose response does not require an input-side threshold crossing.

Mechanism diagnosed: SD-037's multiplicative gain pattern is `output * (1 + gain * override_signal)`. For three of the four motor-coupling consumers (BLA / CeA / PAG) and for the dACC PE-driven bias, the "output" is zero at baseline because each consumer's own input gate is not crossed by fishtank baseline signal magnitudes. Amplifying zero yields zero, no matter how saturated the broadcast.

---

## 2. The four input thresholds

Located in `ree-v3/ree_core/`:

| Consumer | Module | Config knob | Default | What it gates | Biological anchor |
|---|---|---|---|---|---|
| BLA | `amygdala/bla.py` | `BLAConfig.arousal_threshold_on` | 0.4 | `z_harm_a_norm >= threshold` -> `encoding_gain` lifts above 1.0 | Roozendaal inverted-U on-threshold |
| CeA | `amygdala/cea.py` | `CeAConfig.fast_route_threshold` | 0.5 | `|LowFreq(z_harm_a)| > threshold` -> mode_prior + fast_prime become non-zero | Mendez-Bertolo fast subcortical route |
| PAG | `pag/freeze_gate.py` | `PAGFreezeGateConfig.theta_freeze` + `duration_input_threshold` | 2.0 + 0.4 | Two-stage: (i) `z_harm_a > duration_input_threshold` accumulates time-above-threshold; (ii) `z_harm_a * duration_above > theta_freeze` -> freeze commit fires; PAG release tracks subsequent exits | Brandao / Wang-Lin PAG threat duration integration |
| dACC | `cingulate/dacc.py` | implicit PE floor; bias clipped by `dacc_bias_max_abs` | (dacc_bias_max_abs=0.0 default; live experiments set > 0) | PE-driven bias on E3 score reads from `pe = ||z_harm_a(t) - E2_harm_a(z_harm_a(t-1), a(t-1))||`. If `pe` is near-zero at baseline, the computed bias is near-zero before clip. | Behrens / Holroyd ACC-as-PE-magnitude |

The dACC case is slightly different from the other three: there is no single named threshold to lower; the issue is that the **PE magnitude itself** is near-zero at baseline because the substrate's affective stream does not move enough between adjacent ticks to produce a non-trivial residual against E2_harm_a's prediction. Recalibration for dACC therefore consists of (a) characterising the PE distribution under fishtank baseline and (b) ensuring the dACC's internal scaling (`dacc_precision_scale`, `dacc_bias_max_abs`) maps the upper tail of that distribution into a non-zero bias range — not lowering a threshold but rescaling the bias map. This is treated as a knob in the same plan, but the operation is "rescale" rather than "lower threshold".

---

## 3. Plan structure

Four phases. Phase 1 and Phase 3 are **substrate-readiness diagnostics** (claim_ids=[], `experiment_purpose=diagnostic`). Phase 2 is a deterministic recalibration rule that runs on the Phase-1 manifest. Phase 4 is the behavioural validation (V3-EXQ-483f), queued only if Phase 3 passes its acceptance gate.

```
Phase 1 (diagnostic)      Phase 2 (analysis)       Phase 3 (diagnostic)        Phase 4 (validation)
+-------------------+     +-------------------+    +-----------------------+   +-------------------+
| Log raw consumer- |     | Compute p70 per   |    | Re-run baseline with  |   | V3-EXQ-483f       |
| input distribs    | --> | knob; emit per-   | -> | recalibrated knobs    |-> | (queued via       |
| over fishtank     |     | experiment config |    | + verify consumer     |   |  /queue-experiment|
| baseline run      |     | override block    |    | output peaks > 0      |   |  AFTER Phase 3    |
+-------------------+     +-------------------+    +-----------------------+   |  PASS only)       |
                                                            |                  +-------------------+
                                                   FAIL ----+
                                                            v
                                                   Sweep p60/p80; if still
                                                   fails, route to axis (b)
                                                   SD-029-style env curriculum
```

---

## 4. Phase 1 — Substrate-readiness diagnostic (DESIGN here; QUEUE via /queue-experiment)

**Goal:** Measure the per-step distribution of every quantity that feeds a consumer-module input threshold, under the same fishtank baseline conditions V3-EXQ-483e ran on, with the broadcast OFF (so the measurement is of the agent's natural signal magnitudes, not amplified ones).

**Run shape:**

- Substrate: SD-036 + MECH-279 ON (matches 483e ARM_0 OFF_OFF except broadcast also OFF, all cascade gains 0.0). `use_pag_freeze_gate=True`, `use_gabaergic_decay=True`, `use_salience_coordinator=True`, `use_broadcast_override=False`.
- Modules instantiated: BLA + CeA + dACC + PAGFreezeGate all enabled (`use_dacc=True` non-negotiable — closes the V3-EXQ-483c-era oversight). All four kept at their CURRENT defaults during Phase 1; Phase 1 is a measurement pass, not a recalibration.
- Seeds: 42, 7, 19 (matches 483e for direct comparability of step counts).
- Step count: identical to 483e per-seed counts (1514 / 76 / 1349 if reproduced exactly; the Phase 1 script should not hard-code these, it should run the same warmup + eval window 483e used).
- Phasing: same as 483e (P0 warmup, P2 eval). Distributions accumulate across both, but the manifest reports them separately so any phase-specific tail behaviour is visible.

**Quantities to log per step:**

| Quantity | Source | Used by |
|---|---|---|
| `z_harm_a_norm = torch.linalg.norm(z_harm_a)` | latent stack | BLA arousal gate |
| `lowfreq_z_harm_a_norm` (the rolling-window low-frequency component that `cea.py` computes via its existing internal smoothing — invoke `CeAAnalog._compute_lowfreq(...)` or whatever the current method is, and log its norm) | cea.py | CeA fast-route gate |
| `z_harm_a_instant_val` | latent stack | PAG `duration_above_threshold` accumulator (per-tick scalar compared to `duration_input_threshold`) |
| `pag_sustained_product` = running `(z_harm_a * duration_above_duration_input_threshold)` at PAG's own update cadence | pag freeze_gate | PAG `theta_freeze` commit condition |
| `dacc_pe_magnitude = ||z_harm_a(t) - E2_harm_a(z_harm_a(t-1), a(t-1))||` | recomputed in the diagnostic | dACC PE input |
| `bla_pe_magnitude` (BLAAnalog's own `_last_pe_magnitude` after its internal recompute; biologically distinct from the dACC PE because of routing/timing but mathematically related) | bla.py | BLA PE channel |

Distributions emitted per quantity, per seed, and pooled across seeds:

- min, max, mean, std.
- Percentiles: 10, 25, 50, 70, 80, 90, 95, 99.
- Histogram with 20 bins from min to max.
- Fraction of steps at exactly zero (the "dead-floor mass").

**Output:**

- Standard V3 experiment manifest: `evidence/experiments/v3_exq_<NNN>_sd037_axis_a_phase1_consumer_input_distributions_<TS>_v3.json`. claim_ids=[]; `experiment_purpose=diagnostic`. PASS = manifest emitted with all six quantity distributions populated (no scientific PASS/FAIL — this is measurement).
- Plan-side artefact: a markdown summary at `evidence/planning/sd037_consumer_input_distributions_<TS>.md` written by the diagnostic script's post-run analysis block, summarising the percentile table per quantity per seed. This is the input to Phase 2.

**Out of scope for this planning session:** the actual script + queue entry. Both go through `/queue-experiment` in a subsequent session. The queue entry will reference this plan doc.

---

## 5. Phase 2 — Recalibration rule

Deterministic and stated up front so the recalibration is not a free parameter that drifts under fitting pressure.

**Rule (primary):** Set each threshold to the **70th percentile of its measured distribution at fishtank baseline** (pooled across the three seeds, post-warmup eval-window observations only).

Rationale per user direction: a percentile that "admits the upper tail" — high enough that the consumer fires on the genuinely-elevated signal regime rather than constantly, low enough that any signal lift driven by SD-037's broadcast (or by env enrichment in axis (b)) crosses it. The 70th percentile leaves the top 30% of natural baseline ticks above threshold; ON-arms then have headroom both to exceed that natural rate (via cascade amplification once SD-037 fires) and to maintain a discriminable contrast against the OFF baseline.

**Per knob:**

| Knob | Phase 2 value | Notes |
|---|---|---|
| `BLAConfig.arousal_threshold_on` | p70(z_harm_a_norm) | Floor at 0.05 to avoid degenerate "always-on"; ceiling at current default 0.4. If p70 > 0.4, leave default unchanged and flag for axis (b). |
| `CeAConfig.fast_route_threshold` | p70(lowfreq_z_harm_a_norm) | Floor at 0.05; ceiling at current default 0.5. |
| `PAGFreezeGateConfig.duration_input_threshold` | p70(z_harm_a_instant_val) | Floor at 0.05; ceiling at current default 0.4. This is the lower of PAG's two thresholds — it gates the duration accumulator. |
| `PAGFreezeGateConfig.theta_freeze` | p70(pag_sustained_product) under the recalibrated `duration_input_threshold` | Computed conditionally on the new `duration_input_threshold`; if Phase 1 logs the sustained product at the OLD threshold, Phase 2 needs to recompute (Phase 1 script logs both the raw per-tick `z_harm_a` and the running product, so the recomputation is offline). Floor at 0.1; ceiling at current default 2.0. |
| `DACCConfig.dacc_precision_scale` (rescale, not threshold) | computed so p70(dacc_pe_magnitude) maps to `dacc_bias_max_abs / 2` | Treats the upper-tail PE as producing a half-clipped bias; preserves the dACC's headroom. `dacc_bias_max_abs` itself must be set > 0 in the experiment config (separate gating issue from the threshold layer). |

**Sensitivity sweep (fallback within axis (a)):** If Phase 3 verification fails with p70, sweep to p60 (more permissive) and p80 (more conservative) — these are the next two percentiles to try before routing to axis (b). Each sweep point is a separate Phase-3 verification run.

**Phase 2 implementation:** Phase 2 is **not a code change to ree-v3 defaults**. It is a per-experiment override block that the Phase-3 / Phase-4 scripts apply. Default-flips to the consumer-module configs in `ree_core/utils/config.py` are deferred until behavioural validation (Phase 4) confirms the new values produce a discriminable cascade lever — premature default flips would contaminate other in-flight experiments measuring the pre-change baseline.

**MECH-094:** Recalibration does not introduce any new write path during simulation/replay; the existing `simulation_mode` gating on BLA/CeA/PAG is preserved by virtue of being a config-knob change only. No MECH-094 amend required.

**Phase 2 output:** a JSON block under `evidence/planning/sd037_axis_a_recalibration_overrides_<TS>.json` containing the computed per-knob values and the percentiles they were derived from. This is the contract Phase 3 and Phase 4 read from.

---

## 6. Phase 3 — Verification diagnostic

**Goal:** Confirm that the recalibrated thresholds lift consumer outputs above zero at fishtank baseline — necessary precondition for SD-037's broadcast amplification to produce any behavioural lever in Phase 4.

**Run shape:** Same fishtank baseline conditions as Phase 1, but with the Phase 2 recalibration overrides applied to `BLAConfig` / `CeAConfig` / `PAGFreezeGateConfig` / `DACCConfig` for this experiment only. Broadcast still OFF (this is a measurement of whether the consumer modules now fire on their own under baseline signal — not a test of the cascade).

3 seeds (42, 7, 19), 483e step counts. Same metric set 483e tracked:

- `bla_encoding_gain_peak`
- `cea_mode_prior_peak`, `cea_fast_prime_peak`
- `pag_release_count_end`
- `dacc_bias_nonzero_steps`
- `beta_release_count`
- plus the Phase 1 distribution snapshot for direct before/after comparison

**Acceptance gate for queuing V3-EXQ-483f:**

All four of:
- `bla_encoding_gain_peak > 0` in >= 2/3 seeds.
- `cea_mode_prior_peak > 0` in >= 2/3 seeds.
- `pag_release_count_end > 0` in >= 2/3 seeds.
- `dacc_bias_nonzero_steps > 0` in >= 2/3 seeds.

The 2-of-3-seeds floor (rather than 3-of-3) absorbs natural between-seed variance without admitting a single-seed false positive. The `> 0` bar is deliberately weak — the C2 cascade-engagement ratios in Phase 4 are the real test of magnitude. Phase 3 is testing only that the consumers are NO LONGER PINNED AT ZERO.

**FAIL routes:**

- 0 of 4 cleared -> Phase 2 sensitivity sweep (p60, then p80). If neither sweep clears 2-of-4 minimum, route to axis (b) SD-029-style sustained-threat env curriculum.
- 1-3 of 4 cleared -> per-knob diagnosis: which consumer is still pinned? Re-examine that consumer's distribution at p70 — is the p70 above the consumer's hard floor? Is the consumer's gating function more than one threshold (PAG has two: the duration_input_threshold + the theta_freeze product)? Tighten or relax that specific knob; do NOT re-sweep the other three. Re-run Phase 3.

**Out of scope for axis (a):** if the failure mode is "PAG `pag_release_count_end > 0` requires sustained-threat windows that fishtank simply does not produce naturally (the running product is a duration integral, and duration above threshold may genuinely be zero in steady-state fishtank)", then axis (b) env curriculum is the correct response — recalibrating the PAG threshold below the noise floor would make it fire constantly without representing the biology. This is the case in which axis (a) cannot succeed for the PAG channel alone, and axis (b) is the legitimate next move.

---

## 7. Phase 4 — V3-EXQ-483f (deferred; out of scope for this session)

Queued only if Phase 3 passes its acceptance gate. Out of scope for this planning session beyond stating its acceptance contract.

**Shape:** Same 4-arm 2x2 factorial as 483e (OFF_OFF / ON_OFF / OFF_ON / ON_ON, 3 seeds), but on the recalibrated substrate. Reuses the SD-036 + MECH-279 PAG-engaging substrate config; broadcast + all four MECH-281 cascade gains the toggled axes.

**Acceptance contract (same as 483e for direct comparability):**

- C1: substrate-readiness sub-checks (cue_fires + override_signal + approach_commit + goal_active).
- C2_cascade_engagement: ARM_3 / ARM_2 ratios >= 1.5x (lateral_pfc), 1.3x (bla), 1.3x (cea) on >=2/3 seeds.
- C3_lift_vs_baseline: ARM_3 `goal_norm_peak > ARM_0 + 0.01` in 3/3 seeds.
- C4_action_divergence: `TV(ARM_3, ARM_2) >= 0.05` per seed.

A PASS would resolve SD-037 / MECH-280 / MECH-281's `pending_retest_after_substrate=true` flag and route to governance for promotion candidacy.

A FAIL on the recalibrated substrate would be a load-bearing falsification of the "consumer-input-threshold layer is the sole missing piece" hypothesis. The next reading would either be (a) MECH-295 bridge structurally dominates effective_drive at the goal-seeding site even with cascade engaged (matches the 483d autopsy's `MECH-295 bridge dominates effective_drive` observation — would route to MECH-295 axis), or (b) the env itself is too sparse for SD-037 behavioural validation at any threshold setting (routes to env redesign at a level above current curriculum extensions).

---

## 8. Axis (b) fallback: SD-029-style sustained-threat env curriculum

**Reserved, not designed here.** Trigger conditions for moving to axis (b):

- Phase 3 verification fails at p70 AND p60 AND p80.
- OR Phase 3 verification clears BLA / CeA / dACC but not PAG (PAG's two-stage product gating is plausibly a duration-integral problem that no static threshold can fix in steady-state fishtank).
- OR Phase 4 (post-axis-(a)) fails on the same shape as 483e.

Axis (b) sketch (NOT implemented in this plan): an env knob analogous to SD-029's `scheduled_external_hazard` that drives z_harm_a above the consumer-input thresholds during scheduled windows. Could co-instantiate with SD-022's scheduled-injection extension, which lands directly on the harm_obs pathway. Substrate addition would be at the env / curriculum layer, not in `ree_core/`'s regulator stack.

Axis (b) plan would be authored in a separate /implement-substrate session if axis (a) is empirically exhausted.

---

## 9. Out-of-scope for this plan

- No ree-v3 code edits in this session.
- No queue entry for V3-EXQ-483f. The diagnostic Phase 1 script + queue entry go through /queue-experiment in a separate session.
- No claims.yaml edits. SD-037 / MECH-280 / MECH-281 already correctly carry `pending_retest_after_substrate=true` and `epistemic_category=substrate_ceiling` from the 2026-05-31 governance pass.
- No default-flip on `BLAConfig.arousal_threshold_on` / `CeAConfig.fast_route_threshold` / `PAGFreezeGateConfig.theta_freeze` / `duration_input_threshold` / `DACCConfig.dacc_precision_scale`. Phase 2 sets per-experiment overrides only. Default flips wait for Phase 4 behavioural validation.
- Lateral PFC (`LateralPFCAnalog`) is excluded from recalibration. It is the only consumer that responded at all in 483e (1.08-1.18x) because its `eff_eta = update_eta * (1 + override_eta_gain * override_signal)` path does not have an input-side threshold — the rule_state EMA accelerates under any non-zero source. No recalibration target.
- MECH-091 urgency-interrupt is a downstream consumer of the same z_harm_a magnitude as the PAG path; its `beta_release_count = 0` is co-explained by the same upstream threshold non-crossing. It should automatically lift once the PAG threshold is cleared by the recalibration; no separate recalibration target.

---

## 10. Risks and dependencies

- **Recalibration alone may be insufficient for PAG.** PAG's commit condition is a duration integral; if z_harm_a in fishtank is genuinely transient rather than sustained, no static threshold lowering will produce non-zero `pag_release_count_end`. This is the cleanest predictor for needing axis (b). Phase 3 will distinguish.
- **MECH-295 bridge dominance is a real risk for C3_lift.** The 483d autopsy observed MECH-295 bridge dominating `effective_drive` at the goal-seeding site. Even with cascade engaged in Phase 4, if MECH-295 produces the bulk of the goal-seeding signal, the C3_lift criterion may still FAIL. This is a Phase-4 risk, not a Phase-1/2/3 risk; calling it out so that a C2 PASS + C3 FAIL in Phase 4 is correctly diagnosed as MECH-295-axis rather than re-opening axis (a).
- **dACC default `dacc_bias_max_abs=0.0`.** Phase 1's diagnostic script must set `dacc_bias_max_abs > 0` to produce a non-trivial PE distribution (otherwise the dACC output is structurally zero regardless of PE input). This is a script-level setting, not a default flip.
- **Concurrent session siblings on substrate_queue.json.** This planning session edits one entry (SD-037). The substrate_queue file is high-contention; pathspec-limited commits + re-read-before-write keep us disjoint from other sessions editing other entries.

---

## 11. Cross-references

- `evidence/planning/failure_autopsy_V3-EXQ-483e_2026-05-31.{md,json}` — Section 8 of the autopsy MD names the two-axis fork and the consumer-input threshold knobs.
- `evidence/planning/substrate_queue.json` — SD-037 entry; `metric_trajectory.next_step` (2026-05-31T16:48Z) carries the IGW-20260531-001 routing prose; this plan doc is the structured expansion.
- `docs/architecture/sd_037_broadcast_override_regulator.md` — substrate design; consumer-cascade amend section (2026-05-30) describes the four MECH-281 wiring sites this plan provisions input for.
- `evidence/planning/inter_governance_workset.md` — IGW-20260531-001 disposition.
- `targeted_review_homeostatic_override/SYNTHESIS.md` and `targeted_review_orexin_kinetics/synthesis.md` — biological anchors for the broadcast architecture; do NOT need to be re-pulled for Phase 1/2/3.

---

## 12. Provenance

Authored 2026-05-31 in session `implement-substrate-sd037-axis-a-consumer-input-recalibration-plan-20260531T165400Z`. No code touched. Plan-only landing on REE_assembly master. Next session: `/queue-experiment` for the Phase 1 diagnostic.
