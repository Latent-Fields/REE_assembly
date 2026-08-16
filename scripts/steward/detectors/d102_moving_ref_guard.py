#!/usr/bin/env python3
"""D-102 -- the moving-ref guard: pin origin, re-read before acting, ABORT if moved.

THE INCIDENT, AND WHY THIS IS P0. During the 2026-08-15 session origin/master
advanced three times: 05:05, 05:08 and 05:38 UTC. An equivalence check run
before the 05:38 fetch reported "identical" for self_attribution_plan.md -- a
file that had by then been substantially rewritten upstream (+254 lines, the
GAP-6 split). The stale "verified" answer was acted on.

A verified-then-stale check is MORE DANGEROUS THAN NO CHECK, because it is
trusted. An unchecked divergence makes a session cautious; a check that says
"identical" makes it confident. So the guard is not an accuracy improvement, it
is the difference between a wrong answer being caught and a wrong answer being
believed.

WHAT THIS DETECTOR ADDS ON TOP OF RefPin
=====================================================================
_gitlane.RefPin is the primitive: capture SHAs once, read every blob through
the pinned SHA, assert_unmoved() before publishing. D-101 uses it internally
and discards its own verdict if its pin shifts. That closes the WITHIN-detector
window. Two windows remain, and this detector closes both:

  1. THE TAIL WINDOW. A ref can move after D-101 finishes but before the report
     is written and read. So D-102 runs LAST and re-verifies every pin any
     git-lane detector published this run. If one moved, the report carries an
     explicit "verdict computed against a ref that has since moved" finding,
     and the verdict must be recomputed rather than acted on.

  2. THE CROSS-RUN WINDOW -- the perishability question, which is the one a
     human actually needs answered. A steward report is read minutes to hours
     after it is generated. Knowing origin moved 3 times in the 40 minutes
     around the last run tells you a git-lane verdict in that report is
     perishable and must be re-derived before acting. Knowing it has not moved
     in two days tells you it is still good. That is why the pins are persisted
     to state/steward_ref_pins.json with timestamps and diffed run over run.

USING THE GUARD FROM A RECONCILE STEP. Any consumer that intends to ACT on a
git-lane verdict -- and acting is always outside these detectors -- should call
guard() with the SHAs the verdict was computed against:

    from detectors.d102_moving_ref_guard import guard
    guard(repo, {"origin/master": "<sha the report recorded>"})

It raises _gitlane.RefMoved if reality has moved on. Fail loud, then re-derive.
Never soften it to a warning: a warning on a moving ref is how the 2026-08-15
answer got trusted.

THIS DETECTOR NEVER FETCHES. `fetch` is deliberately absent from the git lane's
read-only allowlist, because fetching MOVES remote-tracking refs -- it would be
the guard causing the movement it exists to detect. The lane observes the
checkout as it finds it; whoever fetches does so explicitly, outside.
"""

from __future__ import annotations

from pathlib import Path

from . import _gitlane as G
from ._common import Context, finding

DETECTOR_ID = "D-102"
DETECTOR_TITLE = "Moving ref guard"
TIER = "T2"


def guard(repo: Path, expected: dict[str, str]) -> None:
    """Re-read `expected` {ref: sha} and raise _gitlane.RefMoved on any change.

    The abort primitive. Call this immediately before any action taken on a
    git-lane verdict, passing the SHAs that verdict was computed against.
    """
    repo = Path(repo).resolve()
    moves = []
    for ref, sha in (expected or {}).items():
        now = G.git(repo, "rev-parse", "--verify", "%s^{commit}" % ref).strip()
        if now != sha:
            moves.append((ref, sha, now))
    if moves:
        raise G.RefMoved(moves)


def _pin_refs_for(repo: Path) -> list[str]:
    branch = G.current_branch(repo)
    if not branch:
        return []
    upstream = G.upstream_ref(repo, branch) or "origin/%s" % branch
    return [r for r in (branch, upstream) if r]


def run(ctx: Context) -> tuple[list[dict], dict]:
    findings = []
    current: dict[str, dict] = {}
    prior: dict = ctx.prior_ref_pins or {}

    for repo in ctx.git_repos or [ctx.repo_root]:
        repo = Path(repo).resolve()
        if not G.is_git_repo(repo):
            continue
        refs = _pin_refs_for(repo)
        if not refs:
            continue
        pin = G.RefPin.capture(repo, refs)
        current[str(repo)] = pin.to_dict()

        # --- window 1: pins any git-lane detector published THIS run ---
        published = (ctx.ref_pins or {}).get(str(repo))
        if published:
            try:
                guard(repo, published.get("shas") or {})
            except G.RefMoved as exc:
                findings.append(finding(
                    detector=DETECTOR_ID,
                    subject="%s:in-run" % repo.name,
                    title=("%s: ref moved AFTER this run's git-lane verdict was "
                           "computed" % repo.name),
                    detail=(
                        "A git-lane verdict in this report was computed against "
                        "refs that have already moved (%s). Do NOT act on it -- "
                        "re-run the analysis. This is the exact 2026-08-15 shape: "
                        "a check that was correct when it ran and wrong by the "
                        "time it was used, which is more dangerous than no check "
                        "because it is trusted." % exc),
                    severity="P0", confidence=1.0, signal="strong",
                    escalate=True, tier=TIER, autofix=False,
                    evidence={"repo": str(repo), "moves": exc.moves,
                              "published_pin": published},
                    route="/governance",
                ))

        # --- window 2: movement since the previous steward run ---
        was = (prior.get(str(repo)) or {}).get("shas") or {}
        moved = [(ref, was[ref], pin.shas.get(ref, ""))
                 for ref in sorted(was)
                 if ref in pin.shas and was[ref] != pin.shas[ref]]
        if moved:
            since = (prior.get(str(repo)) or {}).get("captured_at") or "?"
            remote_moved = [m for m in moved if "/" in m[0]]
            findings.append(finding(
                detector=DETECTOR_ID,
                subject="%s:since-last-run" % repo.name,
                title=("%s: %d pinned ref(s) moved since the last steward run"
                       % (repo.name, len(moved))),
                detail=(
                    "Refs pinned at %s have since changed: %s. This is not a "
                    "defect -- it is the PERISHABILITY of any git-lane verdict "
                    "in this report. %s Re-derive, or call "
                    "d102_moving_ref_guard.guard() with the SHAs the verdict "
                    "recorded, before acting on it."
                    % (since,
                       "; ".join("%s %s -> %s" % (r, o[:12], n[:12])
                                 for r, o, n in moved),
                       "origin is actively moving, so treat any adopt/rebase "
                       "verdict as short-lived." if remote_moved
                       else "Only local refs moved.")),
                severity="P3", confidence=1.0, signal="strong",
                escalate=False, tier=TIER, autofix=False,
                evidence={"repo": str(repo), "pinned_at_prev": since,
                          "pinned_at_now": pin.captured_at,
                          "moved": [{"ref": r, "from": o, "to": n}
                                    for r, o, n in moved]},
                route="/governance",
            ))

    # The runner persists this to state/steward_ref_pins.json (unless writing
    # is off), which is what makes the cross-run comparison possible next time.
    ctx.ref_pins_out.update(current)

    return findings, {
        "detector": DETECTOR_ID, "title": DETECTOR_TITLE, "tier": TIER,
        "n_findings": len(findings),
        "repos_pinned": len(current),
    }
