# R5: widening `_DIVERGENCE_REPOS` -- the re-measurement, and what it narrowed

Status: BUILT AND LANDED 2026-09-07. Closes the last open item of
`chip-20260902-checkoutdiverged-fullfix-r1r2r345`.

Companion to `checkoutdiverged_class_rootcause_20260902.md` (R1-R5 proposed) and
`checkoutdiverged_automated_exit_20260907.md` (R3 / DEFECT A+B). R1, R2, R3 and
R4 were already done; this records R5 and the R4 verification that unblocked it.

## R4 was already satisfied -- the "cloud-3 has neither" note was wrong

The chip's 2026-09-07T18:00Z state audit recorded `ree-cloud-3` as having
NEITHER the `ree-git-sync-repair` timer NOR the script, and cloud-2/cloud-5 as
unverified. Re-measured directly over ssh at 21:10Z, all five boxes:

| box | timer | deployed script | sha (12) | last exit |
|---|---|---|---|---|
| ree-cloud-1 | active | `/usr/local/bin/ree_git_sync_repair.sh` | `4936ab735db4` | 0 |
| ree-cloud-2 | active | same | `4936ab735db4` | 0 |
| ree-cloud-3 | active | same | `4936ab735db4` | 0 |
| ree-cloud-4 | active | same | `4936ab735db4` | 0 |
| ree-cloud-5 | active | same | `4936ab735db4` | 0 |

That sha is byte-identical to `ree-v3` `coordinator/deploy/ree-git-sync-repair.sh`
at worktree, `HEAD` **and** `origin/main`, and it carries the R3 DEFECT A/B fix
(`ahead_content_upstream`, 3 occurrences). Both variants' `REPOS` lists include
`REE_assembly`, so R5's stated precondition -- *"only meaningful after R4, or it
just chips a condition nothing can repair"* -- is met.

The earlier audit most likely hit the false-ABSENT trap it warned about itself:
the deployed path is `/usr/local/bin/`, not `~/REE_Working/scripts/`. **No sudo
hand-over is needed; there is nothing left to install.**

## The measurement

The 2026-09-02 refusal to widen was correct on its data and is now stale on its
own terms. It recorded REE_assembly p90 advance gaps of 339 min and concluded a
1.0h threshold "fires CONTINUOUSLY". **Those gaps were a measurement of the
defect R4 fixes** -- nothing pulled the work repos on the cloud boxes -- not of
REE_assembly's steady state.

Re-run 2026-09-07 over **51,738 reflog entries across 6 hosts** (DLAPTOP +
cloud-1..5; the 09-02 run had 15,134 across 2), gap between successive
local-branch ref advances:

| repo | per-host p90, all history (min) | max p90 | 7d max p90 |
|---|---|---|---|
| REE_Working | 10.7 / 12.9 / 8.6 | **12.9** | 35.1 |
| REE_assembly | 42.3 / 33.2 / 42.9 / 43.7 / 34.0 / 30.8 | **43.7** | 81.2 |
| ree-v3 | 110.5 / 124.9 / 143.8 / 142.9 / 155.6 / 615.2 | **615.2** | 297.0 |

REE_assembly's p90 is now *below* the 55.8 min figure REE_Working's own 1.0h
threshold was set above. **ree-v3 has not moved** and stays excluded: clearing
615 min needs a ~12h threshold, and stale ree-v3 *code* is already source 24's
(daemon drift) job. `ree-v2` / `REE_convergence` have never been measured at
all, which is its own reason not to watch them.

**Caveat, shared with the original measurement:** reflog ref-update gaps count
purely LOCAL commits as advances, while the detector's clock resets only on
actually reaching the recorded origin sha. The p90s are therefore optimistic --
which is why the thresholds carry margin rather than sitting just above them.

## What shipped

`scripts/hygiene_routine_tick.py`

* `_DIVERGENCE_REPOS = ("REE_Working", "REE_assembly")`.
* `_DIVERGENCE_STUCK_HOURS_BY_REPO = {"REE_assembly": 2.0}` + resolver
  `_divergence_threshold_hours()`. 2.0h clears REE_assembly's 7d max p90
  (81.2 min) with 48% margin. **REE_Working keeps 1.0h exactly.**
