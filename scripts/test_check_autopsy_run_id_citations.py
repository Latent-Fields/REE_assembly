#!/usr/bin/env python3
"""Regression tests for check_autopsy_run_id_citations.py.

Hermetic: every test builds a tmp evidence/experiments + evidence/planning tree
and points the module's parameterisable functions (and main() via
--evidence-dir/--planning-dir) at it, so nothing depends on the real evidence
tree. Covers the three manifest-location conventions, the WARN-only-vs-gate exit
contract, the null/missing run_id skip, confirmed-only corpus scoping, glob-safe
resolution of prose 'run_ids', and -- pinned as the concrete regression -- the
2026-08-08 round-4 397d truncated-timestamp defect (the correct run_id resolves,
the 8-character-short one does not).

Run: /opt/local/bin/python3 scripts/test_check_autopsy_run_id_citations.py
"""

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent


def _load_module(name, filename):
    path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


M = _load_module("ree_check_autopsy_run_id_citations",
                 "check_autopsy_run_id_citations.py")

# A real, correctly-formed run_id and the round-4 truncated defect for the same
# experiment (timestamp 202213Z clipped to just the date-T stem).
REAL_397D = "v3_exq_397d_arc007_matched_endpoint_20260423T202213Z_v3"
TRUNC_397D = "v3_exq_397d_arc007_matched_endpoint_20260423T_v3"
FLAT_RID = "v3_exq_500_flatform_20260501T010101Z_v3"
DIRECT_RID = "v3_exq_501_directpack_20260502T020202Z_v3"


def _write_manifest(path, run_id):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"run_id": run_id, "outcome": "FAIL"}))


def _write_autopsy(path, status, run_ids):
    targets = []
    for rid in run_ids:
        targets.append({"run_id": rid} if rid is not None else {"claim_ids": ["X-1"]})
    path.write_text(json.dumps({"status": status, "targets": targets}))


class Fixture:
    """A tmp evidence tree with all three manifest conventions populated."""

    def __init__(self, root):
        self.root = root
        self.evidence = root / "evidence" / "experiments"
        self.planning = root / "evidence" / "planning"
        self.evidence.mkdir(parents=True)
        self.planning.mkdir(parents=True)
        # run-pack manifest.json convention
        _write_manifest(self.evidence / "v3_exq_397d_arc007_matched_endpoint"
                        / "runs" / REAL_397D / "manifest.json", REAL_397D)
        # flat <run_id>.json convention
        _write_manifest(self.evidence / (FLAT_RID + ".json"), FLAT_RID)
        # run-pack direct <run_id>.json convention
        _write_manifest(self.evidence / "v3_exq_501_directpack"
                        / "runs" / (DIRECT_RID + ".json"), DIRECT_RID)


class ResolveTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.fx = Fixture(Path(self.tmp.name))

    def tearDown(self):
        self.tmp.cleanup()

    def test_flat_form_resolves(self):
        self.assertIsNotNone(M.resolve_run_id(FLAT_RID, self.fx.evidence))

    def test_runpack_manifest_form_resolves(self):
        p = M.resolve_run_id(REAL_397D, self.fx.evidence)
        self.assertIsNotNone(p)
        self.assertEqual(p.name, "manifest.json")

    def test_runpack_direct_form_resolves(self):
        p = M.resolve_run_id(DIRECT_RID, self.fx.evidence)
        self.assertIsNotNone(p)
        self.assertEqual(p.name, DIRECT_RID + ".json")

    def test_absent_run_id_unresolved(self):
        self.assertIsNone(
            M.resolve_run_id("v3_exq_999_nonexistent_20260101T000000Z_v3",
                             self.fx.evidence))

    def test_truncated_397d_defect_unresolved(self):
        # The pinned regression: the correct id resolves, the clipped one does not.
        self.assertIsNotNone(M.resolve_run_id(REAL_397D, self.fx.evidence))
        self.assertIsNone(M.resolve_run_id(TRUNC_397D, self.fx.evidence))

    def test_prose_run_id_is_glob_safe(self):
        # 'targets[].run_id' has held prose with parens/colons/spaces/brackets;
        # resolution must return None, never raise or match by glob accident.
        for junk in ["v3_exq_396a_arc016_precision_sweep (3 runs: a, b)",
                     "v3_exq_543_family_17_runs",
                     "v3_exq_*_glob_[abc]?",
                     "has/a/slash_20260101T000000Z_v3"]:
            self.assertIsNone(M.resolve_run_id(junk, self.fx.evidence), junk)


class CitedRunIdsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.fx = Fixture(Path(self.tmp.name))

    def tearDown(self):
        self.tmp.cleanup()

    def test_skips_null_and_missing_run_id(self):
        ap = self.fx.planning / "failure_autopsy_a.json"
        _write_autopsy(ap, "confirmed", [REAL_397D, None, "", 123])
        # helper is called via json directly; forge the mixed-type case by hand
        ap.write_text(json.dumps({"status": "confirmed", "targets": [
            {"run_id": REAL_397D}, {"run_id": None}, {"run_id": ""},
            {"run_id": 123}, {"claim_ids": ["X"]}]}))
        status, rids = M.cited_run_ids(ap, confirmed_only=True)
        self.assertEqual(status, "confirmed")
        self.assertEqual(rids, [REAL_397D])

    def test_confirmed_only_skips_non_confirmed(self):
        ap = self.fx.planning / "failure_autopsy_b.json"
        _write_autopsy(ap, "proposed", [REAL_397D])
        status, rids = M.cited_run_ids(ap, confirmed_only=True)
        self.assertEqual(status, "proposed")
        self.assertIsNone(rids)  # not scanned

    def test_non_confirmed_scanned_when_flag_off(self):
        ap = self.fx.planning / "failure_autopsy_c.json"
        _write_autopsy(ap, "proposed", [REAL_397D])
        status, rids = M.cited_run_ids(ap, confirmed_only=False)
        self.assertEqual(rids, [REAL_397D])


class ScanTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.fx = Fixture(Path(self.tmp.name))

    def tearDown(self):
        self.tmp.cleanup()

    def test_positive_control_all_resolve(self):
        ap = self.fx.planning / "failure_autopsy_good.json"
        _write_autopsy(ap, "confirmed", [REAL_397D, FLAT_RID, DIRECT_RID])
        f = M.scan_file(ap, self.fx.evidence)
        self.assertTrue(f["scanned"])
        self.assertEqual(f["unresolved"], [])
        self.assertEqual(len(f["resolved"]), 3)

    def test_negative_control_fabricated_flagged(self):
        ap = self.fx.planning / "failure_autopsy_bad.json"
        fake = "v3_exq_288_q034_monostrategy_lock_1775783647_v3"
        _write_autopsy(ap, "confirmed", [REAL_397D, fake])
        f = M.scan_file(ap, self.fx.evidence)
        self.assertEqual(f["unresolved"], [fake])
        self.assertEqual(f["resolved"], [REAL_397D])

    def test_truncation_defect_flagged_in_scan(self):
        ap = self.fx.planning / "failure_autopsy_r4.json"
        _write_autopsy(ap, "confirmed", [TRUNC_397D])
        f = M.scan_file(ap, self.fx.evidence)
        self.assertIn(TRUNC_397D, f["unresolved"])

    def test_corpus_scans_only_confirmed(self):
        _write_autopsy(self.fx.planning / "failure_autopsy_x.json",
                       "confirmed", [TRUNC_397D])
        _write_autopsy(self.fx.planning / "failure_autopsy_y.json",
                       "proposed", [TRUNC_397D])
        findings = M.scan_corpus(self.fx.planning, self.fx.evidence)
        self.assertEqual(len(findings), 1)  # only the confirmed one
        self.assertIn(TRUNC_397D, findings[0]["unresolved"])


class QueueStemTest(unittest.TestCase):
    def test_stem_forms(self):
        self.assertEqual(M._queue_stem("V3-EXQ-397d"), "v3_exq_397d_")
        self.assertEqual(M._queue_stem("EXQ-141"), "exq_141_")
        self.assertIsNone(M._queue_stem("not-a-queue-id"))


class MainExitTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.fx = Fixture(Path(self.tmp.name))

    def tearDown(self):
        self.tmp.cleanup()

    def _run(self, extra):
        argv = ["--evidence-dir", str(self.fx.evidence),
                "--planning-dir", str(self.fx.planning)] + extra
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = M.main(argv)
        return rc, buf.getvalue()

    def test_warn_only_default_is_zero_even_with_unresolved(self):
        _write_autopsy(self.fx.planning / "failure_autopsy_x.json",
                       "confirmed", [TRUNC_397D])
        rc, out = self._run([])
        self.assertEqual(rc, 0)
        self.assertIn("UNRESOLVED", out)
        self.assertIn(TRUNC_397D, out)

    def test_exit_nonzero_flag_is_one_on_finding(self):
        _write_autopsy(self.fx.planning / "failure_autopsy_x.json",
                       "confirmed", [TRUNC_397D])
        rc, _ = self._run(["--exit-nonzero"])
        self.assertEqual(rc, 1)

    def test_clean_corpus_is_zero_even_with_gate(self):
        _write_autopsy(self.fx.planning / "failure_autopsy_ok.json",
                       "confirmed", [REAL_397D, FLAT_RID])
        rc, out = self._run(["--exit-nonzero"])
        self.assertEqual(rc, 0)
        self.assertNotIn("UNRESOLVED", out)

    def test_bare_run_id_arg_resolution(self):
        rc, out = self._run([REAL_397D])
        self.assertEqual(rc, 0)
        self.assertNotIn("UNRESOLVED", out)
        rc, out = self._run(["--exit-nonzero", TRUNC_397D])
        self.assertEqual(rc, 1)
        self.assertIn(TRUNC_397D, out)

    def test_ascii_only_output(self):
        _write_autopsy(self.fx.planning / "failure_autopsy_x.json",
                       "confirmed", [TRUNC_397D])
        _, out = self._run([])
        out.encode("ascii")  # raises UnicodeEncodeError if any non-ASCII leaked


if __name__ == "__main__":
    unittest.main(verbosity=2)
