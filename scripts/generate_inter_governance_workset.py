#!/usr/bin/env python3
"""
Generate the post-governance inter-governance workset (machine + human views).

Usage (from REE_assembly root):
    /opt/local/bin/python3 scripts/generate_inter_governance_workset.py

Outputs:
    evidence/planning/inter_governance_workset.v1.json
    evidence/planning/inter_governance_workset.md

Consumed by GET /api/workset and /workset.html. Regenerate via /inter-governance-brief.

SUBSTRATE LANE FAILS OPEN TO "ready" -- KNOWN, AND THE REASON STALENESS IS SILENT
--------------------------------------------------------------------------------
`_substrate_ready_items()` emits an /implement-substrate item for every
substrate_queue entry with `ready: true` that no classifier positively
recognises as done. There is no "unknown status" branch: a status string the
matchers do not understand takes the default, and the default is "go build it".
So a substrate_queue status that drifts, or a new status token nobody taught
this file about, does not error -- it silently becomes a spawned chip to
re-implement something that already landed. When auditing this lane, always ask
what an UNRECOGNISED status does, not just what the listed ones do.

Nothing here is cached: `_load_substrate_queue()` re-reads substrate_queue.json
on every call, and igw_routine_tick.regenerate_workset() shells out to this
script each tick (falling back to the last-good workset on disk ONLY on
timeout/non-zero exit, GENERATOR_TIMEOUT_SEC=420). Staleness in this lane is
therefore a CLASSIFICATION defect, not a freshness one -- do not go looking for
a stale snapshot.

THAT LAST SENTENCE IS TRUE OF THE SUBSTRATE LANE ONLY -- SEE FM8
-----------------------------------------------------------------
It holds because substrate_queue.json lives in THIS repo, next to this script,
so a regen necessarily sees what the session sees. The EXPERIMENT lane's main
input does not: `ree-v3/experiment_queue.json` is a file in a DIFFERENT repo
that this generator never syncs and no IGW tick pulls, so it goes stale
silently and without bound. Read as a general claim about the whole generator,
the sentence above sends you looking for a classification bug that is not there
-- which is what happened on 2026-08-03 (FM8, `_load_queue`). When auditing the
EXPERIMENT lane, check the freshness of the INPUT first.

FM3 (2026-08-03): `implemented_pending_validation` was classified `ready`.
Both `_status_resolved` and `_status_terminal` hard-veto on the substring
"pending", which is right for the retest-blocker question they answer and wrong
for the implement question -- that status asserts the build HAS landed and only
validation is outstanding. It is the second-most-common non-empty status in
substrate_queue.json (11 entries the day this was found). Confirmed incident:
on 2026-08-03 four of the five items rendered as "Substrate ready" (SD-091,
SD-092, SD-modulatory-channel-route-decomp-gate-fix,
mech090-arc071-attick-persistent-handle-fix) were already fully landed in
ree-v3; they had been staged as IGW-20260803-206..209, sat in "awaiting human
launch" for up to two days, and were GC-reaped unused (see
evidence/planning/igw_routine_log.md, STAGE entries 2026-08-02T18:32Z ->
2026-08-03T14:02Z). A manual status correction (98651d2e27) was applied as a
stopgap and did NOT fix it -- the corrected statuses were themselves
`implemented_pending_validation`, so the same four re-qualified as ready on the
very next regen. Fix: `_status_implementation_complete` /
`_substrate_implementation_complete`, which suppress the IMPLEMENT lane only and
leave retest-blocker semantics untouched. Regression test:
scripts/test_generate_inter_governance_workset_substrate_staleness.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote as urlquote

try:
    import yaml as _yaml
except ImportError:
    _yaml = None

ROOT = Path(__file__).resolve().parent.parent
PLANNING = ROOT / "evidence" / "planning"
EVIDENCE = ROOT / "evidence" / "experiments"
CLAIMS_YAML = ROOT / "docs" / "claims" / "claims.yaml"
REE_V3_QUEUE = ROOT.parent / "ree-v3" / "experiment_queue.json"
REE_V3_CORE = ROOT.parent / "ree-v3" / "ree_core"
# Remote-tracking ref the committed queue snapshot is read from (see _load_queue).
# ree-v3's default branch is `main`; the remote-tracking ref, not the local
# branch, because the local branch is exactly what goes stale in a checkout
# nobody pulls.
QUEUE_GIT_REF = "origin/main"

# --- GOV-CONFIRM-1 evidence-confirmer lane (plan: gov_confirm_1_plan.md) -------
# Generative-discovery complement to the consume-only _proposed_experiments lane:
# surface candidate/provisional claims that are confirmable-but-unconfirmed (built
# substrate + thin/zero experimental evidence + lit_conf >= floor, not wall-bound).
# CONFIRMER_AUTOSPAWN_ENABLED is the P1->P2 rollout gate. P1 = surface ONLY: items
# render on /workset with status "surfaced", which the external IGW auto-spawn routine
# (spawns `ready` items) and check_workset_drift (validates `ready` items) both skip.
# P2 (LIVE 2026-07-14, after 3/3 seed confirmers PASSed -- V3-EXQ-757/758/759):
# emit status "ready" (drift-checked + autospawn-eligible) at LOW priority, THROTTLED
# to at most CONFIRMER_AUTOSPAWN_CAP concurrently (post-pass demotes the surplus back
# to "surfaced") so background confirmers drain steadily without a resource spike.
CONFIRMER_AUTOSPAWN_ENABLED = True
CONFIRMER_LIT_FLOOR = 0.6
CONFIRMER_AUTOSPAWN_CAP = 3
PENDING_REVIEW = EVIDENCE / "pending_review.md"
PROMOTION_MD = EVIDENCE / "promotion_demotion_recommendations.md"
SUBSTRATE_QUEUE = PLANNING / "substrate_queue.json"
PROPOSALS_JSON = PLANNING / "experiment_proposals.v1.json"
RUNNER_STATUS = EVIDENCE / "runner_status.json"
RUNNER_STATUS_DIR = EVIDENCE / "runner_status"
REVIEW_TRACKER = EVIDENCE / "review_tracker.json"
OUTPUT_JSON = PLANNING / "inter_governance_workset.v1.json"
OUTPUT_MD = PLANNING / "inter_governance_workset.md"

_EXQ_RE = re.compile(r"V3-EXQ-\d+[a-z]?", re.IGNORECASE)
_CLAIM_TOKEN_RE = re.compile(
    r"\b(?:ARC|INV|MECH|Q|SD|IMPL|DEV)-[\w-]+\b", re.IGNORECASE
)
# Curated outcome lenses for /workset UI (claim search + grouping).
OUTCOME_LENSES: dict[str, dict] = {
    "ARC-065": {
        "label": "Behavioural diversity (ARC-065)",
        "anchor_claims": [
            "ARC-065", "Q-043", "Q-044", "Q-045",
            "MECH-313", "MECH-314", "MECH-314a", "MECH-314b", "MECH-314c",
        ],
        "plan_ids": ["arc_062_rule_apprehension", "infant_substrate"],
    },
    "ARC-062": {
        "label": "Rule apprehension (ARC-062 / MECH-309)",
        "anchor_claims": [
            "ARC-062", "MECH-309", "INV-074", "MECH-333", "MECH-334",
            "MECH-312", "MECH-312a", "MECH-312b", "MECH-312c", "MECH-312d",
        ],
        "plan_ids": ["arc_062_rule_apprehension"],
    },
    "ARC-064": {
        "label": "Bottom-up rule discovery (ARC-064)",
        "anchor_claims": ["ARC-064", "MECH-316", "MECH-317", "MECH-318", "MECH-319"],
        "plan_ids": ["arc_062_rule_apprehension"],
    },
    "sleep_sd017": {
        "label": "Sleep substrate (SD-017 cluster)",
        "anchor_claims": [
            "SD-017", "MECH-204", "MECH-205", "INV-049", "Q-041", "Q-042",
            "ARC-045", "MECH-166", "MECH-111",
        ],
        "plan_ids": ["sleep_substrate"],
    },
    "self_attribution": {
        "label": "Self-attribution (SD-029 / MECH-256)",
        "anchor_claims": [
            "SD-029", "MECH-256", "MECH-257", "MECH-258", "ARC-033", "SD-013",
        ],
        "plan_ids": ["self_attribution"],
    },
    "goal_pipeline": {
        "label": "Goal pipeline / monostrategy",
        "anchor_claims": [
            "SD-049", "SD-015", "MECH-295", "MECH-306", "MECH-117", "ARC-030",
            "ARC-032", "MECH-229", "MECH-230",
        ],
        "plan_ids": ["goal_pipeline"],
    },
    "infant_substrate": {
        "label": "Infant substrate / ISEF",
        "anchor_claims": [
            "DEV-NEED-001", "DEV-NEED-007", "INV-073", "INV-055", "ARC-046",
        ],
        "plan_ids": ["infant_substrate"],
    },
    "commitment_closure": {
        "label": "Commitment / closure governance",
        "anchor_claims": [
            "SD-033a", "SD-033b", "SD-034", "MECH-260", "MECH-262", "MECH-263",
        ],
        "plan_ids": ["commitment_closure", "sd033_governance"],
    },
}
_LANE_SKILLS = {
    "governance": "/governance",
    "experiment": "/queue-experiment",
    "substrate": "/implement-substrate",
    "lit": "/lit-pull",
    "ops": "(manual)",
    "plan": "(plan reconcile)",
    "monitor": "(monitor -- do not re-queue)",
}

# experiment_proposals.v1.json proposal_type values that route to the /lit-pull
# lane/skill instead of /queue-experiment (both observed in the data: an early
# "literature" tag and the current "literature_review").
_LITERATURE_PROPOSAL_TYPES = {"literature_review", "literature"}


def _proposal_lane_skill(proposal_type: str | None) -> tuple[str, str]:
    """Lane/skill for one experiment_proposals.v1.json item, keyed on its OWN
    proposal_type -- never on owner_backlog_id. A single backlog id can back
    proposals of different types (confirmed 2026-08-01: EVB-0481/Q-086 backed
    both an "experimental" EXP- proposal and a "literature_review" LIT-
    proposal; deriving the tag from the backlog id instead of the proposal
    mistagged the literature one as /queue-experiment)."""
    if (proposal_type or "").strip().lower() in _LITERATURE_PROPOSAL_TYPES:
        return "lit", _LANE_SKILLS["lit"]
    return "experiment", _LANE_SKILLS["experiment"]


def _proposal_title(lane: str, claim_id: str | None) -> str:
    """Title for one proposal-lane IGW item, tagged by lane so an experiment
    proposal and a literature-review proposal for the SAME claim_id don't
    render as identical rows in the /workset table (they can coexist -- see
    _proposal_lane_skill). claim_id stays the stable key; only the prefix
    varies. Does not affect IGW ledger identity: stable_hash_item() keys on
    skill, not title."""
    prefix = "Proposal" if lane == "experiment" else "Literature proposal"
    return f"{prefix} for {claim_id}" if claim_id else f"{prefix} (unclaimed)"


# experiment_proposals.v1.json status values meaning "a prior investigation
# adjudicated this proposal as blocked on unbuilt substrate" -- the manually
# maintained field the retest lane below consults. "proposed_blocked_substrate"
# is the one observed variant spelling (MECH-343, EXP-0176) of the same
# semantic as the canonical "blocked_substrate".
_PROPOSAL_BLOCKED_SUBSTRATE_STATUSES = {"blocked_substrate", "proposed_blocked_substrate"}

# FM10 (2026-08-03): the broader "a prior session adjudicated this proposal as
# NOT-QUEUEABLE-NOW" set, consumed by the GOV-CONFIRM-1 confirmer lane. A
# superset of the blocked_substrate family above, adding the statuses whose
# semantic is the same STOP arrived at by a different route:
#   * blocked_on_gate -- an upstream design/claim prerequisite is unresolved.
#   * gated -- a named session recorded a `gating_reason` (and often a
#     `release_condition`) on this proposal. This is the SAME kind of manually
#     written, manually cleared adjudication as blocked_substrate; the only
#     difference is which field the session reached for.
#   * skipped -- deliberately not pursued (the one live case, EXP-0131/ARC-018,
#     is why_now=['active_conflict']).
#   * deferred_substrate_not_ready -- the self-route verdict spelled out.
# Deliberately EXCLUDES `executed`, `queued`, and `proposed`: those are not
# adjudications, they are lifecycle positions ("queued" is already handled by
# the queue gate, `_confirmer_queued_claims`).
#
# TENSION worth stating rather than burying, because it is re-judgeable: the
# confirmer lane deliberately RELAXES the v3_pending drop (user decision
# 2026-07-14, gov_confirm_1_plan.md), and 4 of the 5 live `gated` confirmer
# candidates on 2026-08-03 (MECH-282, SD-055, MECH-339, MECH-340) were gated
# with the reason "hold_pending_v3_substrate governance verdict +
# v3_pending=true". Including `gated` therefore re-imposes, via the proposal
# record, something the lane chose not to impose via the claim record. It is
# nonetheless the right call HERE only because this predicate does NOT drop the
# item -- it renders it `blocked` with the gating_reason shown (see
# _evidence_confirmer_candidates), so the claim stays visible on /workset and
# flips back to eligible the moment a session clears the gate. If this is ever
# changed to a drop, revisit `gated`'s membership first.
_PROPOSAL_ADJUDICATED_NOT_QUEUEABLE_STATUSES = _PROPOSAL_BLOCKED_SUBSTRATE_STATUSES | {
    "blocked_on_gate",
    "gated",
    "skipped",
    "deferred_substrate_not_ready",
}


def _proposals_by_claim(statuses: set[str]) -> dict[str, dict]:
    """claim_id -> first experiment_proposals.v1.json entry whose status is in
    `statuses`. THE single reader of that file's claim field.

    One parser, deliberately -- FM9's whole lesson was that the retest lane and
    the confirmer lane each grew their own reader of the same field pair and
    drifted apart for two months. `_proposal_blocked_substrate_by_claim` (retest
    lane, FM7) and `_confirmer_adjudicated_proposals` (confirmer lane, FM10) are
    both thin wrappers over this with different status sets.

    experiment_proposals.v1.json carries the claim as a SINGULAR `claim_id` on
    every one of its 354 live entries (audited 2026-08-03; zero use the
    `claim_ids` list form the ree-v3 QUEUE uses). The list form is read anyway so
    this cannot become the next singular-vs-list blind spot if the schema drifts.
    First occurrence wins (the file carries duplicate claim ids).
    """
    if not PROPOSALS_JSON.exists():
        return {}
    try:
        data = json.loads(PROPOSALS_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out: dict[str, dict] = {}
    for p in data.get("items") or []:
        if not isinstance(p, dict):
            continue
        if p.get("status") not in statuses:
            continue
        cids = [str(c) for c in (p.get("claim_ids") or []) if c]
        single = p.get("claim_id")
        if single:
            cids.append(str(single))
        for cid in cids:
            if cid and cid not in out:
                out[cid] = p
    return out


def _confirmer_adjudicated_proposals() -> dict[str, dict]:
    """claim_id -> the proposal record a prior session adjudicated as not
    queueable now (FM10). Consumed by the GOV-CONFIRM-1 confirmer lane.

    THE DEFECT THIS CLOSES. `_evidence_confirmer_candidates` is generative: it
    scans the claim registry for built-substrate + zero-evidence candidates and
    AUTHORS a confirmer item. Its own docstring anticipates that the per-item
    /queue-experiment pass "self-routes substrate_not_ready_requeue if only a
    behavioural DV exists" -- but the lane had NO MEMORY of that outcome, so it
    re-offered the identical claim on every regeneration and the metaworker
    dispatcher spent a whole worker re-deriving the same negative.

    Confirmed incident (2026-08-03): MECH-191 was worked TWICE the same day
    (chips igw-confirm-mech191 and igw-233-mech191-confirm), both resolving
    "QUEUED NOTHING -- self-routed substrate_not_ready_requeue". The second of
    those sessions recorded the durable verdict at REE_assembly 38236f6779
    (20:11Z): EXP-0276 (claim_id MECH-191) status=blocked_substrate, with a
    gating_reason that had RE-VERIFIED the block against live ree-v3 substrate.
    The workset regenerated at 22:10Z -- two hours later -- and IGW-20260803-229
    "Confirm evidence: MECH-191" still rendered `ready`.

    NOT the same gap as FM9 (5aa0d3267a), which fixed the queue gate and
    explicitly verified this survivor was "genuinely unqueued". That verdict is
    correct. UNQUEUED IS NOT UNADJUDICATED -- a session can conclude that nothing
    should be queued at all, and that conclusion has to be readable too.

    Reads the same manually-maintained field the retest lane's FM7 fix consults,
    via the same parser (`_proposals_by_claim`). Same staleness semantic: no
    auto-clear, the status sits until a session clears it once the real blocker
    resolves. That is the intended manually-adjudicated behaviour, not a bug.
    """
    return _proposals_by_claim(_PROPOSAL_ADJUDICATED_NOT_QUEUEABLE_STATUSES)


def _proposal_adjudication_reason(prop: dict) -> str:
    """One-line human reason from an adjudicated proposal, for `blocked_by`.

    Prefers the most specific field the adjudicating session filled in, since
    which one it reached for varies by status: structured `blocked_by`, then the
    free-text `gating_reason` / `blocked_note`, then `release_condition`, and
    finally a bare pointer to the record. Never returns empty -- an item rendered
    `blocked` with no reason is indistinguishable from a generator bug.
    """
    pid = prop.get("proposal_id") or "?"
    status = prop.get("status") or "?"
    blocked_by_list = prop.get("blocked_by") or []
    if blocked_by_list:
        detail = ", ".join(str(x) for x in blocked_by_list)[:200]
        return f"experiment_proposals.v1.json {pid} status={status}: blocked by {detail}"
    for field in ("gating_reason", "blocked_note", "release_condition"):
        val = prop.get(field)
        if val:
            return f"experiment_proposals.v1.json {pid} status={status}: {str(val)[:200]}"
    return (
        f"experiment_proposals.v1.json {pid} status={status} "
        f"(backlog_id {prop.get('backlog_id') or '?'}); see the proposal record "
        f"for adjudication detail."
    )


def _proposal_blocked_substrate_by_claim() -> dict[str, dict]:
    """claim_id -> first experiment_proposals.v1.json entry whose status is a
    blocked_substrate variant (FM7).

    The retest lane's blocked-ness (_retest_blockers + the epistemic_category
    ceiling check + _claim_v3_testable) all reason about *unbuilt substrate_queue
    entries*. None of them can see a proposal a prior investigating session
    already adjudicated as blocked on OTHER CLAIMS rather than a substrate_queue
    row. Confirmed incident: INV-089's retest was investigated and closed
    2026-07-31 (session inv089-retest-exq-subagent), which traced the real
    blocker to two unbuilt CLAIMS (MECH-457, INV-088) and recorded
    status=blocked_substrate on the backing proposal (EXP-0080, claim_id
    INV-089) in this file specifically because there was no substrate_queue row
    to hang the block on. _retest_blockers found nothing (no substrate_queue
    entry lists INV-089 in unblocks_claims) and INV-089 carries no
    epistemic_category, so the ceiling fallback never engaged either -- the
    generator re-surfaced it as `ready` the very next regen (IGW-20260802-220),
    wasting a second investigation before the discrepancy was caught again.

    Deliberately read-only and additive: this does not re-derive substrate
    readiness itself, it consults a field a prior session already maintains
    for exactly this purpose. Staleness: there is no auto-clear mechanism (see
    the call site's comment) -- a blocked_substrate status sits until a
    human/session manually clears it once the real blocker resolves, which is
    the intended manually-adjudicated semantic (matches how the INV-089
    investigator explicitly set it, and how claims.yaml pending_retest_after_substrate
    itself works -- also never auto-cleared).

    FM10: body moved into the shared `_proposals_by_claim` parser so the retest
    lane and the confirmer lane cannot grow two readers of this file (the exact
    drift FM9 fixed for the queue). Status set unchanged -- the retest lane's
    scope is deliberately NARROWER than the confirmer lane's
    (_PROPOSAL_ADJUDICATED_NOT_QUEUEABLE_STATUSES): a retest already has an
    explicit claims.yaml pending_retest_after_substrate flag asking for it, so
    only a substrate block should hold it back.
    """
    return _proposals_by_claim(_PROPOSAL_BLOCKED_SUBSTRATE_STATUSES)


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _normalize_status(s: str | None) -> str:
    if not s:
        return "open"
    return str(s).strip().lower().replace(" ", "_").replace("-", "_")


def _parse_plan_frontmatter(path: Path) -> dict | None:
    if _yaml is None:
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    try:
        fm = _yaml.safe_load(text[4:end])
    except Exception:
        return None
    if not isinstance(fm, dict):
        return None
    plan = fm.get("closure_plan")
    return plan if isinstance(plan, dict) else None


def _pending_review_count() -> int:
    if not PENDING_REVIEW.exists():
        return 0
    m = re.search(r"Pending:\s*\*\*(\d+)\*\*", PENDING_REVIEW.read_text(encoding="utf-8"))
    return int(m.group(1)) if m else 0


def _queue_items_from_bytes(raw: str) -> list[dict] | None:
    try:
        data = json.loads(raw)
    except Exception:
        return None
    return [x for x in (data.get("items") or []) if isinstance(x, dict)]


def _queue_from_worktree() -> list[dict]:
    if not REE_V3_QUEUE.exists():
        return []
    try:
        raw = REE_V3_QUEUE.read_text(encoding="utf-8")
    except Exception:
        return []
    return _queue_items_from_bytes(raw) or []


def _queue_from_git(ref: str = QUEUE_GIT_REF) -> list[dict] | None:
    """experiment_queue.json as committed on ree-v3's remote-tracking `ref`.

    Returns None (never []) when the snapshot cannot be read, so the caller can
    tell "no committed snapshot available" apart from "committed queue is empty".
    Reads an already-fetched local ref -- deliberately NO `git fetch`: this
    generator runs on an hourly IGW tick, and a network call there can hang the
    tick behind GENERATOR_TIMEOUT_SEC for no benefit the next tick would not get.
    """
    repo = REE_V3_QUEUE.parent
    if not (repo / ".git").exists():
        return None
    try:
        proc = subprocess.run(
            ["git", "-C", str(repo), "show", f"{ref}:experiment_queue.json"],
            capture_output=True, text=True, timeout=20,
        )
    except Exception:
        return None
    if proc.returncode != 0:
        return None
    return _queue_items_from_bytes(proc.stdout)


def _merge_queue_snapshots(
    worktree: list[dict], committed: list[dict]
) -> list[dict]:
    """Union of the two snapshots, keyed on queue_id, committed body preferred.

    Committed-first because that file is materialised by the coordinator's
    `phase3-queue:` writer from the DB and is the authoritative snapshot; a
    working-tree entry with the same queue_id is at best equal and at worst a
    stale checkout of it. Worktree-only entries are still appended -- that is an
    experiment queued locally and not yet pushed, which must count as queued.
    """
    out: list[dict] = list(committed)
    seen = {
        str(it.get("queue_id"))
        for it in committed
        if it.get("queue_id")
    }
    for item in worktree:
        qid = item.get("queue_id")
        if qid and str(qid) in seen:
            continue
        out.append(item)
    return out


def _load_queue() -> list[dict]:
    """The experiment queue, as fresh as this checkout can make it.

    FM8 (2026-08-03) -- THE WORKING-TREE READ ALONE IS A STALENESS BUG, and it is
    the one this file's header note did NOT cover. That note says staleness here
    is "a CLASSIFICATION defect, not a freshness one -- do not go looking for a
    stale snapshot", and for the SUBSTRATE lane that is true: substrate_queue.json
    lives in THIS repo, alongside this script, so a regen sees whatever the
    session sees. `ree-v3/experiment_queue.json` is the opposite case -- a file in
    a DIFFERENT repo that this generator never syncs and whose checkout no IGW
    tick pulls. It goes stale silently and without limit.

    Confirmed incident (2026-08-03T21:55Z, metaworker cycle 275): the ree-v3
    checkout was 26 commits behind origin/main and its queue held 2 entries
    against origin/main's 8. Every suppression predicate downstream of this
    function was therefore reasoning about experiments that already existed:
      * "Retest after substrate: ARC-045" rendered `ready` although V3-EXQ-436d
        (claim_ids ARC-045/SD-017/MECH-166) was pending -- `_queued_retest_coverage`
        is CORRECT and would have absorbed it; it was never shown the entry.
      * "Queue depth low (0 pending)" against 4 genuinely-pending items.
    Verified by running build_workset() twice on one code base, swapping only this
    function's return: both items drop out with the committed snapshot, and no new
    item appears. So the predicates were never the defect here -- the INPUT was.

    Union rather than replacement because the two sources fail in opposite
    directions: the committed ref misses an experiment queued locally and not yet
    pushed, the working tree misses everything landed since it was last pulled.
    For the question every caller actually asks -- "does an experiment for this
    claim already exist?" -- presence in EITHER is the honest answer.

    Fails open to the old behaviour (worktree only) whenever the committed
    snapshot cannot be read: no ree-v3 checkout, no such ref, git missing or slow,
    unparseable blob. A generator that dies because a sibling repo moved would be
    a worse failure than the staleness it is fixing.
    """
    worktree = _queue_from_worktree()
    committed = _queue_from_git()
    if committed is None:
        return worktree
    return _merge_queue_snapshots(worktree, committed)


def _running_exqs() -> dict[str, str]:
    """queue_id -> machine from fresh runner heartbeats/status (best effort)."""
    out: dict[str, str] = {}
    for d in (EVIDENCE / "runner_heartbeats").glob("*.json") if (EVIDENCE / "runner_heartbeats").is_dir() else []:
        try:
            hb = json.loads(d.read_text(encoding="utf-8"))
        except Exception:
            continue
        exq = hb.get("current_exq")
        if exq:
            out[str(exq)] = str(hb.get("machine") or d.stem)
    return out


def _pending_governance_recs() -> list[dict]:
    if not PROMOTION_MD.exists():
        return []
    rows = []
    for line in PROMOTION_MD.read_text(encoding="utf-8").splitlines():
        if "`pending_user`" not in line and "pending_user" not in line:
            continue
        if not line.strip().startswith("|") or "claim_id" in line:
            continue
        parts = [p.strip().strip("`") for p in line.split("|")[1:-1]]
        if len(parts) >= 5 and parts[0]:
            rows.append({
                "claim_id": parts[0],
                "recommendation": parts[3] if len(parts) > 3 else "",
            })
    return rows


def _claim_retest_ids() -> set[str]:
    if not CLAIMS_YAML.exists():
        return set()
    out: set[str] = set()
    current: str | None = None
    for line in CLAIMS_YAML.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^- id:\s*(\S+)", line)
        if m:
            current = m.group(1)
        if current and "pending_retest_after_substrate" in line:
            if re.search(r"pending_retest_after_substrate:\s*true", line):
                out.add(current)
    return out


def _strip_yaml_scalar(value: str) -> str:
    """Strip an inline `# comment`, surrounding quotes, and whitespace."""
    v = value.split("#", 1)[0].strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
        v = v[1:-1]
    return v.strip()


def _load_claims_meta() -> dict[str, dict]:
    """claim_id -> {status, claim_type, epistemic_category, invariant_type,
    implementation_phase, version_relevance, v3_pending}.

    Line-based block parser (same shape as _claim_retest_ids) so we never pay a
    full yaml.safe_load on the large registry. First occurrence of each field
    inside a `- id:` block wins; inline `# comments` and quotes are stripped.

    implementation_phase / version_relevance feed _is_deferred_beyond_v3 so the
    experiment-proposal lane can suppress claims scoped to V4+ (we work V3 until
    it is finished, then reassess the roadmap before V4 work begins).
    v3_pending feeds _claim_v3_testable so the experiment lanes can suppress
    claims the governance V3-pending gate ignores (R5; mirrors R1 in
    igw_routine_tick._claim_is_v3_testable).
    """
    out: dict[str, dict] = {}
    if not CLAIMS_YAML.exists():
        return out
    current: str | None = None
    fields: dict[str, str] = {}
    keys = (
        "status", "claim_type", "epistemic_category", "invariant_type",
        "implementation_phase", "version_relevance", "v3_pending",
        "title", "location",
    )

    def _flush() -> None:
        if current:
            out[current] = dict(fields)

    for line in CLAIMS_YAML.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^- id:\s*(\S+)", line)
        if m:
            _flush()
            current = _strip_yaml_scalar(m.group(1))
            fields = {}
            continue
        if current is None:
            continue
        for key in keys:
            if key in fields:
                continue
            mm = re.match(r"^\s+" + key + r":\s*(.+)", line)
            if mm:
                fields[key] = _strip_yaml_scalar(mm.group(1))
    _flush()
    return out


_EPI_SUPPRESS_PROPOSAL = {
    "substrate_coherence", "substrate_ceiling", "substrate_conditional",
    "derivational", "out_of_domain", "governance_rule",
}
_CLAIM_DEAD_STATUSES = {"resolved", "superseded", "deprecated"}

# --- R5: experiment-lane testability gate -----------------------------------
# Mirrors R1 (igw_routine_tick._claim_is_v3_testable). A /queue-experiment
# cannot yield contributory V3 evidence for a claim the governance V3-pending
# gate is designed to ignore, so surfacing one as a `ready` experiment-lane IGW
# item is a structural NO-OP. R1 filters these at spawn time; R5 keeps them out
# of the workset's `ready` set at the SOURCE, so most of what R1 would reject
# never reaches it. Keep these two sets identical to R1's UNTESTABLE_EPISTEMIC /
# TESTABLE_CLAIM_STATUSES. Note _EPI_SUPPRESS_PROPOSAL above is intentionally a
# SUPERSET (adds substrate_coherence) used only by the proposal lane.
_TESTABLE_CLAIM_STATUSES = {"candidate", "provisional"}
_UNTESTABLE_EPISTEMIC = {
    "substrate_ceiling", "substrate_conditional", "out_of_domain", "derivational",
    "governance_rule",
}


def _is_deferred_beyond_v3(meta: dict | None) -> bool:
    """True when a claim is scoped to V4+ only (no V3 relevance).

    Roadmap rule: we work V3 until it is finished enough, then reassess the whole
    roadmap before opening V4 work. A V4/V5-only claim must NOT surface as a
    `/queue-experiment` proposal in the meantime -- a probe against it self-routes
    to a blocked_substrate STOP (vacuous), so it is operator noise, not work.

    Suppress when implementation_phase is v4/v5 OR version_relevance names a v4+/v5
    band with no v3 component. Deliberately does NOT suppress:
      * implementation_phase v3 / v3_pending (the live V3 work),
      * version_relevance that includes v3 (e.g. v3_v4 -- still V3-relevant).
    This is independent of epistemic_category: a plain v4 mechanism_hypothesis that
    is not substrate_conditional is still suppressed here.
    """
    if not meta:
        return False
    phase = (meta.get("implementation_phase") or "").strip().lower()
    if phase.startswith("v4") or phase.startswith("v5"):
        return True
    vrel = (meta.get("version_relevance") or "").strip().lower()
    if vrel and "v3" not in vrel and ("v4" in vrel or "v5" in vrel):
        return True
    return False

# Promotion/demotion verdicts that are NOT a governance decision the operator
# can act on in a /governance cycle. The verdict IS the decision: "hold". The
# claim is gated on V3 substrate implementation (and a per-claim retest once the
# substrate lands), or deliberately V4-deferred by architectural commitment.
# These reach pending_user only because the hold recommendation has not yet been
# stamped `applied`; stamping it is a no-op acknowledgement, not an adjudication.
# Surfacing them as `ready` high-severity governance work packages mis-reads a
# HOLD as a pending decision -- they are reframed as `blocked` substrate-lane
# items so they stay visible without masquerading as decisions. Genuinely
# actionable verdicts (narrow_open_question, hold_candidate_resolve_conflict,
# promote_*, demote_*) are NOT in this set and keep their ready governance lane.
_HELD_PENDING_RECS = {
    "hold_pending_v3_substrate": "V3 substrate implementation / per-claim retest",
    "held_v4_by_architectural_commitment": "V4 substrate (architectural commitment)",
}


def _resolve_epistemic_category(meta: dict | None) -> str:
    """Resolved epistemic_category for a claim, mirroring the indexer's
    _resolve_epistemic_category: explicit value wins, else infer from claim_type
    + invariant_type. Unknown / missing -> 'standard'.
    """
    if not meta:
        return "standard"
    explicit = (meta.get("epistemic_category") or "").strip().lower()
    if explicit:
        return explicit
    ctype = (meta.get("claim_type") or "").strip().lower()
    itype = (meta.get("invariant_type") or "").strip().lower()
    if ctype == "architectural_commitment":
        return "substrate_coherence"
    if ctype == "invariant" and itype == "universal":
        return "substrate_coherence"
    if ctype in ("open_question", "question"):
        return "answer_state"
    return "standard"


def _claim_v3_testable(cid: str,
                       claims_meta: dict[str, dict] | None) -> tuple[bool, str]:
    """Return (testable, reason) for one claim -- R5, mirroring R1
    (igw_routine_tick._claim_is_v3_testable).

    NOT v3-testable when claims.yaml shows v3_pending true, an untestable
    resolved epistemic_category (substrate_ceiling / substrate_conditional /
    out_of_domain / derivational), or a status outside {candidate, provisional}.
    An unknown claim (absent from the registry, e.g. a regen lag) fails OPEN so
    a registry gap never silently starves the experiment lanes -- the same
    fail-open contract R1 uses. Keeping this in lockstep with R1 is what makes
    R5 a source-side reduction of NO-OP spawns rather than a divergent second
    filter.

    Note: _load_claims_meta stores fields as strings (yaml scalars), so
    v3_pending arrives as the string "true", not a bool (R1 parses real YAML and
    sees the bool). Compare on the lowercased string accordingly.
    """
    meta = (claims_meta or {}).get(cid)
    if meta is None:
        return True, ""  # unknown -> fail open (matches R1)
    if (meta.get("v3_pending") or "").strip().lower() in ("true", "1", "yes"):
        return False, f"{cid} v3_pending"
    ec = _resolve_epistemic_category(meta)
    if ec in _UNTESTABLE_EPISTEMIC:
        return False, f"{cid} epistemic_category={ec}"
    st = (meta.get("status") or "").strip().lower()
    if st not in _TESTABLE_CLAIM_STATUSES:
        return False, f"{cid} status={st}"
    return True, ""


# claim_evidence.v1.json is ~10 MB. _claims_with_experimental_evidence() and
# _claim_lit_conf() each used to parse it independently, so a single run read it
# twice. Both want only the `claims` map. Memoized here (one-shot script, so a
# plain module-level cache is sufficient -- no mtime keying needed). Returns {}
# on missing/unparseable/malformed, preserving both callers' prior behaviour.
_CLAIM_EVIDENCE_CLAIMS_CACHE: dict | None = None


def _claim_evidence_claims() -> dict:
    """Parse claim_evidence.v1.json once per process; return its `claims` map."""
    global _CLAIM_EVIDENCE_CLAIMS_CACHE
    if _CLAIM_EVIDENCE_CLAIMS_CACHE is None:
        path = EVIDENCE / "claim_evidence.v1.json"
        claims = None
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                claims = data.get("claims") if isinstance(data, dict) else None
            except Exception:
                claims = None
        _CLAIM_EVIDENCE_CLAIMS_CACHE = claims if isinstance(claims, dict) else {}
    return _CLAIM_EVIDENCE_CLAIMS_CACHE


def _claims_with_experimental_evidence() -> set[str]:
    """Claim IDs that already carry genuine experimental evidence per
    claim_evidence.v1.json (genuine_exp_count > 0). Used to suppress stale
    `status: proposed` proposals whose experiment effectively already ran.
    """
    claims = _claim_evidence_claims()
    out: set[str] = set()
    for cid, summary in claims.items():
        if isinstance(summary, dict) and (summary.get("genuine_exp_count") or 0) > 0:
            out.add(str(cid))
    return out


def _queued_retest_coverage(queue_items: list[dict]) -> dict[str, str]:
    """claim_id -> queue_id mapping for claims covered by any queue entry.

    Any item still in ree-v3/experiment_queue.json (pending or claimed) that
    names a claim is treated as a queued retest for that claim. The retest IGW
    loop suppresses pending_retest_after_substrate claims that already have a
    queued retest, matching the operator mental model that a queued retest
    needs no human action until completion.

    Queue entries carry the claim either as a singular `claim_id` string (the
    common case -- e.g. V3-EXQ-610e has claim_id="INV-074") or as a `claim_ids`
    list. BOTH must be read: a 2026-06-04 audit found this function read only
    the list form, so every singular-`claim_id` queued retest went undetected
    and its IGW item stayed `ready` -- which the hourly auto-spawn routine then
    re-spawned every hour as a NO-OP (INV-074 12x over 6 days, MECH-229 8x).

    Returns the first matching queue_id per claim (queue order). If multiple
    queue entries cover the same claim, only the earliest is reported in the
    map; suppression applies regardless.
    """
    out: dict[str, str] = {}
    for item in queue_items:
        if not isinstance(item, dict):
            continue
        qid = item.get("queue_id") or ""
        if not qid:
            continue
        cids = list(item.get("claim_ids") or [])
        single = item.get("claim_id")
        if single:
            cids.append(single)
        for cid in cids:
            cid_s = str(cid)
            if cid_s and cid_s not in out:
                out[cid_s] = str(qid)
    return out


def _confirmer_queued_claims(queue_items: list[dict]) -> set[str]:
    """Claims that already have an experiment in the queue, for the GOV-CONFIRM-1
    anti-double-spawn gate.

    FM9 (2026-08-03): this was an inline set comprehension over `claim_ids` ONLY,
    so it could not see the singular `claim_id` string form -- the exact defect a
    2026-06-04 audit fixed in `_queued_retest_coverage` (see its docstring) and
    which was never propagated to this lane. Singular is the COMMON form, not an
    edge case: 7 of the 8 live queue entries on 2026-08-03 used it, including the
    one that exposed this -- V3-EXQ-887 carries `claim_id: "SD-014"` and no
    `claim_ids` at all, so "Confirm evidence: SD-014" kept rendering `ready` while
    its confirming experiment sat pending in the queue.

    Deliberately a thin wrapper over `_queued_retest_coverage` rather than a
    second reader of the same field pair: one parser, so the retest lane and the
    confirmer lane cannot drift apart again. Pinned by
    `ConfirmerAndRetestLanesAgreeTest`.
    """
    return set(_queued_retest_coverage(queue_items))


_SUBSTRATE_RESOLVED_STATUSES = {
    "implemented", "done", "complete", "validated", "retune_validated",
    "phase_1_implemented", "phase_2_implemented", "phase_3_implemented",
}
_SUBSTRATE_RESOLVED_PHASE_RE = re.compile(r"^phase_\d+_implemented$")

# Terminal tokens for the FM2 fix. A genuinely-DONE substrate often carries a
# rich free-text status (e.g. "amend_validated_v3_exq_614c_..." or
# "substrate_landed_..._subsumed_by_scaffolded_sd054_603f") that the literal
# resolved-set + phase regex above do NOT match, so the entry kept surfacing as
# an "implement this substrate" task. When such a status contains one of these
# tokens AND the entry is ready=True, treat it as resolved. Excludes any
# "*pending*" status (wants a downstream validation step).
_SUBSTRATE_TERMINAL_TOKENS = ("validated", "landed", "subsumed", "superseded", "closed")


def _status_resolved(value: str) -> bool:
    """True if a single status string indicates a done/validated substrate.

    Accepts the literal set above, the phase_N_implemented family, and any
    `implemented_*` suffix (e.g. `implemented_env_curriculum_amend`) -- but
    NOT `*_pending_*` (e.g. `substrate_landed_pending_validation`), which
    explicitly want a downstream validation step.
    """
    s = (value or "").strip().lower()
    if not s or "pending" in s:
        return False
    if s in _SUBSTRATE_RESOLVED_STATUSES:
        return True
    if s.startswith("implemented_"):
        return True
    if _SUBSTRATE_RESOLVED_PHASE_RE.match(s):
        return True
    return False


def _status_terminal(value: str) -> bool:
    """True if a status string carries a terminal/done marker.

    Used ONLY in combination with ready=True (see _substrate_resolved). This is
    the looser, token-substring cousin of _status_resolved that catches the rich
    free-text statuses the literal set misses (FM2: MECH-341, MECH-090). Excludes
    any "*pending*" status, which explicitly wants a downstream validation step.
    """
    s = (value or "").strip().lower()
    if not s or "pending" in s:
        return False
    return any(tok in s for tok in _SUBSTRATE_TERMINAL_TOKENS)


# --- FM3: build-landed-but-validation-pending (2026-08-03) --------------------
# Both matchers above hard-veto on the SUBSTRING "pending". That is correct for
# the RETEST-BLOCKER question they answer ("is this substrate finished enough
# that a retest of the claim it unblocks is meaningful?"), but it is wrong for
# the IMPLEMENT question ("should a /implement-substrate chip be spawned to
# BUILD this?"). `implemented_pending_validation` asserts the opposite of what
# the veto reads it as: the code has LANDED and only a downstream validation
# step is outstanding. It is the second-most-common non-empty status in
# substrate_queue.json (11 entries on 2026-08-03), so the veto mis-routes a
# whole class, not an edge case.
#
# The pending qualifier must name a downstream VERIFICATION step. A status like
# `partially_implemented_pending_consumer_wiring` names remaining BUILD work and
# must keep surfacing as implementable -- hence the explicit suffix allowlist
# plus the `partial` guard, rather than a bare "has an implemented token" test.
_PENDING_VALIDATION_RE = re.compile(
    r"pending_(validation|validations|verification|review|"
    r"governance_review|retest|evidence|experiment)\b"
)
_IMPLEMENTATION_COMPLETE_TOKENS = (
    "implemented", "landed", "subsumed", "superseded", "closed", "validated",
)


def _status_implementation_complete(value: str) -> bool:
    """True if the status asserts the BUILD has landed -- even when a downstream
    validation step is still outstanding.

    Superset of `_status_resolved` / `_status_terminal`: everything they call
    done is build-complete too. What this adds is the `*_pending_<verification>`
    family those two veto on a bare "pending" substring (FM3).

    NOT build-complete:
      * `pending_implementation` -- the build has not started.
      * `partially_implemented_pending_consumer_wiring` -- real build work
        remains; `partial` guard plus the suffix allowlist both reject it.
      * `candidate_v3_pending`, `blocked_pending_discrimination`,
        `parked_pending_env_entropy_precondition` -- the pending qualifier
        names something other than a verification step.
    """
    s = (value or "").strip().lower()
    if not s:
        return False
    if _status_resolved(s) or _status_terminal(s):
        return True
    if "partial" in s:
        return False
    if not _PENDING_VALIDATION_RE.search(s):
        return False
    return any(tok in s for tok in _IMPLEMENTATION_COMPLETE_TOKENS)


_LEADING_CLAIM_TOKEN_RE = re.compile(r"^\s*([A-Z]+-\d+[a-z]?)\b")


def _load_substrate_queue() -> list[dict]:
    if not SUBSTRATE_QUEUE.exists():
        return []
    try:
        sq = json.loads(SUBSTRATE_QUEUE.read_text(encoding="utf-8"))
    except Exception:
        return []
    return [it for it in (sq.get("queue") or []) if isinstance(it, dict)]


def _substrate_by_id() -> dict[str, dict]:
    """sd_id -> entry, indexed for O(1) lookup."""
    return {it["sd_id"]: it for it in _load_substrate_queue() if it.get("sd_id")}


def _substrate_resolved(entry: dict | None) -> bool:
    """True if a substrate_queue entry is genuinely DONE -- no longer a retest
    blocker and no longer implementable.

    `ready` is the AUTHORITY; the status string is only a hint. This is the
    FM1+FM2 fix for the old status-string-only matcher.

    NOT resolved (still a blocker, still implementable) whenever EITHER:
      * `ready is False` -- regardless of how 'done' the status string reads.
        Entries like ARC-046 (status='implemented', ready=False,
        depends_on_unresolved names goal-pipeline enrichment) or SD-049
        (status='phase_1_implemented', ready=False) were read as resolved off
        the status string alone, which dropped them as retest blockers and
        rendered their substrate_ceiling retests false-ready (FM1).
      * a non-empty `depends_on_unresolved` -- unresolved prerequisites remain,
        regardless of status.

    Only once ready is not False AND there are no unresolved deps does the status
    decide done-ness, via three signals (in order):
      1. an explicit `done`/`landed` boolean True (structured; preferred -- see
         the writeup note on the `ready` semantic overload),
      2. the legacy implemented / phase_N / validated resolved-set
         (_status_resolved), still consulting BOTH status fields so a custom
         `implementation_status` variant cannot shadow a `validated` status
         (MECH-302 regression, hash 994434ce5e5b, 2026-05-30),
      3. ready is True AND a terminal token (validated/landed/subsumed/
         superseded/closed) appears in either status field -- the FM2 fix for
         rich free-text done statuses (MECH-341, MECH-090) that (2) misses.
    """
    if not entry:
        return False
    if entry.get("ready") is False:
        return False
    if entry.get("depends_on_unresolved"):
        return False
    if entry.get("done") is True or entry.get("landed") is True:
        return True
    impl = entry.get("implementation_status") or ""
    status = entry.get("status") or ""
    if _status_resolved(impl) or _status_resolved(status):
        return True
    if entry.get("ready") is True and (_status_terminal(impl) or _status_terminal(status)):
        return True
    return False


def _substrate_implementation_complete(entry: dict | None) -> bool:
    """True if this substrate_queue entry's BUILD has landed -- so it must not
    be routed to /implement-substrate -- even if it is not yet `_substrate_
    resolved` (validation outstanding).

    Deliberately NARROWER in effect than `_substrate_resolved`: this suppresses
    the IMPLEMENT lane only. The entry keeps whatever retest-blocker semantics
    `_substrate_resolved` gives it, because "the code landed" and "the claim it
    unblocks is retestable" are different questions and only the first one is
    settled by an `implemented_pending_validation` status.

    `depends_on_unresolved` still wins: an entry with unresolved prerequisites
    stays in the lane so the substrate loop can surface it as `blocked` with a
    blocked_by descriptor, rather than vanishing silently.
    """
    if not entry:
        return False
    if entry.get("depends_on_unresolved"):
        return False
    impl = entry.get("implementation_status") or ""
    status = entry.get("status") or ""
    return _status_implementation_complete(impl) or _status_implementation_complete(status)


def _substrate_ready_items() -> list[dict]:
    out = []
    for item in _load_substrate_queue():
        if not item.get("ready"):
            continue
        if _substrate_resolved(item):
            continue
        if _substrate_implementation_complete(item):
            continue
        out.append(item)
    return out


# Statuses this file's classifiers recognise at all. Anything outside the union
# of them lands in the fail-open default -- `ready`, i.e. "go build it" -- which
# is why a stale or novel status string degrades SILENTLY into spawned
# /implement-substrate work rather than erroring. `_unclassified_ready_items`
# exists to make that default visible; see the FM3 note above.
def _unclassified_ready_items() -> list[dict]:
    """substrate_queue entries surfacing as implementable ONLY because no
    classifier recognised their status string.

    Advisory: the generator reports these on stderr and still emits them, since
    a genuinely-unbuilt entry with an unusual status must not be dropped. A
    LANDED entry appearing here means the status vocabulary has drifted and the
    matchers above need a new case.
    """
    out = []
    for item in _substrate_ready_items():
        impl = (item.get("implementation_status") or "").strip().lower()
        status = (item.get("status") or "").strip().lower()
        if not impl and not status:
            continue  # blank status is a recognised state, not drift
        recognised = any(
            fn(v)
            for v in (impl, status)
            for fn in (_status_resolved, _status_terminal, _status_implementation_complete)
        )
        if recognised:
            continue
        if any(
            v.startswith(("pending_", "candidate_", "proposed", "blocked_", "parked_"))
            for v in (impl, status)
            if v
        ):
            continue  # explicitly-not-built vocabulary, correctly ready
        out.append(item)
    return out


def _retest_blockers(
    claim_id: str, substrate_by_id: dict[str, dict]
) -> tuple[list[str], list[dict]]:
    """Compute blocked_by descriptors + structured substrate entries for a retest claim.

    Walks substrate_queue twice:
      1. Direct: entries whose unblocks_claims contains claim_id and are not resolved.
      2. Transitive: for each direct entry, parse leading-ID tokens from its
         depends_on_unresolved list. Skip resolved IDs silently; surface unresolved
         IDs (with sd_id link if a substrate entry exists) or free-text entries
         (when no leading ID can be extracted) as informational blockers.

    Returns (blocker_strings, structured_substrate_entries):
      - blocker_strings: human-readable list for the IGW item's blocked_by field.
      - structured_substrate_entries: substrate_queue dicts (with sd_id) that
        should be surfaced as their own "Implement substrate: SD-X" IGW items.
    """
    blocker_strs: list[str] = []
    structured: list[dict] = []
    seen_sd_ids: set[str] = set()

    direct = [
        e for e in substrate_by_id.values()
        if claim_id in (e.get("unblocks_claims") or []) and not _substrate_resolved(e)
    ]
    for entry in direct:
        sid = entry.get("sd_id") or ""
        status = entry.get("implementation_status") or entry.get("status") or "unknown"
        blocker_strs.append(f"{sid} [{status}]")
        if sid and sid not in seen_sd_ids:
            seen_sd_ids.add(sid)
            structured.append(entry)
        for dep_str in entry.get("depends_on_unresolved") or []:
            if not isinstance(dep_str, str) or not dep_str.strip():
                continue
            m = _LEADING_CLAIM_TOKEN_RE.match(dep_str)
            if m:
                dep_id = m.group(1)
                dep_entry = substrate_by_id.get(dep_id)
                if _substrate_resolved(dep_entry):
                    continue
                if dep_entry:
                    dep_status = (
                        dep_entry.get("implementation_status")
                        or dep_entry.get("status")
                        or "unknown"
                    )
                    blocker_strs.append(
                        f"{dep_id} [{dep_status}] (transitive via {sid})"
                    )
                    if dep_id not in seen_sd_ids:
                        seen_sd_ids.add(dep_id)
                        structured.append(dep_entry)
                else:
                    blocker_strs.append(
                        f"{dep_id} [no-substrate-entry] (transitive via {sid}): "
                        f"{dep_str[:120]}"
                    )
            else:
                blocker_strs.append(f"free-text (via {sid}): {dep_str[:160]}")
    return blocker_strs, structured


def _implement_substrate_blockers(
    entry: dict, substrate_by_id: dict[str, dict]
) -> list[str]:
    """Compute blocked_by descriptors for an /implement-substrate IGW item.

    Symmetric to _retest_blockers but rooted at the substrate entry itself
    rather than at a retest claim. Returns empty when the entry is ready
    (no ready=false + no unresolved depends_on_unresolved tokens). Returns
    non-empty when (a) ready=false (surfaces ready_blocked_by) OR (b)
    depends_on_unresolved contains leading-claim-tokens that resolve to
    substrate_queue entries still in a non-resolved status.

    Same depends_on_unresolved parsing convention as _retest_blockers:
    leading SD/ARC/MECH/Q token extracted via _LEADING_CLAIM_TOKEN_RE;
    resolved IDs skipped silently; no-leading-ID entries surfaced as
    free-text descriptors.
    """
    blockers: list[str] = []
    if entry.get("ready") is False:
        ready_blocked_by = entry.get("ready_blocked_by")
        if isinstance(ready_blocked_by, str) and ready_blocked_by.strip():
            blockers.append(f"ready_blocked_by: {ready_blocked_by[:200]}")
        else:
            blockers.append("ready=false (no ready_blocked_by detail)")
    for dep_str in entry.get("depends_on_unresolved") or []:
        if not isinstance(dep_str, str) or not dep_str.strip():
            continue
        m = _LEADING_CLAIM_TOKEN_RE.match(dep_str)
        if m:
            dep_id = m.group(1)
            dep_entry = substrate_by_id.get(dep_id)
            if _substrate_resolved(dep_entry):
                continue
            if dep_entry:
                dep_status = (
                    dep_entry.get("implementation_status")
                    or dep_entry.get("status")
                    or "unknown"
                )
                blockers.append(f"{dep_id} [{dep_status}]")
            else:
                blockers.append(
                    f"{dep_id} [no-substrate-entry]: {dep_str[:120]}"
                )
        else:
            blockers.append(f"free-text: {dep_str[:160]}")
    return blockers


def _proposed_experiments(
    claims_meta: dict[str, dict] | None = None,
    exp_evidence: set[str] | None = None,
) -> list[dict]:
    """`status: proposed` experiment proposals that are still actionable (FM4).

    The old version returned every proposed entry, surfacing stale proposals
    whose claim had moved on. We now skip a proposal when ANY of:
      * (R5, 2026-06-18) the claim is not v3-testable per _claim_v3_testable --
        the same predicate the R1 runtime backstop uses: v3_pending: true, an
        untestable epistemic_category, or a status outside {candidate,
        provisional}. This subsumes the old dead-status check and closes the
        v3_pending leak that surfaced MECH-270/271/337 as ready proposals.
      * its claim's claims.yaml status is resolved/superseded/deprecated
        (e.g. Q-035 EXP-0087 -- claim already resolved),
      * its claim's resolved epistemic_category is one that promote/demote (and
        therefore experiment proposals) are inappropriate for:
        substrate_coherence / substrate_ceiling / substrate_conditional /
        derivational / out_of_domain
        (e.g. ARC-063 EXP-0084 -- architectural_commitment -> substrate_coherence;
        MECH-312 EXP-0110 -- depends on unbuilt ARC-063 rule-creator substrate
        -> substrate_conditional),
      * the claim is scoped to V4+ only (implementation_phase v4/v5 or a v4+/v5
        version_relevance band with no v3 component -- _is_deferred_beyond_v3).
        We work V3 until it is finished, then reassess the roadmap before V4
        work; a V4-only proposal self-routes to a blocked_substrate STOP, so it
        is operator noise. This catches plain v4 claims that are NOT also
        substrate_conditional (e.g. MECH-362 / Q-057 happen to be both).
      * the claim already shows genuine experimental evidence in
        claim_evidence.v1.json (proposal effectively executed but not marked).
      * the claim_id is NOT registered in claims.yaml at all (a placeholder /
        proposed-but-unregistered id like MECH-CBBL-PROPOSED). You cannot queue
        a /queue-experiment run tagging a claim that does not exist; surfacing it
        as a ready experiment item is a pure false-positive. (FM5, 2026-06-10.)
      * the claim is substrate-blocked: some unresolved substrate_queue entry
        lists it in unblocks_claims (same _retest_blockers walk the retest lane
        uses). The retest lane already respects this; the proposal lane silently
        did not, so v3_pending claims whose substrate is built=false (e.g.
        MECH-316 / MECH-317, gated by ARC-064 ready=false + their own ready=false
        entries) surfaced as ready and self-routed to a blocked_substrate STOP on
        queue. This is the substrate-readiness gate, NOT a blanket v3_pending
        filter -- a v3_pending claim whose substrate_queue entry is ready=true
        (e.g. MECH-333 via test_bed_enrichment_crystallization_necessity) is
        correctly KEPT. (FM6, 2026-06-10.)

    Also deduplicates by proposal_id (the proposals file carries duplicate IDs --
    two EXP-0085, two EXP-0087, etc.), keeping the first occurrence.
    """
    if not PROPOSALS_JSON.exists():
        return []
    try:
        data = json.loads(PROPOSALS_JSON.read_text(encoding="utf-8"))
    except Exception:
        return []
    claims_meta = claims_meta if claims_meta is not None else _load_claims_meta()
    exp_evidence = exp_evidence if exp_evidence is not None else _claims_with_experimental_evidence()
    substrate_by_id = _substrate_by_id()
    out: list[dict] = []
    seen_ids: set[str] = set()
    for p in data.get("items") or []:
        if not isinstance(p, dict) or p.get("status") != "proposed":
            continue
        pid = str(p.get("proposal_id") or "")
        if pid and pid in seen_ids:
            continue
        if pid:
            seen_ids.add(pid)
        cid = str(p.get("claim_id") or "")
        if cid not in claims_meta:  # FM5: unregistered / placeholder claim id
            continue
        meta = claims_meta.get(cid) or {}
        # R5: the same testability predicate the R1 runtime backstop uses --
        # status in {candidate, provisional}, NOT v3_pending, epistemic_category
        # not in the untestable set. Subsumes the old _CLAIM_DEAD_STATUSES check
        # (candidate/provisional excludes resolved/superseded/deprecated) AND
        # closes the v3_pending leak that surfaced MECH-270/271/337 as ready
        # proposals (2026-06-18 audit). Mirrors igw_routine_tick.
        if not _claim_v3_testable(cid, claims_meta)[0]:
            continue
        # Proposal lane additionally suppresses substrate_coherence (foundational
        # design IS the substrate -- a SUPERSET of the R1 untestable set).
        if _resolve_epistemic_category(meta) in _EPI_SUPPRESS_PROPOSAL:
            continue
        if _is_deferred_beyond_v3(meta):
            continue
        if cid in exp_evidence:
            continue
        if _retest_blockers(cid, substrate_by_id)[0]:  # FM6: substrate-blocked
            continue
        out.append(p)
    return out[:15]


def _claim_lit_conf() -> dict[str, float]:
    """claim_id -> literature_confidence from claim_evidence.v1.json (0.0 if
    absent). Feeds the GOV-CONFIRM-1 confirmer lane's 'worth confirming' floor."""
    claims = _claim_evidence_claims()
    out: dict[str, float] = {}
    for cid, summary in claims.items():
        if not isinstance(summary, dict):
            continue
        try:
            out[str(cid)] = float(summary.get("literature_confidence") or 0.0)
        except (TypeError, ValueError):
            out[str(cid)] = 0.0
    return out


