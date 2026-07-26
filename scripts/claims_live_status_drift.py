#!/usr/bin/env python3
"""claims_live_status_drift.py -- detect drift between a claim's STORED `live_status`
block and the value re-derived from its current fields right now (SHP-4 of the
status/history plane-separation design,
evidence/planning/status_history_plane_separation_design.md Sec.4b + Sec.7).

Mirror of scripts/claims_doc_drift.py (SHP-5, doc-status plane) and the status-plane
section of scripts/check_closure_drift.py (SHP-2, closure-plan plane), for the claims
registry. `live_status` is a pure projection over each claim's own current-state fields
(`status` + `v3_pending` + `epistemic_category`), so it must be re-stamped whenever those
move. This checker re-derives every claim's `live_status` and flags any whose STORED
block has gone stale vs the derivation -- exactly the rot a status-plane field accumulates
if the registry moves and the stamper is not re-run.

Resolution + derivation are single-sourced from scripts/apply_live_status.py (the stamper),
so this checker and the stamper can never disagree about the derived reading -- the "two
implementations drift apart" trap check_closure_drift.py's own docstring warns about.

Buckets (mirrors the closure-drift / claims-doc-drift split):

  1. Reading drift (HARD).  A claim carries a stored `live_status.reading` (or
     `needs_review`) that != the value re-derived from the claim now. In a healthy
     pipeline the stamper runs immediately before this check, so this bucket is empty; a
     non-empty bucket means the claim's status/gate fields moved and `apply_live_status.py`
     was not re-run (or the block was hand-edited). This is the only bucket `--strict`
     fails on.

  2. Unstamped (SOFT).  A registered claim has no `live_status` block yet -- run
     scripts/apply_live_status.py. Not a --strict failure (the stamper just has not run).

  3. Internal-inconsistency (REVIEW).  A claim whose re-derived `needs_review` is true:
     its own current-state fields contradict each other (a promoted status still carrying
     the V3-pending gate, or a promoted status tagged substrate_ceiling). Surfaced for a
     human glance; never a gate. (These overlap the HARD bucket only if the stored
     needs_review also drifted; otherwise they are correctly-stamped-but-worth-reviewing.)

  4. Event-provenance drift (SOFT).  The SHP-4 `live_status.evidence` sub-block (`from` /
     `as_of` / `verdict`, projected from the event log via project_status_head) no longer
     matches the freshly re-projected head -- a newer autopsy / PASS manifest / decision
     landed since the stamper last ran. Fluctuates legitimately as the fleet produces
     evidence, so it is NEVER a --strict failure; re-run apply_live_status.py to refresh.

  5. Never-reviewed (INFO).  A claim with no `last_reviewed` history value -- has not been
     reviewed under the history plane yet. Listed as a count + sample for visibility only;
     `last_reviewed` is record-once and legitimately absent for most claims.

Output: evidence/planning/claims_live_status_drift.md (+ .json sidecar). Exit 0 by default
(warn-only, like claims_doc_drift.py / check_closure_drift.py); `--strict` exits 1 when any
HARD reading drift is present.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/claims_live_status_drift.py           # warn-only
    /opt/local/bin/python3 scripts/claims_live_status_drift.py --strict   # exit 1 on hard drift
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
PLANNING_DIR = REPO_ROOT / "evidence" / "planning"
DRIFT_REPORT = PLANNING_DIR / "claims_live_status_drift.md"
DRIFT_JSON = PLANNING_DIR / "claims_live_status_drift.json"

# Single-source the derivation from the stamper.
sys.path.insert(0, str(SCRIPTS_DIR))
try:
    import apply_live_status as als  # noqa: E402
except ImportError as exc:  # pragma: no cover
    print(f"ERROR: cannot import scripts/apply_live_status.py: {exc}", file=sys.stderr)
    sys.exit(0)


def _stored_live_status(claim):
    """The claim's stored live_status block as (reading, needs_review) or None if absent."""
    ls = claim.get("live_status")
    if not isinstance(ls, dict):
        return None
    return (
        None if ls.get("reading") is None else str(ls.get("reading")),
        bool(ls.get("needs_review")),
    )


def _stored_evidence(claim):
    """The claim's stored live_status.evidence sub-block as (from, as_of, verdict), or None
    if absent -- the SHP-4 event-provenance augmentation."""
    ls = claim.get("live_status")
    if not isinstance(ls, dict):
        return None
    ev = ls.get("evidence")
    if not isinstance(ev, dict):
        return None
    return (
        None if ev.get("from") is None else str(ev.get("from")),
        None if ev.get("as_of") is None else str(ev.get("as_of")),
        None if ev.get("verdict") is None else str(ev.get("verdict")),
    )


