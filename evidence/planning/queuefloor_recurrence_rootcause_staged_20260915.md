# Queue-floor recurrence: root-cause pass at generation 10

**Status: REVIEWED 2026-09-16 (user). P1 done (8 dead proposal chips withdrawn); P2 landed REE_Working e701ecb56; P3 landed (queue-experiment SKILL.md step 2b); P4 APPROVED as a paced governance item -> chip-20260916-p4-falsifier-authoring-tranche1 (15 per tranche).**

Session `learning-queuefloor-g10-20260915` | 2026-09-15T17:55Z
Routed from `chip-queuefloor-fleet-g10` via `chip-20260915-metaworkerlearning-queuefloor-recurrence-g10`
Orchestrator: `orchestrate-20260915-1743`

Prior pass in this class: `queue_floor_detector_respec_staged_20260907.md` (generation 9). **Read that
first; this document builds on it and does not repeat its refutations.** Its central finding was
accepted and its fix was built. This pass asks what is left.

---

## Summary

Three things are now separable that were not at generation 9.

1. **The instrument was genuinely broken and is now genuinely fixed.** Generations 1-8 were
   observation artifacts, as the g9 pass proved. The fix landed 2026-09-07. It worked: the standing
   chip's lifetime went from a 7.2-minute median refire gap to **164.3 hours**. g9 is the first
   legitimate resolution since g3.

2. **Two of the eleven generations are routing artifacts, not recurrences.** g9 and g11 were each
   minted within minutes of a human *withdrawing* the standing chip in order to route it to
   `/metaworker-learning`. Withdrawal re-arms the generation counter. The true recurrence count is
   nearer **nine than eleven**, and generation number is not a clean severity signal.

3. **The condition itself is real, worsening, and now measurably SUPPLY-shaped rather than
   burst-shaped** -- which reverses the working assumption two prior passes operated under. The
   fleet is not the bottleneck at any point in the last 21 days; authoring is. And the authoring
   pipeline is, at this moment, **mechanically deadlocked**: the queue is starved at depth 1 while
   the proposal minter's allowance is 0, because 8 of the 10 open chips holding the cap shut are
   already known-dead with recorded RED verdicts.

The deadlock in (3) is new, is not addressed by either of the two fixes already chipped tonight,
and is the only finding here that is cheaply actionable.

---

## 1. Drain vs replenish (question 1)

Method: walked every revision of `ree-v3/experiment_queue.json` on the local `main`, scoring each
with `check_experiment_queue_floor.queue_state()`'s own predicate. Queue-file revisions are **not a
uniform time sample** -- the file is committed when it changes, and an empty queue generates no
commits while consuming wall-clock -- so every depth figure below is **time-weighted**, per the
correction the g9 pass established (its section 1a).

**Replication check.** Re-running over g9's exact window reproduces its numbers to the decimal:

| quantity | g9 doc | this pass | verdict |
|---|---|---|---|
| below floor 3 (2026-08-20 -> 09-07) | 88.9% | **88.9%** (393.7h / 442.6h) | replicated |
| at depth 0 | 46.3% | **46.3%** (205.1h) | replicated |
| time-weighted median depth | 1 | **1** | replicated |

**Current state, same method:**

| window | span | below floor 3 | at depth 0 | tw median depth |
|---|---|---|---|---|
| g9 window (08-20 -> 09-07) | 442.6h | 88.9% | 46.3% | 1 |
| last 14 days (09-01 -> now) | 353.8h | 88.9% | **58.1%** | **0** |
| post-fix only (09-08 -> now) | 185.8h | 89.6% | **62.3%** | **0** |

**The condition has worsened.** Time at depth 0 rose 46.3% -> 62.3%; the time-weighted median depth
fell from 1 to 0. The g9 fix was never meant to change this and did not.

**Flow, per day, 2026-08-25 -> 09-15 (307 snapshots, 21 days):**

| quantity | value |
|---|---|
| queue_ids entering | **97** (4.6/day) |
| queue_ids leaving | **98** (4.7/day) |
| net | **-1 over 21 days** |
| median residence (queued -> gone) | **0.96 h** |
| mean residence | 3.05 h |
| p75 / p90 residence | 4.35 h / 9.90 h |
| longest observed residence | 21.7 h (V3-EXQ-959) |

