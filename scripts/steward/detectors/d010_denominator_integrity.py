#!/usr/bin/env python3
"""D-010 -- closure denominator integrity.

THE POINT. D-001 and D-002 find things the closure accounting has dropped. This
one guards the ACCOUNTING ITSELF -- the mechanism that silently dropped SD-031
for ten weeks. It recomputes the V3 closure denominator from first principles,
without importing generate_closure_snapshot.py, and reports every way the real
denominator differs from the one a reader would reasonably assume.

A CORRECTION TO THE OBVIOUS SPEC, because getting this wrong is the whole bug.
The natural one-line statement of the denominator is

    {node : node.status not in DEFERRED_STATUSES and plan.generation == v3}

and it is WRONG. generate_closure_snapshot.py builds the denominator from
`STATUS_WEIGHTS.get(status)` being non-None, and the None-weighted set is a
strict superset of DEFERRED_STATUSES: it also contains assembling,
open_by_design, deferred_v5, parked, parked_indefinite and closed. On the
2026-08-16 tree the true denominator is 117 v3 nodes - 13 deferred - 10
assembling = 94, exactly matching the committed snapshot, where the
DEFERRED_STATUSES-only reading predicts 104. Ten `assembling` nodes are excluded
from the closure percentage by a rule whose name says nothing about them.

That gap is not itself a defect -- excluding assembling work from the % is a
deliberate anti-forcing design choice (see assembly_vs_closure_plan.md). The
defect is that it is INVISIBLE: "deferred" is reported as the exclusion reason in
prose while other statuses are excluded just as silently. So this detector's
standing output is the silent-exclusion surface, which is where the next SD-031
will come from.

CHECKS
  1. structural  -- no non-v3 node inside the denominator; no None-weighted
     status inside it. A violation means the recomputation and the producer
     disagree about the rule itself. P0.
  2. silent exclusion -- statuses excluded from the denominator that are NOT in
     DEFERRED_STATUSES, with the node counts they hide. Standing surface report.
  3. unknown status -- a node status absent from STATUS_WEIGHTS scores 0.0 and
     is counted as unstarted work. That is a guess, not a decision; the closure
     snapshot has been bitten by it before (blocked_pending_substrate, and again
     on 2026-08-13 with closed/parked/pending).
  4. weights drift -- this module's independent STATUS_WEIGHTS copy vs serve.py's
     authoritative CLOSURE_STATUS_WEIGHTS. Independence is the point of the
     detector, so the copy is deliberate and the drift is reported, not absorbed.
  5. snapshot cross-check -- recomputed denominator vs the number committed in
     evidence/planning/closure_status.md.

READ ONLY.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from ._common import (
    DEFAULT_GENERATION,
    DEFERRED_STATUSES,
    STATUS_WEIGHTS,
    Context,
    counts_toward_denominator,
    finding,
)

DETECTOR_ID = "D-010"
DETECTOR_TITLE = "Closure denominator integrity"

_SNAPSHOT_RE = re.compile(
    r"Weighted progress:\s*\*\*([\d.]+)%\*\*\s*across\s*(\d+)\s*non-deferred nodes"
)


def _serve_weights(repo_root: Path):
    """serve.py's authoritative weight table, or None if unavailable."""
    root = str(repo_root)
    added = root not in sys.path
    if added:
        sys.path.insert(0, root)
    try:
        import serve  # type: ignore
        return dict(getattr(serve, "CLOSURE_STATUS_WEIGHTS", {})) or None
    except Exception:
        return None
    finally:
        if added:
            try:
                sys.path.remove(root)
            except ValueError:
                pass


