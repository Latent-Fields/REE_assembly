"""Contract tests for the stamp-only write gate in build_experiment_indexes.py.

WHAT IS BEING PINNED. Every INDEX.md write used to be unconditional, so a full
regen rewrote ~1211 per-experiment INDEX.md files whose entire diff was the
`Generated:` line. That left the shared REE_assembly checkouts permanently
~1218 files dirty (measured 2026-08-08 on ree-cloud-5), which is the
precondition for the escalating git-sync wedge: `pull --rebase --autostash` had
to stash/restore ~1200 files every tick, and ree_git_sync_repair.sh correctly
refuses to auto-repair a checkout with non-telemetry dirt, so it reported
NEEDS_HUMAN every 3h forever. See `_write_index_if_material`'s docstring.

The gate must skip a stamp-only rewrite and must NEVER skip a material one --
the failure directions are asymmetric on purpose, so both are asserted here,
including the fail-open reads.

`test_all_index_writers_route_through_the_gate` is the anti-drift assertion:
the gate is only worth anything if every INDEX.md write site uses it, and a
later edit re-introducing a bare `write_text` at one of them would otherwise be
invisible. It reads the source rather than the behaviour because the four call
sites sit deep inside functions with large fixture requirements. It earned its
keep immediately: it caught the planning-root INDEX.md writer, which the first
pass of this change missed.

The JSON half (`_write_json_if_material`) covers the two artifacts MEASURED to
churn on the stamp alone. One of them, evidence/decisions/decision_state.v1.json,
is the exact path ree_git_sync_repair.sh named in its 2026-08-08T06:14:13Z
NEEDS_HUMAN refusal -- that single file was enough to keep auto-repair disarmed.
Its tests also pin what must NOT be stripped: a per-item `timestamp_utc` is
content, and stripping it would let a real governance change be skipped.

Time-independent (no clock reads); real files in a tempdir.

Run directly:  python test_index_stamp_write_gate.py
Or via pytest:  pytest test_index_stamp_write_gate.py
"""
import json
import os
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build_experiment_indexes as b  # noqa: E402


def _doc(stamp, body="- run alpha\n- run beta"):
    return f"# Experiment Index: demo\n\nGenerated: `{stamp}`\n\n{body}\n"


# --- the skip case: stamp-only difference -------------------------------


def test_stamp_only_difference_is_not_written():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "INDEX.md"
        p.write_text(_doc("2026-08-07T23:57:27.393114Z"), encoding="utf-8")
        wrote = b._write_index_if_material(p, _doc("2026-08-08T09:13:47.000000Z"))
        assert wrote is False


def test_skipped_file_keeps_its_original_bytes():
    """The whole point: no rewrite means no ` M` and no autostash payload."""
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "INDEX.md"
        original = _doc("2026-08-07T23:57:27.393114Z")
        p.write_text(original, encoding="utf-8")
        b._write_index_if_material(p, _doc("2026-08-08T09:13:47.000000Z"))
        assert p.read_text(encoding="utf-8") == original


def test_byte_identical_input_is_not_written():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "INDEX.md"
        p.write_text(_doc("2026-08-07T23:57:27.393114Z"), encoding="utf-8")
        wrote = b._write_index_if_material(p, _doc("2026-08-07T23:57:27.393114Z"))
        assert wrote is False


# --- the write cases: anything material, and every failed read ----------


def test_material_change_is_written_even_with_the_same_stamp():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "INDEX.md"
        stamp = "2026-08-07T23:57:27.393114Z"
        p.write_text(_doc(stamp), encoding="utf-8")
        new = _doc(stamp, body="- run alpha\n- run beta\n- run gamma")
        assert b._write_index_if_material(p, new) is True
        assert p.read_text(encoding="utf-8") == new


def test_material_change_is_written_when_the_stamp_also_moved():
    """The realistic regen: content changed AND the stamp advanced."""
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "INDEX.md"
        p.write_text(_doc("2026-08-07T23:57:27.393114Z"), encoding="utf-8")
        new = _doc("2026-08-08T09:13:47.000000Z", body="- run alpha")
        assert b._write_index_if_material(p, new) is True
        assert p.read_text(encoding="utf-8") == new


def test_absent_file_is_written():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "INDEX.md"
        assert b._write_index_if_material(p, _doc("2026-08-08T09:13:47Z")) is True
        assert p.exists()


def test_undecodable_existing_file_falls_open_to_writing():
    """A bad read must never SUPPRESS a regen -- worst case is one dirty file."""
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "INDEX.md"
        p.write_bytes(b"\xff\xfe\x00 not utf-8 \xc3\x28")
        new = _doc("2026-08-08T09:13:47Z")
        assert b._write_index_if_material(p, new) is True
        assert p.read_text(encoding="utf-8") == new


def test_directory_in_place_of_file_falls_open_and_raises_not_returns_false():
    """An OSError read falls through to the write; the write itself may raise.

    Asserted so the fail-open path is known to REACH the write rather than
    silently returning False -- a silent False here would suppress a real regen.
    """
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "INDEX.md"
        p.mkdir()
        try:
            result = b._write_index_if_material(p, _doc("2026-08-08T09:13:47Z"))
        except (OSError, IsADirectoryError):
            return  # reached the write, which failed loudly -- correct
        assert result is not False


# --- the stamp regex itself ---------------------------------------------


def test_strip_only_touches_the_whole_line_stamp():
    text = "Generated: `2026-01-01T00:00:00Z`\nsee Generated: `x` inline\n"
    stripped = b._strip_generated_stamp(text)
    assert stripped.startswith("Generated: `<stamp>`")
    assert "see Generated: `x` inline" in stripped


