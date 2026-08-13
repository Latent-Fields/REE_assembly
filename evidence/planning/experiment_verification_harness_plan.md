---
closure_plan:
  id: experiment_verification_harness
  generation: process
  title: "Experiment Verification Harness -- Plan of Record (insights follow-on, gaps 1-3)"
  registered: 2026-08-03
  last_updated: 2026-08-03
  owner: machinery
  summary: >
    Close 3 scoped gaps in the incident-driven lint ratchet (a new
    experiment script can dodge the whole 19-lint corpus; no consolidated
    index across the 19 lints; the JSON whole-file-reformat bug class has
    no mechanical check), corrected against an `/insights` report that
    had wrongly framed this as "build a verification harness from
    scratch." generation: process -- infra/tooling lane, not V3 substrate
    science; owns no scientific claims, so it is segmented out of the V3
    closure % and rendered on the shared `process` tab.
  scope_claims: []
  sibling_plans: [substrate_stability_and_drift_detection]
  nodes:
    - id: "experiment_verification_harness:GAP-1"
      title: "Block 1c in precommit_contracts.sh -- run the 19 test_*_lint.py subset for new experiment scripts that would otherwise dodge Block 2"
      phase: 1
      status: done
      severity: high
      owner_exq: null
      last_updated: 2026-08-03
      completion_note: "Landed ree-v3 a249c708b2 (main). 8 new tests added (test_precommit_contracts_experiment_lint_scope.py), red/green-checked (5/8 genuinely failed against the pre-fix script); existing test_precommit_contracts_gate_scope.py + test_precommit_contracts_routing.py (24 tests) re-run clean, no regression. Full ~13min contract suite not run for this change since it touches neither ree_core/ nor experiments/_lib/."
    - id: "experiment_verification_harness:GAP-2"
      title: "tests/contracts/LINT_INDEX.md -- one row per test_*_lint.py file (bug class, motivating incident, hard vs warn-only)"
      phase: 2
      status: done
      severity: medium
      owner_exq: null
      last_updated: 2026-08-03
      completion_note: "Landed ree-v3 74011a8981 (main). Enumerates all 19 lints individually; also corrected a stale '47 lint files' count (from an unfiltered find that double-counted .pyc cache variants and nested .claude/worktrees/ copies) to the real, filtered count of 19 -- now the authoritative count going forward, per this doc's own correction note."
    - id: "experiment_verification_harness:GAP-3"
      title: "scripts/check_json_edit_locality.py -- WARN on whole-file JSON reformats of CLAUDE.md 'exposed files' vs narrow structural appends"
      phase: 3
      status: done
      severity: high
      owner_exq: null
      last_updated: 2026-08-03
      completion_note: "Landed REE_Working 8cc401e (master). 12 new tests, red/green-checked; caught a real bug via a production-scale smoke test against this repo's own 1735-line TASK_CLAIMS.json (--repo . resolved against the script's own location's parent instead of the caller's cwd, so a worktree invocation silently checked the wrong repo's staged set -- fixed, pinned by test_repo_dot_resolves_against_cwd_not_script_location). Standalone tool only -- not wired into any PreToolUse hook (a separate decision, affects every commit fleet-wide)."
---

# Experiment Verification Harness — Plan of Record

**Status:** all 3 gaps landed. **Owner:** interactive sessions (no dedicated chip yet).
**Repos touched:** `ree-v3` (lint corpus, precommit gate), `REE_assembly` (this doc),
`REE_Working` (a new generic JSON-locality check, umbrella repo).

## Origin

Surfaced via `/insights` (2026-08-03) as "Verification Harness Against Self-Introduced
Bugs" — the report's framing was that this needed to be built from scratch. It doesn't.
This doc corrects that and scopes the actual gap.

## What already exists (do not re-build this)

`ree-v3/tests/contracts/` carries **19 `test_*_lint.py` files** as of 2026-08-03 (see
correction note below), each added reactively after one specific confirmed incident —
`test_dacc_last_bundle_lint`,
`test_dead_z_goal_stream_lint`, `test_hardcoded_dry_run_lint`, `test_inert_arm_knob_lint`,
`test_spearman_guard_shape_lint`, `test_precondition_recomputability_lint`, and more.
`validate_experiments.py --checks <name>` and `validate_queue.py` add another layer of
semantic checks (`prereg_share_feasibility_lint`, the mean-vs-quantifier check, the
magnitude-vs-range check), each documented in `.claude/skills/queue-experiment/SKILL.md`
with the incident that motivated it (V3-EXQ-779b, V3-EXQ-643, V3-EXQ-785, ...).

Cross-checked against 59 real `fix(...)` commits in `ree-v3` since 2026-06-15: nearly
every recurring bug class in that history (wrong-attribute reads, tick-0-vs-multi-tick,
degenerate zero-initialized contracts, measurement-window contamination, worktree-blind
path resolution) already has a named lint, or was the proximate cause of one. This is a
mature, incident-driven ratchet — "encode each historical failure mode as an executable
check" is already the standing practice, not a proposal.

## The actual gaps (this plan is scoped to these three, not a rewrite)

### Gap 1 — new experiment scripts can dodge the whole corpus (HIGHEST PRIORITY)

