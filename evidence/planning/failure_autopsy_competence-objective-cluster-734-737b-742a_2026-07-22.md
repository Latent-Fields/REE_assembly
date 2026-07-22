# Failure autopsy — competence-floor cluster: V3-EXQ-734 / 737b / 742a

**Scope:** cluster (3 targets). **Status:** confirmed (user-adjudicated 2026-07-22).
**Generated:** 2026-07-22T03:48:30Z.
**This document promotes and demotes nothing.** It produces a diagnosis and a routing recommendation; `/governance` applies them.

---

## 0. Why these three are one autopsy

All three sit on the `_train_all_on_agent` driver family, share the D0→D3 difficulty
ladder and the same reference band (floor 1.0, random_walk 0.933, local_view_greedy
48.05, greedy_oracle 57.2), and all three FAILed the same load-bearing DV: **D3
foraging competence vs the 1.0 floor**. They are the live gate of the
`conversion_ceiling_root` question and the outer wall of `competence_floor`.

They are **not** three independent bugs. Two of them are a valid convergent
measurement; the third is invalid for a reason that must not be allowed to
contaminate the other two.

---

## 1. Facts reconstructed

### 1a. Recording provenance — complete on all three

`recording_schema: rec/v1`, `substrate_hash`, `machine_class`, `elapsed_seconds`,
full `config` and explicit `seeds` present on every manifest. **No recording debt.**
Every number below was already in the manifests; nothing here required a re-run to
observe. (This is the 780 lesson holding: the discriminator was recorded and simply
had to be consumed.)

### 1b. The z_world encoder guard — the discriminator between the three

| Run | Timestamp | `encoder_moved_in_p0` | Verdict |
|---|---|---|---|
| **V3-EXQ-734** | 2026-07-21T08:43:55Z | **false, all 4 rungs × 4 seeds** — `0 of 61` latent_stack tensors, `0 of 4` world_encoder tensors, `world_encoder_max_abs_delta 0.0` | **INVALID** |
| **V3-EXQ-737b** | 2026-07-21T19:38:27Z | **true** — `7 of 61` latent_stack, `4 of 4` world_encoder, `max_abs_delta 0.103` | **VALID** |
| **V3-EXQ-742a** | 2026-07-21T16:14:24Z | **false in P0 on every arm**; the two `cotrain` arms moved it during the actor-critic phase (`max_abs_delta_ac 0.166`, 6/6 cells) | **cotrain arms VALID, frozen arms INVALID** |

