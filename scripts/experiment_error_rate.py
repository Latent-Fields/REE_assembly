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

  ROOT CAUSE (confirmed 2026-07-20 by session cranky-pascal-46cd9a):
  `ree-v3/coordinator/db.py mark_queue_removed()` sets status='completed' for
  EVERY exit from the queue and originally accepted a `reason` argument that it
  silently DISCARDED. There is no cancelled/removed/errored status, so an
  operator cancellation, a runner ERROR and a scientific FAIL all wrote an
  identical row. ('completed' was never even in the column's declared enum
  comment, `pending|claimed|failed`.)

  So "phantom completion" is a MISNOMER. `status='completed' LEFT JOIN results
  -> no row` does not isolate crashes; it isolates everything that left the
  queue without posting a result -- DELIBERATE CANCELLATIONS INCLUDED.

  Worked example, V3-EXQ-699a, traced end-to-end. Note the ordering: the
  cancellation came FIRST and caused the SIGTERM, not the other way round.

      07-19 21:05:38Z  cloud-3 claims and starts it (est 600 min)
      07-20 08:44:49Z  POST /queue/remove from hub 10.8.0.1 -> 401
            08:45:21Z  POST /queue/remove -> 200   <-- PHANTOM CREATED HERE
            08:46:04Z  POST /queue/remove -> 200
            08:46:25Z  [runner] INFRA-CRASH: exit=-15 (SIGTERM); leaving in
                       queue, releasing claim, no completion written (42047s)
            08:48:28Z  force_stop cmd -> cloud-3 drains
            08:50:17Z  reconcile tick re-upserts from the stale queue file;
                       preserve_claim=True copies the existing status and only
                       refreshes updated_at
            09:40:27Z  V3-EXQ-699b queued as the supersedor

  A /failure-autopsy session deliberately cancelled the 11.7h in-flight run to
  replace it with an instrument repair. Intended workflow, correctly executed;
  the only defect is that it is RECORDED identically to a real completion.

  **`updated_at` is a RED HERRING** -- it is the last reconcile tick, not the
  flip. An earlier revision of this file cited 08:50:17Z as the flip time and
  inferred an operator ssh session as the trigger; both were wrong. Corroboration
  that this generalises: several phantoms have a last claim attempt AFTER their
  updated_at (495a by 24h, 700c-m by 25h, 624 by 11h) -- workers still trying to
  claim items already marked completed, the signature of removal-then-file-lag.

  WHY 654e's synthetic-ERROR path has never fired -- three upstream escape
  hatches, all reached by `continue`:
    1. the infra-crash interceptor (experiment_runner.py:3473, {137,-9,-11,-15,
       143} no-sentinel) continues BEFORE the ERROR branch, so the synthetic
       writer at :3548 is structurally unreachable from it. This is CORRECT --
       the interceptor requeues properly and is NOT a phantom source.
    2. the ERROR-with-missing-manifest guard (:3522) -- leaves in queue, continue.
    3. POST /queue/remove bypasses the runner entirely. 699a's route.
  Fleet-wide since 654e: 2 INFRA-CRASH, 0 synthetic manifests, 0 ERROR-missing.

  WHY `results` has zero ERROR rows all-time: pre-654e,
  `_report_result_and_align` was gated on a non-empty manifest path, so a crash
  with no manifest skipped it while `report_queue_remove(queue_id,"ERROR")`
  still fired. That is exactly the bug 654e fixed; the 5 historical confirmed
  ERRORs (517c, 610a, 612b, 621, 669) simply predate it.

  THE BUCKET IS HETEROGENEOUS -- do not collapse it to one story. Three
  distinct populations have been confirmed in it:
    * operator cancellation  -- V3-EXQ-699a (POST /queue/remove, superseded)
    * genuine crash          -- 517c, 610a, 612b, 621, 669 (confirmed ERROR in
                                the per-machine split; all predate 654e)
    * pure bookkeeping gap   -- V3-EXQ-673: all 6 run manifests exist and are on
                                origin, yet it has NO results row. Nothing
                                crashed and nothing was cancelled; only the
                                results row is missing. This is the counter-
                                example that proves the bucket is not uniformly
                                cancellations, and the reason the phantom count
                                must never be reported as an error count.
                                (673's 3 stranded manifests were recovered from
                                ree-cloud-2 and committed 2026-07-20 in
                                1a4ad27d9e -- it was already the contrast case
                                before that, with 3 of 6 manifests present.)

  CONSEQUENCE FOR THE UPPER BOUND: it is inflated, because it counts deliberate
  cancellations AND bookkeeping gaps as possible errors. Once `removal_reason`
  is live (see below) this script subtracts the cancellations automatically;
  bookkeeping gaps stay in, so even then it remains an upper bound. Until then,
  spot-check a phantom for a `/queue/remove` in the coordinator log and a
  lettered supersedor -- together they mean "deliberately retired", not
  "crashed silently".

  REASON VOCABULARY IS CLOSED at {PASS, FAIL, ERROR} -- verified exhaustively by
  session cranky-pascal-46cd9a, not assumed. experiment_runner.py has exactly
  four report_queue_remove call sites: :3462 "FAIL", :3763 "ERROR", :3832
  "FAIL", and :3961 result["result"], which can only ever be "PASS" (UNKNOWN is
  intercepted at :3843 -- released, left in queue, `continue` -- the pre-
  2026-05-08 V3-EXQ-433f/537/538 silent-drop fix; FAIL and ERROR are consumed at
  their own earlier branches). coordinator_client.report_queue_remove is the
  sole wrapper, so any OTHER reason value is necessarily operator-issued. That
  is what makes the classification below exhaustive rather than merely cautious:
  do NOT widen the set without re-verifying those four call sites.

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
import os
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