_SUBSTRATE_TAG_RE = re.compile(r"\b((?:MECH|ARC|SD|INV|Q|DEV-NEED)-\d+[A-Za-z]?)\b")


def _claims_implemented_in_substrate() -> set[str]:
    """Claim ids that appear (tagged) in ree-v3/ree_core source -- a deterministic
    proxy for 'the mechanism substrate is built', since REE modules cite their
    owning claim id in docstrings/comments. No structured claims.yaml field encodes
    this (`location` points at lit/architecture docs; `assembly_state` does not
    distinguish built from unbuilt), so a one-pass source scan is the honest gate.
    Returns the empty set if the ree_core tree is absent (keeps the confirmer lane
    inert off-box rather than crashing)."""
    if not REE_V3_CORE.exists():
        return set()
    ids: set[str] = set()
    for py in REE_V3_CORE.rglob("*.py"):
        try:
            text = py.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        ids |= set(_SUBSTRATE_TAG_RE.findall(text))
    return ids


def _evidence_confirmer_candidates(
    claims_meta: dict[str, dict],
    exp_evidence: set[str],
    substrate_by_id: dict[str, dict],
    queued_claim_ids: set[str] | None = None,
    adjudicated_by_claim: dict[str, dict] | None = None,
) -> list[dict]:
    """GOV-CONFIRM-1 (plan gov_confirm_1_plan.md): candidate/provisional claims
    that are confirmable-but-unconfirmed -- built substrate + thin/zero experimental
    evidence + lit_conf >= floor + NOT wall-bound/substrate-blocked + NOT V4+.

    The GENERATIVE-DISCOVERY complement to _proposed_experiments (which is
    consume-only -- it re-surfaces hand-authored proposals; nothing scans the
    registry to AUTHOR a confirmer). REUSES the same predicates the proposal /
    retest lanes use:
      * built-substrate gate: claim-id tagged in ree_core (_claims_implemented_in_substrate)
      * exp_evidence -- drop claims that already carry genuine experimental evidence
      * status in _TESTABLE_CLAIM_STATUSES (candidate / provisional)
      * _resolve_epistemic_category in _EPI_SUPPRESS_PROPOSAL -- drop
        governance_rule / substrate_coherence / substrate_ceiling / etc.
      * _is_deferred_beyond_v3 -- drop V4/V5-only
      * _retest_blockers -- drop substrate-blocked (the competence-wall gate)
      * lit_conf >= CONFIRMER_LIT_FLOOR -- worth confirming

    v3_pending RELAXATION (user decision 2026-07-14, gov_confirm_1_plan.md): unlike
    _claim_v3_testable (used by the proposal/retest lanes) this lane does NOT drop
    v3_pending claims. v3_pending means "held until V3 experiments provide evidence";
    a confirming experiment on ALREADY-BUILT substrate is precisely that evidence.
    The built-substrate gate (cid in `built`, applied first) is the safeguard: the
    relaxation only ever admits a v3_pending claim whose mechanism is already
    implemented -- for one still awaiting substrate, the built gate excludes it.

    DISCOVERY only. The judgement piece -- scoping a confirming DV that is buildable
    NOW (a representation-level / functional-signature readout, NOT a committed
    behaviour DV that the competence wall blocks) -- stays in the per-item
    /queue-experiment pass, which self-routes substrate_not_ready_requeue if only a
    behavioural DV exists. Sorted by lit_conf desc.

    FM10 -- MEMORY OF THAT SELF-ROUTE. A candidate whose backing proposal a prior
    session already adjudicated as not-queueable (`adjudicated_by_claim`, from
    `_confirmer_adjudicated_proposals`) is returned with an `adjudication` key
    rather than being dropped. The call site renders it `blocked` with the
    session's own reason in `blocked_by`, so:
      * the dispatcher never spends another worker re-deriving it (the defect:
        MECH-191 worked twice on 2026-08-03, both self-routing);
      * it is NOT muted -- the claim stays on /workset carrying the verdict, and
        re-enters the eligible set automatically when the status is cleared;
      * it consumes no CONFIRMER_AUTOSPAWN_CAP slot (the cap counts `ready`
        only), so a real confirmer takes the freed slot the same regeneration.
    Rendering `blocked` rather than dropping is the FM7 precedent from the retest
    lane, and is what makes including the broad `gated` status safe -- see
    _PROPOSAL_ADJUDICATED_NOT_QUEUEABLE_STATUSES for the v3_pending tension.
    """
    lit_conf = _claim_lit_conf()
    built = _claims_implemented_in_substrate()
    queued_claim_ids = queued_claim_ids or set()
    adjudicated_by_claim = adjudicated_by_claim or {}
    out: list[dict] = []
    for cid, meta in claims_meta.items():
        if cid not in built:  # built-substrate guard FIRST -- also gates the v3_pending relaxation
            continue
        if cid in exp_evidence:
            continue
        if cid in queued_claim_ids:  # a confirmer EXQ is already queued/running for this claim
            continue
        st = (meta.get("status") or "").strip().lower()
        if st not in _TESTABLE_CLAIM_STATUSES:
            continue
        if _resolve_epistemic_category(meta) in _EPI_SUPPRESS_PROPOSAL:
            continue
        if _is_deferred_beyond_v3(meta):
            continue
        if _retest_blockers(cid, substrate_by_id)[0]:
            continue
        lit = lit_conf.get(cid, 0.0)
        if lit < CONFIRMER_LIT_FLOOR:
            continue
        rec = {
            "claim_id": cid,
            "lit_conf": lit,
            "title": meta.get("title") or cid,
            "location": meta.get("location") or "",
        }
        # FM10: carry the prior adjudication through instead of dropping the
        # candidate; the call site turns it into a `blocked` item.
        adj = adjudicated_by_claim.get(cid)
        if adj:
            rec["adjudication"] = {
                "proposal_id": adj.get("proposal_id") or "?",
                "status": adj.get("status") or "?",
                "reason": _proposal_adjudication_reason(adj),
                "session": adj.get("gated_by_session") or "",
            }
        out.append(rec)
    out.sort(key=lambda d: (-d["lit_conf"], d["claim_id"]))
    return out


