# daemondrift + queuefloor: root-cause pass (daemondrift g7 / queuefloor g13)

**Status: AWAITING USER REVIEW.** Nothing below has been built or landed. This document is
measurement, diagnosis and a route; every build it names is chipped, not done.

- Date: 2026-09-23T07:38Z
- Session: `metalearning-recurrence-20260923`
- Skill: `/metaworker-learning` (Steps 0-5)
- Routed from: `chip-20260922-metaworkerlearning-daemondrift-queuefloor-recurrence`
- Dispatched by Orchestrator `orchestrate-20260922-subagent-wave`; user authorised both classes
  2026-09-23 ("Both, via /metaworker-learning").

**Prior passes in these two classes -- read these first; this document builds on them and does
not repeat their refutations:**

| Class | Prior pass | Outcome |
|---|---|---|
| daemondrift | `daemon_code_drift_learning_staged_20260909.md` | R1+R2 landed; R3 (restart automation) **DEFERRED**, Option A **disproven** by GOV-HELDOUT-1 |
| daemondrift | `metaworker_learning_outstanding_classes_staged_20260918.md` (P5) | **HAND BACK** -- all true positives, restarts stay manual |
| queuefloor | `queue_floor_detector_respec_staged_20260907.md` (g9) | detector defect real, fixed 2026-09-07 |
| queuefloor | `queuefloor_recurrence_rootcause_staged_20260915.md` (g10) | P1-P3 landed, P4 approved as a paced tranche |

---

## Headline

**Neither class is un-diagnosed. Both have had a root-cause pass. The two classes have opposite
residuals, and neither residual is the one the re-firing chip asks about.**

- **daemondrift.** The root cause is known, the detector is correct, and the remedy is
  deliberately manual by a user decision taken 2026-09-10 and re-affirmed 2026-09-18. The thing
  that recurs is not the drift -- it is the **routing**. The hygiene tick's generation brake
  re-emits "route this to /metaworker-learning for a root-cause pass" on every generation past 3,
  with no term for "this class has already been root-caused and dispositioned". Nine such chips
  have been minted since the decision that closed the question. **This is the only durable fix
  this class needs, and it is a fix to the brake, not to any daemon.**

- **queuefloor.** The g10 pass's hypothesis (supply-shaped starvation, substrate-blocked) is now
  **confirmed with a named mechanism**, and the mechanism is new since g10: `FILTER F` states its
  own release condition -- *"not re-mintable until a substrate_queue entry unblocking it lands"* --
  and **nothing in the fleet turns that valve.** 51 claims are pinned by FILTER F right now; 23
  of them name a missing BUILD as the release condition; **0 of those 23 have a substrate_queue
  entry.** The minter is not capped and not slow: it has **10 free slots and zero candidates**.

**The dispatch's hypothesis for queuefloor is CONFIRMED.** Queue starvation is not an
authoring-throughput problem. Authoring capacity is not the binding constraint because there is
nothing left to author against.

---

# CLASS 1 -- daemondrift

## 1.1 The recurrence is genuine; the root-cause pass is not owed

`chip-daemondrift-ree-cloud-1-ree-explorer-g7` (generation 7) and
`chip-daemondrift-dlaptop-mac-runner-g3` (generation 3) both carry the tick's generic escalation
text. Both classes are genuinely past threshold. But the escalation asks for work that has been
done three times:

1. **2026-09-09** -- `/metaworker-learning` pass (`daemon_code_drift_learning_staged_20260909.md`).
   R1 (Mac detector must not degrade to "clean" silently) and R2 (auto-resolution must not claim
   remediation it cannot observe) landed. R3, the automated restart, was found **not buildable as
   written** on two independent grounds: the GOV-HELDOUT-1 check scored it **1 right / 3 wrong /
   1 convertible across 5 non-degenerate cases, with 2 of the wrong calls SILENCING**; and one of
   its five required gates (a sync-daemon in-tick marker) **does not exist** (prerequisite R3a,
   still unbuilt today).
