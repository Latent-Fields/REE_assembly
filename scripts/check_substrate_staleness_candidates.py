#!/usr/bin/env python3
"""Substrate-drift candidate report (Phase 0 -- INSTRUMENT ONLY, read-only).

Design plan: REE_assembly/evidence/planning/substrate_stability_and_drift_detection_plan.md

WHY THIS EXISTS
---------------
`ree-v3/experiments/_lib/arm_fingerprint.py` already stamps every recent manifest with a
content-addressed `substrate_hash` (over `ree_core/**` + a few shared experiment libs), and
`evidence/experiments/scripts/build_experiment_indexes.py` (landed 2026-06-02, predates this
script) already HONORS `pending_retest_after_substrate` / `superseded_by_substrate` fields on
a manifest by excluding it from claim confidence/conflict scoring. What is missing is the
PRODUCER: nothing computes whether a claim's recorded substrate has actually moved since its
evidence was gathered. A human has always had to notice this by hand.

Motivating incident: V3-EXQ-875 (MECH-471) ran ~20.5h wall-clock and self-reported
`substrate_stable_across_run: false` -- six `ree_core`-touching commits landed on `ree-v3`
`main` during the run (see `failure_autopsy_V3-EXQ-875_2026-08-03.md`). Benign that time
(all six were default-off flags this run's config never enabled), but nothing before this
script could tell you, for a GIVEN CLAIM's already-recorded evidence, whether `main` has since
drifted in a way that touches it.

WHAT THIS DOES (Phase 0 -- zero validity risk, mirrors arm_reuse_report.py's own posture)
------------------------------------------------------------------------------------------
1. Scans FLAT claim-tagged manifests under `evidence/experiments/*.json` (not the
   `**/runs/**/manifest.json` pack -- see the plan doc section 4.2 for why: the flat file is
   the human/operator-editable override layer `pending_retest_after_substrate` lives on).
2. For each with a recorded top-level `substrate_hash`, fetches `origin/main` in the sibling
   `ree-v3` checkout, materialises a THROWAWAY DETACHED WORKTREE there, and calls the REAL
   `compute_substrate_hash()` found in that worktree's own copy of `arm_fingerprint.py` --
   never reimplemented, so a subtly different reimplementation cannot manufacture a false
   drift signal or a false all-clear.
3. Compares. A mismatch is a DRIFT CANDIDATE, never an automatic flag -- this script NEVER
   writes to any manifest. If `substrate_commit.commit` is also recorded, additionally diffs
   `<recorded-commit>..origin/main` over the same globs so the report names which files
   changed, not just "something changed."
4. Manifests already carrying any of the four staleness-gate fields, or already
   `evidence_direction: superseded`, are excluded from "new candidates" and reported
   separately as "already actioned."
5. Manifests with no recorded `substrate_hash` (pre-recording-standard) are bucketed as
   "no substrate identity recorded" -- reported, never silently dropped.

Nothing here can invalidate an experiment or alter scoring. Read the report, then a human
decides whether to hand-edit a flat manifest's `pending_retest_after_substrate` (or the
per-claim variants) -- exactly as `/failure-autopsy` already does today for other reasons.

Usage (from REE_assembly/ root):
    /opt/local/bin/python3 scripts/check_substrate_staleness_candidates.py
    /opt/local/bin/python3 scripts/check_substrate_staleness_candidates.py --exp-dir evidence/experiments
    /opt/local/bin/python3 scripts/check_substrate_staleness_candidates.py --ree-v3-root ../ree-v3 --ref origin/main

ASCII-only stdout per repo convention.
"""

from __future__ import annotations

import argparse
import glob
import json
import shutil
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]  # REE_assembly root
DEFAULT_EXP_DIR = REPO_ROOT / "evidence" / "experiments"
DEFAULT_REE_V3_ROOT = REPO_ROOT.parent / "ree-v3"

# The four fields the existing gate in build_experiment_indexes.py already honors.
_ALREADY_ACTIONED_FIELDS = (
    "pending_retest_after_substrate",
    "pending_retest_after_substrate_per_claim",
    "superseded_by_substrate",
    "superseded_by_substrate_per_claim",
)


def _run(cmd: List[str], cwd: Optional[Path] = None) -> Tuple[int, str, str]:
    proc = subprocess.run(
        cmd, cwd=str(cwd) if cwd else None,
        capture_output=True, text=True,
    )
    return proc.returncode, proc.stdout, proc.stderr