_EXQ_BASE_RE = re.compile(r"^(V3-EXQ-\d+)", re.IGNORECASE)


def _exq_successor_of(base: str, qid: str) -> bool:
    """True if qid is a lettered or rN suffix iteration of base (e.g. 008 -> 008r2, 008a)."""
    if not qid or qid.upper() == base.upper():
        return False
    q = qid.upper()
    b = base.upper()
    if not q.startswith(b):
        return False
    suffix = q[len(b) :]
    if not suffix:
        return False
    return bool(re.match(r"^[A-Z]+$", suffix)) or bool(re.match(r"^R\d+$", suffix))


# Patterns that carry a decisive PASS/FAIL signal inside result_summary when
# result='UNKNOWN'. Compensates for the runner's UNKNOWN-result silent-drop bug
# at ree-v3/experiment_runner.py:1394. Order does not matter -- first match wins.
# The verdict pattern requires PASS/FAIL as the next token so "verdict:
# INCONCLUSIVE" and "verdict: auroc=0.5000" do not match.
_OUTCOME_IN_SUMMARY_RES = [
    re.compile(r"\bOutcome:\s*(PASS|FAIL)\b", re.IGNORECASE),
    re.compile(r"=>\s*(PASS|FAIL)\b", re.IGNORECASE),
    re.compile(r"===\s*[A-Z0-9._-]+\s+(PASS|FAIL)\s*===", re.IGNORECASE),
    re.compile(r"\bExperiment:\s*(PASS|FAIL)\b", re.IGNORECASE),
    re.compile(r"\bverdict:\s*(PASS|FAIL)\b", re.IGNORECASE),
]

