**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry) beyond the single governance flag (GFLAG-0099) explicitly noted below, which was raised through `governance_flag.py` per standing procedure.**

# repr->authority->selection research thread -- status note, 2026-08-29T02:09:38Z

Session: `metaworker-chip-20260828-repr-authority-selection-thread-resume` (headless,
unattended -- see "why no AskUserQuestion" at the end). This is the fourth session
in the thread (after `insights-7fd98a`, `elated-nobel-914234`, and one dispatch
attempt that died mid-flight without closing -- see Coordination note below).

This note does two things: (1) corrects a stale claim carried forward in the
dispatch brief, and (2) reports one new cross-linked finding, raised as
**GFLAG-0099**. No claim status was changed and no substrate was built.

---

## 1. Correction: "S9.9d grain-arbitration path still open" is stale

The dispatch brief (written by `elated-nobel-914234`, 2026-08-28) listed as
STILL OPEN: *"S9.9d's cheap non-exotic path (arbitrate MECH-288's already-two-scale
segmenter) is unaffected and still open."*

That is a conflation of two different questions. **"Unaffected" is correct** --
GFLAG-0090 (raised by that same session) established that the S9.9d ordering does
not depend on ARC-004's depth-is-timescale premise, which is what GFLAG-0090 was
actually checking. But **"still open" is not correct** as a description of the
probe's viability: `ARC-134` (registered 2026-08-26, the *same day* as the S9.9d
material, by an earlier session in this thread) already states the perceptual
analogue of ARC-069 that S9.9d step 1 called for, and **its own `digestion_note`
already closed S9.9d step 2's specific probe design** -- for three independent
reasons, none about ARC-004:

1. **Largely already run.** V3-EXQ-830 (2026-07-27) is a scale-resolved probe on
   the rollout stream and returned PASS / `non_contributory`, `claim_ids: []`,
   with the slow scale never firing on the rollout stream at all
   (`on_n_sweeps_slow_only: 0` across 2393 sweeps).
2. **No arbitration point exists by design.** Every MECH-288 consumer
   (AnchorSet, StalenessAccumulator, `per_region_vs`) keys on the tuple
   `(scale, segment_id)` and both scales are maintained **in parallel** as
   separate region keys. There is nowhere for an arbitrator to sit; adding one
   would select between two config-fixed grains, not produce a variable
   occupancy count.
3. **Wrong axis.** MECH-288's grain is along TIME (event segments); ARC-134 is
   about carving a SCENE (part-whole). ARC-070 can legitimately borrow the
   segmenter because a policy IS a sequence; a percept in the part-whole sense
   has no sequence to segment.

So the honest current state of the ephaptic/grain leg is: **step 1 is done**
(ARC-134 registered, `candidate`, `v4`), **step 2 as originally conceived is
closed** (not viable, not merely deferred), and **what remains open is ARC-134's
own P0-P3 non-degeneracy preconditions**, all four of which are currently FALSE
in V3 and none of which either ARC-134 or MECH-521 wants built now (both are
explicit: `implementation_phase: v4`, and MECH-521's own notes say "DO NOT build
in V3. DO NOT queue an experiment.").

**Practical consequence:** there is currently no cheap next empirical step on
this leg. The remaining work is desk-level (claim-text amendment, see below) or
gated behind a V4/V5 substrate build (an endogenous perceptual merge/split
operator) that is out of scope for this thread right now.

---

## 2. New finding: GFLAG-0096 and the elated-nobel MECH-448 finding are the same gap

Two things landed in this thread within 48 hours of each other and were never
connected until now:

- **GFLAG-0096** (raised 2026-08-28 by the orphan-prerequisite-investigation
  chip): MECH-521's own derivation toy
  (`mech521_settling_signature_derivation_20260826.md`) found that settling
  alone gives only the pure slot horn (fidelity pinned at 1.000, no graceful
  phase); a **shared normalisation budget** is the missing third ingredient
  needed to reproduce the claimed hybrid signature, and it is "already in REE"
  as the form MECH-448's rank-preserving eligibility envelope
  (`e3_selector.py:_loop_normalize`) uses. The doc's own recommendation --
  amend MECH-521 to name this as a required third factor and re-point part of
  the falsifier at it -- was never applied.
- **`elated-nobel-914234`'s 2026-08-28 finding** (recorded in its closing note,
  not a governance flag): MECH-521's "third ingredient already in REE" claim is
  "right form, wrong population" -- MECH-448 IS a genuine divisive
  normalisation, but it normalises over **E3 action candidates**, and nothing
  normalises over an **online perceptual slot population**, because that
  population does not exist. (ARC-134 itself says so.)

