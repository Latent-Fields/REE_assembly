#!/usr/bin/env python3
"""
sync_v3_results.py -- convert V3 flat JSON result files into run-pack format.

V3 experiment scripts write a single flat JSON file per run:
    evidence/experiments/{experiment_type}/{experiment_type}_{timestamp}.json

build_experiment_indexes.py expects the run-pack format:
    evidence/experiments/{experiment_type}/runs/{run_id}/manifest.json
    evidence/experiments/{experiment_type}/runs/{run_id}/metrics.json

This script scans for flat V3 JSON files (run_id ending in _v3) and creates
the corresponding run-pack directories so the indexer picks them up.

Already-converted runs are skipped (idempotent).

Usage (from REE_assembly root):
    python evidence/experiments/scripts/sync_v3_results.py
"""

import argparse
import fnmatch
import json
import re
import sys
from pathlib import Path
from datetime import timezone, datetime

ROOT = Path(__file__).resolve().parents[4]  # REE_Working root
EVIDENCE_DIR = Path(__file__).resolve().parents[1]  # REE_assembly/evidence/experiments

# Files to skip -- these live in evidence/experiments/ but are not run result files
SKIP_NAMES = {
    "runner_status.json",
    "review_tracker.json",
    "claim_evidence.v1.json",
    "pending_review.md",
}


# Mis-ordered run_id form `..._v3_<timestamp>` (e.g. V3-EXQ-628:
# v3_exq_628_..._evidence_v3_20260602T191625Z) that the canonical
# `endswith("_v3")` check misses. A cloud Phase-3 evidence result whose runs/
# pack failed to sync lands as a flat manifest with this ordering and was NEVER
# converted -> never scored (silent governance drop, confirmed 2026-06-02..06).
_V3_MIDSTRING_RE = re.compile(r"_v3_\d{8}T\d{6,}Z?$")


# The PRODUCER naming convention for a --dry-run smoke: drivers write
# run_id = f"{EXPERIMENT_TYPE}_dry_{timestamp}" (a literal `_dry_` segment
# followed by the compact UTC stamp). Anchored on that whole shape, NOT on a
# bare "dry" substring: `harm_hub_dry` is a real experiment_type stem
# (v3_exq_395) and would match a loose scan. Shared verbatim with
# generate_pending_review.py and build_experiment_indexes.py.
_DRY_RUN_ID_RE = re.compile(r"_dry_\d{8}T\d{6}Z")


def _is_dry_run(data: dict, flat_path: Path | None = None) -> bool:
    """True for a dry-run / smoke artifact that must never be scored.

    FOUR spellings, and all four are load-bearing -- see the parity test in
    scripts/test_generate_pending_review.py::DryRunArmParityTests, which pins
    this function against generate_pending_review._is_dry_run shape-for-shape.

      1. the top-level `dry_run` flag (the pack_writer chokepoint, 2026-07-12);
      2. `flat_path.name.startswith("_dry_")` -- `write_flat_manifest` marks a
         smoke by PREFIXING the filename and leaves the run_id untouched, so no
         key-based arm can see it;
      3. `run_id.endswith("_dry")` -- a bare suffix with no timestamp;
      4. `_DRY_RUN_ID_RE` -- the `_dry_<stamp>` shape, where the stamp TRAILS
         the marker so arm 3 cannot fire.

    ARM 4 WAS MISSING HERE UNTIL 2026-09-09 (chip-20260909-isdryrun-parity-gap),
    and the divergence ran in BOTH directions: generate_pending_review had 4 but
    not 2/3, this side had 1/2/3 but not 4. Measured on the live corpus, 14
    run_ids were dry to pending_review and NOT dry here -- 3 of them carrying an
    asserting `does_not_support`. That is the dangerous direction for THIS
    module specifically: `_is_flat_v3` consults this predicate to REFUSE
    converting a smoke into a runs/ pack, and the pack is what the indexer
    scores. A false negative here is exactly the MECH-245 contamination the
    docstring below describes.
    """
    if str(data.get("dry_run", "")).strip().lower() in ("true", "1", "yes"):
        return True
    if flat_path is not None and Path(flat_path).name.startswith("_dry_"):
        return True
    run_id = str(data.get("run_id", ""))
    if run_id.endswith("_dry"):
        return True
    return bool(_DRY_RUN_ID_RE.search(run_id))


def _is_evidence_grade(data: dict) -> bool:
    """Evidence-grade = experiment_purpose 'evidence' with >=1 non-empty claim id,
    and not a dry run. Diagnostics / baselines / dry artifacts are excluded."""
    if str(data.get("experiment_purpose", "evidence")).strip() != "evidence":
        return False
    cids = data.get("claim_ids") or data.get("claim_ids_tested") or []
    if not (isinstance(cids, list) and any(str(c).strip() for c in cids)):
        return False
    return not _is_dry_run(data)


