#!/usr/bin/env python3
"""
Validate docs/claims/claims.yaml schema.

Currently enforces the invariant-type schema introduced 2026-04-17:
  - invariant_type is mandatory on every claim_type: invariant entry
  - invariant_type must be one of: universal | emergent | grey_zone
  - emergent_from must be non-empty when invariant_type == emergent
  - emergent_from must be empty or absent when invariant_type == universal
  - emergent_from must be a subset of depends_on
  - grey_zone entries pass regardless of emergent_from content

Duplicate-key gate (ERROR-level, added 2026-07-18):
  - a mapping key repeated within the same block (at any nesting depth) is an
    ERROR. PyYAML is last-wins, so every earlier occurrence is silently
    discarded before any consumer -- including the rest of this validator --
    can see it. See load_claims() for why this check cannot live in the
    parsed-dict checks below.

Flag-drift warnings (WARN-level, no exit effect):
  - pending_substrate_reconfirmation: true but all substrates in emergent_from
    are active -> flag is stale, can be cleared.
  - pending_substrate_reconfirmation: false/absent but at least one substrate
    in emergent_from is below active -> invariant should be flagged.
  The flag is a governance artifact, not an auto-derived value. Warnings
  surface drift between flag state and substrate status; governance decides.

Modes:
  --warn             (default) print issues, exit 0
  --strict           print issues, exit 1 if any ERROR (Session D default in governance.sh)
  --audit            print classification counts only (no validation)
  --duplicates-only  run ONLY the duplicate-key gate; exit 1 if any duplicate.
                     Deliberately narrow: this is the mode the PreToolUse
                     git-commit guard blocks on. A duplicate key is definite
                     silent data loss with one unambiguous remedy, so it is
                     worth blocking a commit over; the other ERROR rules are
                     schema/governance findings whose remedy may legitimately
                     be "decide during governance", and coupling them to the
                     commit path would let an unrelated pre-existing ERROR
                     wedge an unrelated commit. --strict remains the full
                     gate for governance.sh.

Called at the top of build_claims_json.py and governance.sh, and (as
--duplicates-only) from the PreToolUse commit guard in .claude/settings.json.
See docs/architecture/invariant_types.md for schema semantics.
"""
import argparse
import datetime
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent
CLAIMS_YAML = REPO_ROOT / "docs" / "claims" / "claims.yaml"

VALID_INVARIANT_TYPES = {"universal", "emergent", "grey_zone"}

# Phase 3 wave 2: epistemic_category schema (warn-only).
# When set, must be one of these values. When unset, the indexer infers
# from claim_type + invariant_type via the Phase 2 mapping.
VALID_EPISTEMIC_CATEGORIES = {
    "standard",
    "substrate_coherence",
    "answer_state",
    "substrate_ceiling",
    "substrate_conditional",
    "derivational",
    "out_of_domain",
    "governance_rule",
}

SUBSTRATE_CLAIM_TYPES = {
    "design_decision",
    "architectural_commitment",
    "architecture_hypothesis",
}

# Substrate-ceiling decision marker (warn-only). A `substrate_ceiling` claim may
# carry `ceiling_decision` to tell the governance Step 6a-v audit
# (scripts/check_substrate_ceiling_audit.py) how the ceiling was routed:
#   `deferred`  -- the build-decision is deliberately parked (the ceiling is NOT
#                  an orphan awaiting a substrate-design owner).
#   `exhausted` -- the ceiling-exhaustion demotion rule (GOV-CEIL-1) fired: N>=3
#                  ceiling hits with no positive discrimination on any richer
#                  substrate; the claim is demoted to a ceiling-exhausted
#                  contested candidate (epistemic_category -> standard, status
#                  floored to candidate, null reading carried co-equally). The
#                  marker is a historical stamp; the demoted claim leaves the
#                  substrate_ceiling set, so the audit no longer processes it.
# When set it must be a known value AND carry a `ceiling_routing_note`
# (reason + date).
VALID_CEILING_DECISIONS = {"deferred", "exhausted"}

