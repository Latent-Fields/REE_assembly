# G3 -- THREAT / DEFENCE / VETO / FREEZE / AFFECT / DRIVE / RESIDUE (D0 code-read inventory)

Auditor: G3 sub-agent for bt0926-dca. Evidence class: D0, read-only code reading. Nothing was run.
Tree: MAIN = `ree-v3` origin/main @ 436a988 (`.../dca/main-wt`). All file:line cites below are on MAIN, with paths relative to `ree_core/`.
None of the G3 files differ on BRANCH: the branch diff touches only agent.py (+7), hippocampal/module.py, e3_selector.py, config.py and waking_trainer*, and none of those hunks are in the G3 rows. So there are no branch-only rows.

## 0. Headline answer: what threat/defence path is live end-to-end at DEFAULT config?

**At defaults the agent has no harm latent at all.** `LatentStackConfig.harm_dim=0` (config.py:150) disables the MECH-099 lateral head (latent/stack.py:891-900, 1031-1037). `use_harm_stream=False` (config.py:336) means no SD-010 HarmEncoder (stack.py:1208-1214). `use_affective_harm_stream=False` (config.py:347) means no SD-011 AffectiveHarmEncoder (stack.py:1219-1226).
So `z_harm = None` and `z_harm_a = None` on every tick (stack.py:1728-1749, 1822). from_dims passes these through unchanged (config.py:9722, 9759-9768).

The consequence is that **every** z_harm/z_harm_a consumer is dead at defaults even if its own flag were flipped, unless SD-010/SD-011 is also on. That covers CeA, BLA, the PAG freeze entry and exit, the MECH-091 urgency interrupt, instrumental avoidance, the escape-affordance family, the MECH-302 relief comparator, the MECH-303/304 safety gates, the AIC, the E3 `lambda_eff` amplification and the orienting harm_s channel.

The only threat-driven edges that are live at defaults all start from the **scalar env harm signal the driver passes into `agent.update_residue(harm_signal)`** (agent.py:12184). There are three:

1. **harm -> residue RBF field -> E3 trajectory cost and hippocampal CEM terrain.** `harm_signal<0 & owned & not hypothesis_tag` triggers `residue_field.accumulate(|harm|*0.1*min(2,world_delta))` at the current z_world (agent.py:12364-12376; residue/field.py:736-784; RBF write field.py:165-180).
   - It is read every E3 tick as `rho_residue(0.5)*phi` in the score (e3_selector.py:1555-1563, 1836, 1869, 1889).
   - It is also read by the hippocampal terrain prior input (hippocampal/module.py:591-604) and by CEM elite scoring (module.py:1785-1797, 1878-1886).
   - Timescale is lifetime: no decay (config.py:3705 `decay_rate=0.0`) and it is not reset per episode (agent.py:4102 docstring).
2. **A second residue write from the same harm event, when committed.** `e3.post_action_update(harm_occurred=harm_signal<0)` (agent.py:12213-12216) writes `accumulate(harm_magnitude=1.0)` whenever `_committed_trajectory is not None` (e3_selector.py:4955-4959).
   - This write **ignores** update_residue's `owned` and `hypothesis_tag` arguments, because post_action_update is called before and outside those gates.
   - It is a shared-source coupling: one harm event produces two ring-buffer writes.
3. **harm -> MECH-091 clock phase reset -> off-schedule E3 re-deliberation.** The same `harm_signal<0` branch calls `self.clock.phase_reset()` (agent.py:12379).
   - That sets `_pending_phase_reset`, so the next `advance()` forces `e3_tick=True` and `e3_quiescent=False` (heartbeat/clock.py:149-155, 189-190), against the default 10-step E3 cadence (config.py:4035).
   - The effect is an immediate re-selection and suppression of that cycle's MECH-092 quiescence flag.

**Nothing live at defaults changes a mode/regime register on threat.**
- No freeze, orienting arrest, veto, interrupt, de-commit or mode prior is constructed.
- The residue path is a smooth, additive, lifetime cost term, not a regime switch. Its discriminating power is itself doubtful: `kernel_bandwidth=1.0` is ~8x the reachable z_world cloud (field.py:426-440 comment; measured harm/safe ratio 1.0067), so the field is near-broadcast across candidates.
- The phase reset is the one threat-triggered *timing* control at defaults. It re-runs selection; it does not change what selection does.

## 1. Inventory table

Legend for the flag columns:
- **Rst** = episode reset. **R** = state reset every episode; **P** = persists across episodes.
- **155** = ARC-155 shape (absolute constant threshold on a learned quantity).
- **156** = ARC-156 shape (exit depends on evidence the regime suppresses).
- **SS** = shared-source coupling.

### A. Harm streams (producers)

