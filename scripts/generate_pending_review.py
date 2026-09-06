#!/usr/bin/env python3
"""
Generate pending_review.md -- lists experiment runs not yet reviewed in a session.

Usage (from REE_assembly root):
    python scripts/generate_pending_review.py

After reviewing, add newly-reviewed run IDs to evidence/experiments/review_tracker.json
and re-run this script to confirm the list clears.

Run as step 3 of the governance pipeline:
    python scripts/sync_v3_results.py
    python scripts/build_experiment_indexes.py
    python scripts/generate_pending_review.py

SECTIONS GENERATED:
  1. FAIL (action required)     -- indexed result files with result != PASS, not yet reviewed
  2. PASS (verify & close)      -- indexed result files with result == PASS, not yet reviewed
  3. Needs discussion           -- runner_status completed entries not covered above:
       a. ERROR / UNKNOWN results (no result file, so not indexed, never in sections 1/2)
       b. Onboarding smoke runs (any result) -- contain hardware/throughput data needed
          for experimental design decisions, regardless of PASS/FAIL status
     Smoke runs are identified by queue_id containing "onboard" or "smoke" (case-insensitive)
     or script path containing "onboard_smoke".
  4. Unclaimed manifests        -- manifest files on disk with PASS/FAIL whose run_id is
     absent from claim_evidence (e.g., substrate-readiness or environment-probe diagnostics
     that intentionally tag no claims, or runs the runner mis-logged as ERROR/UNKNOWN). These
     fall through every other section because they're not in claim_evidence (so sections 1/2
     don't catch them) and the runner_status entry, if present, may already be queue_id-marked
     discussed (so section 3 short-circuits). Marking discussed for these runs MUST be done
     by manifest stem (run_id with timestamp suffix) -- queue_id-level marking is unsafe
     because the same queue_id can have both an ERROR runner_status entry and a separate
     PASS manifest produced by the same run.
"""
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

import yaml

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = ROOT / "evidence" / "experiments"
CLAIM_EVIDENCE = EVIDENCE_DIR / "claim_evidence.v1.json"

# claim_evidence.v1.json is ~10 MB. load_pending_entries() and
# load_indexed_run_ids() each used to json.load() it independently, so a single
# run parsed it twice. Memoized here (one-shot script, so a plain module-level
# cache is sufficient -- no mtime keying needed within a process). Callers keep
# their own .exists() guards: the two have DIFFERENT missing-file behaviour
# (load_pending_entries exits 1, load_indexed_run_ids returns empty).
_CLAIM_EVIDENCE_CACHE: dict | None = None


def _load_claim_evidence() -> dict:
    """Parse claim_evidence.v1.json once per process. Caller must check exists()."""
    global _CLAIM_EVIDENCE_CACHE
    if _CLAIM_EVIDENCE_CACHE is None:
        with open(CLAIM_EVIDENCE) as f:
            _CLAIM_EVIDENCE_CACHE = json.load(f)
    return _CLAIM_EVIDENCE_CACHE
REVIEW_TRACKER = EVIDENCE_DIR / "review_tracker.json"
RUNNER_STATUS = EVIDENCE_DIR / "runner_status.json"          # legacy monolithic
RUNNER_STATUS_DIR = EVIDENCE_DIR / "runner_status"           # per-machine split
OUTPUT = EVIDENCE_DIR / "pending_review.md"
CLAIMS_YAML = ROOT / "docs" / "claims" / "claims.yaml"
RECOMMENDATIONS_MD = EVIDENCE_DIR / "promotion_demotion_recommendations.md"
SUBSTRATE_STATUS_SNAPSHOT = EVIDENCE_DIR / "substrate_status_snapshot.json"
# Grandfather baseline for the reviewed-FAIL-without-autopsy net (2026-08-08).
# Seeded ONCE with the pre-existing legacy debt so the net's first run is not a
# full-corpus dump; see load_reviewed_fail_without_autopsy / main().
FAIL_AUTOPSY_GRANDFATHER = EVIDENCE_DIR / "fail_autopsy_grandfather.json"

# Adjudication flags that block a diagnostic self-route from driving a governance
# action. Mirror of build_experiment_indexes.BLOCKING_ADJUDICATIONS (the canonical
# source + adjudication_blocks_governance_action() guard). Kept as a local literal
# to avoid importing the 4k-line indexer module just for one tuple. STRICTLY excludes
# "unverified" -- absence is surfaced-not-blocked (do not flood on the legacy record).
BLOCKING_ADJUDICATIONS = ("precondition_unmet", "vacuous_pass")

SUBSTRATE_CLAIM_TYPES = {
    "design_decision",
    "architectural_commitment",
    "architecture_hypothesis",
}
SUBSTRATE_SECTION_HEADER = "## Substrate changes with dependent invariants"


def load_tracker() -> tuple[set, set, str]:
    """Return (reviewed_run_ids, discussed_dirs, last_review_utc)."""
    if not REVIEW_TRACKER.exists():
        print("[warn] review_tracker.json not found -- all runs treated as pending", file=sys.stderr)
        return set(), set(), "unknown"
    with open(REVIEW_TRACKER) as f:
        tracker = json.load(f)
    reviewed = set(tracker.get("reviewed_run_ids", []))
    discussed = set(tracker.get("discussed_experiment_dirs", []))
    last_review = tracker.get("last_review_utc", "unknown")
    return reviewed, discussed, last_review


def _is_dry_run(d: dict) -> bool:
    """True if a manifest's top-level dry_run flag is set (any truthy form).

    A --dry-run smoke writes a real flat/pack manifest to evidence/experiments/
    (e.g. V3-EXQ-696: 1 seed, 4 toy episodes, elapsed 29.9s) but is NOT evidence
    -- it must never surface in pending_review. Mirrors the truthy check in
    flat_only_silent_drop_guard (str-cast tolerates bool/int/str forms).
    """
    return str(d.get("dry_run", "")).strip().lower() in ("true", "1", "yes")


def load_dry_run_run_ids() -> set:
    """Run_ids of manifests on disk flagged dry_run -- excluded from every pending bucket.

    claim_evidence entries do not carry the dry_run flag (the indexer drops it),
    so the PASS/FAIL sections -- which read the index, not the manifests -- need
    the run_id set built directly from disk. Scans both the flat top-level
    manifests and the canonical runs/<run_id>/manifest.json packs so a dry_run
    leak via either path is caught (treated like superseded/degenerate).
    """
    if not EVIDENCE_DIR.is_dir():
        return set()
    ids: set[str] = set()
    candidates = list(EVIDENCE_DIR.glob("*.json"))
    candidates += list(EVIDENCE_DIR.glob("*/runs/*/manifest.json"))
    for f in candidates:
        if f.name in _NON_MANIFEST_FILES:
            continue
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        if isinstance(d, dict) and _is_dry_run(d):
            rid = d.get("run_id")
            if rid:
                ids.add(rid)
    return ids


AUTOPSY_GLOB = "evidence/planning/failure_autopsy_*.json"


