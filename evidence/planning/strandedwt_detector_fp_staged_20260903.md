# Stranded-worktree detector: false-positive fix, STAGED (not shipped)

Status: **STAGED -- awaiting user decision.** No change has been made to
`scripts/hygiene_routine_tick.py`.
Author: `chip-20260903-hygiene-backlog-campaign` (session `cool-sutherland-9d984d`), 2026-09-03.
Subject: `_stranded_worktree_findings` / `_registry_rows_subsumed` / `METAWORKER_SCRATCH_FILES`.

## 1. What was measured

All 9 open `chip-strandedwt-*` chips were re-verified on their real hosts over explicit ssh
(ree-cloud-5 x8, ree-cloud-4 x1). The campaign brief's premise -- "all of these are false
positives in substance" -- is **WRONG**. Measured breakdown:

| worktree | box | sole kept path | verdict |
|---|---|---|---|
| exp-0520 / 0522 / 0524 / 0526 | c5 | `?? .launch.sh` | FALSE POSITIVE (scaffolding) |
| exp-0824 | c5 | ` M TASK_CLAIMS.json` | FALSE POSITIVE (registry residue, origin ahead) |
| mech320-vt-floor-diagnostic | c5 | ` M TASK_CLAIMS.json` | FALSE POSITIVE (same) |
| exp-0457 | c5 | ` M TASK_CHIPS.json` | **TRUE POSITIVE -- lost closure** |
| exp-0841-paced | c5 | ` M TASK_CHIPS.json` | **TRUE POSITIVE -- lost closure** |
| mech320-dv-headroom-and-vt-floor | c4 | ` M TASK_CHIPS.json` | **TRUE POSITIVE -- lost closure** |

The three true positives each held a `status=done` + substantive `resolution_note` that existed
ONLY on that worktree's disk; all three chips were still `open` on origin and therefore
redispatchable. Their underlying work HAD landed (REE_assembly `8885f00de6`, `c2e1c48781`,
`02441352b8`, all verified ancestors of origin/master) -- what was lost was the ledger closure.
All three have been recovered by re-issuing `chip_ledger.py resolve` through the coordinator,
with provenance recorded in the note.

**So the detector is not simply noisy: at a 1-in-3 hit rate it is doing real work, and any
narrowing must be justified against that.**

## 2. Root causes of the six false positives