| name | ids | STATUS | signal read | variable changed (consumer) | timescale | endo/harness | consumer check | citations | flags |
|---|---|---|---|---|---|---|---|---|---|
| Lateral harm head (z_harm) | MECH-099 | DEFAULT-OFF-IMPLEMENTED | hazard + contamination view slices of world_obs (50-d) | `LatentState.z_harm` (feeds all z_harm readers below) | per-tick, stateless | ENDOGENOUS obs; weights trained only by harness losses | readers exist (see rows below); none active at defaults | stack.py:891-900, 1031-1037; config.py:150 (`harm_dim=0`) | -- |
| HarmEncoder z_harm_s | SD-010, ARC-027 | DEFAULT-OFF-IMPLEMENTED | env `harm_obs` (51-d proxy fields) | overrides z_harm (stack.py:1728-1732) | per-tick | obs ENDOGENOUS; training HARNESS | readers: orienting, SD-021, valence_harm, E2_harm_s, OFC, SCI | stack.py:1205-1214; config.py:336 | -- |
| AffectiveHarmEncoder z_harm_a | SD-011, ARC-033 | DEFAULT-OFF-IMPLEMENTED | env `harm_obs_a` (EMA of proximity fields, tau ~20) + optional harm_history | `LatentState.z_harm_a`, the input to nearly every threat controller below | per-tick encode of an env-side EMA | obs ENDOGENOUS; aux head trained only if harness calls `compute_harm_accum_loss` (prior record: untrained in every recipe) | many readers; all dead at defaults because this is None | stack.py:1216-1226, 1735-1749; config.py:347, 349 | onset information is destroyed upstream (EMA input; hazard field saturates; cea_onset_input_reprobe_20260925) |
| harm_un EMA | SD-019a | DEFAULT-OFF-IMPLEMENTED | z_harm_s | `z_harm_un`; **redirects** the MECH-091 interrupt signal and E3 urgency input (agent.py:7971-7980, 8013-8019) | EMA alpha 0.2 (`harm_un_ema_alpha`) | ENDOGENOUS | consumer found (agent.py:8013-8019) | agent.py:6317-6340; config.py:368 | Rst R (agent.py:4161 `_harm_un_ema=None`) |
| GABAergic decay regulator | SD-036 | DEFAULT-OFF-IMPLEMENTED | per-stream norm change (suspend-on-input gate; thresholds all 0.0, so the suspend never fires) | multiplies z_harm, z_harm_a, **z_beta** by exp(-tau*tone) each tick; `gaba_tone` also scales the PAG exit threshold (agent.py:11484-11490) | per-tick; tau 0.05/0.02/0.03 | tone is a **HARNESS-SET PARAMETER** (`set_gaba_tone` has no in-tree caller; grep `set_gaba_tone\(`) | consumer found (PAG, and all latent readers) | agent.py:2583-2626, 6300-6314; regulators/gabaergic_decay.py:176-186, 259-340; config.py:7236-7257 | Rst: counters R, tone P. It also decays z_beta, so it couples to MECH-093 arousal/E3 rate (SS) |
| Harm-state recurrence | SD-036 | DEFAULT-OFF-IMPLEMENTED | previous z_harm/z_harm_a | blended z_harm (a=0.5), z_harm_a (a=0.2) | EMA | ENDOGENOUS | consumer = the latent itself | stack.py:1751-1796; config.py:244-257; force-mirrored on when `use_gabaergic_decay` (agent.py:2626) | -- |
| E2_harm_a forward | MECH-258 | DEFAULT-OFF-IMPLEMENTED | z_harm_a_t, a_t | `_harm_a_pred_prev`, used by the BLA remap PE and dACC | per-tick | training HARNESS (external optimizer) | consumer found (agent.py:6480-6516 BLA; 11652 write) | agent.py:516-542, 11652; config.py:4461 | -- |
| E2_harm_s forward | ARC-033, SD-003 | TELEMETRY-ONLY even when on (via agent) | z_harm_s, a | SCI attribution buffer record (agent.py:5543-5556); OFC oracle predictions, "no effect on E3 scores" (agent.py:9571-9590) | per-tick | training HARNESS | the E3 `harm_forward_model` path (e3_selector.py:1828-1830) is **never passed by the agent** (grep `harm_forward_model=` in agent.py: none); only a driver can supply it | agent.py:545-555; config.py:479 | -- |
| Shared harm trunk | ARC-058 | DEFAULT-OFF-IMPLEMENTED (structural) | -- | shares E2_harm_s/E2_harm_a hidden layers | -- | HARNESS config | architecture choice, not a controller | agent.py:516-542; config.py:4476 | -- |
| Harm-surprise PE target | SD-020 | DEFAULT-OFF-IMPLEMENTED (training target only) | harm_obs minus its EMA, times precision | z_harm_a training target inside the harness-called `compute_harm_accum_loss` | EMA alpha 0.1 | HARNESS (loss call) | no runtime controller | config.py:4411-4415 | -- |
| Descending pain modulation | SD-021 (SD-032c path) | DEFAULT-OFF-IMPLEMENTED | beta_gate.is_elevated, or AIC `harm_s_gain` | attenuates z_harm (not z_harm_a) before E3/E2_harm_s | per-tick | ENDOGENOUS (commit state) | consumer = z_harm readers | agent.py:6570-6615; config.py:4422-4424 | SS: commit state gates the harm signal |

### B. Amygdala (SD-035)

