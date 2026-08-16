#!/usr/bin/env python3
"""D-007 -- stale gate reference: a closure node's gate text names a CLEARED gate.

THE FRAMING CONSTRAINT (user-signed-off 2026-08-16). READ THIS BEFORE ANYTHING
ELSE, INCLUDING BEFORE "IMPROVING" THE DETECTOR.

    D-007 is a DOCUMENTATION-ACCURACY detector, never an UNBLOCK-DETECTION one.

        It reports "the gate text is stale."
        It is FORBIDDEN from concluding "the node should be open."

A cleared gate is NOT an unblocked node. Every recorded instance in this repo
ended with the node correctly staying `blocked` on a RE-POINTED gate:

  2026-06-09  self_attribution:GAP-1/GAP-2 re-adjudication (REE_assembly
              43ba39ca9e). Two of GAP-1's three named prerequisites were already
              done -- sleep_substrate:GAP-1 PASS, and "MECH-307 conjunction
              architecture" = goal_pipeline:GAP-1 done. The third, MECH-269
              V_s monostrategy landing, had been satisfied 2026-05-17 (ARC-065
              SP-CEM became the main-path default, V3-EXQ-583) -- ONE DAY AFTER
              the gate was written -- and was insufficient anyway: 543l / 598b /
              614e show the candidate pool collapses at the z_world layer
              UPSTREAM of SP-CEM, so stratified sampling has nothing to
              stratify. Outcome: status stays BLOCKED, gate re-pointed.
  2026-06-23  behavioral_diversity_isolation:GAP-A went `done` on the V3-EXQ-569i
              PASS, and self_attribution:GAP-2's blocking_external names
              "behavioral_diversity_isolation:GAP-A/GAP-B". The 2026-06-20
              V3-EXQ-625e autopsy showed that conversion is ENV-CONDITIONAL and
              does not propagate to a threat-engaged candidate pool. That node
              record names the naive reading by name: "a naive 'GAP-A done ->
              unblock GAP-2' read is the same env-conditional trap the axis_b
              autopsy caught." Outcome: status stays BLOCKED.
  2026-07-29  self_attribution status-table reconcile (REE_assembly 7e60b8a675):
              sleep_substrate:GAP-1 and goal_pipeline:GAP-1 both `done`; the node
              stayed blocked on a re-pointed third gate.

A detector emitting "node should open" would have been WRONG ALL THREE TIMES.
The cost is not noise: the self_attribution plan states that re-queuing on a
falsely-cleared gate re-derives the known `non_contributory` result and burns a
runner session. Do not build that trap into a detector.

CONSEQUENCES OF THE FRAMING, all of them load-bearing:

1. PERMANENTLY T1. Never auto-fix. Re-pointing a gate IS the judgement, and it
   is the judgement three separate governance cycles had to make by hand.
   `TIER = "T1"` and `autofix=False` are asserted structurally below --
   `assert_no_status_proposal()` raises rather than trusting discipline, in the
   same spirit as _common.finding()'s autofix/tier guard.
2. SUPPRESSION KEYS ON (node, gate-set). A node adjudicated "still blocked, gate
   re-pointed" must not re-fire every run, but MUST re-fire when the gate set
   changes. Getting that wrong in either direction defeats the detector: too
   sticky and a genuine new stale gate is swallowed; too loose and every run
   re-escalates a settled adjudication. See _subject().
3. A PRECISION FLOOR APPLIES -- unlike D-002. D-002's misses are SILENT by
   construction (that is the defect it detects), so a floor there would withhold
   real findings forever. D-007's misses are NOT silent: stale plans already
   surface in the morning digest staleness table, so a miss is recoverable and
   trading recall for precision is legitimate. Below PRECISION_FLOOR the
   detector goes LIST-ONLY (escalate=False) -- it still reports every finding,
   it just stops waking a model. See PRECISION_FLOOR / MEASURED_PRECISION.
4. GATE REFERENCES ARE PROSE AS WELL AS STRUCTURED FIELDS. `blocking_external`
   is a list of gate declarations, so every plan:NODE token in it is a gate.
   `resume_condition` is free text that names gates inline AND cites unrelated
   nodes as evidence, so it is parsed CONSERVATIVELY -- a token counts only in a
   clause that reads as a gate and does not read as a citation. Prefer a miss
   over a false positive on prose. Skipped tokens are counted in the summary, so
   the miss is visible rather than silent.

SCOPE, stated because the neighbouring fields are tempting and out of bounds.
Only `blocking_external` and `resume_condition` are read. `depends_on`,
`blocked_by`, `cross_plan_link` and `readiness_gate` are NOT -- `depends_on` in
particular is the structured, map-rendered dependency edge, and "every
depends_on is done therefore the node should open" is exactly the inference this
detector is forbidden from making. Adding it would import the trap through the
back door.

READ ONLY. Never edits claims.yaml, a node status, plan frontmatter or the
queue. Nothing here proposes a status transition; that is enforced, not merely
intended.
"""

