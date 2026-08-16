# Failure autopsy -- V3-EXQ-929 + V3-EXQ-933 (sleep_substrate:GAP-9 within-life trigger family)

- **Generated (UTC):** 2026-08-16T18:24:43Z
- **Scope:** cluster (2 targets, one mechanism staged in two arms)
- **Status:** `confirmed` (STAGING MODE -- Step 8 interactive gate not run; routing is drafted, not final)
- **Trigger:** `/failure-autopsy` mandatory-for-diagnostics rule (2026-08-07 user-instructed correction). Both
  targets are clean, unflagged `experiment_purpose: "diagnostic"` PASSes with `claim_ids: []`. Neither carries
  an indexer `adjudication` flag; both appear under `pending_review.md` "Diagnostic -- autopsy required
  (no confirmed adjudication)".
- **Already-done check:** performed by CONTENT over all 1157 `failure_autopsy_*.json` artifacts (`targets[].run_id`
  match), not by filename glob. **Zero prior coverage** of either run_id.

---

## 0. Dry-run gate (Step 2a) -- run BEFORE any metric was read

```
scripts/check_dry_run_citations.py v3_exq_929_..._v3 v3_exq_933_..._v3
-- 0 dry cited, 0 dry in named families, 0 ambiguous, 2 clean, 0 unknown   (exit 0)
```

| Run ID | `dry_run` | Verdict |
|---|---|---|
| `v3_exq_929_sleep_gap9_within_life_trigger_20260814T081606Z_v3` | absent/false | REAL run -- admissible |
| `v3_exq_933_sleep_gap9_need_arm_20260814T155845Z_v3` | absent/false | REAL run -- admissible |

`dry_run_checked: true`; `excluded_dry_run_ids: []`. No population statistic is quoted in this autopsy, so no
denominator correction applies.

**One wording hazard to fix downstream (not an evidence problem).** `sleep_substrate_plan.md` line 606 cites
929 as *"smoke PASS OFF=0/ON=4/ceiling=1.0"*. The numbers quoted are the REAL run's, and the checker confirms
the cited manifest is not dry -- but calling it a "smoke" invites exactly the V3-EXQ-543i misreading the gate
exists to prevent. Recommend the plan row be reworded (governance, not this skill).

**Criterion reachability.** `validate_experiments.py --checks dry_run_unreachable_criterion` fires on 11 drivers,
all in the `v3_exq_543` lineage; neither target is among them. Both drivers' `--dry-run` reduction is a single
line (`seeds = seeds[:1]`) which changes seed count only -- `LIFE_STEPS`, the ceilings and the thresholds are
untouched -- so no criterion is structurally unsettable under truncation. Manual read performed; lint silence is
not being read as an all-clear.

## 0b. Recording provenance (Step 2b)

`ree-v3/validate_recording.py --paths <both>` -> **2 complete, 0 always-core gaps, 0 thin-pack drops, 0 schema
warnings.** `recording_schema`, `substrate_hash`, `substrate_commit`, `machine`/`machine_class`,
`elapsed_seconds`, `config` and the explicit `seeds` list are all present on both. Substrate identity is clean
and confirms the build order:

| Run | `substrate_commit` | committed | arms present in that substrate |
|---|---|---|---|
| 929 | `817ae377` | 2026-08-14 08:15:07Z | ceiling arm only (need arm hardcoded off) |
| 933 | `1ba76825` | 2026-08-14 15:58:13Z | ceiling + need arm |

933 therefore ran against a strictly later substrate that contains 929's, which is what makes 933's `CEILING`
arm a legitimate reproduction of 929 rather than a different build.

**A recording gap does exist, and it is the load-bearing measurement finding -- see Section 5.**

---

## 1. Facts (no interpretation)

### 1a. V3-EXQ-929 -- ceiling arm (design (a))

2 arms x 3 seeds, one TRUE single continuous life each (`LIFE_STEPS = 120` waking steps, agent never `reset()`,
so `notify_episode_end()` is unreachable and the within-life trigger is the only path to a cycle).

| Arm | `trigger_wired` | ceiling | waking steps | cycles fired | ceiling-arm frac | need-arm fires |
|---|---|---|---|---|---|---|
| OFF (x3 seeds) | False | 25 | 120 | **0** | 0.0 | 0 |
| ON (x3 seeds) | True | 25 | 120 | **4** | **1.0** | 0 |