def load_confirmed_autopsy_run_ids() -> set:
    """Run_ids ADJUDICATED by at least one CONFIRMED failure_autopsy_*.json.

    Two sources, unioned, because a confirmed artifact records adjudication in
    two places (see .claude/skills/failure-autopsy/SKILL.md Step 2a + the Step 9
    schema):

      1. `targets[].run_id`   -- adjudicated AS EVIDENCE (a verdict was reached
                                 about what the run shows).
      2. `excluded_dry_run_ids` -- adjudicated as NON-EVIDENTIARY: a human (or an
                                 autopsy session) inspected the run and concluded
                                 it is a smoke/dry run with nothing to evaluate.

    Both mean "a human has looked at this run", which is exactly the predicate
    the autopsy-required gates below are asking about -- so both belong in this
    set. Source 2 is NOT redundant with load_dry_run_run_ids(): that one reads
    each manifest's own `dry_run` boolean off disk, and pre-2026-07 manifests
    often lack the flag entirely (the skill tells autopsy sessions to fall back
    to inspecting `evidence_direction_note` / `experiment_purpose` text). A run
    determined dry by content inspection and faithfully recorded in
    `excluded_dry_run_ids`, but whose manifest never got the flag written, was
    previously invisible to BOTH sets and could never clear the reviewed-FAIL
    blind-spot net no matter how many times it was re-adjudicated (7 such
    run_ids as of 2026-08-08). Reading it here is the fix; the manifest-flag set
    is deliberately left alone, since other buckets legitimately need "the
    manifest says dry_run" rather than "someone decided it was dry".

    Loosely mirrors check_unapplied_autopsy_recommendations.load_confirmed()'s
    run-id extraction (kept as a small standalone re-scan, not an import, so
    this script has no dependency on that CLI tool's argv/exit-code surface).
    That sibling deliberately does NOT read `excluded_dry_run_ids` and does not
    have this gap: it indexes `targets` in order to audit whether each target's
    `per_claim_recommendation` was applied, and an excluded dry run has no
    target dict and therefore no recommendation to apply.

    Coverage here means "adjudicated at least once", not "adjudicated correctly"
    or "current" -- GOV-APPLY-1 (check_unapplied_autopsy_recommendations.py) is
    the audit for whether a *confirmed* recommendation was actually applied.
    """
    ids: set[str] = set()
    if not EVIDENCE_DIR.parent.is_dir():
        return ids
    for p in sorted((ROOT).glob(AUTOPSY_GLOB)):
        try:
            data = json.loads(p.read_text())
        except Exception:
            continue
        if not isinstance(data, dict) or str(data.get("status")) != "confirmed":
            continue
        for target in data.get("targets", []) or []:
            if not isinstance(target, dict):
                continue
            rid = target.get("run_id")
            if isinstance(rid, str) and rid:
                ids.add(rid)
        for rid in data.get("excluded_dry_run_ids", []) or []:
            if isinstance(rid, str) and rid:
                ids.add(rid)
    return ids


def load_reviewed_fail_without_autopsy(reviewed: set, dry_run_ids: set,
                                       confirmed_autopsy_run_ids: set) -> list[dict]:
    """Claim-tagged, non-diagnostic, terminal FAIL runs that ARE marked reviewed
    but have NO confirmed /failure-autopsy target -- the reviewed-FAIL blind spot.

    load_pending_entries() drops every run_id in reviewed_run_ids, so a
    claim-tagged FAIL that was marked reviewed WITHOUT ever being autopsied
    disappears from the FAIL section (1) and from every other net: the two
    diagnostic-autopsy nets key on experiment_purpose == 'diagnostic' (this is
    evidence-purpose), the unclaimed/ERROR scanners key on claim-less or
    ERROR-class manifests, and load_pending_entries has already excluded it by
    reviewed-status. It then sits unexamined indefinitely. Confirmed on
    ARC-017's V3-EXQ-129/135 pair: run 2026-03-29, marked reviewed, first
    adjudicated 2026-08-07 (~131 days) only because a /thought-digestion
    deferral note named it by hand. This scanner is the reviewed-INDEPENDENT
    net that closes the gap going forward; the pre-existing corpus of such runs
    is grandfathered (see main() + the grandfather baseline) so the first run is
    not a full-corpus dump.

    Reads claim_evidence `entries` only -- unlinked_runs are claim-less by
    definition and so out of scope for a "claim-tagged" net (those are covered
    by load_unclaimed_manifests). Excludes:
      - runs not in reviewed (still surfaced by the FAIL section),
      - dry-run smokes,
      - diagnostic-purpose runs (owned by the two diagnostic-autopsy nets),
      - runs with >=1 confirmed autopsy target (already adjudicated).
    """
    if not CLAIM_EVIDENCE.exists():
        return []
    data = _load_claim_evidence()
    by_run: dict[str, dict] = {}
    for e in data.get("entries", []):
        if e.get("source_type") != "experimental":
            continue
        if e.get("status") != "FAIL":
            continue
        rid = e.get("run_id")
        if not rid or rid not in reviewed:
            continue
        if rid in dry_run_ids or rid in confirmed_autopsy_run_ids:
            continue
        if str(e.get("experiment_purpose", "evidence")) == "diagnostic":
            continue
        cid = e.get("claim_id")
        if not (cid and str(cid).strip()):
            continue
        rec = by_run.setdefault(rid, {
            "run_id": rid,
            "timestamp_utc": e.get("timestamp_utc", "") or "",
            "claims": [],
        })
        if cid not in rec["claims"]:
            rec["claims"].append(cid)
    return sorted(by_run.values(), key=lambda r: (r["timestamp_utc"], r["run_id"]))


def load_fail_autopsy_grandfather() -> set | None:
    """Return the grandfathered legacy run_id set, or None if not seeded yet."""
    if not FAIL_AUTOPSY_GRANDFATHER.exists():
        return None
    try:
        data = json.loads(FAIL_AUTOPSY_GRANDFATHER.read_text())
    except Exception as ex:
        print(f"[warn] could not read {FAIL_AUTOPSY_GRANDFATHER.name}: {ex} "
              "-- treating as unseeded (first run)", file=sys.stderr)
        return None
    return set(data.get("grandfathered_run_ids", []))


def seed_fail_autopsy_grandfather(run_ids: set) -> None:
    """Seed the grandfather baseline with the pre-existing reviewed-FAIL debt.

    Written ONCE, on the first run after this net was installed. Everything in
    it is acknowledged legacy debt (reviewed-but-never-autopsied claim-tagged
    FAILs that accumulated before the net existed) and is NOT flagged; every
    reviewed FAIL that enters the blind-spot state AFTER seeding is absent from
    this set and therefore flagged. Mirrors substrate_status_snapshot.json's
    first-run seed-then-diff pattern.
    """
    payload = {
        "seeded_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "note": ("Legacy reviewed-but-un-autopsied claim-tagged FAIL run_ids, "
                 "grandfathered at net-install time so the reviewed-FAIL net's "
                 "first run is not a full-corpus dump. These are NOT flagged in "
                 "pending_review; a governance session working this debt down "
                 "can /failure-autopsy any of them and it leaves the outstanding "
                 "count automatically (coverage is recomputed from the confirmed "
                 "autopsy corpus each run, this file is never edited to remove "
                 "them). Do NOT add run_ids by hand -- a run that enters the "
                 "reviewed-without-autopsy state after seeding is meant to be "
                 "flagged, not grandfathered."),
        "grandfathered_run_ids": sorted(run_ids),
    }
    FAIL_AUTOPSY_GRANDFATHER.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _manifest_pass_fail(d: dict) -> str | None:
    """Resolve PASS/FAIL from V3 manifests (result, verdict, outcome, or metrics).

    Each of result/verdict/outcome may be a bare string OR a dict carrying the
    verdict under an inner "outcome"/"result"/"verdict" key. The dict shape MUST
    be unwrapped rather than skipped: a truthy dict short-circuits an `or` chain,
    so `d["result"] or d["outcome"]` never reaches a valid top-level string
    outcome when `result` is dict-shaped, the dict fails the ("PASS","FAIL")
    membership test, and the manifest resolves to None. load_unclaimed_manifests
    then drops it entirely -- the same silent-drop class fixed for UNKNOWN
    manifests. Confirmed 2026-07-20 on
    v3_exq_728_trained_allon_capability_point_20260720T155414Z_v3 (dict `result`
    + top-level `outcome: "FAIL"` + claim_ids: []), which was invisible to
    pending_review.md while the indexer path carried the other 64 dict-`result`
    manifests via their claim tags.
    """
    # First-present-wins, matching the original `or` chain: a manifest whose
    # `result` is a non-PASS/FAIL string ("ERROR") still resolves to None here
    # and is left to load_error_manifests, rather than falling through to a
    # sibling field. Only the dict shape is newly unwrapped.
    for field in ("result", "verdict", "outcome"):
        value = d.get(field)
        if not value:
            continue
        if isinstance(value, dict):
            value = next(
                (value[k] for k in ("outcome", "result", "verdict")
                 if isinstance(value.get(k), str)),
                None,
            )
        if value in ("PASS", "FAIL"):
            return value
        break
    metrics = d.get("metrics")
    if isinstance(metrics, dict):
        overall_pass = metrics.get("overall_pass")
        if overall_pass is True:
            return "PASS"
        if overall_pass is False:
            return "FAIL"
    return None