Read together: these are **the same gap from two angles**, not two separate
findings. Verified by tracing both to their root: MECH-521's own `what_would_answer`
already carries this as **P0** ("THE UNIT COUNT MUST BE ENDOGENOUS --
`ObjectFileBuffer.update()` consumes a caller-built `List[EntityObservation]`...
so occupancy today measures the ENVIRONMENT, not the agent"), and it is
**identical** to ARC-134's own **P0** ("AN ENDOGENOUS GRAIN OPERATOR MUST EXIST
-- it does not... there is NO merge and NO split of tokens anywhere"). Until
that operator exists, there is no perceptual-token population for *any*
normalisation scheme -- MECH-448-shaped or otherwise -- to run over. So
GFLAG-0096's amendment is correct and free to make (it sharpens the claim's
desk-level derivation), but **it does not unblock any actual test**: the real
gate is the shared P0, which both claims explicitly decline to build in V3.

This was raised as **GFLAG-0099** (`stale_note`, claims `MECH-521`, `ARC-134`,
`MECH-448`), landed on `REE_assembly` origin/master (`5962b580a5` /
`bac114d474` after ref-convergence), so that `/governance` sees the connective
finding alongside GFLAG-0096 rather than adjudicating it in isolation.

---

## 3. Standing-agenda item 3 ("do new answers pull new directions into V3?")

Re-checked for this leg specifically: **no.** ARC-134, MECH-521, and MECH-522
are all `v4`/`v4_v5` and none of their preconditions are met; none of them
propose V3 work. (Contrast with the ARC-004 leg, where `elated-nobel-914234`
found the serial-smoothing wiring DOES reach V3, per GFLAG-0088.) So on this
leg the answer to the standing question is "not yet, and not expected to be
until the P0 grain-operator gap is closed" -- which is itself useful to have
stated explicitly rather than left implicit.

---

## 4. Still open, unchanged from the dispatch brief

- **The affect-persistence reading** (item 2 in the dispatch brief): genuinely
  untouched this session. Requires the user's directional pick between the
  "unfalsifiable" reading (already worked) and the literal-persistence reading
  (offered, not chosen).
- **GFLAG-0054, 0055, 0088, 0089, 0090, 0091, and now 0094-0099**: all still
  `open`. Governance has not yet run a cycle since the last one closed
  (2026-08-28T18:26:14Z) that would adjudicate any of these.

---

## Coordination note (for the record, not for the user to act on)