Preconditions: `life_exceeds_step_ceiling` 120 vs 25 (met); `on_arm_trigger_wired` 1.0 vs 1.0 (met);
`off_arm_trigger_not_wired` 0.0 vs 0.0 (met). Criteria `c1_off_silent`, `c2_on_fires`, `c3_on_ceiling_arm` --
all `load_bearing: true`, all passed. `criteria_non_degenerate` all true. Label `within_life_trigger_validated`.
`elapsed_seconds` 1.05 for the whole 6-cell run.

### 1b. V3-EXQ-933 -- need arm (design (b)) + ceiling reproduction

3 arms x 3 seeds, same single-continuous-life shape. MEL injected per step via
`mel_consumer.note_step_pe(inject)` immediately BEFORE `update_residue`.

| Arm | `use_mel_entry` | ceiling | injected MEL/step | cycles fired | first fire step | need frac | ceiling frac | min MEL at fire |
|---|---|---|---|---|---|---|---|---|
| CEILING | False | 25 | 0.0 | 4 | 25 | 0.0 | 1.0 | 0.0 |
| NEED_HIGH | True | **100000** | 1.0 | **120** | **1** | 1.0 | 0.0 | 1.0 |
| NEED_SUB | True | 25 | 0.1 | 4 | 25 | **0.0** | 1.0 | 0.100000000000000031 |

(identical across all three seeds; threshold `mel_entry_threshold = 0.5`.)

Preconditions: `life_exceeds_step_ceiling` 120 vs 25 (met); `need_arm_wired` 1.0 vs 1.0 (met);
`stimulus_crossed_threshold` 1.0 vs 0.5 (met). Criteria `c1_need_fires_and_carries`, `c2_demand_sooner`,
`c3_threshold_gates`, `c4_ceiling_baseline` -- all `load_bearing: true`, all passed. Label `need_arm_validated`.
`elapsed_seconds` 1.51 for the whole 9-cell run -- **including 360 completed sleep cycles.**

### 1c. Substrate code paths actually exercised

- `REEAgent.update_residue()` -> `SleepLoopManager.notify_waking_step(agent)`
  (`ree_core/sleep/phase_manager.py:235`).
- Gate: `if not self.within_life_trigger: return None`; then
  `at_ceiling = steps_since_sleep >= within_life_step_ceiling`;
  `need_crossed = mel_consumer is not None and mel_consumer.need_crossed()`;
  fire iff `need_crossed or at_ceiling`.
- `MELConsumer.need_crossed()` (`mel_consumer.py:219`): `use_mel_entry` on AND `accumulator.count > 0` AND
  `current_mel() >= mel_entry_threshold`.
- `MELConsumer.current_mel()` (`mel_consumer.py:119`): **`accumulator.mean()`** -- and
  `WakingMELAccumulator`'s own docstring states the intent explicitly: *"MEL is the MEAN per-step prediction
  error ... so the window length does not bias the load estimate."*
- `_run_cycle` (`phase_manager.py:328`) returns early only when both `sws_enabled` and `rem_enabled` are off
  (both ON here) or when `use_mech286_sleep_onset_gate` blocks (deliberately OFF here). So each recorded fire
  is a cycle that ran to completion and appended to `cycle_history`.

---

## 2. Are the PASSes real, or degenerate? (the central question for a clean diagnostic PASS)

### 2a. `life_exceeds_step_ceiling` is a CONFIG IDENTITY, not a measurement -- in both runs

`waking_steps` is incremented unconditionally inside `for step_idx in range(LIFE_STEPS)`; `done` triggers an
**env**-level `env.reset()` and never breaks the loop. So `min_waking_steps == LIFE_STEPS == 120` on every
execution path, and `STEP_CEILING`/`CEILING_STEP_CEILING == 25` is a module constant. The precondition is
`120 >= 25`: two literals compared. It **cannot fail** and is not an observation.

This is not a hidden defect -- both drivers say so themselves in `ANCHOR_REACHABILITY_EXEMPT`
("reachable by construction (LIFE_STEPS=120 > STEP_CEILING=25)"). But it means the precondition's *stated*
protective function ("a shorter life could silently make the ON arm look non-firing") is real only against a
future edit, never against this execution. **Read it as a build-time assertion, not as evidence.**

### 2b. Which criteria do more than restate their own preconditions?

