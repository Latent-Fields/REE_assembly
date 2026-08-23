# V3-EXQ-947 design + a pre-run finding: MECH-314b's live per-candidate path has ZERO argmin authority at default curiosity weights

**Date:** 2026-08-23
**Chip:** chip-20260823-mech314bc-2x2-diversity-validation
**Driver landed:** `ree-v3/experiments/v3_exq_947_mech314b_percandidate_2x2_diversity_validation.py`
**Queue entry:** NOT appended -- see section 6.

**Headline: with the SD-063 head fully trained (216 P1 updates, 5-class relative
spread 1.76-2.15, i.e. inside the keystone's trained band) and the candidate pool
saturated (4.93 of 5 distinct first actions), turning MECH-314b's live
per-candidate path ON changes the committed action on ZERO of 320 paired ticks --
at BOTH diversity floors. The proposer-diversity ceiling is not what is holding
314b back at default weights. Something downstream of it is.**

---

## 1. What this chip was asked to do

Follow-on 1 of `mech314b_first_action_diversity_spike_2026-08-23.md`: design and
queue the MECH-314b per-candidate live-path validation as a 2x2 (314b ON/OFF x
candidate-pool diversity floor default/raised), with distinct-first-action count
as a mandatory covariate, gated on the corrected readiness assertions from
`sd063_online_head_training_keystone_2026-08-22.md` sections 4-5.

The driver was written, smoke-tested, validator-clean (`validate_experiments.py
--strict`, 0 warnings) and landed. The queue entry was not appended (section 6).

## 2. The design, and the two places it departs from the brief

**Load-bearing DV is YOKED, not free-running.** The ON agent is stepped on the
OFF agent's trajectory, so both see an identical observation sequence and every
tick is a paired argmin comparison at an identical world state. A free-running
comparison compounds after the first divergence and measures behavioural
sensitivity, not per-tick argmin influence; it is recorded as a secondary,
explicitly non-load-bearing diagnostic.

**Readiness gates on a 5-CLASS head probe, not the latched `get_state()` value.**
`e2_world_uncertainty_last_pvar_relative_spread` reports the spread over
whatever batch was last passed in -- which on an ON arm is the CANDIDATE POOL,
i.e. the floor manipulation itself. Reading it would make the readiness
statistic arm-dependent and non-comparable to the keystone's untrained
(0.14-0.26) / trained (1.81-2.37) bands. The driver instead evaluates
`predictive_variance` on all `action_dim` one-hots at a single z_world, which is
arm-independent by construction. Measured values land squarely in the keystone's
bands, which is the independent re-measurement keystone section 4 asked for.

## 3. THE INSTRUMENT DEFECT THIS SESSION FOUND AND FIXED

The first draft yoked the two agents but let them share one global torch RNG
stream. Two agents stepped alternately from one stream interleave their draws,
so the second never sees the state the first saw -- and since E3 selection
samples via `torch.multinomial`, two agents with **identical** configuration
diverge for purely stream-positional reasons.

Negative control, yoking an arm against ITSELF (divergence must be 0):

| control | shared stream (before) | private streams (after) |
|---|---:|---:|
| OFF vs OFF, floor 2 | **19 / 80** | **0 / 80** |
| OFF vs OFF, floor 5 | **37 / 80** | **0 / 80** |
| ON vs ON, floor 2   | 10 / 80 | **0 / 80** |
| ON vs ON, floor 5   | (n/a)   | **0 / 80** |

Each `_Runner` now snapshots and restores its own generator state around every
tick, episode reset and residue update. **The control now runs IN-RUN, per floor
and per 314b level, as a readiness precondition
(`paired_control_is_bit_identical`)**, so a regression in the isolation fails the
gate rather than silently returning a confident number.

**This invalidates one figure previously reported from the 2.5a probe.** That
probe's "15/60 committed-action differences at floor 5" was a FREE-RUNNING
comparison. Under the yoked design with correct RNG isolation the same
configuration gives 0. The free-running figure does not survive the pairing
control and must not be cited as evidence that 314b moves behaviour.

## 4. THE FINDING: zero argmin authority, with every precondition green

Real training budget (4 episodes x 80 steps = 320 ticks, `warmup_steps=100`),
seed 71, `CausalGridWorldV2`, ree-v3 at `cf9aa86`:

| floor | distinct first-action classes | head 5-class rel spread | head P1 steps | pcv cross-candidate rel spread | **yoked divergence** |
|---:|---:|---:|---:|---:|---:|
| 2 (default) | 2.278 | **2.1476** | 216 | 0.1623 | **0 / 320** |
| 5 (=action_dim) | 4.934 | **1.7584** | 216 | 0.6036 | **0 / 320** |

Read the columns together, because that is what makes this a real result rather
than a null run:

* the head is **genuinely trained** -- 216 P1 updates, exactly the keystone's
  figure, and a 5-class relative spread inside its trained band (1.81-2.37),
  an order of magnitude above the untrained band (0.14-0.26);
* the candidate pool is **saturated** -- 4.934 of 5 distinct first actions,
  reproducing the spike's 4.98 and removing the proposer ceiling entirely;
* the per-candidate vector **carries real cross-candidate span** -- 0.6036
  relative spread, so the manipulation is emphatically NOT a uniform additive
  constant and is therefore not annihilated by the argmax (the V3-EXQ-604c
  failure class does not apply here);
* and the committed action **still never changes**.

So every readiness precondition the ARC-065 section-5 gate asks for is GREEN,
and the DV is exactly zero. Under the driver's pre-registered routing this is
`evidence_direction: weakens` for MECH-314b with a green gate -- a genuine
negative result carrying claim evidence, NOT a `substrate_not_ready_requeue`.

**Most likely mechanism, NOT yet measured -- this is a hypothesis, flagged as
such.** `curiosity_uncertainty_weight` defaults to 0.05 and `curiosity_bias_scale`
to 0.1, while the head's predictive variances are ~1e-4 to 1e-3. The resulting
`last_uncertainty_dev_range` measured ~1.5e-05 -- plausibly orders of magnitude
below the spread of the other E3 score channels, so 314b's deviation would be
arithmetically incapable of moving an argmin regardless of how well the head is
trained or how diverse the pool is. **This has not been confirmed** and no
comparison against the other channels' magnitudes was run.

## 5. Consequence for the experiment as briefed

The 2x2 as specified would spend its full compute budget to return a determinate
`weakens`, because the effect is already zero at n=320 on both floors. That is a
real finding, but it is not the most informative use of the run.

**Recommended amendment, for a human to accept or reject:** keep the 2x2 and add
a third axis on the ON arms -- `curiosity_uncertainty_weight` (or
`curiosity_bias_scale`) at its default plus 2-3 escalating levels -- converting a
determinate null into a dose-response that answers "at what authority does 314b
become selection-relevant, and is that authority defensible against the shared
clamp's total-budget argument". Note this runs directly into the **unratified**
section-4 budget-split question in
`mech314bc_percandidate_extension_staged_2026-08-08.md` (the user declined to
ratify static per-flavour weights on 2026-08-22 and routed it to
`curiosity_budget_split_eligibility_design_2026-08-22.md`, which recommends
Design B). A dose sweep would supply exactly the missing measurement that design
pass is gated on -- but it is a scope change beyond this chip's brief, so it is
recommended here rather than queued.

Per the standing rule, the amendment must NOT be implemented by lowering
`YOKED_DIVERGENCE_FLOOR`: a pre-registered threshold that provably fails is a
design-time proof, and lowering it would convert a detected artifact into a
citable result.

## 6. Why no queue entry was appended

`ree-v3/experiment_queue.json` is held by an ACTIVE `TASK_CLAIMS.json` claim,
`worktree-agent-a53b125a2ecbdbfa7`, opened 2026-08-23T05:45:43Z. That claim
belongs to this chip's own ORIGINAL `spawn_task` worker, which opened it 15
seconds before the chip was even recorded in `TASK_CHIPS.json` and then did
nothing further -- no worktree, no process, no commits, on any box. `task_claim.py
open` arbitration correctly refused this session (exit 3), as it refused the two
preceding re-dispatches.

This is already raised as decision chip
`chip-20260823-taskclaims-orphaned-claim-blocks-mech314bc-validation` and is NOT
re-raised here. Closing another session's work claim is not a call this session
may make on its own judgment. The claim ages past the 6h staleness threshold at
2026-08-23T11:45:43Z, after which `task_claim.py` arbitration excludes it
automatically and the append can proceed normally.

**The queue entry is therefore the one piece of the brief not delivered.** The
driver is landed, smoke-tested and validator-clean; appending the entry is a
single `/queue-experiment` step 5-8 pass once the claim clears.

## 7. Scope held

This session did not: append the queue entry (section 6); close or modify another
session's TASK_CLAIMS entry; change any `claims.yaml` field on MECH-314b, Q-044
or ARC-065; touch `ree_core/` (the driver is experiment-side only); or implement
the section-5 dose-axis amendment (section 5, recommended not built).

## 8. Re-derive brake (MOVE-3), recorded

MECH-314b's brake count is 3 (>= threshold 2): `failure_autopsy_604a-624a-630`,
`failure_autopsy_gapA-cluster-604b-648a-649`, `failure_autopsy_V3-EXQ-604c`. The
brake is **RELEASED**: the named upstream substrate in 604c's
`recommended_substrate_queue_entry` is the ARC-065 Phase-2 per-candidate
extension ("give uncertainty and learning-progress the same per-candidate
treatment"), which landed 2026-08-08 and became live with SD-063 online training
on 2026-08-22 (ree-v3 `88287f11c6`). MECH-314c is NOT released (its source,
MECH-482's `epistemic_deficit` accumulator, is unbuilt) and is deliberately not
tagged by this experiment.

## 9. Substrate-path overlap gate (skill step 2.5c), recorded

Three open `corrupting` `substrate_queue.json` entries name files this driver's
agent imports at module level. `mode-governance-engagement`
(`SalienceCoordinator.tick`) and `MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION`
(`agent.py::run_sws_schema_pass`) are not in this driver's causal path -- no
mode-governance knob is enabled and no sleep pass is ever run.
`contextmemory-write-path-addressing-degeneracy` (`e1_deep.py`
`ContextMemory.write`) IS potentially in path via E1, but applies identically to
every arm and interacts with neither factor, so it biases the load-bearing
contrast toward the null rather than toward a false positive. Recorded in the
manifest's `custom_information.substrate_defect_note`. **A reviewer who disagrees
with that judgment should treat it as a stop, per the skill's literal reading.**
