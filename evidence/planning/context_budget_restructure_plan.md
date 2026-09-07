# Context-budget restructure: plan of record

**Opened:** 2026-09-07T17:55:42Z
**Status:** COMPLETE (2026-09-07). WI-1 landed ree-v3 `main` 89907e3; WI-2 landed umbrella `master` + ree-v3 `main` `a3cd923b8f` (chip `chip-20260907-umbrella-claudemd-wi2-skill-scoping`). Both outcomes recorded below, including WI-2's GOV-HELDOUT-1 result and its negative-control findings.
**Evidence base:** [`token_split_measurement_20260907.md`](token_split_measurement_20260907.md)
(REE_assembly `b36526f715`). Every figure below comes from that measurement; nothing here
is re-derived or estimated independently.

**Goal:** recover ~14% of the fleet's billed input-token budget, losslessly, by
re-granularizing instructional context behind loading mechanisms that already exist.

**Non-goal:** adopting a tool-output compression layer. That was measured and declined --
addressable surface 20.6% of budget, realistic saving 4-6%, and it puts a lossy layer
between the model and the byte-exact reads the concurrency doctrine depends on.

---

## 1. The finding this rests on

Post-fix corpus: 295 sessions, 38,828 assistant turns, 11.47 B billed input tokens.
Fit quality R^2 median 0.9954, per-turn residual median 0.9%.

**~59% of every token billed is instructional context before any work product exists.**

The single worst offender:

| file | size | approx tokens |
|---|---|---|
| **`ree-v3/CLAUDE.md`** | **1,472,082 chars** | **~368,000** |
| `CLAUDE.md` (umbrella) | 154,611 chars | ~38,650 |

`ree-v3/CLAUDE.md` is 214 top-level sections of **per-feature substrate records**
(SD-082, SD-063, ARC-110, MECH-463, ...), 139 distinct feature IDs, median section
~5,900 chars. It is injected whole as a `nested_memory` attachment whenever a session
touches `ree-v3/`.

**The decisive measurement -- how much of it a loading session actually uses:**

> Across the 25 post-fix sessions that loaded it, the **median session referenced 2 of
> the 139 feature IDs (1.4%)**. Mean 3.3, max 20. **Nine of 25 referenced zero.**

Those sessions cost a median **30.6 M** billed input tokens against **17.3 M** for
sessions that do not load it -- 1.8x -- and harness injections are **51.30%** of their
budget.

---

## 2. Why the fix is NOT a new loader

Two lazy-loading mechanisms already exist and already work:

1. **Skills already do progressive disclosure.** The 29 `SKILL.md` files total
   ~1,088,000 chars (~272,000 tokens) of body, but the *measured* fixed baseline is
   ~92,000 tokens in total. Bodies demonstrably do not load up front -- only descriptions.
2. **Nested `CLAUDE.md` is already directory-triggered.** Only 25 of 295 sessions ever
   loaded `ree-v3/CLAUDE.md`. The trigger is working as designed.

**The defect is the granularity of what sits behind those triggers, not the triggers.**
Building a per-skill context loader would add a mechanism to solve a problem that is
actually a content-layout problem.

The umbrella `CLAUDE.md` already contains the proven template: the **`A-01`..`A-94`
skill-archaeology pattern** -- a one-line pointer carrying a token cost and a
"not needed to follow the rule, read it before changing it" note, with the content in a
separate file read on demand.

---

## 3. Why the key is FEATURE, not SKILL

The original framing was per-skill context. The measurement does not support it as the
primary key:

| sessions | count | share of budget |
|---|---|---|
| invoke **no** skill | 173 (58.6%) | 21.0% |
| invoke **exactly 1** skill | 68 (23.1%) | 29.0% |
| invoke **2+** skills | 54 (18.3%) | **50.1%** |

Only 23% are single-skill. `session-land` alone appears in 87 sessions -- it is the
near-universal closing skill, which is why `<work skill> + session-land` is both the
commonest shape and half the budget. **Keying context on skill identity would miss most
of the spend.**

