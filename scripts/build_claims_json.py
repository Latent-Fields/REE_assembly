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


REPO_ROOT = Path(__file__).parent.parent
CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"
OUTPUT_JSON = REPO_ROOT / "docs" / "assets" / "data" / "claims.json"
VALIDATOR = Path(__file__).parent / "validate_claims.py"
CLAIM_EVIDENCE = REPO_ROOT / "evidence" / "experiments" / "claim_evidence.v1.json"
SUBSTRATE_QUEUE = REPO_ROOT / "evidence" / "planning" / "substrate_queue.json"

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
# A question that has been answered/retired/superseded -- or settled by an
# adjudication decision -- is no longer ASKED even though it keeps its
# open_question/question claim_type for history. Such claims fall through to the
# exp_conf split (shown if confirmed, else believed) instead of asked, so they
# are not expected to carry a `what_would_answer` falsification condition.
# Mirror of the terminal-status guard in scripts/validate_claims.py.
TERMINAL_STATUSES = {
    "legacy", "resolved", "retired", "superseded", "candidate_resolved",
    "deprecated", "applied",
}
STANCE_VALUES = {"shown", "believed", "asked"}


def resolve_epistemic_stance(claim, exp_conf):
    """Return (stance, is_explicit). Explicit `epistemic_stance` overrides;
    otherwise derive from claim_type + epistemic_category + exp_conf."""
    explicit = str(claim.get("epistemic_stance", "") or "").strip().lower()
    if explicit in STANCE_VALUES:
        return explicit, True
    claim_type = str(claim.get("claim_type", "") or "").strip()
    category = str(claim.get("epistemic_category", "") or "").strip().lower()
    status = str(claim.get("status", "") or "").strip().lower()
    lifecycle = str(claim.get("lifecycle_stage", "") or "").strip().lower()
    is_terminal = status in TERMINAL_STATUSES or lifecycle == "adjudicated"
    if not is_terminal and (category in ASKED_CATEGORIES
                            or claim_type in ASKED_CLAIM_TYPES):
        return "asked", False
    if exp_conf >= SHOWN_EXP_CONF_GATE:
        return "shown", False
    return "believed", False


# ── Assembly-state consolidation (MOVE-4 claims-layer follow-on, 2026-06-22) ──
# ONE canonical, machine-readable claim-level field that consolidates the 6
# scattered substrate-blocked conventions (epistemic_category
# substrate_conditional / substrate_ceiling, v3_pending, implementation_phase>=v4,
# implementation_phase=v3, the pending_* booleans) WITHOUT collapsing their
# distinct semantics: each maps to a distinct `assembly_state` value, so the same
# maturity buckets MOVE-4 draws over closure-plan nodes can be drawn over the
# whole claims registry. This is ADDITIVE -- it does not change any
# promotion/demotion/hold dispatch (those still read epistemic_category /
# v3_pending in build_experiment_indexes.py). An explicit `assembly_state` on a
# claim overrides the derivation (same pattern as epistemic_category /
# epistemic_stance).
#
# CANONICAL DERIVATION -- kept byte-for-byte in sync with
# serve.py:_resolve_claim_assembly_state (MOVE-1 precedent: one source of truth,
# a synced sibling copy). Bucket mapping is shared with serve.py:_claims_assembly_view.
ASSEMBLY_STATES = {
    "mature",            # adjudication substantially done (active/stable)
    "enriching",         # substrate_ceiling: V3-tractable, substrate too coarse -> enrich
    "awaiting_substrate",  # substrate_conditional: planned upstream not yet built
    "gated_v3",          # v3_pending / implementation_phase=v3 manual-or-phase hold
    "deferred_future",   # implementation_phase v4/v5/v6/post_v5 (parked out of v3)
    "remaining",         # open assertion, not assembly-blocked
    "parked",            # legacy/superseded/retired/applied (inactive)
    "blocked",           # explicitly blocked
}
ASSEMBLY_STATUS_VALUES = {"queued", "in_progress", "built"}

