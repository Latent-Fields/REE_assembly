**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml, experiment_queue.json, or ree-v3/experiments/. No experiment was queued.**

# MECH-033 GOV-FANOUT-1 discrimination portfolio -- design audit, BLOCKED on two comparator decisions

- Produced by: headless science session `science-20260925-orchc-mech033-fanout` (worktree `metaworker-science-20260925-orchc-mech033-fanout`, host `ree-cloud-5`), 2026-09-25.
- Chip: `chip-20260924-mech033-fanout-portfolio` (left OPEN / unclaimed; see resolution note).
- Source spec: `REE_assembly/evidence/planning/failure_autopsy_gflag0452-D2-cluster_2026-09-24.json`, `targets[5]` (`V3-EXQ-308`), key `fanout_recommendation`.
- Governance ratification: 2026-09-24, user decision `rec-20260924-a796e485`; MECH-033 `active -> provisional`, 308 `supports -> non_contributory`.
- Pre-flight: AMBER by `orchestrate-20260924-1707`, 2026-09-25T02:01:28Z, with three named build-time checks.

**Outcome: no script written, nothing queued.** Two of the pre-flight's three named AMBER caveats
were checked against the live tree FIRST, as the brief requires, and **both are real**. Under the
consent rule that is a STOP, not something to design around. Legs 2 and 3 of the portfolio are
sound and buildable as specified; legs 1 and 4 have comparator problems that would reintroduce the
exact confound the portfolio exists to remove.

---

## 1. Premise audit (re-measured, not assumed)

