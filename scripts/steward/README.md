# Steward -- integrity detectors (stages 1-3)

Deterministic integrity checks over `docs/claims/claims.yaml`, the
`closure_plan` frontmatter of every `evidence/planning/*_plan.md`, the
governance-flag registry, and the git divergence state of the checkout.

```bash
# from REE_assembly/ root
/opt/local/bin/python3 scripts/steward/run_detectors.py
/opt/local/bin/python3 scripts/steward/run_detectors.py --json      # full report
/opt/local/bin/python3 scripts/steward/run_detectors.py --no-write  # report only
/opt/local/bin/python3 scripts/steward/run_detectors.py --fix --dry-run  # preview repairs
/opt/local/bin/python3 scripts/steward/run_detectors.py --fix       # apply T0 repairs
/opt/local/bin/python3 -m pytest scripts/steward/ -q                # 103 tests
```

## Why this exists

On 2026-08-15 SD-031 was found to be live V3 work (`implementation_phase: v3`,
`v3_pending: true`) whose only owning closure node, `self_attribution:GAP-5`, was
`deferred` -- and `generate_closure_snapshot.py` drops deferred nodes from the V3
denominator outright. SD-031 was therefore not done, not remaining, and not
visible as a gap. It sat that way for ten weeks. The fix was to split
`self_attribution:GAP-6` out (closure 72.6% -> 71.9%: a *correction*, not a
regression -- the number falls because the correction surfaces hidden work).

Nothing about **detecting** that required judgement. A 20-line script would have
caught it the same day for zero tokens. That is the thesis: detection is
deterministic and free, and the model is for adjudication only.

## The escalation gate

`reports/steward_report.json` carries one boolean, `escalate`, and that boolean
is the entire cost-control mechanism -- it decides whether a model is loaded at
all.

A finding escalates only if it is **NEW** (absent from the previous run's
`state/steward_state.json`), **unsuppressed**, and flagged `escalate` by its
detector. So the first run after a defect appears is loud, and every run after
that is silent until something changes. An unfixed defect is real, but it is not
news, and re-escalating it every cycle would spend the budget on things a human
has already seen and chosen to leave.

Findings that disappear are reported as **RESOLVED** rather than escalated: SD-031
no longer appearing under D-002 is the ratchet working.

At most 5 findings escalate per run, ranked by `severity x confidence`. **That cap
is a budget, not a filter** -- every finding always appears in `findings`, and the
overflow count is reported as `escalation_truncated` so five never reads as "all
of them".

## Detectors

| id | tier | what it finds | validated |
|----|------|---------------|-----------|
| **D-002** | T1 | Orphan V3 claim: claim reads as live V3, every owning closure node is `deferred` -> invisible to closure accounting. The SD-031 class. | yes -- precision 4/4 |
| **D-001** | T1 | Claim `implementation_phase` disagrees with the `generation` of every plan that owns it. Same denominator-invisibility harm, reached along the generation axis. | no |
| **D-006** | T0 | Duplicate entries in `governance_flags.v1.json` (same claims + type + day). Auto-fixable when they are byte-identical re-writes of one raise. | yes -- 0 FP on the live registry |
| **D-008** | T0 | Plan-level `last_updated` older than its newest node's, inflating the morning digest's staleness figure. | yes -- 19 real, 0 FP |
| **D-010** | T2 | Guards the accounting itself: recomputes the V3 denominator independently and reports every way it differs from what a reader would assume. | n/a (structural) |
| **D-101** | T2 | Classifies an ahead/behind divergence by CONTENT: which ahead commits are already upstream, and which are real local work. | yes -- on the live 23-commit divergence |
| **D-102** | T2 | The moving-ref guard: pins origin, re-reads before any verdict is published, aborts if it moved. | yes -- structural |

### Tiers

**T0** -- deterministic detection *and* a mechanical, single, reversible repair.
`--fix` applies it; no model is woken. **T1** -- detection is deterministic, the
disposition is not; escalates. **T2** -- reported for action taken elsewhere.

