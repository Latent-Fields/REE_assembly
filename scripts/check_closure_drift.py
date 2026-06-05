#!/usr/bin/env python3
"""Detect closure_plan staleness across evidence/planning/*_plan.md.

A closure_plan node is *drifted* when its `status` is non-terminal
(in-progress / blocked / upstream-blocked / partial) but its `owner_exq`
has reached a terminal state -- the experiment has either left the
ree-v3/experiment_queue.json queue with a manifest in
REE_assembly/evidence/experiments/, or has a confirmed
failure_autopsy_<exq>_*.json artifact under evidence/planning/.

Two suppressors keep legitimate-but-non-terminal nodes out of the
"drifted" bucket (they are recorded in a separate "Suppressed" section
so suppression is auditable, never silent):

  1. Case 3 self-tag: the node carries a governance_<date> entry whose
     value contains the substring "Case 3 in closure-drift terms". This
     is the convention plans use to mark a node as legitimately
     non-terminal pending an upstream substrate or successor EXQ.

  2. Owner-exq manifest is non-contributory: the manifest exists but
     its `evidence_direction` field is in {non_contributory, superseded,
     inconclusive}. The experiment ran to completion but did not
     produce closure-grade evidence.

The owner_exq comparison above keys ENTIRELY on the node's recorded
`owner_exq`, which let goal_pipeline:GAP-2 hide on 2026-06-03: its
owner_exq pinned a stale lineage letter (514g) while the consequential
evidence (514l FAIL + 632/634 autopsies) landed on later letters and on
the node's `unblocks_claims` (MECH-229/230 reclassified substrate_ceiling)
-- none of which the owner_exq check looks at, and the 514g manifest's
non_contributory direction would only have parked it in Suppressed. So a
second, date-aware pass runs for EVERY non-terminal node (including ones
the rules above suppress) and reports them under "Stale since last
update" when either signal fires:

  A. Lineage-advanced: a later-lettered sibling of owner_exq (same EXQ
     number, lexically greater letter) has terminal evidence (manifest or
     failure_autopsy) -- the owner_exq pointer is behind its own lineage.

  B. Claims-reclassified-since: a CONFIRMED failure_autopsy whose
     targets[].claim_ids intersect the node's `unblocks_claims` is dated
     (generated_utc, else filename date) strictly AFTER the node's
     `last_updated` -- a governance decision the plan node has not yet
     absorbed. Same-day counts as reconciled (strict >), so a node updated
     in the same governance cycle that produced the autopsy stays clean.

These are review hints, not drift: a node can legitimately appear here
and still be correct (e.g. the maintainer judged the new evidence does
not change the node). They surface the "did the plan absorb today's
governance?" question that the owner_exq-only check could not ask.

Output is a markdown report at
REE_assembly/evidence/planning/closure_drift.md. The script exits 0
regardless of findings -- it is a governance hint, not a gate.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/check_closure_drift.py
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required.", file=sys.stderr)
    sys.exit(0)


REPO_ROOT = Path(__file__).resolve().parents[1]
PLANNING_DIR = REPO_ROOT / "evidence" / "planning"
EXPERIMENTS_DIR = REPO_ROOT / "evidence" / "experiments"
QUEUE_FILE = REPO_ROOT.parent / "ree-v3" / "experiment_queue.json"
DRIFT_REPORT = PLANNING_DIR / "closure_drift.md"

KNOWN_PLANS = [
    "arc_062_rule_apprehension_plan.md",
    "commitment_closure_plan.md",
    "infant_substrate_plan.md",
    "goal_pipeline_plan.md",
    "self_attribution_plan.md",
    "sd033_governance_plan.md",
    "sleep_substrate_plan.md",
    "behavioral_diversity_isolation_plan.md",
    "sd_037_axis_a_consumer_input_recalibration_plan.md",
    "sd_037_axis_b_sustained_threat_curriculum_plan.md",
]

NON_TERMINAL_STATUSES = {
    "in_progress",
    "in-progress",
    "blocked",
    "upstream_blocked",
    "upstream-blocked",
    "partial",
    "tracked",
    "open",
    # Plan-doc node sits at this status when its owner_exq has reached a
    # terminal state but the closure needs a governance-level decision that
    # cannot come out of the standard pipeline (e.g. R4.b on diagnostic-probe
    # evidence where scoring_excluded prevents auto-promotion). Added 2026-05-29
    # after behavioral_diversity_isolation:GAP-D was missed by this script for
    # 24h while parked here. Flagging it for the drift report makes the next
    # /governance cycle see it.
    "pending_governance_stamp",
}

EXQ_RE = re.compile(r"V3-EXQ-(\d+[a-z]?)", re.IGNORECASE)


def parse_plan_frontmatter(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    try:
        fm = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    if not isinstance(fm, dict):
        return None
    return fm


def load_queue_ids() -> set[str]:
    if not QUEUE_FILE.exists():
        return set()
    try:
        data = json.loads(QUEUE_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return set()
    items = data.get("items", data) if isinstance(data, dict) else data
    out: set[str] = set()
    if isinstance(items, list):
        for it in items:
            if isinstance(it, dict) and isinstance(it.get("queue_id"), str):
                out.add(it["queue_id"].upper())
    return out


def find_terminal_manifest(exq_id: str) -> Path | None:
    """Look for evidence/experiments/v3_exq_<num>_*_v3.json (flat or in subdir)."""
    m = EXQ_RE.search(exq_id)
    if not m:
        return None
    suffix = m.group(1).lower()
    pattern = f"v3_exq_{suffix}_"
    if not EXPERIMENTS_DIR.exists():
        return None
    # flat manifests at top of experiments/
    for p in EXPERIMENTS_DIR.glob(f"{pattern}*_v3.json"):
        return p
    # nested under per-experiment dirs
    for p in EXPERIMENTS_DIR.glob(f"{pattern}*/*_v3.json"):
        return p
    return None


CASE_3_MARKER = "Case 3 in closure-drift terms"
NON_CONTRIBUTORY_DIRECTIONS = {"non_contributory", "superseded", "inconclusive"}


def node_is_case_3(node: dict) -> bool:
    """True if any governance_<date> field on the node carries the Case-3 marker."""
    for k, v in node.items():
        if not isinstance(k, str) or not k.startswith("governance_"):
            continue
        if isinstance(v, str) and CASE_3_MARKER in v:
            return True
    return False


def manifest_evidence_direction(manifest_path: Path) -> str | None:
    """Read the manifest's evidence_direction field, lowercased. None on read error."""
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    direction = data.get("evidence_direction")
    if not isinstance(direction, str):
        return None
    return direction.strip().lower()


