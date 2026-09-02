#!/usr/bin/env python3
"""Re-check every blocked proposal against the substrate that blocks it.

WHY THIS EXISTS
---------------
A `/queue-experiment` Step 2.5 stop writes `status: blocked_substrate` plus a
`blocked_by` list naming the substrate the proposal is waiting on. That write
is ONE-WAY. Nothing re-reads it when the named substrate later lands, so a
proposal blocked in June stays blocked in September even though its blocker
was implemented and validated weeks ago. The block dies in a resolve note.

Measured 2026-09-02 over the live registry: 19 proposals carry `blocked_by`,
naming 23 distinct unblockers. Of those, FOUR are already satisfied in
substrate_queue.json (`modulatory-bias-selection-authority` = implemented,
`sd_zworld_warmup_optimizer_group` = validated,
`contextmemory-write-path-addressing-degeneracy` = implemented_pending_validation,
`SD-e1-rollout-consistency-training` = item2_substrate_landed) and THIRTEEN
have no substrate_queue entry at all -- the owed build is UNOWNED, so no lane
is going to produce it.

This script is READ-ONLY. It writes nothing, edits no registry, and opens no
claim. It answers one question -- "which blocks are stale, and which owed
builds has nobody adopted?" -- and prints the three buckets that follow from
it. Acting on a finding is a governance decision, not this script's job.

BUCKETS
  READY      every named blocker is satisfied -> the block is stale, the
             proposal is a candidate to return to `proposed`.
  PARTIAL    some blockers satisfied, some not -> still blocked, but the
             remaining set is smaller than the note says.
  OWNED      blocked, and every unsatisfied blocker has a substrate_queue
             entry -- the build has an owner and a lane.
  UNOWNED    blocked, and at least one blocker has NO substrate_queue entry.
             This is the bucket that never moves on its own.

`blocked_by` has no schema -- entries are variously a claim id (`MECH-054`),
a substrate_queue `sd_id` (`modulatory-bias-selection-authority`), or free
prose with the id embedded (`mech151-... (substrate_queue.json, status ...)`).
The leading token before the first ` (` or ` -- ` is taken as the id, which
is what every live entry actually uses.

Usage:
  python3 scripts/audit_blocked_proposal_unblockers.py            # report
  python3 scripts/audit_blocked_proposal_unblockers.py --json     # machine-readable
  python3 scripts/audit_blocked_proposal_unblockers.py --bucket UNOWNED
Exit code is 0 even with findings, so it chains safely.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# substrate_queue statuses that mean "the thing the proposal was waiting for
# now exists". Deliberately a allow-list of OBSERVED values rather than a
# substring match on "implement": `proposed_GATED_on_ARC-007_..._DO_NOT_BUILD_YET`
# contains neither, and a loose match would read a long prose status as
# satisfied. Unknown statuses fall through to NOT satisfied, which is the safe
# direction (a stale block is a missed opportunity; a falsely-cleared block
# queues an experiment against absent substrate).
SATISFIED_STATUSES = {
    "implemented",
    "implemented_pending_validation",
    "validated",
    "candidate_substrate_landed",
    "item2_substrate_landed_validation_owed",
}

BLOCKED_STATUSES = {
    "blocked_substrate",
    "proposed_blocked_substrate",
    "deferred_substrate_not_ready",
    "blocked_on_gate",
    "gated",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def unblocker_id(raw: str) -> str:
    """Leading id token from a free-form blocked_by entry."""
    return re.split(r"\s+\(|\s+--\s+", str(raw))[0].strip()


def load_substrate_index(path: Path) -> tuple[dict, dict]:
    doc = json.loads(path.read_text(encoding="utf-8"))
    by_sd, by_claim = {}, {}
    for entry in doc.get("queue", []):
        if not isinstance(entry, dict):
            continue
        sd = str(entry.get("sd_id") or "").strip()
        if sd:
            by_sd[sd] = entry
        claims = entry.get("unblocks_claims") or entry.get("claim_ids") or []
        if isinstance(claims, str):
            claims = [claims]
        for c in claims:
            by_claim.setdefault(str(c).strip(), []).append(entry)
    return by_sd, by_claim


def resolve_blocker(bid: str, by_sd: dict, by_claim: dict) -> dict:
    """Ownership + satisfaction verdict for one blocker id."""
    entry = by_sd.get(bid)
    via = "sd_id"
    if entry is None and bid in by_claim:
        entry = by_claim[bid][0]
        via = "claim"
    if entry is None:
        return {"id": bid, "owned": False, "satisfied": False,
                "via": None, "sd_id": None, "status": None, "ready": None}
    status = str(entry.get("status") or "").strip()
    return {
        "id": bid,
        "owned": True,
        "satisfied": status in SATISFIED_STATUSES,
        "via": via,
        "sd_id": entry.get("sd_id"),
        "status": status,
        "ready": entry.get("ready"),
    }


def audit(root: Path) -> list[dict]:
    planning = root / "evidence" / "planning"
    by_sd, by_claim = load_substrate_index(planning / "substrate_queue.json")
    proposals = json.loads(
        (planning / "experiment_proposals.v1.json").read_text(encoding="utf-8")
    )
    out = []
    for item in proposals.get("items", []):
        if not isinstance(item, dict):
            continue
        if str(item.get("status") or "") not in BLOCKED_STATUSES:
            continue
        raw = item.get("blocked_by") or []
        if isinstance(raw, str):
            raw = [raw]
        if not raw:
            continue
        blockers = [resolve_blocker(unblocker_id(r), by_sd, by_claim) for r in raw]
        outstanding = [b for b in blockers if not b["satisfied"]]
        if not outstanding:
            bucket = "READY"
        elif any(not b["owned"] for b in outstanding):
            bucket = "UNOWNED"
        elif len(outstanding) < len(blockers):
            bucket = "PARTIAL"
        else:
            bucket = "OWNED"
        out.append({
            "proposal_id": item.get("proposal_id"),
            "backlog_id": item.get("backlog_id"),
            "proposal_type": item.get("proposal_type"),
            "claim_id": item.get("claim_id"),
            "status": item.get("status"),
            "bucket": bucket,
            "blockers": blockers,
            "outstanding": [b["id"] for b in outstanding],
            "unowned": [b["id"] for b in outstanding if not b["owned"]],
        })
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--bucket", help="show only this bucket "
                                     "(READY/PARTIAL/OWNED/UNOWNED)")
    ap.add_argument("--root", default=None, help="REE_assembly root (default: inferred)")
    args = ap.parse_args()

    root = Path(args.root) if args.root else repo_root()
    rows = audit(root)
    if args.bucket:
        rows = [r for r in rows if r["bucket"] == args.bucket.upper()]

    if args.json:
        print(json.dumps({"findings": rows, "n": len(rows)}, indent=2))
        return 0

    order = ["READY", "PARTIAL", "UNOWNED", "OWNED"]
    counts = {b: sum(1 for r in rows if r["bucket"] == b) for b in order}
    print("BLOCKED-PROPOSAL UNBLOCKER AUDIT")
    print("=" * 74)
    print("proposals carrying blocked_by: %d   %s" % (
        len(rows), "  ".join("%s=%d" % (b, counts[b]) for b in order)))

    for bucket in order:
        sel = [r for r in rows if r["bucket"] == bucket]
        if not sel:
            continue
        print("\n[%s]  %d" % (bucket, len(sel)))
        if bucket == "READY":
            print("  every named blocker is satisfied -- the block is STALE.")
        elif bucket == "UNOWNED":
            print("  no substrate_queue entry for the blocker: the owed build has")
            print("  no owner and no lane, so this never moves on its own.")
        for r in sel:
            print("  %-9s %-11s %-18s %s" % (
                r["proposal_id"], r["claim_id"], r["proposal_type"] or "?",
                r["status"]))
            for b in r["blockers"]:
                if b["satisfied"]:
                    mark = "OK  "
                elif not b["owned"]:
                    mark = "MISS"
                elif b["ready"] is True:
                    # substrate_queue says ready=True but the status string is
                    # not one this script recognises as satisfied (several are
                    # free prose). Not auto-cleared -- flagged for a human.
                    mark = "WAIT*"
                else:
                    mark = "WAIT"
                detail = ("no substrate_queue entry" if not b["owned"]
                          else "%s (ready=%s)" % (b["status"][:46], b["ready"]))
                print("       %-4s %-44.44s %s" % (mark, b["id"], detail))

    if any(b["ready"] is True and not b["satisfied"] and b["owned"]
           for r in rows for b in r["blockers"]):
        print("\nWAIT* = substrate_queue says ready=True but its status string is not one")
        print("this script recognises as satisfied (several statuses are free prose).")
        print("Not auto-cleared -- read the entry and decide.")
    if counts["READY"]:
        print("\nNEXT: the READY rows are candidates to return to `proposed`. That is a")
        print("governance decision (the substrate landing may not restore the design's")
        print("validity) -- route via governance_flag.py, do not hand-edit the registry.")
    if counts["UNOWNED"]:
        print("\nNEXT: the UNOWNED blockers need a substrate_queue entry before any")
        print("lane can pick them up -- /implement-substrate has nothing to read.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