| name | ids | STATUS | signal read | variable changed (consumer) | timescale | endo/harness | consumer check | citations | flags |
|---|---|---|---|---|---|---|---|---|---|
| Amygdala master | SD-035 | DEFAULT-OFF-IMPLEMENTED | -- | constructs BLA/CeA; sub-switches `use_bla_analog`/`use_cea_analog`=True are inert under master False | -- | HARNESS | -- | config.py:7115-7121; agent.py:2498 | -- |
| BLA encoding gain / arousal tag | MECH-074a | DEFAULT-OFF-IMPLEMENTED | z_harm_a magnitude vs `arousal_threshold_on` 0.4 / peak 0.7 (inverted-U) | `encoding_gain` goes to hippocampal trajectory `memory_strength` (agent.py:4596-4619 episode-end record; 11337-11349 commit record, only with `use_backward_credit_sweep`, config.py:3561). memory_strength weights replay (module.py:3199), only on the diverse-replay path | window 18000 steps, half-life 3600 | obs ENDOGENOUS; thresholds HARNESS-SET | consumer found but itself gated off (replay_diversity_enabled=False, config.py:4330) | amygdala/bla.py:150-180; agent.py:6509-6530; config.py:7125-7132 | 155 (absolute 0.4/0.7 on a learned latent); Rst R (agent.py:4439 bla.reset) |
| BLA retrieval bias | MECH-074b | DEFAULT-OFF-IMPLEMENTED | stored exploration arousal tags | `retrieval_bias` goes to `hippocampal.diverse_replay` | per-tick | ENDOGENOUS | consumer agent.py:12166-12176, gated on replay_diversity_enabled | config.py:7136-7142 | -- |
| BLA remap | MECH-074d | DEFAULT-OFF-IMPLEMENTED | z_harm_a PE vs its running sigma (relative, remap_pe_sigma 1.0) + attribution proxy | in-place blend of E1 ContextMemory slots (agent.py:5823-5845) | per-tick; PE EMA alpha 0.02 | ENDOGENOUS | consumer found (agent.py:6531-6536); needs E2_harm_a for the PE | bla.py:221-244; config.py:7146-7156 | Rst R: PE EMA re-initialised each episode, so the sigma baseline never matures across episodes |
| BLA trainable attribution head | MECH-074d 2nd pass | DEFAULT-OFF-IMPLEMENTED | z_self/z_world/z_harm_a | head weights (own optimizer, per tick in sense()) | per-tick online learning | ENDOGENOUS | feeds the remap gate | agent.py:2519-2549, 6537-6546; config.py:7170-7195 (`bla_attribution_head="contribution_threshold"`) | -- |
| CeA fast route: mode_prior / fast_prime | MECH-046, MECH-074c | DEFAULT-OFF-IMPLEMENTED (double-gated: amygdala master AND `use_salience_coordinator`=False, config.py:4593) | low_freq = `||z_harm_a||_1/dim` > `fast_route_threshold` 0.5 | coordinator affinity `cea_mode_prior`, weight {external_task: 1.0}, and salience `cea_fast_prime`, weight 0.5 (agent.py:2573-2577, 9071-9087); also veto-readout telemetry | fire resets an 8-step override window; pulse half-life 4 steps | obs ENDOGENOUS; threshold/cap HARNESS-SET | consumer found (salience coordinator). **Ceiling**: salience contribution <= 0.5 x cap 0.8 = 0.4 < switch_threshold 1.0 (salience_coordinator.py:311), so CeA alone can never trip a switch | amygdala/cea.py:259-457 (gate :308-337); config.py:7201-7226 | 155 (absolute 0.5 on a learned latent: never fires untrained, always fires after SD-011 harm_accum training, per cea_gate_calibration_probe_20260925); Rst R (cea.py:249-256) |
| CeA `pre_softmax_additive` | SD-035 | NAMED-CONCEPT (dead config knob) | -- | nothing | -- | HARNESS | grep `pre_softmax_additive` finds only config.py:7215, 9111, 10843, agent.py:2559 (passthrough) and the CeAConfig field def cea.py:174. **Never read.** mode_prior is summed into coordinator affinity regardless, so the flag cannot turn anything on or off | -- | -- |
| CeA `cortical_confirmation` / `escapability_hint` / `cue_features` | MECH-074c, Q-036 | NAMED-CONCEPT (in-agent) | -- | the hold-the-pulse branch (cea.py:392-403) is unreachable because the agent always passes None (agent.py:6564-6572); the other two are documented V3 no-ops (cea.py:275-282) | -- | -- | -- | as cited | -- |

### C. PAG freeze / orienting / avoidance

