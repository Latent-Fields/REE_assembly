#!/usr/bin/env python3
"""
Generate pending_review.md -- lists experiment runs not yet reviewed in a session.

Usage (from REE_assembly root):
    python scripts/generate_pending_review.py

After reviewing, add newly-reviewed run IDs to evidence/experiments/review_tracker.json
and re-run this script to confirm the list clears.

Run as step 3 of the governance pipeline:
    python scripts/sync_v3_results.py
    python scripts/build_experiment_indexes.py
    python scripts/generate_pending_review.py

SECTIONS GENERATED:
  1. FAIL (action required)     -- indexed result files with result != PASS, not yet reviewed
  2. PASS (verify & close)      -- indexed result files with result == PASS, not yet reviewed
  3. Needs discussion           -- runner_status completed entries not covered above:
       a. ERROR / UNKNOWN results (no result file, so not indexed, never in sections 1/2)
       b. Onboarding smoke runs (any result) -- contain hardware/throughput data needed
          for experimental design decisions, regardless of PASS/FAIL status
     Smoke runs are identified by queue_id containing "onboard" or "smoke" (case-insensitive)
     or script path containing "onboard_smoke".
"""
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = ROOT / "evidence" / "experiments"
CLAIM_EVIDENCE = EVIDENCE_DIR / "claim_evidence.v1.json"
REVIEW_TRACKER = EVIDENCE_DIR / "review_tracker.json"
RUNNER_STATUS = EVIDENCE_DIR / "runner_status.json"          # legacy monolithic
RUNNER_STATUS_DIR = EVIDENCE_DIR / "runner_status"           # per-machine split
OUTPUT = EVIDENCE_DIR / "pending_review.md"


def load_tracker() -> tuple[set, set, str]:
    """Return (reviewed_run_ids, discussed_dirs, last_review_utc)."""
    if not REVIEW_TRACKER.exists():
        print("[warn] review_tracker.json not found -- all runs treated as pending", file=sys.stderr)
        return set(), set(), "unknown"
    with open(REVIEW_TRACKER) as f:
        tracker = json.load(f)
    reviewed = set(tracker.get("reviewed_run_ids", []))
    discussed = set(tracker.get("discussed_experiment_dirs", []))
    last_review = tracker.get("last_review_utc", "unknown")
    return reviewed, discussed, last_review


def load_pending_entries(reviewed: set) -> list[dict]:
    """Load PASS/FAIL entries from claim_evidence not yet in reviewed_run_ids."""
    if not CLAIM_EVIDENCE.exists():
        print("[error] claim_evidence.v1.json not found -- run build_experiment_indexes.py first",
              file=sys.stderr)
        sys.exit(1)
    with open(CLAIM_EVIDENCE) as f:
        data = json.load(f)
    entries = [
        e for e in data.get("entries", [])
        if e.get("source_type") == "experimental"
        and e.get("run_id") not in reviewed
    ]
    by_run: dict[str, dict] = {}
    for e in entries:
        run_id = e["run_id"]
        if run_id not in by_run:
            by_run[run_id] = {
                "run_id": run_id,
                "timestamp_utc": e.get("timestamp_utc", ""),
                "status": e.get("status", "?"),
                "claims": [],
                "failure_signatures": [],
            }
        by_run[run_id]["claims"].append(e.get("claim_id", "?"))
        by_run[run_id]["failure_signatures"].extend(e.get("failure_signatures", []))
    return sorted(by_run.values(), key=lambda r: r["timestamp_utc"])


def _is_smoke_run(queue_id: str, script: str) -> bool:
    """Return True if this entry is an onboarding smoke run."""
    combined = (queue_id + " " + script).lower()
    return "onboard" in combined or "smoke" in combined


def _derive_dir_name(output_file: str, queue_id: str) -> str:
    """Derive the experiment directory name from output_file path, same logic as explorer.html."""
    if not output_file:
        return queue_id
    path = output_file.replace("\\", "/")
    parts = path.split("experiments/")
    if len(parts) > 1:
        segment = parts[-1].split("/")[0]
        if segment.endswith(".json"):
            segment = re.sub(r"_\d{8}T\d{6}Z?\.json$", "", segment)
        if segment:
            return segment
    # bare filename
    basename = path.split("/")[-1]
    if basename.endswith(".json"):
        basename = re.sub(r"_\d{8}T\d{6}Z?\.json$", "", basename)
    return basename or queue_id


