# V3-EXQ-1056 REFUSED at `/queue-experiment` Step 2.5a -- SD-061's declared levers are not reachable at any config the registered design names

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml, substrate_queue.json or experiment_queue.json. No experiment was queued. No script was landed.**

- Session: `metaworker-science-20260918-sd061-mech343-q056` (headless, ree-cloud-5)
- Campaign: `science-20260918-sd061-mech343-q056`
- Chip: `chip-20260918-sd061-mech343-q056-proposal-entropy-upstream-leg`
- Generated: 2026-09-18T21:03:31Z
- Substrate read at: ree-v3 `origin/main` `f21a8c50`; REE_assembly `origin/master`
- Decision chip raised: `chip-20260918-sd061-lever-inertness-decision`

---

## 1. What was asked, and how far it got

Design, review, smoke-test and queue the UPSTREAM (proposal-layer) leg of the registered
Q-056 three-arm difficulty-gated proposal-entropy falsifier against the SD-061 substrate,
tagging `MECH-343`, `EXPERIMENT_PURPOSE="evidence"`.

Every pre-flight gate up to and including the empirical probe was run. The first four
passed. The fifth -- `/queue-experiment` **Step 2.5a (empirical confirmation, one-tick
probe)** -- failed, and it failed in the exact way that step exists to catch: *the doc
says IMPLEMENTED, the probe shows the feature is not reachable at runtime.*

| Gate | Outcome |
|---|---|
| STOP-CHECK (queued? already run? resources owned?) | PASS -- queue empty on `origin/main`; only prior SD-061 run is V3-EXQ-694 (readiness diagnostic, PASS 2026-06-19); narrow slot claim `ree-v3/experiment_queue.json/V3-EXQ-1056` opened clean (exit 0) |
| 2.4 GOV-REUSE-1 | PASS (run needed) -- see s.5 |
| 2.5 substrate readiness (doc) | PASS -- SD-061 is `implemented_pending_validation`, both modules present in `ree_core` |
| 2.5b re-derive brake (MECH-343) | PASS -- count 0, not braked |
| 2.5c substrate-path overlap | PASS -- see s.5 |
| **2.5a empirical confirmation** | **FAIL -- four independent findings below** |

---

## 2. Findings (all measured on ree-v3 `origin/main` `f21a8c50`, ree-cloud-5)

Probes: `ree-v3/experiments/_scratch/exq1056_feasibility_probe.py` and
`exq1056_probe3.py` (throwaway, untracked). Configuration in every probe:
`REEConfig.goal_stream(...)` (the canonical goal bundle), `CausalGridWorldV2`
(`size=8, num_resources=3, num_hazards=2, use_proxy_fields=True`), `alpha_world=0.9`,
sleep off, `z_goal` pinned, the agent selecting its own actions through
`act_with_split_obs` (i.e. a genuine ecological loop, NOT V3-EXQ-694's synthetic
hand-set `_last_stuck_score`).

### F1. SD-061's declared temperature lever has NO live consumer at any config the design record names

`differentiable_cem_temperature` has exactly ONE consumer in `ree_core`:

```
ree_core/hippocampal/module.py:2406   if getattr(self.config, "use_differentiable_cem", False):
ree_core/hippocampal/module.py:2416       float(getattr(self.config, "differentiable_cem_temperature", 1.0)),
```

`use_differentiable_cem` is SD-055 substrate and defaults **False**
(`ree_core/utils/config.py:2842`). Runtime confirmation:
`hippocampal.config.use_differentiable_cem = False` on a `goal_stream` agent built with
`use_difficulty_gated_proposal_entropy=True` at shipped defaults.

So `agent.py:6211-6213`, which is SD-061's temperature half, writes a value that nothing
reads, and `agent.py:6248`'s `finally:` restore restores a value that nothing read.

**This is not recorded anywhere.** `use_differentiable_cem` is named in NONE of:

- `REE_assembly/docs/architecture/sd_061_difficulty_gated_proposal_entropy.md` -- whose
  **Config** section enumerates all 13 SD-061 knobs and omits it, and whose data-flow
  block asserts `differentiable_cem_temperature *= gain` as an operative step;
- `ree-v3/docs/substrate/SD-061-difficulty-gated-proposal-entropy.md`;
- `claims.yaml` SD-061 `what_would_answer` -- whose criterion (2) states as MET
  ("V3-EXQ-694 C2, 3/3") that the regulator "adds exactly `extra` candidates **and lifts
  `differentiable_cem_temperature` transiently**";
- `claims.yaml` MECH-343 `what_would_answer` -- whose mandatory precondition is
  "DECLARE WHICH TEMPERATURE the entropy DV reads ... SD-061's regulator lifts
  `differentiable_cem_temperature` on the ARC-018/CEM PROPOSAL layer";