def test_a_changed_non_stamp_line_that_mentions_generated_is_material():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "INDEX.md"
        stamp = "2026-08-07T23:57:27.393114Z"
        p.write_text(_doc(stamp, body="This index is generated by `a.py`."),
                     encoding="utf-8")
        new = _doc(stamp, body="This index is generated by `b.py`.")
        assert b._write_index_if_material(p, new) is True


def test_gate_matches_the_igw_routine_tick_stamp_regex():
    """Deliberate shared shape -- see the comment above _GENERATED_STAMP_RE."""
    assert b._GENERATED_STAMP_RE.pattern == r"^Generated: `[^`]*`$"
    assert b._GENERATED_STAMP_RE.flags & re.M


# --- anti-drift: every INDEX.md write site must use the gate ------------


def test_all_index_writers_route_through_the_gate():
    src = Path(b.__file__).read_text(encoding="utf-8")
    stray = re.findall(r'INDEX\.md"\s*\)\s*\.write_text', src)
    assert not stray, (
        "an INDEX.md write site bypasses _write_index_if_material -- "
        "the stamp-only write gate is only effective if ALL of them use it"
    )
    assert src.count("_write_index_if_material(") >= 5  # 1 def + 4 call sites


# --- the JSON gate ------------------------------------------------------


def _state(stamp, items=("a", "b")):
    return json.dumps({"generated_at_utc": stamp, "items": list(items),
                       "schema_version": "decision_state/v1"},
                      indent=2, sort_keys=True) + "\n"


def test_json_stamp_only_difference_is_not_written():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "decision_state.v1.json"
        original = _state("2026-08-07T22:56:39.828281Z")
        p.write_text(original, encoding="utf-8")
        assert b._write_json_if_material(p, _state("2026-08-07T23:57:27.393114Z")) is False
        assert p.read_text(encoding="utf-8") == original


def test_json_material_change_is_written():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "decision_state.v1.json"
        p.write_text(_state("2026-08-07T22:56:39.828281Z"), encoding="utf-8")
        new = _state("2026-08-07T23:57:27.393114Z", items=("a", "b", "c"))
        assert b._write_json_if_material(p, new) is True
        assert p.read_text(encoding="utf-8") == new


def test_json_compare_survives_key_reordering():
    """Parsed compare, not textual -- key order must not force a write."""
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "x.json"
        p.write_text('{"generated_at_utc": "A", "z": 1, "a": 2}\n', encoding="utf-8")
        assert b._write_json_if_material(p, '{"a": 2, "z": 1, "generated_at_utc": "B"}\n') is False


def test_json_unparseable_existing_falls_open_to_writing():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "x.json"
        p.write_text("{ this is not json", encoding="utf-8")
        new = _state("2026-08-08T09:13:47Z")
        assert b._write_json_if_material(p, new) is True
        assert p.read_text(encoding="utf-8") == new


def test_json_absent_file_is_written():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "x.json"
        assert b._write_json_if_material(p, _state("2026-08-08T09:13:47Z")) is True


def test_per_item_timestamps_are_content_not_stamps():
    """A decision entry's own timestamp_utc must NOT be stripped -- stripping
    it would let a real governance change be skipped as immaterial."""
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "x.json"
        p.write_text(json.dumps({"generated_at_utc": "A",
                                 "d": {"timestamp_utc": "2026-01-01T00:00:00Z"}}) + "\n",
                     encoding="utf-8")
        new = json.dumps({"generated_at_utc": "B",
                          "d": {"timestamp_utc": "2026-06-06T00:00:00Z"}}) + "\n"
        assert b._write_json_if_material(p, new) is True


def test_json_stamp_keys_are_only_whole_run_stamps():
    assert b._JSON_RUN_STAMP_KEYS == {"generated_at_utc", "generated_at"}
    assert "timestamp_utc" not in b._JSON_RUN_STAMP_KEYS
    assert "assigned_at" not in b._JSON_RUN_STAMP_KEYS


def test_the_two_measured_json_artifacts_route_through_the_gate():
    """decision_state.v1.json is the path ree_git_sync_repair.sh named in its
    2026-08-08T06:14:13Z NEEDS_HUMAN refusal -- it must stay gated."""
    src = Path(b.__file__).read_text(encoding="utf-8")
    for name in ("decision_state.v1.json", "arm_fingerprint_index.json"):
        assert not re.search(re.escape(name) + r'"\s*\)\s*\.write_text', src), name
        assert name in src


def test_planning_json_artifacts_are_deliberately_not_json_gated():
    """They were measured to carry real content changes beside their stamp, so
    gating them buys nothing and only adds a way to suppress a real write."""
    src = Path(b.__file__).read_text(encoding="utf-8")
    for line in src.splitlines():
        if "_write_json_if_material(" in line and (
                "evidence_backlog" in line or "architecture_gap_register" in line):
            raise AssertionError("planning artifact should not be stamp-gated")


def test_pending_review_is_deliberately_not_gated():
    """verify_governance_cycle.py parses pending_review.md's stamp for
    freshness, so that artifact must keep advancing its stamp every run."""
    src = Path(b.__file__).read_text(encoding="utf-8")
    for line in src.splitlines():
        if "_write_index_if_material(" in line and "pending_review" in line:
            raise AssertionError("pending_review.md must not be stamp-gated")


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"PASS {name}")
            except Exception as exc:  # noqa: BLE001
                failures += 1
                print(f"FAIL {name}: {exc}")
    print(f"\n{failures} failure(s)")
    sys.exit(1 if failures else 0)