| Criterion | Could it have failed given the preconditions + the build? | Verdict |
|---|---|---|
| 929 `c1_off_silent` | Yes, weakly. The precondition reads the FLAG (`within_life_trigger` False); c1 reads the BEHAVIOUR (0 cycles). It would catch a second, unexpected firing path (a default-on cadence, `notify_episode_end` firing anyway). Given no `agent.reset()` and `K = 10^7`, that residual is small. | near-entailed, small real content |
| 929 `c2_on_fires` | **Yes, genuinely.** A wired flag with `notify_waking_step` never called from `update_residue`, or with `_run_cycle` early-returning, yields 0 fires with the precondition still met. This is the actual GAP-9 question -- structural reachability. | **REAL -- carries the run** |
| 929 `c3_on_ceiling_arm` | **No.** 929's substrate (`817ae377`) has the need arm hardcoded off and no `mel_consumer` configured, so `within_life_trigger_arm_need` can only ever be 0.0 and the ceiling fraction can only ever be 1.0. | **structurally unfailable** |
| 933 `c1_need_fires_and_carries` | Partly. "Fires >= 1" is real; "need frac == 1.0" is entailed, because NEED_HIGH's ceiling is 100000 in a 120-step life so no fire *can* be ceiling-attributed. And the readiness precondition `stimulus_crossed_threshold` already requires `fires >= 1` on this arm -- so c1 substantially restates it. | near-entailed |
| 933 `c2_demand_sooner` | Weak. Constant injection of 1.0 against threshold 0.5 makes `need_crossed()` true at step 1 by arithmetic. Confounded (NEED_HIGH also has a 4000x higher ceiling) but **conservatively** so: a higher ceiling can only DELAY a ceiling fire, never manufacture "sooner". | confounded but conservative; low information |
| 933 `c3_threshold_gates` | **Yes.** Same wiring as NEED_HIGH; only the magnitude differs. It discriminates between two candidate crossing statistics: under a SUM/integral, 0.1/step crosses 0.5 by step 5 and c3 fails; under a MEAN it never crosses. It passed. | **REAL -- the only magnitude-discriminating criterion in the cluster** |
| 933 `c4_ceiling_baseline` | **No.** `use_mel_entry=False` makes `need_crossed()` return False unconditionally, so need frac 0.0 / ceiling frac 1.0 is forced. | **structurally unfailable** |

**Net: the cluster's 7 load-bearing criteria reduce to 2 that could have failed** (929 c2, 933 c3), 3 that are
near-entailed by their own preconditions or arm geometry (929 c1, 933 c1, 933 c2) and 2 that are structurally
unfailable (929 c3, 933 c4). Both PASSes are **REAL, not vacuous** -- but they are considerably thinner than
"3 of 3" and "4 of 4 load-bearing criteria passed" reads.

The indexer's `vacuous_pass` flag would not have caught this and did not fire, correctly by its own definition:
`criteria_non_degenerate` is true because the ARMS genuinely separated. Arm separation is not the same property
as criterion informativeness, which is why this autopsy is required rather than the flag.

### 2c. The finding 933's PASS masks: NEED_HIGH fired on 120 of 120 waking steps

Not a footnote -- it is the run's most consequential observation and nothing in the acceptance rule looks at it.
`notify_waking_step`'s only re-entrancy guard is `_within_life_cycle_active` (in-cycle), and `_run_cycle` calls
`mel_consumer.on_cycle_complete()` which RESETS the accumulator. So under sustained supra-threshold demand the
next step re-injects 1.0, the mean is 1.0 again, and the trigger fires again. **There is no refractory period,
no hysteresis, and no minimum inter-cycle interval on the need arm.** The step ceiling is a *maximum* interval
backstop; nothing bounds the minimum.

The regime this produced -- a sleep cycle on every single waking step -- is degenerate as an organism state
even though it satisfies every pre-registered criterion. And it is precisely the regime the arm is *intended
for*: design (b) exists to fire in a non-converging environment that sustains high MEL, which is exactly the
condition that produces continuous sleep here.

---

## 3. Claim layer (Step 3)

**Both targets are UNTAGGED (`claim_ids: []`)**, so GOV-FAILLOC-1's claim-free branch applies and the
Claim-alignment row of the four-layer table is **n/a**. There is no `claims.yaml` entry to align, weaken,
strengthen, demote or split, and `per_claim_recommendation` has **no claim to key on** -- it is emitted as an
empty object with an explicit note rather than inventing a claim.

`sleep_substrate:GAP-9` is a **plan node** in
[`evidence/planning/sleep_substrate_plan.md`](sleep_substrate_plan.md), not a claims.yaml claim -- the plan's
own traceability row (line 670) records `n/a (plan node, no claims.yaml claim)`. Naming the owning plan is
required when describing a GAP: **the gap is GAP-9 of the sleep-substrate plan-of-record**, registered
2026-08-12, design brief 2026-08-14
(`evidence/literature/targeted_review_sleep_onset_multiinput_gap9/synthesis.md`).

