#!/usr/bin/env python3
"""Steward detector runner -- stage 1.

Runs every registered detector, diffs the result against the previous run, applies
suppressions, and writes reports/steward_report.json carrying a single boolean:

    escalate: true|false

THAT BOOLEAN IS THE WHOLE POINT. It is the gate that decides whether a model is
loaded at all. Detection is deterministic and costs nothing; adjudication is what
costs tokens. A repo with no NEW unsuppressed findings must produce
`escalate: false` so the Steward skill never loads, and the standing cost of
running this on every governance cycle stays at roughly one second of CPU.

CLASSIFICATION, against state/steward_state.json:

    NEW        finding_id absent from the previous run  -> escalation candidate
    RECURRING  present in both                          -> never escalates
    RESOLVED   present previously, absent now           -> reported, not escalated

Only NEW findings escalate. This is what makes the second consecutive run quiet:
an unfixed defect is real, but it is not NEWS, and re-escalating it every cycle
would burn the budget on things a human has already seen and chosen to leave.
RESOLVED entries are reported because a finding disappearing is how a fix is
confirmed -- SD-031 no longer appearing in D-002 is the ratchet working.

BUDGET. At most MAX_ESCALATE findings are escalated per run, ranked by
severity x confidence. The cap is a BUDGET, not a filter: ranking decides the
order things are looked at under contention, it never withholds a finding from
the report. Everything is always in `findings`. When the cap truncates, the
report says so explicitly (`escalation_truncated`) rather than silently
presenting five as if they were all of them.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/steward/run_detectors.py
    /opt/local/bin/python3 scripts/steward/run_detectors.py --json
    /opt/local/bin/python3 scripts/steward/run_detectors.py --no-write   # dry run

Exit code is 0 whether or not findings exist -- this is a hint, never a gate, so
it is safe to chain in governance.sh. --exit-nonzero-on-escalate opts in to a
gate. ASCII-only output (Windows terminals).
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from detectors import DETECTORS  # noqa: E402
from detectors._common import (  # noqa: E402
    Context,
    load_context,
    rank_score,
    repo_root_from_here,
)

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore

MAX_ESCALATE = 5

STATE_DIRNAME = "state"
REPORT_DIRNAME = "reports"
STATE_FILE = "steward_state.json"
SUPPRESSIONS_FILE = "suppressions.yaml"
LEDGER_FILE = "steward_ledger.jsonl"
REPORT_FILE = "steward_report.json"


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_suppressions(path: Path) -> list[dict]:
    """Load suppressions.yaml -> list of entries.

    An entry needs a `finding_id`, which may be an fnmatch pattern so a whole
    class (one plan, one detector) can be suppressed with one line. `reason` is
    required in spirit; a suppression with no stated reason is how a real defect
    gets buried, so it is reported in the run banner when missing.
    """
    if not path.exists() or yaml is None:
        return []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    if isinstance(data, dict):
        data = data.get("suppressions") or []
    if not isinstance(data, list):
        return []
    out = []
    for e in data:
        if isinstance(e, dict) and e.get("finding_id"):
            out.append(e)
    return out


def match_suppression(finding_id: str, suppressions: list[dict]) -> dict | None:
    for s in suppressions:
        pat = str(s["finding_id"])
        if pat == finding_id or fnmatch.fnmatch(finding_id, pat):
            return s
    return None


def load_state(path: Path) -> dict:
    if not path.exists():
        return {"findings": {}, "runs": 0, "last_run": None}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {"findings": {}, "runs": 0, "last_run": None}
    if not isinstance(data, dict):
        return {"findings": {}, "runs": 0, "last_run": None}
    data.setdefault("findings", {})
    data.setdefault("runs", 0)
    return data


def classify(findings: list[dict], prior: dict) -> tuple[list[dict], list[dict]]:
    """Annotate findings NEW/RECURRING and build the RESOLVED list."""
    prior_findings = prior.get("findings", {}) or {}
    seen_now = set()
    for f in findings:
        fid = f["finding_id"]
        seen_now.add(fid)
        was = prior_findings.get(fid)
        if was:
            f["classification"] = "RECURRING"
            f["first_seen"] = was.get("first_seen")
            f["times_seen"] = int(was.get("times_seen", 1)) + 1
        else:
            f["classification"] = "NEW"
            f["first_seen"] = None   # filled with this run's timestamp below
            f["times_seen"] = 1

    resolved = []
    for fid, rec in sorted(prior_findings.items()):
        if fid not in seen_now:
            resolved.append({
                "finding_id": fid,
                "classification": "RESOLVED",
                "detector": rec.get("detector"),
                "subject": rec.get("subject"),
                "title": rec.get("title"),
                "severity": rec.get("severity"),
                "first_seen": rec.get("first_seen"),
                "last_seen": rec.get("last_seen"),
                "times_seen": rec.get("times_seen"),
            })
    return findings, resolved


def run_all(ctx: Context) -> tuple[list[dict], list[dict]]:
    findings: list[dict] = []
    summaries: list[dict] = []
    for mod in DETECTORS:
        t0 = time.time()
        try:
            f, s = mod.run(ctx)
        except Exception as exc:  # one broken detector must not kill the run
            f, s = [], {
                "detector": getattr(mod, "DETECTOR_ID", mod.__name__),
                "error": "%s: %s" % (type(exc).__name__, exc),
                "n_findings": 0,
            }
        s = dict(s)
        s["duration_s"] = round(time.time() - t0, 3)
        findings.extend(f)
        summaries.append(s)
    return findings, summaries


def build_report(ctx: Context, state_dir: Path, now: str,
                 duration_s: float) -> dict:
    findings, summaries = run_all(ctx)
    prior = load_state(state_dir / STATE_FILE)
    suppressions = load_suppressions(state_dir / SUPPRESSIONS_FILE)

    findings, resolved = classify(findings, prior)

    for f in findings:
        if f.get("first_seen") is None:
            f["first_seen"] = now
        f["last_seen"] = now
        sup = match_suppression(f["finding_id"], suppressions)
        if sup:
            f["suppressed"] = True
            f["suppression_reason"] = sup.get("reason")
            f["suppression_pattern"] = sup.get("finding_id")
        else:
            f["suppressed"] = False

    candidates = [f for f in findings
                  if f["classification"] == "NEW"
                  and not f["suppressed"]
                  and f.get("escalate")]
    candidates.sort(key=lambda f: (-rank_score(f), f["finding_id"]))
    escalated = candidates[:MAX_ESCALATE]

    findings.sort(key=lambda f: (-rank_score(f), f["finding_id"]))

    return {
        "generated_at": now,
        "duration_s": round(duration_s, 3),
        "repo_root": str(ctx.repo_root),
        "schema": "steward_report.v1",
        "escalate": bool(escalated),
        "escalated": [f["finding_id"] for f in escalated],
        "escalation_budget": MAX_ESCALATE,
        "escalation_candidates": len(candidates),
        "escalation_truncated": max(0, len(candidates) - len(escalated)),
        "counts": {
            "total": len(findings),
            "new": sum(1 for f in findings if f["classification"] == "NEW"),
            "recurring": sum(1 for f in findings
                             if f["classification"] == "RECURRING"),
            "resolved": len(resolved),
            "suppressed": sum(1 for f in findings if f["suppressed"]),
        },
        "detectors": summaries,
        "findings": findings,
        "resolved": resolved,
        "parse_errors": ctx.parse_errors,
    }


def write_state(state_dir: Path, report: dict, now: str) -> None:
    findings = report["findings"]
    state = {
        "schema": "steward_state.v1",
        "last_run": now,
        "runs": load_state(state_dir / STATE_FILE).get("runs", 0) + 1,
        "findings": {
            f["finding_id"]: {
                "detector": f["detector"],
                "subject": f["subject"],
                "title": f["title"],
                "severity": f["severity"],
                "confidence": f["confidence"],
                "first_seen": f["first_seen"],
                "last_seen": f["last_seen"],
                "times_seen": f["times_seen"],
            }
            for f in findings
        },
    }
    (state_dir / STATE_FILE).write_text(
        json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def append_ledger(state_dir: Path, report: dict, now: str) -> None:
    """One line per run. This is what calibrates escalation ranking later.

    Deliberately records the counts and the escalated ids only -- the full
    findings live in the report. The ledger's value is the time series.
    """
    entry = {
        "ts": now,
        "escalate": report["escalate"],
        "escalated": report["escalated"],
        "counts": report["counts"],
        "duration_s": report["duration_s"],
        "by_detector": {s.get("detector"): s.get("n_findings", 0)
                        for s in report["detectors"]},
    }
    with (state_dir / LEDGER_FILE).open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, sort_keys=True) + "\n")


def print_banner(report: dict) -> None:
    c = report["counts"]
    print("Steward stage 1 -- %d finding(s) in %.2fs  [new %d / recurring %d / "
          "resolved %d / suppressed %d]"
          % (c["total"], report["duration_s"], c["new"], c["recurring"],
             c["resolved"], c["suppressed"]))
    for s in report["detectors"]:
        if s.get("error"):
            print("  %-7s ERROR %s" % (s.get("detector", "?"), s["error"]))
        else:
            print("  %-7s %3d finding(s)  %.2fs  %s"
                  % (s.get("detector", "?"), s.get("n_findings", 0),
                     s.get("duration_s", 0.0), s.get("title", "")))
    if report["resolved"]:
        print("  RESOLVED since last run:")
        for r in report["resolved"]:
            print("    - %s  %s" % (r["finding_id"], r.get("title") or ""))
    if report["escalate"]:
        print("  ESCALATE: %d (budget %d, %d not shown)"
              % (len(report["escalated"]), report["escalation_budget"],
                 report["escalation_truncated"]))
        for fid in report["escalated"]:
            f = next(x for x in report["findings"] if x["finding_id"] == fid)
            print("    [%s %s conf=%.2f] %s"
                  % (f["severity"], f["signal"], f["confidence"], f["title"]))
    else:
        print("  ESCALATE: no -- nothing new and unsuppressed. "
              "Steward skill should NOT load.")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Run Steward integrity detectors.")
    ap.add_argument("--repo-root", default=None,
                    help="REE_assembly root (default: inferred from this file)")
    ap.add_argument("--state-dir", default=None,
                    help="override state/ dir (tests use a tmpdir)")
    ap.add_argument("--report", default=None, help="override report path")
    ap.add_argument("--no-write", action="store_true",
                    help="do not write state, ledger or report")
    ap.add_argument("--json", action="store_true",
                    help="print the report JSON to stdout")
    ap.add_argument("--exit-nonzero-on-escalate", action="store_true",
                    help="exit 2 when escalate is true (opt-in gate)")
    args = ap.parse_args(argv)

    repo_root = Path(args.repo_root).resolve() if args.repo_root \
        else repo_root_from_here()
    state_dir = Path(args.state_dir).resolve() if args.state_dir \
        else _HERE / STATE_DIRNAME
    report_path = Path(args.report).resolve() if args.report \
        else _HERE / REPORT_DIRNAME / REPORT_FILE

    state_dir.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    now = _utc_now()
    ctx = load_context(repo_root)
    report = build_report(ctx, state_dir, now, 0.0)
    report["duration_s"] = round(time.time() - t0, 3)

    if not args.no_write:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        append_ledger(state_dir, report, now)
        write_state(state_dir, report, now)

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print_banner(report)

    if args.exit_nonzero_on_escalate and report["escalate"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
