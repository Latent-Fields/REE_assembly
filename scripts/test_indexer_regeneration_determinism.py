#!/usr/bin/env python3
"""Contract tests: build_experiment_indexes.py is REGENERATION-DETERMINISTIC.

The property under test: rebuilding the indexes over an unchanged corpus must
produce byte-identical derived artifacts apart from the generation stamp
(`Generated:` / `generated_at`). Nothing pinned this before, and it was
violated.

INCIDENT (2026-07-27). Two indexer runs 36 minutes apart on the same corpus
produced different derived artifacts for 107 index files, and the 06:12Z
regeneration committed 226 (claim, run) `timestamp_utc` modifications with no
underlying data change. Root cause: `_parse_timestamp` fell back to the
manifest file's **mtime** when `timestamp_utc` was blank. 131 of 2645 run-pack
manifests have a blank timestamp, and 29 experiment types hold more than one
such run, so:

  1. `latest_run_id` -- selected as the last element of a
     (timestamp_utc, run_id) sort -- ordered those runs by mtime, which bears
     no relation to when the run happened and changes on any checkout. It
     flipped to an EARLIER run between rebuilds
     (v3_exq_060_arc016_beta_gate_fixed_threshold: 20260321T131836Z ->
     20260321T131212Z). `latest_run_id` is a field of
     claim_evidence.v1.json, so the run designated as a claim's most recent
     evidence changed on a rebuild.
  2. The durable `timestamp_utc` column was written with an mtime, i.e. a
     regeneration time -- a wall-clock value that looks authoritative and
     changes every build.

FIX: `_parse_timestamp` resolves declared timestamp -> timestamp embedded in
the record's own identifier -> explicit unknown ("" + epoch-0 sentinel). No
wall-clock or mtime fallback at any point.

Run: /opt/local/bin/python3 scripts/test_indexer_regeneration_determinism.py
"""

import importlib.util
import json
import os
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


# --------------------------------------------------------------------------
# Fixture corpus
# --------------------------------------------------------------------------

def _write_run_pack(base_dir: Path, experiment_type: str, run_id: str,
                    *, timestamp_utc: str, claim_ids, status: str = "PASS",
                    direction: str = "supports", mtime: float | None = None):
    """Materialise one evidence/experiments/<type>/runs/<run_id>/ pack."""
    run_dir = base_dir / experiment_type / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "run_id": run_id,
        "experiment_type": experiment_type,
        "timestamp_utc": timestamp_utc,
        "architecture_epoch": "ree_hybrid_guardrails_v1",
        "status": status,
        "outcome": status,
        "claim_ids_tested": list(claim_ids),
        "evidence_direction": direction,
        "experiment_purpose": "evidence",
        "artifacts": {"metrics_path": "metrics.json", "summary_path": "summary.md"},
    }
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (run_dir / "metrics.json").write_text(
        json.dumps({"values": {"score": 0.5}}, indent=2) + "\n")
    (run_dir / "summary.md").write_text(f"# {run_id}\n")
    if mtime is not None:
        for name in ("manifest.json", "metrics.json", "summary.md"):
            os.utime(run_dir / name, (mtime, mtime))


def _epoch(y, m, d, hh=0, mm=0, ss=0) -> float:
    return datetime(y, m, d, hh, mm, ss, tzinfo=timezone.utc).timestamp()


