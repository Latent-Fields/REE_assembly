# Cross-dispatcher-cycle collision detection: feasibility investigation

**Status: AWAITING USER REVIEW.**

Chip: `chip-20260817-hygienetick-crossdispatcher-collision-scan`
Date: 2026-08-18 | Box: ree-cloud-5 (headless metaworker worker)
Outcome: **detector NOT built -- withdrawn on evidence.** Two durable-fix chips spawned instead.

---

## 1. What was asked

Build a `hygiene_routine_tick.py` finding-source that detects cross-dispatcher-cycle
collisions, per the gap named in
`evidence/planning/metaworker_support_skill_design_staged_20260817.md` section 1c
("only one artifact trace exists, caught incidentally via the chip-ledger-integrity
category, not a purpose-built detector").

The proposed signal, from the chip brief: flag when two DIFFERENT `claimed_by` values
in `TASK_CHIPS.json` carry `claimed_at` timestamps within a short window, with a
deliberately conservative false-positive-reduction approach.

The brief also stated the outcome bar explicitly: *"do not ship something noisy just to
close the chip... rather than landing a source that will train people to ignore
hygiene_tick chips."* That bar is what this investigation ended up turning on.

## 2. Conclusion, up front

**The detector should not be built yet, and the per-episode chip shape is wrong
regardless of data quality.** Three independent findings, in increasing order of
importance:

1. **`TASK_CHIPS.json` contains no usable machine discriminator.** Every candidate was
   tested against the live 435-claim corpus and every one failed. (Section 3.)
2. **The only working discriminator is out-of-band and seasonally fragile** -- git
   author timezone offset. It silently degrades to useless every winter. (Section 4.)
3. **Granting that discriminator, collisions run at ~3 episodes/day, continuously, for
   the entire 16-day measurement window.** Overlap is the steady state, not an incident.
   A per-episode chip source would emit ~3 chips/day forever, and the correct response
   to a permanently-elevated rate is one durable fix, not 46 chips. (Section 5.)

Finding 3 is the load-bearing one. Findings 1-2 say *"you cannot measure this well
today"*; finding 3 says *"even measured perfectly, this is the wrong artifact shape."*

## 3. No in-ledger machine discriminator exists

Corpus: `TASK_CHIPS.json` at 2026-08-18T06:30Z -- 935 chips, of which **435** carry both
`claimed_by` and a parseable `claimed_at`. `claim_note` is present on 434 of the 435.

### 3a. `claimed_by` -- confirmed unusable, as the brief said

Free-text, session-id-shaped: 358 are bare uuid4, the rest are worktree slugs or ad-hoc
labels. No host component. `chip_ledger.CONTENTION_EXIT` (code 3) is a process exit
status and is never persisted, so there is no ledger trail of actual claim races to mine.
Both points in the brief are confirmed.

### 3b. Worktree root in `claim_note` -- looked decisive, is a RED HERRING

`metaworker-dispatch/SKILL.md` step 4c always passes
`--note "worktree $WT (dispatched by this metaworker-dispatch cycle)"` with `$WT`
absolute, and 359/435 (82.5%) of notes carry a parseable root. The roots partition
cleanly into two values, which reads as a free host discriminator:

| root | claims |
|---|---|
| `/Users/dgolden/REE_Working` | 342 |
| `/home/ree/REE_Working` | 17 |

**It is not a host discriminator.** `metaworker-dispatch/SKILL.md` *hardcodes* the Mac
path in `WT=`, so a dispatcher on ree-cloud-5 that follows the skill literally writes a
`/Users/dgolden/...` path while running on the cloud box. Measured directly: of the 342
Mac-rooted claims, **226 explicitly name `ree-cloud-5` in the same note**.

This was the investigation's first working hypothesis and it was wrong. Recorded here so
the next session does not re-derive it: cross-root pair counts looked encouraging (88
naive pairs at W=60s down to 2 cross-root, a 97.7% reduction) and were meaningless.

### 3c. Explicit host token in `claim_note` -- real, but only one box ever uses it

Scanning notes for fleet host tokens (`ree-cloud-N`, `ree-worker-N`, `DLAPTOP[-N]`,
`Daniel-PC`, `EWIN-PC`) finds one in 249/435 (57%).

**A correction that matters:** a naive scan over the whole note is wrong, because chip_refs
themselves embed host names (`chip-strandedwt-ree-cloud-5-...`, `chip-refwedge-dlaptop-...`)
and the note embeds the worktree path, which embeds the chip_ref. Six claims were
attributed to the host named in their own *subject*. After stripping the `worktree <path>`
span first, 243/435 (56%) remain attributable -- and the distribution collapses:

| attributed host | claims |
|---|---|
| `ree-cloud-5` | 242 |
| `ree-cloud-4` | 1 |

The single `ree-cloud-4` row is *also* a subject mention, not a dispatcher self-ID:
`"worktree mel-dose-sweep-inv-051-6b93d7 -- verifying live PHASE3_SPOOL_SIDEFILES state on
hub + ree-cloud-4"`.

**So: zero claims in the entire corpus are attributable to the Mac dispatcher.** The cloud
dispatcher self-identifies by hand (`"...ree-cloud-5, cycle 2753"`); the Mac adds nothing
equivalent, because the skill's note template contains no host field. Cross-host pair
count over the whole corpus: **0 at W=300s, 0 at W=600s**; the 3 pairs at W=1800s all
derive from the false `ree-cloud-4` attribution above.

Recall for the exact event the detector exists to catch (Mac dispatcher || cloud
dispatcher) is therefore **structurally zero**, not merely low.

### 3d. The `"interactive"` prose token -- a coin flip

The Mac dispatcher's notes sometimes read `"(dispatched by this metaworker-dispatch cycle,
interactive...)"`. Tested as a weak discriminator against the tz ground truth of section 4:

