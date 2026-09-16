"""Contract tests for recover_stranded_run.py -- the path-3 detector and the
sanctioned stranded-run recovery tool.

Two jobs:

1. DETECTOR on the LIVE corpus: every evidence/experiments/*/runs/*/manifest.json
   is experiment_pack/v1 OR is on the explicit allow-list in
   recover_stranded_run.py (path-3 verbatim copies, pre-schema legacy packs).
   A new pack outside the schema fails
   test_live_corpus_has_no_unallowlisted_pack -- that is the point: the count
   cannot grow silently. The fix is to recover through the tool, not to extend
   the list; extending the list is a reviewed decision recorded in
   INTERFACE_CONTRACT.md alongside.

2. TOOL behaviour on synthetic trees: writes a proper 3-file experiment_pack/v1
   pack from a flat manifest; --dry-run writes nothing; refuses to overwrite an
   existing pack (and leaves it byte-identical); refuses an ineligible flat
   (dry-run smoke / wrong epoch); output is ASCII.

Run directly:  python test_recover_stranded_run.py
Or via pytest:  pytest test_recover_stranded_run.py
"""
import contextlib
import io
import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import recover_stranded_run as r  # noqa: E402

LIVE_EVIDENCE_DIR = Path(__file__).resolve().parents[1]
HAS_LIVE_CORPUS = any(LIVE_EVIDENCE_DIR.glob("*/runs/*/manifest.json"))


# --- live-corpus detector ---------------------------------------------------

def test_live_corpus_has_no_unallowlisted_pack():
    """The detector that the 2026-08-08 investigation asked for: path 3 (hand-copying
    a flat manifest into runs/<run_id>/manifest.json) must not be used again."""
    if not HAS_LIVE_CORPUS:
        return  # unit-test context without the evidence tree
    res = r.scan_non_v1_packs(LIVE_EVIDENCE_DIR)
    assert res["total"] > 0
    assert res["unreadable"] == [], res["unreadable"]
    assert res["unexpected"] == [], (
        "pack(s) outside experiment_pack/v1 that are not allow-listed -- recover "
        "stranded runs with recover_stranded_run.py, never by copying the flat "
        "manifest: %r" % (res["unexpected"],))


def test_live_corpus_allowlist_entries_exist_and_are_still_non_v1():
    """Keeps the allow-list honest in both directions: an entry that vanished, or
    was regenerated into experiment_pack/v1 (option B, if ever taken), must be
    removed from the list rather than linger as a stale exemption."""
    if not HAS_LIVE_CORPUS:
        return
    stale = []
    for key in r.ALLOWLIST:
        p = LIVE_EVIDENCE_DIR / key / "manifest.json"
        if not p.is_file():
            stale.append((key, "missing"))
            continue
        sv = json.loads(p.read_text(encoding="utf-8")).get("schema_version")
        if sv == r.PACK_SCHEMA:
            stale.append((key, "now experiment_pack/v1"))
    assert stale == [], "remove from ALLOWLIST (and INTERFACE_CONTRACT.md): %r" % (stale,)


def test_allowlist_size_matches_documented_counts():
    """7 path-3 verbatim copies + 5 pre-schema legacy packs as of 2026-09-16 (the 6
    synthetic-assay manifests were moved out of runs/ the same day and are no longer
    packs). If this changes, the change must be deliberate and documented."""
    assert len(r.PATH3_VERBATIM_COPY_PACKS) == 7
    assert len(r.PRE_SCHEMA_LEGACY_PACKS) == 5
    assert not hasattr(r, "SYNTHETIC_ASSAY_PACKS")
    assert len(r.ALLOWLIST) == 12


def test_live_scan_cli_exits_zero():
    if not HAS_LIVE_CORPUS:
        return
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = r.main(["--scan", "--evidence-dir", str(LIVE_EVIDENCE_DIR)])
    assert code == 0, buf.getvalue()
    assert "OK:" in buf.getvalue()


# --- synthetic-tree helpers -------------------------------------------------

def _flat(run_id, **over):
    d = {
        "run_id": run_id,
        "experiment_type": "v3_exq_999_synthetic_test",
        "architecture_epoch": "ree_hybrid_guardrails_v1",
        "run_timestamp": "20260916T000000Z",
        "status": "PASS",
        "claim_ids_tested": ["MECH-999"],
        "evidence_direction": "supports",
        "experiment_purpose": "evidence",
        "metrics": {"a": 1.0, "b": 2},
        "arm_results": [{"arm": "x"}],
    }
    d.update(over)
    return d


