#!/usr/bin/env python3
"""Canary for the SD-106 / MECH-567 refusal write-back blind spot.

THE CASE. GFLAG-0425 (2026-09-19, REE_assembly b501e436b16) records that
SD-106 / MECH-567's M1_FALSIFY route is not buildable -- `oracle_action` has
zero references in `ree_core/`. The proposal it refers to, EXP-0255, is still
`status: proposed` with no `blocked_by`, because the refusing /queue-experiment
session was scoped out of experiment_proposals.v1.json and could only raise a
governance flag by hand. `audit_blocked_proposal_unblockers.py` was therefore
structurally blind to the exact shape it exists to find.

WHAT THIS PINS, and the honest division of labour between the two halves:

  * The AUDIT change alone does NOT fix EXP-0255. A proposal left `proposed` is
    outside BLOCKED_STATUSES, so neither the old nor the new audit can see it.
    Pinned below, so nobody later reads the new UNATTRIBUTED bucket as having
    covered this case.
  * The WRITE-BACK is what closes it. After record_proposal_refusal.py runs,
    both the old and the new audit find EXP-0255 -- which is the point: the
    route puts the refusal in the two fields the standing detector already
    reads, rather than inventing a second detector.
  * The AUDIT change closes the OTHER half: a proposal blocked with an EMPTY
    blocked_by. The old code `continue`d past those, dropping 146 live rows
    from a census whose header read like a total. The new code counts them.

Run: /opt/local/bin/python3 -m pytest scripts/test_record_proposal_refusal.py -q
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import audit_blocked_proposal_unblockers as aud   # noqa: E402
import record_proposal_refusal as rpr             # noqa: E402

PY = "/opt/local/bin/python3"

# EXP-0255 as it stands in the live registry on 2026-09-23: the motivating case.
SD106_PROPOSAL = {
    "proposal_id": "EXP-0255", "backlog_id": "EVB-1786",
    "claim_id": "MECH-567", "proposal_type": "experimental",
    "status": "proposed", "objective":
        "Reduce uncertainty for MECH-567 via targeted experiment runs.",
}
# The second half: blocked, but naming nothing.
UNATTRIBUTED_PROPOSAL = {
    "proposal_id": "EXP-9999", "claim_id": "MECH-000",
    "proposal_type": "experimental", "status": "blocked_substrate",
}


def _fixture(tmp_path: Path) -> Path:
    planning = tmp_path / "evidence" / "planning"
    planning.mkdir(parents=True)
    (planning / "substrate_queue.json").write_text(
        json.dumps({"queue": [{"sd_id": "SD-UNRELATED", "status": "implemented",
                               "ready": True}]}), encoding="utf-8")
    (planning / "experiment_proposals.v1.json").write_text(
        json.dumps({"items": [dict(SD106_PROPOSAL),
                              dict(UNATTRIBUTED_PROPOSAL)]}, indent=2,
                   sort_keys=True) + "\n", encoding="utf-8")
    return tmp_path


# The revision immediately before the UNATTRIBUTED bucket. Pinned to a sha for
# the reason spelled out in test_audit_blocked_proposal_unblockers.PRE_FIX_SHA:
# against HEAD this canary would start skipping the moment the fix landed, and
# a skipped canary is indistinguishable from a passing one.
PRE_FIX_SHA = "0c24017da5d"


def _old_audit(tmp_path: Path):
    r = subprocess.run(
        ["git", "-C", str(ROOT), "show",
         "%s:scripts/audit_blocked_proposal_unblockers.py" % PRE_FIX_SHA],
        capture_output=True, text=True)
    assert r.returncode == 0, (
        "cannot read the pinned pre-fix revision %s -- this canary must FAIL "
        "rather than skip: %s" % (PRE_FIX_SHA, r.stderr.strip()))
    src = r.stdout
    assert "UNATTRIBUTED" not in src, (
        "%s already carries the fix; the pin is wrong" % PRE_FIX_SHA)
    path = tmp_path / "old_aud.py"
    path.write_text(src, encoding="utf-8")
    spec = importlib.util.spec_from_file_location("old_aud", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _rows(mod, root):
    return {r["proposal_id"]: r for r in mod.audit(root)}


# --------------------------------------------------------------------------
# the blind spot, before anything is written back
# --------------------------------------------------------------------------
def test_sd106_shape_is_invisible_to_both_audits(tmp_path):
    """A refusal left as `proposed` is outside BLOCKED_STATUSES entirely.

    The new bucket does NOT rescue this shape and must not be read as if it did.
    """
    root = _fixture(tmp_path / "reg")
    assert "EXP-0255" not in _rows(aud, root)
    assert "EXP-0255" not in _rows(_old_audit(tmp_path), root)


def test_old_audit_drops_the_unattributed_row(tmp_path):
    """Blocked with an empty blocked_by: silently skipped before the fix."""
    root = _fixture(tmp_path / "reg")
    assert "EXP-9999" not in _rows(_old_audit(tmp_path), root)


def test_new_audit_counts_the_unattributed_row(tmp_path):
    root = _fixture(tmp_path / "reg")
    row = _rows(aud, root)["EXP-9999"]
    assert row["bucket"] == "UNATTRIBUTED"
    assert row["undetermined"] == ["no_blocked_by"]


# --------------------------------------------------------------------------
# the write-back is what closes SD-106
# --------------------------------------------------------------------------
def test_write_back_makes_sd106_visible_to_the_standing_audit(tmp_path):
    root = _fixture(tmp_path / "reg")
    rc = subprocess.run(
        [PY, str(SCRIPTS / "record_proposal_refusal.py"),
         "--root", str(root), "--proposal", "EXP-0255",
         "--blocked-by", "sd-mech567-oracle-action-channel",
         "--route", "implement_substrate",
         "--session", "igw-240-proposal-for-mech-567",
         "--note", "oracle_action has zero references in ree_core/",
         "--governance-flag", "GFLAG-0425",
         "--no-commit", "--skip-claim-check"],
        capture_output=True, text=True).returncode
    assert rc == 0

    row = _rows(aud, root)["EXP-0255"]
    assert row["bucket"] == "UNOWNED", row["bucket"]
    assert row["unowned"] == ["sd-mech567-oracle-action-channel"]

    # and the PRE-FIX audit finds it too -- the route works through the
    # detector that already existed, rather than needing a new one.
    assert "EXP-0255" in _rows(_old_audit(tmp_path), root)

    item = {i["proposal_id"]: i for i in json.loads(
        (root / "evidence" / "planning"
         / "experiment_proposals.v1.json").read_text())["items"]}["EXP-0255"]
    assert item["status"] == "blocked_substrate"
    assert item["blocked_by"] == ["sd-mech567-oracle-action-channel"]
    assert item["refusal_route"] == "implement_substrate"
    assert item["refused_by_session"] == "igw-240-proposal-for-mech-567"
    assert item["governance_flag"] == "GFLAG-0425"
    assert item["refused_utc"].endswith("Z")


# --------------------------------------------------------------------------
# the guarantees that keep the route from recreating the blind spot
# --------------------------------------------------------------------------
def test_refuses_an_unattributed_refusal(tmp_path):
    """No --blocked-by means no blocker named, which is the blind spot."""
    root = _fixture(tmp_path / "reg")
    r = subprocess.run(
        [PY, str(SCRIPTS / "record_proposal_refusal.py"), "--root", str(root),
         "--proposal", "EXP-0255", "--route", "governance", "--session", "s",
         "--note", "n", "--no-commit", "--skip-claim-check"],
        capture_output=True, text=True)
    assert r.returncode == 2
    assert "--blocked-by is mandatory" in r.stderr


def test_only_status_values_the_audit_reads_are_accepted(tmp_path):
    root = _fixture(tmp_path / "reg")
    r = subprocess.run(
        [PY, str(SCRIPTS / "record_proposal_refusal.py"), "--root", str(root),
         "--proposal", "EXP-0255", "--blocked-by", "sd-mech567-oracle",
         "--route", "governance", "--session", "s", "--note", "n",
         "--status", "proposed", "--no-commit", "--skip-claim-check"],
        capture_output=True, text=True)
    assert r.returncode != 0, "writing a non-blocked status must be refused"


def test_every_writable_status_is_one_the_audit_reads():
    """Derived, not restated: a status the audit ignores would be invisible."""
    assert set(rpr.BLOCKED_STATUSES) <= set(aud.BLOCKED_STATUSES)
    assert rpr.BLOCKED_STATUSES, "empty tuple would make this vacuous"


def test_unknown_proposal_is_an_error_not_a_silent_no_op(tmp_path):
    root = _fixture(tmp_path / "reg")
    r = subprocess.run(
        [PY, str(SCRIPTS / "record_proposal_refusal.py"), "--root", str(root),
         "--proposal", "EXP-NOPE", "--blocked-by", "X", "--route", "governance",
         "--session", "s", "--note", "n", "--no-commit", "--skip-claim-check"],
        capture_output=True, text=True)
    assert r.returncode == 4


def test_no_other_proposal_is_touched(tmp_path):
    root = _fixture(tmp_path / "reg")
    path = root / "evidence" / "planning" / "experiment_proposals.v1.json"
    before = {i["proposal_id"]: dict(i)
              for i in json.loads(path.read_text())["items"]}
    subprocess.run(
        [PY, str(SCRIPTS / "record_proposal_refusal.py"), "--root", str(root),
         "--proposal", "EXP-0255", "--blocked-by", "sd-mech567-oracle",
         "--route", "implement_substrate", "--session", "s", "--note", "n",
         "--no-commit", "--skip-claim-check"], check=True)
    after = {i["proposal_id"]: dict(i)
             for i in json.loads(path.read_text())["items"]}
    assert after["EXP-9999"] == before["EXP-9999"]
    assert set(after) == set(before)


def test_dry_run_writes_nothing(tmp_path):
    root = _fixture(tmp_path / "reg")
    path = root / "evidence" / "planning" / "experiment_proposals.v1.json"
    raw = path.read_text()
    subprocess.run(
        [PY, str(SCRIPTS / "record_proposal_refusal.py"), "--root", str(root),
         "--proposal", "EXP-0255", "--blocked-by", "sd-mech567-oracle",
         "--route", "governance", "--session", "s", "--note", "n",
         "--dry-run", "--skip-claim-check"], check=True)
    assert path.read_text() == raw


def test_refuses_naming_the_claim_as_its_own_blocker(tmp_path):
    """Found BY this canary: --blocked-by MECH-567 on EXP-0255 (claim MECH-567)
    produced a self-block the audit can say nothing about. Naming the claim
    under test is never the useful answer -- name the substrate."""
    root = _fixture(tmp_path / "reg")
    r = subprocess.run(
        [PY, str(SCRIPTS / "record_proposal_refusal.py"), "--root", str(root),
         "--proposal", "EXP-0255", "--blocked-by", "MECH-567",
         "--route", "implement_substrate", "--session", "s", "--note", "n",
         "--no-commit", "--skip-claim-check"],
        capture_output=True, text=True)
    assert r.returncode == 2
    assert "OWN claim_id" in r.stderr


def test_self_block_override_still_available(tmp_path):
    root = _fixture(tmp_path / "reg")
    r = subprocess.run(
        [PY, str(SCRIPTS / "record_proposal_refusal.py"), "--root", str(root),
         "--proposal", "EXP-0255", "--blocked-by", "MECH-567",
         "--route", "implement_substrate", "--session", "s", "--note", "n",
         "--allow-self-block", "--no-commit", "--skip-claim-check"],
        capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