| name | ids | STATUS | signal read | variable changed (consumer) | timescale | endo/harness | consumer check | citations | flags |
|---|---|---|---|---|---|---|---|---|---|
| PAG freeze gate | MECH-279, MECH-280 | DEFAULT-OFF-IMPLEMENTED | `||z_harm_a||_2` by default. Alternatives: LPB external_magnitude, or z_harm_suffering if redirected (agent.py:11464-11482). **Entry**: z x duration_above(0.4) > theta_freeze 2.0. **Exit**: z < theta_freeze x override_factor x desc_factor x gaba_tone; min/max duration 0 means no cap | **post-selection action substitution**: emitted action replaced by the STAY one-hot (`pag_freeze_noop_action_class`, CGW STAY; was class 0 = a MOVE until 2026-09-25). E3 selection/commit still runs underneath. ilPFC (IA) can suppress (agent.py:11505-11552) | per-E3-tick counter | obs ENDOGENOUS; theta HARNESS-SET | consumer found (agent.py:11527-11552; also sets `_forced_hold_still` for MECH-357 credit) | pag/freeze_gate.py:14-29, 467-540; agent.py:2628-2661, 11449-11552; config.py:7263-7267 | **155** (V3-EXQ-1107: theta 0.8 vs norm 2.8-4.2, so freeze from tick 1). **156**: exit needs z_harm_a to fall, but z_harm_a is an EMA of hazard proximity and the frozen agent emits STAY, so it cannot leave the hazard; no max-duration cap. Rst R (freeze_gate.py:348-362) |
| PAG descending release | MECH-287 option B | DEFAULT-OFF-IMPLEMENTED (also needs `use_anchor_sets` / `use_per_region_vs` to produce any drive) | hippocampal anchor invalidations: T3 broadcast strength + hysteresis resets (module.py:4068-4069, 4285; consumed module.py:4072-4088) | `_pag_desc_release_trace` (decay 0.95) raises the PAG exit threshold x(1+alpha*r) (freeze_gate.py:491-497) | per waking sense() | ENDOGENOUS | consumer found (agent.py:11496-11503) | agent.py:2664-2690, 6944-6958; config.py:7292-7295 | **156**: invalidations need world-state change, which the STAY-freeze suppresses. V3-EXQ-1106: 0 drive-steps-while-frozen (ARC-156 citation). Rst R (agent.py:4464-4465) |
| Defensive orienting arrest | MECH-489, SD-099 | DEFAULT-OFF-IMPLEMENTED | onset delta > 0.010 above its own EMA baseline (alpha 0.02) of (a) residue surprise, only non-zero if `surprise_gated_replay`=True (agent.py:12352-12353; config.py:4266), or (b) `||z_harm_s||` (needs SD-010/MECH-099) | STAY substitution OR-composed with PAG, **not** IA-suppressible (agent.py:11554-11580); post-override approach/withdraw score bias | per-E3-tick; baseline frozen while active | ENDOGENOUS (relative onset) | consumer found | pag/defensive_orienting.py:196-330; agent.py:2727-2765, 10380-10470; config.py:7309-7320 | **156 shape**: exit = identification confidence += rate x (1 - current_excess/peak). With floor_rise=0 and max_duration=0, arrest near a persistent stimulus keeps excess ~peak, so there is no exit. Rst R. SS: orienting input piggybacks on the MECH-205 surprise path |
| Instrumental avoidance (ilPFC) | MECH-357, SD-058 | DEFAULT-OFF-IMPLEMENTED | z_harm_a norm drop after a directed action (credits efficacy); threat envelope floor 0.1 / ref 0.5 | `avoidance_efficacy` gives (a) an E3 per-action bias (agent.py:9983) and (b) PAG freeze suppression above 0.5 (agent.py:11511-11526) | EMA lr 0.05, leak 0.02 | ENDOGENOUS | consumer found | agent.py:2230-2245, 6145-6158; config.py:6801-6813 | 155 (absolute floor/ref on a learned norm); Rst: efficacy **P** across episodes (agent.py:4395-4399). SS: z_harm_a norm drives both PAG entry and IA suppression |
| LPB interoceptive routing | MECH-282 | DEFAULT-OFF-IMPLEMENTED | **raw** harm_obs (hazard slice) + drive_level | masks the resource slice fed to HarmEncoder (agent.py:6007-6009); `external_magnitude` becomes the PAG input (agent.py:11464-11468); `z_harm_intero` feeds SD-037 | per-tick, non-trainable | ENDOGENOUS obs | consumer found | regulators/lpb_interoceptive_routing.py:1-60; agent.py:2849-2858, 6080-6098; config.py:7412 | notable: the only PAG input path that **bypasses the untrained encoder** |

### D. Veto

| name | ids | STATUS | signal read | variable changed (consumer) | timescale | endo/harness | consumer check | citations | flags |
|---|---|---|---|---|---|---|---|---|---|
| Two-part veto readout | MECH-039 (+MECH-046 DV) | TELEMETRY-ONLY even when on | CeA / override (INTERRUPT); PAG freeze, habenula, MECH-449 deltas (CONTROL) | readout dict only (`get_veto_readout`) | per-step | -- | config docstring states "NO effect on scoring, selection or any producer" (config.py:5940-5963); the code only reads producer state (agent.py:4773-5100) | agent.py:4773-5100; config.py:5958 | -- |
| Go/No-Go constitution + endogenous safety No-Go | MECH-449, ARC-107 | DEFAULT-OFF-IMPLEMENTED (triple-gated: `use_go_nogo_constitution` config.py:2299, `use_gng_endogenous_safety` 2353, **and** the enclosing branch needs `use_modulatory_shortlist_then_modulate` (2121) or `use_f_eligibility_demotion` (2242) with a non-None modulatory accumulator, e3_selector.py:4353-4360) | per-candidate mean E3.harm_eval_head over predicted z_world, **z-scored against a per-agent running mean/sd** (EMA 0.999, sd floor 0.01, warmup 200), mapped so No-Go fires at z >= 2; the perseveration axis reuses the dACC MECH-260 vector | `eligible_idx`: vetoed candidates dropped from the argmin set (e3_selector.py:4438-4449). Fail-open: if all are unsafe, the fallback commits a vetoed candidate | per E3 tick; running scale **P** per agent (agent.py:4185 comment) | ENDOGENOUS (harm valuation; head trained by harness) | consumer found. **But the downstream freeze masks it**: PAG substitution happens after selection (agent.py:11527-11552), so the veto cannot show in the executed action while frozen. Q-111 / V3-EXQ-1090: veto fires, executed action 0 on 3000/3000 ticks | agent.py:5123+, 10843-10870; e3_selector.py:2267+, 4438-4449; config.py:2267-2360 | **ARC-155-compliant by design** (relative running-z). SS: shares harm_eval_head with the E3 M term |