@contextlib.contextmanager
def _tree():
    with tempfile.TemporaryDirectory() as td:
        ev = Path(td) / "evidence" / "experiments"
        ev.mkdir(parents=True)
        yield ev


def _write_flat(ev, run_id, **over):
    p = ev / (run_id + ".json")
    p.write_text(json.dumps(_flat(run_id, **over), indent=2) + "\n", encoding="utf-8")
    return p


def _run(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = r.main(argv)
    return code, buf.getvalue()


# --- recovery ----------------------------------------------------------------

def test_recover_writes_experiment_pack_v1_from_flat():
    with _tree() as ev:
        rid = "v3_exq_999_synthetic_test_20260916T000000Z_v3"
        flat = _write_flat(ev, rid)
        code, out = _run([str(flat), "--evidence-dir", str(ev)])
        assert code == 0, out
        run_dir = ev / "v3_exq_999_synthetic_test" / "runs" / rid
        for name in r.PACK_FILES:
            assert (run_dir / name).is_file(), name
        m = json.loads((run_dir / "manifest.json").read_text())
        assert m["schema_version"] == "experiment_pack/v1"
        assert m["run_id"] == rid
        assert m["claim_ids_tested"] == ["MECH-999"]
        assert "arm_results" not in m  # projected, not a verbatim copy
        assert m != json.loads(flat.read_text())
        met = json.loads((run_dir / "metrics.json").read_text())
        assert met["values"] == {"a": 1.0, "b": 2}
        assert "WROTE" in out
        # the tree is now clean under the detector
        assert r.scan_non_v1_packs(ev)["unexpected"] == []


def test_recovered_pack_is_byte_identical_to_convert_flat_to_runpack():
    """Path 1 (governance.sh's convert_flat_to_runpack) and this tool must agree
    byte-for-byte. The flat is placed in a per-experiment SUBDIR so both writers
    resolve the run dir from the flat's parent and never touch the live tree
    (convert_flat_to_runpack's evidence_dir default is bound at import time to
    the live checkout, so a top-level tmp flat would land THERE)."""
    import sync_v3_results as s
    rid = "v3_exq_999_synthetic_test_20260916T000000Z_v3"
    with _tree() as ev:
        sub = ev / "v3_exq_999_synthetic_test"
        sub.mkdir()
        flat = sub / (rid + ".json")
        flat.write_text(json.dumps(_flat(rid), indent=2) + "\n", encoding="utf-8")
        code, out = _run([str(flat), "--evidence-dir", str(ev)])
        assert code == 0, out
        run_dir = sub / "runs" / rid
        mine = {n: (run_dir / n).read_bytes() for n in r.PACK_FILES}
    with _tree() as ev2:
        sub2 = ev2 / "v3_exq_999_synthetic_test"
        sub2.mkdir()
        flat2 = sub2 / (rid + ".json")
        flat2.write_text(json.dumps(_flat(rid), indent=2) + "\n", encoding="utf-8")
        assert s.convert_flat_to_runpack(flat2) == rid
        run_dir2 = sub2 / "runs" / rid
        assert run_dir2.is_dir(), "convert_flat_to_runpack wrote outside the tmp tree"
        theirs = {n: (run_dir2 / n).read_bytes() for n in r.PACK_FILES}
    assert mine == theirs


def test_dry_run_writes_nothing():
    with _tree() as ev:
        rid = "v3_exq_999_synthetic_test_20260916T000000Z_v3"
        flat = _write_flat(ev, rid)
        code, out = _run(["--dry-run", str(flat), "--evidence-dir", str(ev)])
        assert code == 0, out
        assert "DRY-RUN" in out
        assert not (ev / "v3_exq_999_synthetic_test").exists()


def test_refuses_to_overwrite_existing_pack():
    with _tree() as ev:
        rid = "v3_exq_999_synthetic_test_20260916T000000Z_v3"
        flat = _write_flat(ev, rid)
        run_dir = ev / "v3_exq_999_synthetic_test" / "runs" / rid
        run_dir.mkdir(parents=True)
        curated = b'{"schema_version": "experiment_pack/v1", "status": "SUPERSEDED", "hand": 1}\n'
        (run_dir / "manifest.json").write_bytes(curated)
        code, out = _run([str(flat), "--evidence-dir", str(ev)])
        assert code == 2, out
        assert "REFUSED" in out and "already exists" in out
        assert (run_dir / "manifest.json").read_bytes() == curated
        assert not (run_dir / "metrics.json").exists()
        assert not (run_dir / "summary.md").exists()


def test_refuses_dry_run_smoke_and_wrong_epoch():
    with _tree() as ev:
        smoke = _write_flat(ev, "v3_exq_999_synthetic_test_20260916T000000Z_v3", dry_run=True)
        code, out = _run([str(smoke), "--evidence-dir", str(ev)])
        assert code == 2 and "dry-run" in out, out
        v2 = _write_flat(ev, "v2_thing_20260916T000000Z_v3", architecture_epoch="v2")
        code, out = _run([str(v2), "--evidence-dir", str(ev)])
        assert code == 2 and "architecture_epoch" in out, out
        assert not any(ev.glob("*/runs/*/manifest.json"))


def test_refuses_a_pack_manifest_as_input():
    with _tree() as ev:
        run_dir = ev / "v3_exq_999_synthetic_test" / "runs" / "rid_v3"
        run_dir.mkdir(parents=True)
        p = run_dir / "manifest.json"
        p.write_text(json.dumps(_flat("rid_v3")), encoding="utf-8")
        code, out = _run([str(p), "--evidence-dir", str(ev)])
        assert code == 2 and "already a runs/ pack" in out, out


# --- detector on synthetic trees --------------------------------------------

def test_scan_flags_verbatim_copy_and_passes_allowlisted():
    with _tree() as ev:
        rid = "v3_exq_999_synthetic_test_20260916T000000Z_v3"
        flat = _write_flat(ev, rid)
        run_dir = ev / "v3_exq_999_synthetic_test" / "runs" / rid
        run_dir.mkdir(parents=True)
        (run_dir / "manifest.json").write_bytes(flat.read_bytes())  # path 3, by hand
        res = r.scan_non_v1_packs(ev)
        assert res["total"] == 1 and res["v1"] == 0
        assert len(res["unexpected"]) == 1
        key, reason = res["unexpected"][0]
        assert key == "v3_exq_999_synthetic_test/runs/" + rid
        assert "VERBATIM-COPY" in reason
        code, out = _run(["--scan", "--evidence-dir", str(ev)])
        assert code == 3 and "UNEXPECTED" in out and "FAIL" in out, out
        # same tree, entry allow-listed -> clean
        res2 = r.scan_non_v1_packs(ev, allowlist={key: "test"})
        assert res2["unexpected"] == [] and res2["allowlisted"] == [key]


def test_scan_counts_v1_and_flags_unreadable():
    with _tree() as ev:
        good = ev / "exp_a" / "runs" / "r1"
        good.mkdir(parents=True)
        (good / "manifest.json").write_text('{"schema_version": "experiment_pack/v1"}')
        bad = ev / "exp_b" / "runs" / "r2"
        bad.mkdir(parents=True)
        (bad / "manifest.json").write_text("{not json")
        res = r.scan_non_v1_packs(ev)
        assert res["total"] == 2 and res["v1"] == 1
        assert [k for k, _ in res["unreadable"]] == ["exp_b/runs/r2"]
        code, _ = _run(["--scan", "--evidence-dir", str(ev)])
        assert code == 3


def test_output_is_ascii():
    with _tree() as ev:
        rid = "v3_exq_999_synthetic_test_20260916T000000Z_v3"
        flat = _write_flat(ev, rid, summary_markdown="caf\u00e9 \u2192 done")
        code, out = _run(["--dry-run", str(flat), "--evidence-dir", str(ev)])
        assert code == 0
        out.encode("ascii")  # raises if not ASCII
        code, out = _run(["--scan", "--evidence-dir", str(ev)])
        out.encode("ascii")


if __name__ == "__main__":
    names = [n for n in sorted(globals()) if n.startswith("test_")]
    failed = 0
    for n in names:
        try:
            globals()[n]()
            print("PASS", n)
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print("FAIL", n, "--", exc)
    print("%d/%d passed" % (len(names) - failed, len(names)))
    sys.exit(1 if failed else 0)