2. **2026-09-10** -- user AskUserQuestion: *"restart automation stays DEFERRED, restarts stay
   manual... Per-generation daemondrift chips continue to route as they already do; **no further
   re-raise of this class-level option set**."*
3. **2026-09-18** -- batched `/metaworker-learning` pass, P5 daemondrift = **HAND BACK**: *"All
   true positives; restarts stay manual (user decision 2026-09-10)."* User answered option A,
   which included that hand-back.

## 1.2 Is an automated remedy safe? Per subject, evidenced

The dispatch asked for this explicitly, including the CLAUDE.md constraint that absence of
telemetry is not abandonment and that killing a live worker mid-claim causes duplicate runs. The
question resolves to: **for each monitored daemon, does a queryable, authoritative "am I mid-work"
predicate exist?**

| Daemon | Box | Mid-work predicate? | Verdict on automating a restart |
|---|---|---|---|
| `mac-runner` | dlaptop | **YES** -- coordinator `/shadow/status` per-machine `state`/`current_exq`/`progress`; `/queue/active` claimed rows; `runner.pid`; graceful SIGTERM drain (finishes the experiment, no deadline) | Technically safe **and currently forbidden** -- see 1.3 |
| `ree-sync-daemon` | ree-cloud-1 | **PARTIAL** -- three separate shell checks (two `git status --porcelain` + empty spool). `/writer-health` has `last_tick_at` and `last_commit_at` but **no in-tick flag, no lock file, no drain mode, no SIGTERM handler** | **NO.** This is R3a, named 2026-09-09, still unbuilt. A mid-tick kill leaves staged-not-committed files or a stale `index.lock`; precedents 5h31m (2026-07-18) and a ~4049-restart crash loop (2026-08-01) |
| `ree-coordinator` | ree-cloud-1 | **NO** -- `/health` is liveness only; no in-flight-request counter, no drain | **NO.** Additionally `db.init_db()` runs `executescript(schema.sql)` at process start, so an unattended restart applies schema DDL to the live authoritative coordination DB |
| `ree-explorer` | ree-cloud-1 | **NO** -- no drain, no busy flag, no queryable lock. Process-level locks only | **NO.** It is not read-only: POST handlers do inline `git commit`+`push` of coordination data (`/api/workset/assign`, `/api/review/discuss`, `/api/decisions/resolve`), and a `_auto_pull` thread runs `git pull` on two repos every 300s. A restart drops in-flight writes invisibly |
| `mac-serve` | dlaptop | **NO** | **NO, and not programmatically restartable** -- unsupervised foreground child of the user's Terminal; there is no launchd plist for it |
| `ree-runner` | ree-cloud-1 | n/a | Retired 2026-08-30; in `_DAEMON_DRIFT_DO_NOT_RESTART`; reports INACTIVE and is never chipped |

**Answer: no safe automated remedy exists for the class.** Five of six subjects lack the
predicate an automated restarter would need. The sixth, `mac-runner`, has the best predicate in
the fleet -- and is precisely the subject where an automated restart is now **prohibited by a
standing user instruction**. The intersection of *"can be proven idle"* and *"may be restarted
unattended"* is **empty**.

**The cheapest reliable detector already exists and is correct**:
`ree-v3/coordinator/deploy/daemon_code_drift.py` is read-only, resolves each unit's own checkout
dynamically (`resolve_repo`), compares systemd `ExecMainStartTimestamp` against the **git
committer date** of a hand-maintained import-closure allowlist, and is gated on the un-picked-up
commit having waited > 24h. Since R1+R2 it emits **positive CURRENT readings** rather than an
absence of complaint. Nothing further is owed on detection.

## 1.3 Two live defects found by this pass (both chipped)

**(a) The `mac-runner` remediation recipe is stale, and following it would silently retire the
runner while reporting a restart.** `scripts/hygiene_routine_tick.py:10668-10672` tells the
clicking session:

> `POST {"kind": "stop"} ... launchd com.ree.runner KeepAlive respawns it on current code within
> seconds (confirmed 2026-08-29).`

