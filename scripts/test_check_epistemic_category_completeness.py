#!/usr/bin/env python3
"""Regression tests for check_epistemic_category_completeness.py (GOV-CAT-1).

Hermetic: every test builds a tmp `failure_autopsy_*.json` corpus and a tmp
baseline file and points `scan()` / `main()` at them via --autopsy-dir /
--baseline, so nothing depends on the real evidence tree or on the real backlog
snapshot.

The tests that matter most are the NEGATIVE CONTROLS, because every failure mode
this arm has is a silent one:

  * an in-enum value must NOT fire (else the arm is noise and gets ignored);
  * neither exclusion mechanism may BLANKET-SILENCE -- a new out-of-enum value in
    a baselined artifact, and a new one in an artifact carrying a metabolization
    marker, must both still fire (this is the hit-scoping property the whole
    design rests on, and the one a later "simplification" would quietly drop);
  * a marker with no `metabolized_hits` must be IGNORED and REPORTED, never
    treated as silencing the file;
  * the enum must be the IMPORTED object, not a restated copy;
  * `--strict`'s exit contract must be UNCHANGED by the validity arm.

Run: /opt/local/bin/python3 scripts/test_check_epistemic_category_completeness.py
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


M = _load_module("ree_check_epistemic_category_completeness",
                 "check_epistemic_category_completeness.py")

VALID = "substrate_ceiling"          # in the enum
OTHER_VALID = "standard"             # in the enum
BAD = "measurement_test_design_defect"   # the corpus's most common out-of-enum value
BAD2 = "competence_implementation_gap"   # the 2026-08-08/09 live incident value


def _target(run_id, category=None, claim_ids=("MECH-1",), per_claim=None,
            legacy=False):
    t = {"run_id": run_id}
    if legacy:
        t["claim_id"] = list(claim_ids)[0] if claim_ids else "MECH-1"
    else:
        t["claim_ids"] = list(claim_ids)
    if category is not None:
        t["recommended_epistemic_category"] = category
    if per_claim is not None:
        t["recommended_epistemic_category_per_claim"] = per_claim
    return t


def _write_autopsy(planning, stem, targets, status="confirmed", extra=None):
    data = {"status": status, "targets": targets}
    if extra:
        data.update(extra)
    path = planning / ("failure_autopsy_%s.json" % stem)
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def _write_baseline(path, entries):
    path.write_text(json.dumps({"entries": entries}), encoding="utf-8")
    return path


class _TmpCorpus(unittest.TestCase):
    """Base fixture: a tmp planning dir plus an (initially absent) baseline."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.planning = self.root / "planning"
        self.planning.mkdir()
        self.baseline_path = self.root / "baseline.v1.json"
        self.addCleanup(self._tmp.cleanup)

    def scan(self, baseline=None):
        return M.scan(self.planning, baseline or {})

    def run_main(self, *argv):
        """Invoke main() with argv, returning (rc, stdout)."""
        old = sys.argv
        sys.argv = ["check_epistemic_category_completeness.py",
                    "--autopsy-dir", str(self.planning),
                    "--baseline", str(self.baseline_path)] + list(argv)
        buf = io.StringIO()
        try:
            with redirect_stdout(buf):
                rc = M.main()
        finally:
            sys.argv = old
        return rc, buf.getvalue()


class EnumSourceTest(unittest.TestCase):
    """The enum is IMPORTED from validate_claims.py, never restated."""

    def test_enum_is_the_registry_gates_own_object(self):
        # Loading the module must have IMPORTED validate_claims -- a restated
        # copy of the eight values would leave this absent.
        self.assertIn("validate_claims", sys.modules)
        self.assertIs(M.VALID_EPISTEMIC_CATEGORIES,
                      sys.modules["validate_claims"].VALID_EPISTEMIC_CATEGORIES)
        # And it agrees with a fresh read of the file on disk, so the assertion
        # cannot pass off a stale sys.modules entry as the registry's enum.
        fresh = _load_module("ree_validate_claims_for_test", "validate_claims.py")
        self.assertEqual(M.VALID_EPISTEMIC_CATEGORIES,
                         fresh.VALID_EPISTEMIC_CATEGORIES)

    def test_no_restated_enum_literal_in_the_module(self):
        """A future edit must not reintroduce a local copy of the eight values."""
        src = (SCRIPTS_DIR / "check_epistemic_category_completeness.py").read_text(
            encoding="utf-8")
        body = src.split('"""', 2)[-1]  # ignore the docstring, which names them
        self.assertNotIn("substrate_coherence", body)
        self.assertNotIn("derivational", body)


