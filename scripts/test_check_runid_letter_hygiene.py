#!/usr/bin/env python3
"""Regression tests for check_runid_letter_hygiene.py.

Hermetic: every test builds a tmp evidence/experiments tree and points the
module's functions at it via `--evidence-dir` / direct calls, so nothing
depends on the real evidence tree. Covers the positive case (letter correctly
encoded -> not flagged), the negative case (letter dropped -> flagged, the
pinned V3-EXQ-920/920a regression), the SD-068 shape (descriptive slug, no
number in run_id at all -> not this defect, not flagged), the "different
naming shape" exclusion (742-m / 742m-b -> LETTERED_QUEUE_ID_RE does not
match, not flagged), and stem-collision detection independent of the
letter-drop detector.

Run: /opt/local/bin/python3 scripts/test_check_runid_letter_hygiene.py
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


M = _load_module("ree_check_runid_letter_hygiene", "check_runid_letter_hygiene.py")


def _write_manifest(path, queue_id, run_id):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"queue_id": queue_id, "run_id": run_id}))


class Fixture:
    def __init__(self, root):
        self.root = root
        self.evidence = root / "evidence" / "experiments"
        self.evidence.mkdir(parents=True)


class LoadPairsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.fx = Fixture(Path(self.tmp.name))

    def tearDown(self):
        self.tmp.cleanup()

    def test_flat_manifest_pair_loaded(self):
        _write_manifest(self.fx.evidence / "v3_exq_042_foo_20260101T000000Z_v3.json",
                         "V3-EXQ-042", "v3_exq_042_foo_20260101T000000Z_v3")
        pairs = M.load_pairs(self.fx.evidence)
        self.assertEqual(len(pairs), 1)
        self.assertEqual(pairs[0][:2], ("V3-EXQ-042", "v3_exq_042_foo_20260101T000000Z_v3"))

    def test_runpack_manifest_pair_loaded(self):
        _write_manifest(self.fx.evidence / "v3_exq_050_bar" / "runs"
                         / "v3_exq_050_bar_20260101T000000Z_v3" / "manifest.json",
                         "V3-EXQ-050", "v3_exq_050_bar_20260101T000000Z_v3")
        pairs = M.load_pairs(self.fx.evidence)
        self.assertEqual(len(pairs), 1)

    def test_manifest_missing_either_id_skipped(self):
        _write_manifest(self.fx.evidence / "no_queue.json", None, "v3_exq_1_x_20260101T000000Z_v3")
        _write_manifest(self.fx.evidence / "no_run.json", "V3-EXQ-2", None)
        self.assertEqual(M.load_pairs(self.fx.evidence), [])

    def test_non_manifest_json_silently_skipped(self):
        (self.fx.evidence / "review_tracker.json").write_text(
            json.dumps({"reviewed_run_ids": ["x"]}))
        self.assertEqual(M.load_pairs(self.fx.evidence), [])


class LetterDropTest(unittest.TestCase):
    def test_letter_correctly_encoded_not_flagged(self):
        pairs = [("V3-EXQ-042a", "v3_exq_042a_foo_20260101T000000Z_v3", "p1")]
        self.assertEqual(M.find_letter_drops(pairs), [])

    def test_unlettered_queue_id_not_checked(self):
        pairs = [("V3-EXQ-042", "v3_exq_042_foo_20260101T000000Z_v3", "p1")]
        self.assertEqual(M.find_letter_drops(pairs), [])

    def test_letter_dropped_is_flagged(self):
        # The pinned V3-EXQ-920a regression shape (confirmed
        # failure_autopsy_V3-EXQ-920a_2026-08-16).
        pairs = [("V3-EXQ-920a",
                   "v3_exq_920_uncensored_survival_single_life_fishtank_20260814T223432Z_v3",
                   "v3_exq_920_..._20260814T223432Z_v3.json")]
        findings = M.find_letter_drops(pairs)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["queue_id"], "V3-EXQ-920a")

    def test_sd068_descriptive_slug_shape_not_flagged(self):
        # run_id encodes no number at all -- a different naming convention,
        # not this defect (autopsy Section 7a: "not a de-duplication hazard").
        pairs = [("V3-EXQ-778b",
                   "v3_exq_sd068_null_content_control_diagnostic_20260101T000000Z_v3",
                   "p1")]
        self.assertEqual(M.find_letter_drops(pairs), [])

    def test_hyphenated_naming_shape_excluded_by_construction(self):
        # "742-m" / "742m-b" do not match LETTERED_QUEUE_ID_RE at all -- a
        # different naming shape, not the bug-fix letter-suffix convention.
        pairs = [("V3-EXQ-742-m", "v3_exq_742m_mech457_bias_head_baseline_mint_20260101T000000Z_v3", "p1")]
        self.assertEqual(M.find_letter_drops(pairs), [])

    def test_zero_padded_number_still_matches(self):
        pairs = [("V3-EXQ-042a", "v3_exq_042_foo_20260101T000000Z_v3", "p1")]
        findings = M.find_letter_drops(pairs)
        self.assertEqual(len(findings), 1)


class StemCollisionTest(unittest.TestCase):
    def test_two_queue_ids_same_stem_flagged(self):
        pairs = [
            ("V3-EXQ-920", "v3_exq_920_fishtank_20260811T210906Z_v3", "p1"),
            ("V3-EXQ-920a", "v3_exq_920_fishtank_20260814T223432Z_v3", "p2"),
        ]
        findings = M.find_stem_collisions(pairs)
        self.assertEqual(len(findings), 1)
        self.assertEqual(set(findings[0]["queue_ids"].keys()), {"V3-EXQ-920", "V3-EXQ-920a"})

    def test_distinct_stems_not_flagged(self):
        pairs = [
            ("V3-EXQ-1", "v3_exq_1_alpha_20260101T000000Z_v3", "p1"),
            ("V3-EXQ-2", "v3_exq_2_beta_20260101T000000Z_v3", "p2"),
        ]
        self.assertEqual(M.find_stem_collisions(pairs), [])

    def test_single_run_same_queue_id_not_flagged(self):
        # Re-emission of the SAME queue_id (e.g. runner restart) is not a
        # collision between two DIFFERENT queue_ids.
        pairs = [
            ("V3-EXQ-1", "v3_exq_1_alpha_20260101T000000Z_v3", "p1"),
            ("V3-EXQ-1", "v3_exq_1_alpha_20260102T000000Z_v3", "p2"),
        ]
        self.assertEqual(M.find_stem_collisions(pairs), [])


class MainTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.fx = Fixture(Path(self.tmp.name))

    def tearDown(self):
        self.tmp.cleanup()

    def test_clean_corpus_exits_zero(self):
        _write_manifest(self.fx.evidence / "a.json", "V3-EXQ-1a",
                         "v3_exq_1a_foo_20260101T000000Z_v3")
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = M.main(["--evidence-dir", str(self.fx.evidence), "--exit-nonzero"])
        self.assertEqual(rc, 0)

    def test_finding_default_still_exits_zero(self):
        _write_manifest(self.fx.evidence / "a.json", "V3-EXQ-1a",
                         "v3_exq_1_foo_20260101T000000Z_v3")
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = M.main(["--evidence-dir", str(self.fx.evidence)])
        self.assertEqual(rc, 0)  # not gated by default -- see module docstring

    def test_finding_with_exit_nonzero_flag_exits_one(self):
        _write_manifest(self.fx.evidence / "a.json", "V3-EXQ-1a",
                         "v3_exq_1_foo_20260101T000000Z_v3")
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = M.main(["--evidence-dir", str(self.fx.evidence), "--exit-nonzero"])
        self.assertEqual(rc, 1)

    def test_missing_evidence_dir_is_usage_error(self):
        rc = M.main(["--evidence-dir", str(self.fx.root / "nonexistent")])
        self.assertEqual(rc, 2)

    def test_json_output_is_valid_json(self):
        _write_manifest(self.fx.evidence / "a.json", "V3-EXQ-1a",
                         "v3_exq_1_foo_20260101T000000Z_v3")
        buf = io.StringIO()
        with redirect_stdout(buf):
            M.main(["--evidence-dir", str(self.fx.evidence), "--json"])
        doc = json.loads(buf.getvalue())
        self.assertEqual(len(doc["letter_drops"]), 1)


if __name__ == "__main__":
    unittest.main()
