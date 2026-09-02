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
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Optional

def _indexer_version() -> str:
    """Short content hash of THIS script, recorded in the derived read-model.

    A hand-maintained version string is the thing nobody remembers to bump, so a
    consumer could not tell whether a DB was built by the indexer it expects. A
    content hash cannot go stale by omission. Falls back to "unknown" rather than
    raising -- this is metadata, never a gate.
    """
    try:
        import hashlib
        return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:12]
    except Exception:
        return "unknown"


INDEXER_VERSION = _indexer_version()


def _atomic_write_text(path: Path, text: str) -> None:
    """Replace `path` with `text` in one indivisible step (temp + os.replace).

    WHY THIS EXISTS, and why it is NOT ceremony. `Path.write_text()` is
    `open(path, "w").write(text)`: it TRUNCATES at open() and then writes the
    payload in several write() syscalls once it is past the ~8 KiB stdio
    buffer. This regen rewrites ~10 artifacts under evidence/planning/ and
    evidence/experiments/ -- several of them well past that buffer
    (experiment_proposals.v1.json is ~868 KB) -- and it does NOT run alone:

      * experiment_proposals.v1.json is also written by the umbrella's
        confirmer_verdict.py (on the hot path of the concurrent headless-chip
        population, behind chip_ledger.py's confirmer gate) and by
        igw_routine_tick.py's retire path (unattended, on a timer). governance.sh
        holds only a DIRECTORY-SCOPE claim over evidence/, which is advisory
        (a NOTE that fails open), not a hard mutex -- so a confirmer chip
        resolving mid-regen is a concrete two-writer collision.
      * two regens can themselves overlap: serve.py's `build_indexes` action,
        governance.sh, proposal_routine_tick.py and ree_metaworker_heartbeat.py
        can each launch this script.

    A single non-atomic writer already tears every CONCURRENT READ during its
    multi-syscall write (measured elsewhere: 1612/2212 reads unparseable); two
    non-atomic writers of differing length additionally leave a CORRUPT FINAL
    file (a valid prefix followed by the longer writer's tail). os.replace() is
    atomic on POSIX and, because the temp file is created in the SAME directory,
    a same-filesystem rename -- so every reader sees one writer's whole document
    or another's, never a splice, and a loser of the rename race is discarded
    whole.

    This is the same primitive as the umbrella's
    scripts/task_claim.atomic_write_text(); it is re-stated here rather than
    imported because build_experiment_indexes.py lives in REE_assembly, a
    separate repo, and CLAUDE.md explicitly rejects a cross-repo sys.path import
    for shared code (it works on the Mac and silently falls back on the hub and
    cloud workers). A ~15-line textbook idiom did not warrant the vendored-copy
    machinery (a new module + audit_vendored_copies.py registration + an ongoing
    byte-identity obligation) that a genuinely non-trivial shared module like
    graceful_timeout.py needs. The drift guard is
    test_build_experiment_indexes.py::test_regen_writes_shared_artifacts_atomically,
    which fails if any bare .write_text()/open(..,"w") to these paths returns.
    """
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".tmp.")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, path)
    except BaseException:
        # Never leave a half-written .tmp.* beside the real file -- another
        # session's `git status` reads it as untracked junk in a shared checkout.
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def _relpath_or_fallback(path: Path, base: Path) -> str:
    """Like `Path.relative_to(base).as_posix()`, but falls back to
    `os.path.relpath` (which permits ".." segments) when `path` is not nested
    under `base`. A pack's manifest/metrics/summary files always live under
    their own experiment_dir, so `.relative_to()` alone was sufficient before
    flat-only-orphan discovery (2026-09-01): that path's manifest can live at
    the TOP level of evidence/experiments/ while `experiment_dir` is the
    `<base>/<experiment_type>/` subdirectory the index is being written into,
    which `.relative_to()` rejects outright rather than link incorrectly.
    """
    try:
        return path.relative_to(base).as_posix()
    except ValueError:
        return os.path.relpath(path, base)


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
    # queue_id (2026-08-19, run_id identifier hygiene): "" for legacy manifests
    # that predate the field. Exists so _detect_and_mark_duplicate_emissions can
    # tell "the same queue item re-emitted" from "two different queue items whose
    # run_id happens to collapse to the same experiment_type stem" -- see that
    # function's docstring. Not otherwise scored or surfaced.
    queue_id: str = ""
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
    # substrate_commit / enabled_default_off_flags -- the two PROSPECTIVE provenance
    # fields substrate_stability_and_drift_detection_plan.md's drift detector needs
    # (nodes `substrate-commit-coverage` and `P1c-prospective-recording`). Surfaced
    # for queryability, NEVER scored: their whole purpose is letting a later reader
    # reconstruct WHICH substrate was tested, and letting a governance session
    # measure adoption coverage with a GROUP BY instead of a corpus re-scan.
    # substrate_commit is the bare sha (the manifest field is a dict; the dict's
    # `dirty` / `dirty_paths` stay in the manifest, which is authoritative).
    # enabled_default_off_flags is None when the run never measured it, and a
    # (possibly empty) dict when it did -- the distinction manifest_core.py's own
    # docstring insists on, and collapsing it here would destroy it in the read
    # model exactly as an earlier draft of the producer destroyed it at the source.
    substrate_commit: str = ""
    enabled_default_off_flags: dict[str, Any] | None = None
    label_balance: dict[str, Any] = field(default_factory=dict)
    # Recording-provenance surfacing (2026-07-16): the machine + machine_class the
    # run executed on. machine_class is the cloud-authoritative gate class (SD-024)
    # and the arm-reuse fingerprint key. Read from the pack after the unconditional
    # flat-provenance backfill (_merge_flat_manifest_overrides), so a thin
    # pre-2026-07-16 pack still surfaces the flat sibling's value. Surfaced for
    # queryability, NOT scored.
    machine: str = ""
    machine_class: str = ""
    # canonical-profile provenance (2026-08-12): which curated organism bundle
    # (if any) built this run's config -- ree-v3 ree_core/utils/canonical_profile.py
    # (CanonicalProfileSpec) + experiments/_lib/canonical_profile_fingerprint.py
    # (freeze+persist). canonical_profile is the "<name>@<version>" qualified
    # name; canonical_profile_hash is the frozen artifact's content hash.
    # Caller-supplied only -- absent on every run that does not construct its
    # config from a profile, which as of introduction is the entire corpus.
    # Surfaced for queryability AND consumed by the cross-epoch aggregation
    # guard (_detect_cross_epoch_pooling) below; still NOT scored -- it does
    # not touch confidence, conflict, or scoring_excluded on its own.
    canonical_profile: str = ""
    canonical_profile_hash: str = ""
    # z_goal-stream liveness (2026-07-27). The runtime backstop's counter block
    # (ree-v3 experiments/_lib/z_goal_stream.py), carried verbatim for
    # queryability. Surfaced, NEVER scored: it does not touch confidence,
    # conflict, scoring_excluded or adjudication -- this is record-and-surface,
    # not a gate.
    #   {"ticks_total": N, "ticks_active": M, "writer_calls": W,
    #    "active_frac": M/N, "writer_defect": bool,
    #    "goal_state_present": bool, "n_agents": k}
    # READ IT VIA `writer_defect`, NOT `active_frac`. A zero fraction is a
    # legitimate and common reading -- a goal-OFF parity arm and a negative
    # control (V3-EXQ-626b's ARM_NO_BENEFIT) both read 0.0 correctly, and so
    # does a correctly-wired run whose GoalState benefit gate never opened
    # because the agent met no resource (measured on a StepHarness run, which
    # structurally cannot carry the defect). `writer_calls == 0` with
    # `ticks_total > 0` is the unambiguous defect signature; `writer_defect` is
    # that verdict precomputed by the producer. An EMPTY dict here means the run
    # recorded no block at all -- UNMEASURED, which is almost the whole
    # historical corpus. Unmeasured is never rendered as 0.0 and never flagged.
    z_goal_stream: dict[str, Any] = field(default_factory=dict)


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
                             being false.

                             RUN-LEVEL COMBINATION MODE (2026-08-26,
                             failure_autopsy_V3-EXQ-946_2026-08-25.md Sec.6).
                             (3b) itself has NO representation of AND-vs-OR
                             combination semantics by default: a criterion
                             tagged load_bearing:true can mean EITHER "my own
                             failure alone invalidates the overall PASS" (an
                             AND-gate member -- the V3-EXQ-621a pattern (3b)
                             exists to catch) OR "I am a genuine, meaningful,
                             worth-surfacing finding for MY OWN arm/operating-
                             point's conclusion, deliberately OR-combined with
                             my siblings" (V3-EXQ-946 `overall_pass =
                             any(per_arm_pass.values())`; V3-EXQ-927/928's
                             `any_fix_clears`; V3-EXQ-948's own
                             combination_rule, "PASS is carried by ONE
                             criterion... not by a conjunction"). A driver
                             using OR-semantics declares it explicitly via
                             `interpretation.criteria_aggregation: "any"`
                             (absent, or any other value, defaults to "all",
                             the historical implicit AND behaviour every
                             pre-2026-08-26 manifest keeps unchanged). Under
                             "any", (3b) fires only when EVERY load_bearing:true
                             criterion has passed:false, so a genuinely vacuous
                             OR-driver PASS (every declared load-bearing
                             criterion failed) is still caught -- it just stops
                             firing on the FIRST false entry the way "all" mode
                             does, which is exactly the M-of-N shape "all" mode
                             cannot represent. Distinct in kind from the four
                             legacy-path sub-cases documented below: those all
                             fix a NAME/KEY-MATCHING mismatch between
                             criteria_non_degenerate{} and criteria[] in code
                             that (3b) never even reaches once it fires; this
                             fixes (3b) itself, upstream of that path, and has
                             no join/key-matching involved. NARROW BY
                             MEASUREMENT: of 941 manifests under
                             evidence/experiments as of 2026-08-26, exactly 4
                             distinct runs (8 files, flat+pack) are
                             diagnostic/baseline, overall PASS, and carry >=2
                             load_bearing:true criteria with a passed=true/false
                             mix -- V3-EXQ-927, V3-EXQ-928, V3-EXQ-946,
                             V3-EXQ-948 -- all corrected to declare
                             criteria_aggregation="any". A fifth candidate,
                             V3-EXQ-921, was found by the same sweep and ruled
                             OUT: its experiment_purpose is "evidence", so it
                             never reaches this function at all (returns "n/a"
                             at the top-of-function purpose gate) regardless of
                             its criteria[] shape -- left unmodified.

                             CONVENTION for the legacy check: a key
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
                             That key-to-name join is PREFIX-TOLERANT: an exact
                             match always wins, and failing that a key inherits a
                             criterion's tag only when it prefixes exactly ONE
                             name on an underscore boundary. Keying it on exact
                             equality alone let the 783 exclusion be silently
                             defeated by an author spelling one criterion two
                             ways -- short key in criteria_non_degenerate{}, long
                             name in criteria[] -- which is how V3-EXQ-830 drew a
                             spurious vacuous_pass despite passing its own
                             load-bearing criterion (failure_autopsy_V3-EXQ-830_
                             2026-07-29.md Sec.2). Ambiguous (>=2 candidates) and
                             unmatched keys inherit nothing, so ambiguity resolves
                             toward FLAGGING and no existing adjudication moves.
                             ONE NARROW EXCEPTION to that unmatched-key default:
                             when criteria[] declares an AGGREGATE non-degeneracy
                             criterion (name ending "_non_degenerate") tagged
                             load_bearing:true that PASSED, unmatched keys are
                             the informational excess that aggregate deliberately
                             does not cover, and are excluded. Fixes the third
                             join-mismatch sub-case, where -- unlike 783 and 830
                             -- no criteria[] entry exists to be found at all,
                             by design (V3-EXQ-906 reports 10 channels and gates
                             on 4 via one aggregate; failure_autopsy_V3-EXQ-906_
                             2026-08-09.md). Safe because a degenerate GATED
                             subset makes the aggregate itself passed:false,
                             which (3b) catches before this path runs.
                             A FOURTH exception covers manifests with no
                             criteria[] array AT ALL, using an
                             <arm_label>::<check_name> key convention: a False
                             key is excluded from the vacuity check if some
                             OTHER key sharing the same <arm_label> prefix is
                             True (the author's own paired sanity-check/
                             load-bearing-gate design, e.g. V3-EXQ-908's
                             per-arm C1/C1b pair). See failure_autopsy_V3-EXQ-908_
                             2026-08-10.md.
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
    #
    # RUN-LEVEL COMBINATION MODE (2026-08-26, failure_autopsy_V3-EXQ-946_2026-08-25
    # .md Sec.6). See the "vacuous_pass" docstring entry above for the full
    # rationale and the NARROW BY MEASUREMENT count. `criteria_aggregation: "any"`
    # (driver-declared, defaults to "all" -- unchanged AND behaviour) switches the
    # (3b) test from "ANY load_bearing:true criterion failed" to "EVERY
    # load_bearing:true criterion failed" -- still catches a genuinely vacuous
    # OR-driver PASS, stops false-flagging a legitimate M-of-N OR pass.
    if str(status).upper() == "PASS":
        criteria = interp.get("criteria")
        if isinstance(criteria, list):
            lb_entries = [c for c in criteria
                          if isinstance(c, dict) and c.get("load_bearing") is True]
            if str(interp.get("criteria_aggregation", "all")).strip().lower() == "any":
                if lb_entries and all(c.get("passed") is False for c in lb_entries):
                    return label, "vacuous_pass"
            else:
                for c in lb_entries:
                    if c.get("passed") is False:
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
    #
    # THE JOIN IS PREFIX-TOLERANT, because keying it on exact string equality let
    # the 783 exclusion be silently defeated by an author who spells the same
    # criterion two ways -- a SHORT key in criteria_non_degenerate{} and a LONG
    # name in criteria[]. V3-EXQ-830 shipped keys {C_DECIDABLE, C_SLOW_FIRES,
    # C_DISSOCIABLE, C_CONTROL} against names {C_DECIDABLE_instrument_returned_a
    # _reading, C_SLOW_FIRES_on_rollout, C_DISSOCIABLE_low_cofire_distinct
    # _positions, C_CONTROL_slow_silent_with_flag_off}: NO key matched any name,
    # so nothing was excluded and C_DISSOCIABLE:false (a criterion its author had
    # explicitly tagged load_bearing:false, and which is degenerate for the
    # correct reason -- dissociability is unmeasurable when the slow scale never
    # fires) produced a spurious vacuous_pass on a run whose load-bearing
    # criterion passed. Same OUTCOME class as 783, different ROUTE: there the
    # exclusion was absent, here it is present but its join key mismatched.
    # See failure_autopsy_V3-EXQ-830_2026-07-29.md Sec.2.
    #
    # CONSERVATIVE BY CONSTRUCTION -- a false HIT here would suppress a real
    # vacuity flag, so the resolution never guesses:
    #   * an EXACT name match always wins (identical to the pre-2026-07-29
    #     behaviour, so every existing adjudication is preserved);
    #   * failing that, a key inherits a criterion's tag ONLY if it prefixes
    #     exactly ONE name AND does so on an underscore boundary (key + "_"),
    #     so C_DISSOCIABLE matches C_DISSOCIABLE_low_cofire... but never
    #     C_DISSOCIABLEXYZ;
    #   * 0 candidates (unmatched) or >= 2 (ambiguous) inherit NOTHING and are
    #     left exactly as before -- ambiguity is resolved toward flagging.
    # Only the short-key/long-name direction is tolerated; a key LONGER than its
    # name is not the observed shape and stays unmatched.
    by_name: dict = {}
    _criteria = interp.get("criteria")
    if isinstance(_criteria, list):
        for c in _criteria:
            if isinstance(c, dict) and isinstance(c.get("name"), str):
                by_name[c["name"]] = c.get("load_bearing")

    def _load_bearing_for(key: str) -> Any:
        if key in by_name:
            return by_name[key]
        candidates = [n for n in by_name if n.startswith(key + "_")]
        if len(candidates) == 1:
            return by_name[candidates[0]]
        return None

    # THIRD sub-case of the join-mismatch class (V3-EXQ-906, 2026-08-09). Both
    # precedents above assume a criteria[] entry EXISTS to be found by a better
    # name match -- 783 the exclusion was absent, 830 the join key mismatched.
    # Here there is nothing to find: the driver reports a BROAD per-channel
    # non-degeneracy telemetry block in criteria_non_degenerate{} but gates on a
    # NARROW subset via ONE AGGREGATE criterion, so the excess keys have no
    # corresponding criteria[] entry AT ALL, BY DESIGN. V3-EXQ-906 reports 10
    # channels and gates on 4 of them via `core_channels_non_degenerate`; the
    # unmatched channel_vigor:false / channel_z_block:false then trip a spurious
    # vacuous_pass on a run whose load-bearing gate genuinely cleared. Same
    # mechanism on both V3-EXQ-665 runs and V3-EXQ-664 (all 2026-06-10, none
    # previously autopsied). See failure_autopsy_V3-EXQ-906_2026-08-09.md Sec.1.
    #
    # THE LICENCE IS AN EXPLICIT, LOAD-BEARING, CLEARED AGGREGATE -- not the mere
    # absence of a match. A criteria[] entry whose NAME ends in "_non_degenerate"
    # IS a non-degeneracy assertion in the same vocabulary as the crit{} keys (the
    # same naming-convention device the "_branch" exclusion above already uses),
    # so when the author declares one, tags it load_bearing:true, and it PASSED,
    # they have said which non-degeneracy assertions gate this run: the aggregate.
    # The unmatched remainder is then the informational excess the aggregate
    # deliberately does not cover, and is excluded from the vacuity check.
    #
    # SAFETY -- this cannot suppress a real vacuity flag on the aggregate's own
    # scope. Should the gated subset go degenerate, the aggregate itself carries
    # passed:false, and the (3b) check above fires vacuous_pass BEFORE this path
    # is reached. Requiring load_bearing:true AND passed:true is what makes the
    # licence conditional rather than a blanket "unmatched => informational".
    #
    # NARROW BY MEASUREMENT, not by assertion. Over all 463 manifests under
    # evidence/experiments as of 2026-08-09 this moves EXACTLY the four runs named
    # above, all vacuous_pass -> verified. The blanket alternative ("criteria[] is
    # present, so any unmatched key is informational") was measured first and
    # rejected: it additionally cleared V3-EXQ-859/863 (mech448/449_ablation
    # _discriminates both false against a lone `sample_adequate` criterion),
    # V3-EXQ-767/768 (pref_*_varies_across_seeds:false -- absent seed variation IS
    # degeneracy) and V3-EXQ-792a, none of which has been adjudicated and several
    # of which look like genuine flags. Ambiguity still resolves toward FLAGGING.
    _aggregate_cleared = False
    if isinstance(_criteria, list):
        for c in _criteria:
            if (isinstance(c, dict)
                    and isinstance(c.get("name"), str)
                    and c["name"].endswith("_non_degenerate")
                    and c.get("load_bearing") is True
                    and c.get("passed") is True):
                _aggregate_cleared = True
                break

    def _out_of_aggregate_scope(key: str) -> bool:
        if not _aggregate_cleared:
            return False
        if key in by_name:
            return False
        return len([n for n in by_name if n.startswith(key + "_")]) != 1

    # FOURTH sub-case of the join-mismatch class (V3-EXQ-908, 2026-08-10). Unlike
    # all three precedents above, this manifest's interpretation block carries NO
    # criteria[] array AT ALL -- by_name is empty, _aggregate_cleared can never be
    # True, and none of the exclusions above can ever fire here. With nothing to
    # match, the legacy fallback would flag on criteria_non_degenerate{}'s bare
    # False values alone.
    #
    # V3-EXQ-908 reports per-arm keys using an <arm_label>::<check_name> naming
    # convention: A2_tagger_gumbel::C1_breaks_saddle=False sits beside
    # A2_tagger_gumbel::C1b_context_dependent=True for the SAME arm. The driver's
    # own docstring (v3_exq_908_sd016_h3_hard_selection.py, "DV-SYMMETRY CHECK")
    # explains why: for a hard-selection arm, near-zero entropy (C1) is a
    # mechanical byproduct of the selector's own construction (topk k=1 forces
    # exactly 0; annealed Gumbel anneals toward 0), not evidence of context-
    # discrimination -- the genuinely informative, independently-measured gate is
    # C1b. A False C1 beside a True C1b for the same arm is the author's own
    # DV-symmetry design working as intended, not a gate cleared on nothing. See
    # failure_autopsy_V3-EXQ-908_2026-08-10.md Sec.1.
    #
    # THE LICENCE: a key that follows the <arm>::<check> convention (contains
    # "::") and is False is excluded from the vacuity check if some OTHER key
    # sharing the same <arm> prefix is True. GATED to manifests with no
    # criteria[] array at all -- a manifest that DOES carry criteria[] already
    # has the three exclusions above to draw on, and narrowing this one to the
    # exact confirmed shape keeps it from interacting with that logic in any
    # unmeasured way. Ambiguity still resolves toward FLAGGING: a False key with
    # no True same-arm sibling (or no "::" at all) stays in the vacuity check.
    #
    # NARROW BY MEASUREMENT: across every manifest under evidence/experiments as
    # of 2026-08-10, exactly ONE (V3-EXQ-908) uses the "::" arm-prefix convention
    # in criteria_non_degenerate{} at all, so this exclusion is inert everywhere
    # else today.
    _no_criteria_array = not (isinstance(_criteria, list) and len(_criteria) > 0)

    def _has_true_arm_sibling(key: str) -> bool:
        if not _no_criteria_array or "::" not in key:
            return False
        prefix = key.split("::", 1)[0]
        return any(str(k2).split("::", 1)[0] == prefix and str(k2) != key
                   and v2 is True
                   for k2, v2 in crit.items() if "::" in str(k2))

    non_load_bearing = {k for k in (str(x) for x in crit.keys())
                        if _load_bearing_for(k) is False}
    degeneracy_assertions = [v for k, v in crit.items()
                             if not str(k).endswith("_branch")
                             and str(k) not in non_load_bearing
                             and not _out_of_aggregate_scope(str(k))
                             and not _has_true_arm_sibling(str(k))]
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


# --------------------------------------------------------------------------
# Literature per-paper identity, for duplicate-entry deduplication (GFLAG-0032).
#
# Mirrors, byte-for-byte, three functions that already exist elsewhere in the
# repo: REE_assembly/scripts/verify_literature_identifiers.normalise_doi,
# REE_assembly/scripts/audit_literature_duplicate_entries.normalise_pmid, and
# REE_assembly/scripts/audit_literature_bibliographic_accuracy.norm_title (via
# its strip_accents helper). Reimplemented LOCALLY rather than imported
# cross-directory: those three modules pull in urllib/network-capable code
# paths (live DOI/PubMed identifier resolution) that this indexer -- stdlib
# only per the module docstring, run on every commit and by several
# concurrent writers -- must not depend on. test_build_experiment_indexes.py
# pins these three functions byte-identical against the canonical
# implementations so the copies cannot silently drift; if the canonical
# DOI/title normalisation rules ever change, update both sides.


def _lit_normalise_doi(doi: Any) -> str | None:
    """Comparison form for a DOI. Never used to rewrite a record's field."""
    if not doi:
        return None
    text = str(doi).strip().lower()
    text = re.sub(r"^https?://(dx\.)?doi\.org/", "", text)
    text = re.sub(r"^doi:\s*", "", text)
    text = re.sub(r"/{2,}", "/", text)
    return text.rstrip(". ") or None


def _lit_normalise_pmid(pmid: Any) -> str | None:
    """Comparison form for a PMID. Never used to rewrite a record's field."""
    if pmid is None:
        return None
    text = str(pmid).strip().lower()
    text = text.replace("pmid:", "").strip()
    text = text.lstrip("0") or text
    return text or None


def _lit_norm_title(title: Any) -> str:
    """Accent-, markup- and punctuation-normalised title, for EXACT equality only.

    Fuzzy title matching is deliberately NOT reproduced here -- see
    _group_literature_by_paper below for why.
    """
    if not isinstance(title, str):
        return ""
    stripped = "".join(
        c for c in unicodedata.normalize("NFKD", title) if not unicodedata.combining(c)
    )
    t = stripped.lower()
    t = re.sub(r"<[^>]+>", " ", t)  # crossref titles carry markup
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return " ".join(t.split())


class _LiteratureUnionFind:
    """Union-find that remembers which route(s) merged each group.

    Mirrors audit_literature_duplicate_entries.py's Union class in spirit --
    a group merged only by an identical DOI/PMID/title is auditable back to
    that fact via `routes()`.
    """

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self._edge_routes: dict[int, set[str]] = defaultdict(set)

    def find(self, i: int) -> int:
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def union(self, i: int, j: int, route: str) -> None:
        ri, rj = self.find(i), self.find(j)
        if ri != rj:
            self.parent[rj] = ri
            ri = self.find(ri)
        self._edge_routes[ri].add(route)

    def routes(self) -> dict[int, list[str]]:
        merged: dict[int, set[str]] = defaultdict(set)
        for root, routes in self._edge_routes.items():
            merged[self.find(root)] |= routes
        return {root: sorted(routes) for root, routes in merged.items()}


def _group_literature_by_paper(
    lit_entries: "list[LiteratureRecord]",
) -> "tuple[dict[tuple[str, str], int], dict[int, list[str]]]":
    """Union-find grouping of literature records that name the SAME PAPER.

    Same three EXACT routes as audit_literature_duplicate_entries.py's
    GROUPING_KEYS: normalised DOI, normalised PMID, exact normalised title.
    Fuzzy title matching is deliberately excluded -- measured over this
    corpus (evidence/planning/literature_duplicate_entries_2026-08-14.md),
    7 of 9 fuzzy-title pairs were DIFFERENT papers by the same author (e.g.
    Craig 2002 "How do you feel?..." vs Craig 2003 "Interoception:..."), so a
    fuzzy route here would silently merge two independent studies and make
    one of them vanish from a claim's scored evidence -- the opposite of
    what this fix exists to prevent. Exact-title matching measured clean
    over the same corpus.

    A record with no doi/pmid/title in common with any other record is its
    own singleton group and can never be deduplicated against anything --
    this is the safe default for the ~un-identified tail of the corpus.

    Returns (group_of, routes_by_group):
      group_of[(literature_type, entry_id)] -> union-find root index.
      routes_by_group[root] -> sorted routes ("doi"/"pmid"/"title") that
      connected that group, for the `duplicate_route` audit field. Absent
      for singleton groups (nothing ever unioned).
    """
    n = len(lit_entries)
    uf = _LiteratureUnionFind(n)

    for field_name, route in (("doi", "doi"), ("pmid", "pmid"), ("title_norm", "title")):
        seen: dict[str, int] = {}
        for i, lit in enumerate(lit_entries):
            value = getattr(lit, field_name)
            if not value:
                continue
            if value in seen:
                uf.union(seen[value], i, route)
            else:
                seen[value] = i

    group_of = {
        (lit.literature_type, lit.entry_id): uf.find(i)
        for i, lit in enumerate(lit_entries)
    }
    return group_of, uf.routes()


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
    # Mirrors RunRecord.evidence_direction_per_claim. A literature entry can bear
    # differently on the several claims it tags just as an experiment run can, and
    # without this the blanket evidence_direction was applied to every one of them.
    evidence_direction_per_claim: dict[str, str] = field(default_factory=dict)
    architecture_epoch: str = ""
    confidence: float = 0.5
    confidence_rationale: str = ""
    failure_signatures: list[str] = field(default_factory=list)
    # Per-paper identity (GFLAG-0032 dedup), normalised at scan time.
    doi: str | None = None
    pmid: str | None = None
    title_norm: str = ""


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


def _batch_keys_for_entries(entries: list[dict[str, Any]]) -> set[str]:
    """Collapse experimental entries into distinct minute-truncated "batch" keys
    (falling back to the run_id prefix when no timestamp is present). Used to
    count how many distinct targeted evidence batches back a conflict signal,
    both for the general recent-activity signal and for the mandatory-decision
    freshness gate."""
    batch_keys: set[str] = set()
    for entry in entries:
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
    return batch_keys


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


def _is_dry_run(manifest: dict[str, Any]) -> bool:
    """True if a manifest's top-level dry_run flag is set (any truthy form).

    A `--dry-run` smoke writes a real manifest (flat AND run-pack) into
    evidence/experiments/, but it is NOT evidence: the driver's dry-run branch
    collapses the design to a couple of toy episodes and often a single seed, so
    its PASS/FAIL is meaningless. Mirrors `_is_dry_run` in
    scripts/generate_pending_review.py verbatim -- the str-cast tolerates the
    bool / int / str spellings that have all appeared in the corpus.
    """
    return str(manifest.get("dry_run", "")).strip().lower() in ("true", "1", "yes")


def _load_dry_run_run_ids(base_dir: Path) -> set[str]:
    """run_ids of every manifest on disk that is a `--dry-run` smoke.

    WHY A RUN_ID SET AND NOT A PER-FILE FLAG CHECK. The two signals live in
    DIFFERENT files for the same run, so neither alone is sufficient:

      * the FLAT manifest carries the top-level `dry_run` flag (drivers thread
        `"dry_run": args.dry_run` into the dict they serialise), and when
        `pack_writer.write_flat_manifest` is also threaded it additionally
        prefixes the filename `_dry_<run_id>.json`; while
      * the RUN PACK -- `<experiment_type>/runs/<run_id>/manifest.json`, which
        is what `_scan_runs` actually scores -- was written from a different
        code path (`experiment_pack/v1`) that had NO dry_run field at all.

    So the pack that reaches scoring was indistinguishable from a real run when
    read on its own; the flag had to be carried across from its flat sibling by
    run_id. That is exactly the shape of the confirmed 2026-07-26 MECH-245
    contamination: two 1-seed smokes of V3-EXQ-825 landed as
    `_dry_..._v3.json` (flagged, correctly named, harmless) AND as two
    `status: FAIL` / `evidence_direction: weakens` packs (unflagged, scored),
    which became that claim's entire negative evidence base while its one
    genuine run PASSED.

    PACKS NOW SELF-IDENTIFY, AND THE RUN_ID ARM STAYS ANYWAY (2026-07-28).
    Both pack writers were taught to emit a truthy top-level `dry_run`
    (`sync_v3_results.build_runpack_docs` unconditionally;
    `pack_writer.PackWriter.write_pack` via a new `dry_run=` argument), and all
    36 historical dry packs on disk were backfilled with the flag, so there is
    no longer any pack whose ONLY carrier is a flat sibling. Callers of
    `_scan_runs` / `_iter_manifests_with_arm_results` accordingly test
    `_is_dry_run(manifest) or run_id in dry_run_ids`, and the first arm now
    fires on its own for every known case.

    The run_id arm is NOT removed, because `write_pack`'s new argument is
    OPT-IN: a driver that threads `dry_run` to `write_flat_manifest` but not to
    `write_pack` still emits an unflagged pack, and the flat sibling is again
    the only carrier. Same for any driver that hand-rolls its own pack dict.
    Keeping the carry costs one directory walk and preserves the backstop for
    exactly the silent-failure class that produced the MECH-245 incident.

    The coupling this closes was a live cleanup trap: while the pack could not
    self-identify, deleting a flat dry-run manifest WITHOUT also deleting its
    pack silently promoted that smoke back to real scored evidence. Deleting a
    flat manifest on its own is still never correct -- but it is no longer
    load-bearing for the dry-run exclusion.

    THE SUBDIRECTORY FLAT GLOB WAS MISSING, AND IT WAS LEAKING (fixed 2026-07-28).
    This scanned `*.json` (top level) and `**/runs/**/manifest.json` (packs) but NOT
    `*/*.json` -- a flat manifest living in its per-experiment subdirectory,
    `<experiment_type>/<run_id>.json`, which is the OTHER placement
    `sync_v3_results._derive_experiment_type_and_dir` handles and the one older
    drivers use. A dry smoke written there was invisible to this function, so its
    pack scored. Measured at the 2026-07-28 backfill: 13 of the 36 dry packs on
    disk were STILL being counted as real evidence after the cb7298c1c4 fix --
    v3_exq_147a / 166b / 166c / 166d / 207 / 208 / 209 / 210 / 211 / 212 (x2) /
    365 / 407 -- contributing phantom PASS/FAIL runs to ARC-042, MECH-070,
    MECH-075, MECH-104, MECH-153, MECH-155, MECH-156 and MECH-231. Adding the
    glob is a no-op TODAY (those packs now carry the flag themselves, so the
    `_is_dry_run(manifest)` arm catches them), and is kept precisely so the
    backstop is not holed the same way for the next unflagged pack.

    Scans all three globs so a flag arriving via any path is caught. Best-effort:
    an unreadable or non-dict file contributes nothing rather than raising.
    """
    ids: set[str] = set()
    if not base_dir.is_dir():
        return ids
    for path in (list(base_dir.glob("*.json"))
                 + list(base_dir.glob("*/*.json"))
                 + list(base_dir.glob("**/runs/**/manifest.json"))):
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(manifest, dict):
            continue
        # THE SUFFIX FORM WAS MISSING, AND IT WAS LEAKING (fixed 2026-09-01,
        # found while building flat-only-orphan discovery -- see
        # _scan_flat_only_orphans). This checked the documented `_dry_<run_id>
        # .json` PREFIX convention only, but a second, equally real naming
        # convention is live in the corpus: `<run_id>_dry.json` (SUFFIX,
        # `stem.endswith("_dry")` -- e.g. v3_exq_259_wanting_gradient_
        # navigation_dry.json, an all-zero toy companion of a real run in the
        # same directory). scripts/audit_flat_only_orphaned_manifests.py's own
        # `_is_dry_run` already checks both forms; this one didn't. Confirmed
        # zero effect on any manifest that reaches scoring TODAY (none of the
        # 14 newly-caught run_ids match an existing run pack -- they were
        # flat-only and therefore invisible before flat-only-orphan discovery
        # existed at all), so this is a pure correctness fix for that new
        # path, not a change to any previously-scored evidence.
        if not (_is_dry_run(manifest) or path.name.startswith("_dry_")
                or path.stem.endswith("_dry")):
            continue
        run_id = manifest.get("run_id")
        if run_id:
            ids.add(str(run_id))
    return ids


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
    # substrate_commit / enabled_default_off_flags / substrate_commit_unavailable
    # (2026-09-01). Same PROVENANCE-not-direction status as substrate_hash above --
    # absent from _FLAT_DIRECTION_FIELDS, so they never change how a run scores.
    # They are listed here because the pack projection did not carry
    # enabled_default_off_flags until the same date: measured 2026-09-01, 33 flat
    # manifests had the field and 0 of their pack copies did, so the indexer read
    # 0 of 1832 runs as having recorded it while a third of recent flat manifests
    # actually had. The flat overlay fixes the historical corpus immediately; the
    # sync_v3_results mapping fixes packs written from now on. Both are needed --
    # neither alone makes the recorded coverage true.
    "substrate_commit",
    "enabled_default_off_flags",
    "substrate_commit_unavailable",
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
    # z_goal_stream (2026-07-27) is backfilled for the same reason machine_class
    # was: the run-pack mapper is a whitelist, so a pack materialised by a
    # sync_v3_results predating the mapping drops the block even when the flat
    # sibling carries it. Pure provenance -- not in _FLAT_DIRECTION_FIELDS, so it
    # cannot change how a run scores. Unlike its three string siblings this value
    # is a DICT, which is why _prov_is_empty below is type-aware.
    "z_goal_stream",
    # substrate_commit / substrate_commit_unavailable / enabled_default_off_flags
    # (2026-09-01), same whitelist-gap reason as z_goal_stream and machine_class
    # before them. Measured that day: 33 flat manifests carried
    # enabled_default_off_flags and 0 of their pack copies did, so the index read
    # 0 of 1832 runs as having recorded it. sync_v3_results now maps all three, but
    # that only helps packs written from now on -- this backfill is what makes the
    # EXISTING corpus's coverage readable. Pure provenance: none is in
    # _FLAT_DIRECTION_FIELDS, so none can change how a run scores.
    "substrate_commit",
    "substrate_commit_unavailable",
    "enabled_default_off_flags",
)