# Statuses that count as terminal-positive for the flag-drift check.
# 'implemented' is included per 2026-04-17 governance decision: SD-005 and other
# 'implemented' substrates are wired into the codebase and should not trigger
# pending_substrate_reconfirmation drift warnings. If governance later wants
# 'resolved' / 'validated' / 'stable' treated the same way, extend this set.
ACTIVE_EQUIVALENT_STATUSES = {"active", "implemented"}


def build_substrate_status_map(claims):
    """Return {substrate_id: status} for all substrate claims."""
    status_map = {}
    for c in claims:
        if not isinstance(c, dict):
            continue
        if c.get("claim_type") in SUBSTRATE_CLAIM_TYPES:
            sid = c.get("id")
            if sid:
                status_map[sid] = c.get("status", "unknown")
    return status_map


class DuplicateKeyLoader(yaml.SafeLoader):
    """SafeLoader that RECORDS duplicated mapping keys instead of dropping them.

    PyYAML resolves a repeated key last-wins: the earlier occurrence's content
    is discarded during construction, so by the time any consumer sees the
    parsed dict the defect is already invisible. That is why the duplicate
    check cannot be a parsed-dict check like every other rule in this file --
    it has to run inside the loader, on the node tree, where both occurrences
    still exist.

    Collects rather than raises so ONE run reports EVERY duplicate. The
    2026-07-18 cleanup (b8492a7180) recovered 26 duplicated keys across 25
    claims; a raising loader would have surfaced them one commit at a time.

    Findings land on `self.duplicate_keys` as (key, [line, line, ...]),
    1-indexed, in file order.
    """

    def __init__(self, stream):
        super().__init__(stream)
        self.duplicate_keys = []

    def construct_mapping(self, node, deep=False):
        lines_by_key = {}
        for key_node, _value_node in node.value:
            # Scalar keys only. A non-scalar key is not something this registry
            # uses, and reading key_node.value directly (rather than
            # construct_object) avoids constructing the key twice.
            if not isinstance(key_node, yaml.ScalarNode):
                continue
            lines_by_key.setdefault(key_node.value, []).append(
                key_node.start_mark.line + 1)
        for key, lines in lines_by_key.items():
            if len(lines) > 1:
                self.duplicate_keys.append((key, lines))
        return super().construct_mapping(node, deep=deep)


def _claim_id_at_line(claim_starts, line):
    """Return the id of the claim whose block contains `line`.

    claim_starts is an ascending list of (line, claim_id) for each `- id:`
    top-level entry. Returns '<unknown>' for a line above the first claim.
    """
    found = "<unknown>"
    for start_line, cid in claim_starts:
        if start_line > line:
            break
        found = cid
    return found


def _scan_claim_starts(text):
    starts = []
    for i, raw in enumerate(text.split("\n"), 1):
        if raw.startswith("- id:"):
            starts.append((i, raw[len("- id:"):].strip()))
    return starts


def load_claims():
    """Parse claims.yaml. Returns (claims, duplicate_key_issues)."""
    if not CLAIMS_YAML.exists():
        print(f"ERROR: {CLAIMS_YAML} not found", file=sys.stderr)
        sys.exit(2)
    text = CLAIMS_YAML.read_text(encoding="utf-8")

    loader = DuplicateKeyLoader(text)
    try:
        claims = loader.get_single_data()
        duplicates = loader.duplicate_keys
    finally:
        loader.dispose()

    if not isinstance(claims, list):
        print("ERROR: claims.yaml top level must be a list", file=sys.stderr)
        sys.exit(2)

    claim_starts = _scan_claim_starts(text)
    issues = []
    for key, lines in sorted(duplicates, key=lambda kv: kv[1][0]):
        cid = _claim_id_at_line(claim_starts, lines[0])
        kept = lines[-1]
        dropped = ", ".join(str(n) for n in lines[:-1])
        issues.append((
            "ERROR",
            f"{cid}: duplicate key '{key}' at lines {dropped}, {kept} -- YAML is "
            f"last-wins, so line {kept} SILENTLY DISCARDS the content at line(s) "
            f"{dropped}; no consumer (this validator, build_claims_json.py, "
            f"serve.py, every governance audit) can see it. MERGE the blocks "
            f"into one key -- do not just delete the earlier one."))
    return claims, issues