def _z_goal_writer_defect(run: dict) -> bool:
    """True ONLY for the unambiguous dead-z_goal-stream defect.

    Keys on the producer's precomputed `writer_defect` verdict -- i.e. the run
    stepped the agent (`ticks_total > 0`) and `update_z_goal`, the substrate's
    SOLE z_goal writer, was never called. z_goal then sat at zero-init for the
    whole run and the E3 goal term, MECH-293 ghost probes, MECH-288's slow BOCPD
    scale, MECH-189 super-ordinal anchors, the SD-057 incentive bank, the
    MECH-295 liking->approach bridge and the frontopolar counterfactual read all
    silently no-opped. Confirmed on V3-EXQ-626 and V3-EXQ-830.

    DELIBERATELY NOT keyed on `active_frac == 0.0`, and this is the whole point
    of the helper. A zero fraction is a legitimate and common reading, produced
    by at least three benign shapes: a goal-OFF parity arm, a negative control
    (V3-EXQ-626b's ARM_NO_BENEFIT), and a correctly-wired run whose GoalState
    benefit gate never opened because the agent met no resource -- the last of
    which is measured, not hypothetical, on a StepHarness run that structurally
    cannot carry the defect. Flagging the fraction would bury the real signal
    under those.

    `is True` rather than a truthiness test: the producer also writes None for
    "nothing measured" (`ticks_total == 0`), for a training-phase-only
    observation (`eval_stepped=False`), and for a driver that deliberately
    pins z_goal outside `update_z_goal` as an experimental control
    (`goal_pinned=True`, e.g. V3-EXQ-642a/642b) -- see
    `experiments/_lib/z_goal_stream.py`'s module docstring for all three. An
    ABSENT block means the run never measured the stream at all -- almost the
    whole historical corpus. None of these is a defect, and none may be
    rendered as one.
    """
    block = run.get("z_goal_stream")
    if not isinstance(block, dict) or not block:
        return False
    return block.get("writer_defect") is True


def _accumulate_pending_run(by_run: dict, e: dict, default_claim: str) -> None:
    run_id = e["run_id"]
    if run_id not in by_run:
        by_run[run_id] = {
            "run_id": run_id,
            "timestamp_utc": e.get("timestamp_utc", ""),
            "status": e.get("status", "?"),
            "claims": [],
            "failure_signatures": [],
            # Diagnostic adjudication gate (2026-06-06): the indexer attaches
            # adjudication in {verified, precondition_unmet, vacuous_pass,
            # unverified, n/a} to diagnostic/baseline runs. Surfaced below so a
            # flagged self-route is visible before governance acts on it.
            "adjudication": e.get("adjudication", "n/a"),
            "interpretation_label": e.get("interpretation_label", ""),
            # experiment_purpose (2026-08-07): 'diagnostic' vs 'evidence'. Used
            # by the diagnostic-autopsy-required gate below -- ALL diagnostic
            # results (PASS or FAIL), not only ones the indexer flagged
            # untrustworthy via `adjudication`, must clear /failure-autopsy
            # before governance marks them reviewed. See CLAUDE.md / user
            # standing instruction: a diagnostic result's self-routed reading
            # is not verified until adjudicated, regardless of whether it
            # happens to route a visible governance decision.
            "experiment_purpose": e.get("experiment_purpose", "evidence"),
            # Recorded (NON-GATING) preconditions (2026-07-20): unmet entries from
            # interpretation.recorded_preconditions[] -- guard findings the run's
            # author deliberately did NOT gate on (an arm-symmetric prior, or a
            # readout-side question with an unaffected control). Surfaced under
            # their own non-blocking heading, kept strictly OUT of `flagged` below
            # so they never read as action-required.
            "recorded_preconditions_unmet": e.get("recorded_preconditions_unmet", []),
            "preconditions_scope_note": e.get("preconditions_scope_note", ""),
            # z_goal-stream liveness (2026-07-27): the indexer carries the run's
            # z_goal_stream counter block through when the run measured one.
            # Absent => UNMEASURED (almost the whole corpus) => never flagged.
            # Read via _z_goal_writer_defect, never via active_frac.
            "z_goal_stream": e.get("z_goal_stream") or {},
        }
    claim = e.get("claim_id") or default_claim
    if claim not in by_run[run_id]["claims"]:
        by_run[run_id]["claims"].append(claim)
    by_run[run_id]["failure_signatures"].extend(e.get("failure_signatures", []))


def load_pending_entries(reviewed: set, dry_run_ids: set) -> list[dict]:
    """Load PASS/FAIL from claim_evidence entries + unlinked_runs not yet reviewed.

    dry_run_ids (built from on-disk manifests by load_dry_run_run_ids) are excluded
    here too: claim_evidence carries a PASS/FAIL status for a dry-run manifest even
    when the indexer marked it scoring_excluded, so without this guard a --dry-run
    smoke surfaces in the FAIL/PASS section (incident V3-EXQ-696).
    """
    if not CLAIM_EVIDENCE.exists():
        print("[error] claim_evidence.v1.json not found -- run build_experiment_indexes.py first",
              file=sys.stderr)
        sys.exit(1)
    data = _load_claim_evidence()
    by_run: dict[str, dict] = {}
    for e in data.get("entries", []):
        if e.get("source_type") != "experimental":
            continue
        if e.get("run_id") in reviewed:
            continue
        if e.get("run_id") in dry_run_ids:
            continue
        if e.get("status") not in ("PASS", "FAIL"):
            continue
        _accumulate_pending_run(by_run, e, e.get("claim_id", "?"))
    for e in data.get("unlinked_runs", []):
        if e.get("source_type") != "experimental":
            continue
        if e.get("run_id") in reviewed:
            continue
        if e.get("run_id") in dry_run_ids:
            continue
        if e.get("status") not in ("PASS", "FAIL"):
            continue
        _accumulate_pending_run(by_run, e, "(no claim tags)")
    return sorted(by_run.values(), key=lambda r: r["timestamp_utc"])


def _is_smoke_run(queue_id: str, script: str) -> bool:
    """Return True if this entry is an onboarding smoke run."""
    combined = (queue_id + " " + script).lower()
    return "onboard" in combined or "smoke" in combined


def _derive_dir_name(output_file: str, queue_id: str) -> str:
    """Derive the experiment directory name from output_file path, same logic as explorer.html."""
    if not output_file:
        return queue_id
    path = output_file.replace("\\", "/")
    parts = path.split("experiments/")
    if len(parts) > 1:
        segment = parts[-1].split("/")[0]
        if segment.endswith(".json"):
            segment = re.sub(r"_(?:v\d+_)?\d{8}T\d{6}Z?(?:_v\d+)?\.json$", "", segment)
        if segment:
            return segment
    # bare filename
    basename = path.split("/")[-1]
    if basename.endswith(".json"):
        basename = re.sub(r"_(?:v\d+_)?\d{8}T\d{6}Z?(?:_v\d+)?\.json$", "", basename)
    return basename or queue_id


# Hours after which the git runner_status mirror is considered frozen.
# The per-run outcome lists inside runner_status/*.json have NO coordinator
# /shadow/status equivalent, so this reader keeps the git files -- but the
# git materialization of that telemetry is retired (2026-09-01), so once
# every file is older than this (by mtime AND embedded last_updated) the
# counts derived from them may be incomplete and we say so.
RUNNER_STATUS_STALE_HOURS = 48.0


def _runner_status_mirror_is_stale() -> bool:
    """True when EVERY runner_status file is >48h old by mtime AND embedded ts.

    A file counts as fresh if either its mtime or its embedded last_updated
    timestamp is within the window (an unparseable embedded timestamp falls
    back to mtime alone). No files at all -> not stale; since 2026-09-06 the directory is gone from
    master, so this always returns False now and an empty completed list is the
    real signal that runner_status corroboration is unavailable (the absent-dir case
    already degrades to the legacy monolithic file / empty result).
    Never raises.
    """
    try:
        files = (sorted(RUNNER_STATUS_DIR.glob("*.json"))
                 if RUNNER_STATUS_DIR.is_dir() else [])
        if not files and RUNNER_STATUS.exists():
            files = [RUNNER_STATUS]
        if not files:
            return False
        now = datetime.now(timezone.utc)
        cutoff_s = RUNNER_STATUS_STALE_HOURS * 3600.0
        for f in files:
            try:
                mtime_age = (now.timestamp() - f.stat().st_mtime)
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