def load_runner_status_undiscussed(reviewed: set, discussed: set,
                                   indexed_run_ids: set) -> list[dict]:
    """Load runner_status completed entries that need discussion but are not in sections 1/2.

    Includes:
    - ERROR / UNKNOWN entries not already in discussed_dirs
    - Onboarding smoke runs (any result) not already in discussed_dirs or reviewed_run_ids
    - FAIL / PASS entries whose result file exists on disk but is NOT yet in the index
      (completed after the last build_experiment_indexes.py run — stale index gap)

    Excludes:
    - Entries whose derived dir_name OR queue_id is in discussed_dirs
    - Entries whose run_id is in reviewed_run_ids
    - Entries whose run_id IS in indexed_run_ids (already covered by sections 1/2)
    """
    # Read completed entries from per-machine files (preferred) or legacy monolithic
    all_completed: list[dict] = []
    if RUNNER_STATUS_DIR.is_dir():
        for f in sorted(RUNNER_STATUS_DIR.glob("*.json")):
            try:
                data = json.loads(f.read_text())
                all_completed.extend(data.get("completed", []))
            except Exception:
                pass
    elif RUNNER_STATUS.exists():
        try:
            with open(RUNNER_STATUS) as f:
                rs = json.load(f)
            all_completed = rs.get("completed", [])
        except Exception:
            pass

    if not all_completed:
        return []

    pending = []
    seen_queue_ids: set[str] = set()

    for entry in all_completed:
        queue_id = entry.get("queue_id", "")
        result = entry.get("result", "")
        output_file = entry.get("output_file", "") or ""
        script = entry.get("script", "") or ""
        claimed_at = (entry.get("claimed_by") or {}).get("claimed_at", "")

        if queue_id in seen_queue_ids:
            continue
        seen_queue_ids.add(queue_id)

        dir_name = _derive_dir_name(output_file, queue_id)
        is_smoke = _is_smoke_run(queue_id, script)

        # Check if already discussed
        if dir_name in discussed or queue_id in discussed:
            continue

        # Check if already covered by sections 1/2 via indexed run_id
        # (output_file can give us the run_id if we derive it)
        run_id_from_file = ""
        if output_file:
            # run_id is typically the stem without .json
            basename = output_file.replace("\\", "/").split("/")[-1]
            if basename.endswith(".json"):
                run_id_from_file = basename[:-5]  # strip .json
        # Normalise run_id for comparison: output_file stems omit the _v2/_v3 suffix
        # that indexed run_ids carry. Try both with and without common suffixes.
        def _in_reviewed_or_indexed(stem: str) -> bool:
            if not stem:
                return False
            for candidate in [stem, stem + "_v3", stem + "_v2"]:
                if candidate in reviewed or candidate in indexed_run_ids:
                    return True
            return False

        if _in_reviewed_or_indexed(run_id_from_file):
            # Already reviewed, OR it's in claim_evidence and will appear in sections 1/2
            continue

        # Detect stale-index gap: result file exists on disk but not yet indexed.
        # This catches FAIL/PASS experiments that completed after the last index build.
        # We only flag stale if the file exists AND none of its run_id variants are indexed.
        result_file_path = None
        if output_file:
            p = Path(output_file)
            result_file_path = p if p.is_absolute() else ROOT / output_file
        # Only flag stale if the result file is inside EVIDENCE_DIR (V3 results).
        # V2 experiment files live in ree-v2/ — their run_ids are transformed on sync
        # and don't match the basename, so stale detection would false-fire for all V2 runs.
        result_file_in_evidence = (
            result_file_path is not None
            and result_file_path.exists()
            and result_file_path.is_relative_to(EVIDENCE_DIR)
        )
        stale_index = (
            result_file_in_evidence
            and bool(run_id_from_file)
            and not _in_reviewed_or_indexed(run_id_from_file)
        )

        # Include if: ERROR/UNKNOWN, smoke run, or stale-index gap (not yet indexed)
        if result in ("ERROR", "UNKNOWN") or is_smoke or stale_index:
            pending.append({
                "queue_id": queue_id,
                "result": result,
                "script": script,
                "dir_name": dir_name,
                "claimed_at": claimed_at,
                "is_smoke": is_smoke,
                "stale_index": bool(stale_index),
            })

    # Sort by claimed_at (chronological)
    return sorted(pending, key=lambda r: r["claimed_at"])


