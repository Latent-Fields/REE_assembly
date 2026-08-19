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
     DEFERRED_STATUSES and are NOT LABELLED by the snapshot where the percentage
     is read. Standing surface report. See "CYCLE-1 REFINEMENT" below.
  3. unknown status -- a node status absent from STATUS_WEIGHTS scores 0.0 and
     is counted as unstarted work. That is a guess, not a decision; the closure
     snapshot has been bitten by it before (blocked_pending_substrate, and again
     on 2026-08-13 with closed/parked/pending).
  4. weights drift -- this module's independent STATUS_WEIGHTS copy vs serve.py's
     authoritative CLOSURE_STATUS_WEIGHTS. Independence is the point of the
     detector, so the copy is deliberate and the drift is reported, not absorbed.
  5. snapshot cross-check -- recomputed denominator vs the number committed in
     evidence/planning/closure_status.md.

CYCLE-1 REFINEMENT (2026-08-18) -- both standing findings adjudicated.
=====================================================================
CHECK 2 was a FALSE POSITIVE as written. Its detail asserted the exclusion is
"unlabelled", and for `assembling` that has not been true since the snapshot
grew its Assembly-frontier block: closure_status.md states the count two lines
under the percentage ("a SEPARATE axis, not counted in the % above") and again
as a dedicated section listing all ten nodes. The check asserted a property it
never measured. It now MEASURES it -- EXCLUSION_LABELS maps an excluded status
to the marker the snapshot uses, and a status counts as labelled only when that
marker is present AND the count it states matches. Absent marker, wrong count,
or an unreadable snapshot all read as UNLABELLED, so the failure direction is
loud. A suppression was rejected: `subject` was a constant, so any suppression
narrow enough to be honest was impossible to write -- it would have muted the
check for `parked` / `closed` / `deferred_v5` too, which really would be silent.
The subject now carries the status set for the same reason D-007's carries its
gate set: a NEW unlabelled status is a different finding_id and escalates on its
own merits rather than inheriting an old disposition.

CHECK 5 conflated two failures with opposite urgency under one finding_id. A
mismatch is nearly always REGEN LAG (plan edits since the last governance run;
the snapshot is rebuilt at governance.sh Step 3c-bis) and self-heals. It is
occasionally the accounting genuinely breaking, which is a P1 nobody should have
to dig for. THE SNAPSHOT DISCRIMINATES ITSELF, exactly and with no dates or git:
it commits its own per-status tally. Tally differs from the recomputation ->
the snapshot was built from different inputs -> lag, and the specific statuses
that moved are named. Tally IDENTICAL but denominator differs -> same inputs,
different answer -> the denominator RULE has diverged from the producer, which
is the accounting breaking. Measured on origin/master e0c9901eac: committed
denominator 94 vs recomputed 95, committed tally blocked=11 deferred=13 done=62
open=8 vs recomputed blocked=12 deferred=12 done=63 open=7 -- lag, and a clean
`generate_closure_snapshot.py` run moved it to 95 / 72.3%, confirming it.

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
# T2: this detector reports a verdict on the accounting mechanism itself
# (structural invariants, the silent-exclusion surface, weight drift, snapshot
# lag) rather than a defect a human or model adjudicates per-instance -- action
# on any of it is taken elsewhere (governance.sh regen, or a
# generate_closure_snapshot.py / _common.py edit). The original spec in
# docs/DETECTORS.md called this "T0-assert"; that is not a value
# _common.finding() accepts, and the doc's own AS-BUILT note (2026-08-16)
# already corrects it: "Emitted tier is T2, not T0-assert." This was already
# T2 by way of _common.finding()'s default (never overridden), which happened
# to match; made explicit here so it no longer depends on that default -- see
# chip-20260817-steward-emitted-tier-vs-designed-tier.
TIER = "T2"

_SNAPSHOT_RE = re.compile(
    r"Weighted progress:\s*\*\*([\d.]+)%\*\*\s*across\s*(\d+)\s*non-deferred nodes"
)
# The snapshot's own per-status tally line, and the "## Overall" block it sits
# in. Check 5 uses the tally as an exact lag discriminator; check 2 reads the
# Overall block because that is where a reader meets the percentage -- a label
# buried further down the file does not stop the percentage being misread.
_OVERALL_RE = re.compile(r"^##\s+Overall\s*$(.*?)(?=^##\s)", re.M | re.S)
_TALLY_RE = re.compile(r"^-\s*Status tally:\s*(.+)$", re.M)
_TALLY_PAIR_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)=(\d+)")
_INT_RE = re.compile(r"\d+")

