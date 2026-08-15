"""/machines must key on CANONICAL machine identity, not the reported hostname.

WHAT THIS PINS
--------------
macOS re-suffixes `LocalHostName` on a Bonjour collision, so across Jul-Aug 2026
one physical laptop reported `DLAPTOP-4.local` and then `DLAPTOP-5.local`. Every
REE coordination path keys on that STRING -- and the Phase-3 heartbeat writer
materialises `runner_heartbeats/<machine>.json` from the coordinator DB without
ever deleting a superseded file, so a re-suffixed box leaves one file per
spelling sitting side by side. `read_machines()` keyed those raw, so /machines
rendered ONE laptop as TWO cards, the stale one ageing into a dead-looking box.

THE NEGATIVE CONTROLS ARE THE POINT
-----------------------------------
`test_cloud_fleet_is_not_collapsed` and its status/coordinator siblings are why
roughly half this file exists. The obvious implementation of the fix -- strip a
trailing `-<digits>` -- would give `ree-cloud-1` .. `-5` and `ree-worker-1` .. `-4`
ONE shared row, i.e. turn a two-card cosmetic bug into a fleet-wide outage in
which every machine's telemetry overwrites every other's. `machine_identity` is
an allowlist precisely to prevent that, and these tests exist to stop a later
session widening the predicate back into it.

Time-independent: every timestamp is written by the test, and `read_machines()`
excludes rows older than MACHINE_STALE_EXCLUDE_HOURS, so fixtures are stamped
relative to a `now` the test computes rather than pinned to a wall-clock date.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_serve():
    """Import REE_assembly/serve.py under its own name.

    Loaded by path rather than by `import serve` so the test does not depend on
    the working directory pytest happened to be invoked from. `serve.py` sits
    beside its vendored `machine_identity.py`, so ROOT goes on sys.path.
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