This chip (`chip-20260828-repr-authority-selection-thread-resume`) was
dispatched twice to the same worktree: a first attempt (session_uuid
`01ac71af...`, dispatch cycle 766 on `ree-cloud-4`) opened both the chip claim
and a `TASK_CLAIMS.json` entry (`repr-authority-selection-thread-resume-20260828`,
22:41:00Z) but never closed -- consistent with the "killed while blocked on a
question" hazard the brief itself warns about. This session (session_uuid
`4d103c48...`) is the redispatch; the coordinator's live chip-claim state
already reflected the handover correctly. The orphaned `TASK_CLAIMS.json` entry
and two legitimately-different concurrent GOV-APPLY-1 claims on `claims.yaml`
were resolved via `--allow-overlap` rather than blocking on them (documented in
this session's `task_claim.py open` call and its `chip_ledger.py resolve` note).

## Why no `AskUserQuestion` this session

This session is a headless, unattended `claude -p` dispatch (per the worker
contract in its own system prompt) -- not a live interactive session the user
is watching. The thread's own hazard note is explicit: a prior session in this
exact thread was killed by its daemon while blocked on a question the user
never saw. So rather than opening a blocking question, this session did the
work above that does not depend on the user's answer, and leaves the open
choice (which of the STILL OPEN items to pick up next -- item 2 above, or
something else) for the next *interactive* session to actually ask.

---

## Addendum, 2026-08-29T02:35:14Z (fifth session, `633c57e0-...`, headless)

Re-verified everything in this note against live state; nothing has changed
since the fourth session wrote it roughly 25 minutes earlier:

- **No `/governance` apply cycle has run** since the 18:26:14Z (2026-08-28)
  wave cited above (`git log --since` on `REE_assembly` confirms the next
  commits are all lit-pull/planning/heartbeat/GOV-APPLY-1-partial traffic,
  no governance apply pass).
- **All 12 open flags** (GFLAG-0054/0055/0088/0089/0090/0091/0094-0099)
  re-read from `evidence/planning/governance_flags.v1.json`: still `open`,
  unchanged targets. GFLAG-0096 in particular is still unratified, so the
  MECH-521 `what_would_answer` amendment it recommends was correctly left
  unapplied (per the brief's own conditional).
- **claims.yaml unchanged**: ARC-133/134 and MECH-516..523 all still
  `candidate`, same `implementation_phase`/`v3_pending` values as before.
- **`chip_ledger.py list --status open`** has no new follow-on chip tied to
  this thread's claims (MECH-521/ARC-134/MECH-448/GFLAG-0094-0099) beyond
  what already existed. Two things worth naming for the record, neither
  acted on because they are outside this chip's scope:
  - `chip-20260826-representation-authority-selection-bottleneck` (the
    thread's original, broader "develop the thought" chip) shows a claim by
    session `c6a1254b-...` at `2026-08-29T00:59:57Z`, but `ps aux` on this
    box (`ree-cloud-5`, the same host the claim names) shows no live
    process for that session -- so that claim is very likely stale/dead,
    not a live parallel session. Left alone; it is a hygiene-tick /
    zombie-reaper concern, not this chip's.
  - Two prior dead-dispatch worktrees for this exact resume chip
    (`metaworker-chip-20260828-repr-authority-selection-thread-resume`) and
    the litpull sibling (`metaworker-chip-20260826-litpull-repr-authority-
    selection-family`) still exist on disk. Not touched here either --
    worktree GC is a separate concern from this thread's research content.

**Net effect of this session: verification only, no new substance.** The two
STILL OPEN user-facing items (affect-persistence reading; whether to
commission ARC-134's P0 build) remain exactly as the fourth session left
them, and still require an interactive session to ask. No new `GFLAG` was
raised and no claim was touched.

## Addendum, 2026-08-29T03:08:47Z (sixth session, headless)

Re-verified everything again against live state; nothing has changed since
the fifth session's addendum ~33 minutes earlier:

- `git -C REE_assembly log --since "2026-08-29T02:35:14Z" --oneline` shows
  only two `phase3-heartbeats:` orchestrator-tick commits and the fifth
  session's own addendum commit (`2409f74c09`) -- no `/governance` apply
  cycle, no lit-pull, no claim edits.
- All 12 flags (GFLAG-0054/0055/0088/0089/0090/0091/0094-0099), re-read
  directly from `evidence/planning/governance_flags.v1.json`'s `items` list:
  still `status: "open"`, unchanged. GFLAG-0096 remains unratified, so the
  conditional MECH-521 `what_would_answer` amendment stays correctly
  unapplied.
- `claims.yaml`: ARC-133/134 and MECH-516..523 all still `candidate`, same
  `implementation_phase`/`v3_pending` values as every prior check in this
  thread.
- `chip_ledger.py list --status open` has no new follow-on tied to this
  thread beyond this session's own resume chip
  (`chip-20260829b-repr-authority-selection-thread-resume`). The two
  previously-noted informational items (the possibly-stale claim on
  `chip-20260826-representation-authority-selection-bottleneck`, and the
  leftover dead-dispatch worktrees) were not re-checked in depth this
  session since nothing about them is this chip's job to resolve and
  neither had changed on the last check.

**Still headless -- no `AskUserQuestion` opened, for the same reason as every
prior session in this thread.** The two STILL OPEN user-facing items above
are unchanged and still need an interactive session. This session is closing
as a no-op verification per its own dispatch brief's standing-work item 5
("if nothing changed and nothing new landed... stop there, do not manufacture
busywork") rather than inventing unrequested substantive work.

---

Addendum, 2026-08-29T03:43:07Z (seventh session, `c918dfa4-...`, headless):
re-checked at this timestamp -- still no change (no governance apply cycle,
all 12 flags open, claims.yaml unchanged, no new relevant chips). This is now
**four consecutive no-op sessions** (4th-7th). Per the brief's own
instruction, surfacing rather than deciding: the same-cadence automatic
resume no longer seems to be finding anything to act on, and may be better
served waiting for an actual triggering event (a governance apply cycle
landing on the flags above, or the user returning) rather than continuing at
the current cadence. Not stopping the resume chip over this without the
user's say-so -- one more resume chip spawned below per standing
instructions.

Addendum, 2026-08-29T04:15:37Z (eighth session, headless): re-checked --
still no change (no governance apply cycle since 03:43:07Z, all 12 flags
open, claims.yaml unchanged since 2026-08-28T21:00:57Z, no new relevant
chips). **Five consecutive no-op sessions now (4th-8th).** Same cadence
observation as the seventh session stands, restated rather than
re-litigated. One more resume chip spawned below per standing instructions.

Addendum, 2026-08-29T04:46:28Z (ninth session, headless): re-checked --
still no change. `git log --since "2026-08-29T04:15:37Z"` on `REE_assembly`
shows only `phase3-heartbeats:` orchestrator ticks plus the eighth session's
own addendum commit -- no `/governance` apply cycle. All 12 flags
(GFLAG-0054/0055/0088/0089/0090/0091/0094-0099) re-read directly from
`evidence/planning/governance_flags.v1.json`: still `open`, unchanged.
`claims.yaml`: ARC-133/134 and MECH-516..523 all still `candidate`, same
`implementation_phase`/`v3_pending` values. `chip_ledger.py list --status
open` has no new follow-on tied to this thread's claims beyond what already
existed (this session's own resume chip, a pre-existing stale-claim hygiene
chip for an earlier dead-dispatch worktree, and unrelated chips). **Six
consecutive no-op sessions now (4th-9th).** Same cadence observation as the
seventh/eighth sessions stands, restated rather than re-litigated: the
thread is currently waiting on an external trigger (a governance apply
cycle landing on these flags, or the user returning), not on further
same-cadence polling. Continuing per standing instructions without
unilaterally slowing or stopping the resume cadence -- one more resume chip
spawned below.

Addendum, 2026-08-29T05:19:52Z (tenth session, headless): re-checked --
still no change. `git log --since "2026-08-29T04:46:28Z"` on `REE_assembly`
shows only `phase3-heartbeats:` orchestrator ticks plus the ninth session's
own addendum commit -- no `/governance` apply cycle. All 12 flags still
`open`, unchanged; `claims.yaml` unchanged; no new relevant follow-on chip
(only the same pre-existing stale-claim hygiene chip and this session's own
resume chip). **Seven consecutive no-op sessions now (4th-10th).** Per the
brief's own instruction at this threshold: restating rather than deciding --
the resume cadence is still finding nothing to act on, and the wait is on an
external trigger (a governance apply cycle landing on these flags, or the
user returning), not on more polling at the current interval. Not
unilaterally slowing or stopping the cadence without the user's say-so --
one more resume chip spawned below.