# Successors whose result is UNKNOWN (no decisive PASS/FAIL signal) still count
# as "completed" if they ran at least this many seconds without crashing. The
# floor excludes startup crashes (typically 1-30s) but admits any successor that
# meaningfully exercised the script. Long INCONCLUSIVE or numeric-verdict runs
# prove the runtime issue is fixed; the remaining scientific evaluation belongs
# in /governance or /failure-autopsy, not /diagnose-errors.
_MIN_SUCCESSOR_RUNTIME_SECS = 300


def _effective_result(entry: dict) -> str:
    """Return the entry's scientific result, recovering from UNKNOWN-result silent-drop."""
    res = (entry.get("result") or "").upper()
    if res in ("PASS", "FAIL", "ERROR"):
        return res
    summary = entry.get("result_summary") or ""
    for pat in _OUTCOME_IN_SUMMARY_RES:
        m = pat.search(summary)
        if m:
            return m.group(1).upper()
    return res


def _successor_counts_as_completed(entry: dict) -> bool:
    """A successor counts as completed if it shows the script is no longer broken.

    Two ways: (1) decisive PASS/FAIL via _effective_result, or (2) a non-ERROR
    run that lasted at least _MIN_SUCCESSOR_RUNTIME_SECS.
    """
    res = _effective_result(entry)
    if res in ("PASS", "FAIL"):
        return True
    if res == "ERROR":
        return False
    try:
        secs = float(entry.get("actual_secs") or 0)
    except (TypeError, ValueError):
        secs = 0.0
    return secs >= _MIN_SUCCESSOR_RUNTIME_SECS


