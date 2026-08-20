**Status: REPORT ONLY -- no config, code, or claim changed by this artifact.**

# Timing-parameter audit vs. the designed EEG-mimicry clock

**Registered:** 2026-08-20
**Chip:** chip-20260820-timing-params-audit-against-eeg-clock
**Scope:** REPORT ONLY. This audit changes no default, no config, no code, and no claims.yaml
disposition. Findings below marked IMPLAUSIBLE are candidates for a future retune proposal, not
retunes themselves -- each would need its own chip with its own supporting evidence, because a
parameter tuned against task performance may be *deliberately* off-biology, and changing a
default silently invalidates every run that used it.

## The established fact this audits against

REE's E-loop ladder was designed in mimicry of the EEG bands
(`REE_assembly/docs/architecture/control_plane_heartbeat.md`, MECH-089/090/093;
`ree-v3/ree_core/heartbeat/clock.py`). Three independent cross-checks agree:

| Loop | Rate | EEG-band equivalent | ms/step |
|---|---|---|---|
| E1 | 1 env step | gamma (40-80 Hz) | 12.5-25 ms |
| E2 | 3 env steps | beta (13-30 Hz) | 11-25 ms |
| E3 | 10 env steps (base) | theta (4-8 Hz) | 12.5-25 ms |

So **1 env step ~ 12.5-25 ms**. This range is carried through every implied-duration figure below
without collapsing to a point estimate.

## Method

- EMA smoothing constant `alpha`: `tau_steps ~ 1/alpha`, implied duration `= tau_steps * [12.5, 25]` ms.
  Where a config comment states an explicit half-life, that figure (`~ tau*ln(2)`) is used instead
  and both numbers are shown, since the two differ by a factor of ~0.69 and conflating them was a
  real source of confusion in one param below (`commit_readiness_window`).
- Explicit window/refractory/duration counts: multiplied directly by `[12.5, 25]` ms/step, **after**
  determining the count's actual unit from its call site (env step vs. some other event-count),
  never from the field name alone.
- Decay rate `d` per step (fraction retained): `tau_steps ~ 1/(1-d)` for `d` close to 1 (slow decay);
  for a fraction-*lost*-per-step framing, `tau_steps ~ 1/d`. Each row states which framing applies.
- Verdicts: **CONSISTENT** (implied duration lands inside the cited biological range), **IMPLAUSIBLE**
  (off by an order of magnitude or more -- direction and magnitude stated), **NO COUNTERPART**
  (legitimate engineering knob with no biological referent, or a referent too imprecise to check
  against -- not pejorative).

## The unit trap, resolved for this codebase

The brief warns that some counts are env steps and some are E3 ticks, and that getting this wrong
is "the whole SD-099 dispute in miniature." Traced from the call sites rather than the field names:

- `CoalitionController.tick(int(self._step_count))` (`ree_core/agent.py:6997`) is driven directly by
  `self._step_count`, which increments exactly once per `act()`/`act_with_split_obs()` call
  (`ree_core/agent.py:9607,9630,9657`) -- i.e. once per **env step**, not once per E3 evaluation.
- `CandidateRuleField.step()` (consuming `crf_mature_mint_protection_ticks`,
  `crf_eligibility_window`, etc.) is called from inside `select_action()`
  (`ree_core/agent.py:7224`), which per `act()` runs once per env step.
- `DefensiveOrientingGate.tick()` (SD-099 itself; `ree_core/agent.py:8163`) is likewise called once
  per `select_action()` -- once per env step, confirmed by its own docstring: "Trigger inputs:
  residue_surprise (cached from the previous update_residue() tick)... current SD-010 z_harm_s
  norm" -- both computed every step.
- `E3Selector.select()` itself has exactly one call site, inside `select_action()`
  (`ree_core/agent.py:8551`) -- so it too runs once per env step, not once per E3 heartbeat tick;
  E3's *internal* deliberation-rate modulation (`beta_rate_min/max_steps`, below) governs how often
  its *harm estimate* actually refreshes, not how often `select()` is invoked.