class ValidityArmTest(_TmpCorpus):
    def test_in_enum_value_does_not_fire(self):
        """NEGATIVE CONTROL: a valid category is never reported."""
        _write_autopsy(self.planning, "ok_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", VALID),
            _target("v3_exq_2_b_20260101T000000Z_v3", OTHER_VALID),
        ])
        b = self.scan()
        self.assertEqual(b["invalid_category"], [])
        self.assertEqual(b["missing_category"], [])

    def test_out_of_enum_value_fires(self):
        _write_autopsy(self.planning, "bad_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD),
        ])
        b = self.scan()
        self.assertEqual(len(b["invalid_category"]), 1)
        f = b["invalid_category"][0]
        self.assertEqual(f["value"], BAD)
        self.assertEqual(f["field"], "recommended_epistemic_category")
        self.assertEqual(f["companion_md"], "failure_autopsy_bad_2026-08-09.md")

    def test_per_claim_map_is_swept_on_target_and_at_file_level(self):
        _write_autopsy(self.planning, "pc_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", VALID,
                    per_claim={"MECH-1": VALID, "MECH-2": BAD2}),
        ], extra={"recommended_epistemic_category_per_claim": {"ARC-9": BAD}})
        b = self.scan()
        got = {(f["field"], f["claim"], f["value"])
               for f in b["invalid_category"]}
        self.assertEqual(got, {
            ("recommended_epistemic_category_per_claim", "MECH-2", BAD2),
            ("recommended_epistemic_category_per_claim", "ARC-9", BAD),
        })

    def test_normalization_matches_the_registry_gate(self):
        """`.strip().lower()`, exactly as validate_claims.py normalizes."""
        _write_autopsy(self.planning, "norm_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", "  Substrate_Ceiling  "),
            _target("v3_exq_2_b_20260101T000000Z_v3", "N/A"),
        ])
        b = self.scan()
        self.assertEqual([f["value"] for f in b["invalid_category"]], ["N/A"])

    def test_empty_and_null_are_the_completeness_arms_business_not_this_one(self):
        _write_autopsy(self.planning, "empty_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", None),
            _target("v3_exq_2_b_20260101T000000Z_v3", ""),
        ])
        b = self.scan()
        self.assertEqual(b["invalid_category"], [])
        self.assertEqual(len(b["missing_category"]), 2)

    def test_only_confirmed_artifacts_are_swept(self):
        _write_autopsy(self.planning, "draft_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD),
        ], status="draft")
        self.assertEqual(self.scan()["invalid_category"], [])

    def test_legacy_claim_id_target_reports_both_defects(self):
        """A bad value on an unkeyed target is two defects, not one."""
        _write_autopsy(self.planning, "legacy_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD, legacy=True),
        ])
        b = self.scan()
        self.assertEqual(len(b["unkeyed_schema"]), 1)
        self.assertEqual(len(b["invalid_category"]), 1)

    def test_unparseable_artifact_is_skipped_not_fatal(self):
        (self.planning / "failure_autopsy_broken_2026-08-09.json").write_text(
            "{not json", encoding="utf-8")
        _write_autopsy(self.planning, "ok_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD),
        ])
        self.assertEqual(len(self.scan()["invalid_category"]), 1)

    def test_absent_corpus_surfaces_nothing(self):
        b = M.scan(self.root / "does-not-exist", {})
        self.assertEqual(sum(len(v) for v in b.values()), 0)


