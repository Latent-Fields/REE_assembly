# A1 integrated closed-loop acceptance: pre-registration DRAFT v2 (coupled loop-repair campaign)

- **Status: DRAFT v2. The user's decisions on v1 are folded in; A1 is HELD until both variants pass their member gates (rec-20260925-38b81685).** v1 written 2026-09-25 by session `bt0925-a1prereg` (headless design worker, `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-coupled-a1-preregistration-draft`. v2 written 2026-09-25T14:27Z by `bt0925-a1v2`, chip_ref `chip-20260925-coupled-a1-prereg-v2`.
- **Nothing was queued, built or registered.** No queue entry, no `ree_core` edit, no registry edit. A1 cannot queue until W6 (the integrated preset), I1 (the acceptance instruments) and both variants' member gates exist and pass; see sec 1 and sec 7.1.
- **Evidence domain of this document: D0 + one re-analysis.** The design is D0. The absolute floors in sec 6 come from a new re-analysis of existing raw probe data (`probes/a1_draft/floor_grounding.py`). No new agent run was made.
- **Refs at writing:** ree-v3 `origin/main` @ `23714f0562`; `origin/integration/coupled-loop-repair` @ `cc20be5663` (= BR0, no branch commits yet). REE_assembly `origin/master` @ `eecdfe2e4d0`. **v2 re-measure (14:27Z):** ree-v3 `origin/main` @ `1a61800c0c`; the branch is still `cc20be5663`; REE_assembly `origin/master` @ `2ba75b0f60`.
- **Parent:** `coupled_loop_repair_campaign_plan.md` sec 5 (the A1 draft this refines), sec 6 (sequencing, merge gate), sec 9 and "User decisions on this plan". Where this document differs from plan sec 5, the difference is listed in sec 13 with its reason.
- **Skeleton:** `probes/a1_draft/a1_integrated_acceptance_skeleton.py`. It has the arm wiring and I1 call sites, and it implements the whole scoring half (margins, criteria, verdict ladder, head-to-head, NOVAL attribution, the pre-A1 hold). `--selftest` (v2: 29 cases plus 5 mutations) shows that every criterion can FAIL, that every CANNOT_DETERMINE and INVALID branch can be reached, and that each head-to-head, attribution and hold branch gives its pre-registered answer.
  - The two red-team cases (RT-1, RT-2) were mutation-checked. With the pre-red-team rules restored (`>= 0` P1g, no balloon guard), both flip to BAD (sec 15).
- **Red-team: CONTESTED.** An independent sonnet subagent reviewed it read-only. Its findings RT-1 through RT-4 and RT-6 are folded in; RT-5 stays open (sec 15).

## v2 changes (2026-09-25, `bt0925-a1v2`)

**Sources:** the user decisions in `coupled_loop_repair_campaign_plan.md` "User decisions on this plan" (rows through rec-20260925-b9652a9b); the plan's Decision log entry 2026-09-25T14:19Z (`2ba75b0f60`); the action-space design's A1 edits E1-E9 (`action_space_proposals_design_20260925.md` sec 5.2, `412882b845`); probe N3-pre (`n3_pre_e3_aggregation_probe_20260925.md`, `d4bb6449b3`). Skeleton v2: REE_assembly `6d1face27d`.

| # | change | where | source |
|---|---|---|---|
| V1 | Floors **accepted**: reward 0.90 benign / 2.4 trapped, harm contacts 1.6 / 4.8 (per 100 steps; contacts per 600-step window) | sec 0, 6.3, 14 | rec-20260925-5fc6c256 |
| V2 | Benign reward-change (P4) floor **0.92 -> 1.44**, the harm-bearing-seed value (2 x 0.643 x sqrt(1.25)) | sec 6.3, 13, skeleton `FLOORS` | rec-20260925-aa066e96 |
| V3 | P1g (strict `> 0`) **accepted** | sec 0, 8 | rec-20260925-5fc6c256 |
| V4 | **A1 is held until INT-CODEC and INT-ACT both pass their member gates**; they then run head to head on one pinned sha. Option (b) (INT-ACT first under a lettered id) is not taken | sec 0, 7.1, 8.3, 14 | rec-20260925-38b81685 |
| V5 | The two no-valuation arms INT-CODEC-NOVAL and INT-ACT-NOVAL are **required** in GROUNDED mode (no longer optional). They carry a pre-registered attribution readout that never moves a verdict (sec 8.4). In ABSENT mode they are the same as INT-v and are not run | sec 5.1, 8.4, 11 | rec-20260925-c2519d92 |
| V6 | **Consumer-mediated gate leg on both variants.** W1(e) keeps its containment-vs-shuffled check AND gains the G-ASP-style leg (E3's pick in env-Q-best vs today's native pool, > 0.10 on >= 4/5 seeds, E3 and head frozen). G-ASP (e) uses the same leg. Both are pre-A1 gates, not in-run checks | sec 7.1 | rec-20260925-b9652a9b |
| V7 | E1: `INT-ASP` -> **`INT-ACT`** everywhere (also -SHUF, -FROZEN, -R1, -NOVAL). "ASP" stays the name of the mechanism | throughout | design E1 |
| V8 | E2: premise Q5 "gap" -> closed by the design and plan row W1-alt (build not started) | sec 1 | design E2 |
| V9 | E3: INT-ACT's config is spelled out | sec 5.1 | design E3 |
| V10 | E4: the SHUF asymmetry is stated. INT-ACT-SHUF has no codec labels and no `terrain_prior` target to permute, so it destroys strictly less than INT-CODEC-SHUF, and R0 covers fewer groups. Each P3 is against the variant's own SHUF; the head-to-head reads P1b only | sec 5.3, 7 | design E4 |
| V11 | E5: R1 for INT-ACT = G-ASP (b)-(d) in-run; R1 for INT-CODEC = W1 (b)-(d) in-run. Gate (e) of both is pre-A1 | sec 7 | design E5 |
| V12 | E6: **one** CEM elite scoring window for both variants (`CEM_SCORE_WINDOW`); its value is fixed when W4 lands (U4 open) | sec 5.4 | design E6 |
| V13 | E7: **one** W3 buffer action format for both variants: the executed vector as fed to E2 | sec 5.4 | design E7 |
| V14 | E8: "proposal m4" is kept for INT-CODEC only. Both variants report the E3-picked class modal share over probe states | sec 6.1 | design E8 |
| V15 | E9: the tie-rule wording no longer says ASP "deletes the codec". It removes the decoder and `terrain_prior` from the act path; they stay constructed but unused | sec 8.3 | design E9 |
| V16 | R3 is **re-referenced**: W4(c)'s pick-flip is measured against a trained action-blind head, not the untrained init head. W4(b) moves after W5 and is reported in A1, not gated | sec 7, 7.1 | Decision log 14:19Z |
| V17 | Kept unchanged, as the brief requires: the per-variant INT-v-R1 reseed arms and the 3 x floor balloon guard (RT-2) | sec 5.1, 6.2 | red-team |
| V18 | Cost re-estimated with the trainer overhead applied to INT arms only and the NOVAL arms required: **~28 CPU-h (ABSENT) / ~33 CPU-h (GROUNDED)** for 10 admitted seeds, before screen and reserves | sec 11 | this revision |
| V19 | The skeleton is updated to match: arm table, floors, P1g strict flag, parity constants, the `a1_queueable` hold, `attribution`, head-to-head cases. `--selftest`: 29 cases plus 5 mutations, each of which restores one retired rule and must flip its case | skeleton | this revision |
| V20 | **New open item (from N3-pre):** pick-in-Q-best readouts are capped by E3's valuation until W5. That covers W4(b), and also the **consumer-mediated (e) leg that both member gates now carry** (sec 14, O3) | sec 14 | N3-pre `d4bb6449b3` |

