#!/usr/bin/env python3
"""
Pin: every test file in this repo is actually reachable by CI.

WHY THIS EXISTS. On 2026-07-27 the same defect was confirmed three times in one
day: a test file that no runner reaches, which therefore never runs, while
nothing fails and nothing warns.

  * REE_Working f3ed4eaf3b (ree-v3) -- scripts/remote_pytest.sh defaulted to
    `tests/`, collecting 2499 tests and ZERO of the 264 under coordinator/.
    Two regressions sat on trunk undetected for months.
  * REE_Working e2558ead00 (ree-v3) -- that fix named a second root and STILL
    missed four files (45 tests). Found only by re-auditing the first fix.
  * This repo -- 127 live tests across 7 files that nothing ran at all.

The lesson from the second recurrence is the one that matters, and it is not
"remember to add the path". `remote_pytest.sh --selftest` had been GREEN the
whole time those four files were stranded, because it pinned a hardcoded list
of roots and the list agreed with itself. It only became useful once it stopped
checking a list and started ENUMERATING the tree, failing on any collectable
file the runner could not reach. That is what this module does for CI.

WHAT IS AND IS NOT AT RISK HERE. `.github/workflows/tests.yml` runs a bare
`pytest` from the repo root with no path arguments, so collection cannot go
stale the way a path list can -- there is no list. Two things still can:

  1. The workflow's `paths:` TRIGGER filter. It is scoped so the continuous
     phase3 coordination-data commits do not each fire a CI run. A test file
     (or a subject under test) outside that filter is still collected when CI
     runs, but editing it no longer TRIGGERS CI -- so a change can break its
     own test and land green. This is the exact stale-list shape, one level up.
  2. A pytest config appearing later. `testpaths` in a new pytest.ini /
     pyproject.toml / setup.cfg / tox.ini would silently narrow the bare-root
     run back down. ree-v3 has no such config either, which is precisely why
     collection there was purely by path.

Stdlib-only, and runs under both pytest and `python3 scripts/test_ci_test_coverage_pin.py`.
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = REPO_ROOT / ".github" / "workflows" / "tests.yml"

# Mirrors the sweep exclusions in remote_pytest.sh's _selftest_default_args:
# nested worktrees under .claude are full repo copies (collecting those would
# double-run everything), and virtualenvs are not ours.
_EXCLUDE_PARTS = (".git", ".claude", ".venv", "node_modules", "__pycache__")


def _iter_test_files():
    for pat in ("test_*.py", "*_test.py"):
        for p in REPO_ROOT.rglob(pat):
            if any(part in _EXCLUDE_PARTS for part in p.parts):
                continue
            if p.is_file():
                yield p


def _glob_to_regex(glob: str) -> re.Pattern:
    """GitHub Actions path-filter glob -> regex.

    `**` spans directory separators, `*` and `?` do not. Written out rather
    than delegated to fnmatch because fnmatch's `*` matches `/`, which would
    make this pin far too permissive -- it would report coverage for paths the
    real filter does not match, i.e. fail open, which is the one thing a gate
    must never do.
    """
    out, i = [], 0
    while i < len(glob):
        c = glob[i]
        if c == "*":
            if glob[i:i + 2] == "**":
                out.append(".*")
                i += 2
                continue
            out.append("[^/]*")
        elif c == "?":
            out.append("[^/]")
        else:
            out.append(re.escape(c))
        i += 1
    return re.compile("^" + "".join(out) + "$")


def _workflow_trigger_globs():
    """Extract the `paths:` list under on.push from the workflow.

    Deliberately a small strict reader rather than a YAML dependency: the file
    is one we author and control, and a shape change SHOULD make this speak up.
    """
    assert WORKFLOW.exists(), f"missing CI workflow: {WORKFLOW}"
    lines = WORKFLOW.read_text(encoding="utf-8").splitlines()
    globs, in_paths, paths_indent = [], False, None
    for raw in lines:
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        stripped = line.strip()
        if stripped == "paths:":
            in_paths, paths_indent = True, indent
            continue
        if in_paths:
            if stripped.startswith("- ") and indent > paths_indent:
                globs.append(stripped[2:].strip().strip("'\""))
            else:
                in_paths = False
    assert globs, (
        f"found no `paths:` entries in {WORKFLOW.name}. Either the trigger "
        f"filter was removed (in which case delete this reader too) or the "
        f"workflow's shape changed and this pin can no longer see it."
    )
    return globs


def _subjects_of(test_path: Path):
    """Best-effort: the in-repo files a test file exercises.

    Resolved from the test's own text rather than a maintained map, for the
    same reason this module enumerates instead of listing: a hand-kept map is
    green while it is wrong. Two shapes, both used in this repo:
      * `import build_experiment_indexes as b` after a sys.path insert
      * `REPO_ROOT / "serve.py"` / spec_from_file_location on a .py literal
    Only names that resolve to a real file are returned, so third-party and
    stdlib imports fall away on their own.
    """
    text = test_path.read_text(encoding="utf-8")
    found = set()

    for name in re.findall(r"^\s*(?:import|from)\s+([A-Za-z_][A-Za-z0-9_]*)", text, re.M):
        for cand in (test_path.parent / f"{name}.py", REPO_ROOT / f"{name}.py"):
            if cand.is_file():
                found.add(cand)

    for literal in re.findall(r"[\"']([A-Za-z0-9_./-]+\.py)[\"']", text):
        for cand in (test_path.parent / literal, REPO_ROOT / literal):
            if cand.is_file():
                found.add(cand)

    found.discard(test_path)
    return found


def _covered(rel: str, patterns) -> bool:
    return any(p.match(rel) for p in patterns)


# --------------------------------------------------------------------------


def test_sweep_is_not_vacuous():
    """A pin that found nothing to check would pass forever, proving nothing."""
    files = list(_iter_test_files())
    assert files, (
        f"found NO test files under {REPO_ROOT}. The sweep is broken or the "
        f"repo path is wrong; every other assertion here would pass vacuously."
    )
    assert len(files) >= 5, f"only {len(files)} test file(s) found; expected >=5"


def test_every_test_file_triggers_ci():
    """Editing any test file must actually trigger the CI workflow."""
    patterns = [_glob_to_regex(g) for g in _workflow_trigger_globs()]
    stranded = []
    for p in _iter_test_files():
        rel = p.relative_to(REPO_ROOT).as_posix()
        if not _covered(rel, patterns):
            stranded.append(rel)
    assert not stranded, (
        "these test files are not matched by the `paths:` trigger filter in "
        ".github/workflows/tests.yml, so editing one would NOT run CI:\n  "
        + "\n  ".join(sorted(stranded))
        + "\nAdd the path (or its directory) to that filter."
    )


def test_every_subject_under_test_triggers_ci():
    """Editing a subject must trigger the test that covers it.

    The sharper half of the pin. A stranded TEST file is at least visible when
    someone edits it; a stranded SUBJECT means a change to production code
    lands without running the test written for it, which is how the ree-v3
    coordinator regressions survived on trunk. serve.py sits at the repo root
    and is only in the filter because test_coord_snap_cache.py exercises it.
    """
    patterns = [_glob_to_regex(g) for g in _workflow_trigger_globs()]
    stranded = {}
    for p in _iter_test_files():
        for subject in _subjects_of(p):
            rel = subject.relative_to(REPO_ROOT).as_posix()
            if not _covered(rel, patterns):
                stranded.setdefault(rel, []).append(
                    p.relative_to(REPO_ROOT).as_posix()
                )
    assert not stranded, (
        "these files are exercised by a test but are not matched by the "
        "`paths:` trigger filter in .github/workflows/tests.yml, so editing "
        "one would NOT run the test that covers it:\n  "
        + "\n  ".join(f"{k}  (tested by {', '.join(v)})"
                      for k, v in sorted(stranded.items()))
        + "\nAdd the path (or its directory) to that filter."
    )


def test_no_pytest_config_narrows_bare_root_collection():
    """The workflow passes no paths, which is only safe while nothing narrows.

    `testpaths` in any of these would silently shrink the bare-root run back to
    a path list -- reintroducing the ree-v3 failure mode without touching the
    workflow at all.
    """
    offenders = []
    for name in ("pytest.ini", "pyproject.toml", "setup.cfg", "tox.ini"):
        cfg = REPO_ROOT / name
        if not cfg.is_file():
            continue
        text = cfg.read_text(encoding="utf-8")
        if re.search(r"^\s*testpaths\s*[=:]", text, re.M):
            offenders.append(name)
    assert not offenders, (
        f"{', '.join(offenders)} now declare(s) `testpaths`, which narrows the "
        f"bare `pytest` run in .github/workflows/tests.yml to a path list. "
        f"Either drop testpaths, or make the workflow pass explicit paths AND "
        f"extend this pin to check them against the tree (see the "
        f"_selftest_default_args pattern in scripts/remote_pytest.sh)."
    )


def test_workflow_runs_pytest_without_path_arguments():
    """Guards the 'no list can go stale because there is no list' property."""
    text = WORKFLOW.read_text(encoding="utf-8")
    runs = re.findall(r"^\s*run:\s*(.*(?:pytest).*)$", text, re.M)
    assert runs, f"{WORKFLOW.name} does not appear to run pytest at all"
    bare = [
        r for r in runs
        if re.search(r"pytest(\s+-[^\s]+)*\s*$", r.strip())
        or re.search(r"pytest\s+(-\S+\s*)*(-q|-p\s+\S+)", r.strip())
    ]
    assert bare, (
        "no pytest invocation in the workflow looks path-argument-free. If a "
        "path list was added deliberately, extend this pin to assert every "
        "test file in the tree is reachable from it -- do not just delete "
        "this check, which is what left four ree-v3 files stranded."
    )


ALL_TESTS = [
    test_sweep_is_not_vacuous,
    test_every_test_file_triggers_ci,
    test_every_subject_under_test_triggers_ci,
    test_no_pytest_config_narrows_bare_root_collection,
    test_workflow_runs_pytest_without_path_arguments,
]


def main():
    failed = 0
    for t in ALL_TESTS:
        try:
            t()
            print(f"PASS  {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {t.__name__}\n      {e}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"ERROR {t.__name__}\n      {type(e).__name__}: {e}")
    print(f"\n{len(ALL_TESTS) - failed}/{len(ALL_TESTS)} checks passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
