# REE breakthrough integration pass -- synthesis (2026-09-24 17:03Z -> 2026-09-25, orchestrate-20260924-breakthrough)

**Status:** synthesis of one overnight orchestrator pass. Everything below is from small Mac probes at world_dim=32 (the deployed value) unless stated; domains are stated per finding and are not inflated. Nothing here is a claim promotion; all registry consequences were routed to /governance as flags (GFLAG-0479, 0481, 0484-0491).

## 1. The one-sentence result

The native closed learning loop is **not closed inside ree_core**: at REEConfig defaults the agent does **no waking gradient learning at all** (census: 0 optimizers, 0/717k parameters moved in 40 train-mode ticks), every trained parameter is trained by a *driver*-built optimizer, and no driver recipe trains everything the agent reads when it acts. Every broken edge found tonight is a local symptom of that single structural fact.

## 2. The edges, in loop order (what was believed / what was measured / domain / record)

| Loop link | Believed | Measured | Domain | Record (REE_assembly) |
|---|---|---|---|---|
| observation -> z_self -> consumer | DR-13 GRU trains via E1/E2 z_self losses | Nothing trains it (E1/E2 see detached copies). Even trained, **no valuation consumer reads z_self**: 0/68 E3 ticks, 0/12 episodes changed action under z_self intervention; z_world canary moved 4-30% | D3 (negative) for z_self->selection; D2 at E1 | zself_causal_reach_trace_20260924.md (884a6b1ca3); build landed ree-v3 863d23d |
| observation -> z_world -> consumer | untested rung on CURRENT_FRONT | **z_world D2 REACHED** at E1 and E3 selection (which content, not established) | D2 | same |
| candidate generation | terrain prior / monostrategy = z_world under-differentiation | Proposals are state-invariant (same first-action class at every state). Root: the hippocampal `action_object_decoder` is **never trained anywhere** (dead-optimizer pattern in ~13 drivers). Training it alone FAILS (pre-registered, 5 seeds): the proposal edge is a **codec with three coupled defects** (untrained decoder; unbounded decode fed to E2 as the action; first CEM iteration samples ~12x off-range) | D0 (trace) + D2 (probe, FAIL) | monostrategy_type_a_vs_b_discrimination_20260924.md (948d58cd3e); action_decoder_training_trace_20260924.md (622716398d4); action_decoder_training_causal_probe_20260925.md (a369f411ff8) |
| repertoire: absence vs access collapse | open (dynamic-coordination thought) | **Type A at generation**; no ecology in ree-v3 satisfies the Type-B prerequisites (>=2 useful strategies + switching required). Dynamic coordination has **not earned a build** | D1/D2 | 948d58cd3e |
| prediction of alternatives (E2 world) | E2 rollouts inform E3 | E2 world head has **no waking objective** (untrained in >= half of recent drivers); even trained it is action-blind at chance **because the agent's own one-action behaviour starves it of action coverage** (a fresh head on action-diverse data works: k>=10, executed-action pick 0.74-0.82 on PCA-32); the encoder is a secondary ceiling (~half the action signal lost) | D1/D2 | e2_rollout_divergence_and_proposal_state_dependence_20260924.md + addenda 1-3 (f300ebf64d, 2d848ca2d3, ca212aff26, 1b09b81b4d) |
| native evaluation/ranking (E3) | E3 ranks by predicted consequence | >98% of E3's across-candidate score variance comes from rollout steps >5 (action-uninformative); a depth-1 read of E3's own scorer tracks true consequence, the full horizon does not. Commitment itself (ARC-016 gate) runs on E2's one-step world error | D2 | same; GFLAG-0485, GFLAG-0486 |
| evaluation -> grounded value | trained evaluators suffice | Env benefit shaping never fires (hazard wins the tie); with it enabled the benefit head trains and beats a shuffled control 3/3, but harm rises 3-5x: **nothing calibrates E3's main channels against grounded outcome** (commensurability only equalises spread -- noise gets a vote; ARC-108 gating is unarmed here and reweights only modulatory channels from an evaluator proxy) | D3 on env reward | e3_evaluation_edge_test_20260924.md + addenda (4ea0931b0f, 7f852bcf4b, 8ab5ce6fc1, 5e3c956b41) |
| experienced consequence -> learning | ree_core learns online | **At defaults, no waking gradient learning.** harm_eval_head (read every E3 tick, commented 'TRAINED') untrained in 4/5 recipes; the all-ON recipe (14/69 recent drivers) trains no E1 and no E2-self; the beta/theta/delta depth stack random in 4/5 and added into z_world/z_self every sense() | D1 (reach) | gradient_reach_census_20260925.md (940c690c9dd); GFLAG-0491 |
| residue (MECH-018) | GFLAG-0441 sampling fix repairs integrate() | Fix landed (ree-v3 3230cd56, default OFF) and is correct as geometry (target/peak ~1.5e-05 -> ~0.61) but **D1 only**: consumers query 12-121 widths from the trained shell; consumer response indistinguishable from a shuffled control; avoidance weakened/reversed | D2 (negative) | residue_consumer_reach_world_dim32_20260924.md (82819a1058); GFLAG-0479 |
| relational memory (MECH-468/469/470) | typed-vs-collapsed now testable | MECH-468 dumps have **zero production callers**; the only native relational consumer (SD-097 topology) is single-type, default-off, never enabled; discrimination NOT runnable | D0 | relational_edge_consumer_reach_20260924.md (410e589ce1); GFLAG-0484 |

