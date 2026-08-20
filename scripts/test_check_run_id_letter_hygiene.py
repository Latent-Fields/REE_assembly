#!/usr/bin/env python3
"""Regression tests for check_run_id_letter_hygiene.py.

Hermetic: is_letter_drop() and scan() are exercised against a tmp
evidence/experiments tree, never the real corpus -- so these tests do not
drift as the real corpus grows. One separate, best-effort test re-runs scan()
against the REAL evidence dir (skipped if absent, e.g. staged-tree test runs
that exclude evidence/ -- see CLAUDE.md "Running the test suite") and pins it
to the current known-baseline set, so a genuine corpus change is visible
without being load-bearing for the hermetic suite.

Run: /opt/local/bin/python3 scripts/test_check_run_id_letter_hygiene.py
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


M = _load_module("ree_check_run_id_letter_hygiene", "check_run_id_letter_hygiene.py")


class IsLetterDropTests(unittest.TestCase):
    def test_genuine_letter_drop(self):
        # The pinned V3-EXQ-920a shape: number present, letter absent.
        self.assertTrue(M.is_letter_drop(
            "V3-EXQ-920a",
            "v3_exq_920_uncensored_survival_single_life_fishtank_20260814T223432Z_v3",
        ))

    def test_letter_correctly_carried_is_not_flagged(self):
        self.assertFalse(M.is_letter_drop(
            "V3-EXQ-878a",
            "v3_exq_878a_mech332_commitment_calibration_20260808T193223Z_v3",
        ))

    def test_unlettered_queue_id_is_not_flagged(self):
        self.assertFalse(M.is_letter_drop(
            "V3-EXQ-920",
            "v3_exq_920_uncensored_survival_single_life_fishtank_20260811T210906Z_v3",
        ))

    def test_sd068_shape_number_never_present_is_not_flagged(self):
        # The autopsy's explicit non-hazard: run_id never encodes the number
        # at all, so there is nothing to drop a letter FROM.
        self.assertFalse(M.is_letter_drop(
            "V3-EXQ-778b",
            "v3_exq_sd068_null_content_control_diagnostic_20260717T160320Z_v3",
        ))

    def test_missing_or_empty_inputs_are_not_flagged(self):
        self.assertFalse(M.is_letter_drop("", "v3_exq_1_foo_20260101T000000Z_v3"))
        self.assertFalse(M.is_letter_drop("V3-EXQ-1a", ""))
        self.assertFalse(M.is_letter_drop(None, None))


def _write_manifest(path, queue_id=None, run_id=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = {"outcome": "PASS"}
    if queue_id is not None:
        doc["queue_id"] = queue_id
    if run_id is not None:
        doc["run_id"] = run_id
    path.write_text(json.dumps(doc))


class ScanTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.evidence = self.root / "evidence" / "experiments"
        self.evidence.mkdir(parents=True)

    def test_scan_finds_the_defect_shape(self):
        _write_manifest(
            self.evidence / "v3_exq_612_smoke_20260528T175700Z_v3.json",
            queue_id="V3-EXQ-612d",
            run_id="v3_exq_612_smoke_20260528T175700Z_v3",
        )
        findings = M.scan(self.evidence, self.root)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["queue_id"], "V3-EXQ-612d")
        self.assertEqual(
            findings[0]["path"],
            "evidence/experiments/v3_exq_612_smoke_20260528T175700Z_v3.json",
        )

    def test_scan_clean_corpus_finds_nothing(self):
        _write_manifest(
            self.evidence / "v3_exq_878a_20260808T193223Z_v3.json",
            queue_id="V3-EXQ-878a",
            run_id="v3_exq_878a_mech332_commitment_calibration_20260808T193223Z_v3",
        )
        self.assertEqual(M.scan(self.evidence, self.root), [])

    def test_scan_skips_reserved_plumbing_filenames(self):
        (self.evidence / "review_tracker.json").write_text(
            json.dumps({"queue_id": "V3-EXQ-1a", "run_id": "v3_exq_1_20260101T000000Z_v3"})
        )
        self.assertEqual(M.scan(self.evidence, self.root), [])

    def test_scan_skips_dry_run_prefixed_files(self):
        _write_manifest(
            self.evidence / "_dry_v3_exq_612_smoke_20260528T175700Z_v3.json",
            queue_id="V3-EXQ-612d",
            run_id="v3_exq_612_smoke_20260528T175700Z_v3",
        )
        self.assertEqual(M.scan(self.evidence, self.root), [])

    def test_scan_tolerates_unreadable_json(self):
        (self.evidence / "corrupt.json").write_text("{not json")
        self.assertEqual(M.scan(self.evidence, self.root), [])

    def test_scan_skips_manifest_missing_either_id(self):
        _write_manifest(self.evidence / "no_queue.json", run_id="v3_exq_1_20260101T000000Z_v3")
        _write_manifest(self.evidence / "no_run.json", queue_id="V3-EXQ-1a")
        self.assertEqual(M.scan(self.evidence, self.root), [])

    def test_missing_evidence_dir_returns_empty(self):
        self.assertEqual(M.scan(self.evidence / "does_not_exist", self.root), [])


class MainExitCodeTests(unittest.TestCase):
    """Exercises main() for real, with EVIDENCE_DIR/ROOT/KNOWN_LETTER_DROPS
    monkeypatched onto the loaded module -- main() reads all three as module
    globals at call time, so this is the only way to reach its actual
    exit-code branches hermetically."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.evidence = self.root / "evidence" / "experiments"
        self.evidence.mkdir(parents=True)
        self._orig_evidence_dir = M.EVIDENCE_DIR
        self._orig_root = M.ROOT
        self._orig_baseline = M.KNOWN_LETTER_DROPS
        M.EVIDENCE_DIR = self.evidence
        M.ROOT = self.root
        self.addCleanup(self._restore)

    def _restore(self):
        M.EVIDENCE_DIR = self._orig_evidence_dir
        M.ROOT = self._orig_root
        M.KNOWN_LETTER_DROPS = self._orig_baseline

    def test_new_finding_exits_nonzero(self):
        _write_manifest(
            self.evidence / "v3_exq_612_smoke_20260528T175700Z_v3.json",
            queue_id="V3-EXQ-612d",
            run_id="v3_exq_612_smoke_20260528T175700Z_v3",
        )
        M.KNOWN_LETTER_DROPS = frozenset()
        self.assertEqual(M.main([]), 1)

    def test_baseline_entry_no_longer_reproducing_exits_nonzero(self):
        # Nothing on disk matches the pinned entry -- "fixed" (or the
        # manifest moved) still requires a deliberate baseline update.
        M.KNOWN_LETTER_DROPS = frozenset({"V3-EXQ-612d"})
        self.assertEqual(M.main([]), 1)

    def test_finding_matching_baseline_exits_zero(self):
        _write_manifest(
            self.evidence / "v3_exq_612_smoke_20260528T175700Z_v3.json",
            queue_id="V3-EXQ-612d",
            run_id="v3_exq_612_smoke_20260528T175700Z_v3",
        )
        M.KNOWN_LETTER_DROPS = frozenset({"V3-EXQ-612d"})
        self.assertEqual(M.main([]), 0)

    def test_clean_empty_corpus_exits_zero(self):
        M.KNOWN_LETTER_DROPS = frozenset()
        self.assertEqual(M.main([]), 0)


class RealCorpusBaselineTest(unittest.TestCase):
    """Best-effort: skipped when the real evidence dir isn't present (e.g. a
    staged remote-worker tree, which excludes evidence/ -- see CLAUDE.md
    "Running the test suite"). Pins the CURRENT real-corpus finding set to
    KNOWN_LETTER_DROPS so a genuine future change is visible here too, not
    only via `python3 scripts/check_run_id_letter_hygiene.py` run by hand."""

    def test_real_corpus_matches_pinned_baseline(self):
        if not M.EVIDENCE_DIR.is_dir():
            self.skipTest("real REE_assembly/evidence/experiments/ not present "
                           "in this checkout (expected on a staged remote-worker "
                           "tree)")
        findings = M.scan()
        found_qids = {f["queue_id"] for f in findings}
        self.assertEqual(
            found_qids, M.KNOWN_LETTER_DROPS,
            "real corpus letter-drop findings drifted from the pinned "
            "baseline -- see this module's own main() output for detail, "
            "then update KNOWN_LETTER_DROPS deliberately",
        )


if __name__ == "__main__":
    unittest.main()