# Fields for which ONLY None means absent -- an empty container is a MEASUREMENT.
#
# _prov_is_empty treats {} as nothing-worth-backfilling, which is right for
# z_goal_stream ({} there means the run was never instrumented) and wrong for
# enabled_default_off_flags, where {} is the positive statement "measured, every
# known default-off knob confirmed off". Collapsing those two would destroy in the
# index exactly the distinction manifest_core.enabled_default_off_flags_for_agents
# was corrected to preserve at the source (see that function's docstring and the
# substrate_stability plan's P1c completion note, where an earlier draft made the
# same mistake one layer up).
_FLAT_PROVENANCE_NONE_IS_ABSENT = frozenset({"enabled_default_off_flags"})


def _prov_flat_absent(field: str, value: Any) -> bool:
    """Field-aware emptiness for the provenance backfill. See the set above."""
    if field in _FLAT_PROVENANCE_NONE_IS_ABSENT:
        return value is None
    return _prov_is_empty(value)


def _prov_is_empty(value: Any) -> bool:
    """True when a provenance value carries nothing worth backfilling.

    Type-aware because `_FLAT_PROVENANCE_BACKFILL_FIELDS` mixes strings with the
    dict-valued `z_goal_stream`: the previous `str(value).strip() == ""` test
    renders an empty dict as the non-empty literal "{}" and would therefore
    backfill `z_goal_stream: {}` onto the pack -- writing an UNMEASURED run into
    the shape of a measured one. Behaviour for str/None is unchanged.
    """
    if value is None:
        return True
    if isinstance(value, (dict, list, tuple, set)):
        return not value
    return str(value).strip() == ""

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
        if _prov_flat_absent(fld, flat_val):
            continue
        pack_val = pack.get(fld, _MISSING)
        if pack_val is _MISSING or _prov_flat_absent(fld, pack_val):
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


