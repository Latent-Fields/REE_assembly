# statusregress detector: 14 findings, 19 sessions, 0 repairs

**Status: AWAITING USER REVIEW**

Raised by `/metaworker-learning`, session `metaworker-learning-statusregress-fp`, 2026-08-22T04:52:49Z.
Subject: hygiene_routine_tick.py source 17, the `chip-statusregress-*` detector.

---

## 1. What was measured

The detector walks `TASK_CHIPS.json`'s git history and flags any commit that regresses a
chip's `status` out of terminal, or clears `claimed_by` / `resolved_at`, without that
commit's own subject line declaring the mutation for that specific `chip_ref`. It landed
2026-08-19T02:58:05Z (`REE_Working 38b319a0`) and has never been modified since.

Yield over its entire life to date (2026-08-19 -> 2026-08-22, n=14 findings):

| metric | value |
|---|---|
| findings minted | 14 |
| headless sessions consumed | **19** (14 findings + 5 follow-on GC chips) |
| wall clock consumed | **12.5 h** (median finding 15.1 min) |
| **repair edits to TASK_CHIPS.json produced** | **0 of 14** |
| genuine-and-repaired | 0 |
| real regression, already self-healed before the worker arrived | 2 |
| legitimate declared action misread as a regression | 7 |
| flagged sha is a convergence/cherry-pick artifact | 3 |
| outright duplicate of an earlier finding | 2 |
| distinct rows implicated by the 13 non-bulk findings | 10 |
| findings concerning just 3 rows | **8 of 14** |

All 14 fired on a `claimed_by` clear. None fired on a live status regression.

---

## 2. The detector is not miscoded. Two of its stated design premises are false.

This matters for what the fix should be, so it is stated precisely. Flagging an
*already-self-healed* regression is **deliberate**, is the detector's whole reason to exist
(a point-in-time check is structurally blind to it), and is pinned by
`ChipStatusRegressionSelfHealTest`. Nothing below argues that should change.

What the block comment at `hygiene_routine_tick.py:5259-5355` gets wrong is the surrounding
cost and sharedness model.

**Premise 1 -- the cost of a false positive.** Verbatim: *"a false positive here costs a
human one grep against the live row, never a repair."*

Falsified. The finding is minted as `kind: work`, `origin: hygiene_tick`, which
`dispatch_candidate_order.py` classifies as dispatchable housekeeping. So it does not reach a
human doing a grep; it reaches a **headless worker** that performs full git archaeology.
Realised cost 19 sessions / 12.5 h / 0 repairs. The design anticipated one narrow
false-positive source (a `--message` override) and no rate at all -- *"no false-positive rate
was ever anticipated, measured, or recorded."*

**Premise 2 -- sharedness.** Verbatim: *"SHARED, not machine-local ... the SUBJECT (a
specific commit already pushed to a tracked, fleet-shared file) is visible to and identically
diagnosable from any box that has fetched it."*

Falsified for 12 of 14. Measured from the Mac main checkout, `origin` freshly fetched:

| | |
|---|---|
| flagged commits reachable from `origin/master` | **2 of 14** |
| flagged shas that do not resolve as a git object here at all | 9 of 14 |
| findings dispatched to a different box than raised them (`same_machine`) | **7 of 14 (50%)** |

Mechanism: the tick scans `pointer..HEAD` on the box's **local** branch, which includes
commits that have not yet reached origin. `ref_convergence` route-B then re-lands those under
**different shas**. The premise's "already pushed" clause does not hold at scan time.

This also falsifies the comment's third claim, that two boxes *"converge on the same finding
set."* Because `chip_ref` is keyed on the commit sha, the same underlying row transition
mints a *different* chip on each box. That is the duplicate mechanism, and it is why 3 rows
account for 8 of 14 findings -- `chip-20260821-heartbeat-hysteresis-remeasure` alone was
flagged 4 times, under 4 shas, investigated by 4 separate sessions, all concluding the same
thing.