from __future__ import annotations

import re

from ._common import Context, finding

DETECTOR_ID = "D-007"
DETECTOR_TITLE = "Stale gate reference (gate text names a cleared gate)"
TIER = "T1"

# ---------------------------------------------------------------------------
# The precision floor (consequence 3 above)
# ---------------------------------------------------------------------------
# PRECISION_FLOOR is the SKILL.md figure: below it the detector is list-only
# until refined. MEASURED_PRECISION is what a HAND AUDIT of the live findings
# returned -- it is evidence, not a target, and it must be re-measured (and
# re-written here) rather than inherited when the detector changes.
#
# 2026-08-16, REE_assembly at f7ab285529: 3 findings, all 3 hand-audited against
# the plan frontmatter -- precision 3/3.
#
#   self_attribution:GAP-1  names sleep_substrate:GAP-1, `done`.
#   self_attribution:GAP-2  names behavioral_diversity_isolation:GAP-A, `done`.
#   self_attribution:GAP-6  names behavioral_diversity_isolation:GAP-A, `done`,
#                           inside the chain "GAP-A/GAP-I -> FULLSTACK".
#
# TWO OF THE THREE ARE CORROBORATED BY PRE-EXISTING GOVERNANCE RECORDS written
# months before this detector existed, which is what makes the number evidence
# rather than self-assessment: the 2026-07-29 status-table reconcile says of
# GAP-1 "Two of the three gates named below HAVE CLEARED", and
# governance_2026_06_23 says of GAP-2's gate that GAP-A "has PARTIALLY fired ...
# is now status=done". The third (GAP-6, a node created 2026-08-15) has no
# independent record and rests on this session's reading.
#
# STATE THE WEAKNESSES PLAINLY rather than letting 3/3 read as validation:
#   * n=3 is a SMALL SAMPLE. It is above the floor, not comfortably above it.
#   * Unlike D-002's 4/4, this was NOT an independent adjudication chip.
#   * All three sit in ONE plan (self_attribution), so the sample says little
#     about how the parser behaves on other plans' prose conventions.
# RE-MEASURE and rewrite these constants when the detector changes or when a
# governance cycle adjudicates a batch. Do not inherit the figure.
#
# That all three findings are STILL LIVE is itself the point: the 2026-06-09
# gate text has been stale for over two months and no cycle removed it, because
# every cycle correctly re-pointed the gate in a governance NOTE and left the
# original blocking_external list standing.
PRECISION_FLOOR = 0.6
MEASURED_PRECISION: float | None = 1.0
MEASURED_AT = ("2026-08-16 / REE_assembly f7ab285529 / n=3, 3 genuine "
               "(2 corroborated by pre-existing governance notes)")

# Only the two fields the framing names. See SCOPE in the module docstring for
# why depends_on is deliberately absent.
GATE_FIELDS = ("blocking_external", "resume_condition")

# A node only carries a gate claim while it is asserting that it is WAITING.
# A `done`/`closed` node's gate text is history, not a stale assertion, and
# firing on it is pure noise against a detector that has a precision floor.
# `partial` / `in_progress` are excluded for the same reason: the node is
# demonstrably moving, so its gate text is not what is holding it.
TERMINAL_OR_MOVING = {
    "done", "closed", "partial", "in_progress", "in-progress",
    "pending_governance_stamp",
}

# What counts as CLEARED. Deliberately `done` alone, exactly as the framing
# specifies -- NOT the wider "excluded from the closure denominator" set. A gate
# node that is `deferred` or `parked` has not been satisfied; it has been set
# down, and reading that as a cleared gate would invert the meaning.
CLEARED_STATUSES = {"done"}

# plan_id:NODE-ID, optionally compounded with '/' (the live corpus really does
# write `behavioral_diversity_isolation:GAP-A/GAP-B` as one gate naming two
# nodes). Plan ids are lowercase snake_case throughout the corpus; node ids are
# alnum with - and _ separators (GAP-1, GAP-I-absorption, GAP-C-build, SELF-2,
# MAE-3, P1b, FULLSTACK). The regex is deliberately loose because the REAL
# filter is resolution against the parsed plans -- an unknown plan id or node id
# is skipped and counted, never guessed at.
_GATE_RE = re.compile(
    r"\b([a-z][a-z0-9_]{2,}):"
    r"([A-Za-z][A-Za-z0-9]*(?:[-_][A-Za-z0-9]+)*)"
    r"((?:/[A-Za-z][A-Za-z0-9]*(?:[-_][A-Za-z0-9]+)*)*)"
)

