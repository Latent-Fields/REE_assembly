#!/usr/bin/env python3
"""
sync_v3_results.py -- convert V3 flat JSON result files into run-pack format.

V3 experiment scripts write a single flat JSON file per run:
    evidence/experiments/{experiment_type}/{experiment_type}_{timestamp}.json

build_experiment_indexes.py expects the run-pack format:
    evidence/experiments/{experiment_type}/runs/{run_id}/manifest.json
    evidence/experiments/{experiment_type}/runs/{run_id}/metrics.json

This script scans for flat V3 JSON files (run_id ending in _v3) and creates
the corresponding run-pack directories so the indexer picks them up.

Already-converted runs are skipped (idempotent).

Usage (from REE_assembly root):
    python evidence/experiments/scripts/sync_v3_results.py
"""

import json
import sys
from pathlib import Path
from datetime import timezone, datetime

ROOT = Path(__file__).resolve().parents[4]  # REE_Working root
EVIDENCE_DIR = Path(__file__).resolve().parents[1]  # REE_assembly/evidence/experiments

# Files to skip -- these live in evidence/experiments/ but are not run result files
SKIP_NAMES = {
    "runner_status.json",
    "review_tracker.json",
    "claim_evidence.v1.json",
    "pending_review.md",
}


def _is_flat_v3(data: dict) -> bool:
    """Return True if this JSON looks like a V3 flat result file."""
    run_id = str(data.get("run_id", ""))
    epoch = str(data.get("architecture_epoch", ""))
    return run_id.endswith("_v3") and epoch == "ree_hybrid_guardrails_v1"