class BaselineExclusionTest(_TmpCorpus):
    def test_baselined_value_is_excluded_not_actionable(self):
        _write_autopsy(self.planning, "b_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD),
        ])
        b = self.scan({"failure_autopsy_b_2026-08-09": {BAD}})
        self.assertEqual(b["invalid_category"], [])
        self.assertEqual(len(b["invalid_baselined"]), 1)

    def test_baseline_cannot_blanket_silence_a_new_value(self):
        """HIT-SCOPING. The baselined artifact gains a DIFFERENT bad value; it fires."""
        _write_autopsy(self.planning, "b_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD),
            _target("v3_exq_2_b_20260101T000000Z_v3", BAD2),
        ])
        b = self.scan({"failure_autopsy_b_2026-08-09": {BAD}})
        self.assertEqual([f["value"] for f in b["invalid_category"]], [BAD2])
        self.assertEqual(len(b["invalid_baselined"]), 1)

    def test_baseline_is_scoped_to_its_own_artifact(self):
        """A value baselined for artifact A does not excuse it in artifact B."""
        _write_autopsy(self.planning, "a_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD)])
        _write_autopsy(self.planning, "b_2026-08-09", [
            _target("v3_exq_2_b_20260101T000000Z_v3", BAD)])
        b = self.scan({"failure_autopsy_a_2026-08-09": {BAD}})
        self.assertEqual([f["artifact"] for f in b["invalid_category"]],
                         ["failure_autopsy_b_2026-08-09.json"])

    def test_a_brand_new_artifact_is_never_baselined(self):
        """The actual prospective risk: a new artifact has no entry, so it fires."""
        _write_autopsy(self.planning, "old_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD)])
        _write_autopsy(self.planning, "new_2026-08-10", [
            _target("v3_exq_2_b_20260101T000000Z_v3", BAD)])
        b = self.scan({"failure_autopsy_old_2026-08-09": {BAD}})
        self.assertEqual([f["artifact"] for f in b["invalid_category"]],
                         ["failure_autopsy_new_2026-08-10.json"])

    def test_missing_or_malformed_baseline_excludes_nothing(self):
        """Fails toward REPORTING the backlog, never toward silently passing."""
        _write_autopsy(self.planning, "b_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD)])
        self.assertEqual(M.load_baseline(self.root / "absent.json"), {})
        (self.root / "junk.json").write_text("{not json", encoding="utf-8")
        self.assertEqual(M.load_baseline(self.root / "junk.json"), {})
        _write_baseline(self.root / "noentries.json", "not-a-dict")
        self.assertEqual(M.load_baseline(self.root / "noentries.json"), {})

    def test_baseline_values_are_normalized_on_read(self):
        _write_autopsy(self.planning, "b_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", "N/A")])
        _write_baseline(self.baseline_path,
                        {"failure_autopsy_b_2026-08-09": ["  n/a  "]})
        b = self.scan(M.load_baseline(self.baseline_path))
        self.assertEqual(b["invalid_category"], [])
        self.assertEqual(len(b["invalid_baselined"]), 1)

    def test_build_baseline_round_trips_to_silence(self):
        _write_autopsy(self.planning, "b_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD),
            _target("v3_exq_2_b_20260101T000000Z_v3", BAD2),
        ])
        snap = M.build_baseline(self.planning)
        self.assertEqual(snap["n_instances"], 2)
        self.assertEqual(snap["n_artifacts"], 1)
        _write_baseline(self.baseline_path, snap["entries"])
        b = self.scan(M.load_baseline(self.baseline_path))
        self.assertEqual(b["invalid_category"], [])
        self.assertEqual(len(b["invalid_baselined"]), 2)


