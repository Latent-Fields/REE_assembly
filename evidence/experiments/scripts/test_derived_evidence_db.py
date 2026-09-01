#!/usr/bin/env python3
"""Tests for derived_evidence_db.py (derived_evidence_index:P1).

Time-independent. Real sqlite files and real git repos in a tempdir -- no mocks
of git or sqlite, because both of the things worth testing here (the skew gate's
verdict, and the atomic replace) are properties of the real tools.

Roughly half of these are NEGATIVE CONTROLS: the gate must NOT fire on the benign
count direction (uncommitted new manifests, which is the normal state of a live
box), must NOT fire outside a git checkout, and the never-measured / measured-empty
distinction for enabled_default_off_flags must survive the round trip.
"""
from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import derived_evidence_db as dedb  # noqa: E402


def _git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True,
                   capture_output=True)


def _init_repo(repo: Path) -> None:
    _git(repo, "init", "-q")
    _git(repo, "config", "user.email", "t@example.invalid")
    _git(repo, "config", "user.name", "t")


MATRIX = {
    "schema_version": "claim_evidence_matrix/v1",
    "generated_at_utc": "2026-01-01T00:00:00Z",
    "claims": {
        "MECH-457": {
            "genuine_exp_count": 3, "pass_runs": 2, "fail_runs": 1,
            "evidence_quadrant": "novel_discovery",
            "overall_confidence": 0.71, "experimental_confidence": 0.66,
            "experimental_confidence_decoupled": 0.66,
            "literature_confidence": 0.4, "literature_confidence_parallel": 0.4,
            "entries_total": 3, "runs_total": 3,
            "latest_run_id": "r2_v3", "latest_timestamp_utc": "2026-01-01T00:00:00Z",
            "confidence_rationale": "exp=3",
            "exp_posterior": {"mean": 0.66}, "lit_posterior": {"mean": 0.4},
            "direction_counts": {"supports": 2, "weakens": 1},
        },
        "ARC-001": {
            "genuine_exp_count": 0, "evidence_quadrant": "plausible_unproven",
            "experimental_confidence_decoupled": 0.0,
            "literature_confidence_parallel": 0.659,
        },
    },
    "entries": [
        {"claim_id": "MECH-457", "run_id": "r1_v3", "source_type": "experimental",
         "evidence_direction": "supports", "confidence": 0.75, "status": "PASS",
         "timestamp_utc": "2025-12-01T00:00:00Z", "scoring_excluded": ""},
        {"claim_id": "MECH-457", "run_id": "r2_v3", "source_type": "experimental",
         "evidence_direction": "weakens", "confidence": 0.5, "status": "FAIL",
         "timestamp_utc": "2026-01-01T00:00:00Z", "scoring_excluded": ""},
        {"claim_id": "MECH-457", "run_id": "r0_v3", "source_type": "experimental",
         "evidence_direction": "supports", "confidence": 0.9, "status": "PASS",
         "timestamp_utc": "2025-11-01T00:00:00Z", "scoring_excluded": "superseded"},
    ],
    "unlinked_runs": [
        {"run_id": "u1_v3", "experiment_type": "u1", "source_type": "experimental",
         "status": "PASS", "timestamp_utc": "2026-01-01T00:00:00Z"},
    ],
}


class _Run:
    """Duck-typed stand-in for the indexer's RunRecord (see _run_rows)."""
    def __init__(self, run_id, **kw):
        self.run_id = run_id
        self.experiment_type = kw.get("experiment_type", "t")
        self.timestamp_raw = kw.get("timestamp_raw", "2026-01-01T00:00:00Z")
        self.final_status = kw.get("final_status", "PASS")
        self.machine = kw.get("machine", "ree-cloud-2")
        self.machine_class = kw.get("machine_class", "linux-x86_64")
        self.architecture_epoch = "ree_hybrid_guardrails_v1"
        self.manifest_path = kw.get("manifest_path")
        self.experiment_purpose = "evidence"
        self.evidence_class = "exp:simulation"
        self.evidence_level = "C"
        self.evidence_direction = "supports"
        self.adjudication = "n/a"
        self.queue_id = kw.get("queue_id", "")
        self.canonical_profile = ""
        self.substrate_hash = kw.get("substrate_hash", "abc123")
        self.substrate_commit = kw.get("substrate_commit", "deadbeef")
        self.superseded_by_substrate = ""
        self.enabled_default_off_flags = kw.get("enabled_default_off_flags", None)


class DerivedDbTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.base = Path(self._tmp.name) / "experiments"
        self.base.mkdir(parents=True)

    def tearDown(self):
        self._tmp.cleanup()

    # -- census / skew gate ------------------------------------------------

    def test_census_outside_git_is_not_applicable_not_clean(self):
        """No checkout -> in_git is None and the gate cannot fire.

        The distinction matters: reporting 0 would read as 'checked, nothing
        missing', which is a different and stronger claim than 'not checkable'.
        """
        (self.base / "a_v3.json").write_text("{}")
        cen = dedb.manifest_census(self.base)
        self.assertFalse(cen["git_applicable"])
        self.assertIsNone(cen["n_manifests_in_git"])
        self.assertEqual(cen["n_tracked_absent"], 0)

    def test_gate_does_not_fire_on_uncommitted_new_manifests(self):
        """NEGATIVE CONTROL, and the reason this gate is not `on_disk != in_git`.

        A run that finished and has not been committed yet is the NORMAL state.
        A gate that refused here would fire on essentially every real build.
        """
        _init_repo(self.base)
        (self.base / "committed_v3.json").write_text("{}")
        _git(self.base, "add", "-A")
        _git(self.base, "commit", "-qm", "one")
        (self.base / "fresh_v3.json").write_text("{}")  # untracked
        cen = dedb.manifest_census(self.base)
        self.assertGreater(cen["n_manifests_on_disk"], cen["n_manifests_in_git"])
        self.assertEqual(cen["n_tracked_absent"], 0)
        dedb.build_derived_db(self.base, MATRIX)  # must not raise

    def test_gate_fires_on_tracked_but_absent(self):
        """The 2026-07-18 SD-068 signature: tracked, never materialised on disk."""
        _init_repo(self.base)
        (self.base / "gone_v3.json").write_text("{}")
        _git(self.base, "add", "-A")
        _git(self.base, "commit", "-qm", "one")
        (self.base / "gone_v3.json").unlink()
        cen = dedb.manifest_census(self.base)
        self.assertEqual(cen["n_tracked_absent"], 1)
        with self.assertRaises(dedb.DerivedIndexSkewError):
            dedb.build_derived_db(self.base, MATRIX)

    def test_refusal_leaves_a_previous_db_intact(self):
        """A refusal must not truncate the last good build to a smaller one."""
        _init_repo(self.base)
        (self.base / "gone_v3.json").write_text("{}")
        _git(self.base, "add", "-A")
        _git(self.base, "commit", "-qm", "one")
        dedb.build_derived_db(self.base, MATRIX)
        good = dedb.derived_db_path(self.base).read_bytes()
        (self.base / "gone_v3.json").unlink()
        with self.assertRaises(dedb.DerivedIndexSkewError):
            dedb.build_derived_db(self.base, MATRIX)
        self.assertEqual(dedb.derived_db_path(self.base).read_bytes(), good)

    def test_allow_missing_runs_bypasses_and_records_the_bypass(self):
        _init_repo(self.base)
        (self.base / "gone_v3.json").write_text("{}")
        _git(self.base, "add", "-A")
        _git(self.base, "commit", "-qm", "one")
        (self.base / "gone_v3.json").unlink()
        res = dedb.build_derived_db(self.base, MATRIX, allow_missing_runs=True)
        self.assertEqual(res["meta"]["skew_gate"], "bypassed_allow_missing_runs")
        self.assertEqual(res["meta"]["n_tracked_absent"], "1")

    def test_read_path_predicate_matches_the_indexer(self):
        """Pinned against the indexer's own _is_indexer_read_path (see the
        docstring on this module's copy for why it is duplicated)."""
        idx_path = Path(__file__).resolve().parent / "build_experiment_indexes.py"
        src = idx_path.read_text()
        ns: dict = {}
        start = src.index("def _is_indexer_read_path(")
        end = src.index("\ndef ", start + 1)
        exec(compile(src[start:end], str(idx_path), "exec"), ns)
        theirs = ns["_is_indexer_read_path"]
        corpus = [
            "run_v3.json", "notes.md", "a/runs/r1/manifest.json",
            "a/runs/r1/metrics.csv", "a/b.json", "runs/r1/manifest.json",
            "a/b/c/runs/x/anything", "a/runs.json", "scripts/foo.py",
        ]
        for rel in corpus:
            self.assertEqual(dedb._is_indexer_read_path(rel), theirs(rel), rel)

    # -- content -----------------------------------------------------------

    def test_tables_populated_from_matrix(self):
        dedb.build_derived_db(self.base, MATRIX)
        conn = dedb.open_readonly(self.base)
        self.assertIsNotNone(conn)
        try:
            self.assertEqual(
                conn.execute("SELECT COUNT(*) FROM entries").fetchone()[0], 3)
            self.assertEqual(
                conn.execute("SELECT COUNT(*) FROM claim_rollup").fetchone()[0], 2)
            self.assertEqual(
                conn.execute("SELECT COUNT(*) FROM unlinked_runs").fetchone()[0], 1)
            row = conn.execute(
                "SELECT genuine_exp_count, evidence_quadrant FROM claim_rollup "
                "WHERE claim_id='MECH-457'").fetchone()
            self.assertEqual((row[0], row[1]), (3, "novel_discovery"))
        finally:
            conn.close()

    def test_query_entries_excludes_scoring_excluded_by_default(self):
        dedb.build_derived_db(self.base, MATRIX)
        conn = dedb.open_readonly(self.base)
        try:
            live = dedb.query_entries(conn, claim_id="MECH-457")
            self.assertEqual({e["run_id"] for e in live}, {"r1_v3", "r2_v3"})
            allrows = dedb.query_entries(conn, claim_id="MECH-457",
                                         include_excluded=True)
            self.assertEqual(len(allrows), 3)
            sup = dedb.query_entries(conn, claim_id="MECH-457",
                                     evidence_direction="supports")
            self.assertEqual([e["run_id"] for e in sup], ["r1_v3"])
            hi = dedb.query_entries(conn, claim_id="MECH-457", min_confidence=0.7)
            self.assertEqual([e["run_id"] for e in hi], ["r1_v3"])
        finally:
            conn.close()

    def test_query_entries_is_parameterised_not_interpolated(self):
        """A claim_id carrying SQL must be matched literally, never executed."""
        dedb.build_derived_db(self.base, MATRIX)
        conn = dedb.open_readonly(self.base)
        try:
            rows = dedb.query_entries(conn, claim_id="X'; DROP TABLE entries;--")
            self.assertEqual(rows, [])
            self.assertEqual(
                conn.execute("SELECT COUNT(*) FROM entries").fetchone()[0], 3)
        finally:
            conn.close()

    def test_never_measured_flags_are_distinct_from_measured_empty(self):
        """The distinction manifest_core insists on must survive into the DB.

        never measured -> has_enabled_default_off_flags=0, n=NULL
        measured, none enabled -> 1, 0
        measured, two enabled  -> 1, 2
        Collapsing any pair would make an adoption-coverage query silently wrong.
        """
        runs = {"t": [
            _Run("never_v3", enabled_default_off_flags=None),
            _Run("empty_v3", enabled_default_off_flags={}),
            _Run("two_v3", enabled_default_off_flags={"a.b": True, "c": 1}),
        ]}
        dedb.build_derived_db(self.base, MATRIX, by_experiment=runs)
        conn = dedb.open_readonly(self.base)
        try:
            got = {
                r["run_id"]: (r["has_enabled_default_off_flags"],
                              r["n_enabled_default_off_flags"])
                for r in conn.execute(
                    "SELECT run_id, has_enabled_default_off_flags, "
                    "n_enabled_default_off_flags FROM runs")
            }
        finally:
            conn.close()
        self.assertEqual(got["never_v3"], (0, None))
        self.assertEqual(got["empty_v3"], (1, 0))
        self.assertEqual(got["two_v3"], (1, 2))

    def test_substrate_commit_coverage_is_one_group_by(self):
        """The query the substrate-stability plan needed a corpus re-scan for."""
        runs = {"t": [
            _Run("a_v3", substrate_commit="cafe1"),
            _Run("b_v3", substrate_commit="cafe1"),
            _Run("c_v3", substrate_commit=""),
        ]}
        dedb.build_derived_db(self.base, MATRIX, by_experiment=runs)
        conn = dedb.open_readonly(self.base)
        try:
            n_with = conn.execute(
                "SELECT COUNT(*) FROM runs WHERE substrate_commit != ''").fetchone()[0]
            n_without = conn.execute(
                "SELECT COUNT(*) FROM runs WHERE substrate_commit = ''").fetchone()[0]
        finally:
            conn.close()
        self.assertEqual((n_with, n_without), (2, 1))

    def test_review_tables_mirror_review_tracker_json(self):
        (self.base / "review_tracker.json").write_text(json.dumps({
            "last_review_utc": "2026-01-02T00:00:00Z",
            "reviewed_run_ids": ["r1_v3", "r2_v3"],
            "discussed_experiment_dirs": ["dir_a"],
        }))
        dedb.build_derived_db(self.base, MATRIX)
        conn = dedb.open_readonly(self.base)
        try:
            self.assertEqual(
                {r[0] for r in conn.execute("SELECT run_id FROM review")},
                {"r1_v3", "r2_v3"})
            self.assertEqual(
                [r[0] for r in conn.execute("SELECT dir FROM discussed_dirs")],
                ["dir_a"])
        finally:
            conn.close()

    def test_rebuild_is_idempotent_and_replaces_atomically(self):
        dedb.build_derived_db(self.base, MATRIX)
        first = dedb.derived_db_path(self.base)
        inode = first.stat().st_ino
        dedb.build_derived_db(self.base, MATRIX)
        self.assertNotEqual(first.stat().st_ino, inode,
                            "rebuild must os.replace a fresh file, not mutate in place")
        self.assertFalse(list(first.parent.glob("*.tmp-*")),
                         "no temp file may survive a successful build")
        conn = dedb.open_readonly(self.base)
        try:
            self.assertEqual(
                conn.execute("SELECT COUNT(*) FROM entries").fetchone()[0], 3,
                "a rebuild must not double-insert")
        finally:
            conn.close()

    def test_open_readonly_returns_none_when_absent(self):
        """NEGATIVE CONTROL: absent is a normal state, not an error."""
        self.assertIsNone(dedb.open_readonly(self.base))

    def test_open_readonly_refuses_writes(self):
        dedb.build_derived_db(self.base, MATRIX)
        conn = dedb.open_readonly(self.base)
        try:
            with self.assertRaises(sqlite3.OperationalError):
                conn.execute("DELETE FROM entries")
        finally:
            conn.close()

    def test_claim_summary_rows_are_the_four_explorer_fields(self):
        dedb.build_derived_db(self.base, MATRIX)
        conn = dedb.open_readonly(self.base)
        try:
            rows = dedb.claim_summary_rows(conn)
        finally:
            conn.close()
        self.assertEqual(set(rows), {"MECH-457", "ARC-001"})
        self.assertEqual(
            sorted(rows["MECH-457"]),
            ["evidence_quadrant", "experimental_confidence_decoupled",
             "genuine_exp_count", "literature_confidence_parallel"])

    def test_build_meta_records_the_integrity_verdict(self):
        res = dedb.build_derived_db(self.base, MATRIX, indexer_version="v-test")
        conn = dedb.open_readonly(self.base)
        try:
            meta = dedb.build_meta(conn)
        finally:
            conn.close()
        self.assertEqual(meta["indexer_version"], "v-test")
        self.assertEqual(meta["schema_version"], str(dedb.SCHEMA_VERSION))
        self.assertEqual(meta["n_entries"], "3")
        self.assertEqual(meta["skew_gate"], "not_applicable_no_git")
        self.assertEqual(meta["matrix_schema_version"], "claim_evidence_matrix/v1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