Arrival and departure are balanced to within 1%. **Residence is dominated by run time, not queueing**
-- the median item is gone within an hour of arriving, and the fleet consumed everything offered on
every one of the 21 days. There is no backlog anywhere in the system.

**Is the floor of 3 the right shape?** Two answers, and they differ.

*As a severity threshold, no.* Depth is below 3 for 88.9% of wall-clock and has been for a month.
An alarm that is true 89% of the time carries almost no information per firing; it reports the
system's normal operating state. Sample-weighted, floor 3 fires on 59.3% of snapshots, floor 2 on
32.2%, floor 1 on 6.5%.

*As a statement of what the fleet needs, yes, and it is if anything too low.* Runs finish in
0.5-6.2h and the fleet drains the queue to empty within an hour of each arrival. A floor of 3
against a ~1h median service time buys roughly three hours of forward work. The g9 pass refuted
lowering or retiring the floor on four independent grounds and those grounds still hold; nothing
here reopens them.

**The honest reading: the floor is not mis-set, it is mis-typed.** It is a stock threshold
reporting a flow deficit. `check_experiment_queue_floor.py`'s own docstring anticipated exactly
this in its RESIDUAL section, written 2026-08-26: *"a queue being CONSUMED faster than it is
filled... the fix is more likely to be a rate term (depth vs. consumption) than a higher floor."*
That prediction is now confirmed by measurement. It is recorded here rather than proposed as a
build -- see section 6 for why a better-typed detector would change nothing the user does not
already know.

---

## 2. Authoring throughput and yield (question 2)

Tonight's 7 designs -> 5 refused / 2 queued is **better than the historical norm, not an outlier.**

**All-time, `chip-proposal-exp-*` (n = 495, ledger `/Users/dgolden/REE_Working/TASK_CHIPS.json`):**

| | n | note |
|---|---|---|
| minted ever | 495 | pipeline is 6 weeks old; 94% of it is the last fortnight |
| closed in bulk, never adjudicated | **372 (77%)** | 173 stale-EXP-id sweep + 156 paced curation + 43 other |
| adjudicated (a session did pre-flight and wrote a reasoned note) | **113** | |
| ...of which QUEUED a real V3-EXQ | **12 (10.6%)** | 95% CI [6.2, 17.6] |
| end-to-end yield, minted -> queued | **~3.0%** | 95% CI [1.8, 4.9] |

**Refusal reasons, adjudicated subset (n = 113 all-time / 96 over 14 days), stable across both:**

| reason | share of adjudicated |
|---|---|
| substrate not built / gated / v4-v5-held | **58%** |
| criterion cannot fail (degenerate, DV-invariant, vacuous) | 19% |
| no-experiment falsifier (`what_would_answer` bars minting) | 7% |
| unwired producer / consumer-site-read-as-proof | 2% named explicitly (absorbed into "substrate" elsewhere) |
| already run / evidence exists | 1% |
| queued | 10.6% |

**Settling the question `proposal_backlog_dripfeed.py` left open.** That file's `DEFAULT_FLOOR`
comment (lines 41-95) states its baseline is contaminated by the two bulk withdrawal spikes and
pre-registers exactly how to settle it: *"re-measure over a cohort minted AFTER REE_assembly
83f0ded88f (stable ids), once ~30 such chips have resolved"*, on three numbers (a) conversion,
(b) latency, (c) burst- vs supply-shape. `83f0ded88f` is dated 2026-09-04T14:32Z. That cohort now
exists:

| | value |
|---|---|
| cohort size (spawned after 83f0ded88f) | 29 (19 resolved, 10 open) |
| **(a) conversion, resolved -> a genuinely queued experiment** | **3 / 19 = 15.8%**, 95% CI **[5.5, 37.6]** |
| **(b) median open-to-resolved latency** | **24.5 h** (p25 0.5h, p75 84.9h) |
| **(c) shape** | **supply-shaped** -- see section 1 |

The three genuine conversions are `chip-proposal-exp-1212-paced` -> V3-EXQ-1037,
`chip-proposal-exp-1186` -> V3-EXQ-1040, `chip-proposal-exp-1210-paced` -> V3-EXQ-784a.