**(a) `.launch.sh` missing from `METAWORKER_SCRATCH_FILES`** -- 4 chips.
278-byte dispatcher launcher: `#!/bin/bash -l` / `cd <worktree>` /
`exec claude -p --session-id <uuid> --permission-mode auto < DISPATCH_BRIEF.md`.
Written by the OUT-OF-REPO launcher on the dispatching box -- no writer exists anywhere in this
repo (`grep -rl 'launch\.sh' scripts .claude/skills` finds only `mcp_server_launch.sh`). It
embeds the same session uuid as `.session_uuid`, whose exemption comment already describes this
exact provenance and this exact defect ("Naming a Step is what kept `.session_uuid` off this set
until 2026-08-18"). Zero durable content in all four instances, byte-inspected.

**(b) `_registry_rows_subsumed`'s `hollow_note` clause vs the chip archive** -- the dominant
noise source, firing on 156-502 rows per worktree.
The clause treats "local row has a `resolution_note`, live row has none" as the amend-hollow-ack
loss shape. But `chip_ledger.py archive` (daily, 04:30 launchd `com.ree.chiparchive`) MOVES
`prompt`/`resolution_note`/`prompt_history` into `chip_archive/<YYYY-MM>.json` and records
`archived: {file, month, fields, at}` on the row. The predicate reads `l.get("resolution_note")`
raw -- **precisely the bug CLAUDE.md already documents**: *"Read archived fields through
`chip_ledger.archived_field(chip, field)`, never `chip.get(field)`. A raw `.get()` reads an
archived chip as 'never had one' -- silently, and precisely for the OLDEST resolved chips."*
`_registry_rows_subsumed` was never updated alongside the other three call sites.
Corroborating timing: the archive last ran 2026-09-03T03:30:16Z; the first of these chips
appeared 2026-09-03T04:22:55Z.

**(c) `_registry_rows_subsumed`'s `row_only_local` clause vs the hub's 24h retention** --
the dominant noise source for `TASK_CLAIMS.json` (88-186 rows per worktree).
The hub materializer drops `done` claims older than 24h from the rendered file. A worktree
snapshot older than that window therefore *necessarily* contains rows the live copy lacks, and
"a row only this worktree has -> NOT subsumed" fires on every one. Structural, not incidental.

## 3. Proposed minimal fix (three parts, independently landable)

1. Add `".launch.sh"` to `METAWORKER_SCRATCH_FILES`.
2. In `_registry_rows_subsumed`, treat a live row as having a note when its `archived` metadata
   lists that field -- i.e. route the read through `chip_ledger.archived_field()`.
3. In `_registry_rows_subsumed`, exempt a local-only row that is terminal (`done`/`withdrawn`)
   AND whose terminal timestamp predates the retention horizon (24h): aged out, not lost.

## 4. GOV-HELDOUT-1 check -- OUTCOME: PASSED for (2); (1) and (3) reported honestly as narrower

Method: re-ran the CURRENT and PROPOSED predicates side by side, on the actual surviving
worktrees, against the actual live render. Non-degeneracy guard applied -- only cases where the
two give DIFFERENT answers are counted.

**Held-out cases (resolved BEFORE this campaign, by other sessions, verdict independent of this
wording). `chip-strandedwt-...-abc2aefce4a2` was EXCLUDED as degenerate -- it is cited in
`_registry_rows_subsumed`'s own docstring, so the current wording was written from it.**

| # | case | CURRENT | PROPOSED | independent prior verdict | agrees? |
|---|---|---|---|---|---|
| 1 | `exp-0545` / TASK_CHIPS.json | RAISE (hollow_note=502) | SUPPRESS | "Verified false positive... zero refs unique to the worktree. No true loss." | YES |
| 2 | `igw-manual-assignment-staleness` / TASK_CHIPS.json | RAISE (hollow_note=502) | SUPPRESS | "registry mods are pre-cutover client-side drift, not rescuable content" | YES |
| 3 | `gflag0078-sd069-stepcap` / TASK_CHIPS.json (cloud-4) | RAISE (hollow_note=371) | SUPPRESS | "already-superseded by the live materialized file... no loss" | YES |

Three non-degenerate held-out cases, three agreements. **Fix (2) passes.**

**Negative controls -- the fix must NOT blind the detector:**

| control | CURRENT | PROPOSED | required |
|---|---|---|---|
| `exp-0457` / TASK_CHIPS.json (real lost closure), vs pre-remedy render | RAISE (`live_less_terminal`=1, hollow_note=156) | **RAISE (`live_less_terminal`=1)** | still raise -- PASS |
| `exp-0841-paced` / TASK_CHIPS.json (real lost closure), same | RAISE (same shape) | **RAISE (`live_less_terminal`=1)** | still raise -- PASS |
| `igw-manual-assignment-staleness` WORKTREE overall (`check_staleness.py`, `staleness_dump.json` half-written, no git object) | RAISE | **RAISE** -- non-registry paths untouched by all three parts | still raise -- PASS |
| `chip-strandedwt-dlaptop-...-3a3e4718aa68` (` M CLAUDE.md [no git object]`) | RAISE | RAISE (degenerate; fix touches no non-registry path) | still raise -- PASS |

The first two controls are the important ones: the true positives are caught by
`live_less_terminal`, a clause **none of the three parts touches**. The fix strips 156 rows of
`hollow_note` noise off each of those reports, making the single real row the only line left --
it makes a true positive MORE legible, not less.

`chip-20260807-thoughtdigestion-trial-5` (the confirmed permanently-unrecoverable loss) is the
standing negative control for the **GC `--force` rule**, a different mechanism from this
predicate; it is not a case this wording can give an answer on either way. Phase A of this
campaign followed that rule unchanged (`rm -f` known scratch, then a PLAIN `worktree remove`).

**Where the check did NOT pass, stated rather than papered over:**

- **Fix (1) `.launch.sh` has ZERO held-out cases.** Across all 81 other `chip-strandedwt-*`
  ledger rows, not one names `.launch.sh`. Per CLAUDE.md that is itself the finding: the rule is
  scoped to its motivating incident (four worktrees from one dispatch cycle) and should be
  shipped as such, not as a general principle. It does meet `METAWORKER_SCRATCH_FILES`' own
  standard -- "ADD A NAME ONLY ON MEASUREMENT, never on resemblance" -- with four byte-inspected
  instances and a traced writer.
- **Fix (3) flips NO verdict on its own.** Measured: it cuts `row_only_local` from 150->7,
  186->9, 107->10, 99->1, 88->1, but every one of those worktrees still RAISES, because each
  retains at least one **non-terminal** local-only row. Fix (3) buys legibility, not suppression.

## 5. Residual after all three parts -- THE ACTUAL DECISION

The two registry-residue false positives in this campaign (`exp-0824`,
`mech320-vt-floor-diagnostic`) **still raise** under the full proposed fix, each on exactly one
row: `('orchestrate-20260901-curate-r3', '2026-09-01T19:27:14Z')`, status `active` in the
snapshot, absent from the live render.

That row was independently confirmed CLOSED (its own
`chip-staleclaim-orchestrate-20260901-curate-r3-20260901T192714Z`, resolved `done`, cites
`--from-commit 244573a3`) -- but **the detector cannot know that from the two files alone**, and
a non-terminal local-only row is exactly what a genuinely lost claim looks like. Suppressing it
would mean asserting "an `active` claim that vanished from the render was closed, not lost",
which is the dangerous direction: false "not stranded" is silent data loss, false "stranded" is
noise.

**Recommendation: ship (1)+(2)+(3), accept that ~2 residual registry chips per cycle remain, and
do NOT add a rule about non-terminal local-only rows.** Expected effect on the measured backlog:
6 of 9 chips suppressed at source (4 by (1), 2 partially by (2)+(3)... see caveat above), the 3
true positives preserved and made more legible.

## 6. What the narrowed detector would NO LONGER catch

Stated explicitly, as required:

- **(1)** A durable artifact a worker deliberately named `.launch.sh`. Nothing writes that name
  except the dispatcher's launcher, but the exemption is by exact basename, so a human or worker
  choosing that filename for real content would be silenced. Same accepted residual risk as
  every other name in `METAWORKER_SCRATCH_FILES`.
- **(2)** A genuine hollow-ack (local note, no live note) **on a chip whose live row has already
  been archived** -- i.e. resolved >=14 days ago. The amend-hollow-ack incident this clause
  defends against is a same-day shape, so the overlap is small but not zero.
- **(3)** A `done`/`withdrawn` claim that was genuinely lost AND is more than 24h old. The
  clause cannot distinguish "aged out of the render" from "never reached the coordinator" for a
  terminal row past the retention horizon. Note the loss is bounded: the row is terminal, so
  what would be lost is a `completion_note`, not in-flight work.

## 7. Relationship to the two open decision chips

- `chip-20260903-cloud5-no-puller-for-work-repos`: **does not bear on this.**
  `_registry_rows_subsumed` compares against the UMBRELLA main checkout, and ree-cloud-5's
  umbrella checkout was measured current this cycle (HEAD == origin/master, 0 behind,
  TASK_CLAIMS 159/159 and TASK_CHIPS 2944/2944 rows vs origin). That chip's blast radius is the
  work repos only.
- `chip-20260903-untracked-manifest-collision-recurring-class`: a different mechanism (untracked
  evidence manifests colliding with the phase3 writer). Shares only the ancestor cause -- the
  Phase-3 split between what a worker writes locally and what the hub renders -- which is also
  the ancestor of the registry-residue class here. Worth deciding together for that reason.