def _has_completed_successor(qid: str, completed_by_qid: dict[str, dict]) -> bool:
    """True when a successor -- or a later non-ERROR self-run -- shows the script works.

    Suppresses 'Diagnose ERROR' IGW items in three cases:
      - A lettered or rN successor PASSed or FAILed decisively.
      - A lettered or rN successor ran without crashing for at least the
        runtime floor (proves runtime issue resolved even if science inconclusive).
      - The same qid later ran without ERROR (self-succession via re-queue).
    """
    self_entry = completed_by_qid.get(qid)
    if (
        self_entry is not None
        and (self_entry.get("result") or "").upper() != "ERROR"
        and _successor_counts_as_completed(self_entry)
    ):
        return True
    m = _EXQ_BASE_RE.match(str(qid))
    if not m:
        return False
    base = m.group(1)
    for other_qid, entry in completed_by_qid.items():
        if not _exq_successor_of(base, other_qid):
            continue
        if _successor_counts_as_completed(entry):
            return True
    return False


def _discussed_qids() -> set[str]:
    """Queue IDs already dispositioned via /diagnose-errors NO-OP closes
    (or any other manual review) -- recorded in review_tracker.json's
    `discussed_experiment_dirs`. Suppresses re-surfacing in the workset.
    """
    if not REVIEW_TRACKER.exists():
        return set()
    try:
        rt = json.loads(REVIEW_TRACKER.read_text(encoding="utf-8"))
    except Exception:
        return set()
    return {str(x) for x in (rt.get("discussed_experiment_dirs") or []) if x}


def _undiagnosed_errors(queue_items: list[dict]) -> list[dict]:
    queued_types = {
        (it.get("experiment_type") or "").lower()
        for it in queue_items
    }
    discussed_qids = _discussed_qids()
    errors: list[dict] = []
    paths = []
    if RUNNER_STATUS.exists():
        paths.append(RUNNER_STATUS)
    if RUNNER_STATUS_DIR.is_dir():
        paths.extend(sorted(RUNNER_STATUS_DIR.glob("*.json")))
    completed_by_qid: dict[str, dict] = {}
    for path in paths:
        try:
            st = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for entry in st.get("completed") or []:
            if not isinstance(entry, dict):
                continue
            qid = entry.get("queue_id") or ""
            if qid and qid not in completed_by_qid:
                completed_by_qid[qid] = entry
            elif qid and entry.get("result") != "ERROR":
                completed_by_qid[qid] = entry
    seen: set[str] = set()
    for path in paths:
        try:
            st = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for entry in st.get("completed") or []:
            if not isinstance(entry, dict):
                continue
            if entry.get("result") != "ERROR":
                continue
            qid = entry.get("queue_id") or ""
            # Non-EXQ queue ids (V3-ONBOARD-smoke-*, infra smokes, etc.)
            # have their own retry cadence and aren't appropriate for
            # /diagnose-errors. _EXQ_BASE_RE also cannot resolve their
            # successors, so without this skip they perpetually surface.
            if qid and not _EXQ_BASE_RE.match(qid):
                continue
            # ERRORs dispositioned via /diagnose-errors NO-OP closes leave a
            # trail in review_tracker.json's discussed_experiment_dirs.
            # Suppress here so they don't perpetually re-surface as chips
            # after the work has already been done.
            if qid and qid in discussed_qids:
                continue
            et = (entry.get("experiment_type") or "").lower()
            key = qid or et
            if key in seen:
                continue
            seen.add(key)
            if et in queued_types:
                continue
            if qid and _has_completed_successor(qid, completed_by_qid):
                continue
            errors.append(entry)
    return errors[:20]


