# N3 proper: which E3 horizon aggregation tracks true consequence with the REAL W3 member head? (pre-registered probe)

- **STATUS: FINAL (2026-09-25T22:11Z). RESULTS appended below; the pre-registration (committed 21:32Z as `78820b45c7`) is unchanged apart from this line. Pre-registered verdict: NONE_PASS.** Preconditions all hold (W3 head L2R bar 4/5, missed only on s532 at 0.467; twin at chance 5/5; every canary PASS), so this is a real verdict, not CANNOT_DETERMINE. **Gate (a) passes for DISC_0.5 (4/5), DISC_0.8 (4/5) and D1 (4/5, excluded by SD-081). Gate (c) passes for no aggregation (DISC_0.5 0/5; best 1/5).** The literal action-blind reference was degenerate on 100% of states, as predicted, so (c) was read against the pre-registered BLINDR fallback. Against it, real and twin move E3's pick about equally often (0.59-1.00 vs 0.79-1.00), because the fixed-permutation twin is anti-mapped, not blank (premise 4). **W4 is not buildable on the gate as written. It is buildable on DISC_0.5 if the gate owner re-specifies (c)** (options in the last section).
- Session `bt0925-n3` (orchestrate-20260924-breakthrough-c2), chip_ref `chip-20260925-coupled-n3-proper`. Brief: `.scratch/breakthrough-20260924/Z_n3proper.md`. Plan of record: `coupled_loop_repair_campaign_plan.md` sec 3 (W3, W4), sec 4 (N3 row), decision log 2026-09-25T14:19Z.
- **Design = N3-pre** (`n3_pre_e3_aggregation_probe_20260925.md`, `d4bb6449b3`) **with the proxy head REPLACED by the W3 member** (`E2WorldMember`, ree-v3 `integration/coupled-loop-repair` @ `042895a`), trained natively by the W3 member-gate protocol (`w3_e2_world_member_build_20260925.md`, `f82cb986c5`; `probes/w3/w3_l2r_member_probe.py`), and with the three gate-definition fixes of the 14:19Z decision log entry.
- Code: ree-v3 @ `042895a3a2` in a throwaway detached worktree (`/Users/dgolden/REE_Working/.scratch/wt-n3`). **No ree_core edits.** Instruments: `experiments/_lib/coupled_acceptance.py` (I1, on the branch via main `c9612dd`): `collect_probe_states`, `env_q_values`, `probe_state_validation`, `e3_score_fn`, `e3_choice_quality`, `spearman`, and its pinned canaries `canary_e3_structure` / `canary_action_discrimination`. Probe script: `probes/n3/n3_probe.py`.
- Evidence domain targeted: **D2** for (a) and (c) (swapping the head / the aggregation changes the native consumer's ranking, read against cloned-env consequence). No D3.

## Premises re-measured before pre-registering (D0 code read at `042895a`)

1. **E3's score reads z_world only.** `score_trajectory` (`e3_selector.py:1790`) = F (`compute_reality_cost` :1493, mean squared world step) + lambda M (`compute_harm_cost_fallback` :1520, harm_eval over world states) + rho Phi_R (:1836), each through `_get_world_states` (:1473), which truncates to `_score_depth_limit` (SD-081's knob). No term reads the action sequence or z_self when world_states exist.
2. **Consequence for the action-blind reference (gate (c)).** `world_forward` (`e2_fast.py:201`) = `z + world_transition(cat(z, world_action_encoder(a)))`, and `rollout_with_world` calls `self.world_forward` per step (:832). An exactly action-blind head therefore gives **every candidate in a pool the identical z_world rollout, so every candidate the identical E3 score**: its pick is a 32-way tie. **Prediction (stated before any run): the literal action-blind reference is DEGENERATE on 100% of states**, and flip-vs-it cannot separate real from twin (under a fair tie-break both flip at 1 - 1/32). The fallback below is pre-registered for exactly this.
3. **Depth-1 IS the habit read** (`_score_depth_limit = max(2, dualsystem_habit_depth)`, `e3_selector.py:2088`; `dualsystem_habit_depth` 2). Unchanged from N3-pre: D1 is reported for reference only and cannot be selected.
4. **The W3 twin is anti-mapped, not blank.** With the FIXED permutation [1,2,3,4,0] on retained babbling, the W3 gate twin scored disc4 0.127-0.190 (below chance 0.25): it has learned a wrong action map. It is therefore as action-SENSITIVE as the real head, only mis-mapped. Expected consequence, stated in advance: gate (a) can separate real from twin (ranking tracks truth vs a permuted truth); a pure flip-rate gate (c) probably cannot, because both heads move the pick. This is a prediction, not a gate change.
5. **O7 (W3 buffer format) is set at `042895a`**: raw obs re-encoded at replay + `agent._last_action` as fed to E2 (W3 record P5). This probe uses those defaults.