**Governance-relevant state to surface: the plan node was already flipped to `done`.** `sleep_substrate_plan.md`
line 606 records GAP-9 `done` as of 2026-08-14 "(BOTH arms)", citing exactly these two runs as its validation --
i.e. the closure was taken on two diagnostic PASSes that had not been autopsied. Section 6 states what this
autopsy finds that closure supports and what it does not.

**Granularity-debt recurrence trigger: DOES NOT FIRE.** `granularity_debt_cluster.py` is claim-keyed and both
targets are claim-free, so no cluster exists to count and no `claim_alignment` distribution can be computed.
Recorded honestly rather than substituted with a filename-neighbourhood grep (the 2026-07-22 over-count
failure mode).

**Re-derive brake: DOES NOT FIRE, by construction.** The brake counts `substrate_ceiling` readings per claim
under R1-R3; with `claim_ids: []` there is no claim to count against, and neither target is recommended
`substrate_ceiling`. `fired: false`.

---

## 4. Biological-reference triage (Step 4) -- this is where the load-bearing finding is

### 4a. The reference mechanism, and the lit entry EXISTS

`evidence/literature/targeted_review_sleep_onset_multiinput_gap9/synthesis.md` (2026-08-14) is the design's own
literature basis, so `lit_status: present`. Two sources are decisive:

- **Borbely two-process (1982; 2016).** Process S is a **homeostatic accumulator**: sleep pressure GROWS with
  time awake and is **discharged by sleep**. The synthesis states plainly that *"(b) is Process S / INV-050's
  third drive, and it is the best-grounded of the three"* -- i.e. the MEL/need arm is grounded in Process S
  specifically, not in a generic threshold.
- **Saper 2010 flip-flop switch.** Sleep-wake is a mutually-inhibitory switch that is *sharply bistable but
  intrinsically UNSTABLE*, held in place by orexin acting from **outside** the switch. The synthesis's own
  design language: *"a sharp bistable switch, plus a continuous stabiliser acting from outside it."*

### 4b. Divergence 1 -- the PRIMARY arm is a LEVEL DETECTOR, not Process S. Load-bearing.

`need_crossed()` compares `current_mel()` -- the **MEAN** per-step waking PE since the last cycle -- against a
fixed threshold. `WakingMELAccumulator`'s docstring makes the invariance deliberate: *"so the window length does
not bias the load estimate."*

Time-invariance is the **right** property for the role the statistic was built for (GAP-5b duration scaling:
how *hard* was this wake window, independent of how long it was). It is the **wrong** property for the role it
was reused in. Process S's defining behaviour is that a constant sub-threshold demand *eventually* crosses,
because pressure integrates over time awake. A mean never does.

The reuse route is visible in the source: `need_crossed()` was factored out of `entry_permitted()` so the GAP-9
step trigger could *"reuse the exact same crossing predicate"*. The factoring is clean; what travelled with it
was the duration-consumer's scale-free semantics, into an entry-timing role where scale-freeness inverts the
intended dynamic.

**Both runs' results are exactly what a level detector predicts, and neither could have detected the
divergence:**
- NEED_HIGH (1.0 constant) crosses on step 1 and on every step after a reset -> 120/120 fires, first fire 1.
- NEED_SUB (0.1 constant) never crosses, **for 120 steps** -> need frac 0.0.

**`c3_threshold_gates` is the same observation under two opposite framings.** Pre-registered as
"sub-threshold demand does not spuriously fire the need arm", it PASSES. Read against the design's own cited
Process S basis -- "does accumulated waking demand eventually reach the entry threshold?" -- the identical
measurement is a **negative result**: 120 waking steps of continuous non-zero learning demand produced zero
demand-driven sleep. The run cannot arbitrate between the framings because its acceptance rule only encodes
the first.

### 4c. Divergence 2 -- a bistable switch was run with its stabiliser deliberately disabled

`use_mech286_sleep_onset_gate` (the orexin / wake-stability analog) was OFF in both runs. That was the **correct**
call and the synthesis explicitly instructed it (MECH-286's threat term reads a signal V3-EXQ-917 measured at
chance-level place-safety discrimination; enabling it would confound the first true-single-life sleep result).