def _extract_claim_tokens(*parts: str | list | None) -> set[str]:
    out: set[str] = set()
    for part in parts:
        if part is None:
            continue
        if isinstance(part, list):
            for x in part:
                if x is not None:
                    for m in _CLAIM_TOKEN_RE.finditer(str(x)):
                        out.add(m.group(0).upper())
            continue
        for m in _CLAIM_TOKEN_RE.finditer(str(part)):
            out.add(m.group(0).upper())
    return out


_GENERATION_RE = re.compile(r"^v(\d+)$", re.IGNORECASE)
# Node-level generation hint from free text (node titles/notes). Matches a
# standalone Vn generation token (V4, V5, "V5-only") but NOT an experiment id
# like "V3-EXQ-603" -- the negative lookahead drops the EXQ case so a node that
# merely references a V3 experiment is not mislabeled.
_NODE_VERSION_HINT_RE = re.compile(r"(?<![A-Za-z0-9])[Vv]([3-9])\b(?!-EXQ)")


def _norm_generation(val, plan_id: str | None = None) -> str:
    """Normalize a plan's generation bucket.

    Authoritative source is the plan frontmatter's `closure_plan.generation`
    field. An explicit value is preserved -- 'v4'/'v5'/... normalize to 'vN',
    and non-numeric buckets like 'meta' (cross-cutting roadmaps) are kept
    verbatim (lowercased) rather than coerced to a version. With no explicit
    generation, falls back to a trailing `_vN` suffix on the plan id, then
    defaults to 'v3' (plans without a generation are V3-era active substrate).
    """
    if val is not None and str(val).strip():
        s = str(val).strip().lower()
        m = _GENERATION_RE.match(s)
        return ("v" + m.group(1)) if m else s
    if plan_id:
        m = re.search(r"_v(\d+)$", str(plan_id))
        if m:
            return "v" + m.group(1)
    return "v3"


def _node_version_hint(*texts) -> str | None:
    """Return a 'vN' generation hint parsed from node free text, or None.

    Used for plan nodes (e.g. in a `generation: meta` cross-cutting roadmap)
    that declare their target generation only in the title/note, such as
    "Minimal 2-agent world (... currently V5-only)".
    """
    for t in texts:
        if not t:
            continue
        m = _NODE_VERSION_HINT_RE.search(str(t))
        if m:
            return "v" + m.group(1)
    return None


def _load_plan_registry() -> dict[str, dict]:
    """plan_id -> {title, scope_claims, generation} from *_plan.md frontmatter."""
    reg: dict[str, dict] = {}
    if not PLANNING.exists():
        return reg
    for path in sorted(PLANNING.glob("*_plan.md")):
        plan = _parse_plan_frontmatter(path)
        if not plan:
            continue
        plan_id = str(plan.get("id") or path.stem.replace("_plan", ""))
        scope = []
        for c in plan.get("scope_claims") or []:
            for m in _CLAIM_TOKEN_RE.finditer(str(c)):
                scope.append(m.group(0).upper())
        reg[plan_id] = {
            "title": str(plan.get("title") or plan_id.replace("_", " ").title()),
            "scope_claims": sorted(set(scope)),
            "generation": _norm_generation(plan.get("generation"), plan_id),
        }
    return reg


def _lens_token_sets(plan_reg: dict[str, dict]) -> dict[str, set[str]]:
    """lens_id -> expanded claim/gap tokens for matching."""
    out: dict[str, set[str]] = {}
    for lid, spec in OUTCOME_LENSES.items():
        tokens = _extract_claim_tokens(spec.get("anchor_claims") or [])
        for pid in spec.get("plan_ids") or []:
            pinfo = plan_reg.get(str(pid)) or {}
            tokens |= set(pinfo.get("scope_claims") or [])
            tokens.add(str(pid).upper())
        out[lid] = tokens
    return out


def _item_match_tokens(item: dict) -> set[str]:
    tokens = _extract_claim_tokens(
        item.get("claim_ids"),
        item.get("unblocks"),
        item.get("title"),
        item.get("why_now"),
    )
    for gid in item.get("gap_ids") or []:
        tokens |= _extract_claim_tokens(str(gid))
        if ":" in str(gid):
            tokens.add(str(gid).split(":", 1)[0].upper())
    if item.get("plan_id"):
        tokens.add(str(item["plan_id"]).upper())
    return tokens


def _matched_lenses(item: dict, lens_tokens: dict[str, set[str]]) -> list[str]:
    itoks = _item_match_tokens(item)
    hits = []
    for lid, ltoks in lens_tokens.items():
        if itoks & ltoks:
            hits.append(lid)
    return sorted(hits)


def _enrich_workset_items(items: list[dict], plan_reg: dict[str, dict]) -> tuple[dict, dict]:
    lens_tokens = _lens_token_sets(plan_reg)
    by_plan: dict[str, list[str]] = {}
    lens_counts: dict[str, int] = {lid: 0 for lid in OUTCOME_LENSES}

    for it in items:
        unblocks = it.get("unblocks") or []
        it["unblock_count"] = len(unblocks)
        pid = it.get("plan_id")
        if pid:
            pinfo = plan_reg.get(str(pid)) or {}
            it["plan_title"] = pinfo.get("title") or str(pid).replace("_", " ").title()
            # Generation follows the owning plan (V4/V5/V6 roadmaps carry an
            # explicit numeric `generation`; V3-era plans have none -> "v3").
            # ONLY for a non-numeric roadmap bucket (e.g. `generation: meta` /
            # `process` cross-cutting plans whose nodes each target a different
            # generation) do we defer to a per-node title hint like "... V5-only".
            # A plan with a real vN generation is single-generation, so an
            # incidental version mention in a node title (usually a V3
            # prerequisite) must NOT override the plan's own bucket.
            plan_gen = pinfo.get("generation") or "v3"
            if _GENERATION_RE.match(plan_gen):
                it["version"] = plan_gen
            else:
                it["version"] = _node_version_hint(it.get("title")) or plan_gen
            by_plan.setdefault(str(pid), []).append(it["id"])
        else:
            # Non-plan lanes (governance / experiment / substrate / ops) are all
            # current-cycle work against the active V3 substrate.
            it["version"] = "v3"
        matched = _matched_lenses(it, lens_tokens)
        it["matched_lenses"] = matched
        for lid in matched:
            lens_counts[lid] = lens_counts.get(lid, 0) + 1

    lenses_meta = {
        lid: {
            "label": spec["label"],
            "item_count": lens_counts.get(lid, 0),
            "plan_ids": list(spec.get("plan_ids") or []),
        }
        for lid, spec in OUTCOME_LENSES.items()
    }
    indexes = {"by_plan": {k: sorted(v) for k, v in sorted(by_plan.items())}}
    return lenses_meta, indexes


def _plan_gap_items() -> list[dict]:
    nodes: list[dict] = []
    if not PLANNING.exists():
        return nodes
    for path in sorted(PLANNING.glob("*_plan.md")):
        plan = _parse_plan_frontmatter(path)
        if not plan:
            continue
        plan_id = str(plan.get("id") or path.stem.replace("_plan", ""))
        for n in plan.get("nodes") or []:
            if not isinstance(n, dict):
                continue
            nid = str(n.get("id") or "")
            if not nid:
                continue
            status = _normalize_status(n.get("status"))
            if status in ("done", "deferred", "deferred_v4"):
                continue
            nodes.append({
                "gap_id": nid,
                "plan_id": plan_id,
                "plan_file": path.name,
                "title": n.get("title") or nid,
                "status": status,
                "severity": n.get("severity") or "medium",
                "owner_exq": n.get("owner_exq"),
                "depends_on": list(n.get("depends_on") or []),
                "unblocks_claims": list(n.get("unblocks_claims") or []),
                "resume_condition": n.get("resume_condition"),
            })
    return nodes


def _gap_blocked_by(gap: dict, by_id: dict[str, dict]) -> list[str]:
    blockers = []
    for dep in gap.get("depends_on") or []:
        dep_n = by_id.get(str(dep))
        if dep_n and dep_n["status"] not in ("done", "deferred", "deferred_v4"):
            blockers.append(f"{dep} [{dep_n['status']}]")
    return blockers


def _infer_lane(gap: dict, live: dict[str, str]) -> tuple[str, str, str]:
    owner = str(gap.get("owner_exq") or "")
    exq_m = _EXQ_RE.search(owner)
    exq = re.sub(r"^v3-exq", "V3-EXQ", exq_m.group(0), count=1, flags=re.IGNORECASE) if exq_m else None
    if exq and exq in live:
        return "monitor", _LANE_SKILLS["monitor"], "in_flight"
    if exq:
        return "experiment", _LANE_SKILLS["experiment"], gap["status"]
    if gap["status"] == "blocked":
        return "plan", _LANE_SKILLS["plan"], "blocked"
    if gap["status"] in ("open", "in_progress", "partial"):
        return "plan", _LANE_SKILLS["plan"], "ready" if gap["status"] == "open" else gap["status"]
    return "plan", _LANE_SKILLS["plan"], gap["status"]


def _priority_score(item: dict) -> int:
    sev = item.get("severity") or ""
    status = item.get("status") or ""
    lane = item.get("lane") or ""
    base = 50
    if lane == "governance":
        base = 5
    if sev == "load-bearing":
        base -= 20
    elif sev == "high":
        base -= 10
    if status == "ready":
        base -= 5
    if status == "in_flight":
        base += 3
    if status == "blocked":
        base += 8
    return base


def _make_brief(item: dict) -> str:
    lines = [
        f"REE inter-governance work item: {item['id']}",
        f"Title: {item['title']}",
        f"Lane: {item['lane']} | Skill: {item['skill']}",
        f"Status: {item['status']}",
    ]
    if item.get("gap_ids"):
        lines.append(f"Gap(s): {', '.join(item['gap_ids'])}")
    if item.get("owner_exq"):
        lines.append(f"Owner EXQ: {item['owner_exq']}")
    if item.get("claim_ids"):
        lines.append(f"Claims: {', '.join(item['claim_ids'])}")
    if item.get("owner_backlog_id"):
        lines.append(f"Proposal backlog id (stable): {item['owner_backlog_id']}")
    if item.get("blocked_by"):
        lines.append(f"Blocked by: {'; '.join(item['blocked_by'])}")
    lines.append(f"Why now: {item.get('why_now', '')}")
    lines.append("")
    lines.append("Instructions:")
    if item["skill"] == "/governance":
        lines.append("- Run /governance from REE_assembly; walk pending_review with user.")
    elif item["skill"] == "/queue-experiment":
        lines.append("- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.")
        lines.append("- Design the experiment for the Claims id above (the stable target). To read the"
                     " backing proposal, look it up by claim_id in experiment_proposals.v1.json -- the"
                     " auto EXP-#### proposal_ids (>= EXP-0177) are ephemeral and renumber every"
                     " governance cycle, so do NOT trust an EXP-#### number frozen in any older brief.")
    elif item["skill"] == "/implement-substrate":
        lines.append("- Use /implement-substrate for the SD/MECH named in title.")
    elif item["skill"] == "/lit-pull":
        lines.append("- Use /lit-pull for the claim cluster named.")
    elif item["skill"] == "/diagnose-errors":
        lines.append("- Use /diagnose-errors; re-queue via lettered EXQ if code fix needed.")
    elif item["skill"] == "(monitor -- do not re-queue)":
        lines.append("- Monitor runner/machines. Do NOT re-queue same EXQ ID. On finish: /governance + plan reconcile.")
    else:
        lines.append("- Update plan-of-record doc and closure frontmatter when complete.")
    if item.get("plan_file"):
        lines.append(f"- Plan doc: REE_assembly/evidence/planning/{item['plan_file']}")
    lines.append(f"- Workset: http://localhost:8000/workset")
    if item.get("closure_links"):
        for link in item["closure_links"]:
            lines.append(f"- Closure: http://localhost:8000{link}")
    return "\n".join(lines)


def reconcile_spawned_task_assignments(
    items: list[dict], *, now_iso: str | None = None
) -> list[str]:
    """Auto-release spawned_task assignments whose item is no longer `ready`.

    End-of-skill spawn_task chips are mirrored into igw_assignments.json under
    agent kind "spawned_task" (scripts/igw_chip_assign.py). That mirror is only
    released manually today (dismiss_task -> igw_chip_assign.py release). When the
    chipped work actually LANDS -- the claim gains experimental evidence, a
    proposal is marked executed, a substrate entry resolves, or a queued retest
    auto-absorbs the item -- the underlying workset item drops out of the `ready`
    set, but the spawned_task assignment lingers as active. A stale active mirror
    (a) keeps the IGW auto-spawn routine skipping the item forever (its
    eligibility gate skips items with any active assignment) and (b) shows a stale
    "assigned" chip on /workset + /igw.

    This reconcile closes that gap: for every ACTIVE spawned_task assignment,
    release it (released_by=reconcile, reason=work_landed_or_item_gone) unless its
    stable_hash still matches a `ready` item in the freshly-built workset.

    Idempotent: igw_assignments_lib.release() is a no-op (returns None) when no
    active assignment exists for the (stable_hash, spawned_task, agent_label) key,
    so re-running over the same workset releases nothing new. ASCII-only.

    `items` must already carry a "stable_hash" field (build_workset sets it before
    calling this). Returns the list of stable_hashes released this pass.
    """
    try:
        import igw_assignments_lib as ial
    except ImportError:
        return []
    ready_hashes = {
        it.get("stable_hash")
        for it in items
        if it.get("status") == "ready" and it.get("stable_hash")
    }
    released: list[str] = []
    # Snapshot once; release() re-reads the ledger per call, so iterating this
    # captured list stays correct as the file mutates underneath us.
    for ent in ial.active_entries():
        if ent.get("agent") != "spawned_task":
            continue
        sh = ent.get("stable_hash")
        if not sh or sh in ready_hashes:
            continue
        result = ial.release(
            sh,
            agent="spawned_task",
            agent_label=ent.get("agent_label"),
            released_by="reconcile",
            reason="work_landed_or_item_gone",
            now_iso=now_iso,
        )
        if result is not None:
            released.append(sh)
    return released