def _parse_timestamp(ts: str | None) -> str:
    """Normalise a compact timestamp (20260320T193340Z) to ISO-8601."""
    if not ts:
        return ""
    ts = ts.strip()
    # Already ISO-8601
    if "T" in ts and "-" in ts:
        return ts
    # Compact: 20260320T193340Z
    try:
        dt = datetime.strptime(ts, "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return ts


def convert_flat_to_runpack(flat_path: Path) -> str:
    """
    Convert a flat V3 JSON file to a run-pack directory.
    Returns the run_id if conversion happened, '' if skipped.
    """
    try:
        data = json.loads(flat_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"  [skip] {flat_path.name}: read error -- {exc}", flush=True)
        return ""

    if not _is_flat_v3(data):
        return ""

    run_id = str(data["run_id"])

    # Prefer the experiment_type field; fall back to parent dir name.
    # If the file lives directly in evidence/experiments/ (parent IS the base dir),
    # derive experiment_type from the run_id stem instead.
    parent_name = flat_path.parent.name
    if parent_name == EVIDENCE_DIR.name:
        # File is at top level -- derive experiment_type from run_id
        # run_id format: {experiment_type}_{timestamp}_v3  OR
        #                {timestamp}_{experiment_type}_v3
        # Use the data field if present; otherwise strip trailing timestamp+_v3 suffix
        raw = str(data.get("experiment_type", run_id))
        # strip trailing _v3 and timestamp component
        import re as _re
        experiment_type = _re.sub(r'_\d{8}T\d{6}Z_v3$', '', raw)
        experiment_type = _re.sub(r'_v3$', '', experiment_type)
        # create a subdirectory for this experiment under EVIDENCE_DIR
        exp_dir = EVIDENCE_DIR / experiment_type
        exp_dir.mkdir(parents=True, exist_ok=True)
    else:
        experiment_type = str(data.get("experiment_type", parent_name))
        exp_dir = flat_path.parent

    # Destination: exp_dir/runs/{run_id}/
    run_dir = exp_dir / "runs" / run_id
    if (run_dir / "manifest.json").exists():
        return ""  # already converted

    run_dir.mkdir(parents=True, exist_ok=True)

    # Build manifest.json
    ts_compact = str(data.get("run_timestamp") or "")
    ts_iso = _parse_timestamp(ts_compact)

    # Gather claim_ids -- flat JSON may have claim_ids (list) or claim (single string)
    claim_ids = data.get("claim_ids") or []
    if not claim_ids and data.get("claim"):
        claim_ids = [data["claim"]]

    # Support both "status" (runner-written manifests) and "overall_outcome" (flat JSON scripts)
    raw_status = data.get("status") or data.get("overall_outcome", "UNKNOWN")
    raw_upper = str(raw_status).upper()
    if raw_upper in ("PASS", "FAIL", "UNKNOWN"):
        status = raw_upper
    elif raw_upper.startswith("FAIL"):
        status = "FAIL"
    elif raw_upper.startswith("PASS"):
        status = "PASS"
    else:
        # PARTIAL_*, INCONCLUSIVE, etc. -- preserve as-is for human review
        status = raw_upper
    evidence_direction = str(data.get("evidence_direction", "unknown"))
    experiment_purpose = str(data.get("experiment_purpose", "evidence"))

    manifest = {
        "schema_version": "experiment_pack/v1",
        "architecture_epoch": data.get("architecture_epoch", "ree_hybrid_guardrails_v1"),
        "experiment_type": experiment_type,
        "run_id": run_id,
        "status": status,
        "timestamp_utc": ts_iso,
        "source_repo": {"name": "ree-v3", "commit": "", "branch": "main"},
        "runner": {"name": "ree-v3-harness", "version": "3.0.0"},
        "artifacts": {"metrics_path": "metrics.json", "summary_path": "summary.md"},
        "stop_criteria_version": "stop_criteria/v1",
        "claim_ids_tested": claim_ids,
        "evidence_class": "simulation",
        "evidence_direction": evidence_direction,
        "experiment_purpose": experiment_purpose,
        "producer_capabilities": {
            "sd005_split_latent": True,
            "sd004_action_objects": True,
            "sd006_multirate_clock": True,
        },
        "environment": {
            "env_id": "ree.causal_grid_world_v3",
            "env_version": "3.0.0",
            "dynamics_hash": "unknown",
            "reward_hash": "unknown",
            "observation_hash": "unknown",
            "config_hash": "unknown",
            "tier": "causal_grid_world_v3",
        },
        "failure_signatures": [],
    }

    # Build metrics.json
    raw_metrics = data.get("metrics", {})
    metrics_doc = {
        "schema_version": "metrics/v1",
        "values": raw_metrics,
    }

    # Build summary.md
    summary = data.get("summary_markdown", "")
    if not summary:
        n_pass = sum(1 for v in (data.get("criteria") or {}).values() if v)
        n_total = len(data.get("criteria") or {})
        summary = f"# {experiment_type}\n\nStatus: **{status}**"
        if n_total:
            summary += f"  ({n_pass}/{n_total} criteria)"
        summary += "\n"

    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (run_dir / "metrics.json").write_text(json.dumps(metrics_doc, indent=2) + "\n", encoding="utf-8")
    (run_dir / "summary.md").write_text(summary, encoding="utf-8")

    return run_id


def main():
    converted = []
    skipped_norun = 0

    # Scan flat JSON files -- both at top level and one dir deep
    # Top-level: evidence/experiments/*.json
    # Sub-level:  evidence/experiments/{exp_type}/*.json
    all_json = sorted(set(EVIDENCE_DIR.glob("*.json")) | set(EVIDENCE_DIR.glob("*/*.json")))
    for json_path in all_json:
        if json_path.name in SKIP_NAMES:
            continue
        # Skip files inside runs/ subdirectories (already converted)
        if "runs" in json_path.parts:
            continue
        run_id = convert_flat_to_runpack(json_path)
        if run_id:
            print(f"  converted: {run_id}", flush=True)
            converted.append(run_id)
        else:
            skipped_norun += 1

    print(f"\nsync_v3_results: {len(converted)} new run-pack(s) created, "
          f"{skipped_norun} file(s) skipped (already converted or non-run).",
          flush=True)


if __name__ == "__main__":
    main()