def _stamp(now: datetime, *, minutes_ago: float) -> str:
    return (now - timedelta(minutes=minutes_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")


def _write(directory: Path, name: str, payload: dict) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / f"{name}.json").write_text(json.dumps(payload))


@pytest.fixture
def fleet(serve, tmp_path, monkeypatch):
    """Point serve.py's telemetry dirs at a tmp tree and force git-only mode.

    `_load_coordinator_cfg` is stubbed empty so `read_machines()` takes the git
    branch and never touches the network; the coordinator branch is exercised
    separately by stubbing the snapshot fetch instead.
    """
    hb_dir = tmp_path / "runner_heartbeats"
    st_dir = tmp_path / "runner_status"
    monkeypatch.setattr(serve, "HEARTBEAT_DIR", hb_dir)
    monkeypatch.setattr(serve, "STATUS_DIR", st_dir)
    monkeypatch.setattr(serve, "_load_coordinator_cfg", lambda: {})
    monkeypatch.delenv("MACHINE_STALE_EXCLUDE_HOURS", raising=False)
    return hb_dir, st_dir


def _machines(serve) -> dict:
    return {m["machine"]: m for m in serve.read_machines()["machines"]}


# ---------------------------------------------------------------------------
# The defect: one laptop, two heartbeat files, must render as ONE row.
# ---------------------------------------------------------------------------

def test_drifted_heartbeat_files_merge_to_one_machine(serve, fleet):
    hb_dir, _ = fleet
    now = datetime.now(timezone.utc)
    # The stale file sorts FIRST alphabetically, so a last-write-wins merge would
    # hand the row to it. That is the specific failure this asserts against.
    _write(hb_dir, "DLAPTOP-4.local", {
        "machine": "DLAPTOP-4.local", "hostname": "DLAPTOP-4.local",
        "last_tick_utc": _stamp(now, minutes_ago=120),
        "state": "idle", "current_exq": None,
    })
    _write(hb_dir, "DLAPTOP", {
        "machine": "DLAPTOP", "hostname": "DLAPTOP",
        "last_tick_utc": _stamp(now, minutes_ago=1),
        "state": "running", "current_exq": "V3-EXQ-900",
    })

    rows = _machines(serve)

    assert list(rows) == ["DLAPTOP"], (
        "one physical laptop must produce exactly one /machines row")
    assert rows["DLAPTOP"]["state"] == "running"
    assert rows["DLAPTOP"]["current_exq"] == "V3-EXQ-900"
    assert rows["DLAPTOP"]["fresh"] is True


def test_merge_prefers_the_fresher_tick_regardless_of_filename_order(
        serve, fleet):
    """Same two files, freshness reversed -- the merge must follow the TICK.

    Sorted glob order is fixed, so this is what separates "picks the fresher"
    from "happens to pick the one that sorts last".
    """
    hb_dir, _ = fleet
    now = datetime.now(timezone.utc)
    _write(hb_dir, "DLAPTOP-4.local", {
        "machine": "DLAPTOP-4.local",
        "last_tick_utc": _stamp(now, minutes_ago=1),
        "state": "running", "current_exq": "V3-EXQ-901",
    })
    _write(hb_dir, "DLAPTOP", {
        "machine": "DLAPTOP",
        "last_tick_utc": _stamp(now, minutes_ago=90),
        "state": "idle", "current_exq": None,
    })

    rows = _machines(serve)

    assert list(rows) == ["DLAPTOP"]
    assert rows["DLAPTOP"]["current_exq"] == "V3-EXQ-901"


def test_a_telemetry_file_with_no_tick_never_beats_one_that_ticked(
        serve, fleet):
    hb_dir, _ = fleet
    now = datetime.now(timezone.utc)
    _write(hb_dir, "DLAPTOP", {
        "machine": "DLAPTOP", "state": "unknown", "current_exq": None})
    _write(hb_dir, "DLAPTOP-5.local", {
        "machine": "DLAPTOP-5.local",
        "last_tick_utc": _stamp(now, minutes_ago=2),
        "state": "running", "current_exq": "V3-EXQ-902",
    })

    rows = _machines(serve)

    assert list(rows) == ["DLAPTOP"]
    assert rows["DLAPTOP"]["current_exq"] == "V3-EXQ-902"


def test_drifted_status_files_merge_too(serve, fleet):
    """Status files are keyed by FILENAME stem only -- no `machine` field to
    fall back on -- so they need the same treatment as heartbeats."""
    _, st_dir = fleet
    now = datetime.now(timezone.utc)
    _write(st_dir, "DLAPTOP-4.local", {
        "idle": True, "current": None,
        "last_updated": _stamp(now, minutes_ago=45)})
    _write(st_dir, "DLAPTOP", {
        "idle": False, "current": "V3-EXQ-903",
        "last_updated": _stamp(now, minutes_ago=1)})

    rows = _machines(serve)

    assert list(rows) == ["DLAPTOP"]
    assert rows["DLAPTOP"]["status_current"] == "V3-EXQ-903"
    assert rows["DLAPTOP"]["status_idle"] is False


def test_heartbeat_and_status_under_different_spellings_join_one_row(
        serve, fleet):
    """The cross-source case: heartbeat written post-fix, status left pre-fix.

    Before the merge these were two rows, each half-populated -- one with
    has_heartbeat and no status, one with has_status and no heartbeat.
    """
    hb_dir, st_dir = fleet
    now = datetime.now(timezone.utc)
    _write(hb_dir, "DLAPTOP", {
        "machine": "DLAPTOP",
        "last_tick_utc": _stamp(now, minutes_ago=1),
        "state": "running", "current_exq": "V3-EXQ-904"})
    _write(st_dir, "DLAPTOP-4.local", {
        "idle": False, "current": "V3-EXQ-904",
        "last_updated": _stamp(now, minutes_ago=1)})

    rows = _machines(serve)

    assert list(rows) == ["DLAPTOP"]
    assert rows["DLAPTOP"]["has_heartbeat"] is True
    assert rows["DLAPTOP"]["has_status"] is True


def test_hostname_is_canonical_and_the_drifted_spelling_is_preserved(
        serve, fleet):
    """`hostname` must not be able to re-split a row that /machines merged --
    but the raw spelling is the signal the split was noticed by, so it survives
    as `hostname_reported` rather than being normalised away silently."""
    hb_dir, _ = fleet
    now = datetime.now(timezone.utc)
    _write(hb_dir, "DLAPTOP", {
        "machine": "DLAPTOP", "hostname": "DLAPTOP-5.local",
        "last_tick_utc": _stamp(now, minutes_ago=1), "state": "idle"})

    row = _machines(serve)["DLAPTOP"]

    assert row["hostname"] == "DLAPTOP"
    assert row["hostname_reported"] == "DLAPTOP-5.local"


def test_hostname_reported_is_absent_when_nothing_drifted(serve, fleet):
    """Negative control for the field above: it is a drift SIGNAL, so it must
    not appear on every ordinary row."""
    hb_dir, _ = fleet
    now = datetime.now(timezone.utc)
    _write(hb_dir, "ree-cloud-2", {
        "machine": "ree-cloud-2", "hostname": "ree-cloud-2",
        "last_tick_utc": _stamp(now, minutes_ago=1), "state": "idle"})

    row = _machines(serve)["ree-cloud-2"]

    assert row["hostname"] == "ree-cloud-2"
    assert "hostname_reported" not in row


# ---------------------------------------------------------------------------
# NEGATIVE CONTROLS -- the cloud fleet must NOT collapse.
# These are the assertions that stop a later session replacing the allowlist
# with a `-<digits>` regex and taking the whole fleet's telemetry down.
# ---------------------------------------------------------------------------

def test_cloud_fleet_is_not_collapsed(serve, fleet):
    hb_dir, _ = fleet
    now = datetime.now(timezone.utc)
    fleet_names = [
        "ree-cloud-1", "ree-cloud-2", "ree-cloud-3", "ree-cloud-4",
        "ree-cloud-5", "ree-worker-1", "ree-worker-2", "ree-worker-3",
        "ree-worker-4",
    ]
    for i, name in enumerate(fleet_names):
        _write(hb_dir, name, {
            "machine": name, "hostname": name,
            "last_tick_utc": _stamp(now, minutes_ago=1),
            "state": "running", "current_exq": f"V3-EXQ-9{i:02d}"})

    rows = _machines(serve)

    assert sorted(rows) == sorted(fleet_names), (
        "the numbered cloud fleet are DISTINCT machines -- collapsing them "
        "would give the whole fleet one shared row")
    for i, name in enumerate(fleet_names):
        assert rows[name]["current_exq"] == f"V3-EXQ-9{i:02d}", (
            f"{name} must keep its own in-flight experiment")


def test_cloud_fleet_status_files_are_not_collapsed(serve, fleet):
    _, st_dir = fleet
    now = datetime.now(timezone.utc)
    for i in (1, 2, 3, 4):
        _write(st_dir, f"ree-cloud-{i}", {
            "idle": False, "current": f"V3-EXQ-91{i}",
            "last_updated": _stamp(now, minutes_ago=1)})

    rows = _machines(serve)

    assert sorted(rows) == [f"ree-cloud-{i}" for i in (1, 2, 3, 4)]


def test_an_unknown_numbered_host_is_not_collapsed(serve, fleet):
    """A base that is NOT in SUFFIX_BLIND_BASES keeps its suffix. Pins that the
    merge is opt-in per machine rather than applied to anything numbered."""
    hb_dir, _ = fleet
    now = datetime.now(timezone.utc)
    for name in ("buildbox-7", "buildbox-8"):
        _write(hb_dir, name, {
            "machine": name,
            "last_tick_utc": _stamp(now, minutes_ago=1), "state": "idle"})

    assert sorted(_machines(serve)) == ["buildbox-7", "buildbox-8"]


def test_laptop_and_cloud_fleet_coexist(serve, fleet):
    """The realistic board: the drifted laptop merges while the fleet does not,
    in one call. Neither behaviour may be bought at the other's expense."""
    hb_dir, _ = fleet
    now = datetime.now(timezone.utc)
    _write(hb_dir, "DLAPTOP-4.local", {
        "machine": "DLAPTOP-4.local",
        "last_tick_utc": _stamp(now, minutes_ago=30), "state": "idle"})
    _write(hb_dir, "DLAPTOP", {
        "machine": "DLAPTOP",
        "last_tick_utc": _stamp(now, minutes_ago=1), "state": "running"})
    for i in (1, 2, 3):
        _write(hb_dir, f"ree-cloud-{i}", {
            "machine": f"ree-cloud-{i}",
            "last_tick_utc": _stamp(now, minutes_ago=1), "state": "running"})

    assert sorted(_machines(serve)) == [
        "DLAPTOP", "ree-cloud-1", "ree-cloud-2", "ree-cloud-3"]


# ---------------------------------------------------------------------------
# The coordinator branch -- a second, independently-keyed source of rows.
# ---------------------------------------------------------------------------

def test_coordinator_snapshots_merge_by_canonical_identity(
        serve, tmp_path, monkeypatch):
    """The DB holds rows under every hostname a box has ever reported, so the
    coordinator path needs the same merge -- and it is applied inside the
    fetch, because that dict is cached and cached raw keys would re-split the
    laptop on every cache hit."""
    now = datetime.now(timezone.utc)
    monkeypatch.setattr(serve, "HEARTBEAT_DIR", tmp_path / "hb")
    monkeypatch.setattr(serve, "STATUS_DIR", tmp_path / "st")
    monkeypatch.setattr(serve, "_load_coordinator_cfg", lambda: {
        "COORDINATOR_URL": "http://10.8.0.1:8787",
        "COORDINATOR_LOCAL_TOKEN": "test-token"})
    monkeypatch.setattr(serve, "_fetch_coordinator_machine_snapshots",
                        lambda cfg: serve._merge_by_canonical_machine({
                            "DLAPTOP-4.local": {
                                "last_tick_utc": _stamp(now, minutes_ago=60),
                                "state": "idle", "current_exq": None},
                            "DLAPTOP": {
                                "last_tick_utc": _stamp(now, minutes_ago=1),
                                "state": "running",
                                "current_exq": "V3-EXQ-920"},
                            "ree-cloud-1": {
                                "last_tick_utc": _stamp(now, minutes_ago=1),
                                "state": "running",
                                "current_exq": "V3-EXQ-921"},
                            "ree-cloud-2": {
                                "last_tick_utc": _stamp(now, minutes_ago=1),
                                "state": "running",
                                "current_exq": "V3-EXQ-922"},
                        }, "last_tick_utc"))

    rows = _machines(serve)

    assert sorted(rows) == ["DLAPTOP", "ree-cloud-1", "ree-cloud-2"]
    assert rows["DLAPTOP"]["current_exq"] == "V3-EXQ-920"
    assert rows["ree-cloud-1"]["current_exq"] == "V3-EXQ-921"
    assert rows["ree-cloud-2"]["current_exq"] == "V3-EXQ-922"


# ---------------------------------------------------------------------------
# Command delivery -- keyed by the same identity the runner polls under.
# ---------------------------------------------------------------------------

def test_commands_file_is_canonical_for_every_spelling(serve):
    paths = {serve._commands_file(n)
             for n in ("DLAPTOP", "DLAPTOP-4.local", "DLAPTOP-5.local")}
    assert len(paths) == 1, (
        "a command issued against a drifted spelling must land in the file "
        "runner_remote_control.get_machine_id() actually polls")
    assert paths.pop().name == "DLAPTOP.json"


def test_commands_file_keeps_the_cloud_fleet_separate(serve):
    paths = [serve._commands_file(f"ree-cloud-{i}") for i in (1, 2, 3, 4, 5)]
    assert len({p.name for p in paths}) == 5


# ---------------------------------------------------------------------------
# The vendored copy is the same file as ree-v3's canonical one.
# ---------------------------------------------------------------------------

def test_vendored_machine_identity_is_byte_identical_to_ree_v3():
    """Vendoring is the design (a cross-repo sys.path hop breaks on the hub and
    the cloud workers). This is what keeps it safe. Skips rather than fails
    where ree-v3 is not checked out -- the hub and the workers have only one
    repo, and "cannot see the sibling" is not the same claim as "they differ";
    scripts/audit_vendored_copies.py is the gate that sees all copies at once.
    """
    vendored = ROOT / "machine_identity.py"
    canonical = ROOT.parent / "ree-v3" / "machine_identity.py"
    if not canonical.exists():
        pytest.skip("ree-v3 not checked out beside REE_assembly")
    assert vendored.read_bytes() == canonical.read_bytes(), (
        "re-vendor with: cp ree-v3/machine_identity.py "
        "REE_assembly/machine_identity.py  (canonical -> copy, never reverse)")
