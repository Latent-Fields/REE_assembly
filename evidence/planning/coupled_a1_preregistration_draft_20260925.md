# A1 integrated closed-loop acceptance: pre-registration DRAFT (coupled loop-repair campaign)

- **Status: DRAFT for the user to fix (plan sec 9).** Written 2026-09-25 by session `bt0925-a1prereg` (headless design worker, `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-coupled-a1-preregistration-draft`.
- **Nothing was queued, built or registered.** No queue entry, no `ree_core` edit, no registry edit. A1 cannot queue until W6 (the integrated preset) and I1 (the acceptance instruments) exist; see sec 1.
- **Evidence domain of this document: D0 + one re-analysis.** The design is D0. The absolute floors in sec 6 come from a new re-analysis of existing raw probe data (`probes/a1_draft/floor_grounding.py`). No new agent run was made.
- **Refs at writing:** ree-v3 `origin/main` @ `23714f0562`; `origin/integration/coupled-loop-repair` @ `cc20be5663` (= BR0, no branch commits yet). REE_assembly `origin/master` @ `eecdfe2e4d0`.
- **Parent:** `coupled_loop_repair_campaign_plan.md` sec 5 (the A1 draft this refines), sec 6 (sequencing, merge gate), sec 9 and "User decisions on this plan". Where this document differs from plan sec 5, the difference is listed in sec 13 with its reason.
- **Skeleton:** `probes/a1_draft/a1_integrated_acceptance_skeleton.py`. It has the arm wiring and I1 call sites, and it implements the whole scoring half (margins, criteria, verdict ladder, head-to-head). `--selftest` shows that every criterion can FAIL and that every CANNOT_DETERMINE and INVALID branch can be reached.

## 0. Decisions already taken (implemented here, not reopened)

| decision | effect on A1 | ledger |
|---|---|---|
| Env tie-break ON in every arm | `proximity_approach_magnitude_tiebreak=True` in every arm, calibration arms included | rec-20260925-b4355023 |
| Codec repair AND action-space proposals, in parallel, head-to-head | two tested variants, INT-CODEC and INT-ASP. Each gets its own SHUF and FROZEN controls. Both are scored against the same criteria (sec 8.3) | rec-20260925-6a675285 |
| If V3-EXQ-1105a fails, run A1 without grounded valuation | `valuation_mode` is GROUNDED or ABSENT. It is fixed from C2's verdict before any admitted seed runs (sec 5.2) | rec-20260925-805f605c |
| 5 trapped + 5 benign seeds; margin = 2 x SD of NATIVE vs reseeded-NATIVE deltas, with absolute floors; 3,000 closed-loop steps per arm | locked in (sec 3, 6). The floor values are derived in sec 6 | rec-20260925-7e7e9825 |

## 1. Premises re-measured

| # | premise (from the brief or plan) | re-measured 2026-09-25T12:35Z | verdict |
|---|---|---|---|
| Q1 | V3-EXQ-1105a is queued at `e00d95da6a` (C2) | on `origin/main`: commit `e00d95d` is present, and the queue item `V3-EXQ-1105a` is `pending`, affinity `any`, 305 min. There is no manifest yet. | holds. C2 has not run, so `valuation_mode` is still undetermined |
| Q2 | I1 instruments are being built in `experiments/_lib/coupled_acceptance.py` | **not on origin/main.** An uncommitted draft (1,007 lines) sits in `.scratch/wt-i1` (based on `cc20be5`). It includes `classify_stratum`, `write_stratum_sidecar`, `require_stratum_sidecar`, `admit_seeds`, `outcome_decomposition`, `action_discrimination`, `collect_probe_states`, `e3_depth_structure`, `head_swap_flip_rate`, `cem_codec_trace`, `codec_roundtrip_accuracy`, and a canary for each. Read, not edited. | **corrected.** The skeleton cites that draft's names as a guide only. Re-read it on origin when porting |
| Q3 | N0 is answered: workers fetch `integration/*` heads through their runner pull | plan row N0 (D1, 11:40Z): all 3 runner workers fetch `+refs/heads/*` | holds, **for heads only.** A pinned sha that a rebase or force-push later removes from every head is not fetched (sec 10) |
| Q4 | Workers can pin `ree_core` to a branch sha | `experiments/_lib/substrate_pin.py` (main): `pin_ree_core(ref)` runs `git rev-parse --verify <ref>^{commit}` and hard-fails when the ref is unresolved. `verify_pin` has a structural check and a marker check | holds |
| Q5 | "The ASP variant has a build path" | **no status-table row exists** for action-space proposals. Plan sec 2 has W1 (codec) and N4 only, and the user decision is recorded only in the decisions table | **gap.** A1 cannot run INT-ASP until an ASP build row exists and its member gate is defined. Flagged in sec 14 |
| Q6 | The env's seed is independent of the agent's seed | `CausalGridWorldV2` draws only from `self._rng = np.random.default_rng(seed)` (`causal_grid_world.py:1604` @ `23714f0562`); a grep finds no global `np.random.` call. The probe harnesses call `seed_all(seed)` once and pass the same `seed` to the env (`probes/rollout/rollout_fidelity_probe.py` `build_B`) | holds for the env. **The A1 harness must split the two seeds** (sec 3). The existing harness pattern does not |
| Q7 | "Env reward" measures grounded outcome | per-step reward is the env's `harm_signal`. With tie-break ON, that includes **approach shaping**: +`proximity_benefit_scale` (0.03) x resource-field on `benefit_approach` steps (`:2733-2745`, `:340`), and -0.05 x hazard-field on `hazard_approach` steps. Consumption is +0.3 (`resource_benefit`, `:275`, `:2367`); hazard contact is -0.5 (`:273`, `:2627-2635`). Resources do not respawn (`resource_respawn_on_consume=False`, `:336`), so consumption reward is capped at 3 x 0.3 per 200-step episode (0.45 per 100). In the T2 regime (tie-break ON), seed 64's native arm spent 112 of 1,500 steps on `benefit_approach` | **corrected.** Raw env reward can rise from hovering in resource fields without consuming anything, which K5/V2 excludes. A grounded-component criterion P1g is added (sec 8) |
| Q8 | Plan sec 5 floors (reward 0.25 / 1.0 per 100; contacts 1.0; FIRST->LAST change 0.25) are adequate | re-derived from measured replicate spread (sec 6). The benign reward floor is 0.57 (plan: 0.25); the FIRST->LAST floor is 0.90 (plan: 0.25). **The plan's P4 floor sits at 0.3 x the measured replicate noise** | **corrected** (sec 6) |

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
| INT-ASP, -SHUF, -FROZEN | s | W6 preset, action-space proposal variant | as above | yes | as above |
| INT-v-NOVAL (GROUNDED mode only; optional, sec 14) | s | INT-v with valuation ABSENT | ON | **no** | reported only: what valuation contributes |

That is 10 arms per seed in ABSENT mode and 12 in GROUNDED mode with the NOVAL diagnostics.

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
- **The permutation seed is `s + 7`**, drawn from a private generator, so SHUF does not consume the agent's RNG stream differently from INT beyond what the targets themselves cause.
- **Self-supply check (red-team item RT-3).** SHUF must not supply its own asserted value. Two checks enforce this:
  - R2 requires SHUF's E2 head to FAIL the W3(a) disc bar, which shows the shuffle destroyed the label information;
  - SHUF's `outcome_decomposition` is computed by the same I1 function on the env's own `transition_type` stream, never on the permuted labels.

## 6. DVs, margins and absolute floors

### 6.1 DVs (all per 100 steps, per arm, per window)

- **Primary:** env reward in LAST, meaning `100 x sum(harm_signal) / 600`.
- **Grounded component** `G`: the part of LAST's env reward on steps whose `transition_type` is a true contact (`agent_caused_hazard`, `env_caused_hazard`, `env_caused_multisource`) or a consumption (`resource`). It excludes the approach and proximity shaping terms. It is computed from the same per-step reward and the same `transition_type` (I1-6 category sets).
- **Secondary:** true harm contacts in LAST, and the reward change FIRST -> LAST.
- **Reported:** consumptions, proximity steps, `benefit_approach` steps, early terminations, action entropy and class coverage, proposal m4, E2 disc4_h1 / disc5_h1 and k, ARC-016 `running_variance` and commit rate, per-group losses.

### 6.2 Margin rule (accepted)

margin(metric, stratum) = max( 2 x RMS of the per-seed deltas NATIVE - NATIVE-Rk, pooled over that stratum's admitted seeds ; floor(metric, stratum) ).

- The RMS form matches the 1105 detector's leave-one-out SD.
- A margin is CANNOT_DETERMINE when any admitted seed has fewer than 2 completed NATIVE-Rk arms, or the stratum has fewer than 8 deltas.
- The same margin is used for every comparison on that metric and stratum (P1, P2, P3, P4). See RT-2 for the caveat that INT-vs-INT noise may exceed NATIVE reseed noise.

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
| reward, LAST | benign | 0.257 (750-step half2) | 25 (15) | 0.514 | x1.118 | **0.57** | 0.25 |
| reward, LAST | trapped | 1.056 (half2) | 10 (10) | 2.112 | x1.118 | **2.4** | 1.0 |
| true contacts, LAST 600 | benign | 0.808 | 25 (10) | 1.617 | none (exact 600) | **1.6** | 1.0 |
| true contacts, LAST 600 | trapped | 2.385 | 10 (9) | 4.769 | none | **4.8** | 1.0 |
| reward change FIRST -> LAST (P4) | benign | 0.411 (half1 -> half2) | 25 (15) | 0.822 | x1.118 | **0.90** | 0.25 |

- **Why these are LOWER-BOUND noise estimates (so the floors are not over-strict):**
  - (i) a matched-step weight walk perturbs less than a full agent reseed, which also changes the initial weights of every module;
  - (ii) 10 of the 25 benign deltas came from seeds 61-63, where every NULL replicate reproduced M0 exactly. Over the two harm-bearing benign seeds alone (64, 65), 2 x RMS is 0.81 for reward (0.90 after window correction) and 2.56 for contacts;
  - (iii) the benign population in the v2 screen (early terminations 0-8 per 600 steps, 12 of 15 seeds with >= 3) looks more like seeds 64-65 than 61-63.
  - **So the runtime 2 x SD will probably exceed the floors in the benign stratum. The floors bind mainly when a stratum's reseeds happen to coincide (a degenerate SD), and preventing that is their purpose.**
- **Why they are not the NATIVE regime.** The T2 agent carried the R5b scaffold, the COV head, R2 depth 2 and trained evaluators. It was not NATIVE. There is no measurement of NATIVE-vs-reseeded-NATIVE spread with tie-break ON in any record (`r5b_r2_fresh_seed_replication` is tie-break OFF, and its arms differ in configuration, not in seed). **DRAFT flag:** the floors are grounded in the nearest measured analog, not in the target quantity. The runtime 2 x SD term measures the target quantity directly, and that term dominates wherever the reseeds actually vary.
- **Floors not derived:**
  - consumptions (reported only). Measured 2 x RMS is 0.74 benign and 0.89 trapped;
  - the trapped reward change (P4 is benign-only).

### 6.4 Can P1b pass? (headroom, stated before the run)

- In the v2 screen, benign NATIVE-analog reward over the first 600 steps averaged -0.49 per 100 (between-seed SD 0.43, n = 15).
- Consumption reward is capped at 0.45 per 100 (Q7).
- Beating NATIVE by > 0.57 on a benign seed therefore needs roughly: most of the harm removed, plus some added consumption or approach shaping.
- That is reachable, but it is not slack. P1g stops the approach shaping part from carrying the gain alone.
- **A P1b FAIL with P1g, P2 and P3 all holding is a "gain too small for the margin" outcome.** The autopsy reports it as such. It is not "the loop did not close".

## 7. Preconditions (INVALID: fix, re-run under a lettered id, never scored as FAIL)

Each is checked per admitted seed, per tested variant v. A failure on any admitted seed makes variant v INVALID.

| id | check | instrument |
|---|---|---|
| R0 | every trainer group's guard verdict is PASS; none is CANNOT_DETERMINE (Q4d) | C0 grad-reach guard (`ree_core/utils/grad_reach_guard.py`), trainer ON |
| R1 | CODEC only: W1 gates (b) round trip >= 0.95 per class; (c) median decoded norm in [0.5, 2] x one-hot norm over 3 CEM iterations, no growth; (d) iteration-0 O-norm in [0.5, 2] x encoder-image median. ASP: that variant's own member gate (**undefined, Q5**) | I1-4 `cem_codec_trace`, `codec_ranges`, `codec_roundtrip_accuracy` |
| R2 | at the end of the run, INT-v's E2 world head meets W3(a) (disc4_h1 >= 0.47 and k = 10) on the held-out uniform-random set, **and INT-v-SHUF's head does not** | I1-1 `action_discrimination` |
| R3 | W4(c): real-head pick-flip rate minus shuffled-head pick-flip rate > 0.15 on >= 20 cloned-env probe states | I1-2 `collect_probe_states`, I1-3 `head_swap_flip_rate` |
| R4 | GROUNDED only: the 1105a primary detector D_N is silent on INT-v | 1105a scorer |
| R5 | liveness: every group's held-out loss at LAST is below INT-v-FROZEN's (reported per group) | trainer telemetry |
| R6 | provenance: `verify_pin` passes (structural + marker), and the executed `ree_core` sha equals the pre-registered 40-hex sha | `substrate_pin.verify_pin`, `pin_manifest_block` |
| R7 | instrument sanity: no I1 instrument used in scoring returns CANNOT_DETERMINE on a scored arm (e.g. an unknown `transition_type` in `outcome_decomposition`) | I1 verdict fields |

Every I1 instrument used here also carries its pinned canary (I1 contract tests). The A1 script re-runs the cheap canaries at start: stratum, outcome decomposition, and action discrimination on a label-shuffled toy head at chance. A canary that fails makes the run ERROR before any arm is read.

## 8. Criteria and verdict

">= 4/5" means at least 4 of that stratum's 5 admitted seeds. Each criterion is evaluated separately for each tested variant v. T = INT-v, S = INT-v-SHUF, F = INT-v-FROZEN, N = NATIVE. The margins m are from sec 6.

| id | stratum | statement | kind |
|---|---|---|---|
| **P1b (PRIMARY)** | benign | reward_LAST(T) - reward_LAST(N) > m_reward on >= 4/5 | superiority |
| **P1g** | benign | G_LAST(T) - G_LAST(N) >= 0 on >= 4/5 (the gain is not carried by approach shaping alone; Q7, K5/V2) | sign guard |
| P1t | trapped | reward_LAST(N) - reward_LAST(T) <= m_reward on >= 4/5 (gain reported) | non-inferiority |
| P2 | each stratum separately | contacts_LAST(T) - contacts_LAST(N) <= m_contacts on >= 4/5 | non-inferiority |
| P3 | each stratum separately | reward_LAST(T) - reward_LAST(S) > m_reward on >= 4/5 | superiority |
| P4 | benign | [reward_LAST - reward_FIRST](T) - [same](F) > m_change on >= 4/5 | superiority |

### 8.1 Verdict ladder (per variant, evaluated in this order)

1. **ERROR**: a canary failed, or the pin could not be verified. It is not a verdict about the loop.
2. **INVALID**: any precondition R0-R7 failed on any admitted seed. Fix and re-run under a lettered id. It is never scored as FAIL.
3. **CANNOT_DETERMINE**:
   - a stratum has fewer than 5 admitted seeds after reserves (`under_admitted:<stratum>`);
   - a margin is not computable (`margin_undetermined:<metric>:<stratum>`);
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
  - about 6.4k steps per arm (2,400 dev + about 1,000 warmup + 3,000 closed loop), x 10 arms (ABSENT) or 12 (GROUNDED + NOVAL);
  - benign: about 64-77k steps x 0.02 s x 1.2, i.e. roughly 0.5 h;
  - trapped: the same steps x 0.2 s x 1.2, i.e. roughly 4-5 h.
- **10 admitted seeds:** about 2.5 CPU-h benign + about 22 CPU-h trapped, so **~25 CPU-h (ABSENT) to ~30 CPU-h (GROUNDED + NOVAL)**. Reserves add up to about 40% more if all four are used.
- **Screen:** about 33 NATIVE-only seeds x about 5-10 min = **3-6 h**.
- **Total:** about 30-45 CPU-h. That is consistent with plan sec 5 (35-45 CPU-h) and dominated by the trapped seeds.
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
| floors | reward 0.25 / 1.0, contacts 1.0, change 0.25 | 0.57 / 2.4, 1.6 / 4.8, 0.90 | derived from measured replicate spread (6.3). The plan's P4 floor was below the measured noise |
| grounded-component guard | absent | P1g added | env reward includes approach shaping with tie-break ON (Q7). K5/V2 excludes approach steps as evidence of benefit |
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
2. **P1g:** accept the grounded-component sign guard (recommended). The alternative is to score raw env reward alone and let approach shaping count.
3. **ASP build path (Q5):** the head-to-head needs an ASP build row and an ASP member gate (the R1 analog). Until they exist, the options are:
   - (a) hold A1 until both exist; or
   - (b) run A1 with CODEC only and record the head-to-head as not run.
   Neither is recommended here, because the user asked for both in parallel. This is a planning gap for the orchestrator or `/governance` to route.
4. **NOVAL diagnostics** in GROUNDED mode: +2 arms (about +20% cost) in exchange for a reported measure of what valuation contributes. Recommended, because it localises a FAIL.
5. **Head-to-head tie rule:** "ASP wins within margin" (simplicity) vs "the user decides at merge".
6. **An INT reseed arm (RT-2):** add INT-v-R1 per seed (about +20% cost) so the P3 margin is computed from INT-vs-INT noise, not NATIVE reseed noise. See sec 15.

## 15. Red-team pass

*(filled in below after the independent red-team review)*
