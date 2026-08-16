"""The region <-> experiment join behind the two Explorer read-side panels.

WHAT THIS PINS
--------------
`serve._region_experiment_index()` and `serve._regions_for_claim_ids()` back two
panels that are inverses of each other:

  (A) /brain-map sidebar   -- "which experiments recently touched this region"
  (B) /api/experiment/detail -- "which regions did this run exercise"

Both walk the same three-hop path, entirely over data the governance pipeline
already produces and none of which this code may mutate:

  claim_evidence.v1.json `entries`  (claim_id, run_id, status, timestamp)
    -> claims.yaml `subject`, whose first dotted component is a subject prefix
    -> brain_region_map.yaml `subject_prefixes`, which name the owning region.

THE NEGATIVE CONTROLS ARE THE POINT
-----------------------------------
Roughly half this file asserts what the join must NOT do, because every one of
those is a way the panel silently lies rather than visibly breaks:

  * literature entries must not appear -- they carry a claim_id and a run_id
    exactly like an experimental one, so a join that forgets `source_type`
    reports paper citations as experiment runs;
  * a region row must carry only the claims of THAT region, not every claim the
    run tested, or a multi-region run over-attributes itself everywhere;
  * `recent_experiments_total` must count runs BEFORE the per-region cap, or the
    sidebar reads "12" for a region with 300 runs;
  * prefix matching must be on the full first dotted component -- a `str.startswith`
    shortcut would let region `hipp` swallow `hippocampus`'s claims;
  * every documented failure (missing region map, missing/corrupt evidence index,
    no PyYAML) must degrade to an empty index, since these panels are additive
    and must never take the page down.

Time-independent: every fixture timestamp is a literal written by the test, and
nothing here reads the wall clock or the repository's real evidence tree.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_serve():
    """Import REE_assembly/serve.py under its own name.

    By path rather than `import serve` so the test does not depend on the
    working directory pytest was invoked from; ROOT goes on sys.path because
    serve.py sits beside its vendored modules.
    """
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location("serve", ROOT / "serve.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def serve():
    return load_serve()


# --- fixture data ------------------------------------------------------------
# Two regions and one engineering node. `hipp` exists only as a negative control
# for prefix matching: its prefix is a strict prefix of `hippocampus`'s, so a
# startswith-based join would hand it MECH-001.

REGION_MAP = {
    "schema_version": 1,
    "regions": [
        {"id": "hippocampus", "label": "Hippocampus", "subject_prefixes": ["hippocampus"]},
        {"id": "cingulate", "label": "Cingulate / salience", "subject_prefixes": ["cingulate"]},
        {"id": "hipp_decoy", "label": "Decoy", "subject_prefixes": ["hipp"]},
    ],
    "engineering_nodes": [
        {"id": "control_plane", "label": "Control plane", "subject_prefixes": ["control"]},
    ],
}

CLAIMS = [
    {"id": "MECH-001", "subject": "hippocampus.replay", "title": "replay"},
    # Second hippocampus claim, deliberately with NO entries: it exists only so
    # the inverse join has a region with claim_count 2 to sort above the ties.
    {"id": "MECH-003", "subject": "hippocampus.consolidation", "title": "consolidation"},
    {"id": "MECH-002", "subject": "cingulate.salience", "title": "salience"},
    {"id": "ARC-010", "subject": "control.gating", "title": "gating"},
    {"id": "ORPHAN-1", "subject": "nowhere.at.all", "title": "unmapped"},
    {"id": "NOSUBJ-1", "title": "no subject at all"},
]


def _entry(claim_id, run_id, ts, status="PASS", source_type="experimental", **extra):
    e = {
        "claim_id": claim_id,
        "run_id": run_id,
        "timestamp_utc": ts,
        "status": status,
        "source_type": source_type,
        "experiment_type": run_id[:-3] if run_id.endswith("_v3") else run_id,
        "confidence_rationale": "rationale for " + run_id,
    }
    e.update(extra)
    return e


ENTRIES = [
    # run A: two claims, two DIFFERENT regions -- the over-attribution control.
    _entry("MECH-001", "run_a_20260101T000000Z_v3", "20260101T000000Z"),
    _entry("MECH-002", "run_a_20260101T000000Z_v3", "20260101T000000Z"),
    # run B: newer, one region, carries an interpretation_label (preferred summary).
    _entry("MECH-001", "run_b_20260202T000000Z_v3", "20260202T000000Z",
           status="FAIL", interpretation_label="valid_null_no_replay_effect"),
    # run C: oldest, hippocampus again -- gives the region 3 runs to order and cap.
    _entry("MECH-001", "run_c_20251212T000000Z_v3", "20251212T000000Z", status="ERROR"),
    # a LITERATURE entry shaped exactly like an experimental one: must not appear.
    _entry("MECH-001", "lit_paper_2024", "20260303T000000Z", source_type="literature"),
    # a claim whose subject maps to no region: must not create a region.
    _entry("ORPHAN-1", "run_d_20260104T000000Z_v3", "20260104T000000Z"),
    # engineering-node claim: engineering nodes participate like regions.
    _entry("ARC-010", "run_e_20260105T000000Z_v3", "20260105T000000Z"),
]


@pytest.fixture
def joined(serve, tmp_path, monkeypatch):
    """Point the three source files at a tmp tree and clear the index cache.

    The cache is keyed on (mtime_ns, size) of all three files, so a test that
    only monkeypatched the paths would be served the previous test's index.
    """
    map_file = tmp_path / "brain_region_map.yaml"
    evid_file = tmp_path / "claim_evidence.v1.json"
    claims_file = tmp_path / "claims.yaml"

    yaml = pytest.importorskip("yaml", reason="the region map is YAML")
    map_file.write_text(yaml.safe_dump(REGION_MAP), encoding="utf-8")
    evid_file.write_text(json.dumps({"claims": {}, "entries": ENTRIES}), encoding="utf-8")
    claims_file.write_text(yaml.safe_dump({"claims": CLAIMS}), encoding="utf-8")

    monkeypatch.setattr(serve, "BRAIN_REGION_MAP_FILE", map_file)
    monkeypatch.setattr(serve, "_TL_CLAIM_EVIDENCE", evid_file)
    monkeypatch.setattr(serve, "_TL_CLAIMS_YAML", claims_file)
    monkeypatch.setattr(serve, "_REGION_EXPERIMENTS_CACHE", {"key": None, "index": None})
    monkeypatch.setattr(serve, "_BRAIN_REGION_MAP_CACHE", {"key": None, "doc": {}})
    monkeypatch.setattr(serve, "_TL_CLAIMS_CACHE", {"key": None, "claims": []})
    return {"map": map_file, "evidence": evid_file, "claims": claims_file}


def _rows(serve, region_id):
    return (serve._region_experiment_index()["by_region"]).get(region_id, [])


# --- forward direction: region -> experiments (panel A) -----------------------

def test_region_collects_the_runs_that_tested_its_claims(serve, joined):
    got = {r["run_id"] for r in _rows(serve, "hippocampus")}
    assert got == {
        "run_a_20260101T000000Z_v3",
        "run_b_20260202T000000Z_v3",
        "run_c_20251212T000000Z_v3",
    }


def test_rows_are_newest_first(serve, joined):
    assert [r["run_id"] for r in _rows(serve, "hippocampus")] == [
        "run_b_20260202T000000Z_v3",
        "run_a_20260101T000000Z_v3",
        "run_c_20251212T000000Z_v3",
    ]


def test_row_carries_outcome_and_readable_timestamp(serve, joined):
    row = _rows(serve, "hippocampus")[0]
    assert row["outcome"] == "FAIL"
    assert row["completed_at"] == "2026-02-02T00:00:00Z"
    assert row["timestamp_utc"] == "20260202T000000Z"


def test_summary_prefers_interpretation_label_over_rationale(serve, joined):
    by_run = {r["run_id"]: r for r in _rows(serve, "hippocampus")}
    assert by_run["run_b_20260202T000000Z_v3"]["summary"] == "valid_null_no_replay_effect"
    assert by_run["run_c_20251212T000000Z_v3"]["summary"] == (
        "rationale for run_c_20251212T000000Z_v3"
    )


def test_engineering_nodes_join_like_regions(serve, joined):
    assert [r["run_id"] for r in _rows(serve, "control_plane")] == [
        "run_e_20260105T000000Z_v3"
    ]


# --- forward direction: negative controls ------------------------------------

def test_literature_entries_are_excluded(serve, joined):
    """A lit entry carries claim_id + run_id exactly like an experimental one.

    Dropping the source_type test would render paper citations as experiment
    runs -- with a manifest link that resolves to nothing."""
    all_runs = {
        r["run_id"] for rows in serve._region_experiment_index()["by_region"].values()
        for r in rows
    }
    assert "lit_paper_2024" not in all_runs


def test_a_region_row_carries_only_that_regions_claims(serve, joined):
    """run_a tested MECH-001 (hippocampus) and MECH-002 (cingulate).

    Each region must see only its own; attaching the full run claim set would
    over-attribute every multi-region run to every region it touches."""
    hip = {r["run_id"]: r for r in _rows(serve, "hippocampus")}
    cin = {r["run_id"]: r for r in _rows(serve, "cingulate")}
    assert hip["run_a_20260101T000000Z_v3"]["claim_ids"] == ["MECH-001"]
    assert cin["run_a_20260101T000000Z_v3"]["claim_ids"] == ["MECH-002"]


def test_a_claim_with_no_region_creates_no_region(serve, joined):
    idx = serve._region_experiment_index()
    assert "ORPHAN-1" not in idx["claim_to_regions"]
    all_runs = {r["run_id"] for rows in idx["by_region"].values() for r in rows}
    assert "run_d_20260104T000000Z_v3" not in all_runs


def test_a_claim_with_no_subject_is_skipped(serve, joined):
    assert "NOSUBJ-1" not in serve._region_experiment_index()["claim_to_regions"]


def test_prefix_match_is_the_whole_first_component_not_a_startswith(serve, joined):
    """`hipp` is a strict string prefix of `hippocampus`.

    A startswith-based join would hand the decoy region MECH-001's runs, i.e.
    silently duplicate every hippocampus experiment onto a region that owns
    none of them."""
    idx = serve._region_experiment_index()
    assert idx["claim_to_regions"]["MECH-001"] == ["hippocampus"]
    assert _rows(serve, "hipp_decoy") == []


def test_total_counts_runs_before_the_cap(serve, joined, monkeypatch):
    """The sidebar prints this number; capping it would understate the region."""
    monkeypatch.setattr(serve, "_REGION_EXPERIMENTS_MAX_PER_REGION", 2)
    monkeypatch.setattr(serve, "_REGION_EXPERIMENTS_CACHE", {"key": None, "index": None})
    idx = serve._region_experiment_index()
    assert idx["totals"]["hippocampus"] == 3
    assert len(idx["by_region"]["hippocampus"]) == 2


def test_cap_keeps_the_newest_rows(serve, joined, monkeypatch):
    monkeypatch.setattr(serve, "_REGION_EXPERIMENTS_MAX_PER_REGION", 1)
    monkeypatch.setattr(serve, "_REGION_EXPERIMENTS_CACHE", {"key": None, "index": None})
    assert [r["run_id"] for r in _rows(serve, "hippocampus")] == [
        "run_b_20260202T000000Z_v3"
    ]


# --- inverse direction: run -> regions (panel B) ------------------------------

def test_inverse_join_maps_a_runs_claims_to_regions(serve, joined):
    got = serve._regions_for_claim_ids(["MECH-001", "MECH-002"])
    assert [r["region_id"] for r in got] == ["cingulate", "hippocampus"]
    assert all(r["claim_count"] == 1 for r in got)


def test_inverse_join_orders_by_claim_count_then_region_id(serve, joined):
    got = serve._regions_for_claim_ids(["MECH-001", "MECH-003", "MECH-002", "ARC-010"])
    # hippocampus has 2 -> leads; cingulate and control_plane tie at 1 and are
    # broken by region_id, so the order is stable across runs.
    assert [(r["region_id"], r["claim_count"]) for r in got] == [
        ("hippocampus", 2), ("cingulate", 1), ("control_plane", 1),
    ]


def test_inverse_join_carries_the_regions_label_and_bucket(serve, joined):
    got = serve._regions_for_claim_ids(["ARC-010"])
    assert got == [{
        "region_id": "control_plane",
        "label": "Control plane",
        "bucket": "engineering",
        "claim_ids": ["ARC-010"],
        "claim_count": 1,
    }]


def test_inverse_join_dedupes_a_repeated_claim(serve, joined):
    got = serve._regions_for_claim_ids(["MECH-001", "MECH-001"])
    assert got[0]["claim_ids"] == ["MECH-001"]
    assert got[0]["claim_count"] == 1


@pytest.mark.parametrize("claim_ids", [[], None, ["NOPE-999"], [""], [None]])
def test_inverse_join_is_empty_for_unmapped_or_absent_input(serve, joined, claim_ids):
    assert serve._regions_for_claim_ids(claim_ids) == []


# --- fail-soft: every documented degradation path ----------------------------
# These panels are additive. A missing or malformed source must omit the panel,
# never raise into the request handler and take /api/brain-map down with it.

def _clear(serve, monkeypatch):
    monkeypatch.setattr(serve, "_REGION_EXPERIMENTS_CACHE", {"key": None, "index": None})
    monkeypatch.setattr(serve, "_BRAIN_REGION_MAP_CACHE", {"key": None, "doc": {}})
    monkeypatch.setattr(serve, "_TL_CLAIMS_CACHE", {"key": None, "claims": []})


def test_missing_region_map_yields_an_empty_index(serve, joined, monkeypatch):
    joined["map"].unlink()
    _clear(serve, monkeypatch)
    assert serve._region_experiment_index()["by_region"] == {}
    assert serve._regions_for_claim_ids(["MECH-001"]) == []


def test_missing_evidence_index_yields_no_rows(serve, joined, monkeypatch):
    """The claim->region half must survive: panel B still resolves without runs."""
    joined["evidence"].unlink()
    _clear(serve, monkeypatch)
    idx = serve._region_experiment_index()
    assert idx["by_region"] == {}
    assert idx["claim_to_regions"]["MECH-001"] == ["hippocampus"]


def test_corrupt_evidence_index_yields_no_rows(serve, joined, monkeypatch):
    joined["evidence"].write_text("{not json at all", encoding="utf-8")
    _clear(serve, monkeypatch)
    assert serve._region_experiment_index()["by_region"] == {}


def test_entries_of_the_wrong_shape_are_skipped_not_fatal(serve, joined, monkeypatch):
    joined["evidence"].write_text(json.dumps({
        "entries": ["a string", None, 42, {"claim_id": "MECH-001"}, ENTRIES[0]],
    }), encoding="utf-8")
    _clear(serve, monkeypatch)
    assert [r["run_id"] for r in _rows(serve, "hippocampus")] == [
        "run_a_20260101T000000Z_v3"
    ]


def test_entries_not_a_list_yields_no_rows(serve, joined, monkeypatch):
    joined["evidence"].write_text(json.dumps({"entries": {"nope": 1}}), encoding="utf-8")
    _clear(serve, monkeypatch)
    assert serve._region_experiment_index()["by_region"] == {}


def test_missing_claims_yaml_yields_an_empty_index(serve, joined, monkeypatch):
    joined["claims"].unlink()
    _clear(serve, monkeypatch)
    assert serve._region_experiment_index()["by_region"] == {}


def test_no_pyyaml_yields_an_empty_index(serve, joined, monkeypatch):
    """_brain_load_region_map() returns {} without PyYAML, which must not raise."""
    monkeypatch.setattr(serve, "_YAML_OK", False)
    _clear(serve, monkeypatch)
    assert serve._region_experiment_index()["by_region"] == {}
    assert serve._regions_for_claim_ids(["MECH-001"]) == []


# --- caching ------------------------------------------------------------------

def test_index_is_cached_between_calls(serve, joined):
    assert serve._region_experiment_index() is serve._region_experiment_index()


def test_a_rebuilt_evidence_index_is_picked_up_on_the_next_call(serve, joined):
    """Keyed on mtime+size, not a TTL: a governance rebuild must be visible on
    the very next request, matching _load_claim_evidence_claims()'s contract."""
    before = len(_rows(serve, "hippocampus"))
    joined["evidence"].write_text(json.dumps({"entries": [
        _entry("MECH-001", "run_z_20260909T000000Z_v3", "20260909T000000Z"),
    ]}), encoding="utf-8")
    rows = _rows(serve, "hippocampus")
    assert before == 3
    assert [r["run_id"] for r in rows] == ["run_z_20260909T000000Z_v3"]


