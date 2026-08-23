---
title: "SD-QUEUE-SEED-ENFORCEMENT: validate_queue.seed_enforcement_lint"
parent: "Specs, Diagrams & Versions"
grandparent: Architecture
nav_order: 10
---

# SD-QUEUE-SEED-ENFORCEMENT: validate_queue.seed_enforcement_lint

**Claim ID:** SD-QUEUE-SEED-ENFORCEMENT
**Subject:** validate_queue.py / experiment_runner.py -- queue-declared seed count vs actually-executed seed count
**Status:** IMPLEMENTED
**Registered:** 2026-08-12
**Depends on:** (none unresolved)
**Blocks:** (none named -- infrastructure/instrumentation fix, not gating any claim)

## Problem

`experiment_queue.json`'s `"seeds": N` field is consumed ONLY by
`experiment_runner.py`'s `_run_axis_count`, for progress-bar and ETA
denominators. It is NEVER translated into a `--seeds` CLI argument passed to
the experiment script's subprocess. A driver's own `argparse` default is
therefore the sole source of truth for how many seeds actually run, and
nothing cross-checked the declared count against either an explicit
`--seeds` override in the queue item's `args` or the target script's own
argparse default.

This does not merely under-power a run -- it silently converts an
under-powered run into a scientific FAIL, which then enters governance as
evidence. Confirmed twice within two days, on different drivers
(`failure_autopsy_V3-EXQ-912-913-fishtank-cluster_2026-08-11.json`):

- **V3-EXQ-912**: queue declared `"seeds": 2`; the script's own `--seeds`
  argparse default was `[0]` (1 seed), so 1 seed ran.
  `n_segments_total=60` instead of the designed 120;
  `n_uncensored_deaths_total=4 < MIN_UNCENSORED_DEATHS_TOTAL=10`, which
  DROVE the FAIL.
- **V3-EXQ-920**: queue correctly declared `"seeds": 8`; only 1 of the
  pre-registered 8 seeds executed. Worse, the manifest's own self-routed
  label (`single_life_uncensored_survival_still_censoring_dominated`) was
  FLATLY WRONG -- `pct_right_censored_pooled=0.0`, literally zero censoring.
- Sibling **V3-EXQ-913** avoided the defect only because its author happened
  to set the script's own seed default correctly -- luck, not a property of
  the system.

Because this can corrupt adjudication of ANY multi-seed experiment (not just
the two that surfaced it), and because the queue is DB-authoritative
(materialised on the hub by `phase3_queue_writer` from the coordinator DB,
not by a Claude-issued `git commit`), a commit-time-only check would leave
daemon-materialised and cloud-worker-pulled entries unprotected.

## Solution

A single precise, statically-verified lint --
`validate_queue.seed_enforcement_lint(source, item, filename)` -- wired into
`validate()`'s existing per-item loop (same place `prereg_share_feasibility_lint`
and the `emit_outcome` disallowed-kwargs check already read the script
source). It fires as a blocking ERROR only when ALL of:

1. the queue item's declared `seeds` count `N > 1` (via a `_declared_seed_count`
   helper mirroring `experiment_runner._run_axis_count`'s int-or-list handling);
2. no explicit `--seeds` token is present in the item's `args` (parsed with
   `shlex.split` for the shell-string form, matching
   `experiment_runner.run_experiment`'s own args handling exactly, so the lint
   sees precisely what will reach the subprocess command line); and
3. the target script's own `--seeds` argparse `default=` is statically
   resolvable via `ast` (`_script_seeds_default_count`) to `M` seed values,
   with `M < N`.

Resolution handles: an inline literal list/tuple (`default=[42, 123]`), a
bare module-level name (`default=SEEDS`), and `list(SEEDS)`/`tuple(SEEDS)`
wrapping a module-level literal list/tuple (`_module_list_constants`, a
companion to the existing `_module_numeric_constants` helper used by the
pre-registration-feasibility lint). Anything else -- `default=None` (the
largest single pattern in the corpus, ~44 scripts), a `type=str` comma-string
contract, a computed expression, or no `--seeds` argument at all -- resolves
to `None` and the lint is silent. **Fail-soft by design: an unresolvable
default means "no mismatch can be asserted," never "assume a shortfall."**
Swept the resolver over the full 1351-script `experiments/` corpus with zero
crashes; it confidently resolves ~11% (152/1351) and defers on the rest.

**Why one check gives both enforcement points for free, without a second
implementation.** `validate()` is already called from two places:
`main()` (the `PreToolUse` commit-blocking hook) and
`experiment_runner.load_queue()` (every runner's startup, on every machine,
`sys.exit(1)` on any error). Embedding the check inside `validate()` means it
is simultaneously:

- **Loud at commit time** (option "(b)" in the originating task) -- cannot
  break a running experiment, and catches a human-authored queue edit before
  it lands.
- **Enforced at runner startup on every machine** (the blast-radius concern
  behind option "(a)") -- including cloud workers that `git pull origin main`
  and run directly, which never go through a Claude-issued `git commit` and
  so never see the commit hook at all. This closes the exact gap a
  commit-hook-only fix would have left open.

**Why NOT runner-side seed synthesis (the task's literal option "(a)").**
Surveying the `--seeds` argparse shape across the corpus found real
heterogeneity: `nargs="+", default=[...]` (a literal list of intentional
seed VALUES, e.g. `[42, 123, 456]`), `type=int, default=N_SEEDS` (a single
int COUNT, different CLI contract), and `type=str, default="42,123"` (a
comma-string contract). A runner that blindly synthesized `--seeds 0..N-1`
would (a) silently overwrite an author's deliberately-chosen seed values
with arbitrary ones even in the *already-correct* case, which risks breaking
arm-reuse fingerprint matching (seed identity matters for baseline reuse
per `arm_reuse_fingerprint_plan.md`), and (b) guess at seed values the
author never specified for the *shortfall* case, rather than recovering
their actual intent. A loud, precise refusal (via the shared `validate()`
enforcement point above) is strictly safer than a silent guess, and was
chosen instead.

**Backward compatible.** Fires only on the fully-conjunctive, statically
verified case; every ambiguous shape is silent. `test_no_false_positives`-
equivalent coverage: `test_resolver_never_crashes_across_experiments_corpus`
(pinned) plus a corpus sweep during implementation found zero spurious
findings against the current corpus (the live queue was empty of items at
implementation time, so no queue-entry-level corpus check was possible;
the per-script resolver sweep is the available proxy).

## Architecture Context

Sits alongside the other AST-based static lints already in `validate_queue.py`
(`prereg_share_feasibility_lint`, the `emit_outcome` disallowed-kwargs check,
the re-derive brake backstop) -- all fail-soft, precision-first checks that
read a driver script's source once and share the same `ast.parse` call site.
No `ree_core/` substrate changes; this is purely queue/runner instrumentation.

## What This SD Enables

- Prevents a silent seed-count shortfall from masquerading as a scientific
  FAIL or a mislabeled manifest, for any future multi-seed queue entry whose
  script has a statically-resolvable `--seeds` default.
- Protects the runner fleet-wide (Mac, hub, cloud workers) at startup, not
  only queue entries a human commits through Claude Code.

## Related Claims

None directly gated; this is an instrumentation/data-integrity fix protecting
the evidentiary validity of any multi-seed experiment's FAIL/PASS
classification. Source autopsy:
`evidence/planning/failure_autopsy_V3-EXQ-912-913-fishtank-cluster_2026-08-11.json`.