### E. Interrupt / de-commit / relief / safety / escape

| name | ids | STATUS | signal read | variable changed (consumer) | timescale | endo/harness | consumer check | citations | flags |
|---|---|---|---|---|---|---|---|---|---|
| Urgency interrupt | MECH-091 | DEFAULT-OFF-IMPLEMENTED by upstream gate only: **it has no flag of its own** and is live whenever z_harm_a exists (SD-011 on) | `||z_harm_a||_2` (or z_harm_un / z_harm_suffering if redirected) > `urgency_interrupt_threshold` 0.8, while beta is elevated | `beta_gate.release()`, `_committed_step_idx=0`, anchor keys cleared | per select_action tick | obs ENDOGENOUS; threshold HARNESS-SET | consumer = beta gate (agent.py:8030-8036) | agent.py:7960-8036; config.py:1659-1664 | **155**: absolute 0.8 vs measured norms 2.8-4.2 (1107), so once SD-011 is on it fires on every committed tick. Commitment is then impossible under threat. SS with PAG (same z_harm_a norm) |
| Harm phase reset | MECH-091, MECH-092 | **LIVE-AT-DEFAULTS** | env `harm_signal<0` (driver call), owned, not hypothesis | `clock._pending_phase_reset` forces an E3 tick at the next advance and sets quiescent=False (clock.py:149-155, 189-190) | event, one tick | env obs via **driver** call (ENDOGENOUS content, HARNESS-dependent delivery) | consumer found (clock.advance, agent.py:12042/12074/12096) | agent.py:12364-12379 | not a regime change: it re-times selection only |
| Volatility estimate | MECH-104, Q-007 | TELEMETRY-ONLY at defaults | var(E3 running_variance) over a 10+ window | latent volatility input only if `volatility_signal_dim>0` (default 0, config.py:436; agent.py:6005-6006); otherwise the veto-readout dict | per E3 tick | ENDOGENOUS | grep `volatility_estimate`: only agent.py:5040 (telemetry) and 6006 (gated). The MECH-104 de-commit itself has **no dedicated code**; comments name it `control_plane.volatility_interrupt` = the ARC-016 rv commit gate (agent.py:1268-1271), which is G1's row | e3_selector.py:1031-1033, 1118-1125 | -- |
| AIC analog | SD-032c | DEFAULT-OFF-IMPLEMENTED | z_harm_a norm (or suffering), drive_level (goal_state), beta elevated, coordinator mode | `aic_salience` goes to the coordinator MECH-259 urgency trigger (agent.py:9047-9052); `harm_s_gain` goes to SD-021 | per-tick | ENDOGENOUS | consumer found | cingulate/aic_analog.py:29-36, 174-261; agent.py:885-895, 6425-6466; config.py:4822 | SS: drive + threat into one salience scalar |
| Relief-completion comparator | MECH-302 | DEFAULT-OFF-IMPLEMENTED | z_harm_a norm drop >= 0.10 over 5 ticks, from >= 0.05 | `beta_gate.release()` + VALENCE_LIKING write (only if valence_liking_enabled); also drives the MECH-304 prototype update | 5-tick window | ENDOGENOUS | consumer found (agent.py:8469-8486, 6988-6992) | comparator/suffering_derivative_comparator.py:1-53; agent.py:6972-6981; config.py:4928-4932 | 155 (absolute drop on a learned norm); Rst R. SS: one event fires both release and safety learning |
| Conditioned safety store | MECH-304, SD-051 | DEFAULT-OFF-IMPLEMENTED | cosine(z_world, EMA prototype); prototype updated only on MECH-302 events | beta release when sim > 0.5 (+ liking write) | EMA alpha 0.1 | ENDOGENOUS | consumer found (agent.py:8494-8517) | safety/conditioned_safety_store.py; agent.py:960-975, 6983-6992; config.py:4949-4956 | Rst: prototype **R** per episode (agent.py:4234-4237), so learned safety does not carry across episodes |
| Contextual safety terrain | MECH-303 | DEFAULT-OFF-IMPLEMENTED | `||z_harm_a||` < 0.05 (or proximity < 0.25) triggers accumulate_safety at z_world | beta release when evaluate_safety >= 1.0 (agent.py:8522-8545); also feeds the escape bridge safety signal | accumulate 0.01 per tick; terrain P | ENDOGENOUS | consumer found | agent.py:7005-7040; residue/field.py:874-916; config.py:3811, 4975 | 155 (absolute harm-absent threshold on a learned norm) |
| Escape affordance bridge (+ relief/safety half-switches default True) | SD-059, MECH-358 | DEFAULT-OFF-IMPLEMENTED (half-switches inert under master False) | z_harm_a norm drop after an action class (relief); threat absent (safety); optional trained safety signal | per-action approach bias into the E3 score_bias (agent.py:10069) | EMA 0.1, leak 0.01 | ENDOGENOUS | consumer found | pfc/escape_affordance_bridge.py; agent.py:2258-2280, 6166-6222; config.py:6887-6915 | 155 (threat floor 0.1 / ref 0.5 absolute) |
| Trainable escape learner (relief critic / safety predictor default True) | post-603i | DEFAULT-OFF-IMPLEMENTED | z_world, z_self, z_harm_a, action | trained heads give an approach bias (agent.py:10112) | online optimizer lr 0.03 | ENDOGENOUS | consumer found | pfc/trainable_escape_affordance_learner.py; agent.py:6226-6245; config.py:6944-6961 | learned predictions **P** (agent.py:4410-4415) |
| E2 escape linker | post-603i | DEFAULT-OFF-IMPLEMENTED (the E3 bias needs a further flag, `use_e2_escape_linker_e3_bias`) | E2.world_forward geometry + z_harm_a norm | viability readouts, then a bias (agent.py:10172) | online | ENDOGENOUS | consumer gated by a second flag | pfc/e2_escape_affordance_linker.py; agent.py:6252-6290; config.py:6970-6975 | -- |
| Blocked agency | MECH-353 | DEFAULT-OFF-IMPLEMENTED | outcome mismatch (floor mode `absolute` 0.1 default; `relative` option exists), motor agency, goal_active | E3 assert bias (agent.py:9944); de-commit after 5 consecutive ticks (agent.py:8409-8420) | leaky integrator (0.2 / 0.1) | ENDOGENOUS | consumer found | affect/blocked_agency.py; agent.py:2110-2143, 5250-5320; config.py:6704-6732 | 155 at default floor mode; Rst R |
| Harm suffering accumulator | MECH-219, SD-019b | DEFAULT-OFF-IMPLEMENTED; **TELEMETRY-ONLY when on without a redirect flag** | z_harm_un, escapability (`constant` 1.0 = HARNESS) | `z_harm_suffering`; read only via the redirect flags `harm_suffering_redirect_{aic,pag,mech091,dacc,pacc}` (all False) | asym EMA (rise 0.2, fall 0.01) | escapability HARNESS | consumers found but each is flag-gated (agent.py:6433-6438, 11474-11482, 8025-8029) | affect/harm_suffering_accumulator.py; agent.py:2155-2180, 6355-6365; config.py:6838-6858 | requires use_harm_un; Rst R |
| TPJ agency comparator | MECH-095 | TELEMETRY-ONLY even when on | E2 efference prediction vs next z_self | `_tpj_last_agency_signal` / `_is_self_caused` | per-tick | ENDOGENOUS | grep `tpj_last_agency_signal|tpj_last_is_self_caused` across ree_core: only assignments/resets; no reader. `owned=` for update_residue is left to the driver (config.py:5030-5036) | comparator/tpj_comparator.py; agent.py:979-990, 4630-4663 | -- |