But the consequence must be recorded: Saper's switch without its external stabiliser is *predicted* to chatter --
rapid, repeated state transitions. **That is exactly what NEED_HIGH produced (120 transitions in 120 steps).**
So the degenerate regime in Section 2c is not an incidental artifact of a saturating stimulus; it is the
biologically-predicted signature of a bistable switch with no stabiliser, observed in the substrate and recorded
by the run without being flagged. Read that way, 933 contains a *positive*, biology-consistent finding that its
own acceptance rule discarded.

### 4d. Does the failure resemble a missing dependency of the reference mechanism?

Yes, on both axes -- and this is the constructive reading. Nothing here says the GAP-9 mechanism class is wrong.
What the cluster shows is that the built trigger is missing two dependencies the reference architecture requires:
a **time-integrating pressure term** (Process S) and a **stabiliser / hysteresis** holding the switch after it
flips (Saper). Under the skill's default stance this is a *discovered prerequisite*, not a falsification -- and
the synthesis had already named the cheap next build (Section 5.3: route the term into the graded DURATION
multiplier `MELConsumer.scale_steps()` rather than a boolean permit).

---

## 5. Four-layer diagnosis (Step 5)

Shared across both targets except where split.

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **n/a** | `claim_ids: []` on both; no claims.yaml entry exists to align. GAP-9 is a plan node. |
| Biological reference | **clear** | Borbely Process S + Saper flip-flop-with-stabiliser, both in the design's own 2026-08-14 synthesis. Divergence identified on both axes (4b, 4c) and is load-bearing by default, not a caveat. |
| Developmental / dependency prerequisites | **missing** | The need arm depends on (i) a time-integrating pressure term and (ii) a post-fire refractory/hysteresis. Neither exists. The ecological MEL producer is separately parked (GAP-5b / V3-EXQ-718a: measured CausalGridWorldV2 MEL is noise-level ~1e-5). |
| Implementation completeness | **partial** | 929: v1 ceiling arm only, need arm hardcoded off -- partial *by design*. 933: need arm present and wired, but as a level detector with no refractory. Both: the fired cycle runs to completion but with an untrained agent and an empty replay sampler it performs essentially no consolidation work (360 cycles in 1.51 s total). |
| Environment adequacy | **wrong pressures (acknowledged, bypassed)** | The ecological producer is deliberately bypassed: MEL is *injected* via `note_step_pe`, standing in for a non-converging world. Honest and precedented (V3-EXQ-718a did the same), but it means neither run says anything about entry timing under a realistic demand *trajectory* -- only under two constants. |
| Measurement adequacy | **under-instrumented** | Two distinct gaps, see below. |
| Integration adequacy | **isolated** | Trigger and cycle exercised in isolation from learning, goal and hippocampal state. Nothing downstream of the fire was measured. |
| Scale / capacity | **unknown** | Untrained agent by design; the DV is structural. No scale claim is made or supported. |

**Measurement / recording gaps -- distinguish the two, they route differently.**

- **RECORDING debt (cheap, decisive).** `_run_cycle` merges a rich metric dict into `cycle_history` on every
  fire -- `replay_diversity_index`, `mel_sws_steps_effective` / `mel_rem_steps_effective`, the `mel_consumer`
  metrics block, `post_sleep_z_goal_retention`, the cross-module-consolidation readouts. The drivers extract
  **only** `within_life_trigger_arm_ceiling` / `_arm_need` / `_steps_at_fire` / `_mel_at_fire` and discard the
  rest. So the manifests can answer *"did the trigger fire?"* and cannot answer *"did the fired cycle do
  anything?"* -- the readout existed at run time and was not written. Per the Experimental Recording Standard
  (`experimental_recording_standard_2026-07-12.md` §3b/§3c) the repair is a same-question re-run that RECORDS
  it, not a blind re-run. Runtime is ~1.5 s, so this is close to free.
- **MEASUREMENT debt (needs redesign).** No criterion reads inter-cycle interval, so the 120/120 regime of
  Section 2c is invisible to the acceptance rule; and no criterion varies demand over TIME, so the Process-S
  property is untestable by this design regardless of instrumentation.

### Failure-location summary (GOV-FAILLOC-1)

Both targets are **PASSes**; **no "REE failed" read is made anywhere in this autopsy**, and none is available.
Recorded explicitly because GOV-FAILLOC-1 applies symmetrically to claim-free diagnostics:

| Bucket | Reads from | Status |
|---|---|---|
| MECHANISM FAILED | Implementation completeness = `partial` | **not_established** |
| MEASURES FAILED | Measurement adequacy = `under-instrumented` | **not_established** |
| ENVIRONMENT FAILED | Environment adequacy = `wrong pressures` | **not_established** |
| REE FAILED | requires all three `established` | **false** |

**Net classification: NOT APPLICABLE -- no failure to locate.** The load-bearing corollary, which the parent
should carry forward: because Implementation, Measurement and Environment each independently read
partial / under-instrumented / wrong-pressures, **any future negative organism-level result from this
apparatus could not be charged to REE either.** The gate would refuse it on all three counts.

### Epistemic category

**`standard`** for both targets. These are claim-free substrate-readiness validations; no epistemic suppression
is asserted, no claim's answer is being declared substrate-gated, and "no category applies" is spelled
`standard` (never `n/a`). Reaching for `substrate_ceiling` or `substrate_conditional` here would silently remove
claims from GOV-GRAN-1 surfacing and v3-testability -- and there is no claim to remove, so the stamp exists
purely to keep the target visible to R3 and GOV-CAT-1. The failure-mode diagnosis lives in the note fields, not
in this field.

### Evidence direction

**`non_contributory` (RETAINED as the drivers self-set it)** -- correct, because `claim_ids: []` means nothing
weights any claim. Per the skill's rule, the interpretable signal is stated explicitly before this is recorded:
the runs establish (i) within-life sleep-cycle reachability in a true single continuous life, which was
structurally impossible before the GAP-9 build, (ii) that the need arm is wired end to end through
`note_step_pe -> need_crossed -> notify_waking_step -> _run_cycle`, and (iii) -- unrecorded by the runs
themselves -- that the arm is a level detector with no refractory. `non_contributory` here means "weights no
claim", **not** "uninformative".

---

## 6. Cluster pattern (Step 6)

| Experiment | Arm under test | Negative-control / absolute criterion | Discrimination criteria | Read |
|---|---|---|---|---|
| V3-EXQ-929 | design (a) ceiling | `c1_off_silent` PASS (flag-off arm silent) | `c2_on_fires` PASS (real), `c3_on_ceiling_arm` PASS (unfailable) | Reachability established. One informative criterion. |
| V3-EXQ-933 | design (b) need + (a) reproduced | `c4_ceiling_baseline` PASS (unfailable), `c3_threshold_gates` PASS | `c1_need_fires_and_carries` PASS (near-entailed), `c2_demand_sooner` PASS (confounded, conservative) | Wiring established. One informative criterion, whose reading inverts under the design's own cited biology. |

