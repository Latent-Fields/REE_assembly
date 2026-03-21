#!/usr/bin/env python3
"""
build_contributions.py — Rebuild contributors/contributions.json

Reads:
  - evidence/decisions/decision_log.v1.jsonl  → governance decision counts per actor
  - evidence/experiments/runner_status.json   → completed run metadata
  - evidence/experiments/**/manifest.json      → experiment run packs (for episode counts)
  - ../ree-v3/experiment_queue.json            → queue calibration + estimated_minutes
  - git log --shortstat across all repos       → coding attribution by lines changed

Writes:
  - contributors/contributions.json

Run from REE_assembly root:
    python3 contributors/build_contributions.py
"""

import json
import glob
import subprocess
import sys
import re
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent  # REE_assembly root
PARENT = ROOT.parent                           # REE_Working root

# ── Machine registry ──────────────────────────────────────────────────────────
# Add known machines here. TDP is average CPU load wattage (not TDP peak).
# For GPU machines, add gpu_watts for the GPU share.
MACHINE_REGISTRY = {
    "DLAPTOP-4.local": {
        "display_name": "Daniel's MacBook Air (M2)",
        "owner": "Daniel Golden",
        "hardware": "Apple M2 Air 8GB",
        "tdp_watts": 15,      # M2 Air under load ~10-20W average
        "gpu_watts": 0,
    },
    "cyberpower-pc": {
        "display_name": "CyberPower PC (i5-8600K + GTX 1050 Ti)",
        "owner": "Daniel Golden",
        "hardware": "i5-8600K, GTX 1050 Ti 4GB, 8GB RAM",
        "tdp_watts": 65,      # i5-8600K under load
        "gpu_watts": 75,      # GTX 1050 Ti under load
    },
    "Daniel-PC": {
        "display_name": "CyberPower PC (i5-8600K + RTX 2060 Super)",
        "owner": "Daniel Golden",
        "hardware": "i5-8600K OC 4.3GHz, RTX 2060 Super 8GB, 8GB DDR4",
        "tdp_watts": 65,      # i5-8600K under load
        "gpu_watts": 175,     # RTX 2060 Super under load
    },
}

# ── Cost model ─────────────────────────────────────────────────────────────────
ELECTRICITY_RATE_EUR = 0.27        # Irish residential (per kWh)
ELECTRICITY_CURRENCY = "EUR"
CLOUD_INSTANCE = "AWS t3.medium"
CLOUD_USD_PER_HOUR = 0.0416        # on-demand price as of 2026

# ── Calibration fallback (ms per episode × condition when no other timing) ────
MS_PER_EPISODE_CONDITION = 8000    # from ree-v3 queue calibration
SYNTHETIC_EPOCH_CUTOFF = "2026-02-27T00:00:00Z"  # runs before this are synthetic

# ── Repos to scan for git attribution ─────────────────────────────────────────
REPOS = [
    ROOT,                         # REE_assembly
    PARENT / "ree-v3",
    PARENT / "ree-v2",
    PARENT / "ree-v1-minimal",
    PARENT / "REE_convergence",
]


def is_genuine_run(run_id: str, completed_at: str) -> bool:
    """Return True if this is a genuine (non-synthetic) experiment run."""
    if "toyenv_internal_minimal" in run_id:
        return False
    if completed_at and completed_at < SYNTHETIC_EPOCH_CUTOFF:
        return False
    return True


def estimate_run_hours(item: dict) -> float:
    """Estimate wall-clock hours for a completed run."""
    # Best: actual_secs from status entry
    if "actual_secs" in item:
        return item["actual_secs"] / 3600

    # Good: estimated_minutes from queue entry
    if "estimated_minutes" in item:
        return item["estimated_minutes"] / 60

    # Fallback: episodes × ms calibration
    episodes = item.get("episodes_per_run", 0)
    conditions = item.get("conditions", 1)
    seeds = item.get("seeds", 1)
    if episodes:
        return episodes * conditions * seeds * MS_PER_EPISODE_CONDITION / 1000 / 3600

    # Last resort: assume 30 minutes per run
    return 0.5