> **A counting trap, recorded because it nearly went into this document as a finding.** Matching
> `V3-EXQ-\d+` anywhere in a resolution note gives 7/19 = 36.8%. Four of those seven notes name an
> EXQ id **while explicitly declining to queue** (`chip-proposal-exp-0913-paced`: "NOT BUILDABLE --
> no experiment authored/queued"; `-1216-paced`: "no experiment queued"; `-0046`: "not queued";
> `-0901-paced`: "NOT QUEUED, correctly -- duplicate"). Each cites a *prior* run as the reason for
> refusing. The regex measures citation, not conversion. Every conversion figure above is
> hand-adjudicated.

**Verdict against the dripfeed's own pre-registered rule** (*"RAISE the floor only if (a) is
materially better than single digits AND (c) shows supply-shaped starvation"*): (c) is met. (a) is
**ambiguous and under-powered** -- the point estimate of 15.8% is above single digits, but n=19 is
below the ~30 the rule asked for and the 95% CI [5.5, 37.6] still spans single digits. **The rule's
own condition is therefore not met, and this document does not propose raising the floor.**

**What raising it would cost, for completeness.** At 15.8% conversion and 24.5h median latency, a
cap of 10 sustains 9.8 resolutions/day -> **1.55 queued experiments/day**, about **34%** of the
observed 4.6/day. The remainder arrives through orchestrator-directed sessions, `/governance` and
IGW. Buying +1 queued experiment/day through this channel needs ~6.3 more resolved chips/day, i.e.
a cap near **16** -- sixteen concurrent Opus `/queue-experiment` sessions, most of which would
refuse. The dripfeed's standing objection ("more chips, not more experiments") survives this
re-measurement.

---

## 3. Where the designs come from -- and the live deadlock (question 3)

`experiment_proposals.v1.json`: 1111 items, 646 `proposed`. The minter is
`/Users/dgolden/REE_Working/scripts/proposal_routine_tick.py` (**not** under `REE_assembly/scripts/`).

**Three multiplicative losses between the pool and a queued experiment:**

| stage | survivors | loss |
|---|---|---|
| 646 `proposed` | | |
| minus `proposal_type != experimental` (`:529`) | 185 | **71%** -- the pool is 461 `literature_review`, invisible to this minter by design |
| minus not-v3-testable, already-run, FILTER C (`:544-559`) | **74 eligible** | |
| of those 74, claim has a `what_would_answer` at all | **14 (18.9%)** | **81% back a claim with NO falsifier** |
| of the 74, `chip_ref` not already consumed | **7** | 51 withdrawn + 10 done + 6 open are permanently unreachable |

**The minter performs no falsifier check of any kind.** `what_would_answer` does not appear
anywhere in `proposal_routine_tick.py`. Ordering is `priority` then `proposal_id`; 73 of 74
eligible items are `medium`, so selection degenerates to **alphabetical by proposal id**. No
scientific-value, dependency-count or falsifier signal enters it.

**How the two fixes chipped tonight land against this.** `chip-20260915-proposal-minter-skip-no-experiment-falsifiers`
targets claims whose `what_would_answer` is present and *declares* no experiment -- measured at
**3 items** of the open pool (0.5%). The far larger bucket is **absent** falsifiers: **60 of the 74
eligible (81%)**, of which 48 are `mechanism_hypothesis`. Skipping those would be correct but would
cut the mintable pool to 14, which is a research-direction decision, not a filter setting. It is
raised as P4 below, not folded into the chipped fix.
`chip-20260915-preflight-producer-trace-predicate` addresses the 2%-named / substrate-absorbed
producer-trace bucket and is being worked by `cranky-mestorf-85a0e9`. Neither is re-proposed here.

### 3a. The deadlock, live at 2026-09-15T17:55Z

```
check_experiment_queue_floor.py:  STARVED -- depth 1 < floor 3 (pending 0, claimed 1)
open chip-proposal-* chips:       10   (dripfeed DEFAULT_FLOOR = 10)  ->  topup_allowance = 0
```

