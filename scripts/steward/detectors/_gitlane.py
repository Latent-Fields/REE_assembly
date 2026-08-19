#!/usr/bin/env python3
"""Shared git primitives for the Steward git lane (D-101, D-102).

THE GIT LANE REPORTS AND CLASSIFIES. IT NEVER ACTS.
=====================================================================
These detectors run against a SHARED checkout that other machines push to.
Nothing here may move a ref, stage, commit, push, rebase, reset, or force
anything -- a human or a dedicated reconcile chip acts on the verdict.

That rule is enforced STRUCTURALLY, not by comment: every git call goes
through git(), which refuses any subcommand outside READ_ONLY_SUBCOMMANDS.
A future edit that reaches for `git update-ref` here raises GitLaneViolation
instead of silently mutating a checkout three other boxes are pushing to.
The allowlist is deliberately a WHITELIST -- a blacklist would have to
anticipate every mutating porcelain command, and the one it forgets is the
one that runs.

WHY A PIN (D-102), AND WHY IT IS THE LOAD-BEARING PART
=====================================================================
On 2026-08-15 origin/master advanced three times inside one session (05:05,
05:08, 05:38 UTC). An equivalence check run before the 05:38 fetch reported
"identical" for self_attribution_plan.md -- a file that had by then been
rewritten upstream (+254 lines, the GAP-6 split). The stale "verified"
answer was acted on.

A verified-then-stale check is MORE DANGEROUS THAN NO CHECK, because it is
trusted. So the pin is not a convenience wrapper; it is the mechanism that
makes this class of error impossible to hit silently:

  * RefPin.capture() resolves every ref to a concrete SHA once, up front.
  * Every read afterwards goes through the pin and names the SHA, never the
    symbolic ref. `git diff <a> <b> -- <path>` against a remote-tracking ref
    that may move is EXACTLY how the above went wrong, so the pin's API does
    not expose a path that can do it.
  * assert_unmoved() re-reads before any verdict is published and raises
    RefMoved if anything shifted -- the analysis is then discarded, not
    reported. Aborting is the correct outcome: a conclusion computed across
    a ref move is not a weaker conclusion, it is an unsound one.

ASCII-only output per the repo-wide rule.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

# Every subcommand the git lane is permitted to run. All are read-only:
# they inspect objects and refs and write nothing (no index, no worktree, no
# ref, no remote). `fetch` is deliberately ABSENT -- fetching moves
# remote-tracking refs, which is precisely the movement the pin exists to
# detect. The lane observes the checkout as it finds it.
READ_ONLY_SUBCOMMANDS = frozenset({
    "rev-parse", "rev-list", "cherry", "show", "diff-tree", "cat-file",
    "for-each-ref", "log", "merge-base", "status", "symbolic-ref", "name-rev",
})


class GitLaneViolation(RuntimeError):
    """A non-read-only git subcommand was attempted. Always a bug, never data."""


class RefMoved(RuntimeError):
    """A pinned ref changed value. Any analysis in flight is now unsound."""

    def __init__(self, moves: list[tuple[str, str, str]]) -> None:
        self.moves = moves
        detail = "; ".join("%s %s -> %s" % (r, (o or "absent")[:12],
                                            (n or "absent")[:12])
                           for r, o, n in moves)
        super().__init__("pinned ref moved during analysis: " + detail)


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def git(repo: Path, *args: str, check: bool = False) -> str:
    """Run one READ-ONLY git command in `repo` and return stdout.

    Raises GitLaneViolation for anything outside READ_ONLY_SUBCOMMANDS. On a
    non-zero exit returns "" unless check=True -- most callers are probing for
    the absence of something (a path not in a tree, a ref that does not exist)
    and absence is an answer, not an error.
    """
    if not args:
        raise GitLaneViolation("no git subcommand given")
    sub = args[0]
    if sub not in READ_ONLY_SUBCOMMANDS:
        raise GitLaneViolation(
            "git lane is read-only: refused subcommand %r. If a reconcile step "
            "genuinely needs to act, it belongs outside the detectors." % sub)
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        if check:
            raise RuntimeError("git %s failed: %s"
                               % (" ".join(args), proc.stderr.strip()))
        return ""
    return proc.stdout


def is_git_repo(path: Path) -> bool:
    return bool(git(Path(path), "rev-parse", "--git-dir").strip())


def current_branch(repo: Path) -> str:
    out = git(repo, "rev-parse", "--abbrev-ref", "HEAD").strip()
    return "" if out in ("", "HEAD") else out


def upstream_ref(repo: Path, branch: str) -> str:
    """The branch's configured upstream, e.g. origin/master. "" if unset."""
    return git(repo, "rev-parse", "--abbrev-ref",
               "%s@{upstream}" % branch).strip()