# A completed experiment with no results row. NOT necessarily a crash -- see the
# module docstring: mark_queue_removed() collapses cancellation/ERROR/FAIL into
# status='completed'. `removal_reason` (added by session cranky-pascal-46cd9a in
# ree-v3 coordinator/db.py) disambiguates them. It is read ONLY IF PRESENT, so
# this probe keeps working against a hub whose migration has not run yet, and
# starts subtracting cancellations automatically the moment it has.
cols = [r[1] for r in rows("PRAGMA table_info(experiments)")]
has_reason = "removal_reason" in cols
out["has_removal_reason"] = has_reason
reason_sel = "e.removal_reason" if has_reason else "NULL"

phantom = rows(
    "SELECT e.queue_id, e.claimed_by_machine, e.updated_at, %s "
    "FROM experiments e LEFT JOIN results r ON r.queue_id = e.queue_id "
    "WHERE e.status = 'completed' AND r.run_id IS NULL %s "
    "ORDER BY e.updated_at DESC" % (reason_sel, where_e), args_e)
out["phantoms"] = [
    {"queue_id": q, "machine": m, "updated_at": u, "removal_reason": rr}
    for (q, m, u, rr) in phantom]

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


# Hours after which the git runner_status split is considered frozen. The
# per-run outcome lists it carries have NO coordinator /shadow/status
# equivalent, so the git read stays -- but its git materialization is retired
# (2026-09-01), so a fully-stale directory means the corroboration counts may
# be incomplete and the report says so (non-fatal either way; the DB is the
# authority for the rate itself).
RUNNER_STATUS_STALE_HOURS = 48.0


def runner_status_split_is_stale():
    """True when EVERY runner_status file is >48h old by mtime AND embedded ts.

    A file is fresh if either its mtime or its embedded last_updated is within
    the window (unparseable embedded timestamp -> mtime alone decides). An
    absent directory or no files returns False -- that case already reads as
    "0 file(s) read" in the report. Never raises.
    """
    from datetime import datetime, timezone
    status_dir = (pathlib.Path(__file__).resolve().parent.parent
                  / "evidence" / "experiments" / "runner_status")
    try:
        if not status_dir.is_dir():
            return False
        files = sorted(status_dir.glob("*.json"))
        if not files:
            return False
        now = datetime.now(timezone.utc)
        cutoff_s = RUNNER_STATUS_STALE_HOURS * 3600.0
        for f in files:
            try:
                mtime_age = now.timestamp() - f.stat().st_mtime
            except OSError:
                continue
            if mtime_age <= cutoff_s:
                return False
            emb = ""
            try:
                emb = str(json.loads(f.read_text()).get("last_updated") or "")
            except Exception:
                emb = ""
            if emb:
                try:
                    ts = datetime.fromisoformat(emb.replace("Z", "+00:00"))
                    if ts.tzinfo is None:
                        ts = ts.replace(tzinfo=timezone.utc)
                    if (now - ts).total_seconds() <= cutoff_s:
                        return False
                except Exception:
                    pass
        return True
    except Exception:
        return False


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