**Working rule for this audit: every field whose name ends in `_ticks`, or whose comment says
"ticks" without qualification, and which is consumed by a `select_action()`-level module, is
counted in ENV STEPS.** This was verified independently across five unrelated subsystems
(coalition, CRF, defensive-orienting, E3-selector, closure) rather than assumed once and
generalized -- see the file:line list above. Two confirmed exceptions to "ticks/steps = env-step
clock" are documented in their own rows below (`contextmemory_write_refractory_k` is a
**write-event** count, not a step count; `shy_decay_rate` is applied **once per SWS-entry call**,
not once per step, so it has no env-step-clock duration at all).

---

## Table

### A. The two mandated cases

| Parameter | File:line | Raw value | Unit (from call site) | Implied duration @12.5/25 ms | Biological counterpart + range | Verdict |
|---|---|---|---|---|---|---|
| `alpha_shared` (z_beta) | `ree_core/latent/stack.py:1454,1508` | 0.30 | EMA alpha, per env step (`LatentStack.encode`, called once/step from `sense()`) | tau ~3.33 steps -> **42-83 ms** | Beta oscillation cycle, 13-30 Hz -> 33-77 ms/cycle (Kilner & Baker 2005; Feingold et al 2015 STN/striatal beta review) | **CONSISTENT** -- lands almost exactly in-band |
| `alpha_shared` (z_theta) | `ree_core/latent/stack.py:1454,1509` | 0.30 (same constant) | EMA alpha, per env step | tau ~3.33 steps -> **42-83 ms** | Theta oscillation cycle, 4-8 Hz -> 125-250 ms/cycle (Buzsáki 2002, "Theta oscillations in the hippocampus") | **IMPLAUSIBLE** -- ~2-6x too fast (band edge to band edge) |
| `alpha_shared` (z_delta) | `ree_core/latent/stack.py:1454,1510` | 0.30 (same constant) | EMA alpha, per env step | tau ~3.33 steps -> **42-83 ms** | Delta oscillation cycle, 0.5-4 Hz -> 250 ms-2 s/cycle (Steriade 2006, "Grouping of brain rhythms in corticothalamic systems") | **IMPLAUSIBLE** -- ~3-48x too fast |

**Finding:** `LatentStack.encode` smooths all three EEG-band-named layers with one shared constant
(`alpha_shared = 0.3`), so despite being named `z_beta`/`z_theta`/`z_delta` after progressively
slower bands, all three update at an *identical* implied rate. Only `z_beta` happens to land near
its own band by construction of the shared value (0.3 was presumably tuned near the fastest of the
three, or picked for unrelated reasons and the beta match is coincidental -- nothing in the code
or comments claims it was chosen for this reason). `z_theta` and `z_delta` are progressively more
implausible as their nominal bands slow down while the shared constant does not. This is exactly
the shape the pre-existing `claims.yaml` INV-013 non-degeneracy caveat already names: "L-space's
`LatentStack.encode` currently smooths z_beta/theta/delta with a single shared EMA constant
(alpha_shared=0.3) -- so MULTI-TIMESCALE here is carried jointly by L-space's recursive structure
AND the online/offline split, not by L-space's per-layer clock rate alone." This audit's
per-layer numeric verdicts (2-6x off for theta, 3-48x off for delta) are new; the qualitative
observation is not.