- `experiments/v3_exq_694_sd061_difficulty_gated_proposal_entropy_readiness.py`, which
  never sets it -- so **V3-EXQ-694's PASS certified the count-widening half only**, and
  its C2 "regulator load-bearing" criterion was (correctly, by its own comment) gated on
  candidate COUNT alone.

With `use_differentiable_cem=True` the lever *is* live and reaches the proposer --
measured inside `propose_trajectories`, the effective temperature moved
1.0 -> 1.4558 / 1.4839 / 1.4924 / 1.4972 / 1.4993 / 1.4995 / 1.5000 across successive
proposals while `n_candidates` went 32 -> 36. So the gap is a missing config coupling,
not a broken implementation.

**Consequence for this experiment.** At shipped defaults ARM 2 reduces to
candidate-COUNT widening only -- precisely the manipulation V3-EXQ-694 already ran and
which MECH-343's own `PRIOR TO CARRY IN` records as pointing AGAINST confirmation
(ON-arm first-action entropy FELL on 3/3 seeds: -0.0812 / -0.0734 / -0.0953). Running
the falsifier at defaults tests a strictly WEAKER manipulation than MECH-343 asserts and
is close to a foregone null.

### F2. Two of the detector's four DECLARED inputs are structurally absent -- and `use_dacc=True` does not fix one of them

`sd_061_difficulty_gated_proposal_entropy.md` declares the detector inputs as
`goal_proximity, score_margin, committed_action_class, dacc.choice_difficulty,
goal_salience`. Measured presence over an ecological loop (counts of non-`None` arguments
actually reaching `StuckStateDetector.update`):

| input | 60-tick probe (defaults) | 100-tick probe (`use_dacc=True`) |
|---|---|---|
| `goal_proximity` | 60 / 60 | 100 / 100 |
| `goal_salience` | 60 / 60 | 100 / 100 |
| `score_margin` | 59 / 60 | 99 / 100 |
| `committed_action_class` | **0 / 60** | **0 / 100** |
| `choice_difficulty` | **0 / 60** | **0 / 100** |

- `choice_difficulty` needs `agent._dacc_last_bundle` (`agent.py:7058-7063`).
  **Setting `use_dacc=True` through `REEConfig.goal_stream(...)` did NOT populate it** --
  `getattr(ag, "_dacc_last_bundle", None) is not None` measured **False**. So the axis is
  not reachable by the obvious knob; whatever additionally gates the dACC bundle is
  unidentified and is itself a second doc-vs-runtime gap.
- `committed_action_class` needs `e3._committed_trajectory`, which needs a commitment.
  None occurred (see F4).

**MECH-343 MANDATES** reporting "the SD-032b dACC `choice_difficulty` contribution to
`stuck_score` separately so a null is attributable." That obligation cannot be discharged
on a run where the axis is `None` at every tick. A pre-registered precondition that
provably cannot be satisfied is a design-time proof, not a threshold to lower.

### F3. The ecological non-vacuity precondition NEVER FIRES -- and it is a near-arithmetic consequence of F2

`StuckStateDetector` combines only the axes that are PRESENT
(`stuck_state_detector.py:325-331`, `combine_mode="mean"` default). With two present axes
and the goal-progress axis saturated (`last_deficit_progress = 1.0`) while the margin axis
is inert (`last_deficit_margin = 0.0`), the per-tick evidence is exactly
`mean(1.0, 0.0) = 0.5000` -- identical to `stuck_threshold` (0.5). The asymmetric EMA
approaches that value from below and `is_stuck` requires `>= 0.5`, so the gate is reached
only in the limit.

Measured, every arm, 100 ticks, in the hard `scheduled_action_block` ecology:

```
[ARM2_dacc_on]     stuck 0.0000..0.5000  duty(>=0.5)=0.000  beta_rises=0
[ARM1_gains_zero]  stuck 0.0000..0.5000  duty(>=0.5)=0.000  beta_rises=0
[ARM0_flag_off]    stuck 0.0000..0.0000  duty(>=0.5)=0.000  beta_rises=0
```

MECH-343's precondition, verbatim: "`detector_peak` must exceed threshold and then decay,
on >= 2/3 seeds, from naturally-arising goal blockage." Measured `detector_peak` does not
exceed threshold on ANY seed in ANY arm. This is G9 pole (A), NEVER-FIRES.

Q-056 supplies the handling ("self-routes to a harder environment, not a verdict"), but a
harder environment is not the lever here: the ceiling is set by which axes exist, not by
how hard the world is. The only routes above 0.5 are (i) a non-zero margin deficit -- the
E3 first-action margin was above `stuck_score_margin_floor` (0.05) at every measured tick
-- or (ii) restoring one of the two absent axes, which is F2.