### F. Valence / wanting / liking

| name | ids | STATUS | signal read | variable changed (consumer) | timescale | endo/harness | consumer check | citations | flags |
|---|---|---|---|---|---|---|---|---|---|
| Valence vector master | SD-014, ARC-036 | DEFAULT-OFF-IMPLEMENTED in effect: `valence_enabled=True` is a **permission** switch, but **no writer is live at defaults**, so readers see zeros | -- | `rbf_field.valence_vecs` read by hippocampal scoring/replay (module.py:1160, 1814, 3089, 3741, 4179) | none (no decay unless valence_bounding) | -- | writers audited, all gated off: agent.py:6617 (valence_harm), 8481/8512 (MECH-302/304 + liking), 12330-12348 (surprise_gated_replay), 13437 (MECH-295), 13601/13612/13661 (serotonin `tonic_5ht_enabled=False`), 13685 (valence_liking), 13744/13759 (schema_wanting); module.py:3667 (backward_credit_sweep), 3781 (offline_wanting_spread) | residue/field.py:918-1056; config.py:3972-3992 | P (lives in the residue field, not reset) |
| valence_harm | SD-014 h | DEFAULT-OFF-IMPLEMENTED | post-SD-021 `||z_harm_s||` | VALENCE_HARM_DISCRIMINATIVE at z_world | per sense() | ENDOGENOUS | hippocampal readers above | agent.py:6616-6630; config.py:4431 | -- |
| valence_liking | SD-014 l | DEFAULT-OFF-IMPLEMENTED | benefit_exposure >= 0.1 (driver calls `update_liking`) plus relief/safety events | VALENCE_LIKING | event | HARNESS call | as above | agent.py:13668-13689; config.py:4432-4433 | -- |
| incentive sensitization | SD-014 (EXQ-887 fix) | DEFAULT-OFF-IMPLEMENTED (also needs serotonin on) | benefit salience x drive | per-node gain, then VALENCE_WANTING | saturating accumulator | ENDOGENOUS + HARNESS call | as above | agent.py:13595-13630; config.py:4450-4453 | -- |
| schema wanting | SD-014/MECH-307 | DEFAULT-OFF-IMPLEMENTED | E1 schema salience >= 0.3 | VALENCE_WANTING (+ anticipatory liking) | per-tick | ENDOGENOUS | as above | agent.py:13730-13770; config.py:1038 | -- |
| MECH-205 surprise valence write | MECH-205, MECH-307 | DEFAULT-OFF-IMPLEMENTED (`surprise_gated_replay=False`, config.py:4266) | E3 PE minus its EMA > 1e-5 | VALENCE_SURPRISE (signed/split variants); caches `_last_residue_surprise` for orienting | EMA | ENDOGENOUS | consumers: hippocampal replay priority, orienting | agent.py:12298-12353 | SS: one PE event feeds both valence and orienting |
| Benefit eval (Go channel) | ARC-030, MECH-112 | DEFAULT-OFF-IMPLEMENTED | resource/goal proximity | E3 score minus benefit (after warmup) | per-tick | ENDOGENOUS | consumer e3_selector.py:1891-1905 | config.py:1608 | G2 overlap |
| MECH-295 liking bridge | MECH-295 | DEFAULT-OFF-IMPLEMENTED | drive_level x goal proximity; drive floor 0.01 | per-candidate E3 approach bias (agent.py:9654-9690) + anticipatory liking write (13418-13440) | per-tick | drive = env-derived | consumer found | config.py:7773-7800 | the floor was historically never crossed (config comment re V3-EXQ-540c); G2 overlap |