**These are ONE mechanism validated twice at the wiring level, not two independent validations.** They are the
staged v1/v2 build of a single composed trigger (`need_crossed or at_ceiling`) in one function,
`notify_waking_step`. 933's `CEILING` arm literally re-runs 929's finding on a later substrate (4 fires, first
fire step 25, ceiling frac 1.0 -- identical to 929's ON arm), and 929's `c3` and 933's `c4` are the same
unfailable assertion stated twice.

**The structural property, which is the load-bearing output.** Both runs' acceptance rules are built entirely
from *wiring, reachability and arm-attribution labelling* predicates. Not one criterion in either run reads a
**timing** property -- inter-cycle interval, time-to-cross under sustained demand, or demand-proportionality of
onset. That is precisely the property distinguishing the Process-S accumulator the design brief specified from
the level detector that was built. So the cluster is not "N independent bugs"; it is **one composed trigger,
validated twice against the half of its specification that is about connectivity, and never once against the
half that is about dynamics.**

Two live readings, both consistent with everything measured:
1. **Instrumentation reading (favoured).** The trigger is correctly wired and the mechanism class is right; what
   is missing is a time-integrating pressure term and a stabiliser. Cheap, named builds -- `complicated
   (buildable)`.
2. **Specification reading.** `current_mel()`'s mean semantics were a deliberate choice for the duration
   consumer and are simply the wrong statistic for entry timing, so the "PRIMARY" arm does not implement design
   (b) as the synthesis defined it, and GAP-9's `done` status overstates what was built.

They are not exclusive and both force the same next action, which is why no `fanout_recommendation` is emitted:
the bottleneck routes to **one unambiguous build**, not to a discrimination among rival hypotheses.

---

## 7. Learning extracted, and repair pathway (Step 7)

**Node classification (work-graph debt vocabulary).** `complicated (buildable)` -- the fix is a named build with
no open question. The two candidate statistics are both readable in the source, the design brief already names
the preferred shape (graded duration multiplier, Section 5.3), and no fact is missing. **Do not queue a spike to
re-confirm what is already known how to build.**

Learning:

1. A **wiring precondition is not evidence the mechanism did anything** -- and in this cluster 5 of 7
   load-bearing criteria are wiring, geometry or labelling assertions. `criteria_non_degenerate` was true
   throughout and is a weaker guarantee (the arms separated) than criterion informativeness.
2. `life_exceeds_step_ceiling` compares two module constants on every execution path. A precondition whose
   measured value cannot vary is a build-time assertion. **When a precondition is structurally satisfied,
   say so in the manifest** rather than emitting it as `measured`/`threshold`, which reads as an observation.
3. **Factoring a predicate out for reuse can silently transplant an invariance property into a role where it
   inverts the intended dynamic.** `current_mel()`'s time-invariance is correct for duration scaling and wrong
   for entry timing; nothing at the factoring site flagged the role change. This is a reusable engineering
   lesson beyond sleep.
4. **The same measurement can pass one framing and fail another.** 933's `c3` is a PASS as
   "threshold gating works" and a negative result as "does accumulated demand eventually cross?" -- and a
   pre-registered acceptance rule encodes only one of them. Where a criterion is a two-sided reading, declare
   both directions in the interpretation grid (existing standing guidance for diagnostic descriptions).
5. **A saturated arm is not a validated arm.** Firing on 120 of 120 steps satisfied every criterion while
   demonstrating that the trigger has no minimum inter-cycle interval. Diagnostics validating a trigger should
   carry a degeneracy guard on the fire RATE, not only on the fire COUNT.
6. **Recording debt, not measurement debt, blocks the "did the cycle do work?" question** -- the metrics exist
   in `cycle_history` at run time and were discarded. Runtime here is ~1.5 s, so recording them is close to free.

### Routing (DRAFT -- staging mode, not confirmed at a Step 8 gate)

| Target | Routing | Why |
|---|---|---|
| V3-EXQ-929 | **`queue-experiment`** -- same-question re-run, alphabetic suffix (**929a**), whose ONLY change is to RECORD the discarded `cycle_history` merged metrics | Textbook recording gap: the readout existed at run time and was not written. Cite `experimental_recording_standard_2026-07-12.md` §3b/§3c; require `stamp_recording_core(...)` and emission of per-fire `replay_diversity_index`, `mel_sws_steps_effective` / `mel_rem_steps_effective`, the `mel_consumer` metrics block and the inter-fire step gap. Do NOT re-run blind. |
| V3-EXQ-933 | **`implement-substrate`** -- `create` a substrate_queue entry (no existing entry covers this gap) | Missing prerequisites are named, buildable and grounded in the design's own literature: (i) a time-integrating sleep-pressure term for the ENTRY role, distinct from `current_mel()`'s deliberately scale-free duration statistic; (ii) a post-fire refractory / hysteresis so the switch cannot chatter. The synthesis's Section 5.3 already names the preferred shape. |

**Substrate queue check performed:** 157 entries in `evidence/planning/substrate_queue.json`; the nearest
neighbours are `SD-MEL-CONSUMER` (implemented; consumer capability validated by injection, ecological
demonstration re-parked) and `SD-MEL-PRODUCER` (implemented). **No entry covers the within-life ENTRY-TIMING
trigger**, so `action: create` rather than `amend`. Suggested id `SD-SLEEP-ENTRY-PRESSURE`; governance may
rename or, alternatively, prefer to carry it as a GAP-9 successor node on `sleep_substrate_plan.md` -- flagged
as a decision for the gate, since GAP-9 there is currently `done`.

`severity: degrading`, `substrate_paths: ree_core/sleep/mel_consumer.py::need_crossed`,
`ree_core/sleep/mel_consumer.py::current_mel`, `ree_core/sleep/phase_manager.py::notify_waking_step`. Classified
`degrading` rather than `corrupting` because the defect is reachable only behind `use_mel_entry`, which is
default-off -- so it does not silently corrupt unrelated experiments and should WARN, not BLOCK, at
`/queue-experiment` Step 2.5c. **Revisit toward `corrupting` the moment any experiment enables `use_mel_entry`
in a sustained-demand environment**, where continuous sleep would suppress waking learning in a way that could
read as a substrate ceiling rather than as a trigger defect.

No `resolves_prior_failure_record`: this is a new, independent finding on a new entry.

### Draft `evidence_quality_note` (governance writes it; this skill does not)

There is **no claim to attach a note to** (`claim_ids: []` on both targets), so no `evidence_quality_note` is
drafted. The equivalent durable text belongs on the GAP-9 plan node and is drafted in Section 8 below.

---

## 8. What the confirmation gate must decide (Step 8 NOT run -- staging mode)

1. **Is GAP-9's `done` status still correct?** This autopsy supports `done` for **design (a), the step-count
   ceiling backstop** -- 929's `c2` is real and reachability is genuinely established. It does **not** support
   `done` for **design (b) as specified**: the built need arm is a level detector on a deliberately
   time-invariant statistic, with no refractory, and no run has tested its timing behaviour. Options: leave
   `done` with a scope caveat; split the row into (a) done / (b) partial; or reopen a GAP-9 successor node.
2. **Accept or revise the substrate routing** (`create SD-SLEEP-ENTRY-PRESSURE` vs a GAP-9 successor plan node).
3. **Accept or drop 929a** (the recording-only re-run). It is ~1.5 s of compute; the argument against it is that
   the same instrumentation could simply be folded into the eventual GAP-9-v2 validation instead of spending a
   queue id.
4. **`severity: degrading` vs `corrupting`** for the Step 2.5c gate -- see the revisit condition above.
5. **Wording fix** on `sleep_substrate_plan.md` line 606, which calls 929 a "smoke PASS".

Per the 2026-07-30 user-instructed rule, this session **does not `spawn_task`** any follow-on its own routing
names. `/governance` chips it once ratified at its Step 2b -- and must first check
`evidence/planning/igw_routine_ledger.json` / `igw_assignments.json` for an already-staged identical build.

---

## 9. Hypothesis-space ledger (Step 9b) -- DRAFTED ONLY, nothing written

Staging mode: `hypothesis_space_registry.v1.json` and its siblings are **untouched**. The intended disposition
is recorded under `hypothesis_space_ledger_pending` in the companion JSON.

**Recommended action: NONE.** No `fanout_recommendation` is emitted (the bottleneck routes to one unambiguous
build, which the skill lists as exempt), and neither target adjudicates a pre-registered leg -- both are
claim-free substrate-readiness validations with no rival-hypothesis set. Registering them would add a question
whose "hypotheses" are build-status facts, inflating the frozen denominator with legs that were never rival
explanations. No growth-restriction check applies, because no existing question is being attached to.

An **optional** new question is sketched in the JSON should governance want the Process-S-vs-level-detector
divergence tracked as a first-class open question rather than only as a substrate item. It is a sketch, not a
pre-registration, and nothing may be appended from it without an interactive confirmation.

---

## Human gate -- CONFIRMED 2026-08-16T18:41:10Z

Written headless in STAGING MODE, then confirmed at a consolidated interactive gate covering all 7 artifacts of this batch. Decisions:

1. SD-017/ARC-045/MECH-166: ACCEPTED the 436e 'standard' -> substrate_ceiling flip AND the re-derive brake refusal of a V3-EXQ-436g (SD-017 count 2 -> 3). Removes the three claims from the v3-testable pool. Rationale: 436e's 'standard' was stamped on the explicit condition 'substrate shipped, merely needs switching on', and 436f is that condition's re-check trigger and falsifies it. The 538a peripheral-co-tag off-ramp was offered and NOT taken.
2. MECH-152: the HELD demotion is REFUSED and the claim stays 'provisional' -- on INSTRUMENT grounds, not claim strength. Governance must NOT read 922a as support. The same Pearson-r critique disqualifies EXQ-194's r=0.70 support symmetrically, so 194 and 922 are to be RE-ADJUDICATED. Route a NEW EXQ scoring modulation depth against the claim's own band.
3. GAP-9: sleep_substrate_plan.md's 2026-08-14 'done (both arms)' is CORRECTED -- done for design (a) only; arm (b) REOPENED (a level detector shipped where the brief specifies Process S). SD-SLEEP-ENTRY-PRESSURE to be created, severity degrading. Note entry_permitted() delegates to the same need_crossed(), so the boundary-path K-cadence trigger inherits the divergence untested.
4. CROSS-CLUSTER: four independent instances of a mechanism tested in a NON-PRODUCTION configuration (927/928 mode_partitioned_cem False; 930 use_contextual_safety_terrain False; 934 salience_affinity_input_cap None + use_external_task_drive False; 931 HippocampalConfig.wanting_weight ships 0.0 not 0.5). AUTHORISED: chip a warn-only authoring lint plus a corpus audit.

Routing stands as drafted except where a decision above overrides it.
