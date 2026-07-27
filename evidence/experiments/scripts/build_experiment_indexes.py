#!/usr/bin/env python3
"""Build evidence indexes from experimental and literature artefacts.

This script scans:
  evidence/experiments/**/runs/**/manifest.json
  evidence/literature/**/entries/**/record.json

It regenerates:
  evidence/experiments/INDEX.md
  evidence/experiments/claim_evidence.v1.json
  evidence/experiments/conflicts.md
  evidence/experiments/promotion_demotion_recommendations.md
  evidence/decisions/decision_state.v1.json
  evidence/planning/evidence_backlog.v1.json
  evidence/planning/experiment_proposals.v1.json
  evidence/planning/architecture_gap_register.v1.json
  evidence/planning/ARCHITECTURE_GAP_REGISTER.md
  evidence/experiments/<experiment_type>/INDEX.md
  evidence/experiments/<experiment_type>/experiment.md (auto Design implications block)
  evidence/experiments/TODOs.md
  evidence/literature/INDEX.md

Dependencies: Python standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Optional

START_MARKER = "<!-- AUTO-DESIGN-IMPLICATIONS:START -->"
END_MARKER = "<!-- AUTO-DESIGN-IMPLICATIONS:END -->"

ADAPTER_SCHEMA_VERSION = "jepa_adapter_signals/v1"
ADAPTER_REQUIRED_PE_FIELDS = {"mean", "p95"}
ADAPTER_REQUIRED_SIGNAL_METRICS = {
    "latent_prediction_error_mean",
    "latent_prediction_error_p95",
    "latent_residual_coverage_rate",
    "precision_input_completeness_rate",
}
ADAPTER_ALLOWED_UNCERTAINTY = {"none", "dispersion", "ensemble", "head"}


@dataclass
class StopHit:
    metric: str
    op: str
    threshold: float
    value: float

    def render(self) -> str:
        return f"{self.metric} {self.op} {self.threshold} (value={_fmt_number(self.value)})"


@dataclass
class RunRecord:
    experiment_type: str
    run_id: str
    timestamp_raw: str
    timestamp: datetime
    manifest_path: Path
    metrics_path: Path
    summary_path: Path
    manifest_status: str
    final_status: str = "PASS"
    fail_hits: list[StopHit] = field(default_factory=list)
    failure_signatures: list[str] = field(default_factory=list)
    metrics: dict[str, float] = field(default_factory=dict)
    deltas: dict[str, float] = field(default_factory=dict)
    claim_ids_tested: list[str] = field(default_factory=list)
    evidence_class: str = "simulation"
    evidence_direction: str = "unknown"
    evidence_direction_per_claim: dict[str, str] = field(default_factory=dict)
    direction_explicitly_set: bool = False
    architecture_epoch: str = ""
    adapter_signals_path: Path | None = None
    experiment_purpose: str = "evidence"
    # Diagnostic adjudication gate (2026-06-06): the self-routed
    # interpretation.label is a HYPOTHESIS, not a verdict. interpretation_label
    # carries it for surfacing; adjudication is the machine-derived trust flag
    # in {verified, precondition_unmet, vacuous_pass, unverified, n/a} computed
    # by _compute_adjudication() from interpretation.preconditions[] +
    # interpretation.criteria_non_degenerate{}. Only diagnostic/baseline runs
    # are flagged; evidence runs carry "n/a". Absent structures => "unverified"
    # (legacy, surfaced-but-not-blocked). See evidence/planning/
    # proposal_diagnostic_adjudication_gate_2026-06-06.md.
    interpretation_label: str = ""
    adjudication: str = "n/a"
    # Recorded (NON-GATING) preconditions: unmet entries from
    # interpretation.recorded_preconditions[], surfaced for governance visibility
    # only. NEVER feeds `adjudication`, scoring_excluded, confidence or conflict --
    # see _recorded_precondition_findings for why the split exists.
    recorded_preconditions_unmet: list[dict] = field(default_factory=list)
    preconditions_scope_note: str = ""
    adapter_contract_status: str = "n/a"
    adapter_contract_errors: list[str] = field(default_factory=list)
    evidence_level: str = "C"
    # Substrate-staleness gate (2026-06-02): manually-set manifest fields that
    # mark this run's evidence as mechanistically stale because a substrate it
    # depends on changed AFTER the run was recorded. Either flag excludes the
    # entry from confidence/conflict scoring (scoring_excluded="stale_substrate")
    # while leaving it in the full entry log. Distinct from the time-only
    # epoch gate (stale_epoch) and from duplicate/iteration supersession
    # (superseded). Default-absent => bit-identical to pre-gate behaviour.
    pending_retest_after_substrate: bool = False
    superseded_by_substrate: str = ""
    # Per-claim staleness (mirrors evidence_direction_per_claim): de-weights ONLY
    # the listed claim(s) in a multi-claim manifest, leaving the other tagged
    # claims' evidence intact. Use when a substrate change makes the run stale
    # for one claim but not the others it tests.
    #   pending_retest_after_substrate_per_claim: ["MECH-307"]
    #   superseded_by_substrate_per_claim: {"SD-049": "SD-049@2026-05-31"}
    pending_retest_after_substrate_per_claim: list[str] = field(default_factory=list)
    superseded_by_substrate_per_claim: dict[str, str] = field(default_factory=dict)
    # Non-degeneracy gate (2026-06-11): an explicitly-set manifest flag marking a
    # run's result as structurally DEGENERATE -- a discriminative metric pinned at
    # a constant (zero cross-arm/cross-seed variance, or floor-pinned on every
    # step) so its criterion cannot fire regardless of behaviour. Examples:
    # V3-EXQ-514m (C_WL=0.0 on a valence channel that was never written),
    # V3-EXQ-642 (z_block identically 0 on an untrained encoder). A degenerate run
    # is excluded from confidence/conflict scoring (scoring_excluded="degenerate")
    # while staying in the full entry log -- exactly parallel to "superseded"
    # (corrected iteration) and "stale_substrate" (mechanistically outdated), but
    # for the vacuous-criterion failure mode that previously had to be caught by a
    # manual /failure-autopsy and hand-reclassified non_contributory. The ree-v3
    # runtime helper (experiments/_experiment_lib.check_degeneracy) sets these at
    # measurement time; a failure-autopsy may also set them by hand. The
    # whole-run form excludes every tagged claim; the per-claim form de-weights
    # ONLY the named claim(s). Default-absent (None) => no-op, bit-identical to
    # pre-gate behaviour.
    #   non_degenerate: false                            (whole run vacuous)
    #   non_degenerate_per_claim: {"MECH-229": false}    (vacuous for one claim)
    #   degeneracy_reason: "C_WL pinned at 0.0; valence channel never written"
    non_degenerate: bool | None = None
    non_degenerate_per_claim: dict[str, bool] = field(default_factory=dict)
    degeneracy_reason: str = ""
    # Experimental Recording Standard always-core (2026-07-12). Surfaced for
    # queryability ONLY -- neither field feeds confidence/conflict scoring. Widening
    # the consumed-field set to make these visible is the standard's section-4
    # deferred-hardening item; changing how they SCORE requires user sign-off.
    #   substrate_hash: content hash over ree_core/** + env + _lib/** (the reuse
    #     prerequisite -- 0% of flat manifests carried it pre-standard).
    #   label_balance: {"<label>": {"train_pos_frac": .., "eval_pos_frac": ..}} --
    #     the 047m false-clear fix (a saturated TRAINING label invalidates a run).
    substrate_hash: str = ""
    label_balance: dict[str, Any] = field(default_factory=dict)
    # Recording-provenance surfacing (2026-07-16): the machine + machine_class the
    # run executed on. machine_class is the cloud-authoritative gate class (SD-024)
    # and the arm-reuse fingerprint key. Read from the pack after the unconditional
    # flat-provenance backfill (_merge_flat_manifest_overrides), so a thin
    # pre-2026-07-16 pack still surfaces the flat sibling's value. Surfaced for
    # queryability, NOT scored.
    machine: str = ""
    machine_class: str = ""


def _is_number(value: Any) -> bool:
    """True for a real int/float (excludes bool, which is an int subclass)."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _precondition_direction(p: dict) -> str:
    """Resolve a precondition's bound DIRECTION for the (3a) numeric recompute.

    Returns:
      - "lower" -- a FLOOR; met := measured >= threshold. This is the default,
                   and the semantics of the hundreds of legacy floor
                   preconditions: a below-floor measured is the
                   trivial-prediction signature the author cannot see.
      - "upper" -- a CEILING; met := measured <= threshold. A "stayed below the
                   explosion/instability ceiling" check (e.g.
                   rolled_out_zworld_*_bounded, threshold 1e6). Here
                   measured << threshold means the check PASSED, not failed --
                   treating it as a floor false-flags it `precondition_unmet`
                   (the 2026-06-07 V3-EXQ-648a / V3-EXQ-649 directionality bug).

    Honours an explicit per-entry hint, in priority order:
      1. `comparator`: the PASS comparison, i.e. met == (measured <comparator>
         threshold). ">=" / ">" -> lower; "<=" / "<" -> upper.
      2. `direction`:  "lower"/"floor"/"min" -> lower;
                       "upper"/"ceiling"/"max" -> upper.
    Anything unrecognised (or absent) falls back to "lower" so the existing
    floor manifests keep their meaning with no edit. Authors of bounded-ceiling
    preconditions MUST set direction:"upper" (or comparator:"<=") -- see the
    queue-experiment SKILL.md adjudication-precondition guidance.

    SINGLE-BOUND ONLY. This resolves which side one bound sits on; it cannot
    describe a two-sided band. For that -- and for comparator STRICTNESS, which
    this function deliberately discards -- see _precondition_unmet, which is the
    entry point the adjudicator actually calls.
    """
    if not isinstance(p, dict):
        return "lower"
    comp = p.get("comparator")
    if isinstance(comp, str):
        c = comp.strip()
        if c in (">=", ">"):
            return "lower"
        if c in ("<=", "<"):
            return "upper"
    direction = p.get("direction")
    if isinstance(direction, str):
        d = direction.strip().lower()
        if d in ("lower", "floor", "min", "lower_bound"):
            return "lower"
        if d in ("upper", "ceiling", "max", "upper_bound"):
            return "upper"
    return "lower"


_INTERVAL_DIRECTIONS = ("interval", "between", "band", "range", "two_sided", "two-sided")


def _precondition_unmet(p: dict) -> Optional[bool]:
    """Recompute one precondition's `met` from its reported bounds.

    Returns True (UNMET), False (met), or None when the entry exposes no
    numeric bound spec and is therefore not recomputable -- the caller then
    falls through to the legacy author-trusted `met is False` path.

    Three shapes, in resolution order:

    1. INTERVAL (two-sided) -- `threshold_low` AND `threshold_high` both
       numeric. Met when measured lies BETWEEN them. Strictness per leg via
       `comparator_low` (default ">=", i.e. the low bound is inclusive) and
       `comparator_high` (default "<="). This is the only shape that can
       express a check like `E_SAT_LOW < S < E_SAT_HIGH` (V3-EXQ-779b
       baseline_entropy_headroom): before this existed, such a check could
       only declare ONE of its two legs, and the undeclared leg -- 779b's
       `E_SAT_LOW = 0.02` floor -- was absent from the manifest entirely, so
       the indexer's recompute could not reproduce `met` and silently
       adjudicated on the ceiling leg alone. A `direction` of "interval" /
       "between" / "band" / "range" declares the shape explicitly; it is
       accepted but NOT required, because the presence of both bounds is
       already unambiguous.

    2. SINGLE BOUND -- numeric `measured` + `threshold`, direction resolved by
       _precondition_direction. Now honours STRICTNESS: a `comparator` of ">"
       (resp. "<") makes the bound exclusive, so measured == threshold is
       UNMET. Previously ">" and ">=" were byte-identical in effect because
       the recompute hardcoded the non-strict comparison; no manifest in the
       corpus declared a strict comparator at the time this was added (survey
       2026-07-19: 1553 precondition entries, comparator values {"<=": 4}),
       so honouring strictness changed no existing adjudication.

    3. NOT RECOMPUTABLE -- returns None.

    Bounds that are inverted (low > high) are treated as not recomputable
    rather than as always-unmet: an inverted interval is an authoring error,
    and silently flagging every such run `precondition_unmet` would repeat the
    2026-06-07 directionality bug's failure mode of turning a schema mistake
    into a corpus-wide false adjudication.
    """
    if not isinstance(p, dict):
        return None
    m = p.get("measured")
    if not _is_number(m):
        return None

    lo, hi = p.get("threshold_low"), p.get("threshold_high")
    if _is_number(lo) and _is_number(hi):
        if lo > hi:
            return None  # inverted interval -- authoring error, do not adjudicate
        lo_strict = str(p.get("comparator_low", ">=")).strip() == ">"
        hi_strict = str(p.get("comparator_high", "<=")).strip() == "<"
        low_ok = (m > lo) if lo_strict else (m >= lo)
        high_ok = (m < hi) if hi_strict else (m <= hi)
        return not (low_ok and high_ok)

    # An entry that DECLARES itself two-sided but ships fewer than both bounds is
    # malformed, not single-bounded. Falling through would silently read it as a
    # FLOOR (_precondition_direction does not recognise "interval" and defaults to
    # "lower"), i.e. adjudicate a band on one leg -- the exact defect the interval
    # shape exists to remove. Refuse to recompute instead.
    d = p.get("direction")
    if isinstance(d, str) and d.strip().lower() in _INTERVAL_DIRECTIONS:
        return None

    t = p.get("threshold")
    if not _is_number(t):
        return None
    comp = p.get("comparator")
    comp = comp.strip() if isinstance(comp, str) else ""
    if _precondition_direction(p) == "upper":
        return m >= t if comp == "<" else m > t
    return m <= t if comp == ">" else m < t


def _compute_adjudication(interpretation: Any, status: str,
                          experiment_purpose: str) -> tuple[str, str]:
    """Diagnostic adjudication gate -- derive the trust flag for a self-routed run.

    Returns (interpretation_label, adjudication_flag). The flag is one of:
      - "n/a"             -- not a diagnostic/baseline run (evidence runs are
                             adjudicated by the normal claim-confidence path).
      - "unverified"      -- diagnostic/baseline run whose manifest declares
                             NEITHER preconditions[] NOR criteria_non_degenerate
                             (legacy; surfaced but not blocked).
      - "precondition_unmet" -- a self-route premise did not hold. Fired by
                             EITHER (3a) a readiness-kind precondition entry whose
                             RECOMPUTED met is false -- a FLOOR fails below
                             threshold (measured < threshold), a CEILING fails
                             above it (measured > threshold), per
                             _precondition_direction; author-free, catches the
                             trivial-prediction signature the author cannot see --
                             OR the legacy author-trusted
                             interpretation.preconditions[].met == false.
      - "vacuous_pass"    -- overall PASS that clears a gate on nothing. Fired by
                             EITHER (3b) a criterion tagged load_bearing:true with
                             passed:false (the V3-EXQ-621a aggregation-vacuity
                             pattern) OR the legacy criteria_non_degenerate value
                             being false. CONVENTION for the legacy check: a key
                             in criteria_non_degenerate is a NON-DEGENERACY
                             ASSERTION (True=non-degenerate/good), so a False value
                             flags a gate cleared on nothing -- EXCEPT keys whose
                             name ends in "_branch". Those are BRANCH-SELECTORS
                             (direction-neutral: False = "took the other branch",
                             often the GOOD outcome, e.g. V3-EXQ-723 J-lens
                             diffuse_branch=False = took the compact/present branch)
                             and are excluded from the vacuity check. Without the
                             exclusion, a branch-selector False spuriously yields
                             vacuous_pass -- the same directionality false-flag class
                             as V3-EXQ-648a/649. Keep branch-selectors in
                             signature_gates{} where they belong; if a manifest also
                             places one in criteria_non_degenerate{}, the "_branch"
                             suffix makes the indexer ignore it.
                             ALSO EXCLUDED: keys whose matching interpretation
                             .criteria[] entry (matched on `name`) is tagged
                             load_bearing:false. The legacy check is otherwise
                             load_bearing-BLIND, so a manifest supplying BOTH
                             blocks passed (3b) -- which honours the tag -- and
                             was then blocked by the legacy path on a criterion
                             its own author had explicitly declared not
                             load-bearing (V3-EXQ-783 C2_event_selectivity, a
                             recorded caveat on a run whose load-bearing
                             C1_cr_crossing was non-degenerate and passed; see
                             failure_autopsy_V3-EXQ-783_2026-07-18.md Sec.2 --
                             adjudicated a FALSE POSITIVE). Same false-flag class
                             as the 648a/649 branch-selector case, and the
                             explicit tag is strictly better evidence than a name
                             suffix. Behaviour is UNCHANGED when criteria[] is
                             absent or a key has no matching entry, so the
                             hundreds of pre-convention manifests that expose no
                             load_bearing tag keep their present adjudication.
      - "verified"        -- declared structure(s) present and all checks hold.

    The (3a)/(3b) author-free checks run AHEAD of the legacy author-trusted
    checks; the legacy path remains the fallback. (3a) RECOMPUTES met from numeric
    measured+threshold and does NOT trust an author-supplied `met` when both are
    present (the legacy met-loop skips those entries -- recompute is authoritative).

    See evidence/planning/proposal_trivial_prediction_readiness_gate_2026-06-06.md
    (Q1-Q4 sign-off), its parent proposal_diagnostic_adjudication_gate_2026-06-06.md,
    and the V3-EXQ-642 / V3-EXQ-621a autopsies for the motivating failure modes.
    """
    interp = interpretation if isinstance(interpretation, dict) else {}
    label = str(interp.get("label", "") or "")
    if experiment_purpose not in ("diagnostic", "baseline"):
        return label, "n/a"
    preconditions = interp.get("preconditions")
    preconditions = preconditions if isinstance(preconditions, list) else []

    # (3a) Readiness recompute (proposal_trivial_prediction_readiness_gate_2026-06-06,
    # Q1). For any precondition entry carrying numeric measured+threshold (a
    # readiness-kind entry), RECOMPUTE met from measured+threshold and do NOT
    # trust the author-supplied `met`. The comparison RESPECTS the precondition's
    # bound direction (_precondition_direction): a FLOOR is unmet when measured
    # falls BELOW threshold (measured < threshold) -- the trivial-prediction
    # signature the author cannot see (V3-EXQ-642 pred_mag<floor masked by a low
    # wf_mse; 264 pred_norm~0; 620 identically-zero distributions); a CEILING is
    # unmet only when measured rises ABOVE threshold (measured > threshold).
    # Direction defaults to floor, so the hundreds of legacy floor preconditions
    # are unaffected; without this, an upper-bound "stayed below the explosion
    # ceiling" check (rolled_out_zworld_*_bounded, measured 0.19 vs threshold 1e6)
    # was false-flagged precondition_unmet (V3-EXQ-648a / V3-EXQ-649, 2026-06-07).
    # Bound resolution (incl. the two-sided INTERVAL shape and comparator
    # strictness) lives in _precondition_unmet; None == not recomputable, which
    # falls through to the legacy author-trusted path below.
    for p in preconditions:
        if _precondition_unmet(p) is True:
            return label, "precondition_unmet"

    # (3b) Aggregation-vacuity (the V3-EXQ-621a pattern). An overall PASS while a
    # criterion explicitly tagged load_bearing:true did not pass clears a gate on
    # nothing. Gated on the explicit load_bearing tag so it never over-fires on a
    # legitimate M-of-N pass.
    if str(status).upper() == "PASS":
        criteria = interp.get("criteria")
        if isinstance(criteria, list):
            for c in criteria:
                if (isinstance(c, dict)
                        and c.get("load_bearing") is True
                        and c.get("passed") is False):
                    return label, "vacuous_pass"

    # --- legacy author-trusted checks (fallback for declarations that expose no
    # numeric measured/threshold or load_bearing tag) ---
    crit = interp.get("criteria_non_degenerate")
    crit = crit if isinstance(crit, dict) else {}
    if not preconditions and not crit:
        return label, "unverified"
    # An unmet precondition invalidates the self-route's premise -> highest priority.
    # Skip readiness-kind entries already governed by the (3a) numeric recompute
    # above (recompute is authoritative when measured+threshold are present).
    for p in preconditions:
        if not isinstance(p, dict):
            continue
        if _precondition_unmet(p) is not None:
            continue  # governed by the (3a) recompute above, which is authoritative
        if p.get("met") is False:
            return label, "precondition_unmet"
    # A PASS that rests on a degenerate criterion clears a gate on nothing.
    # Exclude BRANCH-SELECTOR keys (name ends in "_branch"): for a selector,
    # False means "took the other branch" (often the GOOD outcome, e.g.
    # V3-EXQ-723 J-lens diffuse_branch=False = took the compact/present branch),
    # NOT "this criterion is degenerate". Treating a selector False as degeneracy
    # is the V3-EXQ-648a/649 directionality false-flag class. See docstring
    # CONVENTION note + failure_autopsy_V3-EXQ-723_2026-07-09.md Sec.3.
    # ALSO exclude keys the manifest's own criteria[] tags load_bearing:false.
    # (3b) above honours that tag; this legacy path was blind to it, so a manifest
    # supplying BOTH blocks cleared (3b) and was then blocked here on a criterion
    # its author had explicitly declared a non-blocking caveat (V3-EXQ-783
    # C2_event_selectivity -- see failure_autopsy_V3-EXQ-783_2026-07-18.md Sec.2).
    # Absent criteria[] / unmatched keys are untouched, so legacy manifests that
    # expose no load_bearing tag keep their present adjudication.
    non_load_bearing = set()
    _criteria = interp.get("criteria")
    if isinstance(_criteria, list):
        for c in _criteria:
            if isinstance(c, dict) and c.get("load_bearing") is False:
                name = c.get("name")
                if isinstance(name, str):
                    non_load_bearing.add(name)
    degeneracy_assertions = [v for k, v in crit.items()
                             if not str(k).endswith("_branch")
                             and str(k) not in non_load_bearing]
    if str(status).upper() == "PASS" and any(v is False for v in degeneracy_assertions):
        return label, "vacuous_pass"
    return label, "verified"


# Canonical set of adjudication flags that BLOCK a diagnostic/baseline self-route
# from driving a governance action. Keyed STRICTLY on the active-failure flags --
# NEVER include "unverified". A legacy manifest with no preconditions[] is
# `unverified`, and treating absence as blocking would fire against the entire
# pre-convention record (hundreds of runs, incl. past legitimate gate-clears).
# `unverified` is surfaced-not-blocked; the retrospective audit handles legacy.
BLOCKING_ADJUDICATIONS = ("precondition_unmet", "vacuous_pass")


def adjudication_blocks_governance_action(adjudication: str) -> tuple[bool, str]:
    """Headless-governance guard: may a diagnostic with this adjudication flag
    drive a governance action (clear/keep a v3_pending, mint/AMEND a
    substrate_queue entry, close/route a thought-intake)?

    Returns (blocked, reason). Strictly keyed on BLOCKING_ADJUDICATIONS so it is
    inert against the legacy `unverified` population and never breaks the pipeline
    against the pre-convention record. This is the single source of truth the
    future headless-governance path calls; the interactive /governance walk and
    generate_pending_review's flagged-filter mirror the same set. DORMANT today
    (no automated gate-clearing exists yet) -- landed keyed-correctly so the
    headless path inherits the footgun-free version. See
    evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.
    """
    flag = str(adjudication or "")
    if flag == "precondition_unmet":
        return True, ("self-route premise unmet -- adjudicate via /failure-autopsy "
                      "before acting (do NOT trust the self-routed label)")
    if flag == "vacuous_pass":
        return True, ("PASS rests on a degenerate criterion -- do NOT clear a gate "
                      "or mint a task; adjudicate via /failure-autopsy")
    # verified / unverified / n/a / unknown -> not blocked (absence is not blocking).
    return False, ""


# --- Recorded (NON-GATING) preconditions ----------------------------------
#
# `interpretation.recorded_preconditions[]` is the auditable-but-non-adjudicating
# sibling of `interpretation.preconditions[]`. Same entry shape (the ree-v3
# experiments/_lib/zworld_encoder_guard.zworld_precondition() shaper emits into
# either list), but it is READ HERE ONLY FOR SURFACING and is deliberately NOT
# consulted by _compute_adjudication().
#
# WHY THE SPLIT EXISTS -- do NOT "simplify" this by folding these entries into the
# flat preconditions[] list. _compute_adjudication reads preconditions[] FLAT and
# ARM-BLIND and returns a whole-run `precondition_unmet` on the FIRST unmet entry.
# A guard finding that is real but does NOT invalidate the run's premise (an
# arm-symmetric prior; a readout-side question with an unaffected control) would
# then vacate a valid result -- the V3-EXQ-785 vacating defect. So a driver whose
# premise survives the finding records it here instead, and states why in
# `interpretation.preconditions_scope_note`.
#
# THE INVARIANT THIS FUNCTION MUST PRESERVE: an unmet recorded_precondition is
# INFORMATIONAL ONLY. It must never (a) change the adjudication flag, (b) exclude
# the run from confidence/conflict scoring, or (c) alter evidence_direction. It is
# surfaced in the derived artifacts and in pending_review.md under a separate
# non-blocking heading so a non-gating finding is visible to governance rather than
# sitting unread in the manifest. Pinned by
# test_build_experiment_indexes.py::test_recorded_precondition_* .
#
# See evidence/planning/zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md.
def _recorded_precondition_findings(interpretation: Any) -> list[dict]:
    """Unmet entries from `interpretation.recorded_preconditions[]`, for surfacing.

    `met` is resolved the same way the adjudicating path resolves it -- numeric
    recompute via _precondition_unmet when measured+threshold are present (so a
    recorded entry and a gating entry agree on the same statistic), falling back to
    the author-supplied `met` when it is not recomputable. Returns [] for any
    manifest that declares no recorded_preconditions, so legacy output is
    byte-identical.
    """
    interp = interpretation if isinstance(interpretation, dict) else {}
    recorded = interp.get("recorded_preconditions")
    if not isinstance(recorded, list):
        return []
    findings: list[dict] = []
    for p in recorded:
        if not isinstance(p, dict):
            continue
        unmet = _precondition_unmet(p)
        if unmet is None:  # not recomputable -> fall back to the author's own verdict
            unmet = p.get("met") is False
        if not unmet:
            continue
        finding = {"name": str(p.get("name", "") or "(unnamed)")}
        for key in ("arm", "context", "measured", "threshold", "description"):
            if p.get(key) not in (None, ""):
                finding[key] = p[key]
        findings.append(finding)
    return findings


@dataclass
class LiteratureRecord:
    literature_type: str
    entry_id: str
    timestamp_raw: str
    timestamp: datetime
    record_path: Path
    summary_path: Path
    claim_ids_tested: list[str] = field(default_factory=list)
    evidence_class: str = "review"
    evidence_direction: str = "unknown"
    architecture_epoch: str = ""
    confidence: float = 0.5
    confidence_rationale: str = ""
    failure_signatures: list[str] = field(default_factory=list)


@dataclass
class DecisionLogEntry:
    claim_id: str
    decision_status: str
    recommendation: str
    decision_needed: str
    timestamp_utc: str
    selected_option: str = ""
    rationale: str = ""
    actor: str = "user"


def _fmt_number(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, int):
        return str(value)
    if float(value).is_integer():
        return str(int(value))
    return f"{value:.6f}".rstrip("0").rstrip(".")


def _fmt_delta(value: float | None) -> str:
    if value is None:
        return "n/a"
    sign = "+" if value >= 0 else ""
    return f"{sign}{_fmt_number(value)}"


# Timestamps embedded in a run_id / entry_id. Two shapes are in the corpus:
#   compact  -- 20260321T131836Z_v3_exq_060_...  /  ..._20260329T203824_v3
#   epoch    -- v3_exq_208_arc022_..._1775182116_v3   (10-digit epoch seconds)
# The epoch form is guarded to the 1e9..2e9 second band so a 10-digit seed or
# hash suffix is not mistaken for a time.
_RUNID_COMPACT_TS_RE = re.compile(r"(\d{8})T(\d{6})Z?")
_RUNID_EPOCH_TS_RE = re.compile(r"(?:^|[_-])(1[0-9]{9})(?:[_-]|$)")

# Sentinel for a run whose time cannot be recovered from any data-derived
# source. Deterministic and maximally-old, so such a run never wins a
# "latest" selection unless it is the only candidate. NEVER a wall clock.
_UNKNOWN_TIMESTAMP_DT = datetime(1970, 1, 1, tzinfo=timezone.utc)


def _timestamp_from_identifier(identifier: str) -> tuple[str, datetime] | None:
    """Recover a run's time from a timestamp embedded in its run_id/entry_id.

    Returns ``(iso_string, datetime)`` or ``None``. The ISO string is emitted
    in the same ``...Z`` form as a real ``timestamp_utc`` so downstream string
    sorts order derived and declared timestamps consistently.
    """
    if not identifier:
        return None
    match = _RUNID_COMPACT_TS_RE.search(identifier)
    if match:
        try:
            dt = datetime.strptime(match.group(1) + match.group(2), "%Y%m%d%H%M%S")
        except ValueError:
            dt = None
        if dt is not None:
            dt = dt.replace(tzinfo=timezone.utc)
            return dt.isoformat().replace("+00:00", "Z"), dt
    match = _RUNID_EPOCH_TS_RE.search(identifier)
    if match:
        try:
            dt = datetime.fromtimestamp(int(match.group(1)), tz=timezone.utc)
        except (ValueError, OverflowError, OSError):
            return None
        return dt.isoformat().replace("+00:00", "Z"), dt
    return None


def _parse_timestamp(raw: str | None, identifier: str = "") -> tuple[str, datetime]:
    """Resolve a record's timestamp deterministically.

    Order of precedence: the declared ``timestamp_utc``; then a timestamp
    parsed out of the record's own identifier; then an explicit unknown
    (empty string + epoch-0 sentinel).

    There is deliberately NO wall-clock or file-mtime fallback. Both are
    unstable across regenerations and machines: an mtime fallback here was
    the cause of `latest_run_id` flipping between rebuilds for the 29
    experiment types holding runs with a blank ``timestamp_utc``, and of
    a regeneration time being written into the durable ``timestamp_utc``
    column of the derived artifacts (where it looks authoritative and
    changes every build). An empty marker is strictly better than a
    plausible-looking wrong value.
    """
    if raw:
        normalized = raw
        if normalized.endswith("Z"):
            normalized = normalized[:-1] + "+00:00"
        try:
            dt = datetime.fromisoformat(normalized)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return raw, dt.astimezone(timezone.utc)
        except ValueError:
            pass
    derived = _timestamp_from_identifier(identifier)
    if derived is not None:
        return derived
    return "", _UNKNOWN_TIMESTAMP_DT


def _parse_timestamp_only(raw: str) -> datetime:
    normalized = raw
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"
    dt = datetime.fromisoformat(normalized)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _normalize_direction(raw: str | None) -> str:
    # "superseded" marks a run as invalidated by a corrected iteration -- it is
    # preserved in the entry log but excluded from scoring (see loop below).
    allowed = {"supports", "weakens", "mixed", "unknown", "superseded",
                "non_contributory", "inconclusive", "does_not_support"}
    # Map synonyms to canonical values.
    synonyms = {"does_not_support": "weakens"}
    value = (raw or "unknown").strip().lower()
    if value not in allowed:
        return "unknown"
    return synonyms.get(value, value)


def _normalize_confidence(raw: Any, default: float = 0.5) -> float:
    value = default
    if isinstance(raw, (int, float)):
        value = float(raw)
    value = max(0.0, min(1.0, value))
    return round(value, 3)


def _coerce_bool(raw: Any) -> bool:
    """Coerce a manifest value to bool, accepting JSON bools and truthy strings.

    Manifests are hand-edited and may carry true/false, "true"/"false",
    "yes"/"1", etc. Anything not recognised as truthy is False, so an absent
    or malformed flag never accidentally excludes evidence from scoring.
    """
    if isinstance(raw, bool):
        return raw
    if isinstance(raw, (int, float)):
        return raw != 0
    if isinstance(raw, str):
        return raw.strip().lower() in {"true", "1", "yes", "y", "t"}
    return False


def _normalize_evidence_level(raw: Any) -> str:
    """Validate evidence_level is one of A-E; default to C (single controlled experiment)."""
    VALID = {"A", "B", "C", "D", "E"}
    value = str(raw).strip().upper() if raw is not None else ""
    return value if value in VALID else "C"


def _normalize_text_list(raw: Any) -> list[str]:
    if not isinstance(raw, list):
        return []
    out: list[str] = []
    for item in raw:
        token = str(item).strip()
        if token:
            out.append(token)
    return out


