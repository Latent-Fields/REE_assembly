#!/usr/bin/env python3
"""GOV-UMPIRE-1 canonical readiness umpire -- deterministic detector, v1.

Derives two artifacts from the experimental manifest corpus:
    REE_assembly/evidence/planning/canonical_readiness.v1.json
    REE_assembly/evidence/planning/canonical_readiness.md

WHAT THIS IS. A read-only observer over evidence/experiments/**/*.json (flat
manifests + runs/**/manifest.json packs). It answers the questions the claim
(GOV-UMPIRE-1, docs/claims/claims.yaml) requires: is there an identifiable
recurring organism (Gate A); which mechanisms have actually coexisted in the
same run (Gate C -- the substantive new computation this pass adds); and,
because instrumentation for the remaining gates does not exist yet, it says so
explicitly (Gates B/D/E/F) rather than inferring green from absence.

STRUCTURAL PROHIBITION (binding -- see claims.yaml GOV-UMPIRE-1 and the source
thought docs/thoughts/2026-08-31_canonical_readiness_umpire.md section 4). This
module MUST NEVER:
  - write to ree-v3/ree_core/utils/canonical_profile.py or any canonical-profile
    artifact under REE_assembly/docs/architecture/canonical_profiles/;
  - admit a member into a canonical profile, or declare a canonical version;
  - write to docs/claims/claims.yaml or any governance-disposition file.
It may only write its own two derived artifacts named above. It detects,
derives, reports, and escalates state TRANSITIONS. It never adjudicates.

CONSERVATIVE POSTURE. Unknown, false, and unmeasured are three distinct states.
Gates B, D, E and F have no instrumentation in this pass and are reported as
UNMEASURED, not as failing (false) and not as passing (true) -- an unmeasured
gate can never itself satisfy the state machine, so the effect on the overall
verdict is the same as a failure, but the *reason* recorded is honest about
why: nobody looked, not "we looked and it isn't there".

EXPECTED FIRST VERDICT. Per the source thought and the governing claim's own
notes: NO_WARRANT, with reasons, is the expected v1 output. Anything else
should be treated as a bug until independently confirmed -- see the module's
own test suite (test_generate_canonical_readiness.py) for the synthetic
fixtures that pin each gate's arithmetic.

FUTURE GOVERNANCE.SH INTEGRATION (not wired in this pass). The natural hook is
a new step in scripts/governance.sh, after the experiment-index rebuild and
before promotion_demotion_recommendations.md generation, that runs this script
and (a) fails loudly only on a STATE transition (never on a persistent known
state, per the Steward "escalate new information only" principle already used
elsewhere in this codebase for TASK_CLAIMS/TASK_CHIPS staleness), and
(b) appends a one-line transition note to WORKSPACE_STATE.md when the state
changes. That wiring is deliberately deferred to a future pass so this first
landing can be reviewed on its own.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

SCHEMA = "canonical_readiness/v1"

# --------------------------------------------------------------------------
# Constants -- thresholds are stated explicitly so a reviewer can see exactly
# what "recurring" means and argue with the number, rather than it being
# buried in conditional logic.
# --------------------------------------------------------------------------

# A group of manifests must reach at least this size, AND span at least
# DISTINCT_EXPERIMENT_MIN distinct `experiment_type` values, before it counts
# as evidence of a *recurring organism* rather than "several seeds of one
# experiment" or "several unrelated experiments that happened to run against
# the same code checkout in the same week" (both confirmed patterns in the
# live corpus at authoring time -- see the module docstring's sibling design
# note in evidence/planning/thought_intake_2026-08-31_canonical_readiness_umpire.md).
EXACT_RECURRENCE_MIN = 3
FINGERPRINT_RECURRENCE_MIN = 3
DISTINCT_EXPERIMENT_MIN = 2

# Top-level files under evidence/experiments/ that are aggregate/index
# artifacts, not per-run manifests. Never treated as a manifest even though
# they are *.json and sit in the same directory.
NON_MANIFEST_TOP_LEVEL = {
    "arm_fingerprint_index.json",
    "claim_evidence.v1.json",
    "review_tracker.json",
    "substrate_status_snapshot.json",
}

# Flags reported in the human-readable top-N coexistence table.
TOP_N_PAIRS = 15
TOP_N_FLAGS = 20

STATES = (
    "NO_WARRANT",
    "ADMISSION_PASS_WARRANTED",
    "REFERENCE_ORGANISM_REVIEW_WARRANTED",
    "USER_DECISION_REQUIRED",
    "CANONICAL_OBSERVED",
)


# --------------------------------------------------------------------------
# Corpus loading
# --------------------------------------------------------------------------


def _read_json(path: Path) -> Optional[dict]:
    try:
        data = json.loads(path.read_text())
    except Exception:
        return None
    if not isinstance(data, dict) or "run_id" not in data:
        return None
    return data


def load_manifest_corpus(evidence_dir: Path) -> Tuple[Dict[str, dict], Dict[str, int]]:
    """Scan evidence_dir for manifests and return (run_id -> merged manifest, counts).

    Two shapes exist in the corpus:
      - flat: evidence_dir/*.json (older convention; carries
        `enabled_default_off_flags` on some manifests that the newer nested
        pack schema dropped).
      - nested: evidence_dir/**/runs/**/manifest.json (newer
        `experiment_pack/v1` schema).

    When a run_id exists in both shapes, this does a FIELD-LEVEL merge (nested
    value wins per-key when present; flat fills any key nested lacks) rather
    than a whole-record "prefer nested" swap. A whole-record swap was
    measured, at authoring time, to silently zero every `enabled_default_off_flags`
    reading in the corpus (33/33 flag-bearing flat manifests have a nested
    counterpart that omits the field entirely) -- exactly the kind of
    "inferring green from absence" this module's own conservative posture
    exists to avoid. See the design exploration this module was built from.
    """
    counts = {"flat_candidates": 0, "flat_valid": 0, "nested_candidates": 0, "nested_valid": 0}

    flat: Dict[str, dict] = {}
    for path in sorted(evidence_dir.glob("*.json")):
        if path.name in NON_MANIFEST_TOP_LEVEL:
            continue
        counts["flat_candidates"] += 1
        data = _read_json(path)
        if data is not None:
            counts["flat_valid"] += 1
            flat[data["run_id"]] = data

    nested: Dict[str, dict] = {}
    for path in sorted(evidence_dir.glob("**/runs/**/manifest.json")):
        counts["nested_candidates"] += 1
        data = _read_json(path)
        if data is not None:
            counts["nested_valid"] += 1
            nested[data["run_id"]] = data

    merged: Dict[str, dict] = {}
    for run_id, rec in flat.items():
        merged[run_id] = dict(rec)
    for run_id, rec in nested.items():
        if run_id in merged:
            out = dict(merged[run_id])
            for k, v in rec.items():
                out[k] = v
            merged[run_id] = out
        else:
            merged[run_id] = dict(rec)

    counts["merged_total"] = len(merged)
    return merged, counts


def filter_scorable(manifests: Dict[str, dict]) -> Tuple[Dict[str, dict], Dict[str, int]]:
    """Drop manifests explicitly marked as not load-bearing for scoring.

    Mirrors the indexer's own exclusion convention (evidence_direction ==
    "superseded", or a truthy scoring_excluded field) rather than inventing a
    new one -- see CLAUDE.md "EXQ Versioning and Supersession Policy" and the
    `scoring_excluded` field it documents.
    """
    kept: Dict[str, dict] = {}
    excluded_superseded = 0
    excluded_scoring = 0
    for run_id, rec in manifests.items():
        if rec.get("evidence_direction") == "superseded":
            excluded_superseded += 1
            continue
        if rec.get("scoring_excluded"):
            excluded_scoring += 1
            continue
        kept[run_id] = rec
    diag = {
        "input_total": len(manifests),
        "excluded_superseded": excluded_superseded,
        "excluded_scoring_excluded": excluded_scoring,
        "kept_total": len(kept),
    }
    return kept, diag


# --------------------------------------------------------------------------
# Gate A -- identifiable organism
# --------------------------------------------------------------------------


def _flags_signature(flags: Any) -> Optional[Tuple[Tuple[str, str], ...]]:
    if not isinstance(flags, dict) or not flags:
        return None
    return tuple(sorted((str(k), json.dumps(v, sort_keys=True, default=str)) for k, v in flags.items()))


def _group_best(groups: Dict[Any, List[dict]], min_size: int) -> Optional[dict]:
    """Among groups keyed arbitrarily, return the best one that clears
    min_size AND spans >= DISTINCT_EXPERIMENT_MIN distinct experiment_type
    values (the guard against "many seeds of one experiment" and "many
    unrelated one-off experiments sharing a code snapshot" both counting as
    false recurrence)."""
    best = None
    for key, recs in groups.items():
        etypes = {r.get("experiment_type") for r in recs}
        if len(recs) < min_size or len(etypes) < DISTINCT_EXPERIMENT_MIN:
            continue
        if best is None or len(recs) > len(best["recs"]):
            best = {"key": key, "recs": recs, "distinct_experiment_types": sorted(t for t in etypes if t)}
    return best


def compute_gate_a(manifests: Dict[str, dict]) -> dict:
    total = len(manifests)
    with_commit = 0
    with_hash = 0
    with_flags = 0

    exact_groups: Dict[Tuple[str, Tuple[Tuple[str, str], ...]], List[dict]] = defaultdict(list)
    hash_groups: Dict[str, List[dict]] = defaultdict(list)

    for rec in manifests.values():
        commit = rec.get("substrate_commit")
        commit_sha = commit.get("commit") if isinstance(commit, dict) else None
        if commit_sha:
            with_commit += 1
        sub_hash = rec.get("substrate_hash")
        if sub_hash:
            with_hash += 1
            hash_groups[sub_hash].append(rec)
        flags = rec.get("enabled_default_off_flags")
        sig = _flags_signature(flags)
        if sig is not None:
            with_flags += 1
            if commit_sha:
                exact_groups[(commit_sha, sig)].append(rec)

    exact_best = _group_best(exact_groups, EXACT_RECURRENCE_MIN)
    hash_best = _group_best(hash_groups, FINGERPRINT_RECURRENCE_MIN)

    def _summarize(best: Optional[dict]) -> Optional[dict]:
        if best is None:
            return None
        return {
            "group_size": len(best["recs"]),
            "distinct_experiment_types": best["distinct_experiment_types"],
            "example_run_ids": sorted(r.get("run_id") for r in best["recs"])[:8],
        }

    satisfied = exact_best is not None
    if satisfied:
        tier = "exact_recurring_configuration"
        reason_codes: List[str] = []
    else:
        tier = None
        reason_codes = ["NO_IDENTIFIABLE_ORGANISM"]
        if with_commit == 0:
            reason_codes.append("no manifest in the scorable corpus records substrate_commit")
        elif with_flags == 0:
            reason_codes.append(
                "manifests record substrate_commit but none record enabled_default_off_flags, "
                "so exact configuration identity cannot be established"
            )
        else:
            reason_codes.append(
                f"no (substrate_commit, enabled_default_off_flags) combination recurs across "
                f">={DISTINCT_EXPERIMENT_MIN} distinct experiment_type values at size "
                f">={EXACT_RECURRENCE_MIN}"
            )
        if hash_best is not None:
            reason_codes.append(
                "substrate_hash recurrence exists (see fingerprint_recurring_best_group) but is "
                "code-identity only -- it does not by itself establish that the SAME configuration "
                "was tested, only that the SAME code checkout was; per Gate A tier 2 this is "
                "informational, not sufficient to satisfy the gate on its own in this detector"
            )

    return {
        "satisfied": satisfied,
        "tier": tier,
        "reason_codes": reason_codes,
        "diagnostics": {
            "total_scorable_manifests": total,
            "manifests_with_substrate_commit": with_commit,
            "manifests_with_substrate_hash": with_hash,
            "manifests_with_enabled_default_off_flags": with_flags,
            "exact_recurring_best_group": _summarize(exact_best),
            "fingerprint_recurring_best_group": _summarize(hash_best),
            "equivalence_for_purpose_tier_status": "unmeasured",
        },
    }


# --------------------------------------------------------------------------
# Gate C -- coexistence (the substantive new computation)
# --------------------------------------------------------------------------


def compute_gate_c(manifests: Dict[str, dict]) -> dict:
    flag_counts: Counter = Counter()
    pair_counts: Counter = Counter()
    manifests_with_any_flag = 0
    manifests_with_multi_flags = 0

    for rec in manifests.values():
        flags = rec.get("enabled_default_off_flags")
        if not isinstance(flags, dict) or not flags:
            continue
        manifests_with_any_flag += 1
        keys = sorted(flags.keys())
        for k in keys:
            flag_counts[k] += 1
        if len(keys) >= 2:
            manifests_with_multi_flags += 1
            for i in range(len(keys)):
                for j in range(i + 1, len(keys)):
                    pair_counts[(keys[i], keys[j])] += 1

    distinct_flags = sorted(flag_counts.keys())
    n = len(distinct_flags)
    total_possible_pairs = n * (n - 1) // 2
    pairs_observed = len(pair_counts)

    never_paired = sorted(
        flag
        for flag in distinct_flags
        if not any(flag in pair for pair in pair_counts)
    )

    top_pairs = [
        {"a": a, "b": b, "count": c}
        for (a, b), c in sorted(pair_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:TOP_N_PAIRS]
    ]
    top_flags = [
        {"flag": f, "count": c}
        for f, c in flag_counts.most_common(TOP_N_FLAGS)
    ]

    return {
        "status": "computed",
        "contributes_to_state": "informational -- see resolve_state()'s docstring for why Gate C "
        "does not independently gate the state machine in this v1",
        "diagnostics": {
            "manifests_with_any_flag": manifests_with_any_flag,
            "manifests_with_multi_flag_combination": manifests_with_multi_flags,
            "distinct_flags_observed": n,
            "total_possible_pairs_among_observed_flags": total_possible_pairs,
            "pairs_observed_at_least_once": pairs_observed,
            "pairs_never_combined_among_observed": total_possible_pairs - pairs_observed,
            "flags_observed_only_alone_never_paired": never_paired,
            "top_flags_by_corpus_appearance": top_flags,
            "top_coexisting_pairs": top_pairs,
        },
        "caveat": (
            "The flag-bearing subset of the corpus is thin (a small fraction of the scorable "
            "manifests carry enabled_default_off_flags at all) and clustered -- a high pairwise "
            "coexistence rate among the flags that DO appear reflects a small number of "
            "'many-flags-at-once' runs, not a broad, repeated demonstration that the listed "
            "mechanisms jointly produce non-degenerate behaviour across many independent trials. "
            "Read counts, not ratios."
        ),
    }


# --------------------------------------------------------------------------
# Gates B, D, E, F -- explicit unmeasured stubs
# --------------------------------------------------------------------------


def _unmeasured_gate(name: str, description: str) -> dict:
    return {
        "status": "unmeasured",
        "satisfied": False,
        "reason": (
            f"No instrumentation exists in this detector pass for Gate {name} ({description}). "
            "This is reported as UNMEASURED, not FALSE: absence of evidence is not evidence of "
            "absence, and this detector's conservative posture requires that distinction stay "
            "visible rather than collapsing to a green or red reading."
        ),
    }


def compute_gate_b() -> dict:
    return _unmeasured_gate(
        "B",
        "canonical-profile candidate substrate -- admission-doctrine criteria per "
        "evidence/planning/architecture_epoch_investigation.md section 9 "
        "(corpus enablement, cited-evidence-run check, non-degeneracy, known-interaction check)",
    )


def compute_gate_d() -> dict:
    return _unmeasured_gate(
        "D",
        "whole-organism non-degeneracy -- moves, observation variance, action collapse, "
        "candidate generation, no NaN dominance; couples to the GOV-CAPCONTRACT-1 "
        "capability/plasticity contract",
    )


def compute_gate_e() -> dict:
    return _unmeasured_gate(
        "E",
        "behavioural evidence -- Behavioural Evidence Ladder rung attributable to a single "
        "identifiable organism",
    )


def compute_gate_f() -> dict:
    return _unmeasured_gate(
        "F",
        "reproducibility -- same frozen configuration (or same developmental recipe/constitution) "
        "across multiple seeds/runs/machines",
    )


# --------------------------------------------------------------------------
# State machine
# --------------------------------------------------------------------------


def resolve_state(gate_a: dict, gate_b: dict, gate_d: dict, gate_e: dict, gate_f: dict) -> dict:
    """Resolve the umpire state machine.

    Gate C is deliberately NOT a direct input here. Per the source thought
    (docs/thoughts/2026-08-31_canonical_readiness_umpire.md section 2),
    canonical readiness is a set of gates, not a score -- but Gate C's own
    finding ("have these faculties actually coexisted") is evidence *feeding*
    Gates B and D's future instrumentation (a coexistence claim is only
    meaningful once there is an identifiable organism to test it against, and
    once the non-degeneracy/admission-doctrine gates exist to consume it), not
    an independent fifth veto in this v1. Its diagnostics are still reported
    at top level, unabridged, precisely so a reviewer can see the coexistence
    picture without it silently deciding the verdict on its own.

    Gates A/B/D/E/F are each a hard AND-conjunction requirement (never a
    weighted score -- see the source thought's explicit rejection of a
    percentage). An UNMEASURED gate cannot satisfy that conjunction, so it
    behaves like a failure for state-machine purposes even though its own
    status field says "unmeasured" rather than "false".
    """
    gates = {"A": gate_a, "B": gate_b, "D": gate_d, "E": gate_e, "F": gate_f}
    unsatisfied = []
    for name, gate in gates.items():
        satisfied = gate.get("satisfied", False)
        if not satisfied:
            if gate.get("status") == "unmeasured":
                unsatisfied.append(f"Gate {name}: unmeasured ({gate.get('reason')})")
            else:
                reasons = gate.get("reason_codes") or ["unsatisfied"]
                unsatisfied.append(f"Gate {name}: {'; '.join(reasons)}")

    if unsatisfied:
        state = "NO_WARRANT"
    else:
        # Every gate this detector CAN evaluate has passed, but B/D/E/F can
        # never be satisfied in this v1 (they are unconditional stubs), so
        # this branch is unreachable today. It is written out anyway, rather
        # than asserted unreachable, because a future pass that fills in
        # real instrumentation for B/D/E/F should find a working state
        # machine here, not a NotImplementedError.
        state = "ADMISSION_PASS_WARRANTED"

    return {"state": state, "reasons": unsatisfied}


# --------------------------------------------------------------------------
# Transition detection against the prior derived artifact
# --------------------------------------------------------------------------


def _predicate_snapshot(result: dict) -> Dict[str, Any]:
    return {
        "state": result["state"],
        "gate_a_satisfied": result["gates"]["A"]["satisfied"],
        "gate_b_status": result["gates"]["B"]["status"],
        "gate_d_status": result["gates"]["D"]["status"],
        "gate_e_status": result["gates"]["E"]["status"],
        "gate_f_status": result["gates"]["F"]["status"],
    }


def diff_against_prior(current: dict, prior: Optional[dict]) -> dict:
    """Classify each tracked predicate as unchanged / newly_satisfied /
    newly_blocked / withdrawn / restored / initial, per the Steward
    "escalate new information only" principle this detector borrows.
    """
    current_snap = _predicate_snapshot(current)
    if prior is None:
        return {
            "has_prior": False,
            "predicate_transitions": {k: "initial" for k in current_snap},
            "state_transition": "initial",
            "escalate": True,
        }

    prior_snap = _predicate_snapshot(prior)
    transitions: Dict[str, str] = {}
    for key, cur_val in current_snap.items():
        prev_val = prior_snap.get(key)
        if prev_val == cur_val:
            transitions[key] = "unchanged"
            continue
        # Boolean-shaped predicates get satisfied/blocked/restored/withdrawn
        # vocabulary; string-shaped ones (state, gate statuses) just report
        # the from->to change.
        if isinstance(cur_val, bool) and isinstance(prev_val, bool):
            if cur_val and not prev_val:
                transitions[key] = "newly_satisfied"
            elif not cur_val and prev_val:
                transitions[key] = "newly_blocked"
            else:
                transitions[key] = "changed"
        else:
            transitions[key] = f"changed ({prev_val!r} -> {cur_val!r})"

    state_changed = current_snap["state"] != prior_snap["state"]
    if state_changed:
        state_transition = f"{prior_snap['state']} -> {current_snap['state']}"
    else:
        state_transition = "unchanged"

    escalate = state_changed or any(v not in ("unchanged",) for v in transitions.values())

    return {
        "has_prior": True,
        "prior_state": prior_snap["state"],
        "predicate_transitions": transitions,
        "state_transition": state_transition,
        "escalate": escalate,
    }


# --------------------------------------------------------------------------
# Assembly
# --------------------------------------------------------------------------


def build_readiness_report(evidence_dir: Path, generated_at_utc: str) -> dict:
    raw_manifests, load_counts = load_manifest_corpus(evidence_dir)
    scorable, filter_diag = filter_scorable(raw_manifests)

    gate_a = compute_gate_a(scorable)
    gate_b = compute_gate_b()
    gate_c = compute_gate_c(scorable)
    gate_d = compute_gate_d()
    gate_e = compute_gate_e()
    gate_f = compute_gate_f()

    resolved = resolve_state(gate_a, gate_b, gate_d, gate_e, gate_f)

    result = {
        "schema": SCHEMA,
        "generated_at_utc": generated_at_utc,
        "state": resolved["state"],
        "reasons": resolved["reasons"],
        "corpus": {"load": load_counts, "filter": filter_diag},
        "gates": {
            "A": gate_a,
            "B": gate_b,
            "C": gate_c,
            "D": gate_d,
            "E": gate_e,
            "F": gate_f,
        },
    }
    return result


def render_markdown(result: dict, transition: dict) -> str:
    state = result["state"]
    lines: List[str] = []
    lines.append(f"# Canonical Readiness ({result['schema']})")
    lines.append("")
    lines.append(f"Generated: {result['generated_at_utc']}")
    lines.append("")
    lines.append(f"## Verdict: {state}")
    lines.append("")
    if state == "NO_WARRANT":
        lines.append(
            "There is not yet sufficient evidence to justify a canonical-profile admission "
            "pass. This is the normal developmental state before the relevant conditions have "
            "converged -- it is not a failure of the project."
        )
        lines.append("")
        lines.append("Reasons this pass:")
        for r in result["reasons"]:
            lines.append(f"- {r}")
    else:
        lines.append("Reasons this pass:")
        for r in result["reasons"] or ["all evaluable gates satisfied"]:
            lines.append(f"- {r}")
    lines.append("")

    lines.append("## Transition since the previous derived artifact")
    lines.append("")
    if not transition["has_prior"]:
        lines.append("No prior artifact found -- this is the first run. Every predicate reads INITIAL.")
    else:
        lines.append(f"State: {transition['state_transition']}")
        if transition["escalate"]:
            lines.append("")
            lines.append("**ESCALATION** -- one or more predicates changed since the last run.")
        lines.append("")
        lines.append("Predicate transitions:")
        for k, v in transition["predicate_transitions"].items():
            lines.append(f"- {k}: {v}")
    lines.append("")

    lines.append("## Gate A -- identifiable organism")
    ga = result["gates"]["A"]
    lines.append("")
    lines.append(f"Satisfied: {ga['satisfied']} (tier: {ga['tier']})")
    d = ga["diagnostics"]
    lines.append(
        f"- Scorable manifests: {d['total_scorable_manifests']} "
        f"(with substrate_commit: {d['manifests_with_substrate_commit']}, "
        f"with substrate_hash: {d['manifests_with_substrate_hash']}, "
        f"with enabled_default_off_flags: {d['manifests_with_enabled_default_off_flags']})"
    )
    if d["exact_recurring_best_group"]:
        g = d["exact_recurring_best_group"]
        lines.append(
            f"- Best exact-recurring-configuration group: {g['group_size']} manifests across "
            f"{len(g['distinct_experiment_types'])} distinct experiment types"
        )
    else:
        lines.append("- No exact-recurring-configuration group clears the threshold.")
    if d["fingerprint_recurring_best_group"]:
        g = d["fingerprint_recurring_best_group"]
        lines.append(
            f"- Best substrate_hash (code-identity only) recurrence: {g['group_size']} manifests "
            f"across {len(g['distinct_experiment_types'])} distinct experiment types"
        )
    lines.append(f"- Equivalent-for-purpose tier: {d['equivalence_for_purpose_tier_status']}")
    lines.append("")

    lines.append("## Gate C -- coexistence (mechanisms exercised together)")
    gc = result["gates"]["C"]
    lines.append("")
    dc = gc["diagnostics"]
    lines.append(
        f"- Manifests carrying any enabled_default_off_flags: {dc['manifests_with_any_flag']} "
        f"({dc['manifests_with_multi_flag_combination']} with >=2 flags)"
    )
    lines.append(
        f"- Distinct flags observed: {dc['distinct_flags_observed']}; pairs observed at least "
        f"once: {dc['pairs_observed_at_least_once']} of {dc['total_possible_pairs_among_observed_flags']} "
        f"possible ({dc['pairs_never_combined_among_observed']} never combined)"
    )
    if dc["top_coexisting_pairs"]:
        lines.append("")
        lines.append("Top coexisting pairs:")
        for p in dc["top_coexisting_pairs"][:10]:
            lines.append(f"- {p['a']} + {p['b']}: {p['count']}")
    lines.append("")
    lines.append(f"Caveat: {gc['caveat']}")
    lines.append("")

    for gate_name, title in (
        ("B", "canonical-profile candidate substrate"),
        ("D", "whole-organism non-degeneracy"),
        ("E", "behavioural evidence"),
        ("F", "reproducibility"),
    ):
        g = result["gates"][gate_name]
        lines.append(f"## Gate {gate_name} -- {title}")
        lines.append("")
        lines.append(f"Status: {g['status'].upper()}")
        lines.append(f"{g['reason']}")
        lines.append("")

    lines.append("---")
    lines.append(
        "This artifact is produced by REE_assembly/scripts/generate_canonical_readiness.py, a "
        "read-only detector. It has no authority to admit a canonical profile member or declare "
        "a canonical version. See docs/claims/claims.yaml GOV-UMPIRE-1."
    )
    lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def _default_paths() -> Tuple[Path, Path, Path]:
    """Return (evidence_experiments_dir, output_json_path, output_md_path),
    resolved relative to this script's own location so it works from any
    cwd (including a worktree, per CLAUDE.md's worktree-safety rules)."""
    repo_root = Path(__file__).resolve().parent.parent  # REE_assembly/
    evidence_dir = repo_root / "evidence" / "experiments"
    out_json = repo_root / "evidence" / "planning" / "canonical_readiness.v1.json"
    out_md = repo_root / "evidence" / "planning" / "canonical_readiness.md"
    return evidence_dir, out_json, out_md


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if the state (or any tracked predicate) changed since the prior "
        "committed artifact. Still writes the artifacts.",
    )
    parser.add_argument(
        "--evidence-dir",
        type=Path,
        default=None,
        help="Override the evidence/experiments/ directory to scan (for testing).",
    )
    parser.add_argument(
        "--out-json",
        type=Path,
        default=None,
        help="Override the output JSON path (for testing).",
    )
    parser.add_argument(
        "--out-md",
        type=Path,
        default=None,
        help="Override the output Markdown path (for testing).",
    )
    args = parser.parse_args(argv)

    default_evidence, default_json, default_md = _default_paths()
    evidence_dir = args.evidence_dir or default_evidence
    out_json = args.out_json or default_json
    out_md = args.out_md or default_md

    if not evidence_dir.is_dir():
        print(f"ERROR: evidence directory not found: {evidence_dir}", file=sys.stderr)
        return 2

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    result = build_readiness_report(evidence_dir, generated_at)

    prior: Optional[dict] = None
    if out_json.exists():
        try:
            prior = json.loads(out_json.read_text())
        except Exception:
            prior = None

    transition = diff_against_prior(result, prior)
    result["transition_since_prior"] = transition

    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    md = render_markdown(result, transition)
    out_md.write_text(md)

    print(f"canonical readiness: {result['state']}")
    for r in result["reasons"]:
        print(f"  reason: {r}")
    print(f"transition: {transition['state_transition']}")
    print(f"wrote: {out_json}")
    print(f"wrote: {out_md}")

    if args.check and transition["escalate"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