## 0. Decisions already taken (implemented here, not reopened)

| decision | effect on A1 | ledger |
|---|---|---|
| Env tie-break ON in every arm | `proximity_approach_magnitude_tiebreak=True` in every arm, calibration arms included | rec-20260925-b4355023 |
| Codec repair AND action-space proposals, in parallel, head-to-head | two tested variants, INT-CODEC and INT-ACT. Each gets its own SHUF and FROZEN controls. Both are scored against the same criteria (sec 8.3) | rec-20260925-6a675285 |
| If V3-EXQ-1105a fails, run A1 without grounded valuation | `valuation_mode` is GROUNDED or ABSENT. It is fixed from C2's verdict before any admitted seed runs (sec 5.2) | rec-20260925-805f605c |
| 5 trapped + 5 benign seeds; margin = 2 x SD of NATIVE vs reseeded-NATIVE deltas, with absolute floors; 3,000 closed-loop steps per arm | locked in (sec 3, 6). The floor values are derived in sec 6 | rec-20260925-7e7e9825 |
| Measured floors (reward 0.90 / 2.4, contacts 1.6 / 4.8) and P1g | accepted; they supersede the plan's draft floors (sec 6.3, sec 8) | rec-20260925-5fc6c256 |
| Benign reward-change floor | 1.44 (harm-bearing-seed value), not 0.92 (sec 6.3) | rec-20260925-aa066e96 |
| Action-space proposals have no build or gate yet | **hold A1 until both variants pass their member gates**; then run them head to head (sec 7.1, 8.3) | rec-20260925-38b81685 |
| No-valuation diagnostic arms | **added**: INT-CODEC-NOVAL and INT-ACT-NOVAL in GROUNDED mode, with an attribution readout (sec 5.1, 8.4) | rec-20260925-c2519d92 |
| Gate parity between the variants (design U1) | the consumer-mediated leg is added to BOTH gates: W1(e) keeps containment-vs-shuffled and gains it; G-ASP (e) uses it (sec 7.1) | rec-20260925-b9652a9b |
| W4 gate definitions after N3-pre (orchestrator, standing delegation rec-20260924-fb429c72) | W4(c) re-referenced to a trained action-blind head (R3); W4(b) moved after W5 (reported in A1); DISC_0.5 is N3 proper's lead aggregation | plan Decision log 2026-09-25T14:19Z (`2ba75b0f60`) |

## 1. Premises re-measured

| # | premise (from the brief or plan) | re-measured 2026-09-25T12:35Z | verdict |
|---|---|---|---|
| Q1 | V3-EXQ-1105a is queued at `e00d95da6a` (C2) | on `origin/main`: commit `e00d95d` is present, and the queue item `V3-EXQ-1105a` is `pending`, affinity `any`, 305 min. There is no manifest yet. | holds. C2 has not run, so `valuation_mode` is still undetermined |
| Q2 | I1 instruments are being built in `experiments/_lib/coupled_acceptance.py` | **not on origin/main.** An uncommitted draft (1,007 lines) sits in `.scratch/wt-i1` (based on `cc20be5`). It includes `classify_stratum`, `write_stratum_sidecar`, `require_stratum_sidecar`, `admit_seeds`, `outcome_decomposition`, `action_discrimination`, `collect_probe_states`, `e3_depth_structure`, `head_swap_flip_rate`, `cem_codec_trace`, `codec_roundtrip_accuracy`, and a canary for each. Read, not edited. | **corrected.** The skeleton cites that draft's names as a guide only. Re-read it on origin when porting |
| Q3 | N0 is answered: workers fetch `integration/*` heads through their runner pull | plan row N0 (D1, 11:40Z): all 3 runner workers fetch `+refs/heads/*` | holds, **for heads only.** A pinned sha that a rebase or force-push later removes from every head is not fetched (sec 10) |
| Q4 | Workers can pin `ree_core` to a branch sha | `experiments/_lib/substrate_pin.py` (main): `pin_ree_core(ref)` runs `git rev-parse --verify <ref>^{commit}` and hard-fails when the ref is unresolved. `verify_pin` has a structural check and a marker check | holds |
| Q5 | "The ASP variant has a build path" | v1: **no status-table row existed** for action-space proposals. v2 (14:27Z): plan row `W1-alt` exists (`not-started`), and the member gate G-ASP (a)-(f) is defined in `action_space_proposals_design_20260925.md` sec 4 (`412882b845`) | **closed by the design (`412882b845`) and plan row W1-alt (build not started).** A1 still waits for the W1-alt build and its gate (sec 7.1) |
| Q6 | The env's seed is independent of the agent's seed | `CausalGridWorldV2` draws only from `self._rng = np.random.default_rng(seed)` (`causal_grid_world.py:1604` @ `23714f0562`); a grep finds no global `np.random.` call. The probe harnesses call `seed_all(seed)` once and pass the same `seed` to the env (`probes/rollout/rollout_fidelity_probe.py` `build_B`) | holds for the env. **The A1 harness must split the two seeds** (sec 3). The existing harness pattern does not |
| Q7 | "Env reward" measures grounded outcome | per-step reward is the env's `harm_signal`. With tie-break ON, that includes **approach shaping**: +`proximity_benefit_scale` (0.03) x resource-field on `benefit_approach` steps (`:2733-2745`, `:340`), and -0.05 x hazard-field on `hazard_approach` steps. Consumption is +0.3 (`resource_benefit`, `:275`, `:2367`); hazard contact is -0.5 (`:273`, `:2627-2635`). Resources do not respawn (`resource_respawn_on_consume=False`, `:336`), so consumption reward is capped at 3 x 0.3 per 200-step episode (0.45 per 100). In the T2 regime (tie-break ON), seed 64's native arm spent 112 of 1,500 steps on `benefit_approach` | **corrected.** Raw env reward can rise from hovering in resource fields without consuming anything, which K5/V2 excludes. A grounded-component criterion P1g is added (sec 8) |
| Q8 | Plan sec 5 floors (reward 0.25 / 1.0 per 100; contacts 1.0; FIRST->LAST change 0.25) are adequate | re-derived from measured replicate spread (sec 6). The benign reward floor is 0.90 (plan: 0.25); the FIRST->LAST floor is 0.92 pooled (plan: 0.25), **1.44 in v2** by user decision. **The plan's P4 floor sat at 0.3 x the measured replicate noise** | **corrected** (sec 6); the floors are user-accepted in v2 |
| Q9 (v2) | C2 has not run yet (Q1) | 14:27Z, on `origin/main` @ `1a61800c0c`: queue item `V3-EXQ-1105a` is `claimed` (running). There is no manifest yet | holds. `valuation_mode` is still undetermined |
| Q10 (v2) | I1 is not on main (Q2) | `experiments/_lib/coupled_acceptance.py` is absent from `origin/main` @ `1a61800c0c`. Plan row I1: built and contracts green, awaiting its commit | holds. The skeleton's I1 names remain a guide |
| Q11 (v2) | The branch has no commits beyond BR0 | `git ls-remote`: `integration/coupled-loop-repair` = `cc20be5663` | holds. No W-member has landed, so no gate can be read yet |

