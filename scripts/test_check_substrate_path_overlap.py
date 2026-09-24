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

    def test_entry_is_open_true_when_pending_validation(self):
        # GOV-SUBPATH-1 lockstep fix (2026-09-18): 'implemented' is a strict
        # prefix of 'implemented_pending_validation', so a substring test
        # misread this as CLOSED. The /queue-experiment Step 2.5c predicate
        # this checker must mirror tests 'pending' FIRST and always reads it
        # as OPEN -- landed but unconfirmed is exactly the window a
        # corrupting defect is most likely still live in.
        self.assertTrue(self.M._entry_is_open(
            {"status": "implemented_pending_validation"}))
        self.assertTrue(self.M._entry_is_open(
            {"implementation_status": "implemented",
             "status": "implemented_pending_validation"}))

    def test_entry_is_open_true_for_exact_closed_token_substring_of_prose(self):
        # A status that merely CONTAINS a closed token as a substring of a
        # longer free-text word must NOT read as closed -- only an EXACT
        # match against the enum does. Confirmed live-registry miss
        # (2026-09-16): 'mech448_lead_lever_BUILT_VALIDATED_PROMOTED...'
        # contains 'validated' but is not one of the closed enum values.
        self.assertTrue(self.M._entry_is_open(
            {"status": "mech448_lead_lever_built_validated_promoted_provisional"}))

    def test_entry_is_open_false_for_exact_closed_token(self):
        # An exact match against the closed enum (no surrounding prose,
        # no 'pending') is still CLOSED.
        self.assertFalse(self.M._entry_is_open({"status": "validated"}))
        self.assertFalse(self.M._entry_is_open({"status": "wontfix"}))
        self.assertFalse(self.M._entry_is_open({"status": "closed_aleatoric"}))

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

    def test_modules_overlap_bare_package_import_does_not_match_a_submodule(self):
        # chip-20260923-govsubpath1-package-prefix-fix, defect 1 (the
        # PACKAGE-PREFIX OVER-MATCH). This used to be
        # test_modules_overlap_target_submodule_of_import and asserted the
        # OPPOSITE (True) under the comment "driver imports the package;
        # target names a module inside it" -- that was the bug itself,
        # restated as a pinned test: a bare `import ree_core.predictors`
        # (or `from ree_core.predictors import SomethingElse`, which also
        # lands the bare package name "ree_core.predictors" in `imported`)
        # does NOT prove the driver ever touches e3_selector specifically.
        # ree_core/policy/__init__.py imports tonic_vigor at module load, so
        # treating package-import as "imports everything inside" would flag
        # every importer of the package -- the over-broad reading this
        # module docstring explicitly rejects ("stay DIRECT-import").
        self.assertFalse(self.M._modules_overlap(
            {"ree_core.predictors.e3_selector"}, {"ree_core.predictors"}))

    def test_modules_overlap_false_when_unrelated(self):
        self.assertFalse(self.M._modules_overlap(
            {"ree_core.predictors.e3_selector"}, {"ree_core.agent"}))

    def test_modules_overlap_false_for_unrelated_sibling_name_in_target_package(self):
        # The EXACT measured false-positive (2026-09-23): V3-EXQ-544a/844/
        # 904/919 do `from ree_core.policy import ChunkedPrimitive` (or
        # ChunkState / NoiseFloor) and never reference tonic_vigor, but the
        # pre-fix detector flagged them anyway because "ree_core.policy" (a
        # bare package name) is a string-prefix of the flagged target
        # "ree_core.policy.tonic_vigor". Uses resolve_driver_imports() so
        # this exercises the real producer of `imported`, not a hand-built
        # set that might not match what the parser actually emits.
        imported = self.M.resolve_driver_imports(
            "from ree_core.policy import ChunkedPrimitive\n")
        self.assertIn("ree_core.policy", imported)  # sanity: the bare name IS present
        self.assertFalse(self.M._modules_overlap(
            {"ree_core.policy.tonic_vigor"}, imported),
            "importing a SIBLING name from the target's package must not "
            "match the target module itself")

    def test_modules_overlap_true_for_the_three_direct_import_forms(self):
        # The three forms the module docstring/fix says must KEEP matching
        # -- each puts the target's own dotted name literally in `imported`
        # (see resolve_driver_imports), so `imp == target` catches all
        # three without any prefix heuristic.
        target = {"ree_core.policy.tonic_vigor"}
        cases = [
            "import ree_core.policy.tonic_vigor\n",
            "from ree_core.policy.tonic_vigor import ScoreBias\n",
            "from ree_core.policy import tonic_vigor\n",
        ]
        for source in cases:
            with self.subTest(source=source):
                imported = self.M.resolve_driver_imports(source)
                self.assertTrue(self.M._modules_overlap(target, imported),
                                "%r must still match %r" % (source, target))


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
            entries, missing, err = self.M.load_corrupting_entries(path)
            self.assertIsNone(err)
            self.assertEqual([e["sd_id"] for e in entries], ["SD-A"])
            self.assertEqual(entries[0]["modules"], {"ree_core.predictors.e3_selector"})
            self.assertEqual(missing, [])

    def test_unreadable_file_reports_error_not_crash(self):
        entries, missing, err = self.M.load_corrupting_entries(Path("/nonexistent/substrate_queue.json"))
        self.assertEqual(entries, [])
        self.assertEqual(missing, [])
        self.assertIsNotNone(err)

    def test_corrupting_entry_missing_added_utc_is_excluded_not_gated(self):
        # GOV-SUBPATH-1 fail-safe (2026-08-10 incident): an open severity=corrupting
        # entry with substrate_paths but no added_utc must NOT enter `entries` --
        # doing so previously made every completed run a false-positive candidate,
        # since the added_utc<stamp comparison never fires with nothing to compare.
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write_queue(tmp, [
                {"sd_id": "SD-NO-DATE", "title": "orienting decision scale",
                 "severity": "corrupting",
                 "substrate_paths": ["ree_core/agent.py::select_action"]},
            ])
            entries, missing, err = self.M.load_corrupting_entries(path)
            self.assertIsNone(err)
            self.assertEqual(entries, [])
            self.assertEqual([e["sd_id"] for e in missing], ["SD-NO-DATE"])

    def test_corrupting_entry_unparseable_added_utc_is_excluded_not_gated(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write_queue(tmp, [
                {"sd_id": "SD-BAD-DATE", "severity": "corrupting",
                 "substrate_paths": ["ree_core/agent.py"],
                 "added_utc": "not-a-date"},
            ])
            entries, missing, err = self.M.load_corrupting_entries(path)
            self.assertEqual(entries, [])
            self.assertEqual([e["sd_id"] for e in missing], ["SD-BAD-DATE"])


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

    def test_missing_added_utc_does_not_flood_with_false_candidates(self):
        # Regression for the 2026-08-10 incident: SD-ORIENTING-DECISION-SCALE
        # shipped with no added_utc, so EVERY completed run whose driver
        # imported ree_core.agent (hundreds of them, historical and current
        # alike) was reported as a candidate. With the fail-safe, an entry
        # missing added_utc is excluded from gating entirely -- 0 candidates,
        # surfaced instead via entries_missing_added_utc.
        queue_path, ree_v3_root = self._fixture(
            entries=[{
                "sd_id": "SD-NO-DATE", "title": "orienting decision scale",
                "severity": "corrupting",
                "substrate_paths": ["ree_core/agent.py::select_action"],
                # no added_utc
            }],
            by_run={
                "v3_exq_905_old_20200101T000000Z_v3": {
                    "experiment_type": "v3_exq_905_old", "dry_run": False, "paths": [],
                },
                "v3_exq_906_new_20260802T000000Z_v3": {
                    "experiment_type": "v3_exq_906_new", "dry_run": False, "paths": [],
                },
            },
            driver_sources={
                "v3_exq_905_old": "import ree_core.agent\n",
                "v3_exq_906_new": "import ree_core.agent\n",
            },
        )
        result = self.M.scan(queue_path, ree_v3_root)
        self.assertEqual(result["n_candidates"], 0)
        self.assertEqual(result["n_entries"], 0)
        self.assertEqual([e["sd_id"] for e in result["entries_missing_added_utc"]],
                          ["SD-NO-DATE"])

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
        self.assertEqual(result["entries_missing_added_utc"], [])

    def test_package_prefix_over_match_end_to_end(self):
        """chip-20260923-govsubpath1-package-prefix-fix, defect 1, exercised
        through the full scan() pipeline (not just _modules_overlap in
        isolation): a driver importing an unrelated sibling name from the
        flagged target's PACKAGE must not be reported as a candidate, while
        a driver that actually imports the flagged target still is. This is
        the real measured shape -- V3-EXQ-544a et al import ChunkedPrimitive
        from ree_core.policy, never tonic_vigor, against a substrate_queue
        entry naming ree_core/policy/tonic_vigor.py."""
        queue_path, ree_v3_root = self._fixture(
            entries=[{
                "sd_id": "MECH-320", "title": "tonic vigor coupling bug",
                "severity": "corrupting",
                "substrate_paths": ["ree_core/policy/tonic_vigor.py"],
                "added_utc": "2026-08-01T00:00:00Z",
            }],
            by_run={
                "v3_exq_544a_noisefloor_20260802T000000Z_v3": {
                    "experiment_type": "v3_exq_544a_noisefloor", "dry_run": False, "paths": [],
                },
                "v3_exq_920_tonic_vigor_user_20260802T000000Z_v3": {
                    "experiment_type": "v3_exq_920_tonic_vigor_user", "dry_run": False, "paths": [],
                },
            },
            driver_sources={
                # sibling import from the SAME package -- must NOT match.
                "v3_exq_544a_noisefloor": "from ree_core.policy import ChunkedPrimitive\n",
                # a genuine direct import of the flagged module -- must match.
                "v3_exq_920_tonic_vigor_user": "from ree_core.policy import tonic_vigor\n",
            },
        )
        result = self.M.scan(queue_path, ree_v3_root)
        self.assertEqual(result["n_candidates"], 1)
        self.assertEqual(result["candidates"][0]["run_id"],
                         "v3_exq_920_tonic_vigor_user_20260802T000000Z_v3")


if __name__ == "__main__":
    unittest.main(verbosity=2)
