#!/usr/bin/env python3
"""
Build docs/assets/data/epistemic_overlay.json -- the epistemic-overlay GRAPH layer
(Phase 1, Option C + C-slice of Option D).

DERIVE-ONLY. Reads two inputs and writes one derived output:
  reads : docs/claims/claims.yaml                       (emergent_from edges)
          evidence/experiments/claim_evidence.v1.json   (per-node Beta posteriors)
  writes: docs/assets/data/epistemic_overlay.json       (viz-ready graph overlay)

It NEVER mutates a hand-authored source and PROMOTES/DEMOTES NOTHING. It surfaces:
  1. a per-claim viz bundle: the exp/lit Beta posteriors (mirrored from the
     canonical claim_evidence matrix), own-evidence belief, and a support/weaken
     conflict split for split-fill rendering.
  2. a promotion-gate HONESTY surface: how the candidate->provisional gate WOULD
     read under "posterior mean >= 0.62 AND credible interval excludes 0.5",
     compared against the current bare-threshold heuristic. Informational only.
  3. the emergent_from SINGLE-HOP alarm: a claim believed while a claim it is
     emergent_from is contradicted (unsupported_foundation) or untested
     (untested_foundation). ONE hop -- not belief propagation.

Phase-2 seed: this is the graph layer a factor-graph/MRF grows into. The unary
potentials it reads (exp_posterior/lit_posterior) do not change; pairwise
potentials and damped loopy BP replace the single-hop alarm here. Plan:
evidence/planning/epistemic_overlay_plan.md.

Output is labelled "model-based, not yet calibrated" -- there is no resolved-claim
validation set yet. Do not overstate rigour downstream.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"
CLAIM_EVIDENCE = REPO_ROOT / "evidence" / "experiments" / "claim_evidence.v1.json"
OUTPUT_JSON = REPO_ROOT / "docs" / "assets" / "data" / "epistemic_overlay.json"

# Thresholds (mirror the existing gate + memo sec 4).
GATE_MEAN = 0.62          # candidate->provisional exp_conf gate (decision_criteria.v1)
BELIEF_HIGH = 0.62        # "believed" child
BELIEF_LOW = 0.45         # "contradicted/weak" foundation


def _conflict_split(direction_counts):
    """Support/weaken split for split-fill rendering + conflict_ratio.
    conflict_ratio = 2*min(s,w)/(s+w): 0 = no conflict, 1 = perfectly split."""
    supports = int(direction_counts.get("supports", 0))
    weakens = int(direction_counts.get("weakens", 0))
    total = supports + weakens
    ratio = round((2.0 * min(supports, weakens)) / float(total), 3) if total else 0.0
    return {"supports": supports, "weakens": weakens, "conflict_ratio": ratio}


def _own_belief(meta):
    """Own-evidence (unary) belief: prefer experimental, fall back to literature,
    else None (untested). Returns (source, mean, posterior_dict) or (None, None, None)."""
    exp = meta.get("exp_posterior") or {}
    lit = meta.get("lit_posterior") or {}
    if int(exp.get("n_entries", 0)) > 0:
        return "exp", exp.get("mean"), exp
    if int(lit.get("n_entries", 0)) > 0:
        return "lit", lit.get("mean"), lit
    return None, None, None


def _posterior_gate(meta):
    """Honest promotion-gate surface for candidate->provisional. Compares the
    posterior reading (mean >= 0.62 AND CI excludes 0.5) against the current
    bare exp_conf >= 0.62 heuristic. Informational -- flips no status."""
    exp = meta.get("exp_posterior") or {}
    mean = exp.get("mean")
    ci_low = exp.get("ci_low")
    ci_high = exp.get("ci_high")
    exp_conf = float(meta.get("experimental_confidence", 0.0) or 0.0)
    if mean is None or ci_low is None or ci_high is None:
        return None
    ci_excludes_half = (ci_low > 0.5) or (ci_high < 0.5)
    would_promote = (mean >= GATE_MEAN) and (ci_low > 0.5)
    heuristic_would_promote = exp_conf >= GATE_MEAN
    return {
        "mean": mean,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "ci_excludes_half": ci_excludes_half,
        "would_promote_candidate_to_provisional": would_promote,
        "heuristic_exp_conf": round(exp_conf, 3),
        "heuristic_would_promote": heuristic_would_promote,
        "agrees_with_current_heuristic": would_promote == heuristic_would_promote,
        "note": "confidence dimension only; the live gate also requires entry"
                " count, conflict_ratio and >=1 supporting entry",
    }


def _emergent_alarm(child_id, parents, ev_claims):
    """Single-hop emergent_from alarm. Fires ONLY when the child is itself
    believed (own-evidence >= HIGH). Distinguishes a contradicted foundation
    (unsupported_foundation: parent has evidence and belief <= LOW) from an
    untested one (untested_foundation: parent has no evidence at all). Absence of
    evidence is NOT evidence of absence -- kept as a separate, softer flag."""
    child_meta = ev_claims.get(child_id)
    if not child_meta:
        return None
    _, child_mean, _ = _own_belief(child_meta)
    if child_mean is None or child_mean < BELIEF_HIGH:
        return None  # child not believed -> a weak foundation is unremarkable

    unsupported = []
    untested = []
    for p in parents:
        p_meta = ev_claims.get(p)
        if not p_meta:
            untested.append({"parent": p, "reason": "no_evidence_entries"})
            continue
        _, p_mean, _ = _own_belief(p_meta)
        if p_mean is None:
            untested.append({"parent": p, "reason": "no_directional_evidence"})
        elif p_mean <= BELIEF_LOW:
            unsupported.append({
                "parent": p,
                "parent_mean": p_mean,
                "gap": round(child_mean - p_mean, 4),
            })

    if not unsupported and not untested:
        return None
    out = {"child_mean": child_mean}
    if unsupported:
        unsupported.sort(key=lambda d: d["parent_mean"])  # weakest first
        out["unsupported_foundation"] = {
            "weakest_parent": unsupported[0]["parent"],
            "weakest_parent_mean": unsupported[0]["parent_mean"],
            "gap": unsupported[0]["gap"],
            "all": unsupported,
        }
    if untested:
        out["untested_foundation"] = {"parents": untested}
    return out


def main():
    if not CLAIMS_YAML.exists():
        print(f"ERROR: {CLAIMS_YAML} not found", file=sys.stderr)
        sys.exit(1)
    if not CLAIM_EVIDENCE.exists():
        print(f"ERROR: {CLAIM_EVIDENCE} not found -- run build_experiment_indexes.py first",
              file=sys.stderr)
        sys.exit(1)

    with open(CLAIMS_YAML, encoding="utf-8") as f:
        claims = yaml.safe_load(f)
    if not isinstance(claims, list):
        print("ERROR: claims.yaml top level must be a list", file=sys.stderr)
        sys.exit(1)

    ev = json.loads(CLAIM_EVIDENCE.read_text(encoding="utf-8"))
    ev_claims = ev.get("claims", {}) if isinstance(ev, dict) else {}
    posterior_model = ev.get("posterior_model", {})

    emergent_map = {}
    for c in claims:
        cid = c.get("id")
        if not cid:
            continue
        efrom = c.get("emergent_from") or []
        if efrom:
            emergent_map[cid] = list(efrom)

    overlay = {}
    n_unsupported = 0
    n_untested = 0
    n_gate_disagree = 0
    for cid, meta in ev_claims.items():
        source, mean, _post = _own_belief(meta)
        entry = {
            "exp_posterior": meta.get("exp_posterior"),
            "lit_posterior": meta.get("lit_posterior"),
            "own_belief": {"source": source, "mean": mean},
            "conflict": _conflict_split(meta.get("direction_counts", {})),
        }
        gate = _posterior_gate(meta)
        if gate:
            entry["posterior_gate"] = gate
            if not gate["agrees_with_current_heuristic"]:
                n_gate_disagree += 1
        if cid in emergent_map:
            entry["emergent_from"] = emergent_map[cid]
        overlay[cid] = entry

    # Emergent alarms: iterate over claims WITH emergent_from (child may or may
    # not itself have an evidence row -- if it has none it cannot be "believed",
    # so the alarm self-suppresses inside _emergent_alarm).
    for cid, parents in emergent_map.items():
        alarm = _emergent_alarm(cid, parents, ev_claims)
        if alarm:
            overlay.setdefault(cid, {"exp_posterior": None, "lit_posterior": None,
                                     "own_belief": {"source": None, "mean": None},
                                     "conflict": _conflict_split({}),
                                     "emergent_from": parents})
            overlay[cid]["alarms"] = alarm
            if "unsupported_foundation" in alarm:
                n_unsupported += 1
            if "untested_foundation" in alarm:
                n_untested += 1

    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    out = {
        "schema_version": "epistemic_overlay/v1",
        "generated_at_utc": generated_at,
        "phase": "1 (Option C + C-slice of D)",
        "derive_only": True,
        "promotes_demotes": "nothing",
        "posterior_model": posterior_model,
        "calibration": posterior_model.get("calibration", "model-based, not yet calibrated"),
        "thresholds": {
            "gate_mean": GATE_MEAN,
            "belief_high": BELIEF_HIGH,
            "belief_low": BELIEF_LOW,
        },
        "counts": {
            "claims": len(overlay),
            "emergent_from_claims": len(emergent_map),
            "unsupported_foundation_alarms": n_unsupported,
            "untested_foundation_alarms": n_untested,
            "posterior_gate_disagreements": n_gate_disagree,
        },
        "plan": "evidence/planning/epistemic_overlay_plan.md",
        "claims": dict(sorted(overlay.items())),
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, sort_keys=False)
        f.write("\n")

    print(f"Written {len(overlay)} claims -> {OUTPUT_JSON}")
    print(f"  emergent_from claims: {len(emergent_map)}")
    print(f"  alarms: unsupported_foundation={n_unsupported} "
          f"untested_foundation={n_untested}")
    print(f"  posterior_gate disagreements vs heuristic: {n_gate_disagree}")
    print(f"  calibration: {out['calibration']}")


if __name__ == "__main__":
    main()