## 2. The question and the domain

- **Question:** does the integrated loop close? Take the W6 preset (trainer ON, every group guard-green) with either proposal variant. Does it (a) earn more grounded env reward than NATIVE on benign starts, (b) without doing worse on hazard-trapped starts and without more true harm contacts, (c) only when its grounding targets are real, and (d) because it learns during waking?
- **Domain if valid: D3.** This is closed-loop env reward under a real policy difference, with shuffled and frozen controls. A PASS certifies the integrated preset in this one regime. It does not certify any member alone (plan sec 3).
- **Debt class:** `complex (probe-gated)`. The run is the probe (plan row A1).

## 3. Regime, seeds and strata

- **Env:** `CausalGridWorldV2(size=8, num_hazards=2, num_resources=3, max_episode_steps=200, proximity_approach_magnitude_tiebreak=True)`. `world_dim` 32 (the deployed value). The Phase-0 env (size 12) is reported as a secondary regime and has no criterion.
- **Env seed vs agent seed.** Every arm uses `env_seed = s`.
  - NATIVE and every INT-* arm use `agent_seed = s`.
  - NATIVE-Rk uses `agent_seed = s + 10,000 x k`, k = 1..3.
  - The env is constructed with `seed=s` BEFORE the agent RNG is seeded (Q6).
  - **Caveat:** an INT-* agent constructs extra modules, so its initial weights differ from NATIVE's even at the same agent seed. Matching agent seeds removes the shared part of the init noise. It does not make NATIVE and INT bit-comparable.
- **Seed range:** 301 upward, screened in ascending order. It is disjoint from 42-200, from 1105's 111-200 and from 1105a's 201-290.
- **Stratum** (plan sec 5; implemented by I1-5 `classify_stratum`):
  - A seed is `hazard_trapped` iff NATIVE has >= 10 episodes that terminate with length < 200 steps within its closed-loop steps 0-599. Otherwise it is `benign`.
  - An episode still running at step 600 does not count.
  - The classification uses NATIVE **alone**. It is written to the sidecar (`write_stratum_sidecar`, write-once) before NATIVE's step 600 and before any other arm starts.
  - Every other arm calls `require_stratum_sidecar` before its first step. If the sidecar is missing, the arm raises.
- **Admission:** the first 5 benign and the first 5 trapped seeds in screen order, plus 2 reserves per stratum (sec 9).
  - Screen ceiling: 80 seeds.
  - Expected screen length: at the measured trapped rate of 0.21 (4 of 19; `probes/nulldet2/results/SCREEN_log.json`), 7 trapped seeds (5 + 2 reserves) need about 33 screened seeds.
- **Stratum source of truth:** the in-run NATIVE classification, not the screen (sec 9, cross-machine rule).

## 4. Phases (per arm, identical lengths in every arm)