def load_runner_status_undiscussed(reviewed: set, discussed: set,
                                   indexed_run_ids: set) -> list[dict]:
    """Load runner_status completed entries that need discussion but are not in sections 1/2.

    Includes:
    - ERROR / UNKNOWN entries not already in discussed_dirs
    - Onboarding smoke runs (any result) not already in discussed_dirs or reviewed_run_ids
    - FAIL / PASS entries whose result file exists on disk but is NOT yet in the index
      (completed after the last build_experiment_indexes.py run — stale index gap)

    Excludes:
    - Entries whose derived dir_name OR queue_id is in discussed_dirs
    - Entries whose run_id is in reviewed_run_ids
    - Entries whose run_id IS in indexed_run_ids (already covered by sections 1/2)
    """
    # The git telemetry mirror is retired (2026-09-01); warn when frozen so
    # nobody reads a quiet section as "no undiscussed runs".
    if _runner_status_mirror_is_stale():
        print(
            "[warn] WARNING: the git runner_status telemetry mirror "
            "(evidence/experiments/runner_status/) is retired/frozen -- every "
            "file is older than %dh. Runner-status-derived counts below may "
            "be incomplete; the coordinator DB is the live authority."
            % int(RUNNER_STATUS_STALE_HOURS),
            file=sys.stderr)

    # Read completed entries from per-machine files (preferred) or legacy monolithic
    all_completed: list[dict] = []
    if RUNNER_STATUS_DIR.is_dir():
        for f in sorted(RUNNER_STATUS_DIR.glob("*.json")):
            try:
                data = json.loads(f.read_text())
                all_completed.extend(data.get("completed", []))
            except Exception:
                pass
    elif RUNNER_STATUS.exists():
        try:
            with open(RUNNER_STATUS) as f:
                rs = json.load(f)
            all_completed = rs.get("completed", [])
        except Exception:
            pass

    if not all_completed:
        return []

    pending = []
    seen_queue_ids: set[str] = set()

    for entry in all_completed:
        queue_id = entry.get("queue_id", "")
        result = entry.get("result", "")
        output_file = entry.get("output_file", "") or ""
        script = entry.get("script", "") or ""
        claimed_at = (entry.get("claimed_by") or {}).get("claimed_at", "")

        if queue_id in seen_queue_ids:
            continue
        seen_queue_ids.add(queue_id)

        dir_name = _derive_dir_name(output_file, queue_id)
        is_smoke = _is_smoke_run(queue_id, script)

        # Check if already discussed
        if dir_name in discussed or queue_id in discussed:
            continue

        # Check if already covered by sections 1/2 via indexed run_id
        # (output_file can give us the run_id if we derive it)
        run_id_from_file = ""
        if output_file:
            # run_id is typically the stem without .json
            basename = output_file.replace("\\", "/").split("/")[-1]
            if basename.endswith(".json"):
                run_id_from_file = basename[:-5]  # strip .json
        # Normalise run_id for comparison: output_file stems omit the _v2/_v3 suffix
        # that indexed run_ids carry. Try both with and without common suffixes.
        def _in_reviewed_or_indexed(stem: str) -> bool:
            if not stem:
                return False
            for candidate in [stem, stem + "_v3", stem + "_v2"]:
                if candidate in reviewed or candidate in indexed_run_ids:
                    return True
            return False

        if _in_reviewed_or_indexed(run_id_from_file):
            # Already reviewed, OR it's in claim_evidence and will appear in sections 1/2
            continue

        # Detect stale-index gap: result file exists on disk but not yet indexed.
        # This catches FAIL/PASS experiments that completed after the last index build.
        # We only flag stale if the file exists AND none of its run_id variants are indexed.
        result_file_path = None
        if output_file:
            p = Path(output_file)
            result_file_path = p if p.is_absolute() else ROOT / output_file
        # Only flag stale if the result file is inside EVIDENCE_DIR (V3 results).
        # V2 experiment files live in ree-v2/ — their run_ids are transformed on sync
        # and don't match the basename, so stale detection would false-fire for all V2 runs.
        result_file_in_evidence = (
            result_file_path is not None
            and result_file_path.exists()
            and result_file_path.is_relative_to(EVIDENCE_DIR)
        )
        stale_index = (
            result_file_in_evidence
            and bool(run_id_from_file)
            and not _in_reviewed_or_indexed(run_id_from_file)
        )

        # Include if: ERROR/UNKNOWN, smoke run, or stale-index gap (not yet indexed)
        if result in ("ERROR", "UNKNOWN") or is_smoke or stale_index:
            pending.append({
                "queue_id": queue_id,
                "result": result,
                "script": script,
                "dir_name": dir_name,
                "claimed_at": claimed_at,
                "is_smoke": is_smoke,
                "stale_index": bool(stale_index),
            })

    # Sort by claimed_at (chronological)
    return sorted(pending, key=lambda r: r["claimed_at"])


def load_indexed_run_ids() -> set:
    """Return run_ids known to claim_evidence (linked entries + unlinked_runs)."""
    if not CLAIM_EVIDENCE.exists():
        return set()
    data = _load_claim_evidence()
    ids = {e["run_id"] for e in data.get("entries", []) if "run_id" in e}
    for e in data.get("unlinked_runs", []):
        rid = e.get("run_id")
        if rid:
            ids.add(rid)
    return ids


# Top-level JSON files in EVIDENCE_DIR that are tracker/index artifacts, not manifests.
_NON_MANIFEST_FILES = {
    "claim_evidence.v1.json",
    "review_tracker.json",
    "runner_status.json",
    "substrate_status_snapshot.json",
}


def load_unclaimed_manifests(reviewed: set, discussed: set,
                             indexed_run_ids: set) -> list[dict]:
    """Return PASS/FAIL manifests on disk whose run_id is NOT in claim_evidence.

    Walks EVIDENCE_DIR for top-level *.json files that look like result manifests
    (have a run_id and a result field), and reports any that:
      - have result PASS or FAIL,
      - are not in indexed_run_ids (i.e. claim_evidence has no entry for the run_id),
      - are not in reviewed (run_id), and
      - have neither the manifest stem nor the run_id in discussed_dirs.

    Marking discussed for these runs must be done by manifest stem (filename without
    .json) -- queue_id-level marking is unsafe because the runner's ERROR/UNKNOWN
    record for a queue_id can be marked discussed even when a separate PASS manifest
    for the same run exists on disk.
    """
    if not EVIDENCE_DIR.is_dir():
        return []

    out = []
    for f in sorted(EVIDENCE_DIR.glob("*.json")):
        if f.name in _NON_MANIFEST_FILES:
            continue
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        if _is_dry_run(d):
            continue
        run_id = d.get("run_id")
        if not run_id:
            continue
        result = _manifest_pass_fail(d)
        if not result:
            continue
        if run_id in indexed_run_ids:
            continue
        if run_id in reviewed:
            continue
        stem = f.stem
        if stem in discussed or run_id in discussed:
            continue
        out.append({
            "manifest_stem": stem,
            "run_id": run_id,
            "result": result,
            "experiment_type": d.get("experiment_type", ""),
            "evidence_direction": d.get("evidence_direction", ""),
            "timestamp_utc": d.get("timestamp_utc", "") or "",
            "queue_id": d.get("queue_id", "") or "",
            # Read straight off the flat manifest: these runs are by definition
            # absent from claim_evidence, so the indexer never saw them and the
            # block can only come from disk. Same absent==UNMEASURED rule.
            "z_goal_stream": d.get("z_goal_stream") or {},
        })

    return sorted(out, key=lambda r: (r["timestamp_utc"], r["run_id"]))


def load_error_manifests(reviewed: set, discussed: set,
                         indexed_run_ids: set) -> list[dict]:
    """Return ERROR-class manifests on disk not yet reviewed -> /diagnose-errors.

    The experiment runner writes a synthetic ERROR manifest when a script
    crashes before producing one (result==ERROR with empty output_file -- the
    FAIL/ERROR-class twin of the fixed UNKNOWN silent-drop; incident
    V3-EXQ-654e). Such a manifest carries outcome/result == "ERROR" and is
    scoring-neutral (claim_ids=[]), so it is invisible to the PASS/FAIL
    sections (1/2) and to the unclaimed-manifest section (which keys on
    _manifest_pass_fail). Without this scanner the crash would surface only
    via the runner_status section -- which depends on the runner_status file
    materialising on origin, the exact path that left V3-EXQ-654e invisible.
    Surfacing the durable manifest directly makes the crash reviewable and
    routes it to /diagnose-errors.

    Reports manifests that:
      - have outcome OR result == "ERROR" (or "UNKNOWN"),
      - are not in indexed_run_ids (ERROR records carry no claim tags, so they
        are never indexed -- defensive),
      - are not in reviewed (run_id), and
      - have neither the manifest stem nor the run_id in discussed_dirs.

    Mark discussed by adding the manifest stem (filename minus .json) to
    discussed_experiment_dirs, same as the unclaimed-manifest section.
    """
    if not EVIDENCE_DIR.is_dir():
        return []
    out = []
    for f in sorted(EVIDENCE_DIR.glob("*.json")):
        if f.name in _NON_MANIFEST_FILES:
            continue
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        if _is_dry_run(d):
            continue
        run_id = d.get("run_id")
        if not run_id:
            continue
        outcome = (d.get("outcome") or d.get("result") or "").upper()
        if outcome not in ("ERROR", "UNKNOWN"):
            continue
        if run_id in indexed_run_ids or run_id in reviewed:
            continue
        stem = f.stem
        if stem in discussed or run_id in discussed:
            continue
        out.append({
            "manifest_stem": stem,
            "run_id": run_id,
            "outcome": outcome,
            "queue_id": d.get("queue_id", "") or "",
            "machine": d.get("machine", "") or "",
            "result_summary": (d.get("result_summary", "") or "")[:80],
            "timestamp_utc": d.get("timestamp_utc", "") or "",
        })
    return sorted(out, key=lambda r: (r["timestamp_utc"], r["run_id"]))


