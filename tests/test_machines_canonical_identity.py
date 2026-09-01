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


# ---------------------------------------------------------------------------
# read_merged_runner_status() -- the SECOND endpoint with the same defect.
#
# `/machines` was fixed first (81ee2c7066) and this function deliberately left
# alone to keep that commit's scope. It builds a UNION view rather than one row
# per box, and it keyed on the raw filename stem: `completed` and `queue` were
# always safe (both deduplicate by queue_id) but `current` was not, so one box
# owning two status files contributed the same in-flight experiment twice under
# two `_machine` labels.
#
# LATENT, NOT LIVE when this was written: every status file on disk had
# `current: null`, so `current_list` was empty and nothing duplicated. It fires
# when a file is left holding a non-null `current` (runner killed mid-run) and
# the box then restarts under a different identity spelling.
# ---------------------------------------------------------------------------

@pytest.fixture
def status_only(serve, tmp_path, monkeypatch):
    """Point STATUS_DIR/STATUS_FILE at a tmp tree.

    STATUS_FILE is redirected to a path that does not exist so the monolithic
    fallback cannot fire from the real repo during the per-machine tests; the
    fallback has its own tests below which create it explicitly.
    """
    st_dir = tmp_path / "runner_status"
    monkeypatch.setattr(serve, "STATUS_DIR", st_dir)
    monkeypatch.setattr(serve, "STATUS_FILE", tmp_path / "runner_status.json")
    return st_dir


def _status(now, *, minutes_ago, current=None, idle=True, pid=None,
            completed=(), queue=()):
    return {
        "last_updated": _stamp(now, minutes_ago=minutes_ago),
        "current": current,
        "idle": idle,
        "runner_pid": pid,
        "completed": list(completed),
        "queue": list(queue),
    }


def test_drifted_status_files_yield_one_current_entry(serve, status_only):
    """THE DEFECT. Two files, one box, one in-flight experiment.

    The stale file sorts FIRST alphabetically, so this also pins that the
    survivor is chosen by tick and not by glob order.
    """
    now = datetime.now(timezone.utc)
    _write(status_only, "DLAPTOP-4.local", _status(
        now, minutes_ago=200, idle=False, pid=97092,
        current={"queue_id": "V3-EXQ-930"}))
    _write(status_only, "DLAPTOP", _status(
        now, minutes_ago=1, idle=False, pid=4242,
        current={"queue_id": "V3-EXQ-931"}))

    merged = serve.read_merged_runner_status()

    assert len(merged["current"] and [merged["current"]]) == 1
    assert merged["current"]["queue_id"] == "V3-EXQ-931", (
        "the FRESHER file's in-flight experiment must win")
    assert merged["current"]["_machine"] == "DLAPTOP", (
        "the label must be the canonical identity, not the filename stem")
    assert merged["current_all"] is None, (
        "one physical box must not populate current_all -- that field means "
        "'more than one machine is running', not 'more than one file exists'")


def test_status_merge_follows_the_tick_not_the_filename(serve, status_only):
    """Same two files, freshness reversed. Separates 'picks the fresher' from
    'happens to pick whichever sorts last'."""
    now = datetime.now(timezone.utc)
    _write(status_only, "DLAPTOP-4.local", _status(
        now, minutes_ago=1, idle=False, pid=97092,
        current={"queue_id": "V3-EXQ-932"}))
    _write(status_only, "DLAPTOP", _status(
        now, minutes_ago=200, idle=False, pid=4242,
        current={"queue_id": "V3-EXQ-933"}))

    merged = serve.read_merged_runner_status()

    assert merged["current"]["queue_id"] == "V3-EXQ-932"
    assert merged["current"]["_machine"] == "DLAPTOP"


def test_single_drifted_file_is_relabelled_canonically(serve, status_only):
    """Today's actual board: one `DLAPTOP-4.local.json`, no twin yet. Nothing
    merges, but the label must still be canonical so a consumer cannot re-split
    the box on `_machine` after the twin appears."""
    now = datetime.now(timezone.utc)
    _write(status_only, "DLAPTOP-4.local", _status(
        now, minutes_ago=5, idle=False, pid=97092,
        current={"queue_id": "V3-EXQ-934"}))

    merged = serve.read_merged_runner_status()

    assert merged["current"]["_machine"] == "DLAPTOP"
    assert list(merged["machines"]) == ["DLAPTOP"]


def test_machines_submap_and_runner_pid_key_canonically(serve, status_only):
    """Same defect class in two more fields. `running_machines` counted the two
    files as two boxes, so the `len(...) == 1` backward-compat path -- which
    exists to surface a single running machine's PID -- silently never fired
    for a drifted laptop."""
    now = datetime.now(timezone.utc)
    _write(status_only, "DLAPTOP-4.local", _status(
        now, minutes_ago=200, idle=False, pid=97092))
    _write(status_only, "DLAPTOP", _status(
        now, minutes_ago=1, idle=False, pid=4242))

    merged = serve.read_merged_runner_status()

    assert list(merged["machines"]) == ["DLAPTOP"]
    assert merged["machines"]["DLAPTOP"]["runner_pid"] == 4242
    assert merged["runner_pid"] == 4242, (
        "one box running one runner must expose that PID")