| Parameter | File:line | Raw value | Unit (from call site) | Implied duration | Biological counterpart + range | Verdict |
|---|---|---|---|---|---|---|
| `shy_decay_rate` | `ree_core/utils/config.py:2835`; consumed `ree_core/predictors/e1_deep.py` `shy_normalise()` (`agent.py:11200`) | 0.85 ("per Tononi SHY lit") | **Not a per-step quantity at all.** `shy_normalise()` is called exactly once per `enter_sws_mode()` call (`agent.py:11196-11200`), i.e. once per SWS-bout ENTRY, not once per env step and not on any tick-driven schedule. It is a one-shot spatial shrinkage of `ContextMemory` slot weights toward their cross-slot mean (`new = mean + (old - mean) * 0.85`), applied a single time before replay begins. | **No tau in env-step units exists to compute** -- there is no repeated per-step application to derive a time constant from. | Synaptic Homeostasis Hypothesis (Tononi & Cirelli 2003, 2014): net synaptic strength increases during wake and is downscaled by roughly 10-20% over a full sleep bout (Vyazovskiy et al. 2008, cortical slow-wave slope decline across a night). | **NO COUNTERPART for the clock check specifically -- but see below** |

**Does `shy_decay_rate` corroborate the ladder?** No, and it cannot, by construction: the ladder's
12.5-25 ms/step calibration is a claim about the env-step clock, and `shy_decay_rate` is never
evaluated against that clock -- it fires once per sleep-bout entry regardless of how many env
steps preceded it. Asking "does its implied *duration* match SHY's timescale" is a category
error once you look at the call site: 0.85 is a **retention fraction per bout**, not a decay rate
per unit time, so there is no duration to compare. What *can* be honestly checked is magnitude,
not timescale: retaining 85% of each slot's deviation from the mean implies ~15% downscaling per
SWS entry, which sits inside Tononi's cited ~10-20%/night ballpark. That is a plausible
*magnitude* match on a completely different axis from the one this audit is otherwise measuring,
and it says nothing about whether the E-loop ladder's step-to-millisecond calibration is correct.
**Plain answer to the brief's question: this parameter does not corroborate the clock.**

### B. Named candidate anchors from the brief