| | note contains "interactive" | does not |
|---|---|---|
| Mac (+01:00) | 121 | 88 |
| cloud (+00:00) | 121 | 406 |

Precision 50.0%. Free prose written by whichever session happened to be dispatching, not a
template field. Unusable.

## 4. The only working discriminator is out-of-band, and seasonally fragile

Git **author timezone offset** on `chips: claim` commits separates the two dispatchers
cleanly, because git stamps the committing box's local TZ and ree-cloud-5 runs UTC while
the Mac runs Europe/Dublin:

- 736 `chips: claim` commits on `origin/master` in the trailing 16 days.
- **527 at `+00:00`** (ree-cloud-5) / **209 at `+01:00`** (Mac interactive dispatcher).
- Author TZ == committer TZ in all 736, so `ree_commit.py`'s cherry-pick push-retry does
  not confound the signal.
- Validated against note content: every `+01:00` sample carries `"interactive"` and/or a
  Mac-only marker; every `+00:00` sample that self-identifies says `ree-cloud-5`.

Note this also *quantifies the invisibility* in section 3c: ~28% of claims are
Mac-dispatched and none of them are attributable from the ledger.

**Why this must not be built on.** The offset is `+01:00` only during Irish summer time.
From late October the Mac also commits at `+00:00` and the discriminator becomes a
constant -- no error, no log line, the detector simply stops finding anything. That is
precisely the failure class CLAUDE.md documents for `--laptop-yield-to-cloud`, which was
silently disarmed for three weeks by a raw hostname comparison. Shipping a detector whose
core signal dies on a calendar date, in a file nobody will re-audit in October, is worse
than shipping nothing.

Git authorship is not an alternative: **all 736 commits are authored `REE Automation (Mac)
<nooarche@users.noreply.github.com>`** -- the fleet-wide bot identity. Identical on both
boxes.

## 5. The decisive finding: collisions are the steady state, ~3/day

Using the section-4 tz discriminator as ground truth, over the trailing 16 days:

| window W | cross-TZ claim pairs | distinct episodes | rate |
|---|---|---|---|
| 300s (one cloud-5 timer grid cell) | 77 | ~46 | **~2.9/day** |
| 600s | 167 | ~96 | ~6.0/day |
| 1800s | 518 | ~200 | ~12.5/day |

The Mac interactive dispatcher and ree-cloud-5's 5-minute systemd timer overlap
**several times a day, every day, for the entire window**. The flock guard installed
2026-08-09 (`chip-20260809-metaworker-cycles-overlap`) fixed *same-box* reentrancy and is
per-box by construction; there is no cross-box coordination of any kind. The timing-offset
scheme the user described -- querying cloud-5's timer grid and offsetting by the midpoint
-- is documented nowhere in `metaworker-dispatch/SKILL.md` (confirmed by full read, both
during the 1c design research and again here).

**This is what makes the per-episode chip shape wrong independently of everything above.**
A hygiene source emitting one chip per episode would emit ~3/day indefinitely. Each chip
would be individually true and collectively useless, and it would be doing so about a
condition whose correct remedy is a single fix applied once. That is the exact outcome the
chip brief warned against.

It also means the "one artifact trace" framing in design-doc section 1c understates the
problem by roughly two orders of magnitude: this is not a rare event that went undetected,
it is a continuous regime that nothing was measuring.

## 6. What should be built instead (in this order)

**Fix A -- `chip_ledger.py cmd_claim` should stamp `claimed_host`.**
`cmd_record` already stamps `origin_host` from `chip_ledger.local_host()`, for exactly
this class of reason (its own docstring: "a consumer can tell 'this finding is mine to
judge' from 'this finding belongs to another machine'"). `cmd_claim` writes
`claimed_by`/`claimed_at`/`claim_note` and no host. Adding `claimed_host` alongside them
is a few lines with an in-file precedent, and it takes attribution from 56%-and-wrong to
100%-and-exact with no prose parsing and no seasonal dependency. Chip:
`chip-20260818-chipledger-claim-stamps-claimed-host`.

**Fix B -- close the cross-box dispatch overlap itself, and document the offset scheme.**
The ~3/day measurement above is the finding; the remedy needs live human judgment
(is concurrent cross-box dispatch acceptable? should the Mac dispatcher yield to the cloud
grid, mirroring `--laptop-yield-to-cloud`? should the offset scheme be written into
`metaworker-dispatch/SKILL.md` and enforced?). Raised as a **decision** chip, not a work
chip: `chip-20260818-crossbox-dispatch-overlap-decision`.

**Then, and only then, a detector -- as a RATE/REGIME source, not a per-episode one.**
Once `claimed_host` exists, the right shape is a single chip when the cross-host claim rate
over the lookback exceeds a threshold, with a *stable* chip_ref (so it does not re-mint per
episode), no auto-resolve branch, and the "PROXY SIGNAL, NOT A VERDICT" prompt framing the
classifier-block source established. That collapses 46 episodes into one standing finding
and is genuinely low-noise. It is deliberately **not** built here: with zero historical
cross-host pairs it could only be tested against synthetic data, and it would sit dormant
and unvalidated until Fix A lands. The design is recorded here so the follow-on does not
re-derive it.

## 7. Gate / provenance

`scripts/hygiene_routine_tick.py` and `scripts/test_hygiene_routine_tick.py` were **not
modified** -- the conclusion is that no source should be added yet. Baseline recorded
anyway before the investigation began: `scripts/test_hygiene_routine_tick.py` -> **285
tests, OK** (2026-08-18T06:30Z).

A live sibling session (`chip-20260817-hygienetick-clinicalhours-guard-check`) held the
`task_claim.py` arbitration claim on `scripts/hygiene_routine_tick.py` throughout this
work. Per the chip brief's own instruction the two were **sequenced, not raced**; since the
outcome is withdrawal, no edit to the contended file was ever needed and the contention
resolved without waiting.

All figures above are reproducible from `TASK_CHIPS.json` and
`git log --format=%aI --follow -- TASK_CHIPS.json` on `origin/master`.