def flat_only_silent_drop_guard(indexed_run_ids: set) -> list[str]:
    """WARN on evidence-grade flat-only manifests the indexer never scored.

    An evidence-grade run (experiment_purpose 'evidence', >=1 non-empty claim id,
    not a dry run) whose canonical runs/<run_id>/manifest.json pack is absent AND
    whose run_id is missing from claim_evidence has been silently dropped from
    scoring -- the V3-EXQ-628 failure mode (a cloud Phase-3 result landed flat-only
    when its runs/ pack failed to sync, so build_experiment_indexes.py, which scans
    **/runs/**/manifest.json, never saw it and the claim sat at exp_conf=0 with no
    evidence). governance.sh runs sync_v3_results.py + build_experiment_indexes.py
    BEFORE this script, so a non-empty result here means an evidence run slipped
    through both -- repair it (reconstruct the runs/ pack) before closing the cycle.

    Returns the offending run_ids and prints a WARNING per run plus a summary.
    ASCII-only output (Windows cp1252 safe).
    """
    if not EVIDENCE_DIR.is_dir():
        return []
    offenders = []
    for f in sorted(EVIDENCE_DIR.glob("*.json")):
        if f.name in _NON_MANIFEST_FILES:
            continue
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        run_id = d.get("run_id")
        if not run_id:
            continue
        # Evidence-grade only: experiment_purpose 'evidence' with >=1 claim id.
        if str(d.get("experiment_purpose", "evidence")).strip() != "evidence":
            continue
        cids = d.get("claim_ids") or d.get("claim_ids_tested") or []
        if not (isinstance(cids, list) and any(str(c).strip() for c in cids)):
            continue
        # Dry-run / smoke artifacts are never scored by design -- skip.
        if (str(d.get("dry_run", "")).strip().lower() in ("true", "1", "yes")
                or str(run_id).endswith("_dry")):
            continue
        et = d.get("experiment_type") or ""
        has_pack = bool(et) and (EVIDENCE_DIR / et / "runs" / run_id / "manifest.json").exists()
        if has_pack or run_id in indexed_run_ids:
            continue
        offenders.append({
            "run_id": run_id,
            "file": f.name,
            "claim_ids": [str(c).strip() for c in cids if str(c).strip()],
        })

    for o in offenders:
        print(
            "WARNING: evidence-grade flat-only manifest never scored "
            "(no runs/ pack, absent from claim_evidence): "
            f"{o['run_id']} claims={o['claim_ids']} file={o['file']}. "
            "Re-run sync_v3_results.py + build_experiment_indexes.py to ingest, "
            "or reconstruct the canonical runs/ pack.",
            file=sys.stderr,
        )
    if offenders:
        print(
            f"WARNING: {len(offenders)} evidence-grade flat-only manifest(s) "
            "unscored -- silent-drop guard (see lines above).",
            file=sys.stderr,
        )
    return [o["run_id"] for o in offenders]