@dataclass
class RefPin:
    """An immutable snapshot of one repo's refs, taken once, verified later.

    Read every blob through this object. It is the only supported way to look
    at a ref in the git lane, and that is the point: an API that cannot name a
    moving ref cannot be misused the way the 2026-08-15 session's check was.
    """

    repo: Path
    captured_at: str
    shas: dict[str, str] = field(default_factory=dict)

    @classmethod
    def capture(cls, repo: Path, refs: list[str]) -> "RefPin":
        repo = Path(repo).resolve()
        shas = {}
        for ref in refs:
            if not ref:
                continue
            shas[ref] = git(repo, "rev-parse", "--verify", "%s^{commit}" % ref).strip()
        return cls(repo=repo, captured_at=_utc_now(), shas=shas)

    def sha(self, ref: str) -> str:
        """The pinned SHA for `ref`. KeyError if it was never pinned.

        Deliberately strict: reading a ref that was not pinned is how a moving
        target gets back into the analysis, so it is an error rather than a
        lazy resolve.
        """
        if ref not in self.shas:
            raise KeyError("ref %r was not pinned; pin it at capture time" % ref)
        return self.shas[ref]

    def moved(self) -> list[tuple[str, str, str]]:
        """Re-read every pinned ref. Returns [(ref, pinned, current), ...]."""
        out = []
        for ref, old in self.shas.items():
            new = git(self.repo, "rev-parse", "--verify",
                      "%s^{commit}" % ref).strip()
            if new != old:
                out.append((ref, old, new))
        return out

    def assert_unmoved(self) -> None:
        """Re-read before publishing any verdict. Raise RefMoved if anything shifted."""
        moves = self.moved()
        if moves:
            raise RefMoved(moves)

    def blob_sha(self, ref: str, path: str) -> str:
        """Blob SHA of `path` at the PINNED commit. "" when absent from that tree.

        Compare these, never `git diff --quiet <a> <b> -- <path>` against a ref
        that may move. See the module docstring.
        """
        return git(self.repo, "rev-parse", "--verify",
                   "%s:%s" % (self.sha(ref), path)).strip()

    def blob_lines(self, ref: str, path: str) -> list[str]:
        text = git(self.repo, "show", "%s:%s" % (self.sha(ref), path))
        return text.splitlines()

    def to_dict(self) -> dict:
        return {"repo": str(self.repo), "captured_at": self.captured_at,
                "shas": dict(self.shas)}

    @classmethod
    def from_dict(cls, d: dict) -> "RefPin":
        return cls(repo=Path(d.get("repo", ".")),
                   captured_at=str(d.get("captured_at") or ""),
                   shas=dict(d.get("shas") or {}))


# --------------------------------------------------------------------------
# Commit-level reads, all against pinned SHAs
# --------------------------------------------------------------------------

def commits_between(repo: Path, base_sha: str, head_sha: str) -> list[str]:
    """SHAs in base..head, OLDEST FIRST.

    Oldest-first because that is the order a recovery cherry-pick must use
    (CLAUDE.md's recovery procedure), so a report read top-to-bottom is
    directly actionable.
    """
    out = git(repo, "rev-list", "--reverse", "%s..%s" % (base_sha, head_sha))
    return [l.strip() for l in out.splitlines() if l.strip()]