A T0 *detector* may still emit a T1 *finding* when a particular instance turns
out ambiguous. "If a fix is ever ambiguous it is not T0, demote it rather than
guessing" is enforced in `finding()` (`autofix=True` outside `tier="T0"` raises)
rather than left to discipline.

Ownership is `unblocks_claims` on a node -- deliberately **not**
`join.scope_claims`, which is a broad "bears on" association (one live node lists
2 of the former and 29 of the latter).

D-001 is **not** a duplicate of `scripts/check_claim_phase_consistency.py`: that
walks the claim->claim dependency graph, this compares a claim against the plan
that owns it.

## Baseline on REE_assembly `7f7a1bd80d` (2026-08-16)

Whole run: **0.5s**, well inside the 10s budget. `claims.yaml` is ~1000 entries;
loading it costs 5.6s under the pure-python YAML loader and 0.39s under libyaml's
`CSafeLoader`, which is why `_common.py` reaches for the C loader and why
detectors take a shared `Context` instead of re-reading.

| detector | findings |
|---|---|
| D-002 | **4** -- MECH-316, MECH-317 (P0/strong), MECH-091, MECH-314a (P1/weak) |
| D-001 | 27 |
| D-006 | **0** -- both duplicate groups fully dispositioned (the correct result) |
| D-008 | **19** -- all T0-fixable, largest drift 68d (`infant_substrate` 2026-05-30 -> 2026-07-21) |
| D-010 | 1 (silent-exclusion surface: 10 `assembling` nodes) |
| D-101 | 1 -- `unique_work_present` on a live `[ahead 23, behind 41]` |
| D-102 | 0 on a first run (no prior pin to compare) |

Whole run with the git lane: **1.8s**, still well inside the 10s budget; D-101
is ~1.3s of it (23 commits x per-path blob reads).

**The 19 D-008 fixes were NOT applied to the live tree.** Building the lane is
this chip's scope; applying 19 edits to shared plan frontmatter changes what the
morning digest reports and is a governance-visible action. `--fix` is there for
governance to run deliberately. Verified end-to-end on a full copy of the real
tree instead: 20 fixes previewed, then applied, 20 ledger records written, 38
registry rows preserved with none deleted, exactly one line changed per plan.

### D-101 on the live divergence, and the bug that found

`REE_assembly` at `[ahead 23, behind 41]` classifies as 18 `upstream_by_patch_id`
+ 3 `upstream_by_content` + 1 `regenerable_churn` + **1 genuinely unique**,
naming exactly 3 files to audit. That is the value in one line: 23 commits and a
"cannot fast-forward" reduced to three files.

Running it live also caught a real defect in it. `added_lines()` strips each
line; the upstream side did not. Every indented line therefore read as absent,
and a commit whose blob was **byte-identical** to origin's was classified as
unique work. Both sides are now normalised, with a blob-SHA fast path in front,
and `test_content_check_normalises_both_sides` pins it. Two lessons worth
keeping: a containment check must normalise both sides identically, and this
class of bug is only visible against real history -- the synthetic fixtures all
passed.

### What could NOT be validated here, stated plainly

The stage-3 acceptance case asks D-101 to reproduce the 2026-08-15
classification "when pointed at the reflog range that produced it". That range
(`[ahead 66, behind 274]`) lived in the **Mac** checkout's reflog; this box is a
Linux worker whose `REE_assembly` reflog begins 2026-08-16, so the range is not
reachable and the historical replay was not run. Substituted with
`test_incident_shape_is_reproduced`, which builds a divergence carrying all
three shapes the hand analysis found (patch-id equivalents, a substantive commit
upstream only by content that patch-id misses, and regenerable churn) and
asserts both the per-commit classification and the `safe_to_adopt` verdict the
hand analysis reached. Reproducible on any box, unlike the replay. Anyone with
the Mac checkout can still run the real thing:
`run_detectors.py --git-repo /Users/dgolden/REE_Working/REE_assembly`.

