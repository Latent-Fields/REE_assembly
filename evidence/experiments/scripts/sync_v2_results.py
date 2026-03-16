#!/usr/bin/env python3
"""Sync V2 experiment results from ree-v2 into REE_assembly run pack format.

Reads flat JSON results from ree-v2/evidence/experiments/*/*.json
and creates manifest.json + metrics.json + summary.md run packs in
REE_assembly/evidence/experiments/<claim_probe_*>/runs/<run_id>/.

Only the most recent JSON per experiment directory is ingested (earlier runs
were pre-E2-training-fix re-runs and should be treated as superseded).

Idempotent: skips run packs whose run_id already exists.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
EVIDENCE_EXPERIMENTS_DIR = SCRIPT_DIR.parent         # REE_assembly/evidence/experiments/
REPO_ROOT = EVIDENCE_EXPERIMENTS_DIR.parent.parent   # REE_assembly/
V2_EVIDENCE_DIR = REPO_ROOT.parent / "ree-v2" / "evidence" / "experiments"


def _claim_to_experiment_type(claim_id: str) -> str:
    """MECH-071 → claim_probe_mech_071, ARC-007 → claim_probe_arc_007, etc."""
    normalized = claim_id.lower().replace("-", "_")
    return f"claim_probe_{normalized}"


def _run_id_from(run_timestamp: str, exp_name: str) -> str:
    # Compact ISO timestamp: 20260315T183757_causal_attribution_calibration_v2
    ts = run_timestamp[:19].replace(":", "").replace("-", "").replace("T", "T")
    return f"{ts}_{exp_name}_v2"


def _load_latest(exp_dir: Path) -> dict | None:
    json_files = sorted(exp_dir.glob("*.json"))
    if not json_files:
        return None
    latest: dict | None = None
    latest_ts = ""
    for jf in json_files:
        try:
            d = json.loads(jf.read_text(encoding="utf-8"))
        except Exception:
            continue
        ts = str(d.get("run_timestamp", ""))
        if ts > latest_ts:
            latest_ts = ts
            latest = d
    return latest


def _write_run_pack(run_dir: Path, data: dict, exp_name: str) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)

    claim_id = data.get("claim", "unknown")
    verdict = str(data.get("verdict", "UNKNOWN")).upper()
    run_timestamp = data.get("run_timestamp", "")
    aggregate = data.get("aggregate", {})
    config = data.get("config", {})
    experiment_type = _claim_to_experiment_type(claim_id)
    evidence_direction = "supports" if verdict == "PASS" else "weakens"

    # manifest.json
    manifest = {
        "schema_version": "experiment_pack/v1",
        "experiment_type": experiment_type,
        "run_id": run_dir.name,
        "status": verdict,
        "timestamp_utc": run_timestamp,
        "architecture_epoch": "ree_hybrid_guardrails_v1",
        "source_repo": {
            "name": "ree-v2",
            "commit": "",
            "branch": "main"
        },
        "runner": {
            "name": "ree-v2-causal-gridworld-runner",
            "version": "v2"
        },
        "scenario": {
            "name": exp_name,
            "condition": "multi_seed_aggregate",
            "substrate": data.get("substrate", "ree-v2"),
            "evb_id": data.get("evb_id", "")
        },
        "stop_criteria_version": "stop_criteria/v1",
        "claim_ids_tested": [claim_id],
        "evidence_class": "simulation",
        "evidence_direction": evidence_direction,
        "failure_signatures": ([] if verdict == "PASS"
                               else [f"v2_verdict_fail:{exp_name}"]),
        "artifacts": {
            "metrics_path": "metrics.json",
            "summary_path": "summary.md"
        }
    }
    (run_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )

    # metrics.json — flatten aggregate scalars; add fatal_error_count=0
    metrics_values: dict[str, float] = {}
    for k, v in aggregate.items():
        if isinstance(v, (int, float)):
            metrics_values[k] = float(v)
    metrics_values.setdefault("fatal_error_count", 0.0)

    metrics = {
        "schema_version": "experiment_pack_metrics/v1",
        "values": metrics_values
    }
    (run_dir / "metrics.json").write_text(
        json.dumps(metrics, indent=2), encoding="utf-8"
    )

    # summary.md
    lines = [
        f"# {exp_name}",
        "",
        f"**Claim:** {claim_id}  ",
        f"**Verdict:** {verdict}  ",
        f"**Run timestamp:** {run_timestamp}  ",
        f"**Substrate:** {data.get('substrate', 'ree-v2')}  ",
        "",
        "## Aggregate Results",
        "",
    ]
    for k, v in aggregate.items():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "## Config", ""]
    for k, v in config.items():
        lines.append(f"- `{k}`: {v}")
    (run_dir / "summary.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if not V2_EVIDENCE_DIR.exists():
        print(f"ERROR: ree-v2 evidence dir not found: {V2_EVIDENCE_DIR}", file=sys.stderr)
        sys.exit(1)

    created = 0
    skipped = 0
    errors = 0

    for exp_dir in sorted(V2_EVIDENCE_DIR.iterdir()):
        if not exp_dir.is_dir():
            continue

        data = _load_latest(exp_dir)
        if data is None:
            print(f"SKIP (no valid JSON): {exp_dir.name}")
            continue

        claim_id = data.get("claim", "unknown")
        if not claim_id or claim_id == "?":
            print(f"SKIP (no claim ID): {exp_dir.name}")
            continue

        exp_name = exp_dir.name
        run_timestamp = data.get("run_timestamp", "")
        experiment_type = _claim_to_experiment_type(claim_id)
        run_id = _run_id_from(run_timestamp, exp_name)
        run_dir = EVIDENCE_EXPERIMENTS_DIR / experiment_type / "runs" / run_id

        if (run_dir / "manifest.json").exists():
            print(f"SKIP (exists): {experiment_type}/runs/{run_id}")
            skipped += 1
            continue

        try:
            _write_run_pack(run_dir, data, exp_name)
            verdict = str(data.get("verdict", "?")).upper()
            print(f"CREATE [{verdict}]: {experiment_type}/runs/{run_id}")
            created += 1
        except Exception as exc:
            print(f"ERROR: {exp_dir.name}: {exc}", file=sys.stderr)
            errors += 1

    print(f"\nDone: {created} created, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