def _build_fixture_corpus(base_dir: Path, *, mtime_scheme: str):
    """A corpus that reproduces the incident.

    Every experiment type below holds >1 run and >=1 run with a BLANK
    `timestamp_utc` -- the 29-experiment-type population from the incident.
    `mtime_scheme` picks which wall-clock the files carry, so the two builds
    in the determinism test see different mtimes for identical content (what
    a checkout, an rsync, or a pack-heal does in the live repo).
    """
    a, b = (_epoch(2026, 5, 1), _epoch(2026, 4, 18)) if mtime_scheme == "one" \
        else (_epoch(2026, 7, 27, 6, 12), _epoch(2026, 7, 27, 5, 36))

    # 1. Both runs blank, run_id carries a compact ...Z stamp. This is the
    #    v3_exq_060 shape: the mtimes are deliberately INVERTED against the
    #    real run order, so an mtime-ordered build picks the earlier run.
    _write_run_pack(base_dir, "exp_compact_z",
                    "20260321T131212Z_exp_compact_z_v3",
                    timestamp_utc="", claim_ids=["MECH-001"], mtime=a)
    _write_run_pack(base_dir, "exp_compact_z",
                    "20260321T131836Z_exp_compact_z_v3",
                    timestamp_utc="", claim_ids=["MECH-001"], mtime=b)

    # 2. Trailing compact stamp without the Z suffix (v3_exq_163 shape).
    _write_run_pack(base_dir, "exp_compact_noz",
                    "exp_compact_noz_20260329T203824_v3",
                    timestamp_utc="", claim_ids=["MECH-002"], mtime=a)
    _write_run_pack(base_dir, "exp_compact_noz",
                    "exp_compact_noz_20260330T090000_v3",
                    timestamp_utc="", claim_ids=["MECH-002"], mtime=b)

    # 3. Epoch-seconds suffix (v3_exq_207/208 shape).
    _write_run_pack(base_dir, "exp_epoch", "exp_epoch_probe_1775167615_v3",
                    timestamp_utc="", claim_ids=["MECH-003"], mtime=a)
    _write_run_pack(base_dir, "exp_epoch", "exp_epoch_probe_1775181944_v3",
                    timestamp_utc="", claim_ids=["MECH-003"], mtime=b)

    # 4. No recoverable stamp anywhere (v3_exq_255/256 shape) -- must resolve
    #    to an explicit unknown, deterministically, never to a wall clock.
    _write_run_pack(base_dir, "exp_unknown", "exp_unknown_alpha_v3",
                    timestamp_utc="", claim_ids=["MECH-004"], mtime=a)
    _write_run_pack(base_dir, "exp_unknown", "exp_unknown_beta_v3",
                    timestamp_utc="", claim_ids=["MECH-004"], mtime=b)

    # 5. Mixed: one dated run, one blank. The dated run must win regardless
    #    of mtime, and the blank run must not displace it.
    _write_run_pack(base_dir, "exp_mixed", "exp_mixed_dated_v3",
                    timestamp_utc="2026-04-02T10:00:00Z",
                    claim_ids=["MECH-005"], mtime=b)
    _write_run_pack(base_dir, "exp_mixed",
                    "20260401T080000Z_exp_mixed_blank_v3",
                    timestamp_utc="", claim_ids=["MECH-005"], mtime=a)

    # 6. Control: both runs fully dated. Must be untouched by the fix.
    _write_run_pack(base_dir, "exp_dated", "exp_dated_first_v3",
                    timestamp_utc="2026-03-01T09:00:00Z",
                    claim_ids=["MECH-006"], mtime=a)
    _write_run_pack(base_dir, "exp_dated", "exp_dated_second_v3",
                    timestamp_utc="2026-03-02T09:00:00Z",
                    claim_ids=["MECH-006"], mtime=b)


def _regenerate(corpus: Path, generated_at: str) -> dict:
    by_experiment = IDX._scan_runs(corpus, {})
    return IDX._write_claim_evidence_matrix(
        base_dir=corpus,
        by_experiment=by_experiment,
        by_literature={},
        generated_at=generated_at,
        planning_criteria={},
    )


def _serialize(matrix: dict) -> str:
    return json.dumps(matrix, sort_keys=True, indent=2, default=str)


def _claim(matrix: dict, claim_id: str) -> dict:
    return matrix["claims"][claim_id]


# --------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------