def write_pending_review(runs: list[dict], runner_undiscussed: list[dict],
                         unclaimed: list[dict],
                         error_manifests: list[dict],
                         last_review_utc: str,
                         fail_needs_autopsy: list[dict] | None = None,
                         grandfathered_outstanding: int = 0) -> None:
    fail_needs_autopsy = fail_needs_autopsy or []
    passes = [r for r in runs if r["status"] == "PASS"]
    fails  = [r for r in runs if r["status"] != "PASS"]
    # Diagnostic adjudication gate: diagnostics/baselines whose self-route the
    # indexer flagged as untrustworthy. These still appear in their FAIL/PASS
    # table for the normal review flow; this is a focused callout so governance
    # does not act on the label before it is adjudicated.
    flagged = [r for r in runs
               if r.get("adjudication") in BLOCKING_ADJUDICATIONS]
    # Diagnostic-autopsy-required gate (2026-08-07, user-instructed broadening):
    # `flagged` above only catches a diagnostic whose self-route the indexer
    # marked untrustworthy. That is a NARROWER net than "every diagnostic
    # result needs /failure-autopsy" -- a diagnostic PASS/FAIL that cleared its
    # own preconditions carries no `adjudication` flag and sailed straight into
    # the ordinary PASS/FAIL tables with no signal it needed adjudication at
    # all. Confirmed live 2026-08-07 governance cycle: two experiment_purpose
    # "diagnostic" PASSes (a substrate-regression check, a safety-gate fire
    # test) were about to be applied as routine evidence PASSes purely because
    # neither carried a blocking adjudication flag. This bucket is the
    # blanket, purpose-keyed net: ANY experiment_purpose == "diagnostic" run
    # (PASS or FAIL) not covered by at least one CONFIRMED failure_autopsy_*
    # target, regardless of adjudication flag or whether it visibly "routes a
    # decision". Membership here does not remove the run from its normal
    # PASS/FAIL table -- same non-exclusionary pattern as `flagged`.
    confirmed_autopsy_run_ids = load_confirmed_autopsy_run_ids()
    needs_diagnostic_autopsy = [
        r for r in runs
        if r.get("experiment_purpose") == "diagnostic"
        and r["run_id"] not in confirmed_autopsy_run_ids
    ]
    # Recorded (NON-GATING) preconditions -- a SEPARATE, non-blocking list. These
    # runs are NOT flagged: their author put the finding in
    # recorded_preconditions[] precisely because it does not invalidate the run's
    # premise. Surfacing it here gives the key a consumer (it was previously
    # write-only) without making it read as action-required. A run can appear in
    # both lists independently; membership here confers no blocking status and does
    # not affect the counts of PASS/FAIL or `flagged`.
    recorded = [r for r in runs if r.get("recorded_preconditions_unmet")]
    # Dead z_goal stream -- another SEPARATE, non-blocking list, on the `recorded`
    # pattern. Drawn from BOTH the indexed runs and the unclaimed manifests: a
    # substrate-readiness diagnostic tagging no claims is exactly the shape both
    # confirmed defects took, and those can land outside claim_evidence entirely.
    # Membership confers no blocking status, changes no count above, and never
    # excludes a run from scoring.
    zgoal_dead = ([r for r in runs if _z_goal_writer_defect(r)]
                  + [r for r in unclaimed if _z_goal_writer_defect(r)])

    total_pending = (len(runs) + len(runner_undiscussed) + len(unclaimed)
                     + len(error_manifests) + len(fail_needs_autopsy))
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "# Pending Experiment Review",
        "",
        f"Generated: `{now}`  ",
        f"Last review: `{last_review_utc}`  ",
        f"Pending: **{total_pending}** item(s)"
        f" -- {len(passes)} PASS, {len(fails)} FAIL,"
        f" {len(runner_undiscussed)} runner-only (ERROR/UNKNOWN/smoke),"
        f" {len(unclaimed)} unclaimed manifest(s),"
        f" {len(error_manifests)} ERROR manifest(s)"
        f"; {len(flagged)} diagnostic self-route(s) flagged for adjudication"
        + (f"; {len(needs_diagnostic_autopsy)} diagnostic run(s) with no confirmed autopsy"
           if needs_diagnostic_autopsy else "")
        + (f"; {len(fail_needs_autopsy)} reviewed FAIL(s) with no confirmed autopsy"
           if fail_needs_autopsy else "")
        + (f"; {grandfathered_outstanding} legacy reviewed-FAIL(s) grandfathered (awaiting autopsy)"
           if grandfathered_outstanding else "")
        + (f"; {len(recorded)} run(s) with recorded (non-gating) preconditions"
           if recorded else "")
        + (f"; {len(zgoal_dead)} run(s) with a DEAD z_goal stream"
           if zgoal_dead else ""),
        "",
    ]

    if total_pending == 0:
        lines += ["All experiments reviewed. Nothing pending.", ""]
    else:
        if fails:
            lines += ["## FAIL (action required)", ""]
            lines += ["| Run ID | Timestamp | Claims | Failure signatures |",
                      "|--------|-----------|--------|--------------------|"]
            for r in fails:
                claims = ", ".join(sorted(set(r["claims"])))
                sigs = ", ".join(sorted(set(r["failure_signatures"])))[:80] or "—"
                ts = r["timestamp_utc"][:16] if r["timestamp_utc"] else "?"
                lines.append(f"| `{r['run_id']}` | {ts} | {claims} | {sigs} |")
            lines.append("")

        if passes:
            lines += ["## PASS (verify & close)", ""]
            lines += ["| Run ID | Timestamp | Claims |",
                      "|--------|-----------|--------|"]
            for r in passes:
                claims = ", ".join(sorted(set(r["claims"])))
                ts = r["timestamp_utc"][:16] if r["timestamp_utc"] else "?"
                lines.append(f"| `{r['run_id']}` | {ts} | {claims} |")
            lines.append("")

        if flagged:
            lines += ["## Diagnostic adjudication required (self-route unverified)", ""]
            lines += [
                "These diagnostic/baseline runs carry a self-routed "
                "`interpretation.label`, but the indexer flagged it as untrustworthy: "
                "`precondition_unmet` (a declared precondition's `met` is false -- the "
                "self-route's premise did not hold) or `vacuous_pass` (an overall PASS "
                "rests on a degenerate criterion). The label must NOT drive a governance "
                "action (clear `v3_pending` / mint-or-AMEND `substrate_queue` / "
                "close-or-route a thought-intake) until adjudicated -- run "
                "`/failure-autopsy` on the run (it accepts a flagged PASS target too). "
                "See evidence/planning/proposal_diagnostic_adjudication_gate_2026-06-06.md.",
                "",
                "| Run ID | Status | Self-route label | Adjudication |",
                "|--------|--------|------------------|--------------|",
            ]
            for r in flagged:
                label = r.get("interpretation_label") or "—"
                lines.append(
                    f"| `{r['run_id']}` | {r['status']} | {label} | "
                    f"**{r['adjudication']}** |"
                )
            lines.append("")

        if needs_diagnostic_autopsy:
            lines += ["## Diagnostic -- autopsy required (no confirmed adjudication)", ""]
            lines += [
                "Every `experiment_purpose: \"diagnostic\"` result (PASS or FAIL) needs "
                "a CONFIRMED `/failure-autopsy` (alias `/diagnostic-autopsy`) target before "
                "governance marks it reviewed or applies anything from it -- not only the "
                "ones the indexer flagged untrustworthy above. A diagnostic's self-routed "
                "reading is a hypothesis about what it found, not a verdict; only the "
                "autopsy's four-layer diagnosis confirms it. This list is broader than "
                "'Diagnostic adjudication required' above: it fires on `experiment_purpose` "
                "alone, regardless of `adjudication` flag or whether the result visibly "
                "routes a decision.",
                "",
                "| Run ID | Status | Self-route label |",
                "|--------|--------|-------------------|",
            ]
            for r in needs_diagnostic_autopsy:
                label = r.get("interpretation_label") or "—"
                lines.append(f"| `{r['run_id']}` | {r['status']} | {label} |")
            lines.append("")

        if fail_needs_autopsy:
            lines += ["## Reviewed FAIL with no confirmed autopsy (blind-spot net)", ""]
            lines += [
                "These are claim-tagged, non-diagnostic, terminal **FAIL** runs "
                "that were marked reviewed in `review_tracker.json` but carry NO "
                "confirmed `/failure-autopsy` target. Being marked reviewed does "
                "NOT exempt a FAIL from autopsy. `load_pending_entries` drops "
                "every reviewed run_id, so without this net a claim-tagged FAIL "
                "can be marked reviewed with no diagnosis and vanish from every "
                "other section -- the ARC-017 V3-EXQ-129/135 pair sat in exactly "
                "this state for ~131 days (run 2026-03-29, first adjudicated "
                "2026-08-07, caught only because a /thought-digestion deferral "
                "note named it by hand). Run `/failure-autopsy` on each run "
                "below (accepts the pair together); once a CONFIRMED autopsy "
                "target exists the row clears automatically on the next generate. "
                "Legacy runs already in this state when the net was installed are "
                "grandfathered in `fail_autopsy_grandfather.json` and are NOT "
                "listed here"
                + (f" -- **{grandfathered_outstanding}** such legacy run(s) "
                   "remain un-autopsied (acknowledged debt, not counted in the "
                   "pending total; work them down via /failure-autopsy at "
                   "governance's discretion)." if grandfathered_outstanding
                   else "."),
                "",
                "| Run ID | Timestamp | Claims |",
                "|--------|-----------|--------|",
            ]
            for r in fail_needs_autopsy:
                claims = ", ".join(sorted(set(r["claims"])))
                ts = r["timestamp_utc"][:16] if r["timestamp_utc"] else "?"
                lines.append(f"| `{r['run_id']}` | {ts} | {claims} |")
            lines.append("")

        if recorded:
            lines += ["## Recorded (non-gating) preconditions", ""]
            lines += [
                "**No action is required on account of this section.** These runs "
                "declare a readiness finding in `interpretation.recorded_preconditions[]` "
                "that did NOT hold -- but the author deliberately did not gate the run on "
                "it, because the run's premise survives the finding (e.g. a shared "
                "symmetric prior that biases every arm identically, or a readout-side "
                "question with an unaffected control). The entries are kept out of the "
                "adjudicating `interpretation.preconditions[]` on purpose: that list is "
                "read flat and arm-blind, so an entry there would return a whole-run "
                "`precondition_unmet` and bury a valid result. Each run's own "
                "`preconditions_scope_note` states the reasoning. Read this as an audit "
                "trail when interpreting the run -- it is NOT an adjudication flag, does "
                "not block a governance action, and does not exclude the run from "
                "scoring. See evidence/planning/"
                "zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md.",
                "",
                "| Run ID | Status | Recorded precondition(s) not met | Scope note |",
                "|--------|--------|----------------------------------|------------|",
            ]
            for r in recorded:
                findings = r.get("recorded_preconditions_unmet") or []
                names = sorted({str(f.get("name", "?")) for f in findings
                                if isinstance(f, dict)})
                arms = sorted({str(f.get("arm")) for f in findings
                               if isinstance(f, dict) and f.get("arm")})
                detail = ", ".join(names) or "—"
                if arms:
                    shown = ", ".join(arms[:4]) + ("..." if len(arms) > 4 else "")
                    detail += f" ({len(findings)} entr{'y' if len(findings) == 1 else 'ies'}"
                    detail += f"; arms: {shown})"
                note = (r.get("preconditions_scope_note") or "").replace("|", "/")
                if len(note) > 200:
                    note = note[:197] + "..."
                lines.append(
                    f"| `{r['run_id']}` | {r['status']} | {detail} | {note or '—'} |"
                )
            lines.append("")

        if zgoal_dead:
            lines += ["## Dead z_goal stream (interpret before trusting a z_goal readout)", ""]
            lines += [
                "**This is a record, not a gate.** No claim status, confidence or "
                "`v3_pending` changes on account of it, and the runs below are scored "
                "exactly as they would be otherwise. It is here so the condition is seen "
                "at review time instead of only by whoever opens the raw manifest.",
                "",
                "Each run below reports `z_goal_stream.writer_defect: true`: the agent was "
                "stepped, but `REEAgent.update_z_goal` -- the **sole** z_goal writer in the "
                "substrate -- was never called. z_goal therefore sat at zero-init for the "
                "whole run, `GoalState.is_active()` returned False throughout, and every "
                "consumer received `current_z_goal=None` on every tick: the E3 goal term, "
                "MECH-293 ghost probes, MECH-288's slow BOCPD scale, MECH-189 super-ordinal "
                "anchors, the SD-057 incentive bank, the MECH-295 liking->approach bridge "
                "and the frontopolar counterfactual read all silently no-opped. Nothing "
                "raises. The usual cause is a driver that hand-rolls its inner loop and "
                "omits the call (V3-EXQ-626, whose five criteria were all keyed on a z_goal "
                "that never left zero; V3-EXQ-830, caught only because its readiness gate "
                "happened to name an ad-hoc `zgoal_present_frac`).",
                "",
                "**A result that does not read z_goal is unaffected** -- V3-EXQ-816's "
                "harness carries no defect for its own question. Judge each run by whether "
                "its criteria depend on a live z_goal; if they do, the run measured "
                "something other than what it claimed to.",
                "",
                "**`active_frac` is NOT the signal and must not be read as one.** A zero "
                "fraction is legitimate and common -- a goal-OFF parity arm, a negative "
                "control (V3-EXQ-626b's ARM_NO_BENEFIT), and a correctly-wired run whose "
                "`GoalState` benefit gate never opened because the agent met no resource "
                "all read 0.0 correctly. `writer_calls == 0` is what separates the defect "
                "from those, and it is the only thing flagged here. A run with **no** "
                "`z_goal_stream` block is UNMEASURED, not zero, and never appears below -- "
                "which is almost the whole historical corpus (the runtime backstop landed "
                "in ree-v3 `d6d1da96d9`, 2026-07-27). Full interpretation rules: ree-v3 "
                "`experiments/_lib/z_goal_stream.py`.",
                "",
                "| Run ID | Status | Ticks | writer_calls | active_frac | GoalState |",
                "|--------|--------|-------|--------------|-------------|-----------|",
            ]
            for r in zgoal_dead:
                blk = r.get("z_goal_stream") or {}
                # Indexed runs carry `status`; unclaimed manifests carry `result`.
                status = r.get("status") or r.get("result") or "?"
                frac = blk.get("active_frac")
                frac_s = "n/a" if frac is None else f"{float(frac):.3f}"
                present = blk.get("goal_state_present")
                present_s = ("live" if present is True
                             else "absent" if present is False else "?")
                lines.append(
                    f"| `{r['run_id']}` | {status} | {blk.get('ticks_total', '?')} | "
                    f"**{blk.get('writer_calls', 0)}** | {frac_s} | {present_s} |"
                )
            lines.append("")

        if unclaimed:
            lines += ["## Unclaimed manifests (PASS/FAIL with no claim tags)", ""]
            lines += [
                "These manifests are on disk with PASS/FAIL but their run_id is absent "
                "from `claim_evidence.v1.json`. Common causes: substrate-readiness or "
                "environment-probe diagnostics that intentionally tag no claims, or runs "
                "the runner mis-logged as ERROR/UNKNOWN while the manifest landed cleanly. "
                "Mark discussed by adding the **manifest stem** (filename minus `.json`) "
                "to `discussed_experiment_dirs` -- queue_id-level marking is unsafe here, "
                "see header docstring.",
                "",
                "| Result | Manifest stem | Experiment type | Queue ID | Direction |",
                "|--------|---------------|-----------------|----------|-----------|",
            ]
            for r in unclaimed:
                lines.append(
                    f"| {r['result']} | `{r['manifest_stem']}` | "
                    f"{r['experiment_type'] or '?'} | {r['queue_id'] or '?'} | "
                    f"{r['evidence_direction'] or '?'} |"
                )
            lines.append("")

        if error_manifests:
            lines += ["## Needs diagnosis (ERROR manifests -> /diagnose-errors)", ""]
            lines += [
                "These are durable ERROR-class result manifests on disk -- most "
                "commonly a runner-synthesized record for a crash-before-manifest "
                "(a script that exited non-zero before writing any manifest; "
                "incident V3-EXQ-654e). They are scoring-neutral (no claim tags) "
                "so they never weight claim confidence, but each is a real code "
                "crash that needs `/diagnose-errors` and a re-queue under a NEW "
                "letter. Mark discussed by adding the **manifest stem** (filename "
                "minus `.json`) to `discussed_experiment_dirs`.",
                "",
                "| Outcome | Manifest stem | Queue ID | Machine | Summary |",
                "|---------|---------------|----------|---------|---------|",
            ]
            for r in error_manifests:
                summary = r["result_summary"] or "—"
                lines.append(
                    f"| {r['outcome']} | `{r['manifest_stem']}` | "
                    f"{r['queue_id'] or '?'} | {r['machine'] or '?'} | {summary} |"
                )
            lines.append("")

        if runner_undiscussed:
            lines += ["## Needs discussion (ERROR / UNKNOWN / smoke)", ""]
            lines += [
                "These entries completed in the runner but have no indexed result file "
                "(ERROR/UNKNOWN) or are onboarding smoke runs. They must be discussed and "
                "then added to `discussed_experiment_dirs` in review_tracker.json.",
                "",
                "| Queue ID | Result | Script | Notes |",
                "|----------|--------|--------|-------|",
            ]
            for r in runner_undiscussed:
                script_short = r["script"].split("/")[-1] if r["script"] else "?"
                if r["is_smoke"]:
                    note = "smoke run"
                elif r.get("stale_index"):
                    note = f"{r['result']} (index stale — run build_experiment_indexes.py)"
                else:
                    note = r["result"]
                lines.append(
                    f"| `{r['queue_id']}` | {r['result']} | `{script_short}` | {note} |"
                )
            lines.append("")

    lines += [
        "---",
        "",
        "## How to mark runs as reviewed",
        "",
        "- PASS/FAIL runs (claim-tagged): add run IDs to `reviewed_run_ids` in review_tracker.json",
        "- ERROR/UNKNOWN/smoke: add queue_id or dir_name to `discussed_experiment_dirs` in review_tracker.json",
        "- Unclaimed manifests (PASS/FAIL, no claim tags): add the manifest stem (filename minus `.json`) to `discussed_experiment_dirs`",
        "- ERROR manifests (crash-before-manifest / runner ERROR record): run `/diagnose-errors`, re-queue under a NEW letter, then add the manifest stem to `discussed_experiment_dirs`",
        "- Diagnostic self-route flagged (`precondition_unmet` / `vacuous_pass`): adjudicate via `/failure-autopsy` before the label drives a governance action; clearing the run for review does not clear the adjudication flag (the manifest's `interpretation` is the source of truth -- a re-queued successor supersedes it).",
        "- Diagnostic (`experiment_purpose: \"diagnostic\"`), no confirmed autopsy: ALL diagnostic PASS/FAIL results require a confirmed `/failure-autopsy` target before governance marks them reviewed -- not only ones the indexer flagged untrustworthy. Run `/failure-autopsy` (accepts a PASS target too), then mark reviewed once confirmed.",
        "- Reviewed FAIL with no confirmed autopsy (blind-spot net): a claim-tagged, non-diagnostic FAIL that is already `reviewed` but was never autopsied. Run `/failure-autopsy` on it; the row clears automatically once a CONFIRMED autopsy target covers the run_id. Do NOT re-mark it reviewed to silence it (it is already reviewed -- that is the blind spot). Legacy such runs are grandfathered in `fail_autopsy_grandfather.json` and never listed; do not hand-edit that file.",
        "- Recorded (non-gating) preconditions: nothing to clear. The run is reviewed and closed by the normal PASS/FAIL route above; the recorded finding is an audit trail to read alongside the result, not a flag to adjudicate.",
        "- Update `last_review_utc`, then re-run this script to confirm the list clears.",
        "",
        "```bash",
        "python scripts/generate_pending_review.py",
        "```",
    ]

    OUTPUT.write_text("\n".join(lines) + "\n")
    print(
        f"Written {OUTPUT.relative_to(ROOT)}"
        f" -- {len(runs)} indexed pending, {len(runner_undiscussed)} runner-only pending,"
        f" {len(unclaimed)} unclaimed manifest(s), {len(error_manifests)} ERROR manifest(s)"
    )