def _resolve_flat_sibling(base_dir: Path, run_dir: Path, run_id: str) -> Path | None:
    """Locate the flat manifest sibling of a run pack, or None if there is none.

    A run pack lives at ``<base>/<experiment_type>/runs/<run_id>/manifest.json``
    and its flat sibling is written to ONE of two places, and historically both
    were used:

      1. ``<base>/<run_id>.json``            -- the top level, and
      2. ``<base>/<experiment_type>/<run_id>.json`` -- beside the run's own
         experiment-type directory (``run_dir.parent.parent``).

    Until 2026-08-14 only (1) was consulted, so a run whose flat copy lives in
    (2) got ``{}`` from the lookup and the governance overlay in
    ``_merge_flat_manifest_overrides`` became a silent no-op -- silent because
    the WARNING there is gated on the overlay having applied. Measured on the
    corpus at the time of the fix: 231 packs had ONLY a subdirectory sibling,
    26 of which carried an annotated governance correction that disagreed with
    an unannotated pack and was therefore never reaching the index (the
    confirmed live case being V3-EXQ-245's two `weakens` rows still scoring
    against MECH-120 after governance reclassified them `non_contributory` on
    2026-04-08).

    ORDER IS LOAD-BEARING: top level FIRST, subdirectory only as a fallback.
    This is deliberately the opposite of "resolve relative to the pack", which
    is the intuitive reading and is WRONG on the real data. 18 packs carry BOTH
    siblings, and in all 18 the top-level copy is the one governance annotated
    -- consistent with the convention documented at the merge call site, that a
    correction is written to ``evidence/experiments/<run_id>.json``. In 6 of
    those the SUBDIRECTORY copy is an unannotated emitter artefact, so
    preferring it would suppress a correction that applies today: a strictly
    additive fix would have become a regression. Checking the top level first
    keeps every currently-working case bit-identical and only adds behaviour
    where the lookup previously found nothing at all.

    Deliberately NOT a glob over the tree: both candidates are exact paths, so
    this costs at most two stat calls per pack.
    """
    for candidate in (base_dir / f"{run_id}.json",
                      run_dir.parent.parent / f"{run_id}.json"):
        if candidate.is_file():
            return candidate
    return None


# Status precedence for a FLAT-ONLY orphan (no pack anywhere). Wider than the
# pack loop's own `status | outcome` read below because `result` is a real
# status carrier in this corpus's "substrate_readiness" diagnostic family --
# several on-disk flat manifests predate pack_writer.write_flat_manifest
# (whose own precedence is the narrower `status | overall_outcome | outcome`)
# and use `result` only. Mirrors scripts/audit_flat_only_orphaned_manifests.
# _resolve_flat_status (kept in sync by hand; that script is read-only
# detection, this is the discovery path that makes a finding actually count).
_FLAT_ONLY_STATUS_FIELDS = ("status", "overall_outcome", "outcome", "result")
_FLAT_ONLY_NON_MANIFEST_NAMES = {"claim_evidence.v1.json"}


def _resolve_flat_only_status(manifest: dict[str, Any]) -> str | None:
    for key in _FLAT_ONLY_STATUS_FIELDS:
        val = manifest.get(key)
        if val not in (None, ""):
            return str(val)
    return None


def _collect_pack_run_ids(base_dir: Path) -> set[str]:
    """run_ids covered by a real run pack (runs/<run_id>/manifest.json),
    UNFILTERED by any dry-run/epoch exclusion the pack loop below applies --
    a flat manifest is only a true orphan if no pack anywhere matches it by
    run_id, regardless of whether that pack itself would score."""
    ids: set[str] = set()
    for manifest_path in base_dir.glob("**/runs/**/manifest.json"):
        run_dir = manifest_path.parent
        if run_dir.parent.name != "runs":
            continue
        ids.add(run_dir.name)
        pm = _load_json(manifest_path)
        rid = pm.get("run_id") if isinstance(pm, dict) else None
        if isinstance(rid, str) and rid.strip():
            ids.add(rid.strip())
    return ids


def _scan_flat_only_orphans(
    base_dir: Path, pack_run_ids: set[str], dry_run_ids: set[str],
) -> list[tuple[Path, dict[str, Any]]]:
    """Flat manifests at evidence/experiments/<run_id>.json or
    evidence/experiments/<experiment_type>/<run_id>.json with NO matching run
    pack anywhere -- structurally invisible to the `**/runs/**/manifest.json`
    glob the pack loop below relies on exclusively. See evidence/planning/
    flat_only_manifest_indexer_invisibility_staged_20260901.md (root-cause
    writeup) and scripts/audit_flat_only_orphaned_manifests.py (the read-only
    detector this discovery path is modeled on -- kept in sync by hand).

    Dry-run smokes are excluded via the SAME `dry_run_ids` set the pack loop
    already builds (it scans this identical flat-file set), so no separate
    dry-run check is needed here. Best-effort JSON read, matching
    `_load_dry_run_run_ids`'s posture for the same corpus-wide flat scan: an
    unreadable or non-dict file contributes nothing rather than raising.
    """
    findings: list[tuple[Path, dict[str, Any]]] = []
    seen: set[Path] = set()
    flat_paths = sorted(base_dir.glob("*.json")) + sorted(base_dir.glob("*/[!_]*.json"))
    for path in flat_paths:
        if path in seen:
            continue
        seen.add(path)
        if path.name in _FLAT_ONLY_NON_MANIFEST_NAMES:
            continue
        if "runs" in path.parts:
            continue
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(manifest, dict):
            continue
        run_id = manifest.get("run_id")
        if not isinstance(run_id, str) or not run_id.strip():
            continue
        run_id = run_id.strip()
        if run_id in pack_run_ids or run_id in dry_run_ids:
            continue
        if _resolve_flat_only_status(manifest) is None:
            continue
        findings.append((path, manifest))
    return findings


def _build_run_record(
    experiment_type: str,
    run_id: str,
    manifest: dict[str, Any],
    manifest_path: Path,
    metrics_path: Path,
    summary_path: Path,
    adapter_signals_path: Path | None,
    metrics: dict[str, float],
    status: str,
    current_epoch: str,
    epoch_start: datetime | None,
) -> RunRecord:
    """Construct a RunRecord from an already-resolved manifest + status +
    metrics dict. Shared by _scan_runs's two discovery paths -- the run-pack
    glob (status via `status | outcome`, metrics via the pack's own
    metrics.json) and the flat-only-orphan path (status via the wider
    `status | overall_outcome | outcome | result` precedence
    `_resolve_flat_only_status` uses, metrics = {} since a pack-less flat
    manifest has no separate metrics.json to point metrics_path at -- its own
    `metrics` field, when present, is an arbitrarily-nested diagnostic dict,
    not the flat `{name: float}` shape metrics.json's `values` key carries).
    """
    timestamp_raw, timestamp = _parse_timestamp(manifest.get("timestamp_utc"), run_id)
    architecture_epoch = str(manifest.get("architecture_epoch", "")).strip()
    if not architecture_epoch and current_epoch and epoch_start and timestamp >= epoch_start:
        architecture_epoch = current_epoch

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
    # substrate_commit is recorded as a dict {commit, dirty, branch?, ...}; the
    # bare sha is what a diff needs, so that is what is surfaced. A legacy
    # manifest carrying a bare string is accepted too (absent on both shapes
    # collapses to "" -- a no-op default, same posture as substrate_hash).
    raw_substrate_commit = manifest.get("substrate_commit")
    if isinstance(raw_substrate_commit, dict):
        substrate_commit = str(raw_substrate_commit.get("commit", "") or "").strip()
    else:
        substrate_commit = str(raw_substrate_commit or "").strip()
    # None (never measured) is DELIBERATELY distinct from {} (measured, nothing
    # enabled) -- see the RunRecord field comment.
    raw_flags = manifest.get("enabled_default_off_flags")
    enabled_default_off_flags = raw_flags if isinstance(raw_flags, dict) else None
    raw_label_balance = manifest.get("label_balance") or {}
    label_balance = raw_label_balance if isinstance(raw_label_balance, dict) else {}
    # machine / machine_class read AFTER the flat-provenance backfill above, so
    # a thin pre-2026-07-16 pack still surfaces the flat sibling's provenance.
    machine = str(manifest.get("machine", "") or "").strip()
    machine_class = str(manifest.get("machine_class", "") or "").strip()
    # queue_id, same reason -- see the RunRecord field comment for why this
    # exists (run_id identifier hygiene / letter-drop stem collisions).
    queue_id = str(manifest.get("queue_id", "") or "").strip()
    # canonical-profile provenance, read the same way as substrate_hash above:
    # caller-supplied, absent on the legacy corpus (no-op default).
    canonical_profile = str(manifest.get("canonical_profile", "") or "").strip()
    canonical_profile_hash = str(manifest.get("canonical_profile_hash", "") or "").strip()
    # z_goal-stream liveness block, read AFTER the flat-provenance backfill
    # (same reason as machine_class: a pack from before the mapper carried it
    # is thin). A non-dict or empty value collapses to {} == UNMEASURED, which
    # is emitted nowhere -- so a missing block can never be mistaken for a
    # measured zero. See the RunRecord field comment for why writer_defect,
    # and not active_frac, is the readable signal.
    raw_z_goal_stream = manifest.get("z_goal_stream") or {}
    z_goal_stream = raw_z_goal_stream if isinstance(raw_z_goal_stream, dict) else {}

    return RunRecord(
        experiment_type=experiment_type,
        run_id=run_id,
        timestamp_raw=timestamp_raw,
        timestamp=timestamp,
        manifest_path=manifest_path,
        metrics_path=metrics_path,
        summary_path=summary_path,
        manifest_status=status,
        queue_id=queue_id,
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
        substrate_commit=substrate_commit,
        enabled_default_off_flags=enabled_default_off_flags,
        label_balance=label_balance,
        machine=machine,
        machine_class=machine_class,
        canonical_profile=canonical_profile,
        canonical_profile_hash=canonical_profile_hash,
        z_goal_stream=z_goal_stream,
    )


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

    # Smoke runs are not evidence. Resolved ONCE for the whole scan: the pack
    # being scored carries no dry_run field of its own, so the flag has to come
    # from its flat sibling by run_id. See _load_dry_run_run_ids.
    dry_run_ids = _load_dry_run_run_ids(base_dir)
    n_dry_skipped = 0

    for manifest_path in sorted(base_dir.glob("**/runs/**/manifest.json")):
        run_dir = manifest_path.parent
        if run_dir.parent.name != "runs":
            continue
        experiment_type = run_dir.parent.parent.name

        # Cheap pre-read form of the check below, for a pack written under a
        # `_dry_`-prefixed directory or experiment_type.
        if run_dir.name.startswith("_dry_") or experiment_type.startswith("_dry_"):
            n_dry_skipped += 1
            continue

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

        # A `--dry-run` smoke never scores. `run_id in dry_run_ids` is the
        # load-bearing arm (the flag lives on the flat sibling, not here); the
        # `_is_dry_run(manifest)` arm covers a future pack that carries the flag
        # itself. Deliberately BEFORE the flat-override merge below, so a smoke
        # cannot pick up a governance annotation on the way out.
        if run_id in dry_run_ids or _is_dry_run(manifest):
            n_dry_skipped += 1
            continue

        # Flat-manifest authoritative override (2026-06-14). Governance /
        # failure-autopsy corrections land on evidence/experiments/<run_id>.json
        # (with an evidence_direction_note / degeneracy_reason), not this pack
        # copy. When the flat copy carries such an annotation and the pack does
        # not, the flat copy is the corrected one and its governance fields are
        # overlaid here so a flat-only correction is not silently ignored. The
        # inverse legacy shape (pack annotated, flat a stale earlier emission --
        # the v3_exq_150-series) is left untouched. A missing sibling => {} =>
        # no-op (legacy/synthetic runs without a flat sibling are untouched).
        # The sibling may sit at the top level OR in the run's experiment-type
        # directory; see _resolve_flat_sibling for why the top level wins when
        # both exist.
        _flat_path = _resolve_flat_sibling(base_dir, run_dir, run_id)
        flat_manifest = _load_json(_flat_path) if _flat_path is not None else {}
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

        run_id = run_id or run_dir.name

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

        by_experiment[experiment_type].append(_build_run_record(
            experiment_type, run_id, manifest, manifest_path, metrics_path, summary_path,
            adapter_signals_path, metrics, status, current_epoch, epoch_start,
        ))

    if n_dry_skipped:
        print(f"Excluded {n_dry_skipped} dry-run smoke pack(s) from scoring "
              f"({len(dry_run_ids)} dry-run run_id(s) on disk).")

    # Flat-only orphan discovery (2026-09-01, GFLAG-0111): a manifest written
    # ONLY via pack_writer.write_flat_manifest, with no matching run pack
    # anywhere, is invisible to the glob loop above regardless of its run_id's
    # naming. See _scan_flat_only_orphans for the detection semantics and
    # evidence/planning/flat_only_manifest_indexer_invisibility_staged_20260901.md
    # for the corpus scan + affected-claim table this closes.
    pack_run_ids = _collect_pack_run_ids(base_dir)
    flat_only_orphans = _scan_flat_only_orphans(base_dir, pack_run_ids, dry_run_ids)
    n_flat_only_skipped_no_type = 0
    for flat_path, flat_manifest in flat_only_orphans:
        run_id = str(flat_manifest.get("run_id", "")).strip()
        experiment_type = str(flat_manifest.get("experiment_type", "")).strip()
        if not experiment_type and flat_path.parent != base_dir:
            experiment_type = flat_path.parent.name
        if not experiment_type:
            n_flat_only_skipped_no_type += 1
            continue
        status = str(_resolve_flat_only_status(flat_manifest) or "UNKNOWN").upper()
        by_experiment[experiment_type].append(_build_run_record(
            experiment_type, run_id, flat_manifest, flat_path, flat_path, flat_path,
            None, {}, status, current_epoch, epoch_start,
        ))
    if flat_only_orphans:
        print(f"Discovered {len(flat_only_orphans)} flat-only orphaned manifest(s) "
              f"with no matching run pack (scored directly from the flat file; "
              f"{n_flat_only_skipped_no_type} skipped for missing experiment_type).")

    for runs in by_experiment.values():
        runs.sort(key=lambda r: (r.timestamp, r.run_id))
    return by_experiment