### G. Residue field (MECH-018 / SD-005)

| name | ids | STATUS | signal read | variable changed (consumer) | timescale | endo/harness | consumer check | citations | flags |
|---|---|---|---|---|---|---|---|---|---|
| Residue RBF harm field | MECH-018, SD-005, ARC-013/INV (no-erasure) | **LIVE-AT-DEFAULTS** | env `harm_signal<0` (driver's `update_residue`), located at the current **z_world** (endogenous latent), scaled x0.1 and x min(2, world_delta) if supplied | RBF `centers`/`weights`/`active_mask` (ring of 32 slots, field.py:165-180). Read by **E3 score** `rho_residue(0.5)*phi` over every candidate (e3_selector.py:1555-1563, 1836, 1869, 1889) and by **hippocampal** terrain-prior input (module.py:591-604) + CEM elite terrain score (module.py:1785-1797, 1878-1886) | **lifetime**: decay_rate 0.0 (config.py:3705); not reset per episode (agent.py:4102) | content ENDOGENOUS (z_world); event delivery via DRIVER call | consumers found (above). Both MECH-131 lesion switches `terrain_prior_residue_channel_enabled` / `score_trajectory_residue_terrain_enabled` default True (config.py:3095, 3116), so the reads are on | agent.py:12364-12376; residue/field.py:736-784; e3_selector.py:413 (E3 holds the same field, agent.py:409-410) | Observations. (i) Bandwidth 1.0 is ~8x the reachable z_world cloud, so the field is near-broadcast (field.py:426-440, measured ratio ~1.007) and weakly argmin-relevant. (ii) The ring recycles the slot location but `weights[idx] += intensity` keeps the old weight, so old harm mass is **transported** to the new location (field.py:170-172). (iii) **SS / second writer**: E3 post_action_update writes `harm_magnitude=1.0` again when committed (e3_selector.py:4955-4959), bypassing `owned` and `hypothesis_tag`. (iv) This is the only cross-episode threat memory at defaults |
| Neural-field approximator | MECH-018 | LIVE-AT-DEFAULTS as a **static** term (no within-life change) | z_world | `evaluate()` = rbf + 0.1 x **untrained** Softplus MLP (field.py:466-473, 707-735): a fixed random positive offset added to every E3 residue cost and hippocampal terrain read | never changes at defaults | -- | training needs `use_offline_integration_gradient_step` (config.py:3734) plus a caller: `offline_integration()` has no in-tree caller (config.py:7657-7672); the sleep call site is `use_sleep_residue_integration=False`. CANNOT-DETERMINE whether a driver's optimizer over `agent.parameters()` touches it (driver-dependent) | field.py:1225-1400 | not a controller; a frozen random prior |
| Residue `integrate()` | MECH-018 | DEFAULT-OFF-IMPLEMENTED | stored harm locations | neural_field params | per sleep cycle / driver call | HARNESS | see above | agent.py:14005-14028; config.py:7657-7674 | GFLAG-0441 sampling collapse at world_dim 32 unless `use_dim_scaled_integrate_sampling` |
| Benefit terrain + DA-modulated density | ARC-030, SD-024, MECH-232 | DEFAULT-OFF-IMPLEMENTED | benefit exposure (+ phasic DA for the cluster count) | benefit RBF, read by the hippocampal terrain prior (module.py:612-615) and E3 benefit | lifetime | ENDOGENOUS + driver | consumer found | field.py:182-254, 786-872; config.py:3782, 3957 | "DA-named analogue" = allocation count/bandwidth, not a controller; G2 overlap |
| `_harm_this_episode` | -- | TELEMETRY-ONLY at defaults | harm magnitude | metrics + `get_state().harm_accumulated` | per episode (R) | -- | grep `harm_this_episode`: only agent.py:12366 (write), 12389 (metrics), 14826 (get_state) | agent.py:3428, 4133 | -- |

### H. Drive (light touch; G2 owns)

| name | ids | STATUS | signal read | variable changed | timescale | endo/harness | consumer check | citations | flags |
|---|---|---|---|---|---|---|---|---|---|
| drive_level | SD-012 | CANNOT-DETERMINE here (G2 row) | body obs (`compute_drive_level`, static) | read by AIC, LPB, MECH-295, PCC (all off at defaults) and the goal pathway | per-tick | env obs | the G3-family consumers are all default-off | agent.py:13693; agent.py:6440-6442, 6085-6089 | -- |

## 2. Dead ends

These are controllers whose output nobody reads, knobs nothing reads, and variables that matter but have no live endogenous setter.

- **CeA `pre_softmax_additive`** (config.py:7215 = True): a dead knob, never read (grep above). It "describes" behaviour that happens regardless of its value.
- **CeA `cortical_confirmation` hold branch**: unreachable, because the agent always passes None (agent.py:6564-6572). `escapability_hint` and `cue_features` are documented no-ops.
- **MECH-039 veto readout**: telemetry even when on.
- **TPJ comparator (MECH-095)**: telemetry even when on; nothing reads agency_signal.
- **E2_harm_s via the agent**: telemetry even when on (SCI buffer + OFC "no score effect"). The E3 `harm_forward_model` path exists but the agent never passes it.
- **Harm suffering accumulator (MECH-219)**: telemetry when on unless one of five redirect flags is also on.
- **MECH-104 volatility_estimate**: telemetry at defaults (volatility_signal_dim=0). There is no dedicated MECH-104 de-commit code.
- **`_harm_this_episode`**: telemetry.
- **Valence vector**: `valence_enabled=True` but no live writer at defaults, so every hippocampal valence read returns zeros.
- **`gaba_tone`**: sets the PAG exit threshold and the decay rate, but nothing endogenous sets it (`set_gaba_tone` has no in-tree caller). It is a harness pharmacology knob.
- **`harm_suffering_escapability_mode="constant"` 1.0**: escapability, the variable MECH-219 is about, is harness-set.
- **Upstream starvation**: z_harm and z_harm_a do not exist at defaults. Even when SD-011 is on, the AffectiveHarmEncoder is trained only if the harness calls `compute_harm_accum_loss` (prior records: untrained in every recipe). So every z_harm_a controller is fed by an untrained, EMA-smoothed latent whose onset information was destroyed upstream.
- **Freeze masks veto**: the MECH-449 No-Go acts on `eligible_idx` inside E3, but the PAG freeze replaces the emitted action afterwards (agent.py:11527-11552). While frozen, the veto's decision never reaches behaviour (Q-111 / V3-EXQ-1090).
- **Episode resets erase within-life threat learning** for CeA, BLA (including the remap PE baseline), PAG, orienting, the MECH-302 comparator, the MECH-304 safety prototype, blocked agency and the suffering accumulator. What persists: IA efficacy, trainable escape predictions, the MECH-449 running harm scale, the residue/safety/benefit RBF fields and gaba_tone.

## 3. Live edges at defaults (signal -> variable (consumer file:line))

1. env harm_signal<0 (driver `update_residue`, agent.py:12364) -> residue RBF weights/centers at the current z_world (field.py:170-172) -> E3 trajectory score phi, rho=0.5 (e3_selector.py:1836, 1869, 1889).
2. The same residue field -> hippocampal terrain-prior input (module.py:591-604) and CEM elite terrain score (module.py:1785-1797, 1878-1886).
3. harm_occurred while committed (agent.py:12213-12216) -> second residue write, harm_magnitude=1.0 (e3_selector.py:4955-4959). This bypasses `owned` and `hypothesis_tag`.
4. env harm_signal<0 -> `clock._pending_phase_reset` (agent.py:12379 -> clock.py:189) -> forced E3 tick and quiescent=False at the next advance (clock.py:149-155).
5. Static, no within-life change: the untrained neural_field adds a fixed 0.1 x MLP(z_world) to edges 1-2 (field.py:718, 732).

Nothing else in the threat/defence/veto/freeze/affect family changes a downstream variable at default config.

## 4. ARC-155 / ARC-156 summary (when the family is switched on)

**ARC-155 (absolute threshold on a learned quantity):**
- CeA 0.5 on `||z_harm_a||_1/dim`
- PAG theta_freeze on `||z_harm_a||_2` x duration
- MECH-091 urgency 0.8 on `||z_harm_a||_2`
- BLA arousal 0.4/0.7
- MECH-302 drop 0.10 / min 0.05
- MECH-303 harm-absent 0.05
- IA and escape-bridge threat floor 0.1 / ref 0.5
- blocked-agency outcome floor 0.1 (absolute mode default)

**Compliant exceptions:** the MECH-449 running-z safety No-Go, the BLA remap sigma (baseline reset per episode, though), and the orienting onset-over-own-baseline.

**ARC-156 (exit starved by the regime):**
- **PAG freeze exit** needs z_harm_a to fall, but STAY keeps the agent at the hazard and z_harm_a is an EMA. No max-duration cap by default.
- **MECH-287 descending release** needs anchor invalidations, which need world change, which STAY suppresses. V3-EXQ-1106: 0 drive-steps while frozen.
- **Defensive orienting exit** needs the excess to fall relative to its peak while the agent is arrested at the stimulus. floor_rise=0 and max_duration=0.

**Shared source:** a single `||z_harm_a||` scalar simultaneously drives
- the PAG entry and exit,
- the MECH-091 de-commit,
- IA freeze suppression,
- the escape-bridge threat envelope,
- AIC urgency,
- CeA (L1 form),
- the MECH-302 relief event, which is also the MECH-304 learning trigger.

When SD-011 is on at calibrated scale, these fire together (freeze from tick 1 plus de-commit every committed tick). They are not an arbitrated regime choice.