And the umbrella file is mostly not skill-specific:

| section | share of file | scopable to a skill? |
|---|---|---|
| Concurrency Rules | 23.3% | **no** -- every session that writes |
| Session Startup Protocol | 15.5% | **no** |
| Session Land Protocol | 14.4% | **no** -- 87 sessions run it |
| Worktree / Chipped Sessions | 6.0% | **no** |
| General Rules + Git Policy | 5.0% | **no** |
| test suite, scripts corpus, coordinator, experiments, governance, misc | **~29%** | **yes** |

~64% is genuinely universal. So skill-scoping is a real but *secondary* lever, and
`ree-v3/CLAUDE.md` -- keyed on feature ID -- is the primary one.

---

## 4. Work items

### WI-1 (primary): `ree-v3/CLAUDE.md` -> thin index + per-feature files

Split the 214 sections into `ree-v3/docs/substrate/<FEATURE-ID>.md`, leaving an index of
headings plus whatever preamble is genuinely universal to ree-v3 work.

- 214 headings as an index is ~17 KB (~4,300 tok) against ~368,000 tok today.
- Pointer form: copy the umbrella's archaeology annotation exactly -- feature ID, one-line
  summary, approximate token cost, and when to read it.
- **Byte-exactness is a hard requirement.** Extracted section content must be
  byte-identical to what it replaced; verify mechanically (concatenate the extracted files
  in original order and diff against the original file) rather than by inspection.

**Expected saving: ~9.2% of total fleet budget; ~46% for the 25 sessions that load it.**

**OUTCOME (landed 2026-09-07, ree-v3 `main` 89907e3; 5 commits, `integration/reev3-claudemd-split`
merged and deleted).**

| | before | after |
|---|---|---|
| `ree-v3/CLAUDE.md` | 1,478,781 bytes (~369,695 tok) | 65,719 bytes (~16,429 tok) |

-95.56%. 200 per-feature records extracted to `ree-v3/docs/substrate/` across 117 feature IDs;
14 non-per-feature sections kept inline (26,199 chars).

**Classification test actually applied:** extract iff the section is a *per-feature substrate
record*; general conventions, operational references, architecture-invariant lists and scope
doctrine stay inline. Feature-keying, not size, decides. 172 of the 200 keyed automatically off
a leading `SD-`/`MECH-`/`ARC-`/`INV-`/`Q-`/`DR-` token or a named substrate slug; 28 were
assigned an ID by hand where the heading names the feature descriptively.

**Two borderline calls, recorded so they can be revisited rather than reconstructed:**
- `Q-020 Decision` is feature-KEYED but is a 366-char architecture invariant reading as a
  continuation of `Key Architecture Constraints` -- a pointer would cost more than the content.
  Kept inline.
- `V3 / V4 Scope Boundary` (7.5 KB), `Remote Control` (6.0 KB), `Troubleshooting Runner`
  (4.6 KB) and `Regression Suite` (3.6 KB) are large but not per-feature, so WI-1 correctly
  left them. They ARE skill-scopable, so they are carried into WI-2's scope (~21 KB of the
  file's remaining 66 KB).

**Byte-exactness, verified mechanically** by recomposing the pre-split file from the 200
committed `docs/substrate/*.md` blobs plus the 14 inline sections, in original document order,
and diffing against `d5566f4:CLAUDE.md`:

```
original (d5566f4:CLAUDE.md) : 1,478,619 chars  sha256 c79c441fcb9e267a5218f30d99ff6e90f8b2ac3ca65dab5ef1f29f5c9fe39813
recomposed from HEAD blobs   : 1,478,619 chars  sha256 c79c441fcb9e267a5218f30d99ff6e90f8b2ac3ca65dab5ef1f29f5c9fe39813
RESULT: PASS -- byte-identical, 0 bytes differ
```

Link audit: 200 index links / 200 unique / 200 files on disk / 0 broken / 0 orphaned.

