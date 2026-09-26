# Dynamic-control audit, steps 1-2: inventory of REE's coordination/control mechanisms and the causal map of what can change what within a lifetime

- **Written:** 2026-09-26T12:15Z. Session `bt0926-dca` (Worker DC-A, `orchestrate-20260924-breakthrough-c2`), chip_ref `chip-20260926-dynctl-a-inventory-causal-map`.
- **Scope:** audit steps 1 (inventory) and 2 (causal connectivity) of `docs/thoughts/2026-09-26_dynamic_control_coordination_hole.md` (d12f095ed2). Step 3 (imposed-regime corpus) is DC-B; step 5 (biology) is DC-C (`dynamic_control_audit_biology_20260926.md`); steps 4 and 6-9 are DC-D. **Read-only.** No ree_core edits, nothing queued, no registry edits, no chips, nothing run.
- **Builds on, does not re-register:** `thought_intake_2026-09-26_dynamic_control_coordination_hole.md` (a57efa78b7e) and the claims it points to: **ARC-155** (operating points must be denominated on the signal's own scale), **ARC-156** (strong regimes need an exit input that keeps changing during the regime), **ARC-157**, **Q-111** (do corrected controllers compose without an authority principle), **Q-112**, **MECH-597**. Dynamic control is treated as a hypothesis, not a design. No executive is proposed here.
- **Code under audit:** ree-v3 `origin/main` @ **`436a988742`** (MAIN) and `integration/coupled-loop-repair` @ **`4070b0efa4`** (BRANCH). Both are private detached worktrees. Every `file:line` is on MAIN unless marked `BR:`. The branch differs from main only in the default-OFF campaign members (W1 codec, W1-alt ASP, W3 E2WorldMember, W4 discounted aggregation, W6a WorldEncoderMember). None of them adds a controller: the rv/PE/surprise, threat and mode code is byte-identical on the branch.
- **Evidence domain:** **D0 (code read) throughout**, except where an edge cites a prior measured record (D1/D2). The edge lists carry the level per edge.
- **Method.** One config pass plus five parallel code-read sub-audits. Their full tables (about 240 rows, all with file:line) are committed as appendices, `probes/dca/G1..G5_*.md`:
  - **Config pass:** an `ast` parse of `config.py` dataclass defaults and the `from_dims` defaults. No import, no torch. Of 1262 fields, 240 are `use_*` / `*_enabled` switches and **only 16 default True**. `from_dims` agrees with the dataclasses on every bool.
  - **Five sub-audits:** G1 precision/E3/commit, G2 modes/cingulate/PFC/heartbeat, G3 threat/affect/residue, G4 neuromodulator/uncertainty/curiosity, G5 memory/plasticity/sleep/babbling.
  - **Verification:** I re-read the load-bearing rows myself (sec 1, sec 4) and settled one disagreement between sub-audits (sec 4, edge L6).

## 0. Headline

1. **At defaults, REE has exactly one endogenous regime variable that changes within a life: the E3 `committed` flag.** It is set by `rv < 0.40`, where rv is E3's running variance of its own world-prediction error (`e3_selector.py:4246-4250`; bar at `config.py:1308`).
   - Its only behavioural effect is the choice rule: argmin when committed (`e3_selector.py:4666`), softmax sampling at T = 1 otherwise (`:4688`). It also forces an extra E3 tick on commit entry.
   - It is an **ARC-155 case, and measured absorbing**: trained rv sits around 1e-6 to 1.6e-5, five orders below 0.40, and the committed step fraction is 1.0000 even at sweep amplitude 0.999 (`config.py:1291-1306`, GFLAG-0346).
   - It is also an **ARC-156 case (D0)**. Every variability lever REE has acts on softmax temperature, and the committed argmin branch ignores temperature. The levers are the noise floor, the entropy floor and the phasic burst.
   - Its input is endogenous, but it is **ticked only when the driver calls `update_residue`** (`agent.py:12213`, the only caller of `post_action_update`). A driver that skips the call leaves rv at 0.5, so the agent never commits.
2. **Everything else that moves within a life at defaults is either a fixed rule or driven by the harness:**
   - **Residue field.** The env harm scalar, passed in by the driver, writes the residue RBF ring. E3 and the CEM read the ring as a cost.
   - **Phase resets.** Harm and commit entry each force an off-schedule E3 tick.
   - **Action-hold length.** The E3 cadence sets how long an action is held, from `||z_beta||` through an absolute scale. This input spans 0.91% of its mean on a trained agent (D1), so the hold length is effectively a constant of about 9 steps.
3. **No operating-mode, threat, freeze, veto, neuromodulator, surprise, curiosity, sleep, plasticity-gating or babbling controller is live at defaults.**
   - **Threat:** the whole threat stack has **no input**. `harm_dim = 0` and both harm streams are off, so `z_harm` and `z_harm_a` are `None` on every tick (`latent/stack.py:1728-1749`).
   - **Learning and memory:** nothing endogenous changes any learning rate, write permission, retention policy, sleep entry or babbling state. No optimizer exists at defaults.
4. **Even when switched on, the regime machinery is disconnected. The worst cases:**
   - **The mode register has no behavioural consumer.**
     - The agent never passes `operating_mode` to the hippocampal proposer (`agent.py:7453-7462`).
     - Four of the MECH-261 write gates have no reader.
     - The mode sequence changed nothing observable in the one trace that checked it (D1).
   - **A frozen retained set cannot be unfrozen, by anything.** The E2WorldMember retained set (BR) has no unfreeze path at all.
   - **The babbling generator has no in-core caller.**
   - **Exactly one endogenous learning-rate modulator exists.** It is SD-PP-4, it acts during sleep only, and it is default-OFF.
5. **Named concepts with zero code on both trees (16 claim-level, plus 4 dead names in code):** ACh plasticity gain (MECH-398), ACh write gate (MECH-207), LC-NE tonic explore/exploit gain (MECH-433), stuckness annealing (MECH-527), learned PE routing (MECH-590), the MECH-104 volatility de-commit, reliability-weighted arbitration (MECH-312a / MECH-235), and learning-mechanism meta-selection (MECH-474), among others.
   - In every one of the user's ten named regime decisions, the variable that would carry the decision is either a harness constant or has no endogenous setter at defaults (sec 5c).

**Counts per status class** (consolidated inventory, sec 3; one row per mechanism after de-duplicating the sub-audits' about 240 rows):

| status class | rows | of which |
|---|---:|---|
| LIVE-AT-DEFAULTS | **13** | 8 rows (#1, 2, 56, 57, 99-102) make up 6 control edges with an endogenous signal: rv, the commit gate, the E3 cadence, phase reset, the residue write and the residue read. The other 5 rows (#7, 10, 36, 59, 103) are fixed rules or plumbing, not controllers. |
| DEFAULT-OFF-IMPLEMENTED | **106** | 16 are inert **even when switched ON**: zero default gain or weight, no agent-side producer, a dead parent flag, or an unreachable branch |
| TELEMETRY-ONLY | **16** | 8 are telemetry at defaults (computed, read by nothing); 8 are telemetry even when ON (one of them is the grad-reach guard, an abort-only instrument) |
| NAMED-CONCEPT | **20** | 16 are claim-level (sec 7: zero code on both trees); 4 are code-level dead names (unread gates, dead knobs, sec 3.9) |
| PROPOSED | **19** | campaign-plan rows and substrate_queue rows (sec 8) |
| **total** | **174** | Counted mechanically from the status column of sec 3 plus the rows of secs 7 and 8. Counts depend on row granularity; the sub-audits' ~240 finer rows show the same split. |

## 1. Premises re-measured (D0 against `436a988`)

| # | premise (source) | re-measured | verdict |
|---|---|---|---|
| P1 | No native ACh / MECH-398 / MECH-207 signal in ree_core (N5 P1, at `1b013d6`) | Literal-id grep over `ree_core/**/*.py` on both trees finds 0 files for MECH-398, MECH-207 and MECH-590. G4 also grepped `acetylchol`, `cholin` and `ach_`: every `ach_` hit is `approach_`. | **holds**, now on both current trees |
| P2 | "At REEConfig defaults the agent does no waking gradient learning" (census `940c690c9dd`, at `863d23d`) | `waking_trainer_enabled` is False (`config.py:8088`), so `WakingTrainer` is None (`agent.py:3709-3712`). Every `torch.optim` site sits behind a default-OFF master or a harness-called method (G5). | **holds** at `436a988` |
| P3 | Coordinator switching dynamics (modetrace `e2bbd2a98e`, at `23714f0`) | `tick` is unchanged at `salience_coordinator.py:533-719`. The episode reset has drifted from `agent.py:4119` to `:4180-4181`, and `use_external_task_drive` from `config.py:4614` to `:4706`. The code is the same. | **holds**. Line numbers corrected. |
| P4 | "The coordinator ticks every env step" (implicit in the modetrace's per-tick counts) | `select_action` returns early between E3 ticks (`agent.py:8623-8661`), before dACC (`:8862`), pACC (`:8745`), the coordinator (`:9041-9143`) and closure (`:11736`). | **corrected.** The coordinator, dACC, pACC, closure, the stuck detector and tonic vigor all tick per **E3 tick** (every 5-20 env steps). Only AIC and the broadcast override tick per env step. |
| P5 | The CeA gate and its 0.4 < 1.0 salience ceiling (ceacal / ceacal2) | `cea.py:308-337`, `agent.py:2573-2577` and `salience_coordinator.py:311` are unchanged. | **holds.** Additionally, at defaults CeA is **not constructed** (`use_amygdala_analog = False`, `config.py:7115`). Even with it on, CeA has no input unless SD-011 is also on. |
| P6 | "E3 rv is the E2 world head's realised one-step error" (GFLAG-0486; plan W3 note) | StepHarness order is sense (`_harness.py:218`), select, `env.step` (`:354`), then `update_residue` (`:361`). `update_residue` passes `self._current_latent.z_world` (`agent.py:12211`), which at that point is the **pre-step** latent z_t. The reference is `world_states[1]` of the trajectory selected at the **last E3 tick** (`e3_selector.py:4942-4945`). | **corrected (D0; needs a D1 check).** On an E3 tick, rv's input is `\|\|z_t - E2(z_t, a_t)\|\|^2`, i.e. E2's *predicted displacement*, not a realised error. One tick later it is a genuine one-step error. After that it is drift against a stale prediction. G1 and G4 reached this independently. |
| P7 | The SD-008 reset-init knobs (GFLAG-0559/0560) are default OFF | All four `use_*_ema_reset_init` are False (`config.py:175-196`). rv is **never reset per episode** (E3 has no `reset()`). | **holds.** New consequence: the zero-init transient feeds rv, and rv carries it across episodes into the next commit decision (G4). |
| P8 | `use_mech307` / `use_consumer_conjunction_read` "default True in from_dims" (my own first grep, config lines 8194-8196) | Those lines belong to the `enable_goal_stream()` preset. In both the dataclass and `from_dims` they are False (G4). | **corrected** (my misread; no record carried it) |

## 2. How to read the inventory

- **Status classes** follow the brief. Two sub-flags are added:
  - **inert-when-ON**: the mechanism is implemented and gated off, but switching its flag ON still changes nothing. Causes are a default gain of 0, no agent-side producer, a dead parent flag, or an unreachable branch.
  - **tel@def vs tel-always**: telemetry at defaults only, or telemetry even when switched on.
- **E/H:** **E** means the input is endogenous (computed by the agent from its own observations, latents or errors). **H** means the harness supplies it: a driver call, a config constant, or a schedule. "E (H-ticked)" means an endogenous quantity that only updates when the driver makes a specific call.
- **Timescale:** "tick" is an env step. "E3" is an E3 tick (every 5-20 steps). "ep-R" means the state resets every episode; "ep-P" means it persists across episodes.
- Citations are MAIN `file:line`. The sub-audit appendices carry the full citation sets.

## 3. Consolidated inventory

### 3.1 Precision, gain and commitment

| # | mechanism (ids) | status | reads | can change (consumer) | timescale | E/H | cite |
|---|---|---|---|---|---|---|---|
| 1 | E3 running variance rv (ARC-016) | **LIVE** | `\|\|z_world_pre - E2 traj.world_states[1]\|\|^2` (P6) | rv, the commit gate's input | EMA 0.05, init 0.5, ep-P | E (H-ticked via `update_residue`) | e3:1046-1116, 4920-4951; ag:12205-12216 |
| 2 | E3 commit gate `committed = rv < 0.40` (ARC-016, MECH-090 entry) | **LIVE** | rv vs a constant bar | argmin vs softmax sampling (e3:4666 / 4688); beta elevate/release; phase reset on entry (ag:11430); second residue write on harm (e3:4955-4959) | per E3 tick | E signal, H bar | e3:4141-4250; config:1308 |
| 3 | current_precision = 1/rv | TEL (tel@def) | rv | nothing at defaults; every consumer is flag-gated | tick | E | e3:868-871 |
| 4 | Volatility estimate var(rv) (Q-007; "LC-NE tonic"; MECH-104 lit basis) | TEL (tel@def) | 100-sample var(rv) | z_beta input only if `volatility_signal_dim > 0` (default 0) | 100 ticks, ep-P | E | e3:525-527, 1118-1125; ag:6004-6006 |
| 5 | `last_instantaneous_pe` | TEL (tel@def) | raw per-update PE | SD-069 only when its source is `"instantaneous_pe"` (default is rv) | tick | E | e3:1036-1052; ag:10367 |
| 6 | BetaGate latch (MECH-090) | TEL (tel@def; see sec 4 L6) | `committed` | `_beta_elevated`. At defaults every behaviour-changing reader is flag-gated. The held action equals the selected action on the commit tick. Between-tick stepping is dead because `post_action_update` tears `_committed_trajectory` down every step. | E3, ep-R | E | bg:22-260; ag:11355-11447, 8623-8661; e3:5199 |
| 7 | SD-008 z_world / z_self EMAs (alpha 0.3) and `alpha_shared = 0.3` (a literal) | **LIVE** (fixed rule) | raw encode vs prev latent | smoothed latents, read everywhere | EMA 0.3; prev zeroed each episode | H constant; no within-life setter (MECH-157 is off) | stack:1545-1551, 1626, 1711, 1722 |
| 8 | SD-008 reset-init knobs x4 | OFF | reset tick | skip the EMA on t = 0 | per episode | H | config:175-196; stack:1554-1590 |
| 9 | MECH-157 mode precision routing | OFF | coordinator `operating_mode` (or a harness override) | alpha_eff for z_world; E2 anchor pull | tick | E if the coordinator is on | config:303; stack:1631-1665; ag:6030-6072 |
| 10 | Latent per-channel precision gains `sigmoid(logit)` | **LIVE** (fixed rule; gradient-only) | none (a parameter) | scales latents and PE weights | never within life | - | stack:1021-1029, 1079-1092 |
| 11 | MECH-108 breath sweep | OFF | fixed cycle | commit bar x(1 - amp) | fixed period | H | clk:78-109; e3:4173 |
| 12 | SD-011 urgency-scaled commit bar | OFF, inert-when-ON (`urgency_weight` 0.0; `z_harm_a` None) | `\|\|z_harm_a\|\|` | commit bar | E3 | E | e3:4191-4198 |
| 13 | SD-093 progress-velocity bar modulation | OFF | goal velocity | commit bar | E3 | E | e3:4218-4224 |
| 14 | ARC-029(D) variance-tracking commit bar (the ARC-155 remedy for #2) | OFF | quantile of the run's own gate variance | replaces the absolute bar | window W, ep-P | E | e3:873-1024, 4165-4172 |
| 15 | SD-063 conditional precision gate | OFF, inert-when-ON (the agent never passes `conditional_predictive_variance`) | E2 predictive variance | commit variance | E3 | would be E | e3:4240-4250 |
| 16 | Harm-score-variance commit mode | OFF, inert-when-ON (the kwarg is never passed) | cross-candidate harm variance | committed | E3 | E | e3:4230-4237 |
| 17 | SD-076 waking confidence inflation | OFF | error_var (asymmetric EMA) or OU noise | rv | EMA/OU, ep-P | E / H (OU) | e3:1054-1112 |
| 18 | MECH-204 REM recalibration (A) / broadcast (B) | OFF; B is inert-when-ON (gain 0.0) | serotonin zero-point | rv | per sleep bout / tick | E target, H gain | e3:1300-1364; ag:7952-7958 |
| 19 | MECH-027 precision-scaled / MECH-439 gap-scaled commit temperature | OFF | precision margin / F gap | committed-branch softmax | E3 | E | e3:4612-4664 |
| 20 | E3 channel commensurability | OFF | per-channel EMA of cross-candidate SD | per-channel score divisor | EMA 0.05, ep-P | E | e3:1724-1790, 1850-1862 |
| 21 | DR-12 PE-confidence weighting; self-viability weighting | OFF, inert-when-ON (the signals only arrive via harness `set_injected_*`) | injected PE / viability | score penalty | E3 | **H** | ag:4680-4705, 10869-10880 |
| 22 | MECH-090 R-c readiness margin gate; readiness conjunction | OFF | score margin; env-privileged limb-damage outcome | beta admission | E3 | E / **H** (env ground truth) | ag:11136-11150, 11220-11226; bg:180-240 |
| 23 | MECH-342 maintenance release | OFF | margin + nav competence deficit | beta release | leaky 0.2/0.1 | E / H | ag:8058-8111 |
| 24 | Natural-commit urgency release; SD-033e frontopolar de-commit | OFF; frontopolar is inert-when-ON (gain 0.0) | commit run length x entry gap; counterfactual value | beta release | tick | E | ag:8125-8168 |
| 25 | Natural-commit latch hold; ARC-108 rho ramp | OFF | committed | re-asserts beta each tick | tick | E | ag:8565-8622 |
| 26 | Bistable beta plus MECH-105 completion release | OFF | hippocampal completion signal >= 0.75 | beta release | E3 | E, constant bar | ag:7489-7512; bg:282-300 |
| 27 | SD-084 / ARC-071 persistent program handle, reselection short-circuit, chunk execution | OFF | beta + chunk tag | skips E3 re-deliberation | tick | E | ag:8631-8720 |
| 28 | Closure commit entry and closure-to-beta coupling | OFF | closure latch | beta, independent of rv | E3 | E | ag:11171-11235 |

### 3.2 Selection variability and exploration

| # | mechanism (ids) | status | reads | can change (consumer) | timescale | E/H | cite |
|---|---|---|---|---|---|---|---|
| 29 | MECH-440 noisy selection head (+ self-anneal) | OFF, inert-when-ON (`sigma_init` 0.0) | normalised top-2 gap | per-candidate score noise | EMA 0.01 | E | e3:845-866, 4033-4056 |
| 30 | MECH-441 model-disagreement curiosity | OFF, inert-when-ON (weight 0.0) | ensemble disagreement | score bias | E3 | E read, H-trained | ag:10881-10910 |
| 31 | MECH-341 E3 score diversity (2 sub-flags default True) | OFF (master False) | first-action classes | entropy bonus; stratified select replaces argmin | E3 | E | e3:3671, 4606-4610; config:5843-5845 |
| 32 | SD-105 selection entropy floor | OFF | EMA of precommit entropy | temperature (argmin ignores it) | integrator, ep-P | E | ag:10290-10312 |
| 33 | MECH-313 noise floor | OFF | none | temperature | tick | H | ag:10282-10288 |
| 34 | SD-069 phasic surprise burst ("LC-NE phasic") | OFF | rv, or instantaneous PE | temperature delta (argmin ignores it) | refractory | E | ag:10362-10376 |
| 35 | SD-061 stuck-state detector + difficulty-gated proposal entropy | OFF | progress stall, margin, dACC difficulty, committed diversity | candidate count, CEM temperature | asymmetric EMA, ep-R | E, absolute floors | ag:1800-1880, 8345-8398 |
| 36 | Support-preserving CEM (SP-CEM) | **LIVE** (fixed rule) | first-action class counts of elites | elite class floor, ao_std floor | per CEM iteration | H constants | hip:1475-1600, 2458-2494 |
| 37 | MECH-267 `mode_partitioned_cem` (default True) | OFF, inert-when-ON (dead parent: needs mode conditioning plus a supplied mode) | mode scale | ao_std | per CEM iteration | - | config:3325-3353; hip:2469-2507 |
| 38 | MECH-314 structured curiosity (3 sub-flags default True) | OFF; 314b/c at their default "broadcast" source are argmin-inert offsets | residue/visitation novelty; rv; PE change | score bias | E3, ep-R | E | ag:1909-1914, 9800 |
| 39 | SD-025 curiosity + familiarity (sub-flag default True) | OFF (`curiosity_weight` 0.0) | visit-count EMA | CEM novelty term | EMA 0.01, ep-P | E | hip:187-198, 1889-1911 |
| 40 | SD-102 / MECH-482 epistemic deficit | OFF | uncertainty x realised error | 314c learning progress | EMA, ep-R | E | ag:1955-1985 |
| 41 | MECH-111 novelty EMA | TEL (tel@def; H-fed: no ree_core caller; score consumer deleted) | E1 PE (driver-fed) | only the SD-081 fallback | EMA | **H** | e3:141, 1413, 1813 |
| 42 | Visitation counter | TEL (tel@def) | waking z_world region | read only under `use_completion_promotion_gate` | tick, ep-P | E | ag:6845-6862 |
| 43 | MECH-320 tonic vigor (DA vigour analogue) | OFF | reward EWMA, drive, rv <= 1.0 | act-vs-noop bias | half-life 100, ep-R | E | ag:2070-2098, 9857-9920 |
| 44 | W2a StructuredBabbler | TEL (tel-always: constructed, **no in-core caller**) | own RNG | nothing in ree_core; the harness executes `next_action()` | per call | **H** decides when | structured_babbling.py:24-28; ag:3719-3722 |
| 45 | W1-alt action-space proposals (BR) | OFF (fixed rule, no controller) | none | proposal pool | E3 | H | BR: hip (ASP block) |
| 46 | W1 codec: bounded decode, iteration-0 image match (BR) | OFF (fixed rule) | codec | proposal decode | E3 | H | BR: hip; BR: waking_trainer_codec.py |

### 3.3 E3 arbitration and basal-ganglia-like selection

| # | mechanism (ids) | status | reads | can change (consumer) | timescale | E/H | cite |
|---|---|---|---|---|---|---|---|
| 47 | SD-081 dual-system habit vs planned arbitration | OFF. When ON it runs on rv only: its habit-uncertainty fallback `_novelty_ema` is never updated in ree_core, so it is a constant 0. | u_planned = rv; u_habit = 1 - familiarity, or `_novelty_ema` | blend weight; habit depth | EMA 0.05, ep-P | E (half-dead) | e3:1999-2180; ag:10934-10952 |
| 48 | W4 discounted aggregation (BR) | OFF (fixed gamma 0.5, no controller) | - | planned-score aggregation | - | H | BR e3:1827-1845 |
| 49 | ARC-108 learned channel gating plus MECH-451 finer (signed RPE delta_t) | OFF | delta_t = (benefit - harm head) - V-hat | w_chan, w_chan_finer | three-factor, ep-P | E | e3:3748, 5003-5040 |
| 50 | Modulatory selection authority / routing / shortlist-then-modulate | OFF | bias range vs score range | rescaled bias; shortlist winner | E3 | H constants | e3:3602-3810, 4356-4590 |
| 51 | MECH-448 F-eligibility demotion (+ adaptive floor) | OFF | F-merit share | eligible set | E3 | H / E (adaptive) | e3:2181, 4351 |
| 52 | MECH-449 Go/No-Go plus endogenous running-z safety No-Go | OFF (triple-gated) | harm_eval over predicted states, z-scored per agent | No-Go on the eligible set | EMA 0.999, ep-P | E (**the ARC-155-compliant form**) | e3:4353-4449; ag:4724-4744, 10843-10866 |
| 53 | BG loop family: segregation, D1/D2, loop traces, M_cross, spiral gain, parity (ARC-109/110, MECH-452) | OFF | per-loop preferences; da = tanh(V-hat); delta_t | cross-loop winner | E3, plastic | E / H | e3:2752-3260, 4468 |
| 54 | MECH-450 learned settling W_lat; soft competitive settling | OFF, inert-when-ON (W_lat init 0; gain 0.0) | delta_t | within-set reorder | rounds | E / H | e3:2532-2618, 4492-4520 |
| 55 | ARC-108 JOB-2(d) habenula negative-RPE de-commit | OFF (two flags, synced only by `from_dims`, plus the closure operator) | delta_t < 0 | beta release, committed handles cleared | post-action | E | ag:12257-12296; e3:4992 |

### 3.4 Clock, heartbeat and timing

| # | mechanism (ids) | status | reads | can change (consumer) | timescale | E/H | cite |
|---|---|---|---|---|---|---|---|
| 56 | MECH-093 E3 cadence from `\|\|z_beta\|\|` (SD-006) | **LIVE** | `\|\|z_beta\|\|` x 1.0, clamped to [0,1] | `_current_e3_steps` in [5,20]. This sets when E3 re-selects; between E3 ticks the last action is **repeated** (ag:8623-8661) and candidates are cached (ag:7533-7537). | tick; reset to 10 each episode | E, but absolute scale (ARC-155); z_beta comes from the random depth stack (census #13) | ag:7261; clk:200-217 |
| 57 | MECH-091 phase reset (salient-event E3 resync) | **LIVE** | env harm (driver-delivered); commit entry | forces an E3 tick at the next advance; clears quiescence | event | E content, H delivery | ag:11430, 12379; clk:147-155, 182-191 |
| 58 | MECH-092 quiescent replay | TEL (tel-always: output discarded; `replay()` writes no state) | quiescent E3 tick | **nothing.** The only side effect is global `torch.randn` draws (e2_fast.py:864) on the RNG stream the act path's multinomial also uses. | E3 | E | ag:12059-12060, 12121-12183; hip:2985-3057 |
| 59 | Theta-buffer summary (MECH-089) | **LIVE** (plumbing) | last 10 z_world | `z_world_for_e3` | 10-step cycle | E | ag:452-464, 7360 |
| 60 | MECH-294 multi-content theta packet | TEL (tel-always; `last_theta_packet` has no reader) | goal/risk/state | - | E3 | E | ag:473, 4155, 7486 |
| 61 | MECH-057a action-loop completion gate | OFF, inert-when-ON (unreachable branch: a preceding branch returns first) | caller flag | cached candidates | - | H | ag:7533-7545 |

### 3.5 Operating modes, cingulate, PFC and closure

| # | mechanism (ids) | status | reads | can change (consumer) | timescale | E/H | cite |
|---|---|---|---|---|---|---|---|
| 62 | SalienceCoordinator register (SD-032a, MECH-259, MECH-048) | OFF | dACC pe/foraging/difficulty, AIC, PCC, drive, CeA, override, external_task_drive, closure_event | `current_mode`, `operating_mode`, write gates | E3, **ep-R** (restarts in external_task) | E inputs, H constants (switch 1.0, bias 1.0) | sc:266-741; ag:726-769, 9036-9155 |
| 63 | MECH-266 Schmitt hysteresis | OFF, inert-when-ON (dicts empty; no endogenous writer) | operating_mode[current] | exit gating | E3 | H | sc:361-362, 506-531 |
| 64 | Affinity input cap / squash (`mode-governance-engagement`) | OFF | raw affinity inputs | logit bounding | E3 | H | sc:388-416, 593-616 |
| 65 | MECH-261 write-gate registry | OFF (readers: autonomic, e3_policy, sd_033a, sd_033b) | operating_mode | gate in [0,1] per target | per call | E | sc:207-263 |
| 66 | MECH-267 hippocampal mode conditioning | OFF, inert-when-ON (**the agent never passes `operating_mode` to `propose_trajectories`**; only experiment scripts do) | operating_mode | CEM std, horizon, mode value | per proposal | would be E | ag:7453-7462; hip:2001-2190 |
| 67 | SD-032b dACC (+ MECH-268 saturation) | OFF; its E3 adapter is inert-when-ON (weights 0.0) | `\|\|z_harm_a - pred\|\|`, falling back to `\|\|z_harm_a\|\|`; needs SD-011 | coordinator salience + internal_planning affinity; stuck detector | E3, EMA 0.05, ep-R | E, cap/scale H | dacc:144-373; ag:8862-9023 |
| 68 | SD-032c AIC analogue | OFF | `\|\|z_harm_a\|\|` / drive / beta / mode | aic_salience; harm_s_gain | tick, own-EMA **ratio** (scale-relative), ep-R | E | aic:176-270; ag:6416-6468 |
| 69 | SD-032d PCC analogue | OFF | task-success EMA (**driver-fed** `note_task_outcome`), drive, offline recency | switch threshold multiplier; mode temperature | E3, ep-R | **H** / E | pcc; ag:14064-14074 |
| 70 | SD-032e pACC drive sensitisation | OFF | `\|\|z_harm_a\|\|` gated by write_gate("autonomic") | effective drive for ~8 controllers | EMA 0.002, **ep-P** (one of the few cross-episode controllers) | E | pacc:180-311; ag:8745-8766 |
| 71 | external_task_drive (`mode-governance-engagement`) | OFF | beta elevated + goal proximity, with goal active required | external_task affinity + salience | E3 | E (identically 0 with z_goal off) | config:4706-4716; ag:9095-9133 |
| 72 | SD-091 claustrum coalition + MECH-481 endogenous trigger | OFF (exit is **timer-only**: `tick()` gets no agent_state) | E3 score margin (absolute 0.05 by default) | channel gains on 8 consumer sites | 50-tick timer, ep-R | E / H | ag:774-877, 9156-9235 |
| 73 | SD-033a lateral PFC rule_state (SD-082 bias) | OFF; the bias head is zero-init, so inert until harness-trained | pooled z_world | rule_state; score bias | E3, ep-R | E | lpfc:302-350; ag:9328-9510 |
| 74 | ARC-063 candidate rule field | OFF | action/outcome recurrence | LPFC rule slots | E3, ep-R | E | ag:1036-1134 |
| 75 | SD-033b OFC (state code, devaluation head) | OFF; bias inert until trained | z_world (+ z_harm) | state code; score bias | E3, ep-R | E | ofc:125-360; ag:9512-9594 |
| 76 | ARC-062 gated policy | OFF | z_world / z_self / z_harm_a | score bias | E3 | E (driver-trained) | ag:9241-9325 |
| 77 | MECH-319 simulation-mode rule gate | OFF, inert-when-ON (every agent call passes `simulation_mode=False`) | caller flag | LPFC update admission | per call | H | ag:2394-2412 |
| 78 | SD-034 closure operator | OFF | stable rule_state (delta < 0.001 absolute), beta, mode, gate | beta release, dACC No-Go, residue discharge, closure_event (**latched +0.5 internal_planning for the rest of the episode**) | E3, ep-R | E, absolute bar | co:330-760 |
| 79 | MECH-321 policy decomposition mid-execution probe | OFF | segment boundary while committed | release / re-plan | tick | E | ag:8224-8330 |
| 80 | SD-037 broadcast override ("orexin") | OFF | drive + `\|\|z_harm\|\|` window | override_signal: coordinator affinity 0.3, z_goal seeding, LPFC eta, PAG | tick, ep-R | E, absolute 0.5 | ag:2798-2826, 6379-6415 |
| 81 | SD-012 goal / drive (z_goal, drive_level) | OFF (`z_goal_enabled` False; drive_level reads 0.0 everywhere at defaults) | drive_level **passed in by the driver** to `update_z_goal` | drive into ~8 controllers; z_goal | per driver call | **H**-plumbed | goal.py:88; ag:13196-13360, 8766-8768 |

### 3.6 Threat, defence and veto (the whole family has no input at defaults: `z_harm` and `z_harm_a` are None)

| # | mechanism (ids) | status | reads | can change (consumer) | timescale | E/H | cite |
|---|---|---|---|---|---|---|---|
| 82 | Harm latents: MECH-099 z_harm, SD-010 z_harm_s, SD-011 z_harm_a | OFF (`harm_dim=0`, both streams off) | hazard/resource fields; `harm_obs_a` is an env-side EMA | inputs to every row below | tick | E obs; weights H-trained only (untrained in every recipe: census, modetrace) | config:150, 336, 347; stack:1205-1226, 1728-1749 |
| 83 | SD-019a harm_un; SD-036 GABAergic decay + recurrence | OFF (`gaba_tone` is harness-set: `set_gaba_tone` has no in-tree caller) | z_harm_s; per-stream norms | redirected urgency; decays z_harm, z_harm_a, **z_beta** | EMA | E / **H** tone | ag:6317-6340, 2589-2626; stack:1751-1796 |
| 84 | MECH-258 E2_harm_a forward | OFF | z_harm_a, a | prediction used by the BLA remap PE and dACC | tick | H-trained | ag:516-542, 11652 |
| 85 | SD-020 harm-surprise PE (training target); SD-021 descending modulation | OFF | harm vs EMA x precision/500; beta / AIC gain | aux-loss target; z_harm attenuation | EMA | E; loss H-called | config:4411-4424; ag:6570-6615 |
| 86 | SD-035 BLA (encoding gain, retrieval bias, remap, attribution head) | OFF (master `use_amygdala_analog` False; sub-switches True are inert) | `\|\|z_harm_a\|\|` (inverted-U 0.4/0.7); remap PE vs own sigma | memory_strength; replay retrieval bias; ContextMemory remap | ep-R (remap baseline never matures) | E | bla; ag:2498-2549, 6480-6546 |
| 87 | MECH-046 CeA fast route | OFF (double-gated: amygdala + coordinator) | `\|\|z_harm_a\|\|_1/dim > 0.5` (absolute) | coordinator affinity external_task 1.0, salience 0.5 (ceiling 0.4 < 1.0) | E3 | E | cea:308-337; ag:2573-2577, 9071-9087 |
| 88 | MECH-279 PAG freeze gate | OFF | `\|\|z_harm_a\|\|_2` x duration > 2.0; exit z < theta x factors (no max duration) | **post-selection substitution of STAY** for the chosen action | tick, ep-R | E, absolute theta | ag:11464-11552; pag/freeze_gate.py |
| 89 | MECH-287 option-B descending release | OFF (also needs anchor sets / per-region V_s) | anchor invalidations (T3 broadcast, hysteresis resets) | PAG exit threshold x(1 + alpha r) | trace 0.95, ep-R | E | ag:6946-6958; freeze_gate:491-497 |
| 90 | SD-099 / MECH-489 defensive orienting | OFF; its surprise channel is identically 0 unless MECH-205 is also on | onset over own EMA of residue surprise or `\|\|z_harm_s\|\|` | STAY arrest; approach/withdraw bias | E3, ep-R | E (scale-relative) | ag:10451, 11554-11580, 12352-12362 |
| 91 | MECH-091 urgency interrupt (no flag of its own) | OFF (input None) | `\|\|z_harm_a\|\|` > 0.8 while elevated | beta release | tick | E, absolute 0.8 | ag:7994-8040 |
| 92 | MECH-357 / SD-058 instrumental avoidance | OFF | z_harm_a drop after a directed action | per-action bias; PAG suppression above 0.5 | EMA 0.05, ep-P | E | ag:2230-2245, 9983, 11511-11526 |
| 93 | MECH-282 LPB interoceptive routing | OFF | raw harm_obs hazard slice + drive | HarmEncoder mask; PAG input; SD-037 input | tick | E | ag:2849-2858, 6080-6098 |
| 94 | MECH-302 relief comparator; MECH-304 conditioned safety store; MECH-303 safety terrain | OFF | z_harm_a drop >= 0.10; cosine to safety prototype; harm-absent < 0.05 | beta release; liking writes; safety terrain | windows / EMA; the MECH-304 prototype is **ep-R** | E, absolute bars | ag:6972-7040, 8469-8545 |
| 95 | Escape-affordance family: bridge, trainable relief/safety learner (default True under a False master), E2 linker | OFF | z_harm_a drop per action class; trained heads | per-action approach bias | online, ep-P | E | ag:2258-2325, 6166-6290, 10069-10172 |
| 96 | MECH-353 blocked agency | OFF | outcome mismatch (absolute 0.1 floor by default) | E3 assert bias; de-commit after 5 ticks | leaky, ep-R | E | ag:2110-2143, 8409-8420 |
| 97 | SD-011 `lambda_eff` harm-cost amplification | OFF, inert-when-ON (`affective_harm_scale` 0; z_harm_a None) | `\|\|z_harm_a\|\|` | ethical cost weight | E3 | E | e3:1851-1856 |
| 98 | MECH-219 harm-suffering accumulator | OFF; telemetry when ON unless one of 5 redirect flags is set | z_harm_un; escapability (**constant 1.0 = H**) | z_harm_suffering | asymmetric EMA | E / **H** | ag:6433-6438, 8025-8029, 11474-11482 |

### 3.7 Residue, valence and neuromodulator-named analogues

| # | mechanism (ids) | status | reads | can change (consumer) | timescale | E/H | cite |
|---|---|---|---|---|---|---|---|
| 99 | MECH-018 / SD-005 residue RBF harm field (write) | **LIVE** | env `harm_signal < 0` (driver's `update_residue`) at the current z_world | 32-slot ring: centres/weights; FIFO overwrite; no decay | per harm event, **ep-P**, lifetime | trigger H-delivered env scalar; location E | ag:12363-12379; field:165-180, 736-784 |
| 100 | Commit-gated second residue write | **LIVE** | harm while committed | a second ring write, magnitude 1.0; **bypasses `owned` / `hypothesis_tag`** | per harm event | E x H | e3:4955-4959; ag:12213-12216 |
| 101 | Residue read into E3 score (Phi_R, rho 0.5) | **LIVE** | residue over candidate z_world | trajectory cost | E3 | E state, H weight | e3:1555-1563, 1836-1889 |
| 102 | Residue read into hippocampal terrain prior and CEM elite ranking (MECH-131) | **LIVE** | residue field | CEM initial mean; elite argsort | per proposal / iteration | E | hip:591-617, 1785-1800, 1878-1886 |
| 103 | Residue neural_field (untrained Softplus MLP) | **LIVE** (static; never changes within life) | z_world | a fixed random +0.1 x MLP offset on every residue read | never | - | field:466-473, 707-735 |
| 104 | Residue `integrate()`; SD-024 DA-modulated RBF density; benefit terrain | OFF | stored harm locations; benefit x drive | neural_field params; benefit RBF allocation | sleep / contact | E / H | ag:14005-14031, 13277-13294; field:182-254 |
| 105 | Valence vector (SD-014; `valence_enabled` True) | OFF in effect: **no writer is live at defaults**, so readers see zeros | - | hippocampal valence reads | - | - | hip:1160, 1814, 3089; writers ag:6617, 8481, 12330, 13595-13770 |
| 106 | MECH-205 surprise-gated replay / valence write; MECH-307 split/signed surprise | OFF | E3 PE - `_pe_ema` (zero-init each episode: GFLAG-0559 shape) | VALENCE_SURPRISE writes; replay weight; orienting input | EMA 0.02, ep-R | E, absolute 1e-5 | ag:12134-12139, 12298-12353 |
| 107 | ARC-030 benefit eval; MECH-295 liking bridge | OFF | resource/goal proximity; drive x proximity | E3 benefit; approach bias | tick | E / H drive | e3:1891-1905; ag:9654-9690 |
| 108 | MECH-203/204 serotonin module | OFF (constructed at ag:513; every method no-ops; `tonic_5ht` fixed at 0.5; waking dynamics also need driver calls) | benefit / harm exposure | seeding gain, wanting floor, replay drive, REM zero-point | per call, zero-point ep-P | E / **H** calls | serotonin.py:38-240; ag:513, 5945-5965 |
| 109 | MECH-457 actor-critic TD advantage | OFF | critic TD | policy head | driver-stepped | **H** | ag:420 |

### 3.8 Memory gating, plasticity, sleep/waking and babbling

| # | mechanism (ids) | status | reads | can change (consumer) | timescale | E/H | cite |
|---|---|---|---|---|---|---|---|
| 110 | WakingTrainer + HarmEval / E1 / E2-self members (C1, T1) | OFF | native losses over own buffers | member params; **fixed Adam lr** | every K ticks (**K mutated at runtime by the harness** in EXQ-1108), ep-P buffers | **H** (enable, K, lr, membership) | wt:145-432; ag:3709-3712, 12386-12402 |
| 111 | E2WorldMember with FROZEN retained set (W3, BR) | OFF; **no unfreeze path and no eviction**; source switched only by harness calls | re-encoded raw obs + action | e2 world head | every K x updates_per_step; lr 3e-4 fixed; retained set ep-P | **H** (`set_e2_world_source`, `append_external`, `schedule_external`: callers only in EXQ-1108 and tests) | BR: wt:344-358, 502-542, 771-780 |
| 112 | WorldEncoderMember (W6a, BR); CodecMember (W1, BR) | OFF | SD-070 P0a objective on the live sense path; codec objective | encoder / codec params, fixed lr | every K | H | BR: waking_trainer_world_encoder.py; BR: waking_trainer_codec.py |
| 113 | C0 grad-reach guard | TEL (instrument that aborts on FAIL, never a controller) | which params got gradient | raises `WakingTrainerReachError` | first 8 steps | H | wt:349-360, 416-432 |
| 114 | Other online learners: BLA attribution head, trainable escape heads, SD-063 uncertainty head online | OFF | their objectives | their heads, fixed lr | tick | H | ag:2519-2549, 586-612, 6226-6245 |
| 115 | MECH-333 critical-period closure: EWC anchor + gated_policy `crystallize()` | OFF; **harness-triggered even when armed** (called only from an experiment's phase-3 callback) | weight magnitude x mask | `requires_grad=False`; an EWC penalty for the driver's loss | once | **H** | gated_policy:349-412; field:638-705 |
| 116 | SD-PP-4 provenance-conditioned consolidation gain | OFF (needs SD-PP-1/2/3 + sleep world-forward consolidation) | replay provenance (evidence precision, PE, surprise) vs current pi_epi | **per-step lr of the sleep e2_world consolidation** (the ONLY endogenous lr modulator in ree_core) | per sleep step | E | cross_module_consolidation.py:215-246 |
| 117 | SD-PP-1 observation reliability; SD-PP-2 world-forward epistemic precision; SD-PP-3 provenance recorder | OFF | frame-difference variance; E2 PE EMA; reads at record time | consumed only by #116 | EMA | E | ag:3104-3170 |
| 118 | MECH-273 offline lr scale; MECH-423 cross-module consolidation | OFF | - | offline lr = waking x 0.1; module params | per sleep cycle | H | ag:3063-3080, 3266-3305 |
| 119 | SD-017 SleepLoopManager (every K episodes) | OFF | episode count | runs a sleep cycle | K = 1 episode | **H** schedule | pm:253-276; ag:3178, 4124-4125 |
| 120 | GAP-9 within-life sleep trigger (ceiling arm) | OFF | waking step count | sleep cycle | every 1000 steps | **H** | ag:12236-12253; pm:325-411 |
| 121 | SD-MEL consumer duration factor; MEL need arm; SD-SLEEP-ENTRY-PRESSURE | OFF. At sub-knob defaults the need and pressure arms are **degenerate**: threshold 0.0, so they fire on any PE, or every 2 steps. | mean waking E3 PE since the last cycle | SWS/REM step counts; sleep entry | per cycle / step, ep-P | E, absolute thresholds | mel:174-369; pm:268-358 |
| 122 | MECH-286 sleep-onset permit gate | OFF; **never permits** if the staleness accumulator is off | override signal, max staleness, `\|\|z_harm_a\|\|` | permit / block a sleep cycle | per attempt | E, absolute 0.3/0.4 | sleep_onset_gate.py:25-113; pm:446-455 |
| 123 | SD-017 SWS/SHY and REM passes; `e1._offline_mode` write gate | OFF (entered only by the sleep loop or the harness) | theta buffer / anchors; precision at REM entry | E1 schema slots; rv; E1 context-memory write permission | per sleep phase | H entry | ag:14033-14360 |
| 124 | Sleep-aggregation cluster: MECH-285 sampler, MECH-272 routing, MECH-275 aggregator, MECH-273 self-model | OFF | staleness-weighted anchors; routed evidence | anchor beliefs; self-model params | per sleep cycle | mixed | ag:3178-3305 |
| 125 | MECH-165 replay diversity; MECH-290 backward credit sweep; offline wanting spread | OFF | episode trajectories + BLA bias; completion release | exploration buffer; VALENCE_WANTING | per episode / release | E / H | ag:4582-4610; hip:3667, 3781 |
| 126 | Hippocampal invalidation/retention stack: MECH-288 event segmenter, MECH-287 invalidation trigger, MECH-269/284 anchor sets + hysteresis, per-stream / per-region V_s, VS rollout gate, VS commit release | OFF; **the whole stack resets every episode** | PE z-scores; BOCPD on z_goal; boundary events; V_s | segments, anchor inactive, broadcast, snapshot substitution, beta release | tick, **ep-R** | E, absolute V_s bars 0.3/0.4 | ag:4516-4544, 6730-6940 |
| 127 | MECH-284 staleness accumulator (shared source for 4 roles) | OFF | broadcasts vs active anchors | region staleness, read by anchor hysteresis, MECH-285 sampler, MECH-286 permit, VS gate | leak 0.995, ep-R | E | staleness_accumulator.py:86-196 |
| 128 | MECH-292/293 ghost goal bank; SD-097 possibility topology | OFF | inactive-anchor payloads; remap relations | ghost-seeded CEM candidates | per proposal | E | hip propose path; ghost_goal_bank.py:454 |
| 129 | MECH-468 relational dumps (A/C/D) | TEL (tel-always; **zero production callers**) | pairwise / co-membership | - | - | - | anchor_set.py:579-583; ghost_goal_bank.py:416-425 |
| 130 | Experience / transition / harm-replay FIFO buffers | TEL (tel@def; read only by harness-called losses or OFF members) | waking latents | trimmed to 1000 | tick | H capacity | ag:7059-7060, 12421-12422 |
| 131 | MECH-324 chunk maintenance / dissolution / reacquisition | OFF | real-execution count; outcome-variance hysteresis | chunk state, selection weight | per chunk execution | E | policy_chunking.py:1505-1568 |

### 3.9 Telemetry-only and dead names (not listed above)

| # | item | status | note / cite |
|---|---|---|---|
| 132 | MECH-039 two-part veto readout | TEL (tel-always) | "NO effect on scoring, selection or any producer" (config:5940-5963; ag:4773-5100) |
| 133 | MECH-095 TPJ agency comparator | TEL (tel-always) | `_tpj_last_agency_signal` has no reader (ag:4630-4663); `owned` for residue is left to the driver |
| 134 | E2_harm_s forward through the agent; OFC outcome-oracle predictions | TEL (tel-always) | the agent never passes `harm_forward_model` to E3; oracle "no effect on E3 scores" (ag:9571-9594) |
| 135 | `SelectionResult.precision`; `_harm_this_episode` | TEL (tel@def) | no reader |
| 136 | MECH-261 gates `hc_viability`, `sensory_buffer`, `sd_033c`, `sd_033d` | NAMED-CONCEPT (code-level) | registered, 0 readers (sc:207-263) |
| 137 | SD-091 control-demand types (8 of 10) | NAMED-CONCEPT (code-level) | enum only; no template (claustrum/control_demand.py:1-60) |
| 138 | CeA `pre_softmax_additive` (default True) | NAMED-CONCEPT (dead knob) | never read (cea.py:174; ag:2559 passthrough only) |
| 139 | CeA `cortical_confirmation` / `escapability_hint` / `cue_features` | NAMED-CONCEPT (in-agent) | the agent always passes None (ag:6564-6572) |

The 16 claim-level NAMED-CONCEPT rows (#140-155: MECH-398, MECH-207, MECH-433, MECH-527, MECH-474, MECH-590, MECH-312a, MECH-235, MECH-596, MECH-280, ARC-037, MECH-585, MECH-104 (de-commit route), MECH-510/511, MECH-206, Q-041) are in sec 7. The 19 PROPOSED rows are in sec 8. (MECH-497, INV-022 and ARC-155/156/Q-111 are listed in sec 7 for completeness but are principles or failure modes, not mechanisms, and are not counted.)

**Count check.** Taken from the status column of rows 1-139:
- LIVE: 13 (#1, 2, 7, 10, 36, 56, 57, 59, 99-103).
- DEFAULT-OFF: 106, of which 16 are marked inert-when-ON.
- TEL: 16.
- Code-level NAMED-CONCEPT: 4 (#136-139).

Secs 7 and 8 add 16 claim-level NAMED-CONCEPT rows and 19 PROPOSED rows.

## 4. Causal map: edges LIVE within a lifetime at defaults

This is the default agent, driven through the canonical StepHarness (one `sense`, one `select_action`, `env.step`, one `update_residue` per step). Evidence levels: D0 is code read, D1 means measured to exist or move, D2 means an intervention changed a native consumer.

| # | edge (signal -> controlled variable) | consumer file:line | E/H | evidence |
|---|---|---|---|---|
| L1 | E2 rollout prediction `world_states[1]` vs pre-step z_world -> **rv** (EMA 0.05, not reset per episode) | e3:4942-4947 -> 1113-1116; tick source ag:12213 | E, **H-ticked** | D0. The input's composition is the P6 correction (D0; D1 check owed). |
| L2 | **rv -> committed** (`rv < 0.40`, absolute) | e3:4246-4250 | E vs H bar | D0 + **D1**: trained rv 1e-6 to 1.6e-5, committed fraction 1.0000 even at sweep 0.999 (`config.py:1291-1306`, GFLAG-0346): **absorbing** |
| L3 | **committed -> choice rule** (argmin vs softmax sampling at driver T = 1.0) | e3:4666 / 4688 | E | D0 |
| L4 | committed entry -> `clock.phase_reset` -> forced E3 tick next step | ag:11430 -> clk:147-155 | E | D0 |
| L5 | committed + harm -> second residue write (bypasses `owned` / `hypothesis_tag`) | e3:4955-4959 | E x H | D0 |
| L6 | committed -> BetaGate elevate/release. **No action effect at defaults.** | ag:11355-11447 | E | D0, **verified by me**. G2 read this as an action hold; G1 read it as inert. G1 is right. On commit `_committed_step_idx = 0` (ag:11367), so the propagated action is `traj.actions[0]`, the selected action. Between E3 ticks `_committed_trajectory` is None because `post_action_update` clears it every step (e3:5199), so the else-branch repeats `_last_action` (ag:8623-8645), which happens whether or not beta is elevated. |
| L7 | **`\|\|z_beta\|\|` -> E3 cadence** (5-20 steps), which sets **how long each action is repeated** and when candidates are regenerated | ag:7261 -> clk:200-217 -> clk advance; hold ag:8623-8645; cache ag:7533-7537 | E; absolute scale 1.0 | D0 + **D1**: on a trained agent, `\|\|z_beta\|\|` spans 0.701772-0.708161 (0.91% of its mean), so e3_steps is effectively a constant of about 9 (`substrate_queue` row `mech005-endogenous-arousal-dynamic-range`, measured 2026-09-22). z_beta comes from a depth stack that is random in 4/5 recipes (census #13). **A live edge with no dynamic range.** |
| L8 | **env harm -> residue ring write** at the current z_world (FIFO over 32 slots, no decay, lifetime) | ag:12363-12379; field:165-180 | trigger = driver-delivered env scalar; location E | D0 + **D1**: the only parameter that moves at defaults (census `940c690c9dd`) |
| L9 | env harm -> `clock.phase_reset` -> forced E3 tick; quiescence suppressed | ag:12379 -> clk:149-155 | H-delivered | D0 |
| L10 | **residue field -> E3 trajectory cost** (rho 0.5 x Phi_R) -> choice | e3:1836-1889 | E | D0; **consumer reach D2-negative** at world_dim 32: consumer response indistinguishable from a shuffled control (`residue_consumer_reach_world_dim32_20260924.md`, 82819a1058, with the GFLAG-0441 fix). The kernel bandwidth is about 8x the reachable z_world manifold, so the read is near-broadcast (measured harm/safe ratio 1.0067; field:426-440 comment). |
| L11 | residue field -> hippocampal terrain prior + CEM elite ranking | hip:591-617, 1785-1800 | E | D0 (same reach caveat) |
| L12 | first-action-class support -> SP-CEM elite floors (fixed rule) | hip:1475-1600 | H rule | D0 |
| L13 | quiescent E3 tick -> MECH-092 replay -> **global RNG draws only** (a hidden coupling: replay timing shifts the stream the act path's multinomial reads) | ag:12121-12183; e2_fast:864 | E | D0 |
| L14 | observation -> z_world -> E3 selection (the content path, not a control edge; listed because every control edge above rides on it) | ag:5224 ff.; e3 | E | **D2** at E1 and E3 selection (`zself_causal_reach_trace_20260924.md`, 884a6b1ca3) |

**The live control graph in words:** at defaults there is a single loop. E2's world prediction error goes into rv, rv sets committed, and committed switches the choice between argmin and sampling. Commit entry also triggers an extra E3 tick. rv is not reset per episode, so the commit regime carries over between episodes. Alongside it:
- **Clock:** the E3 re-selection cadence (and so the action-repeat length) is set from `||z_beta||` through an absolute scale. Measured, this is flat.
- **Residue:** the driver-supplied harm scalar writes a lifetime RBF cost field. E3 and the CEM read it, and the reach test did not distinguish it from a shuffled field. The harm scalar also forces phase resets.

No signal changes a mode, a threat state, a learning rate, a memory write or retention policy, sleep, or babbling.

## 5. Causal map: edges that exist only when switched ON (DEFAULT-OFF), with the evidence that exists

### 5a. Edges

| # | edge | shape flags | evidence (record) |
|---|---|---|---|
| O1 | dACC pe/foraging -> coordinator salience **and** internal_planning affinity | shared source (**Q-111 / ARC-156**) | **D2**: one switch per life, then locked; reversals 0/0/0 (modetrace A1) |
| O2 | external_task_drive -> external_task affinity + salience | the independent input | **D2**: within-life reversals 0/0/0 -> 2/16/25 (modetrace A4) |
| O3 | coordinator operating_mode -> LPFC/OFC write rates, pACC write rate, closure admissibility, MECH-157 alpha, AIC harm_s_gain, dACC bias scaling | most need a second flag; the dACC adapter weights are 0 | D0. **The mode sequence reached no behaviour** in the one trace that checked it (episode and tick counts identical across register sequences, modetrace sec 1c: D1-negative). Registered as `mech019-operating-mode-enabled-consumer`. |
| O4 | coordinator -> hippocampal proposer (MECH-267) | **edge absent**: the agent never passes operating_mode | D0 (ag:7453-7462) |
| O5 | `\|\|z_harm_a\|\|` -> CeA fire -> coordinator (+0.4 salience maximum) | ARC-155 (absolute 0.5 on an unanchored latent); structural ceiling | **D1**: never fires untrained, always fires after harm_accum; **D2**: forced fire every tick gives 0/0/0 switches (modetrace A3; ceacal; ceacal2) |
| O6 | `\|\|z_harm_a\|\|` x duration -> PAG freeze -> STAY substitution | ARC-155 + **ARC-156** (exit needs z_harm_a to fall while STAY holds the agent at the hazard; no max duration) | measured: V3-EXQ-1107 (freeze from tick 1; post-training `\|\|z_harm_a\|\|` 2.8-4.2 vs theta 0.8), cited by ARC-155 |
| O7 | anchor invalidations -> PAG descending release | **ARC-156** (evidence starvation) | measured: V3-EXQ-1106, 0 drive-steps while frozen, 3/3 |
| O8 | MECH-449 running-z safety -> No-Go on the eligible set | the only ARC-155-compliant threat gate; **masked by O6** (freeze substitutes after selection) | measured: V3-EXQ-1090, veto fires 3/3 but the executed action is 0 on 3000/3000 ticks (Q-111) |
| O9 | `\|\|z_harm_a\|\|` -> MECH-091 urgency release; AIC; IA; escape bridge; MECH-302 relief (and MECH-304 learning) | **one scalar drives 7 controllers** that fire together, unarbitrated | D0 (G3) |
| O10 | rv / precommit entropy / constant -> phasic burst, entropy floor, noise floor -> **temperature** | **disconnected in the committed regime** (argmin ignores T) | D0 (G1) |
| O11 | ARC-029 quantile bar -> commit bar (the ARC-155 remedy for L2) | scale-relative | D0; `MECH465-COMMIT-GATE-HEADROOM` reached the band by recalibration (V3-EXQ-1015) |
| O12 | signed RPE delta_t -> w_chan, w_chan_finer, W_lat, M_cross, habenula de-commit | one teaching signal, five roles | D0 |
| O13 | rv (+ a constant 0 novelty EMA) -> SD-081 habit/planned blend | half-dead: the habit-uncertainty source is never updated | D0 |
| O14 | E3 score margin -> coalition trigger -> 8 channel gains | absolute 0.05; **timer-only exit** | D0 |
| O15 | stuck score -> proposal breadth (SD-061) | absolute floors; no ecology exercises it (`sd061-resume-progress-ecology`) | D0 |
| O16 | waking E3 PE -> MEL sleep duration / MEL entry / entry pressure; staleness -> MECH-286 permit | thresholds of 0.0 are degenerate; the permit never fires with staleness off | D0 (G5) |
| O17 | replay provenance -> SD-PP-4 -> sleep consolidation lr | **the only endogenous lr modulator**; sleep only | D0 |
| O18 | member losses -> WakingTrainer params (fixed lr; harness K) | no endogenous gain on any member | D0; members gated D1 (W3 record f82cb986c5; W6a record) |
| O19 | (none) -> E2WorldMember retained set FROZEN / UNFROZEN | **no endogenous edge exists**; W2b was not built because N5 found no detector | N5 (`b26d8e8d9d`): detection D1-negative 5/5; wholesale revision worked on 1 seed |
| O20 | (none) -> babbling on/off | **no endogenous edge**; StructuredBabbler has no in-core caller | D0 (G5) |
| O21 | pACC `\|\|z_harm_a\|\|` -> drive_bias (cross-episode) -> ~8 controllers | gated by write_gate("autonomic"), so it adapts 3x slower outside external_task | D0 |
| O22 | AIC (own-EMA ratio) -> coordinator salience | scale-relative (ARC-155-compliant) | D0 |

### 5b. Dead ends

**Controllers whose input exists but whose output nobody reads:**
- **At defaults:**
  - The BetaGate latch (L6).
  - MECH-092 replay (L13). It is output-discarded, with an RNG side effect.
  - current_precision, the volatility estimate ("LC-NE tonic", Q-007), `last_instantaneous_pe`.
  - The visitation counter and the experience buffers.
  - The serotonin module: constructed, `tonic_5ht` fixed at 0.5.
  - The residue neural field: a static random offset.
- **Even when switched on:**
  - The MECH-039 veto readout, the TPJ agency comparator, the OFC oracle and E2_harm_s through the agent.
  - The MECH-294 theta packet and the MECH-468 relational dumps.
  - The StructuredBabbler.
  - Four MECH-261 write gates.
  - The mode register as far as the hippocampal proposer is concerned (O4).
  - The coordinator register generally: no behavioural reach was measured (O3).
- **Inert even when ON by default parameters:**
  - Zero gain or weight: MECH-440 sigma, MECH-441 weight, MECH-204B gain, frontopolar gain, soft settling gain, SD-011 urgency weight, `affective_harm_scale`, the dACC adapter weights.
  - No agent-side producer or unreachable: SD-063 (the agent never supplies the variance), the harm-variance commit mode, the simulation-mode gate, the action-loop gate.
  - SD-081's never-updated novelty EMA.
  - MECH-266 has no endogenous writer.

**Variables that matter but nothing endogenous sets (at defaults, and in most cases also when switched on):**
- **Commitment and choice:** the commit bar (0.40); E3 softmax temperature (a driver kwarg, 1.0); every E3 score weight.
- **Representation smoothing:** alpha_world, alpha_self and alpha_shared (0.3; alpha_shared is not even configurable).
- **Timing:** the E3 cadence has an endogenous input but no dynamic range (L7).
- **Learning:** every waking learning rate, the trainer cadence K (mutated by the harness at runtime) and member membership.
- **Memory and development:** the retained-set freeze state; babbling on/off and epoch length; critical-period closure timing (a harness phase-3 callback).
- **Sleep:** entry at defaults (no sleep occurs at all); the sleep K schedule and the step ceiling.
- **Goals and outcomes:** drive_level (driver-supplied); PCC task success (driver-supplied).
- **Threat parameters:** `gaba_tone` (a harness pharmacology knob) and MECH-219 escapability (constant 1.0).
- **Mode governance:** the coordinator switch threshold and weights; coalition duration (a timer).
- **Residue:** ring capacity (32) and FIFO eviction.

### 5c. The user's ten regime decisions, mapped onto the causal map

Each row names the variable that would carry the decision and says what sets it now.

| regime decision (thought doc) | variable that would carry it | what sets it now |
|---|---|---|
| trust vs interrogate the world model | commit state; learning gate on E2 | rv vs a constant bar, which is absorbing once trained (L2). No interrogation state exists. |
| exploit vs explore | argmin vs sampling; temperature; proposal breadth | argmin vs sampling follows L2/L3. T is a driver constant. Every T lever is OFF, and disconnected when committed (O10). |
| alter precision or routing | alpha_world; MECH-157 routing; channel precision | constants (0.3); MECH-157 is OFF and needs the OFF coordinator |
| classify PE (noise / action failure / model error / change) | MECH-590 route; ARC-037 attribution | NAMED-CONCEPT only |
| freeze vs reopen plasticity | member lr; `requires_grad` | fixed lr (H); crystallize() is a harness callback; the only endogenous lr gain is sleep-only and OFF (O17) |
| quarantine obsolete experience and relearn | retained-set freeze; eviction | no endogenous path on either tree (O19). N5 showed that the revision works when imposed. |
| habitual vs deliberative | SD-081 blend; MECH-596 route | OFF; half-dead fallback (O13); MECH-596 NAMED-CONCEPT |
| enter or leave defensive/freeze | PAG / orienting / MECH-091 state | OFF and **inputless at defaults**; ARC-155/156 when on (O6, O7, O9) |
| which representations influence E3 | channel gating (ARC-108); write gates (MECH-261) | OFF (O12, O3) |
| broad operating regime | coordinator register | OFF; one-way switch without an independent input (O1/O2); no behavioural reach (O3); resets every episode |

**Cross-episode carry.** At defaults only rv and the residue field persist across episodes. With everything switched on:
- **Persist:** pACC drive_bias, instrumental-avoidance efficacy, the trainable escape heads, the MECH-449 running scale, the ARC-108 weights, the commensurability EMAs, and the sleep / MEL / trainer buffers.
- **Reset every episode:** every mode, threat and hippocampal-invalidation controller, i.e. the coordinator, dACC, AIC, PCC, the coalition, LPFC/OFC, closure, CeA, BLA, PAG, orienting, the MECH-302/304 gates, blocked agency, the event segmenter, anchors, staleness and invalidation.

So no within-life regime controller can carry a learned regime across an episode boundary. The one that does carry state, rv, carries an absorbing one.

## 6. What the map says about ARC-155 / ARC-156 / Q-111 (evidence for DC-D; not a recommendation)

- **ARC-155 (absolute operating points on learned quantities).**
  - **At defaults:** the ARC-155 instances are the commit bar (L2, measured absorbing) and the MECH-093 clamp (L7, measured flat).
  - **When switched on:**
    - Threat: CeA 0.5, PAG theta, MECH-091 0.8, BLA 0.4/0.7, MECH-302/303 bars.
    - Modes and arbitration: coordinator switch 1.0 on unbounded dacc_pe, closure 0.001, coalition 0.05, stuck floors 0.05.
    - Memory and sleep: V_s bars 0.3/0.4, MECH-286 bars, MEL thresholds 0.0.
  - **Already scale-relative:** the AIC ratio, dACC foraging, the MECH-449 running z, orienting onset-over-baseline, the event-segmenter z-scores, the adaptive F floor, and the ARC-029 quantile bar.
  - **Pattern:** the corrected forms are already written, and every one is default-OFF.
- **ARC-156 (exit starved by the regime).**
  - Committed argmin vs the temperature levers (L2/O10, D0).
  - PAG freeze (O6/O7, measured).
  - The coordinator's internal_planning lock (O1, measured).
  - The coalition's timer-only exit.
  - The retained-set FROZEN state, which has no exit at all (O19).
  - DISSOLVED chunks (terminal with retention off).
- **Q-111 (composition).**
  - Freeze masks the veto (O8, measured).
  - One `||z_harm_a||` scalar drives seven threat controllers unarbitrated (O9).
  - One rv drives the commit gate plus five optional consumers.
  - One delta_t drives five learning roles.
  - One staleness scalar drives four hippocampal/sleep roles.
  - Shared-source coupling is the dominant pattern wherever more than one controller is switched on.
- **Shape of the hole, stated as a D0 observation only (the decision belongs to DC-D):**
  - At defaults REE is **not** a set of working controllers that fail to coordinate. It has one live regime variable, and that variable is absorbing.
  - Most of the coordination machinery is default-OFF.
  - When switched on, it is largely inputless (threat), consumer-less (modes), or harness-gated (plasticity, memory, babbling, sleep).
  - The distributed, scale-relative pieces the user's framing prefers already exist as code, but only as default-OFF alternatives.

## 7. NAMED-CONCEPT rows (claim-level; no code computes it)

Method: I grepped every id below as a literal string over `ree_core/**/*.py` on MAIN `436a988` and got 0 files. The sub-audits then checked each family semantically for unnamed implementations. Status and phase come from `REE_assembly/docs/claims/claims.yaml` at `2e1f6a60e4`.

| claim | status / phase | what it would control | nearest existing code (and why it is not this) |
|---|---|---|---|
| MECH-398 ACh-analog plasticity-gain gate | candidate / v4 | a state-conditional gain in [0,1] on encoder learning rates and residue write magnitude | None. N5 implemented `g` harness-side (`n5_ach_gated_unfreeze_probe_20260926.md` P1). No member lr is modulated by any agent signal (#110-112). |
| MECH-207 ACh write-gate on the surprise buffer | candidate / v4 | whether a PE-tagged episode is written for updating | None. MECH-205 (#106, default OFF) weights replay start points and valence writes by PE minus its EMA. It is not a coincidence write gate. |
| MECH-433 LC-NE tonic explore/exploit gain | candidate / v4 | value-independent broad gain on exploration | SD-069 (#34) is the phasic half only, and it acts on T. The "volatility estimate" (#4) is telemetry. |
| MECH-527 stuckness-triggered attractor-escape annealing | candidate / v3 | organism-level annealing when stuck | SD-061 (#35) widens CEM proposals only. No ecology exercises it. |
| MECH-474 learning-mechanism meta-selection | candidate / v3 | which learning mechanism the control plane runs | None. Trainer members are chosen by config (#110). |
| MECH-590 learned PE routing R = P(route \| PE, context, history) | candidate / v4 | whether an error recruits orient, defend, repair or hold | None. Its loci (CeA, SD-069, SD-099, MECH-104) are fixed-sign arithmetic. |
| MECH-104 volatility-interrupt de-commit | provisional / v3 | an unexpected-harm volatility spike -> de-commit | Only lit-basis comments (G4: 11 hits, all comments). #4 is telemetry. |
| MECH-312a / MECH-235 reliability-weighted MB/MF arbitration | candidate | habit vs deliberative by reliability | SD-081 (#47) exists, but its weight is rv plus a dead fallback, not a reliability estimate. |
| MECH-596 dual-route proposal generation | candidate / v3 | habit (ASP) vs deliberative (codec) proposer | Both proposers exist default-OFF on BR (#45, #46). The arbitration (campaign W1-both) is not started. |
| MECH-280 LH-PAG override of freeze | candidate / v3 | orexin-type release of freeze | None. MECH-287 (#89) is the implemented cousin. |
| ARC-037 / MECH-585 PE attribution routing (self / world / noise) | candidate / v3 | classifying an error | None as a controller. TPJ (#133) is telemetry. |
| MECH-510 / MECH-511 PE-precision axis; learning-eligibility gate for deep revision | candidate / v4 | when a mismatch earns durable revision | None |
| MECH-206 CA1 PE comparator writing the surprise buffer | candidate / v3 | surprise-buffer write | None |
| Q-041 unified threshold supervisor vs scattered adaptive loci | open / v3 | cross-substrate threshold adaptation | None by design. Of the "scattered loci" it lists, only ARC-016 is live, and ARC-016 is L2. |
| (not counted) MECH-497 evidence corruption; INV-022 heterogeneous precision; ARC-155 / ARC-156 / Q-111 | candidate | principles or failure modes | At defaults there is effectively **one** live precision scalar (rv), against INV-022. Sec 6 maps the principles. |

## 8. PROPOSED rows (plan / substrate_queue; nothing built)

| row | source | would control | status (as of this read) |
|---|---|---|---|
| W2b ACh-gated unfreeze (MECH-398 g on member lr; MECH-207 coincidence unfreezes the retained set) | `coupled_loop_repair_campaign_plan.md` sec 2/3 | member lr; retained-set FROZEN flag | **blocked**: N5 CANNOT_DETERMINE. No detector was found (0/5 separation). Revision works only wholesale (1 seed). |
| N5b (active-probing detector + wholesale quarantine / re-babble) | N5 record sec 5 | same as W2b | proposed probe |
| W6 integrated trainer preset | campaign plan | which members run (a config preset, i.e. harness-set) | blocked on W1 / W2b / W4 / W5b |
| W1-both (habit/deliberative proposer arbitration + route-of-origin tag) | campaign plan, MECH-596 | proposer route per state | not started |
| W5b grounded-valuation member | campaign plan | E3 primary channel weights from grounded outcome | blocked on W5a / C2 |
| `mode-governance-engagement` (saturating affinity operator, graded commitment term, production default) | substrate_queue | coordinator register dynamics | implemented_pending_validation (knobs default-OFF: #64, #71) |
| `mech019-operating-mode-enabled-consumer` | substrate_queue | give `operating_mode` an enabled consumer (O3, O4) | registration only |
| `sd_salience_contested_mode_occupancy` | substrate_queue | make modes genuinely occupied | probe_queued |
| `dacc-pe-scale-normalisation` | substrate_queue | normalise `dacc_pe` at source (ARC-155 form) | pending_implementation |
| `mech005-endogenous-arousal-dynamic-range` | substrate_queue | make the E3 rate track endogenous arousal (L7) | registration only |
| `mech005-betagate-decommit-counter-and-commit-ceiling` | substrate_queue | BetaGate release instrument / commit ceiling | registration only |
| `commit-readiness-gate-no-behavioural-consumer` | substrate_queue | route CommitReadiness to behaviour | registration only; 0/150 action divergences when ON |
| `MECH465-COMMIT-GATE-HEADROOM` (optional adaptive commit threshold) | substrate_queue | commit bar vs rv scale (L2) | partial; the adaptive bar is "a SEPARATE decision" |
| `MECH054-SIGNED-HARM-BENEFIT-PE-PRECISION` | substrate_queue | separate pi_H / pi_B precision | proposed |
| `SD-026` prospective precision write channel | substrate_queue | attention -> precision write | no status |
| `SD-PP-B6/B7/B11` (epistemic/aleatoric split; learned sensory precision; harm-stream reliability) | substrate_queue | precision producers | registration only |
| `mech001-astrocytic-regulatory-field-registration` (a slow field R(x,t) feeding precision routing) | substrate_queue | slow regulatory field | registration only |
| `sd032b-payoff-self-feedback-integrator` | substrate_queue | the dACC payoff proxy is E3's own previous score | pending_implementation |
| CeA fast route from raw `hazard_at_agent` + a rate-of-change gate | GFLAG-0556/0557 (`cea_onset_input_reprobe_20260925.md`) | CeA fire onset | routed to the SD-035/MECH-046 owner; not built |

## 9. Limits and uncertainty

- **D0 throughout, except the edges that cite records.** "LIVE" means code-reachable and consumed at default config under the canonical StepHarness. It does not mean behaviourally material. The two live edges that were tested for material effect (L7 range, L10 consumer reach) came back flat or negative.
- **"At defaults" means `REEConfig.from_dims` defaults.** Almost no fleet driver runs at defaults. The all-ON and tier-1 recipes switch families on. DC-B catalogues those imposed regimes.
- **P6 (what rv measures) is a D0 finding from two independent reads.** A cheap D1 check is owed: log `error_var` on E3 ticks vs non-E3 ticks. It bears on GFLAG-0486 and the W3 commit-gate note.
- **Row granularity changes the counts** (sec 0 table note). The qualitative split does not change: LIVE rows are under 10%, and all of them sit in the E3-commit / clock / residue backbone.
- **Sub-audit reliability.** Five parallel code reads, cross-checked against each other. The one conflict found (L6) was settled against the code. G1 and G4 reached P6 independently. G2's "LIVE" label for the beta gate is overruled here. I did not re-read every row myself. Rows cited only in an appendix carry that appendix's D0 reading.

## Appendices (committed alongside)

`REE_assembly/evidence/planning/probes/dca/`:
- `G1_precision_e3.md`: precision, E3 arbitration, commitment
- `G2_modes.md`: modes, cingulate, PFC, closure, heartbeat
- `G3_threat.md`: threat, defence, veto, affect, residue
- `G4_neuromod_uncertainty.md`: neuromodulator analogues, uncertainty, curiosity
- `G5_memory_plasticity_sleep.md`: memory gating, plasticity, sleep, babbling

Each has full file:line citations on MAIN `436a988742` / BR `4070b0efa4`. Config-default extraction was an `ast` parse of `ree_core/utils/config.py` (scripts in `.scratch/breakthrough-20260924/dca/cfg_fields.py`, `fromdims.py`; not committed).