def collect_compute() -> dict:
    """Collect compute data from runner_status.json and experiment manifests."""
    machines: dict = {}

    def add_run(hostname: str, hours: float, completed_at: str, queue_id: str):
        if hostname not in machines:
            reg = MACHINE_REGISTRY.get(hostname, {})
            machines[hostname] = {
                "display_name": reg.get("display_name", hostname),
                "owner": reg.get("owner", "Unknown"),
                "hardware": reg.get("hardware", "Unknown"),
                "tdp_watts": reg.get("tdp_watts", 15),
                "gpu_watts": reg.get("gpu_watts", 0),
                "total_cpu_hours": 0.0,
                "total_experiments": 0,
                "first_run": None,
                "last_run": None,
            }
        m = machines[hostname]
        m["total_cpu_hours"] += hours
        m["total_experiments"] += 1
        if m["first_run"] is None or completed_at < m["first_run"]:
            m["first_run"] = completed_at
        if m["last_run"] is None or completed_at > m["last_run"]:
            m["last_run"] = completed_at

    # Read runner_status.json completed entries
    status_file = ROOT / "evidence" / "experiments" / "runner_status.json"
    if status_file.exists():
        try:
            status = json.loads(status_file.read_text())
        except Exception as e:
            print(f"  Warning: could not read runner_status.json: {e}")
            status = {}
        for entry in status.get("completed", []):
            run_id = entry.get("queue_id", "") or entry.get("run_id", "")
            completed_at = entry.get("completed_at", "")
            if not is_genuine_run(run_id, completed_at):
                continue
            # runner_status completed[] entries don't carry hostname; attribute to
            # "DLAPTOP-4.local" (the primary machine) as default for historical runs
            hostname = entry.get("machine", "DLAPTOP-4.local")
            hours = estimate_run_hours(entry)
            add_run(hostname, hours, completed_at, run_id)

    # Also scan experiment queue files for claimed runs with machine info
    for ver in ("v3", "v2"):
        qf = PARENT / f"ree-{ver}" / "experiment_queue.json"
        if not qf.exists():
            continue
        try:
            q = json.loads(qf.read_text())
        except Exception:
            continue
        for item in q.get("items", []):
            if item.get("status") not in ("completed", "failed"):
                continue
            cb = item.get("claimed_by") or {}
            hostname = cb.get("machine", "DLAPTOP-4.local")
            completed_at = item.get("failed_at") or item.get("claimed_by", {}).get("claimed_at", "")
            queue_id = item.get("queue_id", "")
            if not completed_at:
                continue
            hours = estimate_run_hours(item)
            add_run(hostname, hours, completed_at, queue_id)

    # Compute costs per machine
    total_cpu_hours = 0.0
    total_experiments = 0
    for hostname, m in machines.items():
        total_watts = m["tdp_watts"] + m["gpu_watts"]
        kwh = m["total_cpu_hours"] * total_watts / 1000
        m["estimated_electricity_cost_eur"] = round(kwh * ELECTRICITY_RATE_EUR, 4)
        m["estimated_cloud_equivalent_cost_usd"] = round(m["total_cpu_hours"] * CLOUD_USD_PER_HOUR, 4)
        m["total_cpu_hours"] = round(m["total_cpu_hours"], 3)
        total_cpu_hours += m["total_cpu_hours"]
        total_experiments += m["total_experiments"]

    return {
        "cost_model": {
            "electricity_kwh_rate": ELECTRICITY_RATE_EUR,
            "electricity_rate_currency": ELECTRICITY_CURRENCY,
            "cloud_instance": CLOUD_INSTANCE,
            "cloud_usd_per_hour": CLOUD_USD_PER_HOUR,
            "notes": (
                "Irish residential electricity rate. "
                "Cloud equivalent = AWS t3.medium on-demand. "
                "Compute hours are wall-clock hours on the contributing machine. "
                "Electricity cost uses measured or estimated TDP under load."
            ),
        },
        "machines": machines,
        "totals": {
            "cpu_hours": round(total_cpu_hours, 3),
            "experiments": total_experiments,
        },
    }