def _is_flat_v3(data: dict, flat_path: Path | None = None) -> bool:
    """Return True if this JSON should be converted to a runs/ pack.

    Canonical `..._v3`-suffixed run_ids convert (subject to the dry-run gate
    below). The mis-ordered `..._v3_<timestamp>` form converts ONLY when it is
    an evidence-grade casualty -- this closes the 628-class silent-drop gap for
    evidence runs without sweeping the historical mid-string DIAGNOSTIC backlog
    (claim_ids=[] or experiment_purpose=diagnostic) into pending_review.

    DRY RUNS ARE REFUSED ON BOTH BRANCHES (2026-07-28). Until now `_is_dry_run`
    was consulted only via `_is_evidence_grade` on the mid-string branch, so a
    `--dry-run` smoke with a canonical `..._v3` run_id -- the overwhelmingly
    common shape -- converted unconditionally. That conversion is what actually
    contaminates governance: the flat smoke keeps its `dry_run` flag and is
    ignored downstream, but `build_runpack_docs` emits an `experiment_pack/v1`
    manifest with NO dry_run field, and the pack is what the indexer scores.
    Confirmed on MECH-245, where two 1-seed V3-EXQ-825 smokes became that
    claim's entire negative evidence base (2 FAIL / `weakens`) while its one
    genuine run PASSED. Refusing here is the upstream half of the fix; the
    indexer's own exclusion is the backstop for packs already on disk.
    """
    epoch = str(data.get("architecture_epoch", ""))
    if epoch != "ree_hybrid_guardrails_v1":
        return False
    if _is_dry_run(data, flat_path):
        return False
    run_id = str(data.get("run_id", ""))
    if run_id.endswith("_v3"):
        return True
    if _V3_MIDSTRING_RE.search(run_id) and _is_evidence_grade(data):
        return True
    return False