**And the goal-progress axis is saturated from the start** (`deficit_progress = 1.0`
throughout), so MECH-343's leg **(c) "both decay after goal progress resumes" is
unmeasurable**: progress never resumes, so there is no decay to observe.

### F4. DV (b), "arbitration cycles before commitment", has no non-degenerate reading here

Zero beta rising edges in every arm, every probe; `mech090_n_elevation_admitted = 0`,
`use_commit_readiness_gate = False`. Beta elevation gates on `_commit_for_beta`
(`agent.py:9882-9886`), i.e. the E3 natural-commit path -- which is MECH-342's registered
open failure ("no natural commit when score margins are flat", V3-EXQ-629), a connected
failure MECH-343's own `notes` already cite. With zero commitments there is no
"cycles-before-commitment" to count, so one of the three legs MECH-343 says arms 1/2/3
must discriminate on cannot be measured at all.

### F5. Arm-2-vs-arm-3 is degenerate by construction at this operating point

`compute_proposal_gain` maps the GRADED `stuck_score`, not the binary `is_stuck`
(`difficulty_gated_proposal_entropy.py:138`). At a `stuck_score` that sits just under
threshold and barely varies, ARM 2's widening is therefore a near-CONSTANT mild lift:
measured `n_candidates` 32 -> 36 (`extra = round(8 * ~0.45) = 4`) with the gate never
firing. ARM 3 ("entropy ALWAYS high") is the same lever held constant. So at this
operating point ARM 2 IS a weaker ARM 3, and Q-056's load-bearing contrast -- "arm 2
STRICTLY beats ... arm 3", the difficulty-GATING distinction -- cannot discriminate.
This is the red-team "criterion cannot discriminate by construction" family, established
before the run rather than after.

### F6. (Positive, and reusable) The ARM-1 construction works, and is now proven

Running ARM 1 as `use_difficulty_gated_proposal_entropy=True` with
`dgpe_candidate_widen_max=0` and `dgpe_temperature_gain_max=0.0` gives the identity gain
`(0, 1.0)` at s = 0.00 / 0.25 / 0.50 / 1.00, so both consumer guards
(`agent.py:6199` `_dgpe_extra > 0`, `agent.py:6205` `_dgpe_temp_gain > 1.0`) stay false and
the proposal path is the un-regulated one, **while the detector still runs read-only**.

Measured parity against the literal flag-OFF arm over 100 ticks, same seed, same env:

```
PARITY actions_identical=True  entropy_identical=True
```

This is how a future Q-056 run can carry Q-056's own "arm 1 must actually get stuck"
precondition without a shadow detector and without perturbing arm 1. Worth keeping
whichever way the decision below goes.

---

## 3. Why this is a REFUSAL and not a design problem to solve in-session

The campaign's consent rule: STOP on a choice that is not specified by the chip, the
pre-flight, or a ratified plan-of-record AND that changes WHAT GETS MEASURED. Each of the
following is exactly that, and there are four of them:

1. **Whether to set `use_differentiable_cem=True`** -- decides whether the run tests
   "count-widening" or "count-widening + within-class temperature". It also imports SD-055's
   CEM refit (softmax-weighted mean over ALL candidates instead of argsort-over-elites) as a
   co-manipulation in every arm, which changes the proposal distribution that IS the DV.
