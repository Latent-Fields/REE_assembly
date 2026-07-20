#!/usr/bin/env python3
"""Unapplied confirmed-autopsy recommendation audit (governance Step 3h, GOV-APPLY-1).

The FIFTH sibling of the failure-autopsy standing scans. The other four ask what a
set of verdicts MEANS, or whether the verdict was RECORDED. This one asks the next
question along: was the recorded verdict ever APPLIED?

  * GOV-CEIL-1  (check_substrate_ceiling_audit.py)      -- >=N ceiling verdicts on one claim
  * GOV-DIAG-1  (check_diagnostic_chain_recurrence.py)  -- >=N claimless no-verdict autopsies
  * GOV-GRAN-1  (check_granularity_debt_recurrence.py)  -- >=N structurally-different failures
  * GOV-CAT-1   (check_epistemic_category_completeness.py) -- the verdict was never RECORDED
  * GOV-APPLY-1 (this file)                             -- the verdict was never APPLIED

WHY THIS AUDIT EXISTS -- the already-reviewed blind spot
-------------------------------------------------------
/governance discovers autopsy recommendations by walking
`evidence/experiments/pending_review.md` and, for each run_id it surfaces, looking up
a confirmed `failure_autopsy_*.json` and reading its `recommended_*` fields
(governance SKILL.md Step 2 item 5). A run already listed in
`review_tracker.json:reviewed_run_ids` is ABSENT from pending_review.md -- so that
lookup NEVER RUNS for it.

The cycle therefore assumes adjudication precedes review. That assumption is FALSE
for every RE-adjudication, and a corpus sweep re-opens completed, reviewed runs BY
CONSTRUCTION. The recommendation is landed, confirmed, and structurally invisible.

Confirmed instance (the case this audit was built from), diagnosed in
`evidence/planning/intra_run_substrate_divergence_sweep_2026-07-20.md` sec 10:
`failure_autopsy_V3-EXQ-604c_2026-07-20` is confirmed and recommends demoting
MECH-314b / MECH-314c / Q-044 (`mixed` -> `non_contributory`, substrate_ceiling, on
structural vacuity). Its run is in reviewed_run_ids and returns 0 hits in
pending_review.md. The demotion survived THREE routing attempts (two spawn_task
chips that never produced a session, one application pass that landed the
substrate_queue entry but never reached the claim layer) before being caught by
hand.

The harm is not neutral. An unapplied demotion DECAYS INTO A POSITIVE CLAIM: while
604c sat unapplied, `inter_governance_workset.md` IGW-20260720-020 went on asserting
"Q-044/MECH-314-family leg is satisfied by V3-EXQ-604c PASS", which is precisely the
reading the autopsy withdrew.

WHAT IT DOES *NOT* DO. It never edits claims.yaml, and it is not a gate. It makes an
invisible debt visible; a human applies it in a /governance run. Read-only.

BUCKETS
-------
  unapplied_disposition  A confirmed target's `per_claim_recommendation[<claim>]`
                         records a `change` other than "STANDS" (e.g.
                         "mixed -> non_contributory"), and claims.yaml does not
                         reflect it. ACTIONABLE and STRICT-FAILING. This is the
                         high-precision bucket: the artifact states, in
                         machine-readable form, that a claim-layer change is owed.

  superseded_citation    A claim whose `live_status.evidence.from` cites autopsy X
                         for run R, while a NEWER confirmed adjudication of the same
                         run R exists. The claim is being weighted by a superseded
                         reading. WARN-only: supersession does not always change the
                         claim-layer disposition (R1-R3 shape (c) retains both
                         direction and category), so a hit here is "re-read", not
                         "re-apply".

COVERAGE IS REPORTED, DELIBERATELY
----------------------------------
`per_claim_recommendation` is a NEW convention (introduced by the 604c artifact),
so bucket 1 can only see targets that adopt it. The audit prints its own coverage
(`N of M confirmed targets carry a machine-readable per-claim disposition`) rather
than silently implying it checked everything.

That under-claim is deliberate, and it is the honest design. The rejected
alternative was to INFER "change owed" by comparing each target's
`recommended_epistemic_category` against the claim's current one. Measured
2026-07-20, that yields 338 claim-level mismatches, the overwhelming majority of
which are NOT defects -- an affirming autopsy (routing `governance-affirm`,
direction unchanged) legitimately recommends a per-target category that the claim
layer never mirrors. `failure_autopsy_V3-EXQ-778a_2026-07-20` is the canonical
example: `instrument_repair_validated` against four claims that correctly carry no
category. A 338-line report that is mostly wrong would be ignored, and an ignored
report is the same failure as no report. Precision first; coverage grows as the
convention spreads.

KNOWN LIMIT. Bucket 2 keys on run_id, so it cannot see a supersession that moves to
a DIFFERENT run. Q-044 is exactly that case -- it cites the 604b cluster autopsy
while the superseding adjudication is of 604c, a different run -- and is caught only
by bucket 1. Do not read an empty bucket 2 as "no stale citations".

USAGE
  python3 scripts/check_unapplied_autopsy_recommendations.py
  python3 scripts/check_unapplied_autopsy_recommendations.py --strict  # exit 1 on bucket 1
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
AUTOPSY_GLOB = "evidence/planning/failure_autopsy_*.json"
CLAIMS_YAML = "docs/claims/claims.yaml"

STANDS = "STANDS"


def _load_json(path: Path):
    try:
        with open(path) as fh:
            return json.load(fh)
    except Exception:
        return None


def _claim_ids(target: dict) -> list:
    cids = target.get("claim_ids")
    if isinstance(cids, list) and cids:
        return [c for c in cids if isinstance(c, str)]
    single = target.get("claim_id")
    return [single] if isinstance(single, str) and single else []


def load_confirmed(root: Path):
    """Return (targets, latest_by_run, runs_by_slug).

    targets     : list of (generated_utc, slug, target dict)
    latest_by_run: run_id -> (generated_utc, slug)   [R2: latest adjudication wins]
    runs_by_slug: slug -> set(run_id)
    """
    targets = []
    latest = {}
    runs_by_slug = {}
    for p in sorted(glob.glob(str(root / AUTOPSY_GLOB))):
        path = Path(p)
        data = _load_json(path)
        if not isinstance(data, dict):
            continue
        if str(data.get("status")) != "confirmed":
            continue
        gen = str(data.get("generated_utc") or "")
        slug = path.stem
        for target in data.get("targets", []) or []:
            if not isinstance(target, dict):
                continue
            targets.append((gen, slug, target))
            run_id = target.get("run_id")
            if not isinstance(run_id, str) or not run_id:
                continue
            runs_by_slug.setdefault(slug, set()).add(run_id)
            # R2 -- the most recent adjudication of a run supersedes its predecessors
            if run_id not in latest or (gen, slug) > latest[run_id]:
                latest[run_id] = (gen, slug)
    return targets, latest, runs_by_slug


def load_claims(root: Path) -> dict:
    """Index claims.yaml by id. Falls back to a regex scan if PyYAML is absent."""
    path = root / CLAIMS_YAML
    try:
        import yaml  # noqa: F401
    except ImportError:
        return _load_claims_regex(path)
    import yaml
    try:
        with open(path) as fh:
            doc = yaml.safe_load(fh)
    except Exception:
        return _load_claims_regex(path)
    claims = {}

    def harvest(node):
        if isinstance(node, dict):
            cid = node.get("id")
            if isinstance(cid, str):
                claims[cid] = node
            for value in node.values():
                harvest(value)
        elif isinstance(node, list):
            for value in node:
                harvest(value)

    harvest(doc)
    return claims


def _load_claims_regex(path: Path) -> dict:
    """Degraded index: id -> {} so membership tests still work without PyYAML."""
    try:
        text = path.read_text()
    except OSError:
        return {}
    return {m.group(1): {} for m in re.finditer(r"^\s*-?\s*id:\s*(\S+)\s*$", text, re.M)}


def _reflects(claim: dict, change: str, recommended_direction, slug: str) -> bool:
    """Is this per-claim disposition already reflected in claims.yaml?

    Deliberately BIASED TOWARD FALSE POSITIVES (reporting an applied item costs one
    glance; omitting an unapplied one is the whole defect). Applied iff EITHER the
    claim's live_status provenance cites this autopsy, OR its recorded direction
    already equals the recommendation's right-hand side.
    """
    if not isinstance(claim, dict) or not claim:
        return False
    live = claim.get("live_status")
    if isinstance(live, dict):
        evidence = live.get("evidence")
        if isinstance(evidence, dict) and slug in str(evidence.get("from") or ""):
            return True
    target_state = None
    if isinstance(change, str) and "->" in change:
        target_state = change.split("->")[-1].strip()
    elif isinstance(recommended_direction, str):
        target_state = recommended_direction.strip()
    if not target_state:
        return False
    for field in ("evidence_direction", "epistemic_category", "status"):
        if str(claim.get(field) or "").strip() == target_state:
            return True
    if isinstance(live, dict) and str(live.get("reading") or "").strip() == target_state:
        return True
    return False


def scan(root: Path) -> dict:
    targets, latest, runs_by_slug = load_confirmed(root)
    claims = load_claims(root)

    unapplied = []
    n_with_pcr = 0
    for gen, slug, target in targets:
        run_id = target.get("run_id")
        # R2 -- only the latest adjudication of a run is authoritative
        if isinstance(run_id, str) and run_id in latest and latest[run_id] != (gen, slug):
            continue
        pcr = target.get("per_claim_recommendation")
        if not isinstance(pcr, dict) or not pcr:
            continue
        n_with_pcr += 1
        for cid, rec in pcr.items():
            if not isinstance(rec, dict):
                continue
            change = str(rec.get("change") or "").strip()
            if not change or change.upper() == STANDS:
                continue
            claim = claims.get(cid)
            if claim is None:
                continue  # claim id not in registry -- GOV-CAT-1's lane, not ours
            if _reflects(claim, change, rec.get("recommended_evidence_direction"), slug):
                continue
            unapplied.append({
                "claim_id": cid,
                "change": change,
                "artifact": slug,
                "generated_utc": gen,
                "run_id": run_id,
                "recommended_epistemic_category": rec.get("recommended_epistemic_category"),
            })

    superseded = []
    for cid, claim in sorted(claims.items()):
        live = claim.get("live_status") if isinstance(claim, dict) else None
        if not isinstance(live, dict):
            continue
        evidence = live.get("evidence")
        if not isinstance(evidence, dict):
            continue
        match = re.match(r"(failure_autopsy_[^#\s]+)", str(evidence.get("from") or ""))
        if not match:
            continue
        cited = match.group(1).strip()
        for run_id in sorted(runs_by_slug.get(cited, ())):
            newest = latest.get(run_id, ("", ""))[1]
            if newest and newest != cited:
                superseded.append({
                    "claim_id": cid, "cites": cited,
                    "superseded_by": newest, "run_id": run_id,
                })
                break

    return {
        "unapplied_disposition": unapplied,
        "superseded_citation": superseded,
        "n_confirmed_targets": len(targets),
        "n_with_per_claim_recommendation": n_with_pcr,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 if any unapplied_disposition is found")
    parser.add_argument("--root", default=str(REPO_ROOT),
                        help="REE_assembly root (default: this script's parent)")
    args = parser.parse_args()

    root = Path(args.root)
    buckets = scan(root)
    unapplied = buckets["unapplied_disposition"]
    superseded = buckets["superseded_citation"]
    n_targets = buckets["n_confirmed_targets"]
    n_pcr = buckets["n_with_per_claim_recommendation"]

    print("Unapplied confirmed-autopsy recommendation audit (GOV-APPLY-1)")
    print("  unapplied claim disposition (ACTIONABLE): %d" % len(unapplied))
    print("  superseded live_status citation (WARN)  : %d" % len(superseded))
    print("  coverage: %d of %d confirmed targets carry a machine-readable"
          % (n_pcr, n_targets))
    print("            per-claim disposition; the rest CANNOT be checked.")

    if unapplied:
        print("")
        print("ACTIONABLE -- a confirmed autopsy records a claim-layer change that")
        print("claims.yaml does not reflect. These are invisible to the /governance")
        print("walk whenever the run is already in reviewed_run_ids (the whole point")
        print("of this audit). Apply them in a /governance run; do NOT edit here.")
        for item in sorted(unapplied, key=lambda d: (d["generated_utc"], d["claim_id"])):
            print("  - %-12s %s" % (item["claim_id"], item["change"]))
            print("      from %s (%s)" % (item["artifact"], item["generated_utc"][:10]))
    else:
        print("")
        print("  -- no confirmed autopsy has an unapplied claim disposition.")

    if superseded:
        print("")
        print("WARN -- claim live_status cites an autopsy that a NEWER confirmed")
        print("adjudication of the same run supersedes. Re-read before citing; under")
        print("R1-R3 shape (c) a supersession may legitimately retain the reading.")
        for item in superseded:
            print("  - %-12s cites %s" % (item["claim_id"], item["cites"]))
            print("      superseded by %s" % item["superseded_by"])

    print("")
    print("Read-only. Promotes/demotes nothing. See intra_run_substrate_divergence_"
          "sweep_2026-07-20.md sec 10.")

    if args.strict and unapplied:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
