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

On TOP of the five-way partition, the audit computes the GOV-CEIL-1
ceiling-exhaustion OVERLAY. A `ceiling hit` is one confirmed
`failure_autopsy_*.json` whose target lists the claim AND recommends
`substrate_ceiling`. A ceiling drawn from `mapped` or `orphaned` whose hit
count reaches N (CEILING_EXHAUSTION_N, default 3) with no positive
discrimination on a richer substrate has EXHAUSTED its grace: the
inert-mechanism null reading now stands co-equal, and the claim is surfaced
(ACTIONABLE) for demotion to a ceiling-exhausted contested candidate
(epistemic_category -> standard, status floored to candidate, null reading
carried co-equally, `ceiling_decision: exhausted`). `ceiling_may_have_lifted`
(owed retest runs first), `parked` (deliberate deferral / user waiver), and
`self_handled` are exempt. Detection is automatic; application is user-approved
at governance Step 6a-v. Absent an autopsy corpus every count is 0, so a missing
corpus can never mass-demote.

The audit READS ONLY. All writes flow through the Step 6a-iv create/amend
pathway, a /failure-autopsy flag, a hand-applied park marker, or (for an
exhausted ceiling) the user-approved GOV-CEIL-1 demotion at Step 6a-v.

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
DEFAULT_AUTOPSY_DIR = REPO_ROOT / "evidence" / "planning"

CEILING_CATEGORY = "substrate_ceiling"
PARK_DECISION = "deferred"

# GOV-CEIL-1 (ceiling-exhaustion demotion rule). N distinct confirmed
# substrate_ceiling failure-autopsy verdicts on a claim, with NO positive
# discrimination on any richer substrate, exhausts the ceiling's grace: the
# inert-mechanism null reading has earned co-equal standing and the claim is
# surfaced for demotion (governance Step 6a-v, user-approved). Tunable.
CEILING_EXHAUSTION_N = 3