## Design (fixed)

**Regime** (N3-pre / babbling probe / W3 gate): Phase-0 CausalGridWorldV2 size 12 (`babble_probe.make_env`, env seed = seed*160 + k); `build_B(seed)` agent, world_dim 32 (deployed), alpha_world 0.3; random-init encoder, **frozen**. Mac, `torch.set_num_threads(2)`, one process, one seed per hold of `.scratch/breakthrough-20260924/mac_probe.lock`.

**Seeds: 531, 532, 533, 534, 535** (fresh: not in any committed probe result or record found by grep; W3 used 106-110, N3-pre 521-525). A 1-seed pipeline smoke on **non-registered seed 530** at tiny sizes (post 200 steps, 2 updates/step, 60 probe steps) was the only execution before this commit; its numbers are not results. It validated: all five heads train/score; cloned-env validation max |diff| 0.0; decomposition canary 0.0; relative batch canary 1.2e-7; I1 canaries reproduced; **BLIND degenerate on 100% of states and BLINDR on 0%** (premise 2 confirmed mechanically). The first smoke attempt crashed on the BLIND guard (see 'Also reported'); fixed before this commit.

**Test sets.** TE4: 3,000 held-out uniform {0..3} steps (k = 120..134; the L2R-bar test set). TEW: 3,000 held-out uniform {0..4} steps (k = 160..174; disc5, per-depth fidelity to H = 30).

