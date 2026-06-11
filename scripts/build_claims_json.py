#!/usr/bin/env python3
"""
Build docs/assets/data/claims.json from docs/claims/claims.yaml.

Run this any time claims.yaml is updated (add to governance pipeline).
Output is consumed by docs/assets/js/claim-tooltips.js for hover tooltips
on the GitHub Pages site.

Runs scripts/validate_claims.py in warn-only mode before emitting JSON.
"""
import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent
CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"
OUTPUT_JSON = REPO_ROOT / "docs" / "assets" / "data" / "claims.json"
VALIDATOR = Path(__file__).parent / "validate_claims.py"
CLAIM_EVIDENCE = REPO_ROOT / "evidence" / "experiments" / "claim_evidence.v1.json"

# Epistemic-stance split (shown / believed / asked) -- a derived VIEW over the
# existing registry, not a new hand-labelled axis. The three buckets are the
# author-facing reading of the claim's epistemic status:
#   shown    -- experimentally confirmed: exp_conf cleared the candidate->
#               provisional gate (>= 0.62, the decision_criteria threshold).
#   asked    -- a question, not an assertion (the open-question / derivational /
#               out-of-domain epistemic categories). These should carry a
#               `what_would_answer` line -- the falsification condition that
#               distinguishes genuinely-new epistemic ground from the merely
#               not-yet-operationalised.
#   believed -- an assertion (INV/ARC/MECH/SD) committed to but not yet
#               experimentally shown. The large ideas-first tail.
# An explicit `epistemic_stance: shown|believed|asked` on a claim overrides the
# derivation (same optional-override pattern as `epistemic_category`).
SHOWN_EXP_CONF_GATE = 0.62  # candidate->provisional gate (decision_criteria.v1.yaml)
ASKED_CATEGORIES = {"answer_state", "derivational", "out_of_domain"}
ASKED_CLAIM_TYPES = {"open_question", "question"}
STANCE_VALUES = {"shown", "believed", "asked"}


def resolve_epistemic_stance(claim, exp_conf):
    """Return (stance, is_explicit). Explicit `epistemic_stance` overrides;
    otherwise derive from claim_type + epistemic_category + exp_conf."""
    explicit = str(claim.get("epistemic_stance", "") or "").strip().lower()
    if explicit in STANCE_VALUES:
        return explicit, True
    claim_type = str(claim.get("claim_type", "") or "").strip()
    category = str(claim.get("epistemic_category", "") or "").strip().lower()
    if category in ASKED_CATEGORIES or claim_type in ASKED_CLAIM_TYPES:
        return "asked", False
    if exp_conf >= SHOWN_EXP_CONF_GATE:
        return "shown", False
    return "believed", False


def load_exp_conf():
    """{claim_id: experimental_confidence} from the indexer's evidence matrix.
    Best-effort: an absent/stale matrix just yields exp_conf=0 (-> 'believed'
    for untested assertions), which is the correct default."""
    if not CLAIM_EVIDENCE.exists():
        return {}
    try:
        data = json.loads(CLAIM_EVIDENCE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    claims = data.get("claims", {}) if isinstance(data, dict) else {}
    out = {}
    for cid, meta in claims.items():
        if isinstance(meta, dict):
            try:
                out[cid] = float(meta.get("experimental_confidence", 0.0) or 0.0)
            except (TypeError, ValueError):
                out[cid] = 0.0
    return out


def run_validator():
    if not VALIDATOR.exists():
        return
    subprocess.run([sys.executable, str(VALIDATOR)], check=False)


def main():
    if not CLAIMS_YAML.exists():
        print(f"ERROR: {CLAIMS_YAML} not found", file=sys.stderr)
        sys.exit(1)

    run_validator()

    with open(CLAIMS_YAML, encoding="utf-8") as f:
        claims = yaml.safe_load(f)

    if not isinstance(claims, list):
        print("ERROR: claims.yaml top level must be a list", file=sys.stderr)
        sys.exit(1)

    exp_conf_by_claim = load_exp_conf()

    output = {}
    stance_counts = {"shown": 0, "believed": 0, "asked": 0}
    for claim in claims:
        claim_id = claim.get("id")
        if not claim_id:
            continue
        entry = {
            "type": claim.get("claim_type", ""),
            "subject": claim.get("subject", ""),
            "status": claim.get("status", ""),
            "title": claim.get("title", ""),
        }
        if claim.get("claim_type") == "invariant":
            itype = claim.get("invariant_type")
            if itype is not None:
                entry["invariant_type"] = itype
            efrom = claim.get("emergent_from") or []
            if efrom:
                entry["emergent_from"] = list(efrom)
            if claim.get("pending_substrate_reconfirmation"):
                entry["pending_substrate_reconfirmation"] = True
        stance, is_explicit = resolve_epistemic_stance(
            claim, exp_conf_by_claim.get(claim_id, 0.0))
        entry["epistemic_stance"] = stance
        if is_explicit:
            entry["epistemic_stance_explicit"] = True
        wwa = claim.get("what_would_answer")
        if wwa:
            entry["what_would_answer"] = wwa
        stance_counts[stance] = stance_counts.get(stance, 0) + 1
        output[claim_id] = entry

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, sort_keys=True)
        f.write("\n")

    print(f"Written {len(output)} claims -> {OUTPUT_JSON}")
    print(f"  epistemic_stance: shown={stance_counts['shown']} "
          f"believed={stance_counts['believed']} asked={stance_counts['asked']}")


if __name__ == "__main__":
    main()