def _detect_and_mark_duplicate_emissions(
    by_experiment: dict[str, list[RunRecord]],
) -> list[dict[str, Any]]:
    """Auto-mark byte-identical-output duplicate emissions as superseded.

    Within each experiment_type, runs that share an identical numeric-metrics
    signature AND the same queue_id are treated as duplicate emissions of the
    same underlying run (typical causes: runner re-emission after restart,
    deterministic re-runs from regex-bug-period queue replays). The latest
    emission is kept as canonical; earlier emissions are mutated in-memory to
    evidence_direction='superseded' so the existing scoring loop excludes them.

    The queue_id match is load-bearing, not incidental (2026-08-19, run_id
    identifier hygiene / letter-drop stem collisions -- confirmed
    failure_autopsy_V3-EXQ-920a_2026-08-16). `experiment_type` is a run-pack
    directory name derived from the driver's `EXPERIMENT_TYPE` constant, and a
    lettered bug-fix re-queue (V3-EXQ-920 -> V3-EXQ-920a) commonly reuses that
    constant unchanged, so TWO DIFFERENT queue_ids can legitimately land in one
    experiment_type bucket. Grouping on metrics-signature alone would then treat
    two genuinely different runs as "the same run re-emitted" whenever their
    numeric metrics happen to coincide, silently superseding one queue item's
    real evidence under the other's. A blank queue_id (pre-queue_id-field
    legacy manifests) still groups with other blanks, so old-corpus dedup
    behaviour for that data is unchanged; only cross-queue_id collapsing is new.

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
        by_signature: dict[tuple[str, str], list[RunRecord]] = defaultdict(list)
        for run in runs:
            if not run.metrics:
                continue  # cannot fingerprint without numeric metrics
            sig_src = json.dumps(sorted(run.metrics.items()), default=str)
            sig = hashlib.sha1(sig_src.encode()).hexdigest()[:12]
            by_signature[(sig, run.queue_id)].append(run)
        for (sig, _qid), dup in by_signature.items():
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
        # Per-claim direction overrides, same contract as the manifest path above:
        # when present for a claim_id, replaces the entry-level direction for that
        # claim only; absent keys fall back to it. "unknown" entries are dropped so
        # a placeholder cannot mask the entry-level value.
        raw_per_claim = record.get("evidence_direction_per_claim") or {}
        evidence_direction_per_claim: dict[str, str] = {}
        if isinstance(raw_per_claim, dict):
            for cid, val in raw_per_claim.items():
                normalized = _normalize_direction(val)
                if normalized != "unknown":
                    evidence_direction_per_claim[str(cid)] = normalized
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

        # Per-paper identity for duplicate-entry deduplication (GFLAG-0032).
        # Only `source`'s own doi/pmid/title are read -- nothing here is ever
        # written back to a record.
        source = record.get("source")
        if not isinstance(source, dict):
            source = {}
        doi = _lit_normalise_doi(source.get("doi"))
        pmid = _lit_normalise_pmid(source.get("pmid"))
        title_norm = _lit_norm_title(source.get("title"))

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
                evidence_direction_per_claim=evidence_direction_per_claim,
                architecture_epoch=architecture_epoch,
                confidence=confidence,
                confidence_rationale=confidence_rationale,
                failure_signatures=[str(x) for x in signatures],
                doi=doi,
                pmid=pmid,
                title_norm=title_norm,
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
        # A crash-before-manifest / synthetic runner record carries
        # manifest_status ERROR (or UNKNOWN), never FAIL -- `manifest_fail` above
        # is False for it, and `criteria_fail` is also False (a crashed run has no
        # metrics for fail_if to compare against). Before this branch, that left
        # final_status on its dataclass default of "PASS", so a code crash was
        # reported as a clean pass everywhere final_status is read (confirmed
        # 2026-08-02 on V3-EXQ-870: unlinked_runs carried status="PASS" for a
        # crash-before-manifest ERROR record, and pending_review.md then listed
        # it under "PASS (verify & close)" instead of routing it to
        # /diagnose-errors). Propagate ERROR/UNKNOWN through rather than
        # defaulting past it -- FAIL still takes precedence when a run somehow
        # carries both (defensive; not expected in practice).
        if criteria_fail or manifest_fail:
            run.final_status = "FAIL"
        elif run.manifest_status in ("ERROR", "UNKNOWN"):
            run.final_status = run.manifest_status
        else:
            run.final_status = "PASS"

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
    _atomic_write_text(doc_path, template)
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


# The generated indexes render their run stamp exactly once, as
# ``Generated: `<iso>` ``. Same shape, and deliberately the same regex, as
# scripts/igw_routine_tick.py::_WORKSET_MD_STAMP_RE -- that module solved this
# identical problem for the IGW workset on 2026-08-07 and its reasoning applies
# here verbatim.
_GENERATED_STAMP_RE = re.compile(r"^Generated: `[^`]*`$", re.M)


def _strip_generated_stamp(text: str) -> str:
    return _GENERATED_STAMP_RE.sub("Generated: `<stamp>`", text)


def _write_index_if_material(path: Path, text: str) -> bool:
    """Write `text` to `path` unless it differs from what is there only by stamp.

    THE POINT OF THE GATE -- this is a git-hygiene fix, not a performance one.
    Every write_text here was unconditional, so a full regen rewrote ~1211
    per-experiment INDEX.md files whose entire diff was the `Generated:` line.
    The shared REE_assembly checkouts therefore sat PERMANENTLY ~1218 files
    dirty (measured 2026-08-08 on ree-cloud-5: 1218 dirty, of which 1213 lines
    changed were the stamp and nothing else -- 84% of the whole diff).

    That permanent dirt is the precondition for the escalating git-sync wedge
    this was found under, in three compounding ways:
      - `git pull --rebase --autostash` must stash and restore ~1200 files
        every tick, so any conflict aborts the whole rebase (audit_stashes.py
        reported 8 aborts / 8 starts in 2h on the Mac);
      - ree_git_sync_repair.sh auto-repairs a checkout only when every ahead
        commit and dirty path is telemetry-only, so it correctly REFUSES
        forever while these files are dirty (`NEEDS_HUMAN` every 3h cycle);
      - CLAUDE.md's HEAD/worktree-skew procedure asks the reader to eyeball
        `git status --porcelain`, which is unusable at 1200 lines of noise.

    CLAUDE.md's Coordinator section records that the same pattern in another
    guise -- the 30-minute heartbeat "liveness tick", ~40 redundant commits/day
    -- was RETIRED as the dominant source of REE_assembly history bloat, and
    says not to reintroduce it. Not writing at all is strictly better than
    writing-then-not-committing: it leaves no ` M` for the next session to
    wonder about, and no autostash payload.

    Semantics change, stated plainly: a skipped file keeps its OLD stamp, so
    `Generated:` now means "when this index's CONTENT last changed" rather than
    "when a regen last ran". That is the more useful of the two readings and
    the only consumer that parses a stamp for freshness
    (verify_governance_cycle.py) reads pending_review.md, which is written by a
    different function and is deliberately NOT routed through this helper.

    Failure direction is deliberately asymmetric: any trouble reading the
    existing file (absent, unreadable, undecodable) falls through to WRITING.
    A regen must never be silently suppressed by a bad read -- the worst case
    of writing is the status quo ante, one dirty file.
    """
    try:
        existing = path.read_text(encoding="utf-8")
    except (OSError, ValueError):
        _atomic_write_text(path, text)
        return True
    if _strip_generated_stamp(existing) == _strip_generated_stamp(text):
        return False
    _atomic_write_text(path, text)
    return True


# The JSON artifacts carry the same run stamp under these keys. Only whole-run
# stamps belong here -- a per-item timestamp (`timestamp_utc` on a decision
# entry, `assigned_at`) is CONTENT and must stay comparable.
_JSON_RUN_STAMP_KEYS = {"generated_at_utc", "generated_at"}


def _strip_json_run_stamps(obj):
    """`obj` with every _JSON_RUN_STAMP_KEYS key removed, recursively."""
    if isinstance(obj, dict):
        return {k: _strip_json_run_stamps(v) for k, v in obj.items()
                if k not in _JSON_RUN_STAMP_KEYS}
    if isinstance(obj, list):
        return [_strip_json_run_stamps(v) for v in obj]
    return obj


def _write_json_if_material(path: Path, text: str) -> bool:
    """JSON counterpart of `_write_index_if_material` -- same rationale.

    Applied only to the artifacts MEASURED to churn on the stamp alone
    (2026-08-08, ree-cloud-5): `decision_state.v1.json` and
    `arm_fingerprint_index.json`. That is not a cosmetic pair --
    `evidence/decisions/decision_state.v1.json` is the exact path
    ree_git_sync_repair.sh named in its 2026-08-08T06:14:13Z refusal
    ("REE_assembly NEEDS_HUMAN ... uncommitted non-telemetry change:
    evidence/decisions/decision_state.v1.json"), so this one file was on its own
    enough to keep the auto-repair permanently disarmed.

    Everything else the builder writes under `evidence/planning/` was measured
    to carry REAL content changes alongside its stamp, so gating those would buy
    nothing and only add a way to suppress a genuine write.

    Compared as PARSED JSON, not as text: the writer re-serialises with
    `sort_keys=True`, so a textual compare would be at the mercy of dict
    ordering. Fails OPEN in both directions -- an unreadable or unparseable
    side falls through to writing, because a regen must never be suppressed by
    a comparison this function could not actually make.
    """
    try:
        existing = path.read_text(encoding="utf-8")
        old_obj = json.loads(existing)
        new_obj = json.loads(text)
    except (OSError, ValueError):
        _atomic_write_text(path, text)
        return True
    if _strip_json_run_stamps(old_obj) == _strip_json_run_stamps(new_obj):
        return False
    _atomic_write_text(path, text)
    return True


# Statuses _evaluate_runs actually branches on. Anything else a manifest carries
# in `status` (PARTIAL_*, INCONCLUSIVE, INCONCLUSIVE_UNDERTRAINED, MIXED,
# SUPERSEDED, DIAGNOSTIC_COMPLETE, N/A, ...) falls through that function's
# terminal `else` and becomes final_status="PASS".
_DERIVED_STATUSES = ("PASS", "FAIL", "ERROR", "UNKNOWN")


def _display_status(run: "RunRecord") -> str:
    """Status cell for the INDEX.md tables -- DISPLAY ONLY.

    `final_status` is the pipeline's derived VERDICT and is deliberately coarse:
    _evaluate_runs collapses every status string it does not branch on into
    "PASS" (its terminal `else`). For a rendered table that silently loses
    information -- a run whose manifest says PARTIAL_NO_CANCEL, INCONCLUSIVE or
    MIXED reads as a clean pass. Confirmed 2026-08-08 on
    v3_exq_162_mech137_commit_token_structure (manifest PARTIAL_NO_CANCEL,
    INDEX.md row "PASS"); 34 of the corpus's 37 non-standard-status runs were
    rendering as PASS. Same defect family as the 2026-08-02 ERROR-as-PASS fix in
    _evaluate_runs, one status class further out.

    So: render the derived verdict whenever one was genuinely derived (FAIL from
    stop-criteria / adapter contract / manifest, or ERROR/UNKNOWN propagated
    through), and otherwise fall back to the manifest's own status string rather
    than the "PASS" it was collapsed into.

    This deliberately does NOT touch `final_status` itself. That field feeds
    scoring, evidence-direction inference and claim_evidence.v1.json, where
    widening it would reclassify those 34 runs' evidence direction -- a
    governance change, not a display fix.
    """
    if run.final_status == "FAIL":
        return f"**{run.final_status}**"
    if run.final_status == "PASS" and run.manifest_status not in _DERIVED_STATUSES:
        return run.manifest_status or run.final_status
    return run.final_status


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
            status = _display_status(run)
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
            summary_rel = _relpath_or_fallback(run.summary_path, experiment_dir)
            metrics_rel = _relpath_or_fallback(run.metrics_path, experiment_dir)
            manifest_rel = _relpath_or_fallback(run.manifest_path, experiment_dir)
            adapter_rel = (
                _relpath_or_fallback(run.adapter_signals_path, experiment_dir)
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
    _write_index_if_material(experiment_dir / "INDEX.md", "\n".join(lines).rstrip() + "\n")


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
        # Same display-only rule as the per-experiment table -- see
        # _display_status. `fails` above still counts final_status == "FAIL",
        # which is the derived verdict and is unchanged.
        latest_status_rendered = _display_status(latest) if latest else "n/a"
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

    _write_index_if_material(base_dir / "INDEX.md", "\n".join(lines).rstrip() + "\n")


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
    _write_index_if_material(literature_root / "INDEX.md", "\n".join(lines).rstrip() + "\n")


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


# Cross-epoch / cross-canonical-profile aggregation guard (2026-08-12). See
# REE_assembly/evidence/planning/architecture_epoch_investigation.md Sections
# 4, 10, 11: no comparison/plotting/aggregation tool anywhere in the project
# refused or even flagged when results from different architecture_epoch (or,
# now that it exists, canonical_profile_hash) values were pooled together for
# a single claim's confidence/conflict scoring. `architecture_epoch` today is
# a coarse generation tag (V2 and V3 currently share one string, so
# epoch-based filtering is presently a no-op between those two generations --
# see Section 1); `canonical_profile_hash` is a finer-grained, content-hashed
# identity of which curated organism bundle (if any) built a run's config
# (Section 8). Pooling scored evidence across either boundary silently
# compares results from what may be materially different organisms.
#
# ADDITIVE ONLY: this never sets scoring_excluded and never touches
# confidence/conflict computation, which is already finalized by the time
# this runs (over `claim_to_entries`, the exact same already-scored
# population `_summarize_claim_entries` consumes). It only WARNS (stdout) and
# attaches a `cross_epoch_pooling` finding to the claim's summary dict for
# downstream visibility -- a claim is never excluded, demoted, or
# reclassified by this guard on its own.
#
# Annotation convention (Section 11's "explicit cross-epoch comparison
# annotation", designed here since none existed): a claim is exempt from the
# WARNING (the finding is still recorded, with annotated_intentional=True)
# when EITHER (a) `claims.yaml` declares
# `intentional_cross_epoch_comparison: true` under that claim id (parsed by
# _load_claim_registry; absent on every existing entry today, so this is a
# no-op against the current registry), OR (b) the claim id is passed via the
# `--allow-cross-epoch-claim` CLI flag for a one-off, non-claims.yaml-editing
# override. Both exist for the deliberate "does mechanism X's effect
# replicate under the new profile" comparison Section 11 names.
def _detect_cross_epoch_pooling(
    claim_id: str,
    entries: list[dict[str, Any]],
    claim_registry: "dict[str, dict[str, str]] | None" = None,
    allow_claims: "set[str] | None" = None,
) -> "dict[str, Any] | None":
    """Detect (and, unless annotated, warn about) mixed-epoch/-profile pooling.

    `entries` must be the SCORED entries for this claim (i.e. claim_to_entries
    entries, which already exclude every scoring_excluded branch) -- this
    deliberately does not re-derive that filter so it can never disagree with
    what actually fed confidence/conflict.

    Returns None when the claim's scored evidence is epoch/profile-uniform
    (including when every entry omits the field entirely, e.g. an all-literature
    claim or a pre-Recording-Standard corpus) -- so a normal, single-organism
    claim gets no new key at all and legacy output stays byte-identical.
    """
    epochs = sorted({
        str(e["architecture_epoch"]) for e in entries if e.get("architecture_epoch")
    })
    profiles = sorted({
        str(e["canonical_profile_hash"]) for e in entries if e.get("canonical_profile_hash")
    })
    cross_epoch = len(epochs) > 1
    cross_profile = len(profiles) > 1
    if not (cross_epoch or cross_profile):
        return None

    annotated = bool(allow_claims) and claim_id in allow_claims
    if not annotated and claim_registry:
        meta = claim_registry.get(claim_id) or {}
        annotated = _coerce_bool(meta.get("intentional_cross_epoch_comparison", ""))

    finding: dict[str, Any] = {
        "architecture_epoch_values": epochs if cross_epoch else [],
        "canonical_profile_hash_values": profiles if cross_profile else [],
        "annotated_intentional": annotated,
    }

    if not annotated:
        spans = []
        if cross_epoch:
            spans.append(f"architecture_epoch={epochs}")
        if cross_profile:
            spans.append(f"canonical_profile_hash={profiles}")
        print(
            f"  WARNING: {claim_id} pools SCORED evidence across "
            f"{' and '.join(spans)} -- results from different organisms are "
            f"being aggregated toward this claim's confidence/conflict without "
            f"an explicit cross-epoch annotation. Add "
            f"'intentional_cross_epoch_comparison: true' under {claim_id} in "
            f"claims.yaml, or pass --allow-cross-epoch-claim {claim_id}, if this "
            f"pooling is deliberate."
        )

    return finding


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
    claim_registry: dict[str, dict[str, str]] | None = None,
    allow_cross_epoch_claims: set[str] | None = None,
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
            if run.final_status in ("ERROR", "UNKNOWN"):
                # A crash-before-manifest / synthetic runner record: claim_ids is
                # always empty for these by construction, so every one of them
                # used to land here and get indexed with (before the final_status
                # fix above) a bogus "PASS" status, or (after that fix, without
                # this guard) a correctly-labelled but still-INDEXED "ERROR"/
                # "UNKNOWN" status. Either way, being indexed at all is the
                # second half of the bug: generate_pending_review.py's
                # load_error_manifests() explicitly skips any run_id present in
                # claim_evidence.v1.json (entries OR unlinked_runs) on the
                # documented assumption that "ERROR records carry no claim tags,
                # so they are never indexed" -- so an indexed ERROR run is
                # invisible to BOTH the PASS/FAIL sections (status isn't PASS/
                # FAIL) AND the ERROR-manifest section (already indexed),
                # vanishing from pending_review.md entirely. Confirmed 2026-08-02
                # on V3-EXQ-870 (v3_v3_exq_870_runner_error_20260802T105035Z_v3).
                # Leaving it OUT of claim_evidence keeps that assumption true and
                # lets load_error_manifests() pick it up directly from the raw
                # on-disk manifest, which is the path actually designed to
                # surface it and route it to /diagnose-errors.
                continue
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
            if run.canonical_profile:
                unlinked_entry["canonical_profile"] = run.canonical_profile
            if run.canonical_profile_hash:
                unlinked_entry["canonical_profile_hash"] = run.canonical_profile_hash
            # z_goal-stream liveness: surfaced, never scored. Unlinked runs get it
            # too -- a substrate-readiness diagnostic that tags no claim is exactly
            # the shape both confirmed defects took (V3-EXQ-830 was caught only by
            # its own ad-hoc readiness gate), so omitting it here would blind the
            # surface to its likeliest carrier.
            if run.z_goal_stream:
                unlinked_entry["z_goal_stream"] = run.z_goal_stream
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
            # Canonical-profile provenance: surfaced for queryability AND consumed
            # (alongside architecture_epoch above) by the cross-epoch aggregation
            # guard below. NOT scored on its own.
            if run.canonical_profile:
                entry["canonical_profile"] = run.canonical_profile
            if run.canonical_profile_hash:
                entry["canonical_profile_hash"] = run.canonical_profile_hash
            # z_goal-stream liveness: surfaced for queryability only. Emitted
            # verbatim and ONLY when the run measured it, so an absent key means
            # UNMEASURED and legacy entries stay byte-identical. It deliberately
            # does not appear in any of the scoring_excluded branches below -- a
            # dead z_goal stream is a fact about the run for a reviewer to weigh,
            # not a machine verdict that vacates it.
            if run.z_goal_stream:
                entry["z_goal_stream"] = run.z_goal_stream
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

    # Per-paper duplicate detection (GFLAG-0032 / GFLAG-0030). Grouped once,
    # up front, over every literature record regardless of claim -- a paper
    # legitimately cited for two DIFFERENT claims must still count once PER
    # CLAIM, so the exclusion below is keyed on (claim_id, paper_group), not
    # on paper_group alone. See _group_literature_by_paper for the routes.
    literature_paper_group, literature_paper_routes = _group_literature_by_paper(lit_entries)
    # (claim_id, paper_group) -> "literature_type/entry_id" of the entry kept.
    # lit_entries is already sorted (timestamp, literature_type, entry_id)
    # above, so "first seen" here is deterministically the EARLIEST review of
    # that paper for that claim -- matching the framing already used in
    # evidence/planning/literature_duplicate_entries_2026-08-14.md ("a
    # surplus evidence item is one entry BEYOND THE FIRST"). Nothing about
    # any entry's own recorded confidence/evidence_direction is overwritten
    # or averaged -- every entry keeps exactly what it says; only whether it
    # counts toward claim_to_entries (and therefore confidence/conflict)
    # changes.
    _seen_claim_paper: dict[tuple[str, int], str] = {}

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

        paper_group = literature_paper_group.get((lit.literature_type, lit.entry_id))

        for claim_id in lit.claim_ids_tested:
            entry = {
                "claim_id": claim_id,
                "source_type": "literature",
                "experiment_type": lit.literature_type,
                "run_id": lit.entry_id,
                "timestamp_utc": lit.timestamp_raw,
                "status": "SOURCE",
                "evidence_class": _prefix_class("literature", lit.evidence_class),
                "evidence_direction": lit.evidence_direction_per_claim.get(
                    claim_id, lit.evidence_direction
                ),
                "confidence": lit.confidence,
                "confidence_rationale": lit.confidence_rationale,
                "failure_signatures": lit.failure_signatures,
            }
            if lit.architecture_epoch:
                entry["architecture_epoch"] = lit.architecture_epoch
            matrix["entries"].append(entry)

            # Literature entries are not epoch-filtered, but ARE deduplicated
            # per (claim, paper) here -- GFLAG-0032. A duplicate is not a
            # defect in either record (both can be legitimate, independently
            # authored reviews); the double-count is a property of how
            # claim_to_entries is assembled, not of the corpus, so the fix
            # lives at this join point rather than editing records. The
            # excluded entry stays in matrix["entries"] (full audit log,
            # above) with its own confidence/direction untouched -- only its
            # contribution to this claim's scored evidence is withheld.
            dup_key = (claim_id, paper_group)
            if paper_group is not None and dup_key in _seen_claim_paper:
                entry["scoring_excluded"] = "duplicate_literature_entry"
                entry["duplicate_of"] = _seen_claim_paper[dup_key]
                routes = literature_paper_routes.get(paper_group)
                if routes:
                    entry["duplicate_route"] = routes
                continue
            if paper_group is not None:
                _seen_claim_paper[dup_key] = f"{lit.literature_type}/{lit.entry_id}"

            claim_to_entries[claim_id].append(entry)

    now = _parse_timestamp_only(generated_at)
    for claim_id in sorted(claim_to_entries.keys()):
        summary = _summarize_claim_entries(claim_to_entries[claim_id], now)
        if summary:
            cross_epoch_pooling = _detect_cross_epoch_pooling(
                claim_id, claim_to_entries[claim_id],
                claim_registry=claim_registry,
                allow_claims=allow_cross_epoch_claims,
            )
            if cross_epoch_pooling:
                summary["cross_epoch_pooling"] = cross_epoch_pooling
            matrix["claims"][claim_id] = summary

    matrix["entries"].sort(
        key=lambda e: (e["timestamp_utc"], e["claim_id"], e["experiment_type"], e["run_id"])
    )
    matrix["unlinked_runs"].sort(
        key=lambda e: (e["timestamp_utc"], e["source_type"], e["experiment_type"], e["run_id"])
    )

    _atomic_write_text(
        base_dir / "claim_evidence.v1.json",
        json.dumps(matrix, indent=2, sort_keys=True) + "\n",
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

    _atomic_write_text(base_dir / "TODOs.md", "\n".join(lines).rstrip() + "\n")


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

    intentional_cross_epoch_comparison (2026-08-12): exempts a claim from the
    cross-epoch aggregation guard's WARNING (see _detect_cross_epoch_pooling)
    when its scored evidence deliberately spans more than one
    architecture_epoch or canonical_profile_hash. Absent on every claim today.
    """
    registry: dict[str, dict[str, str]] = {}
    current_id: str | None = None
    current_status: str | None = None
    current_type: str | None = None
    current_invariant_type: str | None = None
    current_epistemic_category: str | None = None
    current_v3_pending: bool = False
    current_diagnostic_evidence_adjudicated: bool = False
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
    # Cross-epoch aggregation guard annotation (2026-08-12) -- see
    # _detect_cross_epoch_pooling. Absent on every existing entry today, so
    # this is a no-op against the current registry.
    current_intentional_cross_epoch: bool = False
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
                    "instantiates": current_instantiates or "",
                    "epistemic_category": current_epistemic_category or "",
                    "v3_pending": str(current_v3_pending),
                    "diagnostic_evidence_adjudicated": str(current_diagnostic_evidence_adjudicated),
                    "implementation_phase": current_impl_phase or "",
                    "evidence_quality_note": (current_eq_note or "").strip(),
                    "defer_promotion_until": current_defer_until or "",
                    "heterogeneity_note": (current_het_note or "").strip(),
                    "assembly_state": current_assembly_state or "",
                    "awaiting": current_awaiting or "",
                    "assembly_status": current_assembly_status or "",
                    "revisit_after": current_revisit_after or "",
                    "intentional_cross_epoch_comparison": str(current_intentional_cross_epoch),
                }
            current_id = line.split(":", 1)[1].strip()
            current_status = None
            current_type = None
            current_invariant_type = None
            current_instantiates = None
            current_epistemic_category = None
            current_v3_pending = False
            current_diagnostic_evidence_adjudicated = False
            current_impl_phase = None
            current_eq_note = None
            current_defer_until = None
            current_het_note = None
            current_assembly_state = None
            current_awaiting = None
            current_assembly_status = None
            current_revisit_after = None
            current_intentional_cross_epoch = False
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

        # `instantiates` names the PARENT claim this one is an instantiation of
        # (e.g. "instantiates: SD-033c"). It is a scalar in every one of its 23
        # occurrences as of 2026-08-26 -- never a list -- so it is parsed with the
        # same single-value + inline-comment handling as its siblings above.
        # Consumed by _build_instantiating_children() to give a design_decision
        # parent visibility into the evidence its children carry; see the
        # "sub-case B" branch in _write_planning_outputs.
        if current_id and line.startswith("  instantiates:"):
            current_instantiates = _strip_inline_yaml_comment(
                line.split(":", 1)[1]
            ).strip("\"'")
            continue

        if current_id and line.startswith("  epistemic_category:"):
            current_epistemic_category = _strip_inline_yaml_comment(line.split(":", 1)[1])
            continue

        if current_id and line.startswith("  v3_pending:"):
            val = _strip_inline_yaml_comment(line.split(":", 1)[1]).lower()
            current_v3_pending = val in ("true", "yes", "1")
            continue

        # Set explicitly by /failure-autopsy at the point it confirms a
        # diagnostic-purpose run's finding into this claim's evidence_quality_note
        # narrative (SD-099/MECH-489 fix shape 1 -- see
        # evidence/planning/design_decision_evidence_credit_gap_20260821.md).
        # Consumed in _write_planning_outputs to suppress missing_experimental_evidence
        # / lit_only_above_cap when exp_count == 0 but the zero is already adjudicated,
        # not merely un-looked-at.
        if current_id and line.startswith("  diagnostic_evidence_adjudicated:"):
            val = _strip_inline_yaml_comment(line.split(":", 1)[1]).lower()
            current_diagnostic_evidence_adjudicated = val in ("true", "yes", "1")
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

        if current_id and line.startswith("  intentional_cross_epoch_comparison:"):
            val = _strip_inline_yaml_comment(line.split(":", 1)[1]).lower()
            current_intentional_cross_epoch = val in ("true", "yes", "1")
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
            "instantiates": current_instantiates or "",
            "epistemic_category": current_epistemic_category or "",
            "v3_pending": str(current_v3_pending),
            "diagnostic_evidence_adjudicated": str(current_diagnostic_evidence_adjudicated),
            "implementation_phase": current_impl_phase or "",
            "evidence_quality_note": (current_eq_note or "").strip(),
            "defer_promotion_until": current_defer_until or "",
            "heterogeneity_note": (current_het_note or "").strip(),
            "assembly_state": current_assembly_state or "",
            "awaiting": current_awaiting or "",
            "assembly_status": current_assembly_status or "",
            "revisit_after": current_revisit_after or "",
            "intentional_cross_epoch_comparison": str(current_intentional_cross_epoch),
        }
    return registry