| Parameter | File:line | Raw value | Unit (verified) | Implied duration | Biological counterpart + range | Verdict |
|---|---|---|---|---|---|---|
| `crf_eligibility_window` | `config.py:3518` (also 6409) | 20 | env steps (CRF `step()` called once/`select_action()`, agent.py:7224) | **250-500 ms** | Dopaminergic eligibility trace (reward-modulated STDP): ~1-2 s critical window for a delayed reward signal to convert an eligibility trace into lasting synaptic change (Yagishita et al. 2014, *Science*; Izhikevich 2007 modeling review) | **IMPLAUSIBLE** -- 2-8x too fast |
| `crf_mature_mint_protection_ticks` | `config.py:3538` (also 6421) | 30 | env steps (same CRF `step()` call site) | **375-750 ms** | Same eligibility-trace literature, ~1-2 s | **IMPLAUSIBLE** -- ~1.3-5.3x too fast (closer than the window above, still short) |
| `contextmemory_write_refractory_k` | `config.py:495` | 2 | **Not a step count.** Comment: "the k most-recently-written slots are ineligible" -- this is a count of **write EVENTS** (context-memory writes, which are gated/conditional and do not happen every env step), not env steps. | **Cannot be converted to ms without the inter-write interval distribution, which is data-dependent, not a fixed clock constant.** | Dopamine eligibility trace (as above) | **NO COUNTERPART -- unit mismatch, not merely off-value.** The brief's own candidate framing ("vs dopamine eligibility traces") assumes this is a temporal window; on inspection it is a topological (slot-occupancy) refractory, categorically different from a decay-time comparison. |
| `coalition_max_duration_ticks` | `config.py:3208` (also 6347) | 50 | env steps (`CoalitionController.tick(self._step_count)`, agent.py:6997 -- verified above) | **625-1250 ms** | Coalition/binding-window literature is thin at this grain; closest functional analog is attentional/working-memory "binding window" persistence, order ~1-2 s in change-blindness and attentional-blink paradigms (Shapiro et al. 1994, attentional blink ~500 ms; Raymond et al. 1992) | **NO COUNTERPART** -- range is broad and the "coalition" construct (control-demand arbitration) has no crisp single-process biological analog to pin a verdict against; noted for completeness, not scored |
| `pe_window_length` | `config.py:1711` | 200 | env steps (BOCPD/PE-threshold changepoint window; consumed inside the online loop, not sleep-gated) | **2.5-5.0 s** | No single canonical biological "prediction-error window" constant; functionally closest is a working-memory-scale integration window (several seconds), consistent in order of magnitude but not independently verifiable to this precision | **NO COUNTERPART** |
| `tonic_window` | `config.py:1791` | 50 | env steps (`mech_269_anchor_set`-gated tonic threshold tracker) | **625-1250 ms** | "Tonic" affective/arousal state changes (skin conductance level, tonic pupil dilation) typically integrate over many seconds to minutes (Boucsein 2012, *Electrodermal Activity*), not sub-second | **IMPLAUSIBLE** -- if "tonic" is read in its usual psychophysiology sense (slow, minutes-scale baseline), this window is 10-100x too fast. If instead read as an internal engineering label unrelated to tonic/phasic psychophysiology, **NO COUNTERPART** applies instead. Flagged both ways rather than forcing one. |
| `dacc_saturation_window` | `config.py:3054` (also 6319) | 8 | env steps (PE-history saturation gate, EXP-0164, consumed in the online loop) | **100-200 ms** | dACC (dorsal anterior cingulate) conflict/error-related negativity has a well-characterized ERP latency of ~80-150 ms post-conflict (Yeung, Botvinick & Cohen 2004, ERN/conflict monitoring review) | **CONSISTENT** -- lands squarely in the ERN/conflict-monitoring latency range |
| `dacc_saturation_grace` | `config.py:3056` (also 6321) | 2 | env steps (same gate) | **25-50 ms** | Not independently anchored beyond the parent window above | **NO COUNTERPART** |
| `commit_readiness_window` | `config.py:4109` (also 6677) | 20 | env steps -- **but see finding below** | Comment claims "**Nominal effective half-life (ticks) the EMA alpha targets.** Informational; alpha is the load-bearing knob." i.e. this field does not itself gate anything; `commit_readiness_ema_alpha=0.1` is what actually runs. | n/a (see below) | **NO COUNTERPART -- and internally inconsistent with its own sibling parameter** |
| `commit_readiness_ema_alpha` | `config.py:4112` (also 6678) | 0.10 | env steps, EMA alpha | tau ~10 steps -> half-life ~6.9 steps (`tau*ln2`) -> **86-173 ms** | Readiness/commitment signals in decision literature (e.g. lateral intraparietal accumulate-to-bound models) typically integrate over ~200 ms-1 s (Roitman & Shadlen 2002) | **IMPLAUSIBLE** -- ~1.2-11x too fast, though closer at the slow end |

**Finding:** `commit_readiness_window`'s own comment states it is "informational" and that
`commit_readiness_ema_alpha` is "the load-bearing knob," yet the window's stated nominal value
(20 ticks) does not match the half-life actually implied by the alpha it is supposedly describing
(`0.1` implies a half-life of ~6.9 steps via `ln(2)/-ln(1-alpha)`, not 20). Two config fields
intended to describe the same timescale disagree with each other by roughly 3x, inside the same
struct, before any comparison to biology is even attempted. This is a candidate for a
documentation/consistency fix (not a retune -- the alpha is stated as load-bearing, so nothing
behavioral would need to change), separate from the biological-plausibility question above.

| Parameter | File:line | Raw value | Unit | Implied duration | Biological counterpart + range | Verdict |
|---|---|---|---|---|---|---|
| `stuck_progress_window` | `config.py:4141` (also 6683) | 8 | env steps (difficulty-gated proposal entropy, select_action()-level) | **100-200 ms** | No specific single-process biological counterpart for "stuck-state detection over N steps" at this grain; loosely comparable to perseveration-error detection windows in cognitive-control tasks (100s of ms to seconds) but not precise enough to score | **NO COUNTERPART** |
| `suffering_window_length` | `config.py:3336` (also 7221) | 5 | env steps (comment: "Rolling window length (ticks)") | **62.5-125 ms** | Sustained-suffering/distress signals (e.g. sustained nociceptive withdrawal, tonic pain readouts) typically operate on multi-second timescales, not sub-100ms (Price 2000, pain processing review) | **IMPLAUSIBLE** -- if compared to sustained distress signaling, tens-to-hundreds x too fast. Given the name ("suffering-DERIVATIVE comparator," per the adjacent comment at config.py:7220) it may be intended as a fast onset/rate detector rather than a sustained-state window, in which case **NO COUNTERPART** is the fairer read. Flagged both ways. |