class TimestampFromIdentifierTests(unittest.TestCase):
    """The data-derived tiebreak source: a stamp inside the run_id."""

    def test_compact_with_z(self):
        raw, dt = IDX._timestamp_from_identifier(
            "20260321T131836Z_v3_exq_060_arc016_beta_gate_fixed_threshold_v3")
        self.assertEqual(raw, "2026-03-21T13:18:36Z")
        self.assertEqual(dt, datetime(2026, 3, 21, 13, 18, 36, tzinfo=timezone.utc))

    def test_compact_without_z(self):
        raw, _ = IDX._timestamp_from_identifier(
            "v3_exq_163_mech141_dual_timescale_arbitration_20260329T203824_v3")
        self.assertEqual(raw, "2026-03-29T20:38:24Z")

    def test_epoch_seconds_suffix(self):
        raw, dt = IDX._timestamp_from_identifier(
            "v3_exq_208_arc022_hierarchical_pipeline_probe_1775182116_v3")
        self.assertEqual(dt, datetime.fromtimestamp(1775182116, tz=timezone.utc))
        self.assertTrue(raw.endswith("Z"))

    def test_emits_iso_form_so_string_sorts_agree_with_declared(self):
        """Derived stamps must sort against declared ISO stamps correctly.

        A compact `20260321T131836Z` string sorts BEFORE any `2026-...` ISO
        string ('-' < '0'), so emitting the compact form would make every
        derived timestamp look older than every declared one.
        """
        derived, _ = IDX._timestamp_from_identifier("20260321T131836Z_x_v3")
        self.assertLess("2026-03-21T13:18:35Z", derived)
        self.assertGreater("2026-03-21T13:18:37Z", derived)

    def test_hex_and_short_suffixes_are_not_mistaken_for_a_time(self):
        for ident in (
            "v3_exq_164a_mech142_axis_decorrelation_a7622089_v3",
            "v3_exq_162_mech137_commit_token_structure_9e3b4eaa_v3",
            "v3_exq_028_proxy_gradient_world_validation_s0_v3",
            "v3_exq_255_mech203_benefit_tagging_v3",
        ):
            self.assertIsNone(IDX._timestamp_from_identifier(ident), ident)

    def test_empty_identifier(self):
        self.assertIsNone(IDX._timestamp_from_identifier(""))


class ParseTimestampTests(unittest.TestCase):
    """No wall-clock fallback, ever."""

    def test_declared_timestamp_wins(self):
        raw, dt = IDX._parse_timestamp("2026-05-01T12:00:00Z", "20260321T131836Z_x_v3")
        self.assertEqual(raw, "2026-05-01T12:00:00Z")
        self.assertEqual(dt, datetime(2026, 5, 1, 12, 0, 0, tzinfo=timezone.utc))

    def test_blank_falls_back_to_identifier(self):
        raw, _ = IDX._parse_timestamp("", "20260321T131836Z_x_v3")
        self.assertEqual(raw, "2026-03-21T13:18:36Z")

    def test_unparseable_declared_falls_back_to_identifier(self):
        raw, _ = IDX._parse_timestamp("not-a-date", "20260321T131836Z_x_v3")
        self.assertEqual(raw, "2026-03-21T13:18:36Z")

    def test_genuinely_unknown_emits_empty_marker_not_a_clock(self):
        raw, dt = IDX._parse_timestamp("", "v3_exq_255_mech203_benefit_tagging_v3")
        self.assertEqual(raw, "")
        self.assertEqual(dt, IDX._UNKNOWN_TIMESTAMP_DT)
        # The whole point: not a regeneration time.
        self.assertLess(dt, datetime(2020, 1, 1, tzinfo=timezone.utc))

    def test_unknown_is_stable_across_calls(self):
        self.assertEqual(IDX._parse_timestamp("", "abc_v3"),
                         IDX._parse_timestamp("", "abc_v3"))

    def test_no_mtime_fallback_remains(self):
        """Signature no longer accepts a path to stat -- regression guard."""
        raw, _ = IDX._parse_timestamp("", "")
        self.assertEqual(raw, "")


