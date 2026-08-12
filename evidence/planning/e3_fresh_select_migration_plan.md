---
closure_plan:
  id: e3_fresh_select_migration
  generation: process
  title: "E3 Fresh-Select Instrument -- Shared-Helper Migration"
  registered: 2026-07-20
  last_updated: 2026-08-10
  owner: machinery
  summary: >
    Migrate the three E3 sentinel-key freshness instrument call sites
    (699c/699b/689i) off inlined copies onto the shared
    experiments/_lib/fresh_select.py helper, and close the lint-visibility
    gap (no backlog counter existed for the two E3 lints' exemption
    markers) that made the outstanding migration invisible to automated
    checks. generation: process -- infra/tooling lane, not V3 substrate
    science; owns no scientific claims, so it is segmented out of the V3
    closure % and rendered on the shared `process` tab (sibling of
    pack_writer_single_writer_migration, the same "migrate call sites onto
    a shared helper, one lint backlog counter at a time" shape).
  scope_claims: []
  sibling_plans: [pack_writer_single_writer_migration]
  nodes:
    - id: "e3_fresh_select_migration:P0"
      title: "Extract E3 fresh-select instrument into shared helper + migrate first consumer (699c)"
      phase: 0
      status: done
      severity: high
      owner_exq: null
      last_updated: 2026-07-20
      completion_note: "ree-v3 acd48f9 (ff from 67ad105) extracted FreshSelectProbe/FreshSelectCounter into experiments/_lib/fresh_select.py + contract test_fresh_select_wholesale_reassign.py; first consumer v3_exq_699c_pcomp_demotion_x_gonogo_fixed_n.py migrated, both exemption markers removed. Suite at land: 1915 passed / 2 skipped / 39 subtests; both E3 corpus fire pins unchanged (discharge inert until a script imports the helper)."
    - id: "e3_fresh_select_migration:P1"
      title: "Migrate remaining call site V3-EXQ-699b onto the shared helper"
      phase: 1
      status: done
      severity: medium
      owner_exq: "V3-EXQ-699b"
      last_updated: 2026-08-10
      completion_note: "699b migrated off the shared helper, both exemption markers removed, validate_experiments.py reports OK (0 exempt). Two prior FAIL runs (non_contributory / substrate_not_ready_requeue, composition question levers_compound not reached) unaffected -- instrument-only migration."
    - id: "e3_fresh_select_migration:P2"
      title: "Migrate remaining call site V3-EXQ-689i onto the shared helper (preserve is_p1 gating + episode-END flush)"
      phase: 1
      status: done
      severity: medium
      owner_exq: "V3-EXQ-689i"
      last_updated: 2026-08-10
      completion_note: "689i migrated (ree-v3 1233b84e4b), own semantics preserved verbatim (is_p1 gating, episode-END flush -- differs from 699b/699c's is_p2 gating / episode-start flush). Prior run's failure_autopsy (confirmed, user-adjudicated 2026-07-24) recommends evidence_direction: supports for MECH-448, pending governance write-up -- not applied by this migration."
    - id: "e3_fresh_select_migration:P3"
      title: "Build e3-exemption-backlog lint counter (structural fix so this doc becomes unnecessary)"
      phase: 2
      status: done
      severity: medium
      owner_exq: null
      last_updated: 2026-08-10
      completion_note: "ree-v3 78f7543b80 added e3_exemption_backlog_lint to validate_experiments.py, wired into CHECK_NAMES/summary/the shared corpus scan; corpus fire-rate pinned at 10 (699b/689i confirmed clean, the ten firing carry a marker for unrelated reasons). Doc closed: every validate_experiments.py run now reports the outstanding exemption count directly, so no future session needs to find this planning doc."
---

# E3 fresh-select instrument — shared-helper migration (plan of record)

**Opened:** 2026-07-20T12:37Z (session `peaceful-morse-5cf712`)
**Status:** CLOSED — all 3 call sites migrated and the `e3-exemption-backlog` lint counter is built (§4/§5) (updated 2026-08-10)
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

Both still carry their own inlined copy of the instrument **and** a blanket lint exemption. As of
2026-08-09 both have **run** (see §5 for outcomes) and are no longer queue-blocked — neither is in
the live queue. Migration has not started for either (exemption markers still present, confirmed
below); they are simply unblocked and ready to pick up.

| Script | Namespace | Queue id | State (2026-08-09) |
|---|---|---|---|
| `experiments/v3_exq_699b_pcomp_demotion_x_gonogo_fresh_select.py` | `exq699b` | V3-EXQ-699b (priority 28) | RAN 2x (both FAIL) — MIGRATED 2026-08-10 |
| `experiments/v3_exq_689i_mech448_f_eligibility_demotion_falsifier_repair.py` | `exq689i` | V3-EXQ-689i (priority 30) | RAN — unblocked, not migrated |

Exemption markers still present on `origin/main` in both, reconfirmed 2026-08-09
(`E3_DIAGNOSTICS_STALENESS_EXEMPT`, `E3_HOLD_WEIGHTED_READOUT_EXEMPT`, both bound to a local
`_FRESH_SELECT_EXEMPT_REASON`; `validate_experiments.py --paths <script>` still reports `OK`, i.e.
`0 exempt`, for both — neither imports the shared helper yet).

**Unblocking condition — MET for both, 2026-08-09.** 699b ran twice
(`2026-07-24T12:35:50Z`, `2026-07-24T20:59:40Z`) and 689i ran once (`2026-07-22T16:28:50Z`);
neither is in the live queue. Migration may proceed for either script whenever a session picks it
up — see §5 for run outcomes and whether either result changes the migration's priority.

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

**Recommended follow-up (built 2026-08-10, ree-v3 `78f7543b80`):** added an `e3-exemption-backlog`
counter, mirroring the three existing ones — a new, separate lint rather than a change to the two
E3 lints themselves, so their own corpus fire pins are untouched. This doc is now redundant: every
`validate_experiments.py` run reports the outstanding count until the last marker is gone, and no
future session needs to find this planning doc.

## 5. Status table

| Call site | State | Evidence |
|---|---|---|
| 699c | **MIGRATED** | ree-v3 `acd48f9` |
| 699b | **MIGRATED** — off the shared helper (`experiments/_lib/fresh_select.py`), both exemption markers removed, `validate_experiments.py` reports OK (0 exempt); the two prior runs (both FAIL / `non_contributory` / `substrate_not_ready_requeue`, composition question `levers_compound` not reached) are unaffected by this instrument-only migration | runs `v3_exq_699b_..._20260724T123550Z_v3`, `v3_exq_699b_..._20260724T205940Z_v3` (both pre-migration); migration itself: ree-v3 (this session) |
| 689i | **MIGRATED** — off the shared helper (`experiments/_lib/fresh_select.py`), both exemption markers removed, `validate_experiments.py` reports OK (0 exempt); own semantics preserved verbatim (`is_p1` gating, episode-END flush per §3). The prior run (self-routed FAIL `substrate_not_ready_requeue`, but confirmed autopsy adjudicates "gate defect, science upheld" -- C_PRIMARY passed cleanly; recommended `evidence_direction: supports` for MECH-448, pending governance write-up, not applied here) is unaffected by this instrument-only migration | run `v3_exq_689i_..._20260722T162850Z_v3` (pre-migration); `failure_autopsy_V3-EXQ-689i_2026-07-24` (status: confirmed, user-adjudicated 2026-07-24); migration itself: ree-v3 `1233b84e4b` |
| `e3-exemption-backlog` lint counter | **BUILT** — `e3_exemption_backlog_lint` in `validate_experiments.py`, wired into `CHECK_NAMES`/summary/WARNINGS and the shared corpus scan; corpus fire-rate pinned at 10 (699b/689i confirmed clean; the ten firing carry a marker for reasons unrelated to this migration) | ree-v3 `78f7543b80` |

Closed: §5 has no un-migrated call-site rows and the lint counter row is resolved (see
`e3-exemption-backlog` row above, evidence `78f7543b80`).
