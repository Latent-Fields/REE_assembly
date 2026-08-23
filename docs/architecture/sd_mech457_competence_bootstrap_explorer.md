---
title: "Substrate: mech457_competence_bootstrap_explorer"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 29
---

# Substrate: mech457_competence_bootstrap_explorer

**Substrate id:** `mech457_competence_bootstrap_explorer` (composition primitive; no SD-NNN number -- lives in `experiments/_lib/**`, not `ree_core`)
**Subject:** `action_learning.competence_bootstrap_explorer`
**Status:** IMPLEMENTED
**Registered:** 2026-07-16
**Depends on:** `sd_actor_critic_action_learning` (ree_core/action_learning/actor_critic.py, IMPLEMENTED), SD-056 (IMPLEMENTED), MECH-229 VALENCE_WANTING reward channel (agent.actor_critic_reward, IMPLEMENTED), ARC-065 / MECH-314 curiosity-novelty substrate (RND class, landed)
**Blocks (unblocks on validation):** MECH-457 (candidate / v3_pending), INV-088 (candidate / pending_substrate_reconfirmation)

## Problem

The MECH-457 GOV-FANOUT-1 discrimination is CLOSED across five diagnostic autopsies (V3-EXQ-751 through 756). No SINGLE mechanism and no PAIRWISE combination clears the 1.0 foraging-competence floor toward the 48.05 local-view competence ceiling:

- **752 H-credit** (prioritized backward credit-replay), **753 H-return** (Go-Explore archive+reset_to), **754 H-curriculum** (IMGEP/AMIGo goal-frontier), **755 H-mode** (critic-utility explore/exploit gate) -- all collapse to ~0.15-0.45 @D3 (sub-floor, ~= sparse-RL baseline), except H-mode's RND arms which clear the floor but whose arbitration gate adds nothing.
- **756 H-credit x H-return PAIR** -- forages 0.20 z_world / 0.32 raw, `pair_gain_over_best_single` -0.05 / -0.017 (NEGATIVE super-additivity), below even the sparse baseline.
- **751 H-optim** (unsupervised RND explorer) -- the SOLE floor-clear (5.22), but only ~11% of the 48.05 local-view ceiling.

Readiness is MET (env solvable from the 5x5 local view: local-view greedy 48.05, greedy oracle 57.2), so this is a genuine action-learning competence-implementation gap, NOT an env/observability limitation.

**The wall is one structural property with two joined halves** (`failure_autopsy_MECH-457-fanout-755_2026-07-15` cluster read), not an unfound mechanism:

1. **Cold-start / success-dependence (752-754, 756).** Backward credit needs a successful trajectory to propagate from; Go-Explore needs interesting states to archive; AMIGo needs an achievable frontier that carries gradient; the pair combines two such converters. All amplify signal DERIVED FROM PRIOR TASK SUCCESS, so they cannot bootstrap from ~0. Only the two SUCCESS-INDEPENDENT classes -- RND novelty (751, 5.22) and BC imitation (748, 32.72, needs an expert) -- break the floor.
2. **Capacity to convert (755).** Even a competent explore/exploit arbitration GATE over a success-independent drive squeezes no more competence from a low-capacity explorer. The ceiling is the explorer's CAPACITY to convert coverage into competence -- RND reaches only ~11% of the local-view ceiling -- not the way exploration is scheduled.

Every fanout CONVERTER (752 credit, 753 return, 756 pair) ran on the SPARSE base -- no dense drive -> nothing to convert. The genuinely-untested, highest-composition build is the RND success-independent drive COMPOSED WITH a converter, plus adequate budget and a developmental explore->exploit anneal.

## Solution

`experiments/_lib/mech457_bootstrap_explorer.py` -- a composition of ONLY landed pieces (honours the SYNTHESIS.md duplication objection; SYNTHESIS.md rejected building another novelty module):

