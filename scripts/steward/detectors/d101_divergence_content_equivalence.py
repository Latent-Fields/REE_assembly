#!/usr/bin/env python3
"""D-101 -- classify an ahead/behind divergence by CONTENT, not by count.

THE INCIDENT. On 2026-08-15 REE_assembly read "[ahead 66, behind 274], cannot
fast-forward". That looks dangerous enough to block a morning digest, and it
did. Working out what it actually meant took ~15 tool calls by hand: 28 commits
were already upstream by patch-id, every substantive remainder was present on
origin BY CONTENT (SOC-HUM-1..4, GOV-PRESERVE-1, the MECH-357 build note,
preservation_snapshot_plan.md), and the rest was regenerable igw automation
churn. The honest verdict was "safe to adopt". This detector is that analysis,
as a script.

The value is the difference between "272 behind, do not touch" and "safe to
adopt" -- a number that stops work versus a verdict that lets it continue.

THIS DETECTOR NEVER ACTS. It reports and classifies. Every git call goes
through _gitlane.git(), which refuses any non-read-only subcommand, so nothing
here can move a ref, stage, commit, rebase or reset on a shared checkout that
four other writers push to. A human, or a dedicated reconcile chip, acts on the
verdict.

PER-COMMIT CLASSES
=====================================================================
  upstream_by_patch_id  `git cherry` finds an equivalent commit upstream.
                        CLAUDE.md's route A.
  upstream_by_content   Every non-blank line the commit ADDED is already
                        present in origin's blob for that path. This is what
                        catches route A's endemic false negatives: a
                        whole-file read-modify-write that bundled two edits
                        which landed upstream separately, and an append that
                        landed at a different offset (different diff context
                        -> different patch-id). Both shapes are native to the
                        hot multi-writer JSON registries this lane exists for.
  regenerable_churn     Unique content, but confined to machine-written,
                        derive-only paths that the producing automation
                        rewrites on its next tick. Losing these loses nothing.
  superseded_upstream   The commit's content reached origin, but the path it
                        landed at was later renamed (and possibly reframed)
                        upstream, so the OLD path is absent from origin's HEAD
                        tree. A naive read of that absence says "unique";
                        FIELD_NOTES_20260815 section 1 is the incident: a
                        patch-id-equivalent commit whose path had been
                        deliberately renamed away, staged as `A ` after an
                        adopt -- committing it would have resurrected a
                        document, and the framing it carried, that a human
                        chose to drop. Never discard *content* origin never
                        had; this is the opposite case, content origin had and
                        then intentionally moved on from.
  unique                Real local work origin does not have. Never discard.
  merge                 Carries no content of its own; its parents are
                        classified individually.

TASK_CLAIMS.json AND TASK_CHIPS.json ARE NOT CHURN. This is the single most
important line in the file. They look like bookkeeping and they are written by
automation, so the pull toward listing them as regenerable is strong -- and
CLAUDE.md names doing so a category error, with a measured incident behind it:
a decision chip asserted exactly that of 26 commits, of which 15 were genuinely
stranded (7 whole TASK_CLAIMS entries plus their open/close commits, and a
TASK_CHIPS resolution origin still showed `open`). Executed as written it would
have dropped them permanently. The shape of a file explains why a patch-id
proof FAILS; it says nothing about whether the content reached origin. Encoded
here as an explicit deny-list so no future edit can quietly add them.

VERDICTS
=====================================================================
  safe_to_adopt       Nothing substantive would be lost: every ahead commit is
                      upstream by patch-id or by content, or is pure
                      regenerable churn.
  needs_rebase        Substantive unique work exists, but it touches no path
                      origin also changed in the behind range -- so it can be
                      replayed onto origin oldest-first with no conflict.
  unique_work_present Substantive unique work exists AND it touches paths
                      origin also modified. Replaying needs judgement (the
                      read-modify-write contamination class). Stop.

The safe_to_adopt verdict is deliberately NOT an instruction to adopt, and
deliberately does not escalate: it is the de-escalation of a scary-looking
number. Adoption still goes through scripts/safe_adopt_ref.py, whose own
independent recomputation of the discard set stays the gate -- two computations
must agree before any ref moves.
"""

from __future__ import annotations

import fnmatch
from pathlib import Path

from . import _gitlane as G
from ._common import Context, finding

