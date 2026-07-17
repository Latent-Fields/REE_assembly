#!/usr/bin/env python3
"""Anti-Goodhart audit for the Scientific Progress Dashboard's hypothesis space.

Sibling of check_closure_drift.py / check_granularity_debt_recurrence.py. The
hypothesis-space dashboard can be gamed three ways -- this catches all three and
prints them as advisory flags. It NEVER blocks: exits 0 regardless of findings
(design rule 5: "Flags are advisory, printed, non-blocking").

Checks (design rule 5):
  (a) Un-backed surviving-count drop -- a question whose surviving count fell
      (across the append-only time series, or within the registry) with no
      adjudicated `weakens`/discrimination behind the eliminations that caused it.
  (b) Post-hoc enlargement of a frozen initial set -- initial_frozen_count grew
      after registration, or a hypothesis's pre_registered_utc is AFTER the run
      that adjudicated it (retro-padding the denominator).
  (c) Confirmed without a passed control -- a `confirmed` hypothesis whose
      resolution lacks control_passed == true.
  (d) Elimination-bar violation -- an `eliminated`/`split` hypothesis missing the
      full bar (met_elimination_bar + control_passed + non_degenerate == true).

Output: evidence/planning/hypothesis_space_integrity.md.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/check_hypothesis_space_integrity.py
    /opt/local/bin/python3 scripts/check_hypothesis_space_integrity.py --self-test
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PLANNING_DIR = REPO_ROOT / "evidence" / "planning"
REGISTRY = PLANNING_DIR / "hypothesis_space_registry.v1.json"
TIMESERIES = PLANNING_DIR / "hypothesis_space_timeseries.v1.jsonl"
REPORT = PLANNING_DIR / "hypothesis_space_integrity.md"

RESOLVED_OUT_STATES = {"eliminated", "split"}
# An adjudicated basis for an elimination: a weakens, OR a confirmed-cluster
# non_contributory discrimination that met the bar (design's own Dim-3 worked
# example treats a sub-floor discrimination against passing reference bands as an
# elimination -- see the registry's elimination_bar invariant).
ADJUDICATED_DIRECTIONS = {"weakens", "non_contributory"}


def _utc_now_iso_z() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _load_timeseries(path: Path) -> list:
    out = []
    if not path.exists():
        return out
    for ln in path.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln:
            continue
        try:
            out.append(json.loads(ln))
        except ValueError:
            continue
    out.sort(key=lambda r: r.get("date") or "")
    return out


def audit(registry: dict, timeseries: list) -> dict:
    """Return {flag_bucket: [messages]} for each of the four checks."""
    flags = {"a_unbacked_drop": [], "b_enlargement": [],
             "c_confirmed_no_control": [], "d_bar_violation": []}
    questions = registry.get("questions") or []

    for q in questions:
        qid = q.get("qid")
        initial = int(q.get("initial_frozen_count") or 0)
        n_hyps = len(q.get("hypotheses") or [])
        # (b1) denominator consistency: initial_frozen_count must equal the number
        # of pre-registered hypotheses (no phantom denominator padding).
        if initial != n_hyps:
            flags["b_enlargement"].append(
                f"`{qid}`: initial_frozen_count={initial} but {n_hyps} hypotheses "
                "registered -- denominator does not match the enumerated set."
            )
        for h in q.get("hypotheses") or []:
            hid = h.get("hid")
            res = h.get("resolution") or {}
            state = res.get("state") or "untested"
            pre = (h.get("pre_registered_utc") or "")[:10]
            resolved = (res.get("resolved_utc") or "")[:10]
            direction = (res.get("evidence_direction") or "").lower()

            # (b2) retro-padding: a hypothesis pre-registered AFTER the run that
            # adjudicated it (evidence was already in when it was "pre"-registered).
            if pre and resolved and pre > resolved:
                flags["b_enlargement"].append(
                    f"`{qid}`/`{hid}`: pre_registered_utc {pre} is AFTER its "
                    f"resolution {resolved} -- retro-padded pre-registration."
                )

            # (c) confirmed without a passed control.
            if state == "confirmed" and res.get("control_passed") is not True:
                flags["c_confirmed_no_control"].append(
                    f"`{qid}`/`{hid}`: state=confirmed but control_passed="
                    f"{res.get('control_passed')!r} -- a confirmed node needs a passed control."
                )

            # (d) elimination-bar violation.
            if state in RESOLVED_OUT_STATES:
                missing = []
                if res.get("met_elimination_bar") is not True:
                    missing.append("met_elimination_bar")
                if res.get("control_passed") is not True:
                    missing.append("control_passed")
                if res.get("non_degenerate") is not True:
                    missing.append("non_degenerate")
                if missing:
                    flags["d_bar_violation"].append(
                        f"`{qid}`/`{hid}`: state={state} but missing "
                        f"{', '.join(missing)} -- elimination requires the full bar."
                    )
                # (a-registry) un-backed elimination: no adjudicated direction.
                if direction not in ADJUDICATED_DIRECTIONS and direction != "supports":
                    flags["a_unbacked_drop"].append(
                        f"`{qid}`/`{hid}`: eliminated with evidence_direction="
                        f"{direction!r} (no adjudicated weakens/discrimination behind the drop)."
                    )

    # (a-timeseries) a total_surviving drop across snapshots must be matched by a
    # rise in total_resolved_out (adjudicated eliminations). A bare drop with no
    # corresponding resolution is the classic Goodhart move.
    for prev, cur in zip(timeseries, timeseries[1:]):
        d_surv = (cur.get("total_surviving") or 0) - (prev.get("total_surviving") or 0)
        d_res = (cur.get("total_resolved_out") or 0) - (prev.get("total_resolved_out") or 0)
        d_init = (cur.get("total_initial") or 0) - (prev.get("total_initial") or 0)
        if d_surv < 0 and d_res <= 0 and d_init <= 0:
            flags["a_unbacked_drop"].append(
                f"time series {prev.get('date')} -> {cur.get('date')}: "
                f"surviving fell by {-d_surv} but resolved_out did not rise "
                f"(delta_resolved_out={d_res}) -- drop is not backed by adjudicated eliminations."
            )
        # (b-timeseries) frozen initial set grew.
        if d_init > 0:
            flags["b_enlargement"].append(
                f"time series {prev.get('date')} -> {cur.get('date')}: "
                f"total_initial grew by {d_init} -- the frozen denominator was enlarged."
            )
    return flags


def render_report(flags: dict, registry: dict, timeseries: list, now: str) -> str:
    total = sum(len(v) for v in flags.values())
    L = []
    L.append("# Hypothesis-Space Integrity Audit (anti-Goodhart)")
    L.append("")
    L.append(f"Generated: {now}")
    L.append("")
    L.append(
        "GENERATED FILE -- do not edit by hand. Advisory, non-blocking sibling of "
        "`check_closure_drift.py`. It audits `hypothesis_space_registry.v1.json` + "
        "`hypothesis_space_timeseries.v1.jsonl` for the three ways the Narrow/Decide "
        "dashboard could be gamed (design rule 5). Flags are review hints, never a gate."
    )
    L.append("")
    n_q = len(registry.get("questions") or [])
    L.append(
        f"Audited **{n_q}** open question(s) across **{len(timeseries)}** time-series "
        f"snapshot(s). **{total}** flag(s) raised."
    )
    L.append("")
    sections = [
        ("a_unbacked_drop", "(a) Un-backed surviving-count drop",
         "A question's surviving count fell with no adjudicated `weakens`/discrimination behind the elimination."),
        ("b_enlargement", "(b) Post-hoc enlargement of a frozen set",
         "The frozen initial enumeration grew, or a hypothesis was pre-registered after its own adjudicating run."),
        ("c_confirmed_no_control", "(c) Confirmed without a passed control",
         "A `confirmed` hypothesis lacks control_passed == true."),
        ("d_bar_violation", "(d) Elimination-bar violation",
         "An `eliminated`/`split` hypothesis is missing part of the bar (met_elimination_bar + control_passed + non_degenerate)."),
    ]
    for key, title, desc in sections:
        items = flags.get(key) or []
        L.append(f"## {title} ({len(items)})")
        L.append("")
        L.append(f"_{desc}_")
        L.append("")
        if not items:
            L.append("_None._")
        else:
            for msg in items:
                L.append(f"- {msg}")
        L.append("")
    L.append("---")
    L.append("")
    L.append(
        "This audit promotes/demotes nothing. Response to any flag is a human decision "
        "at governance (the same handling as `check_closure_drift.py`)."
    )
    L.append("")
    return "\n".join(L) + "\n"


def _self_test() -> int:
    """Synthetic registry exercising each flag exactly once."""
    reg = {"questions": [
        {"qid": "ok_q", "initial_frozen_count": 2, "hypotheses": [
            {"hid": "h1", "pre_registered_utc": "2026-07-01",
             "resolution": {"state": "eliminated", "resolved_utc": "2026-07-05",
                            "evidence_direction": "weakens", "met_elimination_bar": True,
                            "control_passed": True, "non_degenerate": True}},
            {"hid": "h2", "pre_registered_utc": "2026-07-01",
             "resolution": {"state": "confirmed", "resolved_utc": "2026-07-06",
                            "evidence_direction": "supports", "control_passed": True,
                            "non_degenerate": True}},
        ]},
        {"qid": "bad_q", "initial_frozen_count": 3, "hypotheses": [  # (b) count mismatch: 3 vs 2
            {"hid": "b_retro", "pre_registered_utc": "2026-07-10",   # (b) retro-pad
             "resolution": {"state": "eliminated", "resolved_utc": "2026-07-05",
                            "evidence_direction": "supports",         # (a) unbacked
                            "met_elimination_bar": False,             # (d) bar violation
                            "control_passed": False, "non_degenerate": True}},
            {"hid": "c_nocontrol",
             "resolution": {"state": "confirmed", "control_passed": None}},  # (c)
        ]},
    ]}
    ts = [
        {"date": "2026-07-01", "total_surviving": 5, "total_resolved_out": 0, "total_initial": 5},
        {"date": "2026-07-02", "total_surviving": 3, "total_resolved_out": 0, "total_initial": 5},  # (a) unbacked drop
        {"date": "2026-07-03", "total_surviving": 3, "total_resolved_out": 0, "total_initial": 7},  # (b) init grew
    ]
    flags = audit(reg, ts)
    checks = {
        "a_unbacked_drop": flags["a_unbacked_drop"],
        "b_enlargement": flags["b_enlargement"],
        "c_confirmed_no_control": flags["c_confirmed_no_control"],
        "d_bar_violation": flags["d_bar_violation"],
    }
    failures = [k for k, v in checks.items() if not v]
    for k, v in checks.items():
        print(f"  {'ok  ' if v else 'FAIL'} {k}: {len(v)} flag(s)")
    if failures:
        print(f"SELF-TEST FAILED: no flags raised for {failures}")
        return 1
    print("SELF-TEST PASSED")
    return 0


def main() -> int:
    now = _utc_now_iso_z()
    registry = _load_json(REGISTRY)
    if not isinstance(registry, dict):
        print("hypothesis-space integrity: registry missing; nothing to audit.")
        REPORT.write_text(
            f"# Hypothesis-Space Integrity Audit\n\nGenerated: {now}\n\n"
            "_No registry found; nothing to audit._\n", encoding="utf-8")
        return 0
    timeseries = _load_timeseries(TIMESERIES)
    flags = audit(registry, timeseries)
    REPORT.write_text(render_report(flags, registry, timeseries, now), encoding="utf-8")
    total = sum(len(v) for v in flags.values())
    print(f"Hypothesis-space integrity report written: {REPORT.relative_to(REPO_ROOT)}")
    print(f"  flags: a={len(flags['a_unbacked_drop'])} b={len(flags['b_enlargement'])} "
          f"c={len(flags['c_confirmed_no_control'])} d={len(flags['d_bar_violation'])} "
          f"(total={total}, advisory/non-blocking)")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(_self_test())
    try:
        sys.exit(main())
    except Exception as exc:  # pragma: no cover - advisory, never blocks
        print(f"hypothesis-space integrity: non-fatal error ({exc.__class__.__name__}); exiting 0.",
              file=sys.stderr)
        sys.exit(0)
