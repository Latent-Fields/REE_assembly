# Coupled loop-repair campaign: plan of record (integration-branch campaign, user decision Q2)

- **Status: PLAN OF RECORD, v1 (design only).** Written 2026-09-25T10:31Z by session `bt0925-campaignplan` (Worker X, `orchestrate-20260924-breakthrough`), chip_ref `chip-20260925-coupled-campaign-plan`.
- **Nothing was built, queued, or registered by this document.** It proposes substrate_queue rows (section 7). `/governance` and the user own those rows and the closure-plan frontmatter. This file carries no `closure_plan:` block on purpose: adding one would change the derived closure numbers, and that is `/governance`'s call.
- **Evidence domain: D0.** The plan synthesises measured records. It adds no new measurement. Quantities quoted below carry the record and sha that produced them.
- **Code state re-measured at writing time:** ree-v3 `origin/main` @ `276d9a51a9`. Its `ree_core/` is identical to `b14f7bc`; the only later commits are queue snapshots. REE_assembly `origin/master` @ `892a53036a`. `file:line` citations marked **(main)** are against `276d9a51a9`. The others are quoted from the named record at that record's sha.
- **Inputs, all read in full:**
  - `breakthrough_pass_synthesis_20260925.md`, sections 1-7d (`378aace99b6`)
  - `native_waking_trainer_design_20260925.md` (`0c0f5b76ec`), with its guard addendum (`df840f559c3`). **The skeleton addendum is not on origin yet** (see premise P2).
  - `gradient_reach_census_20260925.md` (`940c690c9dd`)
  - `action_decoder_training_causal_probe_20260925.md` (`a369f411ff8`)
  - `e2_rollout_divergence_and_proposal_state_dependence_20260924.md`, with addenda 1-3
  - `e3_evaluation_edge_test_20260924.md`, with addenda 1-3
  - `babbling_e2_action_coverage_probe_20260925.md` (`0ac69c87446`)
  - `grounded_valuation_null_detector_20260925.md`, v1, v2 and v3-queued sections
  - `r5b_r2_fresh_seed_replication_20260924.md` (`fc987f3b057`), which is where the replication lesson comes from
  - CLAUDE.md "Git Policy -> Why trunk-only (and the one narrow exception)"

## 0. Decisions this plan implements (not reopened here)

| id | decision | source |
|---|---|---|
| Q2 | **One** coupled campaign on a ree-v3 `integration/<slug>` branch. It covers codec repair, E2 world-head action coverage, grounded main-channel valuation, and the trainer switched ON. It is validated **only** as an integrated loop. Single-factor probes cannot validate its parts in isolation. | synthesis section 7, rec-20260925-35999055 |
| Q4a | Hybrid WakingTrainer. The phased trainers become scheduled members. Per-tick online losses are used only for the REINFORCE heads. The trainer is stepped from `update_residue()` every K ticks. | rec-20260925-3677487d |
| Q4b | The skeleton and the harm_eval loss land on main, default-OFF, first. The coupled repair follows on the branch. | rec-20260925-6eb5db00 |
| Q4c | `world_obs_encoder` is trained through the agent's actual read path. It is not allowlisted. | orchestrator, under standing delegation |
| Q4d | The grad-reach guard RAISES when the trainer is ON. | orchestrator, under standing delegation |
| 7b/7d | The E2 world-head member learns from a NEW structured babbling generator: class-balanced, with persistent runs (the L2 form). About 25% of its batches are retained babbling replay. The L2R numbers are its acceptance bar. | rec-20260925-0ad0f56b |
| 7c | Retention uses ACh-gated freeze/unfreeze. The MECH-398 gain is hosted by the WakingTrainer. Destabilisation is MECH-207-style (surprise AND ACh). Re-phasing those claims to v3 is GFLAG-0509, which `/governance` owns. | synthesis section 7c |
| Q1 | Grounded valuation needs a validated reward-hacking detector first. V3-EXQ-1105 was pulled and is being redesigned as V3-EXQ-1105a (`bt0925-1105a`). If the detector fails, valuation is parked. | rec-20260925-713b2cb7, rec-20260925-372b6ca9 |

## 1. Premises re-measured before planning