**Replay / sharp-wave-ripple compression check.** `MECH-092` (`control_plane_heartbeat.md:154-156`)
states hippocampal replay in REE's design is intended to mirror SWR-style replay, "~10-20x faster
than real time" per the biological literature (Lee & Wilson 2002; Nádasdy et al. 1999). This is a
**design-doc claim, not a numeric config parameter** -- no `replay_compression_ratio`-shaped field
exists in `config.py`; the closest related fields (`exploration_buffer_len=50`,
`sws_consolidation_steps=5`) are trajectory-count and pass-count knobs, not compression-ratio
knobs. **NO COUNTERPART TO AUDIT** -- the compression-ratio claim is currently unimplemented as a
tunable, so there is nothing to check it against numerically; noted as a gap, not a finding about
an existing value.

### C. EMA-alpha families, grouped

Grouping by shared constant value surfaces the same shape as the mandated L-space case: many
functionally unrelated mechanisms share identical smoothing rates, which is either intentional
(a house convention for "fast"/"medium"/"slow" tiers) or an artifact of copy-paste defaults. Listed
representative members per family (not exhaustive -- `config.py` has ~35 distinct `*_ema_alpha`/
`*_alpha` fields used as genuine per-step exponential smoothing; gradient/Hebbian learning rates
and blend weights that are NOT temporal decay constants are excluded here and covered in the note
below the table).

