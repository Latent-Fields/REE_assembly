#!/usr/bin/env python3
"""
REE_assembly governance verification gate.

Checks that governance cycle state is internally consistent before a cycle is marked complete.
Writes a deterministic JSON report and exits:
  0 = pass (no block-severity findings)
  1 = fail (one or more block-severity findings)
  2 = usage error / runtime misconfiguration

All checks are read-only. This script never modifies claims, queues, manifests, or any
governance file except its own output directory (evidence/verification/).
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPORT_RELATIVE_PATH = "evidence/verification/governance_verification_latest.json"

# Stale threshold (hours) for per-machine heartbeat freshness check
HEARTBEAT_STALE_HOURS = 4.0


def _coordinator_rows():
    """Live /shadow/status rows keyed by machine, or None when unavailable.

    Coordinator-primary telemetry (2026-09-01): the git materialization of
    runner_heartbeats/ and runner_status/ is being retired (files freeze in
    place), so machine liveness/freshness is judged from the coordinator when
    it answers, and only from the git files when it does not. Never raises;
    any failure (missing client module, missing config, unreachable hub,
    parse error) returns None so callers fall back to today's behavior.
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
        description=(
            "REE_assembly governance verification gate. "
            "Checks internal consistency of repo, runner, and review state. "
            "Exits 0=pass, 1=fail (block findings), 2=usage error."
        )
    )
    parser.add_argument(
        "--repo-root", default=".",
        help="Path to REE_assembly root (default: current directory)"
    )
    parser.add_argument(
        "--stale-hours", type=float, default=12.0,
        help="Hours after which central runner_status.json is considered stale (default: 12)"
    )
    parser.add_argument(
        "--output", default=None,
        help="Override output path for JSON report"
    )
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
    """Parse ISO 8601 timestamp; return UTC-aware datetime or None."""
    if not ts_str:
        return None
    ts_str = ts_str.strip()
    # Normalise trailing Z and +00:00
    ts_str = ts_str.rstrip("Z")
    ts_str = re.sub(r"\+00:00$", "", ts_str)
    for fmt in (
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M",
    ):
        try:
            return datetime.strptime(ts_str, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def now_utc():
    return datetime.now(timezone.utc)


def make_finding(severity, code, message, evidence_paths=None, suggested_next_action=None):
    return {
        "severity": severity,
        "code": code,
        "message": message,
        "evidence_paths": evidence_paths or [],
        "suggested_next_action": suggested_next_action or "",
    }


# ---------------------------------------------------------------------------
# Check A: pending_review.md freshness vs newest manifest
# ---------------------------------------------------------------------------
def check_pending_review_freshness(repo_root, findings):
    pr_path = repo_root / "evidence/experiments/pending_review.md"
    if not pr_path.exists():
        findings.append(make_finding(
            "warn", "PENDING_REVIEW_MISSING",
            "evidence/experiments/pending_review.md not found.",
            evidence_paths=[str(pr_path)],
            suggested_next_action="Run: python scripts/generate_pending_review.py"
        ))
        return

    pr_text = pr_path.read_text(encoding="utf-8")
    m = re.search(r"Generated:\s*`([^`]+)`", pr_text)
    if not m:
        findings.append(make_finding(
            "warn", "PENDING_REVIEW_TIMESTAMP_UNPARSEABLE",
            "Could not parse 'Generated: `...`' timestamp from pending_review.md.",
            evidence_paths=[str(pr_path)],
            suggested_next_action="Check pending_review.md format or re-run generate_pending_review.py."
        ))
        return

    pr_generated = parse_iso_timestamp(m.group(1))
    if pr_generated is None:
        findings.append(make_finding(
            "warn", "PENDING_REVIEW_TIMESTAMP_UNPARSEABLE",
            f"Timestamp '{m.group(1)}' in pending_review.md could not be parsed.",
            evidence_paths=[str(pr_path)],
        ))
        return

    experiments_dir = repo_root / "evidence/experiments"
    newest_mtime = None
    newest_path = None
    for manifest_path in experiments_dir.rglob("manifest.json"):
        try:
            mtime = datetime.fromtimestamp(manifest_path.stat().st_mtime, tz=timezone.utc)
            if newest_mtime is None or mtime > newest_mtime:
                newest_mtime = mtime
                newest_path = manifest_path
        except Exception:
            continue

    if newest_mtime and newest_mtime > pr_generated:
        lag_h = (newest_mtime - pr_generated).total_seconds() / 3600
        findings.append(make_finding(
            "block", "PENDING_REVIEW_STALE_AGAINST_MANIFESTS",
            (
                f"pending_review.md was generated at {pr_generated.isoformat()} but a newer "
                f"manifest exists (mtime {newest_mtime.isoformat()}, lag {lag_h:.1f}h). "
                "New experiment results may not be in the review list."
            ),
            evidence_paths=[str(pr_path), str(newest_path)],
            suggested_next_action="Run: python scripts/generate_pending_review.py; then re-run this verifier."
        ))


# ---------------------------------------------------------------------------
# Check B: roadmap pending count vs pending_review.md count
# ---------------------------------------------------------------------------
def check_roadmap_vs_pending_review(repo_root, findings):
    pr_path = repo_root / "evidence/experiments/pending_review.md"
    roadmap_path = repo_root / "docs/roadmap.md"

    if not pr_path.exists() or not roadmap_path.exists():
        return

    pr_text = pr_path.read_text(encoding="utf-8")
    m_pr = re.search(r"Pending:\s*\*\*(\d+)\*\*", pr_text)
    if not m_pr:
        findings.append(make_finding(
            "warn", "PENDING_REVIEW_COUNT_UNPARSEABLE",
            "Could not parse 'Pending: **N**' from pending_review.md.",
            evidence_paths=[str(pr_path)],
        ))
        return
    pr_count = int(m_pr.group(1))

    roadmap_text = roadmap_path.read_text(encoding="utf-8")
    # First Status Snapshot block
    snap_m = re.search(
        r"(## Status Snapshot[^\n]*\n.*?)(?=\n## Status Snapshot|\Z)",
        roadmap_text, re.DOTALL
    )
    roadmap_count = None
    if snap_m:
        block = snap_m.group(1)
        # Matches: "-> **10 items**" or "**10 items**" in bullet text
        m_rmap = re.search(r"->\s*\*\*(\d+)\*\*\s*item", block)
        if not m_rmap:
            # Fallback: bare "pending_review ... -> N" (header form)
            m_rmap = re.search(r"pending_review\s+\d+\s*->\s*(\d+)", block)
        if m_rmap:
            roadmap_count = int(m_rmap.group(1))

    if roadmap_count is None:
        findings.append(make_finding(
            "warn", "ROADMAP_PENDING_REVIEW_COUNT_UNPARSEABLE",
            "Could not parse pending_review count from most recent roadmap Status Snapshot.",
            evidence_paths=[str(roadmap_path)],
            suggested_next_action="Check roadmap.md snapshot format for '-> **N** items' pattern."
        ))
        return

    if roadmap_count != pr_count:
        findings.append(make_finding(
            "block", "ROADMAP_PENDING_REVIEW_MISMATCH",
            (
                f"Roadmap Status Snapshot says pending_review={roadmap_count}, but "
                f"pending_review.md says Pending={pr_count}. State is inconsistent."
            ),
            evidence_paths=[str(roadmap_path), str(pr_path)],
            suggested_next_action=(
                "Re-run: python scripts/generate_pending_review.py; update roadmap snapshot; "
                "or add a note that the roadmap snapshot is intentionally stale."
            )
        ))


# ---------------------------------------------------------------------------
# Check C: central runner_status.json stale or absent
# ---------------------------------------------------------------------------
def check_central_runner_status(repo_root, findings, stale_hours):
    central_path = repo_root / "evidence/experiments/runner_status.json"
    per_machine_dir = repo_root / "evidence/experiments/runner_status"

    # Coordinator-primary: when the live coordinator answers, the git
    # runner_status materialization is a retired/frozen mirror, so its
    # absence or age is expected and not evidence of a wedged merge.
    # Only judge freshness from the git files when the coordinator is
    # unavailable (rows None/empty -> fall through to today's behavior).
    if _coordinator_rows():
        return

    per_machine_files = []
    if per_machine_dir.exists():
        per_machine_files = [
            f for f in per_machine_dir.glob("*.json") if f.name != "README.md"
        ]

    if not central_path.exists():
        if per_machine_files:
            findings.append(make_finding(
                "warn", "CENTRAL_RUNNER_STATUS_ABSENT",
                (
                    f"evidence/experiments/runner_status.json is absent but "
                    f"{len(per_machine_files)} per-machine runner_status file(s) exist. "
                    "Downstream indexer may use stale or absent central runner data."
                ),
                evidence_paths=[str(central_path), str(per_machine_dir)],
                suggested_next_action=(
                    "Investigate whether the coordinator->central-index merge has wedged. "
                    "If Phase-2 coordinator is active, per-machine files are authoritative."
                )
            ))
        return

    try:
        central = json.loads(central_path.read_text(encoding="utf-8"))
        last_updated_str = central.get("last_updated")
        last_updated = parse_iso_timestamp(last_updated_str)
        if last_updated:
            age_h = (now_utc() - last_updated).total_seconds() / 3600
            if age_h > stale_hours:
                findings.append(make_finding(
                    "warn", "CENTRAL_RUNNER_STATUS_STALE",
                    (
                        f"evidence/experiments/runner_status.json last_updated "
                        f"{last_updated_str} is {age_h:.1f}h old (threshold: {stale_hours}h). "
                        "Per-machine runner_status files may carry more recent data."
                    ),
                    evidence_paths=[str(central_path)],
                    suggested_next_action=(
                        "Check whether coordinator->central-status merge has wedged. "
                        "If Phase-2 coordinator is active, per-machine files are authoritative."
                    )
                ))
    except Exception as exc:
        findings.append(make_finding(
            "warn", "CENTRAL_RUNNER_STATUS_PARSE_ERROR",
            f"Could not parse evidence/experiments/runner_status.json: {exc}",
            evidence_paths=[str(central_path)],
        ))


# ---------------------------------------------------------------------------
# Check D: heartbeat says running but per-machine runner_status says idle
# ---------------------------------------------------------------------------
def check_heartbeat_status_divergence(repo_root, findings):
    heartbeats_dir = repo_root / "evidence/experiments/runner_heartbeats"
    per_machine_dir = repo_root / "evidence/experiments/runner_status"

    # Coordinator-primary: prefer live /shadow/status rows for machine
    # liveness (state / current_exq / last_seen). The git heartbeat file is
    # still consulted per-machine for current_exq_started_utc, which the
    # coordinator rows do not carry. When the coordinator is unavailable
    # (records None) the git glob below runs exactly as before.
    coord_rows = _coordinator_rows()
    records = None
    if coord_rows:
        records = []
        for machine in sorted(coord_rows):
            row = coord_rows[machine]
            hb_git = {}
            hb_file = heartbeats_dir / (machine + ".json")
            if hb_file.exists():
                try:
                    hb_git = json.loads(hb_file.read_text(encoding="utf-8"))
                except Exception:
                    hb_git = {}
            records.append((machine, {
                "state": row.get("state", "") or "",
                "current_exq": row.get("current_exq"),
                "last_tick_utc": str(row.get("last_seen") or ""),
                "current_exq_started_utc":
                    hb_git.get("current_exq_started_utc", ""),
            }, hb_file))

    if records is None:
        if not heartbeats_dir.exists():
            return
        records = []
        for hb_file in sorted(heartbeats_dir.glob("*.json")):
            if hb_file.name == "README.md":
                continue
            try:
                hb = json.loads(hb_file.read_text(encoding="utf-8"))
            except Exception:
                continue
            records.append((hb_file.stem, hb, hb_file))

    for machine, hb, hb_file in records:
        hb_state = hb.get("state", "")
        hb_exq = hb.get("current_exq")
        hb_tick_str = hb.get("last_tick_utc", "")
        hb_tick = parse_iso_timestamp(hb_tick_str)

        # Skip stale heartbeats (machine may be offline)
        if hb_tick:
            age_h = (now_utc() - hb_tick).total_seconds() / 3600
            if age_h > HEARTBEAT_STALE_HOURS:
                continue

        status_path = per_machine_dir / hb_file.name
        if not status_path.exists():
            continue
        try:
            status = json.loads(status_path.read_text(encoding="utf-8"))
        except Exception:
            continue

        status_idle = status.get("idle", None)
        status_last_updated = parse_iso_timestamp(status.get("last_updated", ""))
        hb_run_started = parse_iso_timestamp(hb.get("current_exq_started_utc", ""))

        # Only flag if status file was written AFTER the current run started.
        # If the status predates the run start, it is a stale snapshot from a previous
        # runner startup and the heartbeat is the authoritative live signal.
        status_is_current = (
            status_last_updated is not None
            and hb_run_started is not None
            and status_last_updated >= hb_run_started
        )

        if hb_state == "running" and hb_exq and status_idle and status_is_current:
            findings.append(make_finding(
                "warn", "HEARTBEAT_STATUS_DIVERGENCE",
                (
                    f"Machine {machine}: heartbeat says state=running current_exq={hb_exq}, "
                    f"but runner_status says idle=True current=null. "
                    "Runner may have stopped mid-experiment."
                ),
                evidence_paths=[str(hb_file), str(status_path)],
                suggested_next_action=(
                    f"Check {machine} runner process. If stopped, decide whether "
                    f"{hb_exq} needs to be re-queued or has a manifest."
                )
            ))


# ---------------------------------------------------------------------------
# Check E: EXQ mentioned as drained in roadmap without manifest or disposition
# ---------------------------------------------------------------------------
def check_drained_exq_without_manifest(repo_root, findings):
    roadmap_path = repo_root / "docs/roadmap.md"
    if not roadmap_path.exists():
        return

    roadmap_text = roadmap_path.read_text(encoding="utf-8")
    # Most recent snapshot block only
    snap_m = re.search(
        r"(## Status Snapshot[^\n]*\n.*?)(?=\n## Status Snapshot|\Z)",
        roadmap_text, re.DOTALL
    )
    if not snap_m:
        return

    block = snap_m.group(1)
    # Conservative: only flag when text explicitly says "drained" AND "no ... manifest"
    drained_re = re.compile(
        r"(V3-EXQ-[\w]+|EXQ-[\w]+)\s+(?:drained|force_rerun)[^\n]*"
        r"(?:no [^\n]*manifest|manifest[^\n]*opaque|without[^\n]*manifest)",
        re.IGNORECASE
    )
    seen_exqs = set()
    for m in drained_re.finditer(block):
        exq_id = m.group(1)
        if exq_id in seen_exqs:
            continue
        seen_exqs.add(exq_id)
        context = m.group(0)[:120]
        experiments_dir = repo_root / "evidence/experiments"
        exq_slug = exq_id.lower().replace("-", "_")
        manifests = list(experiments_dir.rglob("manifest.json"))
        found = any(exq_slug in str(p).lower() for p in manifests)

        if not found:
            findings.append(make_finding(
                "block", "EXQ_DRAINED_WITHOUT_MANIFEST_OR_DISPOSITION",
                (
                    f"{exq_id} is mentioned as drained in the roadmap Status Snapshot "
                    f"but no manifest was found in evidence/experiments/. "
                    f"Roadmap context: '{context}'"
                ),
                evidence_paths=[str(roadmap_path)],
                suggested_next_action=(
                    f"Determine {exq_id}'s fate: check per-machine runner_status files "
                    "and coordinator panel. If manifest is on a remote machine, wait for "
                    "sync. If the run was pruned or never ran, add an explicit disposition "
                    "note in roadmap.md. Then re-queue if needed."
                )
            ))


# ---------------------------------------------------------------------------
# Check F: FAIL entries in pending_review without autopsy or diagnosis link
# ---------------------------------------------------------------------------
def check_failed_experiments_without_diagnosis(repo_root, findings):
    pr_path = repo_root / "evidence/experiments/pending_review.md"
    if not pr_path.exists():
        return

    pr_text = pr_path.read_text(encoding="utf-8")
    fail_m = re.search(
        r"## FAIL \(action required\)(.*?)(?=^## |\Z)",
        pr_text, re.DOTALL | re.MULTILINE
    )
    if not fail_m:
        return

    run_ids = re.findall(r"`(v3_exq_[^`]+)`", fail_m.group(1))
    if not run_ids:
        return

    planning_dir = repo_root / "evidence/planning"
    autopsy_files = (
        list(planning_dir.glob("failure_autopsy*.md"))
        + list(planning_dir.glob("failure_autopsy*.json"))
    )
    # Build a combined text of autopsy files for search (cap to avoid memory issues)
    autopsy_text = ""
    for f in autopsy_files[:30]:
        try:
            autopsy_text += f.read_text(encoding="utf-8", errors="ignore").lower()
        except Exception:
            continue

    for run_id in run_ids:
        exq_m = re.search(r"v3_exq_(\w+?)_", run_id)
        if not exq_m:
            continue
        exq_short = exq_m.group(1)

        has_autopsy = (
            exq_short.lower() in autopsy_text
            or any(exq_short.lower() in f.name.lower() for f in autopsy_files)
        )

        if not has_autopsy:
            findings.append(make_finding(
                "warn", "FAILED_EXPERIMENT_WITHOUT_DIAGNOSIS_LINK",
                (
                    f"FAIL experiment '{run_id}' is in pending_review.md FAIL section "
                    "but no failure_autopsy file was found for it in evidence/planning/."
                ),
                evidence_paths=[str(pr_path), str(planning_dir)],
                suggested_next_action=(
                    f"Run /failure-autopsy for this experiment, or add a "
                    "non_contributory rationale with explicit reason to its manifest, "
                    "before closing the governance cycle."
                )
            ))


# ---------------------------------------------------------------------------
# Check G: dirty working tree has heartbeat-adjacent changes in protected files
# ---------------------------------------------------------------------------
def check_heartbeat_scope_bleed(repo_root, findings):
    protected_patterns = [
        "docs/claims/claims.yaml",
        "evidence/planning/",
        "evidence/planning/substrate_queue",
        "evidence/planning/inter_governance_workset",
    ]
    telemetry_patterns = [
        "runner_heartbeats/",
        "runner_status/",
        "_runner_signals/",
        "runner_commands/",
    ]

    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, cwd=str(repo_root)
        )
        if result.returncode != 0:
            return
        dirty_lines = [l.strip() for l in result.stdout.splitlines() if l.strip()]
    except Exception:
        return

    for line in dirty_lines:
        parts = line.split(None, 1)
        if len(parts) < 2:
            continue
        dirty_path = parts[1].strip()
        is_telemetry = any(pat in dirty_path for pat in telemetry_patterns)
        is_protected = any(pat in dirty_path for pat in protected_patterns)
        if is_telemetry and is_protected:
            findings.append(make_finding(
                "warn", "HEARTBEAT_SCOPE_BLEED",
                (
                    f"File '{dirty_path}' is dirty and matches both a telemetry path "
                    "and a protected governance path. Heartbeat machinery may have "
                    "touched governance state."
                ),
                evidence_paths=[str(repo_root / dirty_path)],
                suggested_next_action=(
                    "Review: git diff -- " + dirty_path + ". "
                    "If runner wrote to it, revert the telemetry-driven change and "
                    "re-apply any governance edit manually."
                )
            ))


