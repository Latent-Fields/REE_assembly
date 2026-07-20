# E3 fresh-select instrument — shared-helper migration (plan of record)

**Opened:** 2026-07-20T12:37Z (session `peaceful-morse-5cf712`)
**Status:** IN PROGRESS — 1 of 3 call sites migrated
**Substrate:** `ree-v3` `experiments/_lib/fresh_select.py` (landed `acd48f9`, 2026-07-20)

## Why this doc exists

The remaining work is **invisible to every automated check in the repo**. It was carried by a
`spawn_task` chip, which dies with its session. This doc is the durable record so a governance or
autopsy session picks it up. See §4 for the structural fix that would make this doc unnecessary.

## 1. What landed

`ree-v3` `acd48f9` (on `origin/main`, ff from `67ad105`) extracted the E3 sentinel-key freshness
instrument into a shared helper:

| Artifact | Path |
|---|---|
| Helper | `experiments/_lib/fresh_select.py` — `FreshSelectProbe` / `FreshSelectCounter` (292 lines) |
| Contract | `tests/contracts/test_fresh_select_wholesale_reassign.py` (379 lines) |
| Lint change | discharge **(e)** in both E3 lints in `validate_experiments.py` |
| First consumer | `experiments/v3_exq_699c_pcomp_demotion_x_gonogo_fixed_n.py` — **migrated**, both exemption markers removed |

Suite at land: 1915 passed / 2 skipped / 39 subtests. Both E3 corpus fire pins **unchanged** — the
lint discharge is inert until a script imports the helper.

## 2. Outstanding — the two remaining call sites

Both still carry their own inlined copy of the instrument **and** a blanket lint exemption. Both
are still `status: pending` in `ree-v3/experiment_queue.json` as of 2026-07-20T12:32Z, which is
why they were not migrated at land time: editing a queued script changes what is about to run.

| Script | Namespace | Queue id | Blocking condition |
|---|---|---|---|
| `experiments/v3_exq_699b_pcomp_demotion_x_gonogo_fresh_select.py` | `exq699b` | V3-EXQ-699b (priority 28) | still `pending` |
| `experiments/v3_exq_689i_mech448_f_eligibility_demotion_falsifier_repair.py` | `exq689i` | V3-EXQ-689i (priority 30) | still `pending` |

Exemption markers present on `origin/main` in both (`E3_DIAGNOSTICS_STALENESS_EXEMPT`,
`E3_HOLD_WEIGHTED_READOUT_EXEMPT`, both bound to a local `_FRESH_SELECT_EXEMPT_REASON`).

**Unblocking condition:** each script leaves `pending` — i.e. it has run. Migrate per-script as
each frees; do not wait for both. Expect this to take days: both sit behind 7 pending items and
the fleet was committed ~147h on V3-EXQ-742a at the time of writing.

## 3. How to do the migration

Use the landed **699c** as the reference implementation.

**Preserve each driver's scientific semantics exactly — they differ from 699c and from each other:**

- **689i** gates accumulation on `is_p1`; 699b and 699c gate on `is_p2`.
- **689i** flushes holds at episode **END**; 699b/699c flush at episode **start**.

Keep each driver's own placement of `fs.flush()`. Do not normalise them to a common shape.

After migrating, remove that script's two exemption markers and confirm
`validate_experiments.py --paths <script>` reports `OK` (not `exempt`).

Route script edits through `/queue-experiment` per CLAUDE.md.

### Two traps that already bit this work

- **Never write either marker's literal name in a migrated script, not even in a comment.** Both
  lints test for the marker with a plain **substring search over the source**, so merely naming one
  silently restores the blanket exemption and undoes the narrowing.
- **The failure asymmetry is not what it looks like.** An in-place `.clear()` + `.update()` refactor
  of `last_score_diagnostics` deletes the sentinel too and reads as **FRESH** — the *silent*
  direction. Only writing keys individually reads as latched. The contract pins **both** directions;
  do not "simplify" it to merely check that the dict was refreshed.

### Testing note

The 6 `tests/contracts/test_arm_reuse.py::test_index_writer_*` ERRORs are **pre-existing and
location-dependent** — the test resolves `REE_assembly` as a sibling of the ree-v3 checkout, so
they fire from any worktree outside `REE_Working`. Confirm against `origin/main` before
investigating; they are not a regression.

## 4. Why nothing surfaces this automatically (the structural fix)

`validate_experiments.py` reports `1 OK, 0 exempt` for both scripts today. The exemptions are
**inert-but-present**: the lint only counts a script `exempt` when it *would* have fired and was
suppressed, and these scripts do not fire it. So the outstanding migration is invisible to
validation.

Three sibling lints in the same file **do** carry backlog counters —
`arm-fingerprint-backlog`, `degeneracy-self-report-backlog`, `manifest-writer-backlog` — which
exist for exactly this purpose: making known-outstanding migrations visible on every run. The two
E3 lints have exemption markers but **no backlog counter**.

**Recommended follow-up (not done here):** add an `e3-exemption-backlog` counter to the two E3
lints, mirroring the three existing ones. That would make this doc redundant — every
`validate_experiments.py` run would report the outstanding count until the last marker is gone,
and no future session would depend on finding a planning doc. Not done in this session because it
is a code change with contract implications for the two corpus fire pins, and the session was
closing.

## 5. Status table

| Call site | State | Evidence |
|---|---|---|
| 699c | **MIGRATED** | ree-v3 `acd48f9` |
| 699b | **PENDING** — blocked, still queued | markers on `origin/main` |
| 689i | **PENDING** — blocked, still queued | markers on `origin/main` |
| `e3-exemption-backlog` lint counter | **NOT BUILT** — see §4 | — |

Close this doc when §5 has no PENDING rows.