| Premise (as carried by chip / pre-flight) | Re-measured 2026-09-25 | Verdict |
|---|---|---|
| Work not already done | `grep '308a\|kernel_chain\|MECH-033\|fanout' ree-v3/experiment_queue.json` -> 0 hits (queue holds 3 items); `git -C ree-v3 log --all --since=2026-09-20 --grep=...` -> no portfolio commit | HOLDS -- owed work |
| MECH-033 moved to `provisional` | `claims.yaml` MECH-033 `status: provisional`, `epistemic_category: standard`, `live_status.evidence.from = failure_autopsy_gflag0452-D2-cluster_2026-09-24#V3-EXQ-308` | HOLDS -- status half of the routing already landed |
| 308's "k=3 chain" is one action + forced STAY | `experiments/v3_exq_308_mech033_kernel_chain_discriminative.py:520-522` -- `a_oh[ACTION_DIM - 1] = 1.0` after the first rollout step | HOLDS |
| 308's NO_CHAIN comparator is uniform random | same file, eval loop `else: action_idx = random.randint(0, ACTION_DIM - 1)` | HOLDS |
| `HippocampalModule` exists | `ree_core/hippocampal/module.py:134` | HOLDS |
| E2-scramble / untrained-E2 toggle does not exist | `grep -rn 'scramble\|untrained_e2\|randomize_e2' ree_core/ experiments/` -> 0 hits (only `v3_exq_034`'s **identity** ablation) | HOLDS -- must be built |
| SELF_CHAIN may be random-level degenerate | **CONFIRMED DEGENERATE** -- see sec 2 | CAVEAT #1 IS REAL |
| A full-REEAgent HarmHead-only-greedy (k=0) path exists or is buildable | **NOT BUILDABLE AS SPECIFIED** -- see sec 3 | CAVEAT #2 IS REAL |

---

## 2. BLOCKING FINDING A -- SELF_CHAIN is measured at random level; leg 4 has no valid comparator

`fanout_recommendation.suggested_probes[3]` (axis `instrumentation`, H1) specifies the leg as
"rollouts seeded by E2 action-conditioned kernels vs seeded by **random kernels** at matched CEM
budget (the V3-EXQ-055 AO_CHAIN vs SELF_CHAIN design, **with SELF_CHAIN first checked for
random-level degeneracy**)". The spec asks for that check. It comes back positive.

From the recorded manifest
`REE_assembly/evidence/experiments/v3_exq_055_mech033_kernel_chaining/v3_exq_055_mech033_kernel_chaining_20260320T191345Z.json`:

| metric | AO_CHAIN | SELF_CHAIN | RANDOM | SELF as % of RANDOM |
|---|---|---|---|---|
| `harm_per_step` | 0.0014672 | 0.0684271 | 0.0754013 | **90.8%** |
| `contact_rate` | 0.0011 | 0.0527426 | 0.0605405 | **87.1%** |
| `cal_gap_approach` | 0.7338 | **0.0213** | -- | below 055's own 0.03 calibration floor (C4) |

SELF_CHAIN is within ~9% of uniform-random on the DV and is uncalibrated by 055's own C4
threshold. It is therefore the *same class* of comparator as 308's uniform-random NO_CHAIN: it
removes planning competence wholesale rather than isolating E2 seeding. Using it as leg 4's null
would inherit the D2 ablation confound under a new name. (Single seed, seed=0 -- also not
replicated.)

`_cem_in_self_space` (`experiments/v3_exq_055_mech033_kernel_chaining.py:84-146`) is why: it rolls
out in `z_self` via `agent.e2.rollout_with_world(..., compute_action_objects=False)` and scores via
`agent.residue_field.evaluate_trajectory`. The CEM *budget* is matched, but the space carries no
harm-relevant action-consequence structure, so the arm is planning-shaped noise.

**The spec's literal comparator, "random kernels", is under-specified and admits one sound and one
degenerate reading:**
- (A-i) *untrained / re-initialised E2* supplying kernels -- outputs are still **action-conditioned**, so CEM can still rank candidates. Non-degenerate. But this makes leg 4 the same manipulation as leg 3, differing only in architecture (full REEAgent vs inline).
- (A-ii) kernels replaced by **action-independent noise** -- CEM scores become action-invariant. Degenerate, same failure as sec 3.

Which of these leg 4 measures is not specified anywhere, and it determines whether leg 4 is a
valid H1 test or a restatement of the confound.

---

## 3. BLOCKING FINDING B -- the k=0 "HarmHead-greedy" arm cannot rank actions; leg 1's null is rejected by construction

`suggested_probes[0]` (axis `representation`, H3) specifies: "k=0 arm: **HarmHead-greedy over
current z_world/z_self (no E2)** at matched training vs KERNEL_CHAIN; null: KERNEL_CHAIN harm_rate
not below k=0 by the 0.01 bar."

Every harm readout in the tree is **state-only, with no action input**:

- inline 308 architecture: `HarmHead.forward(z_world, z_self)` -- `v3_exq_308_...py:179-186`, `nn.Linear(world_dim + self_dim, 1)`. No `action_dim` term.
- full REEAgent: `E3Selector.harm_eval_head = nn.Sequential(nn.Linear(world_dim, hidden), ReLU, nn.Linear(hidden, 1), Sigmoid)` -- `ree_core/predictors/e3_selector.py:436-442`. `z_world` only.

With **zero** E2 forward steps there is no action-dependent quantity to score, so the harm score is
identical for all five candidate actions. The arm degenerates to a constant (or arbitrarily
tie-broken) action policy. In an 8x8 `CausalGridWorldV2` with 3 hazards and env drift, a
constant/tie-broken policy performs at or below uniform random.

**Consequence: leg 1's null ("KERNEL_CHAIN harm_rate not below k=0 by >= 0.01") is rejected by
construction.** Any competent planner beats a constant-action policy by more than 1 pp. That is
precisely the D2 confound the portfolio was commissioned to remove -- re-entering the portfolio as
leg 1.

This is not a speculative reading. The substrate already records it, in the one existing experiment
that ablated E2's forward step: `experiments/v3_exq_034_arc025_engine_ablation.py:22, 33` --
*"e2_ablated -- E2.world_forward replaced by identity (returns z_world unchanged, ignoring action)
... PREDICTION: attribution_gap ~ 0 (all actions predict same z_world)"*. Removing E2's
action-conditional forward step is known to make action ranking impossible.

### Three candidate H3 arms exist. None is the literal spec.

| Option | What it is | Status in tree | Cost of the substitution |
|---|---|---|---|
| **B-i** `DIRECT_CRITIC`: action-conditioned harm head `HarmHead(z_world, z_self, a) -> harm`, trained on observed `(state, action, harm)` in the SAME warmup, greedy over 5 actions | one-line widening of 308's `HarmHead` input (`+ ACTION_DIM`) plus its training target | does not exist; trivial to build | adds a trained component the spec does not name; "matched training" must be redefined; and H3's own wording is *"HarmHead **reading the current state**"*, which this contradicts |
| **B-ii** drop leg 1; let leg 3 (E2-scramble) carry H3 | leg 3 is already labelled `H1 vs H3` in the spec | buildable (sec 4) | portfolio drops to 3 legs; H3 is then tested by degradation-of-E2 rather than by absence-of-E2 |
| **B-iii** `ActorCriticPolicy` as the no-E2 arm -- a model-free actor over `z`, trained toward `R_t = benefit_eval - harm_eval` | `ree_core/action_learning/actor_critic.py:81` (`ActorCriticPolicy`), `:215` (`select(z, deterministic)`) | EXISTS in substrate | different *mechanism* (policy-gradient RL, not greedy readout); "matched training" between a greedy planner and a PG actor is not well-defined -- a new confound |

---

## 4. Legs that ARE sound and buildable as specified (no decision needed)

**Leg 2 -- axis `algorithm`, H2 vs H1.** "k=1 vs k=3 with policy-driven (not forced STAY)
continuation, same HarmHead; null: k=3 not below k=1."
- Both arms take >= 1 E2 forward step, so both are action-dependent. **Non-degenerate.** Null is falsifiable in both directions.
- The fix to 308's bug is exact and local: at rollout steps 2..k, re-select the continuation action by the same harm-minimising rule instead of writing `a_oh[ACTION_DIM - 1] = 1.0` (`v3_exq_308_...py:520-522`).
- E3 deep-rollout confound (Worker D: >98% of across-candidate score variance from rollout steps >5): k<=3 sits inside the non-confounded shallow band. Not a threat to this leg.

**Leg 3 -- axis `integration`, H1 vs H3.** "E2-scrambled arm (E2 weights shuffled or untrained,
HarmHead and planner intact) -- the claim's own specified manipulation; null: scrambled-E2
harm_rate within 0.01 of intact."
- A scrambled (randomly re-initialised or weight-permuted) E2 still produces **action-conditioned** outputs, so candidate ranking remains well-defined. **Non-degenerate.** Null falsifiable both ways.
- This is also the manipulation `claims.yaml` MECH-033 `what_would_answer` itself names ("Ablate the E2-kernel-to-hippocampal handoff ... while leaving rollouts and E3 scoring otherwise intact").
- Build note (pre-flight (d), mutation hazard): deep-copy E2's parameters before scrambling; do not mutate the shared module in place if arms share a process.
- Does not exist yet as a flag (`grep` -> 0 hits); `v3_exq_034`'s identity ablation is the nearest precedent and is NOT the same manipulation (identity is action-invariant; scramble is not).