def _governance_prompt_for_substrate(status: str) -> str:
    """One-line prompt per dependent invariant based on substrate status."""
    if status == "superseded":
        return "transfer to successor"
    if status in ("retracted", "demoted"):
        return "re-derive or retract"
    if status == "active":
        return "re-confirm (flag can be cleared)"
    # candidate, provisional, and unrecognised values
    return "re-confirm when substrate is promoted"


def _load_substrate_snapshot() -> dict | None:
    """Return prior-run {substrate_id: status} snapshot, or None if absent."""
    if not SUBSTRATE_STATUS_SNAPSHOT.exists():
        return None
    try:
        with open(SUBSTRATE_STATUS_SNAPSHOT) as f:
            data = json.load(f)
        return data.get("substrate_status") or {}
    except Exception as e:
        print(
            f"[warn] could not read {SUBSTRATE_STATUS_SNAPSHOT.name}: {e} "
            "-- treating as first run",
            file=sys.stderr,
        )
        return None


def _write_substrate_snapshot(current: dict[str, str]) -> None:
    """Write {substrate_id: status} snapshot for next run's diff."""
    payload = {
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "substrate_status": current,
    }
    SUBSTRATE_STATUS_SNAPSHOT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def build_substrate_change_section() -> str:
    """Build the 'Substrate changes with dependent invariants' section body.

    Change detection: compares current substrate statuses against a prior-run
    snapshot cached at `evidence/experiments/substrate_status_snapshot.json`.
    - First run (no snapshot): emit the full list of substrates with dependent
      emergent invariants, then write the snapshot.
    - Subsequent runs: emit only substrates whose status changed (or whose
      dependent-invariants list changed membership), and refresh the snapshot.
    - No changes this run: emit the empty-case header.
    """
    if not CLAIMS_YAML.exists():
        return (
            f"{SUBSTRATE_SECTION_HEADER}\n\n"
            "claims.yaml not found -- section skipped.\n"
        )

    with open(CLAIMS_YAML, encoding="utf-8") as f:
        claims = yaml.safe_load(f) or []

    substrates: dict[str, dict] = {}
    invariants: list[dict] = []
    for c in claims:
        if not isinstance(c, dict):
            continue
        ct = c.get("claim_type")
        if ct in SUBSTRATE_CLAIM_TYPES:
            sid = c.get("id")
            if sid:
                substrates[sid] = c
        elif ct == "invariant" and c.get("invariant_type") == "emergent":
            invariants.append(c)

    # substrate_id -> list of dependent invariants
    dependents: dict[str, list[dict]] = {}
    for inv in invariants:
        for s in inv.get("emergent_from") or []:
            dependents.setdefault(s, []).append(inv)

    current_status = {
        sid: sub.get("status", "unknown")
        for sid, sub in substrates.items()
    }
    prior_status = _load_substrate_snapshot()
    first_run = prior_status is None

    # Decide which substrates to report.
    if first_run:
        report_sids = sorted(
            sid for sid in dependents if sid in substrates
        )
        change_note = (
            "First run with change detection enabled -- full list of "
            "substrates with dependent emergent invariants. Subsequent runs "
            "will show only substrates whose status changed."
        )
    else:
        changed = {
            sid for sid, st in current_status.items()
            if prior_status.get(sid) != st
        }
        # Newly-appeared substrates (not in prior snapshot) also count.
        changed |= {
            sid for sid in current_status
            if sid not in prior_status
        }
        report_sids = sorted(sid for sid in changed if sid in dependents)
        change_note = None  # filled in per case below

    _write_substrate_snapshot(current_status)

    lines = [SUBSTRATE_SECTION_HEADER, ""]

    if not report_sids:
        lines += [
            "No substrate status changes this run. "
            "No dependent invariants flagged.",
            "",
        ]
        return "\n".join(lines) + "\n"

    if change_note is None:
        change_note = (
            f"{len(report_sids)} substrate(s) with dependent emergent "
            "invariants changed status since the prior governance run."
        )
    lines += [
        change_note,
        "",
        "| Substrate | Prior | Current | Dependent invariant | Inv status | Flag | Governance prompt |",
        "|-----------|-------|---------|---------------------|------------|------|-------------------|",
    ]
    for sid in report_sids:
        sub = substrates.get(sid)
        if sub is None:
            lines.append(
                f"| `{sid}` | -- | (not found in claims.yaml) | -- | -- | -- | -- |"
            )
            continue
        cur_status = current_status.get(sid, "?")
        prior = "(new)" if first_run or (
            prior_status is not None and sid not in prior_status
        ) else prior_status.get(sid, "?")
        prompt = _governance_prompt_for_substrate(cur_status)
        for inv in sorted(dependents[sid], key=lambda i: i.get("id", "")):
            inv_id = inv.get("id", "?")
            inv_status = inv.get("status", "?")
            flag = bool(inv.get("pending_substrate_reconfirmation"))
            flag_str = "true" if flag else "false"
            lines.append(
                f"| `{sid}` | `{prior}` | `{cur_status}` | `{inv_id}` "
                f"| `{inv_status}` | {flag_str} | {prompt} |"
            )
    lines.append("")
    return "\n".join(lines) + "\n"