Verified false as of 2026-09-22: `~/Library/LaunchAgents/com.ree.runner.plist` now carries
`RunAtLoad=false` **and** `KeepAlive=false`, and `~/.ree_runner_disabled` (set 2026-09-22T18:10:44Z
by user instruction) makes the launchd wrapper boot the job out. The POST is a graceful drain, so
no experiment is lost -- but **the runner never comes back**, and the session reports "restarted".
This is a self-certifying failure of exactly the shape R2 was built to stop, one level up: the
*remediation recipe* drifted from the system it describes, while the *detector* did not.

This is **generation 2 of a recipe-drift defect** in the same function: the same class was fixed
once already for the retired hub runner
(`chip-20260909-daemondrift-prompt-retired-runner`, REE_Working `77f0b3ba1`, which removed the
retired step and added a DO-NOT-RESTART row). A recipe that asserts a supervision fact has no
test that the fact is still true.

**(b) `chip-daemondrift-dlaptop-mac-runner-g3` is in direct conflict with a standing user
instruction.** The stay-down flag says the runner must finish V3-EXQ-1067 and not restart; the
chip asks for a restart. The chip's own step 1 ("act only in an idle window, `/queue/active`
empty") does hold as a guard, because V3-EXQ-1067 is live -- but the chip should be parked
explicitly, not left to a guard.

*Context worth carrying forward, not a finding of this pass:* `WORKSPACE_STATE.md:490` records
that restarting `mac-serve` is the **prerequisite** for the 2026-09-22 `stop_runner`
bootout-then-`launchctl kill TERM` fix being live -- i.e. the mac-serve drift chip currently gates
a fix that closes a Stop-button data-loss path.

## 1.4 The durable fix: the recurrence brake has no disposition term

`scripts/hygiene_routine_tick.py:6795`:

```python
if gen >= _EPISODIC_ESCALATE_GENERATION:      # == 3
    gen_note += (" That recurrence count says the SYMPTOM fixes are "
                 "not holding: route this to /metaworker-learning "
                 "for a root-cause pass INSTEAD of re-fixing the "
                 "instance -- and say so when resolving.")
```

An unconditional generation count. The only suppression in the path is `_regeneration_too_soon`,
a 24h quiet window that suppresses the **generation increment**, not the routing text. Nothing
consults any record of a completed root-cause pass or a class-level disposition.

**Consequence, measured:** since the 2026-09-10 decision that closed this option set, **9
generation-3-or-higher daemondrift chips** have been minted carrying the routing text
(`ree-explorer` g4/g5/g6/g7, `mac-serve` g4, `ree-sync-daemon` g3/g4, `ree-coordinator` g3,
`mac-runner` g3). Each one invites an expensive `/metaworker-learning` session that can only
re-derive a settled answer. Today's dispatch is the ninth such invitation, and the second to be
accepted.

**A precedent for the fix already exists in the same file.** `hygiene_routine_tick.py:45-46` and
`:1357-1372` implement exactly this pattern for stashes: *"Skips minting a chip for an entry that
carries a `disposition` (from `scripts/stash_dispositions.py`) -- a human has already adjudicated
that."* The episodic-class path has no equivalent.

Work-graph class: **`complicated (buildable)`**. Both the predicate and the storage pattern are
local, read-only and fully specified; there is no unknown.

## 1.5 Held-out check (GOV-HELDOUT-1) -- **caught an over-broad rule**

**First draft of the rule:** *"suppress the `/metaworker-learning` routing text for any class that
carries a recorded class-level disposition."*

Method: for every episodic class with a recorded disposition, count generation-3-or-higher chips
minted **after** the disposition date that carry the routing text. Old and new differ only where
such chips exist.