def _build_instantiating_children(
    claim_registry: dict[str, dict[str, str]],
) -> dict[str, list[str]]:
    """Map a PARENT claim id -> sorted ids of claims declaring `instantiates: <parent>`.

    A `design_decision` claim is frequently validated NOT by a run tagged against
    its own id, but by the mechanism claims that instantiate it. Before 2026-08-26
    nothing in this file read `instantiates` at all, so that relationship was
    invisible to the why_now / auto-proposal layer and such a parent was either
    silently skipped (no claim_meta -> the `continue` in _write_planning_outputs)
    or told it was missing experimental evidence it structurally cannot hold.

    Deliberately NOT a general graph: only the direct parent->child edge is built,
    because that is the only edge the sub-case B branch consumes. As of 2026-08-26
    exactly 9 parents are referenced fleet-wide, 6 of them design_decision.
    """
    children: dict[str, list[str]] = {}
    for child_id, meta in claim_registry.items():
        parent = str(meta.get("instantiates", "") or "").strip()
        if not parent or parent == child_id:
            continue
        children.setdefault(parent, []).append(child_id)
    for kids in children.values():
        kids.sort()
    return children


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
# derivation, or policy rather than by a REE experiment. (answer_state is
# intentionally NOT here -- it keeps its own recommendation handling in
# _recommendation_for_claim. The substrate_* categories previously shared that
# "intentionally NOT here" note too, but that was a bug, not a design choice:
# _recommendation_for_claim's handling of substrate_conditional/substrate_ceiling
# only ever suppresses promote/demote GOVERNANCE recommendations -- it has no
# path back into the EXP-* proposal-eligibility gate below, which is a wholly
# separate call site (the backlog dispatcher). See _PROBE_GATED_EPISTEMIC_
# CATEGORIES for the fix.)
_NON_EXPERIMENTAL_EPISTEMIC_CATEGORIES = {
    "out_of_domain",
    "derivational",
    "governance_rule",
}

