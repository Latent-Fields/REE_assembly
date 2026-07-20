#!/usr/bin/env python3
"""Unit tests for verdict resolution in generate_pending_review.py.

Regression cover for the dict-shaped-`result` silent drop (2026-07-20): a
manifest carrying `result` as a dict short-circuited the `or` chain in
_manifest_pass_fail, resolved to None, and was skipped outright by
load_unclaimed_manifests -- so an unclaimed terminal FAIL never reached
pending_review.md. Confirmed on
v3_exq_728_trained_allon_capability_point_20260720T155414Z_v3.
"""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent / "generate_pending_review.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("ree_gen_pending", SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Shape of the 728 manifest: dict `result` AND a top-level string `outcome`.
DICT_RESULT_MANIFEST = {
    "run_id": "v3_exq_728_trained_allon_capability_point_20260720T155414Z_v3",
    "experiment_type": "v3_exq_728_trained_allon_capability_point",
    "queue_id": "V3-EXQ-728",
    "claim_ids": [],
    "evidence_direction": "non_contributory",
    "timestamp_utc": "20260720T155414Z",
    "result": {
        "outcome": "FAIL",
        "overall_direction": "non_contributory",
        "interpretation_label": "substrate_not_ready_requeue",
        "interpretation": {"label": "substrate_not_ready_requeue"},
    },
    "outcome": "FAIL",
}


class ManifestPassFailTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def test_dict_shaped_result_resolves_to_inner_outcome(self):
        """The defect: truthy dict short-circuited the or-chain -> None."""
        self.assertEqual(
            self.mod._manifest_pass_fail(DICT_RESULT_MANIFEST), "FAIL")

    def test_dict_shaped_result_pass(self):
        self.assertEqual(
            self.mod._manifest_pass_fail({"result": {"outcome": "PASS"}}), "PASS")

    def test_bare_string_result_still_resolves(self):
        self.assertEqual(self.mod._manifest_pass_fail({"result": "PASS"}), "PASS")
        self.assertEqual(self.mod._manifest_pass_fail({"outcome": "FAIL"}), "FAIL")

    def test_metrics_fallback_still_reached(self):
        self.assertEqual(
            self.mod._manifest_pass_fail({"metrics": {"overall_pass": False}}), "FAIL")

    def test_error_manifests_still_resolve_to_none(self):
        """ERROR stays None so load_error_manifests keeps ownership of it."""
        self.assertIsNone(self.mod._manifest_pass_fail({"result": "ERROR"}))
        self.assertIsNone(
            self.mod._manifest_pass_fail({"result": {"outcome": "ERROR"}}))
        self.assertIsNone(self.mod._manifest_pass_fail({}))

    def test_error_result_does_not_fall_through_to_sibling_field(self):
        """First-present-wins, as the original `or` chain did."""
        self.assertIsNone(
            self.mod._manifest_pass_fail({"result": "ERROR", "outcome": "FAIL"}))


class LoadUnclaimedManifestsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def test_dict_result_manifest_surfaces_as_unclaimed(self):
        with tempfile.TemporaryDirectory() as td:
            evidence = Path(td)
            (evidence / "v3_exq_728_dict_result_v3.json").write_text(
                json.dumps(DICT_RESULT_MANIFEST))
            orig = self.mod.EVIDENCE_DIR
            self.mod.EVIDENCE_DIR = evidence
            try:
                out = self.mod.load_unclaimed_manifests(
                    reviewed=set(), discussed=set(), indexed_run_ids=set())
            finally:
                self.mod.EVIDENCE_DIR = orig

        self.assertEqual(len(out), 1, "dict-shaped result manifest was dropped")
        self.assertEqual(out[0]["run_id"], DICT_RESULT_MANIFEST["run_id"])
        self.assertEqual(out[0]["result"], "FAIL")


if __name__ == "__main__":
    unittest.main()