**The queue floor (3) and the proposal-chip cap (10) are wired to entirely separate machinery.**
`dispatch_budget_gate.py` and `dispatch_candidate_order.py` both call
`check_experiment_queue_floor.is_starved()`. `proposal_routine_tick.py` and
`proposal_backlog_dripfeed.py` call **neither**. There is no path from "the queue is empty" back to
"mint another design". Starvation promotes proposal chips to the top of the dispatch order
(`dispatch_candidate_order.py:776-778`), but promotion only reorders chips that already exist.

And the 10 chips holding the cap shut are, as of this measurement:

| chip_ref | spawned | recorded verdict | claimed |
|---|---|---|---|
| `chip-proposal-exp-0944-paced` | 09-10T22:27 | **RED** (4.8 days old) | no |
| `chip-proposal-exp-0662` | 09-14T15:02 | **RED** | no |
| `chip-proposal-exp-0720` | 09-14T15:02 | **RED** | no |
| `chip-proposal-exp-1070` | 09-14T16:02 | **RED** | no |
| `chip-proposal-exp-1072` | 09-14T16:02 | **RED** | no |
| `chip-proposal-exp-1288` | 09-14T16:32 | **RED** | no |
| `chip-proposal-exp-1390` | 09-14T17:32 | **RED** | no |
| `chip-proposal-exp-1176-paced` | 09-14T22:49 | **RED** | no |
| `chip-proposal-exp-1005-paced` | 09-15T01:49 | -- | no |
| `chip-proposal-exp-0965-paced` | 09-15T07:49 | -- | no |

**8 of 10 are already known-dead**, each carrying a measured RED verdict written by a session that
did the work, and none is claimed. The cap counts `status == "open"`, and a chip with a recorded
refusal is still `open` until somebody resolves it. So the authoring pipeline is currently jammed
shut by its own completed findings. This is the proximate, mechanical cause of tonight's depth of 1.

### 3b. The refusal write-back gap

Every one of tonight's five refusals is a substantial measured result -- live probes, seed sweeps,
call-graph traces, each naming a specific unblock route. None of that knowledge reaches any
worklist:

- **The proposal registry is untouched.** Both batch sessions record, verbatim, that they were
  *"barred by launch constraints from editing `experiment_proposals.v1.json`"*
  (`WORKSPACE_STATE.md` 2026-09-15T02:10Z and T06:44Z). The proposals stay `status: proposed`.
- **No governance flag was raised.** Searching all 287 items of
  `evidence/planning/governance_flags.v1.json` for `ARC-057`, `MECH-467`, `INV-095`, `SD-033d`,
  `MECH-237` and their EXP ids returns **one** hit, `GFLAG-0194` from 2026-09-06, already resolved.
  Zero flags from tonight. The route exists (`scripts/governance_flag.py`) and was not used.
- **What was written instead** is prose: `"OWED TO /governance: EXP-0720 -> blocked_substrate..."`
  in a `WORKSPACE_STATE.md` Recent Work line. `/governance` re-derives its worklist from
  `claims.yaml`, `pending_review.md` and the flag registry -- it does not read Recent Work.

So a refused proposal stays `proposed` forever while its `chip_ref` is permanently consumed
(`chip_ledger.py:1138`: *"A chip never reopens"*). It becomes simultaneously **un-testable and
un-removable**: invisible to the minter, still counted in the pool, and its refusal reason recorded
only in a chip prompt nobody re-reads. Measured: **51 of the 74 currently-eligible proposals** have
a withdrawn chip_ref in exactly this state.

---

## 4. Is the recurrence instrument? (question 4)

**Partly, and the part that was instrument has been fixed.** The generation series:

| gen | spawned | resolved | lifetime | refire gap | resolution |
|---|---|---|---|---|---|
| g1 | 08-30T02:34 | 08-30T09:54 | 7.3h | -- | auto, "quiet 7.3h" |
| g2 | 08-30T10:18 | 09-02T20:18 | 82.0h | 23.7 min | auto |
| g3 | 09-02T21:27 | 09-03T03:30 | 6.1h | 68.6 min | auto (the g9 pass judged this the one legitimate early resolution) |
| g4 | 09-03T12:37 | 09-03T18:47 | 6.2h | 546 min | auto |
| g5 | 09-03T18:55 | 09-04T03:05 | 8.2h | 8.4 min | auto |
| g6 | 09-04T03:10 | 09-04T09:23 | 6.2h | 5.0 min | auto |
| g7 | 09-04T09:29 | 09-04T19:19 | 9.8h | 5.9 min | auto, queue at depth 0 throughout |
| g8 | 09-04T19:21 | 09-07T22:23 | 75.0h | 2.5 min | **manual** -- root-cause routing |
| **g9** | 09-07T22:26 | 09-14T18:44 | **164.3h** | 3.4 min | auto |
| g10 | 09-14T22:41 | 09-15T08:36 | 9.9h | **236.5 min** | **manual** -- root-cause routing (this session) |
| g11 | 09-15T08:50 | (OPEN) | -- | 13.5 min | -- |

**The fix worked.** g1-g8 ran 6-10h each with a 7.2-minute median refire gap, which the g9 pass
proved was the tick's own observation record having holes in it. After the observation-gated
resolution landed on 2026-09-07, g9 held for **164.3 hours** -- a 25x increase in standing-chip
lifetime -- and resolved on the evening of 2026-09-14, which is precisely when the orchestrator's
authoring push carried the queue to depth 3-4 (12 queue_ids entered that day). g10 spawned 3.9h
later when depth fell back. **That is a real starve -> recover -> starve cycle, not an observation
gap.** g9 is the first resolution in the series that describes something that actually happened.

**But two generations are routing artifacts.** g9 and g11 were each minted within minutes of a human
*withdrawing* the standing chip in order to route it (g8 -> g9: 3.4 min; g10 -> g11: 13.5 min). The
tick re-observes the still-live condition on its next pass and mints the next generation. Routing a
standing chip by closing it therefore **increments the counter by one every time anyone escalates**.
Both `/metaworker-learning` escalations in this class have paid this cost. The counter that decided
this session was called reads 10; the number of times the condition actually cleared and returned is
nearer **nine**, and two of the increments were caused by the act of asking for help.

**One latent defect, named but not claimed as a cause.** `_queue_floor_episode_slug`
(`hygiene_routine_tick.py:8597`) keys the episode on the *previous* resolution, so the key is
constant for a whole episode and `record_episode` is idempotent against it -- hence
`episode_count = 1` and a frozen `last_episode_at` in every note above. `_hygiene_resolution`
computes `age_h = now - last_episode_at`, so **`age_h` measures how long the starvation has been
continuously true, and the rule resolves the chip when that exceeds 6 hours.** The term is inverted
in meaning: persistence reads as quiet. In production this is currently **masked** by the g9
clean-streak gate, which requires positively-clean observations and returns `None` (hold) when it
has none -- and `chip-queuefloor-fleet` has no entry at all in
`logs/hygiene_episodic_clean_streak.json`, while refwedge, daemondrift and checkoutdiverged all do.
The note text "episodic class quiet for 164.3h ... -- remedied" is therefore misleading even when
the resolution underneath it is correct. Recorded as a latent hazard and a reporting defect; it did
**not** cause g10.

---

## 5. Work-graph classification (question 5)

Replenishment is not one node. Splitting it by the CLAUDE.md vocabulary:

| sub-node | class | why |
|---|---|---|
| The minter deadlock (3a) -- starvation cannot reach the minter; cap counts dead chips | **`complicated (buildable)`** | Both predicates are read-only, local, and fully specified. Nothing is unknown. |
| Refusal write-back (3b) -- refusals reach no worklist | **`complicated (buildable)`** | The route (`governance_flag.py`) and the schema both exist; what is missing is that anyone calls them. |
| The `age_h` sign inversion + note text (4) | **`complicated (buildable)`** | Mechanical, and currently masked. |
| **Falsifier debt** -- 60 of 74 eligible proposals back a claim with no `what_would_answer` | **`complex (probe-gated)`** -> resolves to **`puzzle (known rules)`** per claim | For each claim the rules are known (what would falsify it is a scientific judgement the registry already has a slot for); the missing thing is the fact, and it is gettable. 48 of 60 are `mechanism_hypothesis`. |
| **Substrate-blocked refusals** -- 58% of all adjudicated refusals | **`complex (probe-gated)`** | Each needs a scoping spike to say whether the build is reachable; that is `/implement-substrate`'s pipeline, not this one. |
| **Research direction and cadence** -- what to author at all | **not a debt node** | This is the user's call, correctly. The g9 pass said the same in its section 6 and declined to chip it. That still stands. |