# substrate_conditional / substrate_ceiling: EXPLICIT-only categories meaning
# "no build-relevant action is available until an upstream probe/substrate
# lands" (REE_assembly/CLAUDE.md "Epistemic categories"). Neither is
# REE-experiment-testable right now by definition -- substrate_conditional's
# upstream dependency is planned but not yet built, and substrate_ceiling's
# documented remedy is substrate enrichment, "not more experiments on the
# existing substrate". A claim in either category must not seed an EXP-*
# proposal even though it may still be perfectly fine to route to /lit-pull
# (the literature-proposal branch is untouched by this gate).
_PROBE_GATED_EPISTEMIC_CATEGORIES = {
    "substrate_conditional",
    "substrate_ceiling",
}


def _is_deferred_to_later_generation(registry_meta: "dict[str, Any] | None") -> bool:
    """True when a claim is v3_pending AND implementation_phase names a
    generation >= v4 -- i.e. deliberately deferred to a later architecture
    generation by an explicit commitment, not merely awaiting V3 substrate
    readiness (that narrower case is implementation_phase == "v3" with no V3
    runs yet, handled separately by the hold_pending_v3_substrate branch).

    Shared by _recommendation_for_claim's held_v4_by_architectural_commitment
    gate and _is_experiment_ineligible_claim below, so both call sites
    recognize the same signal instead of drifting apart.
    """
    if not registry_meta:
        return False
    v3_pending = str(registry_meta.get("v3_pending", "False")).strip().lower() in ("true", "yes", "1")
    impl_phase = str(registry_meta.get("implementation_phase", "")).strip().lower()
    later_gen = re.fullmatch(r"v(\d+)", impl_phase)
    return bool(v3_pending and later_gen and int(later_gen.group(1)) >= 4)