class RegenerationDeterminismTests(unittest.TestCase):
    """The property the incident violated."""

    # The generation stamp is held FIXED across the two builds on purpose.
    # `generated_at` is the pipeline's `now`, and recency decay / posterior
    # weighting read it by design -- a later build legitimately scores an
    # ageing corpus lower. That clock-dependence is not the defect. The defect
    # is dependence on anything ELSE that moves between builds, which for the
    # incident was file mtime. So: same corpus, same stamp, different mtimes.

    STAMP = "2026-07-27T06:12:00Z"

    def test_two_builds_over_same_corpus_are_byte_identical(self):
        with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
            # Identical content, different mtimes -- what a checkout produces.
            _build_fixture_corpus(Path(d1), mtime_scheme="one")
            _build_fixture_corpus(Path(d2), mtime_scheme="two")
            first = _regenerate(Path(d1), self.STAMP)
            second = _regenerate(Path(d2), self.STAMP)
            self.assertEqual(_serialize(first), _serialize(second))

    def test_rebuild_in_place_after_touching_mtimes_is_byte_identical(self):
        """The literal incident shape: rebuild the same tree twice."""
        with tempfile.TemporaryDirectory() as d:
            corpus = Path(d)
            _build_fixture_corpus(corpus, mtime_scheme="one")
            first = _regenerate(corpus, self.STAMP)
            # A checkout / rsync / pack-heal rewrites files without changing
            # their content. Only mtime moves.
            touched = _epoch(2026, 7, 27, 6, 12)
            for path in corpus.rglob("*.json"):
                os.utime(path, (touched, touched))
            second = _regenerate(corpus, self.STAMP)
            self.assertEqual(_serialize(first), _serialize(second))

    def test_generation_stamp_is_the_only_clock_in_the_output(self):
        """Two builds an hour apart differ ONLY in clock-derived scoring.

        Ordering and identity fields -- entry order, run ids, timestamps,
        `latest_run_id` -- must be bit-identical regardless of build time.
        """
        with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
            _build_fixture_corpus(Path(d1), mtime_scheme="one")
            _build_fixture_corpus(Path(d2), mtime_scheme="two")
            first = _regenerate(Path(d1), "2026-07-27T05:36:00Z")
            second = _regenerate(Path(d2), "2026-07-27T06:12:00Z")
            spine = lambda m: [  # noqa: E731
                (e["run_id"], e["claim_id"], e["timestamp_utc"]) for e in m["entries"]
            ]
            self.assertEqual(spine(first), spine(second))
            self.assertEqual(
                {c: v["latest_run_id"] for c, v in first["claims"].items()},
                {c: v["latest_run_id"] for c, v in second["claims"].items()})

    def test_latest_run_id_is_stable_and_data_derived(self):
        """The exact v3_exq_060 flip: mtimes inverted against real run order."""
        with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
            _build_fixture_corpus(Path(d1), mtime_scheme="one")
            _build_fixture_corpus(Path(d2), mtime_scheme="two")
            first = _regenerate(Path(d1), "2026-07-27T05:36:00Z")
            second = _regenerate(Path(d2), "2026-07-27T06:12:00Z")
            for claim_id, expected in (
                ("MECH-001", "20260321T131836Z_exp_compact_z_v3"),
                ("MECH-002", "exp_compact_noz_20260330T090000_v3"),
                ("MECH-003", "exp_epoch_probe_1775181944_v3"),
                ("MECH-005", "exp_mixed_dated_v3"),
                ("MECH-006", "exp_dated_second_v3"),
            ):
                self.assertEqual(_claim(first, claim_id)["latest_run_id"], expected,
                                 f"{claim_id} build 1")
                self.assertEqual(_claim(second, claim_id)["latest_run_id"], expected,
                                 f"{claim_id} build 2")

    def test_all_unknown_experiment_falls_back_to_lexicographic_run_id(self):
        with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
            _build_fixture_corpus(Path(d1), mtime_scheme="one")
            _build_fixture_corpus(Path(d2), mtime_scheme="two")
            first = _regenerate(Path(d1), "2026-07-27T05:36:00Z")
            second = _regenerate(Path(d2), "2026-07-27T06:12:00Z")
            # Both blank + both unrecoverable => stable lexicographic pick.
            self.assertEqual(_claim(first, "MECH-004")["latest_run_id"],
                             "exp_unknown_beta_v3")
            self.assertEqual(_claim(second, "MECH-004")["latest_run_id"],
                             "exp_unknown_beta_v3")

    def test_no_entry_carries_a_regeneration_time(self):
        """No `timestamp_utc` in a derived artifact may be a build clock."""
        with tempfile.TemporaryDirectory() as d:
            _build_fixture_corpus(Path(d), mtime_scheme="two")
            matrix = _regenerate(Path(d), "2026-07-27T06:12:00Z")
            build_day = "2026-07-27"
            for entry in matrix["entries"]:
                ts = str(entry.get("timestamp_utc", ""))
                self.assertFalse(
                    ts.startswith(build_day),
                    f"{entry['run_id']} carries a regeneration time: {ts!r}")

    def test_unknown_run_reports_empty_timestamp_not_a_clock(self):
        with tempfile.TemporaryDirectory() as d:
            _build_fixture_corpus(Path(d), mtime_scheme="two")
            matrix = _regenerate(Path(d), "2026-07-27T06:12:00Z")
            unknown = [e for e in matrix["entries"]
                       if e["run_id"].startswith("exp_unknown_")]
            self.assertEqual(len(unknown), 2)
            for entry in unknown:
                self.assertEqual(entry["timestamp_utc"], "")

    def test_recovered_timestamps_are_the_run_id_stamps(self):
        with tempfile.TemporaryDirectory() as d:
            _build_fixture_corpus(Path(d), mtime_scheme="two")
            matrix = _regenerate(Path(d), "2026-07-27T06:12:00Z")
            by_run = {e["run_id"]: e["timestamp_utc"] for e in matrix["entries"]}
            self.assertEqual(by_run["20260321T131836Z_exp_compact_z_v3"],
                             "2026-03-21T13:18:36Z")
            self.assertEqual(by_run["exp_compact_noz_20260329T203824_v3"],
                             "2026-03-29T20:38:24Z")
            self.assertEqual(by_run["exp_dated_second_v3"], "2026-03-02T09:00:00Z")


class RecencyScoreUnknownTimestampTests(unittest.TestCase):
    """An explicit-unknown timestamp contributes no recency signal.

    `_recency_score` previously called `_parse_timestamp_only` unguarded,
    which raised on the empty marker the fix now emits.
    """

    NOW = datetime(2026, 7, 27, 6, 0, 0, tzinfo=timezone.utc)

    def test_all_unknown_scores_zero_instead_of_raising(self):
        entries = [{"timestamp_utc": ""}, {"timestamp_utc": ""}]
        self.assertEqual(IDX._recency_score(entries, self.NOW, 90), 0.0)

    def test_unknown_entries_are_skipped_not_treated_as_now(self):
        dated = {"timestamp_utc": "2026-07-01T00:00:00Z"}
        self.assertEqual(
            IDX._recency_score([dated], self.NOW, 90),
            IDX._recency_score([dated, {"timestamp_utc": ""}], self.NOW, 90))

    def test_unparseable_entry_is_skipped(self):
        self.assertEqual(
            IDX._recency_score([{"timestamp_utc": "garbage"}], self.NOW, 90), 0.0)

    def test_empty_entry_list_unchanged(self):
        self.assertEqual(IDX._recency_score([], self.NOW, 90), 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
