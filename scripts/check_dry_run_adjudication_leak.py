#!/usr/bin/env python3
"""Dry-run adjudication-leak audit (governance Step 3i, GOV-DRY-1).

The SIXTH sibling of the governance standing scans, and the only one that audits
whether an artifact reasoned over evidence that DOES NOT EXIST:

  * GOV-CEIL-1  (check_substrate_ceiling_audit.py)        -- >=N ceiling verdicts on one claim
  * GOV-DIAG-1  (check_diagnostic_chain_recurrence.py)    -- >=N claimless no-verdict autopsies
  * GOV-GRAN-1  (check_granularity_debt_recurrence.py)    -- >=N structurally-different failures
  * GOV-CAT-1   (check_epistemic_category_completeness.py)-- the verdict was never RECORDED
  * GOV-APPLY-1 (check_unapplied_autopsy_recommendations.py) -- the verdict was never APPLIED
  * GOV-DRY-1   (this file)                               -- the verdict rests on a SMOKE

WHY THIS AUDIT EXISTS. A `--dry-run` smoke is a truncated budget (typically ~30
steps/episode and 1-4 episodes against a full run's hundreds) emitted to prove a
driver executes. Its metrics are not measurements of anything: detector gates that
require a mid-training episode index never arm, and criteria pinned by truncation
report a PASS/FAIL that is an artifact of the budget. The SCORING path has been
gated since `cb7298c1c4` in three places -- `sync_v3_results.py` (pack converter),
`build_experiment_indexes.py:1174` (indexer), and `generate_pending_review.py`
(dry run_ids excluded from every pending bucket).

Nothing gated the ADJUDICATION path. A `/failure-autopsy` or `/governance` session
could read a dry manifest and reason over its metrics as evidence, and did --
confirmed twice, in opposite directions, six hours apart on 2026-05-19 for
V3-EXQ-543i, where the CORRECT 01:13Z diagnosis ("vacuous, a truncation artifact")
was overwritten at 07:06Z by a cross-run basin-nondeterminism narrative built
entirely on the smoke, over a real-run set with ZERO variance. That phantom then
propagated into `substrate_queue.json` as an acceptance bar any future ARC-062 fix
must clear. Full analysis:
`evidence/planning/dry_run_smoke_in_autopsy_audit_2026-07-28.md`.

`scripts/check_dry_run_citations.py` (2026-07-28) made the check AVAILABLE, and
the `/failure-autopsy` + `/governance` skills now REQUIRE it. But that is skill
prose: it works only while every session remembers to run it. The audit's own
closing finding is that this defect was caught and patched per-instance at least
FOUR times without the pipeline being fixed -- "a correct local diagnosis does not
survive on its own; only a gate does." This file is that gate.

WHAT IS SWEPT, in two independent halves:

  1. CITATIONS -- every confirmed (`status: confirmed`) `failure_autopsy_*.json`
     and every string in `evidence/planning/substrate_queue.json`, harvested for
     run_ids that resolve to a dry manifest. Ids are found by regex over EVERY
     string, prose included, because the confirmed damage in the 543i case was a
     prose citation in a `failure_record` note, not a schema field.

  2. STAMPS -- every dry manifest carrying governance-grade metadata it cannot
     support. This is the precondition for half 1: a smoke stamped with
     `evidence_direction` / `epistemic_category` is indistinguishable, to a reader,
     from adjudicated evidence.

     ONLY *ASSERTING* STAMPS ARE REPORTED, and this distinction is the whole
     design. A dry manifest reading `evidence_direction: superseded` or
     `non_contributory` is CORRECTLY QUARANTINED -- that stamp is the desired end
     state, not a defect, and flagging it would fire on 19 of the 36 dry run_ids
     forever while telling governance to undo the right thing. What is reported is
     a stamp that ASSERTS: a direction (`supports` / `weakens` / `mixed` /
     `unknown`), a per-claim direction map containing one, or any
     `epistemic_category` (an adjudicated governance category no smoke can earn).

DETECTION IS NOT RE-IMPLEMENTED. Both halves resolve dryness through
`check_dry_run_citations.build_index()`, which itself imports `_is_dry_run` from
`scripts/generate_pending_review.py`. One truthiness check, three consumers -- a
second copy is how the forms drift.

METABOLIZED EXCLUSIONS. Two mechanisms, both hit-scoped:

  * A SEED table (`_ADJUDICATED_CITATIONS` / `_ADJUDICATED_STAMPS`) carrying what
    the 2026-07-28 audit and the `dry_run_stamped_manifest_sweep_2026-07-28.md`
    corpus sweep already adjudicated. Without it this audit would report ~20
    findings on its first run, every cycle, forever -- and GOV-FROZEN-1's design
    notes name ALARM FATIGUE as itself a Goodhart vector: a warn-only flag that
    recurs every cycle with a plausible narrative gets accepted by default.
    Excluded items are still PRINTED under "adjudicated", so nothing is hidden --
    they are merely not actionable.

  * An IN-BAND marker for future adjudications, so the next one needs no code
    change. A `failure_autopsy_*.json` may carry a top-level block:

        "dry_run_citation_metabolized": {
          "date": "2026-08-01",
          "metabolized_hits": ["v3_exq_..._v3"],   # REQUIRED
          "note": "why citing this smoke is correct / how it was adjudicated"
        }

    Mirrors GOV-DIAG-1's `diagnostic_recurrence_metabolized`, including its two
    load-bearing properties: the exclusion is HIT-SCOPED (only the listed run_ids
    are subtracted, so a NEW dry citation in the same artifact still fires -- a
    marker can quiet the citation it names, never permanently deafen the file),
    and `metabolized_hits` is REQUIRED (a marker missing it is IGNORED and reported
    as malformed, failing loud rather than silently blanket-silencing).

STAMP EXCLUSIONS ARE KEYED ON (run_id, flat|pack), not on run_id alone. That
precision is load-bearing and was found by the corpus sweep: `a6fda79367` stamped
the three 543f *flats* with `epistemic_category: substrate_ceiling` by family match
but never touched their *packs*, which still assert
`evidence_direction_per_claim: {"ARC-062": "weakens"}` from a smoke -- in the
canonical file the indexer reads. A run_id-scoped exclusion of 543f would mask
exactly the finding worth having.

Absent any dry manifest every count is 0, so a missing or unreadable evidence tree
can never mass-surface (same non-falsifying-safe posture as its five siblings).

This audit READS ONLY. It promotes / demotes nothing, edits no manifest, and does
not touch claims.yaml. Every write it recommends is governance's. It is WARN-ONLY
and always exits 0 unless `--strict`.

Usage:
  python3 scripts/check_dry_run_adjudication_leak.py            # human report, exit 0
  python3 scripts/check_dry_run_adjudication_leak.py --strict   # exit 1 if any actionable
  python3 scripts/check_dry_run_adjudication_leak.py --json     # machine-readable
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_AUTOPSY_DIR = REPO_ROOT / "evidence" / "planning"
DEFAULT_SUBSTRATE_QUEUE = REPO_ROOT / "evidence" / "planning" / "substrate_queue.json"

# Reuse the adjudication guard's index + id harvesting. Do NOT re-implement the
# dryness check here; that module already imports the single `_is_dry_run` from
# generate_pending_review.py.
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from check_dry_run_citations import (  # noqa: E402
        RUN_ID_RE,
        _looks_like_run_id,
        build_index,
    )
except ImportError as exc:  # pragma: no cover - environment problem, be loud
    raise SystemExit(
        "cannot import from scripts/check_dry_run_citations.py: %s" % exc
    )

# In-band marker key on a failure_autopsy_*.json. See the module docstring.
METABOLIZED_KEY = "dry_run_citation_metabolized"

# Fields that RECORD a dry-run exclusion rather than CITE the run as evidence.
# `check_dry_run_citations.py`'s own Step 2a gate writes these on a confirmed
# autopsy to document that a dry sibling was checked and correctly excluded --
# e.g. `excluded_dry_run_ids: [...]` plus a `dry_run_check_note` explaining why.
# A run_id mentioned ONLY inside one of these two fields is the audit doing its
# job, not a leak: flagging it penalises exactly the behaviour GOV-DRY-1 exists
# to encourage. `_harvest` skips descending into these keys (at any depth) so a
# run_id named ONLY here is never counted as cited -- one also named in a
# `target` / `failure_record` / reasoning field elsewhere in the same document
# is unaffected, since that occurrence is found via the un-skipped fields.
EXCLUSION_RECORD_FIELDS = frozenset({"excluded_dry_run_ids", "dry_run_check_note"})

# A stamp that ASSERTS a direction. `superseded` / `non_contributory` are
# deliberately absent: on a dry manifest those are the CORRECT quarantine, not a
# defect. `unknown` is included because it still occupies the direction field on
# an artifact that has no direction to report.
ASSERTING_DIRECTIONS = {"supports", "weakens", "mixed", "unknown"}

# Fields checked for an asserting stamp.
DIRECTION_FIELD = "evidence_direction"
PER_CLAIM_FIELD = "evidence_direction_per_claim"
CATEGORY_FIELD = "epistemic_category"

# --- SEED EXCLUSIONS -------------------------------------------------------
# Adjudicated by evidence/planning/dry_run_smoke_in_autopsy_audit_2026-07-28.md
# and evidence/planning/dry_run_stamped_manifest_sweep_2026-07-28.md. Hit-scoped:
# {artifact stem: {run_id, ...}} -- a NEW dry citation in the same file still fires.
_ADJUDICATED_CITATIONS: dict[str, set[str]] = {
    # Case 1. The 07:06Z autopsy that built a basin-nondeterminism narrative on the
    # smoke, and the CORRECT 01:13Z autopsy it overwrote (which cites the same run
    # precisely in order to call it vacuous -- a correct citation).
    "failure_autopsy_543i_2026-05-19": {
        "v3_exq_543i_arc062_differential_heads_falsifier_20260518T063711Z_v3",
    },
    "failure_autopsy_V3-EXQ-543i_2026-05-19": {
        "v3_exq_543i_arc062_differential_heads_falsifier_20260518T063711Z_v3",
    },
    # Case 2. Population members of a 17-run corpus analysis; conclusion survives,
    # one prevalence statistic inflated (recomputed in the audit).
    "failure_autopsy_sd081-spearman-degenerate-dv_2026-07-27": {
        "v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T125958Z_v3",
        "v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T130046Z_v3",
        "v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T130300Z_v3",
        "v3_exq_543g_arc062_outcome_coupled_falsifier_20260517T144716Z_v3",
        "v3_exq_543h_arc062_crystallization_falsifier_20260518T060905Z_v3",
        "v3_exq_543i_arc062_differential_heads_falsifier_20260518T063711Z_v3",
    },
}

# substrate_queue.json citations already adjudicated. The audit RECOMMENDED a write
# here (strike failure_record[3]; drop the K>=3 / basin-determinism bar from the
# `target` of [3] and [4]) which governance has not yet applied -- tracking an
# unapplied recommendation is GOV-APPLY-1's lane, not this one, so it is excluded
# here and printed under "adjudicated" rather than re-reported as a fresh leak.
_ADJUDICATED_QUEUE_CITATIONS: set[str] = {
    "v3_exq_543i_arc062_differential_heads_falsifier_20260518T063711Z_v3",
}

# Asserting stamps already adjudicated. Keyed (run_id, "flat"|"pack") -- see the
# docstring for why run_id alone would mask the 543f pack finding.
_ADJUDICATED_STAMPS: dict[tuple[str, str], str] = {
    # Audit secondary finding: byte-identical superseded + substrate_ceiling applied
    # by a6fda79367 by family match. Dispositions stand; verdict came from the
    # 543h autopsy, which correctly read only non-dry runs.
    ("v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T125958Z_v3", "flat"):
        "audit 2026-07-28 secondary finding (a6fda79367 family sweep); dispositions stand",
    ("v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T130046Z_v3", "flat"):
        "audit 2026-07-28 secondary finding (a6fda79367 family sweep); dispositions stand",
    ("v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T130300Z_v3", "flat"):
        "audit 2026-07-28 secondary finding (a6fda79367 family sweep); dispositions stand",
    ("v3_exq_543g_arc062_outcome_coupled_falsifier_20260517T144716Z_v3", "flat"):
        "audit 2026-07-28 secondary finding (a6fda79367 family sweep); dispositions stand",
    ("v3_exq_543h_arc062_crystallization_falsifier_20260518T060905Z_v3", "flat"):
        "audit 2026-07-28 secondary finding (a6fda79367 family sweep); dispositions stand",
    # Already a documented, deliberately-deferred category: the pack carries the
    # superseded + dry-run note, only the flat still reads `mixed`. Both run_ids are
    # listed by name in flat_vs_runs_direction_mismatch_triage_2026_05_31.md bucket
    # (b) -- "regenerating flat is out of scope this pass". Fold into that pass.
    ("v3_exq_157_q017_control_axis_minimal_subset_20260329T081401Z_v3", "flat"):
        "flat_vs_runs triage 2026-05-31 bucket (b); deferred flat-regeneration pass",
    ("v3_exq_161_q024_trajectory_representation_triple_20260329T104847Z_v3", "flat"):
        "flat_vs_runs triage 2026-05-31 bucket (b); deferred flat-regeneration pass",
    # `unknown` is not an assertion of direction, and the target is claimless.
    ("v3_exq_570_e2_rollout_collapse_diagnostic_20260515T232232Z_v3", "pack"):
        "sweep 2026-07-28: ed=unknown is not a direction assertion; claimless target",
}


def _dry_index() -> tuple[dict, set[str]]:
    """Return (by_run, dry_run_ids) from the shared manifest index."""
    by_run, _by_queue = build_index()
    return by_run, {r for r, v in by_run.items() if v["dry_run"]}


def _harvest(value, dry: set[str],
             skip_keys: frozenset[str] = frozenset()) -> set[str]:
    """Dry run_ids mentioned anywhere in a JSON value (prose included).

    `skip_keys` names dict keys whose subtree is never descended into -- used
    to exclude EXCLUSION_RECORD_FIELDS from the citation scan (see its
    docstring) without altering what counts as a citation everywhere else.
    """
    found: set[str] = set()
    stack = [value]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            for k, v in node.items():
                if k in skip_keys:
                    continue
                stack.append(v)
        elif isinstance(node, (list, tuple)):
            stack.extend(node)
        elif isinstance(node, str):
            for s in RUN_ID_RE.findall(node):
                if _looks_like_run_id(s) and s in dry:
                    found.add(s)
    return found


def _load_markers(path: Path, data: dict) -> tuple[set[str], dict | None]:
    """Read an artifact's in-band metabolization marker.

    Returns (metabolized_hits, malformed_record). A marker without a non-empty
    `metabolized_hits` is IGNORED and reported -- it never blanket-silences.
    """
    marker = data.get(METABOLIZED_KEY)
    if not isinstance(marker, dict):
        return set(), None
    hits = marker.get("metabolized_hits")
    if isinstance(hits, str):
        hits = [hits]
    hits = {str(h).strip() for h in (hits or []) if str(h).strip()}
    if not hits:
        return set(), {
            "artifact": path.name,
            "reason": "missing or empty metabolized_hits",
            "date": marker.get("date"),
        }
    return hits, None


def scan_citations(autopsy_dir: Path, queue_path: Path,
                   dry: set[str]) -> dict[str, list]:
    """Half 1 -- dry run_ids cited by confirmed autopsies + substrate_queue.json."""
    actionable: list[dict] = []
    adjudicated: list[dict] = []
    malformed: list[dict] = []

    if autopsy_dir.is_dir():
        for path in sorted(autopsy_dir.glob("failure_autopsy_*.json")):
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (ValueError, OSError):
                # Unparseable artifacts are the JSON-validity gate's business.
                continue
            if not isinstance(data, dict):
                continue
            if str(data.get("status", "")).strip().lower() != "confirmed":
                continue
            cited = _harvest(data, dry, skip_keys=EXCLUSION_RECORD_FIELDS)
            if not cited:
                continue
            marker_hits, bad = _load_markers(path, data)
            if bad:
                malformed.append(bad)
            excused = set(_ADJUDICATED_CITATIONS.get(path.stem, set())) | marker_hits
            for run_id in sorted(cited):
                rec = {"source": path.name, "run_id": run_id, "kind": "autopsy"}
                (adjudicated if run_id in excused else actionable).append(rec)

    if queue_path.is_file():
        try:
            qdata = json.loads(queue_path.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            qdata = None
        if qdata is not None:
            for run_id in sorted(_harvest(qdata, dry)):
                rec = {"source": queue_path.name, "run_id": run_id,
                       "kind": "substrate_queue"}
                (adjudicated if run_id in _ADJUDICATED_QUEUE_CITATIONS
                 else actionable).append(rec)

    return {"actionable": actionable, "adjudicated": adjudicated,
            "malformed_markers": malformed}


def scan_stamps(by_run: dict, dry: set[str]) -> dict[str, list]:
    """Half 2 -- dry manifests carrying an ASSERTING governance stamp.

    Quarantine stamps (`superseded` / `non_contributory` with no category and no
    directional per-claim entry) are correct on a smoke and are never reported.
    """
    actionable: list[dict] = []
    adjudicated: list[dict] = []

    for run_id in sorted(dry):
        for rel in by_run[run_id]["paths"]:
            try:
                data = json.loads((REPO_ROOT / rel).read_text(encoding="utf-8"))
            except (ValueError, OSError):
                continue
            if not isinstance(data, dict):
                continue
            direction = str(data.get(DIRECTION_FIELD) or "").strip().lower()
            category = str(data.get(CATEGORY_FIELD) or "").strip().lower()
            per_claim = data.get(PER_CLAIM_FIELD) or {}
            per_bad = sorted(
                {str(c) for c, v in per_claim.items()
                 if str(v).strip().lower() in ASSERTING_DIRECTIONS}
            ) if isinstance(per_claim, dict) else []

            reasons = []
            if direction in ASSERTING_DIRECTIONS:
                reasons.append("%s=%s" % (DIRECTION_FIELD, direction))
            if per_bad:
                reasons.append("%s asserts on %s" % (PER_CLAIM_FIELD, ", ".join(per_bad)))
            if category:
                reasons.append("%s=%s" % (CATEGORY_FIELD, category))
            if not reasons:
                continue

            kind = "pack" if "/runs/" in rel else "flat"
            # A backfill skeleton is the sharpest case: a direction with no run
            # behind it at all. Surfaced inline so the reader does not have to open
            # the file to learn there is no measurement.
            skeleton = (str(data.get("status") or "").upper() == "UNKNOWN"
                        and not data.get("timestamp_utc"))
            rec = {
                "run_id": run_id, "kind": kind, "path": rel,
                "reasons": reasons, "skeleton": skeleton,
                "claim_ids": list(data.get("claim_ids_tested")
                                  or data.get("claim_ids") or []),
            }
            excuse = _ADJUDICATED_STAMPS.get((run_id, kind))
            if excuse:
                adjudicated.append({**rec, "excluded_reason": excuse})
            else:
                actionable.append(rec)

    return {"actionable": actionable, "adjudicated": adjudicated}


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--autopsy-dir", type=Path, default=DEFAULT_AUTOPSY_DIR,
                    help="directory holding failure_autopsy_*.json")
    ap.add_argument("--substrate-queue", type=Path, default=DEFAULT_SUBSTRATE_QUEUE,
                    help="substrate_queue.json to sweep for dry-run citations")
    ap.add_argument("--json", action="store_true", dest="as_json",
                    help="emit machine-readable JSON")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any actionable citation or stamp is found")
    args = ap.parse_args()

    by_run, dry = _dry_index()
    cites = scan_citations(args.autopsy_dir, args.substrate_queue, dry)
    stamps = scan_stamps(by_run, dry)

    n_cite = len(cites["actionable"])
    n_stamp = len(stamps["actionable"])
    n_bad_marker = len(cites["malformed_markers"])

    if args.as_json:
        json.dump({
            "n_dry_run_ids": len(dry),
            "n_manifests": len(by_run),
            "citations": cites,
            "stamps": stamps,
            "n_actionable_citations": n_cite,
            "n_actionable_stamps": n_stamp,
        }, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
        return 1 if (args.strict and (n_cite or n_stamp)) else 0

    print("Dry-run adjudication-leak audit (GOV-DRY-1): "
          "%d dry run_id(s) of %d manifests" % (len(dry), len(by_run)))
    print("  cited by a confirmed autopsy / substrate_queue (ACTIONABLE): %d" % n_cite)
    print("  dry manifests carrying an ASSERTING stamp   (ACTIONABLE): %d" % n_stamp)
    print("  adjudicated / metabolized (not actionable)             : %d"
          % (len(cites["adjudicated"]) + len(stamps["adjudicated"])))

    if n_cite:
        print("\nACTIONABLE -- a confirmed artifact cites a --dry-run smoke. A smoke is")
        print("NOT evidence: its metrics are truncation artifacts and its PASS/FAIL is")
        print("a property of the budget. Re-read the artifact's reasoning over these")
        print("run_ids before any disposition derived from it is applied or trusted:")
        for f in cites["actionable"]:
            print("  - %s [%s]" % (f["source"], f["kind"]))
            print("      cites DRY %s" % f["run_id"])

    if n_stamp:
        print("\nACTIONABLE -- a dry manifest carries governance-grade metadata it")
        print("cannot support, making it indistinguishable from adjudicated evidence.")
        print("Strip or neutralise the stamp (governance write; never done by this scan):")
        for f in stamps["actionable"]:
            tag = " [BACKFILL SKELETON -- no run behind it]" if f["skeleton"] else ""
            print("  - %s (%s)%s" % (f["run_id"], f["kind"], tag))
            print("      %s" % f["path"])
            print("      %s" % "; ".join(f["reasons"]))
            if f["claim_ids"]:
                print("      claims: %s" % ", ".join(f["claim_ids"]))

    if not n_cite and not n_stamp:
        print("\n  -- no dry-run smoke is cited as evidence or carries an asserting")
        print("     stamp (healthy: every smoke is correctly quarantined).")

    if n_bad_marker:
        print("\nWARN -- malformed %s marker(s), IGNORED (never blanket-silences):"
              % METABOLIZED_KEY)
        for m in cites["malformed_markers"]:
            print("  - %s: %s" % (m["artifact"], m["reason"]))

    adj = cites["adjudicated"] + stamps["adjudicated"]
    if adj:
        print("\nadjudicated (printed so nothing is hidden; no action owed):")
        for f in cites["adjudicated"]:
            print("  - %s cites %s" % (f["source"], f["run_id"]))
        for f in stamps["adjudicated"]:
            print("  - %s (%s): %s" % (f["run_id"], f["kind"], f["excluded_reason"]))

    return 1 if (args.strict and (n_cite or n_stamp)) else 0


if __name__ == "__main__":
    raise SystemExit(main())