DETECTOR_ID = "D-101"
DETECTOR_TITLE = "Divergence content equivalence"
TIER = "T2"   # reports a verdict; a human or a reconcile chip acts

# Machine-written, derive-only paths regenerated by their producer on the next
# tick. A unique commit confined to these loses nothing when discarded.
REGENERABLE_CHURN = (
    "evidence/planning/igw_routine_ledger.json",
    "evidence/planning/igw_assignments.json",
    "evidence/planning/igw_routine_log.md",
    "evidence/experiments/runner_heartbeats/*",
    "evidence/experiments/runner_status/*",
    "evidence/experiments/INDEX.md",
    "evidence/experiments/pending_review.md",
    "evidence/experiments/claim_evidence.v1.json",
    "evidence/experiments/substrate_status_snapshot.json",
    "experiment_queue.json",
)

# NEVER add to REGENERABLE_CHURN. See the module docstring: treating these as
# discardable-by-shape is a documented category error with 15 genuinely
# stranded commits behind it. Asserted by test_gitlane.py.
NEVER_CHURN = (
    "TASK_CLAIMS.json",
    "TASK_CHIPS.json",
    "docs/claims/claims.yaml",
    "WORKSPACE_STATE.md",
)


def _is_churn_path(path: str) -> bool:
    if any(fnmatch.fnmatch(path, p) or path.endswith("/" + p)
           for p in NEVER_CHURN):
        return False
    return any(fnmatch.fnmatch(path, p) for p in REGENERABLE_CHURN)


def _commit_blob(repo: Path, sha: str, path: str) -> str:
    """Blob SHA at an immutable COMMIT sha -- no pin needed, it cannot move."""
    return G.git(repo, "rev-parse", "--verify", "%s:%s" % (sha, path)).strip()


def _content_upstream(repo: Path, pin: G.RefPin, upstream: str,
                      sha: str, paths: list[str]) -> tuple[bool, list[str]]:
    """True when every path's added content is already present upstream."""
    missing = []
    for path in paths:
        # Fast, exact path first: identical blob means identical content, no
        # line analysis needed and no chance of a normalisation mismatch.
        if _commit_blob(repo, sha, path) == pin.blob_sha(upstream, path):
            continue
        added = G.added_lines(repo, sha, path)
        if not added:
            # Pure deletion or mode change, and the blobs already disagree.
            missing.append(path)
            continue
        # BOTH SIDES MUST BE NORMALISED THE SAME WAY. added_lines() strips each
        # line, so the upstream side must strip too -- comparing stripped
        # against unstripped makes every indented line look absent, which
        # classifies content that IS upstream as unique. Found live on
        # 2026-08-16 against a commit whose blob was byte-identical to
        # origin's; pinned by test_gitlane.py.
        upstream_lines = {l.strip() for l in pin.blob_lines(upstream, path)}
        if not all(line in upstream_lines for line in added):
            missing.append(path)
    return (not missing), missing


def _superseded_paths(repo: Path, upstream_sha: str, pin: G.RefPin,
                       upstream: str, paths: list[str]) -> dict[str, str]:
    """Of `paths`, the ones absent from upstream's HEAD tree that were
    RENAMED away somewhere in upstream's history (not merely deleted).
    {old_path: new_path}. See FIELD_NOTES_20260815 section 1.

    Only worth checking for a path already known to be missing upstream by
    exact name -- a present path needs no rename search.
    """
    out: dict[str, str] = {}
    for path in paths:
        if pin.blob_sha(upstream, path):
            continue
        target = G.renamed_away_target(repo, upstream_sha, path)
        if target:
            out[path] = target
    return out