**Third, unstated premise -- one declared mutation per commit.** The exemption regexes
require the *entire* subject to be `chips: resolve <ref> -> <status>` or
`chips: unclaim <ref>`. `metaworker-dispatch` routinely batches several claim/unclaim actions
plus a `record` into one whole-file write, so the subject names one ref while the diff
legitimately mutates others. This is the single dominant false-positive source (7 of 14).

---

## 3. Step 1 threshold: the honest reading, including the reading that cuts against this

`/metaworker-learning` fires on *recurrence*, so the counting has to be done explicitly rather
than assumed.

**The reading that does NOT qualify.** The skill's opening frames it as a class that "has been
fixed more than once." The detector has been fixed **zero** times -- confirmed by
`git log -S` on `chip-statusregress-`, `_chip_status_regression_findings` and
`_HYGIENE_STATUSREGRESS_PREFIX`, and by `git log -L` on the function body: all return only
the creating commit. On that reading this is a first patch and belongs to
`/metaworker-repair`.

**The reading that does qualify**, and which is the skill's own stated lineage --
`/failure-autopsy`'s MOVE-3 re-derive brake, "Nth occurrence of the same failure -> hard-gate
against repeating the same ineffective response." The failure has occurred 14 times and been
met 14 times with the identical ineffective response: dispatch a worker, audit the commit,
conclude "no repair needed," resolve, GC the worktree. Threshold is 2.

**Why the second reading should win here, on a substantive rather than definitional ground.**
The obvious one-off patch is actively dangerous. The dominant false-positive source is the
batched-write case, and the obvious repair is to widen the exemption regex to tolerate
multi-ref subjects. That would weaken precisely the discriminator the design identifies as
load-bearing: *"a 'chips: resolve OTHER-ref -> done' commit does NOT exempt a status
regression it also happens to carry on ref X, which is exactly the read-modify-write shape
this exists to catch."* A repair-scoped session, reading 7 of 14 findings blaming batched
writes, would very plausibly make exactly that change and silently destroy the detector's
only real capability. Deciding *not* to widen the discriminator -- and fixing the producer
instead -- is a design judgement with a held-out check attached, which is what this skill is
for and what `/metaworker-repair` is explicitly not scoped to run.

**Also relevant to scope:** this is not a candidate for the CLAUDE.md chip-exception list.
It gets an ordinary decision chip.

---

## 4. Options

The detector's subject field, `claimed_by`, has **no monotonicity invariant** -- that is why
`merge_origin_into_local`'s guard (`ddbafb8243`) covers the status half and deliberately does
not cover this half. So no option below makes the detector "smarter about legitimacy" in
general; that is not available.

**A. Fix the producer, not the discriminator (durable correctness).** Make `chip_ledger.py`
declare every ref a commit mutates -- e.g. a `chips-mutated: <ref>, <ref>` trailer written by
the same code that performs the whole-file write. The detector's exemption test then becomes
*sound* rather than *more permissive*: it keeps refusing to exempt an undeclared ride-along,
while a batched write truthfully declares all of its refs. Addresses the dominant FP source
(7 of 14) without touching the asymmetry. Cost: a change to the hottest registry writer in
the fleet, so it needs its own care.

**B. Stop routing a report-only signal through the dispatch queue (cost).** The detector is
documented "REPORT ONLY, NEVER REPAIR" and has no auto-resolution branch; yet it mints a
dispatchable `kind: work` chip. Record findings somewhere that does not consume a worker
(a log, or a non-dispatchable kind), preserving the audit trail the SelfHeal test protects
while removing the 19-session cost. This is the single highest-leverage change and is
independent of A.

**C. Per-row dedup (duplicates).** Suppress a finding whose affected rows are all already
named by an open statusregress chip. Same-file precedent exists: `_existing_chip_covering_sha`
(fail-open, terminal-status-aware, records the skip in meta rather than dropping it silently).
Would have suppressed at least 5 of 14.