def run(ctx: Context) -> tuple[list[dict], dict]:
    findings: list[dict] = []

    v3_nodes = [n for n in ctx.nodes if n.generation == DEFAULT_GENERATION]
    denom = [n for n in v3_nodes if counts_toward_denominator(n.status)]
    excluded = [n for n in v3_nodes if not counts_toward_denominator(n.status)]

    # --- 1. structural invariants -----------------------------------------
    bad_gen = [n for n in denom if n.generation != DEFAULT_GENERATION]
    bad_weight = [n for n in denom if STATUS_WEIGHTS.get(n.status, 0.0) is None]
    if bad_gen or bad_weight:
        findings.append(finding(
            detector=DETECTOR_ID,
            subject="denominator_invariant",
            title="Closure denominator violates its own construction rule",
            detail=(
                "Recomputed denominator contains %d node(s) of non-v3 generation "
                "and %d node(s) whose status is weight-None (excluded by rule). "
                "The recomputation and generate_closure_snapshot.py disagree "
                "about what the denominator IS, which invalidates the closure "
                "percentage outright."
                % (len(bad_gen), len(bad_weight))
            ),
            severity="P0", confidence=0.99, signal="strong", escalate=True,
            evidence={
                "non_v3_in_denominator": [n.node_id for n in bad_gen],
                "weight_none_in_denominator": [n.node_id for n in bad_weight],
            },
        ))

    # --- 2. silent exclusion surface --------------------------------------
    silent: dict[str, list[str]] = {}
    for n in excluded:
        if n.status not in DEFERRED_STATUSES:
            silent.setdefault(n.status, []).append(n.node_id)
    if silent:
        n_hidden = sum(len(v) for v in silent.values())
        findings.append(finding(
            detector=DETECTOR_ID,
            subject="silent_exclusion_surface",
            title="%d v3 node(s) are excluded from the closure denominator by a "
                  "status that is not 'deferred'" % n_hidden,
            detail=(
                "Statuses excluded from the V3 denominator but absent from "
                "DEFERRED_STATUSES: %s. The closure snapshot reports 'deferred' "
                "as the exclusion reason in prose, so these nodes leave the "
                "denominator without that being stated where the percentage is "
                "read. Excluding them may well be correct (assembling work is "
                "held out by design); the finding is that the exclusion is "
                "unlabelled. This is the surface the next SD-031 comes from."
                % ", ".join("%s=%d" % (k, len(v)) for k, v in sorted(silent.items()))
            ),
            severity="P2", confidence=0.6, signal="weak", escalate=True,
            evidence={"by_status": {k: sorted(v) for k, v in silent.items()},
                      "deferred_statuses": sorted(DEFERRED_STATUSES)},
        ))

    # --- 3. unknown statuses ----------------------------------------------
    unknown: dict[str, list[str]] = {}
    for n in ctx.nodes:
        if n.status not in STATUS_WEIGHTS:
            unknown.setdefault(n.status, []).append(
                "%s:%s" % (n.plan_file, n.node_id))
    if unknown:
        findings.append(finding(
            detector=DETECTOR_ID,
            subject="unknown_status",
            title="%d closure node status string(s) have no weight and score as "
                  "unstarted" % len(unknown),
            detail=(
                "Status(es) %s appear on closure nodes but are absent from "
                "STATUS_WEIGHTS, so they fall through to 0.0 and are counted as "
                "unstarted work regardless of what they mean. Add an explicit "
                "weight (or None to exclude) rather than leaving the default to "
                "decide."
                % ", ".join(sorted(unknown))
            ),
            severity="P1", confidence=0.9, signal="strong", escalate=True,
            evidence={"by_status": {k: sorted(v) for k, v in unknown.items()}},
        ))

    # --- 4. weight table drift vs serve.py --------------------------------
    authoritative = _serve_weights(ctx.repo_root)
    drift_detail = None
    if authoritative:
        diffs = {}
        for k in set(authoritative) | set(STATUS_WEIGHTS):
            a = authoritative.get(k, "<absent>")
            b = STATUS_WEIGHTS.get(k, "<absent>")
            if a != b:
                diffs[k] = {"serve_py": a, "steward": b}
        if diffs:
            drift_detail = diffs
            findings.append(finding(
                detector=DETECTOR_ID,
                subject="weights_drift",
                title="Steward's independent status-weight table has drifted from "
                      "serve.py CLOSURE_STATUS_WEIGHTS",
                detail=(
                    "%d status weight(s) differ between serve.py (authoritative) "
                    "and this detector's deliberately independent copy: %s. The "
                    "copy exists so the denominator can be recomputed without "
                    "trusting the producer, so this is reported rather than "
                    "auto-synced -- but a real weight change upstream must be "
                    "mirrored here or every later denominator check is measured "
                    "against a stale rule."
                    % (len(diffs), ", ".join(sorted(diffs)))
                ),
                severity="P1", confidence=0.9, signal="strong", escalate=True,
                evidence={"diffs": diffs},
            ))

    # --- 5. cross-check against the committed snapshot --------------------
    snap = ctx.repo_root / "evidence" / "planning" / "closure_status.md"
    committed_denom = None
    committed_pct = None
    if snap.exists():
        m = _SNAPSHOT_RE.search(snap.read_text(encoding="utf-8"))
        if m:
            committed_pct = float(m.group(1))
            committed_denom = int(m.group(2))
    if committed_denom is not None and committed_denom != len(denom):
        findings.append(finding(
            detector=DETECTOR_ID,
            subject="snapshot_denominator_mismatch",
            title="Committed closure snapshot denominator (%d) does not match "
                  "recomputation (%d)" % (committed_denom, len(denom)),
            detail=(
                "evidence/planning/closure_status.md states %d non-deferred "
                "nodes; recomputing from plan frontmatter gives %d. Most often "
                "this is simple staleness -- the snapshot is rebuilt by "
                "governance.sh, so plan edits since the last governance run show "
                "up here. Regenerate with scripts/generate_closure_snapshot.py; "
                "if the numbers still differ, the accounting is genuinely broken "
                "and the committed closure percentage is wrong."
                % (committed_denom, len(denom))
            ),
            severity="P2", confidence=0.5, signal="weak", escalate=True,
            evidence={"committed_denominator": committed_denom,
                      "recomputed_denominator": len(denom),
                      "committed_pct": committed_pct},
        ))

    tally: dict[str, int] = {}
    for n in v3_nodes:
        tally[n.status] = tally.get(n.status, 0) + 1

    summary = {
        "detector": DETECTOR_ID,
        "title": DETECTOR_TITLE,
        "n_findings": len(findings),
        "v3_nodes": len(v3_nodes),
        "denominator": len(denom),
        "excluded": len(excluded),
        "committed_denominator": committed_denom,
        "status_tally_v3": dict(sorted(tally.items())),
        "serve_weights_available": bool(authoritative),
        "weights_drift": drift_detail,
    }
    return findings, summary