def classify_repo(repo: Path, branch: str = "", upstream: str = "") -> dict:
    """Classify one repo's divergence. Pure analysis; writes nothing.

    Raises _gitlane.RefMoved if either pinned ref shifted while we worked --
    the caller must discard the result rather than report it. A conclusion
    computed across a ref move is unsound, not merely weaker.
    """
    repo = Path(repo).resolve()
    branch = branch or G.current_branch(repo)
    if not branch:
        return {"repo": str(repo), "skipped": "detached HEAD"}
    upstream = upstream or G.upstream_ref(repo, branch) or "origin/%s" % branch

    pin = G.RefPin.capture(repo, [branch, upstream])
    if not pin.shas.get(branch) or not pin.shas.get(upstream):
        return {"repo": str(repo), "branch": branch, "upstream": upstream,
                "skipped": "ref not resolvable (no remote-tracking ref?)"}

    branch_sha = pin.sha(branch)
    upstream_sha = pin.sha(upstream)

    ahead = G.commits_between(repo, upstream_sha, branch_sha)
    behind = G.commits_between(repo, branch_sha, upstream_sha)

    # Paths origin touched in the behind range -- the conflict surface.
    upstream_paths: set[str] = set()
    for sha in behind:
        upstream_paths.update(G.changed_paths(repo, sha))

    patch_ids = G.patch_id_equivalent(repo, upstream_sha, branch_sha)

    commits = []
    for sha in ahead:
        meta = G.commit_meta(repo, sha)
        if G.is_merge(repo, sha):
            meta.update({"klass": "merge", "paths": []})
            commits.append(meta)
            continue

        paths = G.changed_paths(repo, sha)
        meta["paths"] = paths

        if sha in patch_ids:
            # A patch-id hit proves the WHOLE diff already exists upstream,
            # so a path missing from HEAD is never a content gap -- only ever
            # upstream having since moved that path elsewhere. Resolve which,
            # before publishing, per FIELD_NOTES_20260815 section 1.
            superseded = _superseded_paths(repo, upstream_sha, pin, upstream, paths)
            if superseded:
                meta["klass"] = "superseded_upstream"
                meta["superseded_paths"] = superseded
            else:
                meta["klass"] = "upstream_by_patch_id"
        else:
            ok, missing = _content_upstream(repo, pin, upstream, sha, paths)
            if ok:
                meta["klass"] = "upstream_by_content"
            else:
                # Route A's false-negative shapes (section 2) can leave a
                # renamed-away path unresolved by both patch-id and the plain
                # content probe -- follow rename history before concluding
                # unique. Requires EVERY missing path to resolve as a rename;
                # a partial resolution is not enough to clear the commit.
                superseded = _superseded_paths(repo, upstream_sha, pin,
                                                upstream, missing)
                still_missing = [p for p in missing if p not in superseded]
                if superseded and not still_missing:
                    meta["klass"] = "superseded_upstream"
                    meta["superseded_paths"] = superseded
                elif paths and all(_is_churn_path(p) for p in paths):
                    meta["klass"] = "regenerable_churn"
                else:
                    meta["klass"] = "unique"
                    meta["missing_paths"] = missing
                    if superseded:
                        meta["superseded_paths"] = superseded
        commits.append(meta)

    substantive = [c for c in commits if c["klass"] == "unique"]
    contested = sorted({p for c in substantive
                        for p in c.get("missing_paths") or []
                        if p in upstream_paths})

    if not substantive:
        verdict = "safe_to_adopt"
    elif contested:
        verdict = "unique_work_present"
    else:
        verdict = "needs_rebase"

    # Re-read before publishing. This is the whole point of D-102's guard.
    pin.assert_unmoved()

    tally: dict[str, int] = {}
    for c in commits:
        tally[c["klass"]] = tally.get(c["klass"], 0) + 1

    return {
        "repo": str(repo), "branch": branch, "upstream": upstream,
        "branch_sha": branch_sha, "upstream_sha": upstream_sha,
        "pinned_at": pin.captured_at,
        "ahead": len(ahead), "behind": len(behind),
        "verdict": verdict, "tally": tally, "commits": commits,
        "substantive_unique": [c["sha"] for c in substantive],
        "contested_paths": contested,
    }