# Clause-level cues for prose parsing (resume_condition only).
#
# A CITATION VETO BEATS A GATE CUE, and the ordering is not cosmetic. The live
# corpus contains clauses carrying both, e.g. self_attribution:GAP-2's
# "Empirical proof of insufficiency: sleep_substrate:GAP-2 records '...'"
# (citation "records", gate cue "after") and its closing "See 2026-06-09
# re-adjudication note + sleep_substrate:GAP-2 (identical gate) + ..." (citation
# "see", gate cue "gate"). Both are cross-references to evidence, not gates, and
# both would be false positives if the gate cue won.
_GATE_CUES = (
    "gate", "gated", "resume", "resumes", "unblock", "unblocks", "block",
    "blocked", "blocks", "prerequisite", "precondition", "requires",
    "required", "pending", "await", "awaits", "awaiting", "wait", "waits",
    "until", "once", "before", "after", "when ", "upstream", "depends",
    "contingent", "hold", "holds",
)
_CITATION_CUES = (
    "see ", "see:", "records", "recorded", "cf.", "cf ", "per the",
    "as noted", "documented in", "retained for reconstruction",
    "prior gate text", "quoted", "citing", "reference only", "e.g.",
)

# Clause splitter. Semicolons matter as much as full stops here: the corpus
# routinely chains a citation and an unrelated observation into one sentence
# separated by ';', and splitting on '.' alone would let the citation veto leak
# across into a clause it does not govern (or vice versa).
_CLAUSE_RE = re.compile(r"(?<=[.;])\s+")

# Keys a D-007 finding may never carry, at any depth. This is the schema half of
# the framing constraint: prose can say whatever it needs to, but the STRUCTURE
# must offer a consumer no field to read a status transition or an autofix out
# of. Asserted in run() and pinned by test_d007_stale_gate_reference.py.
FORBIDDEN_KEYS = frozenset({
    "proposed_status", "suggested_status", "new_status", "status_transition",
    "transition", "unblock", "unblocks", "should_open", "should_unblock",
    "proposed_node_status", "recommended_status", "action", "autofix_payload",
    "fix", "patch", "edit", "apply",
})


class StatusProposalForbidden(RuntimeError):
    """A D-007 finding carried a status-transition or autofix-shaped field.

    Raised rather than warned. D-007's entire justification is that it does not
    make this inference, so a finding that structurally offers one is a bug in
    the detector, not a finding to be published with a caveat.
    """


# ---------------------------------------------------------------------------
# parsing
# ---------------------------------------------------------------------------

def _expand(match: re.Match) -> list[tuple[str, str]]:
    """One regex match -> [(plan_id, node_id), ...], expanding the /-compound."""
    plan_id, head, rest = match.group(1), match.group(2), match.group(3) or ""
    ids = [head] + [p for p in rest.split("/") if p]
    return [(plan_id, n) for n in ids]


def _tokens_in(text: str) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for m in _GATE_RE.finditer(text):
        out.extend(_expand(m))
    return out


def _prose_tokens(text: str) -> tuple[list[tuple[str, str]], int]:
    """Gate tokens from free text, plus a count of tokens vetoed as citations.

    A clause qualifies only if it reads as a gate AND does not read as a
    citation. Returning the vetoed count is what keeps the conservatism honest:
    the summary reports it, so a miss is a number someone can look at rather
    than silence.
    """
    kept: list[tuple[str, str]] = []
    vetoed = 0
    for clause in _CLAUSE_RE.split(text):
        toks = _tokens_in(clause)
        if not toks:
            continue
        low = clause.lower()
        if any(c in low for c in _CITATION_CUES):
            vetoed += len(toks)
            continue
        if not any(c in low for c in _GATE_CUES):
            vetoed += len(toks)
            continue
        kept.extend(toks)
    return kept, vetoed


def _field_text(value) -> str:
    """blocking_external is a list, resume_condition a string; both may be either."""
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return "\n".join(str(v) for v in value)
    return str(value)


