#!/opt/local/bin/python3
"""Regression test: check_citation_staleness.py flags file.py:LINE citations
in claims.yaml that have drifted past end-of-file, are missing, or resolve
ambiguously -- against real git repos, not mocks.

Run: /opt/local/bin/python3 scripts/test_check_citation_staleness.py

THE GAP THIS PINS. Confirmed incident GFLAG-0010: citations like
`config.py:2306` drifted 190-1150 lines from the real location, found only by
a session manually diffing against ree-v3 HEAD during an unrelated review. No
automated validator existed. The load-bearing test here is the worktree-
mirror-exclusion regression: ree-v3 has git-ignored worktree mirrors that a
raw filesystem walk over the repo would double-count as ambiguous matches;
resolution must go through `git ls-files`, not `Path.glob`, or every common
filename in this codebase would spuriously flag AMBIGUOUS.

Module is loaded via importlib (matching this repo's test convention for
check_*.py scripts, e.g. test_check_substrate_staleness_candidates.py) rather
than a package import, since scripts/ is not a package.

ASCII-only. Exits 0 on pass.
"""
import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent / "check_citation_staleness.py"
_spec = importlib.util.spec_from_file_location("check_citation_staleness", SCRIPT_PATH)
ccs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ccs)


def _git(repo, *args):
    p = subprocess.run(["git", "-C", str(repo)] + list(args),
                       capture_output=True, text=True)
    assert p.returncode == 0, "git %s failed: %s" % (args, p.stderr)
    return p.stdout.strip()


def _git_repo(base: Path, name: str, files: dict) -> Path:
    """Create a real git repo at base/name with `files` (relpath -> content)
    committed. Returns the repo path."""
    repo = base / name
    repo.mkdir(parents=True)
    _git(repo, "init", "-q", ".")
    _git(repo, "config", "user.name", "Test Bot")
    _git(repo, "config", "user.email", "test@example.invalid")
    for relpath, content in files.items():
        p = repo / relpath
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        _git(repo, "add", relpath)
    _git(repo, "commit", "-q", "-m", "seed")
    return repo


def _lines(n: int) -> str:
    return "\n".join("line %d" % i for i in range(1, n + 1)) + "\n"


def _claims_yaml_text(entries: list) -> str:
    import yaml
    return yaml.safe_dump(entries, sort_keys=False)


