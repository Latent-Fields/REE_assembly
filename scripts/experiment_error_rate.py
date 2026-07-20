#!/usr/bin/env python3
"""Live ERROR-rate signal for the V3 experiment corpus (coordinator-DB authoritative).

WHY THIS EXISTS
---------------
Two older paths for "how often do experiments crash?" are both broken, and each
fails SILENTLY in a way that produces a plausible-looking number:

1. `REE_assembly/evidence/experiments/runner_status.json` -- FROZEN. Its
   `last_updated` is 2026-06-09T06:00:15Z and its 840 `completed` entries span
   2026-02-26 .. 2026-06-09. Post-Phase-3 cutover (2026-05-28/29) the runner no
   longer maintains it; the coordinator DB + `phase3:` manifest writers are
   authoritative. Reading it yields a real-looking 10.4% that is 40+ days stale.

2. A scan of `evidence/experiments/*.json` manifests -- STRUCTURALLY BLIND to
   ERROR. An ERROR is by definition a crash BEFORE the manifest is written, so
   ERROR runs cannot appear in a manifest scan. Such a scan reports
   `error_rate = 0.0%`, which is an ARTIFACT OF THE METHOD, not a finding.

   Note it is GITIGNORED and untracked (REE_assembly/.gitignore line 10), so it
   is a PER-MACHINE local artifact. A `_frozen` marker block was added to the
   Mac's copy on 2026-07-20, but that marker CANNOT travel -- other machines'
   copies carry no warning at all. This docstring and the /insights skill are
   the only portable statement of the hazard; do not rely on the marker.

This script reads the coordinator DB on the hub, which is the only source that
records non-completing runs distinguishably.

WHAT IT MEASURES (three buckets, reported separately -- do not silently merge)
-----------------------------------------------------------------------------
* `results` rows by outcome (PASS / FAIL / ERROR / UNKNOWN). The `results`
  table has an explicit ERROR outcome, written by the runner's crash-before-
  manifest path (ree-v3 `75ceb5f`, V3-EXQ-654e, 2026-06-17), which synthesizes a
  scoring-neutral ERROR manifest and ships it via `_report_result_and_align`.
  This is the AUTHORITATIVE ERROR count.

* PHANTOM completions -- `experiments.status='completed'` with NO `results` row.
  The DB row was flipped to completed without any manifest or results row. These
  are crash-like but UNCLASSIFIED; they are reported as their own bucket and are
  NOT folded into the ERROR numerator, because we cannot tell a crash from a
  bookkeeping gap without reading the worker's journalctl.

  DO NOT assume a phantom is a silent code crash. One was traced end-to-end on
  2026-07-20 (V3-EXQ-699a) and the mechanism was NOT crash-before-manifest:

      21:05:38Z  cloud-3 claims and starts it (est 600 min)
      08:45:50Z  a user session opens on cloud-3 (operator ssh; no OOM in journal)
      08:46:25Z  [runner] INFRA-CRASH: exit=-15 (likely SIGTERM); leaving in
                 queue, releasing claim, no completion written. actual_secs=42047
      08:49:28Z  ree-runner service Stopped + Started (operator restart)
      08:50:17Z  DB row flips to status='completed'
      09:40:27Z  V3-EXQ-699b queued as the supersedor

  So the runner behaved CORRECTLY and said so loudly -- it classified the
  SIGTERM as transient infra, kept the item in queue, and deliberately wrote no
  completion. The phantom was created by the SUBSEQUENT completed-flip plus
  supersession by 699b, not by a silent crash. The 654e synthetic-ERROR path
  correctly did not fire, because this was never a code crash.

  Consequence for reading the output: the printed upper bound treats every
  phantom as a crash, so it is a genuine UPPER bound and is expected to be
  pessimistic. An operator-killed-then-superseded run inflates it without any
  code being at fault. Before citing the upper bound as an error rate, spot-check
  a phantom's journalctl for `INFRA-CRASH` and its queue_id for a lettered
  supersedor -- both together mean "deliberately retired", not "crashed silently".

* CORROBORATING -- per-machine `evidence/experiments/runner_status/<machine>.json`.
  NOTE the distinction that motivated this whole tool: the MONOLITHIC
  `runner_status.json` is frozen at 2026-06-09, but the PER-MACHINE split is
  still live (files updated within the last day) and it is the richest record of
  ERROR entries, because the runner writes an ERROR there on every crash --
  including crashes that never reach the coordinator. It is read here as a
  cross-check on the ERROR numerator ONLY. It must NOT be used as the
  denominator: the runner deduplicates `completed` by queue_id (preferring
  non-ERROR over ERROR), so its run count is lossy -- it shows 61 classified
  runs for a 30-day window in which the DB holds 179.

* UNMEASURABLE -- transient/infra crashes (exit {137,-9,-11,-15,143} with no
  sentinel: OOM kill, scaler power-off mid-run) are intercepted UPSTREAM by the
  runner, which keeps the item in the queue and releases the claim so it is
  retried. By design these leave no row in any table. A deterministic crash of
  this class retries forever and is invisible here. The script says so out loud
  rather than pretending the denominator is complete.

FAIL-LOUD CONTRACT
------------------
If the hub is unreachable or the DB cannot be read, this script exits NON-ZERO
and prints an explicit error. It NEVER prints a zero or an empty result that a
caller could mistake for "no errors occurred". That distinction is the entire
point of the tool -- a false zero is what it was built to eliminate.

USAGE
-----
    python3 scripts/experiment_error_rate.py                # last 30 days
    python3 scripts/experiment_error_rate.py --days 90
    python3 scripts/experiment_error_rate.py --all
    python3 scripts/experiment_error_rate.py --json         # machine-readable

ASCII-only output (CLAUDE.md rule: no em-dashes/arrows in printed text).
"""