def test_stale_twin_does_not_keep_the_box_looking_busy(serve, status_only):
    """A superseded file is a ghost: the box's live state is the fresh file's.

    Scope note: this is IDENTITY keying, not staleness -- see the companion
    test below, which pins that a lone stale file is deliberately still
    counted."""
    now = datetime.now(timezone.utc)
    _write(status_only, "DLAPTOP-4.local", _status(
        now, minutes_ago=200, idle=False, pid=97092))
    _write(status_only, "DLAPTOP", _status(
        now, minutes_ago=1, idle=True, pid=None))

    merged = serve.read_merged_runner_status()

    assert merged["idle"] is True


def test_a_lone_stale_file_still_counts_as_running(serve, status_only):
    """SCOPE GUARD, passes before and after. `runner_status/DLAPTOP-4.local.json`
    has sat at `idle: false, runner_pid: 97092` since 2026-07-27 and still
    feeds `any_running`. That is a STALENESS bug -- it happens with a single
    file and has nothing to do with identity keying -- and it was deliberately
    NOT fixed here. This pins the boundary so the omission reads as a decision
    rather than an oversight."""
    now = datetime.now(timezone.utc)
    _write(status_only, "DLAPTOP-4.local", _status(
        now, minutes_ago=60 * 24 * 19, idle=False, pid=97092))

    assert serve.read_merged_runner_status()["idle"] is False


def test_history_is_a_union_across_both_drifted_files(serve, status_only):
    """REGRESSION GUARD, passes before and after -- and the reason this function
    is NOT simply passed through `_merge_by_canonical_machine` the way
    /machines is.

    That helper drops the losing payload entirely, which is right for an
    endpoint rendering one ROW per box and wrong here: the superseded twin
    holds real run history the fresh file does not carry (626 completed entries
    in `DLAPTOP-4.local.json` when this was written). Live state collapses;
    history unions."""
    now = datetime.now(timezone.utc)
    _write(status_only, "DLAPTOP-4.local", _status(
        now, minutes_ago=200,
        completed=[{"queue_id": "V3-EXQ-940", "result": "PASS"}],
        queue=[{"queue_id": "V3-EXQ-942"}]))
    _write(status_only, "DLAPTOP", _status(
        now, minutes_ago=1,
        completed=[{"queue_id": "V3-EXQ-941", "result": "PASS"}],
        queue=[{"queue_id": "V3-EXQ-943"}]))

    merged = serve.read_merged_runner_status()

    assert {c["queue_id"] for c in merged["completed"]} == {
        "V3-EXQ-940", "V3-EXQ-941"}, "the stale twin's runs must not vanish"
    assert {q["queue_id"] for q in merged["queue"]} == {
        "V3-EXQ-942", "V3-EXQ-943"}


def test_completed_dedup_still_prefers_non_error_across_drifted_files(
        serve, status_only):
    """The union must keep the existing ERROR-replacement rule, which now runs
    across two files belonging to one box."""
    now = datetime.now(timezone.utc)
    _write(status_only, "DLAPTOP-4.local", _status(
        now, minutes_ago=200,
        completed=[{"queue_id": "V3-EXQ-944", "result": "ERROR"}]))
    _write(status_only, "DLAPTOP", _status(
        now, minutes_ago=1,
        completed=[{"queue_id": "V3-EXQ-944", "result": "PASS"}]))

    merged = serve.read_merged_runner_status()

    assert len(merged["completed"]) == 1
    assert merged["completed"][0]["result"] == "PASS"


# --- NEGATIVE CONTROLS: the numbered fleet must NOT collapse ----------------
# This is the whole point. `machine_identity` is an allowlist, not a
# `-<digits>` regex; without these a later session can widen the predicate and
# turn a duplicate-row cosmetic bug into every machine's status overwriting
# every other machine's.

def test_cloud_fleet_each_keeps_its_own_current_entry(serve, status_only):
    now = datetime.now(timezone.utc)
    fleet_names = [
        "ree-cloud-1", "ree-cloud-2", "ree-cloud-3", "ree-cloud-4",
        "ree-cloud-5", "ree-worker-1", "ree-worker-2", "ree-worker-3",
        "ree-worker-4",
    ]
    for i, name in enumerate(fleet_names):
        _write(status_only, name, _status(
            now, minutes_ago=1, idle=False, pid=1000 + i,
            current={"queue_id": f"V3-EXQ-95{i}"}))

    merged = serve.read_merged_runner_status()

    assert sorted(merged["machines"]) == sorted(fleet_names)
    assert merged["current_all"] is not None
    got = {c["_machine"]: c["queue_id"] for c in merged["current_all"]}
    assert got == {n: f"V3-EXQ-95{i}" for i, n in enumerate(fleet_names)}, (
        "the numbered fleet are DISTINCT machines -- collapsing them would "
        "hide every in-flight experiment but one")