def load_indexed_run_ids() -> set:
    """Return the set of run_ids present in claim_evidence (indexed experiments)."""
    if not CLAIM_EVIDENCE.exists():
        return set()
    with open(CLAIM_EVIDENCE) as f:
        data = json.load(f)
    return {e["run_id"] for e in data.get("entries", []) if "run_id" in e}


def write_pending_review(runs: list[dict], runner_undiscussed: list[dict],
                         last_review_utc: str) -> None:
    passes = [r for r in runs if r["status"] == "PASS"]
    fails  = [r for r in runs if r["status"] != "PASS"]

    total_pending = len(runs) + len(runner_undiscussed)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "# Pending Experiment Review",
        "",
        f"Generated: `{now}`  ",
        f"Last review: `{last_review_utc}`  ",
        f"Pending: **{total_pending}** item(s)"
        f" -- {len(passes)} PASS, {len(fails)} FAIL,"
        f" {len(runner_undiscussed)} runner-only (ERROR/UNKNOWN/smoke)",
        "",
    ]

    if total_pending == 0:
        lines += ["All experiments reviewed. Nothing pending.", ""]
    else:
        if fails:
            lines += ["## FAIL (action required)", ""]
            lines += ["| Run ID | Timestamp | Claims | Failure signatures |",
                      "|--------|-----------|--------|--------------------|"]
            for r in fails:
                claims = ", ".join(sorted(set(r["claims"])))
                sigs = ", ".join(sorted(set(r["failure_signatures"])))[:80] or "—"
                ts = r["timestamp_utc"][:16] if r["timestamp_utc"] else "?"
                lines.append(f"| `{r['run_id']}` | {ts} | {claims} | {sigs} |")
            lines.append("")

        if passes:
            lines += ["## PASS (verify & close)", ""]
            lines += ["| Run ID | Timestamp | Claims |",
                      "|--------|-----------|--------|"]
            for r in passes:
                claims = ", ".join(sorted(set(r["claims"])))
                ts = r["timestamp_utc"][:16] if r["timestamp_utc"] else "?"
                lines.append(f"| `{r['run_id']}` | {ts} | {claims} |")
            lines.append("")

        if runner_undiscussed:
            lines += ["## Needs discussion (ERROR / UNKNOWN / smoke)", ""]
            lines += [
                "These entries completed in the runner but have no indexed result file "
                "(ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and "
                "then added to `discussed_experiment_dirs` in review_tracker.json.",
                "",
                "| Queue ID | Result | Script | Notes |",
                "|----------|--------|--------|-------|",
            ]
            for r in runner_undiscussed:
                script_short = r["script"].split("/")[-1] if r["script"] else "?"
                if r["is_smoke"]:
                    note = "smoke run"
                elif r.get("stale_index"):
                    note = f"{r['result']} (index stale — run build_experiment_indexes.py)"
                else:
                    note = r["result"]
                lines.append(
                    f"| `{r['queue_id']}` | {r['result']} | `{script_short}` | {note} |"
                )
            lines.append("")

    lines += [
        "---",
        "",
        "## How to mark runs as reviewed",
        "",
        "- PASS/FAIL runs: add run IDs to `reviewed_run_ids` in review_tracker.json",
        "- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json",
        "- Update `last_review_utc`, then re-run this script to confirm the list clears.",
        "",
        "```bash",
        "python scripts/generate_pending_review.py",
        "```",
    ]

    OUTPUT.write_text("\n".join(lines) + "\n")
    print(
        f"Written {OUTPUT.relative_to(ROOT)}"
        f" -- {len(runs)} indexed pending, {len(runner_undiscussed)} runner-only pending"
    )


def main():
    reviewed, discussed, last_review_utc = load_tracker()
    indexed_run_ids = load_indexed_run_ids()
    runs = load_pending_entries(reviewed)
    runner_undiscussed = load_runner_status_undiscussed(reviewed, discussed, indexed_run_ids)
    write_pending_review(runs, runner_undiscussed, last_review_utc)


if __name__ == "__main__":
    main()
