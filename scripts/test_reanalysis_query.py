#!/usr/bin/env python3
"""Tests for scripts/reanalysis_query.py's `query` subcommand.

Regression cover for the scanned-vs-matched count defect (reported
2026-09-22 by session inv023-science-20260922 during a GOV-REUSE-1
not-recoverable check): `cmd_query` used to reassign its `rows` variable to
the POST-filter list (`rows = [s for s in rows if keep(s)]`) and then print
`len(rows)` as "scanned N manifests" -- so a `--claim` filter that
legitimately matches nothing printed byte-identically to a broken or empty
scan root ("scanned 0 manifests" either way). GOV-REUSE-1 exists to
establish NEGATIVES ("no prior run covers this claim"); an instrument that
cannot distinguish "nothing matched" from "nothing was looked at" cannot
establish one. The session nearly discarded a valid result over this.

THE MUTATION CHECK IS THE POINT (mirrors test_check_manifest_degeneracy_
consistency.py's own framing): TestScannedVsMatchedCount.
test_the_two_cases_are_distinguishable_on_scanned_count asserts on the
`n_manifests_scanned` FIGURE differing between the two cases, not merely on
the printed text differing -- so a future revert to `len(rows)` (the
post-filter count) collapses both cases back to 0 and this test fails,
exactly as it should.

Isolated from the live `evidence/experiments/` tree (1061 manifests there
today -- slow, and couples this test to production data): every fixture is
written to a tempdir, and `EXPERIMENTS_DIR` is monkeypatched onto the module
for the duration of each test, restored in cleanup.

Run:
    /opt/local/bin/python3 scripts/test_reanalysis_query.py
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import reanalysis_query as mod  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]


# ----------------------------------------------------------------------------
# fixture / invocation helpers
# ----------------------------------------------------------------------------
def _write_manifest(dirpath: Path, run_id: str, claim_ids=None, **extra) -> Path:
    manifest = {
        "run_id": run_id,
        "claim_ids": claim_ids or [],
        "outcome": "PASS",
        "experiment_purpose": "evidence",
        "machine_class": "mac",
        **extra,
    }
    path = dirpath / f"{run_id}.json"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    return path


def _query_args(claim=None, purpose=None, readout=None, substrate_hash=None,
                 require_readout=False, as_json=False) -> argparse.Namespace:
    return argparse.Namespace(
        claim=claim, purpose=purpose, readout=readout,
        substrate_hash=substrate_hash, require_readout=require_readout,
        json=as_json,
    )


def _run_query_text(**kw) -> str:
    args = _query_args(as_json=False, **kw)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = mod.cmd_query(args)
    assert rc == 0, f"cmd_query returned {rc}"
    return buf.getvalue()


def _run_query_json(**kw) -> dict:
    args = _query_args(as_json=True, **kw)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = mod.cmd_query(args)
    assert rc == 0, f"cmd_query returned {rc}"
    return json.loads(buf.getvalue())


class Harness(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self._orig_experiments_dir = mod.EXPERIMENTS_DIR
        self.addCleanup(self._restore_experiments_dir)

    def _restore_experiments_dir(self):
        mod.EXPERIMENTS_DIR = self._orig_experiments_dir

    def use_root(self, path) -> None:
        mod.EXPERIMENTS_DIR = str(path)


# ----------------------------------------------------------------------------
# (1) the regression guard
# ----------------------------------------------------------------------------
class TestScannedVsMatchedCount(Harness):
    """Case (a): valid root, --claim matches nothing -> scanned = TRUE total.
    Case (b): broken/nonexistent scan root -> scanned = 0.
    Both cases have n_matched == 0; only the scanned figure must tell them
    apart. reanalysis_query.py has no --root flag (EXPERIMENTS_DIR is
    resolved from the script's own path), so "broken scan root" is simulated
    the way it happens for real -- a mis-homed checkout resolving to a
    directory that does not exist -- by pointing EXPERIMENTS_DIR elsewhere.
    """

    def test_valid_root_zero_match_claim_filter_reports_true_total(self):
        for i in range(3):
            _write_manifest(self.tmp, f"run_{i}", claim_ids=["MECH-1"])
        self.use_root(self.tmp)

        data = _run_query_json(claim="ZZZ-NONEXISTENT-9999")
        self.assertEqual(data["n_manifests_scanned"], 3)
        self.assertEqual(data["n_manifests_after_claim_purpose_filter"], 0)
        self.assertEqual(data["n_matched"], 0)

    def test_broken_scan_root_scanned_is_zero(self):
        broken = self.tmp / "does_not_exist"
        self.use_root(broken)

        data = _run_query_json(claim="ZZZ-NONEXISTENT-9999")
        self.assertEqual(data["n_manifests_scanned"], 0)
        self.assertEqual(data["n_manifests_after_claim_purpose_filter"], 0)
        self.assertEqual(data["n_matched"], 0)

    def test_the_two_cases_are_distinguishable_on_scanned_count(self):
        """THE MUTATION CHECK. Assert on the FIGURE, not the text: if
        cmd_query ever again reports the post-filter count as "scanned",
        both cases collapse to n_manifests_scanned == 0 and this fails."""
        for i in range(5):
            _write_manifest(self.tmp, f"run_{i}", claim_ids=["MECH-1"])
        self.use_root(self.tmp)
        valid_root = _run_query_json(claim="ZZZ-NONEXISTENT-9999")

        broken = self.tmp / "does_not_exist"
        self.use_root(broken)
        broken_root = _run_query_json(claim="ZZZ-NONEXISTENT-9999")

        self.assertEqual(valid_root["n_matched"], 0)
        self.assertEqual(broken_root["n_matched"], 0)
        self.assertNotEqual(
            valid_root["n_manifests_scanned"], broken_root["n_manifests_scanned"],
            "scanned counts must differ: a genuine zero-match filter against "
            "a real scan root is not the same observation as a broken one")
        self.assertEqual(valid_root["n_manifests_scanned"], 5)
        self.assertEqual(broken_root["n_manifests_scanned"], 0)

    def test_text_output_reports_both_numbers_distinctly(self):
        for i in range(4):
            _write_manifest(self.tmp, f"run_{i}", claim_ids=["MECH-1"])
        self.use_root(self.tmp)

        text = _run_query_text(claim="ZZZ-NONEXISTENT-9999")
        self.assertIn("scanned 4 manifests", text)
        self.assertIn("0 matched the filters", text)

    def test_matched_count_reflects_a_real_hit(self):
        _write_manifest(self.tmp, "run_hit", claim_ids=["MECH-1"])
        _write_manifest(self.tmp, "run_miss", claim_ids=["MECH-2"])
        self.use_root(self.tmp)

        data = _run_query_json(claim="MECH-1")
        self.assertEqual(data["n_manifests_scanned"], 2)
        self.assertEqual(data["n_manifests_after_claim_purpose_filter"], 1)
        self.assertEqual(data["n_matched"], 1)

    def test_require_readout_narrows_matched_below_filter_count(self):
        """Three distinct stages: scanned >= after-filter >= matched."""
        _write_manifest(self.tmp, "run_a", claim_ids=["MECH-1"], some_metric_x=1.0)
        _write_manifest(self.tmp, "run_b", claim_ids=["MECH-1"])
        self.use_root(self.tmp)

        data = _run_query_json(claim="MECH-1", readout="metric_x",
                                require_readout=True)
        self.assertEqual(data["n_manifests_scanned"], 2)
        self.assertEqual(data["n_manifests_after_claim_purpose_filter"], 2)
        self.assertEqual(data["n_matched"], 1)


# ----------------------------------------------------------------------------
# (2) ASCII-only stdout (repo convention)
# ----------------------------------------------------------------------------
class TestAsciiOutput(unittest.TestCase):
    def test_source_files_are_ascii(self):
        for name in ("reanalysis_query.py", "test_reanalysis_query.py"):
            text = (REPO_ROOT / "scripts" / name).read_text(encoding="utf-8")
            for i, line in enumerate(text.splitlines(), 1):
                try:
                    line.encode("ascii")
                except UnicodeEncodeError:
                    self.fail(f"{name}:{i} non-ASCII: {line!r}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