def find_failure_autopsy(exq_id: str) -> Path | None:
    if not PLANNING_DIR.exists():
        return None
    m = EXQ_RE.search(exq_id)
    if not m:
        return None
    suffix = m.group(1)
    for p in PLANNING_DIR.glob(f"failure_autopsy_V3-EXQ-{suffix}_*.json"):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return p  # presence is the signal even if unreadable
        status = (data.get("status") or "").lower()
        if status in {"confirmed", "complete", "completed"}:
            return p
        return p
    return None


# --- Date-aware "stale since last update" pass (signals A + B) ----------------

CONFIRMED_AUTOPSY_STATUSES = {"confirmed", "complete", "completed"}
_AUTOPSY_NAME_RE = re.compile(r"failure_autopsy_V3-EXQ-(\d+)([a-z]?)_(\d{4}-\d{2}-\d{2})", re.IGNORECASE)
_MANIFEST_NAME_RE = re.compile(r"v3_exq_(\d+)([a-z]?)_", re.IGNORECASE)


def _to_date(value):
    """Coerce a YAML date/datetime or ISO/YYYY-MM-DD string to a date. None on failure."""
    if isinstance(value, datetime):
        return value.date()
    # yaml.safe_load turns an unquoted YYYY-MM-DD into datetime.date already
    if hasattr(value, "year") and hasattr(value, "month") and not isinstance(value, str):
        return value
    if isinstance(value, str) and len(value) >= 10:
        try:
            return datetime.strptime(value[:10], "%Y-%m-%d").date()
        except ValueError:
            return None
    return None


def _exq_num_letter(exq_id: str):
    """('514g') -> (514, 'g'); ('582') -> (582, ''). None if not an EXQ id."""
    m = EXQ_RE.search(exq_id or "")
    if not m:
        return None
    mm = re.match(r"(\d+)([a-z]?)$", m.group(1).lower())
    if not mm:
        return None
    return int(mm.group(1)), mm.group(2)


