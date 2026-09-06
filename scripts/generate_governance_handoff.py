#!/usr/bin/env python3
"""
Generate a structured governance handoff document from current REE_assembly state.

Reads:
  evidence/verification/governance_verification_latest.json (if present)
  evidence/experiments/pending_review.md
  docs/roadmap.md
  evidence/planning/inter_governance_workset.v1.json
  evidence/experiments/runner_heartbeats/*.json

Writes:
  evidence/handoffs/active_governance_handoff.json
  evidence/handoffs/active_governance_handoff.md

This script is read-only with respect to all governance files. Its only writes are
to evidence/handoffs/.
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

VERIFICATION_REPORT_PATH = "evidence/verification/governance_verification_latest.json"
HANDOFF_JSON_PATH = "evidence/handoffs/active_governance_handoff.json"
HANDOFF_MD_PATH = "evidence/handoffs/active_governance_handoff.md"

HEARTBEAT_STALE_HOURS = 4.0


def _coordinator_rows():
    """Live /shadow/status rows keyed by machine, or None when unavailable.

    Coordinator-primary telemetry (2026-09-01): the git materialization of
    runner_heartbeats/ is retired (removed from master 2026-09-06), so in-flight
    liveness is judged from the coordinator when it answers and from the git
    files only when it does not. Never raises; any failure returns None so
    callers fall back to today's behavior.
    """
    try:
        _here = str(Path(__file__).resolve().parent)
        if _here not in sys.path:
            sys.path.insert(0, _here)
        import fleet_status_client
    except Exception:
        return None
    try:
        rows = fleet_status_client.machine_rows()
    except Exception:
        return None
    return rows or None


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate REE_assembly governance handoff (JSON + Markdown)."
    )
    parser.add_argument("--repo-root", default=".", help="Path to REE_assembly root")
    return parser.parse_args()


def get_git_head(repo_root):
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True, text=True, cwd=str(repo_root)
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def parse_iso_timestamp(ts_str):
    if not ts_str:
        return None
    ts_str = ts_str.strip().rstrip("Z")
    ts_str = re.sub(r"\+00:00$", "", ts_str)
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M"):
        try:
            return datetime.strptime(ts_str, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def now_utc():
    return datetime.now(timezone.utc)


def load_verification_report(repo_root):
    path = repo_root / VERIFICATION_REPORT_PATH
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def load_pending_review(repo_root):
    path = repo_root / "evidence/experiments/pending_review.md"
    out = {"pending_count": None, "generated_at": None, "fails": [], "passes": [], "errors": []}
    if not path.exists():
        return out

    text = path.read_text(encoding="utf-8")

    m = re.search(r"Pending:\s*\*\*(\d+)\*\*", text)
    if m:
        out["pending_count"] = int(m.group(1))

    m = re.search(r"Generated:\s*`([^`]+)`", text)
    if m:
        out["generated_at"] = m.group(1)

    fail_m = re.search(r"## FAIL.*?\n(.*?)(?=^## |\Z)", text, re.DOTALL | re.MULTILINE)
    if fail_m:
        out["fails"] = re.findall(r"`(v3_exq_[^`]+)`", fail_m.group(1))

    pass_m = re.search(r"## PASS.*?\n(.*?)(?=^## |\Z)", text, re.DOTALL | re.MULTILINE)
    if pass_m:
        out["passes"] = re.findall(r"`(v3_exq_[^`]+)`", pass_m.group(1))

    return out


def load_roadmap_immediate_queue(repo_root):
    path = repo_root / "docs/roadmap.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    m = re.search(r"### Immediate Work Queue[^\n]*\n(.*?)(?=\n###|\n## |\Z)", text, re.DOTALL)
    if not m:
        return []
    items = re.findall(r"^\d+\.\s+\*\*([^*]+)\*\*", m.group(1), re.MULTILINE)
    return items


def load_workset_summary(repo_root):
    path = repo_root / "evidence/planning/inter_governance_workset.v1.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        s = data.get("summary", {})
        return {
            "total": s.get("total"),
            "ready": s.get("ready"),
            "in_flight": s.get("in_flight"),
            "blocked": s.get("blocked"),
            "pending_review_count": s.get("pending_review_count"),
            "live_exqs": s.get("live_exqs", []),
        }
    except Exception:
        return None


def load_in_flight_experiments(repo_root):
    heartbeats_dir = repo_root / "evidence/experiments/runner_heartbeats"

    # Coordinator-primary: prefer live /shadow/status rows for in-flight
    # detection. The git heartbeat file (when present) only enriches the
    # title/claim fields, which the coordinator rows do not carry. Output
    # shape is identical to the git path below.
    coord_rows = _coordinator_rows()
    if coord_rows:
        in_flight = []
        for machine in sorted(coord_rows):
            row = coord_rows[machine]
            last_seen = str(row.get("last_seen") or "")
            tick = parse_iso_timestamp(last_seen)
            if tick:
                age_h = (now_utc() - tick).total_seconds() / 3600
                if age_h > HEARTBEAT_STALE_HOURS:
                    continue
            if row.get("state") == "running" and row.get("current_exq"):
                prog = row.get("progress") or {}
                hb_git = {}
                hb_file = heartbeats_dir / (machine + ".json")
                if hb_file.exists():
                    try:
                        hb_git = json.loads(hb_file.read_text(encoding="utf-8"))
                    except Exception:
                        hb_git = {}
                in_flight.append({
                    "machine": machine,
                    "exq": row.get("current_exq"),
                    "title": hb_git.get("current_title", ""),
                    "claim_id": hb_git.get("current_claim_id", ""),
                    "progress_pct": (prog.get("overall_pct")
                                     if isinstance(prog, dict) else None),
                    "last_tick_utc": last_seen or None,
                })
        return in_flight

    # Git fallback -- unchanged legacy read of the frozen heartbeat mirror.
    if not heartbeats_dir.exists():
        return []

    in_flight = []
    for hb_file in sorted(heartbeats_dir.glob("*.json")):
        if hb_file.name == "README.md":
            continue
        try:
            hb = json.loads(hb_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        tick = parse_iso_timestamp(hb.get("last_tick_utc", ""))
        if tick:
            age_h = (now_utc() - tick).total_seconds() / 3600
            if age_h > HEARTBEAT_STALE_HOURS:
                continue

        if hb.get("state") == "running" and hb.get("current_exq"):
            prog = hb.get("progress", {})
            in_flight.append({
                "machine": hb.get("machine", hb_file.stem),
                "exq": hb.get("current_exq"),
                "title": hb.get("current_title", ""),
                "claim_id": hb.get("current_claim_id", ""),
                "progress_pct": prog.get("overall_pct"),
                "last_tick_utc": hb.get("last_tick_utc"),
            })
    return in_flight


def determine_next_action(verification_report, pending_review, in_flight, immediate_queue):
    """Return a single concrete next action string."""
    if verification_report:
        blocks = [f for f in verification_report.get("findings", []) if f["severity"] == "block"]
        if blocks:
            action = blocks[0].get("suggested_next_action") or (
                f"Resolve block [{blocks[0]['code']}]: {blocks[0]['message'][:80]}"
            )
            return action

    if pending_review.get("fails"):
        n = len(pending_review["fails"])
        return (
            f"Run /failure-autopsy for {n} FAIL experiment(s) in pending_review.md, "
            "then re-run governance pipeline."
        )

    pending = pending_review.get("pending_count") or 0
    if pending > 0:
        return (
            f"Walk the {pending} pending experiments in pending_review.md "
            "(PASS: verify+close; FAIL: failure-autopsy or non_contributory; "
            "ERROR: runner-ack). Re-run generate_pending_review.py after."
        )

    if in_flight:
        exqs = [e["exq"] for e in in_flight]
        return (
            f"Wait for in-flight experiment(s) ({', '.join(exqs)}) to complete, "
            "then re-run governance pipeline."
        )

    if immediate_queue:
        return immediate_queue[0]

    return (
        "Run bash scripts/governance.sh to regenerate pending_review.md, "
        "then walk any new items."
    )


def generate_handoff(repo_root):
    generated_at = now_utc().isoformat()
    git_head = get_git_head(repo_root)

    verification_report = load_verification_report(repo_root)
    pending_review = load_pending_review(repo_root)
    workset_summary = load_workset_summary(repo_root)
    in_flight = load_in_flight_experiments(repo_root)
    immediate_queue = load_roadmap_immediate_queue(repo_root)

    ver_status = "not_run"
    ver_report_path = None
    open_risks = []
    blocked_items = []

    if verification_report:
        ver_status = verification_report.get("status", "unknown")
        ver_report_path = VERIFICATION_REPORT_PATH
        for f in verification_report.get("findings", []):
            if f["severity"] == "block":
                blocked_items.append({
                    "code": f["code"],
                    "message": f["message"],
                    "suggested_next_action": f.get("suggested_next_action", ""),
                })
            if f["severity"] in ("block", "warn"):
                open_risks.append(
                    f"{f['severity'].upper()} [{f['code']}]: {f['message'][:120]}"
                )

    # Summary
    parts = []
    pending = pending_review.get("pending_count")
    if pending is not None:
        parts.append(f"{pending} experiments pending review")
        n_pass = len(pending_review.get("passes", []))
        n_fail = len(pending_review.get("fails", []))
        if n_pass or n_fail:
            parts.append(f"({n_pass} PASS / {n_fail} FAIL)")
    if in_flight:
        parts.append(f"{len(in_flight)} experiment(s) in flight")
    if workset_summary:
        parts.append(
            f"workset: {workset_summary.get('ready', '?')} ready / "
            f"{workset_summary.get('blocked', '?')} blocked"
        )
    summary = "; ".join(parts) if parts else "No summary data available."

    next_action = determine_next_action(
        verification_report, pending_review, in_flight, immediate_queue
    )

    relevant_files = [
        "evidence/experiments/pending_review.md",
        "docs/roadmap.md",
        "evidence/planning/inter_governance_workset.v1.json",
        "FLEET_STATUS.md",  # live-status branch; coordinator /shadow/status is the source of truth
    ]
    if ver_report_path:
        relevant_files.insert(0, ver_report_path)

    assumptions = []
    if verification_report is None:
        assumptions.append(
            "No verification report found -- run verify_governance_cycle.py first."
        )
    if workset_summary is None:
        assumptions.append(
            "inter_governance_workset.v1.json not found -- workset summary absent."
        )
    if not in_flight:
        assumptions.append(
            "No machines report running state in recent heartbeats -- "
            "all runners may be idle or heartbeats may be stale (>4h)."
        )

    return {
        "generated_at_utc": generated_at,
        "git_head": git_head,
        "verification_status": ver_status,
        "verification_report_path": ver_report_path,
        "summary": summary,
        "open_risks": open_risks,
        "changed_or_relevant_files": relevant_files,
        "blocked_items": blocked_items,
        "in_flight_experiments": in_flight,
        "failed_attempts_or_unresolved_failures": [
            {"run_id": r, "status": "FAIL", "autopsy": "pending"}
            for r in pending_review.get("fails", [])
        ],
        "next_action": next_action,
        "assumptions_to_validate": assumptions,
    }


def render_markdown(h):
    lines = [
        "# REE_assembly Active Governance Handoff",
        "",
        f"Generated: `{h['generated_at_utc']}`  ",
        f"Git HEAD: `{h.get('git_head', 'unknown')}`  ",
        f"Verification: **{h['verification_status'].upper()}**",
        "",
        "## Summary",
        "",
        h["summary"],
        "",
    ]

    lines += [
        "## Next Action",
        "",
        f"> {h['next_action']}",
        "",
    ]

    if h["blocked_items"]:
        lines += ["## Blocked Items (Verification Gate)", ""]
        for b in h["blocked_items"]:
            lines.append(f"- **[{b['code']}]** {b['message']}")
            if b.get("suggested_next_action"):
                lines.append(f"  - Action: {b['suggested_next_action']}")
        lines.append("")

    if h["open_risks"]:
        lines += ["## Open Risks", ""]
        for r in h["open_risks"]:
            lines.append(f"- {r}")
        lines.append("")

    if h["in_flight_experiments"]:
        lines += ["## In-Flight Experiments", ""]
        for e in h["in_flight_experiments"]:
            pct = f"{e['progress_pct']:.0f}%" if e.get("progress_pct") is not None else "?"
            lines.append(
                f"- **{e['exq']}** on `{e['machine']}` ({pct}) -- {e.get('title', '')}"
            )
        lines.append("")

    if h["failed_attempts_or_unresolved_failures"]:
        lines += ["## Unresolved Failures (Pending Autopsy)", ""]
        for f in h["failed_attempts_or_unresolved_failures"]:
            lines.append(f"- `{f['run_id']}` -- autopsy: {f['autopsy']}")
        lines.append("")

    if h["assumptions_to_validate"]:
        lines += ["## Assumptions to Validate", ""]
        for a in h["assumptions_to_validate"]:
            lines.append(f"- {a}")
        lines.append("")

    lines += ["## Relevant Files", ""]
    for f in h["changed_or_relevant_files"]:
        lines.append(f"- `{f}`")

    return "\n".join(lines)


def main():
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()

    if not repo_root.exists():
        print(f"ERROR: repo_root '{repo_root}' does not exist.", file=sys.stderr)
        sys.exit(2)

    handoff = generate_handoff(repo_root)

    json_path = repo_root / HANDOFF_JSON_PATH
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(handoff, indent=2), encoding="utf-8")

    md_path = repo_root / HANDOFF_MD_PATH
    md_path.write_text(render_markdown(handoff), encoding="utf-8")

    print(f"=== REE Governance Handoff Generated ===")
    print(f"JSON : {json_path}")
    print(f"MD   : {md_path}")
    print(f"Status : {handoff['verification_status'].upper()}")
    print(f"Summary: {handoff['summary']}")
    print()
    print(f"NEXT ACTION: {handoff['next_action']}")
    if handoff["blocked_items"]:
        print()
        print(f"BLOCKED ({len(handoff['blocked_items'])} item(s)):")
        for b in handoff["blocked_items"]:
            print(f"  [{b['code']}] {b['message'][:90]}")


if __name__ == "__main__":
    main()