def _is_experiment_ineligible_claim(registry_meta: dict[str, Any]) -> bool:
    """True when a claim must not seed an experimental (EXP-*) proposal.

    Four independent reasons (any one suffices):
      * registry_meta is empty -- the claim_id has no claims.yaml entry at all
        (claim_registry.get(claim_id, {}) fell through to the default; a real
        parsed entry always carries status/claim_type keys, even blank, so an
        empty dict is unambiguously "not registered"). There is no claims.yaml
        disposition to test, so no targeted experiment can be proposed against
        it -- this is a data-hygiene gap (dead/renamed claim_id), not a
        substrate-readiness one.
      * the claim status is answered/closing (a REE run cannot move it),
      * its resolved epistemic_category is one settled outside REE experiments
        (literature / derivation / policy), or explicitly probe-gated
        (substrate_conditional / substrate_ceiling -- see
        _PROBE_GATED_EPISTEMIC_CATEGORIES), or
      * the claim is deliberately deferred to a later generation (v3_pending
        + implementation_phase >= v4 -- see _is_deferred_to_later_generation).

    Warn-safe: missing/blank fields on a REGISTERED claim resolve to eligible
    (False) so absent metadata never silently suppresses a genuine proposal --
    only a wholly-missing registry entry, or an explicit deferral signal,
    suppresses. Uses _resolve_epistemic_category so an inferred answer_state
    (open_question default) is handled by the status rule, not mis-skipped
    here.
    """
    if not isinstance(registry_meta, dict):
        return False
    if not registry_meta:
        return True
    status = str(registry_meta.get("status", "")).strip().lower()
    if status in _ANSWERED_OR_CLOSING_CLAIM_STATUSES:
        return True
    epistemic_category = _resolve_epistemic_category(
        str(registry_meta.get("claim_type", "")),
        str(registry_meta.get("invariant_type", "")),
        str(registry_meta.get("epistemic_category", "")),
    )
    if epistemic_category in _NON_EXPERIMENTAL_EPISTEMIC_CATEGORIES:
        return True
    if epistemic_category in _PROBE_GATED_EPISTEMIC_CATEGORIES:
        return True
    return _is_deferred_to_later_generation(registry_meta)


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
    _write_json_if_material(
        decisions_dir / "decision_state.v1.json",
        json.dumps(state, indent=2, sort_keys=True) + "\n",
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
    # (_is_deferred_to_later_generation is the shared helper -- also consulted by
    # _is_experiment_ineligible_claim so the EXP-* proposal gate recognizes the
    # same signal.)
    if _is_deferred_to_later_generation(registry_meta):
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

    _atomic_write_text(
        base_dir / "promotion_demotion_recommendations.md",
        "\n".join(lines).rstrip() + "\n",
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

    _atomic_write_text(
        base_dir / "conflicts.md",
        "\n".join(lines).rstrip() + "\n",
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
    # `matrix["entries"]` with source_type=="experimental" are built exclusively
    # from _scan_runs() over completed run manifests (see the entry-construction
    # loop above, ~line 2569) -- every such entry's `experiment_type` therefore
    # names a SPECIFIC, ALREADY-EXECUTED ree-v3/experiments/<type>.py script
    # (convention: v3_exq_NNN_description), not a reusable experiment class.
    # A prior version returned the most-common historical experiment_type here
    # as the "suggestion" for this claim's next experiment -- which is always
    # literally the name of a script that has already run and already produced
    # the evidence being counted. Confirmed 2026-08-02: 35/35 medium-priority
    # proposals hit this fallback and proposed re-running an already-completed
    # script with a completed run pack on disk. There is no reusable signal to
    # extract from `matrix` here, so always hand back the generic placeholder --
    # same as the no-history case -- and leave naming the real next probe to a
    # human / `/queue-experiment` session.
    return f"claim_probe_{claim_id.lower().replace('-', '_')}"


def _suggest_literature_type(claim_id: str, matrix: dict[str, Any]) -> str:
    # Same defect as _suggest_experiment_type above: literature_type values are
    # one-off review identifiers (evidence/literature/<literature_type>/, e.g.
    # `targeted_review_q_088`) naming ONE ALREADY-WRITTEN review for this exact
    # claim, not a reusable category. Returning the historical value verbatim
    # suggests re-running an already-completed literature pull into its own
    # directory. Confirmed live 2026-08-02 (LIT-0483, Q-088: suggested
    # `targeted_review_q_088`, which already has a populated entries/ dir).
    # Always fall back to the generic placeholder.
    return f"targeted_review_{claim_id.lower().replace('-', '_')}"


def _proposal_identity_keys(item: dict[str, Any]) -> list[str]:
    """Every identifier this proposal is known by, backlog_id first.

    backlog_id (EVB-NNNN) is preferred where present -- every auto-generated
    proposal carries one, minted once and carried forward by claim_id (see
    the "Persistent ID assignment" block in main()). proposal_id
    (EXP-/LIT-NNNN) is the fallback for a proposal with no backlog_id, or a
    SECOND match candidate during the transition onto one.

    A single preferred key is not enough to match an OLD record against a
    FRESH item across that transition: the very first regen after a manual
    proposal is minted a backlog_id changes its preferred key from
    proposal_id to backlog_id, while the existing on-disk record was written
    under proposal_id (the only key it had at the time). A single-key lookup
    misses that match -- confirmed empirically 2026-08-02 running the
    newly-minted-backlog_id fix against the (not-yet-regenerated) live
    experiment_proposals.v1.json: MECH-426/427/INV-087 each came back as TWO
    rows, a fresh "proposed" one plus a stale-but-correct one preserved by
    the "historical resolution" re-append safety net -- not silent data
    loss, but not a clean carry-forward either. Returning BOTH keys (when
    both are present) and trying each in turn closes that transitional gap
    without weakening steady-state behaviour (once backlog_id is stable,
    proposal_id is just a redundant second hit).
    """
    keys: list[str] = []
    _bid = str(item.get("backlog_id") or "").strip()
    if _bid:
        keys.append(_bid)
    _pid = str(item.get("proposal_id") or "").strip()
    if _pid and _pid not in keys:
        keys.append(_pid)
    return keys


def _proposal_lane(item: dict[str, Any]) -> str:
    """The LANE half of a proposal's identity key, normalised.

    `backlog_id` is stable but NOT unique: one EVB legitimately backs two
    proposals on the same claim, an `experimental` one and a
    `literature_review` twin (measured 2026-09-02 over the live 1150 items:
    915 distinct backlog_ids, 234 duplicate groups). Keying the status
    carry-forward on the identity key ALONE therefore collapses those two
    onto one dict slot, and whichever record is read second wins -- so a
    resolved EXPERIMENTAL proposal's status is carried onto its LITERATURE
    twin, and vice versa.

    That is not hypothetical. SEVEN literature reviews were found carrying
    `status: blocked_substrate` with a byte-identical `blocked_by` /
    `blocked_note` copied from their experimental twin: EVB-1185, -1398,
    -1401, -1408, -1583, -1585 and -1595. A literature review is never
    blocked by absent V3 substrate -- the papers can be read whatever the
    substrate does -- so those seven were suppressed from the workset for no
    valid reason. (First stated as six on 2026-09-02 from a hand-listed set;
    the re-derivation the repair chip performs found EVB-1595 as well, which
    is why that chip re-derives rather than trusting a list. EVB-1185's pair
    carries `blocked_by: []`, so there the bled field is `blocked_note` only.)

    NORMALISATION IS LOAD-BEARING, not tidiness: manual_proposals.v1.json
    spells the lane `literature` (12 items) while the generated file spells
    it `literature_review` (523 items). Without collapsing the two, a manual
    literature proposal's resolution would stop carrying forward the moment
    this key went in -- turning a cross-lane bleed into a silent wipe, which
    is the strictly worse direction.
    """
    _t = str(item.get("proposal_type") or "").strip()
    if _t.startswith("literature"):
        return "literature"
    return _t or "?"


def lookup_existing_proposal_status(
    item: dict[str, Any],
    status_map: dict[tuple[str, str], dict],
    lanes_by_key: dict[str, set[str]],
) -> dict | None:
    """Resolved status carried forward for `item`, matched on (identity key, LANE).

    Falls back to a lane-agnostic match ONLY where the identity key is
    unambiguous (exactly one lane registered under it). That fallback is what
    preserves the transitional behaviour _proposal_identity_keys documents --
    an old record written under proposal_id before its backlog_id was minted,
    or a lane spelling that changed -- while still refusing the EXP/LIT twin
    collision, where two lanes share one key and a lane-agnostic match IS the
    bug. Module-level (rather than a closure over main()'s two dicts) so the
    twin collision has a direct regression test.
    """
    lane = _proposal_lane(item)
    for k in _proposal_identity_keys(item):
        hit = status_map.get((k, lane))
        if hit is not None:
            return hit
        # Lane-agnostic fallback, deliberately narrow: it fires ONLY when a
        # lane is genuinely UNKNOWN on one side, never merely because the key
        # happens to be unambiguous today. An unambiguous key is exactly the
        # shape the original bleed had -- the experimental twin resolved while
        # its literature twin was still "proposed", so only one lane was
        # registered -- so gating on ambiguity would leave the bug in place.
        # Two KNOWN, DIFFERENT lanes never match, however few are registered.
        lanes = lanes_by_key.get(k)
        if lanes and len(lanes) == 1:
            only = next(iter(lanes))
            if lane == "?" or only == "?":
                return status_map.get((k, only))
    return None


# Status-family fields carried forward from an existing (pre-regen) resolved
# proposal onto its freshly-regenerated counterpart (and written back onto
# manual_proposals.v1.json -- both sites in main() share this same set via
# _existing_proposal_status). Generated proposals always start "proposed";
# any manual resolution -- executed, gated, superseded, or a Step 2.5
# blocked_substrate stop with its reason -- must be in this tuple or it is
# silently wiped on the next regen. blocked_by/blocked_note added
# 2026-08-18 (chip-20260817-blocked-note-not-carried-forward): the
# /queue-experiment skill instructs authors to write both on a
# blocked_substrate stop, but neither field survived a regen, so 43 live
# blocked_substrate proposals had already lost their reason by the time this
# was found.
_PROPOSAL_STATUS_CARRY_FORWARD_FIELDS = (
    "status",
    "executed_by",
    "executed_queue_id",
    "gated_at_utc",
    "gated_by_session",
    "gating_reason",
    "predecessor_disposition",
    "release_condition",
    "superseded_by",
    "blocked_by",
    "blocked_note",
)


def _reserve_manual_proposal_backlog_ids(
    manual_doc: dict[str, Any], used_numeric_ids: set[int]
) -> None:
    """Fold manual_proposals.v1.json's own EVB-NNNN ids into the shared
    reservation set so the auto-backlog minting loop (which only scans
    evidence_backlog.v1.json) can never hand out a number a manual proposal
    already owns. Mutates used_numeric_ids in place, matching the existing
    caller-side convention.
    """
    for _mp_item in manual_doc.get("items", []):
        if not isinstance(_mp_item, dict):
            continue
        _mp_bid = str(_mp_item.get("backlog_id", "")).strip()
        _m = re.fullmatch(r"EVB-(\d{4,})", _mp_bid)
        if _m:
            used_numeric_ids.add(int(_m.group(1)))


def _mint_missing_manual_backlog_ids(
    manual_doc: dict[str, Any], next_idx: int
) -> tuple[bool, int]:
    """Assign a stable EVB-NNNN to every manual proposal that lacks one.

    Mutates manual_doc's items in place. Idempotent: an item that already
    carries a backlog_id (including one minted by a prior call) is left
    untouched, so calling this again on the same doc with the same next_idx
    is a no-op (changed=False) -- the property the carry-forward regression
    test relies on. Returns (changed, next_idx_after) so the caller can
    decide whether to persist manual_doc and can keep allocating from a
    single shared counter.
    """
    changed = False
    for mp in manual_doc.get("items", []):
        if isinstance(mp, dict) and mp.get("proposal_id"):
            if not str(mp.get("backlog_id", "")).strip():
                mp["backlog_id"] = f"EVB-{next_idx:04d}"
                next_idx += 1
                changed = True
    return changed, next_idx


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
    dormant_high_conflict_ratio = float(
        thresholds.get("dormant_high_conflict_ratio", 0.55)
    )
    dormant_high_conflict_min_entries = max(
        1, int(thresholds.get("dormant_high_conflict_min_entries", 2))
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
    # Pre-load frozen mandatory_decision_checkpoint deadlines, keyed by claim_id.
    # decision_deadline_utc must be stamped once, on the FIRST regen where the
    # mandatory-decision condition fires for a claim, and then held constant on
    # every subsequent regen while the condition stays continuously active --
    # otherwise it recomputes as generated_at_dt + N hours on every run and
    # perpetually reads "~N hours from now", so a deadline can never actually be
    # missed (confirmed 2026-08-01: 16 unrelated claims in the pre-fix
    # evidence_backlog.v1.json all shared the identical deadline timestamp,
    # which is only possible if every one was computed from "now" rather than
    # from its own first-trigger time). When a claim's checkpoint clears
    # (resolved, or the item drops out of the backlog entirely), it naturally
    # falls out of this preload on the next regen -- a later re-trigger mints a
    # fresh deadline, which is the correct "re-trigger" behavior, not a bug.
    _existing_decision_deadlines: dict[str, str] = {}
    if _early_backlog_path.exists():
        try:
            _early_doc = json.loads(_early_backlog_path.read_text(encoding="utf-8"))
            for _pit in _early_doc.get("items", []):
                if isinstance(_pit, dict) and _pit.get("pinned", False):
                    _pcid = str(_pit.get("claim_id", "")).strip()
                    if _pcid:
                        _pinned_claim_ids.add(_pcid)
                        _preloaded_pinned_items.append(dict(_pit))
                if isinstance(_pit, dict):
                    _dcid = str(_pit.get("claim_id", "")).strip()
                    _dsignals = _pit.get("signals", {})
                    _ddeadline = (
                        str(_dsignals.get("decision_deadline_utc", "")).strip()
                        if isinstance(_dsignals, dict)
                        else ""
                    )
                    if _dcid and _ddeadline:
                        _existing_decision_deadlines[_dcid] = _ddeadline
        except Exception:
            pass  # Missing or corrupt backlog — no pinned items to protect, no deadlines to freeze
    # ── end pre-load ─────────────────────────────────────────────────────────────

    backlog_items: list[dict[str, Any]] = []
    architecture_items: list[dict[str, Any]] = []
    dormant_high_conflict_items: list[dict[str, Any]] = []
    # Pseudo-claim filter: drop non-canonical claim_ids that flow in via the
    # evidence matrix (e.g. "onboarding" from contributor smoke tests). These
    # are bucket labels for instrumentation runs, not registered claims; without
    # this filter they auto-generate spurious backlog items (canonical incident:
    # phantom EVB-0131 onboarding, surfaced repeatedly in lit-pull-am scans
    # 2026-05-05..05-07). Real claims either (a) appear in claim_registry, or
    # (b) match the canonical prefix pattern and will be added to the registry
    # when fully described.
    _CANONICAL_CLAIM_RE = re.compile(r"^(INV|ARC|MECH|SD|Q|IMPL)-")
    # Parent -> instantiating children, for the design_decision sub-case B branch
    # below. Built once per regen rather than per claim: the registry is ~1050
    # entries and the loop below is already the hot path.
    _instantiating_children = _build_instantiating_children(claim_registry)
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
        # Fix shape 1 (SD-099/MECH-489, 2026-08-26): set explicitly by
        # /failure-autopsy when it confirms a diagnostic-purpose run's finding into
        # this claim's evidence_quality_note narrative. A zero exp_count that has
        # already been adjudicated this way is a settled reading, not an unlooked-at
        # gap -- see evidence/planning/design_decision_evidence_credit_gap_20260821.md.
        diagnostic_evidence_adjudicated = (
            str(registry_meta.get("diagnostic_evidence_adjudicated", "False")) == "True"
        )
        claim_entries = entries_by_claim.get(claim_id, [])
        claim_meta = _summarize_claim_entries(claim_entries, generated_at_dt) if claim_entries else None

        reasons: list[str] = []
        evidence_needed: set[str] = set()
        stage_info: dict[str, Any] = {}
        suppress_structure_signals = False
        suppress_external_precedence = False
        validated_via_instantiating_children = False
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
        recent_targeted_batches = len(_batch_keys_for_entries(decision_recent_exp_entries))
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
            elif claim_type == "design_decision" and _instantiating_children.get(claim_id):
                # ── Sub-case B: design_decision validated via instantiating children ──
                # This parent has NO evidence entry of its own -- no run or paper has
                # ever tagged its id directly -- but that is BY DESIGN, not a gap: it is
                # validated through the claims that instantiate it. Before 2026-08-26
                # this hit the bare `continue` below and vanished from the backlog and
                # proposal outputs entirely, which is indistinguishable from "not yet
                # looked at" and is strictly worse than a noisy-but-visible entry.
                #
                # We surface it with its children's AGGREGATE evidence attached, and
                # deliberately leave `evidence_needed` EMPTY so no experiment proposal
                # is generated against the parent id -- no run can be tagged against a
                # design_decision parent to clear it, so a proposal here would be
                # permanently unactionable. Visibility is the fix; a manufactured
                # proposal is not.
                #
                # Scope note (GOV-HELDOUT-1, 2026-08-26): the sibling "sub-case A"
                # fix -- suppressing missing-evidence signals on a design_decision
                # parent that DOES have a claim_meta entry when its child carries real
                # experimental evidence -- was measured and deliberately NOT built. On
                # all three real instances (SD-091, SD-099, SD-101) the child's runs are
                # themselves scoring_excluded='diagnostic_probe', so the child's
                # genuine_exp_count is 0 and the suppression could never fire. See
                # evidence/planning/design_decision_evidence_credit_gap_20260821.md.
                _child_ids = _instantiating_children[claim_id]
                _child_entries: list[dict[str, Any]] = []
                for _child_id in _child_ids:
                    _child_entries.extend(entries_by_claim.get(_child_id, []))
                _child_meta = (
                    _summarize_claim_entries(_child_entries, generated_at_dt)
                    if _child_entries
                    else None
                ) or {}
                _child_sources = _child_meta.get("source_counts", {})
                validated_via_instantiating_children = True
                reasons.append("validated_via_instantiating_children")
                signals.update(
                    {
                        "overall_confidence": 0.0,
                        "source_counts": {"experimental": 0, "literature": 0},
                        "conflict_ratio": 0.0,
                        "instantiating_children": {
                            "claim_ids": _child_ids,
                            "genuine_exp_count": int(
                                _child_meta.get("genuine_exp_count", 0)
                            ),
                            "experimental_count": int(
                                _child_sources.get("experimental", 0)
                            ),
                            "literature_count": int(_child_sources.get("literature", 0)),
                        },
                    }
                )
            else:
                # GFLAG-0054 fix (2026-09-01): a registered claim of any OTHER
                # claim_type (mechanism_hypothesis, architectural_commitment, ...)
                # with zero evidence entries used to hit this bare `continue` and
                # never enter the backlog at all -- invisible to /lit-pull's
                # worklist from the moment it was registered. See
                # governance_flags.v1.json GFLAG-0054 (MECH-464: registered
                # 2026-07-20 with a written falsifier, never routed).
                # Route it through the same missing-evidence reason vocabulary
                # used below for a claim_meta that DOES exist but is short on
                # one or both source types (exp_count==0 / lit_count==0), so the
                # reason tokens stay honest about what is actually missing
                # rather than reusing the open_question-only token above.
                if diagnostic_evidence_adjudicated:
                    _add_reason("diagnostic_evidence_adjudicated")
                else:
                    _add_reason("missing_experimental_evidence")
                    evidence_needed.add("experimental")
                _add_reason("missing_literature_evidence")
                evidence_needed.add("literature")
                signals.update(
                    {
                        "overall_confidence": 0.0,
                        "source_counts": {"experimental": 0, "literature": 0},
                        "conflict_ratio": 0.0,
                    }
                )
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
            if (
                exp_count == 0
                and literature_confidence >= lit_only_above_cap_threshold
                and not diagnostic_evidence_adjudicated
            ):
                _add_reason("lit_only_above_cap")
            if exp_count == 0:
                if diagnostic_evidence_adjudicated:
                    # Suppress the missing-evidence churn -- the zero is already
                    # adjudicated (fix shape 1), so do not re-propose an experiment
                    # that GOV-REUSE-1 already ruled out re-queuing.
                    _add_reason("diagnostic_evidence_adjudicated")
                else:
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

        # Freshness-since-decision (nag-loop fix, 2026-08-02): once a claim has
        # a recorded decision -- including a deliberate hold_* deferral, not
        # only a terminal retain/hybridize/retire outcome -- only batches that
        # landed AFTER that decision count as "fresh" for the mandatory
        # checkpoint trigger below. Without this, decision_unresolved stays
        # True forever for any hold_* recommendation (it is not a terminal
        # outcome, by design -- see allowed_conflict_outcomes), so the
        # checkpoint re-fires every regen purely because the flat trailing
        # window (recent_targeted_batches, above) still contains batches that
        # predate the decision, whether or not anything has actually changed
        # since a human looked at it. A claim with NO recorded decision keeps
        # the original trailing-window count -- there is nothing to be
        # "since", so first-time triggering is unaffected.
        mandatory_decision_fresh_batches = recent_targeted_batches
        _eff_decision_status = str(effective_decision_state.get("decision_status", "")).strip().lower()
        _eff_decision_ts_raw = str(effective_decision_state.get("timestamp_utc", "")).strip()
        if _eff_decision_status in {"applied", "approved"} and _eff_decision_ts_raw:
            try:
                _eff_decision_dt = _parse_timestamp_only(_eff_decision_ts_raw)
                _entries_since_decision = [
                    e for e in exp_entries
                    if str(e.get("timestamp_utc", "")).strip()
                    and _parse_timestamp_only(str(e["timestamp_utc"])) > _eff_decision_dt
                ]
                mandatory_decision_fresh_batches = len(_batch_keys_for_entries(_entries_since_decision))
                signals["fresh_batches_since_decision"] = mandatory_decision_fresh_batches
            except ValueError:
                pass  # Malformed decision timestamp -- fall back to the trailing-window count

        if (
            not suppress_mandatory_decision
            and
            conflict_ratio >= mandatory_decision_conflict_ratio
            and mandatory_decision_fresh_batches >= mandatory_decision_min_fresh_batches
            and decision_unresolved
        ):
            mandatory_decision_checkpoint = True
            # Freeze on first trigger: reuse the deadline already on record for this
            # claim from the prior regen (if the checkpoint was already active then),
            # rather than recomputing generated_at_dt + N hours every cycle. See the
            # _existing_decision_deadlines preload above for the full rationale.
            decision_deadline_utc = _existing_decision_deadlines.get(claim_id, "")
            if not decision_deadline_utc:
                decision_deadline_utc = (
                    generated_at_dt + timedelta(hours=mandatory_decision_deadline_hours)
                ).isoformat().replace("+00:00", "Z")
            signals["mandatory_decision_checkpoint"] = True
            signals["decision_deadline_utc"] = decision_deadline_utc
            signals["decision_required_outcomes"] = list(allowed_conflict_outcomes)
            _add_reason("mandatory_decision_checkpoint")
        elif (
            not suppress_mandatory_decision
            and claim_meta is not None
            and conflict_ratio >= dormant_high_conflict_ratio
            and entries_total >= dormant_high_conflict_min_entries
            and decision_unresolved
        ):
            # Dormant / at-risk high-conflict watchlist (blind-spot fix,
            # 2026-08-02): mandatory_decision_checkpoint only fires at
            # conflict_ratio >= mandatory_decision_conflict_ratio (0.80 by
            # default) AND with fresh recent batches -- so two classes of
            # genuinely contentious claim were previously invisible to any
            # signal at all: (a) claims nobody has run evidence against
            # recently (conflict is real but the batch floor is never met --
            # "dormant_low_activity" below), and (b) claims worked heavily
            # whose conflict never quite crosses the mandatory bar, so they
            # get reworked indefinitely without ever being forced to a
            # decision ("chronic_under_threshold" below). Deliberately NOT
            # given a decision_deadline_utc / hard SLA: forcing a decision
            # without new evidence would just reproduce the same hold, and a
            # second deadline mechanism would reintroduce the exact
            # never-actually-due failure mode the freshness fix above
            # corrects. This is a no-deadline visibility report only, kept
            # mutually exclusive with mandatory_decision_checkpoint (elif)
            # so a claim never appears in both lists at once.
            dormant_high_conflict_items.append(
                {
                    "claim_id": claim_id,
                    "current_status": current_status,
                    "conflict_ratio": round(conflict_ratio, 3),
                    "recent_targeted_batches": recent_targeted_batches,
                    "entries_total": entries_total,
                    "pattern": (
                        "chronic_under_threshold"
                        if recent_targeted_batches >= mandatory_decision_min_fresh_batches
                        else "dormant_low_activity"
                    ),
                    "latest_decision": effective_decision_state,
                }
            )

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
        # The catch-all below defaults an otherwise-empty need to "experimental".
        # A design_decision parent surfaced via sub-case B must be EXEMPT: no run is
        # ever tagged against a design_decision parent id (its children carry the
        # evidence), so the resulting proposal would be permanently unactionable and
        # would re-issue every single cycle -- precisely the proposal churn this
        # branch exists to stop. Same shape as the two guards just above.
        # diagnostic_evidence_adjudicated (fix shape 1) is exempt for the identical
        # reason: without this, the catch-all would silently re-add "experimental"
        # right after the block above deliberately left it out, re-triggering the
        # exact re-proposal churn GOV-REUSE-1 already ruled out for SD-099/MECH-489.
        if not evidence_needed and not (
            saturation_guard_engaged
            or escalate_architecture_decision
            or validated_via_instantiating_children
            or diagnostic_evidence_adjudicated
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

    # Also reserve numeric EVB-NNNN ids already assigned to manual proposals
    # (evidence/planning/manual_proposals.v1.json) -- those items are never
    # inserted into evidence_backlog.v1.json itself, so _used_numeric_ids
    # above is blind to them. Without this, the auto-backlog minting loop
    # below could hand a fresh claim the SAME EVB-NNNN a manual proposal
    # already owns (see the manual-proposal backlog_id minting further down,
    # which draws from this same numeric pool).
    _manual_proposals_path_for_reservation = planning_root / "manual_proposals.v1.json"
    if _manual_proposals_path_for_reservation.exists():
        try:
            _existing_manual_doc = json.loads(
                _manual_proposals_path_for_reservation.read_text(encoding="utf-8")
            )
            _reserve_manual_proposal_backlog_ids(_existing_manual_doc, _used_numeric_ids)
        except Exception:
            pass  # Corrupt or missing manual proposals -- skip reservation

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

    # Existing (pre-regen) resolved proposals, loaded early so their proposal_id
    # indices can be reserved below BEFORE the auto counter runs -- see the
    # reservation block immediately after. Also reused later (the carry-forward
    # and re-append-missing-resolved-items blocks) so the file is read once.
    _existing_proposal_status: dict[tuple[str, str], dict] = {}
    # identity key -> the set of lanes registered under it, so the read side can
    # tell an UNAMBIGUOUS type-agnostic match (safe: transitional records whose
    # lane spelling changed or is absent) from an AMBIGUOUS one (the EXP/LIT twin
    # collision -- must NOT match across lanes). See _proposal_lane.
    _existing_lanes_by_key: dict[str, set[str]] = {}
    _existing_proposals_doc: dict | None = None
    _existing_proposals_path = planning_root / "experiment_proposals.v1.json"
    if _existing_proposals_path.exists():
        try:
            _existing_proposals_doc = json.loads(
                _existing_proposals_path.read_text(encoding="utf-8")
            )
            for _ep in _existing_proposals_doc.get("items", []):
                _ep_keys = _proposal_identity_keys(_ep)
                if _ep_keys and _ep.get("status", "proposed") != "proposed":
                    _ep_status = {
                        k: _ep[k]
                        for k in _PROPOSAL_STATUS_CARRY_FORWARD_FIELDS
                        if k in _ep
                    }
                    # Register under EVERY identity key this OLD record carries
                    # (not just the preferred one) -- see _proposal_identity_keys.
                    _ep_lane = _proposal_lane(_ep)
                    for _ep_key in _ep_keys:
                        _existing_proposal_status[(_ep_key, _ep_lane)] = _ep_status
                        _existing_lanes_by_key.setdefault(_ep_key, set()).add(_ep_lane)
        except Exception:
            _existing_proposals_doc = None  # malformed existing file -- skip silently

    def _lookup_existing_status(_item: dict) -> dict | None:
        return lookup_existing_proposal_status(
            _item, _existing_proposal_status, _existing_lanes_by_key
        )

    # Numeric proposal-id indices already hand-assigned in manual_proposals.v1.json
    # (e.g. EXP-0085..EXP-0176). The auto counter below MUST skip these so an
    # auto-generated EXP-/LIT-NNNN id never collides with a manual proposal id.
    # The manual ids own the EXP-NNNN namespace and are referenced by governance
    # docs; auto ids are positional/ephemeral (keyed for stability on backlog_id,
    # not proposal_id). Reserve from BOTH prefixes because the EXP/LIT counter is
    # shared -- a manual LIT-0099 must block auto EXP-0099 and LIT-0099 alike.
    # (Fixes the 47 duplicate proposal_ids the old shared-namespace counter
    # produced in the generated experiment_proposals.v1.json.)
    #
    # ALSO reserve every already-RESOLVED existing proposal_id (_existing_proposal_status,
    # loaded above): those items are re-appended verbatim near the end of this
    # function (see "Preserve historical resolution records" below) whenever a
    # claim no longer generates a fresh proposal this cycle (e.g. it just became
    # experiment-ineligible), so their old numeric id must not be handed to an
    # unrelated freshly-generated proposal in the meantime. Confirmed 2026-08-02
    # (chip-20260802-backlog-dispatcher-gating-bug): without this, the same
    # substrate_conditional/v3_pending+v4 gate fix that motivated the
    # re-append produced 18 duplicate proposal_ids (e.g. two different claims
    # both stamped EXP-0039) in the same regen that introduced the re-append.
    _manual_reserved_idx: set[int] = set()
    if _existing_proposals_doc is not None:
        for _ep in _existing_proposals_doc.get("items", []):
            _ep_keys = _proposal_identity_keys(_ep)
            if not _ep_keys or not any(k in _existing_lanes_by_key for k in _ep_keys):
                continue  # only resolved (non-"proposed") entries get re-appended later
            _m = re.match(r"^(?:EXP|LIT)-(\d+)$", str(_ep.get("proposal_id") or ""))
            if _m:
                _manual_reserved_idx.add(int(_m.group(1)))
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

    # Sorted worst-first so the most contentious silent claims surface at the
    # top of any consumer that just reads the first few entries. Shared
    # between the JSON backlog doc below and the human-readable watchlist
    # markdown written further down (see DORMANT_HIGH_CONFLICT_WATCHLIST.md).
    dormant_high_conflict_sorted = sorted(
        dormant_high_conflict_items,
        key=lambda item: -item["conflict_ratio"],
    )

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
        # No-deadline visibility report -- see the dormant_high_conflict_items
        # append site above for the full rationale.
        "dormant_high_conflict": dormant_high_conflict_sorted,
    }
    # Merge in manually-curated proposals that survive pipeline regeneration.
    # Read evidence/planning/manual_proposals.v1.json if it exists; append its
    # items verbatim to the generated list. Manual items must carry:
    #   proposal_id, claim_id, proposal_type, priority, objective, status
    #
    # Every manual item MUST carry a stable backlog_id, minted here on first
    # encounter and persisted back to the source file so it never needs
    # re-minting. Without this, the status carry-forward below (and the
    # "Preserve historical resolution records" re-append further down) falls
    # back to keying on proposal_id for these items instead -- which, unlike
    # every auto-generated proposal, has no code-enforced stability guarantee
    # of its own; it merely happens to hold today because nothing currently
    # rewrites a manual item's proposal_id. Confirmed 2026-08-02
    # (chip-20260802-backlog-null-carryforward): all 81 manual_proposals.v1.json
    # items lacked backlog_id, the one exposed category (every auto-generated
    # proposal always gets one via the "Persistent ID assignment" loop above).
    # Reuses the SAME numeric EVB-NNNN counter/collision-set as that loop so
    # the two ID spaces can never collide, without inserting these proposals
    # into evidence_backlog.v1.json itself (they are direct manual dispatches,
    # not auto-detected evidence gaps).
    manual_proposals_path = planning_root / "manual_proposals.v1.json"
    if manual_proposals_path.exists():
        try:
            manual_doc = json.loads(manual_proposals_path.read_text(encoding="utf-8"))
            _manual_doc_changed, _next_auto_idx = _mint_missing_manual_backlog_ids(
                manual_doc, _next_auto_idx
            )
            for mp in manual_doc.get("items", []):
                if isinstance(mp, dict) and mp.get("proposal_id"):
                    mp_copy = dict(mp)
                    mp_copy["source"] = "manual"
                    proposals.append(mp_copy)
            if _manual_doc_changed:
                _atomic_write_text(
                    manual_proposals_path,
                    json.dumps(manual_doc, indent=2) + "\n",
                )
        except Exception:
            pass  # malformed manual file -- skip silently

    # Carry forward non-proposed status from the existing proposals file.
    # Generated proposals always start as "proposed"; any manual status edits
    # (e.g. "executed") are wiped on regeneration unless we re-apply them here.
    # Key by (identity key, LANE) -- backlog_id preferred and stable across
    # regenerations, proposal_id as fallback for manual proposals that carry no
    # backlog_id. The LANE half is required because backlog_id is NOT unique:
    # see _proposal_lane and _lookup_existing_status.
    # (_existing_proposal_status / _existing_proposals_doc were loaded earlier,
    # before the proposal_id counter, so their numeric ids could be reserved --
    # see "ALSO reserve every already-RESOLVED existing proposal_id" above.)
    for _p in proposals:
        _carried = _lookup_existing_status(_p)
        if _carried is not None:
            _p.update(_carried)

    # Preserve historical resolution records for items that no longer appear
    # in the freshly-generated `proposals` list AT ALL -- e.g. a claim that
    # is now correctly recognized as experiment-ineligible
    # (_is_experiment_ineligible_claim) but had an ALREADY-RESOLVED proposal
    # (executed / gated / blocked_substrate) from before that recognition
    # landed. Without this, an eligibility-gate fix (or any future gate
    # change) silently drops the historical record that an experiment WAS
    # already run and answered for that claim -- real evidence-loss, unlike
    # the desired disappearance of a dead-on-arrival "proposed" item (which
    # legitimately should stop being regenerated). Confirmed 2026-08-02
    # (chip-20260802-backlog-dispatcher-gating-bug): the substrate_
    # conditional/v3_pending+v4 gate fix newly excluded 19 claims whose
    # EXP-*/LIT-* proposal was already executed/gated/blocked_substrate
    # (e.g. Q-007 EXP-0039, executed as V3-EXQ-132) purely because the
    # eligibility check runs before a NEW proposal would be minted -- it has
    # no way to know a resolved proposal for that claim already exists. The
    # carry-forward loop above can't help either: it only updates items still
    # present in `proposals` this cycle. Re-append the prior item verbatim
    # (not just the status-family fields) so it survives regen exactly like
    # any other resolved item does.
    if _existing_proposals_doc is not None:
        _regenerated_bids: set[str] = set()
        for _p in proposals:
            _regenerated_bids.update(_proposal_identity_keys(_p))
        for _ep in _existing_proposals_doc.get("items", []):
            _ep_keys = _proposal_identity_keys(_ep)
            if (
                _ep_keys
                and not any(k in _regenerated_bids for k in _ep_keys)
                and _ep.get("status", "proposed") != "proposed"
            ):
                proposals.append(dict(_ep))
                _regenerated_bids.update(_ep_keys)

    # Write the same carried-forward status back into manual_proposals.v1.json
    # itself. Without this, a manual item's on-disk "status" is frozen at
    # whatever it was authored as -- the merge above always overrides the IN-
    # MEMORY copy from _existing_proposal_status, but nothing ever wrote that resolution
    # back to the source file, so a session reading manual_proposals.v1.json
    # directly (its own docstring calls it the place to "add new items", which
    # reads as authoritative) sees a permanently-stale "proposed" for anything
    # already executed/superseded/gated. Confirmed root cause of proposals
    # being re-investigated as open work long after landing: see
    # WORKSPACE_STATE.md 2026-08-02 (session determined-ritchie-55a3a6).
    # Only the same status-family keys the carry-forward above reads are
    # touched, in place, preserving field order -- so a real diff only shows
    # up when something actually resolved.
    if manual_proposals_path.exists():
        try:
            _manual_doc = json.loads(manual_proposals_path.read_text(encoding="utf-8"))
            _manual_changed = False
            for _mp in _manual_doc.get("items", []):
                if not isinstance(_mp, dict):
                    continue
                _resolved = _lookup_existing_status(_mp)
                if not _resolved:
                    continue
                for _k, _v in _resolved.items():
                    if _mp.get(_k) != _v:
                        _mp[_k] = _v
                        _manual_changed = True
            if _manual_changed:
                _atomic_write_text(
                    manual_proposals_path,
                    json.dumps(_manual_doc, indent=2) + "\n",
                )
        except Exception:
            pass  # malformed manual file -- skip silently, same as the merge above

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

    _atomic_write_text(
        planning_root / "evidence_backlog.v1.json",
        json.dumps(backlog_doc, indent=2, sort_keys=True) + "\n",
    )
    _atomic_write_text(
        planning_root / "experiment_proposals.v1.json",
        json.dumps(proposals_doc, indent=2, sort_keys=True) + "\n",
    )
    _atomic_write_text(
        planning_root / "experiment_proposals_index.v1.json",
        json.dumps(_index_doc, indent=2, sort_keys=True) + "\n",
    )
    _atomic_write_text(
        planning_root / "architecture_gap_register.v1.json",
        json.dumps(architecture_gap_doc, indent=2, sort_keys=True) + "\n",
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

    _atomic_write_text(
        planning_root / "ARCHITECTURE_GAP_REGISTER.md",
        "\n".join(arch_lines).rstrip() + "\n",
    )

    # Human-readable surface for the dormant_high_conflict no-deadline watchlist
    # (see the append site above for the full rationale). The JSON list in
    # evidence_backlog.v1.json is machine-readable only; nothing previously
    # surfaced these genuinely contentious claims to a human reviewer.
    # Derive-only: regenerated from dormant_high_conflict_sorted every run,
    # never hand-edited.
    dormant_lines: list[str] = []
    dormant_lines.append("# Dormant / Chronic High-Conflict Watchlist")
    dormant_lines.append("")
    dormant_lines.append(f"Generated: `{generated_at}`")
    dormant_lines.append("")
    dormant_lines.append(
        "No-deadline visibility report. Lists claims with `conflict_ratio >= "
        + _fmt_number(dormant_high_conflict_ratio)
        + "` and an unresolved decision, but invisible to the "
        + "`mandatory_decision_checkpoint` (which requires `conflict_ratio >= "
        + _fmt_number(mandatory_decision_conflict_ratio)
        + "` AND fresh recent batches). Deliberately carries no deadline -- see "
        + "`evidence_backlog.v1.json` -> `dormant_high_conflict` for the source record "
        + "and the full rationale in `build_experiment_indexes.py`."
    )
    dormant_lines.append("")
    dormant_lines.append(
        "- `dormant_low_activity` -- conflict is real but nobody has run enough "
        "recent evidence against the claim to meet the mandatory-checkpoint batch floor."
    )
    dormant_lines.append(
        "- `chronic_under_threshold` -- worked heavily, but `conflict_ratio` "
        "never quite crosses the mandatory bar, so it is reworked indefinitely "
        "without ever being forced to a decision."
    )
    dormant_lines.append("")
    dormant_lines.append("Sorted worst-conflict-first.")
    dormant_lines.append("")
    dormant_lines.append(
        "| claim_id | pattern | conflict_ratio | current_status | recent_targeted_batches |"
    )
    dormant_lines.append("|---|---|---|---|---|")
    if not dormant_high_conflict_sorted:
        dormant_lines.append("| _none_ | - | - | - | - |")
    else:
        for item in dormant_high_conflict_sorted:
            dormant_lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{item['claim_id']}`",
                        f"`{item['pattern']}`",
                        _fmt_number(float(item.get("conflict_ratio", 0.0))),
                        f"`{item['current_status']}`",
                        str(item.get("recent_targeted_batches", 0)),
                    ]
                )
                + " |"
            )
    _atomic_write_text(
        planning_root / "DORMANT_HIGH_CONFLICT_WATCHLIST.md",
        "\n".join(dormant_lines).rstrip() + "\n",
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
    index_lines.append(
        "- Dormant high-conflict watchlist: "
        + f"`DORMANT_HIGH_CONFLICT_WATCHLIST.md` ({len(dormant_high_conflict_sorted)} item(s))"
    )
    index_lines.append("- Planning criteria: `planning_criteria.v1.yaml`")
    _write_index_if_material(
        planning_root / "INDEX.md",
        "\n".join(index_lines).rstrip() + "\n",
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
    """Yield (manifest_dict, path) for flat + run-pack manifests that have arm_results.

    Dry-run smokes are excluded on the same run_id set the scoring scan uses. A
    smoke's OFF arm is a toy cell (typically 1 seed x a couple of episodes), so
    minting it as a reuse SOURCE would let a later real experiment silently
    inherit a fingerprint-matched baseline computed from nothing.
    """
    dry_run_ids = _load_dry_run_run_ids(base_dir)
    seen: set[Path] = set()
    flat = sorted(base_dir.glob("*.json"))
    nested = sorted(base_dir.glob("**/runs/**/manifest.json"))
    for path in flat + nested:
        rp = path.resolve()
        if rp in seen:
            continue
        seen.add(rp)
        if path.name.startswith("_dry_"):
            continue
        manifest = _load_json(path)
        if not isinstance(manifest, dict):
            continue
        if _is_dry_run(manifest) or str(manifest.get("run_id", "")) in dry_run_ids:
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
    _write_json_if_material(
        base_dir / "arm_fingerprint_index.json",
        json.dumps(index, indent=2, sort_keys=True) + "\n",
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


def _emit_derived_evidence_db(
    base_dir: Path,
    matrix: dict[str, Any],
    by_experiment: dict[str, list[RunRecord]],
    generated_at: str,
    allow_missing_runs: bool,
) -> None:
    """Write the derived SQLite read-model beside claim_evidence.v1.json.

    Import is LOCAL and guarded: this script is invoked by governance.sh, by
    /governance, by the hub, and by ad-hoc sessions, and a missing or broken
    derived-index module must degrade to "no read-model" rather than taking the
    whole evidence rebuild down with it.
    """
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import derived_evidence_db as _dedb  # noqa: WPS433
    except Exception as exc:  # pragma: no cover - import-path dependent
        print(f"[derived-index] SKIPPED (import failed): {exc}", file=sys.stderr)
        return
    try:
        res = _dedb.build_derived_db(
            base_dir, matrix,
            by_experiment=by_experiment,
            generated_at=generated_at,
            indexer_version=INDEXER_VERSION,
            allow_missing_runs=allow_missing_runs,
        )
    except _dedb.DerivedIndexSkewError as exc:
        print("", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print(
            "[derived-index] This is the SECOND, independent skew check "
            "disagreeing with the first (_guard_worktree_materialised passed at "
            "the top of this run). Investigate before trusting any artifact from "
            "this build.",
            file=sys.stderr,
        )
        sys.exit(SKEW_GUARD_EXIT_CODE)
    except Exception as exc:  # pragma: no cover - defensive
        print(f"[derived-index] SKIPPED (build failed): {exc}", file=sys.stderr)
        return
    meta = res["meta"]
    print(
        "[derived-index] %s  claims=%s entries=%s runs=%s  manifests on_disk=%s "
        "in_git=%s tracked_absent=%s  skew=%s"
        % (
            res["path"].name, meta["n_claims"], meta["n_entries"], meta["n_runs"],
            meta["n_manifests_on_disk"], meta["n_manifests_in_git"] or "n/a",
            meta["n_tracked_absent"], meta["skew_gate"],
        )
    )


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
    parser.add_argument(
        "--allow-cross-epoch-claim",
        action="append",
        default=[],
        metavar="CLAIM_ID",
        help=(
            "Exempt CLAIM_ID from the cross-epoch/cross-canonical-profile "
            "aggregation guard's WARNING for this run only (does not edit "
            "claims.yaml). Repeatable. Use for a deliberate one-off "
            "cross-epoch comparison; for a standing exemption, set "
            "'intentional_cross_epoch_comparison: true' under the claim in "
            "claims.yaml instead. See _detect_cross_epoch_pooling."
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
        # A flat-only orphan (2026-09-01, GFLAG-0111) can be the SOLE run for
        # its experiment_type, with no runs/<run_id>/ pack ever written -- so,
        # unlike every pre-existing experiment_type, experiment_dir may not
        # exist on disk yet. mkdir is a no-op for the pack case (dir already
        # there); for the flat-only case it is what makes this loop's own
        # experiment.md / INDEX.md writes below possible at all.
        experiment_dir.mkdir(parents=True, exist_ok=True)
        profile_path = _ensure_experiment_template(experiment_dir, experiment_type)

        design_text, todos = _build_design_implications(runs, args.lookback_failures)
        profile_text = profile_path.read_text(encoding="utf-8")
        profile_text = _replace_between_markers(profile_text, design_text)
        _atomic_write_text(profile_path, profile_text)

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
        claim_registry=claim_registry,
        allow_cross_epoch_claims=set(args.allow_cross_epoch_claim),
    )

    # Derived SQLite read-model (derived_evidence_index:P1). An ADDITIONAL WRITER
    # at the point the matrix is already in memory -- claim_evidence.v1.json above
    # is written unchanged, every un-migrated consumer keeps working, and deleting
    # the DB is always safe. It is NEVER a source of truth; see
    # derived_evidence_db.py's module docstring for the full contract.
    #
    # FAILS OPEN, LOUDLY, WITH ONE EXCEPTION. A derived read-model that cannot be
    # built must not cost a governance run, so any error is printed and swallowed.
    # The exception is DerivedIndexSkewError: that is the same HEAD/worktree-skew
    # refusal `_guard_worktree_materialised` makes at the top of main(), recomputed
    # independently, and reaching it here means the two disagree -- which is itself
    # worth stopping for rather than shrugging past.
    _emit_derived_evidence_db(base_dir, matrix, by_experiment, generated_at,
                              args.allow_missing_runs)

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