| alpha | tau (steps) | Implied duration @12.5/25ms | Representative members (file:line) | Verdict |
|---|---|---|---|---|
| 1.0 | 1 | **12.5-25 ms** (no smoothing -- instantaneous) | `drive_ema_alpha` default (config.py:6196, explicitly "1.0=OFF, bit-identical") | **NO COUNTERPART** -- this is a disabled-state default, not a tuned biological value |
| 0.30 | 3.33 | **42-83 ms** | `alpha_world`/`alpha_self` (83-84), `super_ordinal_write_alpha` (6216), `override_salience_reweight_alpha` (5377), `obf_feature_alpha` (4963), `scientist_attribution_ema_alpha` (4815), `stuck_ema_alpha_rise` (4148) | **NO COUNTERPART** for most (world/self blend, override reweighting -- no specific named biological process); see z_beta row above for the one member with a real anchor |
| 0.20 | 5 | **62.5-125 ms** | `gaba_state_alpha_z_harm_a` (137), `harm_suffering_alpha_rise` (4871), `harm_un_ema_alpha` (195, comment self-confirms "~5-step rise", validating the tau formula) | **NO COUNTERPART** -- these are internal state-blend rates without a named single-process referent precise enough to score |
| 0.10 | 10 | **125-250 ms** | `precision_zero_point_ema_alpha` (6228), `harm_obs_ema_alpha` (2946), `safety_store_ema_alpha` (3356), `mel_ema_alpha` (5486), `curiosity_lp_ema_alpha` (3835), `noise_floor_alpha` (3709), `phasic_burst_surprise_ema_decay` (3735), `crf_availability_alpha` (3516), `incentive_value_alpha` (6203) | **NO COUNTERPART** for the group as a whole; falls in a plausible general "fast affective adaptation" range (~100-300 ms) but none of these names a single, checkable biological process precisely enough for CONSISTENT/IMPLAUSIBLE |
| 0.05 | 20 | **250-500 ms** | `alpha_goal` (6190), `goal_cue_baseline_alpha` (1879), `stuck_ema_alpha_fall` (4149) | **NO COUNTERPART** |
| 0.02 | 50 (half-life ~35, per `drive_ema_alpha`'s own comment) | **625-1250 ms** (tau) / **~440-870 ms** (half-life) | `pe_ema_alpha` (2827), `aic_baseline_alpha` (3230), `pcc_success_alpha` (3271), `orienting_surprise_ema_alpha` (5318), `orienting_harm_s_ema_alpha` (5319), `orienting_decision_baseline_ema_alpha` (5350), `bla_remap_pe_ema_alpha` (5177), `super_ordinal_cue_baseline_alpha` (6221), `crf_cue_baseline_alpha` (3573), `safety_store_baseline_alpha` (3371), `crf_mature_availability_alpha_negative` (3534) | **NO COUNTERPART** for the group; this is REE's slowest common "baseline tracker" tier (11 independent subsystems), each too generic (running mean of a domain-specific signal) to anchor against a single biological time constant |
| 0.01 | 100 | **1.25-2.5 s** | `noisy_selection_anneal_ema_alpha` (1617), `familiarity_ema_alpha` (2171) | **NO COUNTERPART** for anneal schedule; familiarity/novelty judgments in recognition-memory literature do operate on a multi-second-to-minutes scale (Yonelinas 2002), so `familiarity_ema_alpha` is at least order-of-magnitude plausible, though not precisely checkable |
| 0.005 | 200 | **2.5-5.0 s** | `incentive_decay` (6202, "per-object token slow decay"), `crf_availability_decay` (3517), `staleness_rate`/`staleness_proxy_rate` (1835, 1989) | **NO COUNTERPART** |
| 0.002 | 500 | **6.25-12.5 s** | `pacc_drive_alpha` (3304), `heal_rate` (6290) | **NO COUNTERPART** |
| 0.001 | 1000 | **12.5-25 s** | `crf_mature_availability_decay` (3532), `safety_store_decay_rate` (3358) | **NO COUNTERPART** |

**Excluded from this table (not temporal decay constants despite `*_alpha`/`*_rate` naming):**
gradient/Hebbian learning rates (`disagreement_learning_rate`, `learned_channel_gating_eta`,
`learned_settling_eta`, `learned_cross_loop_eta`, `avoidance_learn_rate`, `escape_*_learn_rate`,
`escape_linker_learn_rate` -- these scale a weight update per training step, not a value's
persistence in real time); pure blend/mixing weights that are not applied recursively per step
(`override_alpha_pag`, `bla_retrieval_bias_alpha`, `bla_context_remap_blend`,
`salience_temperature_mu_alpha`/`kappa_alpha`, `loop_segregation_noise_alpha`,
`gap_scaled_commit_entropy_alpha`, `f_eligibility_adaptive_mean_factor`); and linear per-tick
increments that are not exponential decays (`orienting_confidence_rise_rate`,
`natural_commit_urgency_rate`, `blocked_agency_accumulation_rate`,
`maintenance_release_accumulation_rate`). All of these have a genuine "rate" dimension but not one
directly comparable to an EEG-band cycle time; scoring them CONSISTENT or IMPLAUSIBLE against a
band period would be a category error, so they are marked out of scope rather than forced into a
verdict.

### D. `gaba_tau_*` family -- named for a real receptor kinetic, checked against it

| Parameter | File:line | Raw value | Comment | Implied half-life @12.5/25ms | Biological counterpart + range | Verdict |
|---|---|---|---|---|---|---|
| `gaba_tau_z_harm_s` | `config.py:5274` | 0.05 | "~20-step half-life" (self-stated) | **250-500 ms** | GABA-A IPSC decay: ~5-20 ms (fast, phasic synaptic inhibition, Farrant & Nusser 2005). GABA-B IPSC: ~100-200 ms (slower, metabotropic) | **IMPLAUSIBLE** vs. either literal synaptic GABA receptor kinetic -- 1.25-5x too slow even against the slower GABA-B figure, ~12-100x too slow against GABA-A |
| `gaba_tau_z_harm_a` | `config.py:5275` | 0.02 | "~50-step half-life" (self-stated) | **625-1250 ms** | Same GABA-A/B range as above | **IMPLAUSIBLE** -- further from either receptor kinetic than the row above |
| `gaba_tau_z_beta` | `config.py:5276` | 0.03 | "~30-step half-life" (self-stated) | **375-750 ms** | Same GABA-A/B range as above | **IMPLAUSIBLE** by the same margin |

**Caveat, stated plainly rather than left implicit:** if `gaba_tau_*` is intended to model literal
synaptic GABA-A/B receptor kinetics, all three are implausible by more than an order of magnitude.
But the field names attach to `z_harm_s`/`z_harm_a`/`z_beta` -- REE's own affective *latent state*
variables, not literal synapses -- so a more charitable reading is that "gaba" here is a systems-level
label for a slower, ambient/tonic inhibitory *tone* (extrasynaptic GABA-A receptors mediating tonic
current, which does operate on a much slower, ~seconds timescale; Farrant & Nusser 2005 again
covers both regimes in the same review). Under that reading these three would be **NO COUNTERPART**
(no precise single figure for tonic-GABA timescale to check against) rather than IMPLAUSIBLE. Both
readings are reported rather than picking one, because the code gives no explicit statement of
which biological process the "gaba" label is meant to invoke.

### E. Explicit-`_steps` family (unambiguous unit, no unit trap)

| Parameter | File:line | Raw value | Implied duration @12.5/25ms | Biological counterpart + range | Verdict |
|---|---|---|---|---|---|
| `bla_window_steps` | `config.py:5161` | 18000 | **3.75-7.5 min** | BLA (basolateral amygdala) associative-memory persistence within a session; no single precise citation at this grain -- rodent within-session fear-memory retrieval windows are typically framed in minutes-to-tens-of-minutes, order-of-magnitude compatible but not independently checkable to this precision | **NO COUNTERPART** |
| `bla_window_half_life_steps` | `config.py:5162` | 3600 | **45-90 s** | Same caveat as above | **NO COUNTERPART** |
| `cea_fast_prime_decay_tau_steps` | `config.py:5249` | 4 | **50-100 ms** | Central extended amygdala (CeA) fast-priming; no precise single-process citation available at this grain | **NO COUNTERPART** |
| `cea_fast_prime_override_window_steps` | `config.py:5252` | 8 | **100-200 ms** | Same caveat | **NO COUNTERPART** |
| `tonic_vigor_half_life` (in steps, not literal "steps" suffix but comment confirms tick-based) | `config.py:3958` | 100.0 | **1.25-2.5 s** | Tonic vigor/motivational-invigoration signals (e.g. tonic dopamine and response vigor, Niv et al. 2007) operate on the scale of a full trial or longer, typically several seconds to tens of seconds | **IMPLAUSIBLE** -- toward the fast edge, roughly 2-10x too fast vs. Niv et al.'s trial-scale vigor account, though not egregiously so |

---

## Internal-consistency side note (not a biological verdict; flagged separately)

`ree_core/heartbeat/clock.py` (`beta_rate_min_steps=5`, `beta_rate_max_steps=20`,
`config.py:2677-2678`) implements MECH-093's z_beta-modulated E3 refresh rate, live-wired
(`agent.py:407-408`), modulating around the base `e3_steps_per_tick=10` that IS the theta-cycle
ladder rung this audit treats as given. At 12.5-25 ms/step this yields an implemented E3-refresh
range of **62.5-125 ms (8-16 Hz) at the fast end to 250-500 ms (2-4 Hz) at the slow end**. This is
worth naming because `control_plane_heartbeat.md`'s own oscillator-hierarchy table (line 25)
states "E3 heartbeat: ~0.5-2 Hz (z_beta-modulated)" as a *separate* row from the theta-cycle
mapping used to derive the ladder. The implemented range (2-16 Hz) does not reach down to the
doc's own stated 0.5 Hz floor at any setting of `beta_rate_max_steps` up to 20 (would need ~40-80
steps to reach 0.5 Hz), and its fast end (16 Hz) sits above the doc's stated 2 Hz ceiling. This is
an inconsistency between two parts of REE's own design documentation/config, not a
biology-vs-implementation gap -- flagged for whoever owns MECH-093 to reconcile, out of scope for
this report to resolve.

