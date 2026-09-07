# checkoutdiverged: the automated exit (DEFECT A / DEFECT B)

Status: BUILT AND LANDED 2026-09-07. Supersedes the cadence hypothesis (D1) in
`checkoutdiverged_class_rootcause_20260902.md` as the explanation for the
CONTINUING recurrence on DLAPTOP.

## What was actually wrong

The 2026-09-02 root-cause pass shipped R1 (episodic re-minting) and R2
(proof-gated registry exemption on the fast-forward path). Both were verified
BUILT AND WORKING on 2026-09-07 -- and the class re-fired anyway (g2 2026-09-06,
g3 2026-09-07). So the remedy set did not address the live cause.

D1 blamed cadence ("the Mac's puller runs every 3h against a 1h detector
threshold"). That premise is stale: `com.ree.gitsyncrepair.plist` has
`StartInterval = 600` (10 minutes). The puller was running on time, reaching the
repo, and REFUSING every cycle:

    17:27:49Z REE_Working NEEDS_HUMAN (wedged: rebase=0 detached=0 ahead=2 behind=18)
              -- uncommitted non-telemetry change: worktree_session_registry.json
    17:37:56Z REE_Working NEEDS_HUMAN (wedged: ... ahead=2 behind=23)
    17:48:07Z REE_Working NEEDS_HUMAN (wedged: ... ahead=2 behind=28)
              -- uncommitted non-telemetry change: docs/worktree_session_registry.md

`behind` climbing 18 -> 23 -> 28 in 20 minutes (trunk moves ~21 commits/hour)
with `ahead` pinned at 2.

**DEFECT A.** `wedged=1` is set by `[ ahead -gt 0 ] && [ behind -gt 0 ]`. The
wedged path's automated exit (gate 2) required every ahead commit to be
TELEMETRY-ONLY. That became permanently unsatisfiable when the telemetry git
path was retired (CLAUDE.md A-93): coordination-plane ahead commits are
WORKSPACE_STATE / registry / TASK_*, never `runner_heartbeats/`. So the gate
could never pass, the checkout could never self-recover, and hygiene source 25
re-minted `chip-checkoutdiverged-<host>-gN` indefinitely. Note this is NOT "R2
did not work" -- R2 lives entirely inside the `wedged = 0` branch and is never
reached on a wedged repo.

**DEFECT B.** The wedged path's "precious" test (gate 3) used only
`TELEMETRY_RE`, so it called a REGENERATED file precious -- even though the
non-wedged path already relies on `derived_re_for_repo` to assert the opposite
about those exact paths. Two paths disagreeing about the same file.

## The fix

`scripts/ree_git_sync_repair.sh`
* gate 3 now excludes `derived_re` paths as well as telemetry.
* gate 2 widens from "telemetry-only" to "regenerable-only OR provably already
  upstream", via a new `ahead_content_upstream()` helper. It does NOT invent a
  proof: it delegates to `reconcile_wedge_content.py`, the module that already
  adjudicates this exact question for the human path. Two-step, and the ORDER is
  the safety property: `--check` exit 0 = nothing stranded; exit 3 = LAND it
  first with `--apply` (which pushes a reconstruction from a throwaway worktree
  and never moves a ref), then re-check. Landing before discarding is what makes
  it non-destructive. Anything else -- refusal, missing python, missing module,
  timeout -- fails CLOSED to the old NEEDS_HUMAN behaviour.

`scripts/reconcile_wedge_content.py`
* new `--ignore-regenerable-regex`, opt-in and off by default. Needed because
  the allowlist gate is per-commit over the whole ahead RANGE, so ONE regenerated
  file anywhere in the range refused the entire scan -- which made the module
  unusable from the automated path for the commonest wedge shape.
* It does NOT make a path reconcilable; it drops the path from consideration, on
  the caller's assertion that a named tool reproduces it. The caller passes
  exactly its own `derived_re_for_repo`, so no new judgement is introduced.
* LAUNDERING GUARD: a regex matching any RECONCILABLE path REFUSES. Exempting a
  content-bearing path would silently convert "land it" into "ignore it", and a
  later `--adopt` would then discard it -- the exact loss the module exists to
  prevent, arriving through its own safety valve. A bad regex also refuses
  rather than matching nothing.

## Tests

* `scripts/test_ree_git_sync_repair.sh` -- 73 pass (43 pre-existing + 30 new).
  New: A1 (proven-upstream repairs), A2 (refusal -> NEEDS_HUMAN), A3 (stranded
  is LANDED then repaired), A4 (failed land discards nothing), A5 (no prover ->
  fail closed), B1 (derived-only needs no proof), B2 (non-derived still needs
  it), B3 (derived dirt not precious), B4 (real dirt still precious).
* `scripts/test_reconcile_wedge_regenerable.py` -- 8 pass, 6 of them negative
  controls (off by default; unmatched unclassifiable still aborts; bad regex
  refuses; exempting a RECONCILABLE path refuses; `.*` refuses; excluded means
  excluded, never landed).
* `scripts/test_reconcile_wedge_content.py` -- 35 pass, unchanged (no regression
  in the module's existing refusals).

## GOV-HELDOUT-1 check -- RESULT: ONLY 2 NON-DEGENERATE CASES FOUND

CLAUDE.md requires >= 3 historical cases where the OLD and NEW wording give
DIFFERENT answers, and says explicitly: "If you cannot find 3 such cases, that
is itself the finding -- the rule is probably scoped to its motivating incident,
and should be narrowed, or shipped with that stated explicitly." **It is shipped
with that stated explicitly. This is scoped to its motivating shape, not a
general rule.**

NON-DEGENERATE (old and new differ; new is correct):
1. **DLAPTOP g3 at the 17:48Z snapshot, 2026-09-07 (measured, this incident).**
   ahead = a WORKSPACE_STATE append + a merge carrying WORKSPACE_STATE and
   `docs/worktree_session_registry.md`. OLD: NEEDS_HUMAN forever (logged every
   10 min, behind 18 -> 28). NEW: gate 3 passes (derived dirt), gate 2 consults
   the prover, `--check` finds the stranded block, `--apply` lands it, re-check
   clean, REPAIRING. This is exactly what was done BY HAND in this session
   (landed `b2857b5423`, then adopted).
2. **2026-08-15 cloud5-umbrella, 15 of 26 commits genuinely stranded.** OLD:
   NEEDS_HUMAN, after which a human argued from commit SHAPE and would have
   dropped 15 stranded commits. NEW: the prover LANDS stranded content instead
   of anyone discarding it. Stated honestly: this was a ref-adoption situation,
   not literally this script's input, so it is the same decision shape rather
   than the same code path -- weaker evidence than case 1.

DEGENERATE (old and new agree -- these test nothing, and are listed so the
check is not inflated):
* DLAPTOP gen-1 (2026-08-29): ahead = `dispatcher_control.json` lease grants.
  Outside RECONCILABLE -> prover refuses -> NEEDS_HUMAN either way. Correct:
  that is live coordination state.
* DLAPTOP g2 (2026-09-06): ahead = the chip-archive commit touching
  `chip_archive/2026-08.json`. Outside RECONCILABLE -> NEEDS_HUMAN either way.
* DLAPTOP g3 at the 19:51Z snapshot: the range had grown to include a SKILL.md
  commit -> prover refuses -> NEEDS_HUMAN either way. Correct.
* ree-cloud-4 / ree-cloud-5 / REE_assembly-cloud5 (2026-08-30): all `ahead = 0`,
  so the non-wedged path, which R2 already fixed. My change does not reach them.

NEGATIVE CONTROLS (must keep refusing, and do -- pinned by B2/B4/A2/A4/A5):
* An ahead commit touching `ree_core/` (real code).
* Today's REE_assembly wedge (`ahead=13 behind=20`, dirty
  `substrate_status_snapshot.json`): `derived_re` is EMPTY for every repo except
  REE_Working, so gate 3 is byte-identical to before there and it still refuses.
  That was live work owned by `peaceful-kare-a6a78f`; refusing was correct.
* The 2026-07-30 relaxed-montalcini igw-ledger commits: outside RECONCILABLE.

**Honest scope statement.** Of the six real historical instances of this class,
the fix changes the answer on ONE (plus one analogous case). It is not a general
solution to checkoutdiverged; it closes the specific shape where the ahead range
is coordination bookkeeping plus regenerated output. Every other shape still
stops for a human, by design. Whether that materially reduces the recurrence
rate is a MEASUREMENT owed in ~7 days, not a claim made here -- the same
discipline `chip-20260904-refwedge-r1-rate-cost-remeasure` applies to R1.

## Still not done (R5)

`_DIVERGENCE_REPOS` in `hygiene_routine_tick.py` is still `("REE_Working",)`;
divergence of the work repos on any box remains undetected by source 25. R4 gap:
`ree-cloud-3` has neither the sync-repair timer nor the script (cloud-1 and
cloud-4 are fine; the deployed path is `/usr/local/bin/`, so checking the repo
path reports a false ABSENT).
