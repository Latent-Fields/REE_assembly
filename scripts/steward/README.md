# Steward -- integrity detectors (stages 1-4)

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
/opt/local/bin/python3 -m pytest scripts/steward/ -q                # 170 tests
```

> **Design of record: `docs/`** (added 2026-08-17). The original `SKILL.md`
> (skill contract, tiers, ratchet, budgets), `DETECTORS.md` (the full
> 13-detector catalogue, build order and seed suppressions) and the 2026-08-15
> git-lane field notes lived only in an untracked directory on the Mac until
> then, which is why the stage-1 build had to reconstruct detector semantics
> from other evidence when it ran on a cloud worker. **This file is
> authoritative for what exists; `docs/` is authoritative for what was
> intended**, and `docs/README.md` maps the two against each other -- including
> the four unbuilt detectors, the one retired one, and four open items that have
> no other home.

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
| **D-007** | T1 | Stale gate reference: a node's `blocking_external` / `resume_condition` names a closure node that is now `done`. Reports that the gate TEXT is stale -- never that the node should open. | yes -- 3/3, independently re-adjudicated, small/one-plan sample |
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
| D-007 | **3** -- self_attribution GAP-1 (P1), GAP-2 (P2), GAP-6 (P2); all 3 hand-audited genuine |
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

## Stage 4 -- D-007, and the framing that is the whole detector

**D-007 is a DOCUMENTATION-ACCURACY detector, never an UNBLOCK-DETECTION one.**

> It reports "the gate text is stale."
> It is FORBIDDEN from concluding "the node should be open."

That distinction is not a caveat on the detector; it *is* the detector. A
cleared gate is not an unblocked node, and this repo has three recorded
instances to prove it -- every one ended with the node correctly staying
`blocked` on a **re-pointed** gate:

| when | what cleared | what actually happened |
|---|---|---|
| 2026-06-09 | `sleep_substrate:GAP-1` done; `goal_pipeline:GAP-1` done; MECH-269 satisfied 2026-05-17, **one day after the gate was written** | Insufficient anyway -- 543l / 598b / 614e show the candidate pool collapses at the z_world layer *upstream* of SP-CEM, so stratified sampling has nothing to stratify. Status stays blocked, gate re-pointed. |
| 2026-06-23 | `behavioral_diversity_isolation:GAP-A` done on the V3-EXQ-569i PASS | The 2026-06-20 V3-EXQ-625e autopsy showed the conversion is ENV-CONDITIONAL and does not propagate to a threat-engaged candidate pool. The node record names the naive reading by name: *"a naive 'GAP-A done -> unblock GAP-2' read is the same env-conditional trap the axis_b autopsy caught."* |
| 2026-07-29 | `sleep_substrate:GAP-1` and `goal_pipeline:GAP-1` both done | Node stayed blocked on a re-pointed third gate. |

A detector emitting "node should open" would have been **wrong all three times**,
and the cost is not noise: the self_attribution plan states that re-queuing on a
falsely-cleared gate re-derives the known `non_contributory` result and burns a
runner session.

### The framing is enforced structurally, not by comment

`assert_no_status_proposal()` runs over every finding before `run()` returns and
**raises** if one carries `tier != "T1"`, `autofix=True`, or any key from
`FORBIDDEN_KEYS` (`proposed_status`, `unblock`, `should_open`, `fix`, `patch`,
...) at any depth. The acceptance criterion asked for a contract test asserting
on the *schema* rather than on prose, and this is that assertion moved one step
earlier -- to the point of production, in the same spirit as `finding()`'s
autofix/tier guard. Prose in `detail` can and does say "NOT AN UNBLOCK SIGNAL";
what matters is that the **structure** offers a consumer no field to read a
transition out of.

`depends_on` is deliberately **not read**, even though it is the most
gate-shaped field on a node. It is the structured, map-rendered dependency edge,
and "every `depends_on` is done therefore the node should open" is exactly the
inference D-007 exists not to make. Reading it would import the trap through the
back door. `test_depends_on_is_never_read` pins it, with a positive control on
the identical fixture so the silence cannot be the fixture failing to reach the
detector.

### Severity is ranking only

**P2** some named gates cleared, others outstanding. **P1** *all* named gates
cleared -- the node's stated rationale is now entirely vacuous, so the
re-adjudication is overdue. Both tiers report stale text; **neither asserts a
status change**. As with D-002, severity ranks findings under a contended
escalation budget and never withholds one.

### The suppression key is (node, gate-set)

`finding_id` is `D-007:<node>@cleared=<...>;named=<...>`. A node adjudicated
"still blocked, gate re-pointed" must not re-fire every run, but **must** re-fire
when the gate set changes -- too sticky and a genuine new stale gate is
swallowed, too loose and every run re-escalates a settled adjudication. Encoding
both the named set and the cleared subset gets all three cases right: a settled
finding is stable, a re-pointed gate is new, and a *second* gate clearing is new
(that is the P2 -> P1 transition, which is precisely the news the tier ranks).
Only the cleared/outstanding **partition** is folded in, never a raw status, so a
gate moving `open` -> `in_progress` does not churn the key.

### A precision floor applies here -- and it does NOT contradict D-002

D-002's docstring says a precision floor is illegitimate for a detector whose
**misses are silent**. That is the correct rule and D-007 is the other side of
it: stale plans already surface in the morning digest staleness table, so a
D-007 miss is recoverable rather than invisible, and trading recall for
precision is legitimate. Below `PRECISION_FLOOR` (0.6) the detector goes
**list-only** -- `escalate=False`, so it stops waking a model while still
reporting every finding. Withholding a finding from the report would be the
failure D-002 refutes; withholding an *escalation* is the budget working.

`MEASURED_PRECISION` is evidence, not a target. **Re-measure and rewrite it**
when the detector changes; do not inherit it.

### The measurement, with its weaknesses stated

3 findings on the live tree at `origin/master` `8603a6d186`, all 3 hand-audited
genuine -- **3/3**. (Measured twice: once on a checkout 61 commits behind, then
re-run at the tip and found identical -- same nodes, same severities, same veto
counts.) Two of the three are corroborated by governance records written months
before this detector existed, which is what makes the number evidence rather
than self-assessment: the 2026-07-29 reconcile says of GAP-1 *"Two of the three
gates named below HAVE CLEARED"*, and `governance_2026_06_23` says of GAP-2's
gate that GAP-A *"has PARTIALLY fired ... is now status=done"*. The third
(GAP-6, a node created 2026-08-15) rests on this session's reading.

Against that: **n=3 is a small sample**, it was **not** an independent
adjudication chip the way D-002's 4/4 was, and all three sit in **one plan**
(`self_attribution`), so it says little about other plans' prose conventions.
Above the floor, not comfortably above it.

That all three are still live is itself the finding: the 2026-06-09 gate text
has been stale for over two months and no cycle removed it, because every cycle
correctly re-pointed the gate in a governance **note** and left the original
`blocking_external` list standing.

**Independently re-adjudicated 2026-08-18** by a separate session
(`chip-20260816-steward-d007-precision-adjudicate`), addressing the "not an
independent adjudication chip" weakness above. Method: read each node's pre-fix
`blocking_external` / `resume_condition` at `b289311feb^`, then independently
confirmed the *current* status of every gate node the parser resolves --
`sleep_substrate:GAP-1`, `goal_pipeline:GAP-1` and
`behavioral_diversity_isolation:GAP-A` all read `status: done` straight from
their own plan frontmatter -- cross-checked against the pre-existing
`governance_2026_06_09` / `governance_2026_06_23` notes (written months before
the detector existed, so they cannot be the detector reasoning circling back).
**Verdict unchanged: 3/3 genuine, zero false positives**, nothing added to
`suppressions.yaml`.

By the time of this re-adjudication all three had *already* been resolved --
gates re-pointed, both nodes staying `blocked` -- by a separate chip
(`chip-20260817-d007-selfattr-stale-gates`, REE_assembly `b289311feb` +
`b3e0391230`) that landed between the original measurement and this one. That
resolution is itself corroborating: a false positive would have had nothing to
re-point. **D-007 now reports 0 live findings on the current tree** (verified
via `run_detectors.py --json`), which is the expected post-fix state, not a
regression -- a future re-measurement on this tree should expect `n=0` here
until a new instance appears.

Broadening beyond `self_attribution` was **attempted, not skipped**: all 9
gate-bearing nodes currently in the live tree were enumerated and every one
names only outstanding (non-`done`) gates -- true negatives, no additional
stale text. `git log --grep` was also run across `evidence/planning/*.md` for
the same re-point pattern in other plans; the candidates it surfaced (e.g.
`commitment_closure:GAP-4`, `sleep_substrate:GAP-2`) name their gates via
V3-EXQ ids or free prose, not `plan_id:NODE` tokens, so none are additional
D-007-parseable historical instances. **No second-plan sample was found within
this session's search** -- the "all one plan" weakness is confirmed to still
hold, not merely left unexamined.

### The historical replay is the primary test, and it really is historical

`test_d007_stale_gate_reference.py` materialises `evidence/planning/` at
`43ba39ca9e^` (2026-06-09), `fb11650188` (2026-06-23) and `7e60b8a675`
(2026-07-29) into a tmpdir and runs the ordinary `load_context` path over the
real frontmatter -- real prose, not a paraphrase. Unlike the stage-3 git-lane
replay (which needed a range living only in the Mac's reflog), `REE_assembly`'s
history reaches back to 2026-02, so **these ran**. Results:

| revision | finding | severity |
|---|---|---|
| 2026-06-09 (pre) | `self_attribution:GAP-1` names `sleep_substrate:GAP-1` (done) | P1 |
| 2026-06-23 | `self_attribution:GAP-2` names `GAP-A` (done) + `GAP-B` (partial) | **P2** |
| 2026-07-29 | `self_attribution:GAP-1`, every named gate cleared | **P1** |

with **zero** findings proposing a status change at any revision. The P2/P1
split is the acceptance criterion, and it falls out of the data rather than
being asserted into it.

Those tests skip if the history is unreachable (a shallow clone). To stop that
degrading into a vacuous pass the same three incidents are **also** pinned as
synthetic fixtures that always run, carrying the real gate strings verbatim.

**One honest gap in the replay.** The 2026-06-09 incident is detected through
`GAP-1`, not through the `GAP-2` half the write-up leads with. GAP-2's gate that
day was `MECH-269 V_s monostrategy landing` -- a **claim** id, not a `plan:NODE`
reference, and D-007 resolves plan-node gates only. That is a deliberate miss
under the "prefer a miss over a false positive" rule, not an oversight; the
incident is still caught, because the joint re-adjudication's GAP-1 half names a
plan node and is machine-resolvable.

### Parsing prose conservatively

`blocking_external` is a declared gate list, so every `plan:NODE` token in it is
a gate. `resume_condition` is free text that names gates inline *and* cites
unrelated nodes as evidence, so a token there counts only in a clause that reads
as a gate and does not read as a citation -- and **the citation veto beats the
gate cue**. That ordering is load-bearing: GAP-2's real `resume_condition`
contains *"Empirical proof of insufficiency: sleep_substrate:GAP-2 records
'...'"* (citation `records`, gate cue `after`) and *"See the 2026-06-09
re-adjudication note + sleep_substrate:GAP-2 (identical gate)"* (citation `see`,
gate cue `gate`). Both are cross-references, and both would be false positives
if the gate cue won.

**Cues are tested against the clause with the matched tokens blanked out**, so a
reference cannot satisfy its own gate test. This was found by a test, not by
inspection: the corpus contains `global_workspace_jlens:GATE-B`, and any node id
containing a cue word would otherwise make every passing mention of it read as a
gate.

Skipped tokens are **counted**, never silently dropped -- `prose_tokens_vetoed`,
`non_plan_tokens_ignored` (the corpus really does write `generation:v4` and
`status:deferred`, which match the token shape), `dangling_gate_refs` (a real
plan naming a node that does not exist -- a different defect, belonging to the
closure-link checker) and `self_references_skipped`. A miss should be a number
someone can look at.

Known recall limit, stated rather than hidden: bare node ids (`GAP-B`) and
abbreviated prefixes (`arc_062:GAP-B`, where the plan's real id is
`arc_062_rule_apprehension`) are **not** resolved. Resolving them needs a guess
about which plan is meant, which is the false positive the conservatism rule
forbids.

### The volume prediction did not hold, and that is worth recording

D-007 was sequenced last on the expectation that it would be "the highest
escalation volume" detector in the set. It produced **3** findings against
D-001's 27 and D-008's 19, and runs in under 10ms. The conservatism is why: the
`plan:NODE`-only resolution and the citation veto keep it narrow. If a later
revision loosens either, expect that prediction to start being right -- and
re-measure the precision before it does.

### D-004 was NOT built, deliberately

`phantom_owner_exq` was **retired 2026-08-16**: both the one-time fix
(REE_assembly `4fa9f8199b`) and the recurrence rule (REE_Working `67ce615f`, the
morning-digest Step 7c DECLARED-not-owed exemption) have landed. Building it
here would give one defect class two separate suppression states -- the "partial
fix reads as complete" failure that let V3-EXQ-631 recur in the first place.

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

Seeded with the three entries from `docs/DETECTORS.md`. Two are **forward-declared**
for detectors stage 1 does not build (`MAE-3` whole-plan back-pointer,
`V3-EXQ-732b` deliberate refusal); they match nothing today and are kept so the
disposition is not lost when the owning detector lands.

Known clustering worth a future whole-plan entry: of D-001's 27 findings, 10 come
from one `generation: clinical` plan and 3 from one `generation: deferred` plan --
systematic back-pointer patterns rather than 13 independent defects. Collapsing
them is a *disposition*, which stage 1 has no authority to make; it belongs to
governance, and the ledger is what calibrates it.

## Scope -- what stages 1-4 deliberately do not do

- **No edit to `claims.yaml`**, no node status change, nothing queued. The only
  files any auto-fix touches are `governance_flags.v1.json` (one status field
  per row) and plan frontmatter (one date line per plan). D-007 in particular
  edits nothing at all and is permanently T1.
- **Nothing commits, pushes, or moves a ref.** The git lane is read-only by
  whitelist; the auto-fix lane leaves edits in the working tree for review.
- **`--fix` is still not wired.** The runner is wired into `governance.sh`
  (see "Wiring" below), but a bare run; the auto-fix lane stays opt-in.
- **D-007's framing question was resolved by user sign-off 2026-08-16** and is
  now built -- see "Stage 4" above. The sign-off is a CONSTRAINT, not a default
  to improve on: it reports "the gate text is stale" and never "the node should
  be open".
- **D-004 (`phantom_owner_exq`) is NOT built, and should not be.** Retired
  2026-08-16 -- both the one-time fix and the recurrence rule have landed, and
  duplicating it would give one defect class two suppression states.

`state/steward_ledger.jsonl` gets one line per run (counts, escalated ids,
duration, per-detector totals). Its value is the time series.

`state/steward_state.json` is absent until the first run, which is what makes that
first run escalate everything.

## Wiring (2026-08-16)

`scripts/governance.sh` **Step 3m**, a bare run, `|| true`, no
`--exit-nonzero-on-escalate` and no `--fix`.

**Placement is constrained by exactly one thing:** D-010 cross-checks its
recomputed V3 denominator against `evidence/planning/closure_status.md`, which
Step 3c-bis regenerates. Run earlier and it audits a stale snapshot and reports
the staleness as a defect. Nothing else it reads is written by this pipeline.

**No `--exit-nonzero-on-escalate`.** Turning a detector finding into a failed
governance regen would make detection expensive, inverting the design: the whole
argument for running this every cycle is that detection is free.

**No `--fix`, and as of 2026-08-18 that is a decision with a named alternative
rather than a deferral.** The T0 lane has real repairs queued against plan
frontmatter; applying them changes what the morning digest reports. That is a
governance-visible action for a session running `--fix` on purpose -- and there
is now such a session: the **daily sweep** below. Governance stays READ-ONLY.

Two reasons, and the second is the one that makes this structural rather than
stylistic:

1. **A regen side-effect is not a deliberate act.** The sentence above is
   satisfied by a purpose-built job whose entire reason for existing is to apply
   T0 repairs. It would be *falsified*, not satisfied, by bolting `--fix` onto a
   pipeline everyone runs for other reasons.
2. **Step 3m cannot fix without breaking its own placement.** Steward sits at
   Step 3m precisely because D-010 must audit `closure_status.md` AFTER Step
   3c-bis regenerates it. A `--fix` at 3m mutates plan frontmatter that 3c-bis
   has already read, so the snapshot 3c-bis just wrote is stale the moment the
   fix lands. Clearing that needs either a second regen or a re-order that
   breaks D-010's placement constraint. There is no ordering that gets both.

"Run `--fix` by hand when the morning digest complains" was also rejected: it
relies on someone remembering, and the digest currently fires ~9 times in 39
weekdays, so the noticing mechanism is itself unreliable.

`test_governance_wiring.test_no_fix_flag` pins the absence of the flag;
`test_steward_sweep.test_governance_does_not_call_the_sweep` pins that the
pipeline does not reach the sweep by another route either.

## The daily T0 sweep (2026-08-18)

`steward_sweep.py`, scheduled by `com.ree.steward.plist` (launchd,
`StartInterval` 86400), installed with `install_steward_sweep.sh`. **Mac / dev
machine only** -- not the hub, not the cloud workers, same exclusion as the git
commit guards, because those boxes run the phase3 writers against continuously
moving checkouts.

**Daily, not hourly**, because that is the arrival rate: D-008 accrues ~1-3
findings/week (the 20 fixed on 2026-08-16 had accumulated over roughly a
quarter; drift gaps 1-52 days, median ~5). Daily keeps drift under 24h. Hourly
is 24x the commits for no additional freshness.

**Four gates, in this order, and the order is the design.**

| gate | what it refuses |
|---|---|
| pin (D-102) | a detached HEAD or a branch with no resolvable name -- a writer with no pinnable ref refuses rather than writing ungated |
| preview -> guard -> apply | a ref that moved while the detectors ran |
| `check_plan_frontmatter.py --strict` | committing on top of frontmatter the live explorer cannot parse |
| `ree_commit.py` | the race-prone `git commit -- <pathspec>` idiom |

**Preview before guard before apply is the load-bearing ordering.** The preview
is a full `--fix --dry-run` run that writes nothing, and the ref guard fires
between it and the applying run -- so a moving ref aborts *before a single byte
is written*. The obvious cheaper orderings (apply, then guard) all end with "and
then revert someone's file", or with half-applied edits left dirtying a shared
checkout, which the next run's `_dirty_paths` guard then stalls on forever. The
cost is running the detectors twice, ~17s/day.

**It commits through `ree_commit.py`, never plain git.** The 2026-08-16 D-008
fix committed with plain git and drew the pre-push warning *"touches managed
path(s) ... but was not built by ree_commit.py (race-prone idiom)"*.
`evidence/planning/` is a multi-writer tree and `git commit -- <pathspec>`
commits the WORKING-TREE content at commit time while ignoring the index, so any
concurrent writer landing in that gap silently wins. The test proves this from
the **intent record** ree_commit writes, not from a source grep -- the same
artefact the pre-push hook checks.

**Always `--bot`, with no flag to turn it off.** `clinical_hours_guard.py` reads
a personal-identity commit as an assertion that the work was done off clinical
duty, and an unattended job must not make that assertion on the operator's
behalf. It is also what keeps the sweep working in-window: the guard's
`--push-check` exempts a push whose commits are *all* authored AND committed as
the bot. Note the corollary -- if the checkout is ahead with someone's non-bot
commits, the exemption is lost and an in-window push is held. That surfaces as
exit 1 with the commit already made locally, which is correct: a human lands it.

**Scope, and what it must not acquire.** T0 only, and only what `FIXABLE`
offers: D-006 (annotate) and D-008 (forward-only `last_updated` bump). It
commits exactly the paths those fixers report having written, plus
`state/steward_ledger.jsonl`. It does **not** regenerate the closure snapshot,
touch `claims.yaml`, change a node status, or queue anything. Those are
governance's, and a scheduled writer must not acquire them by being convenient.

**One `action: "autofix"`, `source: "steward_sweep"` ledger record per run**,
including runs that fix nothing -- otherwise a job that silently stopped working
looks identical to a quiet week. The record lands *in* the commit it describes,
so it cannot carry the resulting sha; it carries `base` instead, and the commit
is that base's child.

**The ledger append never stays dirty, even when the commit itself fails
(2026-08-29, fleet-wedge campaign W6/C2).** Confirmed live: a sweep's ledger
append sat as a raw uncommitted diff on this shared checkout for hours after
its `ree_commit.py` call failed, blocking every OTHER session's push-retry
against `REE_assembly` until a human hand-landed it (`07ec0b16b0`). The T0
EDITS a failed commit leaves in place stay untouched on purpose (they are
correct; a human should land them, not have them silently undone), but the
ledger append has no such reason to linger. On a commit failure `sweep()`
checks whether HEAD actually advanced: if a local commit landed anyway (the
push was rejected and unretryable), the append is already safely inside it
and nothing is touched; if nothing landed at all, the WHOLE ledger file is
rolled back to its content from before this run started (not just this
module's own summary line -- `run_detectors.py`'s apply pass writes its own
"run" and per-fix "autofix" lines to the same file first) and this module's
own summary is stashed to the gitignored, per-machine
`state/steward_ledger_pending.jsonl`. The next run's `flush_pending()` retries
landing that summary, before that run's own gates, using the identical
committed-locally-or-revert-and-requeue logic -- so a run that still cannot
push leaves no new dirty diff either, and the record survives untouched for
the run after that.

**Known stall mode, stated rather than discovered later.** The frontmatter gate
is repo-wide: a pre-existing broken plan unrelated to the fixes will abort the
sweep every day until it is repaired. That is deliberate -- an unattended writer
should not add commits to a tree whose plan frontmatter the live explorer
already cannot parse -- and it is visible, because the abort logs the checker's
output and writes `aborted: "frontmatter_invalid"` to the ledger.

Exit codes: `0` clean, `1` needs a human, `3` refused by a gate.
Log: `~/Library/Logs/ree_steward_sweep.launchd.log`.
Tests: `test_steward_sweep.py` (31, real git repos, time-independent), roughly
half negative controls -- every gate is a refusal, so a bug in one is silent.

**The `escalate` boolean is printed twice** -- once at Step 3m, and again from
`governance.sh`'s exit trap, so it is the last thing on the screen even when the
regen aborts at a later blocking gate (Step 4b, Step 9c) and even though several
hundred lines of regen output follow the step itself. A gate nobody reads is not
a gate.

### The `ref_moved` abort rate, and the launchd I/O-throttle fix (2026-08-20)

**The measurement, and it is one data point, stated honestly.** By the time the
plist was installed on DLAPTOP (2026-08-20T07:36Z, chip
`chip-20260818-install-steward-sweep-launchd`), exactly one `RunAtLoad` firing
had happened: `07:11:22Z`, `duration_s: 234.473`, `aborted: "ref_moved"` (master
`d7792c59fe55` -> `a0b022a1dedf`; `origin/master` `6a7cd5a7b610` ->
`3cb0cdfbc5d1`). To prove the write path anyway, that same session ran the sweep
once more directly (foreground, not a second launchd firing): `07:19:06Z`,
`duration_s: 82.439`, `committed: true`, 3 T0 repairs applied, landed as
`55f1945eb0`. Both records are in `state/steward_ledger.jsonl`, `source:
"steward_sweep"` -- as of this write-up they are still the only two entries that
source has ever produced, so "the ratio" is 1 abort out of 1 real launchd run,
not a multi-day trend. **That is a real gap against this file's own "MEASURE
FIRST... a single first-run abort is not a trend" standard**, and the honest
resolution is that the fix below rests on the *mechanism*, not the frequency:
the 234.473s vs 82.439s gap (2.9x on the ledger's own `duration_s`, and reported
informally as 234s vs "29s" for the foreground *analysis* phase alone, 8x) was
measured **same-day, same repo state, same detector findings**, isolating the
one thing that differed -- the plist's `ProcessType`/`Nice`/`LowPriorityIO`
combination -- rather than inferring it from noisy day-to-day variance. A gate
correctly refusing on its first live trigger is not proof the gate is
mis-scheduled; the direct A/B timing comparison is what makes it a mechanism
finding rather than a coincidence.

**The fix (`com.ree.steward.plist`): drop `ProcessType Background` and
`LowPriorityIO`, keep `Nice` (lowered 10 -> 5).** `LowPriorityIO` sets
`IOPOL_THROTTLE` explicitly and `ProcessType Background` sets an equivalent
policy implicitly; together they stretch every `git` call the sweep's
pin/preview/guard/apply/commit sequence makes. `Nice` alone is CPU-only
deprioritization and does not touch I/O scheduling, so it is kept (at a lighter
value) for the reason the original comment gave -- this box runs many
concurrent Claude sessions and has taken a jetsam event before -- without
widening the D-102 pin-to-commit window the abort exists to bound.
`StartInterval` (86400, daily) is **unchanged** -- the 2026-08-17 daily decision
is not being revisited here, and `test_plist_parses_and_is_a_daily_agent`
still pins it. `StartCalendarInterval` (a fixed quiet hour) was considered and
**not** used: `origin/master` is written continuously by the phase3 writers and
the cloud fleet (see "Coordinator" in the umbrella CLAUDE.md), so there is no
reliably quiet hour to relocate the schedule to -- shortening the exposure
window is the lever that actually helps, moving it is not.

**Do NOT read this as evidence the gate is too strict, and do not weaken it.**
The gate wrote nothing both times it could have mattered, which is exactly its
job; the fix only removes an artificial 2.9-8x inflation of the window it has
to survive, so a ref move that would have raced it anyway still aborts it.

**Not verifiable from this session, and why.** This measurement and the plist
edit were done on `ree-cloud-5` (chip `chip-20260820-steward-sweep-launchd-refmoved-rate`,
headless) -- `launchctl` does not exist on Linux, so neither the live agent's
loaded state nor the effect of this change could be checked from here, and per
this file's own "Install" line the plist is cached by launchd: editing the
version-controlled copy alone changes nothing until
`install_steward_sweep.sh` is re-run **on DLAPTOP**. That is a required,
undone follow-up, not an optional one -- until it happens, the Mac keeps
running the un-fixed cached plist. The next session on DLAPTOP (interactive,
or the next `/session-land`-style pass that reads `WORKSPACE_STATE.md`) should
re-run the installer and then watch `state/steward_ledger.jsonl` for
`source: "steward_sweep"` records over the following several days to confirm
the fix actually holds beyond this single measured case.

### The report and the ratchet state stay gitignored -- and the two reasons differ

`reports/steward_report.json` and `state/steward_state.json` were left
gitignored, along with `state/steward_ref_pins.json` (which was neither tracked
nor ignored -- a leak, since a governance regen would have left it `??` for a
human to sweep into a landing commit).

**The report: churn with no reader.** ~85KB rewritten in full on every run,
carrying `generated_at`, `duration_s`, and `repo_root` -- an **absolute
machine-local path**, so the file differs between every box by construction. Its
only consumer is `governance.sh`, which wrote it moments earlier. `ref_pins` is
worse: it is *keyed* by that absolute path, so a shared copy would compare this
box's refs against another box's checkout.

**The ratchet state: silent suppression, which is not the same failure at all.**
Committing it would make the ratchet fleet-wide, so a finding escalates once
across all boxes instead of once per box. That sounds strictly better and is not,
because the state's semantic effect is **suppression**: any run anywhere advances
it, including a hand-run test -- which this README explicitly invites ("runnable
by hand"). A throwaway hand-run whose banner nobody read would consume a
finding's one fleet-wide escalation, permanently and silently. The asymmetry
decides it: a per-machine ratchet **over**-escalates at worst -- bounded (one
extra per box), visible, and recoverable -- where a shared one fails by
**withholding**, which is precisely the failure mode `d002`'s "a precision floor
is illegitimate for a detector whose misses are silent" rules out everywhere
else in this module. Concurrent whole-file rewrites of a shared JSON registry
(CLAUDE.md "Read-modify-write contamination") are a second, independent reason,
but the suppression argument is the load-bearing one.

**`state/steward_ledger.jsonl` stays tracked, and that is not inconsistent.** It
is an append-only audit time series -- it merges, it suppresses nothing, and its
whole value is being fleet-wide and durable. The distinction being drawn is
append-only audit (commit it) vs suppression-bearing whole-file rewrite (do not).

**What this costs, stated plainly:** governance cannot read the findings without
running the detectors. That is a real loss for a remote reader, and it is cheap
to reverse if it ever bites -- the fix is a derived, machine-independent
*summary* artifact (findings only, no `repo_root`, no timings), not committing
this report.