def append_substrate_change_section() -> None:
    """Write the substrate-change section into promotion_demotion_recommendations.md.

    Idempotent: if the section already exists in the file, it is replaced.
    Otherwise the section is appended. If the recommendations file does not
    exist yet (e.g., indexer hasn't been run), the section is skipped --
    governance.sh runs the indexer before this script.
    """
    section = build_substrate_change_section()
    if not RECOMMENDATIONS_MD.exists():
        print(
            "[warn] promotion_demotion_recommendations.md not found -- "
            "substrate-change section skipped (run build_experiment_indexes.py first)",
            file=sys.stderr,
        )
        return

    existing = RECOMMENDATIONS_MD.read_text()
    marker = SUBSTRATE_SECTION_HEADER
    idx = existing.find(marker)
    if idx == -1:
        if not existing.endswith("\n"):
            existing += "\n"
        new_content = existing + "\n" + section
    else:
        # Strip the existing section (everything from the marker to EOF) and
        # replace with the regenerated section. The section is always the last
        # block in the file.
        prefix = existing[:idx].rstrip("\n") + "\n\n"
        new_content = prefix + section
    RECOMMENDATIONS_MD.write_text(new_content)
    print(
        f"Appended substrate-change section to "
        f"{RECOMMENDATIONS_MD.relative_to(ROOT)}"
    )


def main():
    reviewed, discussed, last_review_utc = load_tracker()
    indexed_run_ids = load_indexed_run_ids()
    # Run_ids of --dry-run smoke manifests on disk -- excluded from every pending
    # bucket (treated like superseded/degenerate). claim_evidence drops the flag,
    # so the index-derived FAIL/PASS section needs the disk-built set too.
    dry_run_ids = load_dry_run_run_ids()
    flat_only_silent_drop_guard(indexed_run_ids)
    runs = load_pending_entries(reviewed, dry_run_ids)
    pending_run_ids = {r["run_id"] for r in runs}
    runner_undiscussed = load_runner_status_undiscussed(reviewed, discussed, indexed_run_ids)
    unclaimed = [
        u for u in load_unclaimed_manifests(reviewed, discussed, indexed_run_ids)
        if u["run_id"] not in pending_run_ids
    ]
    error_manifests = [
        e for e in load_error_manifests(reviewed, discussed, indexed_run_ids)
        if e["run_id"] not in pending_run_ids
    ]
    # Reviewed-FAIL-without-autopsy blind-spot net (2026-08-08). Reviewed-
    # independent, so it reads claim_evidence directly rather than `runs` (which
    # excludes reviewed run_ids). The pre-existing corpus of such runs is
    # grandfathered on first run so this does not dump the whole FAIL history.
    confirmed_autopsy_run_ids = load_confirmed_autopsy_run_ids()
    fail_candidates = load_reviewed_fail_without_autopsy(
        reviewed, dry_run_ids, confirmed_autopsy_run_ids)
    cand_ids = {r["run_id"] for r in fail_candidates}
    grandfather = load_fail_autopsy_grandfather()
    if grandfather is None:
        seed_fail_autopsy_grandfather(cand_ids)
        grandfather = set(cand_ids)
        print(f"[seed] fail_autopsy_grandfather.json seeded with "
              f"{len(cand_ids)} legacy reviewed-FAIL(s) (not flagged)",
              file=sys.stderr)
    fail_needs_autopsy = [r for r in fail_candidates
                          if r["run_id"] not in grandfather]
    grandfathered_outstanding = len(cand_ids & grandfather)
    write_pending_review(runs, runner_undiscussed, unclaimed,
                         error_manifests, last_review_utc,
                         fail_needs_autopsy=fail_needs_autopsy,
                         grandfathered_outstanding=grandfathered_outstanding)
    append_substrate_change_section()


if __name__ == "__main__":
    main()