def build_workset() -> dict:
    generated = _utc_now()
    items: list[dict] = []
    seq = 0
    live = _running_exqs()
    # Keep both raw snapshots so the summary can report which one the merged
    # queue actually came from -- a silently-stale sibling checkout (FM8) is
    # otherwise invisible in the generated artifact, which is the only thing the
    # metaworker dispatcher ever reads.
    queue_worktree = _queue_from_worktree()
    queue_committed = _queue_from_git()
    queue_items = (
        queue_worktree if queue_committed is None
        else _merge_queue_snapshots(queue_worktree, queue_committed)
    )
    gap_nodes = _plan_gap_items()
    gaps_by_id = {g["gap_id"]: g for g in gap_nodes}

    def add(**kwargs) -> None:
        nonlocal seq
        seq += 1
        iid = kwargs.pop("id", None) or f"IGW-{generated[:10].replace('-', '')}-{seq:03d}"
        kwargs.setdefault("generated_at", generated)
        kwargs["id"] = iid
        if "agent_brief" not in kwargs:
            kwargs["agent_brief"] = _make_brief(kwargs)
        if kwargs.get("gap_ids"):
            kwargs["closure_links"] = [
                f"/closure?highlight={urlquote(g)}"
                for g in kwargs["gap_ids"]
            ]
        items.append(kwargs)

    pr = _pending_review_count()
    if pr > 0:
        add(
            lane="governance",
            skill="/governance",
            status="ready",
            priority=1,
            severity="load-bearing",
            title=f"Complete governance review ({pr} pending)",
            why_now=f"pending_review.md lists {pr} item(s) -- must clear before new work packages.",
            gap_ids=[],
            claim_ids=[],
            owner_exq=None,
            blocked_by=[],
            unblocks=[],
        )

    for rec in _pending_governance_recs()[:12]:
        verdict = (rec.get("recommendation") or "").strip().lower()
        if verdict in _HELD_PENDING_RECS:
            # The verdict IS the decision (hold). Reframe as a blocked/held
            # substrate item instead of a ready governance decision.
            blocker = _HELD_PENDING_RECS[verdict]
            held_v4 = verdict == "held_v4_by_architectural_commitment"
            if held_v4:
                why = (f"promotion_demotion verdict is `{verdict}` -- this claim is "
                       f"deliberately V4-deferred by architectural commitment, not a "
                       f"decision to make in /governance. No V3 action.")
            else:
                why = (f"promotion_demotion verdict is `{verdict}` -- governance is "
                       f"HELD pending substrate, not a decision to make in /governance. "
                       f"Unblocks when the substrate lands AND a per-claim retest "
                       f"supplies V3 evidence.")
            add(
                lane="substrate",
                skill="/implement-substrate",
                status="blocked",
                priority=60,
                severity="low",
                title=f"Held pending substrate: {rec['claim_id']}",
                why_now=why,
                gap_ids=[],
                claim_ids=[rec["claim_id"]],
                owner_exq=None,
                blocked_by=[blocker],
                unblocks=[rec["claim_id"]],
            )
            continue
        add(
            lane="governance",
            skill="/governance",
            status="ready",
            priority=8,
            severity="high",
            title=f"Governance decision: {rec['claim_id']}",
            why_now=f"promotion_demotion recommends {rec.get('recommendation', 'pending_user')}.",
            gap_ids=[],
            claim_ids=[rec["claim_id"]],
            owner_exq=None,
            blocked_by=[],
            unblocks=[rec["claim_id"]],
        )

    for gap in gap_nodes:
        blockers = _gap_blocked_by(gap, gaps_by_id)
        lane, skill, wstatus = _infer_lane(gap, live)
        if blockers and wstatus == "ready":
            wstatus = "blocked"
        owner = gap.get("owner_exq")
        if isinstance(owner, str) and owner.lower() in ("null", "tbd", ""):
            owner = None
        add(
            lane=lane if lane != "monitor" else "experiment",
            skill=skill,
            status=wstatus,
            priority=_priority_score({**gap, "lane": lane, "status": wstatus}),
            severity=gap.get("severity"),
            title=gap["title"][:120],
            why_now=(str(gap.get("resume_condition") or "")[:240] or f"Plan gap {gap['status']} on {gap['plan_id']}."),
            gap_ids=[gap["gap_id"]],
            plan_id=gap["plan_id"],
            plan_file=gap["plan_file"],
            claim_ids=gap.get("unblocks_claims") or [],
            owner_exq=owner,
            blocked_by=blockers,
            unblocks=gap.get("unblocks_claims") or [],
        )

    # Track which substrate sd_ids have been emitted as IGW items so we don't
    # double-emit. Both the "Substrate ready" loop below and the retest-blocker
    # synthesis loop further down feed this set.
    emitted_substrate_sd_ids: set[str] = set()
    substrate_by_id = _substrate_by_id()

    for sq in _substrate_ready_items()[:8]:
        sd = sq.get("sd_id") or "?"
        if sd in emitted_substrate_sd_ids:
            continue
        emitted_substrate_sd_ids.add(sd)
        # Defensive: _substrate_ready_items already filters ready=true, so
        # blockers here should normally be empty. A non-empty list means the
        # substrate_queue entry is internally inconsistent (ready=true but
        # depends_on_unresolved still names a non-resolved substrate); surface
        # as blocked rather than papering over the inconsistency.
        blockers = _implement_substrate_blockers(sq, substrate_by_id)
        status = "blocked" if blockers else "ready"
        if status == "ready":
            title = f"Substrate ready: {sd}"
            why_now = sq.get("implementation_hint", "substrate_queue ready=true")[:200]
        else:
            title = f"Substrate (blocked): {sd}"
            why_now = (
                f"substrate_queue ready=true but {len(blockers)} unresolved "
                f"prerequisite(s) -- see blocked_by."
            )[:240]
        add(
            lane="substrate",
            skill="/implement-substrate",
            status=status,
            priority=25,
            severity="high",
            title=title,
            why_now=why_now,
            gap_ids=[],
            claim_ids=list(sq.get("unblocks_claims") or [])[:6],
            owner_exq=None,
            blocked_by=blockers,
            unblocks=list(sq.get("unblocks_claims") or [])[:6],
        )

    pending_q = [it for it in queue_items if it.get("status") == "pending" and not it.get("claimed_by")]
    if len(pending_q) < 3:
        add(
            lane="ops",
            skill="(manual)",
            status="ready",
            priority=35,
            severity="medium",
            title=f"Queue depth low ({len(pending_q)} pending)",
            why_now="Fewer than 3 unclaimed queue items -- consider /queue-experiment for ready plan gaps.",
            gap_ids=[],
            claim_ids=[],
            owner_exq=None,
            blocked_by=[],
            unblocks=[],
        )

    for err in _undiagnosed_errors(queue_items):
        qid = err.get("queue_id") or "?"
        add(
            lane="experiment",
            skill="/diagnose-errors",
            status="ready",
            priority=30,
            severity="medium",
            title=f"Diagnose ERROR: {qid}",
            why_now=f"Runner ERROR with no queued successor ({err.get('experiment_type', '')}).",
            gap_ids=[],
            claim_ids=[],
            owner_exq=qid if _EXQ_RE.match(str(qid)) else None,
            blocked_by=[],
            unblocks=[],
        )

    claims_meta = _load_claims_meta()
    exp_evidence = _claims_with_experimental_evidence()
    proposal_blocked_by_claim = _proposal_blocked_substrate_by_claim()
    retest_all = sorted(_claim_retest_ids())
    queued_coverage = _queued_retest_coverage(queue_items)
    auto_absorbed_retests: dict[str, str] = {
        cid: queued_coverage[cid] for cid in retest_all if cid in queued_coverage
    }
    retest = [cid for cid in retest_all if cid not in queued_coverage]
    for cid in retest[:10]:
        blocker_strs, structured_blockers = _retest_blockers(cid, substrate_by_id)
        # FM5: a substrate_ceiling retest is genuinely awaiting substrate
        # enrichment. It may render ready ONLY when its unblocking substrate is
        # actually ready/landed (which fix 1 surfaces as an empty blocker list).
        # If NO substrate_queue entry even targets the claim, we cannot confirm
        # the enrichment landed, so keep it blocked rather than false-ready.
        is_ceiling = _resolve_epistemic_category(claims_meta.get(cid)) == "substrate_ceiling"
        if is_ceiling and not blocker_strs:
            unblocking = [
                e for e in substrate_by_id.values()
                if cid in (e.get("unblocks_claims") or [])
            ]
            if not unblocking:
                blocker_strs = [
                    f"substrate_ceiling -- awaiting substrate enrichment "
                    f"(no ready substrate_queue entry targets {cid})"
                ]
        # R5: hold a non-v3-testable retest target -- v3_pending, an untestable
        # epistemic_category (substrate_ceiling / substrate_conditional /
        # out_of_domain / derivational), or a non-candidate status. The
        # governance V3-pending gate ignores such claims, so a headless
        # /queue-experiment is a structural NO-OP. Keep it visible as `blocked`
        # rather than `ready` (mirrors R1 in igw_routine_tick). A
        # substrate_ceiling claim WITHOUT a ready substrate already carries the
        # "awaiting enrichment" blocker set above; only add a reason when none
        # exists yet (e.g. INV-074: substrate_ceiling WITH a ready substrate
        # entry, which previously rendered `ready`).
        testable, untest_reason = _claim_v3_testable(cid, claims_meta)
        held_not_testable = not testable and not blocker_strs
        if held_not_testable:
            blocker_strs = [f"not v3-testable: {untest_reason}"]
        # FM7: a prior /queue-experiment investigation may have already
        # adjudicated this retest's backing proposal as blocked on OTHER
        # CLAIMS (not a substrate_queue row), which _retest_blockers and the
        # epistemic_category ceiling check above cannot see -- see
        # _proposal_blocked_substrate_by_claim() docstring (confirmed
        # incident: INV-089). Only fires when nothing above already blocked
        # the item; if it did, that finding is already correctly `blocked`.
        proposal_block = proposal_blocked_by_claim.get(cid)
        held_proposal_blocked = bool(proposal_block) and not blocker_strs
        if held_proposal_blocked:
            pid = proposal_block.get("proposal_id") or "?"
            blocked_by_list = proposal_block.get("blocked_by") or []
            note = proposal_block.get("blocked_note") or ""
            if blocked_by_list:
                detail = ", ".join(str(x) for x in blocked_by_list)[:160]
                blocker_strs = [
                    f"experiment_proposals.v1.json {pid} status=blocked_substrate: "
                    f"blocked by {detail}"
                ]
            elif note:
                blocker_strs = [
                    f"experiment_proposals.v1.json {pid} status=blocked_substrate: "
                    f"{note[:160]}"
                ]
            else:
                blocker_strs = [
                    f"experiment_proposals.v1.json {pid} status=blocked_substrate "
                    f"(backlog_id {proposal_block.get('backlog_id') or '?'}); see "
                    f"the proposal record for adjudication detail."
                ]
        status = "blocked" if blocker_strs else "ready"
        if status == "ready":
            why_now = "claims.yaml pending_retest_after_substrate=true."
        elif held_proposal_blocked:
            why_now = (
                f"A prior investigation already adjudicated the backing "
                f"proposal as blocked_substrate -- see blocked_by. Do not "
                f"re-investigate; re-run /queue-experiment once the named "
                f"blocker(s) are built."
            )
        elif held_not_testable:
            why_now = (
                f"Held by the governance V3-pending gate ({untest_reason}) -- a "
                f"/queue-experiment cannot yield contributory evidence. See "
                f"blocked_by. (R5; mirrors R1.)"
            )
        elif is_ceiling:
            why_now = (
                f"substrate_ceiling -- awaiting substrate enrichment; blocked by "
                f"{len(blocker_strs)} unresolved prerequisite(s). See blocked_by."
            )
        else:
            why_now = (
                f"Blocked by {len(blocker_strs)} unresolved substrate "
                f"prerequisite(s) -- see blocked_by."
            )
        add(
            lane="experiment",
            skill="/queue-experiment",
            status=status,
            priority=28,
            severity="medium",
            title=f"Retest after substrate: {cid}",
            why_now=why_now,
            gap_ids=[],
            claim_ids=[cid],
            owner_exq=None,
            blocked_by=blocker_strs,
            unblocks=[cid],
        )
        # Surface each structured (sd_id-bearing) blocker as its own
        # "Implement substrate" IGW so the prerequisite work appears in the
        # workset alongside the blocked retest. Idempotent via
        # emitted_substrate_sd_ids: never double-emits a substrate already
        # added by the "Substrate ready" loop above.
        for entry in structured_blockers:
            sid = entry.get("sd_id") or ""
            if not sid or sid in emitted_substrate_sd_ids:
                continue
            emitted_substrate_sd_ids.add(sid)
            entry_status = (
                entry.get("implementation_status")
                or entry.get("status")
                or "unknown"
            )
            # Symmetric prereq-detection: an implement-substrate item is
            # ready only when its own substrate_queue entry is ready=true
            # AND its depends_on_unresolved is empty or fully resolved.
            # Without this check the synthesis loop emitted items as ready
            # even when the substrate_queue itself declared the work
            # blocked -- see IGW-20260529-033 (ARC-046) for the incident.
            sub_blockers = _implement_substrate_blockers(entry, substrate_by_id)
            sub_status = "blocked" if sub_blockers else "ready"
            if sub_status == "ready":
                why_now = (
                    f"substrate_queue entry status={entry_status}; "
                    f"unblocks retest of {cid} "
                    f"(pending_retest_after_substrate)."
                )[:240]
            else:
                why_now = (
                    f"substrate_queue entry status={entry_status} with "
                    f"{len(sub_blockers)} unresolved prerequisite(s); "
                    f"blocks retest of {cid}. See blocked_by."
                )[:240]
            add(
                lane="substrate",
                skill="/implement-substrate",
                status=sub_status,
                priority=20,
                severity="high",
                title=f"Implement substrate: {sid} (unblocks {cid})",
                why_now=why_now,
                gap_ids=[],
                claim_ids=list(entry.get("unblocks_claims") or [])[:6],
                owner_exq=None,
                blocked_by=sub_blockers,
                unblocks=list(entry.get("unblocks_claims") or [])[:6],
            )

    for prop in _proposed_experiments(claims_meta, exp_evidence)[:5]:
        pid = prop.get("proposal_id") or ""
        bid = prop.get("backlog_id") or ""
        cid = prop.get("claim_id") or ""
        # IMPORTANT: do NOT bake the auto-generated EXP-#### proposal_id into the
        # title or any other frozen artifact. Auto proposal_ids (EXP-#### above
        # the ~EXP-0176 manual ceiling) are positional/ephemeral -- the indexer
        # (build_experiment_indexes.py:_alloc_proposal_idx) re-mints them every
        # governance cycle. The IGW ledger freezes the item title when a
        # /queue-experiment item is STAGED, and that item waits 1-3 days for a
        # human launch; in that window governance renumbers the EXP ids, so a
        # frozen "Proposal EXP-0199 (ARC-050)" would resolve to a DIFFERENT
        # claim's proposal at launch (the 2026-06-21 IGW EXP<->claim mismatch).
        # The claim_id is the stable key; title is claim-keyed. The current
        # proposal_id is kept in owner_proposal_id (regenerated each tick, never
        # the frozen source of truth) and the launch path re-resolves it fresh.
        lane, skill = _proposal_lane_skill(prop.get("proposal_type"))
        add(
            lane=lane,
            skill=skill,
            status="ready",
            priority=40,
            severity="medium",
            title=_proposal_title(lane, cid),
            why_now="; ".join(prop.get("why_now") or [])[:200] or "experiment_proposals status=proposed",
            gap_ids=[],
            claim_ids=[cid] if cid else [],
            owner_exq=None,
            owner_backlog_id=bid,
            owner_proposal_id=pid,
            blocked_by=[],
            unblocks=[cid] if cid else [],
        )

    # GOV-CONFIRM-1 evidence-confirmer lane (plan gov_confirm_1_plan.md). Generative
    # complement to the proposals lane above: surface confirmable-but-unconfirmed
    # candidate claims (built substrate + thin evidence) so their confirming
    # experiments get discovered without a hand-authored proposal. P1 (surface-only):
    # status "surfaced" -- rendered on /workset but NOT `ready`, so the external
    # auto-spawn routine and check_workset_drift both skip it. P2 flips
    # CONFIRMER_AUTOSPAWN_ENABLED to emit "ready" (autospawn-eligible) at low priority.
    conf_status = "ready" if CONFIRMER_AUTOSPAWN_ENABLED else "surfaced"
    # Exclude claims that already have a confirmer EXQ in the queue (anti-double-spawn).
    confirmer_queued_claims = _confirmer_queued_claims(queue_items)
    # Cap generous (40): confirmers are LOW-priority background fill, so showing the full
    # confirmable-but-unconfirmed backlog is honest; the ceiling only guards a pathological
    # flood. Concurrency (how many are autospawn-eligible `ready` at once) is capped
    # separately below, post-assignment-merge, at CONFIRMER_AUTOSPAWN_CAP.
    # FM10: claims whose backing proposal a prior session already adjudicated as
    # not-queueable render `blocked` (with that session's reason) instead of
    # `ready`, so the dispatcher stops re-spending workers on a settled negative.
    confirmer_adjudicated = _confirmer_adjudicated_proposals()
    for conf in _evidence_confirmer_candidates(
        claims_meta, exp_evidence, substrate_by_id, confirmer_queued_claims,
        confirmer_adjudicated,
    )[:40]:
        cid = conf["claim_id"]
        adj = conf.get("adjudication")
        if adj:
            item_status = "blocked"
            blockers = [adj["reason"][:240]]
            why_now = (
                f"ALREADY ADJUDICATED -- do not re-investigate. A prior session"
                + (f" ({adj['session']})" if adj["session"] else "")
                + f" recorded {adj['proposal_id']} status={adj['status']} in "
                f"experiment_proposals.v1.json. See blocked_by; re-runs of this "
                f"confirmer are NO-OPs until that status is cleared."
            )[:240]
        else:
            item_status = conf_status
            blockers = []
            why_now = (
                f"GOV-CONFIRM-1: candidate w/ built substrate (tagged in ree_core), "
                f"lit_conf {conf['lit_conf']:.2f}, ZERO experimental evidence. Scope a "
                f"WALL-INDEPENDENT representation/functional-signature confirming DV "
                f"(self-route substrate_not_ready_requeue if only a behavioural DV exists). "
                f"loc: {conf['location']}"
            )[:240]
        add(
            lane="experiment",
            skill="/queue-experiment",
            status=item_status,
            # Low priority: sorts BELOW governance(1-8)/substrate(20-25)/retest(28)/
            # ops(35)/proposals(40) -- confirmers are background fill behind the front.
            priority=55,
            severity="low",
            title=f"Confirm evidence: {cid} (lit {conf['lit_conf']:.2f}, exp ~0)",
            why_now=why_now,
            gap_ids=[],
            claim_ids=[cid],
            owner_exq=None,
            blocked_by=blockers,
            unblocks=[cid],
            confirmer=True,
        )

    items.sort(key=lambda x: (x.get("priority", 99), x.get("id", "")))

    plan_reg = _load_plan_registry()
    lenses_meta, indexes = _enrich_workset_items(items, plan_reg)

    # Compute the identity hash for every item up front -- both the spawned_task
    # auto-release reconcile and the assignment merge key on it.
    try:
        from igw_assignments_lib import (
            assignments_by_hash,
            stable_hash_item,
        )
    except ImportError:
        # Allow running before lib lands without crashing the generator.
        assignments_by_hash = None
        stable_hash_item = None
    if stable_hash_item:
        for it in items:
            it["stable_hash"] = stable_hash_item(it)

    # Auto-release any spawned_task assignment whose underlying item has dropped
    # out of the `ready` set (work landed / no longer eligible). Must run BEFORE
    # the merge so a just-released mirror is not re-attached as "assigned".
    auto_released: list[str] = []
    if stable_hash_item:
        auto_released = reconcile_spawned_task_assignments(items, now_iso=generated)

    # Merge active agent assignments (sole source: evidence/planning/igw_assignments.json)
    # onto each item. Keyed on stable_hash so it survives daily IGW ID rotation.
    # See REE_assembly/scripts/igw_assignments_lib.py for the writer contract.
    assigned_count = 0
    if assignments_by_hash and stable_hash_item:
        by_hash = assignments_by_hash()
        for it in items:
            asgn = by_hash.get(it["stable_hash"]) or []
            it["assignments"] = asgn
            if asgn:
                assigned_count += 1

    # GOV-CONFIRM-1 P2 concurrency cap: keep at most CONFIRMER_AUTOSPAWN_CAP confirmers
    # autospawn-eligible (`ready`) at once. Confirmers already in flight (active
    # assignment) count against the cap and are never demoted; the lowest-priority
    # surplus `ready` confirmers WITHOUT an assignment are demoted back to `surfaced`
    # so the external auto-spawn routine never launches more than the cap concurrently.
    # No-op when the lane is surface-only (nothing is `ready`). Runs AFTER the assignment
    # merge so `it["assignments"]` is populated. Confirmers are emitted lit_conf-desc and
    # share priority 55, so the global (priority,id) sort keeps them lit-desc -- the
    # demoted surplus is the lowest-lit, and the highest-lit keep the free slots.
    if CONFIRMER_AUTOSPAWN_ENABLED:
        conf_items = [it for it in items if it.get("confirmer")]
        in_flight = sum(1 for it in conf_items if it.get("assignments"))
        free_ready = [
            it for it in conf_items
            if it.get("status") == "ready" and not it.get("assignments")
        ]
        slots = max(0, CONFIRMER_AUTOSPAWN_CAP - in_flight)
        for it in free_ready[slots:]:
            it["status"] = "surfaced"

    by_version: dict[str, int] = {}
    for x in items:
        by_version[x.get("version") or "v3"] = by_version.get(x.get("version") or "v3", 0) + 1

    summary = {
        "total": len(items),
        "ready": sum(1 for x in items if x.get("status") == "ready"),
        "in_flight": sum(1 for x in items if x.get("status") == "in_flight"),
        "blocked": sum(1 for x in items if x.get("status") == "blocked"),
        "assigned": assigned_count,
        "spawned_task_auto_released": len(auto_released),
        "pending_review_count": pr,
        "queue_pending": len(pending_q),
        "queue_snapshot": {
            "ref": QUEUE_GIT_REF,
            "worktree_items": len(queue_worktree),
            "committed_items": (
                -1 if queue_committed is None else len(queue_committed)
            ),
            "merged_items": len(queue_items),
            # How many queue entries the working-tree checkout was missing. A
            # non-zero value means ree-v3 is behind and every suppression
            # predicate would have been reasoning about a short queue (FM8).
            "worktree_behind_by": (
                0 if queue_committed is None
                else max(0, len(queue_items) - len(queue_worktree))
            ),
        },
        "live_exqs": sorted(live.keys()),
        "auto_absorbed_retests": auto_absorbed_retests,
        "by_version": {v: by_version[v] for v in sorted(by_version)},
    }

    return {
        "schema_version": "inter_governance_workset/v1.1",
        "generated_at": generated,
        "generator": "scripts/generate_inter_governance_workset.py",
        "summary": summary,
        "lenses": lenses_meta,
        "indexes": indexes,
        "plans": {
            pid: {
                "title": info["title"],
                "scope_claims": info["scope_claims"],
                "generation": info.get("generation") or "v3",
            }
            for pid, info in sorted(plan_reg.items())
        },
        "items": items,
        "references": {
            "closure_v3": "/closure",
            "workset_page": "/workset",
            "machines": "/machines",
            "explorer": "/explorer.html",
        },
    }