**Deviation from this plan's size estimate, stated rather than quietly absorbed.** The
"~17 KB (~4,300 tok)" figure in this section assumed a heading-only index. It did not budget for
the retained universal preamble (26 KB) that this same section instructs be kept, nor for the
per-entry links and token annotations that section 5.1 requires. The landed index is 66 KB.
Cutting summaries to reach 17 KB would have bought ~1% more of the fleet budget while
degrading exactly the signal section 5.1 identifies as the live risk, so it was not done.

**On section 5.1 (a pointer must carry enough signal to know when to follow it).** The
"when to read it" predicate is uniform across substrate records, so it is stated ONCE and
prominently at the head of the file rather than repeated 200 times. Seven entries whose
predicate is WIDER than that default -- standing lints, standing defaults and roll-up ledgers
that bind a session not working on the feature at all (`INV-091`,
`CEILING-ANCHOR-FLOOR-GUARD`, `DV-HEADROOM`, `GATE-DV`, `Q-081`, `SD-DECISIONS-IMPLEMENTED`,
`SD-DECISIONS-VALIDATED`) -- carry an explicit per-entry override telling the reader to follow
them on sight. That override set is the mitigation; the uniform default is orientation.

**Negative control (section 6) checked and NOT triggered:** 200 of 214 sections are per-feature
substrate records against a measured median usage of 2 of 139 feature IDs. Nothing found on
reading contradicted the measurement.

### WI-2 (secondary): umbrella `CLAUDE.md` -> move skill-specific sections into SKILL.md

Candidates, with their share of the umbrella file:

| section | share | destination |
|---|---|---|
| Running the test suite (cloud routing) | 9.0% | `implement-substrate`, `queue-experiment` |
| Running the umbrella `scripts/` test corpus | 3.6% | (sessions editing `scripts/`) |
| Coordinator (Phase 3) | 4.3% | `metaworker-*`, fleet work |
| Multi-Machine Experiment Coordination | 3.1% | `queue-experiment` |
| Experiment Scripts + Runner + EXQ Versioning | 4.4% | `queue-experiment`, `diagnose-errors` |
| Governance Pipeline + Experiment Review Tracking + V3-Pending Gate | 1.3% | `governance` |
| Dev Doctor, Explorer, MCP server, Recommendation ledger, Literature Pulls | ~3.5% | respective skills |

**Expected saving: ~29% of the umbrella file ~= 4.8% of total budget.**

**OUTCOME (landed 2026-09-07; 11 commits -- umbrella `REE_Working` master, `ree-v3` main
`a3cd923b8f`).**

| | before | after | |
|---|---|---|---|
| `CLAUDE.md` (umbrella) | 154,645 chars (~38,661 tok) | 133,024 chars (~33,256 tok) | **-14.0%** |
| `ree-v3/CLAUDE.md` (carried-over sections) | 65,405 chars (~16,351 tok) | 60,910 chars (~15,227 tok) | **-6.9%** |

**-14.0% against this section's ~29% estimate, and the gap is the finding, not a shortfall.**
The estimate was a share-of-file sum over the candidate table. Applying the classification test
below, roughly a third of that candidate mass turned out to be rules rather than reference and
stayed inline -- correctly, per section 5.1's own risk.

**Classification test actually applied** (fixed in slice 1, then applied unchanged): a line
stays in `CLAUDE.md` **iff a session could VIOLATE it without ever reading further** -- i.e. it
is a prohibition or a standing default, not mechanism or evidence. Mechanism goes behind a
pointer; it goes into a `SKILL.md` **body** only where the work is *already gated to that skill*,
so a session that needs the rule has necessarily invoked it.

**This is deliberately weaker than WI-1's mitigation and was designed for that.** WI-1 moved
content behind an index in the same file, so the pointer always loads. A `SKILL.md` body loads
only on invocation, and **173 of 295 sessions (58.6%) invoke no skill at all** -- so a rule moved
into a body is *invisible* to the majority, not merely deferred. Hence: only ONE section moved
into a skill body outright; everything else moved into `docs/reference/` files that keep a
one-line pointer in `CLAUDE.md` (what it covers, token cost, owner, when to read it) AND are
pointed at from the owning `SKILL.md`. One copy, two entry points.