def collect_terminal_lineage() -> dict[int, list[tuple[str, str]]]:
    """Map EXQ number -> [(letter, signal_str)] for every terminal manifest / autopsy.

    Used to detect when a node's owner_exq pins an earlier lineage letter than
    the latest letter that has actually produced terminal evidence.
    """
    fam: dict[int, list[tuple[str, str]]] = {}

    def add(num: int, letter: str, signal: str) -> None:
        fam.setdefault(num, []).append((letter, signal))

    if EXPERIMENTS_DIR.exists():
        for p in EXPERIMENTS_DIR.glob("v3_exq_*_v3.json"):
            mm = _MANIFEST_NAME_RE.match(p.name)
            if mm:
                add(int(mm.group(1)), mm.group(2).lower(), f"manifest `{p.name}`")
        # run-pack dirs (manifest may be runs/<id>/manifest.json, not *_v3.json)
        for d in EXPERIMENTS_DIR.glob("v3_exq_*"):
            if d.is_dir():
                mm = _MANIFEST_NAME_RE.match(d.name)
                if mm:
                    add(int(mm.group(1)), mm.group(2).lower(), f"manifest dir `{d.name}`")
    if PLANNING_DIR.exists():
        for p in PLANNING_DIR.glob("failure_autopsy_V3-EXQ-*_*.json"):
            mm = _AUTOPSY_NAME_RE.match(p.name)
            if mm:
                add(int(mm.group(1)), mm.group(2).lower(), f"autopsy `{p.name}`")
    return fam


def collect_confirmed_autopsies() -> list[dict]:
    """Confirmed failure-autopsies as {date, claim_ids:set, path} for signal B."""
    out: list[dict] = []
    if not PLANNING_DIR.exists():
        return out
    for p in PLANNING_DIR.glob("failure_autopsy_V3-EXQ-*_*.json"):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if (data.get("status") or "").strip().lower() not in CONFIRMED_AUTOPSY_STATUSES:
            continue
        claim_ids: set[str] = set()
        for t in data.get("targets") or []:
            if isinstance(t, dict):
                for c in t.get("claim_ids") or []:
                    if isinstance(c, str):
                        claim_ids.add(c.strip().upper())
        adate = _to_date(data.get("generated_utc"))
        if adate is None:
            mm = _AUTOPSY_NAME_RE.match(p.name)
            if mm:
                adate = _to_date(mm.group(3))
        out.append({"path": p.name, "date": adate, "claim_ids": claim_ids})
    return out


def lineage_advanced(owner_exq: str, fam: dict[int, list[tuple[str, str]]]) -> str | None:
    """If a later-lettered sibling of owner_exq has terminal evidence, describe it."""
    nl = _exq_num_letter(owner_exq)
    if nl is None:
        return None
    num, letter = nl
    successors = [(lt, sig) for (lt, sig) in fam.get(num, []) if lt > letter]
    if not successors:
        return None
    best_letter, best_sig = max(successors, key=lambda t: t[0])
    return (
        f"owner_exq pins V3-EXQ-{num}{letter or '(base)'} but later sibling "
        f"V3-EXQ-{num}{best_letter} has terminal evidence ({best_sig})"
    )


def claims_reclassified_since(node: dict, autopsies: list[dict]):
    """Confirmed autopsies touching this node's unblocks_claims, dated after last_updated."""
    unblocks = {
        str(c).strip().upper()
        for c in (node.get("unblocks_claims") or [])
        if isinstance(c, str)
    }
    if not unblocks:
        return None
    lu = _to_date(node.get("last_updated"))
    hits: list[str] = []
    for a in autopsies:
        if a["date"] is None:
            continue
        if lu is not None and not (a["date"] > lu):
            continue  # same-day or older == already reconciled
        overlap = sorted(a["claim_ids"] & unblocks)
        if overlap:
            hits.append(f"{a['path']} ({a['date'].isoformat()}) reclassified {', '.join(overlap)}")
    if not hits:
        return None
    # cap the rendered list so one ancient node can't flood the row
    shown = hits[:3]
    if len(hits) > 3:
        shown.append(f"(+{len(hits) - 3} more)")
    return "; ".join(shown)