| Class | Disposition | Post-disposition routing chips | Non-degenerate? |
|---|---|---|---|
| daemondrift | 2026-09-10 user: restarts stay manual | 9 | **DISQUALIFIED** -- the rule was written from this class |
| **pausepressure** | 2026-09-18 **WATCH** for generation 11 | **1** (`chip-pausepressure-dlaptop-g11`, 2026-09-18T18:44) | **YES** |
| deployeddrift | 2026-09-18 HAND BACK | 0 | degenerate |
| staleclaim | 2026-09-18 HAND BACK | 0 | degenerate |
| metaworkergc / strandedwt / scriptscorpus / routedwriter | 2026-09-18 NOT A LEARNING JOB | 0 | degenerate |
| refwedge | none (root cause F unfixed) | 13 | degenerate (control -- both route) |
| checkoutdiverged | none (root cause F unfixed) | 7 | degenerate (control -- both route) |
| queuefloor | none settled | 11 | degenerate (control -- both route) |

**Result: one genuinely held-out non-degenerate case, and it REFUTES the first draft.**
`pausepressure`'s disposition was *"WATCH for generation 11"* -- the user explicitly asked to be
told at generation 11. `chip-pausepressure-dlaptop-g11` is that generation. A rule that suppresses
routing whenever a disposition exists would have **silenced the one report the disposition asked
for**. That is the same silencing failure mode the 2026-09-09 held-out check found in Option A.

**Revised rule, which survives the case:** the brake must not suppress -- it must **attach the
disposition**. Replace the unconditional escalation text with the class's recorded disposition,
its date, a link to the staged pass, and its re-escalation trigger. `HAND BACK` / `no further
re-raise` then reads *"already root-caused, remedy is deliberately manual, do not re-derive"*;
`WATCH at generation 11` reads *"you are at generation 11 -- this is the report that was asked
for."* Both receivers get the right instruction; neither is silenced.

**Honest counterweight.** (i) Even the revised rule has **one** non-degenerate held-out case, not
three. Per CLAUDE.md that is itself the finding: this rule is **scoped close to its motivating
population**, which is only two weeks old (the disposition corpus begins 2026-09-10). It should
ship as a narrow fix with that stated, and be re-checked once a second independent cohort of
dispositioned classes exists. (ii) The disposition record does not exist yet -- it would have to
be created, and a hand-maintained disposition file is itself a thing that can go stale, which is
the exact defect found at 1.3(a). Any such file needs a staleness check, or it becomes the next
generation of this problem. (iii) Held-out validation cost real cycles here and returned one
usable case; that is a poor yield, stated rather than padded.

---

# CLASS 2 -- queuefloor

## 2.1 The hypothesis under test, and the verdict

> *Queue starvation is not an authoring-throughput problem; the CONVERSION path from claim to
> queueable experiment is blocked upstream, and the blockage is invisible because nothing
> measures it.*

**CONFIRMED on the substance; the "invisible because nothing measures it" clause is WRONG and is
corrected below.** The conversion path is blocked upstream exactly as hypothesised. But it is
*measured repeatedly* -- by `FILTER F`, by a standing audit script, by a machine-readable
feasibility cache, and by four hand-written staged documents. **What no measurement has is a
consumer.** The gap is **write-back and persistence, not observation.**

That correction matters for the fix: building another detector would repeat the g10 pass's
refused proposal. The missing thing is the write side.

## 2.1a The test that could have refuted it

The honest refutation test is: **are there ready, unblocked candidates sitting unqueued?** If yes,
authoring throughput binds and the hypothesis is wrong.

| Source | Ready-and-unstarted candidates |
|---|---|
| `substrate_queue.json`, unbuilt entries (n=80) | **3** with `ready:true` -- and 2 of those are `proposed_REGISTRATION_ONLY_not_a_build_authorisation`, i.e. explicitly not build-authorised |
| IGW workset, `/queue-experiment` items (n=29) | **2** ready (23 blocked) |
| IGW workset, `/implement-substrate` items (n=20) | **1** ready (19 blocked) |
| `substrate_queue.next_implement_substrate.rationale` (live pointer, 2026-08-21 re-audit) | *"of 161 entries, NONE of the not-yet-built candidates has `ready:true` ... there is no next implement-substrate build right now"* |

**There is no ready inventory.** Nobody is sitting on queueable work for want of hands. The
hypothesis survives its own refutation test.

## 2.1b Flow: arrival and consumption are locked together, every week

Weekly first-appearance of `V3-EXQ-*` ids in `ree-v3/experiment_queue.json` vs first evidence
manifest per id (12 ISO weeks):

