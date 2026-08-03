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

PHASE 1 (added 2026-08-03): OPTIONAL per-claim `substrate_scope` DECLARATIONS in claims.yaml
---------------------------------------------------------------------------------------------
Phase 0's whole-tree comparison is noisy by design (measured: ~93% of evaluable manifests
read as "differs" against a fast-moving `main`). When a claim declares a `substrate_scope` in
`docs/claims/claims.yaml` (the SAME glob format `arm_fingerprint`/`substrate_scope_guard`
already use -- exact file paths, or a `dir/**/*.ext` recursive pattern), this script narrows
relevance PER CLAIM: a drift candidate whose changed-file list (already computed for the
report -- see point 3 above) does not intersect that claim's declared scope is moved out of
"drift candidates" and into a separate "outside declared scope" bucket for that claim only
(other, unscoped claims on the SAME manifest are unaffected). A claim's `substrate_scope` here
is an AUTHOR-DECLARED, deliberately conservative approximation -- NOT machine-proven the way
`substrate_scope_guard`'s call-trace/static-closure guards prove an arm_fingerprint scope; it
is safe to over-include (false candidate, wastes a human's attention) and unsafe to
under-include (false all-clear, hides real drift), so when in doubt declare wider. This
filter only applies when BOTH a scope is declared AND the manifest has a diffable
`substrate_commit.commit` -- otherwise Phase-0 whole-tree behaviour is unchanged for that
claim.

PHASE 1's REAL FINDING, and why PHASE 1b exists
------------------------------------------------
Running Phase 1 against the real corpus with 2 pilot scopes declared (MECH-471, MECH-321)
filtered ZERO candidates: both correctly depend on `ree_core/agent.py`, a genuine hub file
~half of recent substrate-touching commits touch (every new mechanism wires into the live
agent loop through it). Scope narrowing cannot help a claim that legitimately depends on a
hub file -- the noise there is irrelevant CHANGES to a relevant file (a new default-off flag
some other claim's work added), not irrelevant files. See the plan doc section 4.5.

PHASE 1b (added 2026-08-03): DEFAULT-OFF-DIFF FILTER
------------------------------------------------------
For a changed file already deemed in-scope (Phase 1) or scope-less (Phase 0), this asks: is
the ACTUAL DIFF confined to code reachable only when a still-default-off `ree_core/utils/
config.py` flag is enabled -- one this run's own driver never even references? If so, the
file's textual change is real but behaviourally inert for this run, and the whole candidate
downgrades to a new "default-off only" bucket instead of a genuine drift candidate.

MECHANISM (conservative by construction -- every uncertain case falls back to "stays a
genuine candidate," never to "confirmed inert"):
1. `parse_knobs()` is imported UNMODIFIED from the existing `default_off_drift_guard.py`
   (never reimplemented) to get the current set of `False`/`0`/`0.0`-defaulting REEConfig
   fields.
2. For the CURRENT version of a changed `.py` file (`git show <ref>:<path>`), every `if`
   statement whose test is a PURE boolean formula (AND/OR/NOT only) over references to those
   flags has its body's line range recorded, using Kleene (3-valued: True/False/Unknown)
   logic to evaluate the formula against this run's own flag-enablement status (see step 3)
   -- if the formula evaluates to definite `False`, that body is inert for this run,
   REGARDLESS of what any Unknown sub-leaf might have been (`False AND Unknown` is `False`).
   A test containing anything OTHER than a flag reference (a Compare, a Call, an unrelated
   Name) disqualifies that `if` from this analysis entirely -- its body is never treated as
   inert, since a compound condition mixing a flag with an unproven runtime check could still
   be reachable.
3. A run's flag-enablement status is NOT read from the manifest (manifests record the
   experiment DRIVER's own config dict -- seeds, episode counts, env kwargs -- not the actual
   `REEConfig` field values the agent was built with; this is a real, checked limitation, not
   an oversight). Instead, this is a TEXTUAL PROXY over the driver script's source AT THE
   RECORDED COMMIT (`git show <commit>:experiments/<experiment_type>.py`): a flag counts as
   `False` (confirmed unused) ONLY IF ITS NAME NEVER APPEARS ANYWHERE in that source. If the
   name appears at all (set True, set False explicitly, or merely discussed), its status is
   Unknown -- deliberately not resolved either way, since a bare substring hit cannot
   distinguish "sets it True" from "sets it False" from "mentions it in a comment."
4. `git diff --unified=0 <recorded-commit>..<ref> -- <file>` gives the exact NEW-file line
   numbers that changed (from `@@ -a,b +c,d @@` hunk headers -- exact, not context-window
   guesswork). A file is "default-off only" iff EVERY changed line falls inside some
   confirmed-inert `if` body.
5. A candidate downgrades to "default-off only" only when ALL of its changed files across
   ALL its declared/whole-tree-scoped relevance are default-off-only; a single genuinely live
   changed file keeps it a real candidate, mirroring Phase 1's own any-match relevance logic.

RETROACTIVE (this script) VS. PROSPECTIVE (a possible future fix) -- these are two different
things and this script is deliberately only the first. The textual-proxy step 3 above exists
BECAUSE manifests do not record which REEConfig flags a run actually built its agent with --
that is a genuine recording gap, and the ONLY way to close it precisely (record the actual
enabled-flag set at manifest-write time) is a change to the Experimental Recording Standard
that can only ever apply PROSPECTIVELY: it would sharpen every run recorded from that point
forward, but it cannot retroactively add missing telemetry to a run that already completed
without it -- there is no way to recover "what REEConfig fields were live" for a manifest
already on disk today. This script's textual proxy is the version that works retroactively,
against the corpus that already exists, at the cost of being conservative rather than exact.
Building the recording-standard fix is a separate, legitimate follow-on (it would let a FUTURE
version of this filter drop the proxy and read the real flag set directly) but is out of this
script's scope -- noted here so the two are never conflated.

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
import fnmatch
import glob
import json
import shutil
import subprocess
import sys
import tempfile
import uuid
import ast
import re
from pathlib import Path
from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

try:
    import yaml
except ImportError:  # pragma: no cover -- yaml is a hard dep of the pipeline
    yaml = None

REPO_ROOT = Path(__file__).resolve().parents[1]  # REE_assembly root
DEFAULT_EXP_DIR = REPO_ROOT / "evidence" / "experiments"
DEFAULT_REE_V3_ROOT = REPO_ROOT.parent / "ree-v3"
DEFAULT_CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"
DEFAULT_OFF_DRIFT_GUARD = REPO_ROOT / "scripts" / "default_off_drift_guard.py"

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


def load_claim_substrate_scopes(claims_yaml_path: Path) -> Dict[str, List[str]]:
    """claim_id -> declared substrate_scope glob list, for claims that declare one.

    Best-effort: an unreadable/malformed claims.yaml yields {} (Phase-0 behaviour for every
    claim), never a crash -- this is an optional narrowing, not a hard dependency.
    """
    if yaml is None or not claims_yaml_path.exists():
        return {}
    try:
        with open(claims_yaml_path, "r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
    except Exception:
        return {}
    claims = data.get("claims", data) if isinstance(data, dict) else data
    if not isinstance(claims, list):
        return {}
    out: Dict[str, List[str]] = {}
    for c in claims:
        if not isinstance(c, dict):
            continue
        scope = c.get("substrate_scope")
        claim_id = c.get("id")
        if claim_id and isinstance(scope, list) and scope:
            out[str(claim_id)] = [str(g) for g in scope]
    return out


def _file_in_scope(changed_file: str, scope_globs: List[str]) -> bool:
    """Does changed_file fall inside ANY of scope_globs?

    Handles the two scope-declaration shapes actually used in this repo today: an exact
    file path, and a `dir/**/*.ext` recursive pattern (matched as "starts with the prefix
    before '**' AND ends with the same extension" -- correctly matches zero-or-more
    intervening path segments, unlike a naive fnmatch/regex substitution of '**' -> '*',
    which would wrongly REQUIRE at least one intervening segment and under-match files
    directly in the named directory -- the dangerous direction here, since an under-match
    hides genuine relevance). Any other wildcard shape falls back to plain fnmatch as a
    best-effort (over-inclusive on failure to parse is fine; under-inclusive is not, so
    this fallback is deliberately permissive, not a silent no-match).
    """
    for pattern in scope_globs:
        if "**" in pattern:
            prefix, _, rest = pattern.partition("**")
            suffix = ("." + rest.rsplit(".", 1)[-1]) if "." in rest else ""
            if changed_file.startswith(prefix) and (not suffix or changed_file.endswith(suffix)):
                return True
        elif "*" in pattern or "?" in pattern:
            if fnmatch.fnmatch(changed_file, pattern):
                return True
        else:
            if changed_file == pattern:
                return True
    return False


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


# --------------------------------------------------------------------------------------- #
# Phase 1b -- default-off-diff filter                                                      #
# --------------------------------------------------------------------------------------- #


def load_default_off_knob_names(guard_path: Path = DEFAULT_OFF_DRIFT_GUARD) -> Set[str]:
    """The current set of False/0/0.0-defaulting REEConfig field names.

    Reuses default_off_drift_guard.parse_knobs() unmodified -- never reimplemented. Best
    effort: an unreadable/malformed guard script or config.py yields an empty set (Phase 1b
    becomes a no-op, never a crash) rather than blocking the rest of the report.
    """
    if not guard_path.exists():
        return set()
    config_py = REPO_ROOT.parent / "ree-v3" / "ree_core" / "utils" / "config.py"
    if not config_py.exists():
        return set()
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("default_off_drift_guard_mod", guard_path)
        mod = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        # Register BEFORE exec_module: the module defines @dataclass classes, and dataclass
        # resolves postponed annotations via sys.modules[cls.__module__] -- unregistered, that
        # lookup raises AttributeError on a None module, which the broad except below would
        # otherwise swallow into a SILENT empty set (Phase 1b quietly doing nothing, never
        # printing an error). Same fix as this repo's own test_substrate_staleness_gate.py
        # _load_indexer() pattern for build_experiment_indexes.py.
        sys.modules["default_off_drift_guard_mod"] = mod
        spec.loader.exec_module(mod)
        knobs = mod.parse_knobs(config_py)
    except Exception:
        return set()
    return set(knobs.keys())


def _git_show(ree_v3_root: Path, ref: str, path: str) -> Optional[str]:
    rc, out, err = _run(["git", "show", f"{ref}:{path}"], cwd=ree_v3_root)
    return out if rc == 0 else None


def flag_status_from_driver_source(driver_source: Optional[str], knob_names: Set[str]) -> Dict[str, bool]:
    """{knob_name: False} for every knob whose name never appears (as a whole word) anywhere
    in driver_source -- a conservative proxy for "this run's driver left it at its coded
    default." A knob whose name DOES appear is deliberately OMITTED (unknown), never mapped
    to True or False, since a bare substring hit cannot tell "set True" from "set False" from
    "mentioned in a comment." driver_source=None (unresolvable) yields {} -- every knob
    unknown, so Phase 1b will not confirm anything inert for this run.
    """
    if not driver_source:
        return {}
    out: Dict[str, bool] = {}
    for name in knob_names:
        if re.search(r"\b" + re.escape(name) + r"\b", driver_source) is None:
            out[name] = False
    return out


def flag_status_from_recorded_config(manifest: Dict[str, Any], knob_names: Set[str]) -> Dict[str, bool]:
    """{knob_name: bool} from the manifest's PROSPECTIVELY RECORDED
    `enabled_default_off_flags` field (ree-v3 experiments/_lib/manifest_core.py's
    stamp_recording_core, when the driver passed agent=). See
    substrate_stability_and_drift_detection_plan.md section 6.

    EXACT, not conservative-by-omission like flag_status_from_driver_source: every
    knob_names entry NOT present in the recorded dict is CONFIRMED disabled (its actual
    runtime value did not differ from the coded default -- not merely "not mentioned in
    source text"), and every one present was genuinely enabled. Matches on the recorded
    key's TRAILING dotted segment, since manifest_core records a nested path (e.g.
    "goal.use_hierarchical_goal_credit") while knob_names are bare field names from
    parse_knobs()'s flat AST parse of config.py.

    Returns {} ONLY when the manifest has no such field at all (absent -- this run's
    driver never passed agent=, or predates P1c) -- the caller's signal to fall back to
    flag_status_from_driver_source. A manifest that DID record (even an empty {},
    meaning "measured, nothing enabled" -- see manifest_core's own docstring for why
    that is recorded rather than omitted) yields one entry per knob_names member, so
    this function's return is only empty when there was truly nothing recorded, PROVIDED
    knob_names itself is non-empty (always true in practice -- ~300+ real knobs).
    """
    recorded = manifest.get("enabled_default_off_flags")
    if not isinstance(recorded, dict):
        return {}
    enabled_bare_names = {str(key).rsplit(".", 1)[-1] for key in recorded}
    return {name: (name in enabled_bare_names) for name in knob_names}


def _eval_flag_formula(node: ast.AST, knob_names: Set[str], flag_status: Dict[str, bool]) -> Optional[bool]:
    """Kleene (3-valued) evaluation of `node` as a pure boolean formula over `knob_names`
    references. Returns True/False when fully resolvable, None ("Unknown") the instant node
    contains anything that is not a recognised flag reference (a Compare, a Call, an
    unrelated Name/Attribute) -- disqualifying that whole sub-formula rather than guessing.
    Kleene AND/OR mean a single confirmed-False leaf can still resolve the whole formula to
    False even beside an Unknown sibling (`False and Unknown` == `False`), which is exactly
    the guarantee this filter needs: one confirmed-disabled flag in an AND-gate is enough.
    """
    if isinstance(node, ast.BoolOp):
        vals = [_eval_flag_formula(v, knob_names, flag_status) for v in node.values]
        if isinstance(node.op, ast.And):
            if any(v is False for v in vals):
                return False
            if any(v is None for v in vals):
                return None
            return True
        else:  # ast.Or
            if any(v is True for v in vals):
                return True
            if any(v is None for v in vals):
                return None
            return False
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        v = _eval_flag_formula(node.operand, knob_names, flag_status)
        return None if v is None else (not v)
    if isinstance(node, ast.Attribute) and node.attr in knob_names:
        return flag_status.get(node.attr)
    if isinstance(node, ast.Name) and node.id in knob_names:
        return flag_status.get(node.id)
    return None


def _line_span(nodes) -> Tuple[Optional[int], Optional[int]]:
    los: List[int] = []
    his: List[int] = []
    for n in nodes:
        for sub in ast.walk(n):
            lineno = getattr(sub, "lineno", None)
            if lineno is not None:
                los.append(lineno)
            end_lineno = getattr(sub, "end_lineno", None)
            if end_lineno is not None:
                his.append(end_lineno)
    if not los or not his:
        return None, None
    return min(los), max(his)


def inert_line_ranges(file_source: str, knob_names: Set[str], flag_status: Dict[str, bool]) -> List[Tuple[int, int]]:
    """Line ranges (1-indexed, inclusive) whose containing `if` body is confirmed inert for
    this run -- the `if`'s test evaluates to definite False under flag_status. Best effort:
    a syntax error in file_source yields [] (nothing confirmed inert), never a crash.
    """
    try:
        tree = ast.parse(file_source)
    except SyntaxError:
        return []
    ranges: List[Tuple[int, int]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.If):
            continue
        verdict = _eval_flag_formula(node.test, knob_names, flag_status)
        if verdict is False:
            _, hi = _line_span(node.body)  # body span for the END; orelse is NOT inert
            if hi is not None:
                # Start at node.lineno (the `if <test>:` line itself), not the body's own
                # start -- a newly-added "if <confirmed-false>:" line has zero effect on
                # anything, precisely because the condition is False, so it is just as inert
                # as its body. Using node.lineno rather than _line_span(node.body)'s own `lo`
                # is what makes the if-line itself count as covered.
                ranges.append((node.lineno, hi))
    return ranges


def changed_line_numbers(ree_v3_root: Path, recorded_commit: str, ref: str, path: str) -> Optional[List[int]]:
    """New-file (post-image) line numbers touched by recorded_commit..ref for `path`, from
    `git diff --unified=0` hunk headers (`@@ -a,b +c,d @@`) -- exact, not context-window
    guesswork. None if the diff itself could not be produced.
    """
    rc, out, err = _run(
        ["git", "diff", "--unified=0", f"{recorded_commit}..{ref}", "--", path],
        cwd=ree_v3_root,
    )
    if rc != 0:
        return None
    lines: List[int] = []
    for hunk in re.finditer(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@", out, re.MULTILINE):
        start = int(hunk.group(1))
        count = int(hunk.group(2)) if hunk.group(2) is not None else 1
        if count == 0:
            continue  # pure deletion in the new file -- no new-file lines to check
        lines.extend(range(start, start + count))
    return lines


def file_is_default_off_only(
    ree_v3_root: Path, recorded_commit: str, ref: str, path: str,
    knob_names: Set[str], flag_status: Dict[str, bool],
) -> Optional[bool]:
    """True iff every changed line in `path` sits inside a confirmed-inert `if` body for this
    run. False if at least one changed line is not covered (a genuine live change). None if
    this could not be determined (not a .py file, unreadable, undiffable, no changed lines)
    -- callers must treat None the same as False (stays a candidate), never as True.
    """
    if not path.endswith(".py"):
        return None
    lines = changed_line_numbers(ree_v3_root, recorded_commit, ref, path)
    if not lines:
        return None
    source = _git_show(ree_v3_root, ref, path)
    if source is None:
        return None
    ranges = inert_line_ranges(source, knob_names, flag_status)
    if not ranges:
        return False
    return all(any(lo <= ln <= hi for lo, hi in ranges) for ln in lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--exp-dir", default=str(DEFAULT_EXP_DIR))
    ap.add_argument("--ree-v3-root", default=str(DEFAULT_REE_V3_ROOT))
    ap.add_argument("--ref", default="origin/main")
    ap.add_argument("--claims-yaml", default=str(DEFAULT_CLAIMS_YAML))
    args = ap.parse_args()

    exp_dir = Path(args.exp_dir)
    ree_v3_root = Path(args.ree_v3_root)
    claim_scopes = load_claim_substrate_scopes(Path(args.claims_yaml))

    manifests = load_flat_claim_tagged_manifests(exp_dir)
    print("substrate-staleness candidate report (READ-ONLY, Phase 0+1)  --  %d claim-tagged flat manifest(s)" % len(manifests))
    print("source: %s" % exp_dir)
    print("comparing against: %s (ree-v3 root: %s)" % (args.ref, ree_v3_root))
    print("claims with a declared substrate_scope: %d (%s)" % (
        len(claim_scopes), ", ".join(sorted(claim_scopes)) or "none"))
    print()

    no_identity: List[Path] = []
    current: List[Path] = []
    already_actioned: List[Tuple[Path, Dict[str, Any]]] = []
    candidate_manifests: List[Tuple[Path, Dict[str, Any]]] = []
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
                candidate_manifests.append((path, manifest))
    except RuntimeError as e:
        print("ERROR: could not resolve current substrate identity: %s" % e)
        return 1

    print("current substrate (%s): %d file(s), hash %s" % (args.ref, current_n_files, current_hash[:12]))
    print()

    # One diff per distinct recorded commit, reused across every claim on every manifest that
    # cites it (a manifest can tag several claims; the changed-file list is the same for all).
    diff_cache: Dict[str, Optional[List[str]]] = {}

    def changed_files_for(commit: str) -> Optional[List[str]]:
        if commit not in diff_cache:
            diff_cache[commit] = _diff_changed_files(ree_v3_root, commit, args.ref, current_globs)
        return diff_cache[commit]

    by_claim_candidate: Dict[str, List[Tuple[Path, Dict[str, Any], Optional[List[str]]]]] = {}
    by_claim_out_of_scope: Dict[str, List[Tuple[Path, Dict[str, Any], List[str]]]] = {}

    for path, manifest in candidate_manifests:
        commit = manifest.get("substrate_commit", {}).get("commit")
        changed = changed_files_for(commit) if commit else None
        for claim_id in manifest.get("claim_ids") or []:
            scope = claim_scopes.get(claim_id)
            if scope and changed is not None:
                relevant = any(_file_in_scope(f, scope) for f in changed)
                if not relevant:
                    by_claim_out_of_scope.setdefault(claim_id, []).append((path, manifest, changed))
                    continue
            by_claim_candidate.setdefault(claim_id, []).append((path, manifest, changed))

    # Phase 1b: of what Phase 1 kept as genuine candidates, is the RELEVANT diff for a claim
    # confined to code reachable only under a still-default-off flag this run's own driver
    # never references? Only ever downgrades (never upgrades) a Phase-1 candidate.
    knob_names = load_default_off_knob_names()
    driver_source_cache: Dict[Tuple[str, str], Optional[str]] = {}
    default_off_cache: Dict[Tuple[str, str, str], Optional[bool]] = {}

    def driver_source_for(commit: str, experiment_type: str) -> Optional[str]:
        key = (commit, experiment_type)
        if key not in driver_source_cache:
            driver_source_cache[key] = (
                _git_show(ree_v3_root, commit, "experiments/%s.py" % experiment_type)
                if experiment_type else None
            )
        return driver_source_cache[key]

    def is_default_off_only_cached(commit: str, experiment_type: str, path: str, flag_status: Dict[str, bool]) -> Optional[bool]:
        # ONLY safe to cache by (commit, experiment_type, path): the textual-proxy
        # flag_status is a pure function of that key (same driver source for every
        # manifest sharing a commit+experiment_type). The RECORDED-config flag_status is
        # NOT -- it is specific to one manifest's own run (two arms of the same
        # experiment_type at the same commit could genuinely record different enabled
        # flags) -- see the caller below, which routes recorded-config lookups around
        # this cache entirely rather than risk a stale cross-manifest hit.
        key = (commit, experiment_type, path)
        if key not in default_off_cache:
            default_off_cache[key] = file_is_default_off_only(
                ree_v3_root, commit, args.ref, path, knob_names, flag_status)
        return default_off_cache[key]

    by_claim_default_off: Dict[str, List[Tuple[Path, Dict[str, Any], Optional[List[str]]]]] = {}
    n_recorded_config_used = 0

    if knob_names:
        narrowed_candidate: Dict[str, List[Tuple[Path, Dict[str, Any], Optional[List[str]]]]] = {}
        for claim_id, entries in by_claim_candidate.items():
            scope = claim_scopes.get(claim_id)
            kept: List[Tuple[Path, Dict[str, Any], Optional[List[str]]]] = []
            for path, manifest, changed in entries:
                commit = manifest.get("substrate_commit", {}).get("commit")
                if not commit or not changed:
                    kept.append((path, manifest, changed))
                    continue
                relevant_files = [f for f in changed if (not scope or _file_in_scope(f, scope))]
                if not relevant_files:
                    kept.append((path, manifest, changed))
                    continue
                experiment_type = str(manifest.get("experiment_type", ""))
                # Prefer the prospectively-RECORDED config (exact) over the textual
                # driver-source proxy (conservative-by-omission) whenever this manifest
                # has it -- P1c (substrate_stability_and_drift_detection_plan.md sec 6).
                recorded_status = flag_status_from_recorded_config(manifest, knob_names)
                if recorded_status:
                    n_recorded_config_used += 1
                    flag_status = recorded_status
                    verdicts = [
                        file_is_default_off_only(ree_v3_root, commit, args.ref, f, knob_names, flag_status)
                        for f in relevant_files
                    ]
                else:
                    flag_status = flag_status_from_driver_source(
                        driver_source_for(commit, experiment_type), knob_names)
                    verdicts = [
                        is_default_off_only_cached(commit, experiment_type, f, flag_status)
                        for f in relevant_files
                    ]
                if verdicts and all(v is True for v in verdicts):
                    by_claim_default_off.setdefault(claim_id, []).append((path, manifest, changed))
                else:
                    kept.append((path, manifest, changed))
            if kept:
                narrowed_candidate[claim_id] = kept
        by_claim_candidate = narrowed_candidate

    n_candidate_pairs = sum(len(v) for v in by_claim_candidate.values())
    n_out_of_scope_pairs = sum(len(v) for v in by_claim_out_of_scope.values())
    n_default_off_pairs = sum(len(v) for v in by_claim_default_off.values())

    print("summary:")
    print("  %4d  no substrate identity recorded (cannot assess)" % len(no_identity))
    print("  %4d  current (matches %s)" % (len(current), args.ref))
    print("  %4d  already actioned (pending_retest_after_substrate / superseded_by_substrate / superseded already set)" % len(already_actioned))
    print("  %4d  drift candidate manifest(s) (recorded substrate differs, not yet actioned)" % len(candidate_manifests))
    print("  %4d  (claim, run) pair(s) filtered OUTSIDE a declared substrate_scope (Phase 1)" % n_out_of_scope_pairs)
    print("  %4d  (claim, run) pair(s) filtered as DEFAULT-OFF ONLY (Phase 1b, %d default-off knob(s) known)" % (n_default_off_pairs, len(knob_names)))
    print("  %4d  (claim, run) pair(s) used the RECORDED config (P1c, exact) rather than the driver-source proxy" % n_recorded_config_used)
    print("  %4d  (claim, run) pair(s) remain DRIFT CANDIDATES after scope + default-off filtering" % n_candidate_pairs)
    print()

    if by_claim_candidate:
        print("drift candidates by claim:")
        for claim_id in sorted(by_claim_candidate):
            scoped = claim_id in claim_scopes
            print("  %s (%d run(s))%s:" % (
                claim_id, len(by_claim_candidate[claim_id]),
                " -- substrate_scope declared" if scoped else ""))
            for path, manifest, changed in by_claim_candidate[claim_id]:
                commit = manifest.get("substrate_commit", {}).get("commit")
                run_id = manifest.get("run_id", path.stem)
                print("    - %s" % run_id)
                print("      manifest: %s" % _display_path(path))
                if commit:
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

    if by_claim_out_of_scope:
        print("filtered OUTSIDE declared substrate_scope (Phase 1 -- not shown as candidates above):")
        for claim_id in sorted(by_claim_out_of_scope):
            print("  %s (%d run(s), scope: %s):" % (
                claim_id, len(by_claim_out_of_scope[claim_id]), claim_scopes[claim_id]))
            for path, manifest, changed in by_claim_out_of_scope[claim_id]:
                run_id = manifest.get("run_id", path.stem)
                print("    - %s (whole-tree diff had %d changed file(s), none in declared scope)" % (run_id, len(changed)))
            print()

    if by_claim_default_off:
        print("filtered as DEFAULT-OFF ONLY (Phase 1b -- not shown as candidates above):")
        for claim_id in sorted(by_claim_default_off):
            print("  %s (%d run(s)):" % (claim_id, len(by_claim_default_off[claim_id])))
            for path, manifest, changed in by_claim_default_off[claim_id]:
                run_id = manifest.get("run_id", path.stem)
                print("    - %s (every relevant changed file's diff sits behind a still-default-off" % run_id)
                print("      flag this run's driver never references)")
            print()

    print("Reminder: this is a READ-ONLY report. Nothing here writes to a manifest, changes")
    print("scoring, or requeues an experiment. A drift candidate is a signal for a human to")
    print("judge relevance, not a verdict -- most substrate churn is irrelevant to most claims.")
    print("A claim's substrate_scope (Phase 1) is an author-declared, deliberately conservative")
    print("approximation, not machine-proven -- treat an out-of-scope filter result as a hint,")
    print("not a guarantee, until the claim's scope has more track record. The default-off filter")
    print("(Phase 1b) is a TEXTUAL PROXY over driver source, not a real REEConfig readout (that")
    print("would need a recording-standard change, and only prospectively -- see the module")
    print("docstring); treat a default-off-only verdict the same way -- a hint, not a guarantee.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