def _subject(node_id: str, cleared: list[str], named: list[str]) -> str:
    """finding_id subject -- the (node, gate-set) suppression key.

    Encodes BOTH which gates the node names and which of them have cleared, so:

      * a settled adjudication ("still blocked, gate re-pointed") stays settled
        across runs, because neither set moves;
      * a re-pointed gate re-fires, because `named` changed;
      * a SECOND gate clearing re-fires, because `cleared` changed -- and that
        is the P2 -> P1 transition, which is exactly the news the severity tier
        exists to rank.

    Only the cleared/outstanding PARTITION is folded in, never a raw status: a
    gate moving `partial` -> `in-progress` (outstanding either way) must not
    churn the id. That is the _common.finding() rule -- "never fold a mutable
    field into the id" -- honoured at the right granularity rather than
    abandoned, since here the partition IS the defect.
    """
    return "%s@cleared=%s;named=%s" % (
        node_id, "+".join(sorted(cleared)) or "-", "+".join(sorted(named)) or "-")


def assert_no_status_proposal(findings: list[dict]) -> None:
    """Raise if any finding structurally proposes a status change or a fix.

    The schema half of the framing constraint, enforced at the point of
    production rather than left to a reviewer. See FORBIDDEN_KEYS.
    """
    def walk(obj, path: str) -> None:
        if isinstance(obj, dict):
            for k, v in obj.items():
                if str(k).lower() in FORBIDDEN_KEYS:
                    raise StatusProposalForbidden(
                        "D-007 finding carries forbidden key %r at %s -- D-007 "
                        "reports stale gate TEXT and never proposes a status "
                        "transition or a repair" % (k, path))
                walk(v, "%s.%s" % (path, k))
        elif isinstance(obj, (list, tuple)):
            for i, v in enumerate(obj):
                walk(v, "%s[%d]" % (path, i))

    for f in findings:
        if f.get("tier") != TIER:
            raise StatusProposalForbidden(
                "D-007 finding %s has tier %r -- D-007 is permanently T1"
                % (f.get("finding_id"), f.get("tier")))
        if f.get("autofix"):
            raise StatusProposalForbidden(
                "D-007 finding %s claims autofix -- re-pointing a gate IS the "
                "judgement and can never be mechanical" % f.get("finding_id"))
        walk(f, f.get("finding_id", "?"))


# ---------------------------------------------------------------------------
# detector
# ---------------------------------------------------------------------------

