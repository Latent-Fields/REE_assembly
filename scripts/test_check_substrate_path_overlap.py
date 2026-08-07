#!/usr/bin/env python3
"""Regression tests for check_substrate_path_overlap.py (GOV-SUBPATH-1).

Covers the helper functions (path->module resolution, open/closed
classification, timestamp extraction/comparison, import resolution, module
overlap) and the end-to-end scan() over real tmp-dir fixtures (a real
substrate_queue.json, a real ree-v3/experiments/<type>.py driver file), with
build_index() monkeypatched to a synthetic manifest index -- the same
setUp/tearDown-monkeypatch pattern test_check_workset_drift.py uses, since
build_index()'s EVIDENCE_DIR is not parameterisable and must not be pointed
at the real evidence tree from a test.

Run: /opt/local/bin/python3 scripts/test_check_substrate_path_overlap.py
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


class HelperTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.M = _load_module("ree_check_substrate_path_overlap_helper_test",
                              "check_substrate_path_overlap.py")

    def test_module_from_path_strips_py_and_dots(self):
        self.assertEqual(
            self.M._module_from_path("ree_core/predictors/e3_selector.py"),
            "ree_core.predictors.e3_selector",
        )

    def test_module_from_path_strips_function_suffix(self):
        self.assertEqual(
            self.M._module_from_path("ree_core/predictors/e3_selector.py::compute_harm_cost_fallback"),
            "ree_core.predictors.e3_selector",
        )

    def test_module_from_path_none_for_non_py(self):
        self.assertIsNone(self.M._module_from_path("docs/architecture/sd_013.md"))

    def test_entry_is_open_default_true(self):
        self.assertTrue(self.M._entry_is_open({}))

    def test_entry_is_open_false_when_implemented(self):
        self.assertFalse(self.M._entry_is_open({"implementation_status": "implemented"}))
        self.assertFalse(self.M._entry_is_open({"status": "implemented_validated"}))
        self.assertFalse(self.M._entry_is_open({"status": "IMPLEMENTED"}))  # case-insensitive

    def test_entry_is_open_true_for_free_text_progress_note(self):
        # 'status' in this corpus is heavily free-text; a note that merely
        # DISCUSSES implementation without being one of the closed markers
        # must stay open (ambiguous -> open is the safe direction).
        self.assertTrue(self.M._entry_is_open(
            {"status": "pending_implementation, awaiting design doc"}))

    def test_run_timestamp_extracts_stamp(self):
        self.assertEqual(
            self.M._run_timestamp("v3_exq_330_sd013_contrastive_20260411T023725Z_v3"),
            "20260411T023725Z",
        )

    def test_run_timestamp_none_when_absent(self):
        self.assertIsNone(self.M._run_timestamp("not-a-run-id"))

    def test_added_utc_compact(self):
        self.assertEqual(self.M._added_utc_compact("2026-08-03T12:00:00Z"), "20260803T120000Z")

    def test_added_utc_compact_none_on_garbage(self):
        self.assertIsNone(self.M._added_utc_compact("not-a-date"))

    def test_resolve_driver_imports_plain_import(self):
        src = "import ree_core.predictors.e3_selector\n"
        self.assertIn("ree_core.predictors.e3_selector", self.M.resolve_driver_imports(src))

    def test_resolve_driver_imports_from_import(self):
        src = "from ree_core.predictors import e3_selector\n"
        imported = self.M.resolve_driver_imports(src)
        self.assertIn("ree_core.predictors", imported)
        self.assertIn("ree_core.predictors.e3_selector", imported)

    def test_resolve_driver_imports_from_import_name(self):
        src = "from ree_core.predictors.e3_selector import compute_harm_cost_fallback\n"
        imported = self.M.resolve_driver_imports(src)
        self.assertIn("ree_core.predictors.e3_selector", imported)

    def test_resolve_driver_imports_ignores_unrelated(self):
        src = "import os\nimport numpy as np\n"
        imported = self.M.resolve_driver_imports(src)
        self.assertNotIn("ree_core.predictors.e3_selector", imported)

    def test_resolve_driver_imports_syntax_error_is_empty(self):
        self.assertEqual(self.M.resolve_driver_imports("def broken(:\n"), set())

    def test_modules_overlap_exact(self):
        self.assertTrue(self.M._modules_overlap(
            {"ree_core.predictors.e3_selector"}, {"ree_core.predictors.e3_selector"}))

    def test_modules_overlap_submodule_of_target(self):
        # target names a package; driver imports something inside it.
        self.assertTrue(self.M._modules_overlap(
            {"ree_core.predictors"}, {"ree_core.predictors.e3_selector"}))

    def test_modules_overlap_target_submodule_of_import(self):
        # driver imports the package; target names a module inside it.
        self.assertTrue(self.M._modules_overlap(
            {"ree_core.predictors.e3_selector"}, {"ree_core.predictors"}))

    def test_modules_overlap_false_when_unrelated(self):
        self.assertFalse(self.M._modules_overlap(
            {"ree_core.predictors.e3_selector"}, {"ree_core.agent"}))


class LoadCorruptingEntriesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.M = _load_module("ree_check_substrate_path_overlap_load_test",
                              "check_substrate_path_overlap.py")

    def _write_queue(self, tmp, entries):
        path = Path(tmp) / "substrate_queue.json"
        path.write_text(json.dumps({"queue": entries}), encoding="utf-8")
        return path

    def test_only_open_corrupting_with_paths_is_returned(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write_queue(tmp, [
                {"sd_id": "SD-A", "severity": "corrupting",
                 "substrate_paths": ["ree_core/predictors/e3_selector.py"],
                 "added_utc": "2026-08-01T00:00:00Z"},
                {"sd_id": "SD-B", "severity": "corrupting",
                 "substrate_paths": ["ree_core/agent.py"],
                 "status": "implemented",
                 "added_utc": "2026-08-01T00:00:00Z"},
                {"sd_id": "SD-C", "severity": "degrading",
                 "substrate_paths": ["ree_core/goal.py"],
                 "added_utc": "2026-08-01T00:00:00Z"},
                {"sd_id": "SD-D", "severity": "corrupting",
                 "added_utc": "2026-08-01T00:00:00Z"},
                {"sd_id": "SD-E", "node_class": "complicated (buildable)"},
            ])
            entries, err = self.M.load_corrupting_entries(path)
            self.assertIsNone(err)
            self.assertEqual([e["sd_id"] for e in entries], ["SD-A"])
            self.assertEqual(entries[0]["modules"], {"ree_core.predictors.e3_selector"})

    def test_unreadable_file_reports_error_not_crash(self):
        entries, err = self.M.load_corrupting_entries(Path("/nonexistent/substrate_queue.json"))
        self.assertEqual(entries, [])
        self.assertIsNotNone(err)


class ScanIntegrationTest(unittest.TestCase):
    """End-to-end scan() over real tmp-dir fixtures, with build_index()
    monkeypatched to a synthetic manifest index (its EVIDENCE_DIR is not
    parameterisable and must never be pointed at the real evidence tree)."""

    @classmethod
    def setUpClass(cls):
        cls.M = _load_module("ree_check_substrate_path_overlap_scan_test",
                              "check_substrate_path_overlap.py")

    def setUp(self):
        self._orig_build_index = self.M.build_index

    def tearDown(self):
        self.M.build_index = self._orig_build_index

    def _fixture(self, entries, by_run, driver_sources):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        queue_path = root / "substrate_queue.json"
        queue_path.write_text(json.dumps({"queue": entries}), encoding="utf-8")
        ree_v3_root = root / "ree-v3"
        (ree_v3_root / "experiments").mkdir(parents=True)
        for exp_type, source in driver_sources.items():
            (ree_v3_root / "experiments" / ("%s.py" % exp_type)).write_text(source, encoding="utf-8")
        self.M.build_index = lambda: (by_run, {})
        return queue_path, ree_v3_root

    def test_candidate_found_after_added_utc_with_import_overlap(self):
        queue_path, ree_v3_root = self._fixture(
            entries=[{
                "sd_id": "SD-A", "title": "e3_selector bug",
                "severity": "corrupting",
                "substrate_paths": ["ree_core/predictors/e3_selector.py"],
                "added_utc": "2026-08-01T00:00:00Z",
            }],
            by_run={
                "v3_exq_900_after_20260802T000000Z_v3": {
                    "experiment_type": "v3_exq_900_after", "dry_run": False, "paths": [],
                },
            },
            driver_sources={
                "v3_exq_900_after": "import ree_core.predictors.e3_selector\n",
            },
        )
        result = self.M.scan(queue_path, ree_v3_root)
        self.assertEqual(result["n_candidates"], 1)
        self.assertEqual(result["candidates"][0]["run_id"], "v3_exq_900_after_20260802T000000Z_v3")
        self.assertEqual(result["candidates"][0]["sd_id"], "SD-A")

    def test_run_before_added_utc_is_not_a_candidate(self):
        queue_path, ree_v3_root = self._fixture(
            entries=[{
                "sd_id": "SD-A", "title": "e3_selector bug",
                "severity": "corrupting",
                "substrate_paths": ["ree_core/predictors/e3_selector.py"],
                "added_utc": "2026-08-01T00:00:00Z",
            }],
            by_run={
                "v3_exq_899_before_20260731T000000Z_v3": {
                    "experiment_type": "v3_exq_899_before", "dry_run": False, "paths": [],
                },
            },
            driver_sources={
                "v3_exq_899_before": "import ree_core.predictors.e3_selector\n",
            },
        )
        result = self.M.scan(queue_path, ree_v3_root)
        self.assertEqual(result["n_candidates"], 0)

    def test_dry_run_excluded(self):
        queue_path, ree_v3_root = self._fixture(
            entries=[{
                "sd_id": "SD-A", "title": "e3_selector bug",
                "severity": "corrupting",
                "substrate_paths": ["ree_core/predictors/e3_selector.py"],
                "added_utc": "2026-08-01T00:00:00Z",
            }],
            by_run={
                "v3_exq_901_dry_20260802T000000Z_v3": {
                    "experiment_type": "v3_exq_901_dry", "dry_run": True, "paths": [],
                },
            },
            driver_sources={
                "v3_exq_901_dry": "import ree_core.predictors.e3_selector\n",
            },
        )
        result = self.M.scan(queue_path, ree_v3_root)
        self.assertEqual(result["n_candidates"], 0)

    def test_no_import_overlap_is_not_a_candidate(self):
        queue_path, ree_v3_root = self._fixture(
            entries=[{
                "sd_id": "SD-A", "title": "e3_selector bug",
                "severity": "corrupting",
                "substrate_paths": ["ree_core/predictors/e3_selector.py"],
                "added_utc": "2026-08-01T00:00:00Z",
            }],
            by_run={
                "v3_exq_902_unrelated_20260802T000000Z_v3": {
                    "experiment_type": "v3_exq_902_unrelated", "dry_run": False, "paths": [],
                },
            },
            driver_sources={
                "v3_exq_902_unrelated": "import ree_core.agent\n",
            },
        )
        result = self.M.scan(queue_path, ree_v3_root)
        self.assertEqual(result["n_candidates"], 0)

    def test_missing_driver_file_is_not_a_crash(self):
        queue_path, ree_v3_root = self._fixture(
            entries=[{
                "sd_id": "SD-A", "title": "e3_selector bug",
                "severity": "corrupting",
                "substrate_paths": ["ree_core/predictors/e3_selector.py"],
                "added_utc": "2026-08-01T00:00:00Z",
            }],
            by_run={
                "v3_exq_903_missing_20260802T000000Z_v3": {
                    "experiment_type": "v3_exq_903_no_such_driver", "dry_run": False, "paths": [],
                },
            },
            driver_sources={},
        )
        result = self.M.scan(queue_path, ree_v3_root)
        self.assertEqual(result["n_candidates"], 0)
        self.assertEqual(result["n_runs_scanned"], 0)

    def test_no_corrupting_entries_short_circuits_cleanly(self):
        queue_path, ree_v3_root = self._fixture(
            entries=[],
            by_run={
                "v3_exq_904_20260802T000000Z_v3": {
                    "experiment_type": "v3_exq_904", "dry_run": False, "paths": [],
                },
            },
            driver_sources={"v3_exq_904": "import ree_core.agent\n"},
        )
        result = self.M.scan(queue_path, ree_v3_root)
        self.assertEqual(result["n_entries"], 0)
        self.assertEqual(result["n_candidates"], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
