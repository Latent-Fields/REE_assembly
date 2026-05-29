#!/usr/bin/env python3
"""Detect closure_plan staleness across evidence/planning/*_plan.md.

A closure_plan node is *drifted* when its `status` is non-terminal
(in-progress / blocked / upstream-blocked / partial) but its `owner_exq`
has reached a terminal state -- the experiment has either left the
ree-v3/experiment_queue.json queue with a manifest in
REE_assembly/evidence/experiments/, or has a confirmed
failure_autopsy_<exq>_*.json artifact under evidence/planning/.

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


def main() -> int:
    queue_ids = load_queue_ids()
    findings: list[dict] = []
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

            findings.append({
                "plan": plan_name,
                "node_id": node.get("id"),
                "node_status": node.get("status"),
                "owner_exq": exq_id,
                "node_last_updated": node.get("last_updated"),
                "manifest": manifest.relative_to(REPO_ROOT).as_posix() if manifest else None,
                "autopsy": autopsy.relative_to(REPO_ROOT).as_posix() if autopsy else None,
                "title": (node.get("title") or "")[:120],
            })

    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = []
    lines.append(f"# Closure-Plan Drift Report")
    lines.append("")
    lines.append(f"Generated: {now_iso}")
    lines.append("")
    lines.append(
        "This report flags closure_plan nodes whose `owner_exq` has reached a "
        "terminal state (manifest landed and / or failure_autopsy artifact "
        "present) but whose `status` is still non-terminal. It also flags "
        "plans missing a top-level `closure_plan.last_updated` field."
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
        f"plans_missing_last_updated={len(missing_plan_last_updated)}  "
        f"plans_missing_on_disk={len(missing_files)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