def scan():
    registry = als.load_registry()
    reading_drift = []
    unstamped = []
    needs_review = []
    never_reviewed = []
    provenance_drift = []

    # Re-project event-stream provenance ONCE (reuses the stamper's build_provenance, which
    # reuses project_status_head's ONE projection path). {} when the projector is unavailable.
    derived_prov = als.build_provenance(registry.keys())
    provenance_available = als._psh is not None

    for cid, claim in registry.items():
        derived_reading = als.derive_reading(claim)
        derived_nr, derived_reasons = als.derive_needs_review(claim)

        if derived_nr:
            needs_review.append({"claim": cid, "reasons": derived_reasons,
                                 "reading": derived_reading})
        if not claim.get("last_reviewed"):
            never_reviewed.append(cid)

        # Provenance drift (SOFT): stored live_status.evidence != freshly-re-projected head.
        # Fluctuates legitimately as new events land between stamps, so it is NEVER a --strict
        # failure -- it just tells the operator to re-run apply_live_status.py.
        if provenance_available:
            stored_ev = _stored_evidence(claim)
            der = derived_prov.get(cid)
            der_tuple = (der["from"], der["as_of"], der["verdict"]) if der else None
            if stored_ev != der_tuple:
                provenance_drift.append({
                    "claim": cid,
                    "stored_from": (stored_ev[0] if stored_ev else None),
                    "derived_from": (der_tuple[0] if der_tuple else None),
                })

        stored = _stored_live_status(claim)
        if stored is None:
            unstamped.append({"claim": cid, "would_derive": derived_reading})
            continue

        stored_reading, stored_nr = stored
        diffs = []
        if stored_reading != derived_reading:
            diffs.append(f"reading: stored={stored_reading!r} derived={derived_reading!r}")
        if stored_nr != derived_nr:
            diffs.append(f"needs_review: stored={stored_nr} derived={derived_nr}")
        if diffs:
            reading_drift.append({
                "claim": cid, "stored_reading": stored_reading,
                "derived_reading": derived_reading, "diffs": diffs,
            })

    return {
        "total": len(registry),
        "reading_drift": reading_drift,
        "unstamped": unstamped,
        "needs_review": needs_review,
        "never_reviewed": never_reviewed,
        "provenance_drift": provenance_drift,
        "provenance_available": provenance_available,
    }