| week | W28 | W29 | W30 | W31 | W32 | W33 | W34 | W35 | W36 | W37 | W38 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| queue entries created | 47 | 62 | 71 | 88 | 54 | 42 | 20 | 28 | 36 | 19 | 39 |
| experiments that ran | 45 | 52 | 63 | 82 | 58 | 42 | 21 | 29 | 37 | 19 | 37 |

**Matched to within a few percent in every single week.** The fleet runs everything authored, in
the week it is authored, and has done for three months. Recent arrivals average **4.3/day** but
are session-shaped (14 on 08-29, 13 on 09-02, 12 on 09-14, 0-8 on every other day). Median
residence in the queue is **0.96 h** (g10). Depth 0 is simply what happens between bursts, and it
is a *supply* signal, not a fleet signal. This independently reproduces g10's 97-in / 98-out over
21 days on a 12-week window.

## 2.2 The decisive measurement

`scripts/proposal_backlog_dripfeed.py --json`, live at 2026-09-23T07:35Z:

```
open_proposals: 0     floor: 10     would_mint: 0     remaining_backlog: 0
```

**Ten free slots and zero candidates.** The g10 pass's proximate cause -- the cap jammed shut by
10 open-but-dead proposal chips -- is **fixed** (P2 landed; the four excluded entries in today's
output are the new exclusion working). The pipeline has moved to its next constraint, and that
constraint is an **empty eligible pool**, not a cap and not a rate.

This agrees independently with this morning's refill session (`queuerefill-20260923`), which found
the candidate surface exhausted: 40 ready SDs excluded because their validation experiment had
already run, 43 with no queueable validation, 4 known-churn, leaving one nominal candidate
(SD-106 -> V3-EXQ-1023) which had also already run.

Two instruments, independent methods, same answer.

## 2.3 The mechanism: FILTER F is a one-way valve

`scripts/proposal_feasibility.py` FILTER F excludes any claim carrying a recorded RED feasibility
verdict. Its own message states the release condition verbatim:

> *"not re-mintable until **a substrate_queue entry unblocking it lands**, its named producer path
> changes, or a newer GREEN is recorded."*

`proposal_feasibility.py pinned` (2026-09-23T07:33Z) -- **51 claims pinned**, denominator checked
against the tool's own count:

| Bucket | n | |
|---|---|---|
| Release condition is a missing **BUILD** (missing subsystem / no producer / unwired / blocked_substrate / zero callers / sequencing-gated) | **23** | of which **0** have any substrate_queue entry |
| Legitimately not an experiment (design_decision, derivational, methodological standard, already answered) | 8 | correctly pinned forever; no build owed |
| Has some substrate_queue mention | 16 | but **8 of those are `proposed_REGISTRATION_ONLY_not_a_build_authorisation`** -- registered, explicitly not authorised |
| Unclassified from the (truncated) reason text | 4 | see limitations |

**23 build-blocked claims; 0 registrations.** That is the conversion blockage, and it is a
*stock*, not a rate.

**Nothing consumes the pin list.** `recorded_infeasibility_reason()` has exactly three callers:
`proposal_routine_tick.py:1015` and `proposal_backlog_dripfeed.py:310` -- both use it as a **gate**,
to exclude -- and the `pinned` subcommand, which is a human report with no automated reader. There
is no path from *"this claim needs a build"* to *"a build is registered"*.

## 2.3a Three more registers of the same debt, none of them read

FILTER F is not the only place this stock is written down. It is written down at least four times,
by four mechanisms, none of which feeds the next:

| Register | What it holds | Why it does not convert |
|---|---|---|
| `proposal_feasibility_cache.v1.json` | **26** RED records -- and the schema has exactly the right slot, `substrate_queue_route` | **24 of the 26 have `substrate_queue_route: null`.** It is itself a register of 24 unregistered builds that nothing reads as such. 26 records against a >=64-claim RED population |
| `REE_assembly/scripts/audit_blocked_proposal_unblockers.py` (standing) | **49 UNOWNED** blocked proposals (43 claims, **64 distinct unowned blocker ids**); top: `SD-070` x5, `ARC-009` x4 | Reports only; its own docstring says the `blocked_by` write is *"ONE-WAY"* |
| same audit, READY bucket | **12** proposals whose named blockers are **all already `implemented`** | Nothing re-reads a `blocked_by` when its blocker lands. E.g. `EXP-0868`/MECH-160 is blocked on ARC-041, MECH-151, MECH-152, SD-016 -- **all four implemented** |
| whole-registry join (this pass + agent) | **122** blocked-ish proposals with no owner on *either* channel (116 claims); most carry `blocked_by: []` | Blocked with no named blocker at all -- unattributable, so no detector can route them |

**The 12 READY are a pure conversion leak and the cheapest item in this document**: they are
proposals that are *already unblocked* and still marked blocked. That is ready inventory hiding
behind a stale field, and it contradicts nothing in 2.1a -- 2.1a measured what is *labelled*
ready; this measures what *is* ready.

**Why the standing audit missed SD-106, the motivating case.** `audit_blocked_proposal_unblockers.py`
only reads proposals whose `status` is blocked **and** which carry `blocked_by`. `EXP-0255` was
left `status: proposed` with no `blocked_by`, because the refusing session was **scoped out of the
proposal registry** by its launch constraints (GFLAG-0425 says so verbatim). The detector was
therefore *structurally blind* to the exact shape it exists to find. This is g10 section 3b's
refusal write-back gap, still live: *"a refused proposal stays `proposed` forever while its
`chip_ref` is permanently consumed."*

## 2.3b Backlog-to-queue latency is not merely unmeasured -- it is unmeasurable

Of 250 `executed` proposals, only **16 (6.4%)** carry both a creation stamp and a queue/execution
stamp (`queued_utc` present on **13**, `executed_utc` on 17). **The schema has no field that
records when a proposal was queued.** The funnel's central latency cannot be derived from the
registry at all without git archaeology. That is a finding in its own right and it is the reason
every latency number in this class's history has come from a hand-run one-off.

## 2.4 Today's two flags are instances of this class, not new problems

- **GFLAG-0425** (`MECH-567`, `SD-106`; REE_assembly `b501e436b16`, on origin/master) -- the
  M1_FALSIFY route is not buildable experiment-side: `ZWorldP0Trainer.observe()` buffers only
  `world_obs` + `resource_proximity_target`, `ZWorldP0Config` has no action/oracle weight, and
  `oracle_action` has zero references in `ree_core/`. The flag itself classifies it correctly:
  *"MECH-567 is **complicated (buildable)** and routes to /implement-substrate"*. No
  substrate_queue entry, no IGW staging.
- **GFLAG-0427** (`campaign-backlogrouting-20260923`) -- a read-only second-pass triage of all
  **64** distinct RED pre-flight verdicts, grouped by failure shape (UNWIRED / MISSING_SUBSYSTEM /
  NO_FALSIFIER / SEQUENCING_GATED / MAGNITUDE_UNREACHABLE / BLOCKED_SUBSTRATE_ALREADY /
  BUILD_ALREADY_CHIPPED / SUPERSEDED / REDESIGN_INSTRUMENT) with a suggested route per bucket.
  It says explicitly: *"no claims.yaml/substrate_queue.json/proposal-file edit made."*

**An important correction to the g10 pass.** Its section 3b found that refusals reached no
worklist and that **zero** governance flags had been raised. That is **no longer true** -- both
flags above were raised today, by the correct route (`scripts/governance_flag.py`), carrying
exactly the right content. The write-back gap the g10 pass named has been partially closed by
practice.

**The residual is therefore narrower and sharper than g10's:** routing knowledge is now produced
correctly, per-incident, by whichever session happens to notice, and once by a deliberate manual
campaign (GFLAG-0427 swept all 64). What is missing is a **routine** that converts the standing
FILTER-F pin population into registrations. GFLAG-0427 is a one-off sweep, not a tick.

## 2.5 Why registration is the right node to unblock