---

## 5. Recommendation put to the user

**Portfolio of 3 legs, not 4, plus one comparator substitution:**

1. **Leg 2 as specified** (k=1 vs k=3, policy-driven continuation) -- H2 vs H1.
2. **Leg 3 as specified** (E2-scramble, planner + HarmHead intact) -- H1 vs H3.
3. **Leg 4 with comparator (A-i)**: full REEAgent + `HippocampalModule`, AO kernels vs **untrained / re-initialised E2** kernels at matched CEM budget. Carry SELF_CHAIN as a third *informational* arm with its degeneracy stated, never as the null.
4. **Leg 1 (k=0): option B-ii -- drop it**, and let leg 3 carry H3.

Reason for the recommendation: it removes both degenerate comparators without inventing a trained
component the spec does not name, and it keeps every remaining null falsifiable in both
directions. The cost is that H3 is tested by E2-degradation rather than E2-absence.

If the user prefers H3 tested by genuine absence-of-E2, **B-i** (`DIRECT_CRITIC`) is the better of
the two remaining options -- it stays a greedy one-step readout, so "matched training" is still
meaningful -- but it *does* change H3's own statement from "HarmHead reading the current state" to
"action-conditioned harm readout", and that rewording should be ratified, not assumed.

**Do not re-letter V3-EXQ-308** (chip instruction + autopsy: a single re-letter inherits the
shared-comparator confound). Whatever is chosen should take fresh queue ids.

---

## 6. Coordination note (not a scientific finding)

`task_claim.py check --resources ree-v3/experiments/ ree-v3/experiment_queue.json` returned exit-3
whole-file contention on `ree-v3/experiment_queue.json` against two peer science sessions
(`metaworker-science-20260925-orchc-arc023-recording` 01:31:00Z -- OWNER;
`...-contamination-probe` 01:31:50Z). Both peers had ALSO opened granular per-queue-id claims
(`ree-v3/experiment_queue.json/V3-EXQ-1098`, `/V3-EXQ-1099`) and their work is already committed as
WIP on `ree-v3` (`b0b2b523`, `43fb9e9f`). The contention is an artifact of the orchestrator opening
coarse whole-file claims for several concurrent science sessions in the same batch. **It became
moot here** -- this session stops before queueing and never touches the queue file. Flagged because
the next batch will hit it again: the coarse claim is what collides, and the granular
`experiment_queue.json/<QUEUE_ID>` form the peers used is what avoids it.