# --- manifest link ------------------------------------------------------------

def test_manifest_url_is_the_run_pack_path_when_present(serve, tmp_path, monkeypatch):
    monkeypatch.setattr(serve, "SERVE_DIR", tmp_path)
    p = tmp_path / "evidence" / "experiments" / "some_exp" / "runs" / "some_exp_20260101T000000Z_v3"
    p.mkdir(parents=True)
    (p / "manifest.json").write_text("{}", encoding="utf-8")
    assert serve._region_experiment_manifest_url(
        "some_exp", "some_exp_20260101T000000Z_v3"
    ) == "/evidence/experiments/some_exp/runs/some_exp_20260101T000000Z_v3/manifest.json"


def test_manifest_url_is_empty_when_the_run_pack_is_absent(serve, tmp_path, monkeypatch):
    """A missing manifest drops the LINK, never the row -- the row still carries
    the outcome and claim ids, which is the useful part."""
    monkeypatch.setattr(serve, "SERVE_DIR", tmp_path)
    assert serve._region_experiment_manifest_url("nope", "nope_20260101T000000Z_v3") == ""


@pytest.mark.parametrize("bad", [("", "run_v3"), ("exp", ""), ("", "")])
def test_manifest_url_is_empty_on_missing_components(serve, bad):
    assert serve._region_experiment_manifest_url(*bad) == ""


@pytest.mark.parametrize("compact,expected", [
    ("20260722T041239Z", "2026-07-22T04:12:39Z"),
    ("2026-07-22T04:12:39Z", "2026-07-22T04:12:39Z"),  # already readable: passthrough
    ("", ""),
    ("garbage", "garbage"),
])
def test_timestamp_is_made_readable_without_ever_raising(serve, compact, expected):
    assert serve._region_experiment_readable_ts(compact) == expected
