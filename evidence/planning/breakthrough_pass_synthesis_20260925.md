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
