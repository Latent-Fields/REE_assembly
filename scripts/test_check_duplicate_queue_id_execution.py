#!/usr/bin/env python3
"""Regression tests for check_duplicate_queue_id_execution.py.

Hermetic: scan() is exercised against a tmp evidence/experiments tree, never
the real corpus -- so these tests do not drift as the real corpus grows. One
separate, best-effort test re-runs scan() against the REAL evidence dir
(skipped if absent, e.g. staged remote-worker tree runs that exclude
evidence/ -- see CLAUDE.md "Running the test suite") and pins it to the
current known-baseline set, so a genuine corpus change is visible without
being load-bearing for the hermetic suite.

Run: /opt/local/bin/python3 scripts/test_check_duplicate_queue_id_execution.py
"""

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent


def _load_module(name, filename):
    path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


M = _load_module(
    "ree_check_duplicate_queue_id_execution",
    "check_duplicate_queue_id_execution.py",
)


def _write_manifest(path, queue_id=None, run_id=None, machine=None,
                     evidence_direction=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = {"outcome": "PASS"}
    if queue_id is not None:
        doc["queue_id"] = queue_id
    if run_id is not None:
        doc["run_id"] = run_id
    if machine is not None:
        doc["machine"] = machine
    if evidence_direction is not None:
        doc["evidence_direction"] = evidence_direction
    path.write_text(json.dumps(doc))


class ScanTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.evidence = self.root / "evidence" / "experiments"
        self.evidence.mkdir(parents=True)

    def test_scan_finds_the_v3_exq_861f_shape(self):
        # Same queue_id, two machines, both PASS -- the confirmed incident.
        _write_manifest(
            self.evidence / "run_dlaptop.json",
            queue_id="V3-EXQ-861f",
            run_id="v3_exq_861f_..._20260824T023853Z_v3",
            machine="DLAPTOP-4.local",
        )
        _write_manifest(
            self.evidence / "run_cloud4.json",
            queue_id="V3-EXQ-861f",
            run_id="v3_exq_861f_..._20260823T210058Z_v3",
            machine="ree-cloud-4",
        )
        findings = M.scan(self.evidence, self.root)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["queue_id"], "V3-EXQ-861f")
        self.assertEqual(len(findings[0]["runs"]), 2)
        machines = {r["machine"] for r in findings[0]["runs"]}
        self.assertEqual(machines, {"DLAPTOP-4.local", "ree-cloud-4"})

    def test_scan_clean_corpus_finds_nothing(self):
        _write_manifest(
            self.evidence / "run_one.json",
            queue_id="V3-EXQ-900", run_id="v3_exq_900_..._v3", machine="ree-cloud-2",
        )
        _write_manifest(
            self.evidence / "run_two.json",
            queue_id="V3-EXQ-901", run_id="v3_exq_901_..._v3", machine="ree-cloud-3",
        )
        self.assertEqual(M.scan(self.evidence, self.root), [])

    def test_a_manifest_marked_superseded_does_not_count_toward_a_duplicate(self):
        # A future consumer might mark one twin superseded rather than
        # deleting it (CLAUDE.md's supersession convention never deletes
        # evidence). That should stop counting as a live duplicate.
        _write_manifest(
            self.evidence / "run_a.json",
            queue_id="V3-EXQ-900", run_id="v3_exq_900_a_v3", machine="ree-cloud-2",
        )
        _write_manifest(
            self.evidence / "run_b.json",
            queue_id="V3-EXQ-900", run_id="v3_exq_900_b_v3", machine="ree-cloud-3",
            evidence_direction="superseded",
        )
        self.assertEqual(M.scan(self.evidence, self.root), [])

    def test_scan_skips_reserved_plumbing_filenames(self):
        (self.evidence / "review_tracker.json").write_text(
            json.dumps({"queue_id": "V3-EXQ-1"})
        )
        (self.evidence / "runner_status.json").write_text(
            json.dumps({"queue_id": "V3-EXQ-1"})
        )
        self.assertEqual(M.scan(self.evidence, self.root), [])

    def test_scan_skips_dry_run_prefixed_files(self):
        _write_manifest(
            self.evidence / "_dry_v3_exq_1_v3.json",
            queue_id="V3-EXQ-1", run_id="v3_exq_1_v3",
        )
        _write_manifest(
            self.evidence / "v3_exq_1_v3.json",
            queue_id="V3-EXQ-1", run_id="v3_exq_1_v3",
        )
        self.assertEqual(M.scan(self.evidence, self.root), [])

    def test_scan_tolerates_unreadable_json(self):
        (self.evidence / "corrupt.json").write_text("{not json")
        self.assertEqual(M.scan(self.evidence, self.root), [])

    def test_scan_skips_manifest_missing_queue_id(self):
        _write_manifest(self.evidence / "no_qid.json", run_id="v3_exq_1_v3")
        self.assertEqual(M.scan(self.evidence, self.root), [])

    def test_missing_evidence_dir_returns_empty(self):
        self.assertEqual(M.scan(self.evidence / "does_not_exist", self.root), [])