def run(ctx: Context) -> tuple[list[dict], dict]:
    by_id = {n.node_id: n for n in ctx.nodes}
    plan_ids = {p["id"] for p in ctx.plans}

    findings: list[dict] = []
    n_gate_bearing = 0
    n_unresolved = 0
    n_prose_vetoed = 0
    n_self_ref = 0
    n_non_plan = 0

    for node in ctx.nodes:
        if node.status in TERMINAL_OR_MOVING:
            continue

        named: dict[str, str] = {}     # full node id -> which field named it
        unresolved: list[str] = []

        for field_name in GATE_FIELDS:
            text = _field_text(node.raw.get(field_name))
            if not text:
                continue
            if field_name == "blocking_external":
                # A declared gate list: every token in it is a gate claim.
                toks = _tokens_in(text)
            else:
                toks, vetoed = _prose_tokens(text)
                n_prose_vetoed += vetoed
            for plan_id, gate_node in toks:
                gate_id = "%s:%s" % (plan_id, gate_node)
                if plan_id not in plan_ids:
                    # Not a plan reference at all. The token shape `word:WORD`
                    # is common in ordinary prose -- the live corpus writes
                    # `generation:v4`, `status:deferred`, and abbreviated
                    # cross-references like `arc_062:GAP-B` whose left side is
                    # not the plan's real id (`arc_062_rule_apprehension`).
                    # These are dropped, not resolved: fuzzy-matching a plan id
                    # is exactly the guess the "prefer a miss over a false
                    # positive" rule forbids. Counted so the miss is visible.
                    n_non_plan += 1
                    continue
                if gate_id == node.node_id:
                    n_self_ref += 1
                    continue
                if gate_id not in by_id:
                    # A REAL plan, naming a node that does not exist in it --
                    # a dangling gate reference. That is a genuine but
                    # DIFFERENT defect (it belongs to the closure-link checker),
                    # so it is counted here and never guessed at.
                    unresolved.append(gate_id)
                    continue
                named.setdefault(gate_id, field_name)

        if not named:
            n_unresolved += len(unresolved)
            continue
        n_gate_bearing += 1
        n_unresolved += len(unresolved)

        cleared = sorted(g for g in named if by_id[g].status in CLEARED_STATUSES)
        if not cleared:
            continue

        outstanding = sorted(g for g in named if g not in cleared)
        all_cleared = not outstanding

        # SEVERITY IS RANKING ONLY. Both tiers report stale TEXT; neither asserts
        # a status change. Under a contended escalation budget the tier decides
        # what gets looked at first, exactly as in D-002 -- it never withholds a
        # finding, and P1 is not a stronger claim about the node's status, only
        # about how completely the node's stated rationale has gone vacuous.
        severity = "P1" if all_cleared else "P2"
        confidence = 0.85 if all_cleared else 0.7
        signal = "strong" if all_cleared else "weak"

        cleared_desc = ", ".join(
            "%s (%s, named in %s)" % (g, by_id[g].status, named[g]) for g in cleared)
        outstanding_desc = ", ".join(
            "%s (%s)" % (g, by_id[g].status) for g in outstanding) or "none"

        detail = (
            "Node %s (status=%s, plan %s) states its gate in terms of closure "
            "node(s) that have since gone `done`. CLEARED: %s. STILL "
            "OUTSTANDING: %s.%s "
            "THIS IS A DOCUMENTATION-ACCURACY FINDING, NOT AN UNBLOCK SIGNAL. "
            "A cleared gate is not an unblocked node: all three recorded "
            "instances of this pattern (2026-06-09, 2026-06-23, 2026-07-29) "
            "ended with the node correctly staying blocked on a RE-POINTED "
            "gate, and the 2026-06-23 node record names the naive reading by "
            "name as 'the same env-conditional trap the axis_b autopsy "
            "caught'. Re-queuing on a falsely-cleared gate re-derives the "
            "known non_contributory result and burns a runner session. "
            "The adjudication asked for is whether the gate TEXT should be "
            "re-pointed to the live blocker -- the answer may well leave the "
            "status exactly as it is."
            % (
                node.node_id, node.status, node.plan_file,
                cleared_desc, outstanding_desc,
                (" Every gate node this text names has cleared, so the node's "
                 "stated rationale is now entirely vacuous and the "
                 "re-adjudication is overdue.") if all_cleared else
                (" Some named gates remain, so the text is partly stale.")
            )
        )

        findings.append(finding(
            detector=DETECTOR_ID,
            subject=_subject(node.node_id, cleared, sorted(named)),
            title="%s names gate node(s) that are now done: %s"
                  % (node.node_id, ", ".join(cleared)),
            detail=detail,
            severity=severity,
            confidence=confidence,
            signal=signal,
            # The precision floor gates ESCALATION only. Every finding is always
            # in `findings`; below the floor the detector simply stops waking a
            # model. Withholding a finding from the report would be the failure
            # mode D-002's docstring refutes.
            escalate=escalates(),
            tier=TIER,
            autofix=False,
            evidence={
                "node_id": node.node_id,
                "node_status": node.status,
                "plan_id": node.plan_id,
                "plan_file": node.plan_file,
                "gates_named": sorted(named),
                "gates_cleared": cleared,
                "gates_outstanding": outstanding,
                "gate_fields": sorted(set(named.values())),
                "gate_node_status": {g: by_id[g].status for g in sorted(named)},
                "framing": "documentation-accuracy: reports stale gate TEXT; "
                           "asserts nothing about whether the node should open",
            },
        ))

    assert_no_status_proposal(findings)

    summary = {
        "detector": DETECTOR_ID,
        "title": DETECTOR_TITLE,
        "tier": TIER,
        "n_findings": len(findings),
        "gate_bearing_nodes_scanned": n_gate_bearing,
        "dangling_gate_refs": n_unresolved,
        "prose_tokens_vetoed": n_prose_vetoed,
        "non_plan_tokens_ignored": n_non_plan,
        "self_references_skipped": n_self_ref,
        "precision_floor": PRECISION_FLOOR,
        "measured_precision": MEASURED_PRECISION,
        "measured_at": MEASURED_AT,
        "escalating": escalates(),
        "note": "Documentation accuracy only. A cleared gate is NOT an unblocked "
                "node; D-007 never proposes a status transition. Prose gate "
                "tokens vetoed as citations are counted, not silently dropped.",
    }
    return findings, summary


def escalates() -> bool:
    """True when the hand-measured precision clears the SKILL.md floor.

    Unmeasured (None) reads as BELOW the floor: an unvalidated detector with a
    precision floor has not earned the right to wake a model, and list-only is
    the state it starts in until an adjudication says otherwise.
    """
    return MEASURED_PRECISION is not None and MEASURED_PRECISION >= PRECISION_FLOOR
