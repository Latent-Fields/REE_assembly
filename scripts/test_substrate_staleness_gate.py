#!/usr/bin/env python3
"""Contract tests for the substrate-staleness scoring gate in
build_experiment_indexes.py (added 2026-06-02, outstanding_tasks_triage item 5).

The gate honors two manually-set manifest fields that mark a run's evidence as
mechanistically stale because a substrate it depends on changed AFTER the run
was recorded:

  - pending_retest_after_substrate: bool                 (run-level)
  - superseded_by_substrate: "<SD-id>@<YYYY-MM-DD>"       (run-level ref string)
  - pending_retest_after_substrate_per_claim: [claim_id]  (per-claim)
  - superseded_by_substrate_per_claim: {claim_id: ref}    (per-claim ref)

The per-claim forms de-weight ONLY the named claim in a multi-claim manifest,
leaving co-tagged claims intact (mirrors evidence_direction_per_claim).
A flagged entry stays in matrix["entries"] (full audit log) but is tagged
scoring_excluded="stale_substrate" and does NOT feed claim confidence/conflict.
When neither field is present the behaviour is bit-identical to the pre-gate
indexer (the run counts normally).

Run: /opt/local/bin/python3 scripts/test_substrate_staleness_gate.py
"""

import importlib.util
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

INDEXER_PATH = (
    Path(__file__).resolve().parents[1]
    / "evidence" / "experiments" / "scripts" / "build_experiment_indexes.py"
)


def _load_indexer():
    spec = importlib.util.spec_from_file_location("ree_indexer", INDEXER_PATH)
    mod = importlib.util.module_from_spec(spec)
    # Register before exec so @dataclass can resolve the module via sys.modules.
    sys.modules["ree_indexer"] = mod
    spec.loader.exec_module(mod)
    return mod


IDX = _load_indexer()


def _make_run(mod, run_id, claim_ids, *, pending=False, superseded_by="",
              pending_per_claim=None, superseded_per_claim=None,
              direction="supports", status="PASS"):
    """Minimal applicable PASS RunRecord tagging one or more claims."""
    if isinstance(claim_ids, str):
        claim_ids = [claim_ids]
    ts = datetime(2026, 5, 1, 12, 0, 0, tzinfo=timezone.utc)
    return mod.RunRecord(
        experiment_type=run_id.rsplit("_", 1)[0],
        run_id=run_id,
        timestamp_raw="2026-05-01T12:00:00Z",
        timestamp=ts,
        manifest_path=Path("/dev/null"),
        metrics_path=Path("/dev/null"),
        summary_path=Path("/dev/null"),
        manifest_status=status,
        final_status=status,
        claim_ids_tested=list(claim_ids),
        evidence_direction=direction,
        experiment_purpose="evidence",
        pending_retest_after_substrate=pending,
        superseded_by_substrate=superseded_by,
        pending_retest_after_substrate_per_claim=list(pending_per_claim or []),
        superseded_by_substrate_per_claim=dict(superseded_per_claim or {}),
    )


def _excl_for(matrix, run_id, claim_id):
    for e in matrix["entries"]:
        if e["run_id"] == run_id and e["claim_id"] == claim_id:
            return e.get("scoring_excluded", "<COUNTS>"), e
    raise AssertionError(f"entry {run_id}/{claim_id} not found")


class CoerceBoolTests(unittest.TestCase):
    def test_json_bool(self):
        self.assertTrue(IDX._coerce_bool(True))
        self.assertFalse(IDX._coerce_bool(False))

    def test_truthy_strings(self):
        for s in ("true", "True", "1", "yes", "Y", "t"):
            self.assertTrue(IDX._coerce_bool(s), s)

    def test_falsey(self):
        for v in ("false", "0", "no", "", "  ", None, [], {}, 0):
            self.assertFalse(IDX._coerce_bool(v), repr(v))

    def test_numeric(self):
        self.assertTrue(IDX._coerce_bool(1))
        self.assertFalse(IDX._coerce_bool(0))