def _parse_timestamp(ts: str | None) -> str:
    """Normalise a compact timestamp (20260320T193340Z) to ISO-8601."""
    if not ts:
        return ""
    ts = ts.strip()
    # Already ISO-8601
    if "T" in ts and "-" in ts:
        return ts
    # Compact: 20260320T193340Z
    try:
        dt = datetime.strptime(ts, "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return ts


def _derive_experiment_type_and_dir(flat_path: Path, data: dict,
                                    evidence_dir: Path = EVIDENCE_DIR):
    """Resolve (experiment_type, exp_dir) for a flat manifest.

    Mirrors the original convert_flat_to_runpack logic exactly: a flat file
    living directly in evidence/experiments/ derives experiment_type from the
    experiment_type field (or run_id stem); one living in a per-experiment
    subdir uses that dir name. `evidence_dir` is parametrised so an external
    caller (the Phase-3 git writer on the coordinator hub) can resolve paths
    against its OWN checkout root rather than this module's __file__.
    """
    evidence_dir = Path(evidence_dir)
    parent_name = flat_path.parent.name
    if parent_name == evidence_dir.name:
        # File is at top level -- derive experiment_type from the
        # experiment_type field (or run_id stem):
        # run_id format: {experiment_type}_{timestamp}_v3  OR
        #                {timestamp}_{experiment_type}_v3
        raw = str(data.get("experiment_type", str(data.get("run_id", ""))))
        # strip trailing _v3 and timestamp component
        experiment_type = re.sub(r'_\d{8}T\d{6}Z_v3$', '', raw)
        experiment_type = re.sub(r'_v3$', '', experiment_type)
        exp_dir = evidence_dir / experiment_type
    else:
        experiment_type = str(data.get("experiment_type", parent_name))
        exp_dir = flat_path.parent
    return experiment_type, exp_dir


def build_runpack_docs(data: dict, experiment_type: str):
    """Pure field mapping: flat manifest dict -> (manifest, metrics_doc, summary).

    This is the single source of truth for the run-pack byte shape. Both the
    local converter (convert_flat_to_runpack, run by governance.sh) and the
    cloud coordinator's Phase-3 git writer (sync_daemon.phase3_git_writer, via
    runpack_for_flat) call it, so a pack materialised on the hub is byte-
    identical to one materialised locally. Reads `data`; writes nothing.
    """
    # Build manifest.json
    ts_compact = str(data.get("run_timestamp") or data.get("timestamp_utc") or "")
    if not ts_compact:
        # Fall back to unix integer timestamp (legacy scripts use int(time.time()))
        ts_int = data.get("timestamp")
        if ts_int and str(ts_int).isdigit():
            from datetime import datetime as _dt
            ts_compact = _dt.utcfromtimestamp(int(ts_int)).strftime("%Y%m%dT%H%M%SZ")
    ts_iso = _parse_timestamp(ts_compact)

    # Gather claim_ids -- flat JSON may have claim_ids, claim_ids_tested (list),
    # or claim (single string). `claim_ids_tested` is the field the V3 recording
    # standard actually specifies (pack_writer.write_pack's own kwarg name), so a
    # flat manifest using only that key previously converted with claim_ids_tested
    # permanently empty -- confirmed on v3_exq_162_mech137_commit_token_structure
    # (MECH-137/138/139), orphaning its evidence from claim_evidence.v1.json since
    # the indexer reads only the pack copy. 27 packs across the tree carry this or
    # the sibling metrics gap below (see chip-20260808-mech138-orphaned-evidence-
    # indexer-stub); the skip-if-pack-exists guard in convert_flat_to_runpack /
    # sync_daemon._materialize_runpacks means this fix only prevents new
    # occurrences -- existing stubs need an explicit forced regeneration.
    claim_ids = data.get("claim_ids") or data.get("claim_ids_tested") or []
    if not claim_ids and data.get("claim"):
        claim_ids = [data["claim"]]

    # Support "status", "overall_outcome", or "outcome" (flat JSON scripts may use any)
    raw_status = data.get("status") or data.get("overall_outcome") or data.get("outcome", "UNKNOWN")
    raw_upper = str(raw_status).upper()
    if raw_upper in ("PASS", "FAIL", "UNKNOWN"):
        status = raw_upper
    elif raw_upper.startswith("FAIL"):
        status = "FAIL"
    elif raw_upper.startswith("PASS"):
        status = "PASS"
    else:
        # PARTIAL_*, INCONCLUSIVE, etc. -- preserve as-is for human review
        status = raw_upper
    evidence_direction = str(data.get("evidence_direction", "unknown"))
    experiment_purpose = str(data.get("experiment_purpose", "evidence"))

    # Per-claim direction overrides for multi-claim experiments
    raw_per_claim = data.get("evidence_direction_per_claim") or {}
    evidence_direction_per_claim = {}
    if isinstance(raw_per_claim, dict):
        evidence_direction_per_claim = {str(k): str(v) for k, v in raw_per_claim.items()}

    # Warn if multi-claim experiment lacks per-claim directions
    if len(claim_ids) > 1 and not evidence_direction_per_claim:
        print(f"  WARNING: multi-claim experiment ({len(claim_ids)} claims) without "
              f"evidence_direction_per_claim -- blanket '{evidence_direction}' applied to all: "
              f"{claim_ids}")

    manifest = {
        "schema_version": "experiment_pack/v1",
        "architecture_epoch": data.get("architecture_epoch", "ree_hybrid_guardrails_v1"),
        "experiment_type": experiment_type,
        "run_id": str(data["run_id"]),
        "status": status,
        "timestamp_utc": ts_iso,
        "source_repo": {"name": "ree-v3", "commit": "", "branch": "main"},
        "runner": {"name": "ree-v3-harness", "version": "3.0.0"},
        "artifacts": {"metrics_path": "metrics.json", "summary_path": "summary.md"},
        "stop_criteria_version": "stop_criteria/v1",
        "claim_ids_tested": claim_ids,
        "evidence_class": "simulation",
        "evidence_direction": evidence_direction,
        "evidence_direction_per_claim": evidence_direction_per_claim if evidence_direction_per_claim else {},
        "experiment_purpose": experiment_purpose,
        "producer_capabilities": {
            "sd005_split_latent": True,
            "sd004_action_objects": True,
            "sd006_multirate_clock": True,
        },
        "environment": {
            "env_id": "ree.causal_grid_world_v3",
            "env_version": "3.0.0",
            "dynamics_hash": "unknown",
            "reward_hash": "unknown",
            "observation_hash": "unknown",
            "config_hash": "unknown",
            "tier": "causal_grid_world_v3",
        },
        "failure_signatures": [],
    }

    # Dry-run self-identification (2026-07-28). Carry a truthy top-level
    # `dry_run` from the flat manifest into the pack so the pack STANDS ALONE as
    # a smoke artifact. Without this the pack -- which is what the indexer
    # actually scores -- has no dry_run field at any point in its life, so the
    # only carrier of the flag for a given run is its FLAT SIBLING, and
    # `build_experiment_indexes._load_dry_run_run_ids` has to carry it across BY
    # RUN_ID. That cross-file coupling is a live trap for evidence-tree cleanup:
    # deleting a flat dry-run manifest without also deleting its pack silently
    # promotes that pack back to real scored evidence. (The upstream `_is_flat_v3`
    # gate above now refuses dry flats outright, so this branch is unreachable in
    # the normal path -- it is deliberate defence in depth for direct callers of
    # this pure function and for any future regression of that gate.) Conditional
    # add on a truthy value, so every non-dry manifest is byte-identical.
    if _is_dry_run(data):
        manifest["dry_run"] = True

    # Diagnostic adjudication gate (2026-06-06): carry the script's self-routed
    # interpretation block (label + preconditions[] + criteria_non_degenerate)
    # through to the runs/ manifest so build_experiment_indexes._compute_adjudication
    # can flag an untrustworthy self-route. Conditional add => legacy flat
    # manifests without an interpretation block produce byte-identical output.
    interpretation = data.get("interpretation")
    if isinstance(interpretation, dict) and interpretation:
        manifest["interpretation"] = interpretation

    # Experimental Recording Standard always-core provenance (2026-07-16). Carry
    # machine / machine_class / substrate_hash from the flat manifest into the
    # pack so the index-scored runs/ artifact is self-describing. Pre-2026-07-16
    # this mapping was absent, so every pack dropped these even when the flat
    # sibling carried them (all packs read machine_class=null) -- gate-critical,
    # because machine_class is the cloud-authoritative gate class (SD-024) and the
    # arm-fingerprint reuse key (linux-x86_64-py3.10 binding). Conditional add:
    # only emit a key when the flat carries a non-empty value, so legacy flat
    # manifests without provenance produce byte-identical output.
    # `substrate_commit` (2026-07-30) rides the same list: it is the DIAGNOSIS half
    # of the provenance pair, useless if it dies at the flat manifest. substrate_hash
    # proves two runs executed different substrate but is opaque; substrate_commit
    # names the commit so the difference reduces to a `git diff` (the V3-EXQ-614 vs
    # 614a case, where a lambda retune between the runs flipped a verdict FAIL ->
    # PASS while every recorded field looked identical). A dict value is non-empty
    # under the same str().strip() test, so it needs no special-casing here.
    for _prov in ("machine", "machine_class", "substrate_hash", "substrate_commit"):
        _val = data.get(_prov)
        if _val is not None and str(_val).strip() != "":
            manifest[_prov] = _val

    # enabled_default_off_flags / substrate_commit_unavailable (2026-09-01) --
    # carried SEPARATELY from the loop above, not appended to it, because both
    # fields distinguish ABSENT from EMPTY and the loop's `str(_val).strip() != ""`
    # test does not express that. An empty dict happens to survive that test by
    # accident (str({}) == "{}"), which is exactly the kind of implicit dependence
    # that breaks the next time the test is tightened. `is not None` says what is
    # meant: for enabled_default_off_flags, {} is the POSITIVE statement "measured,
    # every known default-off knob confirmed off" and is not interchangeable with
    # omission ("never measured") -- see manifest_core.enabled_default_off_flags_
    # for_agents. Without this mapping the field died at the flat manifest: measured
    # 2026-09-01, 33 flat manifests carried it and 0 of their pack copies did, so no
    # pack-scoring surface could ever see it -- the same whitelist gap that dropped
    # machine_class from every pack before 2026-07-16.
    for _prov in ("enabled_default_off_flags", "substrate_commit_unavailable"):
        _val = data.get(_prov)
        if _val is not None:
            manifest[_prov] = _val

    # Remaining Experimental Recording Standard always-core keys (2026-09-09).
    # manifest_core.ALWAYS_CORE_KEYS is (recording_schema, substrate_hash, machine,
    # machine_class, elapsed_seconds, config, seeds). The four provenance members
    # are carried by the loops above; these are the other three plus
    # recording_schema, and until now NO code path put them in a converted pack.
    # The sanctioned writer (ree-v3 experiments/pack_writer.write_pack, via
    # stamp_recording_core / MANDATORY_CORE_KEYS) stamps all of them into the
    # MANIFEST, so a pack_writer pack and a converted pack disagreed on where --
    # in fact whether -- the always-core lives. Measured 2026-09-09 across the
    # 2931 packs in the tree: 2929 carried no recording_schema at all, so
    # validate_recording.check_manifest reported an always-core gap on essentially
    # every converted pack in the corpus -- a check that can never pass, which is
    # a dead check rather than a signal. The flat sibling carried the fields the
    # whole time; this is the same whitelist-omission shape as machine_class
    # (fixed 2026-07-16) and enabled_default_off_flags (fixed 2026-09-01).
    # `is not None` rather than a truthiness test, for the enabled_default_off_flags
    # reason given above: `config: {}` / `seeds: []` / `elapsed_seconds: 0` are
    # measurements, not absences. Nothing in build_experiment_indexes reads any of
    # these four (confirmed 2026-09-09: zero references to recording_schema,
    # elapsed_seconds or seeds, and no manifest read of config), so this changes
    # the pack's SELF-DESCRIPTION and the recording-standard verdict, never a
    # score.
    for _core in ("recording_schema", "elapsed_seconds", "config", "seeds"):
        _val = data.get(_core)
        if _val is not None:
            manifest[_core] = _val

    # z_goal-stream liveness (2026-07-27). Carry the runtime backstop's counter
    # block (ree-v3 experiments/_lib/z_goal_stream.py) through to the pack, which
    # is what build_experiment_indexes scores -- this mapping is a WHITELIST, so
    # without this line the block dies at the flat manifest and no derived surface
    # can ever see it. `update_z_goal` is the sole z_goal writer in the substrate;
    # a driver that hand-rolls its inner loop and omits the call runs with z_goal
    # pinned at zero-init and every z_goal consumer silently no-ops (V3-EXQ-626,
    # V3-EXQ-830). Conditional add on a non-empty dict, so legacy flats (the whole
    # historical corpus) produce byte-identical output and an ABSENT block keeps
    # meaning UNMEASURED rather than measured-zero.
    _zgs = data.get("z_goal_stream")
    if isinstance(_zgs, dict) and _zgs:
        manifest["z_goal_stream"] = _zgs

    # Build metrics.json. 766-style diagnostic manifests store their scalar
    # readouts under `aggregates` (paired with `thresholds`) rather than a
    # top-level `metrics` dict, which left metrics.values={} on the scored pack.
    # Fall back to `aggregates`, then `summary_metrics` (the field name several
    # multi-arm V3 driver scripts actually use -- confirmed empty-values.json on
    # v3_exq_162_mech137_commit_token_structure, whose flat manifest carries a
    # populated `summary_metrics` block that neither prior fallback reads), so
    # the quantitative readouts survive into the runs/ pack under any of the
    # three spellings currently in use across the experiment corpus.
    raw_metrics = data.get("metrics")
    if not raw_metrics:
        agg = data.get("aggregates")
        if isinstance(agg, dict) and agg:
            raw_metrics = dict(agg)
    if not raw_metrics:
        summ = data.get("summary_metrics")
        if isinstance(summ, dict) and summ:
            raw_metrics = dict(summ)
    if not raw_metrics:
        # Fourth spelling: `readout` (2026-09-09). Same scalar-dict shape as
        # `aggregates`, paired with `pre_registered_thresholds` instead of
        # `thresholds` -- confirmed on v3_exq_1014_ext002_lineage_e3_latching_
        # repertoire_spike, whose pack scored with values={} while its flat
        # sibling carried latched_fraction / casualty_latched_fraction /
        # floor_fresh_action_count. An empty `values` is not merely cosmetic on
        # the scored artifact: build_experiment_indexes reads ONLY numeric
        # metrics.values entries, so with none of them (a) no `fail_if` stop
        # threshold can ever fire -- `run.metrics.get(metric)` is None, the check
        # is skipped, and final_status falls back to the manifest's self-declared
        # status, which is what claim_evidence.v1.json records and what drives
        # auto-inferred evidence direction; (b) the duplicate-emission
        # fingerprint is skipped entirely, so a byte-identical re-emission is
        # never auto-superseded and both copies score; (c) no deltas and no
        # key-metrics columns. 1007 of 2931 packs sat at values={} when this was
        # measured; `readout` accounts for the 1014 shape specifically.
        ro = data.get("readout")
        if isinstance(ro, dict) and ro:
            raw_metrics = dict(ro)
    if not isinstance(raw_metrics, dict):
        raw_metrics = {}
    metrics_doc = {
        "schema_version": "metrics/v1",
        "values": raw_metrics,
    }

    # Build summary.md
    summary = data.get("summary_markdown", "")
    if not summary:
        crit = data.get("criteria") or {}
        if isinstance(crit, list):
            # Newer schema: criteria is a list of {name, load_bearing, passed} objects.
            n_pass = sum(1 for c in crit if (c.get("passed") if isinstance(c, dict) else c))
            n_total = len(crit)
        else:
            n_pass = sum(1 for v in crit.values() if v)
            n_total = len(crit)
        summary = f"# {experiment_type}\n\nStatus: **{status}**"
        if n_total:
            summary += f"  ({n_pass}/{n_total} criteria)"
        summary += "\n"

    return manifest, metrics_doc, summary


def runpack_for_flat(flat_path, evidence_dir):
    """External-caller entry point (Phase-3 coordinator git writer).

    Given a flat manifest already written on disk at `flat_path` and the
    evidence/experiments directory it lives under (`evidence_dir`, the caller's
    own checkout root), return
        (run_dir, manifest_doc, metrics_doc, summary)
    for the canonical runs/<run_id>/ pack, or None if the flat manifest is not
    an eligible V3 run (same `_is_flat_v3` gate convert_flat_to_runpack uses).

    Pure: reads `flat_path` but writes nothing and creates no directories. The
    caller owns the write + git-add mechanics and the skip-if-pack-exists
    decision. Reuses the SAME field mapping (build_runpack_docs) and directory
    derivation (_derive_experiment_type_and_dir) as convert_flat_to_runpack so
    the pack byte-shape is identical whether materialised locally by
    governance.sh or on the hub by the Phase-3 writer.
    """
    flat_path = Path(flat_path)
    try:
        data = json.loads(flat_path.read_text(encoding="utf-8"))
    except Exception:
        return None
    if not _is_flat_v3(data):
        return None
    run_id = str(data.get("run_id", ""))
    if not run_id:
        return None
    experiment_type, exp_dir = _derive_experiment_type_and_dir(
        flat_path, data, evidence_dir)
    run_dir = exp_dir / "runs" / run_id
    manifest, metrics_doc, summary = build_runpack_docs(data, experiment_type)
    return (run_dir, manifest, metrics_doc, summary)


def convert_flat_to_runpack(flat_path: Path) -> str:
    """
    Convert a flat V3 JSON file to a run-pack directory.
    Returns the run_id if conversion happened, '' if skipped.
    """
    try:
        data = json.loads(flat_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"  [skip] {flat_path.name}: read error -- {exc}", flush=True)
        return ""

    if not _is_flat_v3(data, flat_path):
        return ""

    run_id = str(data["run_id"])
    experiment_type, exp_dir = _derive_experiment_type_and_dir(flat_path, data)

    # Destination: exp_dir/runs/{run_id}/
    run_dir = exp_dir / "runs" / run_id
    if (run_dir / "manifest.json").exists():
        return ""  # already converted

    run_dir.mkdir(parents=True, exist_ok=True)

    manifest, metrics_doc, summary = build_runpack_docs(data, experiment_type)

    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (run_dir / "metrics.json").write_text(json.dumps(metrics_doc, indent=2) + "\n", encoding="utf-8")
    (run_dir / "summary.md").write_text(summary, encoding="utf-8")

    return run_id


# ---------------------------------------------------------------------------
# Opt-in heal of ALREADY-CONVERTED packs (2026-09-09)
# ---------------------------------------------------------------------------
#
# Every mapping fix in build_runpack_docs above is FORWARD-ONLY: both
# convert_flat_to_runpack and sync_daemon._materialize_runpacks skip when the
# pack already exists, so a pack converted before a fix keeps the gap forever.
# This section is the explicit, opt-in backfill for that.
#
# WHY THIS IS AN ADDITIVE MERGE AND NOT A REGENERATION -- read before "simplifying"
# it into a `--force` that just rewrites the pack from build_runpack_docs.
#
# build_runpack_docs is a WHITELIST: it emits exactly the keys it names. But a
# run-pack manifest is NOT a pure function of its flat sibling once it exists --
# /governance and /failure-autopsy write their adjudications directly onto the
# PACK, and the flat manifest stays the raw as-emitted artifact. Measured
# 2026-09-09 over the 1638 packs that still have a reachable flat source, a
# full regeneration would have:
#   - DROPPED 1124 pack-only key occurrences across 77 keys, including
#     evidence_direction_note (643), epistemic_category (94), superseded_by (62),
#     scoring_excluded (15), governance_applied_utc (11), source_autopsy (8),
#     failure_autopsy_ref (6), governance_override_from/utc, adjudicated_by_autopsy,
#     claim_tag_removed_by_governance;
#   - REVERTED 619 values, including evidence_direction (238) and status (27) --
#     e.g. status SUPERSEDED -> FAIL on v3_exq_085h, evidence_direction
#     supports -> mixed on v3_exq_033, and evidence_direction_per_claim
#     {MECH-071: weakens, ...} -> {} on v3_exq_026.
# That is a wholesale revert of governance state wearing the costume of a
# housekeeping backfill, so the destructive form is deliberately NOT offered.
#
# The heal therefore only ever ADDS a key that the pack does not already have,
# from an explicit allowlist, and the VALUE still comes from build_runpack_docs
# (no field is hand-authored here). It never overwrites and never deletes.

# Manifest keys the heal is allowed to add -- the six Experimental Recording
# Standard always-core members that build_runpack_docs started carrying on
# 2026-09-09.
#
# The first four are safe because NOTHING in build_experiment_indexes reads
# them (verified 2026-09-09: zero references to recording_schema,
# elapsed_seconds or seeds, and no manifest read of config), so adding them
# changes the pack's SELF-DESCRIPTION and its validate_recording verdict and
# cannot move a score.
#
# substrate_hash and machine_class were held back that day pending their own
# measurement, because the indexer DOES reference both (17 and 18 references --
# the SD-024 gate class and the arm-fingerprint reuse key). That measurement ran
# on 2026-09-09; see evidence/planning/runpack_always_core_heal_20260909.md
# sec 5. It cleared them, for a reason worth stating here so it is not
# re-litigated: build_experiment_indexes ALREADY backfills machine_class /
# substrate_hash / machine onto the pack from the SAME flat sibling this heal
# reads, unconditionally, via _FLAT_PROVENANCE_BACKFILL_FIELDS. Measured over
# all 56 affected packs: the two resolvers select the identical flat file 56/56,
# and the value the heal writes equals the value the indexer had already read
# 112/112. Of the indexer's references, none is a comparison, grouping or gate --
# they are the dataclass field, that backfill, and two emit-into-the-index sites;
# the arm-fingerprint reuse key is a NESTED
# arm_results[].arm_fingerprint.machine_class that this heal never touches.
# Confirmed empirically by a full pre/post index rebuild against a run-to-run
# noise control: derived `runs` rows byte-identical, zero status / direction /
# outcome change corpus-wide, arm_fingerprint_index.json hash-identical.
# So the heal makes the pack SELF-DESCRIBING instead of dependent on its flat
# sibling still being reachable -- it does not move a score.
HEAL_MANIFEST_KEYS = ("recording_schema", "elapsed_seconds", "config", "seeds",
                      "substrate_hash", "machine_class")


def heal_pack(flat_path: Path, evidence_dir: Path | None = None,
              manifest_keys=HEAL_MANIFEST_KEYS,
              fill_metrics: bool = False,
              apply: bool = False) -> dict | None:
    """Additively backfill one already-converted pack from its flat sibling.

    Returns None when there is nothing to do (not an eligible V3 flat, no pack
    on disk, or the pack already carries everything). Otherwise returns a record
    describing the change; the change is only WRITTEN when `apply` is True.

    `fill_metrics` additionally copies metrics.values when -- and only when --
    the pack's current `values` is EMPTY and build_runpack_docs produces a
    non-empty one. That is a SCORING-RELEVANT edit (an empty `values` makes
    every fail_if rule unevaluable and suppresses the duplicate-emission
    fingerprint), which is why it is off by default and separately flagged.
    """
    evidence_dir = Path(evidence_dir) if evidence_dir is not None else EVIDENCE_DIR
    try:
        data = json.loads(flat_path.read_text(encoding="utf-8"))
    except Exception:
        return None
    if not _is_flat_v3(data, flat_path):
        return None
    run_id = str(data.get("run_id", ""))
    if not run_id:
        return None

    experiment_type, exp_dir = _derive_experiment_type_and_dir(
        flat_path, data, evidence_dir)
    run_dir = exp_dir / "runs" / run_id
    manifest_path = run_dir / "manifest.json"
    if not manifest_path.is_file():
        return None  # nothing converted yet -- that is convert_flat_to_runpack's job

    try:
        old_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception:
        return None

    new_manifest, new_metrics, _summary = build_runpack_docs(data, experiment_type)

    added = {}
    for key in manifest_keys:
        if key in new_manifest and key not in old_manifest:
            added[key] = new_manifest[key]

    metrics_path = run_dir / "metrics.json"
    metrics_before = None
    metrics_after = None
    if fill_metrics and metrics_path.is_file():
        try:
            old_metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
        except Exception:
            old_metrics = None
        if isinstance(old_metrics, dict) and (old_metrics.get("values") or {}) == {}:
            candidate = new_metrics.get("values") or {}
            if candidate:
                metrics_before = {}
                metrics_after = candidate

    if not added and metrics_after is None:
        return None

    record = {
        "run_id": run_id,
        "experiment_type": experiment_type,
        "run_dir": str(run_dir),
        "flat": str(flat_path),
        "added_manifest_keys": sorted(added),
        "metrics_values_filled": sorted(metrics_after) if metrics_after else [],
    }

    if apply:
        if added:
            merged = dict(old_manifest)
            merged.update(added)
            manifest_path.write_text(
                json.dumps(merged, indent=2) + "\n", encoding="utf-8")
        if metrics_after is not None:
            doc = json.loads(metrics_path.read_text(encoding="utf-8"))
            doc["values"] = metrics_after
            metrics_path.write_text(
                json.dumps(doc, indent=2) + "\n", encoding="utf-8")

    return record


def _flat_candidates():
    """The same file set main()'s conversion scan walks."""
    all_json = sorted(set(EVIDENCE_DIR.glob("*.json")) | set(EVIDENCE_DIR.glob("*/*.json")))
    for json_path in all_json:
        if json_path.name in SKIP_NAMES:
            continue
        if "runs" in json_path.parts:
            continue
        yield json_path


def _dirty_paths(repo_root: Path) -> set:
    """Repo-relative paths with uncommitted changes, for the skip-dirty guard.

    A pack manifest that is ALREADY dirty is carrying another session's
    uncommitted work (typically a live /governance or /failure-autopsy
    adjudication). Healing it is a read-modify-write of that session's content:
    the heal's write-back preserves their edit, and the next commit that names
    the path lands their unfinished work early, under the wrong message and the
    wrong task -- the contamination hazard in CLAUDE.md "Concurrency Rules".
    Confirmed live 2026-09-09: two packs were mid-adjudication when this heal
    first ran. Skipping is the cheap fix -- the pack simply gets healed on a
    later run, once its owner has committed.
    """
    import subprocess
    try:
        out = subprocess.run(
            ["git", "-C", str(repo_root), "status", "--porcelain"],
            capture_output=True, text=True, timeout=120)
    except Exception:
        return set()
    if out.returncode != 0:
        return set()
    dirty = set()
    for line in out.stdout.splitlines():
        if len(line) > 3:
            dirty.add(line[3:].strip().strip('"'))
    return dirty


def run_heal(only=None, fill_metrics=False, apply=False, limit=None,
             exclude_run_ids=(), skip_dirty=True):
    """Drive heal_pack over the corpus. Returns the list of change records."""
    exclude = set(exclude_run_ids or ())
    repo_root = EVIDENCE_DIR.parents[1]  # REE_assembly
    dirty = _dirty_paths(repo_root) if skip_dirty else set()
    n_skipped_dirty = 0
    records = []
    for flat_path in _flat_candidates():
        rec = heal_pack(flat_path, fill_metrics=fill_metrics, apply=False)
        if rec is None:
            continue
        if rec["run_id"] in exclude:
            print(f"  [excluded] {rec['run_id']}", flush=True)
            continue
        if only and not (fnmatch.fnmatch(rec["run_id"], only)
                         or fnmatch.fnmatch(rec["experiment_type"], only)):
            continue
        if dirty:
            rel = Path(rec["run_dir"]).relative_to(repo_root)
            if any(str(rel / n) in dirty for n in ("manifest.json", "metrics.json")):
                print(f"  [skip dirty] {rec['run_id']} -- uncommitted work present",
                      flush=True)
                n_skipped_dirty += 1
                continue
        if limit is not None and len(records) >= limit:
            break
        if apply:
            rec = heal_pack(flat_path, fill_metrics=fill_metrics, apply=True)
            if rec is None:
                continue
        records.append(rec)
    if n_skipped_dirty:
        print(f"  ({n_skipped_dirty} pack(s) skipped as dirty -- another session "
              f"has uncommitted work there; re-run later)", flush=True)
    return records


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Convert V3 flat JSON results into run-packs; "
                    "optionally heal already-converted packs.")
    parser.add_argument(
        "--heal", action="store_true",
        help="Additively backfill always-core keys onto EXISTING packs. "
             "Off by default: governance.sh and the hub sync_daemon call this "
             "script bare and must keep the pure skip-if-exists behaviour.")
    parser.add_argument(
        "--only", metavar="GLOB",
        help="With --heal, restrict to run_ids or experiment_types matching GLOB.")
    parser.add_argument(
        "--limit", type=int, metavar="N",
        help="With --heal, stop after N packs (batching).")
    parser.add_argument(
        "--fill-metrics", action="store_true",
        help="With --heal, also populate metrics.json values when currently "
             "empty. SCORING-RELEVANT -- quantify before landing.")
    parser.add_argument(
        "--exclude-run-id", action="append", default=[], metavar="RUN_ID",
        help="With --heal, skip this run_id (repeatable).")
    parser.add_argument(
        "--no-skip-dirty", action="store_true",
        help="With --heal, do NOT skip packs that already have uncommitted "
             "changes. Off by default; healing a dirty pack read-modify-writes "
             "another session's in-progress work.")
    parser.add_argument(
        "--apply", action="store_true",
        help="With --heal, actually write. Without it the heal is a dry run.")
    args = parser.parse_args(argv)

    if args.heal:
        records = run_heal(only=args.only, fill_metrics=args.fill_metrics,
                           apply=args.apply, limit=args.limit,
                           exclude_run_ids=args.exclude_run_id,
                           skip_dirty=not args.no_skip_dirty)
        n_keys = sum(len(r["added_manifest_keys"]) for r in records)
        n_met = sum(1 for r in records if r["metrics_values_filled"])
        verb = "healed" if args.apply else "would heal"
        print(f"sync_v3_results --heal: {verb} {len(records)} pack(s); "
              f"{n_keys} manifest key(s) added, {n_met} metrics.values filled.",
              flush=True)
        return 0

    converted = []
    skipped_norun = 0

    # Scan flat JSON files -- both at top level and one dir deep
    # Top-level: evidence/experiments/*.json
    # Sub-level:  evidence/experiments/{exp_type}/*.json
    for json_path in _flat_candidates():
        run_id = convert_flat_to_runpack(json_path)
        if run_id:
            print(f"  converted: {run_id}", flush=True)
            converted.append(run_id)
        else:
            skipped_norun += 1

    print(f"\nsync_v3_results: {len(converted)} new run-pack(s) created, "
          f"{skipped_norun} file(s) skipped (already converted or non-run).",
          flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
