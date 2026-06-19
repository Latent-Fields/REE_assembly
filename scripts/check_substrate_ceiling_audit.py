#!/usr/bin/env python3
"""Substrate-ceiling mapping audit (governance Step 6a-v).

Walks every claim in docs/claims/claims.yaml whose resolved epistemic_category
is `substrate_ceiling` and classifies each into one bucket, so the governance
cycle can route the actionable ones without re-deriving the audit by hand and
without re-flagging intentionally-parked / self-handled ceilings every cycle.

A `substrate_ceiling` verdict is a standing claim that the V3 substrate is too
coarse to deliver a needed distinction. Its correct response is substrate
ENRICHMENT, not more experiments on the existing substrate. The audit's job is
to guarantee every such verdict has either a design owner, a deliberate park
decision, or is surfaced as a genuine orphan that needs routing.

Buckets (each claim lands in exactly one). PRECEDENCE: `parked` is checked
FIRST -- an explicit operator park decision (`ceiling_decision: deferred`)
overrides substrate status, so an intentionally-deferred ceiling is never
re-surfaced as `mapped` / `ceiling_may_have_lifted` just because its named
substrate is implemented. The remaining buckets follow top-to-bottom:

  ceiling_may_have_lifted  Mapped AND the unblocking substrate_queue entry is
                           now status=implemented. The bounding substrate has
                           landed; the verdict is testable again. ACTIONABLE
                           -- surface for re-queue / retest (Step 6a-v case 3).

  mapped                   At least one substrate_queue entry lists the claim
                           in its `unblocks_claims` (a design owner exists that,
                           when built, lifts the ceiling). Loop closed; no
                           action (Step 6a-v case 1).

  parked                   Carries the machine-readable park marker
                           `ceiling_decision: deferred` (+ a `ceiling_routing_note`
                           giving the reason/date). The build-decision is
                           deliberately deferred -- the ceiling is NOT awaiting a
                           substrate-design owner. Non-interactive: do NOT flag
                           for /failure-autopsy. Remove the marker to re-route.

  self_handled             Carries `pending_retest_after_substrate: true` AND a
                           substrate_queue entry exists with `sd_id == <claim id>`
                           (the claim IS its own implemented substrate; it bounds
                           dependents, not itself, so nothing lists it in
                           unblocks_claims). Canonical case: SD-037. Non-interactive.

  orphaned                 None of the above: no design owner, not parked, not
                           self-handled. The ceiling was diagnosed but no
                           substrate-design response exists. ACTIONABLE -- route
                           to /failure-autopsy for an enrichment recommendation
                           (Step 6a-v case 2). Never park as a dead-end verdict.

The audit READS ONLY. All writes flow through the Step 6a-iv create/amend
pathway, a /failure-autopsy flag, or a hand-applied park marker.

Resolution note: the audited set is claims with an EXPLICIT
`epistemic_category: substrate_ceiling` (the schema is explicit-only for this
category; this matches the indexer's _resolve_epistemic_category and the
historical governance grep). Rare depends_on-INHERITED ceilings (a claim whose
evidence_quality_note records inheriting the category via a depended-on claim)
are not auto-resolved here; check those by hand per the skill prose.

Usage:
  python3 scripts/check_substrate_ceiling_audit.py            # human report, exit 0
  python3 scripts/check_substrate_ceiling_audit.py --strict   # exit 1 if any orphan
  python3 scripts/check_substrate_ceiling_audit.py --json     # machine-readable buckets
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("PyYAML required (pip install pyyaml)\n")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CLAIMS = REPO_ROOT / "docs" / "claims" / "claims.yaml"
DEFAULT_QUEUE = REPO_ROOT / "evidence" / "planning" / "substrate_queue.json"

CEILING_CATEGORY = "substrate_ceiling"
PARK_DECISION = "deferred"


def _truthy(value) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ("true", "yes", "1")


def load_claims(path: Path) -> list[dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return [c for c in data if isinstance(c, dict) and "id" in c]


def load_queue(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return data.get("queue") or []
    return data or []


def audit(claims: list[dict], queue: list[dict]) -> dict:
    """Return {bucket_name: [ {id, ...}, ... ]} for the substrate_ceiling set."""
    # Map claim id -> list of unblocking queue entries; collect sd_ids present.
    unblocks: dict[str, list[dict]] = {}
    sd_entries: dict[str, list[dict]] = {}
    for entry in queue:
        sid = entry.get("sd_id")
        if sid:
            sd_entries.setdefault(sid, []).append(entry)
        for cid in (entry.get("unblocks_claims") or []):
            unblocks.setdefault(cid, []).append(entry)

    ceilings = [
        c for c in claims
        if str(c.get("epistemic_category", "")).strip().lower() == CEILING_CATEGORY
    ]

    buckets = {
        "ceiling_may_have_lifted": [],
        "mapped": [],
        "parked": [],
        "self_handled": [],
        "orphaned": [],
    }

    for c in ceilings:
        cid = c["id"]
        owners = unblocks.get(cid, [])
        mapped = bool(owners)
        implemented_owner = next(
            (e for e in owners
             if str(e.get("status", "")).strip().lower() == "implemented"),
            None,
        )
        parked = str(c.get("ceiling_decision", "")).strip().lower() == PARK_DECISION
        own_entries = sd_entries.get(cid, [])
        self_handled = _truthy(c.get("pending_retest_after_substrate")) and bool(own_entries)

        retest_owed = _truthy(c.get("pending_retest_after_substrate"))
        rec = {"id": cid, "status": c.get("status")}
        # PRECEDENCE: an explicit operator park decision wins over substrate
        # status. A `ceiling_decision: deferred` claim is intentionally parked
        # (build/retest deferred), so it must NOT re-surface as `mapped` or
        # `ceiling_may_have_lifted` just because its named substrate happens to
        # be implemented -- that defeats the parking convention's whole purpose
        # (stop re-flagging intentionally-parked ceilings every cycle). Remove
        # the marker to re-route. This only affects claims carrying the explicit
        # marker, so un-parked mapped+implemented ceilings still surface normally.
        # (Reordered 2026-06-19: parked was previously checked AFTER mapped, which
        # made the marker inert for every mapped+implemented claim -- the entire
        # substrate_ceiling_lifted_triage_2026-06 bucket.)
        #
        # ceiling-may-have-lifted is actionable only when the bounding substrate
        # has LANDED *and* a retest is still owed. A mapped+implemented ceiling
        # whose retest was already reconciled (no pending_retest flag) is a
        # genuinely closed loop -> plain `mapped`, not a re-surfaced action.
        if parked:
            rec["ceiling_routing_note"] = (c.get("ceiling_routing_note") or "").strip()[:160]
            buckets["parked"].append(rec)
        elif mapped and implemented_owner is not None and retest_owed:
            rec["unblocked_by"] = implemented_owner.get("sd_id")
            buckets["ceiling_may_have_lifted"].append(rec)
        elif mapped:
            rec["unblocked_by"] = [e.get("sd_id") for e in owners]
            buckets["mapped"].append(rec)
        elif self_handled:
            rec["own_substrate_entry"] = [
                {"sd_id": e.get("sd_id"), "status": e.get("status")} for e in own_entries
            ]
            buckets["self_handled"].append(rec)
        else:
            buckets["orphaned"].append(rec)

    return buckets


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--claims", type=Path, default=DEFAULT_CLAIMS)
    ap.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any genuinely-orphaned ceiling exists")
    args = ap.parse_args()

    claims = load_claims(args.claims)
    queue = load_queue(args.queue)
    buckets = audit(claims, queue)

    total = sum(len(v) for v in buckets.values())
    n_orphan = len(buckets["orphaned"])
    n_lifted = len(buckets["ceiling_may_have_lifted"])

    if args.json:
        print(json.dumps({"total": total, "buckets": buckets}, indent=2))
    else:
        print(f"Substrate-ceiling mapping audit: {total} substrate_ceiling claim(s)")
        print(f"  mapped (design owner exists)            : {len(buckets['mapped'])}")
        print(f"  parked (ceiling_decision: deferred)     : {len(buckets['parked'])}")
        print(f"  self-handled (own implemented substrate): {len(buckets['self_handled'])}")
        print(f"  ceiling-may-have-lifted (ACTIONABLE)    : {n_lifted}")
        print(f"  genuinely-orphaned (ACTIONABLE)         : {n_orphan}")
        for cid_rec in buckets["parked"]:
            print(f"    [parked] {cid_rec['id']}")
        for cid_rec in buckets["self_handled"]:
            owns = ", ".join(f"{e['sd_id']}({e['status']})" for e in cid_rec["own_substrate_entry"])
            print(f"    [self-handled] {cid_rec['id']} -- own entry: {owns}")
        if n_lifted:
            print("  -- ceiling-may-have-lifted: surface to user (re-queue/retest):")
            for rec in buckets["ceiling_may_have_lifted"]:
                print(f"    [lifted] {rec['id']} -- unblocking substrate {rec['unblocked_by']} implemented")
        if n_orphan:
            print("  -- ORPHANED: route each to /failure-autopsy (enrichment recommendation):")
            for rec in buckets["orphaned"]:
                print(f"    [orphan] {rec['id']} (status={rec['status']})")
        else:
            print("  -- no genuine orphans; no AskUserQuestion routing needed for orphans.")

    if args.strict and n_orphan:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