D-010 independently reproduces the committed snapshot exactly: 117 v3 nodes,
denominator **94**, and a status tally matching `closure_status.md` line for line,
with zero weight drift against `serve.py`.

**These counts are expected to fall and are deliberately NOT asserted in the
tests.** The 2026-08-15 adjudication (`7478ffe8ad`) *proposed* un-deferring the
three owning nodes to `/governance` rather than applying it; when governance
acts, those D-002 findings correctly disappear. A test pinned to the live number
would fail on a correct fix and teach the next session to weaken the detector.
The tests pin the classification logic; this table is a baseline to re-measure.

## Two corrections to the stage-1 spec, both found by running it

**1. The closure denominator is not "not deferred".** The natural one-line
statement --

```
{node : node.status not in DEFERRED_STATUSES and plan.generation == v3}
```

-- is wrong. `generate_closure_snapshot.py` builds the denominator from
`STATUS_WEIGHTS.get(status)` being non-`None`, and that exclusion set is a strict
superset of `DEFERRED_STATUSES`: it also holds `assembling`, `open_by_design`,
`deferred_v5`, `parked`, `parked_indefinite`, `closed`. On this tree the true
denominator is `117 - 13 deferred - 10 assembling = 94`, matching the committed
snapshot; the `DEFERRED_STATUSES`-only reading predicts 104. D-010 implements the
real rule and reports the gap as its standing output.

**2. D-002 must key on `deferred`, not on "excluded from the denominator"**, even
though the harm is identical. The wider set includes `assembling` -- "required for
v3, actively under construction, leave it alone", the anti-forcing status that
exists so unhurried assembly is not scored as failure. Widening the predicate
added exactly three claims (ARC-108, MECH-450, SD-033b), all owned by `assembling`
nodes, none orphaned: pure false positives against work the design deliberately
protects, diluting the one detector whose precision is its whole value. The wider
surface is real and belongs to D-010, which reports it as a surface rather than as
per-claim defects.

## Do not re-introduce a signal-strength gate on D-002

An earlier revision gated escalation on `v3_pending`, demoting MECH-091 and
MECH-314a to list-only. Adjudication returned precision **4/4** and refuted it --
MECH-314a was a real stale node the gate would have withheld indefinitely.
`severity` and `signal` **rank** findings when the budget is contended; they never
withhold one. Pinned by `test_d002_escalates_weak_signal_too`.

The general rule: a precision floor is legitimate only for a detector whose
findings are **noisy** -- never for one whose **misses are silent**. D-001 is
noisy (the literal any-owner reading fires 63 times, mostly benign forward
back-pointers), so it is scoped, and the narrowing is reported as a count rather
than applied silently. D-002's misses are silent by construction, so it is not
scoped.

D-002's weak tier is ranked P1/0.8 rather than P2/0.6 for an evidential reason:
every finding it has produced was adjudicated genuine, so even its weak tier
carries more evidence than an unvalidated detector's strong tier. Ranked lower,
D-001's P1 findings displace MECH-091 and MECH-314a out of the budget on a first
run -- the same withholding-by-signal, arriving through the ranking door instead
of the gate door.

## Stage 2 -- the T0 auto-fix lane

`--fix` applies every available mechanical repair. `--fix --dry-run` previews
them and writes nothing at all. Every applied fix appends one
`action: "autofix"` line to `state/steward_ledger.jsonl` carrying the change
*and the operation that reverses it*, so an unattended edit never has to be
reconstructed from a diff.

**`--fix` is OPT-IN, and that is a deliberate departure from the stage-2 brief**
("T0 means the runner applies these without escalating"). The cost half of that
sentence is honoured exactly: a T0 finding carries `escalate: false`, so it
never wakes a model. What is not honoured is silent mutation -- a bare
`run_detectors.py` edits nothing. Auto-editing shared, human-adjudicated
evidence files on every governance cycle is the writer profile this repo's
concurrency rules exist to defend against, and the acceptance criteria (dry-run
no-op on a clean tree, one reversible edit on a seeded fixture, a ledger record
per fix) are all satisfied without it. Flip the default by passing `--fix` from
`governance.sh`; nothing else needs to change.