def _load_json(path: Path) -> Optional[Dict[str, Any]]:
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError):
        return None


def _is_dry_run(manifest: Dict[str, Any]) -> bool:
    val = manifest.get("dry_run")
    if isinstance(val, bool):
        return val
    if isinstance(val, str):
        return val.strip().lower() in ("true", "1", "yes")
    return False


def _already_actioned(manifest: Dict[str, Any]) -> bool:
    if str(manifest.get("evidence_direction", "")) == "superseded":
        return True
    for key in _ALREADY_ACTIONED_FIELDS:
        val = manifest.get(key)
        if isinstance(val, bool) and val:
            return True
        if isinstance(val, str) and val.strip():
            return True
        if isinstance(val, (list, dict)) and val:
            return True
    return False


def load_flat_claim_tagged_manifests(exp_dir: Path) -> List[Tuple[Path, Dict[str, Any]]]:
    """Flat (non-nested) manifests directly under exp_dir with at least one claim_id."""
    out: List[Tuple[Path, Dict[str, Any]]] = []
    for f in sorted(glob.glob(str(exp_dir / "*.json"))):
        path = Path(f)
        manifest = _load_json(path)
        if not isinstance(manifest, dict):
            continue
        claim_ids = manifest.get("claim_ids") or []
        if not claim_ids:
            continue
        if _is_dry_run(manifest):
            continue
        out.append((path, manifest))
    return out


class _CurrentSubstrate:
    """Materialises a throwaway detached worktree at `ref` and imports the REAL
    compute_substrate_hash from that worktree's own arm_fingerprint.py.

    Cleans itself up via close()/context-manager -- never leaves a stray worktree behind.
    """

    def __init__(self, ree_v3_root: Path, ref: str):
        self.ree_v3_root = ree_v3_root
        self.ref = ref
        self._scratch: Optional[Path] = None
        self.hash_info: Optional[Dict[str, Any]] = None

    def __enter__(self) -> "_CurrentSubstrate":
        rc, out, err = _run(["git", "fetch", "origin"], cwd=self.ree_v3_root)
        if rc != 0:
            raise RuntimeError(f"git fetch origin failed in {self.ree_v3_root}: {err.strip()}")

        scratch_parent = Path(tempfile.gettempdir())
        self._scratch = scratch_parent / f"substrate-staleness-check-{uuid.uuid4().hex[:10]}"
        rc, out, err = _run(
            ["git", "worktree", "add", "--detach", str(self._scratch), self.ref],
            cwd=self.ree_v3_root,
        )
        if rc != 0:
            raise RuntimeError(
                f"git worktree add --detach {self._scratch} {self.ref} failed: {err.strip()}"
            )

        arm_fp_path = self._scratch / "experiments" / "_lib" / "arm_fingerprint.py"
        if not arm_fp_path.exists():
            raise RuntimeError(f"arm_fingerprint.py not found at {arm_fp_path}")

        import importlib.util
        spec = importlib.util.spec_from_file_location("arm_fingerprint_worktree", arm_fp_path)
        mod = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(mod)

        self.hash_info = mod.compute_substrate_hash(repo_root=self._scratch)
        return self

    def __exit__(self, *exc) -> None:
        if self._scratch is None:
            return
        _run(["git", "worktree", "remove", "--force", str(self._scratch)], cwd=self.ree_v3_root)
        _run(["git", "worktree", "prune"], cwd=self.ree_v3_root)
        if self._scratch.exists():
            shutil.rmtree(self._scratch, ignore_errors=True)


def _display_path(path: Path) -> str:
    umbrella_root = REPO_ROOT.parent  # .../REE_Working
    try:
        return str(path.relative_to(umbrella_root))
    except ValueError:
        return str(path)


