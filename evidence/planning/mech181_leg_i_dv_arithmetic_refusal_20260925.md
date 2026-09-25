# EXP-1401 / MECH-181 leg (i): the CONFIRMING DV is arithmetic in the manipulation -- REFUSED at /queue-experiment

- **Written:** 2026-09-25T02:19:48Z. Session `metaworker-science-20260925-orchc-mech181-maintenance`
  (headless metaworker on `ree-cloud-5`), campaign `science-20260925-orchc-mech181-maintenance`,
  chip_ref `chip-proposal-exp-1401`.
- **Outcome:** **REFUSED. No script written, no queue entry added.** EXP-1401 stays unexecuted and is
  written back `blocked_substrate`.
- **Code under test:** ree-v3 `origin/main` @ `5e18e979`; REE_assembly `origin/master` @ `402ea96099`.
  Every `file:line` below is against those.
- **Route:** leg (ii) -> `/implement-substrate` (a NEW substrate entry; none exists).
  leg (i)'s CONFIRMING criterion -> `/governance` (owed falsifier re-denomination on MECH-181).

---

## 0. Headline

1. **MECH-181 leg (i)'s CONFIRMING criterion cannot fail.** "cumulative offline-phase work
   (`sws_n_writes + rem_n_rollouts`) is monotone in MEASURED MEL" is a **monotone non-decreasing
   function of measured MEL by construction** -- that composition IS the SD-MEL-CONSUMER
   implementation. Its matching FALSIFYING clause (i) ("offline-phase work is flat or non-monotone
   in MEASURED MEL") is therefore unreachable except through the `[0.5, 3.0]` clamp or the buffer
   cap, both of which gate (4) separately requires you to report and exclude. This is the
   `/queue-experiment` Step 2.5d **INERT** shape and a Step 4.5 **BLOCKING** verdict: the criterion
   cannot discriminate under any outcome.
2. **What is left of leg (i) is MECH-180's producer result, already measured.** Gate (1) -- the only
   genuinely empirical leg -- is "measured waking MEL monotone across enrichment levels". That is
   V3-EXQ-1069's P1 gate, and it is **already recorded monotone on 3/3 seeds**.
3. **Leg (ii) RESERVE -- MECH-181's only content over MECH-180 -- is substrate-ABSENT**, re-confirmed:
   `grep -rn "ablat\|attribution_noise\|slot_ablation" ree_core/*.py` finds only unrelated comments;
   no ContextMemory-slot-ablation or E3-attribution-noise-injection mechanism exists anywhere.
4. **The chip's own AMBER pre-flight caveat is FALSE as written** (section 3). Its two named remedies
   train modules the MEL prediction error never reads. Correcting it is what surfaced (1).

---

## 1. The arithmetic (the load-bearing finding)

The MEL consumer's entire mechanism is to scale two offline step counts by a monotone function of
measured MEL. Chain, every link read from source:

| step | site | what it does |
|---|---|---|
| 1 | `ree_core/sleep/mel_consumer.py:253-275` | `duration_factor() = clamp(1 + gain*(mel/ref - 1), mel_duration_factor_min 0.5, mel_duration_factor_max 3.0)` -- **monotone increasing in measured MEL** |
| 2 | `mel_consumer.py:277-283` | `scale_steps(base) = max(1, round(base * factor))` -- monotone non-decreasing in factor |
| 3 | `ree_core/sleep/phase_manager.py:572-582` | the sleep pass overwrites `agent.config.sws_consolidation_steps` and `rem_attribution_steps` with `scale_steps(...)` of their configured values, for the duration of the cycle |
| 4 | `ree_core/agent.py:13190-13197` | `run_sws_schema_pass`: `n_steps = min(config.sws_consolidation_steps, n_buf)`; `indices` has exactly `n_steps` entries |
| 5 | `agent.py:13315-13323` | `n_writes` increments **unconditionally** once per index (the MECH-122 spindle branch selects content, it never skips a write); `metrics["sws_n_writes"] = float(n_writes)` |
| 6 | `agent.py:13400`, `:13504` | `run_rem_*`: `n_steps = config.rem_attribution_steps`, replay called at `max(1, n_steps // 2)`; `metrics["rem_n_rollouts"] = float(len(terrain_scores))` |

Composing 1-6:

```
sws_n_writes    == min( max(1, round(sws_consolidation_steps * duration_factor(mel))), n_buf )
rem_n_rollouts  == a non-decreasing step function of  max(1, round(rem_attribution_steps * duration_factor(mel)))
```

so `sws_n_writes + rem_n_rollouts` is monotone non-decreasing in `mel` **as an identity**, not as a
measurement. Under CLAUDE.md's / `/queue-experiment`'s DV-symmetry table this is the
**monotone-rescaling** row: the manipulation reaches the DV only through a monotone rescaling, and
the DV is a rank/order statistic over arms.

**Confirmed numerically in the lineage's own landed manifest.** V3-EXQ-861i
(`..._20260914T121029Z_v3`), `sws_consolidation_steps` default 5, 6 cycles:

| variant | `mean_duration_factor` | `cumulative_sws_writes` | writes/cycle | `round(5 x factor)` |
|---|---|---|---|---|
| ANCHOR_PRE / PIN_A | 1.00701 | 31.0 | 5.17 | 5 |
| PIN_B / ANCHOR_POST | 0.88446 | 27.0 | 4.50 | 4 |

The DV tracks `round(base x factor)` and nothing else.

**MECH-181's own text already concedes this.** Its gate (1) insists the monotonicity be scored
"against MEASURED MEL not the novelty label, the distinction on which V3-EXQ-718's C1 failed 0/3
while its C2 passed 3/3". C2 -- the measured-MEL leg -- passed 3/3 **because it is the mechanical
half**. The proposal asks for the half that already passes for implementation reasons, and declines
to score the half (C1) that failed.

### Why gates (3) and (4) cannot rescue it
- Gate (3) "consumer un-pinned: `sws_n_writes` / `rem_n_rollouts` must VARY across arms" is
  **guaranteed** by the same scaling whenever measured MEL varies across arms. It is a
  necessary-condition check that passes by construction.
- Gate (4) HEADROOM (report the per-arm saturation fraction against the `[0.5, 3.0]` clamp) removes
  the only route by which the DV could have been non-monotone. Passing gate (4) makes the CONFIRMING
  criterion *more* certain to pass, not less.

---

## 2. What IS already measured (so leg (i) adds no new empirical content)

Gate (1) is the real measurement, and it is recorded. V3-EXQ-1069
(`..._20260920T082003Z_v3`, PASS, INV-063), 798a's validated ladder
`world_rule_shift_interval` in {0, 60, 25, 10} at `depth=2`, mean waking MEL:

| seed | NONE (iv 0) | LOW (60) | MED (25) | HIGH (10) | monotone? | `(HIGH-NONE)/NONE` |
|---|---|---|---|---|---|---|
| 42 | 2.013e-5 | 2.058e-5 | 2.632e-5 | 2.806e-5 | yes | 0.394 |
| 123 | 2.297e-5 | 2.641e-5 | 2.653e-5 | 2.851e-5 | yes | 0.241 |
| 456 | 1.584e-5 | 3.217e-5 | 3.590e-5 | 4.263e-5 | yes | 1.692 |

Monotone 3/3; 798a's registered `MIN_REL_MEL_SPREAD = 0.25` met on 2/3 (seed 123 at 0.241). The
matched-PE observation-noise control exists too -- V3-EXQ-798a `ARM_4_NOISE_LO` at sigma 0.12 reads
3.981e-5 / 3.566e-5 (seeds 42 / 123), i.e. at or above the HIGH arm, which is the intended MEL match.

So a MECH-181 leg-(i) run would re-measure a monotone ladder already recorded on 3/3 seeds, and pair
it with a DV that cannot disagree. **GOV-REUSE-1: gate (1) is recoverable from V3-EXQ-1069 and
V3-EXQ-798a; the CONFIRMING criterion needs no run because it is an identity.**

---

## 3. The chip's AMBER pre-flight caveat is false as written -- correction

The 2026-09-25T02:01Z pre-flight asserted, on the strength of GFLAG-0491's gradient-reach census,
that "in the exact lineage yesterday's verdict leaned on ... z_world and E2WorldForward are FROZEN
AT INIT for the entire run", and NAMED a change: wire in SD-070's `ZWorldP0Trainer` and, ideally,
SD-031's P1. Four corrections, each measured against source:

**(C1) The census finding is real but does not transfer to these drivers.** GFLAG-0491
(`gradient_reach_census_20260925.md`, REE_assembly `940c690c9d`) is correct that at `REEConfig`
defaults the agent builds 0 optimizers and moves 0/717k params. The census itself states the
consequence: *"every trained parameter in REE is trained by a driver-built optimizer"*. These drivers
build one.

**(C2) The MEL prediction error's predictor IS trained, in every driver in this lineage.** The
pre-flight read 861i's `recon.backward()` as "an unrelated read-only reconstruction probe". It is
the E2 world-forward trainer:

```
v3_exq_861i...py:629-650   _e2_train_step():
    z1_pred = agent.e2.world_forward(z0_K, actions_K)
    recon   = F.mse_loss(z1_pred, z1_K)
    recon.backward();  clip_grad_norm_(agent.e2.parameters());  optimiser.step()
v3_exq_861i...py:830       e2_opt = torch.optim.Adam(agent.e2.parameters(), lr=E2_LR)
v3_exq_861i...py:691       called every P0 waking step
```

Measured effect in the landed manifest: `probe_pe_init 0.00358 -> probe_pe_final 0.000145`,
`conv_rel_drop 0.959`. The same `_e2_train_step` exists at `v3_exq_1071...py:538-556` and
`v3_exq_798a...py:604-626`. The MEL PE producer is a converged network, not a frozen random
projection.

**(C3) Neither named remedy touches the MEL PE path.** The MEL PE is
`actual_z_world - ref_trajectory.world_states[1]` (`e3_selector.py:4786-4792`, called from
`agent.py:11225`), and `world_states[1]` is produced by **`E2FastPredictor.world_forward`**
(`e2_fast.py:200-221`, `:822`, `:839`).
- SD-031's `E2WorldForward` (`ree_core/predictors/e2_world.py`) is a **different module**, built only
  under `latent.use_e2_world_forward` (`agent.py:564-571`, default False) and read only by the SD-003
  attribution comparator (`agent.py:4716-4727`).
  `grep -c "E2WorldForward\|e2_world" ree_core/predictors/e3_selector.py` -> **0**.
- SD-070's `ZWorldP0Trainer.world_path_parameters()` (`ree_core/latent/zworld_p0.py:417-480`) is
  `split_encoder.world_encoder.parameters() + [world_precision_logit]` (+ optional skip). It does not
  touch `e2.world_transition` / `world_action_encoder` either.

After an action-map re-permutation the module that must re-learn is `world_forward`. Neither remedy
trains it; both would leave the stated concern untouched.

**(C4) Freezing the encoder is a requirement of the instrument, not the defect.** V3-EXQ-798a:523-524
states it: *"The encoder is frozen (only agent.e2 trains), which is what makes the frozen-probe
battery valid: the captured z0/z1 are CONSTANT across P0 checkpoints."* Adding SD-070 P0 concurrently
would make `conv_rel_drop` -- gate (1)'s own convergence readout -- uninterpretable.

**Gate (2) was already designed, and the pre-flight missed it.** V3-EXQ-798a:203-208 poses the
pre-flight's objection verbatim and resolves it: *"A FROZEN model cannot re-learn, so PE after a shift
would never decay regardless of whether the structure is learnable. The MEL measurement (P1) stays
frozen for comparability with 701c / 718a; the learnability probe (P2) enables online world-forward
training so decay is meaningful."* 798a:921-925 runs that P2 with `train=True`, bins PE by
`env._steps_since_world_rule_shift`, and declares the noise arms' flat quartiles vs the rule-shift
arms' decaying ones the discriminating DV (798a:236-239). That is MECH-181 gate (2), built.

**So the AMBER caveat does not gate this chip. The refusal in section 1 does, and it is a different
and better-founded objection.**

---

## 4. Other gates, recorded for the next session

- **Step 2.5 / 2.5a substrate readiness: PASS.** `world_rule_shift_enabled/_interval/_depth` +
  `steps_since_world_rule_shift` live (`causal_grid_world.py:918-928`); `use_mel_consumer` builds
  `MELConsumer` with `mel_duration_factor_min/max` 0.5/3.0 (`agent.py:2946-2983`), matching gate (4)'s
  clamp bounds exactly; `use_cross_module_consolidation` + `use_sleep_world_forward_consolidation`
  (`config.py:7580-7584`, `:7600`) add the `e2_world` closure to the offline pass
  (`phase_manager.py:762-785`). Nothing here is missing.
- **Step 2.5b re-derive brake:** MECH-181 **0** counted autopsies (not braked). MECH-180 4 and
  INV-050 6, but this would be a new EXQ *number* testing a different claim, so the brake's
  redesign exemption applies; note also that the most recent counted row
  (`failure_autopsy_V3-EXQ-861e_2026-08-21`) is an explicit producer release --
  `re_derive_brake.fired: false`, `recommended_substrate_queue_entry.action: "none"`,
  routing its residual (an H1-measurement-isolation vs H3-substrate discrimination) to
  `/queue-experiment`. **That residual is NOT settled by anything here.**
- **Step 2.5c substrate-path overlap -- three `corrupting` open entries overlap; two release, one
  applies:**
  - `SD-PP-B5-z-world-per-step-displacement-range` -- **releases.** Its own
    `severity_rationale` scopes the corrupting exposure to a consumer that enables
    `use_world_interventional` (default False, `config.py:908`), and says so expressly "so the Step
    2.5c cost is visible". Its `title_correction_2026_09_24` further records that the
    encoder-range premise is measured at `alpha_world` 0.3 and **not reproduced** at SD-008's
    `alpha_world` 0.9 on a live battery -- V3-EXQ-1082's ARM_OFF head reads its action
    (`d_act` 0.341/0.216/0.227, CI>0 3/3) and beats copy-the-input
    (`skill_vs_identity` +0.349/+0.219/+0.215). This lineage runs `alpha_world=0.9`
    (`v3_exq_1071...py:333`, asserted at `:358`). **Any future driver here must set
    `alpha_world >= 0.9` explicitly and assert it** -- `REEConfig.from_dims` defaults to 0.3.
  - `sd_cm_livetap_zworld_scale_anchor` -- **releases.** Scoped to the SD-CM-LIVETAP
    live-encoder tap being "the encoder's only gradient source"; these drivers give the encoder no
    gradient source at all and do not enable the tap.
  - `contextmemory-write-path-addressing-degeneracy` -- **APPLIES, and is measured live here.**
    Under the default `contextmemory_write_selection = "argmin"`, V3-EXQ-861i records
    `per_cycle_n_touched_slots = [1,1,1,1,1,1]`, `n_cycles_insufficient_touched_slots = 6`,
    `mean_sws_new_slot_diversity = 0.0` -- the deterministic single-slot lock that entry describes,
    reproduced in the MECH-180 lineage's own most recent manifest. The ADDRESSING half has a
    validated fix (V3-EXQ-943: BIAS 16/16 occupied 5/5, REFRACTORY >=2 on 5/5, LEGACY 2/5;
    re-confirmed by V3-EXQ-436g) but it is **default OFF**; the CONTENT half is open.
    **Consequence for MECH-181, and it compounds section 1:** with 31 prototypes written into one
    slot, `sws_n_writes` counts a representationally inert operation, so even a DV that were not
    arithmetic would not evidence "the update system stays exercised". Any future driver must set
    `contextmemory_write_selection="refractory"` (or `contextmemory_write_usage_balancing=True`) and
    report `n_touched_slots`, accepting that this departs from the 798a/861 regime.
- **Step 2.6 ethics preflight:** all-`false`, `decision: allow` (SENT-0; V3 is pre-ethical
  instrumentation). No V4-boundary concern.

---

## 5. What is owed, and to whom

1. **`/governance` -- re-denominate MECH-181's leg-(i) CONFIRMING criterion onto a DV that is not an
   identity of the consumer.** Candidates the substrate already exposes, none of them a step count:
   the across-sleep frozen-battery delta (V3-EXQ-1071's `B1_infonce_delta` / `mse_delta`, i.e. what
   sleep ADDED on a FIXED battery); `sws_slot_diversity` / `n_touched_slots` under a non-degenerate
   write path; the `cross_module_consolidation_*` readouts. Until then, leg (i)'s FALSIFYING clause
   (i) is unreachable and leg (i) must not be scored as confirming MECH-181.
   Raised as a `governance_flag.py` `evidence_discrepancy` entry against MECH-181 / MECH-180.
2. **`/implement-substrate` -- build leg (ii)'s matched-insult harness.** ContextMemory slot ablation
   OR E3 attribution-noise injection (MECH-181's own "OR"), with a paired per-seed retention delta.
   **No `substrate_queue.json` entry owns this**; one needs registering. This is
   `complicated (buildable)`, not probe-gated -- the proposal says so itself.
3. **A note for whoever builds leg (ii):** `cross_module_consolidation_steps` is a fixed config value
   and is **NOT** MEL-scaled (`phase_manager.py:572-597` scales only `sws_consolidation_steps` and
   `rem_attribution_steps`). So the offline *gradient* budget is arm-MATCHED. That is convenient for
   leg (i) (no differential-training confound) but it means MECH-181's reserve mechanism, if it is
   meant to run through offline gradient volume, has no wiring at all today.

---

## 6. Negative-instrument note

Every "absent" above is a positive read, not a silent zero, and each names the command that produced
it: the leg-(ii) grep (0 hits, unrelated comments only), the `e3_selector` grep for `e2_world`
(exactly 0), the re-derive-brake counter (0 for MECH-181, printed per-run-id), the queue/ID namespace
checks (`V3-EXQ-1100` free in the queue on `origin/main`, in `experiments/` on `origin/main`, and in
every grep across both repos). `V3-EXQ-1100` was reserved for this work and is **released unused**.