# Excluded statuses the snapshot DOES label, and the marker text it labels them
# with. A status absent from this map is unlabelled by definition.
#
# Several statuses deliberately share one marker: the snapshot's Assembly
# frontier line reports generate_closure_snapshot.ASSEMBLING_STATUSES --
# {assembling, open_by_design} -- as ONE number, so the count is checked against
# their SUM. Splitting them here would make the check fire spuriously the first
# time an `open_by_design` node appears.
#
# THIS MAP IS THE WORDING CONTRACT with generate_closure_snapshot.py, and it is
# deliberately explicit rather than inferred. If the generator renames that
# bullet, the marker stops matching and D-010 escalates -- which is the correct
# direction: a renamed label is exactly as unreadable as an absent one, and the
# check must not pass by guessing at prose.
EXCLUSION_LABELS = {
    "assembling": "Assembly frontier",
    "open_by_design": "Assembly frontier",
}


def _parse_snapshot(path):
    """Read closure_status.md once -> (pct, denominator, tally, overall_block).

    Every element is independently optional. An unreadable or unrecognised
    snapshot yields (None, None, None, None), which both callers treat as the
    LOUD case -- unlabelled for check 2, undiscriminated for check 5.
    """
    if not path.exists():
        return None, None, None, None
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None, None, None, None

    pct = denom = None
    m = _SNAPSHOT_RE.search(text)
    if m:
        pct = float(m.group(1))
        denom = int(m.group(2))

    om = _OVERALL_RE.search(text)
    overall = om.group(1) if om else None

    tally = None
    tm = _TALLY_RE.search(overall if overall is not None else text)
    if tm:
        pairs = _TALLY_PAIR_RE.findall(tm.group(1))
        if pairs:
            tally = {k: int(v) for k, v in pairs}

    return pct, denom, tally, overall