1. **Developmental epoch, 2,400 steps (DRAFT: plan's number, not grounded; see sec 13).** INT-* arms run the W2a structured babbling generator. NATIVE and NATIVE-Rk run unscored native waking steps.
2. **Encoder warmup, identical protocol in every arm.** The SD-070 P0 warmup budget of the rollout records is 20 episodes x 50 steps, preservation 1,000 (`r5b_r2_fresh_seed_replication_20260924.md`). DRAFT until W6a fixes how the encoder is trained through the read path.
3. **Closed loop, 3,000 steps** (accepted). FIRST = closed-loop steps 0-599. LAST = steps 2,400-2,999.
   - INT-*-FROZEN: trainer OFF from the start of phase 3. **Plan sec 5 said "after warmup", which is ambiguous; this draft reads it as "from the first closed-loop step".** FROZEN therefore keeps everything learned in phases 1-2, and P4 isolates learning during the closed loop.
- Per step, record: env reward, `transition_type` (I1-6 `step_outcome`), done flag, executed action class, and in INT arms the trainer group losses.

## 5. Arms

### 5.1 Arm table (execution order within a seed)

| arm | agent seed | config | trainer | scored? | role |
|---|---|---|---|---|---|
| NATIVE | s | all flags off, pinned `ree_core` | - | yes | comparator; **stratum source** |
| NATIVE-R1..R3 | s + 10k x k | as NATIVE | - | **no** | margin calibration only (sec 6) |
| INT-CODEC | s | W6 preset, codec variant (W1), `valuation_mode` | ON | yes | tested |
| INT-CODEC-SHUF | s | as INT-CODEC; every grounding target permuted (5.3) | ON | yes | grounding control (P3) |
| INT-CODEC-FROZEN | s | as INT-CODEC | OFF in phase 3 | yes | learning control (P4) |
| INT-CODEC-R1 | s + 10k | as INT-CODEC | ON | **no** | INT-vs-INT margin calibration only (RT-2) |
| INT-CODEC-NOVAL (GROUNDED mode only) | s | INT-CODEC with valuation ABSENT | ON | **no** | attribution only (sec 8.4) |
| INT-ACT | s | W6 preset + `use_action_space_proposals=True`, `action_space_first_action_mode="stratified"`, `action_space_cem_score_horizon` = `CEM_SCORE_WINDOW` (sec 5.4); codec and prior members NOT registered; `use_action_class_scaffold_candidates=False` asserted; `valuation_mode` | ON | yes | tested |
| INT-ACT-SHUF, -FROZEN, -R1 | s (R1: s + 10k) | as INT-ACT (SHUF per 5.3) | as the CODEC rows | as the CODEC rows | as the CODEC rows |
| INT-ACT-NOVAL (GROUNDED mode only) | s | INT-ACT with valuation ABSENT | ON | **no** | attribution only (sec 8.4) |

That is **12 arms per seed in ABSENT mode and 14 in GROUNDED mode.** v2: the NOVAL arms are required in GROUNDED mode (rec-20260925-c2519d92). In ABSENT mode INT-v already runs without valuation, so INT-v-NOVAL would be the same arm and is not run.

- **Order within a seed:** NATIVE, NATIVE-R1..R3, then the INT-CODEC set, then the INT-ACT set.
- **Why INT-ACT does not register the codec members.** INT-ACT keeps `action_object_decoder` and `terrain_prior` constructed but off the act path. No optimizer holds them, so the guard does not check them (design sec 3.5). Registering them would train modules that nothing reads.

### 5.2 `valuation_mode` (the with/without-valuation variant)

- **GROUNDED** iff C2 (V3-EXQ-1105a) returns PASS AND the W5a battery returns PASS AND W5b is in the W6 preset. Otherwise **ABSENT** (rec-20260925-805f605c).
- It is fixed and written into the queue entry **before any admitted seed runs**. One A1 run has exactly one mode. A mode change is a new lettered id.
- In ABSENT mode:
  - R4 (sec 7) is dropped;
  - the manifest records `valuation_uncalibrated: true`, and any P1 gain is reported as an uncalibrated reward gain (the user's wording);
  - **P2 on benign seeds is expected to fail.** Plan sec 9.4 cites three independent tests for this. It is stated as a prior and is not used to relax P2.

### 5.3 The SHUF construction (P3 control)

- In INT-v-SHUF, every grounding target is permuted across timesteps inside a rolling buffer, with class marginals kept:
  - the harm_eval and benefit_eval targets;
  - the grounded-valuation outcome stream (GROUNDED mode);
  - the `terrain_prior`'s grounded target (CODEC);
  - the codec decode labels (CODEC);
  - the action labels in the E2-world buffer, babbling replay included.
- Inputs, architecture, learning rates and trainer schedule are unchanged.
- **The two SHUF controls are asymmetric (E4), and that is stated here rather than hidden.**
  - INT-ACT has **no** codec decode labels and **no** `terrain_prior` target, so INT-ACT-SHUF permutes only the harm_eval and benefit_eval targets, the valuation stream (GROUNDED) and the E2-world action labels, babbling included. It destroys strictly less than INT-CODEC-SHUF.
  - For the same reason, R0 (the guard) covers fewer groups in INT-ACT than in INT-CODEC.
  - Each variant's P3 is against **its own** SHUF, so each test is internally fair. The head-to-head (8.3) reads P1b only, which does not involve SHUF, so the asymmetry does not tilt it.
  - The per-variant list is pinned in the skeleton as `SHUF_TARGETS`.
- **The permutation seed is `s + 7`**, drawn from a private generator, so SHUF does not consume the agent's RNG stream differently from INT beyond what the targets themselves cause.
- **Self-supply check (red-team Q2: OK).** SHUF must not supply its own asserted value. Two checks enforce this:
  - R2 requires SHUF's E2 head to FAIL the W3(a) disc bar, which shows the shuffle destroyed the label information;
  - SHUF's `outcome_decomposition` is computed by the same I1 function on the env's own `transition_type` stream, never on the permuted labels.

### 5.4 Parity between the two variants (v2: design edits E6, E7)

These are fixed once for both variants, so the head-to-head compares the proposal mechanism and nothing else.

- **One CEM elite scoring window (E6).**
  - INT-ACT's `action_space_cem_score_horizon` and INT-CODEC's CEM elite scorer (`HippocampalModule._score_trajectory`, `module.py:1691`) use the **same** window, `CEM_SCORE_WINDOW`.
  - Today the codec CEM has only a mode-conditioned `max_horizon` (`module.py:2180-2191`). The W1 build must therefore expose the same window argument.
  - The value is either the full horizon for both (today's behaviour, the skeleton's DRAFT default) or W4's chosen aggregation for both. If W4 selects a discount rather than a depth (N3 proper's lead candidate is DISC_0.5), "the same window" means both CEM scorers apply that same aggregation.
  - The choice is design decision U4, which is still open (sec 14). It is fixed in the queue entry when W4 lands. Unequal windows are never allowed, because the CEM scorer's deep steps carry no action information (design P7) and would confound the comparison.
- **One W3 buffer action format (E7).**
  - The W3 `E2WorldMember` stores **the executed action vector as fed to E2**, in both variants.
  - For INT-ACT this is an exact one-hot. For INT-CODEC it is the bounded continuous decode (design P4: the codec path executes continuous vectors even after bounded decode).
  - This choice lets the codec's head train on the format it rolls out. The alternative, argmax one-hots in both, would also be fair. The W3 owner may switch to it before the pin, but only for both variants together. Pinned in the skeleton as `W3_BUFFER_ACTION_FORMAT`.
- **Same everything else:** the env and agent seeds, the phase lengths, the developmental epoch (W2a babbling), the warmup protocol, the trainer schedule, `valuation_mode`, and the pinned sha. Both variants are built on the one branch, so one pin carries both (design sec 3.4).

## 6. DVs, margins and absolute floors

### 6.1 DVs (all per 100 steps, per arm, per window)

- **Primary:** env reward in LAST, meaning `100 x sum(harm_signal) / 600`.
- **Grounded component** `G`: the part of LAST's env reward on steps whose `transition_type` is a true contact (`agent_caused_hazard`, `env_caused_hazard`, `env_caused_multisource`) or a consumption (`resource`). It excludes the approach and proximity shaping terms. It is computed from the same per-step reward and the same `transition_type` (I1-6 category sets).
- **Secondary:** true harm contacts in LAST, and the reward change FIRST -> LAST.
- **Reported:** consumptions, proximity steps, `benefit_approach` steps, early terminations, action entropy and class coverage, E2 disc4_h1 / disc5_h1 and k, ARC-016 `running_variance` and commit rate, per-group losses.
  - **v2 (E8):** "proposal m4" is reported for **INT-CODEC only**. For INT-ACT it is degenerate, because the stratified pool has no majority class by construction. Both variants instead report (i) the E3-picked first-action class's modal share across the probe states (G-ASP (f)), and (ii) the refit-mode step-0 TV across states, if refit is ever used.
  - **v2 (Decision log 14:19Z):** W4(b)'s readout, E3's pick in the env-Q-best set (INT-v vs INT-v-SHUF, on the R3 probe states), is **reported for both variants and gates nothing**. It moved after W5 (sec 7.1, sec 14 O3).
  - **v2 (sec 8.4):** the NOVAL attribution label and its two counts (GROUNDED mode).

### 6.2 Margin rule (accepted)

margin(metric, stratum) = max( 2 x RMS of the per-seed deltas NATIVE - NATIVE-Rk, pooled over that stratum's admitted seeds ; floor(metric, stratum) ).

- The RMS form matches the 1105 detector's leave-one-out SD.
- A margin is CANNOT_DETERMINE when any admitted seed has fewer than 2 completed NATIVE-Rk arms, or the stratum has fewer than 8 deltas.
- **Superiority vs non-inferiority (RT-2).**
  - **Superiority criteria** (P1b, P3, P4) use max(the NATIVE margin above, 2 x RMS of the per-seed INT-v minus INT-v-R1 deltas). The INT-v-R1 arm measures INT-vs-INT noise directly, so a noisier tested preset cannot pass on NATIVE's smaller noise. The INT margin is CANNOT_DETERMINE when a stratum has fewer than 4 INT reseed deltas.
  - **Non-inferiority criteria** (P1t, P2) use the NATIVE margin alone. A large margin makes them lenient, so there is a **balloon guard**: if the sampled 2 x RMS exceeds 3 x its floor for the trapped reward, benign contacts or trapped contacts, the verdict is `CANNOT_DETERMINE: margin_ballooned`. The non-inferiority test is then unfalsifiable at that noise, and it is never read as PASS. The factor 3 is a DRAFT constant.

### 6.3 Absolute floors: derivation and provenance

- **Rule.** floor = 2 x the RMS of **within-seed near-NATIVE replicate deltas**, measured on the closest existing data. The margin rule is thus applied to the best prior noise estimate.
- **Window correction.** Reward in the source is measured over 750-step halves, and A1's windows are 600 steps. Reward floors are scaled by sqrt(750/600) = 1.118, assuming rate variance scales as 1/T.
- **Contact counts** are recomputed exactly on 600-step windows from the per-step `transition_type` stream, so they need no correction.
- **Source data:**
  - grounded-valuation null-detector runs v1 (benign seeds 61-65) and v2 (trapped seeds 66 and 69), T2 regime, **tie-break ON**, 1,500 steps;
  - replicates: the native arm M0 vs NULL0-NULL4. The NULL arms share M0's env seed and agent init. They differ only by a matched-step random walk in the 4 channel weights. Per P-2 of that record, any weight perturbation makes the closed-loop trajectory diverge;
  - record: `grounded_valuation_null_detector_20260925.md`, v1 results and the v2 addendum;
  - raw per-seed JSONs (scratch-only, 3.8 MB, cited by sha1): `NULLDET_s61..65.json` (c93a848e, 16bff5f2, 8fa8b6ef, e4169964, 5e8241b3) and `NULLDET2_s66.json` d701adcd, `NULLDET2_s69.json` 3a2b28ab, under `.scratch/breakthrough-20260924/nulldet{,2}/results/`;
  - analysis: `probes/a1_draft/floor_grounding.py`, with output `floor_grounding.{json,out}` committed alongside.

| metric (per 100) | stratum | measured RMS(NULLj - M0) | n deltas (nonzero) | 2 x RMS | window corr. | **floor** | plan sec 5 draft |
|---|---|---|---|---|---|---|---|
| reward, LAST | benign | **0.403 on the harm-bearing seeds 64-65** (pooled over all 5: 0.257) | 10 (10) (pooled: 25 (15)) | 0.807 (pooled: 0.514) | x1.118 | **0.90** (RT-3; pooled would be 0.57) | 0.25 |
| reward, LAST | trapped | 1.056 (half2) | 10 (10) | 2.112 | x1.118 | **2.4** | 1.0 |
| true contacts, LAST 600 | benign | 0.808 | 25 (10) | 1.617 | none (exact 600) | **1.6** | 1.0 |
| true contacts, LAST 600 | trapped | 2.385 | 10 (9) | 4.769 | none | **4.8** | 1.0 |
| reward change FIRST -> LAST (P4) | benign | **0.643 on the harm-bearing seeds 64-65** (pooled over all 5: 0.411) | 10 (10) (pooled: 25 (15)) | 1.286 (pooled: 0.822) | x1.118 | **1.44** (v2, user rec-20260925-aa066e96; v1 used the pooled 0.92) | 0.25 |

- **Which estimate each floor uses (RT-3).** Superiority floors (reward, reward change) should err large, and non-inferiority floors (contacts) should err small.
  - The benign reward floor is therefore taken from the harm-bearing seeds 64-65 only. On seeds 61-63, every NULL replicate reproduced M0 exactly, so pooling them in shrinks the SD artificially.
  - The contacts floor keeps the pooled value (the conservative direction for P2).
  - The P4 change floor: v1 kept the pooled value (0.92 after RT-4's arithmetic fix). **v2 uses the harm-bearing value, 1.44** (user decision rec-20260925-aa066e96), for the same reason as the reward floor: seeds 61-63 reproduced M0 exactly and shrink the pooled SD.
- **The doc's claim that these are lower-bound noise estimates, and its basis (asserted, not shown; RT-5 open):**
  - (i) a matched-step weight walk perturbs less than a full agent reseed, which also changes the initial weights of every module;
  - (ii) 10 of the 25 benign deltas came from seeds 61-63, where every NULL replicate reproduced M0 exactly. Over the two harm-bearing benign seeds alone (64, 65), 2 x RMS is 0.81 for reward (0.90 after window correction) and 2.56 for contacts;
  - (iii) the benign population in the v2 screen (early terminations 0-8 per 600 steps, 12 of 15 seeds with >= 3) looks more like seeds 64-65 than 61-63.
  - **Expected consequence:** the runtime 2 x SD will probably exceed the floors in the benign stratum. The floors bind mainly when a stratum's reseeds happen to coincide (a degenerate SD), and preventing that is their purpose. RT-5 notes that this ordering is argued, not measured. A floor that is itself an underestimate binds exactly when it is most needed. The INT-reseed term (6.2) and the balloon guard are the partial mitigations.
- **Why they are not the NATIVE regime.** The T2 agent carried the R5b scaffold, the COV head, R2 depth 2 and trained evaluators. It was not NATIVE. There is no measurement of NATIVE-vs-reseeded-NATIVE spread with tie-break ON in any record (`r5b_r2_fresh_seed_replication` is tie-break OFF, and its arms differ in configuration, not in seed). **DRAFT flag:** the floors are grounded in the nearest measured analog, not in the target quantity. The runtime 2 x SD term measures the target quantity directly, and that term dominates wherever the reseeds actually vary.
- **Floors not derived:**
  - consumptions (reported only). Measured 2 x RMS is 0.74 benign and 0.89 trapped;
  - the trapped reward change (P4 is benign-only).

### 6.4 Can P1b pass? (headroom, stated before the run)

- In the v2 screen, benign NATIVE-analog reward over the first 600 steps averaged -0.49 per 100 (between-seed SD 0.43, n = 15).
- Consumption reward is capped at 0.45 per 100 (Q7).
- Beating NATIVE by > 0.90 on a benign seed therefore needs roughly: most of the harm removed, plus added consumption. Shaping alone cannot pass, because P1g is strict.
- That is reachable, but it is not slack. P1g stops the approach shaping part from carrying the gain alone.
- **A P1b FAIL with P1g, P2 and P3 all holding is a "gain too small for the margin" outcome.** The autopsy reports it as such. It is not "the loop did not close".

**Can P4 pass at 1.44? (v2 headroom, D0 arithmetic on measured numbers)**
- P4 needs INT-v's FIRST -> LAST reward change to beat INT-v-FROZEN's by more than 1.44 per 100 on >= 4/5 benign seeds.
- The benign reward range is narrow:
  - a NATIVE-analog FIRST window averages -0.49 per 100 (sec 6.4 above);
  - with zero harm, the best benign LAST is about +0.45 (consumption cap, Q7) plus approach shaping. Shaping was measured at up to about 0.2 per 100: seed 64 spent 112 of 1,500 steps on `benefit_approach`, at 0.03 x field <= 0.03 each.
  - A seed that starts at NATIVE's level and ends harm-free with full consumption therefore changes by about 0.94-1.2.
- **So P4 at 1.44 is reachable only if** (i) INT-v's FIRST window is below NATIVE's (the trainer-ON agent starts worse and learns out of it), (ii) FROZEN's change is negative, or (iii) shaping contributes well beyond the measured analog. Note that P1g does not guard P4.
- **Consequence, fixed now:** a FAIL whose only missing criterion is P4, with the FIRST windows near NATIVE's, is reported as **"P4 headroom-limited"** alongside the named signature "architecture helps, waking learning does not". It is not read as evidence that waking learning is absent. This does not relax P4. The floor is the user's decision. The risk is recorded as open item O6 (sec 14).

## 7. Preconditions (INVALID: fix, re-run under a lettered id, never scored as FAIL)

Each is checked per admitted seed, per tested variant v. A failure on any admitted seed makes variant v INVALID.

| id | check | instrument |
|---|---|---|
| R0 | every trainer group's guard verdict is PASS; none is CANNOT_DETERMINE (Q4d). **v2 (E4):** INT-ACT registers no codec or prior group, so its R0 covers fewer groups than INT-CODEC's. For INT-ACT, G5 LEAK must also report **no** gradient into `action_object_decoder` or `terrain_prior` | C0 grad-reach guard (`ree_core/utils/grad_reach_guard.py`), trainer ON |
| R1 | **INT-CODEC:** W1 gates (b) round trip >= 0.95 per class; (c) median decoded norm in [0.5, 2] x one-hot norm over 3 CEM iterations, no growth; (d) iteration-0 O-norm in [0.5, 2] x encoder-image median. **INT-ACT (v2, E5):** G-ASP (b), (c), (d) of `action_space_proposals_design_20260925.md` sec 4, checked in-run from the propose diagnostics: every candidate action an exact one-hot at every step, `action_space_decoder_calls` = 0, `action_space_max_action_norm` = 1.0; median `world_states` norm at t = H within [0.5, 2] x the t = 0 norm with no per-step growth > 1.05; every class in >= 0.99 of final pools at the stratified counts. **Parity:** both variants check only (b)-(d) in-run. Gate (e) of both is a pre-A1 member-gate precondition (7.1), not an in-run R-check | CODEC: I1-4 `cem_codec_trace`, `codec_ranges`, `codec_roundtrip_accuracy`. ACT: the ASP propose trace (I1, to be built; design sec 6 row 13) |
| R2 | at the end of the run, INT-v's E2 world head meets W3(a) (disc4_h1 >= 0.47 and k = 10) on the held-out uniform-random set, **and INT-v-SHUF's head does not** | I1-1 `action_discrimination` |
| R3 | W4(c), **re-referenced in v2** (plan Decision log 14:19Z): on >= 20 cloned-env probe states, [pick-flip rate of INT-v's real head vs a **trained action-blind head**] minus [the same for INT-v-SHUF's head] > 0.15. The action-blind head uses the same recipe with the action input zeroed; the A1 script trains it at run end on INT-v's own W3 buffer (DRAFT placement). The untrained init head is no longer the reference, because its rollouts blow up (t30 norm 238-940 in N3-pre), so any trained head flips the pick | I1-2 `collect_probe_states`, I1-3 `head_swap_flip_rate` |
| R4 | GROUNDED only: the 1105a primary detector D_N is silent on INT-v | 1105a scorer |
| R5 | liveness: every group's held-out loss at LAST is below INT-v-FROZEN's (reported per group) | trainer telemetry |
| R6 | provenance: `verify_pin` passes (structural + marker), and the executed `ree_core` sha equals the pre-registered 40-hex sha | `substrate_pin.verify_pin`, `pin_manifest_block` |
| R7 | instrument sanity: no I1 instrument used in scoring returns CANNOT_DETERMINE on a scored arm (e.g. an unknown `transition_type` in `outcome_decomposition`) | I1 verdict fields |

### 7.1 Pre-A1 member gates: the hold (v2; not in-run, never scored)

A1 is **held** until every gate below has a recorded PASS on the branch sha that A1 will pin (user decision rec-20260925-38b81685). The skeleton's `a1_queueable` implements the hold; a missing or failed gate returns `HOLD` and names the gate.

| group | gates | source |
|---|---|---|
| shared | C2 verdict recorded (it fixes `valuation_mode`); I1 on main; W3 L2R bar; **W4 (a)** (Spearman margin over the shuffled head) and **W4 (c) re-referenced** (vs a trained action-blind head); W6 guard-green; N0 (done) | plan sec 3, Decision log 14:19Z |
| INT-CODEC | W1 (a) guard, (b) round trip, (c) decoded norm, (d) iteration-0 range, **(e) containment-vs-shuffled AND (e) consumer-mediated** | plan W1; user decision rec-20260925-b9652a9b |
| INT-ACT | G-ASP (a) guard / no leak, (b) valid one-hots, (c) bounded rollouts, (d) coverage, **(e) consumer-mediated**, (f) not state-invariant (creditable only with (e)) | design sec 4 |

- **The consumer-mediated (e) leg, identical for both variants** (rec-20260925-b9652a9b): on >= 20 cloned-env probe states per seed, 5 seeds, the A1 env, with the W3 head and E3 under W4's aggregation both frozen and identical across arms, E3's pick from the variant's pool is in the env-Q-best set more often than its pick from today's native pool, by > 0.10 on >= 4/5 seeds. For INT-ACT there is a second leg, (e2): not worse than a random stratified pool.
- **W4 (b) is not in the hold.** It moved after W5 (Decision log 14:19Z), and A1 reports it only (6.1).
- **Open coupling (O3, sec 14):** both variants' consumer-mediated (e) legs are pick-in-Q-best readouts, the same kind of readout as W4 (b). N3-pre found that readout capped by E3's valuation. The hold may therefore not clear until W5 lands, and in ABSENT mode it may never clear.

Every I1 instrument used here also carries its pinned canary (I1 contract tests). The A1 script re-runs the cheap canaries at start: stratum, outcome decomposition, and action discrimination on a label-shuffled toy head at chance. A canary that fails makes the run ERROR before any arm is read.

## 8. Criteria and verdict

">= 4/5" means at least 4 of that stratum's 5 admitted seeds. Each criterion is evaluated separately for each tested variant v. T = INT-v, S = INT-v-SHUF, F = INT-v-FROZEN, N = NATIVE. The margins m are from sec 6.

| id | stratum | statement | kind |
|---|---|---|---|
| **P1b (PRIMARY)** | benign | reward_LAST(T) - reward_LAST(N) > m_reward on >= 4/5 | superiority |
| **P1g** | benign | G_LAST(T) - G_LAST(N) **> 0 (strict)** on >= 4/5. A tie, including 0 = 0 on a seed with no contacts or consumptions in either arm, does NOT hold (RT-1). The gain must include at least one fewer true contact or one more consumption; approach shaping alone cannot carry it (Q7, K5/V2) | strict sign guard |
| P1t | trapped | reward_LAST(N) - reward_LAST(T) <= m_reward on >= 4/5 (gain reported) | non-inferiority |
| P2 | each stratum separately | contacts_LAST(T) - contacts_LAST(N) <= m_contacts on >= 4/5 | non-inferiority |
| P3 | each stratum separately | reward_LAST(T) - reward_LAST(S) > m_reward on >= 4/5 | superiority |
| P4 | benign | [reward_LAST - reward_FIRST](T) - [same](F) > m_change on >= 4/5 | superiority |

**Multiplicity (RT-6).** 2 variants x 8 sub-criteria (P1b, P1g, P1t, P2b, P2t, P3b, P3t, P4) are 16 tests.
- The adopted control is the **conjunction**: a variant passes only if ALL 8 hold, each at >= 4/5 seeds. That family-wise AND is the whole multiplicity control. No alpha is split, and no single criterion is ever reported as a variant PASS.
- The head-to-head adds no test. It only chooses between two variants that each passed the full conjunction.

### 8.1 Verdict ladder (per variant, evaluated in this order)

1. **ERROR**: a canary failed, or the pin could not be verified. It is not a verdict about the loop.
2. **INVALID**: any precondition R0-R7 failed on any admitted seed. Fix and re-run under a lettered id. It is never scored as FAIL.
3. **CANNOT_DETERMINE**:
   - a stratum has fewer than 5 admitted seeds after reserves (`under_admitted:<stratum>`);
   - a margin is not computable (`margin_undetermined:<metric>:<stratum>`), NATIVE or INT;
   - a non-inferiority margin ballooned (`margin_ballooned`, 6.2);
   - the screen ceiling was reached (`screen_exhausted`).
4. **PASS** iff P1b, P1g, P1t, P2 (both strata), P3 (both strata) and P4 all hold.
5. **FAIL** otherwise. Named signatures are reported, not re-scored:
   - P1t holds without P1b: trapped-only gain, the R5b+R2 signature;
   - P1b holds without P1g: the gain is carried by approach shaping;
   - P1b holds without P3: grounding does not matter;
   - P1b holds without P4: the architecture helps, but waking learning does not;
   - P1b fails while P1g, P2 and P3 hold: the gain is too small for the margin (6.4).

### 8.2 The FAIL path

- The branch is not merged.
- `/failure-autopsy` adjudicates the run.
- The per-workstream precondition readouts localise the failing edge.

### 8.3 Head-to-head (codec vs action-space proposals; rec-20260925-6a675285)

- Either variant INVALID -> **A1 INVALID**. The other variant's result is reported but not acted on, because a merge decision needs both arms of the comparison valid.
- Exactly one variant PASS -> **A1 PASS; that variant wins.**
- Both PASS -> the larger mean benign P1b gain wins if the difference exceeds m_reward(benign). Otherwise **ASP wins**, because it is simpler (it deletes the codec). The user may override at merge time.
- Neither PASS -> FAIL if either variant FAILs, CANNOT_DETERMINE if both are CANNOT_DETERMINE.

## 9. Screening, admission and sidecar mechanics

- **Stage S, screen (queued or run before the A1 items, not scored).**
  - For each seed from 301 in order: run NATIVE only, on the pinned sha, through phases 1-2 and closed-loop steps 0-599.
  - Record the stratum with `classify_stratum`, and append `(seed, stratum, machine, sha)` to a screen artifact.
  - Stop when 5 + 2 of each stratum are found, or at 80 seeds.
  - The screen artifact is committed **before** the A1 items are queued, and the A1 queue entry names the 14 seeds.
- **Stage R, per-seed items (one queue item per seed, `machine_affinity` "any").** Each item:
  1. re-runs NATIVE from scratch;
  2. classifies it in-run at step 599;
  3. writes the sidecar (write-once) before step 600;
  4. only then runs the other arms, each of which calls `require_stratum_sidecar` first.
- **Cross-machine rule.** `torch.multinomial` diverges across machine classes (CLAUDE.md, "Running the test suite"), so a screen made on one machine class may classify a seed differently from the in-run NATIVE on another.
  - **The in-run classification is authoritative.**
  - If it differs from the screen, the seed is scored under its in-run stratum, the mismatch is recorded, and admission is re-counted with the reserves.
  - Reserves run under the same pre-registration. Reserve items run only if needed, so the reserves are pre-registered in advance and never chosen after the fact.
  - Admission order is always screen order, never outcome.
- **Why a screen at all:** without one, about 79% of seeds land in the benign stratum, and filling 5 trapped would cost around 24 full per-seed items (10-12 arms each) instead of 24 NATIVE-only screens.

## 10. `substrate_pin` mechanics

- The A1 queue entry carries `substrate_pin = <40-hex sha>`: the `integration/coupled-loop-repair` head at the moment W6 is guard-green. It is **never** a branch name, because the head moves.
- The script calls `pin_ree_core(sha)` before the first `import ree_core`, then `verify_pin` with a marker, i.e. a symbol present on the branch and absent on main. The W6 preset builder is the natural marker; its name is fixed when W6 lands.
- The manifest carries `pin_manifest_block(pin)`, and the fingerprint uses `pin_fingerprint_kwargs`. Pinned cells are never arm-reuse eligible.
- `experiments/*`, `_lib/*` (I1) and `_harness.py` resolve from **main**. Everything A1 needs outside `ree_core` must therefore be on main (plan sec 6), including the babbling generator W2a, which lands MAIN-OFF.
- **Branch freeze (new rule).** From the queue commit until the last A1 item has a manifest:
  - the branch must not be rebased or force-pushed, and gets no commits;
  - N0 showed that workers fetch heads, not arbitrary shas. A rebase would leave the pinned sha reachable from no head, so the pin would hard-fail (ERROR) on any worker that had not already fetched it.
  - Also push the tag `a1/coupled-loop-repair-<date>` at the pinned sha. It survives a later archive (plan sec 6), but it is not relied on for fetch, since runners do not fetch tags explicitly.
- **Merge after PASS:** by merge commit, so the pinned sha stays an ancestor of main (plan M1(c)).

## 11. Cost estimate (DRAFT; `/queue-experiment` re-measures with trainer-ON timing first, per rec-20260925-7e7e9825)

- **Per-step wall** (from the null-detector runs: 8 arms x 1,500 steps plus a ~240 s preamble, on the shared Mac):
  - benign seeds 424-606 s per seed -> about 0.015-0.03 s per step;
  - trapped seeds 2,313-3,117 s -> about 0.18-0.24 s per step, since episode resets and gated ticks dominate there.
- **Trainer overhead:** 0.07x an act tick at K = 1 for the design's members (`native_waking_trainer_design_20260925.md` sec 2). The W6 preset has more members (codec, prior, E2-world, encoder, valuation), so assume 0.2-0.4x on INT arms. DRAFT, ungrounded.
- **Per seed:**
  - about 6.4k steps per arm (2,400 dev + about 1,000 warmup + 3,000 closed loop), x 12 arms (ABSENT) or 14 (GROUNDED + NOVAL; the INT-R1 arms add 2);
  - benign: about 64-77k steps x 0.02 s x 1.2, i.e. roughly 0.5 h;
  - trapped: the same steps x 0.2 s x 1.2, i.e. roughly 4-5 h.
- **10 admitted seeds:** about 3 CPU-h benign + about 26 CPU-h trapped, so **~30 CPU-h (ABSENT) to ~35 CPU-h (GROUNDED + NOVAL)**. Reserves add up to about 40% more if all four are used.
- **Screen:** about 33 NATIVE-only seeds x about 5-10 min = **3-6 h**.
- **Total:** about 35-50 CPU-h. That is at or slightly above plan sec 5's 35-45 CPU-h, and dominated by the trapped seeds.
- Per-seed items on the fleet, affinity "any". A trapped item at about 5 h fits the fleet's item budget but is long enough that `/queue-experiment` should set `estimated_minutes` from the smoke.

## 12. Stop rules

1. **No interim criterion reads.** Criteria are computed once, after every admitted seed's item has a manifest. Strata, preconditions and canaries may be read as they land; reward deltas may not.
2. **INVALID stops scoring.** If any precondition fails on an admitted seed, stop. Do not score that variant; fix under a lettered id. Two or more INVALID seeds for one variant also send the preset back to its member gates before any re-run.
3. **Screen ceiling:** 80 seeds. Hitting it gives `CANNOT_DETERMINE: screen_exhausted` for the under-filled stratum. The ceiling is not raised mid-run.
4. **Reserves:** at most 2 per stratum, used only to replace a seed that became under-admitted (stratum mismatch) or an item that ERRORed for infrastructure reasons, never one that looked bad.
5. **Pre-registration freeze:** a change to the pinned sha, `valuation_mode`, the floors, the windows or the arm set after the first Stage-R item starts makes a new lettered id. The old items are not rescored under the new rules.
6. **Seed reuse:** no admitted seed is reused by a re-run. A lettered re-run screens from the next unused seed.
7. **Branch freeze** (sec 10) for the lifetime of the run.
8. **Wall cap per item:** 2 x the smoke-measured estimate. An item past its cap is ERROR (infrastructure), is replaced by a reserve under rule 4, and is never scored partially.

## 13. Differences from plan sec 5, with reasons

| item | plan sec 5 | this draft | reason |
|---|---|---|---|
| floors | reward 0.25 / 1.0, contacts 1.0, change 0.25 | 0.90 / 2.4, 1.6 / 4.8, 0.92 | derived from measured replicate spread (6.3, RT-3/RT-4). The plan's P4 floor was below the measured noise |
| margins | one NATIVE-reseed margin for every criterion | superiority uses max(NATIVE, INT-reseed); non-inferiority has a balloon guard; INT-v-R1 arms added | RT-2 |
| grounded-component guard | absent | P1g added (strict > 0, RT-1) | env reward includes approach shaping with tie-break ON (Q7). K5/V2 excludes approach steps as evidence of benefit |
| tested arms | one INTEGRATED | INT-CODEC and INT-ASP, each with SHUF and FROZEN | user decision rec-20260925-6a675285 |
| valuation | "R4 only if W5 in preset" | explicit `valuation_mode`, fixed before admission; optional NOVAL diagnostics | user decision rec-20260925-805f605c |
| env/agent seed | not stated | split (sec 3) | NATIVE-Rk must vary the agent only (Q6) |
| screening | "admit the first 5+5" | separate NATIVE-only screen stage + in-run authoritative classification + 2 reserves per stratum | trapped rate 0.21; cross-machine multinomial divergence |
| FROZEN | "trainer OFF after warmup" | trainer OFF for the whole closed-loop phase | makes P4 isolate closed-loop waking learning |
| preconditions | R0-R5 | + R6 (pin provenance), R7 (instrument CD) | a pin failure or a CD instrument must not score |
| stop rules | none | sec 12 | pre-registration discipline |

Unchanged and still ungrounded (DRAFT): the 2,400-step developmental epoch; the warmup budget under W6a; the trainer-ON cost multiplier.

## 14. Decisions left for the user

1. **Floors:** accept the re-derived floors in sec 6.3, or keep the plan's lower drafts. Keeping the drafts makes P1 and P3 easier to pass and P2 and P1t harder to pass wherever the floor binds.
   - Sub-choice: the P4 change floor is 0.92 (pooled) vs 1.44 (harm-bearing seeds only). 1.44 would be consistent with RT-3's treatment of the reward floor.
2. **P1g:** accept the grounded-component sign guard (recommended). The alternative is to score raw env reward alone and let approach shaping count.
3. **ASP build path (Q5):** the head-to-head needs an ASP build row and an ASP member gate (the R1 analog). Until they exist, the options are:
   - (a) hold A1 until both exist; or
   - (b) run A1 with CODEC only and record the head-to-head as not run.
   Neither is recommended here, because the user asked for both in parallel. This is a planning gap for the orchestrator or `/governance` to route.
4. **NOVAL diagnostics** in GROUNDED mode: +2 arms (about +20% cost) in exchange for a reported measure of what valuation contributes. Recommended, because it localises a FAIL.
5. **Head-to-head tie rule:** "ASP wins within margin" (simplicity) vs "the user decides at merge".
6. **INT reseed arms (RT-2, now in the design):** INT-v-R1 per seed adds 2 arms (about +17% cost). The user may remove them. Superiority margins would then fall back to NATIVE noise only, which RT-2 showed can make P1b and P3 too easy.
7. **Balloon factor:** 3 x floor (DRAFT constant).

## 15. Red-team pass

- **Reviewer:** an independent read-only sonnet subagent (a different model from this Opus author). It had the draft, the skeleton, the floor script, the plan, the null-detector record, the I1 draft and the env source on origin/main.
- **Overall verdict: CONTESTED.**
- **Questions judged OK:**
  - Q2: SHUF does not supply its own asserted value;
  - Q3: the stratum classifier is strictly read first, because `write_stratum_sidecar` and `require_stratum_sidecar` hard-raise;
  - Q6: the verdict ladder has no CANNOT_DETERMINE -> PASS path;
  - Q7: every `causal_grid_world.py` citation matches origin/main;
  - the selftest ran 11/11 at review time.

| id | severity | finding | disposition |
|---|---|---|---|
| RT-1 | MAJOR | P1g `>= 0` is vacuous on benign seeds where both arms have 0 contacts and 0 consumptions (seeds 61-63 pattern). A gain carried only by shaping passes | **FIXED.** Strict `> 0`; ties, 0 = 0 included, do not hold. Selftest case added; mutation-checked (the old rule makes it PASS) |
| RT-2 | MAJOR | one NATIVE-reseed margin serves both non-inferiority (P1t, P2) and superiority (P1b, P3). Large noise makes P1t/P2 near-unfalsifiable; INT-vs-INT noise may exceed NATIVE's. The INT reseed arm was only a sec-14 suggestion | **FIXED.** INT-v-R1 arms implemented; superiority uses max(NATIVE, INT) noise; non-inferiority gets the balloon guard (CD, never PASS). Two selftest cases added; the balloon case is mutation-checked |
| RT-3 | MAJOR | the benign reward floor 0.57 was pooled over seeds where 10/25 replicate deltas were exactly zero. The harm-bearing seeds give 0.90 | **FIXED.** Floor 0.90 |
| RT-4 | MINOR | 2 x 0.411 x sqrt(1.25) = 0.919, i.e. 0.92, not 0.90 | **FIXED.** 0.92 (the consistent harm-bearing alternative, 1.44, goes to the user, sec 14) |
| RT-5 | RISK | the floor noise comes from a T2 agent with a 4-channel weight walk, not NATIVE reseeded with tie-break ON; "lower bound" is asserted, not shown; a floor can bind exactly when most needed | **OPEN.** Disclosed in 6.3. Mitigations: the runtime 2 x SD term, the INT reseed term, the balloon guard. Closing it needs a measured NATIVE-reseed spread with tie-break ON. That is a cheap pre-A1 probe (5 seeds x 4 NATIVE agent seeds x 3,000 steps, NATIVE only), which could also serve as the Stage-S screen if run on the pinned sha |
| RT-6 | MINOR | 16 tests with no named multiplicity control | **FIXED.** The AND-of-all-8-per-variant conjunction is stated as the adopted control (sec 8) |

**Unresolved beyond RT-5 (this author's own open items, not raised by the reviewer):**
- the ASP build path (Q5);
- the 2,400-step developmental epoch and the warmup budget under W6a are ungrounded;
- the trainer-ON cost multiplier is ungrounded;
- the balloon factor of 3 is a DRAFT constant.
