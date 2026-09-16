#!/usr/bin/env python3
"""
recover_stranded_run.py -- the ONLY sanctioned way to hand-recover a stranded run
into a runs/<run_id>/ pack, plus the detector that keeps the tolerated
non-experiment_pack/v1 pack set from growing silently.

Why this exists (evidence/planning/pack_third_writer_path_staged_20260808.md,
approved A+C by the user 2026-09-16):

  A run "strands" when its flat manifest reaches evidence/experiments/ but the
  Phase-3 hub writer never materialised the runs/<run_id>/ pack (batch retry
  never reached the spool, a worker died mid-push, ...). Since the indexer
  scores ONLY the pack (memory: reference_indexer_reads_runs_pack_not_flat), a
  stranded run is silently unscored. Until now recovery was a MANUAL governance
  procedure -- `cp` the flat manifest to runs/<run_id>/manifest.json -- which
  produced a pack in the FLAT schema, verbatim, with no metrics.json sibling.
  Seven such packs landed between 2026-07-20 and 2026-08-09 (the allow-list
  below). The indexer tolerates them (it reads both `status`/`outcome` and
  `claim_ids_tested`/`claim_ids`) but they never get metric display, stop-
  criteria evaluation or duplicate fingerprinting.

  This tool closes that path: it calls the SAME `runpack_for_flat` the hub
  writer and governance.sh use (sync_v3_results.build_runpack_docs is the
  single source of truth for the pack byte-shape), so a hand recovery is
  byte-identical to a hub materialisation.

Rules it enforces, deliberately:

  * It REFUSES to overwrite an existing pack (exit 2). A pack, once it exists,
    is not a pure function of its flat sibling -- /governance and
    /failure-autopsy write adjudications straight onto the pack (see the
    "WHY THIS IS AN ADDITIVE MERGE" comment in sync_v3_results.py). For an
    existing pack use `sync_v3_results.py --heal`; never rebuild.
  * It REFUSES an ineligible flat (exit 2): wrong architecture_epoch, a dry-run
    smoke (all four spellings), or a run_id that is not a V3 run -- the same
    `_is_flat_v3` gate every other writer applies.
  * `--dry-run` prints what would be written and writes nothing.
  * It writes ONLY the three pack files. It does not git-add, commit, or run the
    indexer (CLAUDE.md "Narrow Edits Only"): commit the new pack through
    ree_commit.py and let the next governance regen score it.

Detector (`--scan`): walks every <exp>/runs/<run_id>/manifest.json under the
evidence dir and reports any pack whose schema_version is not
"experiment_pack/v1" and whose "<exp>/runs/<run_id>" is not on the allow-list
below. Exit 3 when any is found. test_recover_stranded_run.py pins the live
corpus against this so the count cannot grow unnoticed. Any new pack outside
experiment_pack/v1 must be produced through this tool (which cannot produce
one) or be explicitly added to the allow-list WITH its landing commit and
reason -- adding to the list is a reviewed decision, not a way to make the
test green.

All stdout/stderr text is ASCII (CLAUDE.md "ASCII-Only in Python Output").

Usage (from anywhere; paths may be absolute or relative to cwd):
    /opt/local/bin/python3 REE_assembly/evidence/experiments/scripts/recover_stranded_run.py \
        --dry-run evidence/experiments/<run_id>.json
    /opt/local/bin/python3 REE_assembly/evidence/experiments/scripts/recover_stranded_run.py \
        evidence/experiments/<run_id>.json           # writes runs/<run_id>/{manifest.json,metrics.json,summary.md}
    /opt/local/bin/python3 REE_assembly/evidence/experiments/scripts/recover_stranded_run.py --scan
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sync_v3_results as _s  # noqa: E402

PACK_SCHEMA = "experiment_pack/v1"
PACK_FILES = ("manifest.json", "metrics.json", "summary.md")

# ---------------------------------------------------------------------------
# ALLOW-LIST of packs that are NOT experiment_pack/v1 and are tolerated as-is.
# Key: "<experiment_type>/runs/<run_id>" relative to evidence/experiments/.
# Mirrored in prose in evidence/experiments/INTERFACE_CONTRACT.md ("Tolerated
# non-experiment_pack/v1 packs"); keep the two in step. Landing commits are the
# commit that ADDED the manifest (git log --diff-filter=A), measured 2026-09-16.
# ---------------------------------------------------------------------------

# Path 3: verbatim copies of the flat manifest, hand-recovered stranded runs.
# manifest.json only; no metrics.json / summary.md sibling. Do NOT regenerate
# (option B was explicitly NOT chosen 2026-09-16: 614 and one 673 carry
# hand-curated corrections).
PATH3_VERBATIM_COPY_PACKS = {
    "v3_exq_614_mech341_p3_behavioural_falsifier_3arm/runs/"
    "v3_exq_614_mech341_p3_behavioural_falsifier_3arm_20260529T191318Z_v3":
        "39664fc7658 2026-07-30 govern: ADMIT recovered V3-EXQ-614 as superseded",
    "v3_exq_673_mech171_vicious_cycle_sleep_disruption/runs/"
    "v3_exq_673_mech171_vicious_cycle_sleep_disruption_20260611T224744Z_v3":
        "1a4ad27d9ee 2026-07-20 evidence: recover 3 stranded V3-EXQ-673 runs",
    "v3_exq_673_mech171_vicious_cycle_sleep_disruption/runs/"
    "v3_exq_673_mech171_vicious_cycle_sleep_disruption_20260612T005615Z_v3":
        "37f1af866f3 2026-07-30 govern: ADMIT 2 recovered stranded runs",
    "v3_exq_673_mech171_vicious_cycle_sleep_disruption/runs/"
    "v3_exq_673_mech171_vicious_cycle_sleep_disruption_20260612T010234Z_v3":
        "1a4ad27d9ee 2026-07-20 evidence: recover 3 stranded V3-EXQ-673 runs",
    "v3_exq_673_mech171_vicious_cycle_sleep_disruption/runs/"
    "v3_exq_673_mech171_vicious_cycle_sleep_disruption_20260612T033246Z_v3":
        "1a4ad27d9ee 2026-07-20 evidence: recover 3 stranded V3-EXQ-673 runs",
    "v3_exq_707c_arc110_loop_segregation_c2_release_repair/runs/"
    "v3_exq_707c_arc110_loop_segregation_c2_release_repair_20260722T041239Z_v3":
        "37f1af866f3 2026-07-30 govern: ADMIT 2 recovered stranded runs",
    "v3_exq_899_arc030_mech307_g0_readiness/runs/"
    "v3_exq_899_arc030_mech307_g0_readiness_20260808T153148Z_v3":
        "7141d4c9190 2026-08-09 evidence: recover stranded V3-EXQ-899 run "
        "(the 7th; landed AFTER the 2026-08-08 investigation counted 6)",
}

# Pre-schema legacy packs (2026-04-06 .. 2026-06-02): written before the
# experiment_pack/v1 projection existed. Historical residue, not an active
# writer. 628 carries schema_version "v1" (not "experiment_pack/v1").
PRE_SCHEMA_LEGACY_PACKS = {
    "v3_exq_241a_sd011_second_source_validation/runs/"
    "v3_exq_241a_sd011_second_source_validation_20260408T190019Z_v3":
        "legacy pre-schema (2026-04-08)",
    "v3_exq_241b_sd011_second_source_info_gain/runs/"
    "v3_exq_241b_sd011_second_source_info_gain_20260408T231939Z_v3":
        "legacy pre-schema (2026-04-08)",
    "v3_exq_247_sd011_sd012_integration/runs/"
    "v3_exq_247_sd011_sd012_integration_20260406T080943Z_v3":
        "legacy pre-schema (2026-04-06)",
    "v3_exq_247_sd011_sd012_integration/runs/"
    "v3_exq_247_sd011_sd012_integration_20260407T105051Z_v3":
        "legacy pre-schema (2026-04-07)",
    "v3_exq_628_mech319_simulation_mode_rule_gate_replay_falsifier_evidence/runs/"
    "v3_exq_628_mech319_simulation_mode_rule_gate_replay_falsifier_evidence_v3_20260602T191625Z":
        "legacy schema_version 'v1' (2026-06-02, mis-ordered run_id)",
}

# Synthetic-assay packs (found 2026-09-16 while building this detector; NOT in
# the 2026-08-08 investigation, which predates them). Written directly by
# REE_assembly/scripts/convergence_signal_synthetic_assay_00N.py -- a FOURTH
# writer, separate from path 3: not stranded-run recoveries, not V3 substrate
# runs (claim_ids: [], status: synthetic_measurement_run_only, no
# architecture_epoch), and no flat sibling. Tolerated as-is pending a decision
# on whether that writer should project through build_runpack_docs.
SYNTHETIC_ASSAY_PACKS = {
    "convergence_signal_synthetic_assay_001/runs/20260909_seed7":
        "52e568f1e16 2026-09-09 Bank synthetic convergence assay 001 seed-7 run",
    "convergence_signal_synthetic_assay_002/runs/20260909_seed11":
        "1d36d59a941 2026-09-09 Bank synthetic convergence assay 002 seed-11 run",
    "convergence_signal_synthetic_assay_003/runs/20260909_seed17":
        "44bf10efba6 2026-09-09 Bank synthetic divergence assay 003 seed-17 run",
    "convergence_signal_synthetic_assay_004/runs/20260909_seed23":
        "42eb7578736 2026-09-09 Bank convergence assay 004 seed-23 manifest",
    "convergence_signal_synthetic_assay_005/runs/20260909_seed29":
        "366ce5a0e17 2026-09-09 Bank convergence assay 005 seed-29 manifest",
    "convergence_signal_synthetic_assay_006/runs/20260909_seed37":
        "6f5b258c4a9 2026-09-09 Bank convergence assay 006 seed-37 manifest",
}

ALLOWLIST = {}
ALLOWLIST.update(PATH3_VERBATIM_COPY_PACKS)
ALLOWLIST.update(PRE_SCHEMA_LEGACY_PACKS)
ALLOWLIST.update(SYNTHETIC_ASSAY_PACKS)


def _say(msg: str, file=None) -> None:
    """Print ASCII-only, replacing anything else rather than crashing."""
    text = str(msg).encode("ascii", "replace").decode("ascii")
    print(text, file=file or sys.stdout, flush=True)


# ---------------------------------------------------------------------------
# Detector
# ---------------------------------------------------------------------------

def pack_key(manifest_path: Path, evidence_dir: Path) -> str:
    """'<experiment_type>/runs/<run_id>' for a runs/*/manifest.json path."""
    rel = Path(manifest_path).resolve().relative_to(Path(evidence_dir).resolve())
    return rel.parent.as_posix()


def scan_non_v1_packs(evidence_dir: Path, allowlist=None) -> dict:
    """Classify every <exp>/runs/<run_id>/manifest.json under evidence_dir.

    Returns {"total": n, "v1": n, "allowlisted": [keys], "unexpected": [(key, reason)],
             "unreadable": [(key, error)]}. Pure: reads only.
    """
    evidence_dir = Path(evidence_dir)
    allowlist = ALLOWLIST if allowlist is None else allowlist
    out = {"total": 0, "v1": 0, "allowlisted": [], "unexpected": [], "unreadable": []}
    for p in sorted(evidence_dir.glob("*/runs/*/manifest.json")):
        out["total"] += 1
        key = pack_key(p, evidence_dir)
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception as exc:  # unreadable is its own bucket, never silently v1
            out["unreadable"].append((key, str(exc)))
            continue
        sv = d.get("schema_version") if isinstance(d, dict) else None
        if sv == PACK_SCHEMA:
            out["v1"] += 1
            continue
        if key in allowlist:
            out["allowlisted"].append(key)
            continue
        flat = evidence_dir / (Path(key).name + ".json")
        verbatim = False
        if flat.is_file():
            try:
                verbatim = json.loads(flat.read_text(encoding="utf-8")) == d
            except Exception:
                verbatim = False
        reason = ("VERBATIM-COPY of flat sibling (path 3 used again)" if verbatim
                  else "schema_version=%r, not on allow-list" % (sv,))
        out["unexpected"].append((key, reason))
    return out


def cmd_scan(evidence_dir: Path) -> int:
    res = scan_non_v1_packs(evidence_dir)
    _say("packs scanned: %d  experiment_pack/v1: %d  allow-listed: %d  unexpected: %d  unreadable: %d"
         % (res["total"], res["v1"], len(res["allowlisted"]), len(res["unexpected"]),
            len(res["unreadable"])))
    missing = sorted(k for k in ALLOWLIST if not (evidence_dir / k / "manifest.json").is_file())
    for k in missing:
        _say("NOTE allow-listed pack no longer on disk (remove it from the list): %s" % k)
    for key, err in res["unreadable"]:
        _say("UNREADABLE %s: %s" % (key, err))
    for key, reason in res["unexpected"]:
        _say("UNEXPECTED %s: %s" % (key, reason))
    if res["unexpected"] or res["unreadable"]:
        _say("FAIL: a pack outside %s is not on the allow-list. Recover stranded runs "
             "through this tool (never cp the flat manifest); a deliberate exception "
             "goes on the allow-list in recover_stranded_run.py AND INTERFACE_CONTRACT.md "
             "with its landing commit." % PACK_SCHEMA)
        return 3
    _say("OK: every pack is %s or allow-listed." % PACK_SCHEMA)
    return 0


# ---------------------------------------------------------------------------
# Recovery
# ---------------------------------------------------------------------------

def recover(flat_path: Path, evidence_dir: Path, dry_run: bool = False) -> tuple[int, str]:
    """Materialise runs/<run_id>/ for one flat manifest.

    Returns (exit_code, run_dir_or_reason). 0 = written (or would be, under
    dry_run); 2 = refused. Never touches an existing pack.
    """
    flat_path = Path(flat_path)
    evidence_dir = Path(evidence_dir)
    if not flat_path.is_file():
        return 2, "REFUSED %s: no such file" % flat_path
    try:
        data = json.loads(flat_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return 2, "REFUSED %s: unreadable JSON -- %s" % (flat_path.name, exc)
    if not isinstance(data, dict):
        return 2, "REFUSED %s: top level is not an object" % flat_path.name
    if flat_path.name == "manifest.json" and flat_path.parent.parent.name == "runs":
        return 2, ("REFUSED %s: that is already a runs/ pack manifest, not a flat "
                   "manifest" % flat_path)

    result = _s.runpack_for_flat(flat_path, evidence_dir)
    if result is None:
        why = []
        if str(data.get("architecture_epoch", "")) != "ree_hybrid_guardrails_v1":
            why.append("architecture_epoch=%r (need ree_hybrid_guardrails_v1)"
                       % data.get("architecture_epoch"))
        if _s._is_dry_run(data, flat_path):
            why.append("dry-run smoke (never scored)")
        rid = str(data.get("run_id", ""))
        if not rid:
            why.append("no run_id")
        elif not rid.endswith("_v3") and not (
                _s._V3_MIDSTRING_RE.search(rid) and _s._is_evidence_grade(data)):
            why.append("run_id %r is not an eligible V3 run" % rid)
        if not why:
            why.append("sync_v3_results._is_flat_v3 gate refused it")
        return 2, "REFUSED %s: not an eligible V3 flat manifest -- %s" % (
            flat_path.name, "; ".join(why))

    run_dir, manifest, metrics_doc, summary = result
    run_dir = Path(run_dir)
    existing = [n for n in PACK_FILES if (run_dir / n).exists()]
    if existing:
        return 2, ("REFUSED %s: pack already exists at %s (%s). A pack is not a pure "
                   "function of its flat sibling once governance has written to it; "
                   "use sync_v3_results.py --heal for an existing pack, never rebuild."
                   % (flat_path.name, run_dir, ", ".join(existing)))

    if dry_run:
        return 0, "DRY-RUN would write %s/{%s} (schema_version=%s, status=%s, claim_ids_tested=%s, metrics=%d)" % (
            run_dir, ",".join(PACK_FILES), manifest.get("schema_version"),
            manifest.get("status"), manifest.get("claim_ids_tested"),
            len(metrics_doc.get("values") or {}))

    run_dir.mkdir(parents=True, exist_ok=True)
    # Same bytes as sync_v3_results.convert_flat_to_runpack.
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (run_dir / "metrics.json").write_text(json.dumps(metrics_doc, indent=2) + "\n", encoding="utf-8")
    (run_dir / "summary.md").write_text(summary, encoding="utf-8")
    return 0, "WROTE %s/{%s} (schema_version=%s, status=%s, claim_ids_tested=%s, metrics=%d)" % (
        run_dir, ",".join(PACK_FILES), manifest.get("schema_version"),
        manifest.get("status"), manifest.get("claim_ids_tested"),
        len(metrics_doc.get("values") or {}))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Recover a stranded run into a proper experiment_pack/v1 pack, "
                    "or --scan for packs outside that schema. ASCII output only.")
    ap.add_argument("flats", nargs="*", help="flat manifest JSON path(s) to recover")
    ap.add_argument("--dry-run", action="store_true", help="report, write nothing")
    ap.add_argument("--scan", action="store_true",
                    help="detector: list packs outside experiment_pack/v1 not on the allow-list (exit 3 if any)")
    ap.add_argument("--evidence-dir", default=str(_s.EVIDENCE_DIR),
                    help="evidence/experiments root (default: this checkout's)")
    args = ap.parse_args(argv)
    evidence_dir = Path(args.evidence_dir).resolve()

    if args.scan:
        if args.flats:
            ap.error("--scan takes no flat paths")
        return cmd_scan(evidence_dir)
    if not args.flats:
        ap.error("give at least one flat manifest path, or --scan")

    worst = 0
    for f in args.flats:
        code, msg = recover(Path(f).resolve(), evidence_dir, dry_run=args.dry_run)
        _say(msg)
        worst = max(worst, code)
    if worst == 0 and not args.dry_run:
        _say("Next: commit the new pack files with ree_commit.py (name the paths explicitly); "
             "do NOT run a full index regen for this -- the next governance regen scores it.")
    return worst


if __name__ == "__main__":
    sys.exit(main())