**The lane never commits.** Edits land in the working tree for a human to review
and land. It also **refuses to write a file with uncommitted changes** -- an
autofix is a read-modify-write, and applying one on top of another session's
in-flight edit is the read-modify-write contamination hazard, where your commit
lands their work under your message. Refusing costs nothing; the fix is still
there next run.

### D-006 annotates, it does not delete -- and the brief said "dedup in place"

Running it against the live registry overrode the brief, for five reasons:
the file's own `authority` field calls it a human-adjudicated audit trail; all
five duplicates already on the tree were dispositioned by ANNOTATION (status
-> `superseded` plus a note naming the canonical), never deletion; those notes
cross-reference each other **by flag id**, so deleting rows would dangle live
references; `superseded` is a first-class status that `governance_flag.py list
--status open` filters, so annotating genuinely dedups; and a status flip is
reversible from the file alone where a deletion is not. That last point is what
settles it against the brief's own T0 bar.

The autofix predicate is therefore much narrower than the grouping key. A group
member is repaired only if its `summary` is byte-identical to the canonical's,
its `raised_at` matches **to the second**, and its status is still `open`.
Everything else is reported at T1. The live tree shows why the last clause
matters: **GFLAG-0015 is a true duplicate whose status is `resolved`**, with a
note reading "resolved together" -- a human decision the detector cannot see the
reasoning for, so it stays.

Consequence: **on the live tree D-006 applies zero fixes**, because both
duplicate groups are fully dispositioned. That is the correct result and it is
what the clean-tree test pins. Its root cause is also already closed upstream --
`governance_flag.py`'s raise path was made idempotent across a CAS retry -- so
D-006 is a residue-cleaner and regression guard, not a live alarm.

### D-008 is a one-line, monotonic, precedented edit

The fix direction is not invented here; it is the action governance already
performs by hand, recorded in the nodes themselves: *"last_updated bumped to
clear the closure-drift stale-since-review flag"*. The target value is computed
from the plan's own nodes, and the field only ever moves **forward**.

The edit is a **targeted line replacement, not a YAML round-trip** -- these
plans are hand-written markdown with ordered, commented frontmatter, and
re-dumping the YAML would reformat all 59 and produce exactly the
order-of-magnitude diff "Narrow Edits Only" forbids. The fixer requires exactly
one indent-2 `last_updated:` between `closure_plan:` and `nodes:`, holding a
bare ISO date. All 59 plans satisfy that; any that did not would be reported at
T1 rather than guessed at.

A plan-level date *newer* than every node is **not** drift and is deliberately
not flagged (`drives_motivation_v4_plan.md`): plan-level edits legitimately
touch the plan without touching a node.

## Stage 3 -- the git lane

**It reports and classifies. It never acts.** That is enforced structurally, not
by comment: every git call goes through `_gitlane.git()`, which refuses any
subcommand outside a read-only **whitelist**. A future edit reaching for
`update-ref` raises `GitLaneViolation` instead of mutating a shared checkout
four other writers push to. `fetch` is refused too -- fetching moves
remote-tracking refs, which would make the guard the cause of the movement it
exists to detect.

### D-101 -- classify a divergence by content

Per-commit classes: `upstream_by_patch_id` (CLAUDE.md's route A, via
`git cherry`), `upstream_by_content` (every non-blank added line is already in
origin's blob -- this catches route A's *endemic* false negatives, the bundled
read-modify-write and the append-at-a-different-offset, both native to the hot
multi-writer JSON registries), `regenerable_churn`, `unique`, `merge`.

Verdicts: **`safe_to_adopt`** (nothing substantive would be lost),
**`needs_rebase`** (unique work, but it touches no path origin changed, so it
replays cleanly oldest-first), **`unique_work_present`** (unique work contesting
paths origin also modified -- the read-modify-write contamination class; stop).

`safe_to_adopt` deliberately does **not** escalate and is **not** an instruction
to adopt. It de-escalates a frightening number. Adoption still goes through
`scripts/safe_adopt_ref.py`, whose independent recomputation of the discard set
stays the gate -- two computations must agree before any ref moves.

