# N3 proper: which E3 horizon aggregation tracks true consequence with the REAL W3 member head? (pre-registered probe)

- **STATUS: PRE-REGISTERED (no registered seed has run).** Results will be appended below this pre-registration without editing it; only this status line changes.
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