**Applying the razor** ("is *that* buildable?"): the first three rows are buildable on demand, so
replenishment is **not blocked** at them -- it is merely unbuilt. The system is genuinely *blocked*
only at the falsifier-debt node, and that block is `puzzle (known rules)`: the answer is gettable
per claim, one judgement at a time. **Prefer surfacing the puzzle over working the backlog** --
which is why P4 below is offered even though P1-P3 are far cheaper.

---

## 6. Causal account: instrument / pipeline / science

**Instrument (fixed, or cheap to fix):**
- g1-g8's generation churn: observation gaps. **Fixed 2026-09-07.** Confirmed by measurement here.
- g9 and g11: minted by the act of routing. Cheap to fix; nobody has.
- The `age_h` sign inversion and the "-- remedied" note text: latent, masked, misleading.
- The chip prompt's "non-critical housekeeping dispatch is preempted until this clears": the g9 pass
  measured the blast radius at 4 chips and offered correcting it as its option B. The claim is still
  in the live prompt. Not re-proposed here -- it belongs to that decision, not this one.

**Pipeline (the new findings):**
- The starvation signal has no path to the minter; the two floors are tuned independently and are
  currently deadlocked at allowance 0 while the queue is empty.
- The cap counts `open` chips, and 8 of 10 are finished work awaiting a resolve.
- Refusals write to a chip prompt and a prose Recent Work line; neither is a worklist. Proposals
  stay `proposed` while their chip_ref is permanently consumed.
- Authoring is coupled to orchestrator session presence. All three dispatchers have carried
  `requested_state: "stop"` since 2026-09-14T21:48Z (`dispatcher_control.json`), correctly -- that
  file fails closed by design after the 2026-08-23 runaway. Arrivals are consequently lumpy and
  session-shaped (12 on 09-14, 13 on 09-02, 15 on 08-29, 0-8 on most days), which is why depth-0 is
  62% of wall-clock even though the daily average nearly meets the floor.

**Science (not a machinery problem):**
- 58% of adjudicated refusals are "substrate not built". That is the largest single cause and it is
  not a pipeline defect -- it is the honest finding that the registry has run ahead of `ree_core`.
- Manifest production: **9.0/day** (08-01..08-19) -> **4.6/day** (08-20..09-07) -> **4.0/day**
  (09-08..09-15). Output roughly halved and has stayed there. Co-occurrence with the starvation
  window, stated as such and not as proven causation.
- Tonight's five refusals are each a real result. Treating them as waste would be the wrong lesson;
  the defect is that they are not *recorded* anywhere a pipeline reads.

**Why a better-typed detector is not proposed.** A rate-term detector (depth vs consumption) would
report, correctly, "authoring 4.6/day, consumption capacity far above it, buffer empty 62% of the
time". Everyone already knows this: it is in the g8 note, the g9 document, the dripfeed's
`DEFAULT_FLOOR` comment and this one. A fourth instrument saying it more precisely does not author
an experiment. The g9 pass declined to chip "author more experiments" on exactly this ground and
was right to.

---

## 7. Held-out check (GOV-HELDOUT-1)

Run against P2, the only proposal below that changes a standing predicate. Required: >= 3 historical
cases the rule was **not** written from, where old and new give **different** answers.

**HO-1 (passes, non-degenerate).** The 2026-09-04 `science-wave-coord-20260904` sweep withdrew
**173** chips whose titles named EXP ids that no longer existed after a governance regen -- open,
uncompleted, and unactionable by any dispatched session. OLD: all 173 counted toward the cap, so
`topup_allowance` was 0 for as long as they sat there, and the pool only reopened when a human ran a
manual sweep. NEW: excluded as unactionable from the moment their proposal_id stopped resolving, so
the minter re-mints with current ids on its next tick without waiting for the sweep. Different
answer; the new one is right, and it is the outcome the sweep's own note asked for
(*"proposal_routine_tick re-mints to its floor of 10 with current ids"*).