# ---------------------------------------------------------------------------
# Check I: substrate_queue node_class well-formed (work-graph debt vocabulary)
# ---------------------------------------------------------------------------
# docs/architecture/work_graph_debt_vocabulary.md -- the bracket is part of the
# token. An UNMARKED substrate_queue entry is read as complicated (buildable)
# (the queue is the execution backlog by construction), so a missing node_class
# is only an aggregate info signal, never a block. This check exists so a bad
# EXPLICIT value cannot slip in and so a "gated on X" phrase without a resolving
# token gets surfaced.
NODE_CLASS_TOKENS = frozenset({
    "complicated (buildable)",
    "complex (probe-gated)",
    "puzzle (known rules)",
    "mystery (known data)",
    "aleatoric (irreducible)",
})


def check_substrate_queue_node_class(repo_root, findings):
    sq_path = repo_root / "evidence" / "planning" / "substrate_queue.json"
    if not sq_path.exists():
        return
    try:
        data = json.loads(sq_path.read_text(encoding="utf-8"))
    except Exception:
        return
    queue = [it for it in (data.get("queue") or []) if isinstance(it, dict)]
    if not queue:
        return

    bad_value = []      # explicit node_class not in the token set
    gated_no_token = []  # "gated on" prose but no valid node_class
    missing = 0
    for entry in queue:
        sid = entry.get("sd_id") or "<no-sd_id>"
        nc = entry.get("node_class")
        has_valid = nc in NODE_CLASS_TOKENS
        if nc is None:
            missing += 1
        elif not has_valid:
            bad_value.append(f"{sid}={nc!r}")
        # "gated on X" language (in hint or free-text status) must resolve to a token
        hint = entry.get("implementation_hint") or ""
        status = entry.get("status") if isinstance(entry.get("status"), str) else ""
        blob = (hint + " " + status).lower()
        if ("gated on" in blob or "gated_on" in blob) and not has_valid:
            gated_no_token.append(sid)

    if bad_value:
        findings.append(make_finding(
            "warn", "SUBSTRATE_QUEUE_NODE_CLASS_INVALID",
            (
                f"{len(bad_value)} substrate_queue entr(y/ies) carry a node_class "
                "outside the work-graph debt vocabulary token set "
                "(docs/architecture/work_graph_debt_vocabulary.md): "
                + "; ".join(bad_value[:12])
            ),
            evidence_paths=[str(sq_path)],
            suggested_next_action=(
                "Set node_class to exactly one of: complicated (buildable), "
                "complex (probe-gated), puzzle (known rules), mystery (known data), "
                "aleatoric (irreducible). The bracket is part of the token."
            )
        ))
    if gated_no_token:
        findings.append(make_finding(
            "warn", "SUBSTRATE_QUEUE_GATED_ON_NO_TOKEN",
            (
                f"{len(gated_no_token)} substrate_queue entr(y/ies) use 'gated on' "
                "language but carry no resolving node_class token: "
                + ", ".join(gated_no_token[:12])
            ),
            evidence_paths=[str(sq_path)],
            suggested_next_action=(
                "'Gated on X' is well-formed only if X resolves to a node_class "
                "token. Classify the entry (usually complex (probe-gated) if the "
                "residual is a reducible unknown) or reword the note."
            )
        ))
    if missing:
        findings.append(make_finding(
            "info", "SUBSTRATE_QUEUE_NODE_CLASS_UNMARKED",
            (
                f"{missing}/{len(queue)} substrate_queue entries lack node_class; "
                "read as complicated (buildable) by default (the queue is the "
                "execution backlog). Governance Step 6a populates it going forward."
            ),
            evidence_paths=[str(sq_path)],
            suggested_next_action=(
                "No action required. node_class is backfilled lazily as a "
                "governance cycle next touches each entry."
            )
        ))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()

    if not repo_root.exists():
        print(f"ERROR: repo_root '{repo_root}' does not exist.", file=sys.stderr)
        sys.exit(2)

    generated_at = now_utc().isoformat()
    git_head = get_git_head(repo_root)

    findings = []
    check_pending_review_freshness(repo_root, findings)
    check_roadmap_vs_pending_review(repo_root, findings)
    check_central_runner_status(repo_root, findings, args.stale_hours)
    check_heartbeat_status_divergence(repo_root, findings)
    check_drained_exq_without_manifest(repo_root, findings)
    check_failed_experiments_without_diagnosis(repo_root, findings)
    check_heartbeat_scope_bleed(repo_root, findings)
    check_substrate_queue_node_class(repo_root, findings)

    block_count = sum(1 for f in findings if f["severity"] == "block")
    warn_count = sum(1 for f in findings if f["severity"] == "warn")
    info_count = sum(1 for f in findings if f["severity"] == "info")
    status = "pass" if block_count == 0 else "fail"

    report = {
        "generated_at_utc": generated_at,
        "repo_root": str(repo_root),
        "git_head": git_head,
        "status": status,
        "findings": findings,
        "summary": {
            "block_count": block_count,
            "warn_count": warn_count,
            "info_count": info_count,
        },
    }

    output_path = Path(args.output) if args.output else repo_root / REPORT_RELATIVE_PATH
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    # Terminal summary (ASCII only)
    status_label = "PASS" if status == "pass" else "FAIL"
    print(f"\n=== REE Governance Verification Gate ===")
    print(f"Status : {status_label}")
    print(f"Block  : {block_count}  Warn: {warn_count}  Info: {info_count}")
    print(f"Report : {output_path}")
    if git_head:
        print(f"HEAD   : {git_head[:12]}")
    print()

    for f in findings:
        prefix = {"block": "[BLOCK]", "warn": "[WARN]", "info": "[INFO]"}.get(
            f["severity"], "[?]"
        )
        print(f"{prefix} {f['code']}")
        print(f"       {f['message'][:120]}")
        if f.get("suggested_next_action"):
            print(f"       -> {f['suggested_next_action'][:100]}")
        print()

    sys.exit(0 if block_count == 0 else 1)


if __name__ == "__main__":
    main()