The repo has already separated registration from authorisation: `substrate_queue.json` carries the
status value `proposed_REGISTRATION_ONLY_not_a_build_authorisation` (45 entries hold it today).
Registering a build-blocked claim therefore does **not** authorise a build and does not consume
research direction -- it makes the debt visible to `/implement-substrate`'s and IGW's existing
intake, which already discover new `substrate_queue.json` entries within minutes.

That is what makes this node cheap to unblock and distinguishes it from the thing the g10 pass
correctly refused to chip ("author more experiments" / "a fourth instrument saying it more
precisely"). This is not another detector. It is the **missing write-side of a detector that
already exists and already names its own release condition**.

## 2.6 Work-graph classification

| Node | Class | Why |
|---|---|---|
| FILTER-F pins never become substrate_queue registrations | **`complicated (buildable)`** | Both sides exist: the pin list is queryable, the registry schema has a registration-only status, the route (`governance_flag.py` -> `/governance` Step 6a) is proven working today. Only the routine is absent. |
| The 23 build-blocked claims themselves | **`complex (probe-gated)`** per claim | Each needs a scoping spike to say whether the build is reachable. That is `/implement-substrate`'s pipeline. Several already carry the spike result (MECH-468: *"a completed scoping spike found the substrate not buildable today"*). |
| The 8 `REGISTRATION_ONLY` entries | **not a debt node** | They are awaiting a build authorisation, which is the user's call. |
| Falsifier debt (g10 P4, tranche 2 open) | **`puzzle (known rules)`** per claim | Unchanged from g10; `chip-20260916-p4-falsifier-authoring-tranche2` is still open. |
| What to research at all | **not a debt node** | The user's call. g9 and g10 both declined to chip it; that still stands. |

Applying the razor: replenishment is **not blocked** at the registration node -- it is merely
unbuilt. The system is genuinely *blocked* at the 23 `complex (probe-gated)` substrate questions,
and being blocked there is an honest scientific finding, not a machinery defect: **the claim
registry has run ahead of `ree_core`.** The g10 pass said this (58% of adjudicated refusals were
"substrate not built"); this pass locates the specific valve that keeps it invisible.

## 2.7 What the floor should be told to say

Not re-proposed as a build, recorded because it keeps being rediscovered. The g9 pass refuted
lowering or retiring the floor on four grounds and the g10 pass found the floor "not mis-set, it
is mis-typed" -- a stock threshold reporting a flow deficit. This pass adds only that the flow
deficit now has a **named upstream cause with a countable stock (23)**, so the honest one-line
report is *"queue empty; 23 claims blocked on unregistered builds"* rather than *"the fleet is
running out of authored experimental work."* That is a chip-text change, not a new instrument.

---

## 3 Measurements this pass could NOT make, and why

1. **The minter's own filter-by-filter eligibility census.** `proposal_routine_tick.py --dry-run`
   returned `PAUSED -- coordination-plane lock held by session governance-20260923-0717; tick
   skipped entirely`. That is the lock working correctly, not a fault. The census would give the
   exact per-FILTER loss table (g10's section 3 shape) for today's pool. **Owed to a session that
   runs after the governance cycle releases.**
2. **Per-week arrival rate into the PROPOSAL backlog.** First-appearance by week on
   `experiment_proposals.v1.json` gives W36 = 768 and W26-W30 = 0, which is nonsense as a rate:
   the file is regenerated wholesale by a generator (`generated_at_utc`, `source_backlog:
   evidence_backlog.v1.json`), so a git diff measures regeneration events, not authoring. Reported
   rather than dressed up. The queue-side flow table in 2.1b is unaffected (that file is
   append-edited, not regenerated). Likewise W39's 47 new SDs is **one bulk registration pass**
   (45 `REGISTRATION_ONLY` entries traced to two audit documents), i.e. a backlog being written
   down, not one growing.
3. **Full RED-verdict reason text.** `proposal_feasibility.py pinned` truncates each reason to
   ~150 characters, so 4 of 51 rows could not be bucketed from its output alone. The full text is
   in the source chips and the feasibility cache. The 23 / 8 split above is therefore a **floor on
   the build-blocked count, not a ceiling** -- the four unclassified could only move the count up.
4. **Whether the 9 post-disposition daemondrift routings each cost a session.** The ledger records
   that the chips were minted, not whether a human clicked them. Two are known to have been
   accepted (`/metaworker-learning` 2026-09-18 and this one). The rest is an upper bound.
5. **A single trustworthy count of "falsifier-carrying claims with no route".** Three predicates
   exist and give **441** (loose keyword + `epistemic_category`), **221** (strict
   `substrate_conditional` only), and **121** (the 2026-08-28
   `unrunnable_falsifier_population_20260828.md` predicate, on a then-1064-claim registry; it is
   1180 now). **These are NOT a time series -- do not read 121 -> 221 -> 441 as growth.** They are
   three different questions. The 23 FILTER-F build-blocked figure in 2.2 is the one number in
   this document with a checked denominator, and it is a **floor, not a ceiling** (4 of 51 rows
   could not be bucketed because `pinned` truncates each reason to ~150 characters; the four could
   only move the count up).
6. **IGW open-assignment count as a work stock.** `igw_assignments.json` shows 312 open of 612,
   but the release path fires on only 300, mostly `claude -p exited; session JSONL present`. 312
   is a bookkeeping artefact, not 312 live work packages, and is not used above.

---

## 4 Decision required

Nothing has been landed. Per `/metaworker-learning` Step 4 this cannot be self-approved. Three
chips have been raised; each is a yes/no for the user.

### D1 -- Fix the stale `mac-runner` remediation recipe. (chipped, `kind: work`)
The narrowest and most urgent item: a recipe that asserts a supervision fact which stopped being
true on 2026-09-22, and whose failure mode is a silent permanent outage reported as a successful
restart. Generation 2 of a recipe-drift defect in the same function. **Recommend: yes.**

### D2 -- Give the recurrence brake a disposition term (attach, do not suppress). (chipped, `kind: decision`)
Per 1.4/1.5. Ships as a narrow fix with its one-held-out-case scope stated, per CLAUDE.md. The
disposition record it needs must itself carry a staleness check, or it becomes D1 again.
**Recommend: yes, narrowly scoped.**

### D3 -- Build the write-back that turns the four existing registers into registrations. (chipped, `kind: decision`)
Per 2.3-2.6. Registration-only, not build authorisation. **Recommend: yes** -- this is the one
change that converts a measured, stationary stock into work the existing `/implement-substrate`
and IGW intakes already know how to pick up. Scope, cheapest first:

1. **Release the 12 stale-blocked proposals** whose named blockers are all `implemented`
   (2.3a). Free conversion, available today, no new machinery.
2. **Backfill `substrate_queue_route` on the 24 null rows** of `proposal_feasibility_cache.v1.json`
   -- the field exists and is 92% empty.
3. **Register the 23 FILTER-F build-blocked claims** (and the 64 distinct unowned blocker ids from
   the standing audit, which overlap) as `proposed_REGISTRATION_ONLY_not_a_build_authorisation`.
4. **Close the structural blind spot** that hid SD-106: a `/queue-experiment` session that refuses
   on substrate-readiness must be able to write the refusal back to the proposal registry, or the
   standing audit stays blind to exactly the shape it exists to find. Today that session is scoped
   out of `experiment_proposals.v1.json` by its launch constraints and can only raise a
   governance flag by hand.

**Do NOT fold in a new detector.** g10 refused that and was right; 2.1 shows observation is not
the gap.

### D4 -- Add a `queued_utc`-equivalent to the proposal schema. (folded into D3's chip, lowest priority)
Per 2.3b. Without it the funnel's central latency stays underivable and every future pass in this
class repeats the same git archaeology. Cheap, but it buys a measurement rather than a
conversion, so it ranks below 1-4 above.

**Explicitly NOT proposed:** any automated daemon restart (1.2 -- no safe predicate for 5 of 6
subjects; the 6th is user-prohibited); any change to the queue floor value (g9's four refutations
stand); any new starvation detector (g10's refusal stands).