**HO-2 (degenerate -- does not count).** The 2026-09-01 mass-mint of 166 chips. Both old and new
count them as open and actionable (no RED verdict, live ids), so both give `allowance = 0`. Tests
nothing.

**HO-3 (degenerate -- does not count).** The 2026-09-10 merge of 8 paced chips into
`chip-20260910-merge-paced-proposal-triage`. They became `withdrawn`, so the old rule already
stopped counting them. Same answer.

**Result: one non-degenerate case, not three.** Per CLAUDE.md's own instruction -- *"If you cannot
find 3 such cases, that is itself the finding"* -- this is reported rather than papered over. The
honest reading is that P2 is **scoped close to its motivating incident**: the population of
open-but-dead proposal chips is only six weeks old, and the two bulk-closure events that dominate
the history were resolved by hand before the predicate could have differed. P2 should therefore be
taken as a **narrow fix for a currently-live jam**, not as a general rule, and if adopted should be
re-checked once a second independent cohort of dead-open chips has accumulated.

**Honest counterweight.** (i) This document is measurement and design only; nothing in it has been
built or tested. (ii) The conversion figure (a) in section 2 rests on n=19 with a CI spanning single
digits -- it is enough to refuse the floor increase, not enough to license one. (iii) Excluding
chips from a cap always risks the cap failing to cap: if a RED verdict were ever recorded on a chip
that was in fact still actionable, P2 would let the minter run past its intended ceiling. The
mitigation is that the exclusion is narrow and reversible, but it is a real trade.

---

## 8. Decision required

Nothing has been landed. Per `/metaworker-learning` Step 4 this cannot be self-approved. Each
proposal is a yes/no.

---

### P1 -- Resolve the 8 dead proposal chips now, to unjam the minter. YES / NO

**Do:** run `chip_ledger.py resolve --status withdrawn` on the 8 open `chip-proposal-exp-*` chips
carrying a recorded RED verdict (listed in section 3a), each note citing the session and verdict
already written in its prompt. This drops the open count 10 -> 2 and restores
`topup_allowance` to 8, letting the minter draw fresh designs on its next hourly tick.

**Changes:** `TASK_CHIPS.json` via the coordinator (`scripts/chip_ledger.py` only -- never a hand
edit).
**Does NOT change:** any script, the floor of 3, `DEFAULT_FLOOR = 10`, the minter's predicates,
`experiment_proposals.v1.json`, or any claim. Purely a ledger hygiene action on findings that are
already complete.
**Note:** this is the one proposal with an immediate effect on tonight's depth of 1. It is also
strictly a symptom fix -- the jam re-forms in roughly a week without P2.

---

### P2 -- Stop counting known-dead chips toward the proposal-chip cap. YES / NO

**Do:** in `count_open_proposal_chips()`, exclude an `open` chip that either (a) carries a recorded
RED/BLOCKING pre-flight verdict in its prompt, or (b) names a `proposal_id` that no longer resolves
in `experiment_proposals.v1.json`. The cap then means "designs actually in flight", which is what
the user ratified it as on 2026-09-01.

**Changes:** `/Users/dgolden/REE_Working/scripts/proposal_backlog_dripfeed.py` (the shared pacing
rule, imported by `proposal_routine_tick.py`), plus tests in the existing
`scripts/test_*` convention.
**Does NOT change:** `DEFAULT_FLOOR` stays **10** -- this document explicitly declines to raise it
(section 2). Does not change the queue floor of 3, the minter's eligibility predicates, ordering,
`dispatch_budget_gate.py`, or `dispatch_candidate_order.py`.
**Caveat, stated plainly:** the held-out check found only **one** non-degenerate case (section 7),
so this is a narrow fix for a live jam rather than a general rule.

---

### P3 -- Make a refusal write back to a worklist. YES / NO

**Do:** amend `/queue-experiment`'s refusal path so that a session refusing a proposal must, before
closing, record the disposition where a pipeline will re-derive it -- either by setting the
proposal's `status` in `experiment_proposals.v1.json` (`blocked_substrate` /
`no_experiment_implied` / `gated`), or, where the session is barred from that file, by raising
`governance_flag.py --flag-type contested_disposition` naming the claim and the measured reason.
Prose in `WORKSPACE_STATE.md` would no longer satisfy "OWED TO /governance".