class MetabolizedMarkerTest(_TmpCorpus):
    def test_marker_excuses_only_the_values_it_names(self):
        _write_autopsy(self.planning, "m_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD),
            _target("v3_exq_2_b_20260101T000000Z_v3", BAD2),
        ], extra={M.METABOLIZED_KEY: {
            "date": "2026-08-10",
            "metabolized_hits": [BAD],
            "note": "adjudicated",
        }})
        b = self.scan()
        self.assertEqual([f["value"] for f in b["invalid_metabolized"]], [BAD])
        self.assertEqual([f["value"] for f in b["invalid_category"]], [BAD2])

    def test_marker_without_hits_is_ignored_and_reported(self):
        """A marker missing metabolized_hits must fail LOUD, never blanket-silence."""
        for marker in ({"date": "2026-08-10", "note": "n"},
                       {"date": "2026-08-10", "metabolized_hits": []},
                       {"date": "2026-08-10", "metabolized_hits": "   "}):
            with self.subTest(marker=marker):
                for p in self.planning.glob("*.json"):
                    p.unlink()
                _write_autopsy(self.planning, "m_2026-08-09", [
                    _target("v3_exq_1_a_20260101T000000Z_v3", BAD),
                ], extra={M.METABOLIZED_KEY: marker})
                b = self.scan()
                self.assertEqual(len(b["invalid_category"]), 1)
                self.assertEqual(len(b["invalid_metabolized"]), 0)
                self.assertEqual(len(b["malformed_markers"]), 1)

    def test_marker_is_scoped_to_its_own_artifact(self):
        _write_autopsy(self.planning, "m_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD),
        ], extra={M.METABOLIZED_KEY: {"metabolized_hits": [BAD]}})
        _write_autopsy(self.planning, "n_2026-08-09", [
            _target("v3_exq_2_b_20260101T000000Z_v3", BAD)])
        b = self.scan()
        self.assertEqual([f["artifact"] for f in b["invalid_category"]],
                         ["failure_autopsy_n_2026-08-09.json"])

    def test_marker_hits_are_normalized(self):
        _write_autopsy(self.planning, "m_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", "N/A"),
        ], extra={M.METABOLIZED_KEY: {"metabolized_hits": " N/a "}})
        self.assertEqual(self.scan()["invalid_category"], [])


class ExitContractTest(_TmpCorpus):
    def test_default_is_warn_only_exit_zero(self):
        _write_autopsy(self.planning, "b_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD)])
        rc, out = self.run_main()
        self.assertEqual(rc, 0)
        self.assertIn("out-of-enum value, new    (ACTIONABLE): 1", out)

    def test_strict_is_unchanged_by_the_validity_arm(self):
        """--strict still gates on missing_category ALONE. No caller's rc moves."""
        _write_autopsy(self.planning, "b_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD)])
        self.assertEqual(self.run_main("--strict")[0], 0)

    def test_strict_still_fires_on_a_missing_category(self):
        _write_autopsy(self.planning, "b_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", None)])
        self.assertEqual(self.run_main("--strict")[0], 1)
        self.assertEqual(self.run_main()[0], 0)

    def test_strict_validity_is_the_opt_in_gate(self):
        _write_autopsy(self.planning, "b_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD)])
        self.assertEqual(self.run_main("--strict-validity")[0], 1)

    def test_strict_validity_passes_when_only_baselined(self):
        _write_autopsy(self.planning, "b_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD)])
        _write_baseline(self.baseline_path,
                        {"failure_autopsy_b_2026-08-09": [BAD]})
        self.assertEqual(self.run_main("--strict-validity")[0], 0)

    def test_json_mode_carries_the_validity_keys(self):
        _write_autopsy(self.planning, "b_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD)])
        rc, out = self.run_main("--json")
        payload = json.loads(out)
        self.assertEqual(rc, 0)
        self.assertEqual(payload["n_invalid_category"], 1)
        self.assertEqual(payload["n_invalid_excluded"], 0)
        # The pre-existing keys morning-digest Step 4c reads are still present.
        for key in ("n_missing_category", "n_unkeyed_schema",
                    "n_claimless_missing"):
            self.assertIn(key, payload)
        self.assertEqual(sorted(payload["valid_categories"]),
                         sorted(M.VALID_EPISTEMIC_CATEGORIES))

    def test_write_baseline_reports_what_it_silences(self):
        _write_autopsy(self.planning, "b_2026-08-09", [
            _target("v3_exq_1_a_20260101T000000Z_v3", BAD)])
        rc, out = self.run_main("--write-baseline")
        self.assertEqual(rc, 0)
        self.assertIn("SILENCED 1 out-of-enum instance(s)", out)
        self.assertTrue(self.baseline_path.is_file())
        # And the written snapshot actually silences on the next run.
        self.assertIn("out-of-enum value, new    (ACTIONABLE): 0",
                      self.run_main()[1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