def collect_decisions() -> dict:
    """Count governance decisions per actor from decision_log.v1.jsonl."""
    log_file = ROOT / "evidence" / "decisions" / "decision_log.v1.jsonl"
    counts: dict[str, int] = {}
    if not log_file.exists():
        return {"total_governance_decisions": 0, "contributors": {}, "source": str(log_file)}

    total = 0
    for line in log_file.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
            actor = entry.get("actor", "unknown")
            counts[actor] = counts.get(actor, 0) + 1
            total += 1
        except json.JSONDecodeError:
            continue

    # Map actor IDs to display names
    actor_display = {
        "dgolden": "Daniel Golden",
        "daniel.golden": "Daniel Golden",
        "daniel.delaharpe.golden@gmail.com": "Daniel Golden",
    }
    contributors = {}
    for actor, count in sorted(counts.items(), key=lambda x: -x[1]):
        display = actor_display.get(actor, actor)
        proportion = round(count / total, 4) if total > 0 else 0.0
        contributors[display] = {
            "actor_id": actor,
            "decisions": count,
            "proportion": proportion,
        }

    return {
        "total_governance_decisions": total,
        "contributors": contributors,
        "source": "evidence/decisions/decision_log.v1.jsonl",
    }


def collect_coding() -> dict:
    """Estimate coding attribution by lines changed, grouped by commit co-authorship.

    Strategy:
    - Commits with 'Co-Authored-By: Claude' → attributed to Claude
    - Commits with 'Co-Authored-By:.*codex' or branch merge from codex/ → Codex
    - All other commits → human (Daniel)

    Limitations: git shortstat counts every file (data JSONs, generated files, etc.)
    which inflates human counts for repos with large auto-generated artifacts.
    The commit-count metric is also reported as a more stable signal.
    """
    results = {
        "Claude (Anthropic)": {"lines_added": 0, "commits": 0},
        "Codex (OpenAI)": {"lines_added": 0, "commits": 0},
        "Daniel Golden": {"lines_added": 0, "commits": 0},
    }
    total_lines = 0
    total_commits = 0

    HASH_RE = re.compile(r"^[0-9a-f]{40}$")

    for repo_path in REPOS:
        if not (repo_path / ".git").is_dir():
            continue
        try:
            # Pass 1: get all hashes in order
            hashes_out = subprocess.run(
                ["git", "log", "--format=%H"],
                capture_output=True, text=True, cwd=str(repo_path), timeout=30
            )
            # Pass 2: get full commit bodies for classification (no stats)
            bodies_out = subprocess.run(
                ["git", "log", "--format=STARTCOMMIT%H%n%B"],
                capture_output=True, text=True, cwd=str(repo_path), timeout=30
            )
            # Pass 3: hash+shortstat (format=%H so we can associate stats with hashes)
            stats_out = subprocess.run(
                ["git", "log", "--shortstat", "--format=%H"],
                capture_output=True, text=True, cwd=str(repo_path), timeout=30
            )
        except (subprocess.TimeoutExpired, FileNotFoundError):
            continue

        # Build classification map from pass 2 (split on STARTCOMMIT marker)
        classification: dict[str, str] = {}
        for block in bodies_out.stdout.split("STARTCOMMIT"):
            if not block.strip():
                continue
            first_line_end = block.find("\n")
            if first_line_end < 0:
                continue
            h = block[:first_line_end].strip()
            body = block[first_line_end:]
            if not HASH_RE.match(h):
                continue
            if re.search(r"Co-Authored-By:.*Claude", body, re.IGNORECASE):
                classification[h] = "Claude (Anthropic)"
            elif (re.search(r"Co-Authored-By:.*codex", body, re.IGNORECASE)
                  or re.search(r"\bcodex/", body, re.IGNORECASE)):
                classification[h] = "Codex (OpenAI)"
            else:
                classification[h] = "Daniel Golden"

        # Build insertion map from pass 3: output is HASH\n\n STATS\n\nHASH\n...
        # We track current hash and assign stats to it when we see "files changed"
        insertions: dict[str, int] = {}
        current_hash = None
        for line in stats_out.stdout.splitlines():
            stripped = line.strip()
            if HASH_RE.match(stripped):
                current_hash = stripped
            elif current_hash and "insertion" in stripped:
                m = re.search(r"(\d+) insertion", stripped)
                insertions[current_hash] = int(m.group(1)) if m else 0

        # Combine: all classified hashes with their insertion counts
        for h, key in classification.items():
            ins = insertions.get(h, 0)
            results[key]["lines_added"] += ins
            results[key]["commits"] += 1
            total_lines += ins
            total_commits += 1

    # Build proportions
    contributors = {}
    for name, data in results.items():
        if total_lines == 0:
            prop_lines = 0.0
        else:
            prop_lines = round(data["lines_added"] / total_lines, 4)
        if total_commits == 0:
            prop_commits = 0.0
        else:
            prop_commits = round(data["commits"] / total_commits, 4)
        contributors[name] = {
            "lines_added": data["lines_added"],
            "commits": data["commits"],
            "proportion_by_lines": prop_lines,
            "proportion_by_commits": prop_commits,
            "basis": "git_history_co_authorship",
        }

    return {
        "baseline_method": "git_co_authorship",
        "baseline_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "total_lines_analyzed": total_lines,
        "total_commits_analyzed": total_commits,
        "contributors": contributors,
        "notes": (
            "Proportions are based on git commit co-authorship markers. "
            "'proportion_by_lines' is biased toward repos with large auto-generated "
            "data files (e.g. ree-v2 synthetic experiment JSONs). "
            "'proportion_by_commits' is a more stable signal for intellectual contribution. "
            "Codex involvement was brief (early literature adjudication phase)."
        ),
    }