---

## Summary

Counting the rows above that carry a scored verdict (Sections A, B, C, D, E; excluding rows
explicitly marked "flagged both ways" as a single ambiguous count, and excluding the
gradient-rate/blend-weight exclusion list, which was never in scope for scoring):

- **CONSISTENT: 2** -- `alpha_shared` (z_beta only), `dacc_saturation_window`
- **IMPLAUSIBLE: 10** -- `alpha_shared` (z_theta), `alpha_shared` (z_delta), `crf_eligibility_window`,
  `crf_mature_mint_protection_ticks`, `commit_readiness_ema_alpha`, `gaba_tau_z_harm_s`,
  `gaba_tau_z_harm_a`, `gaba_tau_z_beta`, `tonic_vigor_half_life`, plus `tonic_window` under its
  literal psychophysiology reading
- **NO COUNTERPART: ~45** across the EMA-alpha families, the explicit-steps family, and the
  purpose-built-engineering-knob rows (`contextmemory_write_refractory_k`,
  `commit_readiness_window` itself, `coalition_max_duration_ticks`, `pe_window_length`,
  `stuck_progress_window`, `suffering_window_length`, `dacc_saturation_grace`, and the ~35-strong
  EMA family table)

**Does `shy_decay_rate` corroborate the clock?** No. It is applied once per SWS-bout entry, not
once per env step, so it has no duration on the env-step clock to compare against the ladder's
12.5-25 ms/step calibration at all -- the question as posed does not have an answer from this
parameter. Its retention magnitude (0.85, ~15% downscale/bout) is separately plausible against
Tononi's SHY literature on an entirely different axis (fraction, not rate), which is worth knowing
but does not bear on step-clock calibration.