class MainExitCodeTests(unittest.TestCase):
    """Exercises main() for real, with EVIDENCE_DIR/ROOT/
    KNOWN_DUPLICATE_QUEUE_IDS monkeypatched onto the loaded module -- main()
    reads all three as module globals at call time, so this is the only way
    to reach its actual exit-code branches hermetically."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.evidence = self.root / "evidence" / "experiments"
        self.evidence.mkdir(parents=True)
        self._orig_evidence_dir = M.EVIDENCE_DIR
        self._orig_root = M.ROOT
        self._orig_baseline = M.KNOWN_DUPLICATE_QUEUE_IDS
        M.EVIDENCE_DIR = self.evidence
        M.ROOT = self.root
        self.addCleanup(self._restore)

    def _restore(self):
        M.EVIDENCE_DIR = self._orig_evidence_dir
        M.ROOT = self._orig_root
        M.KNOWN_DUPLICATE_QUEUE_IDS = self._orig_baseline

    def _write_dup(self, qid="V3-EXQ-900"):
        _write_manifest(self.evidence / "a.json", queue_id=qid, run_id="a_v3",
                        machine="ree-cloud-2")
        _write_manifest(self.evidence / "b.json", queue_id=qid, run_id="b_v3",
                        machine="ree-cloud-3")

    def test_new_finding_exits_nonzero(self):
        self._write_dup()
        M.KNOWN_DUPLICATE_QUEUE_IDS = frozenset()
        self.assertEqual(M.main([]), 1)

    def test_baseline_entry_no_longer_reproducing_exits_nonzero(self):
        M.KNOWN_DUPLICATE_QUEUE_IDS = frozenset({"V3-EXQ-900"})
        self.assertEqual(M.main([]), 1)

    def test_finding_matching_baseline_exits_zero(self):
        self._write_dup()
        M.KNOWN_DUPLICATE_QUEUE_IDS = frozenset({"V3-EXQ-900"})
        self.assertEqual(M.main([]), 0)

    def test_clean_empty_corpus_exits_zero(self):
        M.KNOWN_DUPLICATE_QUEUE_IDS = frozenset()
        self.assertEqual(M.main([]), 0)

    def test_list_flag_does_not_crash_and_prints_both_runs(self):
        self._write_dup()
        M.KNOWN_DUPLICATE_QUEUE_IDS = frozenset({"V3-EXQ-900"})
        self.assertEqual(M.main(["--list"]), 0)

    def test_json_flag_does_not_crash(self):
        self._write_dup()
        M.KNOWN_DUPLICATE_QUEUE_IDS = frozenset({"V3-EXQ-900"})
        self.assertEqual(M.main(["--json"]), 0)


class RealCorpusBaselineTest(unittest.TestCase):
    """Best-effort: skipped when the real evidence dir isn't present (e.g. a
    staged remote-worker tree, which excludes evidence/ -- see CLAUDE.md
    "Running the test suite"). Pins the CURRENT real-corpus finding set to
    KNOWN_DUPLICATE_QUEUE_IDS so a genuine future change is visible here too,
    not only via `python3 scripts/check_duplicate_queue_id_execution.py`."""

    def test_real_corpus_matches_pinned_baseline(self):
        if not M.EVIDENCE_DIR.is_dir():
            self.skipTest("real REE_assembly/evidence/experiments/ not present "
                           "in this checkout (expected on a staged remote-worker "
                           "tree)")
        findings = M.scan()
        found_qids = {f["queue_id"] for f in findings}
        self.assertEqual(
            found_qids, M.KNOWN_DUPLICATE_QUEUE_IDS,
            "real corpus duplicate-execution findings drifted from the "
            "pinned baseline -- see this module's own main() output for "
            "detail, then update KNOWN_DUPLICATE_QUEUE_IDS deliberately",
        )


if __name__ == "__main__":
    unittest.main()
