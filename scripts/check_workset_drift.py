#!/usr/bin/env python3
"""Re-validate every `ready` inter-governance-workset item against ground truth.

Defense-in-depth sibling of check_closure_drift.py. The workset generator
(generate_inter_governance_workset.py) decides readiness from substrate_queue
`ready` flags, claims.yaml status / epistemic_category, queue-claim coverage and
the proposals file. This script reads the WRITTEN
evidence/planning/inter_governance_workset.v1.json and independently re-checks
each item whose status is `ready`, warning when an item is in fact blocked,
done, queued, or otherwise inappropriate to surface as ready. It catches:

  * a stale workset artifact (regenerate fixed the logic but the JSON on disk is
    old),
  * ground-truth drift since the last regen (a queued retest now covers a ready
    retest claim; a substrate flipped ready=False; a claim was resolved),
  * a logic regression in the generator (a class of false-ready slips back in).

It deliberately re-derives readiness from the source-of-truth loaders in
generate_inter_governance_workset rather than trusting the workset's own
`blocked_by`, so a generator bug cannot hide itself.

Output: evidence/planning/workset_drift.md. Exits 0 regardless of findings --
a governance hint, not a gate (matching check_closure_drift.py).

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/check_workset_drift.py
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLANNING = ROOT / "evidence" / "planning"
WORKSET_JSON = PLANNING / "inter_governance_workset.v1.json"
DRIFT_REPORT = PLANNING / "workset_drift.md"

sys.path.insert(0, str(ROOT / "scripts"))
try:
    import generate_inter_governance_workset as g
except Exception as exc:  # pragma: no cover - import guard
    print(f"ERROR: cannot import generate_inter_governance_workset: {exc}", file=sys.stderr)
    sys.exit(0)

_PROPOSAL_TITLE_RE = re.compile(
    r"^(?:Proposal|Literature proposal)\s+(?:for\s+(\S+)|\(unclaimed\))$"
)


def _load_workset() -> dict | None:
    if not WORKSET_JSON.exists():
        return None
    try:
        return json.loads(WORKSET_JSON.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def check() -> list[dict]:
    """Return a list of {item_id, title, reason} drift findings."""
    data = _load_workset()
    if not data:
        return [{"item_id": "-", "title": "(workset missing/unparseable)",
                 "reason": f"cannot read {WORKSET_JSON.relative_to(ROOT)}"}]

    substrate_by_id = g._substrate_by_id()
    claims_meta = g._load_claims_meta()
    queue_items = g._load_queue()
    queued_coverage = g._queued_retest_coverage(queue_items)
    exp_evidence = g._claims_with_experimental_evidence()

    findings: list[dict] = []
    seen_proposal_ids: set[str] = set()

    for it in data.get("items") or []:
        if not isinstance(it, dict) or it.get("status") != "ready":
            continue
        iid = it.get("id") or "?"
        title = it.get("title") or ""
        lane = it.get("lane") or ""
        skill = it.get("skill") or ""

        # Governance / ops / monitor items are human-judged; not drift-checkable here.
        if lane in ("governance", "ops", "plan", "monitor"):
            continue

        # --- Retest-after-substrate items -------------------------------------
        if title.startswith("Retest after substrate:"):
            cids = it.get("claim_ids") or []
            cid = cids[0] if cids else ""
            meta = claims_meta.get(cid) or {}
            cstatus = (meta.get("status") or "").strip().lower()
            if cstatus in g._CLAIM_DEAD_STATUSES:
                findings.append({"item_id": iid, "title": title,
                                 "reason": f"claim {cid} status={cstatus} (dead) -- retest moot"})
                continue
            if cid in queued_coverage:
                findings.append({"item_id": iid, "title": title,
                                 "reason": f"claim {cid} already covered by queued {queued_coverage[cid]} -- should be auto-absorbed, not ready"})
                continue
            blocker_strs, _ = g._retest_blockers(cid, substrate_by_id)
            if blocker_strs:
                findings.append({"item_id": iid, "title": title,
                                 "reason": f"claim {cid} has {len(blocker_strs)} live substrate blocker(s): {blocker_strs[0]}"})
                continue
            if g._resolve_epistemic_category(meta) == "substrate_ceiling":
                unblocking = [e for e in substrate_by_id.values()
                              if cid in (e.get("unblocks_claims") or [])]
                if not unblocking:
                    findings.append({"item_id": iid, "title": title,
                                     "reason": f"substrate_ceiling claim {cid} has no ready substrate_queue entry -- awaiting enrichment, should be blocked"})
                    continue
            continue

        # --- Substrate implement items ----------------------------------------
        m_sub = re.match(r"^Substrate ready:\s*(\S+)", title) or \
            re.match(r"^Implement substrate:\s*(\S+)", title)
        if m_sub:
            sid = m_sub.group(1)
            entry = substrate_by_id.get(sid)
            if entry is None:
                findings.append({"item_id": iid, "title": title,
                                 "reason": f"substrate {sid} has no substrate_queue entry"})
                continue
            if g._substrate_resolved(entry):
                findings.append({"item_id": iid, "title": title,
                                 "reason": f"substrate {sid} is resolved/done -- should not surface as implement-task (status={entry.get('status')})"})
                continue
            if entry.get("ready") is False:
                findings.append({"item_id": iid, "title": title,
                                 "reason": f"substrate {sid} is ready=False -- should be blocked, not ready"})
                continue
            continue

        # --- Proposal items ----------------------------------------------------
        m_prop = _PROPOSAL_TITLE_RE.match(title)
        if m_prop:
            cid = m_prop.group(1) or ""
            # Titles are claim-keyed, not proposal_id-keyed (0e409601fd) -- the
            # current proposal_id lives on the item itself, not in the title.
            pid = it.get("owner_proposal_id") or ""
            dedup_key = pid or iid
            if dedup_key in seen_proposal_ids:
                findings.append({"item_id": iid, "title": title,
                                 "reason": f"duplicate proposal_id {dedup_key} surfaced twice"})
                continue
            seen_proposal_ids.add(dedup_key)
            meta = claims_meta.get(cid) or {}
            cstatus = (meta.get("status") or "").strip().lower()
            if cstatus in g._CLAIM_DEAD_STATUSES:
                findings.append({"item_id": iid, "title": title,
                                 "reason": f"proposal {pid} claim {cid} status={cstatus} (dead)"})
                continue
            epi = g._resolve_epistemic_category(meta)
            if epi in g._EPI_SUPPRESS_PROPOSAL:
                findings.append({"item_id": iid, "title": title,
                                 "reason": f"proposal {pid} claim {cid} epistemic_category={epi} -- experiment inappropriate"})
                continue
            if cid in exp_evidence:
                findings.append({"item_id": iid, "title": title,
                                 "reason": f"proposal {pid} claim {cid} already has experimental evidence -- likely executed"})
                continue
            continue

        # Diagnose-ERROR and other experiment/lit items: re-check queue coverage
        # only (deeper checks live in the generator's own suppressors).
        owner = it.get("owner_exq")
        if isinstance(owner, str) and owner.upper() in {q.upper() for q in queued_coverage.values()}:
            findings.append({"item_id": iid, "title": title,
                             "reason": f"owner_exq {owner} appears already queued"})

    return findings


def main() -> int:
    findings = check()
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = [
        "# Inter-Governance Workset Drift Report",
        "",
        f"Generated: {now_iso}",
        "",
        "Re-validates every `ready` item in "
        "`evidence/planning/inter_governance_workset.v1.json` against current "
        "ground truth (claim status, epistemic_category, substrate_queue `ready` "
        "flags, queue-claim coverage, experimental-evidence presence). A ready "
        "item that is in fact blocked, done, already-queued, or inappropriate is "
        "flagged below. Warn-only -- never blocks the governance pipeline. If "
        "findings appear, regenerate the workset "
        "(`scripts/generate_inter_governance_workset.py`); if they persist, the "
        "generator logic or the ground-truth data has drifted.",
        "",
        f"## Ready items that look wrong ({len(findings)})",
        "",
    ]
    if not findings:
        lines.append("_None -- every ready item re-validates clean._")
    else:
        lines.append("| item | title | reason |")
        lines.append("|------|-------|--------|")
        for f in findings:
            lines.append(
                "| {iid} | {title} | {reason} |".format(
                    iid=f["item_id"],
                    title=(f["title"] or "")[:70].replace("|", "\\|"),
                    reason=f["reason"].replace("|", "\\|"),
                )
            )
    lines.append("")

    DRIFT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Workset drift report written: {DRIFT_REPORT.relative_to(ROOT)}")
    print(f"  ready_items_flagged={len(findings)}")
    if findings:
        for f in findings:
            print(f"  WARN [{f['item_id']}] {f['reason']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