def commit_meta(repo: Path, sha: str) -> dict:
    out = git(repo, "show", "-s", "--format=%H%x1f%an%x1f%aI%x1f%s", sha)
    parts = out.strip().split("\x1f")
    if len(parts) < 4:
        return {"sha": sha, "author": "", "date": "", "subject": ""}
    return {"sha": parts[0], "author": parts[1], "date": parts[2],
            "subject": parts[3]}


def is_merge(repo: Path, sha: str) -> bool:
    out = git(repo, "rev-list", "--parents", "-n", "1", sha).strip()
    return len(out.split()) > 2


def changed_paths(repo: Path, sha: str) -> list[str]:
    out = git(repo, "diff-tree", "--no-commit-id", "--name-only", "-r", sha)
    return [l.strip() for l in out.splitlines() if l.strip()]


def patch_id_equivalent(repo: Path, upstream_sha: str, head_sha: str) -> set[str]:
    """SHAs in upstream..head that git cherry says already exist upstream.

    `git cherry` prints "- <sha>" for a commit whose patch-id is present
    upstream and "+ <sha>" for one that is not. This is route A of CLAUDE.md's
    two proof routes.

    Route A has REAL FALSE NEGATIVES and they are common, not exotic: a
    whole-file read-modify-write that bundled two edits which landed upstream
    separately, and an append that landed at a different offset (the 3 lines of
    diff context differ, so the patch-id does). Both shapes are endemic to the
    hot multi-writer JSON registries this lane exists for. That is exactly why
    content equivalence is checked as well -- and why an unproven commit is
    reported for audit rather than assumed discardable.
    """
    out = git(repo, "cherry", upstream_sha, head_sha)
    found = set()
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("- "):
            found.add(line[2:].strip())
    return found


def added_lines(repo: Path, sha: str, path: str) -> list[str]:
    """Non-blank lines this commit ADDED to `path`.

    --unified=0 so no context lines are mistaken for additions. Uses `git show`
    rather than `git diff <sha>^ <sha>` so a root commit (no parent) works.
    """
    out = git(repo, "show", "--format=", "--unified=0", sha, "--", path)
    lines = []
    for raw in out.splitlines():
        if raw.startswith("+++") or raw.startswith("---"):
            continue
        if raw.startswith("+"):
            body = raw[1:].strip()
            if body:
                lines.append(body)
    return lines


def renamed_away_target(repo: Path, since_sha: str, path: str) -> str:
    """If `path` was renamed to a new name somewhere in the history reachable
    from `since_sha`, return the new path. "" if `path` was never removed
    there, or was removed by a genuine delete rather than a rename.

    Two-step, matching the FIELD_NOTES_20260815 recipe (section 1):

      1. `log --diff-filter=D --follow -- path` finds the commit(s) that
         removed this exact path. No -M here on purpose: without rename
         detection a rename shows as a plain delete of the old path (paired
         with an unrelated-looking add of the new one), which is exactly the
         event this step needs to find -- adding -M would make a rename
         invisible to --diff-filter=D and defeat the search.
      2. `diff-tree -M --name-status` on each candidate re-examines just that
         one commit WITH rename detection, which is what can tell a rename
         apart from a genuine delete (git does not otherwise record "this
         delete and that add were the same file" anywhere).

    A path can be deleted more than once across history (deleted, restored,
    deleted again) -- the first candidate (closest to `since_sha`, since `log`
    lists newest-first) that resolves as a rename wins.
    """
    out = git(repo, "log", since_sha, "--diff-filter=D", "--follow",
              "--format=%H", "--", path)
    for sha in (l.strip() for l in out.splitlines() if l.strip()):
        stat = git(repo, "diff-tree", "--no-commit-id", "-r", "-M",
                   "--name-status", sha)
        for line in stat.splitlines():
            parts = line.split("\t")
            if len(parts) == 3 and parts[0][:1] == "R" and parts[1] == path:
                return parts[2]
    return ""