| Piece | Source | Diagnosis half |
|---|---|---|
| RND success-independent dense drive | `mech457_explorer_classes.RNDModule` (Burda 2018; == ARC-065/MECH-314) | Half 1 -- the off-floor generator |
| first-class RPE actor-critic | `ree_core/action_learning/actor_critic.ActorCriticPolicy` via `RepAgent` (z_world cotrain AND raw 5x5) | the policy taught |
| prioritized backward credit-replay | `mech457_explorer_classes._prioritized_credit_replay` (Mattar&Daw 2018 + Foster&Wilson 2006), NOW fed by RND-generated successes | Half 2 -- converter |
| **training-progress intrinsic-coef/entropy anneal** (NEW) | `linear_anneal` -- a DEVELOPMENTAL schedule `coef_start->coef_end` over `anneal_fraction` | Half 2 -- consolidation |
| increased training budget | `n_episodes` above the 1000 that plateaus RND | Half 2 -- capacity |

The **new primitive** is the developmental anneal: a training-progress schedule (NOT the critic-utility `ModeGate` 755 refuted -- that gate is downstream of competence and cannot manufacture it). LC-NE explore/exploit consolidation (Aston-Jones & Cohen 2005; Daw 2006) instantiated as an ontogenetic schedule that hands coverage off to the extrinsic forage reward as competence rises.

`train_a2c` (the shared fanout trainer) gains two OPTIONAL, no-op-default hooks -- `coef_schedule` / `entropy_schedule` -- computed per episode as `fn(ep, n_episodes)`. Default `None` -> constant (byte-identical to the pre-existing 752-756 callers, confirmed: 1428 tests pass). Mutually exclusive with `mode_gate`.

### Config (no-op default = OFF = 751 RND plateau)

`BootstrapExplorerConfig` defaults reproduce the 751 RND-explorer arm: `use_rnd=True`, constant `intrinsic_coef` 1.0 (`anneal_fraction=0.0`), constant entropy 0.10, `credit_replay=False`, `n_episodes=1000`. `make_off_config()` / `make_on_config()` give the validation ablation pair (ON: coef 1.0->0.05, entropy 0.10->0.03 over 60% of training, credit-replay on, 3x budget).

### Data flow

```
env obs -> RepAgent.encode (z_world cotrain OR raw 5x5)
        -> ActorCriticPolicy.select (action)
        -> env.step -> shaped reward = harm + FORAGE_BONUS + count_novelty + coef_t * RND(z_next)
                                                                   (coef_t from linear_anneal)
        -> GAE + single A2C backward (+ prioritized credit-replay on reward-bearing episodes)
        -> [unshaped foraging_competence eval @D3]
```

## Architecture Context

The training UPDATE lives in `experiments/_lib` (as `actor_critic.py` mandates and as the 752-756 fanout mechanisms do), so each `(config x representation x seed)` cell folds into the arm_fingerprint `substrate_hash` via the `experiments/_lib/**` glob and can be emitted reuse-eligible. No `ree_core` change: the actor-critic, RND, credit-replay, and MECH-229 reward channel all already exist -- the missing primitive is the composition + anneal + budget.

MECH-094: N/A (no memory writes on simulated / non-waking ticks). Phased training: N/A (no new encoder head).

## What This Substrate Enables

- A NEW diagnostic validation EXQ (via `/queue-experiment`) arming OFF (RND plateau) vs ON (composed bootstrap) x {z_world cotrain, raw 5x5} for `foraging_competence @D3`. Load-bearing: ON mean > ~13.05 res/ep (lift >= 7.83 above the 5.22 plateau) on a strict majority of seeds, toward BC 32.72.
- The re-derive brake (fired 3x on the single-axis fanout) is SATISFIED once this upstream substrate is built: the retest is a genuinely-distinct composed-mechanism question, not a same-claim bolt-on.
- On a validation PASS: MECH-457 competence-implementation gap resolved (governance-gated) and the INV-088 V3-EXQ-750 strategy-diversity readout can re-run on matched-competent unsupervised policies (both representations).

## Related Claims

MECH-457 (mechanism_hypothesis; candidate; v3_pending), INV-088 (invariant; emergent; candidate / pending_substrate_reconfirmation), MECH-229, SD-056, ARC-065, MECH-314. Grounding lit: `evidence/literature/targeted_review_action_learning_bootstrap_class_choice/SYNTHESIS.md`.