CODING_DECLARED_TEMPLATE = {
    "_note": (
        "git_analysis cannot detect ChatGPT/Codex contributions without co-authorship markers. "
        "Fill in 'declared_estimates' with your honest assessment and it will be preserved "
        "across governance rebuilds. Use 'basis': 'declared' for human estimates."
    ),
    "declared_estimates": {
        "Claude (Anthropic)": {
            "proportion": None,
            "basis": "declared",
            "note": "Set this to your estimate, e.g. 0.37"
        },
        "ChatGPT / Codex (OpenAI)": {
            "proportion": None,
            "basis": "declared",
            "note": "Set this to your estimate for ChatGPT sessions without co-authorship markers"
        },
        "Daniel Golden (human)": {
            "proportion": None,
            "basis": "declared",
            "note": "Direct human authorship only (architecture decisions, direct edits, prompts that shaped direction)"
        },
    },
}


def main():
    print("Building contributors/contributions.json ...")

    out_file = ROOT / "contributors" / "contributions.json"

    # Preserve existing human-edited sections — do not overwrite
    existing_declared = {}
    existing_intellectual_direction = None
    if out_file.exists():
        try:
            existing = json.loads(out_file.read_text())
            existing_declared = existing.get("coding", {}).get("declared_estimates", {})
            existing_intellectual_direction = existing.get("intellectual_direction")
        except Exception:
            pass

    print("  Collecting compute data ...")
    compute = collect_compute()

    print("  Collecting governance decision data ...")
    decisions = collect_decisions()

    print("  Analysing git coding attribution ...")
    coding = collect_coding()

    # Inject declared estimates section, preserving any user-set values
    declared = CODING_DECLARED_TEMPLATE["declared_estimates"].copy()
    for name, data in existing_declared.items():
        if name in declared:
            declared[name] = data  # preserve user input
        else:
            declared[name] = data  # keep unknown entries too
    coding["_note"] = CODING_DECLARED_TEMPLATE["_note"]
    coding["declared_estimates"] = declared

    output = {
        "schema_version": "contributions/v1",
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "compute": compute,
        "decisions": decisions,
        "coding": coding,
    }
    if existing_intellectual_direction is not None:
        output["intellectual_direction"] = existing_intellectual_direction

    out_file.write_text(json.dumps(output, indent=2) + "\n")
    print(f"  Written: {out_file}")

    # Print summary
    totals = compute["totals"]
    print(f"\n  Compute: {totals['cpu_hours']:.1f} CPU-hours across {totals['experiments']} experiments")
    print(f"  Decisions: {decisions['total_governance_decisions']} total")
    cc = coding["contributors"]
    for name, d in cc.items():
        pct_c = d["proportion_by_commits"] * 100
        pct_l = d["proportion_by_lines"] * 100
        print(f"  Coding ({name}): {d['commits']} commits ({pct_c:.0f}%), {d['lines_added']} lines ({pct_l:.0f}%)")


if __name__ == "__main__":
    main()