**Changes:** `.claude/skills/queue-experiment/SKILL.md` and its `.agents/` mirror; optionally the
launch-constraint boilerplate the orchestrator writes into science-batch prompts, which is what
barred tonight's sessions from the registry.
**Does NOT change:** the minter, either floor, the chip ledger, `claims.yaml`, or any governance
disposition -- P3 makes refusals *visible* to `/governance`, it does not decide any of them.
`/governance` keeps its Step 2b ratification, and the CLAUDE.md rule that a `/failure-autopsy`
session does not chip its own unratified routing is untouched.
**Why it matters more than P1:** without it, 51 of the 74 currently-eligible proposals stay
permanently un-testable and un-removable, and the next five refusals will be re-derived from
scratch by a future session.

---

### P4 -- Commission a falsifier-authoring pass on the 60 claims with no `what_would_answer`. YES / NO

**Do:** work the 60 claims backing the minter's eligible pool that have no falsifier at all (48
`mechanism_hypothesis`, 7 `design_decision`, 4 `invariant`, 1 `mechanism`) -- for each, either author
a `what_would_answer`, or mark it explicitly non-experimental. This is the **81%** loss in section 3
and the single largest determinant of authoring yield; it is `puzzle (known rules)` per claim, and
`/claim-synthesis` or `/governance` is the owning skill, not this one.

**Changes:** `REE_assembly/docs/claims/claims.yaml` (the `what_would_answer` field only), across a
governance cycle rather than one session.
**Does NOT change:** claim `status`, `confidence`, `implementation_phase`, `v3_pending`, or any
evidence attachment. No experiment is queued by this work; it makes future minting honest rather
than producing designs directly.
**Honest counterweight:** 60 claims of genuine scientific judgement is several governance cycles of
the user's own attention, and it competes directly with adjudicating the runs that already exist.
It is offered because it is the only proposal here that raises the *ceiling* rather than clearing a
jam -- P1-P3 together cannot produce a single additional experiment if there is nothing testable to
propose.

---

**Explicitly NOT proposed**, on the grounds cited: raising `DEFAULT_FLOOR` (section 2 -- the
dripfeed's own pre-registered condition is not met); lowering, retiring or re-specifying the queue
floor of 3 (refuted by the g9 pass on four grounds, unchallenged here); rebuilding either fix
already chipped tonight; a rate-term replacement detector (section 6); lowering
`COORDINATOR_STALE_HOURS`; re-enabling the hub runner (both CLAUDE.md "Closed on measurement").

---

## Sources

- `/Users/dgolden/REE_Working/ree-v3/experiment_queue.json` -- 307 revisions, 2026-08-25 -> 09-15,
  scored with `check_experiment_queue_floor.queue_state()`.
- `/Users/dgolden/REE_Working/TASK_CHIPS.json` -- 3575 chips; 495 `chip-proposal-exp-*`; the
  `chip-queuefloor-fleet` g1..g11 series.
- `/Users/dgolden/REE_Working/REE_assembly/evidence/planning/experiment_proposals.v1.json` -- 1111
  items; eligibility re-run through `proposal_routine_tick._eligibility()`.
- `/Users/dgolden/REE_Working/REE_assembly/evidence/planning/governance_flags.v1.json` -- 287 items.
- `/Users/dgolden/REE_Working/scripts/` -- `check_experiment_queue_floor.py`,
  `hygiene_routine_tick.py`, `proposal_routine_tick.py`, `proposal_backlog_dripfeed.py`,
  `dispatch_budget_gate.py`, `dispatch_candidate_order.py`, `dispatcher_control.json`,
  `logs/hygiene_episodic_clean_streak.json`.
- `/Users/dgolden/REE_Working/WORKSPACE_STATE.md` -- 2026-09-15T02:10Z, T06:44Z, T07:45Z, T13:37Z,
  T17:42Z (the orchestrator cycles behind tonight's 7 designs).
- `REE_assembly/evidence/planning/queue_floor_detector_respec_staged_20260907.md` -- generation 9.
- `REE_assembly/evidence/planning/pause_pressure_recurrence_rootcause_staged_20260902.md` -- read
  for shape only.