`ree-v3/scripts/precommit_contracts.sh` Block 2 (the block that runs all 19 lints, via
the shared `tests/contracts/conftest.py::corpus_scan` fixture) only fires when staged
paths match `^(ree_core/|experiments/_lib/)`. A brand-new `experiments/v3_exq_NNN.py` —
the single most common artifact `/queue-experiment` produces — touches neither, so it
gets only Block 1 (`validate_experiments.py --strict`, narrow: conformance + arm
fingerprint) and Block 1b (manifest-writer lint only). It can introduce a fresh instance
of an already-known bad pattern (a new `dead_z_goal_stream`-shaped bug, a new degenerate
contract) undetected until some unrelated later commit happens to touch `_lib/` and a
corpus-count pin breaks somewhere else, misattributed to whatever is staged then.

This is the same root cause as two incidents CLAUDE.md already documents for Block 2's
own trigger scope: the `mech457_retention_trajectory_probe` build (`_lib/` untriggered,
ree-v3 `7e4f6e932b`) and the `coordinator/`-not-collected pytest-default-args incident.
Same shape, third instance, still open — for experiment scripts specifically.

**Fix:** add **Block 1c** to `precommit_contracts.sh`: when any `experiments/*.py`
outside `_lib/` is staged AND Block 2 will *not* already run (i.e. no `ree_core/` or
`_lib/` path is also staged in the same commit — running the full suite already covers
the lints, so Block 1c would be redundant there), run just the `tests/contracts/test_*_lint.py`
subset. This is materially cheaper than the full ~13min suite (dominated by the shared
corpus-scan fixture, ~100s) because it excludes the slow non-lint contracts
(`test_sd081_dualsystem_arbitration`, `test_graceful_timeout_lockfile`, the full non-lint
suite). Runs locally, unconditionally — no OOM-routing logic needed at this size.

### Gap 2 — no consolidated index across the 19 lints

A session authoring a new experiment class has no single place to check "what's already
covered, so I don't need to hand-verify it myself." Add `tests/contracts/LINT_INDEX.md`:
one row per `test_*_lint.py` file — bug class, the incident that motivated it, hard vs.
warn-only. Doubles as an autopsy-session checklist ("does a lint already exist for this
before recommending a new one").

### Gap 3 — the JSON whole-file-reformat class has no mechanical check

The one bug class from the `/insights` report genuinely *not* covered anywhere: an edit
to a shared coordination JSON (`claims.yaml`, `experiment_queue.json`,
`evidence/planning/*.json`, `TASK_CLAIMS.json`) that reformats the whole file instead of
appending narrowly. CLAUDE.md's read-modify-write contamination section already argues
for this at length ("prefer a narrow structural append... diff structurally, not
textually") but the mitigation today is pure discipline, no gate.

**Fix:** `scripts/check_json_edit_locality.py` (umbrella repo) — for staged JSON files on
the CLAUDE.md "exposed files" list, structurally diff old vs. new (added/removed/changed
top-level keys or array items) and WARN (not block — false positives are plausible for
legitimate bulk edits, e.g. a governance regen) when line-churn is wildly disproportionate
to the structural delta. Points at the CLAUDE.md guidance in its own message.

## Status table

| Gap | Fix | Status | Landed at |
|---|---|---|---|
| GAP-1 | Block 1c in `precommit_contracts.sh` + `test_precommit_contracts_experiment_lint_scope.py` | **done** | ree-v3 `a249c708b2` (main) |
| GAP-2 | `tests/contracts/LINT_INDEX.md` | **done** | ree-v3 `74011a8981` (main) |
| GAP-3 | `scripts/check_json_edit_locality.py` | **done** | REE_Working `8cc401e` (master) |

Gap 3 verification: 12 new tests, red/green-checked. Also caught a real bug
via a production-scale smoke test (not just synthetic fixtures) against this
repo's own live 1735-line `TASK_CLAIMS.json`: `--repo .` resolved against the
SCRIPT's own location's parent (always a directory -> always "found") rather
than the caller's cwd, so a worktree invocation silently checked the wrong
repo's staged set. Fixed (CWD-relative resolution tried first), pinned by
`test_repo_dot_resolves_against_cwd_not_script_location`, and re-verified at
production scale (silent on a real narrow append, warns on a real whole-file
reformat of the live file, both staged-then-reverted, never committed).
Standalone tool only -- **not wired into any PreToolUse hook.** That would
affect every commit across every session/worktree/machine in the fleet and
is a separate decision from building the check itself.

Gap 1 verification: 8 new tests added, red/green-checked (5 of 8 genuinely fail
against the pre-fix script, restored and re-verified green); existing
`test_precommit_contracts_gate_scope.py` + `test_precommit_contracts_routing.py`
(24 tests) re-run clean, no regression. Full ~13min contract suite not run for
this change since it touches neither `ree_core/` nor `experiments/_lib/` (would
not trigger Block 2 itself either).

**Correction (2026-08-04):** the original draft of this doc, and the
WORKSPACE_STATE.md entry recording Gap 1's landing, both said "47 lint files."
That count was wrong — it came from an unfiltered `find ... -iname "*lint*"`
that also counted `.pyc` cache variants (2-3 per source file) and nested
`.claude/worktrees/` copies. The real count, filtered to canonical
`tests/contracts/test_*_lint.py` source files only, is **19**. Corrected
throughout this doc while building `LINT_INDEX.md` (Gap 2), which enumerates
all 19 individually and is the authoritative count going forward. Not
retroactively edited in WORKSPACE_STATE.md (append-only history log) — this
note is the correction of record.

## Explicitly out of scope

- Re-deriving the 19 existing lints or their taxonomy from a "clean-slate forensic pass"
  — they already exist and are each individually incident-documented in
  `queue-experiment/SKILL.md` and their own file headers.
- A generic cross-language static-analysis framework. Each gap above is a narrow, scoped
  fix to an existing, working piece of infrastructure.