import argparse
import json
import pathlib
import shlex
import subprocess
import sys

HUB_SSH = "ree@91.98.130.117"
HUB_DB = "/home/ree/REE_Working/ree-v3/coordinator/coordinator.db"

# Runs before this are pre-Phase-3 and not reliably represented in the DB.
DB_COVERAGE_START = "2026-05-21"

# Commit 75ceb5f (V3-EXQ-654e) landed the synthetic ERROR-manifest path.
ERROR_PATH_LIVE_SINCE = "2026-06-17"

# Executed on the hub with its stdlib python3. Reads the DB strictly read-only
# (mode=ro) so it can never dirty the hub tree or disturb the phase3 writers.
REMOTE_PROBE = r'''
import json, sqlite3, sys

db = sys.argv[1]
cutoff = sys.argv[2]  # "" means no lower bound

try:
    con = sqlite3.connect("file:%s?mode=ro" % db, uri=True)
except Exception as exc:
    print("PROBE_ERROR: cannot open db: %s" % exc, file=sys.stderr)
    raise SystemExit(3)

def rows(sql, args=()):
    return list(con.execute(sql, args))

where_r, args_r = "", ()
where_e, args_e = "", ()
if cutoff:
    where_r, args_r = "WHERE received_at >= ?", (cutoff,)
    where_e, args_e = "AND e.updated_at >= ?", (cutoff,)

out = {}
out["outcomes"] = dict(
    rows("SELECT COALESCE(outcome,'(null)'), COUNT(*) FROM results %s "
         "GROUP BY 1" % where_r, args_r))
out["n_results"] = rows("SELECT COUNT(*) FROM results %s" % where_r, args_r)[0][0]
out["span"] = rows(
    "SELECT MIN(received_at), MAX(received_at) FROM results %s" % where_r, args_r)[0]

# Crash-before-manifest signature: a completed experiment with no results row.
phantom = rows(
    "SELECT e.queue_id, e.claimed_by_machine, e.updated_at "
    "FROM experiments e LEFT JOIN results r ON r.queue_id = e.queue_id "
    "WHERE e.status = 'completed' AND r.run_id IS NULL %s "
    "ORDER BY e.updated_at DESC" % where_e, args_e)
out["phantoms"] = [
    {"queue_id": q, "machine": m, "updated_at": u} for (q, m, u) in phantom]

# A results row with an outcome but no manifest bytes would be a second
# crash-before-manifest signature. Reported so a future regression is visible.
out["results_without_manifest"] = rows(
    "SELECT COUNT(*) FROM results %s %s (manifest_bytes IS NULL OR "
    "manifest_bytes = 0)" % (where_r, "AND" if where_r else "WHERE"), args_r)[0][0]

out["uncommitted_results"] = rows(
    "SELECT COUNT(*) FROM results %s %s committed_at IS NULL"
    % (where_r, "AND" if where_r else "WHERE"), args_r)[0][0]

out["per_machine"] = [
    {"machine": m, "n": n, "last": last}
    for (m, n, last) in rows(
        "SELECT machine, COUNT(*), MAX(received_at) FROM results %s "
        "GROUP BY machine ORDER BY 2 DESC" % where_r, args_r)]

out["experiment_status"] = dict(
    rows("SELECT status, COUNT(*) FROM experiments GROUP BY status"))

print(json.dumps(out))
'''