def validate_invariant(claim, substrate_status=None):
    """Return list of (level, msg) tuples for issues on one invariant.

    substrate_status: optional mapping {substrate_id: status} used for
    flag-drift warnings on `pending_substrate_reconfirmation`. If None,
    flag-drift checks are skipped.
    """
    issues = []
    cid = claim.get("id", "<no-id>")
    itype = claim.get("invariant_type")
    efrom = claim.get("emergent_from") or []
    depends_on = claim.get("depends_on") or []

    if itype is None:
        issues.append(("ERROR", f"{cid}: missing invariant_type (universal | emergent | grey_zone)"))
        return issues

    if itype not in VALID_INVARIANT_TYPES:
        issues.append(("ERROR", f"{cid}: invariant_type='{itype}' invalid; must be one of {sorted(VALID_INVARIANT_TYPES)}"))
        return issues

    if itype == "emergent":
        if not efrom:
            issues.append(("ERROR", f"{cid}: invariant_type=emergent requires non-empty emergent_from"))
        else:
            missing = [s for s in efrom if s not in depends_on]
            if missing:
                issues.append(("ERROR", f"{cid}: emergent_from {missing} not in depends_on"))
    elif itype == "universal":
        if efrom:
            issues.append(("ERROR", f"{cid}: invariant_type=universal must have empty/absent emergent_from (found {efrom})"))
    # grey_zone: permissive, no constraint on emergent_from / candidate_emergent_from

    # Flag-drift warnings: pending_substrate_reconfirmation vs substrate status.
    # Warnings only -- the flag is a governance artifact, not auto-derived.
    if substrate_status is not None and itype == "emergent" and efrom:
        flag_set = bool(claim.get("pending_substrate_reconfirmation"))
        substrate_statuses = [
            (s, substrate_status.get(s)) for s in efrom
        ]
        below_active = [
            (s, st) for s, st in substrate_statuses
            if st is not None and st not in ACTIVE_EQUIVALENT_STATUSES
        ]
        all_known_active = (
            substrate_statuses
            and all(st in ACTIVE_EQUIVALENT_STATUSES for _, st in substrate_statuses)
        )
        if flag_set and all_known_active:
            issues.append((
                "WARN",
                f"{cid}: flag is stale -- all substrates now active, "
                f"pending_substrate_reconfirmation can be cleared.",
            ))
        elif (not flag_set) and below_active:
            s, st = below_active[0]
            issues.append((
                "WARN",
                f"{cid}: should be flagged -- substrate {s} is {st}.",
            ))

    return issues