def _is_labelled(overall, marker, expected_count):
    """True when the Overall block states `marker` alongside `expected_count`.

    Requiring the COUNT as well as the marker is what stops a stale label from
    passing: a frontier line left saying 7 while 10 nodes are excluded is not a
    label, it is a second wrong number.
    """
    if not overall or not marker:
        return False
    for line in overall.splitlines():
        if marker in line and str(expected_count) in _INT_RE.findall(line):
            return True
    return False


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

    tally: dict[str, int] = {}
    for n in v3_nodes:
        tally[n.status] = tally.get(n.status, 0) + 1

    snap = ctx.repo_root / "evidence" / "planning" / "closure_status.md"
    committed_pct, committed_denom, committed_tally, overall = _parse_snapshot(snap)

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
            tier=TIER,
            evidence={
                "non_v3_in_denominator": [n.node_id for n in bad_gen],
                "weight_none_in_denominator": [n.node_id for n in bad_weight],
            },
        ))

    # --- 2. silent exclusion surface --------------------------------------
    # Every non-deferred excluded status, partitioned into LABELLED (the
    # snapshot states the exclusion where the percentage is read) and SILENT
    # (it does not). Only the silent half is a finding; the labelled half is
    # reported in the summary so the exclusion stays auditable rather than
    # disappearing from the report along with the finding.
    non_deferred: dict[str, list[str]] = {}
    for n in excluded:
        if n.status not in DEFERRED_STATUSES:
            non_deferred.setdefault(n.status, []).append(n.node_id)

    by_marker: dict[str | None, list[str]] = {}
    for status in non_deferred:
        by_marker.setdefault(EXCLUSION_LABELS.get(status), []).append(status)

    silent: dict[str, list[str]] = {}
    labelled: dict[str, list[str]] = {}
    for marker, statuses in by_marker.items():
        shared = sum(len(non_deferred[s]) for s in statuses)
        target = labelled if _is_labelled(overall, marker, shared) else silent
        for s in statuses:
            target[s] = non_deferred[s]

    if silent:
        n_hidden = sum(len(v) for v in silent.values())
        findings.append(finding(
            detector=DETECTOR_ID,
            # The status set is part of the identity, not a mutable attribute:
            # a NEW unlabelled status is a DIFFERENT defect and must escalate on
            # its own merits instead of inheriting the older set's disposition.
            # Same reasoning as D-007's (node, gate-set) subject.
            subject="silent_exclusion_surface@statuses=%s"
                    % ",".join(sorted(silent)),
            title="%d v3 node(s) are excluded from the closure denominator by a "
                  "status that is not 'deferred' and is not labelled" % n_hidden,
            detail=(
                "Statuses excluded from the V3 denominator, absent from "
                "DEFERRED_STATUSES, and not stated in the snapshot's Overall "
                "block where the percentage is read: %s. Excluding them may well "
                "be correct (assembling work is held out by design); the finding "
                "is that the exclusion is unlabelled, so a reader of "
                "'across N non-deferred nodes' has no way to know these left. "
                "This is the surface the next SD-031 comes from. Fix by labelling "
                "the exclusion in generate_closure_snapshot.py's Overall block "
                "and adding the marker to D-010's EXCLUSION_LABELS -- not by "
                "suppressing this finding."
                % ", ".join("%s=%d" % (k, len(v)) for k, v in sorted(silent.items()))
            ),
            severity="P2", confidence=0.6, signal="weak", escalate=True,
            tier=TIER,
            evidence={"by_status": {k: sorted(v) for k, v in silent.items()},
                      "labelled_exclusions": {k: len(v)
                                              for k, v in sorted(labelled.items())},
                      "deferred_statuses": sorted(DEFERRED_STATUSES),
                      "snapshot_overall_readable": overall is not None},
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
            tier=TIER,
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
                tier=TIER,
                evidence={"diffs": diffs},
            ))

    # --- 5. cross-check against the committed snapshot --------------------
    # The snapshot commits its own per-status tally, and that tally is the exact
    # discriminator between the two very different failures a denominator
    # mismatch can mean. Differing tally == differing INPUTS == regen lag, which
    # governance.sh Step 3c-bis clears on its own. Identical tally == identical
    # inputs producing a different ANSWER == the denominator rule itself has
    # diverged from the producer, which is the accounting breaking and is what
    # this detector exists for. Reporting both at one severity under one
    # finding_id buried the second behind the first.
    tally_delta = None
    if committed_tally is not None:
        keys = set(committed_tally) | set(tally)
        tally_delta = {k: {"committed": committed_tally.get(k, 0),
                           "recomputed": tally.get(k, 0)}
                       for k in sorted(keys)
                       if committed_tally.get(k, 0) != tally.get(k, 0)}

    if committed_denom is not None and committed_denom != len(denom):
        if committed_tally is None:
            lag = "unknown"
        elif tally_delta:
            lag = "explained"
        else:
            lag = "unexplained"

        if lag == "explained":
            sev, conf, esc = "P2", 0.9, False
            why = (
                "The snapshot's own committed status tally DIFFERS from the "
                "recomputation (%s), so the two were computed from different "
                "plan content: this is regen lag, not broken accounting. The "
                "committed percentage is stale rather than wrong-by-rule, and "
                "governance.sh Step 3c-bis regenerates it. Run "
                "scripts/generate_closure_snapshot.py to clear it now."
                % "; ".join("%s %d->%d" % (k, v["committed"], v["recomputed"])
                            for k, v in tally_delta.items())
            )
        elif lag == "unexplained":
            sev, conf, esc = "P1", 0.85, True
            why = (
                "The snapshot's committed status tally is IDENTICAL to the "
                "recomputation, so both were computed from the same plan "
                "content and still disagree about the denominator. This is NOT "
                "regen lag -- regenerating will not fix it. The denominator RULE "
                "has diverged between generate_closure_snapshot.py and this "
                "detector's independent recomputation, and the committed closure "
                "percentage is wrong. Check STATUS_WEIGHTS against serve.py's "
                "CLOSURE_STATUS_WEIGHTS and the generation filter."
            )
        else:
            sev, conf, esc = "P1", 0.5, True
            why = (
                "The snapshot carries no parseable 'Status tally:' line, so lag "
                "cannot be distinguished from a genuine rule divergence. Treated "
                "as the loud case on purpose. Regenerate with "
                "scripts/generate_closure_snapshot.py; if the numbers still "
                "differ, the accounting is genuinely broken."
            )

        findings.append(finding(
            detector=DETECTOR_ID,
            # `lag` is part of the identity: the two cases need different
            # dispositions, and a lag-explained mismatch resolving must not
            # silently carry a rule divergence's `first_seen` with it.
            subject="snapshot_denominator_mismatch@lag=%s" % lag,
            title="Committed closure snapshot denominator (%d) does not match "
                  "recomputation (%d) -- %s"
                  % (committed_denom, len(denom),
                     {"explained": "regen lag",
                      "unexplained": "SAME INPUTS, different answer",
                      "unknown": "cause undetermined"}[lag]),
            detail=(
                "evidence/planning/closure_status.md states %d non-deferred "
                "nodes; recomputing from plan frontmatter gives %d. %s"
                % (committed_denom, len(denom), why)
            ),
            severity=sev, confidence=conf, signal="weak", escalate=esc,
            tier=TIER,
            evidence={"committed_denominator": committed_denom,
                      "recomputed_denominator": len(denom),
                      "committed_pct": committed_pct,
                      "lag": lag,
                      "tally_delta": tally_delta},
        ))

    summary = {
        "detector": DETECTOR_ID,
        "title": DETECTOR_TITLE,
        "n_findings": len(findings),
        "v3_nodes": len(v3_nodes),
        "denominator": len(denom),
        "excluded": len(excluded),
        "committed_denominator": committed_denom,
        "committed_tally_parsed": committed_tally is not None,
        "tally_delta": tally_delta,
        "status_tally_v3": dict(sorted(tally.items())),
        "labelled_exclusions": {k: len(v) for k, v in sorted(labelled.items())},
        "silent_exclusions": {k: len(v) for k, v in sorted(silent.items())},
        "serve_weights_available": bool(authoritative),
        "weights_drift": drift_detail,
    }
    return findings, summary
