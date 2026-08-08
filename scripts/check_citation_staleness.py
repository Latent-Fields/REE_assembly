#!/usr/bin/env python3
"""Detect stale/dangling file.py:LINE citations in docs/claims/claims.yaml.

Incident (GFLAG-0010, evidence/planning/governance_flags.v1.json, 2026-08-08):
SD-087/SD-020/SD-086 cited config.py:2306, agent.py:8636-8642, and
e3_selector.py:1038/:2766 -- all drifted 190-1150 lines from the real
locations, found only because a session happened to manually diff cited line
numbers against ree-v3 HEAD during an unrelated review. 73 `\\.py:\\d+`-style
citations exist across claims.yaml today; nothing validates any of them.

For each citation this resolves which sibling repo the file lives in (see
resolve_citation()), then flags:

  STALE      -- cited line number (or the end of a cited range) exceeds the
                file's current total line count at the resolved repo's HEAD.
                A citation cannot point past end-of-file; this is the one
                deterministic, zero-false-positive signal available without
                understanding what the cited line is supposed to say.
  MISSING    -- the named file does not exist (as a tracked file, at HEAD) in
                ANY known repo. Stronger signal than line-drift: the citation
                may be for a renamed/deleted/relocated file.
  AMBIGUOUS  -- the resolved repo has more than one tracked file matching the
                citation's name/suffix. Reported, not guessed.

WHAT THIS DOES NOT DO: it never inspects the CONTENT at the cited line. A
citation that is in-bounds (file exists, line exists) but now points at the
wrong function/branch/value -- content drift, not line-count drift -- is
invisible to this check by design; that needs semantic understanding this
tool is not attempting. It also does not check WORKSPACE_STATE.md or
governance_flags.v1.json notes -- scope is claims.yaml only, the confirmed
source of the incident. It does not catch a trailing comma-paired second line
number (`theta_buffer.py:146,159` -- only `146` is checked).

Resolves against each sibling repo's git HEAD (git ls-files + git show
<ref>:<path>), not the raw working tree -- matching the "the gate is on
COMMITTED content" convention (audit_worktree_skills.py) and the incident's
own framing ("diffed against ree-v3 HEAD"). This also sidesteps a confirmed
false-positive source: ree-v3 has git-ignored worktree mirrors under
.claude/worktrees/<slug>/... that a raw filesystem walk would double-count as
ambiguous matches; `git ls-files` excludes them for free.

Repo search order is fixed priority (see REPOS below); the first repo with
any tracked-file match wins, and AMBIGUOUS is scoped to multiple matches
WITHIN that one resolved repo -- not "exists in multiple sibling repos",
since several filenames here (agent.py, field.py, e3_selector.py) also exist
in legacy forks and counting cross-repo hits would drown the real signal.

Output: evidence/planning/citation_staleness.md. Warn-only by default (exit 0
regardless of findings, matching every check_*.py in this repo except the one
that earned gate status after a maturation period); --exit-nonzero to gate.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/check_citation_staleness.py
    /opt/local/bin/python3 scripts/check_citation_staleness.py --exit-nonzero
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UMBRELLA = ROOT.parent
CLAIMS_YAML = ROOT / "docs" / "claims" / "claims.yaml"
PLANNING = ROOT / "evidence" / "planning"
REPORT_PATH = PLANNING / "citation_staleness.md"

# Fixed priority order -- see module docstring for why cross-repo ambiguity
# is deliberately not counted.
REPOS = ("ree-v3", "REE_assembly", "ree-v2", "ree-v1-minimal")

CITATION_RE = re.compile(
    r"(?P<path>(?:[\w\-]+/)*[\w\-]+\.py):(?P<line>\d+)(?:-(?P<line_end>\d+))?")


def _git(repo: Path, *args: str) -> str:
    """Run git in `repo`; return stdout, or "" on failure (never raises)."""
    try:
        r = subprocess.run(("git", "-C", str(repo)) + args,
                           capture_output=True, text=True, check=False)
    except OSError:
        return ""
    return r.stdout if r.returncode == 0 else ""


def load_claims_yaml(path: Path) -> list:
    """Same pattern as check_backward_traceability.py's loader."""
    try:
        import yaml
    except ImportError:
        print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
        sys.exit(2)
    raw = path.read_text(encoding="utf-8")
    docs = list(yaml.safe_load_all(raw))
    claims = []
    for doc in docs:
        if isinstance(doc, list):
            claims.extend(doc)
        elif isinstance(doc, dict) and "id" in doc:
            claims.append(doc)
    return claims


