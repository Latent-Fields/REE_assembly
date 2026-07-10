#!/usr/bin/env python3
"""claims_doc_drift.py -- detect drift between an architecture doc's status and
docs/claims/claims.yaml (SHP-5 of the status/history plane-separation design).

Mirror of scripts/check_closure_drift.py, for the doc-status plane instead of the
closure-plan plane. It flags architecture docs whose recorded status has fallen out
of step with the claims registry -- the class of rot the hand-typed `**Status:**`
body lines accumulate silently (confirmed live 2026-07-10: sd_063_*.md still asserted
"v3_pending" though SD-063 had been promoted provisional / v3_pending:false).

Resolution + derivation are single-sourced from docs/apply_status_frontmatter.py (the
stamper), so this checker and the stamper can never disagree about which claim a doc
maps to or what its derived status is -- exactly the "two implementations drift apart"
trap that check_closure_drift.py's own docstring warns about.

Buckets (mirrors the closure-drift report's Drifted / Suppressed / Stale split):

  1. Frontmatter drift (HARD).  A doc carries a stamped `status:` frontmatter value
     that != the value re-derived from claims.yaml right now. In a healthy pipeline the
     stamper runs immediately before this check, so this bucket is empty; a non-empty
     bucket means claims.yaml moved and the doc was not re-stamped, or the frontmatter
     was hand-edited. This is the only bucket `--strict` fails on.

  2. Unstamped-but-resolvable (SOFT).  A doc resolves to a registered claim but has no
     `status:` frontmatter yet -- run docs/apply_status_frontmatter.py. Not a --strict
     failure (it just means the stamper has not run on this tree).

  3. Hand-line contradiction (REVIEW).  A doc still carries a hand-typed `**Status:**`
     body line whose epistemic status word, or its v3_pending assertion, contradicts
     the registry. These are the residual prose lines the stamper deliberately did NOT
     retire (non-destructive razor); they want a human to lift/rewrite. Review hint,
     never a gate.

  4. Unresolved-with-status (INFO).  A doc has a hand `**Status:**` line but names no
     derivable claim id -- outside the stamper's reach; listed for visibility only.

Output: evidence/planning/claims_doc_drift.md (+ .json sidecar). Exit 0 by default
(warn-only, like check_closure_drift.py); `--strict` exits 1 when any HARD frontmatter
drift is present.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/claims_doc_drift.py            # warn-only
    /opt/local/bin/python3 scripts/claims_doc_drift.py --strict    # exit 1 on hard drift
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"
PLANNING_DIR = REPO_ROOT / "evidence" / "planning"
DRIFT_REPORT = PLANNING_DIR / "claims_doc_drift.md"
DRIFT_JSON = PLANNING_DIR / "claims_doc_drift.json"

# Single-source the resolution + derivation from the stamper.
sys.path.insert(0, str(DOCS_DIR))
try:
    import apply_status_frontmatter as asf  # noqa: E402
except ImportError as exc:  # pragma: no cover
    print(f"ERROR: cannot import docs/apply_status_frontmatter.py: {exc}", file=sys.stderr)
    sys.exit(0)

# Epistemic status words only. "implemented" is a BUILD-state word orthogonal to the
# registry's epistemic status, so a hand "IMPLEMENTED" against a registry "provisional"
# is NOT a contradiction -- excluded here to avoid drowning the review bucket in noise.
EPISTEMIC_WORDS = {
    "candidate", "provisional", "active", "open", "stable", "legacy",
    "resolved", "superseded", "retired", "retiring",
}
_V3_PENDING_RE = re.compile(r"v3[_ -]pending", re.IGNORECASE)
# a nearby "false"/"off"/"cleared" negates the pending assertion (e.g. `v3_pending: false`)
_V3_PENDING_NEGATED_RE = re.compile(r"v3[_ -]pending\W{0,3}(?:[:=]\s*)?(?:false|off|cleared)",
                                    re.IGNORECASE)


def handline_contradictions(status_body: str, claim: dict) -> list[str]:
    """Reasons a residual hand **Status:** line contradicts the registry (may be empty)."""
    reasons: list[str] = []
    low = status_body.lower()
    reg_status = str(claim.get("status") or "").strip().lower()
    v3p = claim.get("v3_pending") is True

    hand_words = {t for t in re.split(r"[\s,/`*_().;:]+", low) if t} & EPISTEMIC_WORDS
    if hand_words and reg_status in EPISTEMIC_WORDS and reg_status not in hand_words:
        reasons.append(
            "hand line says {}; registry status is {}".format(
                "/".join(sorted(hand_words)), reg_status))

    if _V3_PENDING_RE.search(low) and not _V3_PENDING_NEGATED_RE.search(low) and not v3p:
        reasons.append("hand line asserts v3_pending but registry v3_pending is not set")
    return reasons


def scan() -> dict:
    registry = asf.load_registry()
    frontmatter_drift: list[dict] = []
    unstamped: list[dict] = []
    handline_review: list[dict] = []
    unresolved_with_status: list[dict] = []
    resolved = 0

    for path in asf.iter_arch_docs():
        basename = os.path.basename(path)
        text = Path(path).read_text(encoding="utf-8")
        cid, method = asf.resolve_claim_id(basename, text, registry)
        status_line = asf.STATUS_LINE_RE.search(text)

        if cid is None:
            if status_line:
                unresolved_with_status.append({
                    "doc": basename,
                    "hand_status": status_line.group(1).strip()[:120],
                })
            continue

        resolved += 1
        claim = registry[cid]
        derived = asf.derive_status(claim)

        fm_lines, _body = asf.split_frontmatter(text)
        stamped = asf.existing_status_fields(fm_lines).get("status")

        if stamped is None:
            unstamped.append({"doc": basename, "claim": cid, "derived": derived})
        elif stamped != derived:
            frontmatter_drift.append({
                "doc": basename, "claim": cid,
                "stamped": stamped, "derived": derived,
            })

        # Residual hand-line contradiction (independent of frontmatter state).
        if status_line:
            reasons = handline_contradictions(status_line.group(1), claim)
            if reasons:
                handline_review.append({
                    "doc": basename, "claim": cid,
                    "hand_status": status_line.group(1).strip()[:120],
                    "reasons": reasons,
                })

    return {
        "resolved": resolved,
        "frontmatter_drift": frontmatter_drift,
        "unstamped": unstamped,
        "handline_review": handline_review,
        "unresolved_with_status": unresolved_with_status,
    }


def render_report(r: dict, now_iso: str) -> str:
    lines: list[str] = []
    lines.append("# Claims-Doc Status Drift Report")
    lines.append("")
    lines.append(f"Generated: {now_iso}")
    lines.append("")
    lines.append(
        "Mirror of the closure-plan drift report, for architecture docs. Flags docs "
        "whose status has fallen out of step with `docs/claims/claims.yaml`. "
        "Resolution + derivation are shared with `docs/apply_status_frontmatter.py`. "
        "Only the **Frontmatter drift** bucket is a hard signal (fails `--strict`); "
        "the rest are review/info hints."
    )
    lines.append("")
    lines.append("Warn-only by default -- run with `--strict` for a blocking gate.")
    lines.append("")
    lines.append(f"Docs resolved to a claim: {r['resolved']}")
    lines.append("")

    fd = r["frontmatter_drift"]
    lines.append(f"## Frontmatter drift -- HARD ({len(fd)})")
    lines.append("")
    lines.append(
        "Stamped `status:` frontmatter != the value re-derived from claims.yaml now. "
        "Re-run `docs/apply_status_frontmatter.py`; if it persists, the frontmatter "
        "was hand-edited or claims.yaml changed without a governance run."
    )
    lines.append("")
    if not fd:
        lines.append("_None._")
        lines.append("")
    else:
        lines.append("| doc | claim | stamped | derived (claims.yaml) |")
        lines.append("|-----|-------|---------|-----------------------|")
        for f in fd:
            lines.append("| {doc} | {claim} | `{stamped}` | `{derived}` |".format(**f))
        lines.append("")

    us = r["unstamped"]
    lines.append(f"## Unstamped but resolvable -- SOFT ({len(us)})")
    lines.append("")
    lines.append("Docs that resolve to a registered claim but have no `status:` "
                 "frontmatter. Run `docs/apply_status_frontmatter.py`.")
    lines.append("")
    if not us:
        lines.append("_None._")
        lines.append("")
    else:
        lines.append("| doc | claim | would-derive |")
        lines.append("|-----|-------|--------------|")
        for u in us:
            lines.append("| {doc} | {claim} | `{derived}` |".format(**u))
        lines.append("")

    hr = r["handline_review"]
    lines.append(f"## Hand-line contradiction -- REVIEW ({len(hr)})")
    lines.append("")
    lines.append(
        "Residual hand-typed `**Status:**` lines (the stamper leaves prose lines in "
        "place per the non-destructive razor) whose epistemic status word or "
        "v3_pending assertion contradicts the registry. Lift/rewrite by hand, then "
        "the frontmatter carries the machine-checkable truth."
    )
    lines.append("")
    if not hr:
        lines.append("_None._")
        lines.append("")
    else:
        lines.append("| doc | claim | hand **Status:** line | why |")
        lines.append("|-----|-------|-----------------------|-----|")
        for h in hr:
            lines.append("| {doc} | {claim} | {hand} | {why} |".format(
                doc=h["doc"], claim=h["claim"],
                hand=h["hand_status"].replace("|", "\\|"),
                why="; ".join(h["reasons"])))
        lines.append("")

    uw = r["unresolved_with_status"]
    lines.append(f"## Unresolved with a hand status line -- INFO ({len(uw)})")
    lines.append("")
    lines.append("Docs with a hand `**Status:**` line but no derivable claim id "
                 "(no `**Claim:**` line, no registered filename stem). Outside the "
                 "stamper's reach; listed for visibility only.")
    lines.append("")
    if not uw:
        lines.append("_None._")
        lines.append("")
    else:
        for u in uw:
            lines.append("- `{doc}` -- \"{hand}\"".format(
                doc=u["doc"], hand=u["hand_status"]))
        lines.append("")

    return "\n".join(lines) + "\n"


def main() -> int:
    strict = "--strict" in sys.argv[1:]
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    r = scan()

    PLANNING_DIR.mkdir(parents=True, exist_ok=True)
    DRIFT_REPORT.write_text(render_report(r, now_iso), encoding="utf-8")
    payload = {"generated_at": now_iso, "counts": {
        "resolved": r["resolved"],
        "frontmatter_drift": len(r["frontmatter_drift"]),
        "unstamped": len(r["unstamped"]),
        "handline_review": len(r["handline_review"]),
        "unresolved_with_status": len(r["unresolved_with_status"]),
    }, **{k: r[k] for k in
          ("frontmatter_drift", "unstamped", "handline_review", "unresolved_with_status")}}
    DRIFT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print(f"Claims-doc drift report written: {DRIFT_REPORT.relative_to(REPO_ROOT)}")
    print("  frontmatter_drift={fd}  unstamped={us}  handline_review={hr}  "
          "unresolved_with_status={uw}".format(
              fd=len(r["frontmatter_drift"]), us=len(r["unstamped"]),
              hr=len(r["handline_review"]), uw=len(r["unresolved_with_status"])))

    if strict and r["frontmatter_drift"]:
        print(f"STRICT: {len(r['frontmatter_drift'])} hard frontmatter-drift doc(s).",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