**Heads** (every trained head: fresh `build_B` agent with the same frozen encoder, `WakingTrainer` with ONLY the `E2WorldMember`, the W3 protocol verbatim: W2a `StructuredBabbler` (5 classes incl. stay, runs {1..4}, seed S*13+1) over Phase-0 episodes k = 0..11 into the FROZEN retained set; 3,000 member updates; then 1,200 native closed-loop `StepHarness` steps (k = 50..55) at 8 member updates per step, 25% retained replay, re-encoded; MSE; lr 3e-4; batch 32; clip 1.0):
| head | difference from REAL |
|---|---|
| **REAL** | none (the W3 member as built) |
| **SHUF** (twin) | retained babbling actions relabelled by the FIXED class permutation [1,2,3,4,0] (decision log 14:19Z item 3; the W3 gate's twin) |
| **BLIND** (gate (c) reference) | the action input to `e2.world_forward` is zeroed throughout the member run (training and the agent's own planning); scored **exactly action-blind** (`world_action_encoder.weight := 0`, so the head's output for any action equals its output for the zero action it was trained on) |
| **BLINDR** (pre-registered fallback reference) | the SAME trained BLIND head, scored with `world_action_encoder.weight` left as trained (= its init, since a zero input gives it no gradient): trained and bounded on zero-action data, action-sensitive only through untrained weights, i.e. action-UNINFORMATIVE rather than action-blind |
| **INIT** | the untrained head (descriptive only; N3-pre's old (c) reference) |

**Probe states.** A fresh agent with the REAL head live runs native waking in env episode k = 100 for 320 harness steps; every 8 steps, I1 `collect_probe_states` records the native CEM pool (RNG-neutral), the true next z_world per class through sense()'s encoder (side-effect-free), and env-Q per class (6 continuations x 4 random steps). >= 20 states per seed are required; if fewer, the seed is re-run with 640 steps (resources rule only). All heads are scored on the same states and pools.

**Aggregations** (N3-pre, unchanged): J_L = native `E3.score_trajectory` with `_score_depth_limit = L`, L = 2..31; Delta_d = J_{d+1} - J_d.
| id | definition | nominal planned depth |
|---|---|---|
| D1 | J_2 | 1 step (== habit read) -- **reference only** |
| **DISC_0.5** (lead) | J_2 + sum_d 0.5^(d-1) Delta_d | 30 (effective ~2) |
| DISC_0.8 | J_2 + sum_d 0.8^(d-1) Delta_d | 30 (effective ~5) |
| FIDW | J_2 + sum_d w_d Delta_d, w_d = 1 iff THIS head's median rollout error at depth d beats persistence on TEW | the deepest weighted d |
| FULL | J_31 (current behaviour) | 30 |

**Candidate sets.** Scaffold pool (pool[0] with step 0 replaced by one-hot c, c = 0..4) for (a) and (b), J_true(c) = E3's score of [z0, true z1(c)]. Native pool (32 recorded candidates) for (c).

## Criteria (fixed)

Per seed and per aggregation, differences REAL minus SHUF:
| gate | quantity | per-seed pass | passes if | status |
|---|---|---|---|---|
| **(a)** | mean over states of Spearman(J_pred, J_true) on the scaffold pool (I1 `e3_choice_quality`, states with non-constant J_true) | diff > 0.15, >= 10 informative states | >= 4/5 seeds | **GATING** |
| **(c)** | native-pool pick-flip vs the action-blind reference, with ties broken uniformly on both sides: flip = 1 - \|P ∩ T\| / (\|P\| \|T\|), P / T = the argmin sets (relative tolerance 1e-6) of the head / the reference | diff > 0.15 | >= 4/5 seeds | **GATING** |
| (b) | P(argmin J_pred on the scaffold pool is in the env-Q-best set) (I1 `e3_choice_quality`, informative states) | diff > 0.10 | >= 4/5 | **REPORTED ONLY** (moved after W5, decision log 14:19Z item 2) |

**Gate (c) reference rule (pre-registered because of premise 2).** The reference is BLIND. It is DEGENERATE on a seed if all candidates are tied (\|T\| = pool size) on >= 50% of that seed's states. On a seed where BLIND is degenerate, (c) is read against **BLINDR** instead; if BLINDR is also degenerate there, that seed's (c) is CANNOT_DETERMINE (counts as not passing). If (c) is CANNOT_DETERMINE on >= 2 seeds, **(c) is CANNOT_DETERMINE overall**, and the probe's selection verdict is CANNOT_DETERMINE (gate-(c) instrument degenerate), with (a) still reported per aggregation. The plain np.argmin flip rate (index tie-break) is reported beside it for transparency, never gated.

**SD-081 compatibility** (N3-pre, unchanged): compatible iff nominal planned depth > 1 step. D1 incompatible by construction; DISC / FULL compatible; FIDW compatible iff REAL has w_d = 1 for some d >= 2 on >= 4/5 seeds. Descriptive for all: native-pool pick agreement with the habit (D1) pick; agreement > 0.9 is flagged as a practically degenerate planned/habit contrast.

**Selection rule.** The SIMPLEST passing aggregation in the order **DISC_0.5 < DISC_0.8 < FIDW < FULL** that passes (a) AND (c) and is SD-081-compatible. D1 is reported only. Nothing passes: **NONE_PASS**.

**CANNOT_DETERMINE (whole probe)** if any of:
1. **the W3 head misses its own L2R bar**: REAL disc4_h1 (TE4) >= 0.47 and k (H = 10) = 10, required on >= 4/5 seeds (W3 member gate (a)'s own rule). Reading of the brief's "misses its own L2R bar on a seed (then say which)": every seed that misses is NAMED and stays in the gate counts; a sensitivity reading without it is reported; the whole probe is CANNOT_DETERMINE only if the bar fails on >= 2 seeds (the bar's own 4/5 rule);
2. **the twin is not at chance**: SHUF disc4_h1 (TE4) <= 0.32 and disc5_h1 (TEW) <= 0.27 (upper bounds: the twin must not carry the TRUE map; below chance = anti-mapped, allowed, as in W3 gate (c)), required on >= 4/5 seeds;
3. **an instrument canary fails on any seed**: I1 `probe_state_validation` not PASS (max |diff| > 1e-5); depth decomposition J_31 vs unlimited J > 1e-5; the batched-vs-single scorer canary > **1e-4 relative to max(1, |J|)** (N3-pre point 4: the absolute 1e-5 was mis-set against float32 at |J| 19-419); I1 `canary_e3_structure` or `canary_action_discrimination` not reproduced; or < 20 probe states after the re-run rule;
4. gate (c) CANNOT_DETERMINE overall (reference rule above): then the SELECTION is CANNOT_DETERMINE while (a) is still reported.

**Also reported.** Per head: disc4 / disc5 / k (TE4), k30 and per-depth fidelity (TEW), rollout norms t1 / t30 vs true, member guard statuses (REAL, SHUF). For BLIND the guard is DISARMED (`waking_trainer_guard_min_steps = 0`, `config.py:8110`): with a zeroed action input `world_action_encoder.weight` is dead by construction and the guard RAISES on a dead tensor (`waking_trainer.py:821`; seen in the smoke). Instead the probe asserts and reports that BLIND's action weight is byte-identical to init, post-phase actions / reward. Per aggregation: the N3-pre-form Spearman (both sides non-constant) as a cross-check; flip vs INIT (old reference); and, descriptively, a "toward-better" reading on the native pool (+1 / 0 / -1 as the head's pick's first-action class has a lower / equal / higher TRUE one-step J than the reference pick's class), which is the other (c) redefinition N3-pre named.

**No tuning, and no extra arms or seeds after seeing results.** Post-hoc diagnostics, if any, are labelled as such.

**Known limits, in advance.** J_true is E3's own one-step score (F favours small moves; `harm_eval_head` untrained), so (a) is partly self-consistency; (b) is capped by valuation until W5 (N3-pre oracle 0.09-0.22 vs chance 0.20). Encoder random-init and frozen (W6a not built). 5 seeds, ~40 states each. The probe agent's residue field is the one at the end of the probe run.

## RESULTS (2026-09-25T22:11Z; full tables in `probes/n3/results/SUMMARY.txt`, raw `N3_s53{1..5}.json` / `.log`)

### Run log (resources only; `results/decisions.log`)
- The Mac probe lock was held by `bt0925-spcem2` from 20:50Z to 21:27Z, so this probe waited. Then: smoke s530 (attempt 1 crashed on the BLIND guard; attempt 2 passed), pre-registration commit at 21:32Z, and seeds 531-535 one per lock hold from 21:45Z to 22:10Z (4.2-6.7 min each).
- Available memory was 1,754-2,078 MB at each start, with no waits. Every seed gave 40-43 probe states, so the re-run rule never fired. Nothing else changed.

### Preconditions (all hold)

| seed | REAL disc4 / k (TE4) | REAL disc5 (TEW) | SHUF disc4 / disc5 | BLIND disc4 (tie-fair disc5) | BLINDR disc4 | REAL t1 / t30 / true norm | BLINDR t30 | INIT t30 |
|---|---|---|---|---|---|---|---|---|
| 531 | **0.510 / 10** | 0.396 | 0.187 / 0.151 | 0.213 (0.200) | 0.207 | 0.39 / 0.63 / 0.34 | 8.4 | 117 |
| 532 | **0.467** / 10 (miss) | 0.385 | 0.163 / 0.154 | 0.283 (0.200) | 0.283 | 0.40 / 0.49 / 0.38 | 6.0 | 1033 |
| 533 | **0.483 / 10** | 0.374 | 0.147 / 0.113 | 0.243 (0.200) | 0.307 | 0.48 / 0.55 / 0.46 | 32.6 | 205 |
| 534 | **0.473 / 10** | 0.292 | 0.227 / 0.149 | 0.227 (0.200) | 0.227 | 0.36 / 0.43 / 0.34 | 13.7 | 154 |
| 535 | **0.477 / 10** | 0.476 | 0.170 / 0.157 | 0.247 (0.200) | 0.303 | 0.42 / 0.49 / 0.40 | 21.9 | 432 |

- **W3 head L2R bar: 4/5.** Only s532 misses, at 0.467 against the 0.47 bar (the W3 gate's own s108 missed at 0.460). Under the pre-registered rule this is not CANNOT_DETERMINE; s532 is named, and a sensitivity reading without it is given below. The member guard PASSed for REAL and SHUF on 5/5 seeds.
- **Twin at chance: 5/5.** It is below chance (disc4 0.147-0.227), i.e. anti-mapped, as in the W3 gate.
- **BLIND is exactly action-blind.** Its `world_action_encoder.weight` is byte-identical to init on 5/5 seeds, its tie-fair disc5 is exactly 0.200, and it is trained and bounded (t30 0.41-0.61).
- **BLINDR** is action-uninformative (disc4 0.207-0.307) but diverges moderately (t30 6-33, true norm ~0.4). That is far below INIT (117-1033), but it is not bounded.
- **Canaries, 5/5 seeds:**
  - cloned-env validation max |diff| 0.0 (40-43 states validated);
  - depth decomposition 0.0;
  - batched-vs-single scorer at most 8.5e-8 relative;
  - I1 `canary_e3_structure` and `canary_action_discrimination` reproduced.
- **Behaviour, for context:** post-phase actions stay concentrated (modal class 57-92%). Native pools carry a median of 3-4 distinct first-action classes.

### Gates per aggregation (REAL / SHUF, with REAL minus SHUF)

| agg | (a) Spearman diff > 0.15 | (c) flip vs BLINDR, diff > 0.15 | (b) pick in env-Q-best, report only | habit-pick agreement | SD-081 |
|---|---|---|---|---|---|
| D1 | 4/5 (+0.74 / +0.61 / +0.11 / +1.00 / +0.70) | 0/5 (-0.21 to +0.03) | 5/5 | 1.00 (by definition) | **incompatible** (reference only) |
| **DISC_0.5** | **4/5** (+0.75 / +0.57 / +0.10 / +0.95 / +0.23); REAL 0.50 / 0.31 / 0.11 / 0.49 / -0.01 vs SHUF -0.24 / -0.26 / 0.02 / -0.47 / -0.24 | **0/5** (-0.20 / +0.02 / +0.07 / +0.10 / -0.05); REAL 0.59-1.00, SHUF 0.79-0.98 | 5/5 (REAL 0.21-0.33 vs SHUF 0.02-0.07; chance 0.20) | 0.35-0.60 (not degenerate) | compatible |
| DISC_0.8 | 4/5 (+0.76 / +0.19 / -0.05 / +0.94 / +0.25) | 1/5 (s534 +0.24) | 4/5 | 0.07-0.28 | compatible |
| FIDW | 3/5 | 0/5 | 1/5 | 0.02-0.10 | compatible (REAL weights depths 2-21..30 on 5/5) |
| FULL | 3/5 (s532 -0.91: REAL anti-tracks) | 1/5 (s533 +0.17) | 1/5 | 0.05-0.14 | compatible |

- **The gate (c) reference rule fired as pre-registered.** BLIND was degenerate (all 32 candidates tied) on 100% of states on 5/5 seeds, and BLINDR on 0%, so (c) was read against BLINDR on every seed. The plain np.argmin flip rates (index tie-break) agree with the tie-fair ones within 0.05. For reference, flip vs INIT is 0.82-1.00 for both heads under every aggregation, which is N3-pre's non-discriminating reading, reproduced.
- **Sensitivity without s532** (the bar-miss seed): DISC_0.5 (a) is 3/4, (c) 0/4. The verdict is unchanged.
- **Pre-registered verdict: NONE_PASS.** No SD-081-compatible aggregation passes (a) and (c) on >= 4/5 seeds. The simplest (a) passer is DISC_0.5; DISC_0.8 also passes (a).

### Reading (not a gate change)

1. **What the W3 member head buys E3 (D2):**
   - With the real head and DISC_0.5, E3's ranking of the five first actions tracks its own score of the TRUE next state (Spearman 0.31-0.50 on 3/5 seeds; ~0.1 on s533 and s535).
   - With the twin, the ranking anti-tracks (-0.24 to -0.47 on 4/5 seeds).
   - Steep aggregations keep this and deep ones wash it out: FULL anti-tracks on s532 (-0.40). This replicates N3-pre and ADDENDUM 2 Measure 2 with the real member.
   - DISC_0.5's planned pick differs from the habit pick at 40-65% of states, so the SD-081 contrast is real, not nominal.
2. **Gate (c) cannot separate a correctly mapped head from a permuted one.** A pick-flip rate measures whether the head's action map changes E3's choice, not whether the map is right. The fixed-permutation twin has a full, wrong action map, so it flips the pick as often as the real head does, as predicted in premise 4.
   - The strictly action-blind reference is degenerate by construction (premise 2: E3 reads z_world only).
   - Against the action-uninformative BLINDR, both heads flip at 0.6-1.0.
   - The descriptive "toward-better" reading does not separate them either (DISC_0.5 REAL minus SHUF: +0.09 / -0.07 / -0.10 / +0.20 / -0.20), because J_true of the first-action class is a noisy one-step proxy for a 30-step candidate.
   - So (c) as specified is a gate-design defect for this twin. It is not evidence that the head fails to reach E3: (a) already shows reach in the predicted direction.
3. **Gate (b) passes 5/5 for DISC_0.5, but mostly because of the twin.** REAL's pick lands in the env-Q-best set 0.21-0.33 of the time, against chance 0.20 (a small excess on 4/5 seeds). The anti-mapped twin lands there 0.02-0.07, well below chance. REAL minus SHUF > 0.10 therefore does not show grounded choice quality. (b) stays after W5, as decided at 14:19Z.

### Options for the W4 gate owner (the orchestrator decides; none taken here)
- **(i) Re-specify (c) as a contrast against the action-blind head on choice QUALITY, not on flip rate.** For example: under DISC_0.5, "REAL's pick has a better env-grounded outcome than the BLIND reference's tie-fair pick". Reading it by env-Q waits on W5 for the same reason as (b). Reading it by J_true is noisy (reading 2 above).
- **(ii) Drop (c) from W4's member gate and gate W4 on (a) alone.** (a) is the head-vs-twin D2 contrast that aggregation can actually affect. On that reading **DISC_0.5 is selected** (4/5, the simplest compatible aggregation), W4 is buildable now, and the choice-quality check moves to the integrated gate after W5 together with (b).
- **(iii) Keep (c) with a twin that is action-blind rather than permuted.** "Real minus BLIND" flip is then 1 - 1/32 for any head, by construction, so this option only moves the defect.

Recommendation, as analysis and not as a decision: (ii). The plan's own rationale for (c) was to stop "any trained head flips the pick" from passing. Against a matched twin, (a) already does that job: the twin anti-tracks where the real head tracks.

### Domains and limits
- D2 for (a): swapping the head changes the native consumer's ranking, in the predicted direction against cloned-env consequence. (c) is a degenerate or non-discriminating instrument here, not evidence. No D3.
- J_true is E3's own one-step score, so (a) is partly self-consistency. Q is noisy.
- The encoder is random-init and frozen (W6a is not built); world_dim 32; size-12 Phase-0 env; 5 seeds with 40-43 states each.

### Reproduction
- `probes/n3/n3_probe.py` (one seed; it expects a detached ree-v3 worktree @ `042895a` at `/Users/dgolden/REE_Working/.scratch/wt-n3`, and imports `probes/babble` and `probes/rollout` read-only).
- `run_one.sh` (Mac probe lock and memory gate); `summarize_n3.py` produces `results/SUMMARY.txt`.