def test_fleet_and_drifted_laptop_coexist(serve, status_only):
    """Neither behaviour may be bought at the other's expense, in one call."""
    now = datetime.now(timezone.utc)
    _write(status_only, "DLAPTOP-4.local", _status(
        now, minutes_ago=200, idle=False, pid=97092,
        current={"queue_id": "V3-EXQ-960"}))
    _write(status_only, "DLAPTOP", _status(
        now, minutes_ago=1, idle=False, pid=4242,
        current={"queue_id": "V3-EXQ-961"}))
    for i in (1, 2, 3):
        _write(status_only, f"ree-cloud-{i}", _status(
            now, minutes_ago=1, idle=False, pid=2000 + i,
            current={"queue_id": f"V3-EXQ-97{i}"}))

    merged = serve.read_merged_runner_status()

    assert sorted(merged["machines"]) == [
        "DLAPTOP", "ree-cloud-1", "ree-cloud-2", "ree-cloud-3"]
    got = {c["_machine"]: c["queue_id"] for c in merged["current_all"]}
    assert got == {
        "DLAPTOP": "V3-EXQ-961",
        "ree-cloud-1": "V3-EXQ-971",
        "ree-cloud-2": "V3-EXQ-972",
        "ree-cloud-3": "V3-EXQ-973",
    }


def test_an_unknown_numbered_host_is_not_collapsed_in_status(
        serve, status_only):
    now = datetime.now(timezone.utc)
    for i in (7, 8):
        _write(status_only, f"buildbox-{i}", _status(
            now, minutes_ago=1, idle=False, pid=3000 + i,
            current={"queue_id": f"V3-EXQ-98{i}"}))

    merged = serve.read_merged_runner_status()

    assert sorted(merged["machines"]) == ["buildbox-7", "buildbox-8"]


# --- the monolithic fallback must be untouched ------------------------------

def test_monolithic_fallback_returns_history_but_never_live_state(
        serve, tmp_path, monkeypatch):
    """The legacy monolith is HISTORY ONLY as of 2026-09-01.

    It used to be returned VERBATIM, which handed the explorer's runner card that
    file's `runner_pid` / `idle` / `current` as CURRENT fleet state. The file has
    been untracked since 2026-03-22 and frozen on disk since 2026-07-20, so what
    that rendered was a months-old snapshot presented as live -- silently, because
    a stale runner card is indistinguishable from a fresh one. `completed` and
    `queue` are real history and are kept (generate_pending_review.py and
    scripts/experiment_error_rate.py both read the same file for exactly that).
    """
    monkeypatch.setattr(serve, "STATUS_DIR", tmp_path / "absent")
    legacy = tmp_path / "runner_status.json"
    legacy.write_text(json.dumps({
        "schema_version": "v1", "runner_pid": 55, "idle": False,
        "current": {"queue_id": "V3-EXQ-STALE"},
        "completed": [{"queue_id": "V3-EXQ-1"}],
        "queue": [{"queue_id": "V3-EXQ-2"}],
    }))
    monkeypatch.setattr(serve, "STATUS_FILE", legacy)

    merged = serve.read_merged_runner_status()

    # History preserved.
    assert merged["completed"] == [{"queue_id": "V3-EXQ-1"}]
    assert merged["queue"] == [{"queue_id": "V3-EXQ-2"}]
    # Live state withheld, and the withholding is declared rather than implicit.
    assert merged["current"] == []
    assert merged["running"] is False
    assert merged["idle"] is True
    assert "runner_pid" not in merged
    assert merged["_legacy_monolithic_fallback"] is True
    assert "_legacy_live_fields_stripped" in merged


def test_monolithic_fallback_does_not_fire_when_per_machine_files_exist(
        serve, tmp_path, monkeypatch):
    now = datetime.now(timezone.utc)
    st_dir = tmp_path / "runner_status"
    monkeypatch.setattr(serve, "STATUS_DIR", st_dir)
    legacy = tmp_path / "runner_status.json"
    legacy.write_text(json.dumps({"runner_pid": 55, "idle": False}))
    monkeypatch.setattr(serve, "STATUS_FILE", legacy)
    _write(st_dir, "DLAPTOP", _status(
        now, minutes_ago=1, idle=False, pid=4242,
        current={"queue_id": "V3-EXQ-990"}))

    merged = serve.read_merged_runner_status()

    assert merged["runner_pid"] == 4242
    assert merged["current"]["queue_id"] == "V3-EXQ-990"


def test_empty_status_dir_and_no_legacy_file_returns_empty(
        serve, tmp_path, monkeypatch):
    monkeypatch.setattr(serve, "STATUS_DIR", tmp_path / "absent")
    monkeypatch.setattr(serve, "STATUS_FILE", tmp_path / "also-absent.json")

    assert serve.read_merged_runner_status() == {}