class StalenessGateTests(unittest.TestCase):
    def _build(self, runs):
        with tempfile.TemporaryDirectory() as d:
            return IDX._write_claim_evidence_matrix(
                base_dir=Path(d),
                by_experiment={"exp": runs},
                by_literature={},
                generated_at="2026-06-02T12:00:00Z",
                planning_criteria={},
            )

    def test_absent_field_counts_normally(self):
        """Bit-identical: a run without the flag is NOT excluded and feeds the claim."""
        run = _make_run(IDX, "exp_normal_v3", "MECH-001")
        m = self._build([run])
        excl, _ = _excl_for(m, "exp_normal_v3", "MECH-001")
        self.assertEqual(excl, "<COUNTS>")
        self.assertIn("MECH-001", m["claims"])

    def test_pending_retest_excluded(self):
        run = _make_run(IDX, "exp_pending_v3", "MECH-002", pending=True)
        m = self._build([run])
        excl, _ = _excl_for(m, "exp_pending_v3", "MECH-002")
        self.assertEqual(excl, "stale_substrate")
        # Excluded => claim has no scoring entries => not summarised.
        self.assertNotIn("MECH-002", m["claims"])

    def test_superseded_by_substrate_excluded_and_ref_echoed(self):
        run = _make_run(IDX, "exp_sup_v3", "MECH-003",
                        superseded_by="SD-056@2026-05-29")
        m = self._build([run])
        excl, entry = _excl_for(m, "exp_sup_v3", "MECH-003")
        self.assertEqual(excl, "stale_substrate")
        self.assertEqual(entry.get("superseded_by_substrate"), "SD-056@2026-05-29")
        self.assertNotIn("MECH-003", m["claims"])

    def test_mixed_set_only_flagged_run_excluded(self):
        """A flagged run is excluded while a clean run on the same claim still counts."""
        clean = _make_run(IDX, "exp_clean_v3", "MECH-004")
        stale = _make_run(IDX, "exp_stale_v3", "MECH-004", pending=True)
        m = self._build([clean, stale])
        self.assertEqual(_excl_for(m, "exp_clean_v3", "MECH-004")[0], "<COUNTS>")
        self.assertEqual(_excl_for(m, "exp_stale_v3", "MECH-004")[0], "stale_substrate")
        # The clean run keeps the claim alive in scoring.
        self.assertIn("MECH-004", m["claims"])

    def test_entry_present_in_audit_log_when_excluded(self):
        """Excluded entries remain in matrix['entries'] for the audit trail."""
        run = _make_run(IDX, "exp_audit_v3", "MECH-005", pending=True)
        m = self._build([run])
        run_ids = {e["run_id"] for e in m["entries"]}
        self.assertIn("exp_audit_v3", run_ids)


class PerClaimStalenessTests(unittest.TestCase):
    def _build(self, runs):
        with tempfile.TemporaryDirectory() as d:
            return IDX._write_claim_evidence_matrix(
                base_dir=Path(d),
                by_experiment={"exp": runs},
                by_literature={},
                generated_at="2026-06-02T12:00:00Z",
                planning_criteria={},
            )

    def test_per_claim_list_excludes_only_named_claim(self):
        """Only the listed claim is de-weighted; co-tagged claims still count."""
        run = _make_run(IDX, "exp_multi_v3", ["MECH-307", "MECH-216", "SD-014"],
                        pending_per_claim=["MECH-307"])
        m = self._build([run])
        self.assertEqual(_excl_for(m, "exp_multi_v3", "MECH-307")[0], "stale_substrate")
        self.assertEqual(_excl_for(m, "exp_multi_v3", "MECH-216")[0], "<COUNTS>")
        self.assertEqual(_excl_for(m, "exp_multi_v3", "SD-014")[0], "<COUNTS>")
        # The non-stale co-tagged claims survive into scoring.
        self.assertIn("MECH-216", m["claims"])
        self.assertIn("SD-014", m["claims"])
        self.assertNotIn("MECH-307", m["claims"])

    def test_per_claim_ref_echoed_only_on_named_claim(self):
        run = _make_run(IDX, "exp_ref_v3", ["SD-049", "SD-015"],
                        direction="weakens",
                        superseded_per_claim={"SD-049": "SD-049@2026-05-31"})
        m = self._build([run])
        excl_049, entry_049 = _excl_for(m, "exp_ref_v3", "SD-049")
        excl_015, entry_015 = _excl_for(m, "exp_ref_v3", "SD-015")
        self.assertEqual(excl_049, "stale_substrate")
        self.assertEqual(entry_049.get("superseded_by_substrate"), "SD-049@2026-05-31")
        self.assertEqual(excl_015, "<COUNTS>")
        self.assertNotIn("superseded_by_substrate", entry_015)

    def test_absent_per_claim_fields_bit_identical(self):
        """No per-claim fields => every claim counts (bit-identical)."""
        run = _make_run(IDX, "exp_clean_multi_v3", ["MECH-101", "MECH-102"])
        m = self._build([run])
        self.assertEqual(_excl_for(m, "exp_clean_multi_v3", "MECH-101")[0], "<COUNTS>")
        self.assertEqual(_excl_for(m, "exp_clean_multi_v3", "MECH-102")[0], "<COUNTS>")


if __name__ == "__main__":
    unittest.main(verbosity=2)