**D. Sha-resolvability / host declaration (artifacts).** Ensure a finding is only worked where
its sha resolves, or declare the origin host in the prompt. **See the held-out check below --
the naive form of this option is wrong**, and it also overlaps the already-open decision chip
`chip-20260822-hygiene-machinelocal-prompts-declare-no-host`, which covers host declaration
for machine-local hygiene findings generally. These two should be decided together or
explicitly sequenced; they touch the same two files.

**E. Do nothing / accept.** Defensible only if the audit trail is judged worth 19 sessions per
3 days. Recorded because the detector is 3 days old and the underlying incident it watches for
is real and confirmed (`58d2532e`).

Recommendation: **B first** (largest cost reduction, no capability loss, independent of the
rest), then **A** (removes the dominant FP at its source), with **C** as a cheap addition.
**D** deferred to, or merged with, the existing open decision chip.

---

## 5. Held-out check (CLAUDE.md "General Rules"; GOV-HELDOUT-1)

Three cases the proposal was not written from, all pre-existing, all non-degenerate (old and
new behaviour genuinely differ). **The check changed the design** -- see case 1.

**Case 1 -- `chip-20260809-sqdrift-stale-checkout-fp` (2026-08-09). FALSIFIES the naive
form of option D.** `substrate_queue_writeback_drift.py` false-positived because it read the
**local** working tree on a box 24 behind origin. The obvious fix -- read origin instead --
was **rejected during that fix**, because the same box was also 23 *ahead*: reading origin
alone *inverts* the bug, falsely accusing an entry corrected locally and not yet pushed. The
implemented fix was **two-view agreement** (report only if working tree AND remote-tracking
ref agree), pinned by `test_the_working_tree_stays_the_PRIMARY_view`.

Applied here: my draft gate "only mint if the flagged sha is reachable from `origin/master`"
gives the **wrong** call under this precedent -- it would silence a genuine regression
committed locally on an ahead box, which is exactly the read-modify-write scenario the
detector exists for. Option D is revised accordingly: unresolvability may **downgrade or
annotate** a finding, never suppress it.

**Case 2 -- `chip-20260817-hygienetick-strandedwt-tip-only-blob-compare` (2026-08-18).**
Same file, same class (a hygiene detector reaching a false verdict from an insufficient git
comparison). Its fix preserved a specific risk asymmetry: *"True only on POSITIVE proof of
reachability, so an undecidable walk ... still REPORTS."* Applied here, this sets the correct
polarity for options C and D: an undecidable check must fall toward **still reporting**, never
toward silence. Old wording (no suppression at all) and new (suppression with a defined
polarity) differ; this case pins which direction the new one must fail.

**Case 3 -- `chip-20260818-hygienetick-sessionuuid-scratchfile` (2026-08-18). NEGATIVE
CONTROL.** Also a hygiene-tick false positive, also in the same file, but its mechanism is a
missing filename in a scratch-file set -- nothing to do with git comparison, dispatch routing
or dedup. The proposal must leave it entirely unaffected, and does. Its resolution also
carries a discipline note worth importing verbatim: *"a name goes on it only on MEASUREMENT,
never resemblance."* This case is what stops options B/C being generalised into "hygiene
findings shouldn't be dispatched," which would be wrong -- that finding was correctly
dispatchable once true.

**Honest counterweight.** The held-out check cost roughly an hour of this session and is not
free; CLAUDE.md is explicit that optimising for easily-checked quality can trade against
depth. Here it paid for itself by killing a wrong gate before it shipped. That is one data
point for GOV-HELDOUT-1, recorded as such -- not proof the practice works.

---

## 6. What this session did NOT do

No code was changed. No fix was built. Per `/metaworker-learning` Step 4, a durable fix to
shared fleet-wide machinery does not get built before a decision chip is answered, and there
is no "obviously safe" carve-out. Claim `metaworker-learning-statusregress-fp` is open.

Known adjacent item: `chip-20260822-hygiene-machinelocal-prompts-declare-no-host` (open,
`kind: decision`) declares the same two resources. Whoever acts on either should check the
other first.