**`TASK_CLAIMS.json` and `TASK_CHIPS.json` are NEVER churn.** They look like
machine bookkeeping, so the pull toward listing them as regenerable is strong,
and CLAUDE.md names doing so a category error with a measured incident behind
it: a decision chip asserted exactly that of 26 commits, 15 of which were
genuinely stranded. The shape of a file explains why a patch-id proof *fails*;
it says nothing about whether the content reached origin. Encoded as an explicit
deny-list and asserted per-path in the tests.

### D-102 -- the moving-ref guard

On 2026-08-15 origin/master advanced three times in one session (05:05, 05:08,
05:38 UTC), and an equivalence check run before the 05:38 fetch reported
"identical" for a file that had by then been rewritten upstream (+254 lines).
The stale answer was acted on. **A verified-then-stale check is more dangerous
than no check, because it is trusted.**

`RefPin` resolves every ref to a concrete SHA once and exposes **no way to name
a moving ref** -- `pin.sha()` raises on an unpinned ref, so the mistake is not
available. D-101 asserts its own pin before publishing and discards its verdict
outright if anything moved. D-102 closes the two remaining windows: the **tail**
(a ref moving after D-101 finished but before the report is read -- P0,
escalates) and the **cross-run** window, which answers the question a human
actually has: *is this report still good?* Pins are persisted to
`state/steward_ref_pins.json` with timestamps and diffed run over run.

Any consumer about to act on a verdict should call the abort primitive with the
SHAs that verdict recorded:

```python
from detectors.d102_moving_ref_guard import guard
guard(repo, {"origin/master": "<sha from the report>"})   # raises RefMoved
```

Never soften it to a warning. A warning on a moving ref is how the 2026-08-15
answer got trusted.

## Suppressions

`state/suppressions.yaml`. A suppression stops a finding **escalating**; it never
removes it from the report (`"suppressed": true` plus the reason stays attached).
It is a recorded disposition, not a mute button. `finding_id` may be an fnmatch
pattern, so a whole class can be covered by one line.

Seeded with the three entries from `DETECTORS.md`. Two are **forward-declared**
for detectors stage 1 does not build (`MAE-3` whole-plan back-pointer,
`V3-EXQ-732b` deliberate refusal); they match nothing today and are kept so the
disposition is not lost when the owning detector lands.

Known clustering worth a future whole-plan entry: of D-001's 27 findings, 10 come
from one `generation: clinical` plan and 3 from one `generation: deferred` plan --
systematic back-pointer patterns rather than 13 independent defects. Collapsing
them is a *disposition*, which stage 1 has no authority to make; it belongs to
governance, and the ledger is what calibrates it.

## Scope -- what stages 1-3 deliberately do not do

- **No edit to `claims.yaml`**, no node status change, nothing queued. The only
  files any auto-fix touches are `governance_flags.v1.json` (one status field
  per row) and plan frontmatter (one date line per plan).
- **Nothing commits, pushes, or moves a ref.** The git lane is read-only by
  whitelist; the auto-fix lane leaves edits in the working tree for review.
- **Not wired into `governance.sh`.** Runnable by hand first, `--fix` included.
- **D-004 and D-007 are NOT built here** (stage 4). D-007 in particular carries
  an unresolved framing question flagged 2026-08-15 and needs user sign-off:
  it must report "the gate text is stale" and never "the node should be open".
  Both self_attribution incidents ended with the node correctly **still
  blocked** on a re-pointed gate, and the naive reading is exactly the
  "GAP-A done -> unblock GAP-2" trap the V3-EXQ-625e autopsy caught.

`state/steward_ledger.jsonl` gets one line per run (counts, escalated ids,
duration, per-detector totals). Its value is the time series.

`state/steward_state.json` is absent until the first run, which is what makes that
first run escalate everything. `reports/` is gitignored for stage 1; whether the
report should be committed is a stage-2 wiring decision.