The SD-070 adoption commit `b523b9c` ("wire the z_world encoder warmup into the
`_train_all_on_agent` family") landed **2026-07-20T20:00:11+01:00**, i.e. *before all
three runs*. 737b picked it up; 734 and 742a's P0 did not. This is the per-copy
defect already recorded on `substrate_queue` entry `sd_zworld_warmup_optimizer_group`
(status `implemented_pending_validation`, priority 1, unblocks MECH-457 / INV-088 /
Q-002) — the same shape as the V3-EXQ-728 record, where the driver defines its own
`_train_all_on_agent` copy. **The substrate entry's `implemented_pending_validation`
status is therefore correct and its validation is NOT complete: 728b validated it on
one driver, 734 and 742a demonstrate two more that the adoption did not reach.**

### 1c. The load-bearing numbers (D3, hazard-free, oracle-achievable)

| Policy | D3 foraging competence | vs floor 1.0 | vs random 0.933 |
|---|---|---|---|
| `greedy_oracle` | 57.2 | ✅ | — |
| `local_view_greedy` (738 denominator, same 5×5 field the encoder senses) | 48.05 | ✅ | — |
| `random_walk` | 0.933 | ✗ | — |
| `ree_bias_head` | 0.533 | ✗ | **below random** |
| `ppo_raw_obs` (737b) | 0.567 | ✗ | **below random** |
| `ppo_ree_latent` (737b, guard GREEN) | 0.233 | ✗ | **below random** |
| `actor_critic_cotrain_plain` (742a, encoder trained in AC) | 0.233 | ✗ | **below random** |
| `actor_critic_cotrain_sf` (742a) | 0.217 | ✗ | **below random** |
| `actor_critic_frozen_plain` / `frozen_sf` (742a, invalid) | 0.200 / 0.267 | ✗ | below random |

737b's own manifest already flags it: `criteria_non_degenerate.ppo_ree_latent_beats_random_floor_at_d3: false`.

### 1d. The survival column — the reason

From 734 `per_rung_report.D0_baseline_724`:

| Policy | foraging_competence | survival_horizon |
|---|---|---|
| `greedy_oracle` | **6.04** | **20.4** |
| `vanilla_ppo` | 0.36 | **175.0** |
| `ree_trained_allon` | 0.09 | 65.7 |
| `random_walk` | 0.23 | 11.3 |

`mean_episode_reward` for random_walk is **−1.006**. The oracle — the policy that
*defines* competence on this yardstick — survives **20.4** steps. Vanilla PPO
survives **175.0**.

---

## 2. The diagnosis

**A trained learner scoring below random walk is not a capacity ceiling.** Under a
capacity or representation ceiling a learner asymptotes *toward* the anchor from
below and plateaus; it does not end up systematically worse than acting at random on
a task a same-observation greedy solves at 48.05. Every learner here was **worse than
random at foraging and far better than the oracle at surviving.**

Vanilla PPO is **8.5× better than the greedy oracle at surviving** and **17× worse at
foraging**. The oracle dies fast *precisely because* it charges resources. So the
return these learners maximise is dominated by episode survival, and survival is
maximised by not foraging. **Every learner is optimising the objective it was given
correctly. The objective is not the foraging objective the DV scores.**

This is the fourth account that none of the three interpretation grids contains:

> **The task the reward defines and the task the DV scores are different tasks.**

Corroboration from the other side of the same programme — **V3-EXQ-792 / 780**: an
imitation-installed raw_view policy reaches **20.933** post-BC and decays to
**11.667** under unconstrained RL refinement, but holds at **0.778–0.871** when the
update is KL-anchored to the installed snapshot. The policy class demonstrably *can*
represent competent foraging on this observation interface. **RL refinement actively
destroys it.** That is exactly what an objective whose optimum is "survive, do not
forage" predicts, and it is not what a representation or capacity ceiling predicts.

### Why the alternative readings do not fit

- **`ree_substrate_ceiling`** (734's grid) requires "vanilla PPO forages the de-risked
  env on the SAME observation interface but REE cannot". PPO recovered only at D2 and
  `ppo_beats_random_at_d3` is **false**. The premise fails.
- **`learner_or_observability_ceiling`** (734's grid) is the row the numbers nominally
  select, and it routes to `/implement-substrate` **on the observation encoding**.
  That is the mis-route this autopsy exists to prevent: 738/792/780 have already shown
  the observation interface carries the information (local_view_greedy 48.05 on the
  same 5×5 field; BC installs 20.9 from it). Building a better encoder cannot fix a
  policy that is correctly declining to forage.
- **Substrate ceiling on the REE representation** — 737b is the fair test (guard
  green, real trainable PPO head on a genuinely prediction-trained z_world) and its
  raw-obs control fails identically. The failure does not discriminate the
  representation.

---

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear → not tested** | MECH-457 (742a) was not given conditions where it could express itself: the contrast is between two learners both facing an objective that penalises the behaviour scored. `weakens` is not earned. |
| Biological reference | **clear — and the failure is the biological prediction** | Foraging in mammals is governed by a *patch-leaving / risk-sensitive foraging* trade-off (marginal value theorem; Charnov). An animal in a hazardous patch with an unbounded survival term and a small consumption term correctly reduces foraging. The observed policy — long survival, near-zero intake — is what a real forager does under high perceived predation risk. This is **not** a translation failure; it is the mechanism working on a mis-set parameter. |
| Prerequisites | **present** | Oracle and local-view anchors clear the floor at every rung; env is achievable. |
| Implementation completeness | **partial — confirmed defect** | `sd_zworld_warmup_optimizer_group` has NOT reached the 734 and 742a driver copies. Two more per-copy strikes beyond the 737/728 records. |
| Environment adequacy | **wrong pressures — DOMINANT LAYER** | The env supplies a survival/harm pressure that dominates the consumption pressure at the training horizon. `mean_episode_reward` −1.006 for random walk; oracle survival 20.4 vs PPO 175.0. |
| Measurement adequacy | **adequate for detection, blind for attribution** | `foraging_competence` and `survival_horizon` were both recorded — the inversion was visible in the manifest all along. What is missing is a **reward decomposition** (per-term return attribution), without which no run in this family can say which term the learner is actually maximising. |
| Integration adequacy | coupled | — |
| Scale / capacity | **adequate — ruled out** | BC installs 20.9 on the same policy class and observation interface. Capacity is not the binding constraint. |

**Recommended `epistemic_category`: `measurement_test_design_defect`** for the two
valid targets (the training objective and the scored DV are different tasks, and no
run in the family decomposes the return), and
**`competence_implementation_gap`** for V3-EXQ-734 (untrained encoder, run invalid).

**NOT `substrate_ceiling` on any of the three.** Recorded explicitly so the re-derive
brake count for MECH-457 is not inflated by a reading this autopsy does not make.

---

## 4. Cluster pattern

| Experiment | Claim | Negative-control / absolute criterion | Discrimination criterion | Read |
|---|---|---|---|---|
| V3-EXQ-734 | — | oracle 6.04–57.2 vs floor 1.0 ✅; D0 incompetence reproduces ✅ | no learner recovers at any rung; PPO only at D2 ✗ | invalid (encoder untrained) |
| V3-EXQ-737b | — | oracle ✅, bias-head reproduces deficit ✅ | ppo_ree_latent 0.233 and ppo_raw_obs 0.567 both sub-floor and sub-random ✗ | valid — objective, not representation |
| V3-EXQ-742a | MECH-457 | oracle + local-view both rungs ✅; bias-head sub-floor contrast holds ✅ | no actor-critic arm clears; cotrain vs frozen indistinguishable ✗ | valid on cotrain arms — objective, not action-learning |

**Independent bugs or one structural property?** **One structural property**, plus one
independent implementation defect.

- The structural property: *every* absolute / negative-control criterion passes and
  *every* discrimination criterion fails, across three structurally different
  learners (bias-head, actor-critic, PPO) and two observation interfaces (raw obs,
  z_world). A failure that is invariant across learner *and* representation is a
  property of neither. It is a property of the **objective they share**.
- The independent defect: the SD-070 encoder-warmup adoption has not reached two of
  the three driver copies.

**Both readings stay live and are pre-registered as such** — see §6.

---

## 5. Learning extracted

1. **The forage-vs-survive inversion is quantified, not merely noted.** Vanilla PPO
   survives 8.5× longer than the greedy oracle while foraging 17× less. This is the
   first run in the programme where the survival column was read alongside the
   competence column, and it reverses the reading of the competence deficit.
2. **A learner below the random-walk anchor falsifies "ceiling" readings by
   construction.** Adopt this as a standing lint: any `substrate_ceiling` /
   `learner_ceiling` self-route on a cell scoring below its own declared random-policy
   floor should be refused at the manifest level. The information was present in
   734/737b/742a and in every predecessor; nothing consumed it.
3. **`sd_zworld_warmup_optimizer_group` is `implemented_pending_validation` and its
   validation is INCOMPLETE.** 728b validated one driver; 734 and 742a are two further
   copies the adoption did not reach. The per-copy `_train_all_on_agent` duplication
   is the root, and it will keep producing silent random-projection runs until the
   copies are collapsed onto one path.
4. **Recording debt: none. Consumption debt: yes.** Every discriminating number
   (`survival_horizon`, `mean_episode_reward`, the guard's per-cell deltas) was
   already in the manifests. The gap is that no criterion *reads* them. Same lesson as
   the 780 note (`bc_warmstart_action_match_recent` recorded and unconsumed).
5. **A reward decomposition is missing from the whole family.** No run records
   per-term return attribution, so "which term is the learner maximising" is
   unanswerable from any existing manifest. This is a **measurement** gap (the metric
   was never computed), not a recording gap.
6. **`H-policy-learning` must NOT be eliminated on this evidence.** 737b was its live
   gate and it returned a null — but a null produced under an objective that penalises
   the scored behaviour does not discriminate the policy-learning axis. Eliminating it
   here would be the "confident-but-wrong verdict on a laundered artifact" that
   GOV-FANOUT-1 exists to prevent.

---

## 6. Repair pathway

**Node classification:** `complex (probe-gated) / puzzle (known rules)` — the frame is
well-posed (we know what a return decomposition is and how to measure it); a fact is
missing (which term dominates). Plus one `complicated (buildable)` sub-node (collapse
the driver copies onto the SD-070 path).

**Re-derive brake:** counted under the R1–R3 convention for every claim in scope.
`MECH-457` = **0** confirmed `substrate_ceiling` hits across 19 autopsy targets;
`MECH-440`, `MECH-163`, `MECH-204`, `SD-076` = 0. **The brake does NOT fire** on any
target here, and this autopsy adds no ceiling reading to any of them.

**Granularity-debt recurrence:** MECH-457 now carries **19 prior confirmed autopsy
targets** across 8 distinct autopsy files, with structurally different failure
signatures each time (representation, exploration, credit, curriculum, arbitration,
drive-schedule, reward-coupling, credit-horizon, BC-prior, approach-primitive,
retention, and now objective). **The recurrence trigger FIRES.** A claim that has
absorbed 19 autopsies without resolving is a claim that is several claims. Surfaced as
a `/claim-synthesis` recommendation independent of this autopsy's own routing.

### Routing

| Target | Routing | What |
|---|---|---|
| **V3-EXQ-734** | `/queue-experiment` — same-question re-run, alphabetic suffix (**734a**) | Sole change: run on the SD-070 encoder-warmup path with the guard GREEN-GATING (not detection-only) so an untrained encoder refuses the cell rather than reporting it. No conclusion may be drawn from 734 as it stands. |
| **V3-EXQ-737b / 742a** | `/queue-experiment` — **new EXQ number**, new question | The **return-decomposition diagnostic**: hold the learner fixed, record per-term return attribution (survival / harm / consumption / proximity) alongside `foraging_competence`, and sweep the consumption:survival weighting. Declared null: the consumption term already dominates at the training horizon and re-weighting does not move D3 competence → the objective is NOT the binding constraint and the observability route re-opens. |
| **cross-cutting** | `/implement-substrate` — **amend** `sd_zworld_warmup_optimizer_group` | Add the two new failure records (734, 742a) and record that the adoption is per-copy incomplete. The fix is to collapse the duplicated `_train_all_on_agent` copies onto the single SD-070 path, not to patch each copy. |
| **MECH-457** | `/claim-synthesis` | Granularity-debt recurrence, 19 targets, distinct signatures. Proposal-first decomposition into testable children. |

### Draft `evidence_quality_note` for MECH-457 (governance to write — do not apply here)

> 2026-07-22 (V3-EXQ-742a actor-critic ON/OFF, evidence, claim_ids=[MECH-457];
> failure_autopsy_competence-objective-cluster-734-737b-742a_2026-07-22). The recorded
> `weakens` is **WITHDRAWN and revised to `non_contributory`**. All four actor-critic
> arms scored 0.200–0.267 D3 foraging competence — **below the run's own declared
> random-walk anchor of 0.933** — while the greedy oracle scored 57.2 and a local-view
> greedy reading the same 5×5 field scored 48.05. A learner below its own random floor
> has not been shown to lack a mechanism; it has been shown to be optimising something
> else. 734's survival column quantifies it: vanilla PPO survives 175.0 steps vs the
> greedy oracle's 20.4 while foraging 17× less, so the return is dominated by episode
> survival and survival is maximised by not foraging. V3-EXQ-792/780 corroborate from
> the other side — a BC-installed raw_view policy reaches 20.933 and decays to 11.667
> under unconstrained RL but holds at 0.778–0.871 under a KL anchor, so the policy
> class demonstrably can represent competent foraging and RL refinement destroys it.
> The MECH-457 contrast was therefore not tested under conditions where it could
> express itself. Additionally the frozen-encoder arms of 742a ran on an untrained
> z_world (`encoder_moved_in_p0 false` on every arm; `sd_zworld_warmup_optimizer_group`
> adoption did not reach this driver copy). MECH-457 stays `candidate` / `v3_pending`;
> `pending_retest_after_substrate` set. NOT a substrate_ceiling reading.

---

## 7. Frozen-ledger delta (Step 9b)

Question **`conversion_ceiling_root`**:

- **Pre-register** new leg `H-objective-misspecification`, axis `reward`, as **labelled
  fan-out growth** (invariant 3a): `initial_frozen_count` 4 → 5,
  `initial_frozen_count_at_registration` preserved at 4, `fanout_growth_events[]`
  entry naming this autopsy, `pre_registration_source` set on the leg.
- **`H-policy-learning`**: stays **`alive`**. Record `resolving_runs`
  `[V3-EXQ-737b, V3-EXQ-742a]` and the basis, but the elimination bar is NOT met —
  a null produced under a mis-specified objective does not discriminate this axis.
- **`H-substrate-ceiling`**: stays **`alive`**, unchanged. Its recorded adjudicating
  run V3-EXQ-734 is now known invalid (untrained encoder); the leg was already `alive`
  so no state moves, but the basis is corrected.

**Circling disclosure — read this before treating the growth as progress.** `reward`
maps to family **`world`**, and `H-reward-balance` (also `world`) is already
**eliminated** by V3-EXQ-735. This growth therefore re-enters a family that has a dead
leg, and `build_hypothesis_space.py` will classify it as **circling**. That
classification is *accepted, not dodged*: the honest axis for this leg is `reward`,
and inventing a fresh axis label to escape the family check would be the dead leg
wearing a new name — exactly what the convergence check exists to catch.

Why it is nonetheless a genuinely new leg, stated so a reader can dispute it:
`H-reward-balance` asked whether **re-weighting reward terms lifts committed-action
diversity** and was tested on the *diversity* DV. This leg asserts something
structurally different — that under the given weighting the **optimal** policy is not
to forage at all, on the *foraging-competence* DV — and rests on evidence
(survival 175.0 vs oracle 20.4; BC-install-then-RL-decay) that did not exist when 735
was adjudicated. If a reader judges that distinction too fine, the correct remedy is
to merge this leg into `H-reward-balance` and re-open that elimination, **not** to
re-label the axis.

`fanout_growth_note` recorded on the question: this campaign has now taken a growth
event on a family with an eliminated member. It has not converged.

---

## 8. Confirmed routing (user-adjudicated 2026-07-22)

The user selected **"Objective mis-specification"** over the `learner_or_observability_ceiling`
reading and over holding both as co-equal rivals — with the explicit instruction that
`H-policy-learning` is not to be eliminated. This document reflects that adjudication.