def scan_per_machine_errors(cutoff):
    """Corroborating ERROR record from the LIVE per-machine runner_status split.

    Numerator cross-check only -- see the module docstring for why this cannot
    supply the denominator (the runner dedupes `completed` by queue_id).

    Best-effort: a missing directory or an unreadable file yields no
    corroboration rather than an error, because the DB remains authoritative.
    Returns (errors_in_window, fleet_last_error_iso, n_files_read).
    """
    status_dir = (pathlib.Path(__file__).resolve().parent.parent
                  / "evidence" / "experiments" / "runner_status")
    if not status_dir.is_dir():
        return [], None, 0
    errs, last, n_files = [], None, 0
    seen = set()
    for path in sorted(status_dir.glob("*.json")):
        try:
            entries = json.loads(path.read_text()).get("completed", [])
        except Exception:
            continue
        n_files += 1
        for e in entries:
            if e.get("result") != "ERROR":
                continue
            when = e.get("completed_at") or ""
            if last is None or when > last:
                last = when
            if cutoff and when[:10] < cutoff:
                continue
            key = (e.get("queue_id"), when)
            if key in seen:
                continue
            seen.add(key)
            errs.append({"queue_id": e.get("queue_id"),
                         "machine": path.stem, "completed_at": when})
    errs.sort(key=lambda x: x["completed_at"], reverse=True)
    return errs, last, n_files


def resolve_cutoff(days):
    """Turn --days into an ISO date string using the hub's clock."""
    if days is None:
        return ""
    cmd = ["ssh", "-o", "ConnectTimeout=10", "-o", "BatchMode=yes", HUB_SSH,
           "date -u -d '%d days ago' +%%Y-%%m-%%d" % days]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    except subprocess.TimeoutExpired:
        raise RuntimeError("hub %s did not respond within 30s" % HUB_SSH)
    except Exception as exc:
        raise RuntimeError("could not invoke ssh: %s" % exc)
    if proc.returncode != 0:
        raise RuntimeError("could not resolve cutoff date on hub: %s"
                           % (proc.stderr or "").strip()[:300])
    return proc.stdout.strip()


