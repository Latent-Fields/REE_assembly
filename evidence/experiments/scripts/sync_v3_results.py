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


def _is_dry_run(data: dict, flat_path: Path | None = None) -> bool:
    """True for a dry-run / smoke artifact that must never be scored.

    `flat_path` adds the third spelling: `pack_writer.write_flat_manifest`
    marks a smoke by PREFIXING the filename `_dry_<run_id>.json` and leaves the
    run_id itself untouched, so neither key-based arm sees it.
    """
    if str(data.get("dry_run", "")).strip().lower() in ("true", "1", "yes"):
        return True
    if flat_path is not None and flat_path.name.startswith("_dry_"):
        return True
    return str(data.get("run_id", "")).endswith("_dry")


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


def main():
    converted = []
    skipped_norun = 0

    # Scan flat JSON files -- both at top level and one dir deep
    # Top-level: evidence/experiments/*.json
    # Sub-level:  evidence/experiments/{exp_type}/*.json
    all_json = sorted(set(EVIDENCE_DIR.glob("*.json")) | set(EVIDENCE_DIR.glob("*/*.json")))
    for json_path in all_json:
        if json_path.name in SKIP_NAMES:
            continue
        # Skip files inside runs/ subdirectories (already converted)
        if "runs" in json_path.parts:
            continue
        run_id = convert_flat_to_runpack(json_path)
        if run_id:
            print(f"  converted: {run_id}", flush=True)
            converted.append(run_id)
        else:
            skipped_norun += 1

    print(f"\nsync_v3_results: {len(converted)} new run-pack(s) created, "
          f"{skipped_norun} file(s) skipped (already converted or non-run).",
          flush=True)


if __name__ == "__main__":
    main()
