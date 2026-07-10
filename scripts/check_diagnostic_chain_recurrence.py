#!/usr/bin/env python3
"""Diagnostic-chain recurrence audit (governance Step 6a-v-ter, GOV-DIAG-1).

The diagnostic-side analog of the re-derive brake / GOV-CEIL-1 ceiling-exhaustion
overlay. Both of those are CLAIM-KEYED: they count confirmed
`failure_autopsy_*.json` verdicts per `claim_id`. A *pure-diagnostic* chain --
one whose targets carry `claim_ids: []` -- accumulates ZERO on that counter, so a
chain of diagnostics circling the same substrate floor never trips the mechanical
brake. It is caught only by a human reading the autopsy stream.

Concrete instance (the validating example): the 4-autopsy chain
V3-EXQ-719a -> 724 -> 732 -> 732a all bottomed out on the same
`f_dominance_conversion_ceiling` / `ree_ai_design_critique_plan:WS-1` competence
floor. 719a was claim-keyed (ARC-062/MECH-309 -> substrate_ceiling; caught by
GOV-CEIL-1). But its pure-diagnostic TAIL -- 724, 732, 732a, all `claim_ids: []`
and `non_contributory` -- was invisible to every claim-keyed counter. 732's
autopsy had to pre-register the recurrence as terminal BY HAND; 732a's honored it
manually. This audit surfaces that pattern MECHANICALLY.

WHAT IS COUNTED. A "diagnostic recurrence hit" (GOV-DIAG-1 definition (a)) is one
confirmed (`status: confirmed`) `failure_autopsy_*.json` target that:

  (i)  carries `claim_ids: []` -- a PURE diagnostic, invisible to the claim-keyed
       re-derive brake and to GOV-CEIL-1 (a claim-tagged diagnostic is ALREADY
       covered by those counters, so counting it here would double-count; it is
       excluded); AND
  (ii) resolved a sub-fork WITHOUT reaching a verdict -- operationalized as
       `recommended_evidence_direction in {non_contributory, inconclusive}`
       (contributed no evidence to any claim, so no substrate question was
       answered). A diagnostic that DID reach a verdict (supports / refutes, or a
       substrate build decision) is NOT a "circling" hit.

Hits are KEYED on the target's `bears_on` work-stream token(s), NOT on claim_id
(the whole point: claim_id is empty). `bears_on` is a string or list of strings
naming the plan work-stream(s) / competence-gap(s) the diagnostic circles --
e.g. `ree_ai_design_critique_plan:WS-1` (a plan work-stream) or
`f_dominance_conversion_ceiling` (a named competence gap). Each token gets one hit
per (artifact stem, run_id) so re-listing a token across an artifact's targets
does not inflate the count.

THE OVERLAY (ACTIONABLE, warn-only). When a `bears_on` token reaches
N (DIAG_RECURRENCE_N, default 3) distinct pure-diagnostic no-verdict hits, the
chain is surfaced with the reading: **"diagnostic-chain recurrence -- the question
may be MIS-POSED, not under-powered."** The recommended response is to RE-POSE the
question (fix the operationalization / measurement), NOT to re-run it harder. This
mirrors 732a's own learning #4 ("a diagnostic chain that keeps resolving sub-forks
without reaching a verdict is telling you the question is mis-posed, not
under-powered"). Detection is automatic; the response is a human governance
decision at Step 6a-v-ter. Absent a `bears_on`-tagged corpus every count is 0, so
a missing / untagged corpus can never mass-surface (same non-falsifying-safe
posture as GOV-CEIL-1).

This audit READS ONLY and PROMOTES / DEMOTES NOTHING. It surfaces a pattern for a
human to route (typically to /governance for a re-operationalization decision, or
to refuse a same-question re-queue in the re-derive brake's spirit). It does not
touch claims.yaml.

Usage:
  python3 scripts/check_diagnostic_chain_recurrence.py            # human report, exit 0
  python3 scripts/check_diagnostic_chain_recurrence.py --strict   # exit 1 if any recurrence
  python3 scripts/check_diagnostic_chain_recurrence.py --json     # machine-readable
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_AUTOPSY_DIR = REPO_ROOT / "evidence" / "planning"

# GOV-DIAG-1 (diagnostic-chain recurrence rule). N distinct confirmed
# pure-diagnostic (claim_ids=[]) no-verdict autopsy targets sharing one bears_on
# work-stream token is enough for "the question may be mis-posed, not
# under-powered" to earn a surface. Matches GOV-CEIL-1's N=3 precedent. Tunable.
DIAG_RECURRENCE_N = 3

# A diagnostic "did not reach a verdict" when it contributed no evidence to any
# claim. non_contributory is the canonical value; inconclusive is its softer
# sibling. supports / refutes / weakens / etc. mean a verdict WAS reached -- not a
# circling hit.
NO_VERDICT_DIRECTIONS = {"non_contributory", "inconclusive"}


def _tokens(value) -> list[str]:
    """Normalize a bears_on field (str | list | None) to a list of clean tokens."""
    if value is None:
        return []
    if isinstance(value, str):
        items = [value]
    elif isinstance(value, (list, tuple)):
        items = list(value)
    else:
        items = [value]
    return [str(x).strip() for x in items if str(x).strip()]


def count_recurrence_hits(autopsy_dir: Path) -> dict[str, dict]:
    """Count pure-diagnostic no-verdict autopsy targets per bears_on token.

    Returns {token: {"n_hits": int, "hits": [(artifact_stem, run_id), ...]}} where
    each hit is a distinct (artifact stem, run_id) so re-listing a token across an
    artifact's targets does not inflate the count. Only confirmed autopsies with
    `claim_ids: []` AND a no-verdict `recommended_evidence_direction` contribute.
    """
    hits: dict[str, set] = {}
    if not autopsy_dir.is_dir():
        return {}
    for fp in sorted(autopsy_dir.glob("failure_autopsy_*.json")):
        try:
            data = json.loads(fp.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        if str(data.get("status", "")).strip().lower() != "confirmed":
            continue
        for tgt in (data.get("targets") or []):
            # (i) PURE diagnostic -- claim_ids must be present-and-empty. A
            # claim-tagged target is caught by the claim-keyed brake / GOV-CEIL-1;
            # counting it here would double-count. A missing claim_ids field is
            # NOT treated as empty (conservative -- only an explicit [] qualifies).
            if "claim_ids" not in tgt:
                continue
            if tgt.get("claim_ids"):  # non-empty list -> claim-keyed, excluded
                continue
            # (ii) resolved without reaching a verdict.
            direction = str(tgt.get("recommended_evidence_direction", "")).strip().lower()
            if direction not in NO_VERDICT_DIRECTIONS:
                continue
            run_key = str(tgt.get("run_id") or tgt.get("queue_id") or fp.stem)
            for tok in _tokens(tgt.get("bears_on")):
                hits.setdefault(tok, set()).add((fp.stem, run_key))
    return {
        tok: {"n_hits": len(keys), "hits": sorted(keys)}
        for tok, keys in hits.items()
    }


def audit(recurrence_hits: dict[str, dict],
          n: int = DIAG_RECURRENCE_N) -> list[dict]:
    """Return the ACTIONABLE recurrence overlay: tokens with n_hits >= n.

    Each record: {token, n_hits, chain (run_ids), artifacts (stems)}. Sorted by
    descending hit count. Empty when nothing reaches the threshold.
    """
    flagged = []
    for tok, rec in recurrence_hits.items():
        if rec["n_hits"] >= n:
            flagged.append({
                "bears_on": tok,
                "n_hits": rec["n_hits"],
                "chain": [run for (_stem, run) in rec["hits"]],
                "artifacts": [stem for (stem, _run) in rec["hits"]],
            })
    flagged.sort(key=lambda r: -r["n_hits"])
    return flagged


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--autopsy-dir", type=Path, default=DEFAULT_AUTOPSY_DIR,
                    help="dir of failure_autopsy_*.json for the GOV-DIAG-1 hit count")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any diagnostic-chain recurrence is flagged")
    args = ap.parse_args()

    recurrence_hits = count_recurrence_hits(args.autopsy_dir)
    flagged = audit(recurrence_hits, n=DIAG_RECURRENCE_N)

    if args.json:
        print(json.dumps({
            "diag_recurrence_n": DIAG_RECURRENCE_N,
            "n_work_streams_seen": len(recurrence_hits),
            "recurrence_flagged": flagged,
            "all_counts": {
                tok: rec["n_hits"] for tok, rec in sorted(recurrence_hits.items())
            },
        }, indent=2))
    else:
        n_ws = len(recurrence_hits)
        n_flag = len(flagged)
        print("Diagnostic-chain recurrence audit (GOV-DIAG-1): "
              f"{n_ws} bears_on work-stream(s) carry pure-diagnostic "
              "(claim_ids=[]) no-verdict autopsies")
        print(f"  diagnostic-chain recurrence N>={DIAG_RECURRENCE_N} (ACTIONABLE): {n_flag}")
        if n_flag:
            print("  -- RECURRENCE: surface to user -- the question may be MIS-POSED,")
            print("     not under-powered. Re-pose (fix the operationalization);")
            print("     refuse a same-question re-queue in the re-derive brake's spirit:")
            for rec in flagged:
                print(f"    [recurrence] {rec['bears_on']} -- {rec['n_hits']} "
                      f"pure-diagnostic no-verdict hits")
                print(f"        chain: {' -> '.join(rec['chain'])}")
        else:
            print(f"  -- no diagnostic-chain recurrence (none at >={DIAG_RECURRENCE_N} "
                  "pure-diagnostic no-verdict hits on one work-stream).")

    if args.strict and flagged:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