def count_ceiling_hits(autopsy_dir: Path) -> dict[str, int]:
    """Count confirmed substrate_ceiling failure-autopsy verdicts per claim.

    A "ceiling hit" (GOV-CEIL-1 definition (a)) is one confirmed
    (`status: confirmed`) `failure_autopsy_*.json` whose target lists the claim
    in `claim_ids` AND carries `recommended_epistemic_category:
    substrate_ceiling`. A claim named by several targets in one artifact, or by
    the same run under multiple autopsies, is counted once per (artifact, run)
    to avoid double-counting a single diagnosis. Returns {claim_id: n_hits}.
    """
    hits: dict[str, set] = {}
    if not autopsy_dir.is_dir():
        return {}
    for fp in sorted(autopsy_dir.glob("failure_autopsy_*.json")):
        try:
            data = json.loads(fp.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        if str(data.get("status", "")).strip().lower() != "confirmed":
            continue
        for tgt in (data.get("targets") or []):
            ec = str(tgt.get("recommended_epistemic_category", "")).strip().lower()
            if ec != CEILING_CATEGORY:
                continue
            # De-dup key: one hit per (artifact stem, run_id) so re-listing a
            # claim across an artifact's targets does not inflate the count.
            run_key = str(tgt.get("run_id") or tgt.get("queue_id") or fp.stem)
            for cid in (tgt.get("claim_ids") or []):
                hits.setdefault(cid, set()).add((fp.stem, run_key))
    return {cid: len(keys) for cid, keys in hits.items()}


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


def audit(claims: list[dict], queue: list[dict],
          ceiling_hits: dict[str, int] | None = None) -> tuple[dict, list]:
    """Classify the substrate_ceiling set.

    Returns `(buckets, exhausted)`:
      * `buckets` -- the five-way partition {bucket_name: [rec, ...]}; each
        substrate_ceiling claim lands in exactly one.
      * `exhausted` -- the GOV-CEIL-1 ACTIONABLE OVERLAY (NOT a partition
        bucket): claims drawn from `mapped` or `orphaned` whose confirmed
        ceiling-hit count >= CEILING_EXHAUSTION_N with no positive discrimination
        on a richer substrate. `ceiling_may_have_lifted` (retest owed first),
        `parked` (deliberate deferral / user waiver), and `self_handled` are
        exempt. Application is user-approved at governance Step 6a-v.

    `ceiling_hits` maps claim id -> confirmed substrate_ceiling autopsy count
    (from `count_ceiling_hits`); absent / None -> every count is 0 (nothing is
    ever flagged exhausted, so a missing autopsy corpus can never mass-demote).
    """
    ceiling_hits = ceiling_hits or {}
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
    exhausted = []  # GOV-CEIL-1 overlay (drawn from mapped + orphaned)

    for c in ceilings:
        cid = c["id"]
        n_hits = int(ceiling_hits.get(cid, 0) or 0)
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
        # Binding-substrate refinement (durable MECH-314 false-positive fix,
        # 2026-07-01). A ceiling whose owed retest was re-pointed to a SPECIFIC
        # (often unbuilt) substrate must not re-surface as `ceiling_may_have_lifted`
        # merely because SOME other, non-binding implemented substrate happens to
        # list it in unblocks_claims (MECH-314's retest is gated on the unbuilt
        # DA-gated arbitration-learning substrate MECH-448/449/ARC-107, yet
        # INF-ENV-004 / modulatory-bias-authority also list it and are implemented).
        # When the claim names `ceiling_retest_binding_substrate` (a list of the
        # claim ids the binding substrate must DELIVER), the ceiling only counts as
        # may-have-lifted once an IMPLEMENTED queue entry actually delivers that
        # binding mechanism (its unblocks_claims intersects the binding set).
        # Absent the field, behaviour is unchanged (any implemented owner + retest).
        _binding = c.get("ceiling_retest_binding_substrate")
        if isinstance(_binding, str):
            _binding = [_binding]
        binding_set = {str(x).strip() for x in (_binding or []) if str(x).strip()}
        binding_impl_entries = [
            e for e in queue
            if str(e.get("status", "")).strip().lower() == "implemented"
            and binding_set & set(e.get("unblocks_claims") or [])
        ] if binding_set else []
        if binding_set:
            lifted_ready = retest_owed and bool(binding_impl_entries)
        else:
            lifted_ready = retest_owed and implemented_owner is not None
        rec = {"id": cid, "status": c.get("status"), "n_ceiling_hits": n_hits}
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
        landed_in = None
        if parked:
            rec["ceiling_routing_note"] = (c.get("ceiling_routing_note") or "").strip()[:160]
            buckets["parked"].append(rec)
            landed_in = "parked"
        elif mapped and lifted_ready:
            rec["unblocked_by"] = (
                [e.get("sd_id") for e in binding_impl_entries] if binding_set
                else implemented_owner.get("sd_id")
            )
            buckets["ceiling_may_have_lifted"].append(rec)
            landed_in = "ceiling_may_have_lifted"
        elif mapped:
            rec["unblocked_by"] = [e.get("sd_id") for e in owners]
            buckets["mapped"].append(rec)
            landed_in = "mapped"
        elif self_handled:
            rec["own_substrate_entry"] = [
                {"sd_id": e.get("sd_id"), "status": e.get("status")} for e in own_entries
            ]
            buckets["self_handled"].append(rec)
            landed_in = "self_handled"
        else:
            buckets["orphaned"].append(rec)
            landed_in = "orphaned"

        # GOV-CEIL-1 ceiling-exhaustion overlay. A ceiling that has failed
        # discrimination N>=CEILING_EXHAUSTION_N times with no positive result on
        # a richer substrate has exhausted its grace: the inert-mechanism null
        # reading now stands co-equal, and the claim is surfaced for demotion to a
        # ceiling-exhausted contested candidate (governance Step 6a-v, user-
        # approved). Overlay only over `mapped` + `orphaned`: `parked` is a
        # deliberate deferral / user waiver, `ceiling_may_have_lifted` has an owed
        # retest that must run first (it may still vindicate the claim), and
        # `self_handled` bounds its dependents, not itself. A mapped-but-unbuilt
        # paper design owner does NOT exempt -- an owner that never lands across N
        # hits does not rescue the claim from the null.
        if landed_in in ("mapped", "orphaned") and n_hits >= CEILING_EXHAUSTION_N:
            exhausted.append({
                "id": cid,
                "status": c.get("status"),
                "n_ceiling_hits": n_hits,
                "bucket": landed_in,
            })

    return buckets, exhausted


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--claims", type=Path, default=DEFAULT_CLAIMS)
    ap.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    ap.add_argument("--autopsy-dir", type=Path, default=DEFAULT_AUTOPSY_DIR,
                    help="dir of failure_autopsy_*.json for the GOV-CEIL-1 hit count")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any genuinely-orphaned OR ceiling-exhausted claim exists")
    args = ap.parse_args()

    claims = load_claims(args.claims)
    queue = load_queue(args.queue)
    ceiling_hits = count_ceiling_hits(args.autopsy_dir)
    buckets, exhausted = audit(claims, queue, ceiling_hits=ceiling_hits)

    total = sum(len(v) for v in buckets.values())
    n_orphan = len(buckets["orphaned"])
    n_lifted = len(buckets["ceiling_may_have_lifted"])
    n_exhausted = len(exhausted)

    if args.json:
        print(json.dumps({
            "total": total,
            "ceiling_exhaustion_n": CEILING_EXHAUSTION_N,
            "buckets": buckets,
            "ceiling_exhausted": exhausted,
        }, indent=2))
    else:
        print(f"Substrate-ceiling mapping audit: {total} substrate_ceiling claim(s)")
        print(f"  mapped (design owner exists)            : {len(buckets['mapped'])}")
        print(f"  parked (ceiling_decision: deferred)     : {len(buckets['parked'])}")
        print(f"  self-handled (own implemented substrate): {len(buckets['self_handled'])}")
        print(f"  ceiling-may-have-lifted (ACTIONABLE)    : {n_lifted}")
        print(f"  genuinely-orphaned (ACTIONABLE)         : {n_orphan}")
        print(f"  ceiling-exhausted N>={CEILING_EXHAUSTION_N} (ACTIONABLE)    : {n_exhausted}")
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
        if n_exhausted:
            print("  -- CEILING-EXHAUSTED (GOV-CEIL-1): surface to user for demotion")
            print("     (epistemic_category -> standard, status floored to candidate,")
            print("      null-mechanism reading carried co-equally, ceiling_decision: exhausted):")
            for rec in sorted(exhausted, key=lambda r: -r["n_ceiling_hits"]):
                print(f"    [exhausted] {rec['id']} -- {rec['n_ceiling_hits']} ceiling hits "
                      f"(from {rec['bucket']}, status={rec['status']})")
        else:
            print(f"  -- no ceiling-exhausted claims (none at >={CEILING_EXHAUSTION_N} hits without a richer-substrate win).")

    if args.strict and (n_orphan or n_exhausted):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
