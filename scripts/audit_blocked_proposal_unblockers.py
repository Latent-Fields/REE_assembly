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

MEASURED 2026-09-23 (session conversionwriteback-20260923, under a human
ruling to release the then-READY rows): the READY bucket held 12 proposals and
ALL TWELVE were false positives. Each was verified per-proposal against the
substrate record and every one failed its own stated release condition -- the
bucket authorised STARTING work on the strength of a negative ("no unsatisfied
blocker") whose predicate was not the one that governs release. Zero were
released. The READY/READY_UNVERIFIED split below is that finding made
structural, per CLAUDE.md "Negative instruments": an explicit cannot-determine
CATEGORY rather than a silently over-confident verdict.

This script is READ-ONLY. It writes nothing, edits no registry, and opens no
claim. It answers one question -- "which blocks are stale, and which owed
builds has nobody adopted?" -- and prints the three buckets that follow from
it. Acting on a finding is a governance decision, not this script's job.

BUCKETS
  READY      every named blocker is satisfied AND the proposal states no
             release condition of its own -> the block is stale, the proposal
             is a candidate to return to `proposed`.
  READY_UNVERIFIED
             blocker statuses look satisfied, but this script CANNOT conclude
             the block is stale. Either the proposal states a release
             condition in prose (which is routinely stronger than the blocker
             statuses -- e.g. "reaches VALIDATED" against a blocker sitting at
             implemented_pending_validation) or a blocker resolved ambiguously
             (self-block / several substrate_queue entries disagreeing).
             A SHORTLIST FOR A HUMAN, NOT A RELEASE LIST.
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


def resolve_blocker(bid: str, by_sd: dict, by_claim: dict,
                    self_claim: str = "") -> dict:
    """Ownership + satisfaction verdict for one blocker id.

    Three ways this returns "cannot determine" rather than a verdict. Each is
    a measured false-positive shape from the 2026-09-23 per-proposal audit of
    the READY bucket, in which 12 of 12 rows were false positives:

    * SELF-BLOCK -- the blocker id equals the proposal's own claim_id. That is
      a claims.yaml experiment-queue gate, not a substrate dependency, and the
      id may collide with an unrelated substrate_queue sd_id (EXP-0440 and
      EXP-0585 are both blocked on the SD-056 claim gate and were resolved
      against the implemented sd_id SD-056).
    * AMBIGUOUS MULTI-ENTRY -- a blocker named as a CLAIM id is resolved
      through `unblocks_claims`, and several entries name it. This used to
      take by_claim[bid][0] and ignore the rest, so one satisfied entry
      outvoted an unsatisfied sibling (EXP-0868's MECH-151 resolved through
      an implemented SD-016 while a `wontfix` entry for that exact gap sat
      beside it).
    * UNOWNED -- unchanged: no substrate_queue entry at all.
    """
    if self_claim and bid == self_claim:
        return {"id": bid, "owned": False, "satisfied": False, "via": None,
                "sd_id": None, "status": None, "ready": None,
                "undetermined": "self_block"}
    entry = by_sd.get(bid)
    if entry is not None:
        status = str(entry.get("status") or "").strip()
        return {"id": bid, "owned": True,
                "satisfied": status in SATISFIED_STATUSES, "via": "sd_id",
                "sd_id": entry.get("sd_id"), "status": status,
                "ready": entry.get("ready"), "undetermined": None}
    hits = by_claim.get(bid) or []
    if not hits:
        return {"id": bid, "owned": False, "satisfied": False,
                "via": None, "sd_id": None, "status": None, "ready": None,
                "undetermined": None}
    sats = [str(e.get("status") or "").strip() in SATISFIED_STATUSES
            for e in hits]
    first = hits[0]
    status = str(first.get("status") or "").strip()
    if len(hits) > 1 and not all(sats):
        unsat = [str(e.get("sd_id") or "?") for e, ok in zip(hits, sats)
                 if not ok]
        return {"id": bid, "owned": True, "satisfied": False, "via": "claim",
                "sd_id": first.get("sd_id"), "status": status,
                "ready": first.get("ready"),
                "undetermined": "ambiguous_multi_entry",
                "unsatisfied_siblings": unsat}
    return {"id": bid, "owned": True, "satisfied": all(sats), "via": "claim",
            "sd_id": first.get("sd_id"), "status": status,
            "ready": first.get("ready"), "undetermined": None}


# Fields in which a human records a condition this script CANNOT evaluate. A
# proposal carrying any of them has a release test of its own that is strictly
# stronger than "every blocked_by id has a satisfied substrate_queue status" --
# typically "reaches VALIDATED" against a blocker sitting at
# implemented_pending_validation, or a condition naming substrate that is not
# in blocked_by at all. Measured 2026-09-23: all 12 then-READY rows carried at
# least one, and all 12 were false positives.
CONDITION_FIELDS = ("release_condition", "gating_reason", "blocked_note")


def stated_conditions(item: dict, raw_blockers: list) -> list[str]:
    """Names of the human-authored condition fields this proposal carries."""
    found = [f for f in CONDITION_FIELDS if str(item.get(f) or "").strip()]
    # Prose inside a blocked_by entry is a condition too: EXP-0176 carries no
    # condition FIELD, and states its release test inside the blocker string.
    for r in raw_blockers:
        if str(r).strip() != unblocker_id(r):
            found.append("blocked_by_prose")
            break
    return found


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
        self_claim = str(item.get("claim_id") or "").strip()
        blockers = [resolve_blocker(unblocker_id(r), by_sd, by_claim,
                                    self_claim) for r in raw]
        outstanding = [b for b in blockers if not b["satisfied"]]
        stated = stated_conditions(item, raw)
        if not outstanding:
            bucket = "READY" if not stated else "READY_UNVERIFIED"
        # UNOWNED keeps its original precedence over the new bucket. A row with
        # a genuinely unowned blocker belongs in the bucket that "never moves on
        # its own" even if some OTHER blocker resolved ambiguously -- routing it
        # to READY_UNVERIFIED instead would shrink the UNOWNED census (measured:
        # 49 -> 42) and hide owed builds behind a softer-sounding label.
        elif any(not b["owned"] and not b.get("undetermined")
                 for b in outstanding):
            bucket = "UNOWNED"
        elif any(b.get("undetermined") for b in outstanding):
            bucket = "READY_UNVERIFIED"
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
            "undetermined": sorted({b["undetermined"] for b in blockers
                                    if b.get("undetermined")}),
            "stated_conditions": stated,
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
    all_rows = audit(root)
    rows = all_rows
    if args.bucket:
        rows = [r for r in all_rows if r["bucket"] == args.bucket.upper()]

    if args.json:
        print(json.dumps({"findings": rows, "n": len(rows)}, indent=2))
        return 0

    order = ["READY", "READY_UNVERIFIED", "PARTIAL", "UNOWNED", "OWNED"]
    # Count over ALL rows, never the --bucket-filtered view: a filtered run used
    # to print "proposals carrying blocked_by: 2", which reads as a data
    # discrepancy against the unfiltered 19 rather than as a filter, and cost a
    # reader a diagnostic detour. The filter belongs in the body, not the census.
    counts = {b: sum(1 for r in all_rows if r["bucket"] == b) for b in order}
    print("BLOCKED-PROPOSAL UNBLOCKER AUDIT")
    print("=" * 74)
    print("proposals carrying blocked_by: %d   %s" % (
        len(all_rows), "  ".join("%s=%d" % (b, counts[b]) for b in order)))
    if args.bucket:
        print("showing only [%s] -- %d of %d" % (
            args.bucket.upper(), len(rows), len(all_rows)))

    for bucket in order:
        sel = [r for r in rows if r["bucket"] == bucket]
        if not sel:
            continue
        print("\n[%s]  %d" % (bucket, len(sel)))
        if bucket == "READY":
            print("  every named blocker is satisfied AND no release condition")
            print("  is stated -- the block is STALE.")
        elif bucket == "READY_UNVERIFIED":
            print("  blocker statuses look satisfied but the proposal states its")
            print("  own release condition, or a blocker resolved ambiguously.")
            print("  READ THE CONDITION BEFORE RELEASING. Measured 2026-09-23:")
            print("  12 of 12 rows in this shape failed their stated condition.")
        elif bucket == "UNOWNED":
            print("  no substrate_queue entry for the blocker: the owed build has")
            print("  no owner and no lane, so this never moves on its own.")
        for r in sel:
            print("  %-9s %-11s %-18s %s" % (
                r["proposal_id"], r["claim_id"], r["proposal_type"] or "?",
                r["status"]))
            if r.get("stated_conditions") or r.get("undetermined"):
                bits = list(r.get("stated_conditions") or [])
                bits += ["blocker:%s" % u for u in (r.get("undetermined") or [])]
                print("       cannot-determine: %s" % ", ".join(bits))
            for b in r["blockers"]:
                if b["satisfied"]:
                    mark = "OK  "
                elif b.get("undetermined"):
                    mark = "????"
                elif not b["owned"]:
                    mark = "MISS"
                elif b["ready"] is True:
                    # substrate_queue says ready=True but the status string is
                    # not one this script recognises as satisfied (several are
                    # free prose). Not auto-cleared -- flagged for a human.
                    mark = "WAIT*"
                else:
                    mark = "WAIT"
                if b.get("undetermined") == "self_block":
                    detail = "blocker id == this proposal's own claim_id"
                elif b.get("undetermined") == "ambiguous_multi_entry":
                    detail = "entries disagree; unsatisfied: %s" % (
                        ", ".join(b.get("unsatisfied_siblings") or [])[:60])
                elif not b["owned"]:
                    detail = "no substrate_queue entry"
                else:
                    detail = "%s (ready=%s)" % (b["status"][:46], b["ready"])
                print("       %-4s %-44.44s %s" % (mark, b["id"], detail))

    if any(b["ready"] is True and not b["satisfied"] and b["owned"]
           for r in rows for b in r["blockers"]):  # footnote follows what is SHOWN
        print("\nWAIT* = substrate_queue says ready=True but its status string is not one")
        print("this script recognises as satisfied (several statuses are free prose).")
        print("Not auto-cleared -- read the entry and decide.")
    if counts["READY"]:
        print("\nNEXT: the READY rows are candidates to return to `proposed`. That is a")
        print("governance decision (the substrate landing may not restore the design's")
        print("validity) -- route via governance_flag.py, do not hand-edit the registry.")
    if counts["READY_UNVERIFIED"]:
        print("\nNEXT: READY_UNVERIFIED is a shortlist to READ, not a release list. Open")
        print("each proposal's release_condition / gating_reason / blocked_note and check")
        print("it against the substrate by hand. On 2026-09-23 all 12 rows in this shape")
        print("failed their own stated condition and none was released.")
    if counts["UNOWNED"]:
        print("\nNEXT: the UNOWNED blockers need a substrate_queue entry before any")
        print("lane can pick them up -- /implement-substrate has nothing to read.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