def render_report(r, now_iso):
    lines = []
    lines.append("# Claims live_status Drift Report")
    lines.append("")
    lines.append(f"Generated: {now_iso}")
    lines.append("")
    lines.append(
        "Mirror of the closure-plan / claims-doc drift reports, for the claims registry's "
        "`live_status` status plane (SHP-4). Flags claims whose stored `live_status` block "
        "has fallen out of step with the value re-derived from the claim's own current "
        "fields (`status` + `v3_pending` + `epistemic_category`). Resolution + derivation "
        "are shared with `scripts/apply_live_status.py`. Only the **Reading drift** bucket "
        "is a hard signal (fails `--strict`); the rest are review/info hints."
    )
    lines.append("")
    lines.append("Warn-only by default -- run with `--strict` for a blocking gate.")
    lines.append("")
    lines.append(f"Claims in registry: {r['total']}")
    lines.append("")

    rd = r["reading_drift"]
    lines.append(f"## Reading drift -- HARD ({len(rd)})")
    lines.append("")
    lines.append(
        "Stored `live_status` != re-derived value. Re-run `scripts/apply_live_status.py`; "
        "if it persists, the block was hand-edited or the claim's fields changed without a "
        "re-stamp."
    )
    lines.append("")
    if not rd:
        lines.append("_None._")
        lines.append("")
    else:
        lines.append("| claim | stored reading | derived reading | drifted fields |")
        lines.append("|-------|----------------|-----------------|----------------|")
        for f in rd:
            lines.append("| {claim} | `{sr}` | `{dr}` | {fields} |".format(
                claim=f["claim"], sr=f["stored_reading"], dr=f["derived_reading"],
                fields="; ".join(f["diffs"])))
        lines.append("")

    us = r["unstamped"]
    lines.append(f"## Unstamped -- SOFT ({len(us)})")
    lines.append("")
    lines.append("Registered claims with no `live_status` block. Run "
                 "`scripts/apply_live_status.py`.")
    lines.append("")
    if not us:
        lines.append("_None._")
        lines.append("")
    else:
        lines.append("| claim | would-derive |")
        lines.append("|-------|--------------|")
        for u in us[:60]:
            lines.append("| {claim} | `{wd}` |".format(
                claim=u["claim"], wd=u.get("would_derive") or "(undeterminable)"))
        if len(us) > 60:
            lines.append(f"| ... | (+{len(us) - 60} more) |")
        lines.append("")

    nr = r["needs_review"]
    lines.append(f"## Internal inconsistency -- REVIEW ({len(nr)})")
    lines.append("")
    lines.append(
        "Claims whose own current-state fields contradict each other (`needs_review` "
        "true): a promoted status still carrying the V3-pending gate, or a promoted status "
        "tagged `substrate_ceiling` (GOV-CEIL-1 floors ceilings to candidate). The derived "
        "`live_status` is a best-effort; a human should reconcile the fields."
    )
    lines.append("")
    if not nr:
        lines.append("_None._")
        lines.append("")
    else:
        lines.append("| claim | derived reading | why |")
        lines.append("|-------|-----------------|-----|")
        for n in nr:
            lines.append("| {claim} | `{rd}` | {why} |".format(
                claim=n["claim"], rd=n["reading"], why="; ".join(n["reasons"])))
        lines.append("")

    pd = r.get("provenance_drift", [])
    lines.append(f"## Event-provenance drift -- SOFT ({len(pd)})")
    lines.append("")
    lines.append(
        "The `live_status.evidence` sub-block (SHP-4 augmentation: `from` / `as_of` / "
        "`verdict`) is projected from the append-only event log via project_status_head. "
        "This flags claims whose stored `evidence` block no longer matches the freshly "
        "re-projected head -- i.e. a newer autopsy / PASS manifest / decision landed (or one "
        "changed) since `apply_live_status.py` last ran. It fluctuates legitimately as the "
        "fleet produces evidence, so it is **warn-only and never a --strict failure**: re-run "
        "`scripts/apply_live_status.py` (under a TASK_CLAIMS claim on docs/claims/claims.yaml) "
        "to refresh. Reading drift (HARD, above) is the gate; provenance drift is a hint."
    )
    lines.append("")
    if not r.get("provenance_available", True):
        lines.append("_Skipped: project_status_head unavailable -- provenance not projected._")
        lines.append("")
    elif not pd:
        lines.append("_None -- every stamped `evidence` block matches its re-projection._")
        lines.append("")
    else:
        lines.append("| claim | stored evidence.from | re-projected from |")
        lines.append("|-------|----------------------|-------------------|")
        for f in pd[:60]:
            lines.append("| {claim} | `{sf}` | `{df}` |".format(
                claim=f["claim"], sf=f["stored_from"] or "_none_",
                df=f["derived_from"] or "_none_"))
        if len(pd) > 60:
            lines.append(f"| ... | | (+{len(pd) - 60} more) |")
        lines.append("")

    nv = r["never_reviewed"]
    lines.append(f"## Never reviewed (no `last_reviewed`) -- INFO ({len(nv)} of {r['total']})")
    lines.append("")
    lines.append(
        "Claims with no `last_reviewed` history value -- not yet reviewed under the history "
        "plane. `last_reviewed` is record-once and legitimately absent for most claims "
        "(seeded from `adjudicated_at_utc`, or set with "
        "`apply_live_status.py --mark-reviewed <ID>`). Count + sample only."
    )
    lines.append("")
    if not nv:
        lines.append("_None -- every claim carries a last_reviewed._")
    else:
        sample = ", ".join(nv[:20])
        lines.append(f"Sample: {sample}" + (" ..." if len(nv) > 20 else ""))
    lines.append("")

    return "\n".join(lines) + "\n"


def main():
    strict = "--strict" in sys.argv[1:]
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    r = scan()

    PLANNING_DIR.mkdir(parents=True, exist_ok=True)
    DRIFT_REPORT.write_text(render_report(r, now_iso), encoding="utf-8")
    payload = {
        "generated_at": now_iso,
        "counts": {
            "total": r["total"],
            "reading_drift": len(r["reading_drift"]),
            "unstamped": len(r["unstamped"]),
            "needs_review": len(r["needs_review"]),
            "never_reviewed": len(r["never_reviewed"]),
            "provenance_drift": len(r.get("provenance_drift", [])),
        },
        "reading_drift": r["reading_drift"],
        "unstamped": r["unstamped"],
        "needs_review": r["needs_review"],
        "never_reviewed": r["never_reviewed"],
        "provenance_drift": r.get("provenance_drift", []),
        "provenance_available": r.get("provenance_available", True),
    }
    DRIFT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print(f"Claims live_status drift report written: {DRIFT_REPORT.relative_to(REPO_ROOT)}")
    print("  reading_drift={rd}  provenance_drift={pd}  unstamped={us}  needs_review={nr}  "
          "never_reviewed={nv}/{tot}".format(
              rd=len(r["reading_drift"]), pd=len(r.get("provenance_drift", [])),
              us=len(r["unstamped"]), nr=len(r["needs_review"]),
              nv=len(r["never_reviewed"]), tot=r["total"]))

    if strict and r["reading_drift"]:
        print(f"STRICT: {len(r['reading_drift'])} hard reading-drift claim(s).", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