def run(ctx: Context) -> tuple[list[dict], dict]:
    findings, results = [], []

    for repo in ctx.git_repos or [ctx.repo_root]:
        repo = Path(repo)
        name = repo.name
        if not G.is_git_repo(repo):
            continue
        try:
            res = classify_repo(repo)
        except G.RefMoved as exc:
            # Do NOT downgrade to a weaker verdict -- publish nothing.
            findings.append(finding(
                detector=DETECTOR_ID, subject="%s:ref-moved" % name,
                title="%s: origin moved mid-analysis, divergence verdict withheld" % name,
                detail=("A pinned ref changed while the divergence was being "
                        "classified (%s). The analysis is unsound and has been "
                        "discarded rather than reported -- a verified-then-stale "
                        "answer is more dangerous than no answer, because it is "
                        "trusted. Re-run when the remote is quiet." % exc),
                severity="P2", confidence=1.0, signal="strong",
                escalate=False, tier=TIER, autofix=False,
                evidence={"repo": str(repo), "moves": exc.moves},
                route="/governance",
            ))
            continue

        if res.get("skipped"):
            continue
        results.append(res)
        # Publish the pin this verdict was computed against, so D-102 can
        # re-verify it at end of run (the tail window) and so a consumer can
        # guard() against these exact SHAs before acting.
        ctx.ref_pins[str(repo)] = {
            "captured_at": res["pinned_at"],
            "shas": {res["branch"]: res["branch_sha"],
                     res["upstream"]: res["upstream_sha"]},
        }
        if res["ahead"] == 0 and res["behind"] == 0:
            continue

        verdict = res["verdict"]
        tally = res["tally"]
        shape = ", ".join("%s=%d" % (k, v) for k, v in sorted(tally.items()))

        if verdict == "safe_to_adopt":
            sev, conf, sig, esc = "P3", 0.9, "strong", False
            headline = ("%s: [ahead %d, behind %d] but NOTHING substantive "
                        "would be lost" % (name, res["ahead"], res["behind"]))
        elif verdict == "needs_rebase":
            sev, conf, sig, esc = "P1", 0.85, "strong", True
            headline = ("%s: %d unique local commit(s), replayable cleanly"
                        % (name, len(res["substantive_unique"])))
        else:
            sev, conf, sig, esc = "P0", 0.9, "strong", True
            headline = ("%s: %d unique local commit(s) CONTEST %d upstream-"
                        "modified path(s)" % (name,
                                              len(res["substantive_unique"]),
                                              len(res["contested_paths"])))

        detail = (
            "branch %s (%s) vs %s (%s), pinned %s.\n"
            "ahead=%d behind=%d; per-commit: %s.\n"
            "VERDICT: %s.\n%s"
            % (res["branch"], res["branch_sha"][:12], res["upstream"],
               res["upstream_sha"][:12], res["pinned_at"],
               res["ahead"], res["behind"], shape or "-", verdict,
               _advice(verdict, res)))

        findings.append(finding(
            detector=DETECTOR_ID, subject=name, title=headline, detail=detail,
            severity=sev, confidence=conf, signal=sig,
            escalate=esc, tier=TIER, autofix=False,
            evidence={
                "repo": str(repo), "branch": res["branch"],
                "upstream": res["upstream"],
                "branch_sha": res["branch_sha"],
                "upstream_sha": res["upstream_sha"],
                "pinned_at": res["pinned_at"],
                "ahead": res["ahead"], "behind": res["behind"],
                "verdict": verdict, "tally": tally,
                "substantive_unique": res["substantive_unique"],
                "contested_paths": res["contested_paths"],
                "commits": [{"sha": c["sha"][:12], "klass": c["klass"],
                             "author": c["author"], "subject": c["subject"]}
                            for c in res["commits"]],
            },
            route="/governance",
        ))

    return findings, {
        "detector": DETECTOR_ID, "title": DETECTOR_TITLE, "tier": TIER,
        "n_findings": len(findings),
        "repos": [{"repo": r["repo"], "verdict": r["verdict"],
                   "ahead": r["ahead"], "behind": r["behind"]}
                  for r in results],
    }


def _advice(verdict: str, res: dict) -> str:
    if verdict == "safe_to_adopt":
        return ("Every ahead commit is already upstream (by patch-id or by "
                "content) or is regenerable churn. Adoption is still performed "
                "by scripts/safe_adopt_ref.py, whose independent recomputation "
                "of the discard set remains the gate -- this verdict lowers the "
                "alarm, it does not authorise the move.")
    if verdict == "needs_rebase":
        return ("Unique local work exists but touches no path origin changed, "
                "so it replays cleanly. Cherry-pick OLDEST FIRST onto origin in "
                "a throwaway worktree and push (CLAUDE.md recovery procedure); "
                "cherry-pick preserves the original author. Commits: %s"
                % ", ".join(s[:12] for s in res["substantive_unique"]))
    return ("Unique local work touches paths origin also modified: %s. A replay "
            "needs judgement -- this is the read-modify-write contamination "
            "class, where a mechanical merge can adopt or clobber another "
            "session's work. Audit each commit's content against origin before "
            "anything moves. Commits: %s"
            % (", ".join(res["contested_paths"][:8]),
               ", ".join(s[:12] for s in res["substantive_unique"])))