def has_manifests_on_disk(queue_id):
    """True if any evidence artifact exists for this queue_id.

    The secondary test that separates the two populations a NULL
    `removal_reason` can mean (suggested by session cranky-pascal-46cd9a):

      * manifests present -> BOOKKEEPING GAP. The run produced evidence, so it
        cannot have crashed before writing a manifest; only the results row is
        missing. V3-EXQ-673 is the worked case (6 manifests, 0 results rows).
      * no manifests      -> CRASH CANDIDATE. Nothing was produced.
        V3-EXQ-699a is the worked case (0 manifests).

    Matching is on the `v3_exq_<id>_` prefix with the trailing underscore as a
    boundary, so `v3_exq_673_` does NOT match the distinct EXQ `v3_exq_673a_`.
    """
    evidence_dir = (pathlib.Path(__file__).resolve().parent.parent
                    / "evidence" / "experiments")
    if not evidence_dir.is_dir():
        return None  # cannot tell -- caller treats as unclassified
    prefix = queue_id.lower().replace("-", "_") + "_"
    try:
        return any(name.startswith(prefix) for name in os.listdir(evidence_dir))
    except OSError:
        return None


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
    has_reason = data.get("has_removal_reason", False)
    # A reason the runner itself reports (PASS/FAIL/ERROR) is a real outcome; any
    # other non-empty reason is an operator cancellation via POST /queue/remove.
    # Only the latter is subtracted -- an ERROR removal is still a crash.
    RUNNER_OUTCOMES = {"PASS", "FAIL", "ERROR"}
    cancelled = [p for p in phantoms
                 if (p.get("removal_reason") or "").strip()
                 and (p["removal_reason"] or "").strip().upper() not in RUNNER_OUTCOMES]
    residual = [p for p in phantoms if p not in cancelled]
    # Secondary split of the residual: evidence on disk means it ran and
    # produced output, so it is a bookkeeping gap, not a crash-before-manifest.
    # GUARD (do not remove): manifest-presence alone is UNSOUND, because a
    # queue_id can carry manifests from an EARLIER run while a LATER run under
    # the same id crashed -- the same-EXQ silent-rerun anti-pattern, which is
    # real in this corpus (V3-EXQ-673 alone has 6 runs). Without this guard the
    # split misfiled 517c, 610a and 621 -- three of the five CONFIRMED crashes
    # -- as bookkeeping gaps and under-stated the upper bound. A queue_id with a
    # confirmed ERROR in the per-machine split is never a gap, whatever is on
    # disk. Uses the ALL-TIME confirmed set, not the windowed one: the crash may
    # predate the window while the phantom row falls inside it.
    _all_errs, _, _ = scan_per_machine_errors("")
    confirmed_error_qids = {e["queue_id"] for e in _all_errs if e.get("queue_id")}
    for p in residual:
        p["has_manifests"] = has_manifests_on_disk(p["queue_id"])
        p["confirmed_error"] = p["queue_id"] in confirmed_error_qids
    gaps = [p for p in residual
            if p.get("has_manifests") is True and not p["confirmed_error"]]
    unexplained = [p for p in residual if p not in gaps]
    n_phantom = len(unexplained)
    n_cancelled = len(cancelled)
    n_gaps = len(gaps)
    rs_errs, rs_last, rs_files = scan_per_machine_errors(cutoff)
    rs_stale = runner_status_split_is_stale()
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
            "phantom_detail": unexplained,
            "bookkeeping_gaps": n_gaps,
            "bookkeeping_gap_detail": gaps,
            "operator_cancellations": n_cancelled,
            "operator_cancellation_detail": cancelled,
            "removal_reason_available": has_reason,
            "runner_status_errors_in_window": len(rs_errs),
            "runner_status_error_detail": rs_errs,
            "fleet_last_error_recorded": rs_last,
            "runner_status_files_read": rs_files,
            "runner_status_split_stale": rs_stale,
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
    if has_reason:
        print("  operator cancellations (deliberate /queue/remove): %d -- EXCLUDED"
              % n_cancelled)
        for p in cancelled[:5]:
            print("      %-16s %s" % (p["queue_id"], p.get("removal_reason")))
    else:
        print("  operator cancellations: NOT SEPARABLE on this hub --")
        print("    the `removal_reason` column is not present in coordinator.db,")
        print("    so deliberate cancellations are still counted below and the")
        print("    upper bound is INFLATED. It self-corrects once the migration")
        print("    lands (ree-v3 coordinator/db.py mark_queue_removed).")
    if n_gaps:
        print("  bookkeeping gaps (evidence on disk, only the results row\n"
              "    missing -- ran fine, did NOT crash): %d -- EXCLUDED" % n_gaps)
        for p in gaps[:5]:
            print("      %-16s %s" % (p["queue_id"], p["updated_at"]))
    print("  unexplained phantoms (no evidence on disk): %d" % n_phantom)
    if n_phantom:
        print("    No evidence on disk, so not separable further here. Contains")
        print("    genuine crashes, plus any cancellation or gap the two tests")
        print("    above could not catch:")
        if has_reason:
            print("      - PRE-MIGRATION cancellations (removal_reason never")
            print("        recorded, so nothing to subtract on)")
        else:
            print("      - ALL cancellations (removal_reason not live on this hub)")
        print("      - a crash whose queue_id also carries an earlier run's")
        print("        manifests is kept HERE, not filed as a gap (same-EXQ")
        print("        rerun guard; it misfiled 517c/610a/621 without it)")
        print("    Not folded into the ERROR numerator. Treating every one as a")
        print("    crash gives an upper bound of %.1f%%; true rate in [%.1f%%, %.1f%%]."
              % (upper, err_rate if err_rate is not None else 0.0, upper))
        for p in unexplained[:10]:
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
    if rs_stale:
        print("  WARNING: the git runner_status telemetry mirror is")
        print("    retired/frozen -- every file is older than %dh (mtime and"
              % int(RUNNER_STATUS_STALE_HOURS))
        print("    embedded timestamps). The corroboration counts above may be")
        print("    incomplete; the coordinator DB remains the authority.")
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