def main():
    ap = argparse.ArgumentParser(
        description="Live ERROR rate for the V3 corpus, from the coordinator DB.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--days", type=int, default=30,
                   help="window in days (default 30)")
    g.add_argument("--all", action="store_true",
                   help="all DB history (from %s)" % DB_COVERAGE_START)
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args()

    days = None if args.all else args.days

    try:
        cutoff = resolve_cutoff(days)
        data = fetch_with_cutoff(cutoff)
    except RuntimeError as exc:
        # FAIL LOUD. Never degrade to a zero or an empty report.
        sys.stderr.write(
            "ERROR: could not read the coordinator DB, so the ERROR rate is "
            "UNKNOWN.\n"
            "  reason: %s\n"
            "  Do NOT substitute a manifest scan: an ERROR is a crash BEFORE\n"
            "  the manifest is written, so a manifest scan always reports 0.0%%,\n"
            "  which is an artifact of the method rather than a finding.\n"
            "  Do NOT substitute runner_status.json: it is frozen at 2026-06-09.\n"
            "  (It is gitignored, so its _frozen marker may be absent on this\n"
            "  machine even though the staleness is real.)\n"
            "  Report the ERROR rate as UNMEASURED for this run.\n" % exc)
        return 2

    outcomes = data["outcomes"]
    n_pass = outcomes.get("PASS", 0)
    n_fail = outcomes.get("FAIL", 0)
    n_error = outcomes.get("ERROR", 0)
    n_unknown = outcomes.get("UNKNOWN", 0)
    classified = n_pass + n_fail + n_error
    err_rate = (n_error / classified * 100.0) if classified else None

    phantoms = data["phantoms"]
    n_phantom = len(phantoms)
    rs_errs, rs_last, rs_files = scan_per_machine_errors(cutoff)
    # Upper bound treats every phantom as a crash; the truth is between the two.
    upper = ((n_error + n_phantom) / (classified + n_phantom) * 100.0
             if (classified + n_phantom) else None)

    if args.json:
        print(json.dumps({
            "window_days": days,
            "cutoff": cutoff or DB_COVERAGE_START,
            "source": "coordinator.db results + experiments (hub %s)" % HUB_SSH,
            "span": data["span"],
            "pass": n_pass, "fail": n_fail, "error": n_error,
            "unknown": n_unknown,
            "classified_runs": classified,
            "error_rate_pct": err_rate,
            "phantom_completions": n_phantom,
            "error_rate_upper_bound_pct": upper,
            "phantom_detail": phantoms,
            "runner_status_errors_in_window": len(rs_errs),
            "runner_status_error_detail": rs_errs,
            "fleet_last_error_recorded": rs_last,
            "runner_status_files_read": rs_files,
            "results_without_manifest": data["results_without_manifest"],
            "uncommitted_results": data["uncommitted_results"],
            "per_machine": data["per_machine"],
            "experiment_status": data["experiment_status"],
            "unmeasurable_note": (
                "Transient/infra crashes (exit 137/-9/-11/-15/143, no sentinel) "
                "are intercepted upstream and retried in-queue; they leave no "
                "row and are not counted in any bucket."),
        }, indent=2))
        return 0

    window = "all DB history" if days is None else "last %d days" % days
    print("V3 experiment ERROR rate -- %s" % window)
    print("source: coordinator DB `results` + `experiments` on hub %s" % HUB_SSH)
    print("span:   %s .. %s" % (data["span"][0], data["span"][1]))
    print()
    print("  PASS   %4d" % n_pass)
    print("  FAIL   %4d" % n_fail)
    print("  ERROR  %4d" % n_error)
    if n_unknown:
        print("  UNKNOWN%4d" % n_unknown)
    print("  ----------------")
    print("  classified runs: %d" % classified)
    if err_rate is None:
        print("  ERROR rate: n/a (no classified runs in window)")
    else:
        print("  ERROR rate: %.1f%%  (%d / %d)" % (err_rate, n_error, classified))
    print()
    print("  phantom completions (completed, no results row): %d" % n_phantom)
    if n_phantom:
        print("    These are crash-like but UNCLASSIFIED. Not folded into the")
        print("    ERROR numerator above. Treating every one as a crash gives an")
        print("    upper bound of %.1f%%; the true rate is in [%.1f%%, %.1f%%]."
              % (upper, err_rate if err_rate is not None else 0.0, upper))
        for p in phantoms[:10]:
            print("      %-16s %-18s %s"
                  % (p["queue_id"], p["machine"] or "(unrecorded)",
                     p["updated_at"]))
        if n_phantom > 10:
            print("      ... and %d more" % (n_phantom - 10))
    print("  corroborating ERROR entries in the LIVE per-machine")
    print("  runner_status/ split (%d file(s) read): %d in window"
          % (rs_files, len(rs_errs)))
    for e in rs_errs[:10]:
        print("      %-16s %-18s %s"
              % (e["queue_id"], e["machine"], e["completed_at"][:19]))
    if len(rs_errs) > 10:
        print("      ... and %d more" % (len(rs_errs) - 10))
    print("  last ERROR recorded anywhere in the fleet: %s"
          % (rs_last[:19] if rs_last else "(none on record)"))
    print("  (numerator cross-check only -- this split dedupes `completed` by")
    print("   queue_id, so it CANNOT supply the denominator.)")
    print()
    if data["results_without_manifest"]:
        print("  WARN: %d results row(s) have an outcome but no manifest bytes."
              % data["results_without_manifest"])
        print("        That is a second crash-before-manifest signature -- investigate.")
    if data["uncommitted_results"]:
        print("  WARN: %d results row(s) not yet committed by sync_daemon."
              % data["uncommitted_results"])
    print("caveats:")
    print("  - The synthetic ERROR-record path went live %s (ree-v3 75ceb5f)."
          % ERROR_PATH_LIVE_SINCE)
    print("    ERROR counts before that date understate the true rate.")
    print("  - Transient/infra crashes (exit 137/-9/-11/-15/143, no sentinel) are")
    print("    intercepted upstream, kept in queue and retried. They leave no row")
    print("    in any table and are counted in NO bucket here. A deterministic")
    print("    crash of that class retries forever and is invisible to this tool.")
    print("  - DB coverage begins %s (Phase-3 cutover). For earlier history the"
          % DB_COVERAGE_START)
    print("    frozen runner_status.json corpus is the only record.")
    return 0


def fetch_with_cutoff(cutoff, timeout=60):
    cmd = ["ssh", "-o", "ConnectTimeout=10", "-o", "BatchMode=yes", HUB_SSH,
           "python3 - %s %s" % (shlex.quote(HUB_DB), shlex.quote(cutoff))]
    try:
        proc = subprocess.run(cmd, input=REMOTE_PROBE, capture_output=True,
                              text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise RuntimeError("hub %s did not respond within %ss" % (HUB_SSH, timeout))
    except Exception as exc:
        raise RuntimeError("could not invoke ssh: %s" % exc)
    if proc.returncode != 0:
        raise RuntimeError("hub probe failed (rc=%d): %s"
                           % (proc.returncode, (proc.stderr or "").strip()[:500]))
    try:
        return json.loads(proc.stdout)
    except Exception as exc:
        raise RuntimeError("hub probe returned unparseable output: %s (%r)"
                           % (exc, proc.stdout[:300]))


if __name__ == "__main__":
    sys.exit(main())