## 3. What was falsified tonight (pre-registered where marked)

- **R5b + R2 as a harm repair** (use_action_class_scaffold_candidates + _score_depth_limit=2): positive on 2/3 seeds in addendum 3, **FAILED a pre-registered 5-fresh-seed replication** (harm better 1/5; R2 necessary 0/5 and harmful in the mean; earlier 2/3 came from hazard-trapped starts). r5b_r2_fresh_seed_replication_20260924.md (fc987f3b057); GFLAG-0489 corrects GFLAG-0487.
- **Decoder training alone** as the proposal repair: **FAILED pre-registered criteria P and C** (a369f411ff8; GFLAG-0490).
- **Class-balanced replay** as the E2 coverage repair: fails (missing classes cannot be reweighted into existence); exploration coverage works.
- **Grounded-valuation battery as first designed**: its reward-hacking (harm-floor) detector missed the positive control; the pre-registered repair FAILED on fresh seed 45 -- stop rule honoured; a relative-to-null detector is owed (grounded_channel_valuation_frontier_design_20260924.md 50b679abb8 + addenda 941d7aa571, 13621d6db8, 28ebf56955).
- **Three independent tests** (addendum 3 arms, the replication, the decoder probe) showed **proposal diversity without a grounded evaluator is undirected** -- it buys harm on benign starts.

## 4. The structural reading

The failures are **coupled**: proposals need a decoder/codec; E2 needs action coverage from proposals; E3 needs informative (shallow or fixed) rollouts and grounded channel worth; and all of it needs a native learner that ree_core does not have. Each single-factor repair tonight either did nothing or exposed the next defect it had been masking (the untrained decoder masked the unbounded decode; the dead benefit channel masked the missing channel calibration). This is the "partition before factorial rescue" boundary: the parts are now partitioned and named; **validating them one at a time in the native regime is not possible**, because each depends on the others.

## 5. Recommended next (for the user and /governance -- decisions held, not taken)