| # | premise | re-measured | verdict |
|---|---|---|---|
| P1 | The guard exists on main as a pure instrument | `ree_core/utils/grad_reach_guard.py` is on origin/main since `ec1f5697f1`. It is imported by nothing. | holds |
| P2 | "The skeleton plus harm_eval is on main" (the brief lists the design "with the guard and skeleton addenda") | **Not yet.** At `276d9a51a9` there is no `waking_trainer` module on origin/main, and no skeleton addendum on REE_assembly origin. The claims `bt0925-wtrainer` through `-wtrainer-5` are active. The worker's scratch draft names the module, the flags (`waking_trainer_enabled` and 6 others) and the seam `WakingTrainerMember`, and reports a green hub suite, but no landed sha. | **corrected**: this plan treats C1 as in progress. Every branch step waits for it. |
| P3 | The decoder CEM defects are still at the cited lines | `hippocampal/module.py:644-647` returns `action_object_decoder(flat)` unbounded, and `:2151` sets `ao_std = torch.ones_like(ao_mean)` **(main)** | holds |
| P4 | E3's benefit gate can open natively | The gate is `_benefit_samples_seen` (`e3_selector.py:708`), checked at `:1892-1896` **(main)**. Its only incrementer, `record_benefit_sample` (`:1366`), has **no caller in ree_core** (`git grep`, main). | holds. This is a wiring gap the valuation workstream must close (W5). |
| P5 | The replication lesson applies to the acceptance design | R5b+R2 won 2/3 seeds, then failed on 5 fresh seeds (harm better on 1/5). The earlier gain came from hazard-trapped starts (`fc987f3b057`). The detector's positive control exists only on trapped starts (1105 v1/v2). | holds. Stratification is per criterion, not pooled. |
| P6 | Fleet experiments can run branch code | The runner executes against the live checkout, i.e. main. `experiments/_lib/substrate_pin.py` (main) can put `ree_core/` from ANY resolvable commit first on `sys.path`, with hard-fail verification. It resolves the ref locally (`git rev-parse --verify`), so it needs the branch commit to be present on the worker. The runner does bare `git fetch origin` / `git pull --rebase`, which by default fetches all heads (D0, not probed). | **puzzle (known rules)**, probe N0 below. `experiments.*` still resolve from main, so the branch must carry **ree_core only**. |
| P7 | Existing registry rows that overlap the campaign | `SD-080` (`pending_implementation`, encoder half only). `e3-outcome-informative-planned-pathway` (priority 1, `pending_implementation`): its leg (i) is an action-conditional E2 world head with a waking objective; its leg (ii) is horizon aggregation, and its hint already says to treat a GFLAG-0485 row as an amend of it. `SD-ZWORLD-SENSE-PATH-PARITY` (`registered_no_build_owed`). `e2-world-forward-sleep-trainer` (adjacent). There is **no WakingTrainer row yet** (GFLAG-0491 is still open). | holds. Section 7 amends rather than duplicates. |
| P8 | Stored replay latents stay valid | Only while the encoder is frozen. Q4c trains `world_obs_encoder` through the read path, so every replay buffer that stores **detached z** goes stale as the encoder moves: the harm_eval buffer, the E1/E2 native buffers (`agent.py:6294-6299`, `:11407-11411` at `863d23d65a`), and the babbling replay. L2R was measured on a random-init, **frozen** encoder (0ac69c87446 Design). | **new coupling**, named as puzzle N2 |

## 2. Status table (the resume primitive)

Update this table every session that touches the campaign; see the resume ritual in section 10. Status values are `done`, `in-progress`, `ready`, `blocked`, `not-started` and `parked`.

"Lands on" means one of three places:
- **MAIN-I**: main, instrument only. It changes no behaviour.
- **MAIN-OFF**: main, default-OFF, bit-identical when OFF.
- **BRANCH**: `integration/coupled-loop-repair`, `ree_core/**` plus its contract tests only.