def _diff_changed_files(
    ree_v3_root: Path, recorded_commit: str, ref: str, globs: List[str]
) -> Optional[List[str]]:
    """git diff --name-only recorded_commit..ref over the substrate globs. None if undiffable."""
    pathspecs = []
    for g in globs:
        # arm_fingerprint globs are already repo-relative fnmatch patterns; git diff -- takes
        # them as pathspecs directly for the common cases used here (dir/**, single files).
        pathspecs.append(g.replace("/**/*.py", "/").rstrip("*"))
    rc, out, err = _run(
        ["git", "diff", "--name-only", f"{recorded_commit}..{ref}", "--"] + pathspecs,
        cwd=ree_v3_root,
    )
    if rc != 0:
        return None
    files = [ln.strip() for ln in out.splitlines() if ln.strip()]
    return files


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--exp-dir", default=str(DEFAULT_EXP_DIR))
    ap.add_argument("--ree-v3-root", default=str(DEFAULT_REE_V3_ROOT))
    ap.add_argument("--ref", default="origin/main")
    args = ap.parse_args()

    exp_dir = Path(args.exp_dir)
    ree_v3_root = Path(args.ree_v3_root)

    manifests = load_flat_claim_tagged_manifests(exp_dir)
    print("substrate-staleness candidate report (READ-ONLY, Phase 0)  --  %d claim-tagged flat manifest(s)" % len(manifests))
    print("source: %s" % exp_dir)
    print("comparing against: %s (ree-v3 root: %s)" % (args.ref, ree_v3_root))
    print()

    no_identity: List[Path] = []
    current: List[Path] = []
    already_actioned: List[Tuple[Path, Dict[str, Any]]] = []
    candidates: List[Tuple[Path, Dict[str, Any]]] = []
    current_globs: List[str] = []

    try:
        with _CurrentSubstrate(ree_v3_root, args.ref) as cur:
            current_hash = cur.hash_info["substrate_hash"]
            current_n_files = cur.hash_info["n_files"]
            current_globs = cur.hash_info.get("globs", [])

            for path, manifest in manifests:
                recorded_hash = manifest.get("substrate_hash")
                if not recorded_hash:
                    no_identity.append(path)
                    continue
                if recorded_hash == current_hash:
                    current.append(path)
                    continue
                if _already_actioned(manifest):
                    already_actioned.append((path, manifest))
                    continue
                candidates.append((path, manifest))
    except RuntimeError as e:
        print("ERROR: could not resolve current substrate identity: %s" % e)
        return 1

    print("current substrate (%s): %d file(s), hash %s" % (args.ref, current_n_files, current_hash[:12]))
    print()
    print("summary:")
    print("  %4d  no substrate identity recorded (cannot assess)" % len(no_identity))
    print("  %4d  current (matches %s)" % (len(current), args.ref))
    print("  %4d  already actioned (pending_retest_after_substrate / superseded_by_substrate / superseded already set)" % len(already_actioned))
    print("  %4d  DRIFT CANDIDATE (recorded substrate differs, not yet actioned)" % len(candidates))
    print()

    if candidates:
        by_claim: Dict[str, List[Tuple[Path, Dict[str, Any]]]] = {}
        for path, manifest in candidates:
            for claim_id in manifest.get("claim_ids") or []:
                by_claim.setdefault(claim_id, []).append((path, manifest))

        print("drift candidates by claim:")
        for claim_id in sorted(by_claim):
            print("  %s (%d run(s)):" % (claim_id, len(by_claim[claim_id])))
            for path, manifest in by_claim[claim_id]:
                commit = manifest.get("substrate_commit", {}).get("commit")
                run_id = manifest.get("run_id", path.stem)
                print("    - %s" % run_id)
                print("      manifest: %s" % _display_path(path))
                if commit:
                    changed = _diff_changed_files(ree_v3_root, commit, args.ref, current_globs)
                    if changed is None:
                        print("      recorded commit %s not diffable against %s locally" % (commit[:12], args.ref))
                    elif changed:
                        print("      changed since %s (%d file(s)):" % (commit[:12], len(changed)))
                        for f in changed[:15]:
                            print("        %s" % f)
                        if len(changed) > 15:
                            print("        ... and %d more" % (len(changed) - 15))
                    else:
                        print("      hash differs but no changed files found in scope diff (check driver_script_in_substrate_hash / n_files)")
                else:
                    print("      no substrate_commit recorded -- cannot name changed files, hash differs regardless")
                print("      suggested (NOT written by this script): pending_retest_after_substrate_per_claim: [\"%s\"]" % claim_id)
            print()

    print("Reminder: this is a READ-ONLY report. Nothing here writes to a manifest, changes")
    print("scoring, or requeues an experiment. A drift candidate is a signal for a human to")
    print("judge relevance, not a verdict -- most substrate churn is irrelevant to most claims.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