def write_markdown(data: dict) -> str:
    lines = [
        "# Inter-Governance Workset",
        "",
        f"Generated: `{data['generated_at']}`",
        f"Schema: `{data['schema_version']}`",
        "",
        "Regenerate: `/inter-governance-brief` or "
        "`python scripts/generate_inter_governance_workset.py` from `REE_assembly/`.",
        "",
        f"UI: http://localhost:8000/workset",
        "",
        "## Summary",
        "",
        f"- Items: **{data['summary']['total']}** "
        f"(ready {data['summary']['ready']}, in_flight {data['summary']['in_flight']}, "
        f"blocked {data['summary']['blocked']})",
        "- By generation: "
        + ", ".join(
            f"{v} {n}" for v, n in sorted((data["summary"].get("by_version") or {}).items())
        ),
        f"- Pending review: **{data['summary']['pending_review_count']}**",
        f"- Queue pending (unclaimed): **{data['summary']['queue_pending']}**",
        "",
    ]
    if data["summary"].get("live_exqs"):
        lines.append("- Live EXQs: " + ", ".join(data["summary"]["live_exqs"][:8]))
        lines.append("")
    absorbed = data["summary"].get("auto_absorbed_retests") or {}
    if absorbed:
        absorbed_str = ", ".join(f"{cid} -> {qid}" for cid, qid in sorted(absorbed.items()))
        lines.append(
            f"- Auto-absorbed retests (queued, suppressed from workset): {absorbed_str}"
        )
        lines.append("")
    lines.extend(["## Work packages", ""])
    for it in data["items"]:
        lines.append(f"### {it['id']} -- {it['title']}")
        lines.append("")
        lines.append(f"- **Lane:** {it['lane']} | **Skill:** `{it['skill']}` | **Status:** {it['status']} | **Priority:** {it.get('priority')} | **Generation:** {it.get('version', 'v3')}")
        if it.get("gap_ids"):
            lines.append(f"- **Gap(s):** {', '.join(it['gap_ids'])}")
        if it.get("owner_exq"):
            lines.append(f"- **Owner EXQ:** {it['owner_exq']}")
        if it.get("blocked_by"):
            lines.append(f"- **Blocked by:** {'; '.join(it['blocked_by'])}")
        lines.append(f"- **Why now:** {it.get('why_now', '')}")
        lines.append("")
        lines.append("<details><summary>Agent brief (copy-paste)</summary>")
        lines.append("")
        lines.append("```")
        lines.append(it.get("agent_brief", ""))
        lines.append("```")
        lines.append("")
        lines.append("</details>")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    data = build_workset()
    OUTPUT_JSON.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    OUTPUT_MD.write_text(write_markdown(data), encoding="utf-8")
    print(f"Wrote {OUTPUT_JSON.relative_to(ROOT)} ({len(data['items'])} items)")
    print(f"Wrote {OUTPUT_MD.relative_to(ROOT)}")
    # FM3 advisory: the substrate lane fails OPEN to "ready", so an unrecognised
    # status string silently becomes a spawned /implement-substrate chip. Name
    # them rather than letting the default stay invisible. Never fatal -- a
    # genuinely-unbuilt entry with an unusual status must still be emitted.
    # FM8 advisory: the ree-v3 checkout is a sibling repo this generator never
    # syncs, so it can sit arbitrarily far behind origin/main. The merge in
    # _load_queue makes that harmless for suppression, but a persistently-behind
    # checkout still means every OTHER ree-v3 reader in this tree is stale, which
    # is worth surfacing rather than silently papering over.
    snap = data["summary"].get("queue_snapshot") or {}
    if snap.get("committed_items") == -1:
        print(
            f"NOTE: could not read the committed queue snapshot "
            f"({snap.get('ref')}:experiment_queue.json) -- fell back to the "
            f"ree-v3 WORKING TREE alone ({snap.get('worktree_items')} entries). "
            f"Queued-experiment suppression may be stale; see the FM8 note on "
            f"_load_queue in this file.",
            file=sys.stderr,
        )
    elif snap.get("worktree_behind_by"):
        print(
            f"NOTE: the ree-v3 working tree is missing "
            f"{snap['worktree_behind_by']} queue entr(ies) present on "
            f"{snap.get('ref')} ({snap.get('worktree_items')} vs "
            f"{snap.get('merged_items')} merged). This workset is correct -- the "
            f"snapshots are merged -- but that checkout is behind; consider "
            f"`git -C ree-v3 pull` so other readers agree with it.",
            file=sys.stderr,
        )

    drift = _unclassified_ready_items()
    if drift:
        print(
            f"NOTE: {len(drift)} substrate_queue entr(ies) are 'Substrate ready' "
            f"only because no status classifier recognised their status string. "
            f"If any of these have LANDED, the status vocabulary has drifted -- "
            f"see the FM3 note in this file:",
            file=sys.stderr,
        )
        for item in drift:
            sd = item.get("sd_id") or "?"
            st = (item.get("status") or item.get("implementation_status") or "")[:80]
            print(f"  - {sd}: status={st!r}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