_INACTIVE_STATUSES = {"legacy", "superseded", "retired", "applied", "deprecated"}
_MATURE_STATUSES = {"active", "stable", "provisional"}
_BLOCKED_STATUSES = {"blocked", "upstream_blocked", "blocked_pending_substrate"}
_FUTURE_PHASES = {"v4", "v5", "v6", "post_v5", "post_v4"}


def _norm_assembly_status_token(raw):
    """Map a (messy, free-text) substrate_queue status/implementation_status blob
    to one of {built, in_progress, queued}. Robust to the giant prose blobs some
    queue rows carry: keys only off the FIRST token / known leading words."""
    s = str(raw or "").strip().lower()
    if not s:
        return None
    head = ""
    for ch in s:
        if ch.isalnum() or ch == "_":
            head += ch
        else:
            break
    # built: implemented / validated / landed / lifted / done
    if head.startswith(("implemented", "validated", "landed", "done")):
        return "built"
    if "ceiling_lifted" in s or head.startswith("ceiling"):
        return "built"
    # actively under construction
    if head.startswith(("phase", "amend", "substrate")) or "pending_validation" in s:
        return "in_progress"
    # everything else (candidate_*, proposed, pending_implementation, design_*,
    # parked_*, None) -> queued / not-yet-built
    return "queued"