def _dedupe_preserve_order(items: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in items:
        token = item.strip()
        if not token or token in seen:
            continue
        out.append(token)
        seen.add(token)
    return out


def _prefix_class(source_type: str, evidence_class: str) -> str:
    token = (evidence_class or "unclassified").strip()
    prefix = "exp" if source_type == "experimental" else "lit"
    if token.startswith(f"{prefix}:"):
        return token
    return f"{prefix}:{token}"


def _load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except (TimeoutError, OSError) as exc:
        # iCloud-offloaded files may raise TimeoutError (errno 60) or OSError (errno 89)
        # when the cloud sync can't complete in time. Return empty dict to skip gracefully.
        print(f"WARNING: skipping unreadable file (iCloud/IO timeout) {path}: {exc}")
        return {}
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON: {path}: {exc}") from exc


def _load_json_compatible_yaml(path: Path, description: str) -> dict[str, Any]:
    """Load JSON-compatible YAML using stdlib json parser.

    Files keep .yaml extension for readability/versioning while remaining JSON-compatible.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise RuntimeError(f"Missing {description} file: {path}") from exc

    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"{path} must be JSON-compatible YAML (YAML 1.2 superset of JSON)."
        ) from exc

    if not isinstance(data, dict):
        raise RuntimeError(f"{description} root must be an object: {path}")
    return data


def _compare(value: float, op: str, threshold: float) -> bool:
    if op == ">":
        return value > threshold
    if op == ">=":
        return value >= threshold
    if op == "<":
        return value < threshold
    if op == "<=":
        return value <= threshold
    if op == "==":
        return value == threshold
    if op == "!=":
        return value != threshold
    raise RuntimeError(f"Unsupported stop criteria operator: {op}")


# Governance/adjudication fields a /failure-autopsy or governance pass may
# correct AFTER a run is recorded. These corrections are written to the FLAT
# manifest (evidence/experiments/<run_id>.json), which is the surface
# /failure-autopsy and operators edit -- NOT the runs/<run_id>/manifest.json
# "pack" copy the indexer scans for scoring. Each of these fields gates scoring
# exclusion or evidence direction, so a flat-only correction that does not
# reach the pack copy is silently ignored and the stale pack value keeps
# scoring (confirmed 2026-06-14: pack `does_not_support` -> weakens on MECH-171
# x3 / MECH-057b while the flat copy already read `non_contributory` /
# `superseded`). The merge below makes the flat copy authoritative for these
# fields only; everything else (metrics, status, claim_ids, timestamps) is
# still read from the pack.
_FLAT_AUTHORITATIVE_FIELDS = (
    "evidence_direction",
    "evidence_direction_per_claim",
    "evidence_direction_note",
    "non_degenerate",
    "non_degenerate_per_claim",
    "degeneracy_reason",
    "superseded_by",
    "pending_retest_after_substrate",
    "pending_retest_after_substrate_per_claim",
    "superseded_by_substrate",
    "superseded_by_substrate_per_claim",
    # Experimental Recording Standard always-core (2026-07-12). These are
    # PROVENANCE/READOUT fields, NOT governance-direction fields -- they never
    # change how a run scores (they are absent from _FLAT_DIRECTION_FIELDS below,
    # so a flat/pack disagreement on them merges silently rather than WARNing).
    # Listing them here just lets a flat-copy value ride the same overlay when a
    # governance correction lands, so the surfaced substrate_hash/label_balance
    # stay consistent with the corrected flat copy. Purpose: make these fields
    # queryable in the emitted index, not load-bearing to promotion math.
    "substrate_hash",
    "label_balance",
)

# Subset of the above whose disagreement actually changes how a run scores a
# claim (direction / exclusion). A mismatch on any of these is the dangerous
# case the 2026-06-14 incident exhibited, so it is WARNed loudly. The remaining
# fields (e.g. degeneracy_reason free text) are merged silently.
_FLAT_DIRECTION_FIELDS = frozenset({
    "evidence_direction",
    "evidence_direction_per_claim",
    "non_degenerate",
    "non_degenerate_per_claim",
    "superseded_by",
    "pending_retest_after_substrate",
    "pending_retest_after_substrate_per_claim",
    "superseded_by_substrate",
    "superseded_by_substrate_per_claim",
})

# Pure-provenance always-core fields backfilled from the flat sibling onto the
# pack UNCONDITIONALLY (independent of the annotation gate) when the pack lacks or
# empties them. None of these are in _FLAT_DIRECTION_FIELDS, so they never change
# how a run scores -- backfill only makes the scored artifact self-describing.
_FLAT_PROVENANCE_BACKFILL_FIELDS = (
    "machine",
    "machine_class",
    "substrate_hash",
)

# Sentinel distinguishing "pack has no such key" from "pack value is None".
_MISSING = object()

# Fields whose presence marks a manifest copy as carrying a DELIBERATE,
# annotated governance decision (the documented signature of a /failure-autopsy
# or supersession correction -- see CLAUDE.md "evidence_direction"). A stale
# auto-emitted sibling carries none of these. This is the discriminator that
# tells the corrected copy from the stale one WITHOUT relying on mtime (which is
# meaningless in a git checkout, where it reflects checkout order, not edits).
_ANNOTATION_MARKER_FIELDS = (
    "evidence_direction_note",
    "degeneracy_reason",
    "superseded_by",
    "superseded_by_substrate",
)


def _is_annotated(manifest: dict[str, Any]) -> bool:
    """True when the manifest copy carries an explicit governance-decision marker."""
    if not isinstance(manifest, dict):
        return False
    for fld in _ANNOTATION_MARKER_FIELDS:
        if str(manifest.get(fld, "") or "").strip():
            return True
    return False


def _merge_flat_manifest_overrides(
    pack_manifest: dict[str, Any],
    flat_manifest: dict[str, Any],
) -> tuple[dict[str, Any], list[tuple[str, Any, Any]], bool]:
    """Overlay flat-sibling governance fields onto the pack WHEN the flat copy
    is the corrected one.

    Returns ``(merged_manifest, disagreements, applied)``:
      * ``disagreements`` -- list of ``(field, pack_value, flat_value)`` for
        every authoritative field the two copies differ on (computed regardless
        of whether the overlay fires, so callers can WARN on genuine conflicts).
      * ``applied`` -- True iff the flat overlay was actually applied.

    **Authority rule (the load-bearing decision).** A correction is, by the
    repo's own convention, written to the flat ``evidence/experiments/<run_id>``
    .json with an explanatory ``evidence_direction_note`` / ``degeneracy_reason``.
    The pack ``runs/<run_id>/manifest.json`` is the historical scoring source.
    So the flat copy overrides the pack ONLY when the flat copy is ANNOTATED and
    the pack copy is NOT -- i.e. the flat carries a deliberate correction the
    pack hasn't received yet (the 2026-06-14 MECH-171/057b/180 case). The
    inverse legacy shape -- pack annotated (manual supersession + note) while the
    flat is a stale earlier emission (the v3_exq_150-series) -- must NOT flip, so
    the overlay is suppressed there and the pack stays authoritative. When both
    or neither copy is annotated, the pack is retained (status quo: the indexer
    has always scored the pack); a both-annotated disagreement is surfaced via
    ``disagreements`` for manual reconciliation.

    Only fields PRESENT in the flat manifest are overlaid (key presence, not
    truthiness -- so an explicit ``non_degenerate: false`` overrides while an
    absent field leaves the pack value intact). A missing flat sibling
    (``flat_manifest == {}``) is a no-op, preserving legacy/synthetic handling.
    """
    if not isinstance(flat_manifest, dict) or not flat_manifest:
        return pack_manifest, [], False
    pack = pack_manifest if isinstance(pack_manifest, dict) else {}

    disagreements: list[tuple[str, Any, Any]] = []
    for fld in _FLAT_AUTHORITATIVE_FIELDS:
        if fld not in flat_manifest:
            continue
        flat_val = flat_manifest[fld]
        pack_val = pack.get(fld, _MISSING)
        if pack_val is _MISSING or pack_val != flat_val:
            disagreements.append(
                (fld, None if pack_val is _MISSING else pack_val, flat_val))

    # Unconditional provenance backfill (2026-07-16). machine_class / substrate_hash
    # / machine are pure PROVENANCE (never in _FLAT_DIRECTION_FIELDS -- they cannot
    # change how a run scores), yet a pre-2026-07-16 pack dropped them entirely
    # (build_runpack_docs did not map them), so the index read machine_class=null /
    # substrate_hash="" for every historical run even though the flat sibling
    # carried the always-core. Fill from the flat copy whenever the pack lacks OR
    # empties the field, regardless of the annotation gate below. This is a no-op
    # once the producer fix propagates (the pack then already carries them), and a
    # no-op for legacy flats that lack provenance. It does NOT set `applied` (that
    # flag guards the direction-field overlay + its WARNings) and never overwrites
    # a non-empty pack value.
    base = pack
    prov_filled: dict[str, Any] = {}
    for fld in _FLAT_PROVENANCE_BACKFILL_FIELDS:
        flat_val = flat_manifest.get(fld)
        if flat_val is None or str(flat_val).strip() == "":
            continue
        pack_val = pack.get(fld, _MISSING)
        if pack_val is _MISSING or str(pack_val or "").strip() == "":
            prov_filled[fld] = flat_val
    if prov_filled:
        base = {**pack, **prov_filled}

    apply_overlay = _is_annotated(flat_manifest) and not _is_annotated(pack)
    if not apply_overlay:
        return (base if prov_filled else pack_manifest), disagreements, False

    merged = dict(base)
    for fld in _FLAT_AUTHORITATIVE_FIELDS:
        if fld in flat_manifest:
            merged[fld] = flat_manifest[fld]
    return merged, disagreements, True


def _scan_runs(base_dir: Path, planning_criteria: dict[str, Any]) -> dict[str, list[RunRecord]]:
    by_experiment: dict[str, list[RunRecord]] = defaultdict(list)

    applicability = (
        planning_criteria.get("evidence_applicability", {})
        if isinstance(planning_criteria, dict)
        else {}
    )
    if not isinstance(applicability, dict):
        applicability = {}
    current_epoch = str(applicability.get("current_architecture_epoch", "")).strip()
    epoch_start_raw = str(applicability.get("epoch_start_utc", "")).strip()
    epoch_start: datetime | None = None
    if epoch_start_raw:
        try:
            epoch_start = _parse_timestamp_only(epoch_start_raw)
        except ValueError:
            epoch_start = None

    for manifest_path in sorted(base_dir.glob("**/runs/**/manifest.json")):
        run_dir = manifest_path.parent
        if run_dir.parent.name != "runs":
            continue
        experiment_type = run_dir.parent.parent.name

        # Early-exit for pre-epoch runs: parse timestamp from directory name without
        # reading the manifest file. Directory names follow YYYY-MM-DDTHHMMSSz_... format
        # (18 chars before the first underscore, e.g. 2026-02-15T145638Z).
        # This avoids iCloud-offloaded file reads for old synthetic runs.
        if epoch_start is not None:
            name = run_dir.name
            try:
                if (len(name) >= 18 and name[4] == "-" and name[7] == "-"
                        and name[10] == "T" and name[17] in ("Z", "z")):
                    dir_ts = datetime(
                        int(name[0:4]), int(name[5:7]), int(name[8:10]),
                        int(name[11:13]), int(name[13:15]), int(name[15:17]),
                        tzinfo=timezone.utc,
                    )
                    if dir_ts < epoch_start:
                        continue
            except (ValueError, IndexError):
                pass  # can't parse from name; fall through to read manifest

        manifest = _load_json(manifest_path)
        run_id = str(manifest.get("run_id", run_dir.name))

        # Flat-manifest authoritative override (2026-06-14). Governance /
        # failure-autopsy corrections land on evidence/experiments/<run_id>.json
        # (with an evidence_direction_note / degeneracy_reason), not this pack
        # copy. When the flat copy carries such an annotation and the pack does
        # not, the flat copy is the corrected one and its governance fields are
        # overlaid here so a flat-only correction is not silently ignored. The
        # inverse legacy shape (pack annotated, flat a stale earlier emission --
        # the v3_exq_150-series) is left untouched. A missing sibling => {} =>
        # no-op (legacy/synthetic runs without a flat sibling are untouched).
        flat_manifest = _load_json(base_dir / f"{run_id}.json")
        manifest, _flat_disagreements, _flat_applied = _merge_flat_manifest_overrides(
            manifest, flat_manifest)
        _dir_disagree = [d for d in _flat_disagreements if d[0] in _FLAT_DIRECTION_FIELDS]
        if _flat_applied:
            for fld, pack_val, flat_val in _dir_disagree:
                print(
                    f"WARNING: flat-manifest correction applied for {run_id}: "
                    f"'{fld}' pack={pack_val!r} -> flat={flat_val!r} (flat carries "
                    f"the governance annotation; pack copy is stale). Re-sync "
                    f"runs/{run_dir.name}/manifest.json to silence this."
                )
        elif _dir_disagree and _is_annotated(manifest) and _is_annotated(flat_manifest):
            # Both copies annotated but disagree: a genuine conflict. Retain the
            # pack (historical scoring source) and surface for manual reconcile.
            for fld, pack_val, flat_val in _dir_disagree:
                print(
                    f"WARNING: flat/pack BOTH annotated but disagree for {run_id}: "
                    f"'{fld}' pack={pack_val!r} flat={flat_val!r} -- pack retained; "
                    f"reconcile manually."
                )

        timestamp_raw, timestamp = _parse_timestamp(
            manifest.get("timestamp_utc"), run_id or run_dir.name
        )
        architecture_epoch = str(manifest.get("architecture_epoch", "")).strip()
        if not architecture_epoch and current_epoch and epoch_start and timestamp >= epoch_start:
            architecture_epoch = current_epoch

        artifacts = manifest.get("artifacts", {}) if isinstance(manifest, dict) else {}
        metrics_rel = artifacts.get("metrics_path", "metrics.json")
        summary_rel = artifacts.get("summary_path", "summary.md")
        adapter_signals_rel = artifacts.get("adapter_signals_path")

        metrics_path = run_dir / metrics_rel
        summary_path = run_dir / summary_rel
        adapter_signals_path: Path | None = None
        if isinstance(adapter_signals_rel, str) and adapter_signals_rel.strip():
            adapter_signals_path = run_dir / adapter_signals_rel.strip()

        metrics_doc = _load_json(metrics_path)
        values = metrics_doc.get("values", {}) if isinstance(metrics_doc, dict) else {}
        metrics: dict[str, float] = {}
        if isinstance(values, dict):
            for k, v in values.items():
                if isinstance(v, (int, float)):
                    metrics[k] = float(v)

        status = str(manifest.get("status") or manifest.get("outcome", "UNKNOWN")).upper()
        signatures = manifest.get("failure_signatures", [])
        if not isinstance(signatures, list):
            signatures = []
        claim_ids_raw = manifest.get("claim_ids_tested") or manifest.get("claim_ids", [])
        if not isinstance(claim_ids_raw, list):
            claim_ids_raw = []
        claim_ids_tested = [str(x).strip() for x in claim_ids_raw if str(x).strip()]
        evidence_class = str(manifest.get("evidence_class", "simulation")).strip() or "simulation"
        evidence_direction = _normalize_direction(manifest.get("evidence_direction"))
        # Per-claim direction overrides: {"ARC-024": "supports", "ARC-026": "weakens"}.
        # When present for a given claim_id, replaces the run-level evidence_direction
        # for that claim only.  Keys not present fall back to the run-level direction.
        raw_per_claim = manifest.get("evidence_direction_per_claim") or {}
        evidence_direction_per_claim: dict[str, str] = {}
        if isinstance(raw_per_claim, dict):
            for cid, val in raw_per_claim.items():
                normalized = _normalize_direction(val)
                if normalized != "unknown":  # skip placeholder/empty entries
                    evidence_direction_per_claim[str(cid)] = normalized
        # direction_explicitly_set: True when manifest has an evidence_direction_note,
        # meaning the direction was a deliberate manual override and should not be
        # auto-inferred (e.g. design-inconclusive experiments marked "unknown").
        direction_explicitly_set = bool(manifest.get("evidence_direction_note"))
        experiment_purpose = str(manifest.get("experiment_purpose", "evidence")).strip() or "evidence"
        interpretation_label, adjudication = _compute_adjudication(
            manifest.get("interpretation"), status, experiment_purpose)
        # Non-gating sibling of the adjudicating preconditions[]. Computed from the
        # same manifest but kept strictly OUT of `adjudication` above -- surfacing
        # only. See _recorded_precondition_findings.
        recorded_preconditions_unmet = _recorded_precondition_findings(
            manifest.get("interpretation"))
        _interp_for_note = manifest.get("interpretation")
        preconditions_scope_note = str(
            (_interp_for_note.get("preconditions_scope_note", "")
             if isinstance(_interp_for_note, dict) else "") or "").strip()
        evidence_level = _normalize_evidence_level(manifest.get("evidence_level"))
        # Substrate-staleness gate: honor manually-set manifest fields that mark
        # this run as mechanistically stale after a downstream substrate change.
        # `pending_retest_after_substrate` accepts a bool or truthy string;
        # `superseded_by_substrate` is a "<SD-id>@<YYYY-MM-DD>" reference string.
        pending_retest_after_substrate = _coerce_bool(
            manifest.get("pending_retest_after_substrate", False))
        superseded_by_substrate = str(
            manifest.get("superseded_by_substrate", "") or "").strip()
        # Per-claim staleness: de-weight only the named claim(s) in a multi-claim
        # manifest. `pending_retest_after_substrate_per_claim` is a list of claim
        # ids; `superseded_by_substrate_per_claim` is {claim_id: "<id>@<date>"}.
        raw_pr_pc = manifest.get("pending_retest_after_substrate_per_claim") or []
        pending_retest_after_substrate_per_claim = (
            [str(x).strip() for x in raw_pr_pc if str(x).strip()]
            if isinstance(raw_pr_pc, list) else [])
        raw_sb_pc = manifest.get("superseded_by_substrate_per_claim") or {}
        superseded_by_substrate_per_claim = (
            {str(k): str(v).strip() for k, v in raw_sb_pc.items() if str(v).strip()}
            if isinstance(raw_sb_pc, dict) else {})
        # Non-degeneracy gate: only an EXPLICIT False excludes; absent/None is a
        # no-op (we must not treat the silent majority of legacy manifests, which
        # carry no flag, as degenerate). `non_degenerate_per_claim` keeps only the
        # entries explicitly set to False.
        raw_nd = manifest.get("non_degenerate", None)
        non_degenerate = _coerce_bool(raw_nd) if raw_nd is not None else None
        raw_nd_pc = manifest.get("non_degenerate_per_claim") or {}
        non_degenerate_per_claim = (
            {str(k): _coerce_bool(v) for k, v in raw_nd_pc.items()
             if _coerce_bool(v) is False}
            if isinstance(raw_nd_pc, dict) else {})
        degeneracy_reason = str(manifest.get("degeneracy_reason", "") or "").strip()
        # Experimental Recording Standard always-core (2026-07-12): surfaced for
        # queryability, NOT scored. substrate_hash is the reuse prerequisite;
        # label_balance is the training/eval class-balance guard (047m false-clear
        # fix). Read defensively -- absent on the legacy corpus (a no-op default).
        substrate_hash = str(manifest.get("substrate_hash", "") or "").strip()
        raw_label_balance = manifest.get("label_balance") or {}
        label_balance = raw_label_balance if isinstance(raw_label_balance, dict) else {}
        # machine / machine_class read AFTER the flat-provenance backfill above, so
        # a thin pre-2026-07-16 pack still surfaces the flat sibling's provenance.
        machine = str(manifest.get("machine", "") or "").strip()
        machine_class = str(manifest.get("machine_class", "") or "").strip()

        by_experiment[experiment_type].append(
            RunRecord(
                experiment_type=experiment_type,
                run_id=run_id,
                timestamp_raw=timestamp_raw,
                timestamp=timestamp,
                manifest_path=manifest_path,
                metrics_path=metrics_path,
                summary_path=summary_path,
                manifest_status=status,
                failure_signatures=[str(x) for x in signatures],
                metrics=metrics,
                claim_ids_tested=claim_ids_tested,
                evidence_class=evidence_class,
                evidence_direction=evidence_direction,
                evidence_direction_per_claim=evidence_direction_per_claim,
                direction_explicitly_set=direction_explicitly_set,
                experiment_purpose=experiment_purpose,
                interpretation_label=interpretation_label,
                adjudication=adjudication,
                recorded_preconditions_unmet=recorded_preconditions_unmet,
                preconditions_scope_note=preconditions_scope_note,
                architecture_epoch=architecture_epoch,
                adapter_signals_path=adapter_signals_path,
                evidence_level=evidence_level,
                pending_retest_after_substrate=pending_retest_after_substrate,
                superseded_by_substrate=superseded_by_substrate,
                pending_retest_after_substrate_per_claim=pending_retest_after_substrate_per_claim,
                superseded_by_substrate_per_claim=superseded_by_substrate_per_claim,
                non_degenerate=non_degenerate,
                non_degenerate_per_claim=non_degenerate_per_claim,
                degeneracy_reason=degeneracy_reason,
                substrate_hash=substrate_hash,
                label_balance=label_balance,
                machine=machine,
                machine_class=machine_class,
            )
        )

    for runs in by_experiment.values():
        runs.sort(key=lambda r: (r.timestamp, r.run_id))
    return by_experiment


def _detect_and_mark_duplicate_emissions(
    by_experiment: dict[str, list[RunRecord]],
) -> list[dict[str, Any]]:
    """Auto-mark byte-identical-output duplicate emissions as superseded.

    Within each experiment_type, runs that share an identical numeric-metrics
    signature are treated as duplicate emissions of the same underlying run
    (typical causes: runner re-emission after restart, deterministic re-runs
    from regex-bug-period queue replays). The latest emission is kept as
    canonical; earlier emissions are mutated in-memory to
    evidence_direction='superseded' so the existing scoring loop excludes them.

    On-disk manifests are NOT modified -- the user's manual supersession
    decisions (visible via evidence_direction_note) remain authoritative. If
    any run in an experiment_type already has evidence_direction='superseded',
    the cluster is assumed hand-resolved and the auto-detector backs off
    entirely.

    Returns a list of warning records (one per auto-marked manifest) for
    diagnostic logging.
    """
    warnings: list[dict[str, Any]] = []
    for experiment_type, runs in by_experiment.items():
        if len(runs) < 2:
            continue
        # Back off if user has already hand-resolved any cluster in this
        # experiment_type -- avoids second-guessing manual decisions.
        if any(r.evidence_direction == "superseded" for r in runs):
            continue
        by_signature: dict[str, list[RunRecord]] = defaultdict(list)
        for run in runs:
            if not run.metrics:
                continue  # cannot fingerprint without numeric metrics
            sig_src = json.dumps(sorted(run.metrics.items()), default=str)
            sig = hashlib.sha1(sig_src.encode()).hexdigest()[:12]
            by_signature[sig].append(run)
        for sig, dup in by_signature.items():
            if len(dup) < 2:
                continue
            dup_sorted = sorted(dup, key=lambda r: (r.timestamp, r.run_id))
            canonical = dup_sorted[-1]
            for stale in dup_sorted[:-1]:
                stale.evidence_direction = "superseded"
                # Per-claim direction overrides become moot once superseded.
                stale.evidence_direction_per_claim = {}
                span_min = (canonical.timestamp - stale.timestamp).total_seconds() / 60.0
                warnings.append(
                    {
                        "experiment_type": experiment_type,
                        "duplicate_run_id": stale.run_id,
                        "canonical_run_id": canonical.run_id,
                        "signature_sha1": sig,
                        "span_minutes": span_min,
                    }
                )
    return warnings


def _scan_literature(
    literature_root: Path,
    planning_criteria: dict[str, Any],
) -> dict[str, list[LiteratureRecord]]:
    by_literature: dict[str, list[LiteratureRecord]] = defaultdict(list)
    if not literature_root.exists():
        return by_literature

    applicability = (
        planning_criteria.get("evidence_applicability", {})
        if isinstance(planning_criteria, dict)
        else {}
    )
    if not isinstance(applicability, dict):
        applicability = {}
    current_epoch = str(applicability.get("current_architecture_epoch", "")).strip()
    epoch_start_raw = str(applicability.get("epoch_start_utc", "")).strip()
    epoch_start: datetime | None = None
    if epoch_start_raw:
        try:
            epoch_start = _parse_timestamp_only(epoch_start_raw)
        except ValueError:
            epoch_start = None

    for record_path in sorted(literature_root.glob("**/entries/**/record.json")):
        entry_dir = record_path.parent
        if entry_dir.parent.name != "entries":
            continue
        literature_type = entry_dir.parent.parent.name

        record = _load_json(record_path)
        entry_id = str(record.get("entry_id", entry_dir.name))
        timestamp_raw, timestamp = _parse_timestamp(
            record.get("timestamp_utc"), entry_id or entry_dir.name
        )

        claim_ids_raw = record.get("claim_ids_tested") or record.get("claim_ids", [])
        if not isinstance(claim_ids_raw, list):
            claim_ids_raw = []
        claim_ids_tested = [str(x).strip() for x in claim_ids_raw if str(x).strip()]

        evidence_class = str(record.get("evidence_class", "review")).strip() or "review"
        evidence_direction = _normalize_direction(record.get("evidence_direction"))
        architecture_epoch = str(record.get("architecture_epoch", "")).strip()
        if not architecture_epoch and current_epoch and epoch_start and timestamp >= epoch_start:
            architecture_epoch = current_epoch
        confidence = _normalize_confidence(record.get("confidence"), default=0.6)
        confidence_rationale = str(record.get("confidence_rationale", "")).strip()

        signatures = record.get("failure_signatures", [])
        if not isinstance(signatures, list):
            signatures = []

        summary_rel = str(record.get("summary_path", "summary.md"))
        summary_path = entry_dir / summary_rel

        by_literature[literature_type].append(
            LiteratureRecord(
                literature_type=literature_type,
                entry_id=entry_id,
                timestamp_raw=timestamp_raw,
                timestamp=timestamp,
                record_path=record_path,
                summary_path=summary_path,
                claim_ids_tested=claim_ids_tested,
                evidence_class=evidence_class,
                evidence_direction=evidence_direction,
                architecture_epoch=architecture_epoch,
                confidence=confidence,
                confidence_rationale=confidence_rationale,
                failure_signatures=[str(x) for x in signatures],
            )
        )

    for entries in by_literature.values():
        entries.sort(key=lambda e: (e.timestamp, e.entry_id))
    return by_literature


def _criteria_for_experiment(stop_criteria: dict[str, Any], experiment_type: str) -> dict[str, Any]:
    default = stop_criteria.get("default", {})
    experiments = stop_criteria.get("experiments", {})
    specific = experiments.get(experiment_type, {}) if isinstance(experiments, dict) else {}
    merged: dict[str, Any] = {"fail_if": []}

    default_fail_if = default.get("fail_if", []) if isinstance(default, dict) else []
    specific_fail_if = specific.get("fail_if", []) if isinstance(specific, dict) else []

    if isinstance(default_fail_if, list):
        merged["fail_if"].extend(default_fail_if)
    if isinstance(specific_fail_if, list):
        merged["fail_if"].extend(specific_fail_if)
    return merged


def _adapter_signature_for_errors(errors: list[str]) -> str:
    detail = " ".join(errors).lower()
    if "missing file" in detail:
        return "contract:jepa_adapter_signals_missing"
    if "schema_version" in detail:
        return "contract:jepa_adapter_signals_version"
    return "contract:jepa_adapter_signals_invalid"


def _validate_jepa_adapter_signals(run: RunRecord) -> tuple[str, list[str]]:
    if run.adapter_signals_path is None:
        return "n/a", []

    path = run.adapter_signals_path
    if not path.exists():
        return "FAIL", [f"missing file: {path.name}"]

    try:
        doc = _load_json(path)
    except RuntimeError as exc:
        return "FAIL", [str(exc)]

    errors: list[str] = []

    if not isinstance(doc, dict):
        return "FAIL", ["root must be an object"]

    if doc.get("schema_version") != ADAPTER_SCHEMA_VERSION:
        errors.append(f"schema_version must be `{ADAPTER_SCHEMA_VERSION}`")

    run_id = str(doc.get("run_id", "")).strip()
    if run_id != run.run_id:
        errors.append(f"run_id mismatch (`{run_id}` != `{run.run_id}`)")

    experiment_type = str(doc.get("experiment_type", "")).strip()
    if experiment_type != run.experiment_type:
        errors.append(
            f"experiment_type mismatch (`{experiment_type}` != `{run.experiment_type}`)"
        )

    adapter = doc.get("adapter")
    if not isinstance(adapter, dict):
        errors.append("adapter object missing")
    else:
        if not str(adapter.get("name", "")).strip():
            errors.append("adapter.name missing")
        if not str(adapter.get("version", "")).strip():
            errors.append("adapter.version missing")

    stream_presence = doc.get("stream_presence")
    if not isinstance(stream_presence, dict):
        errors.append("stream_presence object missing")
        stream_presence = {}

    for key in ("z_t", "z_hat", "pe_latent", "trace_context_mask_ids"):
        if stream_presence.get(key) is not True:
            errors.append(f"stream_presence.{key} must be true")

    uncertainty_present = bool(stream_presence.get("uncertainty_latent"))
    trace_action_token = stream_presence.get("trace_action_token")
    if not isinstance(trace_action_token, bool):
        errors.append("stream_presence.trace_action_token must be boolean")

    pe_latent_fields = doc.get("pe_latent_fields")
    if not isinstance(pe_latent_fields, list):
        errors.append("pe_latent_fields must be an array")
        pe_latent_fields = []
    pe_fields = {str(x) for x in pe_latent_fields}
    missing_pe = sorted(ADAPTER_REQUIRED_PE_FIELDS - pe_fields)
    if missing_pe:
        errors.append(f"pe_latent_fields missing: {', '.join(missing_pe)}")

    uncertainty_estimator = str(doc.get("uncertainty_estimator", "")).strip()
    if uncertainty_estimator not in ADAPTER_ALLOWED_UNCERTAINTY:
        errors.append(
            "uncertainty_estimator must be one of: "
            + ", ".join(sorted(ADAPTER_ALLOWED_UNCERTAINTY))
        )
    if uncertainty_present and uncertainty_estimator == "none":
        errors.append("uncertainty_latent=true requires uncertainty_estimator != none")

    signal_metrics = doc.get("signal_metrics")
    if not isinstance(signal_metrics, dict):
        errors.append("signal_metrics object missing")
        signal_metrics = {}

    missing_metrics = sorted(ADAPTER_REQUIRED_SIGNAL_METRICS - set(signal_metrics.keys()))
    if missing_metrics:
        errors.append(f"signal_metrics missing: {', '.join(missing_metrics)}")

    for metric in ADAPTER_REQUIRED_SIGNAL_METRICS:
        value = signal_metrics.get(metric)
        if not isinstance(value, (int, float)):
            errors.append(f"signal_metrics.{metric} must be numeric")

    for bounded in ("latent_residual_coverage_rate", "precision_input_completeness_rate"):
        value = signal_metrics.get(bounded)
        if isinstance(value, (int, float)) and not (0.0 <= float(value) <= 1.0):
            errors.append(f"signal_metrics.{bounded} must be in [0,1]")

    if uncertainty_present:
        value = signal_metrics.get("latent_uncertainty_calibration_error")
        if not isinstance(value, (int, float)):
            errors.append(
                "signal_metrics.latent_uncertainty_calibration_error required when uncertainty_latent=true"
            )

    return ("FAIL", errors) if errors else ("PASS", [])


def _evaluate_runs(runs: list[RunRecord], criteria: dict[str, Any]) -> None:
    prev_metrics: dict[str, float] | None = None
    for run in runs:
        fail_hits: list[StopHit] = []
        for rule in criteria.get("fail_if", []):
            if not isinstance(rule, dict):
                continue
            metric = rule.get("metric")
            op = rule.get("op")
            threshold = rule.get("threshold")
            if not isinstance(metric, str) or not isinstance(op, str):
                continue
            if not isinstance(threshold, (int, float)):
                continue

            value = run.metrics.get(metric)
            if value is None:
                continue
            if _compare(value, op, float(threshold)):
                fail_hits.append(
                    StopHit(
                        metric=metric,
                        op=op,
                        threshold=float(threshold),
                        value=value,
                    )
                )

        run.fail_hits = fail_hits
        criteria_fail = bool(fail_hits)
        manifest_fail = run.manifest_status == "FAIL"
        run.final_status = "FAIL" if (criteria_fail or manifest_fail) else "PASS"

        if prev_metrics:
            for metric, value in run.metrics.items():
                if metric in prev_metrics:
                    run.deltas[metric] = value - prev_metrics[metric]
        prev_metrics = run.metrics

        if criteria_fail:
            for hit in fail_hits:
                sig = f"stop:{hit.metric}{hit.op}{_fmt_number(hit.threshold)}"
                if sig not in run.failure_signatures:
                    run.failure_signatures.append(sig)

        adapter_status, adapter_errors = _validate_jepa_adapter_signals(run)
        run.adapter_contract_status = adapter_status
        run.adapter_contract_errors = adapter_errors
        if adapter_status == "FAIL":
            run.final_status = "FAIL"
            sig = _adapter_signature_for_errors(adapter_errors)
            if sig not in run.failure_signatures:
                run.failure_signatures.append(sig)


def _select_key_metrics(runs: list[RunRecord], criteria: dict[str, Any], limit: int = 6) -> list[str]:
    metrics: list[str] = []
    for rule in criteria.get("fail_if", []):
        metric = rule.get("metric") if isinstance(rule, dict) else None
        if isinstance(metric, str) and metric not in metrics:
            metrics.append(metric)

    counter: Counter[str] = Counter()
    for run in runs:
        counter.update(run.metrics.keys())

    for metric, _ in counter.most_common():
        if metric not in metrics:
            metrics.append(metric)
        if len(metrics) >= limit:
            break
    return metrics[:limit]


def _ensure_experiment_template(experiment_dir: Path, experiment_type: str) -> Path:
    doc_path = experiment_dir / "experiment.md"
    if doc_path.exists():
        return doc_path

    template = f"""# Experiment: {experiment_type}

## What it tests

- TODO: describe the invariant or mechanism this experiment validates.

## Failure modes it detects

- TODO: list concrete failure signatures this experiment is expected to surface.

## Design implications

{START_MARKER}
No generated implications yet.
{END_MARKER}
"""
    doc_path.write_text(template, encoding="utf-8")
    return doc_path


def _replace_between_markers(text: str, replacement: str) -> str:
    if START_MARKER in text and END_MARKER in text:
        before, rest = text.split(START_MARKER, 1)
        _, after = rest.split(END_MARKER, 1)
        return f"{before}{START_MARKER}\n{replacement}\n{END_MARKER}{after}"

    return text.rstrip() + f"\n\n{START_MARKER}\n{replacement}\n{END_MARKER}\n"


def _build_design_implications(runs: list[RunRecord], lookback_failures: int) -> tuple[str, list[str]]:
    failures = [r for r in runs if r.final_status == "FAIL"]
    if not failures:
        return "No recent FAIL runs. Keep monitoring key stop metrics.", []

    recent = failures[-lookback_failures:]
    signature_counter: Counter[str] = Counter()
    last_seen_run: dict[str, str] = {}

    for run in failures:
        for sig in run.failure_signatures:
            signature_counter[sig] += 1
            last_seen_run[sig] = run.run_id

    lines: list[str] = []
    lines.append("Recent failure runs:")
    for run in reversed(recent):
        signatures = ", ".join(run.failure_signatures) if run.failure_signatures else "none"
        lines.append(f"- `{run.run_id}` at `{run.timestamp_raw}` signatures: {signatures}")

    lines.append("")
    lines.append("Recurring signatures:")
    for sig, count in signature_counter.most_common(8):
        lines.append(f"- `{sig}` occurred in {count} FAIL run(s); latest `{last_seen_run[sig]}`")

    todo_items: list[str] = []
    for sig, count in signature_counter.most_common(6):
        todo_items.append(
            f"[ ] Investigate signature `{sig}` ({count} FAIL run(s), latest `{last_seen_run[sig]}`)."
        )

    lines.append("")
    lines.append("Suggested design TODOs:")
    lines.extend(f"- {todo}" for todo in todo_items)

    return "\n".join(lines), todo_items


def _write_experiment_index(
    experiment_dir: Path,
    experiment_type: str,
    runs: list[RunRecord],
    key_metrics: list[str],
    generated_at: str,
) -> None:
    lines: list[str] = []
    lines.append(f"# Experiment Index: {experiment_type}")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("- Experiment profile: `experiment.md`")
    lines.append("- Stop criteria: `../../stop_criteria.v1.yaml`")
    lines.append("")

    if not runs:
        lines.append("No runs discovered.")
    else:
        lines.append("## Runs")
        lines.append("")
        lines.append(
            "| run_id | timestamp_utc | status | key metrics | deltas vs previous | stop-criteria hits | adapter contract | summary |"
        )
        lines.append(
            "|---|---|---|---|---|---|---|---|"
        )

        for run in reversed(runs):
            status = f"**{run.final_status}**" if run.final_status == "FAIL" else run.final_status
            key_values = []
            delta_values = []
            for metric in key_metrics:
                if metric in run.metrics:
                    key_values.append(f"{metric}={_fmt_number(run.metrics[metric])}")
                if metric in run.deltas:
                    delta_values.append(f"{metric}:{_fmt_delta(run.deltas[metric])}")

            stop_hits = "; ".join(hit.render() for hit in run.fail_hits) if run.fail_hits else "-"
            adapter_status = run.adapter_contract_status
            if adapter_status == "FAIL":
                adapter_status = "**FAIL**"
                if run.adapter_contract_errors:
                    adapter_status += "<br>" + "<br>".join(run.adapter_contract_errors[:2])
            elif adapter_status == "PASS":
                adapter_status = "PASS"
            else:
                adapter_status = "-"
            summary_rel = run.summary_path.relative_to(experiment_dir).as_posix()
            metrics_rel = run.metrics_path.relative_to(experiment_dir).as_posix()
            manifest_rel = run.manifest_path.relative_to(experiment_dir).as_posix()
            adapter_rel = (
                run.adapter_signals_path.relative_to(experiment_dir).as_posix()
                if run.adapter_signals_path
                else None
            )

            summary_link = f"[`summary`]({summary_rel})"
            summary_link += f" / [`manifest`]({manifest_rel}) / [`metrics`]({metrics_rel})"
            if adapter_rel:
                summary_link += f" / [`adapter`]({adapter_rel})"

            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{run.run_id}`",
                        f"`{run.timestamp_raw}`",
                        status,
                        "<br>".join(key_values) if key_values else "-",
                        "<br>".join(delta_values) if delta_values else "-",
                        stop_hits,
                        adapter_status,
                        summary_link,
                    ]
                )
                + " |"
            )

    lines.append("")
    (experiment_dir / "INDEX.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _write_top_level_index(
    base_dir: Path,
    by_experiment: dict[str, list[RunRecord]],
    by_literature: dict[str, list[LiteratureRecord]],
    decision_log_count: int,
    backlog_count: int,
    proposal_count: int,
    architecture_gap_count: int,
    generated_at: str,
) -> None:
    lines: list[str] = []
    lines.append("# Experimental Evidence Index")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("This index is generated by `scripts/build_experiment_indexes.py`.")
    lines.append("")
    lines.append("| experiment_type | latest status | latest run | fails / total | links |")
    lines.append("|---|---|---|---|---|")

    for exp_type in sorted(by_experiment.keys()):
        runs = by_experiment[exp_type]
        total = len(runs)
        fails = sum(1 for r in runs if r.final_status == "FAIL")
        latest = runs[-1] if runs else None
        latest_status = latest.final_status if latest else "n/a"
        latest_status_rendered = (
            f"**{latest_status}**" if latest_status == "FAIL" else latest_status
        )
        latest_run = f"`{latest.run_id}`" if latest else "-"
        links = f"[`INDEX`](./{exp_type}/INDEX.md) / [`profile`](./{exp_type}/experiment.md)"
        lines.append(
            f"| `{exp_type}` | {latest_status_rendered} | {latest_run} | {fails}/{total} | {links} |"
        )

    if not by_experiment:
        lines.append("| _none_ | - | - | - | - |")

    lines.append("")
    lines.append("## Cross-Evidence Outputs")
    lines.append("")
    lines.append("- TODO queue: `TODOs.md`")
    lines.append("- Stop criteria config: `stop_criteria.v1.yaml`")
    lines.append("- Decision criteria config: `decision_criteria.v1.yaml`")
    lines.append("- Legacy adapter signal schema: `schemas/v1/jepa_adapter_signals.v1.json`")
    lines.append("- Claim-evidence matrix: `claim_evidence.v1.json`")
    lines.append("- Conflicts report: `conflicts.md`")
    lines.append("- Promotion/demotion recommendations: `promotion_demotion_recommendations.md`")
    lines.append(f"- Literature index: `../literature/INDEX.md` ({sum(len(v) for v in by_literature.values())} entries)")
    lines.append(f"- Persistent decision log: `../decisions/decision_log.v1.jsonl` ({decision_log_count} entries)")
    lines.append("- Decision state snapshot: `../decisions/decision_state.v1.json`")
    lines.append(f"- Evidence backlog: `../planning/evidence_backlog.v1.json` ({backlog_count} item(s))")
    lines.append(f"- Experiment proposals: `../planning/experiment_proposals.v1.json` ({proposal_count} item(s))")
    lines.append(
        f"- Architecture gap register: `../planning/architecture_gap_register.v1.json` ({architecture_gap_count} item(s))"
    )

    (base_dir / "INDEX.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _write_literature_index(
    literature_root: Path,
    by_literature: dict[str, list[LiteratureRecord]],
    generated_at: str,
) -> None:
    lines: list[str] = []
    lines.append("# Literature Evidence Index")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("| literature_type | latest entry | total entries | links |")
    lines.append("|---|---|---|---|")

    if not by_literature:
        lines.append("| _none_ | - | 0 | - |")
    else:
        for literature_type in sorted(by_literature.keys()):
            entries = by_literature[literature_type]
            latest = entries[-1]
            latest_link = latest.record_path.relative_to(literature_root).as_posix()
            summary_rel = latest.summary_path.relative_to(literature_root).as_posix()
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{literature_type}`",
                        f"[`{latest.entry_id}`]({latest_link})",
                        str(len(entries)),
                        f"[`summary`]({summary_rel})",
                    ]
                )
                + " |"
            )

    lines.append("")
    lines.append("This index is generated by `evidence/experiments/scripts/build_experiment_indexes.py`.")
    literature_root.mkdir(parents=True, exist_ok=True)
    (literature_root / "INDEX.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _experimental_entry_confidence(run: RunRecord, inferred_direction: str) -> tuple[float, str]:
    confidence = 0.6
    rationale_bits: list[str] = []

    if inferred_direction in ("non_contributory", "inconclusive"):
        confidence = 0.0
        rationale_bits.append(f"{inferred_direction} -- excluded from scoring")
    elif inferred_direction == "mixed":
        confidence = 0.5
        rationale_bits.append("mixed direction")
    elif inferred_direction == "unknown":
        confidence = 0.45
        rationale_bits.append("unknown direction")
    elif inferred_direction == "supports" and run.final_status == "PASS":
        confidence = 0.75
        rationale_bits.append("PASS with supporting direction")
    elif inferred_direction == "weakens" and run.final_status == "FAIL":
        confidence = 0.75
        rationale_bits.append("FAIL with weakening direction")
    else:
        confidence = 0.55
        rationale_bits.append("direction/status mismatch")

    if run.fail_hits and inferred_direction in {"mixed", "unknown", "supports"}:
        confidence = max(0.4, confidence - 0.1)
        rationale_bits.append("stop criteria triggered")

    return _normalize_confidence(confidence), "; ".join(rationale_bits)


def _recency_score(entries: list[dict[str, Any]], now: datetime, horizon_days: int) -> float:
    if not entries:
        return 0.0
    parsed: list[datetime] = []
    for e in entries:
        raw = str(e.get("timestamp_utc", "")).strip()
        if not raw:
            # Explicit unknown (see _parse_timestamp): contributes no recency
            # signal rather than a fabricated one.
            continue
        try:
            parsed.append(_parse_timestamp_only(raw))
        except ValueError:
            continue
    if not parsed:
        return 0.0
    latest_ts = max(parsed)
    age_days = max(0.0, (now - latest_ts).total_seconds() / 86400.0)
    score = max(0.0, 1.0 - (age_days / float(horizon_days)))
    return round(score, 3)


def _direction_conflict_ratio(direction_counts: dict[str, int]) -> float:
    supports = int(direction_counts.get("supports", 0))
    weakens = int(direction_counts.get("weakens", 0))
    directional_total = supports + weakens
    if directional_total == 0:
        return 0.0
    # 0.0 => no conflict, 1.0 => perfectly split support/weakening evidence.
    return round((2.0 * min(supports, weakens)) / float(directional_total), 3)


# --- Option E shadow regime -------------------------------------------------
# Lit and exp evidence play different epistemic roles: exp is load-bearing for
# promotion, lit is sanity-check + knowledge-harvest. Phase 1 surfaces the
# decoupled view as additional fields without changing any gates.
# Thresholds match those used by scripts/generate_option_e_shadow.py.
EVIDENCE_QUADRANT_HIGH_EXP = 0.62  # candidate->provisional gate
EVIDENCE_QUADRANT_HIGH_LIT = 0.55


def _evidence_quadrant(exp_conf: float, lit_conf: float, n_exp: int, n_lit: int) -> str:
    has_exp = n_exp > 0 and exp_conf >= EVIDENCE_QUADRANT_HIGH_EXP
    has_lit = n_lit > 0 and lit_conf >= EVIDENCE_QUADRANT_HIGH_LIT
    if has_exp and has_lit:
        return "confirmed_established"
    if has_exp and not has_lit:
        return "novel_discovery"
    if not has_exp and has_lit:
        return "plausible_unproven"
    return "speculative"


# --- Beta-Binomial per-node posterior (epistemic overlay Phase 1) ------------
# Explicit probabilistic per-node score over P(claim is supported): the
# magic-number weighted-linear heuristic's implicit point estimate is augmented
# (NOT replaced -- exp_conf/lit_conf stay) with a Beta posterior mean + credible
# interval. EXP and LIT stay decoupled (two posteriors, never fused). This
# posterior IS the unary potential a Phase-2 factor-graph/MRF consumes unchanged.
# Plan: evidence/planning/epistemic_overlay_plan.md sec 2. Uncalibrated by design.
#
# Self-contained regularized incomplete beta -- no scipy dependency (the indexer
# runs in the governance pipeline with stdlib + torch only). Numerical-Recipes
# style continued fraction; quantile by bisection (I_x is monotone in x).
_POSTERIOR_PRIOR_A = 1.0
_POSTERIOR_PRIOR_B = 1.0
_POSTERIOR_CI_MASS = 0.95
_POSTERIOR_RECENCY_FLOOR = 0.25
_POSTERIOR_HORIZON_EXP = 90
_POSTERIOR_HORIZON_LIT = 365


def _betacf(a: float, b: float, x: float) -> float:
    max_iter = 200
    eps = 3.0e-12
    fpmin = 1.0e-300
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < fpmin:
        d = fpmin
    d = 1.0 / d
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            break
    return h


def _betai(a: float, b: float, x: float) -> float:
    """Regularized incomplete beta I_x(a, b) in [0, 1]."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    bt = math.exp(lbeta + a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _betacf(a, b, x) / a
    return 1.0 - bt * _betacf(b, a, 1.0 - x) / b


def _beta_quantile(a: float, b: float, p: float) -> float:
    """Inverse regularized incomplete beta by bisection."""
    if p <= 0.0:
        return 0.0
    if p >= 1.0:
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if _betai(a, b, mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def _beta_binomial_posterior(
    entries: list[dict[str, Any]],
    now: datetime,
    horizon_days: int,
) -> dict[str, Any]:
    """Beta posterior over P(supported) from directional evidence.

    supports -> alpha, weakens -> beta, mixed -> split; unknown / non_contributory
    / inconclusive / superseded are excluded (matches the existing scoring
    exclusions). Per-entry weight = quality(entry confidence) * recency, with
    recency = max(floor, 1 - age/horizon). Uniform Beta(1,1) prior -- deliberately
    weak, so little evidence pulls the mean toward 0.5 (2 entries must not look
    like 40). Returns mean + equal-tailed credible interval. Not yet calibrated.
    """
    a = _POSTERIOR_PRIOR_A
    b = _POSTERIOR_PRIOR_B
    sup_w = 0.0
    wk_w = 0.0
    n_used = 0
    for e in entries:
        direction = str(e.get("evidence_direction", "unknown"))
        if direction not in ("supports", "weakens", "mixed"):
            continue
        quality = float(e.get("confidence", 0.5) or 0.0)
        if quality <= 0.0:
            continue
        try:
            ts = _parse_timestamp_only(str(e.get("timestamp_utc", "")))
            age_days = max(0.0, (now - ts).total_seconds() / 86400.0)
            recency = max(_POSTERIOR_RECENCY_FLOOR, 1.0 - (age_days / float(horizon_days)))
        except (ValueError, TypeError):
            recency = _POSTERIOR_RECENCY_FLOOR
        w = quality * recency
        if direction == "supports":
            sup_w += w
        elif direction == "weakens":
            wk_w += w
        else:  # mixed
            sup_w += 0.5 * w
            wk_w += 0.5 * w
        n_used += 1
    a += sup_w
    b += wk_w
    mean = a / (a + b)
    lo_p = (1.0 - _POSTERIOR_CI_MASS) / 2.0
    hi_p = 1.0 - lo_p
    return {
        "mean": round(mean, 4),
        "ci_low": round(_beta_quantile(a, b, lo_p), 4),
        "ci_high": round(_beta_quantile(a, b, hi_p), 4),
        "alpha": round(a, 4),
        "beta": round(b, 4),
        "n_support_w": round(sup_w, 4),
        "n_weaken_w": round(wk_w, 4),
        "n_entries": n_used,
    }


def _posterior_model_metadata() -> dict[str, Any]:
    """Matrix-level provenance for the per-node posteriors. The calibration note
    is load-bearing: there is no resolved-claim validation set yet, so these are
    model-based, not calibrated. Do not overstate rigour downstream."""
    return {
        "family": "beta-binomial",
        "prior": f"Beta({_POSTERIOR_PRIOR_A:g},{_POSTERIOR_PRIOR_B:g})",
        "ci_mass": _POSTERIOR_CI_MASS,
        "recency_horizon_days": {"exp": _POSTERIOR_HORIZON_EXP, "lit": _POSTERIOR_HORIZON_LIT},
        "recency_floor": _POSTERIOR_RECENCY_FLOOR,
        "decoupled": True,
        "calibration": "model-based, not yet calibrated",
        "plan": "evidence/planning/epistemic_overlay_plan.md",
    }


def _compute_claim_confidence(
    entries: list[dict[str, Any]],
    now: datetime,
) -> tuple[float, float, float, str]:
    exp_entries = [e for e in entries if e.get("source_type") == "experimental"]
    lit_entries = [e for e in entries if e.get("source_type") == "literature"]

    exp_conf = 0.0
    lit_conf = 0.0

    if exp_entries:
        exp_counts = Counter(str(e.get("evidence_direction", "unknown")) for e in exp_entries)
        directional = exp_counts.get("supports", 0) + exp_counts.get("weakens", 0)
        if directional:
            # Directional net: +1 = all supports, 0 = balanced conflict, -1 = all weakens.
            # Map to [0, 1] where 1.0 = fully supporting, 0.5 = balanced, 0.0 = fully weakening.
            # This prevents "consistent weakening" (supports=0, weakens=N) from producing
            # high consistency (old formula gave abs(0-N)/N = 1.0 regardless of direction).
            net = (exp_counts.get("supports", 0) - exp_counts.get("weakens", 0)) / directional
            consistency = (net + 1.0) / 2.0
        else:
            consistency = 0.4
        volume = min(1.0, len(exp_entries) / 5.0)
        recency = _recency_score(exp_entries, now, horizon_days=90)
        quality = sum(float(e.get("confidence", 0.5)) for e in exp_entries) / len(exp_entries)
        exp_conf = _normalize_confidence(
            0.45 * consistency + 0.25 * volume + 0.20 * recency + 0.10 * quality,
            default=0.0,
        )

    if lit_entries:
        lit_counts = Counter(str(e.get("evidence_direction", "unknown")) for e in lit_entries)
        directional = lit_counts.get("supports", 0) + lit_counts.get("weakens", 0)
        if directional:
            consistency = abs(lit_counts.get("supports", 0) - lit_counts.get("weakens", 0)) / directional
        else:
            consistency = 0.5
        volume = min(1.0, len(lit_entries) / 4.0)
        recency = _recency_score(lit_entries, now, horizon_days=365)
        quality = sum(float(e.get("confidence", 0.5)) for e in lit_entries) / len(lit_entries)
        lit_conf = _normalize_confidence(
            0.50 * quality + 0.20 * consistency + 0.20 * volume + 0.10 * recency,
            default=0.0,
        )

    weights = 0.0
    weighted_sum = 0.0
    if exp_entries:
        w = min(3.0, float(len(exp_entries)))
        weighted_sum += exp_conf * w
        weights += w
    if lit_entries:
        w = min(3.0, float(len(lit_entries)))
        weighted_sum += lit_conf * w
        weights += w
    overall = _normalize_confidence((weighted_sum / weights) if weights else 0.0, default=0.0)

    rationale = (
        f"exp={len(exp_entries)} entry(s), lit={len(lit_entries)} entry(s), "
        f"exp_conf={_fmt_number(exp_conf)}, lit_conf={_fmt_number(lit_conf)}"
    )
    return exp_conf, lit_conf, overall, rationale


def _summarize_claim_entries(
    entries: list[dict[str, Any]],
    now: datetime,
) -> dict[str, Any]:
    ordered_entries = list(entries)
    ordered_entries.sort(key=lambda e: (str(e.get("timestamp_utc", "")), str(e.get("run_id", ""))))
    if not ordered_entries:
        return {}

    direction_counts = {
        "supports": 0,
        "weakens": 0,
        "mixed": 0,
        "unknown": 0,
    }
    genuine_exp_direction_counts: dict[str, int] = {
        "supports": 0,
        "weakens": 0,
        "mixed": 0,
        "unknown": 0,
    }
    genuine_exp_count = 0
    evidence_class_counts: dict[str, int] = {}
    evidence_level_counts: dict[str, int] = {}
    source_counts: dict[str, int] = {"experimental": 0, "literature": 0}

    pass_runs = 0
    fail_runs = 0

    for entry in ordered_entries:
        direction = str(entry.get("evidence_direction", "unknown"))
        direction_counts[direction] = direction_counts.get(direction, 0) + 1

        if _is_genuine_experimental_entry(entry):
            genuine_exp_direction_counts[direction] = (
                genuine_exp_direction_counts.get(direction, 0) + 1
            )
            genuine_exp_count += 1

        evidence_class = str(entry.get("evidence_class", "unclassified"))
        evidence_class_counts[evidence_class] = evidence_class_counts.get(evidence_class, 0) + 1

        # evidence_level is only set on experimental entries (A-E scale, default C).
        if entry.get("source_type") == "experimental" and "evidence_level" in entry:
            level = str(entry["evidence_level"])
            evidence_level_counts[level] = evidence_level_counts.get(level, 0) + 1

        source = str(entry.get("source_type", "experimental"))
        source_counts[source] = source_counts.get(source, 0) + 1

        status = str(entry.get("status", "PASS"))
        if status == "PASS":
            pass_runs += 1
        if status == "FAIL":
            fail_runs += 1

    exp_conf, lit_conf, overall_conf, rationale = _compute_claim_confidence(ordered_entries, now)
    latest = ordered_entries[-1]

    # Beta-Binomial per-node posteriors (epistemic overlay Phase 1). Additive:
    # exp_conf/lit_conf above are untouched. EXP and LIT kept decoupled. These
    # are the unary potentials a Phase-2 MRF consumes unchanged. See
    # evidence/planning/epistemic_overlay_plan.md.
    exp_entries = [e for e in ordered_entries if e.get("source_type") == "experimental"]
    lit_entries = [e for e in ordered_entries if e.get("source_type") == "literature"]
    exp_posterior = _beta_binomial_posterior(exp_entries, now, _POSTERIOR_HORIZON_EXP)
    lit_posterior = _beta_binomial_posterior(lit_entries, now, _POSTERIOR_HORIZON_LIT)

    # Option E shadow fields (decoupled regime, no behavioral effect yet).
    # See REE_assembly/CLAUDE.md "Lit/Exp Decoupling Shadow" for the methodology
    # and the phase 2/3 plan.
    n_exp_scored = source_counts.get("experimental", 0)
    n_lit_scored = source_counts.get("literature", 0)
    quadrant = _evidence_quadrant(exp_conf, lit_conf, n_exp_scored, n_lit_scored)

    return {
        "runs_total": len(ordered_entries),
        "entries_total": len(ordered_entries),
        "pass_runs": pass_runs,
        "fail_runs": fail_runs,
        "latest_run_id": str(latest.get("run_id", "")),
        "latest_timestamp_utc": str(latest.get("timestamp_utc", "")),
        "direction_counts": direction_counts,
        "genuine_exp_direction_counts": genuine_exp_direction_counts,
        "genuine_exp_count": genuine_exp_count,
        "evidence_class_counts": evidence_class_counts,
        "evidence_level_counts": evidence_level_counts,
        "source_counts": source_counts,
        "experimental_confidence": exp_conf,
        "literature_confidence": lit_conf,
        "overall_confidence": overall_conf,
        "confidence_rationale": rationale,
        "experimental_confidence_decoupled": exp_conf,
        "literature_confidence_parallel": lit_conf,
        "evidence_quadrant": quadrant,
        "exp_posterior": exp_posterior,
        "lit_posterior": lit_posterior,
        "recent_entries": ordered_entries[-5:],
    }


def _write_claim_evidence_matrix(
    base_dir: Path,
    by_experiment: dict[str, list[RunRecord]],
    by_literature: dict[str, list[LiteratureRecord]],
    generated_at: str,
    planning_criteria: dict[str, Any] | None = None,
    scoring_exclusions: dict[str, set[str]] | None = None,
) -> dict[str, Any]:
    """Build the claim evidence matrix.

    All entries are included in matrix["entries"] for audit purposes.
    Only *applicable* and *non-excluded* entries feed into claim confidence scores.
    Applicability = epoch filter (stale_if_timestamp_before_epoch_start).
    Exclusions    = per-claim run_ids listed in scoring_exclusions.json (code bugs,
                    wrong-module tests, invalid instrumentation).
    """
    _, is_applicable = _build_applicability_filter(planning_criteria or {})
    excl: dict[str, set[str]] = scoring_exclusions or {}

    exp_runs = [run for exp_runs in by_experiment.values() for run in exp_runs]
    exp_runs.sort(key=lambda r: (r.timestamp, r.experiment_type, r.run_id))

    lit_entries = [entry for lit_runs in by_literature.values() for entry in lit_runs]
    lit_entries.sort(key=lambda e: (e.timestamp, e.literature_type, e.entry_id))

    matrix: dict[str, Any] = {
        "schema_version": "claim_evidence_matrix/v1",
        "generated_at_utc": generated_at,
        "source_root": "evidence",
        "posterior_model": _posterior_model_metadata(),
        "claims": {},
        "entries": [],
        "unlinked_runs": [],
    }

    claim_to_entries: dict[str, list[dict[str, Any]]] = defaultdict(list)

    # Diagnostic adjudication gate -- non-blocking headless visibility (2026-06-06).
    # Count diagnostic/baseline runs whose self-route is `unverified` (manifest
    # declared no preconditions[]/criteria_non_degenerate). Per-run WARN only for
    # runs authored ON/AFTER the convention date (compact-timestamp lexicographic
    # compare) -- legacy runs are immutable and handled by the retrospective audit,
    # so warning on all would flood every governance run. The aggregate count is
    # printed once after the loop so headless logs show the backlog size.
    # Cutoff is the day AFTER the gate landed (2026-06-06): every run authored on
    # that day predates the gate code, so it counts as legacy (aggregate only, no
    # per-run nag) -- only runs from 2026-06-07 on could have known the convention.
    _ADJ_CONVENTION_DATE = "20260607"
    _adj_unverified_total = 0
    _adj_unverified_post_convention = 0

    for run in exp_runs:
        inferred_direction = run.evidence_direction
        if inferred_direction == "unknown" and not run.direction_explicitly_set:
            inferred_direction = "supports" if run.final_status == "PASS" else "weakens"

        if run.experiment_purpose in ("diagnostic", "baseline") and run.adjudication == "unverified":
            _adj_unverified_total += 1
            if (run.timestamp_raw or "")[:8] >= _ADJ_CONVENTION_DATE:
                _adj_unverified_post_convention += 1
                print(f"  WARNING: {run.run_id} is a {run.experiment_purpose} run with no "
                      f"interpretation.preconditions[]/criteria_non_degenerate -> adjudication "
                      f"'unverified' (self-route not machine-checkable). Add the fields per the "
                      f"diagnostic adjudication gate (queue-experiment SKILL.md).")

        if not run.claim_ids_tested:
            unlinked_entry = {
                "source_type": "experimental",
                "experiment_type": run.experiment_type,
                "run_id": run.run_id,
                "timestamp_utc": run.timestamp_raw,
                "status": run.final_status,
                "experiment_purpose": run.experiment_purpose,
                "interpretation_label": run.interpretation_label,
                "adjudication": run.adjudication,
            }
            # Non-gating guard findings: informational, emitted only when present so
            # legacy entries stay byte-identical. Does NOT affect adjudication or
            # scoring -- see _recorded_precondition_findings.
            if run.recorded_preconditions_unmet:
                unlinked_entry["recorded_preconditions_unmet"] = run.recorded_preconditions_unmet
                if run.preconditions_scope_note:
                    unlinked_entry["preconditions_scope_note"] = run.preconditions_scope_note
            # Recording-standard always-core: surfaced for queryability only.
            if run.substrate_hash:
                unlinked_entry["substrate_hash"] = run.substrate_hash
            if run.label_balance:
                unlinked_entry["label_balance"] = run.label_balance
            if run.machine_class:
                unlinked_entry["machine_class"] = run.machine_class
            if run.machine:
                unlinked_entry["machine"] = run.machine
            matrix["unlinked_runs"].append(unlinked_entry)
            continue

        # Warn if multi-claim experiment lacks per-claim direction overrides.
        # Exempt run-level "superseded": supersession is run-scoped (the whole run
        # is excluded below at scoring_excluded="superseded", and there is no
        # per-claim superseded form), so per-claim direction is moot -- the warning
        # would be a pure false positive for a corrected re-run that replaced its
        # predecessor.
        if (len(run.claim_ids_tested) > 1
                and not run.evidence_direction_per_claim
                and run.experiment_purpose == "evidence"
                and inferred_direction != "superseded"):
            print(f"  WARNING: {run.run_id} tags {len(run.claim_ids_tested)} claims "
                  f"without evidence_direction_per_claim -- blanket "
                  f"'{inferred_direction}' applied to all: "
                  f"{run.claim_ids_tested}")

        for claim_id in run.claim_ids_tested:
            # Per-claim direction override: if the manifest declares a specific
            # direction for this claim_id, use it; otherwise fall back to the
            # run-level inferred direction.
            claim_direction = run.evidence_direction_per_claim.get(claim_id, inferred_direction)
            entry_confidence, entry_confidence_rationale = _experimental_entry_confidence(run, claim_direction)
            entry = {
                "claim_id": claim_id,
                "source_type": "experimental",
                "experiment_type": run.experiment_type,
                "run_id": run.run_id,
                "timestamp_utc": run.timestamp_raw,
                "status": run.final_status,
                "evidence_class": _prefix_class("experimental", run.evidence_class),
                "evidence_direction": claim_direction,
                "evidence_level": run.evidence_level,
                "confidence": entry_confidence,
                "confidence_rationale": entry_confidence_rationale,
                "failure_signatures": run.failure_signatures,
                "experiment_purpose": run.experiment_purpose,
            }
            if run.experiment_purpose in ("diagnostic", "baseline"):
                entry["interpretation_label"] = run.interpretation_label
                entry["adjudication"] = run.adjudication
                # Non-gating guard findings: informational only. Emitted alongside
                # the adjudication flag but NEVER folded into it, into
                # scoring_excluded, or into confidence/conflict -- an unmet recorded
                # precondition must not vacate the run (the V3-EXQ-785 defect this
                # key exists to avoid). See _recorded_precondition_findings.
                if run.recorded_preconditions_unmet:
                    entry["recorded_preconditions_unmet"] = run.recorded_preconditions_unmet
                    if run.preconditions_scope_note:
                        entry["preconditions_scope_note"] = run.preconditions_scope_note
            if run.architecture_epoch:
                entry["architecture_epoch"] = run.architecture_epoch
            # Recording-standard always-core: surfaced for queryability only (does
            # NOT affect scoring). Emitted only when present, so legacy entries are
            # byte-identical.
            if run.substrate_hash:
                entry["substrate_hash"] = run.substrate_hash
            if run.label_balance:
                entry["label_balance"] = run.label_balance
            if run.machine_class:
                entry["machine_class"] = run.machine_class
            if run.machine:
                entry["machine"] = run.machine
            matrix["entries"].append(entry)

            # Epoch-stale, explicitly excluded, or superseded entries are logged
            # but do not count toward claim confidence or conflict ratios.
            if not is_applicable(entry):
                entry["scoring_excluded"] = "stale_epoch"
                continue
            if run.run_id in excl.get(claim_id, set()):
                entry["scoring_excluded"] = "invalid_run"
                continue
            if inferred_direction == "superseded":
                entry["scoring_excluded"] = "superseded"
                continue
            # Non-degeneracy gate (2026-06-11): an explicitly-set manifest flag
            # marks this run's result as structurally degenerate for this claim --
            # a discriminative metric pinned at a constant so its criterion could
            # never fire regardless of behaviour (vacuous PASS or FAIL). The entry
            # stays in the full log (with the reason for audit) but stops weighting
            # confidence/conflict, exactly like superseded/stale_substrate. The
            # run-level flag applies to every tagged claim; the per-claim form
            # de-weights ONLY this claim_id. Only an explicit False excludes --
            # absent flags are a no-op against the legacy record.
            if (run.non_degenerate is False
                    or run.non_degenerate_per_claim.get(claim_id) is False):
                entry["scoring_excluded"] = "degenerate"
                if run.degeneracy_reason:
                    entry["degeneracy_reason"] = run.degeneracy_reason
                continue
            # Substrate-staleness gate (2026-06-02): a manually-set manifest
            # flag marks this run's evidence as mechanistically stale because a
            # substrate it depends on changed after the run was recorded. The
            # entry stays in the full log (with the substrate ref for audit) but
            # stops weighting confidence/conflict. Absent flags => no-op.
            # Run-level flags apply to every tagged claim; the per-claim forms
            # de-weight ONLY this claim_id, leaving co-tagged claims intact.
            per_claim_ref = run.superseded_by_substrate_per_claim.get(claim_id, "")
            if (run.pending_retest_after_substrate
                    or run.superseded_by_substrate
                    or claim_id in run.pending_retest_after_substrate_per_claim
                    or per_claim_ref):
                entry["scoring_excluded"] = "stale_substrate"
                ref = run.superseded_by_substrate or per_claim_ref
                if ref:
                    entry["superseded_by_substrate"] = ref
                continue
            if run.experiment_purpose in ("diagnostic", "baseline"):
                entry["scoring_excluded"] = f"{run.experiment_purpose}_probe"
                continue
            if claim_direction in ("non_contributory", "inconclusive"):
                entry["scoring_excluded"] = claim_direction
                continue

            claim_to_entries[claim_id].append(entry)

    if _adj_unverified_total:
        print(f"  adjudication: {_adj_unverified_total} diagnostic/baseline run(s) "
              f"`unverified` (no interpretation.preconditions[]); "
              f"{_adj_unverified_post_convention} authored on/after the "
              f"{_ADJ_CONVENTION_DATE} convention (fix those). Legacy runs are "
              f"immutable -- see the retrospective self-route audit.")

    for lit in lit_entries:
        if not lit.claim_ids_tested:
            matrix["unlinked_runs"].append(
                {
                    "source_type": "literature",
                    "experiment_type": lit.literature_type,
                    "run_id": lit.entry_id,
                    "timestamp_utc": lit.timestamp_raw,
                    "status": "SOURCE",
                }
            )
            continue

        for claim_id in lit.claim_ids_tested:
            entry = {
                "claim_id": claim_id,
                "source_type": "literature",
                "experiment_type": lit.literature_type,
                "run_id": lit.entry_id,
                "timestamp_utc": lit.timestamp_raw,
                "status": "SOURCE",
                "evidence_class": _prefix_class("literature", lit.evidence_class),
                "evidence_direction": lit.evidence_direction,
                "confidence": lit.confidence,
                "confidence_rationale": lit.confidence_rationale,
                "failure_signatures": lit.failure_signatures,
            }
            if lit.architecture_epoch:
                entry["architecture_epoch"] = lit.architecture_epoch
            matrix["entries"].append(entry)

            # Literature entries are not epoch-filtered or excluded for now.
            claim_to_entries[claim_id].append(entry)

    now = _parse_timestamp_only(generated_at)
    for claim_id in sorted(claim_to_entries.keys()):
        summary = _summarize_claim_entries(claim_to_entries[claim_id], now)
        if summary:
            matrix["claims"][claim_id] = summary

    matrix["entries"].sort(
        key=lambda e: (e["timestamp_utc"], e["claim_id"], e["experiment_type"], e["run_id"])
    )
    matrix["unlinked_runs"].sort(
        key=lambda e: (e["timestamp_utc"], e["source_type"], e["experiment_type"], e["run_id"])
    )

    (base_dir / "claim_evidence.v1.json").write_text(
        json.dumps(matrix, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return matrix


def _write_todos(base_dir: Path, todos_by_experiment: dict[str, list[str]], generated_at: str) -> None:
    lines: list[str] = []
    lines.append("# Experiment-Driven TODO Queue")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("Auto-generated from FAIL signatures in Experiment Pack runs.")
    lines.append("")

    if not todos_by_experiment:
        lines.append("No active failure-driven TODO items.")
    else:
        for exp_type in sorted(todos_by_experiment.keys()):
            lines.append(f"## {exp_type}")
            lines.append("")
            for item in todos_by_experiment[exp_type]:
                lines.append(f"- {item}")
            lines.append("")

    (base_dir / "TODOs.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _strip_inline_yaml_comment(value: str) -> str:
    """Strip a trailing ' #...' inline comment from a scalar YAML value.

    Cuts at the first '#' preceded by whitespace, so values that legitimately
    contain '#' mid-token are unaffected (enum/flag fields never do). Used ONLY
    for the enum-like registry fields parsed in `_load_claim_registry` -- NOT for
    prose fields (evidence_quality_note / heterogeneity_note), whose free text may
    contain '#'. Without this, a commented value like
    `epistemic_category: substrate_conditional  # gov note` was captured as the
    literal `"substrate_conditional  # gov note"`, which is not in
    EPISTEMIC_CATEGORIES, so `_resolve_epistemic_category` fell back to inference
    (standard / answer_state) and silently un-suppressed promote/demote/
    narrow_open_question recommendations. Incident 2026-06-18 (substrate_ceiling
    orphan-routing: MECH-102/Q-028/Q-029).
    """
    for i in range(1, len(value)):
        if value[i] == "#" and value[i - 1] in (" ", "\t"):
            return value[:i].strip()
    return value.strip()


def _load_claim_registry(path: Path) -> dict[str, dict[str, str]]:
    """Parse claim id/status/type/v3_pending/implementation_phase from docs/claims/claims.yaml.

    This parser intentionally handles the repository's simple YAML pattern and avoids non-stdlib deps.
    v3_pending and implementation_phase == "v3" both signal that the claim cannot be meaningfully
    tested until the V3 substrate exists — governance recommendations are suppressed for these.
    """
    registry: dict[str, dict[str, str]] = {}
    current_id: str | None = None
    current_status: str | None = None
    current_type: str | None = None
    current_invariant_type: str | None = None
    current_epistemic_category: str | None = None
    current_v3_pending: bool = False
    current_impl_phase: str | None = None
    current_eq_note: str | None = None
    current_defer_until: str | None = None
    current_het_note: str | None = None
    # Assembly-state companion fields (MOVE-4 claims-layer follow-on, 2026-06-22).
    # ACCEPT-only here: parsed so they are machine-readable in the registry and so
    # an explicit `assembly_state` override is captured. They do NOT change any
    # promotion/demotion/hold dispatch -- the canonical derivation +
    # substrate_queue auto-join live in scripts/build_claims_json.py
    # (resolve_assembly_state) and serve.py (_resolve_claim_assembly_state),
    # kept in sync. See assembly_vs_closure_plan.md "Open follow-ons".
    current_assembly_state: str | None = None
    current_awaiting: str | None = None
    current_assembly_status: str | None = None
    current_revisit_after: str | None = None
    _collecting_eq_note: bool = False  # True while reading a block-scalar evidence_quality_note

    if not path.exists():
        return registry

    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        # ── Collect continuation lines for block-scalar evidence_quality_note ──
        if _collecting_eq_note:
            # Block ends when line is not indented deeper than the field (4+ spaces for sub-field)
            if line.startswith("    "):
                current_eq_note = (current_eq_note or "") + " " + line.strip()
                continue
            else:
                _collecting_eq_note = False
                # Fall through to process this non-continuation line normally

        if line.startswith("- id:"):
            if current_id:
                registry[current_id] = {
                    "status": current_status or "unknown",
                    "claim_type": current_type or "unknown",
                    "invariant_type": current_invariant_type or "",
                    "epistemic_category": current_epistemic_category or "",
                    "v3_pending": str(current_v3_pending),
                    "implementation_phase": current_impl_phase or "",
                    "evidence_quality_note": (current_eq_note or "").strip(),
                    "defer_promotion_until": current_defer_until or "",
                    "heterogeneity_note": (current_het_note or "").strip(),
                    "assembly_state": current_assembly_state or "",
                    "awaiting": current_awaiting or "",
                    "assembly_status": current_assembly_status or "",
                    "revisit_after": current_revisit_after or "",
                }
            current_id = line.split(":", 1)[1].strip()
            current_status = None
            current_type = None
            current_invariant_type = None
            current_epistemic_category = None
            current_v3_pending = False
            current_impl_phase = None
            current_eq_note = None
            current_defer_until = None
            current_het_note = None
            current_assembly_state = None
            current_awaiting = None
            current_assembly_status = None
            current_revisit_after = None
            _collecting_eq_note = False
            continue

        if current_id and line.startswith("  status:"):
            current_status = _strip_inline_yaml_comment(line.split(":", 1)[1])
            continue

        if current_id and line.startswith("  claim_type:"):
            current_type = _strip_inline_yaml_comment(line.split(":", 1)[1])
            continue

        if current_id and line.startswith("  invariant_type:"):
            current_invariant_type = _strip_inline_yaml_comment(line.split(":", 1)[1])
            continue

        if current_id and line.startswith("  epistemic_category:"):
            current_epistemic_category = _strip_inline_yaml_comment(line.split(":", 1)[1])
            continue

        if current_id and line.startswith("  v3_pending:"):
            val = _strip_inline_yaml_comment(line.split(":", 1)[1]).lower()
            current_v3_pending = val in ("true", "yes", "1")
            continue

        if current_id and line.startswith("  implementation_phase:"):
            current_impl_phase = _strip_inline_yaml_comment(line.split(":", 1)[1])
            continue

        if current_id and line.startswith("  assembly_state:"):
            current_assembly_state = _strip_inline_yaml_comment(line.split(":", 1)[1])
            continue

        if current_id and line.startswith("  awaiting:"):
            current_awaiting = _strip_inline_yaml_comment(line.split(":", 1)[1]).strip("\"'")
            continue

        if current_id and line.startswith("  assembly_status:"):
            current_assembly_status = _strip_inline_yaml_comment(line.split(":", 1)[1])
            continue

        if current_id and line.startswith("  revisit_after:"):
            current_revisit_after = _strip_inline_yaml_comment(line.split(":", 1)[1]).strip("\"'")
            continue

        if current_id and line.startswith("  evidence_quality_note:"):
            rest = line.split(":", 1)[1].strip().strip("\"'")
            if rest == "|":
                # YAML block scalar — content is on the following indented lines
                current_eq_note = ""
                _collecting_eq_note = True
            else:
                current_eq_note = rest
            continue

        if current_id and line.startswith("  defer_promotion_until:"):
            current_defer_until = _strip_inline_yaml_comment(line.split(":", 1)[1]).strip("\"'")
            continue

        if current_id and line.startswith("  heterogeneity_note:"):
            current_het_note = line.split(":", 1)[1].strip().strip("\"'")
            continue

    if current_id:
        registry[current_id] = {
            "status": current_status or "unknown",
            "claim_type": current_type or "unknown",
            "invariant_type": current_invariant_type or "",
            "epistemic_category": current_epistemic_category or "",
            "v3_pending": str(current_v3_pending),
            "implementation_phase": current_impl_phase or "",
            "evidence_quality_note": (current_eq_note or "").strip(),
            "defer_promotion_until": current_defer_until or "",
            "heterogeneity_note": (current_het_note or "").strip(),
            "assembly_state": current_assembly_state or "",
            "awaiting": current_awaiting or "",
            "assembly_status": current_assembly_status or "",
            "revisit_after": current_revisit_after or "",
        }
    return registry


def _is_inactive_claim_status(status: str) -> bool:
    return str(status).strip().lower() in {"legacy", "superseded", "retired", "applied"}


# Claim statuses that are answered or closing: a REE experiment can no longer
# change the claim's disposition, so it must not seed an EXPERIMENTAL proposal.
# Distinct from _is_inactive_claim_status (which drops the whole backlog item for
# already-dead claims and is shared by several call sites). These statuses still
# flow through the backlog / literature path; only experimental-proposal
# generation is suppressed. ("resolved"=answered, "retiring"=closing,
# "open"=an open_question whose disposition is settled via the answer_state
# narrow_open_question path, not a promote/demote-style experiment probe; an
# open_question is restated as a MECH/SD before it is experiment-promotable.)
_ANSWERED_OR_CLOSING_CLAIM_STATUSES = {"resolved", "open", "retiring"}

# Resolved epistemic_category values whose questions are settled by literature,
# derivation, or policy rather than by a REE experiment. (answer_state and the
# substrate_* categories are intentionally NOT here -- they keep their own
# recommendation handling in _recommendation_for_claim.)
_NON_EXPERIMENTAL_EPISTEMIC_CATEGORIES = {
    "out_of_domain",
    "derivational",
    "governance_rule",
}


def _is_experiment_ineligible_claim(registry_meta: dict[str, Any]) -> bool:
    """True when a claim must not seed an experimental (EXP-*) proposal.

    Two independent reasons (either suffices):
      * the claim status is answered/closing (a REE run cannot move it), or
      * its resolved epistemic_category is one settled outside REE experiments
        (literature / derivation / policy).

    Warn-safe: missing/blank fields resolve to eligible (False) so absent
    metadata never silently suppresses a genuine proposal. Uses
    _resolve_epistemic_category so an inferred answer_state (open_question
    default) is handled by the status rule, not mis-skipped here.
    """
    if not isinstance(registry_meta, dict):
        return False
    status = str(registry_meta.get("status", "")).strip().lower()
    if status in _ANSWERED_OR_CLOSING_CLAIM_STATUSES:
        return True
    epistemic_category = _resolve_epistemic_category(
        str(registry_meta.get("claim_type", "")),
        str(registry_meta.get("invariant_type", "")),
        str(registry_meta.get("epistemic_category", "")),
    )
    return epistemic_category in _NON_EXPERIMENTAL_EPISTEMIC_CATEGORIES


# ── Phase 3 wave 2: epistemic-category resolver ──────────────────────────────
EPISTEMIC_CATEGORIES = (
    "standard",
    "substrate_coherence",
    "answer_state",
    "substrate_ceiling",
    "substrate_conditional",
    "derivational",
    "out_of_domain",
    "governance_rule",
)


def _resolve_epistemic_category(
    claim_type: str,
    invariant_type: str,
    explicit_category: str,
) -> str:
    """Return the resolved epistemic_category for a claim.

    If `explicit_category` is set on the claim (one of EPISTEMIC_CATEGORIES,
    case-insensitive), it takes precedence. Otherwise the category is
    inferred from claim_type + invariant_type using the Phase 2 mapping:

      architectural_commitment            -> substrate_coherence
      invariant + invariant_type=universal -> substrate_coherence
      open_question                       -> answer_state
      everything else                     -> standard

    The "explicit-only" categories (substrate_ceiling, substrate_conditional,
    derivational, out_of_domain, governance_rule) cannot be inferred from
    claim_type alone and require an explicit annotation in claims.yaml.
    governance_rule tags a standing governance gate (welfare / release /
    legal / security policy) that is NOT a testable mechanism: it shares the
    non-`standard` dispatch (promote/demote suppressed) and, like the
    explicit-only categories other than answer_state, never fires
    narrow_open_question. Conflict-resolution alerts may still fire.

    See REE_assembly/CLAUDE.md "Epistemic categories" for the full mapping
    and the recommendation-dispatch consequences.
    """
    explicit = (explicit_category or "").strip().lower()
    if explicit in EPISTEMIC_CATEGORIES:
        return explicit
    ct = (claim_type or "").strip()
    it = (invariant_type or "").strip()
    if ct == "architectural_commitment":
        return "substrate_coherence"
    if ct == "invariant" and it == "universal":
        return "substrate_coherence"
    if ct == "open_question":
        return "answer_state"
    return "standard"


def _default_decision_criteria() -> dict[str, Any]:
    """Phase 3 cutover defaults: gates read experimental_confidence
    (the decoupled signal) via min_exp_conf / max_exp_conf. The actual
    threshold reads in the gate logic accept the legacy keys too as a
    backwards-compat fallback for any YAMLs not yet migrated."""
    return {
        "schema_version": "decision_criteria/v1",
        "decision_status_default": "pending_user",
        "thresholds": {
            "candidate_to_provisional": {
                "min_exp_conf": 0.62,
                "min_experimental_entries": 2,
                "max_conflict_ratio": 0.35,
                "min_supporting_entries": 1,
            },
            "provisional_to_stable": {
                "min_exp_conf": 0.80,
                "min_experimental_entries": 4,
                "min_literature_entries": 2,
                "max_conflict_ratio": 0.20,
            },
            "demote_on_conflict": {
                "min_total_entries": 3,
                "min_conflict_ratio": 0.55,
                "max_exp_conf": 0.55,
            },
        },
    }


def _load_decision_criteria(path: Path) -> dict[str, Any]:
    if not path.exists():
        return _default_decision_criteria()
    data = _load_json_compatible_yaml(path, "decision criteria")
    if "thresholds" not in data:
        data["thresholds"] = _default_decision_criteria()["thresholds"]
    if "decision_status_default" not in data:
        data["decision_status_default"] = "pending_user"
    return data


def _default_planning_criteria() -> dict[str, Any]:
    return {
        "schema_version": "planning_criteria/v1",
        "thresholds": {
            "low_exp_conf": 0.55,
            "lit_only_above_cap": 0.50,
            "conflict_ratio_alert": 0.40,
            "candidate_min_experimental_entries": 2,
            "provisional_min_literature_entries": 2,
            "consider_new_structure_conflict_ratio": 0.70,
            "consider_new_structure_min_failure_signature_repeats": 3,
            "consider_new_structure_min_distinct_signatures": 2,
            "consider_new_structure_min_literature_entries": 2,
            "consider_new_structure_literature_non_support_ratio": 0.50,
            "external_precedence_conflict_ratio": 0.55,
            "external_precedence_min_confidence_delta": 0.05,
            "external_precedence_min_total_entries": 6,
            "external_precedence_min_experimental_entries": 4,
            "external_precedence_min_literature_entries": 4,
            "external_precedence_min_recurring_signatures": 2,
            "proposal_saturation_conflict_ratio": 0.70,
            "proposal_saturation_min_experimental_entries": 16,
            "proposal_saturation_recent_window": 12,
            "proposal_saturation_min_recent_entries": 8,
            "proposal_saturation_max_unique_signature_sets": 2,
            "proposal_saturation_max_directions": 2,
            "escalation_min_conflict_ratio": 0.75,
            "escalation_min_experimental_entries": 24,
            "escalation_min_recurring_signatures": 2,
            "escalation_min_max_signature_count": 8,
            "mandatory_decision_conflict_ratio": 0.80,
            "mandatory_decision_min_fresh_batches": 2,
            "mandatory_decision_recent_window": 24,
            "mandatory_decision_deadline_hours": 72,
            "atomic_split_conflict_ratio": 0.70,
            "atomic_split_min_mixed_entries": 1,
            "atomic_split_min_recurring_signatures": 2,
            "discriminative_pair_conflict_ratio": 0.55,
            "discriminative_pair_min_shared_seeds": 2,
            "literature_min_disconfirming_entries": 1,
        },
        "model_adjudication": {
            "external_precedence_enabled": True,
            "allowed_conflict_outcomes": [
                "retain_ree",
                "hybridize",
                "retire_ree_claim",
            ],
            "default_conflict_outcome": "retain_ree",
            "cascade_policy": {
                "enabled": True,
                "trigger_outcomes": ["retire_ree_claim"],
                "dependency_reopen_status": "candidate",
                "require_followup_proposals": True,
            },
            "temporary_override_mode": {
                "enabled": True,
                "mode_id": "external_model_proxy_override",
                "requirements": [
                    "explicit_proxy_provenance",
                    "calibration_metrics_present",
                    "rollback_trigger_documented",
                ],
            },
            "anti_lock_in_gate": {
                "enabled": True,
                "description": (
                    "If matched external-model evidence repeatedly outperforms REE assumptions, force adjudication "
                    "rather than schema-preserving tuning."
                ),
            },
        },
        "repo_routing": {
            "experimental_default_repo": "ree-v2",
            "exploratory_repo": "ree-experiments-lab",
            "literature_owner": "REE_assembly",
        },
        "dispatch_overrides": {},
        "evidence_applicability": {
            "enabled": True,
            "current_architecture_epoch": "",
            "epoch_start_utc": "",
            "source_types": ["*"],
            "stale_if_timestamp_before_epoch_start": True,
            "require_epoch_tag_for_new_evidence": False,
        },
        "claim_evidence_staging": {
            "enabled": False,
            "claims": {},
        },
    }


def _load_planning_criteria(path: Path) -> dict[str, Any]:
    if not path.exists():
        return _default_planning_criteria()
    data = _load_json_compatible_yaml(path, "planning criteria")
    defaults = _default_planning_criteria()
    for key, value in defaults.items():
        data.setdefault(key, value)
    thresholds = data.get("thresholds")
    if not isinstance(thresholds, dict):
        data["thresholds"] = dict(defaults["thresholds"])
    else:
        for key, value in defaults["thresholds"].items():
            thresholds.setdefault(key, value)
    routing = data.get("repo_routing")
    if not isinstance(routing, dict):
        data["repo_routing"] = dict(defaults["repo_routing"])
    else:
        for key, value in defaults["repo_routing"].items():
            routing.setdefault(key, value)
    dispatch_overrides = data.get("dispatch_overrides")
    if not isinstance(dispatch_overrides, dict):
        data["dispatch_overrides"] = {}
    applicability = data.get("evidence_applicability")
    if not isinstance(applicability, dict):
        data["evidence_applicability"] = dict(defaults["evidence_applicability"])
    else:
        for key, value in defaults["evidence_applicability"].items():
            applicability.setdefault(key, value)
    staging = data.get("claim_evidence_staging")
    if not isinstance(staging, dict):
        data["claim_evidence_staging"] = dict(defaults["claim_evidence_staging"])
    else:
        for key, value in defaults["claim_evidence_staging"].items():
            staging.setdefault(key, value)
        if not isinstance(staging.get("claims"), dict):
            staging["claims"] = {}
    adjudication = data.get("model_adjudication")
    if not isinstance(adjudication, dict):
        data["model_adjudication"] = dict(defaults["model_adjudication"])
    else:
        for key, value in defaults["model_adjudication"].items():
            adjudication.setdefault(key, value)
        cascade_policy = adjudication.get("cascade_policy")
        if not isinstance(cascade_policy, dict):
            adjudication["cascade_policy"] = dict(defaults["model_adjudication"]["cascade_policy"])
        else:
            for key, value in defaults["model_adjudication"]["cascade_policy"].items():
                cascade_policy.setdefault(key, value)
        override_mode = adjudication.get("temporary_override_mode")
        if not isinstance(override_mode, dict):
            adjudication["temporary_override_mode"] = dict(
                defaults["model_adjudication"]["temporary_override_mode"]
            )
        else:
            for key, value in defaults["model_adjudication"]["temporary_override_mode"].items():
                override_mode.setdefault(key, value)
        anti_lock_in = adjudication.get("anti_lock_in_gate")
        if not isinstance(anti_lock_in, dict):
            adjudication["anti_lock_in_gate"] = dict(defaults["model_adjudication"]["anti_lock_in_gate"])
        else:
            for key, value in defaults["model_adjudication"]["anti_lock_in_gate"].items():
                anti_lock_in.setdefault(key, value)
    return data


def _load_scoring_exclusions(path: Path) -> dict[str, set[str]]:
    """Load per-claim run_id exclusion list from docs/claims/scoring_exclusions.json.

    Returns a dict mapping claim_id -> set of run_ids that should be excluded from
    confidence scoring (they remain in the full entry log but do not count toward
    claim confidence or direction counts).
    """
    if not path.exists():
        return {}
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    result: dict[str, set[str]] = {}
    for claim_id, entries in raw.items():
        if claim_id.startswith("_"):
            continue  # skip comment/metadata keys
        if not isinstance(entries, list):
            continue
        run_ids: set[str] = set()
        for item in entries:
            if isinstance(item, dict):
                rid = str(item.get("run_id", "")).strip()
            elif isinstance(item, str):
                rid = item.strip()
            else:
                continue
            if rid:
                run_ids.add(rid)
        if run_ids:
            result[claim_id] = run_ids
    return result


def _load_decision_log(path: Path) -> list[DecisionLogEntry]:
    if not path.exists():
        return []

    entries: list[DecisionLogEntry] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(obj, dict):
            continue

        claim_id = str(obj.get("claim_id", "")).strip()
        decision_status = str(obj.get("decision_status", "")).strip()
        recommendation = str(obj.get("recommendation", "")).strip()
        decision_needed = str(obj.get("decision_needed", "")).strip()
        timestamp_utc = str(obj.get("timestamp_utc", "")).strip()
        if not claim_id or not decision_status or not timestamp_utc:
            continue

        entries.append(
            DecisionLogEntry(
                claim_id=claim_id,
                decision_status=decision_status,
                recommendation=recommendation,
                decision_needed=decision_needed,
                timestamp_utc=timestamp_utc,
                selected_option=str(obj.get("selected_option", "")).strip(),
                rationale=str(obj.get("rationale", "")).strip(),
                actor=str(obj.get("actor", "user")).strip() or "user",
            )
        )
    return entries


def _latest_decision_by_claim(entries: list[DecisionLogEntry]) -> dict[str, DecisionLogEntry]:
    latest: dict[str, DecisionLogEntry] = {}
    for entry in entries:
        existing = latest.get(entry.claim_id)
        if existing is None:
            latest[entry.claim_id] = entry
            continue
        if entry.timestamp_utc >= existing.timestamp_utc:
            latest[entry.claim_id] = entry
    return latest


def _latest_decision_by_claim_and_needed(
    entries: list[DecisionLogEntry],
) -> dict[str, dict[str, DecisionLogEntry]]:
    latest: dict[str, dict[str, DecisionLogEntry]] = {}
    for entry in entries:
        decision_needed = entry.decision_needed.strip()
        if not decision_needed:
            continue
        by_needed = latest.setdefault(entry.claim_id, {})
        existing = by_needed.get(decision_needed)
        if existing is None or entry.timestamp_utc >= existing.timestamp_utc:
            by_needed[decision_needed] = entry
    return latest


def _latest_adjudication_decision_by_claim(
    entries: list[DecisionLogEntry],
    allowed_outcomes: set[str],
) -> dict[str, DecisionLogEntry]:
    latest: dict[str, DecisionLogEntry] = {}
    for entry in entries:
        recommendation = entry.recommendation.strip()
        if recommendation not in allowed_outcomes:
            continue
        existing = latest.get(entry.claim_id)
        if existing is None or entry.timestamp_utc >= existing.timestamp_utc:
            latest[entry.claim_id] = entry
    return latest


def _write_decision_state(
    decisions_dir: Path,
    latest_by_claim: dict[str, DecisionLogEntry],
    generated_at: str,
) -> None:
    state = {
        "schema_version": "decision_state/v1",
        "generated_at_utc": generated_at,
        "source": "evidence/decisions/decision_log.v1.jsonl",
        "claims": {},
    }
    for claim_id in sorted(latest_by_claim.keys()):
        entry = latest_by_claim[claim_id]
        state["claims"][claim_id] = {
            "decision_status": entry.decision_status,
            "recommendation": entry.recommendation,
            "decision_needed": entry.decision_needed,
            "selected_option": entry.selected_option,
            "rationale": entry.rationale,
            "actor": entry.actor,
            "timestamp_utc": entry.timestamp_utc,
        }

    decisions_dir.mkdir(parents=True, exist_ok=True)
    (decisions_dir / "decision_state.v1.json").write_text(
        json.dumps(state, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


# Some experiment scripts emit run_ids in the mis-ordered form
# `..._v3_<timestamp>` instead of the canonical `..._<timestamp>_v3`
# (e.g. V3-EXQ-628: v3_exq_628_..._evidence_v3_20260602T191625Z). A bare
# run_id.endswith("_v3") check misses that ordering, which silently under-counts
# the run as non-genuine (firing the contamination guard's collect_genuine_evidence
# override on a real V3 PASS) and -- via sync_v3_results._is_flat_v3 -- blocked its
# flat->pack conversion entirely (the silent-drop root cause). This matcher accepts
# both orderings.
_V3_MIDSTRING_RE = re.compile(r"_v3_\d{8}T\d{6,}Z?$")


def _is_v3_run_id(run_id: str) -> bool:
    """True for a V3 run_id in either ordering: the canonical `..._<ts>_v3`
    (endswith) or the mis-ordered `..._v3_<ts>` form some scripts emit."""
    rid = str(run_id)
    return rid.endswith("_v3") or bool(_V3_MIDSTRING_RE.search(rid))


def _genuine_run_count(claim_id: str, matrix: dict[str, Any]) -> int:
    """Count experiment entries for claim_id that come from genuine experimental runs.

    Genuine runs are identified by either:
    - architecture_epoch == "ree_v1_minimal_genuine_v1" (V1 substrate), OR
    - run_id ending with "_ree_v1_minimal" (V1 naming convention), OR
    - run_id ending with "_v2" (V2 bridge script naming convention: real ree_core + CausalGridWorld,
      post-2026-03-01, tagged with architecture_epoch="ree_hybrid_guardrails_v1")
    - run_id ending with "_v3" (V3 run packs, future)

    Synthetic pre-contamination runs end with "_toyenv_internal_minimal" and have
    no architecture_epoch — these are excluded.
    """
    count = 0
    for entry in matrix.get("entries", []):
        if str(entry.get("claim_id", "")) != claim_id:
            continue
        if entry.get("source_type") != "experimental":
            continue
        run_id = str(entry.get("run_id", ""))
        epoch = entry.get("architecture_epoch", "")
        if (
            epoch == "ree_v1_minimal_genuine_v1"
            or run_id.endswith("_ree_v1_minimal")
            or run_id.endswith("_v2")
            or _is_v3_run_id(run_id)
        ):
            count += 1
    return count


def _is_genuine_experimental_entry(entry: dict[str, Any]) -> bool:
    """Return True iff this entry is a genuine experimental run (V1, V2, or V3).

    Synthetic pre-contamination entries (ree-v2 / ree-experiments-lab) are
    identified by run_id ending with '_toyenv_internal_minimal' and have no
    architecture_epoch. Genuine entries carry:
    - architecture_epoch == "ree_v1_minimal_genuine_v1" or run_id ending "_ree_v1_minimal" (V1), OR
    - run_id ending "_v2" (real ree_core + CausalGridWorld, V2; architecture_epoch="ree_hybrid_guardrails_v1"), OR
    - run_id ending "_v3" (future V3 substrate runs).
    Literature entries (source_type != 'experimental') always return False.
    """
    if str(entry.get("source_type", "")) != "experimental":
        return False
    run_id = str(entry.get("run_id", ""))
    epoch = entry.get("architecture_epoch", "")
    return (
        epoch == "ree_v1_minimal_genuine_v1"
        or run_id.endswith("_ree_v1_minimal")
        or run_id.endswith("_v2")
        or _is_v3_run_id(run_id)
    )


def _recommendation_for_claim(
    claim_id: str,
    claim_meta: dict[str, Any],
    current_status: str,
    claim_type: str,
    criteria: dict[str, Any],
    registry_meta: "dict[str, Any] | None" = None,
    matrix: "dict[str, Any] | None" = None,
) -> dict[str, Any]:
    # ── Contamination guard ─────────────────────────────────────────────────
    # If the claim has experimental entries but NONE of them come from the
    # genuine ree-v1-minimal substrate (all are from synthetic ree-v2 /
    # ree-experiments-lab runs), override the statistical recommendation with
    # an explicit "collect_genuine_evidence" instruction.  This prevents stale
    # confidence scores and conflict ratios from driving spurious promotions or
    # demotions.
    #
    # Genuine runs are detected by run_id ending with "_ree_v1_minimal" or by
    # an explicit architecture_epoch == "ree_v1_minimal_genuine_v1" tag.
    # Synthetic runs end with "_toyenv_internal_minimal".
    _exp_entries = int(claim_meta.get("source_counts", {}).get("experimental", 0))
    _genuine_count = _genuine_run_count(claim_id, matrix) if matrix is not None else 0
    # Trigger when there ARE experimental entries but NONE are genuine.
    if _exp_entries > 0 and _genuine_count == 0:
        discussion_prompts = [
            "Which uncertainty source dominates: model variance, threshold choice, or claim scope?",
            "What single additional experiment or literature extraction would most reduce uncertainty?",
            "If this decision is wrong, what downstream architecture risk is largest?",
        ]
        return {
            "claim_id": claim_id,
            "current_status": current_status,
            "decision_needed": "Genuine evidence required before any status change",
            "recommendation": "collect_genuine_evidence",
            "synthetic_data_flag": True,
            "rationale": (
                f"All experimental evidence for {claim_id} is from synthetic substrates "
                f"(ree-v2 / ree-experiments-lab). Genuine ree-v1-minimal run count: {_genuine_count}. "
                f"Total synthetic exp entries: {_exp_entries}. "
                "Confidence scores and conflict ratios are unreliable. "
                "Collect ≥1 genuine experimental run on ree-v1-minimal before treating "
                "this claim as a promotion or demotion candidate."
            ),
            "options": [
                "Run the highest-priority EVB item for this claim on ree-v1-minimal (recommended).",
                "Demote to legacy and re-open when genuine evidence is available.",
                "Keep current status and suppress recommendations until genuine run completes.",
            ],
            "discussion_prompts": discussion_prompts,
            "decision_status": str(criteria.get("decision_status_default", "pending_user")),
        }
    # ── end contamination guard ──────────────────────────────────────────────

    # ── V3-pending gate ──────────────────────────────────────────────────────
    # v3_pending: true → unconditional hold (explicit manual gate, cleared by
    #   hand once V3 experiments for that specific claim have run).
    # implementation_phase: v3 → hold only if NO V3 runs exist yet for this
    #   claim; once V3 evidence arrives the claim graduates to normal evaluation.
    _v3_pending = str(registry_meta.get("v3_pending", "False")).lower() in ("true", "yes", "1") if registry_meta else False
    _impl_phase = str(registry_meta.get("implementation_phase", "")).strip().lower() if registry_meta else ""
    _v3_run_ct = sum(
        1 for e in (matrix or {}).get("entries", [])
        if str(e.get("claim_id", "")) == claim_id
        and _is_v3_run_id(str(e.get("run_id", "")))
    ) if matrix is not None else 0
    # V4/V5-architectural sub-case: a claim that is BOTH v3_pending AND explicitly
    # implementation_phase=v4 (or v5) is not "waiting for V3 substrate" -- it is
    # deliberately deferred to a later generation by an architectural commitment
    # (e.g. a thin umbrella / coherence-map like ARC-080, or a V5 social-substrate
    # open-question like Q-073). Routing it to hold_pending_v3_substrate mislabels
    # it and parks it in the V3-substrate decision queue forever (the 2026-04-27
    # misclassification flagged in WORKSPACE_STATE; insights 2026-06-06; extended
    # to v5 2026-07-01 after Q-073 surfaced as pending_user; GENERALIZED to any
    # later generation (v>=4) 2026-07-01 PM after Q-074 (v6) surfaced as the next
    # pending_user in the same shape -- a governance trace confirmed the held set
    # buries no V3-needed claim, so matching any v>=4 is safe and stops this
    # re-recurring at v6/v7/v8). Give it its own recommendation that is
    # structurally "applied" (no V3-substrate decision is pending) so it leaves the
    # pending_user queue and the morning digest. The recommendation KEY stays
    # held_v4_by_architectural_commitment (the shared "architectural-commitment"
    # bucket recognised by the IGW workset suppress set and morning digest)
    # regardless of the exact later generation; only the prose is generation-aware.
    _later_gen = re.fullmatch(r"v(\d+)", _impl_phase)
    if _v3_pending and _later_gen and int(_later_gen.group(1)) >= 4:
        _gen = _impl_phase.upper()
        return {
            "claim_id": claim_id,
            "current_status": current_status,
            "decision_needed": f"Held by {_gen} architectural commitment (no V3-substrate decision required)",
            "recommendation": "held_v4_by_architectural_commitment",
            "rationale": (
                f"Claim is v3_pending AND implementation_phase={_impl_phase}: it is "
                f"deferred to {_gen} by an architectural commitment, not awaiting V3 "
                "substrate. Promotion/demotion stays suppressed; no V3-substrate "
                f"decision is pending. Revisit when {_gen} substrate work is scheduled."
            ),
            "options": [
                f"Keep held under the {_gen} architectural commitment (correct path).",
                "Re-scope to implementation_phase=v3 if the claim becomes V3-tractable.",
                "Mark legacy/superseded if the commitment is withdrawn.",
            ],
            "discussion_prompts": [
                f"Is this claim genuinely {_gen}-scoped, or has a V3 substrate since made it tractable?",
                f"Which {_gen} substrate milestone unblocks this claim?",
            ],
            "decision_status": "applied",
        }
    if _v3_pending or (_impl_phase == "v3" and _v3_run_ct == 0):
        _hold_reason = (
            "Claim is flagged v3_pending (explicit manual gate). "
            "No promotion or demotion should be applied until this flag is cleared."
        ) if _v3_pending else (
            f"Claim has implementation_phase=v3 but no V3 experimental runs yet. "
            f"No promotion or demotion should be applied until V3 experiments complete."
        )
        return {
            "claim_id": claim_id,
            "current_status": current_status,
            "decision_needed": "Hold — V3 substrate required before meaningful evidence can be collected",
            "recommendation": "hold_pending_v3_substrate",
            "rationale": _hold_reason,
            "options": [
                "Wait for V3 substrate implementation (correct path).",
                "Mark as legacy/deferred if claim is being superseded.",
                "Demote to candidate to acknowledge insufficient evidence.",
            ],
            "discussion_prompts": [
                "Which uncertainty source dominates: model variance, threshold choice, or claim scope?",
                "What single additional experiment or literature extraction would most reduce uncertainty?",
                "If this decision is wrong, what downstream architecture risk is largest?",
            ],
            "decision_status": str(criteria.get("decision_status_default", "pending_user")),
        }
    # ── end V3-pending gate ──────────────────────────────────────────────────

    # ── Epistemic-category evidence gating (Phase 3 wave 2) ─────────────────
    # Resolves an explicit `epistemic_category` field on the claim; if absent,
    # falls back to the Phase 2 inferred mapping from claim_type +
    # invariant_type. Resolved values: standard, substrate_coherence,
    # answer_state, substrate_ceiling, substrate_conditional, derivational,
    # out_of_domain, governance_rule. Only `standard` runs the exp_conf-based
    # promotion / demotion logic. Conflict-resolution alerts still fire for
    # every category. narrow_open_question fires only for `answer_state`.
    # governance_rule (welfare/release/legal/security gates) is non-`standard`
    # so promote/demote/narrow are all suppressed -- these are standing
    # governance positions, not testable mechanisms.
    # See REE_assembly/CLAUDE.md "Epistemic categories" for the full mapping.
    _ct = (claim_type or "").strip()
    _it = ""
    _explicit_cat = ""
    if registry_meta is not None:
        _it = str(registry_meta.get("invariant_type", "")).strip()
        _explicit_cat = str(registry_meta.get("epistemic_category", "")).strip()
    epistemic_category = _resolve_epistemic_category(_ct, _it, _explicit_cat)
    _exp_conf_gated = (epistemic_category == "standard")
    _is_answer_state = (epistemic_category == "answer_state")
    # substrate_conditional / substrate_ceiling are the two EXPLICIT-only
    # categories that mean "no build-relevant action is available until an
    # upstream probe/substrate lands" (see REE_assembly/CLAUDE.md "Epistemic
    # categories"). A conflict-resolution hold on one of these claims cannot
    # offer "run conflict-resolution experiments" as a real option -- there is
    # nothing to run yet.
    _is_probe_gated_category = epistemic_category in ("substrate_conditional", "substrate_ceiling")
    # ── end epistemic-category gating ────────────────────────────────────────

    thresholds = criteria.get("thresholds", {})
    t_candidate = thresholds.get("candidate_to_provisional", {})
    t_stable = thresholds.get("provisional_to_stable", {})
    t_demote = thresholds.get("demote_on_conflict", {})

    direction_counts = claim_meta.get("direction_counts", {})
    conflict_ratio = _direction_conflict_ratio(direction_counts)
    # Phase 3 cutover (Option E): promotion / demotion gates read
    # experimental_confidence (the decoupled signal). The legacy
    # overall_confidence is still emitted in the matrix for the explorer and
    # for downstream consumers in transition, but no longer drives gates.
    exp_conf = float(claim_meta.get("experimental_confidence", 0.0))
    overall_conf = float(claim_meta.get("overall_confidence", 0.0))
    exp_entries = int(claim_meta.get("source_counts", {}).get("experimental", 0))
    lit_entries = int(claim_meta.get("source_counts", {}).get("literature", 0))
    total_entries = int(claim_meta.get("entries_total", 0))

    # Threshold reads with backwards-compat fallback: prefer min_exp_conf /
    # max_exp_conf (Phase 3 names); fall back to min_overall_confidence /
    # max_overall_confidence if the new keys aren't present in the YAML.
    def _t(d: dict, new_key: str, legacy_key: str, default: float) -> float:
        if new_key in d:
            return float(d[new_key])
        if legacy_key in d:
            return float(d[legacy_key])
        return float(default)

    decision_needed = "No immediate status change"
    recommendation = "hold"
    rationale = (
        f"epistemic_category={epistemic_category}, exp_conf={_fmt_number(exp_conf)}, "
        f"conflict_ratio={_fmt_number(conflict_ratio)}, exp_entries={exp_entries}, "
        f"lit_entries={lit_entries}"
    )

    if current_status == "candidate":
        if _exp_conf_gated:
            genuine_exp_supports = int(
                claim_meta.get("genuine_exp_direction_counts", {}).get("supports", 0)
            )
            meets_promote = (
                exp_conf >= _t(t_candidate, "min_exp_conf", "min_overall_confidence", 0.62)
                and exp_entries >= int(t_candidate.get("min_experimental_entries", 2))
                and conflict_ratio <= float(t_candidate.get("max_conflict_ratio", 0.35))
                and genuine_exp_supports >= int(t_candidate.get("min_supporting_entries", 1))
            )
            if meets_promote:
                decision_needed = "Promotion review: candidate -> provisional"
                recommendation = "promote_to_provisional"
            elif conflict_ratio > float(t_candidate.get("max_conflict_ratio", 0.35)):
                decision_needed = "Conflict resolution before promotion"
                recommendation = "hold_candidate_resolve_conflict"
        else:
            # Conflict-resolution alert is meaningful even for non-exp_conf-gated
            # claim_types -- substrate validation can still produce conflicting
            # evidence -- but promote_to_provisional is suppressed.
            if conflict_ratio > float(t_candidate.get("max_conflict_ratio", 0.35)):
                recommendation = "hold_candidate_resolve_conflict"
                decision_needed = (
                    "Literature conflict noted; claim stays gated pending upstream probe/substrate"
                    if _is_probe_gated_category else
                    "Conflict resolution before promotion"
                )

    elif current_status == "provisional":
        if _exp_conf_gated:
            meets_stable = (
                exp_conf >= _t(t_stable, "min_exp_conf", "min_overall_confidence", 0.8)
                and exp_entries >= int(t_stable.get("min_experimental_entries", 4))
                and lit_entries >= int(t_stable.get("min_literature_entries", 2))
                and conflict_ratio <= float(t_stable.get("max_conflict_ratio", 0.2))
            )
            demote_trigger = (
                total_entries >= int(t_demote.get("min_total_entries", 3))
                and conflict_ratio >= float(t_demote.get("min_conflict_ratio", 0.55))
                and exp_conf <= _t(t_demote, "max_exp_conf", "max_overall_confidence", 0.55)
            )
            if meets_stable:
                decision_needed = "Promotion review: provisional -> stable"
                recommendation = "promote_to_stable"
            elif demote_trigger:
                decision_needed = "Demotion review: provisional -> candidate"
                recommendation = "demote_to_candidate"

    elif current_status in {"active", "stable"}:
        if _exp_conf_gated:
            demote_trigger = (
                total_entries >= int(t_demote.get("min_total_entries", 3))
                and conflict_ratio >= float(t_demote.get("min_conflict_ratio", 0.55))
                and exp_conf <= _t(t_demote, "max_exp_conf", "max_overall_confidence", 0.55)
            )
            if demote_trigger:
                target = "provisional" if current_status == "stable" else "candidate"
                decision_needed = f"Demotion review: {current_status} -> {target}"
                recommendation = f"demote_to_{target}"

    elif _is_answer_state and total_entries >= 2 and conflict_ratio < 0.35:
        # narrow_open_question fires for answer_state only -- Q-claims that
        # have been explicitly re-categorized (derivational, out_of_domain,
        # substrate_ceiling, substrate_conditional) skip this and stay as
        # `hold` so they do not get inappropriate "narrow this" prompts.
        decision_needed = "Question narrowing review"
        recommendation = "narrow_open_question"

    # ── defer_promotion_until gate ───────────────────────────────────────────
    # If the claim has a defer_promotion_until field set, intercept any
    # promotion recommendation and replace it with defer_promotion.
    # Demotion is still allowed — the defer only blocks upward movement.
    _defer_until = str(registry_meta.get("defer_promotion_until", "")).strip() if registry_meta else ""
    if _defer_until and recommendation.startswith("promote_"):
        recommendation = "defer_promotion"
        decision_needed = f"Promotion deferred until: {_defer_until}"
    # ── end defer_promotion_until gate ───────────────────────────────────────

    # evidence_quality_note is returned as a separate field so the writer can
    # emit it as its own bullet (not concatenated into the rationale line).
    _eq_note = str(registry_meta.get("evidence_quality_note", "")).strip() if registry_meta else ""

    option_set = {
        "promote_to_provisional": [
            "Promote now (faster convergence, risk premature lock-in)",
            "Hold until one additional confirming run (better robustness, slower progress)",
            "Hold and request targeted literature triangulation (better external grounding, extra delay)",
        ],
        "promote_to_stable": [
            "Promote now (clear canonical status, risk under-tested edge cases)",
            "Hold pending stress-test replication (better stress confidence, slower closure)",
            "Split claim scope before promotion (clearer boundaries, added doc work)",
        ],
        "demote_to_candidate": [
            "Demote now (reduces false certainty, destabilizes current roadmap references)",
            "Hold and run conflict-resolution suite first (more data, temporary ambiguity)",
            "Split into subclaims (isolates conflict, increases registry complexity)",
        ],
        "demote_to_provisional": [
            "Demote now (acknowledges uncertainty, may disrupt dependent docs)",
            "Hold and run adjudication experiments (better confidence, slower correction)",
            "Constrain claim scope instead (preserves momentum, might hide deeper conflict)",
        ],
        "hold_candidate_resolve_conflict": [
            "Keep candidate and run conflict-resolution experiments (most balanced)",
            "Promote despite conflict (speed, high lock-in risk)",
            "Demote to legacy (conservative, may discard useful partial mechanism)",
        ],
        "narrow_open_question": [
            "Narrow the question into testable sub-questions (higher tractability)",
            "Keep broad question (flexibility, weaker experiment planning)",
            "Convert one branch into candidate mechanism (progress, possible overcommitment)",
        ],
        "hold": [
            "No status change (stable governance)",
            "Request additional evidence anyway (higher confidence, extra cost)",
            "Force a status vote now (faster decision, weak evidential basis)",
        ],
        "defer_promotion": [
            "Wait for the planned action specified in defer_promotion_until (correct path).",
            "Override defer and promote now if architectural decision has been made (document rationale).",
            "Reassess defer condition — may have been resolved already.",
        ],
    }

    if recommendation == "hold_candidate_resolve_conflict" and _is_probe_gated_category:
        # substrate_conditional / substrate_ceiling claims are deliberately parked
        # pending an upstream probe or substrate build -- "run conflict-resolution
        # experiments" and "promote/demote" don't name an action anyone can take.
        option_set["hold_candidate_resolve_conflict"] = [
            "Acknowledge conflict, no status change (claim remains gated pending the probe/substrate — no build-relevant experiment is available yet)",
            "Escalate the upstream probe/substrate dependency if resolving this conflict has become urgent",
            "Re-open for conflict-resolution experiments once the upstream probe/substrate lands and the gate clears",
        ]

    discussion_prompts = [
        "Which uncertainty source dominates: model variance, threshold choice, or claim scope?",
        "What single additional experiment or literature extraction would most reduce uncertainty?",
        "If this decision is wrong, what downstream architecture risk is largest?",
    ]

    return {
        "claim_id": claim_id,
        "current_status": current_status,
        "decision_needed": decision_needed,
        "recommendation": recommendation,
        "rationale": rationale,
        "evidence_quality_note": _eq_note,
        "options": option_set.get(recommendation, option_set["hold"]),
        "discussion_prompts": discussion_prompts,
        "decision_status": str(criteria.get("decision_status_default", "pending_user")),
    }


def _write_promotion_demotion_recommendations(
    base_dir: Path,
    matrix: dict[str, Any],
    claim_registry: dict[str, dict[str, str]],
    decision_criteria: dict[str, Any],
    latest_decisions: dict[str, DecisionLogEntry],
    latest_decisions_by_needed: dict[str, dict[str, DecisionLogEntry]],
    generated_at: str,
    planning_criteria: dict[str, Any],
) -> None:
    scope_label, is_applicable = _build_applicability_filter(planning_criteria)
    lines: list[str] = []
    lines.append("# Promotion / Demotion Recommendations")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append(f"Decision scope: `{scope_label}`")
    lines.append("")
    lines.append("This file proposes decisions only. No claim status changes are applied automatically.")
    lines.append("Use this as the human-in-the-loop review queue.")
    lines.append("")

    entries_by_claim: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in matrix.get("entries", []):
        if not isinstance(entry, dict):
            continue
        if not is_applicable(entry):
            continue
        # Phase 3 fix: scoring_excluded entries (diagnostic_probe,
        # non_contributory, superseded, stale_epoch, stale_substrate,
        # invalid_run) must NOT
        # feed the gate's claim summary -- the main matrix's claims dict
        # excludes them, so the gate (which reads experimental_confidence
        # post-cutover) was computing inflated values vs the matrix.
        # Without this filter, gate decisions diverge from displayed values.
        if "scoring_excluded" in entry:
            continue
        claim_id = str(entry.get("claim_id", "")).strip()
        if claim_id:
            entries_by_claim[claim_id].append(entry)

    now = _parse_timestamp_only(generated_at)
    scoped_claims: dict[str, dict[str, Any]] = {}
    for claim_id, claim_entries in entries_by_claim.items():
        summary = _summarize_claim_entries(claim_entries, now)
        if summary:
            scoped_claims[claim_id] = summary

    recommendations: list[dict[str, Any]] = []
    for claim_id in sorted(scoped_claims.keys()):
        claim_meta = scoped_claims[claim_id]
        registry_meta = claim_registry.get(claim_id, {})
        current_status = str(registry_meta.get("status", "unknown"))
        if _is_inactive_claim_status(current_status):
            continue
        claim_type = str(registry_meta.get("claim_type", "unknown"))

        rec = _recommendation_for_claim(
            claim_id=claim_id,
            claim_meta=claim_meta,
            current_status=current_status,
            claim_type=claim_type,
            criteria=decision_criteria,
            registry_meta=registry_meta,
            matrix=matrix,
        )

        prior = None
        rec_needed = str(rec.get("decision_needed", "")).strip()
        claim_lane_map = latest_decisions_by_needed.get(claim_id, {})
        if rec_needed:
            prior = claim_lane_map.get(rec_needed)
        if prior is None:
            prior = latest_decisions.get(claim_id)
        rec["last_decision"] = None
        if prior is not None:
            rec["last_decision"] = {
                "decision_status": prior.decision_status,
                "recommendation": prior.recommendation,
                "decision_needed": prior.decision_needed,
                "timestamp_utc": prior.timestamp_utc,
                "selected_option": prior.selected_option,
                "rationale": prior.rationale,
                "actor": prior.actor,
            }
            if prior.recommendation == rec["recommendation"]:
                rec["decision_status"] = prior.decision_status
            else:
                rec["decision_status"] = str(
                    decision_criteria.get("decision_status_default", "pending_user")
                )
                rec["status_note"] = (
                    "Prior decision exists but recommendation changed; needs fresh review."
                )

        # Only surface items requiring explicit review.
        if rec["recommendation"] == "hold" and rec["decision_needed"] == "No immediate status change":
            continue
        recommendations.append(rec)

    lines.append("## Decision Queue")
    lines.append("")
    lines.append("| claim_id | current_status | decision_needed | recommendation | decision_status |")
    lines.append("|---|---|---|---|---|")

    if not recommendations:
        lines.append("| _none_ | - | No status changes recommended | - | - |")
    else:
        for rec in recommendations:
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{rec['claim_id']}`",
                        f"`{rec['current_status']}`",
                        rec["decision_needed"],
                        f"`{rec['recommendation']}`",
                        f"`{rec['decision_status']}`",
                    ]
                )
                + " |"
            )

    lines.append("")
    lines.append("## Decision Details")
    lines.append("")

    if not recommendations:
        lines.append("No pending promotion/demotion decisions from current evidence.")
    else:
        for rec in recommendations:
            claim_id = rec["claim_id"]
            claim_meta = scoped_claims.get(claim_id, {})
            supports = int(claim_meta.get("direction_counts", {}).get("supports", 0))
            weakens = int(claim_meta.get("direction_counts", {}).get("weakens", 0))
            mixed = int(claim_meta.get("direction_counts", {}).get("mixed", 0))
            unknown = int(claim_meta.get("direction_counts", {}).get("unknown", 0))
            conflict_ratio = _direction_conflict_ratio(claim_meta.get("direction_counts", {}))

            lines.append(f"### {claim_id}")
            lines.append(f"- Current status: `{rec['current_status']}`")
            lines.append(f"- Decision needed: {rec['decision_needed']}")
            lines.append(
                "- Why this decision is needed: "
                + f"{rec['rationale']}; directions supports={supports}, weakens={weakens}, mixed={mixed}, unknown={unknown}, conflict_ratio={_fmt_number(conflict_ratio)}"
            )
            _eq = rec.get("evidence_quality_note", "")
            if _eq:
                # Truncate very long notes to ~400 chars for readability in the recommendations file
                _eq_display = _eq[:400] + "…" if len(_eq) > 400 else _eq
                lines.append(f"- Evidence quality note: {_eq_display}")
            lines.append(f"- Recommendation: `{rec['recommendation']}`")
            if rec.get("synthetic_data_flag"):
                lines.append(
                    "- ⚠️ **Synthetic data flag**: All experimental evidence is from synthetic substrates "
                    "(ree-v2 / ree-experiments-lab). Confidence scores unreliable. "
                    "Collect genuine ree-v1-minimal runs before treating as promotion/demotion candidate."
                )
            lines.append("- Options (pros/cons):")
            for option in rec["options"]:
                lines.append(f"  - {option}")
            lines.append("- Discussion scope with Codex:")
            for prompt in rec["discussion_prompts"]:
                lines.append(f"  - {prompt}")
            lines.append(f"- Decision status: `{rec['decision_status']}`")
            if rec.get("status_note"):
                lines.append(f"- Status note: {rec['status_note']}")
            if rec.get("last_decision"):
                prior = rec["last_decision"]
                lines.append(
                    "- Last logged decision: "
                    + f"`{prior['decision_status']}` by `{prior['actor']}` at `{prior['timestamp_utc']}`"
                )
                if prior.get("selected_option"):
                    lines.append(f"- Last selected option: {prior['selected_option']}")
                if prior.get("rationale"):
                    lines.append(f"- Last rationale: {prior['rationale']}")
            lines.append("")

    # ── G4: Heterogeneity warnings ───────────────────────────────────────────
    # GRADE / PRISMA require that divergent evidence carries an explanatory
    # note before governance can aggregate a certainty estimate. Flag any active
    # claim with conflict_ratio > 0.3 that lacks a heterogeneity_note in
    # claims.yaml. This is a documentation gate, not a promotion gate.
    _G4_THRESHOLD = 0.3
    g4_warnings: list[tuple[float, str, str]] = []  # (conflict_ratio, claim_id, status)
    for _g4_cid in sorted(scoped_claims.keys()):
        _g4_meta = scoped_claims[_g4_cid]
        _g4_reg = claim_registry.get(_g4_cid, {})
        if _is_inactive_claim_status(str(_g4_reg.get("status", "unknown"))):
            continue
        _g4_cr = _direction_conflict_ratio(_g4_meta.get("direction_counts", {}))
        if _g4_cr > _G4_THRESHOLD:
            _g4_note = str(_g4_reg.get("heterogeneity_note", "")).strip()
            if not _g4_note:
                g4_warnings.append((_g4_cr, _g4_cid, str(_g4_reg.get("status", "unknown"))))
    g4_warnings.sort(key=lambda x: (-x[0], x[1]))

    lines.append("## G4: Heterogeneity Warnings")
    lines.append("")
    lines.append(
        "Claims with `conflict_ratio > 0.3` that lack a `heterogeneity_note` field in "
        "claims.yaml. Per GRADE/PRISMA, divergent evidence requires an explanatory account "
        "before governance aggregates a certainty estimate. Add a one-sentence note "
        "classifying the conflict as: substrate-version confound, methodological divergence, "
        "genuine scientific contradiction, or supersession lag."
    )
    lines.append("")
    if g4_warnings:
        lines.append("| claim_id | status | conflict_ratio |")
        lines.append("|---|---|---|")
        for _cr, _cid, _st in g4_warnings:
            lines.append(f"| `{_cid}` | `{_st}` | {_fmt_number(_cr)} |")
        lines.append("")
        lines.append(
            f"WARNING: {len(g4_warnings)} active claim(s) have conflict_ratio > 0.3 "
            f"without a heterogeneity_note. Add the field to each entry in "
            f"docs/claims/claims.yaml before the next governance promotion decision."
        )
    else:
        lines.append("All high-conflict active claims carry a `heterogeneity_note`. No warnings.")
    lines.append("")
    # ── end G4 ───────────────────────────────────────────────────────────────

    (base_dir / "promotion_demotion_recommendations.md").write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )


def _majority_direction(entries: list[dict[str, Any]], source_type: str) -> str:
    subset = [e for e in entries if e.get("source_type") == source_type]
    counts = Counter(str(e.get("evidence_direction", "unknown")) for e in subset)
    directional = {"supports": counts.get("supports", 0), "weakens": counts.get("weakens", 0)}
    if directional["supports"] == directional["weakens"]:
        return "tie"
    return "supports" if directional["supports"] > directional["weakens"] else "weakens"


def _build_applicability_filter(
    planning_criteria: dict[str, Any],
) -> tuple[str, Callable[[dict[str, Any]], bool]]:
    cfg = planning_criteria.get("evidence_applicability", {}) if isinstance(planning_criteria, dict) else {}
    if not isinstance(cfg, dict) or not bool(cfg.get("enabled", False)):
        return "all_entries", lambda _entry: True

    epoch = str(cfg.get("current_architecture_epoch", "")).strip()
    epoch_start_raw = str(cfg.get("epoch_start_utc", "")).strip()
    source_types_raw = cfg.get("source_types", ["experimental"])
    stale_before_cutoff = bool(cfg.get("stale_if_timestamp_before_epoch_start", True))
    require_epoch_tag_for_new = bool(cfg.get("require_epoch_tag_for_new_evidence", False))

    source_types: set[str] = set()
    if isinstance(source_types_raw, list):
        source_types = {str(x).strip().lower() for x in source_types_raw if str(x).strip()}
    elif isinstance(source_types_raw, str):
        value = source_types_raw.strip().lower()
        if value:
            source_types = {value}
    all_sources = "*" in source_types or not source_types

    epoch_start: datetime | None = None
    if epoch_start_raw:
        try:
            epoch_start = _parse_timestamp_only(epoch_start_raw)
        except ValueError:
            epoch_start = None

    scope_bits: list[str] = ["current_epoch_applicable"]
    if epoch:
        scope_bits.append(f"epoch={epoch}")

    def _is_applicable(entry: dict[str, Any]) -> bool:
        source_type = str(entry.get("source_type", "")).strip().lower()
        if not all_sources and source_type not in source_types:
            return True

        entry_epoch = str(entry.get("architecture_epoch", "")).strip()
        if entry_epoch:
            if epoch and entry_epoch != epoch:
                return False
            return True

        ts_raw = str(entry.get("timestamp_utc", "")).strip()
        ts: datetime | None = None
        if ts_raw:
            try:
                ts = _parse_timestamp_only(ts_raw)
            except ValueError:
                ts = None

        if epoch_start and stale_before_cutoff and ts and ts < epoch_start:
            return False
        if epoch_start and require_epoch_tag_for_new and ts and ts >= epoch_start:
            return False
        return True

    return ",".join(scope_bits), _is_applicable


def _collect_conflicts(
    matrix: dict[str, Any],
    planning_criteria: dict[str, Any],
    claim_registry: dict[str, dict[str, str]],
) -> tuple[list[dict[str, Any]], str]:
    scope_label, is_applicable = _build_applicability_filter(planning_criteria)
    entries_by_claim: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in matrix.get("entries", []):
        if not isinstance(entry, dict):
            continue
        if not is_applicable(entry):
            continue
        if entry.get("scoring_excluded"):
            continue
        entries_by_claim[str(entry.get("claim_id"))].append(entry)

    conflicts: list[dict[str, Any]] = []
    for claim_id in sorted(entries_by_claim.keys()):
        current_status = str(claim_registry.get(claim_id, {}).get("status", "unknown"))
        if _is_inactive_claim_status(current_status):
            continue
        claim_entries = entries_by_claim.get(claim_id, [])
        if not claim_entries:
            continue
        claim_entries.sort(key=lambda e: (str(e.get("timestamp_utc", "")), str(e.get("run_id", ""))))
        direction_counts = Counter(str(e.get("evidence_direction", "unknown")) for e in claim_entries)
        supports = int(direction_counts.get("supports", 0))
        weakens = int(direction_counts.get("weakens", 0))
        mixed = int(direction_counts.get("mixed", 0))

        direction_conflict = supports > 0 and weakens > 0

        exp_majority = _majority_direction(claim_entries, "experimental")
        lit_majority = _majority_direction(claim_entries, "literature")
        source_conflict = (
            exp_majority in {"supports", "weakens"}
            and lit_majority in {"supports", "weakens"}
            and exp_majority != lit_majority
        )

        if not (direction_conflict or source_conflict):
            continue

        conflict_types: list[str] = []
        if direction_conflict:
            conflict_types.append("directional")
        if source_conflict:
            conflict_types.append("source_disagreement")
        if mixed > 0:
            conflict_types.append("mixed_evidence")

        conflicts.append(
            {
                "claim_id": claim_id,
                "conflict_types": conflict_types,
                "supports": supports,
                "weakens": weakens,
                "conflict_ratio": _direction_conflict_ratio(direction_counts),
                "latest": str(claim_entries[-1].get("run_id", "")),
                "entries_considered": len(claim_entries),
            }
        )
    return conflicts, scope_label


def _write_conflicts_report(
    base_dir: Path,
    matrix: dict[str, Any],
    planning_criteria: dict[str, Any],
    conflicts: list[dict[str, Any]],
    conflict_scope: str,
    generated_at: str,
) -> None:
    lines: list[str] = []
    lines.append("# Evidence Conflict Report")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append(f"Conflict scope: `{conflict_scope}`")
    lines.append("")

    _, is_applicable = _build_applicability_filter(planning_criteria)
    entries_by_claim: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in matrix.get("entries", []):
        if isinstance(entry, dict) and is_applicable(entry):
            entries_by_claim[str(entry.get("claim_id"))].append(entry)

    lines.append("## Conflict Queue")
    lines.append("")
    lines.append("| claim_id | conflict_types | supports | weakens | conflict_ratio | latest | entries_considered |")
    lines.append("|---|---|---|---|---|---|---|")

    if not conflicts:
        lines.append("| _none_ | - | 0 | 0 | 0 | - | 0 |")
    else:
        for item in conflicts:
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{item['claim_id']}`",
                        ", ".join(item["conflict_types"]),
                        str(item["supports"]),
                        str(item["weakens"]),
                        _fmt_number(item["conflict_ratio"]),
                        f"`{item['latest']}`",
                        str(item.get("entries_considered", 0)),
                    ]
                )
                + " |"
            )

    lines.append("")
    lines.append("## Conflict Details")
    lines.append("")

    if not conflicts:
        lines.append("No active evidence conflicts detected.")
    else:
        for item in conflicts:
            claim_id = item["claim_id"]
            claim_meta = matrix["claims"][claim_id]
            claim_entries = entries_by_claim.get(claim_id, [])
            claim_entries.sort(key=lambda e: (e["timestamp_utc"], e["run_id"]))
            recent = claim_entries[-5:]

            signature_counts: Counter[str] = Counter()
            for entry in claim_entries:
                for sig in entry.get("failure_signatures", []):
                    signature_counts[str(sig)] += 1

            lines.append(f"### {claim_id}")
            lines.append(f"- Conflict types: {', '.join(item['conflict_types'])}")
            lines.append(
                "- Evidence breakdown: "
                + f"supports={item['supports']}, weakens={item['weakens']}, conflict_ratio={_fmt_number(item['conflict_ratio'])}, "
                + f"exp_conf={_fmt_number(claim_meta.get('experimental_confidence', 0.0))}, "
                + f"lit_conf={_fmt_number(claim_meta.get('literature_confidence', 0.0))}, "
                + f"overall_confidence_legacy={_fmt_number(claim_meta.get('overall_confidence', 0.0))}"
            )
            lines.append("- Recent entries:")
            for entry in recent:
                lines.append(
                    f"  - `{entry['timestamp_utc']}` `{entry['source_type']}` `{entry['experiment_type']}` "
                    + f"direction=`{entry['evidence_direction']}` confidence={_fmt_number(entry.get('confidence', 0.0))}"
                )

            if signature_counts:
                lines.append("- Recurring failure signatures:")
                for sig, count in signature_counts.most_common(5):
                    lines.append(f"  - `{sig}` ({count})")

            lines.append("- Suggested resolution actions:")
            lines.append("  - Run one targeted adjudication experiment with narrower stop criteria.")
            lines.append("  - Add one replication run with seed sweep to reduce variance ambiguity.")
            lines.append("  - If disagreement persists, split claim scope into separable subclaims.")
            lines.append("")

    (base_dir / "conflicts.md").write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )


def _priority_rank(priority: str) -> int:
    return {"high": 0, "medium": 1, "low": 2}.get(priority, 3)


# Status vocabulary for evidence_backlog.v1.json items. Historically every item was
# emitted with status="open" and never updated, so the "open" count carried no signal
# (see insights_report.md, Literature Coverage note). The status is now DERIVED at
# generation time from the same claim_evidence.v1.json ground truth the backlog is built
# from, so it stays fresh on every governance run. A manual `user_status` override (carried
# forward across regenerations like user_notes) always wins when present.
#
#   open        -- no evidence of the needed type yet and governance has not engaged.
#   in_progress -- partial evidence of the needed type exists, OR a governance decision has
#                  been applied, OR an open mandatory decision checkpoint is pending.
#   covered     -- sufficient evidence of the needed type now EXISTS and routine collection
#                  can stop. Direction-AGNOSTIC: "covered" means the evidence gap the backlog
#                  item asked for is filled (PASS or FAIL); it does NOT assert the claim is
#                  supported. Any remaining action is a governance decision, not more data.
#   superseded  -- the claim itself is superseded in claims.yaml.
#
# Conservative `covered` rule (only mark covered with concrete evidence for THIS claim):
#   - the needed evidence type meets a volume bar (>=2 genuine experimental runs when
#     experimental is needed; >=3 literature entries when literature is needed); AND
#   - no open mandatory_decision_checkpoint; AND
#   - conflict_ratio < 0.5 (not an actively unresolved directional conflict); AND
#   - a governance decision has been applied OR the evidence is strong on its own
#     (>=5 genuine experimental runs, or >=6 literature entries).
# Literature is near-universal across claims, so a literature volume bar NEVER marks an
# experimental-needed item covered -- the needed type gates which volume bar applies.
_BACKLOG_COVERED_MIN_EXP = 2
_BACKLOG_COVERED_MIN_LIT = 3
_BACKLOG_STRONG_EXP = 5
_BACKLOG_STRONG_LIT = 6
_BACKLOG_COVERED_MAX_CONFLICT = 0.5


def _derive_backlog_status(
    *,
    evidence_needed: set[str],
    genuine_exp_count: int,
    lit_count: int,
    conflict_ratio: float,
    decision_status: str,
    mandatory_decision_checkpoint: bool,
    current_status: str | None,
) -> str:
    """Derive an evidence_backlog item status from claim-evidence ground truth.

    `evidence_needed` must be the genuine need snapshotted BEFORE the saturation /
    escalation / mandatory-checkpoint guards discard from it, so the needed-type gating
    is accurate.
    """
    if str(current_status or "").strip().lower() == "superseded":
        return "superseded"

    need = set(evidence_needed)
    decision_applied = str(decision_status or "").strip().lower() in {"applied", "approved"}

    exp_needed = "experimental" in need
    lit_needed = "literature" in need
    # If the need set was emptied by the guards, fall back to experimental (the indexer's
    # own default at the bottom of the loop) so a thin item is not spuriously "covered".
    if not exp_needed and not lit_needed:
        exp_needed = True

    exp_ok = (not exp_needed) or genuine_exp_count >= _BACKLOG_COVERED_MIN_EXP
    lit_ok = (not lit_needed) or lit_count >= _BACKLOG_COVERED_MIN_LIT
    strong = (exp_needed and genuine_exp_count >= _BACKLOG_STRONG_EXP) or (
        lit_needed and lit_count >= _BACKLOG_STRONG_LIT
    )

    covered = (
        exp_ok
        and lit_ok
        and not mandatory_decision_checkpoint
        and float(conflict_ratio) < _BACKLOG_COVERED_MAX_CONFLICT
        and (decision_applied or strong)
    )
    if covered:
        return "covered"

    some_evidence = (exp_needed and genuine_exp_count >= 1) or (
        lit_needed and lit_count >= 1
    )
    if some_evidence or decision_applied or mandatory_decision_checkpoint:
        return "in_progress"
    return "open"


def _backlog_urgency_rank(item: dict[str, Any]) -> tuple[int, float, int, str]:
    reasons = {str(r) for r in item.get("reasons", [])}
    signals = item.get("signals", {})
    conflict_ratio = float(signals.get("conflict_ratio", 0.0))
    entries_total = int(signals.get("entries_total", 0))
    # Lower rank is more urgent.
    # 0: architecture-pressure conflict triage, 1: active conflicts, 2+: evidence-coverage gaps.
    if "mandatory_decision_checkpoint" in reasons:
        tier = 0
    elif "escalate_architecture_decision" in reasons:
        tier = 0
    elif "anti_lock_in_review_required" in reasons or "external_precedence_pressure" in reasons:
        tier = 0
    elif "consider_new_structure" in reasons:
        tier = 1
    elif "active_conflict" in reasons or "directional_conflict_alert" in reasons:
        tier = 2
    elif "missing_experimental_evidence" in reasons:
        tier = 3
    elif "missing_literature_evidence" in reasons:
        tier = 4
    else:
        tier = 5
    return (tier, -conflict_ratio, -entries_total, str(item.get("claim_id", "")))


def _priority_from_reasons(reasons: list[str]) -> str:
    high_markers = {
        "mandatory_decision_checkpoint",
        "escalate_architecture_decision",
        "directional_conflict_alert",
        "active_conflict",
        "missing_experimental_evidence",
        "consider_new_structure",
        "external_precedence_pressure",
        "anti_lock_in_review_required",
        "atomic_split_recommended",
    }
    medium_markers = {
        "low_exp_conf",
        "lit_only_above_cap",
        "low_overall_confidence",  # legacy alias kept for one cycle
        "insufficient_experimental_replication",
        "insufficient_literature_grounding",
        "missing_literature_evidence",
    }
    if any(reason in high_markers for reason in reasons):
        return "high"
    if any(reason in medium_markers for reason in reasons):
        return "medium"
    return "low"


def _suggest_experiment_type(claim_id: str, matrix: dict[str, Any]) -> str:
    counts: Counter[str] = Counter()
    for entry in matrix.get("entries", []):
        if entry.get("claim_id") == claim_id and entry.get("source_type") == "experimental":
            counts.update([str(entry.get("experiment_type", "claim_probe"))])
    if counts:
        return counts.most_common(1)[0][0]
    return f"claim_probe_{claim_id.lower().replace('-', '_')}"


def _suggest_literature_type(claim_id: str, matrix: dict[str, Any]) -> str:
    counts: Counter[str] = Counter()
    for entry in matrix.get("entries", []):
        if entry.get("claim_id") == claim_id and entry.get("source_type") == "literature":
            counts.update([str(entry.get("experiment_type", "targeted_review"))])
    if counts:
        return counts.most_common(1)[0][0]
    return f"targeted_review_{claim_id.lower().replace('-', '_')}"


def _claim_stage_index(stage_order: list[str], stage_id: str) -> int:
    token = str(stage_id).strip()
    if token in stage_order:
        return stage_order.index(token)
    return -1


def _build_claim_evidence_stage_info(
    claim_id: str,
    claim_entries: list[dict[str, Any]],
    stage_cfg: dict[str, Any] | None,
) -> dict[str, Any]:
    if not isinstance(stage_cfg, dict):
        return {}

    configured_order = stage_cfg.get("stage_order", [])
    if isinstance(configured_order, list):
        stage_order = _dedupe_preserve_order([str(token).strip() for token in configured_order])
    else:
        stage_order = []
    if not stage_order:
        stage_order = ["proxy", "integration", "behavioral"]

    configured_stage = str(stage_cfg.get("current_stage", "proxy")).strip() or "proxy"
    if configured_stage not in stage_order:
        configured_stage = stage_order[0]

    observed_classes = _dedupe_preserve_order(
        [str(entry.get("evidence_class", "")).strip() for entry in claim_entries if str(entry.get("evidence_class", "")).strip()]
    )

    advance_rules_raw = stage_cfg.get("advance_rules", {})
    advance_rules: dict[str, list[str]] = {}
    if isinstance(advance_rules_raw, dict):
        for stage_id, prefixes_raw in advance_rules_raw.items():
            stage_token = str(stage_id).strip()
            if not stage_token or stage_token not in stage_order:
                continue
            prefixes: list[str] = []
            if isinstance(prefixes_raw, list):
                prefixes = _dedupe_preserve_order([str(token).strip() for token in prefixes_raw if str(token).strip()])
            if prefixes:
                advance_rules[stage_token] = prefixes

    resolved_stage = configured_stage
    resolved_index = _claim_stage_index(stage_order, resolved_stage)
    for candidate in stage_order:
        candidate_idx = _claim_stage_index(stage_order, candidate)
        if candidate_idx <= resolved_index:
            continue
        prefixes = advance_rules.get(candidate, [])
        if not prefixes:
            continue
        matched = any(
            observed.startswith(prefix)
            for observed in observed_classes
            for prefix in prefixes
        )
        if matched:
            resolved_stage = candidate
            resolved_index = candidate_idx

    governance_cfg = stage_cfg.get("governance", {})
    if not isinstance(governance_cfg, dict):
        governance_cfg = {}

    def _suppressed(min_stage_key: str) -> bool:
        min_stage = str(governance_cfg.get(min_stage_key, "")).strip()
        if not min_stage or min_stage not in stage_order:
            return False
        min_idx = _claim_stage_index(stage_order, min_stage)
        return resolved_index < min_idx

    notes = stage_cfg.get("notes", {})
    if not isinstance(notes, dict):
        notes = {}

    return {
        "claim_id": claim_id,
        "claim_focus": str(stage_cfg.get("claim_focus", "")).strip(),
        "stage_mode": str(stage_cfg.get("stage_mode", "")).strip(),
        "stage_order": stage_order,
        "configured_stage": configured_stage,
        "resolved_stage": resolved_stage,
        "proxy_noise_expected": bool(stage_cfg.get("proxy_noise_expected", False)),
        "observed_evidence_classes": observed_classes,
        "suppress_structure_signals": _suppressed("structure_signals_min_stage"),
        "suppress_external_precedence": _suppressed("external_precedence_min_stage"),
        "suppress_mandatory_decision": _suppressed("mandatory_decision_min_stage"),
        "proxy_interpretation": str(notes.get("proxy_interpretation", "")).strip(),
        "final_test_basis": str(notes.get("final_test_basis", "")).strip(),
    }


def _prior_failed_discriminative_attempts(
    claim_id: str, entries: list[dict[str, Any]]
) -> list[str]:
    """Return run_ids of prior experimental discriminative_pair attempts on this claim
    whose outcome was FAIL or whose evidence_direction was non_contributory / weakens.

    Used to suppress blind re-issue of discriminative_pair auto-stubs in the proposal
    generator when the claim already has a history of failed pair attempts -- the
    correct next step there is /failure-autopsy on the latest failing run, not another
    pair under the same substrate.
    """
    out: list[str] = []
    target = (claim_id or "").upper()
    for e in entries:
        if str(e.get("claim_id", "")).upper() != target:
            continue
        if str(e.get("source_type", "")).lower() != "experimental":
            continue
        exp_type = str(e.get("experiment_type", "")).lower()
        if "discriminative_pair" not in exp_type and "discriminative-pair" not in exp_type:
            continue
        status = str(e.get("status", "")).upper()
        direction = str(e.get("evidence_direction", "")).lower()
        if status == "FAIL" or direction in ("non_contributory", "weakens"):
            rid = e.get("run_id")
            if rid:
                out.append(str(rid))
    return out


def _write_planning_outputs(
    planning_root: Path,
    matrix: dict[str, Any],
    claim_registry: dict[str, dict[str, str]],
    conflicts: list[dict[str, Any]],
    latest_decisions: dict[str, DecisionLogEntry],
    latest_adjudication_decisions: dict[str, DecisionLogEntry],
    planning_criteria: dict[str, Any],
    generated_at: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    thresholds = planning_criteria.get("thresholds", {})
    routing = planning_criteria.get("repo_routing", {})
    adjudication = planning_criteria.get("model_adjudication", {})

    # Phase 3 cutover: prefer low_exp_conf; fall back to legacy low_overall_confidence.
    low_exp_conf_threshold = float(
        thresholds.get("low_exp_conf", thresholds.get("low_overall_confidence", 0.55))
    )
    lit_only_above_cap_threshold = float(thresholds.get("lit_only_above_cap", 0.50))
    conflict_alert_threshold = float(thresholds.get("conflict_ratio_alert", 0.40))
    candidate_min_exp = int(thresholds.get("candidate_min_experimental_entries", 2))
    provisional_min_lit = int(thresholds.get("provisional_min_literature_entries", 2))
    consider_conflict_ratio = float(thresholds.get("consider_new_structure_conflict_ratio", 0.70))
    consider_min_sig_repeats = max(
        1, int(thresholds.get("consider_new_structure_min_failure_signature_repeats", 3))
    )
    consider_min_distinct_sigs = max(
        1, int(thresholds.get("consider_new_structure_min_distinct_signatures", 2))
    )
    consider_min_lit_entries = max(
        1, int(thresholds.get("consider_new_structure_min_literature_entries", 2))
    )
    consider_lit_non_support_ratio = float(
        thresholds.get("consider_new_structure_literature_non_support_ratio", 0.50)
    )
    external_precedence_conflict_ratio = float(
        thresholds.get("external_precedence_conflict_ratio", 0.55)
    )
    external_precedence_min_conf_delta = float(
        thresholds.get("external_precedence_min_confidence_delta", 0.05)
    )
    external_precedence_min_total_entries = max(
        1, int(thresholds.get("external_precedence_min_total_entries", 6))
    )
    external_precedence_min_exp_entries = max(
        1, int(thresholds.get("external_precedence_min_experimental_entries", 4))
    )
    external_precedence_min_lit_entries = max(
        1, int(thresholds.get("external_precedence_min_literature_entries", 4))
    )
    external_precedence_min_recurring = max(
        1, int(thresholds.get("external_precedence_min_recurring_signatures", 2))
    )
    saturation_conflict_ratio = float(thresholds.get("proposal_saturation_conflict_ratio", 0.70))
    saturation_min_exp_entries = max(
        1, int(thresholds.get("proposal_saturation_min_experimental_entries", 16))
    )
    saturation_recent_window = max(
        1, int(thresholds.get("proposal_saturation_recent_window", 12))
    )
    saturation_min_recent_entries = max(
        1, int(thresholds.get("proposal_saturation_min_recent_entries", 8))
    )
    saturation_max_signature_sets = max(
        1, int(thresholds.get("proposal_saturation_max_unique_signature_sets", 2))
    )
    saturation_max_directions = max(
        1, int(thresholds.get("proposal_saturation_max_directions", 2))
    )
    escalation_min_conflict_ratio = float(thresholds.get("escalation_min_conflict_ratio", 0.75))
    escalation_min_exp_entries = max(
        1, int(thresholds.get("escalation_min_experimental_entries", 24))
    )
    escalation_min_recurring = max(
        1, int(thresholds.get("escalation_min_recurring_signatures", 2))
    )
    escalation_min_signature_count = max(
        1, int(thresholds.get("escalation_min_max_signature_count", 8))
    )
    mandatory_decision_conflict_ratio = float(
        thresholds.get("mandatory_decision_conflict_ratio", 0.80)
    )
    mandatory_decision_min_fresh_batches = max(
        1, int(thresholds.get("mandatory_decision_min_fresh_batches", 2))
    )
    mandatory_decision_recent_window = max(
        1, int(thresholds.get("mandatory_decision_recent_window", 24))
    )
    mandatory_decision_deadline_hours = max(
        1, int(thresholds.get("mandatory_decision_deadline_hours", 72))
    )
    atomic_split_conflict_ratio = float(
        thresholds.get("atomic_split_conflict_ratio", 0.70)
    )
    atomic_split_min_mixed_entries = max(
        1, int(thresholds.get("atomic_split_min_mixed_entries", 1))
    )
    atomic_split_min_recurring_signatures = max(
        1, int(thresholds.get("atomic_split_min_recurring_signatures", 2))
    )
    discriminative_pair_conflict_ratio = float(
        thresholds.get("discriminative_pair_conflict_ratio", 0.55)
    )
    discriminative_pair_min_shared_seeds = max(
        2, int(thresholds.get("discriminative_pair_min_shared_seeds", 2))
    )
    literature_min_disconfirming_entries = max(
        1, int(thresholds.get("literature_min_disconfirming_entries", 1))
    )

    default_exp_repo = str(routing.get("experimental_default_repo", "ree-v2"))
    exploratory_repo = str(routing.get("exploratory_repo", "ree-experiments-lab"))
    literature_owner = str(routing.get("literature_owner", "REE_assembly"))
    dispatch_overrides_raw = planning_criteria.get("dispatch_overrides", {})
    dispatch_overrides: dict[str, dict[str, Any]] = {}
    if isinstance(dispatch_overrides_raw, dict):
        for raw_claim_id, raw_override in dispatch_overrides_raw.items():
            claim_key = str(raw_claim_id).strip().upper()
            if not claim_key or not isinstance(raw_override, dict):
                continue
            dispatch_overrides[claim_key] = raw_override

    external_precedence_enabled = bool(adjudication.get("external_precedence_enabled", True))
    allowed_conflict_outcomes_raw = adjudication.get("allowed_conflict_outcomes", [])
    allowed_conflict_outcomes = [
        str(x).strip()
        for x in allowed_conflict_outcomes_raw
        if str(x).strip()
    ]
    if not allowed_conflict_outcomes:
        allowed_conflict_outcomes = [
            "retain_ree",
            "hybridize",
            "retire_ree_claim",
        ]
    default_conflict_outcome = str(adjudication.get("default_conflict_outcome", "retain_ree"))
    cascade_policy = adjudication.get("cascade_policy", {})
    cascade_enabled = bool(cascade_policy.get("enabled", True))
    cascade_trigger_outcomes_raw = cascade_policy.get(
        "trigger_outcomes", ["retire_ree_claim"]
    )
    cascade_trigger_outcomes = [
        str(x).strip()
        for x in cascade_trigger_outcomes_raw
        if str(x).strip()
    ]
    dependency_reopen_status = str(cascade_policy.get("dependency_reopen_status", "candidate"))
    cascade_followup_required = bool(cascade_policy.get("require_followup_proposals", True))
    override_mode = adjudication.get("temporary_override_mode", {})
    override_mode_enabled = bool(override_mode.get("enabled", True))
    override_mode_id = str(override_mode.get("mode_id", "external_model_proxy_override"))
    override_requirements_raw = override_mode.get("requirements", [])
    override_requirements = [
        str(x).strip()
        for x in override_requirements_raw
        if str(x).strip()
    ]
    anti_lock_in_gate = adjudication.get("anti_lock_in_gate", {})
    anti_lock_in_enabled = bool(anti_lock_in_gate.get("enabled", True))
    staging_root = planning_criteria.get("claim_evidence_staging", {})
    staging_enabled = bool(staging_root.get("enabled", False)) if isinstance(staging_root, dict) else False
    staging_claims: dict[str, dict[str, Any]] = {}
    if staging_enabled and isinstance(staging_root, dict):
        raw_claims = staging_root.get("claims", {})
        if isinstance(raw_claims, dict):
            for raw_claim_id, raw_cfg in raw_claims.items():
                claim_key = str(raw_claim_id).strip().upper()
                if not claim_key or not isinstance(raw_cfg, dict):
                    continue
                staging_claims[claim_key] = raw_cfg
    generated_at_dt = _parse_timestamp_only(generated_at)

    conflicts_by_claim = {str(item.get("claim_id")): item for item in conflicts}
    applicability_scope_label, is_applicable = _build_applicability_filter(planning_criteria)
    matrix_claims = matrix.get("claims", {})
    claim_ids = sorted(set(claim_registry.keys()) | set(matrix_claims.keys()))
    entries_by_claim: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in matrix.get("entries", []):
        if not isinstance(entry, dict):
            continue
        claim_key = str(entry.get("claim_id", "")).strip()
        if claim_key:
            # Mirror _write_claim_evidence_matrix policy: literature entries are
            # not epoch-filtered. Without this exemption, pre-cutoff lit entries
            # were silently dropped from the backlog view, causing
            # missing_literature_evidence to fire on claims with valid literature.
            if entry.get("source_type") == "literature" or is_applicable(entry):
                entries_by_claim[claim_key].append(entry)

    # ── Pre-load pinned items to prevent auto-generation collision ────────────────
    # Read the existing backlog BEFORE the auto-generation loop so pinned claim_ids
    # can be skipped during auto-generation. This preserves their rich content
    # (title, description, papers_to_extract, acceptance_criteria, etc.) and
    # their original backlog_id (e.g. EVB-PINNED-Q019) without any merge logic.
    _early_backlog_path = planning_root / "evidence_backlog.v1.json"
    _pinned_claim_ids: set[str] = set()
    _preloaded_pinned_items: list[dict[str, Any]] = []
    if _early_backlog_path.exists():
        try:
            _early_doc = json.loads(_early_backlog_path.read_text(encoding="utf-8"))
            for _pit in _early_doc.get("items", []):
                if isinstance(_pit, dict) and _pit.get("pinned", False):
                    _pcid = str(_pit.get("claim_id", "")).strip()
                    if _pcid:
                        _pinned_claim_ids.add(_pcid)
                        _preloaded_pinned_items.append(dict(_pit))
        except Exception:
            pass  # Missing or corrupt backlog — no pinned items to protect
    # ── end pre-load ─────────────────────────────────────────────────────────────

    backlog_items: list[dict[str, Any]] = []
    architecture_items: list[dict[str, Any]] = []
    # Pseudo-claim filter: drop non-canonical claim_ids that flow in via the
    # evidence matrix (e.g. "onboarding" from contributor smoke tests). These
    # are bucket labels for instrumentation runs, not registered claims; without
    # this filter they auto-generate spurious backlog items (canonical incident:
    # phantom EVB-0131 onboarding, surfaced repeatedly in lit-pull-am scans
    # 2026-05-05..05-07). Real claims either (a) appear in claim_registry, or
    # (b) match the canonical prefix pattern and will be added to the registry
    # when fully described.
    _CANONICAL_CLAIM_RE = re.compile(r"^(INV|ARC|MECH|SD|Q|IMPL)-")
    for claim_id in claim_ids:
        if claim_id not in claim_registry and not _CANONICAL_CLAIM_RE.match(claim_id):
            continue  # Pseudo-claim (smoke-test bucket, instrumentation label, etc.)
        registry_meta = claim_registry.get(claim_id, {})
        current_status = str(registry_meta.get("status", "unknown"))
        if _is_inactive_claim_status(current_status):
            continue
        if claim_id in _pinned_claim_ids:
            continue  # Pinned backlog entry governs this claim; skip auto-generation
        claim_type = str(registry_meta.get("claim_type", "unknown"))
        claim_entries = entries_by_claim.get(claim_id, [])
        claim_meta = _summarize_claim_entries(claim_entries, generated_at_dt) if claim_entries else None

        reasons: list[str] = []
        evidence_needed: set[str] = set()
        stage_info: dict[str, Any] = {}
        suppress_structure_signals = False
        suppress_external_precedence = False
        suppress_mandatory_decision = False

        def _add_reason(token: str) -> None:
            if token and token not in reasons:
                reasons.append(token)

        if staging_enabled:
            stage_info = _build_claim_evidence_stage_info(
                claim_id,
                claim_entries,
                staging_claims.get(claim_id),
            )
            if stage_info:
                suppress_structure_signals = bool(stage_info.get("suppress_structure_signals", False))
                suppress_external_precedence = bool(stage_info.get("suppress_external_precedence", False))
                suppress_mandatory_decision = bool(stage_info.get("suppress_mandatory_decision", False))
                if bool(stage_info.get("proxy_noise_expected", False)):
                    _add_reason("proxy_stage_noise_expected")
        signals: dict[str, Any] = {
            "current_status": current_status,
            "claim_type": claim_type,
        }
        if stage_info:
            signals["evidence_stage"] = stage_info
        overall_conf = 0.0
        exp_count = 0
        genuine_exp_count = 0
        lit_count = 0
        conflict_ratio = 0.0
        entries_total = 0
        experimental_confidence = 0.0
        literature_confidence = 0.0
        confidence_delta_lit_minus_exp = 0.0
        supports_count = 0
        weakens_count = 0
        mixed_count = 0
        external_precedence_candidate = False
        anti_lock_in_review_required = False
        saturation_guard_engaged = False
        escalate_architecture_decision = False
        mandatory_decision_checkpoint = False
        atomic_split_recommended = False
        decision_deadline_utc = ""
        recent_targeted_batches = 0
        saturation_signal_details: dict[str, Any] = {}

        signature_counts: Counter[str] = Counter()
        for entry in claim_entries:
            # Only collect failure signatures from genuine experimental entries or literature.
            # Synthetic experimental entries (_toyenv_internal_minimal) produce invalid counts.
            if (
                str(entry.get("source_type", "")) == "experimental"
                and not _is_genuine_experimental_entry(entry)
            ):
                continue
            for sig in entry.get("failure_signatures", []):
                token = str(sig).strip()
                if token:
                    signature_counts[token] += 1
        recurring_signatures = [
            {"signature": sig, "count": count}
            for sig, count in signature_counts.most_common()
            if count >= consider_min_sig_repeats
        ]
        max_recurring_signature_count = (
            int(recurring_signatures[0].get("count", 0)) if recurring_signatures else 0
        )

        exp_entries = [
            entry
            for entry in claim_entries
            if str(entry.get("source_type", "")) == "experimental"
            and _is_genuine_experimental_entry(entry)
        ]
        exp_entries.sort(key=lambda x: (str(x.get("timestamp_utc", "")), str(x.get("run_id", ""))))
        recent_exp_entries = exp_entries[-saturation_recent_window:]
        if not recent_exp_entries:
            recent_exp_entries = exp_entries
        recent_direction_set = {
            str(entry.get("evidence_direction", "unknown")) for entry in recent_exp_entries
        }
        unique_signature_sets: set[tuple[str, ...]] = set()
        for entry in recent_exp_entries:
            sigs = {
                str(sig).strip() for sig in entry.get("failure_signatures", []) if str(sig).strip()
            }
            if not sigs:
                sigs = {"__none__"}
            unique_signature_sets.add(tuple(sorted(sigs)))
        decision_recent_exp_entries = exp_entries[-mandatory_decision_recent_window:]
        if not decision_recent_exp_entries:
            decision_recent_exp_entries = exp_entries
        batch_keys: set[str] = set()
        for entry in decision_recent_exp_entries:
            ts_raw = str(entry.get("timestamp_utc", "")).strip()
            if ts_raw:
                try:
                    batch_dt = _parse_timestamp_only(ts_raw).replace(second=0, microsecond=0)
                    batch_key = batch_dt.isoformat().replace("+00:00", "Z")
                except ValueError:
                    batch_key = ts_raw
            else:
                run_id = str(entry.get("run_id", "")).strip()
                batch_key = run_id.split("_", 1)[0] if run_id else ""
            if batch_key:
                batch_keys.add(batch_key)
        recent_targeted_batches = len(batch_keys)
        if recent_targeted_batches > 0:
            signals["recent_targeted_batches"] = recent_targeted_batches

        lit_direction_counts: Counter[str] = Counter()
        for entry in claim_entries:
            if str(entry.get("source_type", "")) != "literature":
                continue
            lit_direction_counts.update([str(entry.get("evidence_direction", "unknown"))])
        lit_total = int(sum(lit_direction_counts.values()))
        lit_non_support = int(
            lit_direction_counts.get("weakens", 0) + lit_direction_counts.get("mixed", 0)
        )
        lit_non_support_ratio = round((lit_non_support / lit_total), 3) if lit_total else 0.0

        decision_entry = latest_decisions.get(claim_id)
        outcome_decision_entry = latest_adjudication_decisions.get(claim_id)
        decision_state = {
            "decision_status": decision_entry.decision_status if decision_entry else "none",
            "timestamp_utc": decision_entry.timestamp_utc if decision_entry else "",
            "recommendation": decision_entry.recommendation if decision_entry else "",
        }
        outcome_decision_state = {
            "decision_status": (
                outcome_decision_entry.decision_status if outcome_decision_entry else "none"
            ),
            "timestamp_utc": (
                outcome_decision_entry.timestamp_utc if outcome_decision_entry else ""
            ),
            "recommendation": (
                outcome_decision_entry.recommendation if outcome_decision_entry else ""
            ),
        }
        effective_decision_state = (
            outcome_decision_state
            if outcome_decision_entry is not None
            else decision_state
        )

        if claim_meta is None:
            if claim_type == "open_question":
                reasons.append("no_evidence_for_open_question")
                evidence_needed.update({"experimental", "literature"})
                signals.update(
                    {
                        "overall_confidence": 0.0,
                        "source_counts": {"experimental": 0, "literature": 0},
                        "conflict_ratio": 0.0,
                    }
                )
            else:
                continue
        else:
            overall_conf = float(claim_meta.get("overall_confidence", 0.0))
            source_counts = claim_meta.get("source_counts", {})
            exp_count = int(source_counts.get("experimental", 0))
            genuine_exp_count = int(claim_meta.get("genuine_exp_count", 0))
            lit_count = int(source_counts.get("literature", 0))
            entries_total = int(claim_meta.get("entries_total", 0))
            experimental_confidence = float(claim_meta.get("experimental_confidence", 0.0))
            literature_confidence = float(claim_meta.get("literature_confidence", 0.0))
            confidence_delta_lit_minus_exp = literature_confidence - experimental_confidence
            direction_counts = claim_meta.get("direction_counts", {})
            supports_count = int(direction_counts.get("supports", 0))
            weakens_count = int(direction_counts.get("weakens", 0))
            mixed_count = int(direction_counts.get("mixed", 0))
            # Compute conflict_ratio from genuine experimental + literature only.
            # Synthetic experimental entries inflate conflict signals spuriously.
            _genuine_dirs = claim_meta.get("genuine_exp_direction_counts", {})
            _combined_dirs: dict[str, int] = {
                k: int(_genuine_dirs.get(k, 0)) + int(lit_direction_counts.get(k, 0))
                for k in ("supports", "weakens", "mixed", "unknown")
            }
            conflict_ratio = _direction_conflict_ratio(_combined_dirs)

            signals.update(
                {
                    "overall_confidence": round(overall_conf, 3),
                    "source_counts": {
                        "experimental": exp_count,
                        "literature": lit_count,
                    },
                    "confidence_split": {
                        "experimental_confidence": round(experimental_confidence, 3),
                        "literature_confidence": round(literature_confidence, 3),
                        "delta_lit_minus_exp": round(confidence_delta_lit_minus_exp, 3),
                    },
                    "entries_total": entries_total,
                    "conflict_ratio": conflict_ratio,
                }
            )

            # Phase 3 cutover (Option E): use exp_conf for the low-confidence
            # planning flag, with a separate lit_only_above_cap flag for the
            # case where literature alone is propping a claim up.
            if experimental_confidence < low_exp_conf_threshold:
                _add_reason("low_exp_conf")
            if exp_count == 0 and literature_confidence >= lit_only_above_cap_threshold:
                _add_reason("lit_only_above_cap")
            if exp_count == 0:
                _add_reason("missing_experimental_evidence")
                evidence_needed.add("experimental")
            if lit_count == 0:
                _add_reason("missing_literature_evidence")
                evidence_needed.add("literature")
            if conflict_ratio >= conflict_alert_threshold:
                if not suppress_structure_signals:
                    _add_reason("directional_conflict_alert")
                # Directional conflict requires new experimental discrimination first.
                # Ask for literature only when no literature is present yet.
                evidence_needed.add("experimental")
                if lit_count == 0:
                    evidence_needed.add("literature")
            if current_status == "candidate" and exp_count < candidate_min_exp:
                _add_reason("insufficient_experimental_replication")
                evidence_needed.add("experimental")
            if current_status == "provisional" and lit_count < provisional_min_lit:
                _add_reason("insufficient_literature_grounding")
                evidence_needed.add("literature")

            if claim_id in conflicts_by_claim:
                if not suppress_structure_signals:
                    _add_reason("active_conflict")
                # Conflict claims should always get experimental follow-up.
                # Requiring literature again when it already exists causes an infinite
                # re-proposal loop and task churn.
                evidence_needed.add("experimental")
                if lit_count == 0:
                    evidence_needed.add("literature")

        structure_signals: list[str] = []
        if not suppress_structure_signals:
            if conflict_ratio >= consider_conflict_ratio:
                structure_signals.append("high_conflict_ratio")
            if len(recurring_signatures) >= consider_min_distinct_sigs:
                structure_signals.append("recurring_failure_signatures")
            if (
                lit_total >= consider_min_lit_entries
                and lit_non_support_ratio >= consider_lit_non_support_ratio
            ):
                structure_signals.append("literature_non_support_pressure")
        else:
            signals["stage_structure_signals_suppressed"] = True

        if (
            external_precedence_enabled
            and not suppress_external_precedence
            and conflict_ratio >= external_precedence_conflict_ratio
            and entries_total >= external_precedence_min_total_entries
            and lit_count >= external_precedence_min_lit_entries
            and genuine_exp_count >= external_precedence_min_exp_entries
            and len(recurring_signatures) >= external_precedence_min_recurring
            and confidence_delta_lit_minus_exp >= external_precedence_min_conf_delta
        ):
            structure_signals.append("external_precedence_pressure")
            external_precedence_candidate = True
            _add_reason("external_precedence_pressure")
            evidence_needed.add("experimental")
            if lit_count == 0:
                evidence_needed.add("literature")

            if anti_lock_in_enabled and current_status in {"candidate", "provisional", "active", "stable"}:
                anti_lock_in_review_required = True
                _add_reason("anti_lock_in_review_required")

        consider_new_structure = len(structure_signals) >= 3
        if consider_new_structure:
            _add_reason("consider_new_structure")
            evidence_needed.add("experimental")
            if lit_count == 0:
                evidence_needed.add("literature")

        if (
            conflict_ratio >= saturation_conflict_ratio
            and genuine_exp_count >= saturation_min_exp_entries
            and len(recurring_signatures) >= consider_min_distinct_sigs
            and len(recent_exp_entries) >= saturation_min_recent_entries
            and len(unique_signature_sets) <= saturation_max_signature_sets
            and len(recent_direction_set) <= saturation_max_directions
        ):
            saturation_guard_engaged = True
            saturation_signal_details = {
                "recent_window_used": len(recent_exp_entries),
                "unique_signature_sets": len(unique_signature_sets),
                "unique_directions": len(recent_direction_set),
            }
            signals["proposal_saturation"] = dict(saturation_signal_details)
            _add_reason("saturation_guard_hold")

        if (
            consider_new_structure
            and conflict_ratio >= escalation_min_conflict_ratio
            and exp_count >= escalation_min_exp_entries
            and len(recurring_signatures) >= escalation_min_recurring
            and max_recurring_signature_count >= escalation_min_signature_count
        ):
            escalate_architecture_decision = True
            signals["escalation_required"] = True
            _add_reason("escalate_architecture_decision")

        if (
            conflict_ratio >= atomic_split_conflict_ratio
            and supports_count > 0
            and weakens_count > 0
            and mixed_count >= atomic_split_min_mixed_entries
            and len(recurring_signatures) >= atomic_split_min_recurring_signatures
        ):
            atomic_split_recommended = True
            signals["atomic_split_recommended"] = True
            _add_reason("atomic_split_recommended")

        decision_status = str(outcome_decision_state.get("decision_status", "none")).strip().lower()
        decision_recommendation = str(outcome_decision_state.get("recommendation", "")).strip()
        decision_resolved = (
            decision_status in {"approved", "applied"}
            and decision_recommendation in allowed_conflict_outcomes
        )
        decision_unresolved = not decision_resolved
        if (
            not suppress_mandatory_decision
            and
            conflict_ratio >= mandatory_decision_conflict_ratio
            and recent_targeted_batches >= mandatory_decision_min_fresh_batches
            and decision_unresolved
        ):
            mandatory_decision_checkpoint = True
            decision_deadline_utc = (
                generated_at_dt + timedelta(hours=mandatory_decision_deadline_hours)
            ).isoformat().replace("+00:00", "Z")
            signals["mandatory_decision_checkpoint"] = True
            signals["decision_deadline_utc"] = decision_deadline_utc
            signals["decision_required_outcomes"] = list(allowed_conflict_outcomes)
            _add_reason("mandatory_decision_checkpoint")

        # Snapshot the genuine evidence need BEFORE the guards below discard from it, so the
        # backlog status derivation can gate "covered" on the correct evidence type.
        _status_evidence_needed = set(evidence_needed)

        # Saturation guard prevents infinite re-dispatch loops for stale experimental probes.
        if saturation_guard_engaged and "experimental" in evidence_needed:
            evidence_needed.discard("experimental")
        # Escalation guard routes repeated-failure claims to architecture decisions before more routine reruns.
        if escalate_architecture_decision and "experimental" in evidence_needed:
            evidence_needed.discard("experimental")
        # Mandatory decision checkpoint halts routine reruns until an explicit outcome is recorded.
        if mandatory_decision_checkpoint:
            evidence_needed.discard("experimental")
            evidence_needed.discard("literature")

        if claim_meta is not None and (structure_signals or recurring_signatures):
            architecture_items.append(
                {
                    "gap_id": "",
                    "claim_id": claim_id,
                    "claim_type": claim_type,
                    "current_status": current_status,
                    "overall_confidence": round(overall_conf, 3),
                    "conflict_ratio": round(conflict_ratio, 3),
                    "source_counts": {
                        "experimental": exp_count,
                        "literature": lit_count,
                    },
                    "literature_direction_counts": {
                        "supports": int(lit_direction_counts.get("supports", 0)),
                        "weakens": int(lit_direction_counts.get("weakens", 0)),
                        "mixed": int(lit_direction_counts.get("mixed", 0)),
                        "unknown": int(lit_direction_counts.get("unknown", 0)),
                    },
                    "literature_non_support_ratio": lit_non_support_ratio,
                    "confidence_split": {
                        "experimental_confidence": round(experimental_confidence, 3),
                        "literature_confidence": round(literature_confidence, 3),
                        "delta_lit_minus_exp": round(confidence_delta_lit_minus_exp, 3),
                    },
                    "external_precedence_candidate": external_precedence_candidate,
                    "anti_lock_in_review_required": anti_lock_in_review_required,
                    "saturation_guard_engaged": saturation_guard_engaged,
                    "escalate_architecture_decision": escalate_architecture_decision,
                    "mandatory_decision_checkpoint": mandatory_decision_checkpoint,
                    "decision_deadline_utc": decision_deadline_utc,
                    "decision_required_outcomes": (
                        list(allowed_conflict_outcomes) if mandatory_decision_checkpoint else []
                    ),
                    "recent_targeted_batches": recent_targeted_batches,
                    "atomic_split_recommended": atomic_split_recommended,
                    "saturation_signal_details": saturation_signal_details,
                    "recurring_failure_signatures": recurring_signatures[:5],
                    "trigger_signals": sorted(set(structure_signals)),
                    "evidence_stage": stage_info,
                    "consider_new_structure": consider_new_structure,
                    "recommendation": (
                        "mandatory_decision_checkpoint"
                        if mandatory_decision_checkpoint
                        else
                        "escalate_architecture_decision"
                        if escalate_architecture_decision
                        else "consider_new_structure"
                        if consider_new_structure
                        else "monitor_and_collect_targeted_evidence"
                    ),
                    "adjudication_policy": {
                        "default_conflict_outcome": default_conflict_outcome,
                        "allowed_conflict_outcomes": allowed_conflict_outcomes,
                        "cascade_policy": {
                            "enabled": cascade_enabled,
                            "trigger_outcomes": cascade_trigger_outcomes,
                            "dependency_reopen_status": dependency_reopen_status,
                            "require_followup_proposals": cascade_followup_required,
                        },
                        "temporary_override_mode": {
                            "enabled": override_mode_enabled,
                            "mode_id": override_mode_id,
                            "requirements": override_requirements,
                        },
                        "anti_lock_in_gate_enabled": anti_lock_in_enabled,
                    },
                    "latest_decision": effective_decision_state,
                }
            )

        if not reasons:
            continue

        priority = _priority_from_reasons(reasons)
        # Downgrade from high → medium when ALL escalation signals came from synthetic
        # experimental entries. Genuine-only filtering should prevent most false alarms,
        # but this acts as a safety net for residual cases.
        if (
            priority == "high"
            and genuine_exp_count == 0
            and "mandatory_decision_checkpoint" not in reasons
        ):
            priority = "medium"
            _add_reason("synthetic_signals_only")
        if not evidence_needed and not (
            saturation_guard_engaged or escalate_architecture_decision
        ):
            evidence_needed.add("experimental")

        next_action = "Run targeted experimental probe."
        if evidence_needed == {"literature"}:
            next_action = "Run targeted literature extraction and claim linkage."
        elif evidence_needed == {"experimental", "literature"}:
            next_action = "Run paired experiment + literature cycle before status change."
        if "consider_new_structure" in reasons:
            next_action = (
                "Draft architecture options for this claim, then run one adjudication experiment "
                "and one targeted literature extraction."
            )
        if "external_precedence_pressure" in reasons:
            next_action = (
                "Run matched-protocol adjudication and choose conflict outcome: "
                "retain_ree|hybridize|retire_ree_claim."
            )
        if "anti_lock_in_review_required" in reasons:
            next_action = (
                "Run anti-lock-in review and forbid schema-preserving tuning without selecting a "
                "recorded conflict outcome."
            )
        if "saturation_guard_hold" in reasons:
            next_action = (
                "Pause repetitive low-information reruns and require either a materially different "
                "protocol variation or an architecture decision before new experimental dispatch."
            )
        if "atomic_split_recommended" in reasons:
            next_action = (
                "Split this claim into atomic subclaims before broad reruns; then run one discriminative "
                "support-vs-ablation pair per subclaim."
            )
        if "escalate_architecture_decision" in reasons:
            next_action = (
                "Escalate to architecture decision queue now (retain_ree|hybridize|retire_ree_claim) "
                "and hold additional routine reruns until the decision is recorded."
            )
        if "mandatory_decision_checkpoint" in reasons:
            deadline_note = f" by {decision_deadline_utc}" if decision_deadline_utc else ""
            next_action = (
                "Decision checkpoint required"
                + deadline_note
                + ": choose one outcome "
                + "retain_ree|hybridize|retire_ree_claim and pause routine reruns "
                + "until the decision is recorded."
            )

        backlog_items.append(
            {
                "backlog_id": "",
                "claim_id": claim_id,
                "priority": priority,
                "reasons": sorted(set(reasons)),
                "signals": signals,
                "evidence_needed": sorted(evidence_needed),
                "recommendation": (
                    "mandatory_decision_checkpoint"
                    if mandatory_decision_checkpoint
                    else
                    "escalate_architecture_decision"
                    if escalate_architecture_decision
                    else "consider_new_structure"
                    if consider_new_structure
                    else "collect_targeted_evidence"
                ),
                "next_action": next_action,
                "adjudication_context": {
                    "default_conflict_outcome": default_conflict_outcome,
                    "allowed_conflict_outcomes": allowed_conflict_outcomes,
                    "external_precedence_candidate": external_precedence_candidate,
                    "anti_lock_in_review_required": anti_lock_in_review_required,
                    "saturation_guard_engaged": saturation_guard_engaged,
                    "escalate_architecture_decision": escalate_architecture_decision,
                    "mandatory_decision_checkpoint": mandatory_decision_checkpoint,
                    "decision_deadline_utc": decision_deadline_utc,
                    "decision_required_outcomes": (
                        list(allowed_conflict_outcomes) if mandatory_decision_checkpoint else []
                    ),
                    "atomic_split_recommended": atomic_split_recommended,
                    "saturation_signal_details": saturation_signal_details,
                    "cascade_policy": {
                        "enabled": cascade_enabled,
                        "trigger_outcomes": cascade_trigger_outcomes,
                        "dependency_reopen_status": dependency_reopen_status,
                        "require_followup_proposals": cascade_followup_required,
                    },
                    "temporary_override_mode": {
                        "enabled": override_mode_enabled,
                        "mode_id": override_mode_id,
                        "requirements": override_requirements,
                    },
                },
                "latest_decision": effective_decision_state,
                "status": _derive_backlog_status(
                    evidence_needed=_status_evidence_needed,
                    genuine_exp_count=genuine_exp_count,
                    lit_count=lit_count,
                    conflict_ratio=conflict_ratio,
                    decision_status=str(
                        effective_decision_state.get("decision_status", "none")
                    ),
                    mandatory_decision_checkpoint=mandatory_decision_checkpoint,
                    current_status=current_status,
                ),
            }
        )

    # ── Backlog merge: carry forward user_notes + stable backlog_ids; append pinned ──
    # Pinned items were excluded from auto-generation above so there is no collision.
    # We carry forward (a) user_notes and (b) backlog_id mappings so that EVB-NNNN
    # IDs remain stable across regenerations. The carry-forward keys on claim_id, which
    # is unique within a single backlog (one item per claim that needs evidence).
    existing_backlog_path = planning_root / "evidence_backlog.v1.json"
    _existing_user_notes: dict[str, str] = {}
    _existing_user_status: dict[str, str] = {}  # claim_id -> manual status override
    _existing_backlog_ids: dict[str, str] = {}  # claim_id -> EVB-NNNN
    _used_numeric_ids: set[int] = set()
    if existing_backlog_path.exists():
        try:
            _existing_doc = json.loads(existing_backlog_path.read_text(encoding="utf-8"))
            for _item in _existing_doc.get("items", []):
                if not isinstance(_item, dict):
                    continue
                _cid = str(_item.get("claim_id", "")).strip()
                if _cid and "user_notes" in _item and _item["user_notes"]:
                    _existing_user_notes[_cid] = str(_item["user_notes"])
                # A human-pinned status override always wins over the derived value.
                if _cid and _item.get("user_status"):
                    _existing_user_status[_cid] = str(_item["user_status"])
                _bid = str(_item.get("backlog_id", "")).strip()
                # Only carry forward auto-generated IDs (EVB-NNNN, not EVB-PINNED-*).
                # Pinned items handle their own ID via the _preloaded_pinned_items path.
                if _cid and _bid and not _item.get("pinned", False):
                    _m = re.fullmatch(r"EVB-(\d{4,})", _bid)
                    if _m:
                        _existing_backlog_ids[_cid] = _bid
                        _used_numeric_ids.add(int(_m.group(1)))
        except Exception:
            pass  # Corrupt or missing backlog -- skip carry-forward

    # Restore preserved user_notes + honour manual user_status overrides on auto-generated items
    for item in backlog_items:
        _cid = str(item.get("claim_id", ""))
        if _cid in _existing_user_notes:
            item["user_notes"] = _existing_user_notes[_cid]
        if _cid in _existing_user_status:
            item["user_status"] = _existing_user_status[_cid]
            item["status"] = _existing_user_status[_cid]

    # Append pre-loaded pinned items -- rich content and original backlog_id intact
    backlog_items.extend(_preloaded_pinned_items)
    # ── end merge ────────────────────────────────────────────────────────────────

    backlog_items.sort(
        key=lambda item: (
            _priority_rank(str(item.get("priority", "low"))),
            _backlog_urgency_rank(item),
        )
    )
    # Persistent ID assignment (fixes EVB-ID instability that affected morning-agenda
    # references and silently mis-attached experiment_proposals.v1.json status fields).
    # Strategy: reuse existing EVB-NNNN for any claim_id that was in the previous backlog;
    # assign new IDs starting strictly above the prior max so collisions are impossible.
    _next_auto_idx = (max(_used_numeric_ids) + 1) if _used_numeric_ids else 1
    for item in backlog_items:
        if item.get("pinned", False):
            continue  # Pinned items keep their EVB-PINNED-* IDs from the preload path
        _cid = str(item.get("claim_id", ""))
        if _cid in _existing_backlog_ids:
            item["backlog_id"] = _existing_backlog_ids[_cid]
        else:
            item["backlog_id"] = f"EVB-{_next_auto_idx:04d}"
            _next_auto_idx += 1

    architecture_items.sort(
        key=lambda item: (
            0 if bool(item.get("consider_new_structure", False)) else 1,
            -float(item.get("conflict_ratio", 0.0)),
            str(item.get("claim_id", "")),
        )
    )
    for idx, item in enumerate(architecture_items, start=1):
        item["gap_id"] = f"AGR-{idx:04d}"

    proposals: list[dict[str, Any]] = []
    proposal_counter = 1
    # Numeric proposal-id indices already hand-assigned in manual_proposals.v1.json
    # (e.g. EXP-0085..EXP-0176). The auto counter below MUST skip these so an
    # auto-generated EXP-/LIT-NNNN id never collides with a manual proposal id.
    # The manual ids own the EXP-NNNN namespace and are referenced by governance
    # docs; auto ids are positional/ephemeral (keyed for stability on backlog_id,
    # not proposal_id). Reserve from BOTH prefixes because the EXP/LIT counter is
    # shared -- a manual LIT-0099 must block auto EXP-0099 and LIT-0099 alike.
    # (Fixes the 47 duplicate proposal_ids the old shared-namespace counter
    # produced in the generated experiment_proposals.v1.json.)
    _manual_reserved_idx: set[int] = set()
    _manual_ids_path = planning_root / "manual_proposals.v1.json"
    if _manual_ids_path.exists():
        try:
            _manual_ids_doc = json.loads(_manual_ids_path.read_text(encoding="utf-8"))
            for _mp_item in _manual_ids_doc.get("items", []):
                _mp_match = re.match(
                    r"^(?:EXP|LIT)-(\d+)$",
                    str((_mp_item or {}).get("proposal_id") or ""),
                )
                if _mp_match:
                    _manual_reserved_idx.add(int(_mp_match.group(1)))
        except Exception:
            pass  # malformed manual file -- no reservations (skip silently)

    def _alloc_proposal_idx() -> int:
        """Next auto proposal index, skipping any manual-reserved numeric id."""
        nonlocal proposal_counter
        while proposal_counter in _manual_reserved_idx:
            proposal_counter += 1
        idx = proposal_counter
        proposal_counter += 1
        return idx

    for item in backlog_items:
        claim_id = str(item["claim_id"])
        reasons = [str(r) for r in item.get("reasons", [])]
        signals = item.get("signals", {})
        conflict_ratio = float(signals.get("conflict_ratio", 0.0))
        needed = set(item.get("evidence_needed", []))

        # Experimental-proposal-eligibility gate: do NOT mint an EXP-* proposal
        # for a claim a REE experiment can't or shouldn't settle -- answered/
        # closing statuses (resolved/open/retiring) or a resolved epistemic_
        # category settled by literature/derivation/policy (out_of_domain/
        # derivational/governance_rule). The backlog loop only drops
        # _is_inactive_claim_status claims, so these still arrive here carrying
        # an "experimental" need (live residue: Q-020->EXP-0056, Q-035->EXP-0112,
        # and Q-079 once it next regenerates). The literature branch below is
        # left intact (out_of_domain is answered by literature).
        experiment_ineligible = _is_experiment_ineligible_claim(
            claim_registry.get(claim_id, {})
        )

        if "experimental" in needed and not experiment_ineligible:
            target_repo = exploratory_repo if conflict_ratio >= 0.7 else default_exp_repo
            exp_type = _suggest_experiment_type(claim_id, matrix)
            discriminative_pair_required = (
                conflict_ratio >= discriminative_pair_conflict_ratio
                or "active_conflict" in reasons
                or "directional_conflict_alert" in reasons
                or "mandatory_decision_checkpoint" in reasons
            )
            objective = f"Reduce uncertainty for {claim_id} via targeted experiment runs."
            if discriminative_pair_required:
                objective = (
                    f"Run a discriminative support-vs-ablation pair for {claim_id} "
                    "with matched seeds and pre-registered thresholds."
                )
            if "mandatory_decision_checkpoint" in reasons:
                objective = (
                    f"Generate decision-grade discriminative evidence for {claim_id} before governance deadline."
                )
            dispatch_mode = "discriminative_pair" if discriminative_pair_required else "targeted_probe"
            seed_policy = "matched_shared_seeds" if discriminative_pair_required else "distinct_seeds"
            min_shared_seeds = discriminative_pair_min_shared_seeds if discriminative_pair_required else 0
            require_pre_registered_thresholds = bool(discriminative_pair_required)
            exclude_broad_profile_sweeps = bool(discriminative_pair_required)
            acceptance_checks = [
                "Experiment Pack validates against v1 schema.",
                "Result links to claim_ids_tested and updates matrix direction counts.",
            ]
            if discriminative_pair_required:
                acceptance_checks = [
                    "Run exactly one claim-focused discriminative pair: primary condition vs explicit ablation/control.",
                    f"Use at least {discriminative_pair_min_shared_seeds} matched seeds shared across both pair conditions.",
                    "Pre-register metric thresholds and pass/fail criteria before execution, then report deltas against that registration.",
                    "Avoid broad profile sweeps for this dispatch item; emit only pair-comparison run packs.",
                ] + acceptance_checks
            else:
                acceptance_checks.insert(0, "At least 2 additional runs with distinct seeds.")
            if "atomic_split_recommended" in reasons:
                acceptance_checks.append(
                    "If conflicting behaviors persist, split the claim into atomic subclaims before requesting another broad rerun."
                )
            if "mandatory_decision_checkpoint" in reasons:
                deadline = str(signals.get("decision_deadline_utc", "")).strip()
                outcomes = signals.get("decision_required_outcomes", [])
                outcomes_text = (
                    "|".join(str(x) for x in outcomes if str(x).strip())
                    if isinstance(outcomes, list)
                    else "retain_ree|hybridize|retire_ree_claim"
                )
                deadline_suffix = f" by `{deadline}`" if deadline else ""
                acceptance_checks.append(
                    "Package outputs as decision-grade comparison" + deadline_suffix
                    + f"; explicitly score outcomes `{outcomes_text}`."
                )

            required_pack_contract: dict[str, Any] = {
                "manifest": ["claim_ids_tested", "evidence_class", "evidence_direction"],
                "metrics": "stable numeric keys only",
                "summary": (
                    "include scenario, interpretation, and pairwise deltas "
                    "when dispatch_mode=discriminative_pair"
                ),
                "registered_thresholds": "required when dispatch_mode=discriminative_pair",
            }
            dispatch_override_applied = False
            proposal_patch: dict[str, Any] = {}
            raw_override = dispatch_overrides.get(claim_id.upper(), {})
            experimental_override: dict[str, Any] = {}
            if isinstance(raw_override, dict):
                nested_override = raw_override.get("experimental", {})
                if isinstance(nested_override, dict) and nested_override:
                    experimental_override = nested_override
                elif "experimental" not in raw_override:
                    experimental_override = raw_override
            if experimental_override:
                dispatch_override_applied = True

                override_target_repo = str(experimental_override.get("target_repo", "")).strip()
                if override_target_repo:
                    target_repo = override_target_repo

                override_exp_type = str(
                    experimental_override.get("suggested_experiment_type", "")
                ).strip()
                if override_exp_type:
                    exp_type = override_exp_type

                override_objective = str(experimental_override.get("objective", "")).strip()
                if override_objective:
                    objective = override_objective

                override_dispatch_mode = str(
                    experimental_override.get("dispatch_mode", "")
                ).strip()
                if override_dispatch_mode:
                    dispatch_mode = override_dispatch_mode

                override_seed_policy = str(experimental_override.get("seed_policy", "")).strip()
                if override_seed_policy:
                    seed_policy = override_seed_policy

                if "min_shared_seeds" in experimental_override:
                    try:
                        min_shared_seeds = max(
                            0, int(experimental_override.get("min_shared_seeds", min_shared_seeds))
                        )
                    except (TypeError, ValueError):
                        pass

                if "require_pre_registered_thresholds" in experimental_override:
                    require_pre_registered_thresholds = bool(
                        experimental_override.get("require_pre_registered_thresholds")
                    )

                if "exclude_broad_profile_sweeps" in experimental_override:
                    exclude_broad_profile_sweeps = bool(
                        experimental_override.get("exclude_broad_profile_sweeps")
                    )

                override_acceptance_checks = _normalize_text_list(
                    experimental_override.get("acceptance_checks")
                )
                if override_acceptance_checks:
                    acceptance_checks = override_acceptance_checks
                else:
                    prepend_checks = _normalize_text_list(
                        experimental_override.get("prepend_acceptance_checks")
                    )
                    append_checks = _normalize_text_list(
                        experimental_override.get("append_acceptance_checks")
                    )
                    acceptance_checks = prepend_checks + acceptance_checks + append_checks

                override_pack_contract = experimental_override.get("required_pack_contract")
                if isinstance(override_pack_contract, dict):
                    required_pack_contract.update(override_pack_contract)

                proposal_patch_candidate = experimental_override.get("proposal_patch", {})
                if isinstance(proposal_patch_candidate, dict):
                    proposal_patch = proposal_patch_candidate

            acceptance_checks = _dedupe_preserve_order(acceptance_checks)
            proposal_id = f"EXP-{_alloc_proposal_idx():04d}"
            proposal: dict[str, Any] = {
                "proposal_id": proposal_id,
                "backlog_id": item["backlog_id"],
                "claim_id": claim_id,
                "proposal_type": "experimental",
                "priority": item["priority"],
                "target_repo": target_repo,
                "objective": objective,
                "suggested_experiment_type": exp_type,
                "dispatch_mode": dispatch_mode,
                "seed_policy": seed_policy,
                "min_shared_seeds": min_shared_seeds,
                "require_pre_registered_thresholds": require_pre_registered_thresholds,
                "exclude_broad_profile_sweeps": exclude_broad_profile_sweeps,
                "decision_deadline_utc": str(signals.get("decision_deadline_utc", "")).strip(),
                "decision_required_outcomes": (
                    signals.get("decision_required_outcomes", [])
                    if isinstance(signals.get("decision_required_outcomes", []), list)
                    else []
                ),
                "why_now": reasons,
                "required_pack_contract": required_pack_contract,
                "acceptance_checks": acceptance_checks,
                "status": "proposed",
            }
            if dispatch_override_applied:
                proposal["dispatch_override_applied"] = True
            for key, value in proposal_patch.items():
                if str(key).strip():
                    proposal[str(key)] = value

            # Suppress blind re-issue of discriminative_pair auto-stubs when the
            # claim already has prior FAIL / non_contributory / weakens
            # discriminative_pair attempts on record. The next correct step is
            # /failure-autopsy on the latest failing run, not another pair under
            # the same substrate. Set status=suppressed_prior_attempts_failed so
            # downstream consumers (workset generator filters status=='proposed')
            # naturally skip them. The carry-forward block below preserves
            # status=executed from prior cycles, so a manually-closed proposal
            # still wins.
            if proposal.get("dispatch_mode") == "discriminative_pair":
                prior_fails = _prior_failed_discriminative_attempts(
                    claim_id, matrix.get("entries", [])
                )
                if prior_fails:
                    proposal["status"] = "suppressed_prior_attempts_failed"
                    proposal["prior_failed_run_ids"] = prior_fails
                    proposal["note"] = (
                        f"Suppressed: prior discriminative-pair attempts for "
                        f"{claim_id} on record with FAIL / non_contributory / "
                        f"weakens outcome: {prior_fails}. Route to "
                        f"/failure-autopsy on the latest run before re-issuing."
                    )

            proposals.append(proposal)

        if "literature" in needed:
            lit_type = _suggest_literature_type(claim_id, matrix)
            lit_objective = f"Improve literature grounding and confidence for {claim_id}."
            if "mandatory_decision_checkpoint" in reasons:
                lit_objective = (
                    f"Produce decision-grade literature triangulation for {claim_id}, including disconfirming evidence."
                )
            lit_acceptance_checks = [
                "At least 1 structured literature entry linked to claim_ids_tested.",
                f"Include at least {literature_min_disconfirming_entries} disconfirming/mixed source(s) alongside supporting sources.",
                "Confidence explicitly justified in confidence_rationale and confidence_components.",
                "Direction is supports/weakens/mixed/unknown and reflected in matrix.",
                "Preserve source wording, REE translation, and mapping caveat for each record.",
            ]
            if "mandatory_decision_checkpoint" in reasons:
                deadline = str(signals.get("decision_deadline_utc", "")).strip()
                deadline_suffix = f" by `{deadline}`" if deadline else ""
                lit_acceptance_checks.append(
                    "Complete adjudication-ready literature brief" + deadline_suffix + "."
                )
            proposal_id = f"LIT-{_alloc_proposal_idx():04d}"
            proposals.append(
                {
                    "proposal_id": proposal_id,
                    "backlog_id": item["backlog_id"],
                    "claim_id": claim_id,
                    "proposal_type": "literature_review",
                    "priority": item["priority"],
                    "target_repo": literature_owner,
                    "objective": lit_objective,
                    "suggested_literature_type": lit_type,
                    "disconfirming_evidence_required": literature_min_disconfirming_entries,
                    "mapping_quality_weighting_required": True,
                    "decision_deadline_utc": str(signals.get("decision_deadline_utc", "")).strip(),
                    "why_now": reasons,
                    "required_record_contract": {
                        "record": [
                            "claim_ids_tested",
                            "evidence_class",
                            "evidence_direction",
                            "confidence",
                            "confidence_rationale",
                            "mapping",
                            "confidence_components",
                        ],
                        "mapping_fields": [
                            "mapping.source_claim_statement",
                            "mapping.ree_translation",
                            "mapping.mapping_caveat",
                        ],
                        "confidence_component_fields": [
                            "confidence_components.source_quality",
                            "confidence_components.mapping_fidelity",
                            "confidence_components.transfer_risk",
                        ],
                        "summary": "include caveats, disconfirming evidence, and mapping limits",
                    },
                    "acceptance_checks": lit_acceptance_checks,
                    "status": "proposed",
                }
            )

    planning_root.mkdir(parents=True, exist_ok=True)

    backlog_doc = {
        "schema_version": "evidence_backlog/v1",
        "generated_at_utc": generated_at,
        "evidence_scope": applicability_scope_label,
        "source": {
            "claim_matrix": "evidence/experiments/claim_evidence.v1.json",
            "conflicts": "evidence/experiments/conflicts.md",
            "recommendations": "evidence/experiments/promotion_demotion_recommendations.md",
        },
        "criteria_version": str(planning_criteria.get("schema_version", "planning_criteria/v1")),
        "items": backlog_items,
    }
    # Merge in manually-curated proposals that survive pipeline regeneration.
    # Read evidence/planning/manual_proposals.v1.json if it exists; append its
    # items verbatim to the generated list. Manual items must carry:
    #   proposal_id, claim_id, proposal_type, priority, objective, status
    manual_proposals_path = planning_root / "manual_proposals.v1.json"
    if manual_proposals_path.exists():
        try:
            manual_doc = json.loads(manual_proposals_path.read_text(encoding="utf-8"))
            for mp in manual_doc.get("items", []):
                if isinstance(mp, dict) and mp.get("proposal_id"):
                    mp_copy = dict(mp)
                    mp_copy["source"] = "manual"
                    proposals.append(mp_copy)
        except Exception:
            pass  # malformed manual file -- skip silently

    # Carry forward non-proposed status from the existing proposals file.
    # Generated proposals always start as "proposed"; any manual status edits
    # (e.g. "executed") are wiped on regeneration unless we re-apply them here.
    # Key by backlog_id (stable across regenerations); fall back to proposal_id
    # for manual proposals that may not carry a backlog_id.
    _existing_status: dict[str, dict] = {}
    _existing_proposals_path = planning_root / "experiment_proposals.v1.json"
    if _existing_proposals_path.exists():
        try:
            _existing_doc = json.loads(
                _existing_proposals_path.read_text(encoding="utf-8")
            )
            for _ep in _existing_doc.get("items", []):
                _bid = _ep.get("backlog_id") or _ep.get("proposal_id")
                if _bid and _ep.get("status", "proposed") != "proposed":
                    _existing_status[_bid] = {
                        k: _ep[k]
                        for k in (
                            "status",
                            "executed_by",
                            "executed_queue_id",
                            "gated_at_utc",
                            "gated_by_session",
                            "gating_reason",
                            "predecessor_disposition",
                            "release_condition",
                            "superseded_by",
                        )
                        if k in _ep
                    }
        except Exception:
            pass  # malformed existing file -- skip silently

    for _p in proposals:
        _bid = _p.get("backlog_id") or _p.get("proposal_id")
        if _bid and _bid in _existing_status:
            _p.update(_existing_status[_bid])

    proposals_doc = {
        "schema_version": "experiment_proposals/v1",
        "generated_at_utc": generated_at,
        "source_backlog": "evidence/planning/evidence_backlog.v1.json",
        "manual_proposals_source": "evidence/planning/manual_proposals.v1.json",
        "items": proposals,
    }

    # Write a lightweight companion index for fast proposal surfacing.
    # Omits acceptance_checks and required_pack_contract (the bulk of token cost).
    # Claude reads this file to browse and select proposals; the full file is
    # accessed via bash only when implementing a specific chosen proposal.
    _INDEX_FIELDS = (
        "proposal_id", "backlog_id", "claim_id", "proposal_type",
        "status", "priority", "objective", "suggested_experiment_type",
        "why_now", "target_repo", "dispatch_mode",
        "executed_by", "executed_queue_id",
    )
    _index_items = [
        {k: p[k] for k in _INDEX_FIELDS if k in p}
        for p in proposals
    ]
    _index_doc: dict[str, Any] = {
        "schema_version": "experiment_proposals_index/v1",
        "generated_at_utc": generated_at,
        "note": (
            "Lightweight surfacing index -- no acceptance_checks or pack_contract. "
            "For full proposal detail use experiment_proposals.v1.json via bash."
        ),
        "n_proposed_exp": sum(
            1 for p in _index_items
            if p.get("proposal_type") == "experimental"
            and p.get("status") == "proposed"
        ),
        "n_proposed_lit": sum(
            1 for p in _index_items
            if p.get("proposal_type") != "experimental"
            and p.get("status") == "proposed"
        ),
        "n_executed": sum(1 for p in _index_items if p.get("status") == "executed"),
        "items": _index_items,
    }
    architecture_gap_doc = {
        "schema_version": "architecture_gap_register/v1",
        "generated_at_utc": generated_at,
        "evidence_scope": applicability_scope_label,
        "criteria_version": str(planning_criteria.get("schema_version", "planning_criteria/v1")),
        "source": {
            "claim_matrix": "evidence/experiments/claim_evidence.v1.json",
            "conflicts": "evidence/experiments/conflicts.md",
            "backlog": "evidence/planning/evidence_backlog.v1.json",
        },
        "thresholds": {
            "consider_new_structure_conflict_ratio": consider_conflict_ratio,
            "consider_new_structure_min_failure_signature_repeats": consider_min_sig_repeats,
            "consider_new_structure_min_distinct_signatures": consider_min_distinct_sigs,
            "consider_new_structure_min_literature_entries": consider_min_lit_entries,
            "consider_new_structure_literature_non_support_ratio": consider_lit_non_support_ratio,
            "external_precedence_conflict_ratio": external_precedence_conflict_ratio,
            "external_precedence_min_confidence_delta": external_precedence_min_conf_delta,
            "external_precedence_min_total_entries": external_precedence_min_total_entries,
            "external_precedence_min_experimental_entries": external_precedence_min_exp_entries,
            "external_precedence_min_literature_entries": external_precedence_min_lit_entries,
            "external_precedence_min_recurring_signatures": external_precedence_min_recurring,
            "proposal_saturation_conflict_ratio": saturation_conflict_ratio,
            "proposal_saturation_min_experimental_entries": saturation_min_exp_entries,
            "proposal_saturation_recent_window": saturation_recent_window,
            "proposal_saturation_min_recent_entries": saturation_min_recent_entries,
            "proposal_saturation_max_unique_signature_sets": saturation_max_signature_sets,
            "proposal_saturation_max_directions": saturation_max_directions,
            "escalation_min_conflict_ratio": escalation_min_conflict_ratio,
            "escalation_min_experimental_entries": escalation_min_exp_entries,
            "escalation_min_recurring_signatures": escalation_min_recurring,
            "escalation_min_max_signature_count": escalation_min_signature_count,
            "mandatory_decision_conflict_ratio": mandatory_decision_conflict_ratio,
            "mandatory_decision_min_fresh_batches": mandatory_decision_min_fresh_batches,
            "mandatory_decision_recent_window": mandatory_decision_recent_window,
            "mandatory_decision_deadline_hours": mandatory_decision_deadline_hours,
            "atomic_split_conflict_ratio": atomic_split_conflict_ratio,
            "atomic_split_min_mixed_entries": atomic_split_min_mixed_entries,
            "atomic_split_min_recurring_signatures": atomic_split_min_recurring_signatures,
            "discriminative_pair_conflict_ratio": discriminative_pair_conflict_ratio,
            "discriminative_pair_min_shared_seeds": discriminative_pair_min_shared_seeds,
            "literature_min_disconfirming_entries": literature_min_disconfirming_entries,
        },
        "model_adjudication": {
            "external_precedence_enabled": external_precedence_enabled,
            "allowed_conflict_outcomes": allowed_conflict_outcomes,
            "default_conflict_outcome": default_conflict_outcome,
            "cascade_policy": {
                "enabled": cascade_enabled,
                "trigger_outcomes": cascade_trigger_outcomes,
                "dependency_reopen_status": dependency_reopen_status,
                "require_followup_proposals": cascade_followup_required,
            },
            "temporary_override_mode": {
                "enabled": override_mode_enabled,
                "mode_id": override_mode_id,
                "requirements": override_requirements,
            },
            "anti_lock_in_gate_enabled": anti_lock_in_enabled,
        },
        "items": architecture_items,
    }

    (planning_root / "evidence_backlog.v1.json").write_text(
        json.dumps(backlog_doc, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (planning_root / "experiment_proposals.v1.json").write_text(
        json.dumps(proposals_doc, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (planning_root / "experiment_proposals_index.v1.json").write_text(
        json.dumps(_index_doc, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (planning_root / "architecture_gap_register.v1.json").write_text(
        json.dumps(architecture_gap_doc, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    arch_lines: list[str] = []
    arch_lines.append("# Architecture Gap Register")
    arch_lines.append("")
    arch_lines.append(f"Generated: `{generated_at}`")
    arch_lines.append(f"Evidence scope: `{applicability_scope_label}`")
    arch_lines.append("")
    arch_lines.append(
        "This register highlights claims under structural pressure and flags where the evidence pattern "
        "suggests a **consider new structure** decision."
    )
    arch_lines.append("")
    arch_lines.append(
        "| gap_id | claim_id | status | conflict_ratio | lit_non_support_ratio | confidence_delta_lit_minus_exp | recurring_signatures | consider_new_structure | external_precedence_candidate | recommendation |"
    )
    arch_lines.append("|---|---|---|---|---|---|---|---|---|---|")
    if not architecture_items:
        arch_lines.append("| _none_ | - | - | - | - | - | - | - | - | - |")
    else:
        for item in architecture_items:
            confidence_split = item.get("confidence_split", {})
            arch_lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{item['gap_id']}`",
                        f"`{item['claim_id']}`",
                        f"`{item['current_status']}`",
                        _fmt_number(float(item.get("conflict_ratio", 0.0))),
                        _fmt_number(float(item.get("literature_non_support_ratio", 0.0))),
                        _fmt_number(float(confidence_split.get("delta_lit_minus_exp", 0.0))),
                        str(len(item.get("recurring_failure_signatures", []))),
                        "yes" if bool(item.get("consider_new_structure", False)) else "no",
                        "yes" if bool(item.get("external_precedence_candidate", False)) else "no",
                        f"`{item['recommendation']}`",
                    ]
                )
                + " |"
            )

    consider_items = [item for item in architecture_items if item.get("consider_new_structure")]
    arch_lines.append("")
    arch_lines.append("## Consider New Structure Queue")
    arch_lines.append("")
    if not consider_items:
        arch_lines.append("No claims currently trigger a consider-new-structure recommendation.")
    else:
        for item in consider_items:
            trigger_signals = ", ".join(item.get("trigger_signals", []))
            arch_lines.append(
                f"- `{item['claim_id']}` triggers={trigger_signals}; "
                + f"conflict_ratio={_fmt_number(float(item.get('conflict_ratio', 0.0)))}; "
                + f"lit_non_support_ratio={_fmt_number(float(item.get('literature_non_support_ratio', 0.0)))}."
            )
            rec_sigs = item.get("recurring_failure_signatures", [])
            if rec_sigs:
                formatted = ", ".join(
                    f"`{sig.get('signature', '')}`({int(sig.get('count', 0))})"
                    for sig in rec_sigs
                )
                arch_lines.append(f"  - recurring_signatures: {formatted}")
            stage = item.get("evidence_stage", {})
            if isinstance(stage, dict) and stage:
                resolved_stage = str(stage.get("resolved_stage", "")).strip()
                stage_order = [
                    str(token).strip()
                    for token in stage.get("stage_order", [])
                    if str(token).strip()
                ]
                if resolved_stage:
                    arch_lines.append(
                        "  - evidence_stage: "
                        + f"`{resolved_stage}`"
                        + (f"; stage_order={','.join(stage_order)}" if stage_order else "")
                    )
                if bool(stage.get("proxy_noise_expected", False)):
                    arch_lines.append(
                        "  - interpretation_guard: proxy-stage evidence is expected noisy; avoid final ethics adjudication from proxy-only signals."
                    )
                proxy_note = str(stage.get("proxy_interpretation", "")).strip()
                if proxy_note:
                    arch_lines.append(f"  - proxy_note: {proxy_note}")
                final_note = str(stage.get("final_test_basis", "")).strip()
                if final_note:
                    arch_lines.append(f"  - final_test_basis: {final_note}")
            if bool(item.get("external_precedence_candidate", False)):
                confidence_split = item.get("confidence_split", {})
                arch_lines.append(
                    "  - external_precedence_candidate: yes; "
                    + f"delta_lit_minus_exp={_fmt_number(float(confidence_split.get('delta_lit_minus_exp', 0.0)))}"
                )
            if bool(item.get("saturation_guard_engaged", False)):
                sat = item.get("saturation_signal_details", {})
                arch_lines.append(
                    "  - saturation_guard: engaged; "
                    + f"recent_window_used={_fmt_number(float(sat.get('recent_window_used', 0)))}, "
                    + f"unique_signature_sets={_fmt_number(float(sat.get('unique_signature_sets', 0)))}, "
                    + f"unique_directions={_fmt_number(float(sat.get('unique_directions', 0)))}"
                )
            if bool(item.get("escalate_architecture_decision", False)):
                arch_lines.append(
                    "  - escalation_required: yes; route directly to architecture decision checkpoint."
                )
            if bool(item.get("mandatory_decision_checkpoint", False)):
                arch_lines.append(
                    "  - mandatory_decision_checkpoint: yes; "
                    + f"deadline={item.get('decision_deadline_utc', '') or 'n/a'}; "
                    + "required_outcomes="
                    + "|".join(
                        str(x)
                        for x in item.get("decision_required_outcomes", [])
                        if str(x).strip()
                    )
                )
            if bool(item.get("atomic_split_recommended", False)):
                arch_lines.append(
                    "  - atomic_split_recommended: yes; split into narrower subclaims before broad reruns."
                )

    (planning_root / "ARCHITECTURE_GAP_REGISTER.md").write_text(
        "\n".join(arch_lines).rstrip() + "\n",
        encoding="utf-8",
    )

    index_lines: list[str] = []
    index_lines.append("# Planning Index")
    index_lines.append("")
    index_lines.append(f"Generated: `{generated_at}`")
    index_lines.append("")
    index_lines.append(
        f"- Evidence backlog: `evidence_backlog.v1.json` ({len(backlog_items)} item(s))"
    )
    index_lines.append(
        f"- Experiment proposals: `experiment_proposals.v1.json` ({len(proposals)} item(s))"
    )
    index_lines.append(
        "- Architecture gap register: "
        + f"`architecture_gap_register.v1.json` ({len(architecture_items)} item(s), "
        + f"consider_new_structure={len(consider_items)})"
    )
    index_lines.append("- Planning criteria: `planning_criteria.v1.yaml`")
    (planning_root / "INDEX.md").write_text(
        "\n".join(index_lines).rstrip() + "\n",
        encoding="utf-8",
    )

    return backlog_items, proposals, architecture_items


# ---------------------------------------------------------------------------
# Arm-reuse fingerprint index (plan section 9.1)
# ---------------------------------------------------------------------------
#
# Materialises evidence/experiments/arm_fingerprint_index.json so the Phase 1
# arm-reuse consumer (ree-v3/experiments/_lib/arm_reuse.py) can look up a minted
# OFF/baseline cell by its content-addressed arm_fingerprint. Refreshed on every
# governance run (governance.sh -> build_experiment_indexes.py).
#
# Governance invariants (plan section 9.3):
#   - Only cells with reuse_eligible: true and a non-ERROR, non-superseded parent
#     are indexed as reusable SOURCES. Same-fingerprint runs collapse to one entry
#     (they are by construction the same random variable); prefer the newest
#     non-superseded run.
#   - A REUSED cell (one carrying reused_from_run_id) is a POINTER, not new
#     independent evidence: it is NOT re-indexed as a source (no double-count).
#   - reverse_index maps source_run_id -> [consumer run_ids]; if a source is later
#     superseded / ERROR / missing, every downstream consumer is flagged
#     pending_reuse_revalidation (analogous to pending_substrate_reconfirmation).
# This index NEVER feeds confidence/conflict scoring; it only enables reuse.

_ARM_FP_INDEX_SCHEMA = "arm_fp_index/v1"


def _arm_fp_manifest_timestamp(manifest: dict[str, Any], path: Path) -> str:
    """A sortable timestamp string for collapse-prefer-newest. Best-effort."""
    for key in ("timestamp_utc", "completed_at", "generated_at", "created_utc"):
        val = manifest.get(key)
        if isinstance(val, str) and val:
            return val
    # Fall back to a stamp embedded in the run_id (compact or epoch form). NO
    # mtime fallback -- mtime is unstable across regenerations and checkouts,
    # so it made this collapse-prefer-newest pick flip between rebuilds. An
    # empty string sorts first, i.e. an unknown-time run never displaces a
    # dated one; ties resolve on the sorted manifest iteration order.
    rid = str(manifest.get("run_id", path.stem))
    derived = _timestamp_from_identifier(rid)
    return derived[0] if derived is not None else ""


def _arm_fp_cell_keys(cell: dict[str, Any]) -> list[str]:
    """Metric keys recorded for the cell = every key except the fingerprint sub-dict.

    A key is in cell_keys iff its value is actually present in the recorded cell --
    so the consumer's set(needed_keys) subset of set(cell_keys) check refuses
    whenever the mint did not record a metric the new iteration reads (the
    section-9.2 correctness trap). Conservative: never invent keys.
    """
    return sorted(k for k in cell.keys() if k != "arm_fingerprint")


def _iter_manifests_with_arm_results(base_dir: Path):
    """Yield (manifest_dict, path) for flat + run-pack manifests that have arm_results."""
    seen: set[Path] = set()
    flat = sorted(base_dir.glob("*.json"))
    nested = sorted(base_dir.glob("**/runs/**/manifest.json"))
    for path in flat + nested:
        rp = path.resolve()
        if rp in seen:
            continue
        seen.add(rp)
        manifest = _load_json(path)
        if not isinstance(manifest, dict):
            continue
        if isinstance(manifest.get("arm_results"), list):
            yield manifest, path


def _write_arm_fingerprint_index(base_dir: Path, generated_at: str) -> dict[str, Any]:
    """Build and write arm_fingerprint_index.json. Returns the index dict."""
    repo_root = base_dir.parent.parent  # REE_assembly root

    by_fingerprint: dict[str, dict[str, Any]] = {}
    # (fingerprint -> (timestamp, superseded) of the chosen entry) for collapse.
    _chosen_meta: dict[str, tuple[str, bool]] = {}
    reverse_index: dict[str, list[str]] = {}
    # source_run_id -> superseded/ERROR/missing status, for pending flagging.
    source_status: dict[str, dict[str, Any]] = {}
    consumer_records: list[dict[str, Any]] = []

    n_source_cells = 0
    n_reused_cells = 0

    for manifest, path in _iter_manifests_with_arm_results(base_dir):
        run_id = str(manifest.get("run_id", path.stem))
        experiment_type = str(manifest.get("experiment_type", path.parent.name))
        outcome = str(manifest.get("status") or manifest.get("outcome", "UNKNOWN")).upper()
        superseded = _normalize_direction(manifest.get("evidence_direction")) == "superseded"
        ts = _arm_fp_manifest_timestamp(manifest, path)
        try:
            manifest_rel = str(path.resolve().relative_to(repo_root.resolve()))
        except ValueError:
            manifest_rel = str(path)

        # Record this run's status as a potential reuse SOURCE (for consumer
        # revalidation), regardless of whether it is currently indexable.
        source_status[run_id] = {
            "superseded": superseded,
            "outcome": outcome,
            "present": True,
        }

        for cell in manifest["arm_results"]:
            if not isinstance(cell, dict):
                continue
            fp_obj = cell.get("arm_fingerprint")

            # A reused cell is a POINTER, not a fresh source -> reverse-index only.
            src = cell.get("reused_from_run_id")
            if src:
                n_reused_cells += 1
                src = str(src)
                reverse_index.setdefault(src, [])
                if run_id not in reverse_index[src]:
                    reverse_index[src].append(run_id)
                consumer_records.append({
                    "consumer_run_id": run_id,
                    "source_run_id": src,
                    "reused_fingerprint": cell.get("reused_fingerprint"),
                })
                continue  # never index a reused cell as a source (no double-count)

            if not isinstance(fp_obj, dict):
                continue
            fingerprint = fp_obj.get("arm_fingerprint")
            if not isinstance(fingerprint, str) or not fingerprint:
                continue
            # Index only reuse_eligible + non-ERROR + non-superseded cells.
            if not bool(fp_obj.get("reuse_eligible", False)):
                continue
            if outcome == "ERROR":
                continue
            if superseded:
                continue
            if str(fp_obj.get("schema")) != "arm_fp/v1":
                continue

            n_source_cells += 1
            candidate = {
                "run_id": run_id,
                "manifest_path": manifest_rel,
                "experiment_type": experiment_type,
                "machine_class": fp_obj.get("machine_class"),
                "regime": fp_obj.get("regime"),
                "reuse_eligible": True,
                "outcome": outcome,
                "cell_keys": _arm_fp_cell_keys(cell),
                "superseded": False,
                "fingerprint_schema": fp_obj.get("schema"),
                "seed": fp_obj.get("seed", cell.get("seed")),
                # Audit: whether the mint narrowed its substrate hash to a declared
                # dependency scope (plan sec 11). None/absent -> whole-tree (default).
                "substrate_scope_declared": bool(fp_obj.get("substrate_scope_declared", False)),
                # Triage: the torch build the cell ran under (plan sec 12, 2026-07-19).
                # Also inside machine_class (which is what the hash keys on) -- surfaced
                # separately so a MISS can be read as "torch moved" at the lookup site.
                # None on every pre-2026-07-19 entry: that corpus recorded no torch at
                # all, which is exactly why the sec-12 cut could not be migrated.
                "torch_version": fp_obj.get("torch_version"),
            }
            # Collapse same-fingerprint runs: prefer the newest (all non-superseded
            # here by construction; tie-break on timestamp string).
            prev = _chosen_meta.get(fingerprint)
            if prev is None or ts >= prev[0]:
                by_fingerprint[fingerprint] = candidate
                _chosen_meta[fingerprint] = (ts, False)

    # Flag consumers whose cited source is now superseded / ERROR / missing.
    pending: list[dict[str, Any]] = []
    for rec in consumer_records:
        src = rec["source_run_id"]
        st = source_status.get(src)
        if st is None:
            pending.append({**rec, "reason": "source_run_missing"})
        elif st["superseded"]:
            pending.append({**rec, "reason": "source_superseded"})
        elif st["outcome"] == "ERROR":
            pending.append({**rec, "reason": "source_outcome_error"})

    index = {
        "schema": _ARM_FP_INDEX_SCHEMA,
        "regime": "A",
        "generated_at": generated_at,
        "fingerprint_schema": "arm_fp/v1",
        "n_source_cells": n_source_cells,
        "n_reused_cells": n_reused_cells,
        "n_fingerprints": len(by_fingerprint),
        "by_fingerprint": dict(sorted(by_fingerprint.items())),
        "reverse_index": {k: sorted(v) for k, v in sorted(reverse_index.items())},
        "pending_reuse_revalidation": pending,
    }
    (base_dir / "arm_fingerprint_index.json").write_text(
        json.dumps(index, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return index


# ---------------------------------------------------------------------------
# HEAD/worktree skew guard (2026-07-18, SD-068 / V3-EXQ-778b+778c incident)
#
# `git reset --mixed <remote-ref>` -- the DEFAULT reset, and the usual "adopt
# origin without disturbing my working tree" idiom after a rejected push --
# moves HEAD and the index forward but deliberately does NOT touch the working
# tree. Files ADDED by an adopted commit therefore exist in HEAD and the index
# but are never written to disk. `git status` reports them as " D" (unstaged
# deletion), which reads like a deletion but is the opposite: they were never
# materialised.
#
# This script reads the WORKING TREE. Without this guard it rebuilds happily
# with those runs simply absent -- no error, no warning -- and every derived
# artifact (claim_evidence.v1.json, INDEX.md, pending_review.md, the
# dashboards) silently drops real experimental evidence for every claim those
# runs tagged. Committing that regen is a silent evidence-loss event.
#
# Confirmed incident: 8 files (2 flat manifests + their runs/<run_id>/ packs)
# unmaterialised after two resets adopting 0876de9386 and 4d4816bbe3. The
# rebuild reported 1517 runs instead of 1519 and would have dropped both runs'
# evidence for INV-047 / MECH-168 / MECH-169 / SD-068.
#
# The check lives HERE, inside the script, rather than in a PreToolUse hook or
# a governance.sh wrapper, deliberately. The existing hook guards are all
# `[ -f ]`/`[ -x ]`-gated and therefore fail OPEN and silent when their path
# does not resolve (on 2026-07-18 all 66 worktrees were found in exactly that
# state). A guard that fails open is worse than none. Its failure mode is
# REFUSE TO WRITE, never warn-and-continue: a partial or silently-smaller index
# is worse than no rebuild at all.
#
# Background: CLAUDE.md, "HEAD/worktree skew after `git reset <remote-ref>`".
# ---------------------------------------------------------------------------

SKEW_GUARD_EXIT_CODE = 3


def _is_indexer_read_path(rel_path: str) -> bool:
    """True when a path (relative to evidence/experiments) is one this script reads.

    Two shapes carry run evidence:
      <run_id>.json                                -- flat manifest
      <experiment_type>/runs/<run_id>/<any file>   -- per-run pack
    """
    parts = rel_path.split("/")
    if len(parts) == 1:
        return rel_path.endswith(".json")
    return "runs" in parts[:-1]


def _git_tracked_paths(base_dir: Path) -> list[str] | None:
    """Paths git tracks under base_dir, relative to base_dir.

    Returns None when base_dir is not inside a git checkout or git is
    unavailable -- the skew this guards against cannot occur there, so the
    guard is genuinely not applicable rather than being skipped.
    """
    try:
        proc = subprocess.run(
            ["git", "-C", str(base_dir), "ls-files", "-z", "--", "."],
            capture_output=True,
            check=False,
        )
    except (OSError, ValueError):
        return None
    if proc.returncode != 0:
        return None
    decoded = proc.stdout.decode("utf-8", errors="replace")
    return [p for p in decoded.split("\0") if p]


def _find_unmaterialised_evidence(base_dir: Path) -> list[str]:
    """Evidence files git tracks but which are absent from the working tree."""
    tracked = _git_tracked_paths(base_dir)
    if tracked is None:
        return []
    return sorted(
        rel for rel in tracked
        if _is_indexer_read_path(rel) and not (base_dir / rel).exists()
    )


def _guard_worktree_materialised(base_dir: Path, allow_missing: bool) -> None:
    """Refuse to rebuild when tracked evidence is missing from the working tree.

    Exits non-zero WITHOUT writing anything unless allow_missing is set.
    """
    missing = _find_unmaterialised_evidence(base_dir)
    if not missing:
        return

    stream = sys.stderr
    print("", file=stream)
    print("=" * 72, file=stream)
    print(
        f"[skew-guard] {len(missing)} evidence file(s) are tracked by git but "
        "ABSENT from the working tree.",
        file=stream,
    )
    print("=" * 72, file=stream)
    shown = missing[:40]
    for rel in shown:
        print(f"  {rel}", file=stream)
    if len(missing) > len(shown):
        print(f"  ... and {len(missing) - len(shown)} more", file=stream)
    print("", file=stream)
    print(
        "This is the HEAD/worktree skew signature: a `git reset <remote-ref>` "
        "moved HEAD\nand the index forward without writing newly-added upstream "
        "files to disk. The\nfiles were never materialised -- nothing was deleted.",
        file=stream,
    )
    print("", file=stream)
    print("REMEDY (safe and non-destructive for these paths):", file=stream)
    print("    git -C <REE_assembly> checkout -- .", file=stream)
    print("then re-run this script.", file=stream)
    print("", file=stream)

    if allow_missing:
        print(
            "[skew-guard] --allow-missing-runs was passed: PROCEEDING ANYWAY. "
            "The derived\nartifacts below will be built WITHOUT the evidence "
            "from the files listed above.",
            file=stream,
        )
        print("", file=stream)
        return

    print(
        "REFUSING to write derived artifacts. A silently-smaller index would "
        "drop real\nevidence for every claim those runs tagged, and committing "
        "it is an evidence-loss\nevent. Pass --allow-missing-runs only if the "
        "absence is deliberate.",
        file=stream,
    )
    print("", file=stream)
    sys.exit(SKEW_GUARD_EXIT_CODE)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build experiment evidence indexes.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Path to evidence/experiments",
    )
    parser.add_argument(
        "--lookback-failures",
        type=int,
        default=3,
        help="How many most recent FAIL runs to include in design implications.",
    )
    parser.add_argument(
        "--index-only",
        action="store_true",
        default=False,
        help=(
            "Stop after writing claim_evidence.v1.json and INDEX.md. "
            "Skips backlog regeneration, proposals, architecture gap register, "
            "and promotion/demotion recommendations. "
            "Safe to run immediately after ingesting new experiment results "
            "without clobbering manually-maintained planning artefacts."
        ),
    )
    parser.add_argument(
        "--allow-missing-runs",
        action="store_true",
        default=False,
        help=(
            "Override the HEAD/worktree skew guard and rebuild even when git-tracked "
            "evidence files are absent from the working tree. Use ONLY when the "
            "absence is deliberate -- the derived artifacts will silently omit those "
            "runs' evidence."
        ),
    )
    args = parser.parse_args()

    base_dir = args.root.resolve()

    # Refuse to rebuild off a working tree that is missing tracked evidence.
    # Runs before every read and every write, so a trip leaves all derived
    # artifacts exactly as they were.
    _guard_worktree_materialised(base_dir, args.allow_missing_runs)

    repo_root = base_dir.parent.parent
    evidence_root = base_dir.parent
    literature_root = evidence_root / "literature"
    decisions_dir = evidence_root / "decisions"
    decision_log_path = decisions_dir / "decision_log.v1.jsonl"
    planning_root = evidence_root / "planning"

    stop_criteria = _load_json_compatible_yaml(base_dir / "stop_criteria.v1.yaml", "stop criteria")
    decision_criteria = _load_decision_criteria(base_dir / "decision_criteria.v1.yaml")
    planning_criteria = _load_planning_criteria(planning_root / "planning_criteria.v1.yaml")
    claim_registry = _load_claim_registry(repo_root / "docs/claims/claims.yaml")
    scoring_exclusions = _load_scoring_exclusions(repo_root / "docs/claims/scoring_exclusions.json")
    decision_log_entries = _load_decision_log(decision_log_path)
    latest_decisions = _latest_decision_by_claim(decision_log_entries)
    latest_decisions_by_needed = _latest_decision_by_claim_and_needed(decision_log_entries)
    adjudication_cfg = planning_criteria.get("model_adjudication", {})
    allowed_conflict_outcomes = {
        str(token).strip()
        for token in adjudication_cfg.get("allowed_conflict_outcomes", [])
        if str(token).strip()
    }
    if not allowed_conflict_outcomes:
        allowed_conflict_outcomes = {
            "retain_ree",
            "hybridize",
            "retire_ree_claim",
        }
    latest_adjudication_decisions = _latest_adjudication_decision_by_claim(
        decision_log_entries,
        allowed_conflict_outcomes,
    )

    by_experiment = _scan_runs(base_dir, planning_criteria)
    dedup_warnings = _detect_and_mark_duplicate_emissions(by_experiment)
    if dedup_warnings:
        print(
            f"[dedup-guard] auto-marked {len(dedup_warnings)} duplicate emission(s) as "
            "superseded (in-memory only; on-disk manifests unchanged):",
            file=sys.stderr,
        )
        for w in dedup_warnings:
            print(
                f"  {w['experiment_type']}: {w['duplicate_run_id']} "
                f"(sig={w['signature_sha1']}, +{w['span_minutes']:.1f}min vs canonical "
                f"{w['canonical_run_id']})",
                file=sys.stderr,
            )
    by_literature = _scan_literature(literature_root, planning_criteria)

    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    todos_by_experiment: dict[str, list[str]] = {}

    for experiment_type, runs in by_experiment.items():
        criteria = _criteria_for_experiment(stop_criteria, experiment_type)
        _evaluate_runs(runs, criteria)

        key_metrics = _select_key_metrics(runs, criteria)
        experiment_dir = base_dir / experiment_type
        profile_path = _ensure_experiment_template(experiment_dir, experiment_type)

        design_text, todos = _build_design_implications(runs, args.lookback_failures)
        profile_text = profile_path.read_text(encoding="utf-8")
        profile_text = _replace_between_markers(profile_text, design_text)
        profile_path.write_text(profile_text, encoding="utf-8")

        if todos:
            todos_by_experiment[experiment_type] = todos

        _write_experiment_index(experiment_dir, experiment_type, runs, key_metrics, generated_at)

    _write_todos(base_dir, todos_by_experiment, generated_at)
    _write_literature_index(literature_root, by_literature, generated_at)
    _write_decision_state(decisions_dir, latest_decisions, generated_at)

    matrix = _write_claim_evidence_matrix(
        base_dir, by_experiment, by_literature, generated_at,
        planning_criteria=planning_criteria,
        scoring_exclusions=scoring_exclusions,
    )

    # Arm-reuse fingerprint index (plan section 9.1). Independent of claim scoring;
    # always refreshed (including --index-only) so the Phase 1 consumer's lookup
    # table stays current after every governance run.
    arm_fp_index = _write_arm_fingerprint_index(base_dir, generated_at)
    if arm_fp_index["n_reused_cells"] or arm_fp_index["pending_reuse_revalidation"]:
        print(
            "[arm-reuse] fingerprints=%d source_cells=%d reused_cells=%d pending_revalidation=%d"
            % (
                arm_fp_index["n_fingerprints"],
                arm_fp_index["n_source_cells"],
                arm_fp_index["n_reused_cells"],
                len(arm_fp_index["pending_reuse_revalidation"]),
            )
        )

    if args.index_only:
        total_runs = sum(len(runs) for runs in by_experiment.values())
        total_fail = sum(1 for runs in by_experiment.values() for r in runs if r.final_status == "FAIL")
        total_lit = sum(len(entries) for entries in by_literature.values())
        print(
            "[--index-only] Stopped after claim_evidence matrix and INDEX.md. "
            + f"Indexed {total_runs} run(s) across {len(by_experiment)} experiment type(s); "
            + f"FAIL={total_fail}; literature entries={total_lit}. "
            + "Planning artefacts (backlog, proposals, recommendations) NOT regenerated."
        )
        return

    conflicts, conflict_scope = _collect_conflicts(matrix, planning_criteria, claim_registry)
    backlog_items, proposals, architecture_items = _write_planning_outputs(
        planning_root,
        matrix,
        claim_registry,
        conflicts,
        latest_decisions,
        latest_adjudication_decisions,
        planning_criteria,
        generated_at,
    )
    _write_conflicts_report(base_dir, matrix, planning_criteria, conflicts, conflict_scope, generated_at)
    _write_promotion_demotion_recommendations(
        base_dir,
        matrix,
        claim_registry,
        decision_criteria,
        latest_decisions,
        latest_decisions_by_needed,
        generated_at,
        planning_criteria,
    )
    _write_top_level_index(
        base_dir,
        by_experiment,
        by_literature,
        decision_log_count=len(decision_log_entries),
        backlog_count=len(backlog_items),
        proposal_count=len(proposals),
        architecture_gap_count=len(architecture_items),
        generated_at=generated_at,
    )

    total_runs = sum(len(runs) for runs in by_experiment.values())
    total_fail = sum(1 for runs in by_experiment.values() for r in runs if r.final_status == "FAIL")
    total_lit = sum(len(entries) for entries in by_literature.values())
    print(
        "Indexed "
        + f"{total_runs} run(s) across {len(by_experiment)} experiment type(s); "
        + f"FAIL={total_fail}; literature entries={total_lit}; "
        + f"backlog items={len(backlog_items)}; proposals={len(proposals)}."
    )


if __name__ == "__main__":
    main()