**What moved** (5 new reference files + 2 skill-body moves):

| from | to | kept inline |
|---|---|---|
| Running the test suite | `docs/reference/ree-v3-test-suite-routing.md` | don't run pytest on the Mac; "full suite" is six paths; a worker-green suite is not a gate for an exact-committed-action test |
| `scripts/` test corpus | `docs/reference/scripts-test-corpus.md` | the invocation; run it before landing under `scripts/`; keep it local; the three vacuity rules, restated compactly |
| Coordinator (Phase 3) | `docs/reference/coordinator-phase3.md` | which live sources to read for fleet progress; three prohibitions (hub heartbeat writer, hub runner retired, `_HEARTBEAT_WRITE`) |
| Multi-Machine Coordination | `docs/reference/multi-machine-coordination.md` | `machine_affinity`; do not lower `COORDINATOR_STALE_HOURS` |
| Experiment Scripts (minting default only) | `queue-experiment` SKILL.md **body** | the whole mandatory-skill-path rule; a one-line statement of the default |
| `ree-v3` Remote Control | `ree-v3/docs/reference/remote-control.md` | default-off/bit-identical; the six command kinds; why `start` is not among them |
| `ree-v3` Troubleshooting Runner | `diagnose-errors` SKILL.md **body** | runner log location; never re-queue under the same EXQ ID |

**Negative-control findings -- candidates the plan named that are NOT skill-scopable.** The
section's own negative control ("if MOST candidates fail, WI-2 is wrong as scoped") did NOT
fire: by character mass most candidates did move. These did not:

- **Experiment Scripts, "Mandatory skill path"** -- the clearest case. It is the rule that makes
  a session invoke `/queue-experiment` at all; inside that skill it would be circular and reach
  nobody. Only the minting default moved.
- **Recommendation-Agreement Ledger** -- fires after *any* `AskUserQuestion` marked
  `(Recommended)`, in any session, skill or not.
- **Experiment Review Tracking** -- "do NOT infer discussed status from the filesystem" is a
  prohibition against a plausible wrong inference, reachable by `view-experiments`,
  `morning-digest` and no-skill sessions, not only `/governance`.
- **Governance Pipeline** -- "update all of `claims.yaml` + docs + indexes in a single pass"
  binds thought-intake, `/claim-synthesis` and `/failure-autopsy`, not only `/governance`.
- **Dev Doctor, Explorer, MCP server, V3-Pending Gate, Literature Pulls, EXQ Versioning,
  Experiment Runner** -- all session-startup affordances, standing prohibitions, or too small
  for a pointer to pay for itself. Left inline; the ~3.5% "misc" row of the table is mostly
  unrecoverable for this reason.
- **`ree-v3` V3/V4 Scope Boundary (~7.5 KB)** -- scope doctrine plus explicit do-not-implement
  gates; answers "is this in V3 scope?", which every kind of session asks.
- **`ree-v3` Regression Suite (~3.6 KB)** -- its "when to run what" list is the standing
  pre-commit default for every `ree-v3` code change.

**Byte-exactness, verified mechanically** (not by reading) for every moved block: a non-blank-line
**partition invariant** -- every non-blank line of the original section appears exactly once in
kept-union-moved, the two disjoint -- plus verbatim-containment of each moved block in its
destination, and a check that regions of `CLAUDE.md` outside the edited section are byte-identical
to the previous commit. Links inside moved prose are left repo-root-relative and unrewritten on
purpose, so the text stays byte-identical; each destination file's header says so.

**GOV-HELDOUT-1 check: RUN, 3 non-degenerate held-out cases, rule survived unchanged.** Compared
against the OLD wording (this section's candidate table: move the named section to the named
skill). Only cases where old and new give *different* answers are counted.