def _iter_strings(value):
    """Yield every string leaf inside a nested dict/list/scalar structure.
    Matches check_dry_run_citations.py's own stated philosophy: the confirmed
    damage was a prose citation, not a schema field, so every string is a
    candidate rather than a named subset of fields."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from _iter_strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from _iter_strings(v)


def find_citations(claims: list):
    """[(claim_id, raw_citation, path, line, line_end)] across every string in
    every claim, in claims.yaml order."""
    out = []
    for claim in claims:
        cid = claim.get("id", "?") if isinstance(claim, dict) else "?"
        for text in _iter_strings(claim):
            for m in CITATION_RE.finditer(text):
                line_end = int(m.group("line_end")) if m.group("line_end") else None
                out.append((cid, m.group(0), m.group("path"), int(m.group("line")), line_end))
    return out


def _repo_index(repo_name: str):
    """basename -> [tracked relpaths], from `git ls-files` at HEAD. Cached per
    call site via the caller; empty on any failure (unknown/missing repo)."""
    repo_path = UMBRELLA / repo_name
    out = _git(repo_path, "ls-files", "--", "*.py")
    index = {}
    for relpath in out.splitlines():
        if not relpath:
            continue
        index.setdefault(Path(relpath).name, []).append(relpath)
    return index


def resolve_citation(raw_path: str, repo_indexes: dict):
    """Resolve a citation's path to (repo, relpath) or a (None, reason) verdict.

    Returns one of:
      ("resolved", repo, relpath)
      ("missing", None, None)
      ("ambiguous", repo, [candidates])
    An explicit `<repo>/...` prefix (matching a REPOS name) resolves ONLY
    within that repo -- no fallback to the search order.
    """
    parts = raw_path.split("/")
    explicit_repo = parts[0] if parts[0] in REPOS else None
    name = Path(raw_path).name

    search = (explicit_repo,) if explicit_repo else REPOS
    for repo in search:
        index = repo_indexes.get(repo, {})
        candidates = index.get(name, [])
        if not candidates:
            continue
        if explicit_repo:
            sub_path = "/".join(parts[1:])
            exact = [c for c in candidates if c == sub_path or c.endswith("/" + sub_path)]
            candidates = exact or candidates
        elif "/" in raw_path:
            # Path-qualified (not just a bare filename): match by trailing
            # segment equality, not raw endswith, to avoid a
            # notutils/config.py-style false suffix match.
            wanted = parts
            matching = [c for c in candidates
                       if c.split("/")[-len(wanted):] == wanted]
            if matching:
                candidates = matching
        if len(candidates) == 1:
            return "resolved", repo, candidates[0]
        if len(candidates) > 1:
            return "ambiguous", repo, candidates
        # len == 0 after filtering: fall through to next repo (unqualified case)
    return "missing", None, None


def file_line_count(repo_name: str, relpath: str, ref: str) -> int | None:
    """Line count of relpath at ref, or None if the object doesn't exist.

    `git show` prints "" both for a genuinely empty (0-line) file and for a
    missing object, so existence is checked separately via `cat-file -e`
    rather than inferred from emptiness.
    """
    repo_path = UMBRELLA / repo_name
    exists = subprocess.run(
        ("git", "-C", str(repo_path), "cat-file", "-e", "%s:%s" % (ref, relpath)),
        capture_output=True).returncode == 0
    if not exists:
        return None
    out = _git(repo_path, "show", "%s:%s" % (ref, relpath))
    return len(out.splitlines())


def audit(claims_yaml: Path = CLAIMS_YAML, repos=REPOS, ref: str = "HEAD"):
    claims = load_claims_yaml(claims_yaml)
    citations = find_citations(claims)
    repo_indexes = {repo: _repo_index(repo) for repo in repos}

    stale, missing, ambiguous = [], [], []
    for cid, raw, path, line, line_end in citations:
        status, repo, info = resolve_citation(path, repo_indexes)
        if status == "missing":
            missing.append((cid, raw, repos))
        elif status == "ambiguous":
            ambiguous.append((cid, raw, repo, info))
        else:
            relpath = info
            total = file_line_count(repo, relpath, ref)
            if total is None:
                missing.append((cid, raw, (repo,)))
                continue
            check_line = line_end or line
            if check_line > total:
                stale.append((cid, raw, repo, relpath, total))

    return {
        "citations_checked": len(citations),
        "stale": stale,
        "missing": missing,
        "ambiguous": ambiguous,
    }


def _table(rows, headers):
    if not rows:
        return "_None._\n"
    lines = ["| " + " | ".join(headers) + " |",
             "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(lines) + "\n"


def write_report(result: dict, path: Path = REPORT_PATH) -> None:
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        "# Citation Staleness Report",
        "",
        "Generated: %s" % now,
        "",
        "Warn-only (see check_citation_staleness.py's module docstring for "
        "what this does and does not detect). Citations checked: %d."
        % result["citations_checked"],
        "",
        "## Stale citations (%d)" % len(result["stale"]),
        "",
        _table([(cid, "`%s`" % raw, "%s/%s" % (repo, rel), total)
               for cid, raw, repo, rel, total in result["stale"]],
              ["claim_id", "citation", "resolved", "current EOF"]),
        "## Missing-file citations (%d)" % len(result["missing"]),
        "",
        _table([(cid, "`%s`" % raw, ", ".join(repos))
               for cid, raw, repos in result["missing"]],
              ["claim_id", "citation", "searched repos"]),
        "## Ambiguous citations (%d)" % len(result["ambiguous"]),
        "",
        _table([(cid, "`%s`" % raw, repo, ", ".join(cands))
               for cid, raw, repo, cands in result["ambiguous"]],
              ["claim_id", "citation", "repo", "candidates"]),
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    global UMBRELLA
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--claims-yaml", type=Path, default=CLAIMS_YAML)
    p.add_argument("--repos-root", type=Path, default=UMBRELLA)
    p.add_argument("--repos", type=str, default=None,
                   help="comma-separated override of the default search order")
    p.add_argument("--ref", type=str, default="HEAD")
    p.add_argument("--report", type=Path, default=REPORT_PATH)
    p.add_argument("--exit-nonzero", action="store_true",
                   help="exit 1 if any STALE/MISSING/AMBIGUOUS finding exists")
    args = p.parse_args()

    UMBRELLA = args.repos_root
    repos = tuple(args.repos.split(",")) if args.repos else REPOS

    result = audit(args.claims_yaml, repos, args.ref)
    write_report(result, args.report)

    n = len(result["stale"]) + len(result["missing"]) + len(result["ambiguous"])
    print("Citation staleness report written: %s" % args.report)
    print("  stale=%d  missing=%d  ambiguous=%d  citations_checked=%d"
          % (len(result["stale"]), len(result["missing"]), len(result["ambiguous"]),
             result["citations_checked"]))

    return 1 if (n and args.exit_nonzero) else 0


if __name__ == "__main__":
    raise SystemExit(main())