2. **Whether, and how, to make the `committed_action_class` and `choice_difficulty` axes
   present** -- decides what "stuck" MEANS in the run, i.e. the trigger MECH-343 is about.
   (Per the 2026-09-04 v3closure digestion, the four axes are not interchangeable: axes 1/3
   are stall/lock-in, axes 2/4 are near-tie/ambiguity, and which ones carry the firing
   changes which claim's trigger was tested.)
3. **What ecology, warmup and commitment configuration** would let goal progress resume so
   leg (c) can be measured, and let commitments occur so leg (b) can be counted.
4. **Whether an arm-2-vs-arm-3 contrast that is degenerate at the shipped operating point
   should be run at all**, or whether SD-061 needs a build first.

The chip's own stop list names (1) and (4) directly; the brief's "two stops means stop"
rule says four unspecified choices in one item means the item's premises are stale.

**The AMBER pre-flight named one of these and understated it.** Its caveat was that the
ECOLOGICAL regime is "UNMEASURED" and that the handling is a self-route. It is now measured,
and the result is not "the detector might not fire in this environment" but "two of its four
declared inputs do not exist at runtime, its declared temperature lever has no consumer, and
the gate does not fire in any arm." That is a substrate gap, not an environment-difficulty
gap, and self-routing to a harder environment would not reach it.

---

## 4. Recommendation

**Route SD-061 to `/implement-substrate` for a small, well-defined coupling fix, then
re-queue Q-056 unchanged.** Concretely, three items, in order of confidence:

- **(a) Couple SD-061's temperature half to its consumer.** Either have
  `use_difficulty_gated_proposal_entropy=True` imply `hippocampal.use_differentiable_cem=True`,
  or add an explicit SD-061 knob and say in the design record that the temperature half is
  inert without it. This is the minimum that makes MECH-343's "DECLARE WHICH TEMPERATURE"
  precondition answerable rather than vacuous. It is also owed to the RECORD independently of
  this experiment: SD-061's `what_would_answer` criterion (2) and V3-EXQ-694's C2 are
  currently read as certifying a lift that never occurred.
- **(b) Determine what actually gates `_dacc_last_bundle`** and make `use_dacc=True` sufficient,
  or record what else is required. Until then MECH-343's mandatory per-axis attribution for the
  SD-032b input cannot be produced by any driver.
- **(c) Decide the detector's behaviour when axes are absent.** `combine_mode="mean"` over
  present axes silently rescales the score: with 2 of 4 axes present and one saturated, the
  attainable maximum is pinned at exactly `stuck_threshold`. An axis mask, a
  minimum-present-axes requirement, or a documented recalibration would all be defensible;
  choosing among them is a design decision, not a driver decision.

Re-queuing Q-056 before (a) is, in my judgement, spending a real run to re-derive
V3-EXQ-694's already-recorded negative on a manipulation half the claim does not assert.

**What I did NOT do, deliberately:** I did not turn on `use_differentiable_cem`, `use_dacc`
or any commitment configuration in a queued driver and call the result MECH-343 evidence; I
did not lower `stuck_threshold`; I did not narrow the leg to (a) alone to dodge (b) and (c);
and I did not write the F1/F2 findings into `claims.yaml`, `substrate_queue.json` or
`experiment_proposals.v1.json`. Those are governance's to apply.

---

## 5. Gate records (for the queue-entry `note` a successor will write)

- **GOV-REUSE-1 (Step 2.4).** Decisive readout: candidate first-action-class entropy at
  the PROPOSAL layer under stuck vs a matched within-seed baseline, arms 1/2/3.
  `reanalysis_query.py query --readout candidate_first_action_entropy --claim MECH-343`
  returned 0 matches; the only adjacent recorded readout is V3-EXQ-694's
  `first_action_entropy_base/stuck`, whose manifest carries no top-level `substrate_hash`
  (pre-2026-07-12 standard) and is therefore UNVERIFIABLE -> not recoverable. 694 also has
  no arm 3, no ecological regime, no arbitration-cycle metric, and ran
  `experiment_purpose: "diagnostic"` with `claim_ids: null`. **-> run needed (not a reuse).**
- **Re-derive brake (Step 2.5b).** MECH-343: 0 counted autopsies. Not braked.
- **Substrate-path overlap (Step 2.5c).** No OPEN `corrupting` entry overlaps
  `ree_core/cingulate/stuck_state_detector.py`,
  `ree_core/policy/difficulty_gated_proposal_entropy.py` or
  `ree_core/hippocampal/module.py`. `f_dominance_conversion_ceiling` is
  `implementation_status: wontfix` -> CLOSED under the skill's exact-match test, and in any
  case covers `e3_selector.py::score_trajectory`, which this upstream leg is scoped away
  from. (The 2026-09-18 pre-flight called it OPEN; it is not, under the gate's own
  predicate.) Degrading NOTES that a successor's queue entry should carry:
  `SD-091` (`agent.py::REEAgent.select_action`, `coalition_controller.py` -- keep the
  coalition at its default OFF or its `channel_gain("e3_candidate_count")` confounds the
  DGPE widening) and `SD-MECH267-CEM-SELECTION-FIX` (`hippocampal/module.py`, which is
  where the differentiable-CEM refit in F1 lives).
- **Ethics preflight (Step 2.6).** All flags `false`, `decision: allow` (SENT-0, V3).
- **Red-team (Step 4.5).** NOT RUN -- the session refused at Step 2.5a, which precedes it.

## 6. Claims and chips opened by this session

| id | kind | disposition |
|---|---|---|
| `metaworker-science-20260918-sd061-mech343-q056` | task claim (dispatcher-opened) | closed `--not-landed` |
| `metaworker-science-20260918-sd061-mech343-q056-exq-1056` | task claim, V3-EXQ-1056 slot reservation | closed `--not-landed`; **the ID was never used and is free** |
| `metaworker-science-20260918-sd061-mech343-q056-refusal-record` | task claim, this file | closed on the landing commit |
| `chip-20260918-sd061-mech343-q056-proposal-entropy-upstream-leg` | science chip | `unclaim` -- handed back, blocked on the decision chip |
| `chip-20260918-sd061-lever-inertness-decision` | decision chip | open, awaiting the user |
