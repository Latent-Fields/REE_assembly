# Pause-pressure gate: generation-3 root-cause pass

**Status: AWAITING USER REVIEW. Nothing in this file has been written to any script, skill, or registry.**

- Produced by: `/metaworker-learning`, headless chip `chip-20260902-metaworkerlearning-pausepressure-g3-rootcause` (box `ree-cloud-4`).
- Authorized by: user decision via the Orchestrator lane, 2026-09-02T16:31Z -- route `chip-pausepressure-dlaptop-g3` to a root-cause pass INSTEAD of a third instance-fix or a full pause window.
- Written: 2026-09-02T18:26Z.
- Sister docs: `fleet_commit_sequencing_redesign_20260829.md` (sections 10-12, the pause pattern and the gate's own design), `proposal_tick_massmint_triage_20260901.md` (the 09-01 triage).

---

## Step 1 -- the recurrence is genuine (3 confirmed occurrences, same root cause)

| Gen | Chip | Spawned | Resolved | Trip metrics | Response taken |
|---|---|---|---|---|---|
| g1 | `chip-pausepressure-dlaptop` | 2026-08-29T13:32Z | 2026-08-30T08:17Z | `recorded_7d 716 > 150` | Consolidated update plan: 8 chips resolved/withdrawn, 2 skill holes patched, 40 open chips routed into 7 campaigns |
| g2 | `chip-pausepressure-dlaptop-g2` | 2026-08-30T15:50Z | 2026-09-01T15:29Z | `recorded_7d 704`; episodic gen>=2 `chip-queuefloor-fleet-g2`; `enablement_findings 1` | Curation cycle: 3 duplicate chips absorbed, 1 IGW chip withdrawn, 43 open chips bundled into 6 campaigns |
| g3 | `chip-pausepressure-dlaptop-g3` | 2026-09-02T05:49Z | 2026-09-02T16:56Z | `open_chips 72 > 40`; `recorded_7d 930`; episodic gen>=2 `chip-queuefloor-fleet-g2`; `enablement_findings 3` | **This root-cause pass** |

Same root cause across all three, not merely the same symptom: each trip is driven by the same two
accumulation signals in `scripts/pause_pressure.py` (`open_chips`, `recorded_7d`), and each was answered
with the same class of remedy (curate the chip backlog). Threshold for `/metaworker-learning` is 2; this is 3.

**g2 pre-registered the falsification test, and it has now fired.** Verbatim from its resolution note:

> BASELINE FOR GENERATION 3: chips recorded per week, counting back from 2026-09-01: 680, 593, 531, 249.
> Open-chip count at curation time: 46. **If generation 3 fires with weekly volume still above ~680,
> curation is not the lever and the mint rate itself needs investigating.**

g3 fired at `recorded_7d = 930`. Live at time of writing: **1039**. The volume did not fall after two
curation cycles -- it rose. Open chips went 46 (g2 curation) -> 72 (g3 trip) -> **195 (now)**.
The test g2 set has been passed unambiguously; curation is not the lever.

---

## Step 2 -- what the volume actually is

Decomposition of `recorded_7d` (1041 chips, window 2026-08-26T18:23Z -> 2026-09-02T18:23Z):

| Family | Count | Origin | Status split |
|---|---|---|---|
| `chip-proposal-*` | 303 | `proposal_tick` | 156 withdrawn / 120 open / 27 done |
| `chip-queuefloor-*` | 239 | `hygiene_tick` | 238 done / 1 open |
| `chip-<date>-*` (session/headless-authored) | 306 | `spawn_task`, `headless` | mixed |
| `chip-staleclaim-*` / `statusregress` / `strandedwt` / other detectors | ~150 | `hygiene_tick` | mostly done |

**52% of the 7-day mint is two automated generators.** And of the 195 chips open right now:

| | Open | Share |
|---|---|---|
| `chip-proposal-*` (`proposal_tick`) | **120** | 62% |
| session/headless-authored (`chip-<date>-*`, igw) | **57** | 29% |
| all `hygiene_tick` detectors | 18 | 9% |

115 of those 120 proposal chips were minted **today**, 99 of them inside a **3-minute window** (16:36-16:38Z).

### The genuine backlog has been roughly flat the whole time

The number a curation cycle can actually act on -- session/headless-authored open chips -- is **57**.
g2 curated against 46. g1 against ~40. That component has moved very little across three generations,
and both curation cycles did discharge real work against it. The aggregate the gate reads moved
in the opposite direction because the generators refilled it faster.

---

## Step 3 -- root cause

### Proximate driver (live, still firing): `proposal_routine_tick.py` has no mint cap

`run_tick()` is an unbounded fan-out:

```python
items = [it for it in data.get("items", []) if it.get("status") == "proposed"]
for item in items:
    ...
    chip_ledger.cmd_record(...)      # one chip per eligible proposal, no cap, no floor, no rate limit
```

`grep -n 'MAX|LIMIT|CAP|floor|FLOOR|per_tick|batch' scripts/proposal_routine_tick.py` returns nothing.
The only gate on the whole loop is `is_coordination_plane_paused`.

The tick's safety was argued in its own docstring from a **transient property of the data**, not a
structural bound:

> Verified live: as of this writing every real `status == "proposed"` item in the file is
> `literature`/`literature_review` -- there are currently ZERO experimental proposed items, so a live
> dry-run of this tick chips nothing.

When the proposals file gained experimental `proposed` items, the tick minted the entire eligible set
at once: **166 chips in two minutes on 2026-09-01**.

**The 09-01 remediation did not prevent recurrence, and this is the load-bearing observation.**
`proposal_tick_massmint_triage_20260901.md` withdrew 156 chips and built `proposal_backlog_dripfeed.py`
-- which establishes exactly the right semantics (`DEFAULT_FLOOR = 10`, "TOP-UP, NOT A SCHEDULE",
self-paces against actual throughput). But that pacing was put in a **separate downstream script**,
leaving the generator itself uncapped. So on 2026-09-02 the tick mass-minted again: **119 fresh chips**,
over a *different* EXP-id slice (09-01 minted 168 distinct proposal ids, 09-02 minted 124; **overlap: 5**).
The idempotency-by-chip_ref guard cannot help, because these are genuinely new refs. The drip-feed's
floor of 10 is simply bypassed -- 119 arrived around it in three minutes.

Timeline worth stating plainly: g3 fired at 05:49Z. The second mass-mint landed at 16:36Z. g3 was
resolved at 16:56Z. **The recurrence the gate was escalating had already recurred again, 20 minutes
before anyone closed the chip.**

### Root cause: the gate reports an un-attributed aggregate, so the response is decoupled from the driver

`pause_pressure.chip_metrics()` counts every chip in the ledger with no attribution whatsoever:

```python
open_chips  = [c for c in chips if c.get("status") == "open"]
recorded_7d = [c for c in chips if (c.get("spawned_at") or "") >= week_ago]
```

No filter on `origin`, `kind`, or generator. Consequences, in order:

1. **A mint-and-withdraw event inflates the metric for a full 7 days at zero real backlog.** The 156
   chips withdrawn on 09-01 still count toward `recorded_7d` today. They represent no undischarged work
   of any kind.
2. **Every newly-armed automated generator moves the metric directly**, without any structural work
   having accumulated. The thresholds (40 open, 150/7d) were calibrated before `proposal_tick`,
   before W5a, and before the detector suite reached its current breadth.
3. **The chip text names exactly one remedy** -- "accumulated structural work is cheapest discharged in
   a deliberate halt-campaign-restart window (the 2026-08-29 pattern)". That is a *backlog* remedy.

So each generation the responding session reads a high aggregate, is handed a backlog remedy, correctly
executes it against the ~46-57 chips that are genuinely backlog, and the aggregate does not move --
because 62% of it is a generator nobody was pointed at. **Three generations, three backlog remedies,
zero generator fixes.** The metric's lack of decomposition is what mis-routes the response; the
recurrence is a property of the gate's design, not of any responding session's diligence.

Supporting evidence that the information was genuinely missing rather than ignored: g2's session
*reconstructed the weekly volume series by hand* and wrote the pre-registered test, which is precisely
what a session does when the tool it is using will not tell it what it needs to know.

### Positive control: this exact lever already worked, on the other generator

The `chip-queuefloor-*` family had the identical pathology -- a per-event ref
(`chip-queuefloor-<host>-since-<ISO-timestamp>`) minting a new chip every tick. It produced
**226 chips in 14 days**, peaking at **142 in one day** (2026-08-27).

It was fixed **at the generator**, not by curating the output:
- `2bbc19a8e` W5a recurrence collapse -- one standing chip per (class, subject), coordinator episode
  verb instead of a fresh mint, generation minting on re-fire, 6h resolution hysteresis. Its own
  GOV-HELDOUT-1 check names the "226-queuefloor-chips case (collapse)".
- `46b0e30f8` collapse the standing chip to ONE fleet-wide ref.

Daily queuefloor mint after the fix: **142 -> 52 -> 23 -> 2 -> 0**. The family now contributes 1 open chip.

That same commit built the `/metaworker-learning` escalation at generation >= 3 that routed this chip
here. The machinery worked exactly as designed. The lever was simply never applied to `proposal_tick`,
which is not an episodic hygiene source and so was never in W5a's scope.

---

## Proposed durable fix (two parts -- NOT built; consent-gated per skill Step 4)

**Fix A -- cap the generator (`scripts/proposal_routine_tick.py`).**
Move the pacing from the bolt-on into the generator: keep at most N proposal chips OPEN
(`DEFAULT_FLOOR = 10`, the value the user already ratified on 09-01), mint only the shortfall, by
rank, per tick. Reuse `proposal_backlog_dripfeed.py`'s top-up semantics rather than reimplementing
them -- ideally by having the tick call into that module, so there is one pacing rule and not two.
This makes the drip-feed's floor actually binding instead of bypassable.
*Secondary, cheap:* a generic per-tick mint ceiling for any `*_routine_tick.py`, so the next uncapped
fan-out is bounded before anyone has to notice it.

**Fix B -- attribute the metric (`scripts/pause_pressure.py`).**
Report `open_chips` and `recorded_7d` decomposed by `origin`, and split the PRESSURE verdict into two
arms that route to different remedies:
- **backlog arm** (session/headless/spawn_task-authored chips) over threshold -> the existing curated
  pause-window recommendation. Threshold applies to *this* number.
- **generator arm** (any single automated `origin` over its own share threshold) -> a *generator* fix,
  naming the offending origin and its 7-day count. Explicitly NOT a pause window.

The verdict text must name the driver. Today it says "accumulated structural work"; on g3 the honest
sentence was "62% of your open chips came from `proposal_tick` in the last three minutes."

Cost note, stated rather than skipped: Fix B adds attribution logic to a script whose whole value is
being mechanical and seconds-fast, and every new arm is another thing to calibrate. Fix A risks
under-feeding the science tier if the floor is set too low -- the queue-floor starvation signal
(`chip-queuefloor-fleet-g2`, still open) is the opposing pressure, and these two must be tuned against
each other rather than independently.

---

## Held-out check (GOV-HELDOUT-1)

Three historical cases the fix was **not** written from. Old behavior = today's un-attributed gate
recommending a pause window; new = attributed verdict routing to a generator fix. All three are
non-degenerate (the two answers differ), and in all three the *historically taken* action was a
generator fix, which is what the new wording recommends and the old wording does not.

1. **226 queuefloor chips in 14 days (2026-08-26 -> 08-29), pre-W5a.** Old: `recorded_7d` massively
   over threshold -> PRESSURE -> curated pause window. New: decomposition shows ~100% `hygiene_tick`
   episodic churn on one class -> generator fix. **History: the fix was `2bbc19a8e` + `46b0e30f8`, a
   generator fix, and it drove the family to zero.** New wording gives the right call; old gives the
   wrong one.

2. **The detector false-positive campaign (2026-08-30, commits `015a5254e`, `2d9dab102`, `d82e75808`).**
   Measured FP rates in those commit messages: `statusregress` 52 lifetime chips / **100% FP** / zero
   repairs; `strandedwt` scratch-set drift causing **38 of 61** historical FPs; `hookgating` 9 chips in
   one 11.25h load window, all clean on re-check; `staleclaim` 10 chips over 5 days of C<->D flapping.
   Old: all of these inflate `open_chips`/`recorded_7d` indistinguishably from real work -> PRESSURE ->
   pause window. New: attributed to `hygiene_tick` detectors -> detector fixes. **History: a
   user-approved detector-FP campaign, i.e. generator fixes.** Right call.

3. **455 phantom `logs/wedge_repairs.jsonl` rows (commit `6784e8297`).** This one lands on a *different*
   pause_pressure signal (#3, `wedge_repairs_7d`, threshold 2), which is why it is a genuinely
   independent test of the same principle. Test-fixture paths were spawning real `--adopt` repairs and
   polluting the log. Old: `wedge_repairs_7d` far over threshold -> PRESSURE -> pause window. New:
   phantom/test-fixture rows attributed and excluded -> containment fix at the generator. **History: the
   fix was containment at the generator ("contain W4 wedge auto-repair to local checkouts").** Right call.

**Negative control -- the fix must not suppress a real pause.** g1's discharge (the consolidated update
plan: 8 chips resolved, 2 skill holes patched, 40 routed into campaigns) was genuine structural work that
a pause window genuinely did discharge. Under Fix B the backlog arm still counts 57 authored open chips
today against a threshold of 40, so the pause-window recommendation **still fires**. Attribution changes
what the gate blames, not whether it can still call for a pause. If a proposed implementation of Fix B
would have silenced g1, that implementation is wrong.

**Honest counterweight (required by GOV-HELDOUT-1, not to be dropped when this is quoted):** this
held-out check cost roughly a third of the session's cycles, and it is not free. It did change the
proposal -- an earlier framing of this pass was heading toward "cap `proposal_tick`" alone (Fix A only),
and case 3 in particular is what showed the metric defect generalizes beyond chip-count signals to
signal 3 as well, which is what made Fix B worth proposing at the same time.

---

## What was NOT done here, deliberately

- **Nothing was built or landed.** Skill Step 4 admits no "obviously safe" carve-out for shared
  fleet-wide machinery (`scripts/`), and both proposed files are exactly that.
- **`chip-pausepressure-dlaptop-g3` was already resolved** by the Orchestrator at 2026-09-02T16:56Z with
  an accurate note. It was not re-resolved.
- **The still-open `chip-queuefloor-fleet-g2`** (signal 2) is untouched. It is the opposing pressure to
  Fix A's floor and should be tuned against it, not before it.
- **Signal 4 (`enablement_findings`) was not chased.** Running `audit_mitigation_enablement.py` *from*
  `ree-cloud-4` produces ssh-to-self artifacts -- one "Permission denied" error string is split across
  three rows and read as three separate findings. That is a real measurement defect in the audit but a
  separate, smaller problem; noted here so the next reader does not re-diagnose it.

---

## Addendum -- generation 4, and a correction to its recorded explanation

Found while closing out this pass: **`chip-pausepressure-dlaptop-g4` already exists.** It spawned
2026-09-02T17:10:50Z and was resolved 17:53:16Z -- i.e. generation 4 fired and was closed *while this
generation-3 root-cause pass was being dispatched*. Trip metrics: `open_chips 178 > 40`,
`recorded_7d 1016 > 150`, same episodic gen>=2, `enablement_findings 3`.

That makes the count **four generations in five days**, and it strengthens rather than changes the
root cause above: g4's recorded response was *again* a backlog-side remedy ("letting normal dispatch
catch up"), the fourth in a row, and again no generator was touched.

### Two things in g4's resolution note that matter

**(1) It confirms the remedy text is not actionable -- corroborating Fix B from a different angle.**
Verbatim: *"the Orchestrator initially mis-framed 'schedule a full pause window' as a ready-to-run
procedure; the 2026-08-29 campaign it referenced is a one-time bespoke engineering campaign (already
landed), and section 12 of fleet_commit_sequencing_redesign_20260829.md states the pause-pressure gate
is still a TRIAL with no codified skill. Corrected with the user: no campaign executed."*

So the single remedy the chip names is not merely mis-routed (the finding above) -- it does not exist
as a runnable procedure at all. Every generation has been handed a pointer to a one-time historical
campaign as though it were a repeatable playbook. This is a second, independent reason the verdict text
must name the actual driver rather than prescribe a fixed response, and it should be treated as part of
Fix B's scope.

**(2) Its causal attribution is measurably wrong, and it is the version currently on the ledger.**
Verbatim: *"the Orchestrator had stopped the Dispatcher on both cloud boxes for ~50 min to avoid
contention with a concurrent /governance run, so normal dispatch throughput paused right as governance
minted ~100 chips."*

The ~100 chips are real -- 99 were minted in the 16:36-16:38Z window. **Governance did not mint them.**
They are `chip-proposal-exp-*` with `origin: proposal_tick`. And governance did not create the
eligibility either: counting `status == "proposed" AND proposal_type == "experimental"` items in
`evidence/planning/experiment_proposals.v1.json` across five revisions spanning the whole day gives

| Revision | Committed | experimental + proposed |
|---|---|---|
| `77b60c7bcd` (governance regen) | 05:56Z | 241 |
| `3cfc2317a8` | 15:09Z | 237 |
| `ca55d8610e` (index regen) | 16:59Z | 238 |
| `0bbbb38a2b` | 16:27Z | 239 |
| `37ba3edcbb` (governance regen) | 17:10Z | 238 |

**Flat at 237-241 all day.** There was no eligibility spike for governance to have caused. The pool
has been sitting at roughly that size the whole time.

### What that actually implies (a refinement, in the fix's favour)

`proposal_routine_tick` is idempotent per `proposal_id` (the chip_ref dedup), so it is not an unbounded
*growth* process -- it is an uncapped **one-time drain of a standing ~240-item backlog**. 168 distinct
proposals were drained on 09-01 and 124 on 09-02 (overlap 5), which is close to exhausting the pool.
Two consequences:

- The 120 currently-open proposal chips are largely the *residue of a completed drain*, so this
  particular family will not keep growing at today's rate. Anyone reading `open_chips 195` as runaway
  growth will be wrong -- which is exactly the misreading an un-attributed aggregate invites, and is
  the same error in the opposite direction from g4's.
- But the drain **re-arms whenever the pool grows**, and it drains in minutes rather than at the
  fleet's working rate. Fix A's value is precisely that it converts a minutes-long drain into a paced
  one at the floor the user already ratified. This is a throughput/pacing fix, not a containment fix,
  and the doc's Fix A wording should be read that way.

None of this weakens the root cause: whether the driver is a drain or a growth process, the gate cannot
tell you which, because it does not attribute. Four generations have now been answered with four
backlog-side remedies, one of which pointed at a procedure that does not exist and one of which blamed
the wrong producer. That is the cost of the missing attribution, stated as plainly as the evidence allows.

---

## Generation 5 (2026-09-06) -- the hold lane the gate could not see (/metaworker-learning root-cause pass)

**Recurrence confirmed genuine, not apparent.** `chip-pausepressure-dlaptop-g5` fired on 2026-09-05 (governance-20260905, "FIRED -- PRESSURE") and again on 2026-09-06 (governance-20260906 asked the user "what should this cycle record?"), after the generator arm had been fixed (wave-2 C5: stable proposal ids, claim-gate + evidenceability gates, floor 10) and after TWO curation cycles (wave 2 on 09-04, wave 3 on 09-06) had done exactly what the backlog arm asks: read every open chip, decide, and HOLD what is off the v3 critical path with a stated reason and a review date (2026-09-11). Backlog arm at the 09-06 read: authored open_chips 104 > 40.

**Root cause.** The backlog arm counted every authored open chip, including the 63 the two plans had deliberately parked. The hold was prose (section 3 of each plan), so the gate could not distinguish *curated-and-held* from *uncurated*, and a curation cycle moved the metric by zero. Generations 2-4 were the same defect one level down (generator churn read as backlog, fixed 2026-09-02 by the origin split); this is the same defect one level up.

**Fix landed (REE_Working `scripts/pause_pressure.py`, tests in `scripts/test_pause_pressure.py` HoldLaneTest).** A machine-readable hold lane, `evidence/planning/hold_lane.v1.json` (this repo), regenerated from the wave plan's section 3 at each wave-planning session. The backlog arm now trips on `open_chips_authored_actionable = authored - held`, and reports both numbers in the tripped line. **A hold is not a hide:** an entry whose `review_after` has passed counts again automatically, so parking something forever still trips the gate on the review date; automated-origin chips never count as held; a missing or unreadable lane file holds nothing. First read after landing: 41 actionable (> 40, still tripping by one) with 63 held, `recorded_7d_authored` 226 > 150 (the wave campaigns' own chips) -- so the gate stays PRESSURE honestly on the recorded-7d sub-signal, and the chip's own quiet-6h resolution rule is left to run.

**GOV-HELDOUT-1 record (deliberately stated as short).** Non-degenerate cases -- where the old and new predicate give different verdicts -- exist only from 2026-09-04 onward, because no plan-of-record hold lane existed before wave 2: (1) the 2026-09-05 firing (wave-2 HOLD of 66 chips in force; new predicate: 104-66 < 40 on the open-chips sub-signal, though recorded_7d still tripped); (2) the 2026-09-06 firing (this one). Generations 1-4 are degenerate for this change (no hold lane existed, both predicates agree). **Two cases, not three: the rule is scoped to its motivating incident and is shipped with that stated**, per CLAUDE.md's held-out discipline. The counterweight that keeps it from being a hide is the review-date expiry, which is the only part of the predicate that fires without a human.

**Decision chip raised** (`/metaworker-learning` Step 4): `chip-20260906-decision-pausepressure-hold-lane` -- the user's blanket "we really need to do all of this" (2026-09-06) authorised landing; the chip exists so a veto reverts one file.