* `_DIVERGENCE_AHEAD_ZERO_ONLY = frozenset({"REE_assembly"})` -- fires only in
  the `ahead == 0` shape. Placed *after* the state bookkeeping so a repo that is
  ahead today and fast-forwards to `ahead == 0` tomorrow while still behind the
  same origin sha does not get its timer restarted.
* Per-repo consequence text (`_DIVERGENCE_CONSEQUENCE`). The tldr and prompt
  previously asserted REE_Working's dispatcher consequence for whatever repo
  fired; said of REE_assembly that is simply false.
* Meta gains `threshold_hours_by_repo` and `ahead_zero_only`.

`scripts/test_hygiene_routine_tick.py` -- `_DivergenceHarness.run_at` now PINS
`repo_names=("REE_Working",)`. The pre-existing tests assert on finding counts
and were written when the tuple had one entry; unpinned, every count assertion
would silently become a function of the production tuple's length.

## Why `ahead == 0`, and the held-out check that produced it

Per CLAUDE.md's GOV-HELDOUT-1. Only cases where the OLD and NEW wording give
DIFFERENT answers count.

* **C1 -- E5/E6/E7, 2026-08-30T15:05Z, ree-cloud-5, REE_assembly behind 5,
  ahead 0.** Old: silent, repo unwatched -- and this was a real census episode,
  including the class's first observed instance. New: clock starts, fires at 2h.
  **New is right.** Differs; the one clean historical case.
* **C2 -- DLAPTOP 2026-09-07, REE_assembly ahead=13 / behind=20 for a whole
  session.** Ordinary live work (session `peaceful-kare-a6a78f`, mid-task;
  commits that clear on its next push). The **draft** new rule -- widen at 2.0h,
  ungated -- fires here. That is a false positive on normal operation, i.e. the
  noisy-direction failure the scope comment exists to prevent. **This is the
  case that added the `ahead == 0` gate.** As shipped, both old and new are
  silent.
* **C3 -- E11, 2026-09-02T21:14Z, ree-cloud-4, REE_assembly diverged, detached
  mid-rebase, 8 UU.** The gate's accepted **cost**: `ahead > 0`, so the shipped
  rule stays silent where the ungated draft would have caught it. Accepted
  because that shape is already carried by other sources (`git_sync_repair`
  logs NEEDS_HUMAN on it; `ref_convergence_wedge` covers refused push-retries),
  whereas nothing else covers C1.

**Non-degeneracy finding, recorded as CLAUDE.md requires.** Only **one** clean
old-vs-shipped historical differing case exists (C1); C2 and C3 differ against
the *draft*, not the shipped rule. Per the standing instruction -- *"if you
cannot find 3 such cases, that is itself the finding ... narrowed, or shipped
with that stated explicitly"* -- this ships **narrowed and stated**: one repo,
one shape (`ahead == 0`), one measured threshold. It is **not** a general
licence to widen the detector. Any further repo needs its own advance-gap
measurement, and `DivergenceScopeTest` now enforces that mechanically --
`test_every_watched_repo_has_a_threshold_above_its_measured_p90` fails for any
repo added to `_DIVERGENCE_REPOS` without a recorded figure.

Independent support for the gate, beyond the held-out cases: for `ahead == 0`
the remedy is a zero-risk fast-forward the 10-minute puller *already performs*,
so a finding there means the automation has itself failed -- actionable, and
naturally quiet otherwise. It also implements the root-cause doc's own section-4
point that `ahead` was used in the prompt text but never in the fire decision.

## Verification

`scripts/test_hygiene_routine_tick.py`: **665 pass** (655 pre-existing + 10 new
in `DivergenceMultiRepoTest`, 6 of them negative controls), plus 5 new/rewritten
in `DivergenceScopeTest`. `run_scripts_tests.sh --changed` green from the MAIN
checkout.

Fault-injected, all three go red and restore green:

| neutralised | failures |
|---|---|
| `_DIVERGENCE_AHEAD_ZERO_ONLY` emptied | 4 |
| `_DIVERGENCE_STUCK_HOURS_BY_REPO` emptied | 2 |
| consequence text pinned back to REE_Working's | 1 |