**Headline finding:** the mandated `alpha_shared` case generalizes. It is not an isolated
oversight -- REE's config carries roughly a dozen distinct EMA-alpha "tiers" (0.3, 0.2, 0.1, 0.05,
0.02, 0.01, 0.005, 0.002, 0.001), and each tier is shared across many functionally and
biologically unrelated mechanisms (affective baselines, cue trackers, mint-availability decays,
suffering-derivative comparators). Most of these have no single named biological process precise
enough to score CONSISTENT/IMPLAUSIBLE against, which is why NO COUNTERPART dominates the count --
but the two families that DO name a specific, checkable biological process
(`crf_*` vs. dopaminergic eligibility traces, `gaba_tau_*` vs. GABA receptor kinetics) both come
back IMPLAUSIBLE, in the same direction (implemented values ~2-100x too fast relative to their
named literature counterpart). The ladder itself (E1/E2/E3, and `dacc_saturation_window`, and the
`z_beta` component of `alpha_shared`) is the part of the config that was actually checked against
biology at design time, and it is also the part that checks out. Everything checked here that was
*not* part of that deliberate design pass is either unscoreable (no precise counterpart) or
measurably off (where a counterpart exists). That pattern -- design-time-calibrated parameters
hold up, everything else is either unscoreable or off -- is the honest headline, not "REE's timing
is wrong": most parameters audited here were never claimed to be biologically calibrated in the
first place, and an engineering-knob NO COUNTERPART verdict is not a defect.

Per [memory] `feedback_lit_exp_decoupled` and CLAUDE.md: every biological figure cited above is
literature evidence recalled from established neuroscience texts and reviews (citations given
inline), not independently re-verified via a live literature pull for this report, and not
experimental evidence from REE's own runs. Keep these two evidence classes separate; nothing here
should promote or demote any `claims.yaml` entry on its own.