class CheckCitationStalenessTest(unittest.TestCase):
    def setUp(self):
        self.base = Path(tempfile.mkdtemp(prefix="check_citation_staleness_test_"))
        self.addCleanup(shutil.rmtree, self.base, ignore_errors=True)
        self._patch(ccs, "UMBRELLA", self.base)

    def _patch(self, mod, attr, value):
        old = getattr(mod, attr)
        self.addCleanup(setattr, mod, attr, old)
        setattr(mod, attr, value)

    def _write_claims(self, entries) -> Path:
        p = self.base / "claims.yaml"
        p.write_text(_claims_yaml_text(entries))
        return p

    def _audit(self, entries, repos=("ree-v3", "REE_assembly")):
        claims_yaml = self._write_claims(entries)
        return ccs.audit(claims_yaml=claims_yaml, repos=repos, ref="HEAD")

    # --- stale / not-stale ----------------------------------------------

    def test_stale_bare_filename(self):
        _git_repo(self.base, "ree-v3", {"ree_core/utils/config.py": _lines(100)})
        result = self._audit([{"id": "SD-020", "notes": "config.py:150 says X"}])
        self.assertEqual(len(result["stale"]), 1)
        cid, raw, repo, relpath, total = result["stale"][0]
        self.assertEqual(cid, "SD-020")
        self.assertEqual(raw, "config.py:150")
        self.assertEqual(repo, "ree-v3")
        self.assertEqual(relpath, "ree_core/utils/config.py")
        self.assertEqual(total, 100)

    def test_not_stale_in_bounds(self):
        _git_repo(self.base, "ree-v3", {"ree_core/utils/config.py": _lines(100)})
        result = self._audit([{"id": "SD-020", "notes": "config.py:50 says X"}])
        self.assertEqual(result["stale"], [])
        self.assertEqual(result["missing"], [])
        self.assertEqual(result["ambiguous"], [])

    # --- resolution shapes ------------------------------------------------

    def test_path_qualified_match(self):
        _git_repo(self.base, "ree-v3", {"ree_core/utils/config.py": _lines(100)})
        result = self._audit([{"id": "SD-020",
                               "notes": "ree_core/utils/config.py:150 says X"}])
        self.assertEqual(len(result["stale"]), 1)
        self.assertEqual(result["stale"][0][3], "ree_core/utils/config.py")

    def test_repo_qualified_prefix_no_search_order_fallback(self):
        # agent.py exists in BOTH repos with different sizes; an explicit
        # ree-v3/ prefix must resolve only within ree-v3, not fall back.
        _git_repo(self.base, "ree-v3", {"ree_core/agent.py": _lines(20)})
        _git_repo(self.base, "REE_assembly", {"scripts/agent.py": _lines(9999)})
        result = self._audit(
            [{"id": "MECH-1", "notes": "ree-v3/ree_core/agent.py:9999 says X"}],
            repos=("ree-v3", "REE_assembly"))
        self.assertEqual(len(result["stale"]), 1)
        self.assertEqual(result["stale"][0][2], "ree-v3")
        self.assertEqual(result["stale"][0][3], "ree_core/agent.py")

    def test_missing_file(self):
        _git_repo(self.base, "ree-v3", {"ree_core/utils/config.py": _lines(100)})
        result = self._audit([{"id": "SD-020",
                               "notes": "nonexistent_module.py:10 says X"}])
        self.assertEqual(len(result["missing"]), 1)
        self.assertEqual(result["missing"][0][0], "SD-020")

    def test_ambiguous_within_one_repo(self):
        _git_repo(self.base, "ree-v3", {
            "ree_core/dup.py": _lines(10),
            "ree_core/other/dup.py": _lines(10),
        })
        result = self._audit([{"id": "SD-020", "notes": "dup.py:5 says X"}])
        self.assertEqual(len(result["ambiguous"]), 1)
        cid, raw, repo, candidates = result["ambiguous"][0]
        self.assertEqual(repo, "ree-v3")
        self.assertEqual(len(candidates), 2)
        self.assertEqual(result["stale"], [])
        self.assertEqual(result["missing"], [])

    def test_worktree_mirror_exclusion_regression(self):
        """THE CONCRETE PITFALL. A git-ignored, untracked copy sitting on disk
        under a worktree-mirror-shaped path must not create a false
        AMBIGUOUS -- resolution must use `git ls-files`, not a filesystem
        walk, since it would otherwise double-count it."""
        repo = _git_repo(self.base, "ree-v3", {"ree_core/utils/config.py": _lines(100)})
        mirror = repo / ".claude" / "worktrees" / "fake-session" / "ree_core" / "utils" / "config.py"
        mirror.parent.mkdir(parents=True)
        mirror.write_text(_lines(5))  # untracked, never git add-ed
        result = self._audit([{"id": "SD-020", "notes": "config.py:150 says X"}])
        self.assertEqual(len(result["stale"]), 1, "must resolve unambiguously via git ls-files")
        self.assertEqual(result["ambiguous"], [])

    def test_range_citation(self):
        _git_repo(self.base, "ree-v3", {"ree_core/field.py": _lines(100)})
        result = self._audit([{"id": "MECH-1", "notes": "field.py:95-105 covers this"}])
        self.assertEqual(len(result["stale"]), 1)
        self.assertEqual(result["stale"][0][1], "field.py:95-105")

    # --- attribution -----------------------------------------------------

    def test_claim_id_attribution_from_nested_field(self):
        _git_repo(self.base, "ree-v3", {"ree_core/utils/config.py": _lines(100)})
        result = self._audit([{
            "id": "SD-087",
            "evidence": [{"notes": "see config.py:150 for the write path"}],
        }])
        self.assertEqual(len(result["stale"]), 1)
        self.assertEqual(result["stale"][0][0], "SD-087")

    # --- CLI / exit code ---------------------------------------------------

    def test_exit_nonzero_flag(self):
        _git_repo(self.base, "ree-v3", {"ree_core/utils/config.py": _lines(100)})
        claims_yaml = self._write_claims([{"id": "SD-020", "notes": "config.py:150 says X"}])
        report = self.base / "report.md"

        old_argv = sys.argv
        sys.argv = ["check_citation_staleness.py", "--claims-yaml", str(claims_yaml),
                    "--repos-root", str(self.base), "--repos", "ree-v3",
                    "--report", str(report)]
        try:
            rc_default = ccs.main()
        finally:
            sys.argv = old_argv
        self.assertEqual(rc_default, 0, "warn-only by default")

        sys.argv = ["check_citation_staleness.py", "--claims-yaml", str(claims_yaml),
                    "--repos-root", str(self.base), "--repos", "ree-v3",
                    "--report", str(report), "--exit-nonzero"]
        try:
            rc_gate = ccs.main()
        finally:
            sys.argv = old_argv
        self.assertEqual(rc_gate, 1, "--exit-nonzero must gate on a real finding")
        self.assertTrue(report.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
