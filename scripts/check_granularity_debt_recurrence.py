#!/usr/bin/env python3
"""Granularity-debt recurrence audit (governance Step 6a-v-quater, GOV-GRAN-1).

The THIRD sibling of the claim-keyed recurrence auditors, and the standing-scan
complement to the reactive granularity-debt trigger in the `/failure-autopsy`
skill. The three siblings partition the "recurrent FAIL circling one target"
space by what the recurrence MEANS:

  * GOV-CEIL-1 (check_substrate_ceiling_audit.py) -- CLAIM-keyed, SAME wall.
    >= N `substrate_ceiling` verdicts on one claim -> the claim may be
    unbuildable-as-stated -> user-approved DEMOTION. The signature repeats.
  * GOV-DIAG-1 (check_diagnostic_chain_recurrence.py) -- CLAIMLESS, by bears_on.
    >= N pure-diagnostic (`claim_ids: []`) no-verdict autopsies on one
    work-stream -> the QUESTION is mis-posed -> RE-POSE. Invisible to claim
    counters.
  * GOV-GRAN-1 (this file) -- CLAIM-keyed, DIFFERENT signatures. >= N no-verdict
    non-ceiling autopsies on one claim, failing in structurally DIFFERENT ways
    -> the CLAIM is too coarse (it is several claims) -> `/claim-synthesis`
    decomposition. The claim is not wrong and not hitting one wall; it keeps
    breaking differently because it bundles >1 mechanism.

WHY THIS AUDIT EXISTS. The `/failure-autopsy` skill already tells its author to
read the claim's cluster at write-time (`granularity_debt_cluster.py`) and, on the
second-or-later autopsy circling a claim, fire a `granularity_debt_trigger` +
route to `/claim-synthesis`. That is
a REACTIVE, human-run check: it depends on (a) the second failure being autopsied
at all and (b) the author running the reader and (c) the `/claim-synthesis` handoff
actually being executed. The non-degeneracy net (`scoring_excluded="degenerate"`)
catches the INVERSE granularity problem (an over-specified / degenerate criterion)
with STANDING CODE that runs on every index build and cannot be forgotten. This
audit gives the too-COARSE direction the same standing-scan property: it sweeps
the whole confirmed-autopsy corpus every governance cycle and surfaces two things
a human author can miss --

  1. DROPPED HANDOFF (the reliability hole made mechanical): an autopsy that
     EXPLICITLY fired the granularity trigger / routed to `/claim-synthesis`, but
     for which NO `claim_synthesis_<claim>_*.md` proposal doc exists. The trigger
     fired and the follow-through never happened. This is exactly the "relies on
     a human doing the next step" failure the standing scan is meant to close.
  2. UNFLAGGED RECURRENCE: a claim with >= N no-verdict non-ceiling autopsies
     where no single author fired the trigger, because the recurrence lives
     ACROSS separate autopsy sessions that no one author saw together.

WHAT IS COUNTED. A "granularity-debt hit" is one confirmed (`status: confirmed`)
`failure_autopsy_*.json` target that:

  (i)   carries a NON-empty `claim_ids` -- CLAIM-keyed (the claimless case is
        GOV-DIAG-1's job; counting it here would double-count); AND
  (ii)  resolved WITHOUT a clean verdict -- `recommended_evidence_direction in
        {non_contributory, inconclusive}`. A clean `weakens` / `refutes` is a
        FALSIFICATION (decomposing a wrong claim does not rescue it -> that is
        GOV-CEIL-1 / demotion territory, not granularity debt); AND
  (iii) `recommended_epistemic_category NOT in _EPI_SUPPRESS_PROPOSAL` -- excludes
        substrate_ceiling / substrate_conditional / derivational / etc. Those are
        the SAME-wall / substrate-enrichment story owned by GOV-CEIL-1 and the
        `/claim-synthesis` Step-1 metabolized set; re-flagging them here would
        double-count with GOV-CEIL-1 (symmetric to GOV-DIAG-1 excluding
        claim-tagged targets). What survives is measurement_degeneracy /
        measurement_test_design / etc. -- exactly where the granularity-debt vs
        test-design-debt fork lives.

Hits are keyed on `claim_id`; each hit is a distinct (artifact stem, run_id) so
re-listing a claim across an artifact's targets does not inflate the count. Note
this counts autopsy TARGETS whose own `claim_ids` name the claim -- never files in
the claim's topical neighbourhood, the neighbourhood-grep reading that over-fired
the reactive skill trigger until 2026-07-22 (see `granularity_debt_cluster.py`).

SELF-CHECK ON THE COUNT (added 2026-07-22). Every surfaced record carries the
`claim_alignment` distribution of its hits, bucketed from each target's own
`four_layer_diagnosis.claim_alignment`. A cluster in which NO target reads
`weakened` is measurement or implementation debt, not granularity debt, however
many autopsies exist -- so a P0/P1 whose distribution shows no `weakened` is
flagged as such inline. The count alone is a weak signal; the distribution is
what decided all three claims examined in the 2026-07-22 `/claim-synthesis` pass
(MECH-204 even had a target reading `strengthened`). This is REPORTED, not
enforced: the audit stays warn-only and the discrimination stays human.

METABOLIZED EXCLUSIONS (a claim is NOT surfaced when ANY fires -- mirrors the
`/claim-synthesis` Step-1 disjunction, using only the PRECISE markers to avoid
false exclusion):
  * the claim's `granularity_debt_disposition` in _GD_ADJUDICATED_NOT_DEBT -- a
    human ran the discrimination and recorded verdict (b) NOT-granularity-debt
    (`coherent_campaign` / `passenger_co_claim`) where no substrate-relane is
    honest (working substrate, live iteration, or a passenger co-claim). This is
    the marker for the THIRD adjudication outcome the other two markers cannot
    express (they only cover "split it" and "it's a substrate/same-wall story");
    without it, an adjudicated coherent campaign re-surfaced every cycle. Silences
    THIS scan only; touches no epistemic_category (no false GOV-CEIL-1 seed);
    pair with a `granularity_debt_recurrence_note` for the human-readable trail;
  * the claim's `epistemic_category` in _EPI_SUPPRESS_PROPOSAL (the cheap
    machine-readable pass -- enrichment-in-progress, not undetected debt);
  * the claim carries a `decomposition_note` (the exact marker `/claim-synthesis`
    stamps on an umbrella it has already split -- e.g. INV-064 after 2026-07-12);
  * a `claim_synthesis_<claim>_*.md` proposal doc already exists (already
    synthesized -- done or in-flight);
  * the claim's `status` is dead (resolved / superseded / deprecated);
  * CO-TAGGED-BYSTANDER absorption: EVERY one of the claim's hits is on an
    autopsy target that co-tags an already-synthesized-or-decomposed SIBLING
    claim (the recurrence subject is that already-metabolized umbrella, and this
    claim is only along for the ride). Symmetric to the `_trigger_claims`
    multi-claim narrowing on the P0 path: a run tagged `[SD-034, MECH-268,
    MECH-090]` whose recurrence is SD-034's closure coupling (decomposed into
    MECH-445/446 on 2026-06-19) must not fan its no-verdict hit out to the
    co-tagged MECH-268 -- SD-034 and MECH-090 are already excluded as
    synthesized, so the un-named third claim would otherwise surface alone as a
    pure false positive. Only fires when the claim has NO hit of its own on a
    target free of a metabolized sibling.
  Deliberately NOT excluded on raw reverse-dep fan-in alone: a claim can be
  depended-upon by unrelated downstream consumers (INV-064 <- MECH-214/215)
  without having been decomposed, so bare fan-in over-excludes. The precise
  "already decomposed" markers above are used instead.

THE OVERLAY (ACTIONABLE, warn-only), in priority order:
  * P0 dropped_handoff  -- explicit trigger fired, no proposal doc, not otherwise
                           metabolized. A mechanical reliability failure.
  * P1 unflagged_recurrence -- >= N no-verdict non-ceiling hits, not metabolized,
                           no proposal doc, no explicit trigger. Surface for the
                           human granularity-debt-vs-coherent-substrate-campaign
                           discrimination (the judgment the skill keeps human --
                           cf. the 460e..i lineage, which an author correctly
                           adjudicated NOT granularity debt).
Detection is automatic; the response is a human governance decision at
Step 6a-v-quater (route to `/claim-synthesis` for proposal-first decomposition).
Absent a claim-tagged corpus every count is 0, so a missing / untagged corpus can
never mass-surface (same non-falsifying-safe posture as GOV-CEIL-1 / GOV-DIAG-1).

This audit READS ONLY and PROMOTES / DEMOTES NOTHING. It does not touch
claims.yaml.

Usage:
  python3 scripts/check_granularity_debt_recurrence.py            # human report, exit 0
  python3 scripts/check_granularity_debt_recurrence.py --strict   # exit 1 if any P0/P1
  python3 scripts/check_granularity_debt_recurrence.py --json     # machine-readable
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_AUTOPSY_DIR = REPO_ROOT / "evidence" / "planning"

# Shared with the reactive at-write-time reader so the two never drift on how a
# free-text `claim_alignment` is bucketed. Path insertion keeps this working when
# the module is imported from outside scripts/ (governance / morning-digest).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from granularity_debt_cluster import (  # noqa: E402
    _AMBIGUOUS_BUCKETS as _AMBIGUOUS_ALIGNMENT,
    bucket_alignment,
)
DEFAULT_CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"

# GOV-GRAN-1 (granularity-debt recurrence rule). N distinct confirmed no-verdict
# non-ceiling claim-keyed autopsy targets on ONE claim is the threshold -- it
# matches the /failure-autopsy skill's own "second-or-later autopsy circling the
# same claim" trigger (one autopsy is a diagnosis; the second is a pattern). Lower
# than GOV-CEIL-1 / GOV-DIAG-1's N=3 BECAUSE the differentiator here is not the
# raw count but the STRUCTURAL DIFFERENCE between the signatures -- two
# structurally-different no-verdict failures already imply >= 2 bundled mechanisms.
GRAN_RECURRENCE_N = 2

# A no-verdict direction: the autopsy contributed no evidence to the claim (so no
# clean falsification). A weakens / refutes / supports means a verdict WAS reached.
NO_VERDICT_DIRECTIONS = {"non_contributory", "inconclusive"}

# GOV-GRAN-1 human-adjudication marker. The audit's response to a P1 is explicitly
# a HUMAN decision (Step 6a-v-quater): coarse-claim (-> /claim-synthesis) vs
# coherent substrate campaign (-> metabolize + route to substrate). The existing
# metabolized-exclusion markers only capture two of the three possible outcomes:
# "split it" (decomposition_note / claim_synthesis doc) and "it's a substrate/
# same-wall story" (epistemic_category in _EPI_SUPPRESS_PROPOSAL). There was NO
# way to record the third, common outcome -- "a human ran the discrimination and
# decided NOT granularity debt, and no substrate-relane is honest" -- so those
# claims re-surfaced every cycle even after adjudication (e.g. a coherent-iteration
# campaign whose substrate demonstrably works, or a passenger co-claim that was
# never the failing subject). This enum is that record. A claim carrying
# `granularity_debt_disposition` in this set has been adjudicated (b) by a human;
# it is NOT re-surfaced. It PROMOTES/DEMOTES NOTHING and does NOT touch
# epistemic_category (so it never seeds a false GOV-CEIL-1 demotion count) -- it
# only silences THIS scan for the reason the docstring already sanctions. Pair it
# with a `granularity_debt_recurrence_note` recording the verdict + reasoning
# (the human-readable audit trail; this enum is the machine-readable key).
_GD_ADJUDICATED_NOT_DEBT = {
    "coherent_campaign",   # >1 no-verdict signature = progressive localization of ONE gap, not bundled mechanisms
    "passenger_co_claim",  # the claim was never the failing subject; hits belong to a co-tagged sibling's substrate
}

# Mirror scripts/generate_inter_governance_workset.py:_EPI_SUPPRESS_PROPOSAL. A
# hit whose epistemic_category is one of these is the substrate-enrichment / SAME
# -wall story (GOV-CEIL-1 owns it) -- excluded here to avoid double-count, exactly
# as GOV-DIAG-1 excludes claim-tagged targets. Kept in sync with that set.
_EPI_SUPPRESS_PROPOSAL = {
    "substrate_coherence", "substrate_ceiling", "substrate_conditional",
    "derivational", "out_of_domain", "governance_rule",
}
_CLAIM_DEAD_STATUSES = {"resolved", "superseded", "deprecated"}

# claim-id token, e.g. INV-064, MECH-445, ARC-065, SD-034, Q-080, EVB-0339.
_CLAIM_ID_RE = re.compile(r"\b([A-Z]{2,4}-\d{2,4}[a-z]?)\b")


def _norm_dir(value) -> str:
    return str(value or "").strip().lower()


def _trigger_claims(tgt: dict) -> set[str]:
    """Return the set of claim_ids this target's /claim-synthesis trigger is ABOUT.

    An autopsy target can carry several claim_ids (a run tagged with a cluster of
    claims), but its granularity trigger is about ONE recurrence subject. Bare
    target-level `routing == "claim-synthesis"` does NOT say WHICH claim, so on a
    multi-claim target it must not fan the trigger out to every incidental claim
    (the SD-034 460g case: claim_ids [SD-034, MECH-260, MECH-261], trigger about
    SD-034 -> attributing P0 to MECH-260/261 is a false positive). Attribution
    rule: a claim gets the trigger iff it is the SOLE claim_id, OR it is named in
    the trigger/brake/recommendation block itself.
    """
    claim_ids = [str(c).strip() for c in (tgt.get("claim_ids") or []) if str(c).strip()]
    triggered = False
    gdt = tgt.get("granularity_debt_trigger")
    if isinstance(gdt, dict) and gdt.get("fires") is True:
        triggered = True
    if _norm_dir(tgt.get("routing")) == "claim-synthesis":
        triggered = True
    rdb = tgt.get("re_derive_brake")
    if isinstance(rdb, dict) and _norm_dir(rdb.get("route_to")) == "claim-synthesis":
        triggered = True
    if tgt.get("claim_synthesis_recommended"):
        triggered = True
    if not triggered:
        return set()
    if len(claim_ids) == 1:
        return set(claim_ids)
    # multi-claim target: attribute only to claims NAMED in the trigger fields.
    blob = json.dumps({
        "gdt": gdt, "rdb": rdb,
        "rec": tgt.get("claim_synthesis_recommended"),
    })
    named = set(_CLAIM_ID_RE.findall(blob))
    return {c for c in claim_ids if c in named}


def _alignment_bucket(tgt: dict) -> str:
    """Bucket this target's own `four_layer_diagnosis.claim_alignment`.

    THE COUNT ALONE IS A WEAK SIGNAL. A cluster in which NO target reads
    `weakened` is measurement or implementation debt, not granularity debt,
    however many autopsies exist -- that classification, not the raw count, is
    what decided all three claims examined in the 2026-07-22 `/claim-synthesis`
    pass (MECH-204 even had a target reading `strengthened`). Reporting the
    distribution beside the count makes the audit self-checking rather than
    purely count-driven. Shares its bucketing with
    `scripts/granularity_debt_cluster.py` (the reactive at-write-time reader).
    """
    fld = tgt.get("four_layer_diagnosis")
    return bucket_alignment(fld.get("claim_alignment") if isinstance(fld, dict) else None)


def _fmt_alignment(dist: dict[str, int]) -> str:
    return ", ".join(f"{k}={v}" for k, v in
                     sorted(dist.items(), key=lambda kv: (-kv[1], kv[0]))) or "none"


def _alignment_note(rec: dict) -> str:
    """Inline reading of a record's claim_alignment distribution.

    Asserts the "not granularity debt" clear ONLY when every hit is bucketed to a
    known reading. `other`/`unstamped` hits mean the reading is unknown, not
    known-not-weakened (the free-text tail can bury a weakened reading in prose),
    so those are sent back to the human rather than silently cleared -- failing in
    the safe direction, the same posture as the rest of this audit.
    """
    if rec.get("any_weakened"):
        return ""
    n_amb = sum(v for k, v in (rec.get("alignment") or {}).items()
                if k in _AMBIGUOUS_ALIGNMENT)
    if n_amb:
        return (f"  <- no `weakened`, but {n_amb} free-text/unstamped alignment(s):"
                " read them before concluding")
    return ("  <- NO target reads `weakened`: measurement/implementation"
            " debt, not granularity debt")


def _signature(tgt: dict) -> str:
    """Coarse structural signature of a failure, for the distinct-signature count.

    (epistemic_category, failed_criterion). NOT a fine classifier -- when it reads
    the SAME on every autopsy for a claim the reading is 'may be one wall (check
    GOV-CEIL-1), or a difference this coarse key cannot see'; the human resolves
    it. The explicit-trigger tier does not depend on this (an author who fired the
    trigger already asserted the signatures differ).
    """
    epi = str(tgt.get("recommended_epistemic_category") or "").strip().lower()
    crit = str(tgt.get("failed_criterion") or "").strip().lower()
    return f"{epi}|{crit}"


def _load_claim_meta(claims_yaml: Path) -> dict[str, dict]:
    """Return {claim_id: {epistemic_category, status, has_decomposition_note}}.

    Full safe_load (as generate_pending_review.py does) -- correctness over the
    first-occurrence field scan; the registry is large but this runs once.
    """
    try:
        import yaml  # noqa: PLC0415
    except ImportError:
        return {}
    try:
        with open(claims_yaml, encoding="utf-8") as f:
            claims = yaml.safe_load(f) or []
    except (OSError, ValueError):
        return {}
    meta: dict[str, dict] = {}
    for c in claims:
        if not isinstance(c, dict):
            continue
        cid = c.get("id")
        if not cid:
            continue
        meta[str(cid)] = {
            "epistemic_category": str(c.get("epistemic_category") or "").strip().lower(),
            "status": str(c.get("status") or "").strip().lower(),
            "has_decomposition_note": bool(c.get("decomposition_note")),
            "gd_disposition": str(c.get("granularity_debt_disposition") or "").strip().lower(),
        }
    return meta


def _synthesized_claims(autopsy_dir: Path) -> set[str]:
    """Claim ids already considered in a claim_synthesis_<...>.md proposal doc.

    Scans every claim-id token in each proposal's FILENAME *and CONTENT*. A
    decomposition proposal names its umbrella, its children, and the cluster's
    context claims -- all of which have been reasoned about, so re-surfacing them
    is noise (the SD-034 doc names MECH-260/261 as cluster context; INV-064's doc
    names INV-064/088/089). Deliberate low-noise bias: a claim merely name-dropped
    in a `depends_on` list inside some proposal is treated as considered. This can
    hide a genuinely-fresh recurrence on a name-dropped claim; that trade is
    accepted for a quiet standing scan (the reactive autopsy trigger remains the
    first line, and a real fresh cluster will also fire the P0 explicit-trigger
    path, which is protected by _trigger_claims naming, not by this set).
    """
    out: set[str] = set()
    for fp in autopsy_dir.glob("claim_synthesis_*.md"):
        try:
            text = fp.read_text(encoding="utf-8")
        except OSError:
            text = fp.stem
        out.update(_CLAIM_ID_RE.findall(fp.stem + "\n" + text))
    return out


def count_recurrence_hits(autopsy_dir: Path,
                          absorbing_claims: set[str] | None = None) -> dict[str, dict]:
    """Count no-verdict non-ceiling claim-keyed autopsy hits per claim_id.

    Returns {claim_id: {"n_hits", "n_own_hits", "hits": [(stem, run_id)],
    "signatures": set, "explicit_trigger": bool, "trigger_artifacts": [stem]}}.
    See module docstring for the (i)/(ii)/(iii) hit definition.

    `absorbing_claims` is the set of already-synthesized-or-decomposed umbrella
    claims. A hit whose target co-tags an absorbing sibling (other than the claim
    itself) is counted in `hits` (for display) but NOT in `n_own_hits`: the
    target's recurrence subject is that metabolized umbrella, so it must not
    inflate a co-tagged bystander's own recurrence count. `n_own_hits` is the
    figure the audit qualifies P1 on; `n_hits` stays the full transparency count.
    """
    absorbing_claims = absorbing_claims or set()
    per_claim: dict[str, dict] = {}
    if not autopsy_dir.is_dir():
        return {}
    for fp in sorted(autopsy_dir.glob("failure_autopsy_*.json")):
        try:
            data = json.loads(fp.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        if str(data.get("status", "")).strip().lower() != "confirmed":
            continue
        for tgt in (data.get("targets") or []):
            claim_ids = tgt.get("claim_ids")
            # (i) CLAIM-keyed -- non-empty list only. Missing/empty -> GOV-DIAG-1.
            if not isinstance(claim_ids, list) or not claim_ids:
                continue
            # (ii) no clean verdict.
            if _norm_dir(tgt.get("recommended_evidence_direction")) not in NO_VERDICT_DIRECTIONS:
                continue
            # (iii) non-ceiling epistemic category (else GOV-CEIL-1 owns it).
            epi = str(tgt.get("recommended_epistemic_category") or "").strip().lower()
            if epi in _EPI_SUPPRESS_PROPOSAL:
                continue
            run_key = str(tgt.get("run_id") or tgt.get("queue_id") or fp.stem)
            trig_claims = _trigger_claims(tgt)
            sig = _signature(tgt)
            tgt_claim_set = {str(c).strip() for c in claim_ids if str(c).strip()}
            for cid in claim_ids:
                cid = str(cid).strip()
                if not cid:
                    continue
                # Absorbed iff SOME OTHER co-tagged claim on this target is an
                # already-metabolized umbrella (the recurrence is about it).
                absorbed = bool((tgt_claim_set & absorbing_claims) - {cid})
                rec = per_claim.setdefault(cid, {
                    "hits": set(), "own_hits": set(), "signatures": set(),
                    "explicit_trigger": False, "trigger_artifacts": set(),
                    "alignment": {},
                })
                if (fp.stem, run_key) not in rec["hits"]:
                    bucket = _alignment_bucket(tgt)
                    rec["alignment"][bucket] = rec["alignment"].get(bucket, 0) + 1
                rec["hits"].add((fp.stem, run_key))
                if not absorbed:
                    rec["own_hits"].add((fp.stem, run_key))
                rec["signatures"].add(sig)
                if cid in trig_claims:
                    rec["explicit_trigger"] = True
                    rec["trigger_artifacts"].add(fp.stem)
    return {
        cid: {
            "n_hits": len(rec["hits"]),
            "n_own_hits": len(rec["own_hits"]),
            "hits": sorted(rec["hits"]),
            "n_signatures": len(rec["signatures"]),
            "explicit_trigger": rec["explicit_trigger"],
            "trigger_artifacts": sorted(rec["trigger_artifacts"]),
            "alignment": dict(sorted(rec["alignment"].items(),
                                     key=lambda kv: (-kv[1], kv[0]))),
            "any_weakened": rec["alignment"].get("weakened", 0) > 0,
        }
        for cid, rec in per_claim.items()
    }


def audit(recurrence_hits: dict[str, dict], claim_meta: dict[str, dict],
          synthesized: set[str], n: int = GRAN_RECURRENCE_N) -> dict[str, list]:
    """Partition flagged claims into P0 (dropped_handoff), P1 (unflagged), excluded.

    A claim qualifies for surfacing when n_hits >= n OR an explicit trigger fired
    (a single explicit trigger with a dropped handoff is actionable even at 1 hit).
    Metabolized claims are moved to `excluded` with a reason.
    """
    p0, p1, excluded = [], [], []
    for cid, rec in recurrence_hits.items():
        qualifies = rec["n_hits"] >= n or rec["explicit_trigger"]
        if not qualifies:
            continue
        meta = claim_meta.get(cid, {})
        already_synth = cid in synthesized
        reason = None
        if meta.get("gd_disposition") in _GD_ADJUDICATED_NOT_DEBT:
            reason = f"granularity_debt_disposition={meta['gd_disposition']} (human-adjudicated NOT granularity debt)"
        elif meta.get("epistemic_category") in _EPI_SUPPRESS_PROPOSAL:
            reason = f"epistemic_category={meta['epistemic_category']} (substrate/enrichment; GOV-CEIL-1 lane)"
        elif meta.get("status") in _CLAIM_DEAD_STATUSES:
            reason = f"claim status={meta['status']} (dead)"
        elif meta.get("has_decomposition_note"):
            reason = "already decomposed (decomposition_note present)"
        elif already_synth:
            reason = "already synthesized (claim_synthesis_*.md exists)"
        elif rec["n_own_hits"] < n and not rec["explicit_trigger"]:
            # Co-tagged bystander: every hit shares a target with an
            # already-synthesized/decomposed umbrella (the recurrence subject);
            # no independent recurrence of its own. Mirrors _trigger_claims'
            # multi-claim narrowing on the P0 path.
            reason = ("co-tagged bystander (all hits share an already-synthesized/"
                      "decomposed sibling umbrella; recurrence subject is metabolized)")
        record = {
            "claim_id": cid,
            "n_hits": rec["n_hits"],
            "n_own_hits": rec["n_own_hits"],
            "n_signatures": rec["n_signatures"],
            "chain": [run for (_stem, run) in rec["hits"]],
            "artifacts": [stem for (stem, _run) in rec["hits"]],
            "explicit_trigger": rec["explicit_trigger"],
            "trigger_artifacts": rec["trigger_artifacts"],
            "alignment": rec["alignment"],
            "any_weakened": rec["any_weakened"],
        }
        if reason:
            excluded.append({**record, "excluded_reason": reason})
            continue
        # Not metabolized. P0 = an explicit trigger whose handoff was dropped
        # (no proposal doc). P1 = unflagged recurrence.
        if rec["explicit_trigger"] and not already_synth:
            p0.append({**record, "tier": "dropped_handoff"})
        else:
            p1.append({**record, "tier": "unflagged_recurrence"})
    p0.sort(key=lambda r: (-r["n_hits"], -r["n_signatures"], r["claim_id"]))
    p1.sort(key=lambda r: (-r["n_signatures"], -r["n_hits"], r["claim_id"]))
    return {"dropped_handoff": p0, "unflagged_recurrence": p1, "excluded": excluded}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--autopsy-dir", type=Path, default=DEFAULT_AUTOPSY_DIR,
                    help="dir of failure_autopsy_*.json + claim_synthesis_*.md")
    ap.add_argument("--claims-yaml", type=Path, default=DEFAULT_CLAIMS_YAML,
                    help="claims.yaml for the metabolized-exclusion signals")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any P0/P1 granularity-debt recurrence is flagged")
    args = ap.parse_args()

    claim_meta = _load_claim_meta(args.claims_yaml)
    synthesized = _synthesized_claims(args.autopsy_dir)
    # Absorbing umbrellas = already SPLIT (synthesized OR decomposition_note). A
    # co-tagged hit on such an umbrella's target is the umbrella's recurrence, not
    # a bystander sibling's -- see count_recurrence_hits `absorbing_claims`.
    absorbing_claims = set(synthesized) | {
        cid for cid, m in claim_meta.items() if m.get("has_decomposition_note")
    }
    recurrence_hits = count_recurrence_hits(args.autopsy_dir, absorbing_claims)
    result = audit(recurrence_hits, claim_meta, synthesized, n=GRAN_RECURRENCE_N)
    p0, p1, excluded = (result["dropped_handoff"],
                        result["unflagged_recurrence"], result["excluded"])

    if args.json:
        print(json.dumps({
            "gran_recurrence_n": GRAN_RECURRENCE_N,
            "n_claims_with_hits": len(recurrence_hits),
            "dropped_handoff": p0,
            "unflagged_recurrence": p1,
            "excluded_metabolized": excluded,
        }, indent=2))
    else:
        print("Granularity-debt recurrence audit (GOV-GRAN-1): "
              f"{len(recurrence_hits)} claim(s) carry no-verdict non-ceiling "
              "claim-keyed autopsies")
        print(f"  P0 dropped-handoff (trigger fired, NO proposal doc): {len(p0)}")
        print(f"  P1 unflagged recurrence (>= {GRAN_RECURRENCE_N} hits, not metabolized): {len(p1)}")
        print(f"  excluded (already metabolized): {len(excluded)}")
        if p0:
            print("  -- P0 DROPPED HANDOFF: an autopsy routed to /claim-synthesis but no")
            print("     claim_synthesis_<claim>_*.md exists. Run /claim-synthesis on:")
            for r in p0:
                print(f"    [P0] {r['claim_id']} -- {r['n_hits']} hit(s), "
                      f"{r['n_signatures']} distinct signature(s); "
                      f"trigger in {', '.join(r['trigger_artifacts'])}")
                print(f"        chain: {' -> '.join(r['chain'])}")
                print(f"        claim_alignment: {_fmt_alignment(r['alignment'])}"
                      + _alignment_note(r))
        if p1:
            print("  -- P1 UNFLAGGED RECURRENCE: claim circled by structurally-different")
            print("     no-verdict failures no author flagged. Discriminate coarse-claim")
            print("     (=> /claim-synthesis) vs coherent substrate-build campaign:")
            for r in p1:
                print(f"    [P1] {r['claim_id']} -- {r['n_hits']} hits, "
                      f"{r['n_signatures']} distinct signature(s)")
                print(f"        chain: {' -> '.join(r['chain'])}")
                print(f"        claim_alignment: {_fmt_alignment(r['alignment'])}"
                      + _alignment_note(r))
        if not p0 and not p1:
            print("  -- no actionable granularity-debt recurrence (healthy: the reactive"
                  " autopsy trigger caught everything, or nothing is circling).")

    if args.strict and (p0 or p1):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