1. **2026-05-30 worker restart-loop** (`PHASE3_DISABLE_RUNNER_HEARTBEAT_WRITE`). OLD: the
   prohibition travels into `metaworker-*` with the Coordinator section, invisible to a no-skill
   fleet session. NEW: it stays inline. The incident is itself evidence this is a prohibition
   that gets violated. **Differ; NEW is right.**
2. **V3-EXQ-841 orphaned claim / `feedback_heartbeat_stale_not_abandoned`.** OLD: "do NOT lower
   `COORDINATOR_STALE_HOURS`" travels into `/queue-experiment`, which has nothing to do with
   editing `coordinator/db.py`. NEW: stays inline. The record shows this is the *tempting* wrong
   fix and its cost is a duplicate run. **Differ; NEW is right.**
3. **2026-03-23 six-experiment silent re-queue** (EXQ-075, 074b, 076, 084, 085, 047g). OLD: the
   whole Troubleshooting section, including "never re-queue under the same EXQ ID", moves to
   `/diagnose-errors`. But the sessions that caused the incident were *re-queueing*, not
   diagnosing -- they would never have loaded it. NEW: the diagnoses move, the rule stays.
   **Differ; NEW is right.**

Cases considered and REJECTED as degenerate (old and new agree, so they test nothing): A-93's
retired telemetry doctrine, the 2026-08-12 hand-rolled-close incident, the A-59 mis-homed chip,
the 2026-03-24 missing-`title` incident, and the 43-second woken-worker shutdown.

**Follow-on chipped, not done here** (content edits, not moves): `ree-v3`'s Regression Suite
duplicates the umbrella's full-suite figures with STALE numbers (~1800 tests / ~6 min against
the measured ~13m12s / ~3558); and the block moved into `queue-experiment` restates, and
forward-references, the paragraph now immediately above it.

**Do NOT move:** Concurrency Rules, Session Startup Protocol, Session Land Protocol,
Worktree / Chipped Sessions, General Rules, Git Policy, Timestamps, Python, ASCII-only,
Shell Portability, Hooks, High-Contention Files. A rule `session-land` needs is universal
by definition, and 59% of sessions invoke no skill at all.

### Combined

| lever | saving | risk |
|---|---|---|
| WI-1 | ~9.2% | none |
| WI-2 | ~4.8% | none |
| **both** | **~14%** | **none** |
| *(Headroom best case, for comparison)* | *11.7%* | *lossy, proxy, new failure surface* |
| *(Headroom realistic here)* | *4-6%* | *as above* |

The restructure beats the compression layer's best case and roughly triples its realistic
case, without a lossy layer.

---

## 5. Constraints and known failure modes

1. **The pointer must carry enough signal that the model knows when to follow it.** This
   is the live risk of the archaeology pattern: a rule that is now one line away can be
   *missed* rather than merely deferred. The umbrella's existing annotation form
   (`~N tok; not needed to follow the rule, read it before changing it`) is the mitigation
   and should be copied verbatim in shape.
2. **GOV-HELDOUT-1 applies.** WI-2 edits standing rules. Before landing, check the new
   layout against >=3 historical cases the wording was NOT written from, counting only
   cases where old and new give *different* answers. If 3 such cases cannot be found, say
   so explicitly rather than shipping the check as a rubber stamp.
3. **Byte-exactness on extraction** (WI-1) -- verify by mechanical recomposition, not by
   reading.
4. **`ree-v3` is the executable-code plane.** A change this size spanning sessions belongs
   on a short-lived `integration/<slug>` branch per Git Policy, deleted on merge. It
   touches no coordination data, so it must not be batched with any `evidence/**` or
   `experiment_queue.json` edit.
5. **Land incrementally.** WI-1 is naturally sliceable by feature ID; land verified slices
   rather than one 214-file commit.

---

## 6. Negative control

If a loading session had referenced a *large* share of `ree-v3/CLAUDE.md`'s feature
sections, WI-1 would be wrong -- the file would be earning its place and splitting it
would just add indirection. It does not: median 2 of 139, and 9 of 25 sessions referenced
none. If a future re-measure shows the median session referencing >30% of sections, revisit.