def build_substrate_claim_index(path=SUBSTRATE_QUEUE):
    """Reverse map {claim_id: {"awaiting": sd_id, "assembly_status": state}} from
    substrate_queue.json `queue[].unblocks_claims`. When a claim is unblocked by
    several substrate items, keep the MOST-ADVANCED build state (built >
    in_progress > queued) and record that item's sd_id as the `awaiting` pointer.
    Best-effort: an absent/unreadable queue yields {} (everything falls back to
    epistemic_category-only derivation)."""
    order = {"queued": 0, "in_progress": 1, "built": 2}
    out = {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return out
    queue = data.get("queue", []) if isinstance(data, dict) else []
    for it in queue:
        if not isinstance(it, dict):
            continue
        sd_id = it.get("sd_id")
        # implementation_status is the cleaner signal; fall back to status.
        astatus = (_norm_assembly_status_token(it.get("implementation_status"))
                   or _norm_assembly_status_token(it.get("status"))
                   or ("built" if it.get("ready") is True else "queued"))
        for cid in (it.get("unblocks_claims") or []):
            prev = out.get(cid)
            if prev is None or order[astatus] > order[prev["assembly_status"]]:
                out[cid] = {"awaiting": sd_id, "assembly_status": astatus}
    return out


def resolve_assembly_state(claim, substrate_index=None):
    """Return (assembly_state, awaiting, assembly_status, is_explicit_state).

    assembly_state consolidates the 6 conventions; awaiting/assembly_status are
    taken from explicit claim fields when present, else auto-joined from
    substrate_queue (substrate_index). CANONICAL -- keep in sync with
    serve.py:_resolve_claim_assembly_state."""
    substrate_index = substrate_index or {}
    cid = str(claim.get("id") or "")
    status = str(claim.get("status", "") or "").strip().lower()
    epi = str(claim.get("epistemic_category", "") or "").strip().lower()
    phase = str(claim.get("implementation_phase", "") or "").strip().lower()
    v3p = bool(claim.get("v3_pending"))

    # ── awaiting / assembly_status edge: explicit wins, else auto-join ──
    join = substrate_index.get(cid, {})
    awaiting = str(claim.get("awaiting", "") or "").strip() or str(join.get("awaiting") or "")
    explicit_astatus = str(claim.get("assembly_status", "") or "").strip().lower()
    if explicit_astatus in ASSEMBLY_STATUS_VALUES:
        assembly_status = explicit_astatus
    else:
        assembly_status = join.get("assembly_status") or ""

    # ── assembly_state: explicit override first ──
    explicit_state = str(claim.get("assembly_state", "") or "").strip().lower()
    if explicit_state in ASSEMBLY_STATES:
        return explicit_state, awaiting, assembly_status, True

    # ── canonical derivation (order matters; most-specific WHY first) ──
    if status in _INACTIVE_STATUSES:
        state = "parked"
    elif status in _BLOCKED_STATUSES:
        state = "blocked"
    elif epi == "substrate_conditional":
        state = "awaiting_substrate"
    elif epi == "substrate_ceiling":
        state = "enriching"
    elif v3p:
        # explicit manual hold: held regardless of phase. (substrate_*/blocked
        # above are more informative and win.)
        state = "gated_v3"
    elif phase in _FUTURE_PHASES:
        state = "deferred_future"
    elif status in _MATURE_STATUSES:
        # adjudicated; a retained factual implementation_phase=v3 does NOT regate
        # a promoted claim (see MECH-306 precedent in claims.yaml).
        state = "mature"
    elif phase == "v3":
        state = "gated_v3"
    else:
        state = "remaining"
    return state, awaiting, assembly_status, False


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

    # Share validate_claims' duplicate-key loader. This script is the PRODUCER
    # of docs/assets/data/claims.json, so a last-wins parse here bakes the
    # silent key loss into a derived artifact that looks perfectly well-formed.
    # governance.sh gates on validate_claims.py --strict before reaching this
    # step, but the header of that script also documents running this one
    # standalone -- and run_validator() above is check=False without --strict,
    # so standalone it would print the error and then emit the bad artifact
    # anyway. Duplicates abort here; every other validator finding keeps its
    # existing non-blocking posture (the gate authority stays in one place,
    # validate_claims.py --strict).
    sys.path.insert(0, str(Path(__file__).parent))
    from validate_claims import load_claims as _load_claims_checked

    claims, duplicate_issues = _load_claims_checked()
    if duplicate_issues:
        print(
            f"ERROR: claims.yaml has {len(duplicate_issues)} duplicated key(s); "
            "refusing to build claims.json from a last-wins parse.",
            file=sys.stderr)
        for _lvl, msg in duplicate_issues:
            print(f"  ERROR: {msg}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(claims, list):
        print("ERROR: claims.yaml top level must be a list", file=sys.stderr)
        sys.exit(1)

    exp_conf_by_claim = load_exp_conf()
    substrate_index = build_substrate_claim_index()

    output = {}
    stance_counts = {"shown": 0, "believed": 0, "asked": 0}
    assembly_counts = {}
    for claim in claims:
        claim_id = claim.get("id")
        if not claim_id:
            continue
        entry = {
            "type": claim.get("claim_type", ""),
            "subject": claim.get("subject", ""),
            "status": claim.get("status", ""),
            "title": claim.get("title", ""),
            # Undirected reciprocal-coupling layer (GOV-EDGE-1, 2026-09-04):
            # written on both endpoints in claims.yaml, distinct from the
            # directed `depends_on` DAG. Always emitted (default []) so a
            # consumer can tell "no coupling" from "field unknown".
            "coupled_with": [str(x) for x in (claim.get("coupled_with") or [])],
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

        # Assembly-state consolidation (MOVE-4 claims-layer follow-on). Always
        # emitted so the explorer / closure-map claims toggle can bucket the whole
        # registry by maturity. awaiting/assembly_status are emitted only when
        # non-empty (explicit field or substrate_queue auto-join).
        a_state, a_awaiting, a_status, a_explicit = resolve_assembly_state(
            claim, substrate_index)
        entry["assembly_state"] = a_state
        if a_explicit:
            entry["assembly_state_explicit"] = True
        if a_awaiting:
            entry["awaiting"] = a_awaiting
        if a_status:
            entry["assembly_status"] = a_status
        rv = claim.get("revisit_after")
        if rv:
            entry["revisit_after"] = str(rv)
        assembly_counts[a_state] = assembly_counts.get(a_state, 0) + 1

        output[claim_id] = entry

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, sort_keys=True)
        f.write("\n")

    print(f"Written {len(output)} claims -> {OUTPUT_JSON}")
    print(f"  epistemic_stance: shown={stance_counts['shown']} "
          f"believed={stance_counts['believed']} asked={stance_counts['asked']}")
    print("  assembly_state: " + " ".join(
        f"{k}={assembly_counts[k]}" for k in sorted(assembly_counts)))


if __name__ == "__main__":
    main()
