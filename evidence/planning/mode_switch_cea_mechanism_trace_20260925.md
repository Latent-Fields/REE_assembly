# Mode-switch and CeA-interrupt mechanism trace (2026-09-25)

- **Written:** 2026-09-25T13:05Z. Session `bt0925-modetrace` (breakthrough integration pass `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-mode-switch-cea-mechanism-trace`.
- **Scope:** probe only. No ree_core edits, no queue entries, no chips, no claims.yaml edits.
- **Code under test:** ree-v3 `origin/main` @ **`23714f0`** (private detached worktree). Every `file:line` below is against that sha.
- **Probes:** `REE_assembly/evidence/planning/probes/modetrace/` (scripts + raw JSONL in `results/`). Mac CPU, `torch.set_num_threads(2)`, one process at a time, seeds 11/12/13, 300 env steps per run, `CausalGridWorldV2(size=10, num_hazards=3, num_resources=3)`, hazard injected every 30 steps (`_inject_external_hazard`, as in the EXP-0787 probe). `world_dim = self_dim = 32` (deployed). **Untrained agents** throughout (the question is what the wiring can do, not what a trained agent does); driven through `experiments/_harness.StepHarness` so harm observations reach `sense()`.
- **Domains:** D0 = code read; D1 = measured to exist/move; D2 = intervening changes the native consumer (here: the coordinator's discrete mode register, and CeA's gate input).

## 0. Headline

1. **Q1 (switching). Stale premise corrected.** "The coordinator produces no within-life mode transition" holds only in the dACC-off configuration that MECH-157's precondition and the EXP-0787 probe used. The coordinator has two failure modes, and they have different roots:
   - **dACC OFF (MECH-157 / EXP-0787 config): (c) wiring.** Every live affinity input argues for `external_task`, and the salience aggregate is identically 0.0. Both trigger conditions fail on 100% of ticks. A switch is impossible by construction.
   - **dACC ON, no `external_task_drive`: one switch per life, then locked. The pinning term is the ARGMAX condition.** The only salience source (`dacc_pe`) is also the dominant `internal_planning` affinity source. So the high-salience ticks that could fire the trigger are exactly the ticks that push the argmax away from `external_task`. After reset, the register moves external_task -> internal_planning once and cannot come back. Within-life reversals: **0/0/0**.
   - **D2 intervention: add an independent input that argues for external_task** (`use_external_task_drive`, the lineage's own input). Within-life reversals go **0/0/0 -> 2/16/25**, and switches back into external_task go **0/0/0 -> 1/16/13**. The affinity half alone does nearly all of this (salience weight 0: 2/12/25).
2. **Q2 (CeA). Stale premise corrected: training `harm_eval_head` cannot lift the CeA drive (D2).** CeA's gate reads `mean|z_harm_a|`, the output of `LatentStack.affective_harm_encoder`. `e3.harm_eval_head` is not on that path. With the WakingTrainer ON for 300 steps, the harm_eval_head parameters changed on 3/3 seeds and the affective encoder hash was **bit-identical** on 3/3.
   - **Root: an absolute threshold on an unanchored latent magnitude.** At init, the whole valid input range reaches only `low_freq` 0.14-0.20 (all-ones input), about 3x under the 0.5 threshold. The one existing objective that trains the encoder (SD-011 `harm_accum` aux) drives `low_freq` to **12-17 (mean) on every tick**, about 25-35x over threshold and tonic. That leaves the gate either never firing or always firing. Nothing makes it onset-locked.
   - Even a fire cannot force a coordinator switch. The CeA salience contribution is bounded at `0.5 x 0.8 = 0.4` against `switch_threshold = 1.0`, and its `mode_prior` pushes toward `external_task`, the mode the register already sits in. With a forced fire every tick (instrument arm), switches = **0/0/0**.
3. **Shared upstream.** `dacc_pe`, the coordinator's only live salience source, is also a function of `||z_harm_a||` when `use_e2_harm_a` is off: `dacc.py:213-218` falls back from a prediction error to a plain norm. So the switching alarm and the CeA gate both read the magnitude of the same encoder, and nothing anchors that encoder's scale. This plausibly explains the lineage's `dacc_pe ~16-17` that needed the affinity cap: 935a's curriculum calls `compute_harm_accum_loss` (`experiments/scaffolded_sd054_onboarding.py:1436`), and that objective inflates `|z_harm_a|` about 100x in this probe. This link is **D0 plus an analogy**. I did not re-train a 935a agent.

## 1. Q1 -- why the coordinator does not switch within a life

### 1a. The update rule (D0)

`SalienceCoordinator.tick` (`ree_core/cingulate/salience_coordinator.py:533-719`) is memoryless in its soft vector. Each tick it rebuilds the logits from the current `_input_signals`:

- `external_task` gets `external_task_bias = 1.0` (`:593`), plus `affinity_weight x value` for each input. A value is clipped only when `affinity_input_cap` is set (`:617-639`).
- `operating_mode = softmax(logits / T)` (`:660`).
- `salience_aggregate = sum(salience_weight x value)` (`:664-666`).
- The discrete `current_mode` flips only when all three hold (`:687-694`): `salience_aggregate > enter_threshold` (base `switch_threshold = 1.0`, `:311`, x `(1 + stability_scaling x pcc_stability)`); `operating_mode[current] < exit_threshold` (defaults to 1.0, which is always true, so the MECH-266 Schmitt trigger is inert, as the 935a autopsy found); and `soft_argmax != current_mode`.

`reset()` (`:478-486`) forces `current_mode = external_task` and zeroes every input. It is called on every episode boundary (`agent.py:4119-4120`). That call is the source of the known `n_switches == n_episodes` artifact: one post-reset switch per life.

So there is no hysteresis state or cap that "pins" the register tick to tick. The register moves when both a salience signal and an argmax change are present on the same tick. The questions are which inputs supply each one, and whether they are independent.

**Who argues for what, as wired** (`salience_coordinator.py:285-298`, `agent.py:727-769, 2573-2577, 2785-2791, 2800-2808`, closure `governance/closure_operator.py:708-713, 757-795`):

| input | affinity -> mode | salience weight | live when |
|---|---|---|---|
| `dacc_pe` | internal_planning 1.0, internal_replay 0.5 | 1.0 (`salience_dacc_pe_weight`) | `use_dacc` |
| `dacc_foraging` | internal_planning 1.0, internal_replay 0.3 | 0.5 | `use_dacc` |
| `dacc_difficulty` | internal_planning 0.5 | -- | `use_dacc` |
| `aic_salience` | internal_planning 1.0 | 1.0 | `use_aic_analog` |
| `closure_event` | internal_planning 0.5 | -- | closure fires; **latched until episode reset** (written 1.0, never cleared) |
| `drive_level` | external_task 1.0 | -- | z_goal / drive on |
| `external_task_drive` | external_task 3.0 (935a) | 2.0 (935a) | `use_external_task_drive` |
| `override_signal` | external_task 0.3 | -- | SD-037 on |
| `cea_mode_prior` | external_task 1.0 | -- | CeA fire |
| `cea_fast_prime` | -- | 0.5 | CeA fire |

The asymmetry is what matters: **every salience-bearing input except `external_task_drive` and CeA also argues for internal_planning.** A transition INTO internal_planning is self-consistent: one signal supplies both conditions. A transition BACK to external_task needs, on the same tick, salience > 1 AND an external_task logit above the internal_planning logit. With dACC as the only salience source, the salience rises exactly when the internal_planning logit rises.

### 1b. Measured (D1), per seed 11/12/13

| arm | config delta from EXP-0787 probe config | switches | within-life beyond first | switches INTO external_task | ticks salience > thr |
|---|---|---|---|---|---|
| A0 | none (dACC off, AIC off) | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |
| A1 | + `use_dacc`, cap 2.0 | 3/20/25 | **0/0/0** | 0/0/0 | 38/88/219 |
| A2 | + `use_dacc`, no cap | 3/20/25 | 0/0/0 | 0/0/0 | same as A1 |
| A3 | A0 + CeA threshold 0 (instrument) | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |

(A1's into-external count is implied: every episode starts in external_task and makes at most one switch, all into internal_planning.) Episodes per seed: 9/42/31 (untrained agent, short lives). Coordinator ticks: 140/290/271.

- **A0.** `salience_aggregate` is exactly 0.0 on every tick. The only nonzero affinity inputs are `override_signal -> external_task` (mean 0.03-0.08) and the latched `closure_event -> internal_planning` (mean 0.31-0.40). The external_task logit leads the best other logit by a margin of at least 0.52 on every tick. Both trigger conditions fail everywhere.
- **A1/A2.** `dacc_pe` runs 0.19-1.27, so the salience clears 1.0 on many ticks. The argmax is internal_planning on 97/289/270 of the 140/290/271 ticks, and it is external_task on only 1 tick in seeds 12 and 13. Once the register is in internal_planning, the argmax almost never returns. **Diagnosis: (a)+(c). The inputs that would argue for external_task are absent or far too weak. The single salience source is coupled to the opposing affinity.** Not (b): the cap does not bind here (A1 = A2), and the exit hysteresis is inert. Not (d) at the tick level: reset happens per episode, and it produces the one-switch-per-life artifact.
- **A3.** A CeA fire every tick adds salience ≤ 0.067 (max) and adds `mode_prior` to external_task. The margin **widens** (mean 0.77-0.91). No switch.

### 1c. D2 intervention: an independent external_task input

| arm | delta | switches | within-life beyond first | INTO external_task |
|---|---|---|---|---|
| A1 (control) | dACC + cap | 3/20/25 | 0/0/0 | 0/0/0 |
| **A4** | A1 + `external_task_drive` (aff 3.0, sal 2.0; goal gate off) | 5/32/50 | **2/16/25** | **1/16/13** |
| A5 | A4 with salience weight 0 | 5/28/50 | 2/12/25 | 1/12/13 |

Prediction met on 3/3 seeds. Genuine within-life alternation appears as soon as an input argues for external_task independently of the dACC alarm. The affinity half carries it, because the dACC alarm already clears 1.0 on many ticks. This is the same mechanism that gives 935a's live-margin seeds 57-59 switches over 15 episodes: that driver runs `use_external_task_drive` with these weights plus a cap.

**Incidental (D1, consumer half, out of scope; owned by `chip-20260917-sd032a-operating-mode-no-consumer`).** Per seed, all six arms produced the identical episode count and the identical coordinator-tick count, including A4 against A5, where the register alternated differently. In this config, changing the mode sequence changed nothing observable about the trajectory. This matches MECH-157's precondition that "locking the mode changes zero committed actions".

### 1d. Q1 root, named

**Root: input topology, not dynamics.** In the default wiring, the only salience-bearing source (dACC PE/foraging, and AIC when on) is also an internal_planning affinity source, and no default-ON source argues for external_task with enough weight. Evidence: `salience_coordinator.py:285-298` and `:686-691`; the dACC-off configs additionally have zero salience (`agent.py:764-768` registers only dACC and AIC salience weights). So:

- **dACC off:** switching is impossible (`complicated (buildable)`, config only). Turn on `use_dacc` plus an external_task source.
- **dACC on:** one-way switching. Reversal needs `use_external_task_drive` (exists, default OFF, `config.py:4614`), or another independent external_task source. `drive_level` and `cea_mode_prior` are candidates, but they are silent in these configs.

## 2. Q2 -- the MECH-039 interrupt producer and why it is silent

### 2a. Producer and gate (D0)

- **Producer:** SD-035 `CeAAnalog.tick` (`ree_core/amygdala/cea.py`, called from `agent.py:6093` inside `sense()`). The gate is `low_freq = ||z_harm_a||_1 / dim` (`cea.py:309-331`) and `urgency_fire = low_freq > fast_route_threshold (0.5)` (`:337`). On fire it emits `mode_prior` and `fast_prime`, both `(low_freq - 0.5) / 0.8`-scaled and capped at 0.8 (`:339-365`).
- **Input:** `z_harm_a = LatentStack.affective_harm_encoder(harm_obs_a[, harm_history])` (`latent/stack.py:1612-1621`). The encoder is `Linear-ReLU-Linear` with no output normalisation (`stack.py:175-230`). Its input `harm_obs_a` is the hazard field (25) plus the **resource** field (25) (`config.py:256`).
- **Into the coordinator:** `cea_mode_prior -> external_task 1.0` (affinity) and `cea_fast_prime` salience 0.5 (`agent.py:2573-2577`).
  - **Structural ceiling (D0, confirmed D2 by A3):** CeA's maximum salience contribution is `0.5 x 0.8 = 0.4 < switch_threshold 1.0`. It cannot fire the MECH-259 trigger alone.
  - Its affinity points at `external_task`, the default and post-reset mode. From external_task it cannot produce a switch at all. At most it can co-sponsor a return from internal_planning, and only when another source supplies ≥ 0.6 salience on the same tick.
- **SD-037 `override_signal`** enters only as `external_task` affinity 0.3 (`agent.py:2785-2791`) and has no salience weight. It cannot fire the trigger either. The 0787 probe found its onsets are not onset-locked.

### 2b. The orchestrator's open question (a): does training `harm_eval_head` lift CeA? **No (D2).**

`cea_input_probe.py` uses the EXP-0787 config with `waking_trainer_enabled=True` (cc20be5 HarmEvalMember), runs 300 steps, and hashes parameters before and after:

| seed | harm_eval_head changed | affective_harm_encoder changed | low_freq post-injection / other | threshold |
|---|---|---|---|---|
| 11 | yes | **no** | 0.138 / 0.139 | 0.5 |
| 12 | yes | **no** | 0.130 / 0.128 | 0.5 |
| 13 | yes | **no** | 0.156 / 0.152 | 0.5 |

`harm_eval_head` regresses on `z_world` (`utils/waking_trainer.py:115-133`). It is not upstream of CeA. The census (`probes/census/gradient_reach_census_20260925.md` row `affective_harm_encoder`) independently has this encoder **never trained in any fleet recipe**: D in 1083, O in all-ON, not built in the rest.

### 2c. Dynamic range and the one existing objective (D1/D2)

- **At init** (`cea_input_probe.py`, seeds 11-13):
  - `low_freq` on all recorded inputs: max 0.14-0.18.
  - All-ones input (every field cell saturated): 0.14-0.20. Zeros: 0.04-0.08.
  - Recorded inputs x5: 0.58-0.86. **The gate is unreachable for any valid input**, about 3x short.
  - The channel does carry hazard information: `corr(low_freq, hazard-field mass) = 0.96-0.98`. It sits on the wrong scale.
  - Injection onsets do not move it, because `harm_obs_a` is an EMA and injection relocates an existing hazard.
- **After the only existing encoder objective** (`cea_harmaccum_probe.py`): SD-011 `harm_accum` aux, i.e. `compute_harm_accum_loss`, `agent.py:12554-12617`, MSE of a sigmoid head to `accumulated_harm`, which is ≤ 0.03 in these runs. Offline, 2000 Adam steps at lr 1e-3, weight 1 (the native weight is 0.1, so this is a faster version of the same objective). Loss 0.17-0.29 -> 0.0003. `low_freq` mean goes from 0.11-0.21 to **12.0-16.9** (max 14.4-19.9). **The gate would fire on every tick.** The mean/max ratio of about 0.85 means the signal is tonic, not onset-locked.

**Q2 root, named:** `cea.py:337` applies an absolute threshold to the magnitude of an un-normalised latent. Nothing ties that magnitude to threat: the init scale falls below threshold, and the only training objective overshoots it by an order of magnitude. Neither regime gives a hazard-onset fire. It is not the untrained `harm_eval_head`, which is off-path. And even a well-calibrated CeA fire cannot by itself force the coordinator switch MECH-039/MECH-046 need (section 2a ceiling).

## 3. Recommendation (work-graph debt vocabulary)

| item | class | owner row |
|---|---|---|
| Q1-dACC-off: turn on a salience source (`use_dacc`) plus an external_task source (`use_external_task_drive`) in any config that needs switching | `complicated (buildable)`, config only | `substrate_queue` **mode-governance-engagement** (its switching half). This record names the root that half is missing: input topology / coupling, not the cap. |
| Q1 production-default decision: should `external_task_drive` (or another independent external_task source) be default-on so reversal exists natively? And does reversal survive training (cap-margin interplay, 935a)? | `complex (probe-gated)` -> `puzzle (known rules)`: one trained-agent run with A1/A4 arms on a cloud worker | **mode-governance-engagement**; MECH-157's EXP-0861 stays parked until it is measured on the trained curriculum |
| Q2 CeA gate calibration: a relative/onset gate (baseline-subtracted or derivative of `z_harm_a`), or a magnitude-anchored encoder objective | `complex (probe-gated)` / `mystery (known data)`. The data are in hand, and the question is what the gate SHOULD read. A threshold change on the current input would only move the saturation point. | SD-035 / MECH-046 owner (the EXP-0787 design doc's `puzzle` row is now answered: **no**, training `harm_eval_head` does not lift it) |
| Q2 structural ceiling: CeA salience ≤ 0.4 < 1.0, and its affinity points at the default mode | `complicated (buildable)` once decided. It is a design decision (weights at `agent.py:2573-2577`), and the MECH-039/046 claim holder must decide it. | MECH-039 (EXP-0787 G1/G3), MECH-046 |
| Consumer half (mode sequence has no behavioural reach) | out of scope | `chip-20260917-sd032a-operating-mode-no-consumer` |

**Single next action.** One trained-agent cloud run (935a's curriculum, arms A1 vs A4, 3 seeds) to measure within-life reversals and `|z_harm_a|` / `dacc_pe` scale after training. It releases the Q1 default decision and confirms or refutes the section-0 shared-upstream hypothesis. Owned by the mode-governance-engagement row. I did not queue it.

## 4. Premises re-measured

- "Coordinator produces no within-life mode transition" (rec-20260925-6231be2b context, MECH-157 P5): **true only with dACC off.** With dACC it switches once per life; with an independent external_task input it alternates. The alpha_world 0.57 < 0.9 concern under MECH-157 routing stands whenever external_task is not the argmax.
- "CeA silent because harm_eval_head is untrained": **false.** harm_eval_head is off-path (D2 hash test).
- EXP-0787 section 3 numbers (CeA `low_freq` max 0.172, mean 0.133; 0 switches in 140 ticks): **reproduced exactly** on seed 11 (A0).
- 935a autopsy: "Schmitt trigger inert, exit defaults 1.0": **re-confirmed** at `salience_coordinator.py:684`.

## 5. Uncertainty

- All Q1 numbers come from untrained agents with short lives (7-33 steps). Reversal counts scale with life length, and the trained regime (dacc_pe ~16, cap binding) is not re-measured here.
- The `harm_accum` probe trains offline at weight 1, not in-loop at the native 0.1. The direction is clear and the magnitude is not.
- The shared-upstream hypothesis for 935a's `dacc_pe ~16` is inference, not measurement.