def main() -> int:
    queue_ids = load_queue_ids()
    terminal_fam = collect_terminal_lineage()
    confirmed_autopsies = collect_confirmed_autopsies()
    findings: list[dict] = []
    suppressed: list[dict] = []
    stale_since: list[dict] = []
    missing_plan_last_updated: list[str] = []
    missing_files: list[str] = []

    for plan_name in KNOWN_PLANS:
        path = PLANNING_DIR / plan_name
        if not path.exists():
            missing_files.append(plan_name)
            continue
        fm = parse_plan_frontmatter(path)
        plan = fm.get("closure_plan") if isinstance(fm, dict) else None
        if not isinstance(plan, dict):
            continue

        if not plan.get("last_updated"):
            missing_plan_last_updated.append(plan_name)

        for node in plan.get("nodes", []) or []:
            if not isinstance(node, dict):
                continue
            status = (node.get("status") or "").strip().lower().replace(" ", "_")
            if status not in NON_TERMINAL_STATUSES:
                continue

            # Date-aware stale-since pass: runs for EVERY non-terminal node,
            # independent of whether the owner_exq pass below suppresses it.
            owner_raw = node.get("owner_exq")
            owner_str = owner_raw.strip() if isinstance(owner_raw, str) else ""
            reasons: list[str] = []
            if owner_str:
                la = lineage_advanced(owner_str, terminal_fam)
                if la:
                    reasons.append(la)
            cr = claims_reclassified_since(node, confirmed_autopsies)
            if cr:
                reasons.append(cr)
            if reasons:
                stale_since.append({
                    "plan": plan_name,
                    "node_id": node.get("id"),
                    "node_status": node.get("status"),
                    "owner_exq": owner_str or None,
                    "node_last_updated": node.get("last_updated"),
                    "reasons": reasons,
                })

            owner_exq = node.get("owner_exq")
            if not isinstance(owner_exq, str):
                continue
            exq_id = owner_exq.strip()
            if not EXQ_RE.search(exq_id):
                continue

            still_queued = exq_id.upper() in queue_ids
            manifest = find_terminal_manifest(exq_id)
            autopsy = find_failure_autopsy(exq_id)

            if still_queued:
                continue
            if not manifest and not autopsy:
                continue

            manifest_direction = manifest_evidence_direction(manifest) if manifest else None
            suppress_reason: str | None = None
            if node_is_case_3(node):
                suppress_reason = "case_3_self_tag"
            elif manifest_direction in NON_CONTRIBUTORY_DIRECTIONS:
                suppress_reason = f"manifest_evidence_direction={manifest_direction}"

            record = {
                "plan": plan_name,
                "node_id": node.get("id"),
                "node_status": node.get("status"),
                "owner_exq": exq_id,
                "node_last_updated": node.get("last_updated"),
                "manifest": manifest.relative_to(REPO_ROOT).as_posix() if manifest else None,
                "autopsy": autopsy.relative_to(REPO_ROOT).as_posix() if autopsy else None,
                "title": (node.get("title") or "")[:120],
                "suppress_reason": suppress_reason,
            }
            if suppress_reason:
                suppressed.append(record)
            else:
                findings.append(record)

    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = []
    lines.append(f"# Closure-Plan Drift Report")
    lines.append("")
    lines.append(f"Generated: {now_iso}")
    lines.append("")
    lines.append(
        "This report flags closure_plan nodes whose `owner_exq` has reached a "
        "terminal state (manifest landed and / or failure_autopsy artifact "
        "present) but whose `status` is still non-terminal. Nodes that "
        "self-tag as Case 3 (legitimately non-terminal pending upstream "
        "substrate or successor EXQs) and nodes whose owner_exq manifest is "
        "non-contributory / superseded / inconclusive are recorded under "
        "Suppressed instead, not Drifted. A separate date-aware section, "
        "`Stale since last update`, flags non-terminal nodes (including "
        "suppressed ones) where a later-lettered owner_exq sibling reached "
        "terminal state or a confirmed failure_autopsy touching the node's "
        "`unblocks_claims` post-dates the node's `last_updated` -- the class "
        "of staleness that hid goal_pipeline:GAP-2 on 2026-06-03. The report "
        "also flags plans missing a top-level `closure_plan.last_updated` field."
    )
    lines.append("")
    lines.append("Warn-only -- this script never blocks the governance pipeline.")
    lines.append("")

    lines.append(f"## Drifted nodes ({len(findings)})")
    lines.append("")
    if not findings:
        lines.append("_None._")
        lines.append("")
    else:
        lines.append("| plan | node | status | owner_exq | node last_updated | terminal signal |")
        lines.append("|------|------|--------|-----------|-------------------|-----------------|")
        for f in findings:
            signal_parts = []
            if f["manifest"]:
                signal_parts.append(f"manifest `{f['manifest']}`")
            if f["autopsy"]:
                signal_parts.append(f"autopsy `{f['autopsy']}`")
            lines.append(
                "| {plan} | `{node}` | {status} | {exq} | {lu} | {sig} |".format(
                    plan=f["plan"],
                    node=f["node_id"] or "?",
                    status=f["node_status"] or "?",
                    exq=f["owner_exq"],
                    lu=f["node_last_updated"] or "_unset_",
                    sig=" + ".join(signal_parts) or "?",
                )
            )
        lines.append("")

    lines.append(f"## Suppressed (legitimately non-terminal) ({len(suppressed)})")
    lines.append("")
    if not suppressed:
        lines.append("_None._")
        lines.append("")
    else:
        lines.append(
            "Nodes whose `owner_exq` reached a terminal state but where "
            "suppression rules say the node is legitimately non-terminal "
            "(Case-3 self-tag or non-contributory manifest evidence_direction). "
            "Listed here for audit; not counted as drift."
        )
        lines.append("")
        lines.append("| plan | node | status | owner_exq | suppress reason |")
        lines.append("|------|------|--------|-----------|-----------------|")
        for s in suppressed:
            lines.append(
                "| {plan} | `{node}` | {status} | {exq} | {reason} |".format(
                    plan=s["plan"],
                    node=s["node_id"] or "?",
                    status=s["node_status"] or "?",
                    exq=s["owner_exq"],
                    reason=s["suppress_reason"] or "?",
                )
            )
        lines.append("")

    # Drifted nodes already carry the strongest "go fix me" call; don't repeat
    # them in the review section. Suppressed nodes DO belong here -- suppression
    # on owner_exq is exactly what hid GAP-2.
    drifted_keys = {(f["plan"], f["node_id"]) for f in findings}
    stale_review = [s for s in stale_since if (s["plan"], s["node_id"]) not in drifted_keys]

    lines.append(f"## Stale since last update -- review ({len(stale_review)})")
    lines.append("")
    if not stale_review:
        lines.append("_None._")
        lines.append("")
    else:
        lines.append(
            "Non-terminal nodes (including ones Suppressed above) where newer "
            "evidence landed that the node frontmatter may not have absorbed: a "
            "later-lettered owner_exq sibling reached terminal state (lineage "
            "advanced), and / or a confirmed failure_autopsy touching the node's "
            "`unblocks_claims` is dated after the node's `last_updated`. Review "
            "each: update owner_exq / status / resume_condition and bump "
            "`last_updated`, or (if the new evidence genuinely does not change the "
            "node) bump `last_updated` to acknowledge it. Not counted as drift."
        )
        lines.append("")
        lines.append("| plan | node | status | owner_exq | node last_updated | why |")
        lines.append("|------|------|--------|-----------|-------------------|-----|")
        for s in stale_review:
            exq_disp = s["owner_exq"] or "_none_"
            if len(exq_disp) > 60:
                exq_disp = exq_disp[:57] + "..."
            lines.append(
                "| {plan} | `{node}` | {status} | {exq} | {lu} | {why} |".format(
                    plan=s["plan"],
                    node=s["node_id"] or "?",
                    status=s["node_status"] or "?",
                    exq=exq_disp,
                    lu=s["node_last_updated"] or "_unset_",
                    why="; ".join(s["reasons"]),
                )
            )
        lines.append("")

    lines.append(f"## Plans missing `closure_plan.last_updated` ({len(missing_plan_last_updated)})")
    lines.append("")
    if not missing_plan_last_updated:
        lines.append("_None._")
    else:
        for name in missing_plan_last_updated:
            lines.append(f"- `evidence/planning/{name}`")
    lines.append("")

    if missing_files:
        lines.append(f"## Known plan files missing on disk ({len(missing_files)})")
        lines.append("")
        for name in missing_files:
            lines.append(f"- `evidence/planning/{name}`")
        lines.append("")

    DRIFT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Closure drift report written: {DRIFT_REPORT.relative_to(REPO_ROOT)}")
    print(
        f"  drifted_nodes={len(findings)}  "
        f"suppressed={len(suppressed)}  "
        f"stale_since_review={len(stale_review)}  "
        f"plans_missing_last_updated={len(missing_plan_last_updated)}  "
        f"plans_missing_on_disk={len(missing_files)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
