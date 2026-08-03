#!/usr/bin/env python3
"""Contract tests for check_substrate_staleness_candidates.py (Phase 0 drift-candidate report).

Design plan: REE_assembly/evidence/planning/substrate_stability_and_drift_detection_plan.md

Unit tests cover the pure filtering helpers (_is_dry_run, _already_actioned,
load_flat_claim_tagged_manifests, _display_path). The end-to-end test builds REAL git repos
in a tempdir (a bare "origin" + a local clone standing in for the ree-v3 checkout) and copies
the ACTUAL ree-v3/experiments/_lib/arm_fingerprint.py into the fixture tree, so the test
exercises the real compute_substrate_hash rather than a reimplementation -- proving the
script's own selling point (never reimplement the hash algorithm) is true in practice, not
just asserted in a docstring.

Run: /opt/local/bin/python3 scripts/test_check_substrate_staleness_candidates.py
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]  # REE_assembly root
SCRIPT_PATH = REPO_ROOT / "scripts" / "check_substrate_staleness_candidates.py"
REAL_ARM_FINGERPRINT = REPO_ROOT.parent / "ree-v3" / "experiments" / "_lib" / "arm_fingerprint.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("check_substrate_staleness_candidates", SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["check_substrate_staleness_candidates"] = mod
    spec.loader.exec_module(mod)
    return mod


MOD = _load_module()


def _run(cmd, cwd=None):
    proc = subprocess.run(cmd, cwd=str(cwd) if cwd else None, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} failed: {proc.stderr}")
    return proc.stdout


def _git(repo, *args):
    return _run(["git"] + list(args), cwd=repo)


class IsDryRunTests(unittest.TestCase):
    def test_bool_true(self):
        self.assertTrue(MOD._is_dry_run({"dry_run": True}))

    def test_bool_false(self):
        self.assertFalse(MOD._is_dry_run({"dry_run": False}))

    def test_truthy_string(self):
        for s in ("true", "True", "1", "yes"):
            self.assertTrue(MOD._is_dry_run({"dry_run": s}), s)

    def test_falsey_string_and_absent(self):
        self.assertFalse(MOD._is_dry_run({"dry_run": "false"}))
        self.assertFalse(MOD._is_dry_run({}))


class AlreadyActionedTests(unittest.TestCase):
    def test_none_set(self):
        self.assertFalse(MOD._already_actioned({"claim_ids": ["X"]}))

    def test_superseded_direction(self):
        self.assertTrue(MOD._already_actioned({"evidence_direction": "superseded"}))

    def test_pending_retest_bool(self):
        self.assertTrue(MOD._already_actioned({"pending_retest_after_substrate": True}))
        self.assertFalse(MOD._already_actioned({"pending_retest_after_substrate": False}))

    def test_superseded_by_substrate_string(self):
        self.assertTrue(MOD._already_actioned({"superseded_by_substrate": "SD-070@2026-08-01"}))
        self.assertFalse(MOD._already_actioned({"superseded_by_substrate": ""}))

    def test_per_claim_list(self):
        self.assertTrue(MOD._already_actioned({"pending_retest_after_substrate_per_claim": ["MECH-1"]}))
        self.assertFalse(MOD._already_actioned({"pending_retest_after_substrate_per_claim": []}))

    def test_per_claim_dict(self):
        self.assertTrue(MOD._already_actioned({"superseded_by_substrate_per_claim": {"MECH-1": "SD-1@2026-01-01"}}))
        self.assertFalse(MOD._already_actioned({"superseded_by_substrate_per_claim": {}}))


class LoadFlatManifestsTests(unittest.TestCase):
    def test_filters_correctly(self):
        with tempfile.TemporaryDirectory() as d:
            exp_dir = Path(d)
            (exp_dir / "claim_tagged.json").write_text(json.dumps({"claim_ids": ["MECH-1"], "run_id": "a"}))
            (exp_dir / "no_claim.json").write_text(json.dumps({"claim_ids": [], "run_id": "b"}))
            (exp_dir / "dry_run.json").write_text(json.dumps({"claim_ids": ["MECH-2"], "dry_run": True, "run_id": "c"}))
            (exp_dir / "malformed.json").write_text("{not json")
            (exp_dir / "subdir").mkdir()
            (exp_dir / "subdir" / "nested.json").write_text(json.dumps({"claim_ids": ["MECH-3"]}))

            out = MOD.load_flat_claim_tagged_manifests(exp_dir)
            run_ids = sorted(m.get("run_id") for _, m in out)
            self.assertEqual(run_ids, ["a"])  # no_claim, dry_run, malformed, nested all excluded


class DisplayPathTests(unittest.TestCase):
    def test_relative_to_umbrella_root(self):
        p = REPO_ROOT / "evidence" / "experiments" / "foo.json"
        shown = MOD._display_path(p)
        self.assertFalse(shown.startswith("/"))
        self.assertIn("REE_assembly", shown)

    def test_falls_back_to_absolute_outside_umbrella(self):
        p = Path("/tmp/totally/unrelated/path.json")
        self.assertEqual(MOD._display_path(p), str(p))


@unittest.skipUnless(REAL_ARM_FINGERPRINT.exists(), "real ree-v3 checkout not present")
class EndToEndDetectionTests(unittest.TestCase):
    """Real git repos in a tempdir; copies the REAL arm_fingerprint.py so the hash comparison
    exercises the actual function this script depends on, not a stand-in."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.bare = self.root / "origin.git"
        self.clone = self.root / "ree-v3-clone"
        self.exp_dir = self.root / "evidence_experiments"
        self.exp_dir.mkdir()

        _run(["git", "init", "--bare", "-b", "main", str(self.bare)])

        seed = self.root / "seed"
        seed.mkdir()
        _git(seed, "init", "-b", "main")
        _git(seed, "config", "user.email", "test@example.com")
        _git(seed, "config", "user.name", "Test")

        (seed / "experiments" / "_lib").mkdir(parents=True)
        (seed / "ree_core").mkdir()
        shutil.copy(REAL_ARM_FINGERPRINT, seed / "experiments" / "_lib" / "arm_fingerprint.py")
        (seed / "ree_core" / "foo.py").write_text("VALUE = 1\n")
        _git(seed, "add", "-A")
        _git(seed, "commit", "-m", "commit A -- initial substrate")
        commit_a = _git(seed, "rev-parse", "HEAD").strip()

        (seed / "ree_core" / "foo.py").write_text("VALUE = 2\n")
        _git(seed, "add", "-A")
        _git(seed, "commit", "-m", "commit B -- substrate changed")
        commit_b = _git(seed, "rev-parse", "HEAD").strip()

        _git(seed, "remote", "add", "origin", str(self.bare))
        _git(seed, "push", "origin", "main")

        _run(["git", "clone", str(self.bare), str(self.clone)])

        # Compute the REAL hash at each commit via a throwaway worktree per commit,
        # using the actual compute_substrate_hash -- never reimplemented here either.
        self.hash_a = self._real_hash_at(seed, commit_a)
        self.hash_b = self._real_hash_at(seed, commit_b)
        self.assertNotEqual(self.hash_a, self.hash_b, "fixture commits must differ in substrate")

        self.commit_a = commit_a
        self.commit_b = commit_b

        def manifest(name, **fields):
            (self.exp_dir / f"{name}.json").write_text(json.dumps(fields))

        manifest("current_run", claim_ids=["TEST-CURRENT"], run_id="current_run",
                  substrate_hash=self.hash_b, substrate_commit={"commit": commit_b})
        manifest("stale_run", claim_ids=["TEST-STALE"], run_id="stale_run",
                  substrate_hash=self.hash_a, substrate_commit={"commit": commit_a})
        manifest("actioned_run", claim_ids=["TEST-ACTIONED"], run_id="actioned_run",
                  substrate_hash=self.hash_a, substrate_commit={"commit": commit_a},
                  pending_retest_after_substrate=True)
        manifest("no_identity_run", claim_ids=["TEST-NOID"], run_id="no_identity_run")

    def _real_hash_at(self, seed_repo, commit):
        with tempfile.TemporaryDirectory() as wtdir:
            wt = Path(wtdir) / "wt"
            _git(seed_repo, "worktree", "add", "--detach", str(wt), commit)
            try:
                spec = importlib.util.spec_from_file_location(
                    "arm_fp_fixture", wt / "experiments" / "_lib" / "arm_fingerprint.py")
                m = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(m)
                return m.compute_substrate_hash(repo_root=wt)["substrate_hash"]
            finally:
                _git(seed_repo, "worktree", "remove", "--force", str(wt))

    def tearDown(self):
        self._tmp.cleanup()

    def test_end_to_end_buckets(self):
        buf = io.StringIO()
        argv = [
            "check_substrate_staleness_candidates.py",
            "--exp-dir", str(self.exp_dir),
            "--ree-v3-root", str(self.clone),
            "--ref", "origin/main",
        ]
        old_argv = sys.argv
        sys.argv = argv
        try:
            with contextlib.redirect_stdout(buf):
                rc = MOD.main()
        finally:
            sys.argv = old_argv
        self.assertEqual(rc, 0)
        out = buf.getvalue()

        self.assertIn("1  current (matches origin/main)", out)
        self.assertIn("1  already actioned", out)
        self.assertIn("1  no substrate identity recorded", out)
        self.assertIn("1  DRIFT CANDIDATE", out)
        self.assertIn("TEST-STALE", out)
        self.assertNotIn("TEST-CURRENT (", out)
        self.assertNotIn("TEST-ACTIONED (", out)
        self.assertIn("stale_run", out)
        self.assertIn("ree_core/foo.py", out)  # named in the changed-files diff

        # No leftover worktree from the run under test.
        listing = _git(self.clone, "worktree", "list")
        self.assertEqual(listing.count("\n"), 1, listing)


if __name__ == "__main__":
    unittest.main()