def validate_terminal_dependencies(claims):
    """WARN on a LIVE claim whose depends_on names a terminal-status claim.

    Returns a list of (level, message) tuples, same shape as validate_invariant.
    Lifted out of main() so the two exclusions below are directly testable
    against synthetic fixtures rather than only against the live registry --
    a test keyed on the live corpus would break the moment the backlog it
    reports is actually fixed.
    """
    issues = []
    # ---- superseded / retired depends_on target (WARN-only, added 2026-09-01) ----
    # A LIVE claim carrying a depends_on edge to a claim that has since gone
    # terminal. Nothing else in the pipeline notices: the indexer reads
    # depends_on for the MRF graph and gating without checking the target's own
    # status, so the edge silently keeps asserting a dependency on a claim the
    # registry has retired. Motivating measurement (GFLAG-0064, 2026-09-01): SD-003
    # went `superseded` on 2026-04-18 with successors [MECH-256, SD-029], and
    # SIXTEEN claims still depended on it four months later. The flag that found it
    # named only three of the sixteen -- which is the point: nobody was counting,
    # because nothing was checking.
    #
    # TWO EXCLUSIONS, and they are load-bearing rather than politeness. Measured on
    # the 2026-09-01 corpus, 32 edges point at a terminal target but only 26 are
    # defects; without these the check would false-positive on 6 of 32 (19%), and a
    # lint that fires on correct work gets switched off:
    #   (a) TERMINAL SOURCE. A retired/legacy claim depending on another retired or
    #       legacy claim is frozen history, correctly preserved -- e.g. the IMPL-020
    #       -> IMPL-021 -> IMPL-022 -> IMPL-024 chain, all legacy. Only a claim that
    #       is still live can hold a stale edge.
    #   (b) SUCCESSOR PROVENANCE. A claim listed in its target's own superseded_by
    #       depending on the claim it superseded is a provenance edge, not a stale
    #       one -- e.g. MECH-448 -> MECH-447, where MECH-447.superseded_by names
    #       MECH-448.
    #
    # WARN-ONLY on purpose (stabilise-then-elevate, the posture epistemic_category
    # and assembly_state both shipped under). There are 26 live violations today, so
    # an ERROR here would block governance.sh --strict for everyone on a backlog this
    # check exists to surface, not to gate. Elevate once the count reaches 0.
    #
    # NOT A MECHANICAL REPOINT -- but NOT for the reason first shipped. The original
    # wording of this comment said the obvious fix (point the edge at superseded_by) was
    # wrong because SD-013 -> SD-003 would create a cycle. CORRECTED 2026-09-01, same
    # day: that objection is largely void. This claims graph ALREADY CONTAINS 153 CYCLES
    # over 3915 depends_on edges, including a DIRECT 2-hop one (ARC-007 <-> ARC-018), and
    # the indexer's loopy belief propagation converges over it (converged=True, 21 iters).
    # It is a conceptual dependency web, not a build DAG, so "this would introduce a
    # cycle" is not a disqualifying argument here and should not be used as one.
    # Measured on the SD-003 fan-in: of its 16 dependants, repointing would close a cycle
    # for 7 -- but only ONE of those (SD-013) is direct; the other six are 9-12 hop paths
    # through a single long shared chain, i.e. indistinguishable from the 153 already
    # tolerated.
    # The real reason this stays WARN rather than becoming an auto-fix is SEMANTIC: whether
    # a given successor is actually what the dependant depends on is a per-claim judgement
    # the registry cannot infer. Hence a named successor list and a human.
    TERMINAL_CLAIM_STATUSES = {"superseded", "retired", "legacy", "rejected"}

    def _status_of(claim):
        return str(claim.get("status") or "").strip().lower()

    claims_by_id = {c.get("id"): c for c in claims if c.get("id")}
    for c in claims:
        cid = c.get("id", "<unknown>")
        if _status_of(c) in TERMINAL_CLAIM_STATUSES:
            continue  # exclusion (a): frozen history
        deps = c.get("depends_on") or []
        if not isinstance(deps, list):
            continue
        for dep in deps:
            target = claims_by_id.get(dep)
            if target is None:
                continue  # dangling ids are a different class; 0 in the corpus today
            tstatus = _status_of(target)
            if tstatus not in TERMINAL_CLAIM_STATUSES:
                continue
            succ = target.get("superseded_by") or []
            if isinstance(succ, str):
                succ = [succ]
            if cid in succ:
                continue  # exclusion (b): successor provenance
            hint = (f" -- successors are {', '.join(succ)}; repoint or DROP the edge. "
                    "Judge this SEMANTICALLY (is the successor actually what this claim "
                    "depends on?), not structurally: a successor already depending on this "
                    "claim does NOT disqualify a repoint, because this graph is not acyclic "
                    "and is not meant to be -- 153 cycles already exist in it, including a "
                    "direct 2-hop one, and the indexer's loopy BP converges over them"
                    if succ else
                    " -- no superseded_by recorded on the target, so decide whether to "
                    "drop the edge or name a successor")
            issues.append((
                "WARN",
                f"{cid} depends_on {dep}, which is status: {tstatus}{hint}"))
    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="exit 1 on any ERROR")
    ap.add_argument("--audit", action="store_true", help="print classification counts only")
    ap.add_argument(
        "--duplicates-only",
        action="store_true",
        help="run ONLY the duplicate-key gate; exit 1 if any duplicate (commit-guard mode)",
    )
    args = ap.parse_args()

    claims, duplicate_issues = load_claims()
    invariants = [c for c in claims if c.get("claim_type") == "invariant"]

    # Commit-guard mode. Returns BEFORE the schema/governance checks so that a
    # pre-existing unrelated ERROR elsewhere in the registry can never block a
    # commit that has nothing to do with it.
    if args.duplicates_only:
        dupes = [msg for lvl, msg in duplicate_issues if lvl == "ERROR"]
        if not dupes:
            return 0
        print(f"validate_claims [duplicates-only]: {len(dupes)} duplicate key(s) in claims.yaml")
        for msg in dupes:
            print(f"  ERROR: {msg}")
        return 1

    if args.audit:
        counts = {"universal": 0, "emergent": 0, "grey_zone": 0, "unclassified": 0}
        for c in invariants:
            t = c.get("invariant_type")
            if t in counts:
                counts[t] += 1
            else:
                counts["unclassified"] += 1
        print(f"Total invariants: {len(invariants)}")
        for k, v in counts.items():
            print(f"  {k}: {v}")
        return 0

    substrate_status = build_substrate_status_map(claims)
    # Duplicate keys first: every other check below reads the already-parsed
    # dict, where the earlier occurrence is gone. Reported ahead of the rest
    # because a duplicated key can also mask or fake a schema issue further
    # down (the earlier occurrence's value never reaches the enum checks).
    all_issues = list(duplicate_issues)
    for c in invariants:
        all_issues.extend(validate_invariant(c, substrate_status=substrate_status))

    # Phase 3 wave 2: epistemic_category enum validation across all claims.
    # When the field is set, it must be one of the valid categories. The
    # indexer's _resolve_epistemic_category() SILENTLY falls back to inference
    # on an invalid explicit value -- exactly what an ERROR gate should stop.
    # ELEVATED to ERROR 2026-06-22 (stabilise-then-elevate window done -- the
    # registry has carried explicit epistemic_category values warn-clean since
    # 2026-05-02, gate confirmed at 0 invalid WARNs 2026-06-22T06:32Z): a typo'd
    # explicit epistemic_category now blocks governance.sh --strict instead of
    # masking the bad value behind the inference fallback. Mirrors the
    # assembly_state/assembly_status (df62e84575) and invariant-type ERROR
    # posture. epistemic_stance + ceiling_decision/ceiling_routing_note below
    # stay WARN-only -- they are not the subject of the stabilise-then-elevate
    # note.
    for c in claims:
        ec = c.get("epistemic_category")
        if ec is None:
            continue
        ec_norm = str(ec).strip().lower()
        if not ec_norm:
            continue
        if ec_norm not in VALID_EPISTEMIC_CATEGORIES:
            cid = c.get("id", "<unknown>")
            all_issues.append((
                "ERROR",
                f"{cid}: epistemic_category='{ec}' invalid; must be one of "
                f"{sorted(VALID_EPISTEMIC_CATEGORIES)} (an invalid explicit value "
                "would silently fall back to the indexer's inference -- fix the typo)"
            ))

    # Substrate-ceiling park marker (warn-only). `ceiling_decision`, when set,
    # must be a known value and must be paired with a `ceiling_routing_note`
    # (reason + date) so the Step 6a-v audit's "parked, not orphaned" exclusion
    # is auditable rather than silent. The audit script tolerates a bare marker
    # (treats any `ceiling_decision: deferred` as parked); these warns keep the
    # registry honest. See scripts/check_substrate_ceiling_audit.py.
    for c in claims:
        cd = c.get("ceiling_decision")
        if cd is None or not str(cd).strip():
            continue
        cid = c.get("id", "<unknown>")
        cd_norm = str(cd).strip().lower()
        if cd_norm not in VALID_CEILING_DECISIONS:
            all_issues.append((
                "WARN",
                f"{cid}: ceiling_decision='{cd}' invalid; must be one of "
                f"{sorted(VALID_CEILING_DECISIONS)} (audit treats any non-empty "
                "value as parked)"))
        if not str(c.get("ceiling_routing_note", "") or "").strip():
            all_issues.append((
                "WARN",
                f"{cid}: ceiling_decision set but no `ceiling_routing_note` "
                "-- record the park reason + date for the Step 6a-v audit trail"))

    # Epistemic-stance split (warn-only). An explicit `epistemic_stance` must be
    # one of shown|believed|asked (else build_claims_json falls back to the
    # derivation). And an ASKED-bucket claim -- an open-question/derivational/
    # out-of-domain claim, the question-not-assertion bucket -- should carry a
    # `what_would_answer` line: the falsification condition that distinguishes
    # genuinely-new epistemic ground from the merely not-yet-operationalised.
    # Warn-only; the most ambitious ungrounded claims are exactly the ones this
    # keeps honest. (Independent of exp_conf -- exp_conf separates shown from
    # believed, never asked, so the structural signals below define the bucket.)
    _STANCE_VALUES = {"shown", "believed", "asked"}
    _ASKED_CATEGORIES = {"answer_state", "derivational", "out_of_domain"}
    _ASKED_CLAIM_TYPES = {"open_question", "question"}
    # Terminal statuses: a question that has been answered, retired, or
    # superseded is no longer ASKED, so it should not be flagged for a missing
    # `what_would_answer` falsification condition (writing one for a closed
    # question is semantically backwards). `lifecycle_stage: adjudicated`
    # likewise marks a question that has been settled by an adjudication
    # decision. These claims keep their `open_question`/`question` claim_type
    # for history, so the bucket test below would otherwise fire on them.
    _TERMINAL_STATUSES = {
        "legacy", "resolved", "retired", "superseded", "candidate_resolved",
        "deprecated", "applied",
    }
    for c in claims:
        cid = c.get("id", "<unknown>")
        stance = str(c.get("epistemic_stance", "") or "").strip().lower()
        if stance and stance not in _STANCE_VALUES:
            all_issues.append((
                "WARN",
                f"{cid}: epistemic_stance='{c.get('epistemic_stance')}' invalid; "
                f"must be one of {sorted(_STANCE_VALUES)} (build_claims_json will "
                "fall back to the derivation)"))
        ct = str(c.get("claim_type", "") or "").strip()
        cat = str(c.get("epistemic_category", "") or "").strip().lower()
        status = str(c.get("status", "") or "").strip().lower()
        lifecycle = str(c.get("lifecycle_stage", "") or "").strip().lower()
        is_terminal = (status in _TERMINAL_STATUSES
                       or lifecycle == "adjudicated")
        is_asked = (not is_terminal
                    and (stance == "asked" or cat in _ASKED_CATEGORIES
                         or ct in _ASKED_CLAIM_TYPES))
        if is_asked and not str(c.get("what_would_answer", "") or "").strip():
            all_issues.append((
                "WARN",
                f"{cid}: asked-bucket claim (claim_type={ct or 'n/a'}, "
                f"epistemic_category={cat or 'n/a'}) has no `what_would_answer` "
                "-- state the observation that would answer/falsify it"))

    # Assembly-state companion fields (MOVE-4 claims-layer follow-on).
    # assembly_state consolidates the 6 substrate-blocked conventions into one
    # canonical field (derived in build_claims_json.resolve_assembly_state /
    # serve.py._resolve_claim_assembly_state); an explicit value overrides the
    # derivation, so an INVALID explicit value silently falls back to the
    # derivation. ELEVATED to ERROR 2026-06-22 (one-cycle backwards-compat
    # posture done -- governance cycle c2aeb4823f 2026-06-22T05:19Z ran with the
    # field present and exercised it at 0 assembly WARNs): a typo'd explicit
    # assembly_state / assembly_status now blocks governance.sh --strict instead
    # of silently masking the bad value behind the derivation. revisit_after
    # (date format) stays WARN -- a bad date is ignored by the revisit-due check,
    # not silently substituted. awaiting is a free-form upstream pointer (no enum,
    # no check).
    _ASSEMBLY_STATES = {
        "mature", "enriching", "awaiting_substrate", "gated_v3",
        "deferred_future", "remaining", "parked", "blocked",
    }
    _ASSEMBLY_STATUS_VALUES = {"queued", "in_progress", "built"}
    for c in claims:
        cid = c.get("id", "<unknown>")
        a_state = str(c.get("assembly_state", "") or "").strip().lower()
        if a_state and a_state not in _ASSEMBLY_STATES:
            all_issues.append((
                "ERROR",
                f"{cid}: assembly_state='{c.get('assembly_state')}' invalid; must "
                f"be one of {sorted(_ASSEMBLY_STATES)} (an invalid explicit value "
                "would silently fall back to the derivation -- fix the typo)"))
        a_status = str(c.get("assembly_status", "") or "").strip().lower()
        if a_status and a_status not in _ASSEMBLY_STATUS_VALUES:
            all_issues.append((
                "ERROR",
                f"{cid}: assembly_status='{c.get('assembly_status')}' invalid; must "
                f"be one of {sorted(_ASSEMBLY_STATUS_VALUES)} (an invalid explicit "
                "value would silently fall back to the substrate_queue auto-join -- "
                "fix the typo)"))
        rv = str(c.get("revisit_after", "") or "").strip()
        if rv:
            try:
                datetime.date.fromisoformat(rv)
            except ValueError:
                all_issues.append((
                    "WARN",
                    f"{cid}: revisit_after='{rv}' is not an ISO date (YYYY-MM-DD); "
                    "it will be ignored by the revisit-due check"))

    # diagnostic_evidence_adjudicated (fix shape 1, SD-099/MECH-489, 2026-08-26,
    # warn-only per the stabilise-then-elevate posture used above for
    # epistemic_category/assembly_state). Set explicitly by /failure-autopsy at the
    # point it confirms a diagnostic-purpose run's finding into a claim's
    # evidence_quality_note narrative; consumed by build_experiment_indexes.py to
    # suppress missing_experimental_evidence/lit_only_above_cap when exp_count == 0.
    # See evidence/planning/design_decision_evidence_credit_gap_20260821.md.
    for c in claims:
        cid = c.get("id", "<unknown>")
        if "diagnostic_evidence_adjudicated" not in c:
            continue
        val = c.get("diagnostic_evidence_adjudicated")
        if not isinstance(val, bool):
            all_issues.append((
                "WARN",
                f"{cid}: diagnostic_evidence_adjudicated={val!r} is not a plain "
                "true/false -- the indexer's hand-rolled parser only recognises "
                "true/yes/1 as true (case-insensitive) and treats anything else as "
                "false, so a non-boolean value here silently means false there"))
        elif val and not str(c.get("evidence_quality_note", "") or "").strip():
            all_issues.append((
                "WARN",
                f"{cid}: diagnostic_evidence_adjudicated=true but evidence_quality_note "
                "is empty -- the flag is meant to be set at the point a diagnostic run's "
                "finding is confirmed into the claim's narrative, not on its own"))

    all_issues.extend(validate_terminal_dependencies(claims))

    errors = [msg for lvl, msg in all_issues if lvl == "ERROR"]
    warnings = [msg for lvl, msg in all_issues if lvl == "WARN"]

    if not all_issues:
        print(f"validate_claims: OK ({len(invariants)} invariants checked)")
        return 0

    mode = "strict" if args.strict else "warn-only"
    print(f"validate_claims [{mode}]: {len(errors)} error(s), {len(warnings)} warning(s) across {len(invariants)} invariants")
    for msg in errors:
        print(f"  ERROR: {msg}")
    for msg in warnings:
        print(f"  WARN: {msg}")

    if args.strict and errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