| node | workstream | what | lands on | owner skill | debt class | status | blocking on | next action | last updated |
|---|---|---|---|---|---|---|---|---|---|
| C0 | trainer | grad-reach guard (design M1) | MAIN-I | /implement-substrate | complicated (buildable) | **done** | - | none (ree-v3 `ec1f5697f1`) | 2026-09-25 |
| C1 | trainer | WakingTrainer skeleton plus `HarmEvalMember` (design M2/M3 as scoped by Q4b) | MAIN-OFF | /implement-substrate | complicated (buildable) | **in-progress** (`bt0925-wtrainer`) | landing | land it and append the design addendum with the origin sha | 2026-09-25 |
| C2 | valuation | detector redesign V3-EXQ-1105a | queue (main) | /queue-experiment | complex (probe-gated) -> puzzle | **in-progress** (`bt0925-1105a`) | - | queue, run, adjudicate | 2026-09-25 |
| I1 | instruments | campaign acceptance instruments in `experiments/_lib` (section 3, I1) | MAIN-I | /implement-substrate | complicated (buildable) | not-started | - | build (first buildable step) | 2026-09-25 |
| N0 | infra | can a fleet worker `substrate_pin` an `integration/**` sha? | - | orchestrator probe | puzzle (known rules) | not-started | - | on one worker, after a normal runner cycle, run `git rev-parse --verify origin/integration/<slug>^{commit}`. If it does not resolve, add a named pre-fetch to `substrate_pin`. | 2026-09-25 |
| T1 | trainer | E1 member and E2-self member (their native losses exist). E2-self records its own transitions (design point 3). | MAIN-OFF | /implement-substrate | complicated (buildable) | not-started | C1 | build after C1 lands | 2026-09-25 |
| W2a | babbling | structured babbling generator (L2 form, all action classes incl. stay), as a ree_core developmental source. Constructed only when enabled and never called by default. | MAIN-OFF | /implement-substrate | complicated (buildable) | not-started | - | build (second buildable step) | 2026-09-25 |
| BR0 | branch | cut `integration/coupled-loop-repair` from main | BRANCH | owning session | - | not-started | C1 | cut right after C1 lands, so the branch's trainer is trunk's | 2026-09-25 |
| W3 | E2 world | `E2WorldMember` over a trainer-owned buffer: on-policy plus 25% retained babbling replay, stored as **raw obs** and re-encoded at replay time. FROZEN state only in this step. | BRANCH | /implement-substrate | complicated (buildable) | not-started | BR0, W2a | build (third buildable step); gate = L2R bar | 2026-09-25 |
| N2 | E2 world | does retained replay keep the L2R bar while the encoder trains through the read path (Q4c)? | - | /queue-experiment (pinned) | puzzle (known rules) | not-started | W3, W6a | probe N2 | 2026-09-25 |
| W6a | trainer | world-encoder member: SD-070 P0a moved onto the sense path (`world_obs_encoder -> latent_stack.encode`, the ZSelfP0 `_native_chain` pattern). Buffers age out or are re-encoded. | BRANCH | /implement-substrate | complicated (buildable) | not-started | BR0 | build after W3 | 2026-09-25 |
| W4 | E3 aggregation | E3 scores on its informative depth (depth-1 read / fidelity-weighted horizon / discount), keeping SD-081's planned depth > habit depth | BRANCH | /implement-substrate after probe N3 | complex (probe-gated) -> puzzle | blocked | W3 | probe N3 | 2026-09-25 |
| W1 | codec | whole codec: encoder objective for `e2.action_object_head` + tied decoder + **bounded** decode + iteration-0 sampling matched to the encoder image + `terrain_prior` on a grounded target; codec and prior groups under the guard | BRANCH | /implement-substrate | complicated (buildable), except the prior target | blocked | W4 (for the prior's grounded target and the Q-best coverage check) | build the codec parts (N4 settles the prior target) | 2026-09-25 |
| N4 | codec | which grounded target makes `terrain_prior` state-conditioned beyond a shuffled prior? | - | pinned probe | puzzle (known rules) | blocked | W1 codec parts, W4 | probe N4 | 2026-09-25 |
| W5a | valuation | 5-seed cloud battery (Q1): M2 regression-credit on primary channel weights, vs the M4 null and the raw-rule control | queue (main; the rules are harness-side) | /queue-experiment | complex (probe-gated) -> puzzle | blocked | C2 PASS | queue the battery only if 1105a PASSes; otherwise **park** W5 (Q1) | 2026-09-25 |
| W5b | valuation | port the winning rule into ree_core as a trainer-hosted non-gradient member (primary-channel weights from grounded outcome), plus a `benefit_eval` member that drives `record_benefit_sample` | BRANCH | /implement-substrate | complicated (buildable) | blocked | W5a PASS | build after the battery verdict | 2026-09-25 |
| W2b | babbling | ACh-gated unfreeze: MECH-398 gain g in [0,1] on member learning rates; retained memory re-opened only when surprise AND g coincide (MECH-207) | BRANCH | /implement-substrate after probe N5 | complex (probe-gated) -> puzzle | blocked | W3 | probe N5 (2x2) | 2026-09-25 |
| W6 | trainer | integrated config preset: trainer ON, every group guard-green, guard raises (Q4d) | BRANCH | /implement-substrate | complicated (buildable) | blocked | T1, W1, W2b, W3, W4, W5b, W6a | assemble the preset | 2026-09-25 |
| A1 | acceptance | integrated closed-loop acceptance run (section 5), queued from main, `ree_core` pinned to the branch sha | queue (main) | /queue-experiment (user fixes the pre-registration) | complex (probe-gated): the run IS the probe | blocked | W6, N0, I1 | pre-register | 2026-09-25 |
| M1 | merge | merge gate (section 6), then merge and delete the branch | BRANCH -> main | owning session | complicated (buildable) | blocked | A1 PASS | - | 2026-09-25 |
| F1-F3 | small fixes | section 8 | MAIN | per fix | complicated (buildable) | not-started | - | route per section 6 | 2026-09-25 |

## 3. Workstreams

Every workstream has one rule in common: **its member-level gate is a precondition of the integrated run, not evidence that the loop works.** Q2 accepted that the parts cannot be validated one at a time. A member gate only certifies that the part is well-conditioned and reaches its consumer. It follows the pass's rule on domains: D1 or D2 at most, never credited as D3.

### W-trainer (C0, C1, T1, W6a, W6): the learner

- **Main (default-OFF):**
  - C1: the skeleton and the harm_eval member.
  - T1: the E1 and E2-self members. Their losses already exist natively: `compute_prediction_loss` and `compute_e2_loss` (design section 1a rows 1-3). The E2-self member records its own transitions from `_current_latent`/`_last_action`, so it does not depend on the harness's `record_transition` (design section 2(i)).
  - These members are independent of the coupled set and are guard-armed. They land default-OFF, so the fleet is untouched.
- **Branch:**
  - W6a: the world-encoder member (Q4c). It moves SD-070 P0a onto the actual sense path. This is the build `SD-ZWORLD-SENSE-PATH-PARITY` was registered for, so it amends that row rather than making a new one.
  - W6: the integrated preset.
- **Buffer-staleness requirement (P8).** Once W6a trains the encoder, every member that replays stored latents must do one of two things:
  - re-encode stored raw observations through the current read path, as W3 does by design; or
  - bound buffer age (`waking_trainer_buffer_max`) and report the age-vs-loss relation.
  Which of these the harm_eval member needs is part of probe N2.
- **Acceptance (member level):**
  - guard PASS on every group (G1-G5, design section 3a), with no CANNOT_DETERMINE;
  - RNG neutrality ON: global state identical before and after each update;
  - OFF bit-identity. This is the C1 contract pattern (W2/W2b in the worker's test plan).
  - DEFERRED groups each carry a registered row id, per design section 3c.1: depth stack (census #13); REINFORCE heads (SD-082 / ARC-062); z_self valuation consumer (GFLAG-0481).

### W1 codec: proposal generation (GFLAG-0488/0490, SD-080, census #3)

- **What (branch).** The three coupled defects from `a369f411ff8`, plus the prior:
  1. An encoder objective for `e2.action_object_head` and a decoder tied to it. Trace candidate 2 is the joint codec; the decoder-only fix (candidate 1) FAILED.
  2. Bounded decode before the decoded vector is used as the rollout action (`module.py:644-647` (main), consumed at `:2280`). Today a trained decoder drives decoded norms of 50 -> ~370-1080 over 3 CEM iterations.
  3. Iteration-0 sampling scale matched to the encoder's image (`:2151` (main)). Today samples have norm ~3.9 against an image of ~0.29-0.36.
  4. `terrain_prior` trained on a grounded target, not by behavioural cloning of E3's own picks (which is circular).
  Codec and prior become new trainer groups under the guard.
- **Main part:** codec telemetry only, in I1. That means the per-CEM-iteration O-norm and decoded-norm trace (the `cem_trace_diag` shape), the proposal m4 state-dependence, and the executed-action norm.
- **Why the branch:** the decoder probe showed each defect masks the next. With an untrained decoder, (2) and (3) were latent. With a trained decoder, they bind.
- **Member gate:**
  - (a) guard PASS on the codec and prior groups;
  - (b) held-out round trip `decode(encode(z, a)) = a` >= 0.95 per class;
  - (c) over 3 CEM iterations, the median decoded norm stays within [0.5, 2] x the one-hot norm, with no iteration-on-iteration growth (today it grows ~x3 per iteration);
  - (d) the median iteration-0 sample O-norm is within [0.5, 2] x the encoder-image median norm (today ~12x);
  - (e) **informative D2 (proposal -> choice-relevant pool):** at >= 20 cloned-env probe states per seed, the proposal pool contains a candidate whose first action is in the env-Q-best set more often under the real codec+prior than under a label-shuffled codec+prior, by more than 0.10 on >= 4/5 seeds. Env-Q is the ADDENDUM 3 outcome-3 estimator: 6 random 4-step continuations per state.

  Why (e) and not proposal "variation": variation is not evidence here. A shuffled decoder varied the pool majority exactly as often as an honest one (criterion P failed on the control, 4/5 vs 4/5).
- **Contingency, decided at that time and not now:** if (b)-(d) cannot be met, the synthesis's alternative is action-space proposals, which delete the codec. That is a user decision (section 9).

### W2 babbling: developmental source, retention, freeze/unfreeze (GFLAG-0504, GFLAG-0509, ARC-074)

- **W2a (main, default-OFF): the generator.**
  - Draw a class uniformly over **all** env action classes and hold it for a run length drawn uniformly from {1..4}; repeat. This is the L2 form in `0ac69c87446`, which used classes {0..3} because the native generator only emitted those. The new generator includes the stay class (4), so it matches the 5-class env.
  - It is a ree_core developmental-stage source that the trainer consumes (synthesis 7b, consequence 2). It is not wired to the scheduler's native policy.
  - Pure generator: when OFF it is never constructed.
- **W2b (branch): the unfreeze rule.** Each retained-memory entry carries a `frozen` flag.
  - FROZEN: not evicted or overwritten by on-policy data, and replayed at the ~25% mix. This is the state W3 builds.
  - UNFROZEN: entries become replaceable by fresh babbling bouts or re-labelled experience. That happens only when the ACh-analog gain g (MECH-398, trainer-hosted) AND a surprise signal (E2-world one-step error on the retained set above threshold) coincide (MECH-207).
  - g also scales member learning rates.
  - GFLAG-0509 (re-phase MECH-398/207 to v3) governs **claim tagging only**. It does not block the build.
- **Member gate:**
  - W3's L2R bar (below) holds with FROZEN on;
  - plus probe N5's 2x2 (section 4).

### W3 E2 world-head member (GFLAG-0485 leg (i); `e3-outcome-informative-planned-pathway` leg (i))

- **What (branch).** `E2WorldMember`, stepping the native `compute_e2_world_loss` (design row 4). Its buffer mixes:
  - on-policy transitions, and
  - ~25% retained babbling replay from W2a, stored as raw observations and actions and re-encoded at replay time (P8).
  - Class-balanced replay of the agent's own buffer is **not** used: it was falsified, because it cannot create classes the agent never took (ADDENDUM 2).
- **Why the branch:** without coverage, a native E2-world objective reproduces the 99%-one-class collapse (ADDENDUM 1). So the member's behaviour is only meaningful with W2, and its consumer reading is only informative after W4.
- **Member gate: the L2R bar, re-measured on this member.** It uses the babbling probe's protocol: disc4_h1 on a held-out uniform-random test set, fidelity k at H = 10, and 9,000 on-policy updates after the babbling phase.
  - (a) disc4_h1 >= 0.47 and k = 10 on >= 4/5 seeds (L2R measured 0.473-0.553 and k = 10 on 5/5);
  - (b) retention ratio (post - B0) / (pre - B0) >= 0.5 on >= 4/5, where B0 is the babbling probe's on-policy-data head (L2R 1.31-1.53; one-off L2 met it on 2/5);
  - (c) the label-shuffled babbling-replay control (the B1S analog) does **not** reach (a);
  - (d) guard PASS;
  - (e) the rollout t30 norm stays bounded, with no x1.2/step growth.
  - Report the 5-class disc too. Report ARC-016 `running_variance` and the commit rate, because the commit gate reads this head's one-step error (`e3_selector.py:4945` (main); GFLAG-0486). Training the head changes what "committed" means, and that must be visible.

### W4 E3 aggregation (GFLAG-0485 / 0486; `e3-outcome-informative-planned-pathway` leg (ii))

- **Fact to fix.** More than 98% of E3's across-candidate score variance comes from rollout steps > 5. Scoring the first 1-5 steps flips the pick in 78-100% of cases. A depth-1 read of E3's own scorer tracks true consequence (rho 0.24-0.53 with an action-covered head), but the full horizon does not (rho -0.18 to 0.01) (ADDENDUM 2).
- **Constraints already measured:**
  - R2 alone (`_score_depth_limit = 2`) is not a repair. On fresh seeds it was necessary 0/5 and harmful in the mean.
  - The planned scored depth must stay strictly greater than `dualsystem_habit_depth`, or SD-081's P1 fails by construction. The habit pathway sets `_score_depth_limit = max(2, habit_depth)` at `e3_selector.py:2088` (main).
  - Depth-matching alone was inert on V3-EXQ-1083's statistic (the row's hint).
- **What (branch):** the aggregation that probe N3 selects. Candidates:
  - depth-1 read;
  - per-step weights set by measured fidelity (weight step t by whether the head beats persistence at depth t);
  - geometric discount.
- **Main part:** the depth-variance / truncation-flip / deep-shuffle decomposition and the cloned-env true-consequence Spearman, as I1 instruments.
- **Member gate (the informative D2 the babbling probe could not get):** with the W3 head and the chosen aggregation, on >= 20 cloned-env probe states per seed:
  - (a) Spearman(J_pred, J_true) exceeds the label-shuffled-head arm's by more than 0.15 on >= 4/5 seeds;
  - (b) E3's pick is in the env-Q-best set more often than under the shuffled head, by more than 0.10 on >= 4/5;
  - (c) **the shuffled head moves E3's pick less often than the real head does.** Pick-flip rate vs the init head: real minus shuffled > 0.15 on >= 4/5. Under the current E3 both moved it at 70-100%, which is the non-discriminating D2 in `0ac69c87446`.

  **No D2 reading of any other workstream counts until W4's gate passes.**

### W5 grounded valuation (Q1; GFLAG-0487 / 0501; design `50b679abb8`)

- **Chain:**
  1. C2: V3-EXQ-1105a detector PASS.
  2. W5a: the 5-seed cloud battery, run on **main** because its rules are harness-side (as in the smokes), with M2 first, the M4 null and the M1RAW K3 control.
  3. W5b: port the winner into ree_core on the branch.
  If C2 does not PASS, **W5 is parked** (Q1). The campaign then cannot reach its integrated criterion as specified, and the user decides whether to run A1 without W5 (section 9).
- **W5b content:**
  - (i) A trainer-hosted **non-gradient** member that sets primary-channel weights (F, harm_eval, residue, benefit_eval) from grounded env outcome: contacts and consumptions only, never approach steps (K5/V2).
    - The commensurability operator equalises spread and gives noise a vote (addendum 2), so it is not this.
    - ARC-108 gating reweights only modulatory channels, from an internal proxy, and was unarmed in this regime (addendum 3), so it is not this either.
    - A non-gradient member is outside G1-G5. It gets its own liveness check: weights move within bounds, and they do not move under a frozen outcome stream.
  - (ii) A `benefit_eval` member (`compute_benefit_eval_loss` exists), buffered so it is replay-safe (design section 1b).
  - (iii) Wiring: the member calls `record_benefit_sample` (P4). Without it, E3's benefit channel never opens natively.
- **Member gate:**
  - the battery's own pre-registered verdict (K1-K4, V1-V4 of `50b679abb8`);
  - plus, in the integrated run, the 1105a primary detector is silent on INTEGRATED. Its positive-control canary belongs to the battery, not to A1.

### I1 acceptance instruments (main, instrument-only, `experiments/_lib`)

Every gate above and every A1 precondition reads one of these. They are ported from the committed probes under `REE_assembly/evidence/planning/probes/{rollout,evaluation,babble,trainer}/`. The CEM trace comes from `.scratch/breakthrough-20260924/decoderprobe/cem_trace_diag.py`, which is uncommitted and must be copied before that scratch dir is cleaned.

1. **Action discrimination.** The swap-first-action executed-closest metric (disc_h, over 4 and 5 classes) plus fidelity k, on a held-out uniform-random test set. This is the addendum-1 / babbling metric.
2. **Cloned-env probe states.** True next z per action class through sense()'s own encoder (validated max |diff| 0.0 in ADDENDUM 2), and the env-Q estimator (ADDENDUM 3 outcome 3).
3. **E3 decomposition.** Variance share from steps > d; truncation and deep-shuffle flip rates; Spearman(J_pred, J_true) at full, depth-1 and the chosen aggregation; pick-in-Q-best; head-swap pick-flip rate.
4. **Codec trace.** Per-CEM-iteration O-norm and decoded norm, the iteration-0 range ratio, the round-trip accuracy, the pool's Q-best coverage, and proposal m4.
5. **Stratum classifier.** Writes the NATIVE sidecar before any other arm is read.
6. **Outcome decomposition by `transition_type`.** True contacts, proximity steps, consumptions and approach steps, each counted separately.

These are negative instruments (CLAUDE.md), so each one ships with a pinned canary that must keep reproducing. Examples:
- a label-shuffled head scores disc at chance;
- the untrained-decoder CEM trace reproduces the contraction signature;
- the trained-decoder trace reproduces the divergence signature.

An empty derivation reports CANNOT_DETERMINE, never PASS.

## 4. Probe-gated nodes and the probe that settles each

Every probe below runs **ree_core pinned to a branch sha** (N0). Harness code lives on main (I1). Sizes are Mac-probe or small-cloud, pre-registered, with 5 seeds, stratified where outcome is read.

| node | class | question | probe (pre-register before running) |
|---|---|---|---|
| N0 | puzzle (known rules) | can a worker resolve an `integration/**` sha for `substrate_pin`? | one `git rev-parse` on one worker after a normal runner cycle. Fallback: `substrate_pin` gains a read-only `git fetch origin <ref>` into a private ref namespace. |
| N2 | puzzle (known rules) | does W3 keep the L2R bar while W6a trains the encoder (P8)? | L2R protocol, 5 seeds, arms: frozen encoder / encoder trained through the read path with raw-obs re-encode / encoder trained with stored-z replay. The bar holds, or it identifies which buffer policy keeps it. |
| N3 | puzzle (known rules) | which aggregation makes E3 track true consequence with the W3 head, without breaking SD-081's depth contrast? | re-score recorded candidate sets under {full, depth-1, fidelity-weighted, discount gamma in {0.5, 0.8}} with the W3 head and its shuffled twin, using ADDENDUM 2 Measure 2 plus W4 gates (a)-(c). Pick the simplest aggregation that passes. |
| N4 | puzzle (known rules) | which grounded `terrain_prior` target conditions proposals on state? | matched-step comparison of targets {E3's pick under the W4 aggregation, realised one-step outcome class from trainer replay, BC of E3 (today's circular baseline)}, each against a shuffled-target twin. Readout: W1 gate (e). Candidates must not read env internals. |
| N5 | puzzle (known rules) | does ACh-gated unfreeze revise retained memory only when it should? | 2x2 on the W3 member: {env action-map re-permutation (the SD-MEL-PRODUCER shift) vs none} x {g gated vs g clamped low}. **Pass** means: after the shift, gated re-learns to the bar and clamped does not; with no shift, gated keeps the bar (no spurious destabilisation). Pre-register N updates. |
| C2 / W5a | puzzle (known rules) | is there a validated detector, and does M2 calibrate channel worth? | V3-EXQ-1105a, then the Q1 battery |
| A1 | complex (probe-gated) | does the integrated loop close? | section 5. The run is the probe. |
| start stratum | **aleatoric (irreducible)** | whether a seed's start is hazard-trapped | not researched. **Hedged** by screening and per-stratum criteria (P5). |

Out of scope and deferred with row ids: the depth stack (census #13, `complex (probe-gated)`, needs a z_beta consumer D2 check); the REINFORCE heads (SD-082 / ARC-062); the z_self valuation consumer (GFLAG-0481; the E2-self member trains, but no valuation consumer reads z_self); `residue_field.neural_field` (GFLAG-0479).

## 5. The integrated acceptance criterion (A1): pre-registration DRAFT

This is a draft for the user and `/queue-experiment` to fix before any run. The numbers marked *draft* are proposals.

**Regime** (fixed at pre-registration): CausalGridWorldV2 8x8, 2 hazards, 3 resources, `world_dim` 32 (the deployed value).
- *Draft:* `proximity_approach_magnitude_tiebreak=True` in **every** arm. Without it the env's benefit shaping cannot fire (hazard wins every tie; e3 record P4), so a reward gain could only be harm avoidance. This is a user decision (section 9).
- The Phase-0 env (size 12) is reported as a secondary regime and has no criterion.

**Seeds and strata.**
- Seeds come from a fresh range disjoint from 42-200 and from 1105a's range. *Draft:* 301 upward.
- Each seed is classified from the **NATIVE arm alone**, before any other arm on that seed is read:
  - hazard-trapped: >= 10 early terminations (episode < 200 steps) in NATIVE's first 600 steps;
  - benign: otherwise.
  - The classification is written to a sidecar.
- Admit the first **5 benign and 5 trapped** seeds. *Draft* ceiling: 80 screened seeds. The trapped base rate was 0.21 in the T2 regime and 1/5 in the decoder probe's regime B.
- Fewer than 5 admitted in a stratum makes that stratum's criteria CANNOT_DETERMINE.

**Phases, per arm:**
1. a developmental epoch of equal length in every arm (*draft* 2,400 steps): INTEGRATED, -SHUF and -FROZEN run the W2a babbling generator; NATIVE and NATIVE-Rk run unscored native waking steps;
2. the same encoder warmup for all arms;
3. **3,000 closed-loop steps** (*draft*). Windows: FIRST = steps 0-599, LAST = steps 2,400-2,999.

**Arms:**
- NATIVE: all flags off.
- INTEGRATED: the W6 preset, trainer ON.
- INTEGRATED-SHUF: identical, but every grounding target is permuted across timesteps with class marginals kept. That covers the harm/benefit labels, the grounded-valuation outcome stream, the prior's grounded target, the codec decode labels, and the action labels of the E2-world buffer, babbling replay included.
- INTEGRATED-FROZEN: identical to INTEGRATED, but the trainer is OFF after warmup.
- NATIVE-R1..R3: NATIVE with a different agent seed on the same env seed. These exist **only** to calibrate margins.

**Margins.**
- For each metric and stratum: margin = max(2 x SD of the per-seed (NATIVE - NATIVE-Rk) delta pooled over the stratum, absolute floor).
- *Draft* floors:
  - reward: 0.25 per 100 steps (benign), 1.0 per 100 steps (trapped);
  - true harm contacts: 1.0 per 100 steps;
  - reward change FIRST -> LAST: 0.25 per 100 steps.
- The floors are fixed before any admitted seed runs.

**Preconditions.** These make a run **INVALID** and re-run after the fix. They are **never** scored as a scientific FAIL. Each is checked inside every INTEGRATED arm.
- R0: every trainer group's guard verdict is PASS; none is CANNOT_DETERMINE.
- R1: W1 gates (b)-(d).
- R2: at the end of the run, W3 gate (a) holds on the held-out test set, and the SHUF arm's head does not meet it.
- R3: W4 gate (c): the shuffled head moves E3's pick less often than the real head.
- R4: the 1105a primary detector is silent on INTEGRATED (only if W5 is in the preset).
- R5: liveness. Every group's held-out loss at LAST is lower than FROZEN's (reported per group).

**Criteria** (per stratum; ">= 4/5" means 4 of that stratum's 5 seeds):
- **P1b, grounded outcome, benign (PRIMARY):** INTEGRATED reward per 100 steps in LAST exceeds NATIVE's by more than the margin on >= 4/5 benign seeds.
- **P1t, trapped:** INTEGRATED is not worse than NATIVE by more than the margin on >= 4/5 trapped seeds. The gain is reported.
- **P2, not undirected:** INTEGRATED TRUE harm contacts per 100 steps in LAST do not exceed NATIVE's by more than the margin, on >= 4/5 seeds in **each** stratum.
  - True contacts are `agent_caused_hazard`, `env_caused_hazard` and `env_caused_multisource`.
  - Hazard-proximity steps are reported separately and never scored.
- **P3, shuffled control:** INTEGRATED beats INTEGRATED-SHUF on P1's statistic by more than the margin on >= 4/5 benign seeds and >= 4/5 trapped seeds.
- **P4, the loop closes:** INTEGRATED's reward change FIRST -> LAST exceeds FROZEN's by more than the margin on >= 4/5 benign seeds. Later behaviour is changed by experience.

**Verdict:**
- **PASS** iff P1b, P1t, P2, P3 and P4 all hold.
- **FAIL** if any criterion fails with both strata admitted and the run valid. Explicitly, each of these is a FAIL:
  - P1t passes but P1b fails. That is the R5b+R2 signature: a trapped-only gain.
  - P1 passes but P3 fails. Grounding does not matter.
  - P1 passes but P4 fails. The better architecture helps, but waking learning does not.
- On FAIL the branch is **not** merged. `/failure-autopsy` adjudicates the run, and the per-workstream precondition readouts localise the failing edge.
- **CANNOT_DETERMINE** if a stratum is under-admitted, or if the margin SD cannot be computed (fewer than 2 NATIVE-R replicates complete on a seed).

**Reported, no criterion:**
- consumptions per 100 steps (benefit means consumption; approach steps are reported but never count, per K5/V2);
- action entropy and class coverage;
- proposal m4 state-dependence;
- E2 disc4_h1 / disc5_h1 and k;
- ARC-016 `running_variance` and commit rate (GFLAG-0486);
- per-group losses;
- early terminations.

**Domain reached if valid: D3** (closed-loop env reward under a real policy difference, with shuffled and frozen controls).

**Cost (draft, to be re-estimated at `/queue-experiment` with trainer-ON timing):**
- The trainer adds ~0.07x an act tick at K = 1 (design section 2).
- 10 admitted seeds x 7 arms x ~6k steps is roughly 35-45 CPU-h, plus screening (~3 min per screened seed).
- Queue it as per-seed items on the fleet, with `machine_affinity` "any" and `substrate_pin` set to the acceptance sha. Pinned cells are never arm-reuse eligible (`substrate_pin.py` docstring).

## 6. Sequencing and the integration-branch merge gate (CLAUDE.md Git Policy exception)

**Order.** Each step's gate must pass before the next branch step starts, unless marked parallel.

1. **Main, now or in flight:** C0 (done), C1, C2.
2. **Main, parallel, no dependency on the branch:**
   - I1 instruments;
   - W2a generator;
   - probe N0;
   - small fixes F1-F3;
   - T1, once C1 has landed.
3. **BR0: cut `integration/coupled-loop-repair` from main once C1 is on origin/main.**
4. **Branch:**
   - W3 (L2R bar, frozen encoder)
   - -> W6a encoder member + probe N2
   - -> probe N3 -> W4
   - -> W1 codec parts -> probe N4 -> W1 prior (W1 gate (e))
   - -> W2b via probe N5 (may run in parallel with W1)
   - -> W5b (only after W5a PASS; W5a runs on main in parallel with the branch)
   - -> W6 preset, all groups guard-green.
   - **Rebase the branch onto main at every step boundary.** Each build runs its own contracts on a cloud worker (`remote_pytest.sh tests/contracts/<its tests> -q`).
5. **A1**, queued on main with `substrate_pin` = the branch head sha, which is recorded.
6. **M1 merge gate (only after A1 PASS):**
   - (a) The full ree-v3 suite on a **cloud worker**: `remote_pytest.sh` with no args covers all six roots, and `tests/preflight/`. It must be green, or every red must be shown pre-existing on main with the same failure. The branch does not touch `coordinator/`. If any later step does, add `coordinator/phase3_preflight.py`.
   - (b) Default-OFF bit-identity contracts green for every new flag.
   - (c) Merge by merge commit, so the A1-pinned sha stays an ancestor of main. If a rebase is unavoidable, re-run OFF bit-identity plus one INTEGRATED canary seed on the rebased sha, on the same machine class, because of the cross-machine `multinomial` divergence.
   - (d) All flags stay default-OFF on main. The integrated configuration ships as a named preset. **Turning it on by default is a separate user decision.**
   - (e) Delete the branch, locally and on origin, in the same session as the merge.

**What goes where (enforced for the whole campaign):**
- The branch carries `ree_core/**` and those files' contract tests **only**. `substrate_pin` loads `ree_core/` from the pin and everything else from main, so any `experiments/_lib` code A1 or a probe needs must be on main (I1).
- Queue entries, experiment scripts, evidence and planning docs go direct to main or master.
- A change touching both planes is split.

**Branch lifetime.**
- Opened at BR0. Target merge within ~14 days of BR0.
- While it lives past one session, keep a WORKSPACE_STATE line naming it (the sanctioned parking exception).
- On A1 FAIL, the branch survives only while a `/failure-autopsy`-routed lettered re-run is queued. Otherwise:
  1. tag the A1 sha (`archive/coupled-loop-repair-<date>`) so the manifest's pinned sha stays resolvable;
  2. delete the branch;
  3. write a `NOT LANDED:` WORKSPACE_STATE line with the sha and the reason.

## 7. Registry rows this plan proposes (none made here; `/governance` and the user decide)

1. **New: `sd_native_waking_trainer`** (GFLAG-0491 disposition per Q4a).
   - Covers C1, T1 and W6.
   - Its DEFERRED list carries row ids: depth stack, REINFORCE heads, z_self consumer.
   - The guard contract is its instrument.
2. **Amend `SD-080`**: widen it to the whole codec per GFLAG-0490. That is encoder + tied decoder + bounded decode + iteration-0 scale + a grounded `terrain_prior` target (census #3 / section 7 item 4).
   - This is recommended over a decoder-only row, which GFLAG-0490 shows would reproduce the failure.
   - `ready: false` until BR0.
3. **Amend `e3-outcome-informative-planned-pathway`**: its legs (i) and (ii) are W3 and W4.
   - It is the GFLAG-0485 row its own hint anticipates, so no new row.
   - Point `depends_on_unresolved` at this plan and `sd_native_waking_trainer`.
4. **New: `arc074-structured-babbling-developmental-source`** (GFLAG-0504; W2a + W2b).
   - Its unfreeze half is tagged to MECH-398/207 only if GFLAG-0509 re-phases them.
5. **New: `grounded-primary-channel-valuation`** (GFLAG-0487/0501; W5b, including the `record_benefit_sample` wiring).
   - `ready: false` until C2 PASS and then W5a PASS. It is parked if either fails.
6. **Amend `SD-ZWORLD-SENSE-PATH-PARITY`**: from `registered_no_build_owed_hygiene` to build owed in this campaign (W6a, Q4c).
7. **Optional:** a `closure_plan:` frontmatter block for this file. Nodes = the section 2 rows, `status: assembling` while the branch is open, so the unhurried build is not penalised.

## 8. Small fixes found in the pass (owed; not campaign-gated)

- **F1.** `experiments/_lib/infant_warmup.py:13-14` (main) says InfantCurriculumScheduler's Phase 0 is "plain random-policy stepping with no training of any kind".
  - The first half is wrong. Phase 0 is the agent's own native E3 selection (`act_with_split_obs`, `argmax % 4`, so class 4 is never emitted), per `0ac69c87446` premise 1.
  - Fix the docstring text only. It is a comment edit to an `experiments/_lib` file, so no behaviour changes; route it through the file's owning skill path.
- **F2.** GFLAG-0508 residual (c). Six no-op classes still default to 0 = UP (main):
  - `tonic_vigor_noop_class` (`config.py:5695`)
  - `blocked_agency_noop_class` (`:6644`)
  - `avoidance_noop_class` (`:6708`)
  - `escape_noop_class` (`:6790`)
  - `trainable_escape_noop_class` (`:6837`)
  - `escape_linker_noop_class` (`:6864`)

  The defaults are **not** a one-line fix, because changing them alters freeze-off runs (the flag says so). The campaign-side fix is narrow: **the W6 preset sets every no-op class of any mechanism it enables to the stay class explicitly, and asserts it.** Whether the defaults change is a `/governance` + user decision that follows GFLAG-0508's per-run supersession review.
- **F3.** GFLAG-0484: the MECH-468 relational dumps (A/C/D/E, ree-v3 `c4d6a92`) have zero production callers.
  - The owed small fix is to mark them instrumentation-only in their docstrings, so no evidence reads them as a consumer.
  - The campaign does not use them.
  - The typed-vs-collapsed discrimination stays not runnable. That is `/governance`'s disposition.

## 9. Decisions the user still owns (none taken here)

1. **A1 regime:** tie-break ON in every arm (recommended; otherwise benefit is structurally unreachable), or the default env.
2. **A1 numbers:** seeds per stratum (5+5), the absolute floors, 3,000 closed-loop steps. All are drafts here.
3. **The codec contingency:** if W1 (b)-(d) cannot be met, switch to action-space proposals, or stop.
4. **If C2 fails (W5 parked):** run A1 without grounded valuation (its criteria would then be expected to fail P2 on benign seeds, per three independent tests), or hold the campaign.
5. **After merge:** whether the integrated preset ever becomes default-ON (a separate decision).

## 10. Resume ritual

1. Re-read section 2.
2. `git -C ree-v3 fetch && git -C ree-v3 log --oneline origin/main..origin/integration/coupled-loop-repair` (once BR0 exists).
3. Check the active claims on this plan's resources (`task_claim.py check`).
4. Take the first `ready` row whose "blocking on" is satisfied, and update its row in the same commit as its result.

Decision log entries are appended below, newest last.

### Decision log

- 2026-09-25T10:31Z: plan v1 written (bt0925-campaignplan). Implements Q2, Q4a-d, 7b-7d and Q1 as recorded in the synthesis. P2 corrected: C1 was not on origin/main at `276d9a51a9`.

## User decisions on this plan (2026-09-25T10:41:23Z; answered live in orchestrate-20260924-breakthrough)

| Plan question | User decision | Ledger |
|---|---|---|
| Env tie-break flag in the acceptance runs | **ON in every arm**, so benefit reward is attainable and the acceptance test can detect benefit-seeking, not only harm avoidance | rec-20260925-b4355023 |
| If the whole-codec repair cannot meet its gates | **Pursue BOTH action-space proposals and the codec repair in parallel, and let the evidence decide** (the user's own wording). The proposal workstream therefore carries two arms with a pre-registered head-to-head against the same acceptance criterion; neither is a fallback. | rec-20260925-6a675285 |
| If V3-EXQ-1105a fails validation | **Run the acceptance without grounded valuation**, recording that any reward gain is uncalibrated. The grounding-shuffled control still guards against spurious gains. | rec-20260925-805f605c |
| Draft acceptance numbers (5 trapped + 5 benign seeds; margins 2x SD of NATIVE-vs-reseeded-NATIVE deltas with absolute floors; 3,000 closed-loop steps per arm) | **Accepted as drafted.** Lock them into the pre-registration when the acceptance run is designed; the /queue-experiment smoke re-measures cost first. | rec-20260925-7e7e9825 |

Still open: whether the integrated preset ever goes default-ON after merge. Decide at merge time.