1. **A native waking trainer, owned by ree_core** (census option a): a per-module optimizer set with a **grad-reach guard** (every module in an optimizer must receive gradient -- naive Adam(all) reproduces a 32% dead-optimizer share). This is the root the other rows hang off.
2. Then a **coupled repair campaign on an ree-v3 integration branch** (CLAUDE.md's sanctioned exception): whole-codec repair (or action-space proposals), E2 world-head action coverage, and grounded main-channel valuation (the relative-to-null detector first), validated together against a pre-registered closed-loop criterion on env reward with shuffled controls and hazard-trapped/benign stratification.
3. Registry rows owed via flags: z_self valuation consumer (0481), codec (0488/0490), native trainer / harm_eval_head / depth stack (0491), E2 world objective (0485), commit-gate caveat (0486).
Held questions with options: .scratch/breakthrough-20260924/QUESTIONS.md (umbrella; copied into the WORKSPACE_STATE landing entry).

## 6. Process notes

- Workers: 11 Mac subagents (A-K) + 1 resumed cloud lander; every launch has a dispatch_campaigns launches[] row; all chips resolved.
- Decisions taken under the user's standing delegation (rec-20260924-fb429c72), reasons recorded: z_self objective = body forward model; the valuation smoke and detector re-validation; every probe above. Decisions held: see Section 5.
- Two parallel orchestrators ran overnight on a split (this one: causal edges; orchestrate-20260924-1707: decision lane + cloud science), mutual restarters; one overnight window reconciled to 6 cycles/box.
- Harness hazards seen: a push-retry repeatedly left a staged revert on evidence/planning/igw_routine_log.md (cleared index-only each time); one task_claim open silently failed to register; two workers created worktrees at a relative path inside ree-v3 (cleaned up).

## 7. User decisions on the held questions (2026-09-25T06:15Z, live; addendum 06:22Z)

The user answered the four held questions from Section 5 and `.scratch/breakthrough-20260924/QUESTIONS.md` in a live AskUserQuestion. All four took the recommended option. The recommendation ledger records them as rec-20260925-3677487d, rec-20260925-6eb5db00, rec-20260925-35999055 and rec-20260925-713b2cb7.

| Q | Question | User decision | Consequence for /governance |
|---|---|---|---|
| Q4a | Native waking trainer architecture | **Hybrid WakingTrainer.** Existing phased trainers (SD-070 P0, ZSelfP0) become scheduled members, with per-tick online losses only for the REINFORCE heads. It is stepped from `update_residue()` every K ticks, so every StepHarness driver gets it with no driver edit. | GFLAG-0491 (MECH-523): the owed substrate_queue row is the WakingTrainer per native_waking_trainer_design_20260925.md (0c0f5b76ec). |
| Q4b | Sequencing | **Skeleton + a harm_eval_head loss on ree-v3 main, default-OFF, first.** Then the coupled repair on an `integration/<slug>` branch, gated by the pre-registered closed-loop criterion (design section 4c: env reward, shuffled controls, hazard-trapped/benign stratification). | The main-branch step is in progress (campaign-20260925-bt0925-wtrainer). The guard itself is landing as a pure instrument first (campaign-20260925-bt0925-guard). |
| Q2 | Repair organisation | **One coupled campaign:** codec repair + E2 world-head action coverage + grounded main-channel valuation + trainer ON, together on one ree-v3 integration branch, validated only as an integrated loop. The user accepts that single-factor probes cannot validate its parts in isolation. | GFLAG-0488/0490 (SD-080, ARC-018): fold the decoder/codec rows into the coupled campaign, not a decoder-only row (the decoder-only probe FAILED, a369f411ff8). GFLAG-0485 (E2 world objective) belongs in the same campaign. |
| Q1 | Grounded valuation | **The 5-seed cloud battery** (~5 CPU-h; M2 regression-credit rule first, against the M4 null plus a raw-rule control), **conditional on the relative-to-null detector validating** (campaign-20260925-bt0925-nulldet, in flight). | GFLAG-0487 (INV-054, MECH-523): route to /queue-experiment only if the detector passes its pre-registration. If it fails, park. |

Decided by the orchestrator under the standing delegation (rec-20260924-fb429c72), with reasons. These two were NOT put to the user; both complete the accepted recommended set and are default-OFF and reversible:
- **Q4c:** world_obs_encoder is trained through the agent's actual read path (it is not allowlisted). This is relevant only to the coupled campaign.
- **Q4d:** the grad-reach guard RAISES when the trainer is ON; the existing drivers get a warn-only retro-audit.

**Unchanged by these decisions** (still open, for /governance on the evidence alone): GFLAG-0479 (residue D1-only), GFLAG-0481 (no z_self valuation consumer), GFLAG-0484 (relational dumps have no callers), GFLAG-0486 (commit-gate caveat) and GFLAG-0489 (correction to 0487). Q3 was resolved by evidence: do not adopt R5b+R2 as a default regime.

### 7b. User direction, 2026-09-25T07:29Z: Phase-0 babbling as the developmental source of action-diverse experience

The user directed that **Phase-0 babbling be incorporated as the developmental source (possibly THE source) of the action-diverse experience that trains the native world model (E2's world head)** in the coupled campaign (Q2).

Why this fits the evidence: E2's world head is action-blind because the agent's own one-action behaviour starves it of action coverage. A fresh head on action-diverse data discriminates actions (k>=10, executed-action pick 0.74-0.82 on PCA-32; f300ebf64d + addenda). Exploration coverage works; class-balanced replay cannot create missing classes. ARC-074 (candidate) already commits to a reward-free Phase-0 motor-babbling epoch, before any E3 scoring, that builds sensorimotor mappings.

Gap found (D0 code read, 07:29Z):
- Phase 0 exists only in the experiment drivers: `ree-v3/experiments/infant_curriculum.py` (InfantCurriculumScheduler, episodes 0-99 plus the H_pos exit gate) and `experiments/_lib/infant_warmup.py`. Neither is in ree_core.
- Per `infant_warmup.py`'s docstring, it is "plain random-policy stepping with no training of any kind"; the scheduler varies only novelty_bonus_weight, residue_scale_factor and offline_integration_frequency.
- So the action-diverse experience ARC-074 describes is generated at Phase 0, and nothing learns from it. It is the same dead-loop shape as the census (940c690c9dd).
- MECH-277 (action-space discovery) is a different, V4-scoped mechanism and is not implied here.

Consequences for the coupled campaign:
1. The WakingTrainer's E2-world member takes its developmental training data from a Phase-0 babbling epoch.
2. The babbling epoch becomes a ree_core-owned developmental stage (or at minimum a trainer-consumed source), not a driver-only scheduler setting.
3. OPEN puzzle, being measured now (campaign-20260925-bt0925-babble): does a babbling-trained E2 head STAY action-discriminative once the agent's own on-policy behaviour collapses to one action? The answer decides between a one-off developmental epoch, a retained babbling replay (developmental memory), or a standing babbling floor.

### 7c. User direction, 2026-09-25 ~09:37Z: retained developmental memory needs ACh-gated freeze/unfreeze

Context (INTERIM, not verdicts): the babbling probe (campaign-20260925-bt0925-babble, record babbling_e2_action_coverage_probe_20260925.md when it lands) has three seeds in so far (106-108).
- Before the post-babbling phase, structured high-diversity babbling (L2) gives the E2 world head the best action discrimination.
- Continued on-policy (near one-action) training mostly erases that lead.
- Retaining 25% babbling replay (L2R) PRESERVES it: retention 1.31 and 1.38 on the two seeds run so far.
- The native Phase-0 generator was near-monostrategy on 2 of 3 seeds (entropy 0.23-0.36), so "babbling" as implemented is not reliably diverse.
Final verdicts are pending.

The user's direction: the retained developmental memory should be FROZEN (protected from being overwritten by later one-action experience) but able to be UNFROZEN and updated later. The user identified this with acetylcholine's control of plasticity.

This maps onto existing claims (D0; code read 09:37Z):
- MECH-083 (candidate): ACh as the meta-level plasticity gain governing durable write vs read-through.
- MECH-398 (candidate; implementation_phase v4, v3_pending): an ACh-analog basal-forebrain plasticity-gain scalar in [0,1] multiplying encoder learning rates and residue write magnitudes. NOT implemented anywhere in ree_core (grep 09:37Z).
- MECH-207 (candidate, v4): ACh as a permissive write gate. Prediction error destabilises and updates a stored hippocampal trace only when cholinergic activation co-occurs. This is the reconsolidation or "unfreeze" half.
- MECH-453 (candidate, v4): cholinergic TAN-pause plasticity windows.

Consequence for the coupled campaign (Q2) and the WakingTrainer (Q4a):
- The WakingTrainer (skeleton building, campaign-20260925-bt0925-wtrainer) is the first ree_core component that OWNS learning rates, so it is the natural native host for MECH-398's gain.
- A retained developmental replay (babbling memory) needs two states: FROZEN (retained, low or zero plasticity) and UNFROZEN (reopened when surprise and the ACh-analog gain coincide, per MECH-207).
- Without the unfreeze, retained memory cannot be revised as the world changes. Without the freeze, one-action behaviour overwrites it (the L2 result above).
- This becomes a design requirement of the coupled campaign, not a separate build: the trainer's replay member carries a per-memory frozen flag and an ACh-gated destabilisation rule.
- /governance should consider whether MECH-398 (and MECH-207's destabilisation rule) should be re-phased from v4 to v3 now that a v3 host exists (GFLAG raised).

Evidence domain: D0 (mapping) plus interim D1 (babbling probe). No ACh mechanism has been built or tested.

### 7d. Babbling verdict and user adoption (2026-09-25 ~10:20Z)

Final record: babbling_e2_action_coverage_probe_20260925.md (REE_assembly 0ac69c87446; pre-registration a9f323c92b1, amendment b47b019063, both before any registered seed).
- Existing Phase 0 is NOT babbling. It uses the agent's own action selection (`act_with_split_obs`), emits only 4 of 5 actions and trains nothing. It was less diverse than on-policy behaviour on 4/5 seeds. The `experiments/_lib/infant_warmup.py:14` docstring ("random-policy stepping") is wrong and owes a correction.
- S FAIL (1/5). DR FAIL (0/5). R and R3 CANNOT_DETERMINE. BEH null (predicted reward order held 0/5), so under the pre-registered rule the developmental dose-response claim is NOT supported at this scale.
- Structured babbling (class-balanced, persistent runs) beats on-policy data on 5/5 seeds before the post phase (+0.10 to +0.16 discrimination). It is not durable as a one-off (>= half the gain kept on only 2/5). With ~25% retained replay (L2R) it is kept on 5/5 seeds (ratios 1.31-1.53), in both strata.
- Domain: D1 (discrimination). D2 reach was measured but did not discriminate (the shuffled control moves E3 as often as the real head).

USER DECISION (rec-20260925-0ad0f56b): ADOPT, with L2R as the acceptance bar.
- The coupled campaign's WakingTrainer E2 world-head member uses a NEW structured babbling generator plus ~25% retained babbling replay.
- The retention mechanism to build is the ACh-gated freeze/unfreeze of section 7c.
- The L2R numbers are the member's acceptance bar.

USER DECISION (rec-20260925-372b6ca9): V3-EXQ-1105 PULLED before it started (coordinator /queue/remove, ~10:19Z, status pending -> removed, reason recorded). Its criterion N was non-falsifiable by construction: each null is a random walk scaled by D_W's own divisor sd_h, so every null's z is ~N(0,1). A noisy candidate rule would shield itself the same way. It is to be redesigned as V3-EXQ-1105a, with candidate-shaped nulls and a noisy-hacker positive control. The orchestrator's earlier option-B recommendation missed this; the flaw was caught by the queueing worker's red-team.

## 8. Afternoon 2026-09-25 (orchestrate-20260924-breakthrough-c2)

Window: 2026-09-25T11:30Z to ~14:55Z. Sources: the orchestrator's live log (`.scratch/breakthrough-20260924/QUESTIONS.md`, umbrella, entries from 11:30Z) and the records it cites. Every sha below was checked as an ancestor of its repo's default branch on origin at 14:5xZ. Times are UTC. **Nothing here is a claim promotion.** Registry consequences go to /governance through the flags in 8.5.

### 8.1 What landed (on origin)

**ree-v3 `main`**
- `e00d95da6a` (12:10Z): V3-EXQ-1105a queued. It supersedes 1105 and adds candidate-shaped M2 nulls plus a noisy-hacker positive control. Worker red-team fixes: F1 is a distinct both-missed label; F2 is a per-arm event-window floor of 20, a `null_identical_to_control` flag and CANNOT_DETERMINE branches. The primary, the nulls, the seeds and the thresholds are unchanged from the design. Record: REE_assembly `4f068a823a`.
- `5f965cf` (13:14Z): commit-latency fix P2/R4. The validation-cache record no longer inherits the outer commit's git env (`GIT_INDEX_FILE`), and the cache commit runs `--no-verify`. Fail-before tests are included.
- `1a61800c0c` (14:07Z): **MECH-157 option A**, mode-conditioned precision routing on z_world, default off. Contracts: 5742 pass / 0 fail; remainder: 1179 pass / 0 fail. The lander hit the R4 nested-gate bug live (12:08-12:41Z) and recovered index-only.
- `aa14769` (14:46Z): **MECH-287 option B**, PAG descending release: hippocampal anchor invalidation raises the PAG freeze-exit threshold. Default off.
- `67c7346` (14:51Z): V3-EXQ-1106 queued. It is the MECH-287b Stage-0 precondition gate, a diagnostic pre-registered in `mech287_anchor_freeze_exit_design_20260925.md` sec 6. Status at 14:52Z: on origin's queue file, not yet on the live-status board.
- `integration/coupled-loop-repair` was cut at `cc20be5` (C1, WakingTrainer skeleton) at 11:35Z (BR0). It has **no branch commits yet** and is now 7 commits behind main.

**REE_assembly `master`**
- A1 pre-registration: draft `2028729662` (12:40Z); red-team fold `b92196db2c` (12:58Z); plan row `48adc07e5f`/`bac11d4085`. v2 (with the user decisions and the action-space edits): skeleton `6d1face27d`, draft `c0939a9b4e` + `8fd30619b3`, plan row `6e868f88b0`. O3 folded in at `a5fbbcac2b` (14:40Z).
- Mode-switch + CeA mechanism trace: `e2bbd2a98e` (13:05Z).
- Action-space proposals design (W1-alt): `412882b845` (13:09Z), plan row `8acf3a3a4d`.
- N3-pre aggregation probe: pre-registration `7ba36ff63d` (13:35Z), results `d4bb6449b3` (14:17Z), plan row `2a01f4f849`, decision log `2ba75b0f60`.
- SP-CEM zero-continuation check: `4e7c42c5d7` (D0 trace), `4004f56dd2` (horizon correction), final `847544ac8e` (14:41Z).
- Coupled plan user-decision rows: `13f1ad5e7b`/`dc0bb0c1d2` (A1 answers), `5a761cf284` (U1), `a5fbc191d9` (O3). I1 status row: `c8a7569b6c`.

**REE_Working (umbrella) `master`**, the commit-latency work:
- Diagnosis `88f61a77b` (12:49Z): the full-suite box time is only ~16% used, and one full contracts run takes 32-37 min. Root causes R1-R6. R4 is a nested cache-record gate plus a `GIT_INDEX_FILE` leak, a trunk-contamination hazard that had not yet fired.
- P2/P6 (+ half of P5): `c8a92ea83`, docs `4e679d830`.
- P7, ree-cloud-5 as the resident test slot: `c80078035`.
- P4, a FIFO wait queue instead of refusal: `8e9b736b5`.
- P3, a short lane for targeted runs: `b6333dd25`.
- Docs: `7df239185`.

### 8.2 Findings (evidence domain per finding)

1. **Headline: E3's own valuation is at chance even on TRUE next states, so grounded valuation (W5) is the binding root for choice quality.** N3-pre's oracle read scored E3 on the true next state of each action class, with no world head and no aggregation involved. That pick landed in the env-Q-best set at 0.09 / 0.20 / 0.22 / 0.19 / 0.12, against chance ~0.20 (5 fresh seeds, 521-525). Even perfect one-step prediction does not choose on env consequence under the default E3 valuation: F penalises displacement, `harm_eval_head` is untrained, and there is no benefit channel.
   - Domain: **D1, post-hoc and not pre-registered.** It reproduces e3_evaluation ADDENDUM 3 point 3 on fresh seeds, now with an action-covered head.
   - The probe's own pre-registered verdict is **CANNOT_DETERMINE**: the shuffled twin was at chance on 3/5 seeds, against the 4/5 required. The oracle read does not depend on the twin. (`d4bb6449b3`)
   - Consequence: W4 gate (b) and the consumer-mediated (e) legs cannot pass before W5, whatever the aggregation or proposer.
2. **N3-pre, other readings.** These are PROVISIONAL: the head was a harness-trained proxy of the W3 member, and the result must be re-confirmed by N3 proper.
   - The proxy L2R head meets its bar on 5/5 seeds (disc4 0.470-0.547).
   - Steep aggregations make E3 track its own one-step consequence with the real head and not with the shuffled one: D1 on 5/5 seeds, DISC_0.5 on 4/5. D1 equals the habit read, so SD-081 forbids it, which leaves **DISC_0.5 as the lead**. FULL anti-tracks with the real head.
   - As specified, W4 gate (c) cannot discriminate: the INIT reference head diverges (t30 norm 238-940).
   - FIDW is FULL in disguise.
   - Domain: D1/D2 descriptive under a CANNOT_DETERMINE verdict.
3. **Mode switching (MECH-157 / EXP-0861 premise).** The trace was run on untrained agents, 3 seeds, at ree-v3 `23714f0`. (`e2bbd2a98e`; GFLAG-0554)
   - dACC off: the salience aggregate is identically 0, so no switch can happen. That is a **wiring** fault (D0 + D1).
   - dACC on: one switch per life, then the mode locks. `dacc_pe` is both the only salience source and the dominant internal_planning affinity, so within-life reversals are 0/0/0.
   - Adding the lineage's independent `use_external_task_drive` input raises reversals from 0/0/0 to 2/16/25 (**D2**).
4. **CeA interrupt (MECH-039 / EXP-0787 premise).** Same trace record and flag as finding 3.
   - CeA reads `affective_harm_encoder` (`|z_harm_a|`), not `harm_eval_head`. With the WakingTrainer ON, the encoder stayed bit-identical on 3/3 seeds, so training `harm_eval_head` cannot lift CeA (**D2**). This answers open question (a): NO.
   - The gate is a fixed 0.5 threshold on an unanchored magnitude. At init the latent sits ~3x under that threshold. After SD-011 `harm_accum` training it sits 25-35x over, tonically.
   - Even a forced fire cannot switch mode: 0.4 < 1.0, and switches stayed at 0/0/0 (**D2**).
   - Shared upstream: `dacc_pe` falls back to `||z_harm_a||`, which plausibly explains the lineage's dacc_pe ~16-17 that needed the affinity cap. That link is D0 plus an analogy, not re-trained.
5. **SP-CEM floor tokens lose on construction.** (`847544ac8e`; GFLAG-0555)
   - The default-ON tokens are one-hot at t=0 with exact zeros at t=1..29 (the from_dims horizon is 30), and E3 scores all 31 states (**D0+D1**).
   - They rank **last of 32 at 85/85 states** on 3 seeds (**D1**).
   - A majority-class token built the same way also ranks last, so the construction is the cause, not the class (**D2**).
   - Worker C's order-statistic mechanism is overturned; its descriptive finding stands.
   - Closed-loop consequence: not reached, so there is no D3.
   - The run used world_dim 16, not the deployed 32.
6. **Action-space proposals (W1-alt), design only, D0.** ASP-E is a parameter-free stratified one-hot first action plus a per-class categorical CEM. It sidesteps all three codec defects and the zero-vector continuations.
   - It does not fix W3, W4 or W5. Without them it is expected to reproduce R5b's undirected-noise signature.
   - The literal pool-containment gate (e) is degenerate for this proposer (1.0 by construction), so a consumer-mediated form was proposed. (`412882b845`)
7. **A1 noise floors (measured).** Per 100 steps: reward 0.90 benign / 2.4 trapped; harm contacts 1.6 / 4.8; benign reward change 0.92 (1.44 with the harm-bearing-seed correction); trapped rate 0.21.
   - New rule P1g: a benign gain must include fewer harm contacts or more consumption.
   - Open item RT-5: the floor came from a perturbed T2 agent, not a NATIVE reseed. (`2028729662`, `b92196db2c`)
8. **Fleet/process (infrastructure, measured).** Landing latency was dominated by contracts run 2-6x per landing, the absence of a queue, and the R4 gate bug. The bug fired live once, in the MECH-157 lander, and was recovered. (`88f61a77b`)

### 8.3 User decisions this afternoon (ledger rec-ids)

| Time (Z) | Decision | Ledger |
|---|---|---|
| ~13:25 | Accept the measured A1 floors (0.90/2.4 reward; 1.6/4.8 contacts) and P1g | rec-20260925-5fc6c256 |
| ~13:25 | Benign reward-change floor 1.44 (not 0.92) | rec-20260925-aa066e96 |
| ~13:25 | Hold A1 until both INT-CODEC and INT-ACT pass their member gates; run them head to head | rec-20260925-38b81685 |
| ~13:25 | Add the no-valuation diagnostic arms (~+20% cost) | rec-20260925-c2519d92 |
| 13:52 | U1 gate parity: add the consumer-mediated leg to BOTH W1(e) and W1-alt(e) | rec-20260925-b9652a9b |
| 13:52 | Capacity proposals P3 + P4 + P7 approved (built and landed, 8.1) | rec-20260925-01869834 |
| 14:38 | O3: both variants' consumer-mediated (e) legs move after W5 (reported, not gating); add an env-Q oracle diagnostic | rec-20260925-a16786f5 |

Spend directions, which have no rec-id:
- 11:31Z: run toward 100% weekly before the 18:00Z reset. The orchestrator's operating target was ~97%.
- 12:28Z and 14:28Z: keep work flowing and don't waste the last few percent.
- 12:34Z: investigate why commits are slow. That request produced 8.1's latency work.

The 10:4xZ plan decisions (tie-break ON rec-20260925-b4355023; codec and action space in parallel rec-20260925-6a675285; acceptance without valuation if 1105a fails rec-20260925-805f605c; draft numbers rec-20260925-7e7e9825) are recorded in the plan (`e469729d9b`) and are not repeated here.

### 8.4 Orchestrator decisions under the standing delegation (rec-20260924-fb429c72)

- **N3-pre follow-through** (plan decision log `2ba75b0f60`). These set gate definitions before the real N3 runs; no threshold was moved after a passing result.
  - W4 gate (c) is re-referenced to a trained action-blind head, because the init head diverges.
  - Gate (b) moves to after W5, because valuation caps it (8.2 finding 1).
  - The N3 twin becomes a fixed permutation, because resampled labels could not destroy the correspondence on near-monostrategy seeds.
- **Action-space design questions.**
  - U2: ASP-0 wins a tie within 0.05, because it is simpler.
  - U4: CEM elite window = W4's depth for both variants.
  - U5: BRANCH placement.
  - Reason for all three: the design's recommendations, all reversible. U1 went to the user (8.3). U6, the registry row, is held for /governance.
- **Launch policy.** Kept ~6 workers against a ~2.5-3%/h burn. At 14:20Z weekly usage was 95% and a stop was called. The user then asked not to waste the remainder, so three items were launched early from the post-reset queue (spcem, a1v2, modeq), with workers told to commit incrementally.
- **Queue write under contention.** 1105a was queued while the concurrent `governance-20260925` session held a whole-file claim on `experiment_queue.json`. The worker claimed only the queue id, per /queue-experiment, and it was uncontested.

### 8.5 Governance flags raised this afternoon (reported, not acted on)

- **GFLAG-0554** (stale_note, open; MECH-157, MECH-039, MECH-046, SD-032a). The premises used to park EXP-0861 and EXP-0787 are stale (8.2 findings 3-4). Raised by bt0925-modetrace (REE_assembly `0c0fa148c7`).
- **GFLAG-0555** (stale_note, open; ARC-065). SP-CEM floor tokens lose on construction (8.2 finding 5). The floor-token rebuild options (a)/(b)/(c) go to /governance. Raised by bt0925-spcem (`c9314d51ea`).
- Other 2026-09-25 flags still open on origin: GFLAG-0503, 0507, 0508 (this pass's no-op fix), 0515, 0531. The post-reset list (item 9) names this pass's governance-owned set.

### 8.6 Not landed / in flight at ~14:55Z, and the post-reset queue

In flight (active claims):
- **I1** lander (bt0925-landi1). Instruments were built and contracts ran green (5745 on cloud), but they are not on main. F1 rides with them.
- **T1 + W2a** (bt0925-t1w2a): not on main.
- **MECH-039** veto readout (bt0925-land039): parked on remote branch `origin/bt0925-mech039` @ `1b8422d`; not on main.
- **W1-alt** ASP-E build (bt0925-w1alt, + docs): no commits on the integration branch yet.
- **V3-EXQ-1107**, the trained-agent mode-switch run (bt0925-modeq): not yet queued.
- RT-5 native-reseed probe (bt0925-rt5).
- CeA gate calibration probe (bt0925-ceacal).
- bt0925-land287b is closing: build `aa14769` and queue entry `67c7346` are landed.

Running on the fleet at 14:51Z: V3-EXQ-1105a (ree-cloud-4, ETA ~1.9h), 1090, 1099, 1104, 1067. **W5a stays gated on the 1105a verdict**: the battery is queued only on PASS; on FAIL, A1 runs without grounded valuation (rec-20260925-805f605c).

The post-reset queue (after the 18:00Z weekly reset) is `.scratch/breakthrough-20260924/POST_RESET_20260925.md` (umbrella). Each premise gets re-measured first. In order:
- (0) liveness and relaunch of the workers above;
- (1) the I1 lander;
- (2) the mode-switch follow-up (now bt0925-modeq);
- (3) W3 on the branch after W2a, rebased onto main first;
- (4) N3 proper;
- (5) the W1 codec parts, with the consumer-mediated leg;
- (6) the A1 edits and the RT-5 closer;
- (7) the 1105a adjudication, then W5a only on PASS;
- (8)/(11) SP-CEM follow-ups (confirmed; next is a repeat at world_dim 32 with the full 1061 warmup before any default change, plus the ASP pool-format homogeneity check);
- (9) the governance-owned flags;
- (10) worktree GC for this pass.
