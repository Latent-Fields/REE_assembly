#!/usr/bin/env python3
"""Contract for audit_blocked_proposal_unblockers.py's READY verdict.

WHAT THIS GUARDS
----------------
READY is a NEGATIVE INSTRUMENT: it authorises a human to START work (return a
proposal to `proposed`) on the strength of "no unsatisfied blocker remains".
On 2026-09-23 a per-proposal audit found all 12 READY rows were false
positives -- every one failed a release condition the script never read. Per
CLAUDE.md "Negative instruments", the remedy is an explicit cannot-determine
CATEGORY (READY_UNVERIFIED), and per "The test half" that remedy needs a test
that the OLD code FAILS.

The three false-positive shapes, each pinned below against a FIXTURE so the
test does not rot as the live registry moves:

  A. stated release condition -- blocker statuses satisfied, but the proposal
     states its own (stronger) release test in prose.
  B. ambiguous multi-entry   -- a blocker named as a CLAIM id resolves through
     several substrate_queue entries that disagree; the old code took the
     first and ignored the rest.
  C. self-block              -- the blocker id IS the proposal's own claim_id
     (a claims.yaml queue gate), and may collide with an unrelated sd_id.

Plus two properties over the LIVE registry, written as invariants rather than
pinned counts so they survive governance moving the data:

  * no proposal carrying a stated condition is ever in READY;
  * the UNOWNED census is not reduced by the new bucket (a regression this
    change actually introduced once and had to fix: 49 -> 42).

Run: /opt/local/bin/python3 -m pytest scripts/test_audit_blocked_proposal_unblockers.py -q
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import audit_blocked_proposal_unblockers as aud  # noqa: E402


# --------------------------------------------------------------------------
# fixture: the smallest registry pair that reproduces all three shapes
# --------------------------------------------------------------------------
def _write_fixture(tmp_path: Path) -> Path:
    planning = tmp_path / "evidence" / "planning"
    planning.mkdir(parents=True)
    (planning / "substrate_queue.json").write_text(json.dumps({"queue": [
        {"sd_id": "SD-BUILT", "status": "implemented", "ready": True,
         "unblocks_claims": ["MECH-AMBIG"]},
        {"sd_id": "SD-WONTFIX", "status": "wontfix", "ready": False,
         "unblocks_claims": ["MECH-AMBIG"]},
        {"sd_id": "SD-COLLIDE", "status": "implemented", "ready": True},
        {"sd_id": "MECH-SELF", "status": "implemented", "ready": True},
        {"sd_id": "SD-PENDING", "status": "implemented_pending_validation",
         "ready": False},
    ]}), encoding="utf-8")
    (planning / "experiment_proposals.v1.json").write_text(json.dumps({"items": [
        # A -- clean: blocker satisfied, no stated condition anywhere.
        {"proposal_id": "EXP-CLEAN", "claim_id": "MECH-CLEAN",
         "status": "blocked_substrate", "blocked_by": ["SD-BUILT"]},
        # A' -- same, but states a release condition the script cannot read.
        {"proposal_id": "EXP-COND", "claim_id": "MECH-COND",
         "status": "blocked_substrate", "blocked_by": ["SD-PENDING"],
         "release_condition": "SD-PENDING must reach validated."},
        # A'' -- condition stated only as prose inside blocked_by.
        {"proposal_id": "EXP-PROSE", "claim_id": "MECH-PROSE",
         "status": "blocked_substrate",
         "blocked_by": ["SD-BUILT (substrate_queue) -- but the consumers "
                        "are inert at production defaults."]},
        # B -- claim-id blocker with disagreeing entries.
        {"proposal_id": "EXP-AMBIG", "claim_id": "MECH-OTHER",
         "status": "blocked_substrate", "blocked_by": ["MECH-AMBIG"]},
        # C -- blocker id == own claim_id, colliding with an implemented sd_id.
        {"proposal_id": "EXP-SELF", "claim_id": "MECH-SELF",
         "status": "blocked_substrate", "blocked_by": ["MECH-SELF"]},
    ]}), encoding="utf-8")
    return tmp_path


@pytest.fixture()
def fixture_rows(tmp_path):
    root = _write_fixture(tmp_path)
    return {r["proposal_id"]: r for r in aud.audit(root)}


def test_fixture_is_not_empty(fixture_rows):
    """Guard the derivation: an empty corpus makes every assertion vacuous."""
    assert len(fixture_rows) == 5, fixture_rows.keys()


def test_clean_row_still_reaches_ready(fixture_rows):
    """The fix must not make READY unreachable -- that would be a dead bucket."""
    assert fixture_rows["EXP-CLEAN"]["bucket"] == "READY"


@pytest.mark.parametrize("pid,reason", [
    ("EXP-COND", "release_condition"),
    ("EXP-PROSE", "blocked_by_prose"),
])
def test_shape_a_stated_condition_is_not_ready(fixture_rows, pid, reason):
    row = fixture_rows[pid]
    assert row["bucket"] == "READY_UNVERIFIED"
    assert reason in row["stated_conditions"]


def test_shape_b_ambiguous_multi_entry(fixture_rows):
    row = fixture_rows["EXP-AMBIG"]
    assert row["bucket"] == "READY_UNVERIFIED"
    assert "ambiguous_multi_entry" in row["undetermined"]
    blk = row["blockers"][0]
    assert blk["satisfied"] is False
    assert "SD-WONTFIX" in blk["unsatisfied_siblings"]


def test_shape_c_self_block_does_not_resolve_to_colliding_sd_id(fixture_rows):
    row = fixture_rows["EXP-SELF"]
    assert row["bucket"] == "READY_UNVERIFIED"
    assert "self_block" in row["undetermined"]
    assert row["blockers"][0]["satisfied"] is False


# --------------------------------------------------------------------------
# the blind-spot measurement: the OLD code must FAIL these
# --------------------------------------------------------------------------
# The revision immediately BEFORE the READY/READY_UNVERIFIED split. Pinned to a
# sha, not HEAD: against HEAD this measurement would silently start SKIPPING the
# moment the fix landed, and a skip reads exactly like a pass. The blind spot is
# meant to keep reproducing for as long as the guard exists.
PRE_FIX_SHA = "0c24017da5d~1"


def _old_module(tmp_path: Path):
    """Import the pre-fix revision of the script from git."""
    r = subprocess.run(
        ["git", "-C", str(ROOT), "show",
         "%s:scripts/audit_blocked_proposal_unblockers.py" % PRE_FIX_SHA],
        capture_output=True, text=True)
    assert r.returncode == 0, (
        "cannot read the pinned pre-fix revision %s -- this measurement must "
        "FAIL rather than skip, or a broken read would read as a pass: %s"
        % (PRE_FIX_SHA, r.stderr.strip()))
    src = r.stdout
    assert "READY_UNVERIFIED" not in src, (
        "%s already carries the fix; the pin is wrong" % PRE_FIX_SHA)
    path = tmp_path / "old_audit.py"
    path.write_text(src, encoding="utf-8")
    import importlib.util
    spec = importlib.util.spec_from_file_location("old_audit", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_old_code_fails_all_three_shapes(tmp_path):
    """Measure the blind spot: every shape above read as READY before the fix.

    If this ever stops holding, the fix was not what closed the gap.
    """
    old = _old_module(tmp_path)
    root = _write_fixture(tmp_path / "reg")
    rows = {r["proposal_id"]: r for r in old.audit(root)}
    for pid in ("EXP-COND", "EXP-PROSE", "EXP-AMBIG", "EXP-SELF"):
        assert rows[pid]["bucket"] == "READY", (
            "old code was expected to false-positive on %s" % pid)
    assert rows["EXP-CLEAN"]["bucket"] == "READY"


# --------------------------------------------------------------------------
# live-registry invariants (no pinned counts -- these must not rot)
# --------------------------------------------------------------------------
@pytest.fixture(scope="module")
def live_rows():
    return aud.audit(ROOT)


def test_live_ready_never_holds_a_stated_condition(live_rows):
    bad = [r["proposal_id"] for r in live_rows
           if r["bucket"] == "READY" and r["stated_conditions"]]
    assert not bad, (
        "READY authorises release; these rows state a condition nobody read: %s"
        % bad)


def test_live_unowned_is_not_cannibalised(live_rows):
    """A genuinely unowned blocker outranks an ambiguous one.

    Regression guard: the first draft of READY_UNVERIFIED took precedence over
    UNOWNED and shrank that census from 49 to 42, hiding owed builds behind a
    softer label.
    """
    for r in live_rows:
        genuinely_unowned = [b for b in r["blockers"]
                             if not b["satisfied"] and not b["owned"]
                             and not b.get("undetermined")]
        if genuinely_unowned:
            assert r["bucket"] == "UNOWNED", (
                "%s has an unowned blocker %s but sits in %s"
                % (r["proposal_id"], genuinely_unowned[0]["id"], r["bucket"]))


def test_live_corpus_is_not_empty(live_rows):
    """Denominator floor: a broken read would make the checks above vacuous."""
    assert len(live_rows) > 20, len(live_rows)
