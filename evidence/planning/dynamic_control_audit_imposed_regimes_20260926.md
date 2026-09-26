# Dynamic-control audit, step 3: where the experimenter or harness imposed a regime the organism should have selected

- **Status: FINAL (read-only audit).** Written 2026-09-26 by session `bt0926-dcb` (worker DC-B, orchestrator `orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-dynctl-b-imposed-regimes`.
- **Scope:** step 3 of the user's audit in `docs/thoughts/2026-09-26_dynamic_control_coordination_hole.md` ("find cases in the experimental corpus where the experimenter or orchestrator had to impose a cognitive regime that an autonomous organism should have selected itself"). Plan of record: `.scratch/breakthrough-20260924/DYNCTL_PLAN.md`, row DC-B. This record builds on the intake (`thought_intake_2026-09-26_dynamic_control_coordination_hole.md`) and cites **ARC-155, ARC-156, ARC-157, Q-111, Q-112, MECH-597** without re-registering anything. Dynamic control is treated as a **hypothesis**. This record proposes no controller, and certainly no monolithic executive.
- **Nothing was built, queued, chipped or registered.** No `ree_core`, queue, `claims.yaml` or substrate_queue edits. No probes were run on the Mac.
- **Code read at:**
  - ree-v3 `origin/main` **`436a988`**. All `file:line` citations are against this sha unless marked **(branch)**.
  - **(branch)** = `origin/integration/coupled-loop-repair` **`4070b0e`**.
  - REE_assembly `origin/master` `2e1f6a60e43` at writing time.
- **Evidence domain: D0 throughout.** This record reads code and records, cites measured results from other records, and runs a regex census. It makes no new measurement. Driver counts come from the census and are approximate. The method is in sec 6.

## 0. Headline

1. **The most pervasive imposed regime is the episode boundary, not the curricula.**
   - The harness calls `agent.reset()` explicitly in **1156 of 1559** drivers.
   - `REEAgent.reset()` (`ree_core/agent.py:4101-4552`) wipes about 55 controller states: the PAG freeze gate (`:4458`), the salience coordinator (`:4181`, which forces `current_mode = "external_task"` at `cingulate/salience_coordinator.py:478-485`), the commitment beta gate (`:4156`), dACC (`:4178`), CeA (`:4446`), curiosity (`:4291`), instrumental avoidance (`:4398`), the stuck-state detector (`:4360`), the hippocampal staleness accumulator (`:4544`) and more. It is also the only default route into sleep (`:4126`).
   - So the experimenter's clock is the organism's **de facto regime controller**. It supplies:
     - the only exit from absorbing regimes. V3-EXQ-1107's freeze locks from tick 1 and `pag_max_freeze_duration = 0` means "never", so the life ends frozen. This is ARC-156's evidence-starvation shape, with the reset as the hidden termination input.
     - the "one switch per life" mode artefact.
     - the near-reset EMA transients (GFLAG-0559/0560) that carried W3's `k` criterion and 84% of the gate-(c) failure.
     - a one-hot "world changed" flag. Q-108 forbids exactly this inside its recovery test.
   - Weights and the residue field persist across the boundary (`agent.py:4102`, "Does NOT reset residue"), so this is the same organism with its regime state cleared by the harness. It is not a new organism.
2. **By the user's ten decisions, the most-imposed and most load-bearing are, in order:**
   1. freeze-vs-reopen plasticity
   2. broad regime change, including the episode boundary, curricula and sleep entry
   3. exploit-vs-explore
   4. defensive entry/exit
   5. precision/routing operating points

   The rarest are quarantine-and-relearn (one exploratory, oracle-timed seed: N5 `shift_oraclefull`) and habit-vs-deliberative. Habit-vs-deliberative is rare because it is **pinned for the whole life**, not switched: the native arbitrator SD-081 is default-OFF. Ranking and counts are in sec 3.
3. **The endogenous signal the organism would have had falls into three different situations.** The distinction matters for DC-D's "shape of the failure" (step 4):
   - **(a) Signal measured ABSENT or failed.**
     - Shift / PE attribution: N5, all 5 seeds; V3-EXQ-910, 0/30 aligned.
     - Freeze exit: V3-EXQ-1106, 0 drive-steps while frozen.
     - CeA onset (cea reprobe).
     - Arousal: endogenous `||z_beta||` range ~0.9% (MECH-005 pilot).
   - **(b) Endogenous machinery EXISTS but is default-OFF and almost never composed.**
     - The MEL sleep-need arm: 3 drivers.
     - The SD-091 endogenous coalition trigger: 1 driver.
     - SD-081 dual-system arbitration: 7 driver mentions.
     - The `external_task_drive` channel: 15 drivers.
     - EMA reset-init: campaign preset only.
     - The infant curriculum's metric gates, which read the agent's own state but are applied by the harness, one-way, behind episode floors.
   - **(c) An endogenous signal EXISTS and the harness OVERRIDES it.**
     - E3's running variance is forced to 0.001 (6 drivers).
     - MECH-357's learned avoidance efficacy is held up by a protective scaffold floor (81 drivers).
     - Stage-0 force-feeds benefit and drive into `update_z_goal` (97 drivers).
     - When the organism's gate withholds an action, `StepHarness` substitutes a random one (`experiments/_harness.py:322-327`; 324 drivers contain a withhold-fallback).

   One counterweight belongs with (a)-(c). For explore-to-exploit, an endogenous critic-utility mode gate **was** built and tested (V3-EXQ-755). It added no lift over a fixed schedule, so the harness clock was kept. On that task the missing lever was capacity, not regime selection.
4. **Stale premise corrected.** The capture note says reversals were "restored only by an external task drive, which is an imposed regime". That is only half right.
   - `external_task_drive` is computed **endogenously**, per tick, from the commitment gate and goal proximity (`agent.py:9106-9133`).
   - What the experimenter imposes is the channel's **existence** (`use_external_task_drive` default False, `config.py:4706`) and its **gain**: hand-set affinity 3.0 and salience 2.0 against a bias of 1.0 (V3-EXQ-1107 driver `:451-455`). In the modetrace A4 arm the goal-active gate was also switched off.
   - In the one trained evaluation that measured it, the channel was ~dead: `et_drive_mean` 0.00053 in V3-EXQ-1067. So even the imposed channel does not carry reversals after training.
5. **Two regime decisions have no claim owner** (intake sec 6(ii) asks for exactly this check). Both are surfaced for DC-D and `/governance`. Neither is registered here. Details in sec 4.
   - (i) **Which controller states a life boundary may reset**, versus which must persist and be exited endogenously. SD-075 owns one EMA only; GFLAG-0559/0560 own EMA init only.
   - (ii) **Whether developmental stage transitions** (end of babbling, curriculum stage advance) must be read by the organism or may be set by the experimenter. ARC-019 (provisional) asserts "explicit curriculum gates" and does not say whose.

## 1. Premises re-measured before writing

| # | premise (source) | re-measured | verdict |
|---|---|---|---|
| P1 | "Reversals were restored only by an external task drive, which is an imposed regime" (capture notes, thought doc) | `agent.py:9106-9133`: engagement = `goal_active ? clip(commit_w*beta_elevated + prox_w*goal_proximity(z_world), 0, 1) : 0`. The weights and switch are experimenter-set (`config.py:4706-4716`; 1107 `:451-455`). V3-EXQ-1067 autopsy: eval drive 0.00053 | **corrected**: an imposed channel and gain over an endogenous signal, not an imposed mode. The imposed mode-pin idiom is a different, rarer thing (row R18) |
| P2 | "N5: wholesale quarantine plus renewed babbling appears capable of relearning" (thought doc) | N5 record sec 3a/4.3: `shift_oraclefull` was one seed (721), exploratory and not verdict-bearing. It was triggered at the shift step, which the harness knew | **holds, with the qualifier**: the revision worked only when the harness supplied the timing, the scope (the WHOLE retained set) and the dose (a full 2400-step epoch). All three are decisions the organism did not make |
| P3 | the queue carries regime-imposing work (brief: search `experiment_queue.json`) | `git show origin/main:experiment_queue.json`: **0 items** at `436a988` | nothing queued to classify. The impositions live in drivers, `_lib` helpers, the branch trainer API and the campaign probes |
| P4 | "the coupled-loop campaign sets babbling phases, frozen retained sets and trainer schedules from the harness" (capture notes) | (branch) `ree_core/utils/waking_trainer.py:771` `set_e2_world_source("babble"/"on_policy")` is harness-called (e.g. `probes/w3/w3_l2r_member_probe.py:91`). The retained set is append-only and FROZEN (`:353`, `:524-547`). The trainer steps every K ticks (`on_waking_step`). The A1 draft fixes the developmental epoch at 2400 steps, "DRAFT: plan's number, not grounded" (`coupled_a1_preregistration_draft_20260925.md:235`) | **holds** |
| P5 | a sub-scan reported that 20 drivers pin `e3._running_variance` to a literal | `git grep -l -E '_running_variance\s*=' origin/main -- experiments/v3_*.py`: **6**. The forced-rv arm in `committed_mode_curriculum.py:60-67` is a docstring usage example | **corrected to 6** |
| P6 | sleep has no endogenous trigger | `use_mel_entry` (`config.py:7496`) and `use_within_life_sleep_trigger` (`:7513`) exist, both default False. Enabled in 3 drivers (929/933/933a). The need arm degrades to the step ceiling where MEL is noise-level (`sleep_substrate_plan.md:245`). V3-EXQ-933 found it a level detector (follow-up SD-SLEEP-ENTRY-PRESSURE) | **corrected**: the trigger exists but is default-off and weak in this env. Default entry is a K-episode clock (`sleep/phase_manager.py:2,17-18,253`) or a step modulo (`agent.py:14030-14031`, default 100 at `config.py:4209`) |

## 2. Catalogue of imposed regimes

**Class codes:**
- **T** = timed switch (the harness flips the regime at a clock or phase boundary).
- **P** = pinned for the whole life (a regime an organism would vary is held constant).
- **R** = reactive rescue (the experimenter imposed it after seeing a failure).
- **O** = override (the harness overwrites a native signal or decision).
- **M** = measurement convention (legitimate for measurement, but it still pre-empts the decision).

Many rows are legitimate experimental control. The table records **which decision each pre-empts**. It does not say each is an error.

**Decision codes** (the user's list):
- D1 trust vs interrogate the model
- D2 exploit vs explore
- D3 precision/routing
- D4 PE attribution (noise / action failure / model error / env change)
- D5 freeze vs reopen plasticity
- D6 quarantine and relearn
- D7 habit vs deliberative
- D8 defensive entry/exit
- D9 which representations influence E3
- D10 broad regime

**Prevalence** is census counts over 1559 top-level `experiments/v3_*.py` drivers (sec 6). They are approximate.

Citations marked **+** were located by a sub-scan (two read-only Explore agents) and spot-checked in bulk rather than each re-opened. All unmarked citations were re-opened at the stated sha.

| # | where | what is imposed | stated WHY (record's own words) | cls | decisions pre-empted | endogenous signal available at that moment | prevalence | load-bearing? |
|---|---|---|---|---|---|---|---|---|
| R1 | `agent.py:4101-4552` (`reset()`), called by drivers at every env episode end | ~55 controller-state resets at a harness-chosen time: freeze gate `:4458`, mode register -> external_task (`salience_coordinator.py:478-485`), beta gate `:4156`, dACC `:4178`, CeA `:4446`, curiosity `:4291`, avoidance `:4398`, staleness `:4544`; sleep entry `:4126` | episodic-RL convention: the env respawns the body ("Reset agent for a new episode") | T/O | D10, D8 (exit), D5, D4 (acts as a world-changed flag), D1 (EMA / precision baselines restart) | none needed, because the boundary is exogenous. For a time-out end the organism has **no** event at all. Absorbing regimes have no regime-surviving exit input (ARC-156) other than this | **1156** drivers call `agent.reset()`; 1165 set an episode length | **very high**: 1107's only exit from a freeze on tick 1; `n_switches == n_episodes` (modetrace sec 1a); GFLAG-0559/0560 (W3 k carried by ticks within 8 of a reset; 84% of gate-(c) failure, `gate_c_with_ema_reset_init_20260926.md`); sleep reachable only via boundaries (sleep plan GAP-9 `:236`) |
| R2 | train -> eval by schedule: scaffolded P2 `scaffolded_sd054_onboarding.py:2862,2894`; `committed_mode_curriculum.py:485,494`+; `_lib/probe_warmup.py:765-767`+; `_lib/goal_pipeline_tier1.py:685`+ | plasticity switched off at a phase boundary (`agent.eval()`, `no_grad`, no optimizers) for the measurement window | "frozen-policy measurement" (scaffolded `:45`); bring the agent "to a non-degenerate action-value landscape BEFORE telemetry" (probe_warmup `:28-29`)+ | M/T | D5 | E3 running variance (ARC-016) and curiosity learning-progress exist. None is wired to a plasticity gain. N5 P1: no MECH-398 / MECH-207 / ACh signal in `ree_core` | ~376-470 drivers (warmup + `.eval()` + optimizer) | **high, but methodological**: almost every reported number is a frozen-snapshot readout, so lifelong self-regulated plasticity is essentially untested |
| R3 | random-policy encoder warmup, then freeze: `_lib/zworld_p0_warmup.py:1-8,36-42` (RandomPolicy `:173-174,:226-255`+); `_lib/allon_training.py:533,564`+; `_lib/zharm_a_p0_warmup.py:229-260,653`+ | exploration by a random policy the organism does not choose, in a phase the harness times; encoder trained only there ("P1 = REINFORCE on stop-gradient latents with the encoder optimiser not stepped") | without it z_world "stays a FROZEN RANDOM PROJECTION for the whole run" (`zworld_p0_warmup.py:5-6`); "the agent is deliberately NOT driven here"+ | T | D2, D5 | none native for "my encoder needs training". Novelty / curiosity exist but do not gate encoder plasticity | 519 drivers draw random actions outside a fallback (378 also mention warmup); 34-63 use the z_world P0 lib | **high**: the omitted warmup is the load-bearing defect in V3-EXQ-882/875/728 (~40 autopsies cite it)+ |
| R4 | structured babbling epoch and its END: (branch) `waking_trainer.py:771` `set_e2_world_source`; retained FROZEN `:353,:524-547`; A1 epoch 2400 steps (`coupled_a1_preregistration_draft_20260925.md:235`); campaign plan W2a/W3 rows (`coupled_loop_repair_campaign_plan.md:62,64,131-137`) | the harness decides when the organism babbles, for how long, and that its developmental memory is frozen afterwards | E2's world head is action-blind because the agent's own concentrated behaviour starves it of action coverage (synthesis 7b); one-off exposure is not durable (MECH-597) | T/P | D2, D5, D6 | own-action concentration is endogenously knowable (the modal-class share is 42-94%, W3). **Not read by anything** | campaign probes W3/N2/N3/N5 and A1 INT arms; 1 main driver (V3-EXQ-1108) | **high**: the W3 member-gate PASS and the MECH-597 evidence are conditional on harness-timed babbling plus a frozen retained set |
| R5 | N5 revision: `probes/n5/n5_probe.py` and `n5_probe_explore.py`; record `n5_ach_gated_unfreeze_probe_20260926.md` sec 2, 3a, 4.3 | g, surprise, unfreeze, bout length, FIFO replacement and the `oraclefull` wholesale quarantine plus 2400-step re-babble, all harness-side and triggered at the known shift step | "no usable native g" (P1); the revision half needed wholesale invalidation (sec 4.3) | R/T | D4, D6, D5, D2 | **measured absent**: raw and action-contrastive PE do not separate shift from no shift (clamped pair, 5/5). Spurious opens 5/5. Corroborated by V3-EXQ-910 (`world_rule_shift_occurred` aligned 0/30, `failure_autopsy_V3-EXQ-910_2026-08-10.md:24,120`) | probe-only (5 + 1 seeds) | **decisive for W2b**: the only form that re-learned (s721 0.523) was oracle-timed and wholesale. W2b is "not buildable as specified" |
| R6 | world-shift timing and re-adaptation dose: `v3_exq_1062a_...postshift.py:784-790` (shift enabled "AT THE P2 BOUNDARY, after training"); `v3_exq_1001_...causal_shift.py:331-332` (`READAPT_EPOCHS = 8` on a 15% slice; head frozen `:687`+); `v3_exq_798a_...:505-507` (fixed shift interval, encoder frozen `:523-524`) | the harness knows when the world changed and chooses how much re-learning follows | 1062 autopsy: the shift ran from P0, so the "trained-then-shifted premise was never instantiated" (`failure_autopsy_V3-EXQ-1062_2026-09-22.md:100,155`) | T/R | D4, D5, D6 | none validated (R5) | ~39-55 drivers mention `world_rule_shift` / the action map | **high where used**: the 1062 -> 1062a fix was a harness toggle |
| R7 | SD-054 scaffolded onboarding stage plan (`scaffolded_sd054_onboarding.py:3636-3654`+): Stage-0 forced feed `:2216-2225`; Stage-0b `:2319`+; goal pipeline frozen `_set_goal_pipeline_frozen` `:1913`, set in P0 `:2485` and Stage-H `:2599`, unfrozen `:2270,:2735`; per-stage fresh optimizers `:253-254`; survival gates `:128,:403`; P2 frozen `:2862,:2894` | the whole developmental ordering: when goals may be written, when hazards appear, when the goal term reaches E3, when learning stops | "Infant REE must be fed before mature agency is judged" (`:3636`); the agent "dies before drive_level rises high enough" (design memo)+ | T/O | D10, D5, D9, D8 | drive, benefit exposure and z_goal norm are all native. Stage transitions are episode-budget driven, not read from them. Only the Stage-0 acceptance is metric-gated (`z_goal_formed`) | **~128-130** drivers; `scaffold_stage0_enabled=True` in 97; harm-pathway training in 83 | **very high**: C1 completion otherwise non_contributory; Stage-0 gate sat at its 0.667 floor in 603h/i/r/866b+; Stage-H: 6 inconclusive runs, 19.2 h+ |
| R8 | MECH-357 protective scaffold floor: config `:474-477`, annealed `:2635-2648` | a floor under the organism's own learned avoidance efficacy, annealed 0.8 -> 0 across Stage-H by episode fraction | "the protective scaffold leads acquisition" (`:2630-2634`) | O/T | D8, D1 | **the organism's own efficacy estimate exists**. The floor overrides it | 81 drivers (`scaffold_avoidance_driver_enabled=True`) | **high**: readiness gates read 1.0 "on the strength of the early scaffold-supported episodes", and the INTACT arm is functionally lesioned in the scoring window (`failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16.md:159-160,508-514`)+ |
| R9 | goal-pipeline gate anneals: `_set_p1_anneal_state` `:2034`, loop `:2780-2796`+ (`mech295_min_drive_to_fire` 1.0 -> 0.01, z_beta threshold 0.6 -> 0.3; `hazard_food_attraction` 0 -> 0.7); `drive_floor` anneal 0.9 -> 0.2 (V3-EXQ-622) | operating points lowered on a clock so a mechanism engages | "so the bridge ramps up gradually" (design memo)+ | T | D3, D10 | drive_trace and benefit exposure are native. ARC-155's own-scale denomination is absent | inside R7's 128-130 | **high**: the drive_floor anneal collapses z_goal by 1-6 orders of magnitude (`failure_autopsy_V3-EXQ-622_2026-06-01.md:72,122`)+ |
| R10 | InfantCurriculumScheduler: `infant_curriculum.py:53` (episode floors 0/100/500/2000), metric gates `:61-64`, one-way `:21`, env per phase `:163-226`, `config_overrides` `:228-264` (novelty 0.5/0.7/0.5/0.5, residue 0 -> 0.15, `offline_integration_frequency` 10/20/50/100) | phase advance, novelty weight, residue gain and SLEEP CADENCE per phase | phase schedule (infant substrate sec 6); Phase 3 injects SD-047/048 "to force continued forward-model adaptation" (`:201-206`) | T | D10, D2, D3, D5 | **partly endogenous**: H_pos, z_goal norm and residue coverage are computed from the agent's own state. But the harness applies them, only forward, behind hard episode floors. The h_pos gate was hand-recalibrated 0.70 -> 0.20 (`failure_autopsy_V3-EXQ-591b_2026-06-10.md`), and the robustified gates reject genuine explorers (591d)+ | 30-35 drivers | **moderate**: the novelty knob is dead (consumer deleted, 591h)+ |
| R11 | `committed_mode_curriculum.py`: P0 exit on rv < commit threshold `:10-22,:304-320`+; P2 eval `:485,:494`+; clone resets the beta gate "eval starts uncommitted" `:585-594`; forced-rv control `e3._running_variance = 0.001` (`:60-67` docstring; 6 drivers) | the harness sets E3's own confidence (running variance) to force commitment, and resets commitment at eval | "running_variance starts at 0.5 > commit_threshold (0.40) -> agent never commits" (`:12-15`) | O/T | D1, D7, D10 | **rv IS the native trust signal** (ARC-016). The harness overwrites it | 35-37 importers; 6 drivers pin rv | **high for the commitment cohort**: in 460b/461b/464b/466b closure never fired live; predecessors had "hand-poked" the APIs+ |
| R12 | MECH-457 bootstrap explorer: `_lib/mech457_bootstrap_explorer.py:30-40,80-86` (RND coefficient 1.0 -> 0.05 over 60% of training; entropy 0.10 -> 0.03; 20% full-explore warm-start `:102`+; encoder detached `:97-105`+) | explore -> exploit on a training-fraction clock | "a DEVELOPMENTAL schedule ... LC-NE explore/exploit consolidation instantiated as an ontogenetic schedule. Deliberately NOT the critic-utility ModeGate 755 refuted" | T/R | D2, D5 | **an endogenous candidate was tested and added nothing**: V3-EXQ-755's critic-utility mode gate gave no lift over a same-run fixed-coefficient arm; the residual was explorer capacity (`failure_autopsy_MECH-457-fanout-755_2026-07-15.md:77,122`) | 18 drivers | **high for MECH-457**, and a counter-case: on this task, regime selection was not the binding lever. Only behaviour cloning cleared the floor (747-749)+ |
| R13 | sleep entry by clock: `sleep/phase_manager.py:2,17-18,253` (K-episode, via `reset()` `:4126`); `agent.py:14030-14031` step modulo; per-phase `offline_integration_frequency` (R10); explicit modulo calls (e.g. `if (i+1) % CONSOLIDATE_EVERY`, V3-EXQ-1048 `:749`+) | the offline/waking regime switch is timed by the harness | the default convention; boundary-only by design (`sleep_substrate_plan.md:236`) | T | D10, D5 | MEL need arm and within-life trigger exist, default OFF (`config.py:7496,7513`), 3 drivers. MEL is noise-level in CausalGridWorldV2. The 933 need arm was a level detector, not Process S | `use_sleep_loop=True` 66; sleep/offline calls 59-129; 41 on a modulo | **moderate-high**: V3-EXQ-677 was non_contributory because sleep counts "derive from sleep_interval, not from any novelty/PE signal" (`failure_autopsy_V3-EXQ-677_2026-06-14.md`)+ |
| R14 | `force_cycle()` experimenter-triggered sleep (`developmental_life_definition_decision_2026-08-12.md:33`+; V3-EXQ-1081, 1026+) | sleep inserted at a chosen step | sanctioned so causal sleep tests need not wait for an endogenous trigger | T | D10 | as R13 | few | low (instrument) |
| R15 | PAG freeze gate ON with a hand-set theta and no exit: `config.py:7263-7267` (default off, theta 2.0, `pag_max_freeze_duration` 0 = never); 1107 theta 0.8 | defensive entry by a fixed absolute threshold; exit only by R1 (or a hand-set timer in 10 drivers) | calibration inherited from 935a; no stated exit rationale (1107 autopsy `:14`) | P/T | D8, D3 | **none that changes during the freeze** (ARC-156): 1106 had 0 drive-steps while frozen. `||z_harm_a||` is pinned next to a hazard | **124** drivers `use_pag_freeze_gate=True`; 10 set a max-duration timer | **very high recently**: 1090 (action 0 on 3000/3000), 1106 (100% frozen) and 1107 (freeze from tick 1) are all non_contributory; GFLAG-0508 |
| R16 | freeze held OFF "to de-confound" (`psychiatric_failure_modes_plan.md:151`+, `sd036_observable3_regime_matrix_design_staged_20260919.md:189`+); hazard-free / refuge phases (Stage-0, P0 reef spawn; D3_hazard_free rungs) | the experimenter prevents defensive entry, or removes the threats that would call for it | isolation of the variable under test; survival "structurally guaranteed" in the refuge+ | P | D8 | threat signals exist (CeA, z_harm_a), but are mis-scaled (ARC-155) | 2 drivers set `use_pag_freeze_gate=False`; ~91 match hazard-free patterns | moderate: an env "survivable without foraging" lets avoidance without approach lock in (V3-EXQ-769)+ |
| R17 | `external_task_drive` channel and gain: `config.py:4706-4716` (default off, weights 1.0); 1107 driver `:451-455` (3.0 / 2.0) | a mode-reversal input exists only when the experimenter adds it, at a hand-picked gain | "the lineage's own input"; reversals need an input independent of the dACC alarm (`mode_switch_cea_mechanism_trace_20260925.md` sec 1c-1d) | P | D10, D9 | **endogenous**: beta_elevated and goal proximity (`agent.py:9106-9133`). But dACC PE, the only live salience source, also argues for internal_planning (a shared-source coupling, Q-111) | 15 drivers | **high for the SD-032a / MECH-266 lineage**: every 934-lineage finding "is conditional on two default-off knobs"+; the drive was ~dead in trained eval (1067) |
| R18 | mode register pinned by wrapping the coordinator `tick`: `v3_exq_874b_...:360-380` (`coord._current_mode = mode` after the real tick), also 874 / 940 / 941 | the operating mode fixed per arm | MECH-467 arms; commitment excluded because "the substrate cannot sustain multi-step commitment yet" (874 `:60-66`) | P | D10 | the native coordinator (R17). It cannot hold these modes by itself | 5 drivers | moderate: a probe pinned from tick 0 did not transfer to the live loop (`failure_autopsy_V3-EXQ-874b_2026-08-17.md:108,144`)+ |
| R19 | absolute operating points set by hand: dACC affinity cap / switch threshold (15 drivers); CeA `low_freq > 0.5` (`cea.py:337`, modetrace sec 2a); coalition margin 0.05 (V3-EXQ-1038); PAG theta (R15); h_pos 0.70 -> 0.20 (R10) | when a regime fires is fixed on an absolute raw scale | calibration at build time | P | D3, D10 | ARC-155: an own-scale estimate is absent for these channels. ARC-016 and SD-099 are the only native precedents | 15+ drivers, and every default | **high**: 1067 (dacc_pe over the cap on 100% of ticks); CeA never fires or always fires; the coalition recruitment RATE is "scale-determined, not architectural" (1038 autopsy `:258`) |
| R20 | `alpha_world` pinned for the life: default 0.3 (`config.py:157`, "set to 0.9+ to fix event suppression"); drivers pin 0.9 | the z_world update weight (how much new observation versus persistence) is a per-life constant | SD-008 event-suppression fix | P | D3, D9 | none. There is no adaptive alpha | **796** drivers set 0.9; campaign probes use 0.3 | moderate: 0.9 raises the head's action read (`failure_autopsy_V3-EXQ-1079_2026-09-23.md`)+; the modetrace alpha 0.57 concern |
| R21 | selection temperature and the withhold fallback: `experiments/_harness.py:321` (`temperature=1.0`), `:322-327` (a random action when `select_action` returns None) | exploration temperature fixed. **The organism's decision to withhold action is overwritten with a random action** | keep the loop stepping | P/O | D2, D8 | E3 uncertainty and running variance exist. The withhold decision itself is the organism's | StepHarness in 119 drivers; 192 pass a literal temperature; 324 contain a withhold-fallback | unmeasured. Flagged: a withhold that is always converted to a random act can never express a native freeze or stop |
| R22 | epsilon override applied after `select_action` (V3-EXQ-1077 lineage) | forced exploration substituted after the organism chose | exploration coverage | O | D2, D4 | as R21 | ~32 drivers | the PE is mis-attributed on ~10% of ticks (`failure_autopsy_V3-EXQ-1077_2026-09-24.md:104`)+. An imposed action corrupts the action-failure vs model-error split |
| R23 | who decides WHEN learning happens: the harness calls `record_transition`, not the agent (`native_waking_trainer_design_20260925.md:34,63-66`+); StepHarness forces one `update_z_goal` + `update_residue` per step (`_harness.py:15-23`+); (branch) WakingTrainer steps every K ticks | the learning cadence is fixed or harness-driven | the phased trainers were driver-only; the WakingTrainer moves them into `ree_core` on a fixed K (campaign Q4a) | P | D5 | none: no native plasticity gain (N5 P1) | StepHarness 119; every trainer-member probe | moderate: this is the substrate on which any future D5 controller would act |
| R24 | which modules train in which phase: fresh Adam per stage (`scaffolded_sd054_onboarding.py:253-254`); harm pathway in P0/Stage-H only (`scaffold_train_harm_pathway`, 83 drivers); `E2_TRAIN_IN_P1 = False` (`_lib/allon_training.py:102`); lPFC/OFC REINFORCE in P1 only (`:794`+); `requires_grad False` in 106 drivers | per-module freeze / reopen by phase | e.g. "A0 recipe: SD-056 e2 encoder FROZEN through P1"+ | T | D5, D9 | none native | 83 + 106 + allon 22-37 | **high**: the decoupled encoder LR 3e-4 + warmup "worked" 3/3 vs 1/3 (`failure_autopsy_V3-EXQ-625e_2026-06-20.md`)+ |
| R25 | R5b action-class scaffold candidates (`use_action_class_scaffold_candidates`) | one-hot class candidates injected at E3 | the untrained decoder collapses CEM to one class; "a workaround" (`action_decoder_training_trace_20260924.md:63`)+ | P | D9, D2 | none (a decoder defect) | a small number | **high where used**: `trajectory_class_count >= 2` "only when" on (`behavioral_diversity_acceptance_criteria.md:242`)+; T2 is "not NATIVE" (A1 draft `:390`)+ |
| R26 | EMA reset-init knobs: ON in the campaign preset only (`coupled_loop_repair_campaign_plan.md:414`; GFLAG-0559); `use_zworld_ema_reset_init` default False (`config.py:175`) | the baseline an error / precision signal starts from after R1 | fixes R1's zero-init artefact | P | D1, D3 | n/a (a repair of R1) | campaign probes + A1 INT arms | high inside the campaign (W3 reliability 9/15 -> 13/15, plan W3 row) |
| R27 | SD-081 dual-system arbitration default OFF (`config.py:2500`; habit depth `:2530`); (branch) W4 aggregation gamma fixed 0.5 | habit vs planned read pinned to full-horizon for the whole life | default-off convention; the arbitrator is "the OUTPUT of that arbitrator rather than a property of having two pathways" (`config.py:2490-2496`) | P | D7 | **exists, default off**: relative-uncertainty arbitration (Daw, Niv & Dayan 2005). V3-EXQ-786a's flat recruitment is the "no-arbitrator signature" | 7 drivers mention `dualsystem_` | unknown: D7 has almost no imposition-vs-native contrast in the corpus |
| R28 | SD-091 endogenous coalition trigger default OFF (1 driver: V3-EXQ-1038) | the coalition controller recruited only by the experimenter (or not at all) | default-off convention | P | D10 | **exists**: a margin trigger that fires 7/7 at the shipped threshold, but on an absolute scale | 1 driver | the default composition "still does not recruit the controller" (1038 autopsy `:258`) |
| R29 | MECH-005 arousal driven exogenously (`mech005_successor_pilot_findings_20260922.md:59-69`) | arousal / clock rate set by manipulation | endogenous `||z_beta||` has ~0.9% dynamic range, so it "cannot be driven endogenously at all" | P/R | D3, D10 | **measured absent** (no dynamic range) | few | moderate: evidence must be recorded as an exogenous-equivalent manipulation |

## 3. Ranked summary: which missing decision is imposed most, and how load-bearing it is

This is a judgement ranking over sec 2. It combines prevalence (drivers and instance classes) with load-bearingness (whether results collapse or go non_contributory without the imposition). It is D0.

| rank | decision | rows | how often imposed | load-bearing | endogenous signal status |
|---|---|---|---|---|---|
| 1 | **D5 freeze vs reopen plasticity** | R2, R3, R4, R5, R6, R7, R23, R24, R13 | the default of nearly every driver (~376-470 train -> eval; 519 random-warmup; 106 `requires_grad False`; 83 staged harm training) plus the campaign's frozen retained set | very high: every reported number is a frozen snapshot, and the encoder-warmup omission is a named defect in ~40 autopsies | (a)/(b): no native plasticity gain exists (N5 P1); PE-based detection measured absent (N5, 910) |
| 2 | **D10 broad regime** (life boundary, curricula, sleep, mode) | R1, R7, R9, R10, R11, R13, R14, R17, R18, R28 | R1 alone is in 1156 drivers; curricula ~200 importers | very high: R1 is the hidden exit of absorbing regimes and the source of the reset artefacts | (b) mostly: MEL sleep arm, curriculum metric gates, coalition trigger and external_task_drive all exist, default-off or harness-applied |
| 3 | **D2 exploit vs explore** | R3, R4, R10, R12, R21, R22, R25 | 519 random-draw drivers; babbling in every campaign probe; the MECH-457 clock | high | mixed: own-action concentration is readable but unused (b); the 755 mode gate added nothing (a counter-case) |
| 4 | **D8 defensive entry/exit** | R1, R8, R15, R16, R21 | 124 freeze-gated drivers; 81 scaffold floors; the withhold -> random fallback in 324 | very high in the last week (1090 / 1106 / 1107 non_contributory) | (a) for the exit: nothing changes during a freeze (ARC-156). (c) for efficacy: the learned efficacy is overridden by the floor |
| 5 | **D3 precision / routing operating points** | R9, R19, R20, R26, R29 | 796 drivers pin `alpha_world`; every absolute threshold | high (ARC-155's four measured instances) | (a)/(b): own-scale estimates are absent except ARC-016 / SD-099; the arousal range is absent |
| 6 | **D9 which representations influence E3** | R7, R17, R20, R24, R25 | inside the curricula; R25 in the action-diversity lineage | moderate-high | mostly none native: the goal term's reach is set by stage |
| 7 | **D1 trust vs interrogate the model** | R8, R11, R26, R1 | 6 rv-forcing drivers, 81 floors | moderate, but conceptually sharp: rv is the only native model-confidence signal and the harness overwrites it | (c): the signal exists and is overridden |
| 8 | **D4 PE attribution** | R1, R5, R6, R22 | few explicit instances, but R1 supplies a free "env changed" flag everywhere | high where tested: this is the N5 wall | **(a) measured absent**: the clearest "none available" in the corpus (N5 5/5, 910 0/30) |
| 9 | **D6 quarantine and relearn** | R5, R6 | rarest: 1 exploratory seed plus the 1001 readapt slice | decisive for W2b | none: detection is absent (D4), and revision works only wholesale and oracle-timed |
| 10 | **D7 habit vs deliberative** | R27, R11 | almost never switched; pinned by default-off | unknown | (b): SD-081 exists, default off |

**Reading the ranking.**
- The decisions imposed most often (D5, D10, D2) are imposed mostly as **conventions**: phase schedules, episode boundaries, warmups. Their endogenous signals are mostly present-but-unrecruited (b) or overridden (c).
- The decisions whose endogenous signal is **measured absent** (D4, D6, and the exit half of D8) are imposed rarely, because experiments almost never create the situation. They are also where the hardest failures sit (N5; 1106 / 1107).
- So "most imposed" and "most missing" are different lists. DC-D should not read frequency as severity.

## 4. Cross-cutting findings for DC-D (step 4 onward); none decided here

**F1. The harness's life boundary acts as a hidden distributed controller.**
- R1 exits freezes, resets the mode register, restarts every integrator and baseline, gates sleep, and tells the organism that the world may have changed. It does all of this at a time the organism did not choose, and at a rate set by episode length.
- Any organism-level test that keeps R1 keeps this controller. The A1 draft runs its 3000-step closed loop across env episodes, so it keeps R1.
- In CausalGridWorldV2 the env also re-draws its layout every episode (A1 draft Q13, `causal_grid_world.py:1688-1712` at `f0331054133a`). The reset is therefore a **truthful** world-changed oracle: the organism never has to detect a layout change itself. This is the D4 decision in its most common form, and the harness answers it every episode.
- Two consequences follow:
  1. Absorbing regimes look recoverable in multi-episode drivers only because R1 terminates them. This is ARC-156's starvation shape with the terminator supplied from outside.
  2. A single continuous life (the Q-108 setting) removes that controller. It then exposes every absorbing regime and every zero-init artefact at once: sleep plan GAP-9 found sleep unreachable in a true single life.
- This is D0 plus the cited measurements. The single-life consequence is inferred for the regimes other than sleep, not measured.

**F2. Imposition hides the evidence the hypothesis needs.** Because the harness makes the call, the corpus contains almost no arm where the organism makes it.
- Endogenous sleep entry: 3 drivers.
- Endogenous coalition recruitment: 1.
- Native arbitration: ~0-7.
- An organism-read developmental stage transition: 0. The infant curriculum's metric gates are the closest, and they are harness-applied and one-way.
- Self-reopened plasticity: 0.

So the corpus can mostly say "the machinery works when the regime is supplied". It can rarely say "the organism cannot supply it". The exceptions, where a native trigger was actually tested, are N5 (failed), V3-EXQ-910 (failed), V3-EXQ-1106 (failed), V3-EXQ-933 (level detector) and V3-EXQ-755 (added nothing, because capacity bound first).

**F3. Where removing the imposition collapsed the result** (these impositions are load-bearing, not cosmetic):
- the SD-070 encoder warmup (R3)
- Stage-0 forced feed (the gate at its floor, R7)
- the scaffold floor (R8, the intact arm lesioned in the scoring window)
- the post-training shift toggle (R6)
- the action-class scaffold (R25)
- external_task_drive for reversals (R17)
- the wholesale oracle-timed re-babble (R5)

Each is a place where a missing endogenous decision is currently carried by the experimenter.

**F4. Ownership check (intake sec 6(ii)).** Against the intake's sec 2 owner table, every row maps to an owner **except two**. Both are surfaced for DC-D / `/governance`. Neither is registered:
- **(i) Life-boundary state policy.** Which controller states may a life/episode boundary legitimately reset, and which must persist and be exited endogenously?
  - Partial owners: SD-075 (one EMA's continuity), GFLAG-0559/0560 (EMA initial values), Q-108 (forbids a world-changed flag inside its recovery test), ARC-156 (regime-surviving exit input).
  - None owns the general question R1 raises: ~55 states wiped by an exogenous clock.
- **(ii) Who reads developmental stage transitions.**
  - ARC-019 (provisional) asserts "staged developmental training with explicit curriculum gates". ARC-074 requires a Phase-0 babbling epoch. ARC-075 requires plasticity asymmetry across phases. ARC-157 / Q-112 classify WHICH priors are general or necessary.
  - None asks whether the TRANSITION (end of babbling, stage advance, when retained developmental memory closes) must be triggered by the organism's own evidence. R4, R7 and R10 all answer it exogenously today.
  - ARC-019's wording is in mild tension with the dynamic-control hypothesis: if gates must be explicit and exogenous, the hypothesis is partly pre-empted for development.
- Minor, not claim-shaped: R21's conversion of a native withhold into a random action is a harness convention that can mask native freeze and stop behaviour. It belongs in a harness-hygiene note, not a claim.

**F5. The shape evidence from this corpus search.** This is input to step 4; DC-D decides.
- The sec 2 rows split three ways. Some decisions lack a working detector entirely (D4 / D6 / D8-exit: missing signal). Several have detectors or arbitrators that exist but are default-off or harness-pre-empted (D10 sleep and coalition, D7, D1: composition). Others fail because absolute operating points are mis-scaled (D3: ARC-155).
- That pattern fits "several distributed gaps plus a coordination / composition problem" better than "one missing mechanism". The one shared piece of infrastructure is R1, which currently does coordination work for all of them.
- **This is a corpus-level reading, D0, not a test.**

## 5. Candidate "remove-the-imposition" contrasts (for DC-D to weigh; NOT queued, NOT chipped)

Each contrast removes one imposition and asks whether a native signal takes over. All use signals the organism already has. None uses oracle knowledge of the condition.

1. **Controller persistence across R1.** Reset the body and environment but keep the controller states: `reset()` split into body-only and controller parts, harness-side where possible. Measure: absorbing-regime occupancy, freeze exits, mode reversals, and reset-artefact size. This is the direct test of F1.
2. **N5b as the record specifies.** Active-probe detector (periodic W2a babbling bouts scored action-contrastively) chosen by clamped-pair separation, plus wholesale revision (D4 / D6).
3. **Native sleep entry.** The MEL need arm versus the K-clock on an env where MEL is not noise-level (D10). SD-SLEEP-ENTRY-PRESSURE already owns the fix.
4. **Un-forced rv and no scaffold floor.** Does commitment or avoidance acquisition occur on the organism's own confidence and efficacy (D1 / D8)? The 603u cluster's lesion-in-scoring-window finding is the precedent.
5. **Babbling end read from own-action concentration.** Instead of a fixed 2400 steps (D2 / D5). The A1 draft already flags 2400 as ungrounded.

## 6. Method and uncertainty

- **Census script:** `.scratch/breakthrough-20260924/dcb/dcb_census.py`. It reads blobs at `origin/main` via `git show` (working-tree independent) over 1559 top-level `experiments/v3_*.py` drivers. Output: `census.json`, with 150-most-recent slices. Patterns are regexes and therefore approximate:
  - `random_action_warmup`: "warm" plus randint / choice / random-policy.
  - `train_then_eval_schedule`: optimizer or backward plus eval-episode names.
  - `alpha_world\s*=\s*0\.9`
  - `use_pag_freeze_gate\s*=\s*True`
  - `run_sleep_cycle(` etc.
  - Other counts in sec 2 are `git grep -l` at the same sha.
  - A sub-scan's heuristics (random draws excluding `action is None` fallbacks; warmup + `.eval()` + optimizer) gave the second figure where two are shown.
- **Recency.** In the 150 most recently touched drivers, the same patterns hold at lower absolute counts: random warmup 52, `alpha_world` 0.9 in 62, freeze gate in 11, external_task_drive in 9 of 15, world shift in 18. Recent work is shifting toward campaign probes, which sit outside `experiments/`.
- **What was not done.** Not every one of the 1559 drivers was read, and no driver was run. Load-bearingness is taken from the cited autopsies and records, not re-measured. Rows marked **+** rest on sub-scan citations (±2 lines) that were spot-checked in bulk: scaffolded `:3636`, `:2034`, `:2270` / `:2485` / `:2599` / `:2735` / `:2894`; allon `:102`; zworld P0 `:1-8`, `:36-42`; 1062a `:784-790`; 1001 `:331-332`; the 910 / 1038 / 755 / 1062 / 622 / MECH-457 747-749 / sleep plan quotes. They were not re-opened individually.
- **Uncertainty.**
  - The classification into decisions is interpretive, and several rows map to more than one decision.
  - "Load-bearing" means the cited record says the result depended on it. The records do not always test that with an arm.
  - The judgement that R1 is a regime imposition, rather than neutral episodic bookkeeping, rests on weights and residue persisting across it (`agent.py:4102`). A reader who treats each episode as a new life would classify it as environment design instead. The consequences in F1 hold either way.
