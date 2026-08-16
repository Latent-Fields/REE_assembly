#!/usr/bin/env python3
"""Shared load/parse layer for the Steward integrity detectors.

Every detector reads the same three things -- docs/claims/claims.yaml, the
`closure_plan` frontmatter of every evidence/planning/*_plan.md, and the
node->claim ownership index derived from them. Parsing those once and handing
the result to each detector is what keeps the whole run inside its budget:
claims.yaml is ~1000 entries / ~51k lines and costs 5.6s under the pure-python
yaml loader versus 0.39s under libyaml's CSafeLoader (measured 2026-08-16 on
ree-cloud-5). Detectors therefore MUST take a Context rather than re-reading.

OWNERSHIP MODEL (the load-bearing definition -- read this before changing a
detector). A closure node OWNS a claim when the claim id appears in that node's
`unblocks_claims` list. This is deliberately NOT `join.scope_claims`, which is a
broad "bears on" association: arc_062_rule_apprehension:GAP-I-absorption lists 2
claims under unblocks_claims and 29 under scope_claims, and using the latter
would make almost every claim look owned by almost every node. `unblocks_claims`
is the relation the closure map actually uses to say "closing this node is what
discharges this claim".

ASCII-only output per the repo-wide rule (these run on Windows terminals too).
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

# libyaml when available (14x faster on claims.yaml); silently fall back so a
# machine without the C extension still runs, just slower.
try:
    _LOADER = yaml.CSafeLoader  # type: ignore[attr-defined]
except AttributeError:  # pragma: no cover - depends on libyaml presence
    _LOADER = yaml.SafeLoader


# Node status weights. Kept as an INDEPENDENT copy on purpose -- D-010's whole
# job is to recompute the closure denominator without trusting the producer, so
# importing generate_closure_snapshot.py's copy would defeat the check. Drift
# between this table and serve.py's authoritative CLOSURE_STATUS_WEIGHTS is
# itself reported by D-010 rather than silently absorbed.
#
# None == excluded from the closure progress denominator.
STATUS_WEIGHTS: dict[str, float | None] = {
    "done": 1.0,
    "partial": 0.5,
    "in_progress": 0.4,
    "in-progress": 0.4,
    "blocked": 0.1,
    "upstream_blocked": 0.1,
    "blocked_pending_substrate": 0.1,
    "tracked": 0.2,
    "pending_governance_stamp": 0.4,
    "open": 0.0,
    "pending": 0.0,
    "assembling": None,
    "open_by_design": None,
    "deferred": None,
    "deferred V4": None,
    "deferred_v4": None,
    "deferred_v5": None,
    "parked": None,
    "parked_indefinite": None,
    "closed": None,
}

# The subset of excluded statuses that the closure snapshot labels "deferred".
# NOTE the asymmetry, which is the single most important fact in this file and
# the reason D-010 exists: DEFERRED_STATUSES is NOT the denominator exclusion
# set. The denominator excludes every status whose weight is None -- which also
# covers assembling / open_by_design / parked / closed / deferred_v5. On the
# 2026-08-16 tree that is 117 v3 nodes - 13 deferred - 10 assembling = 94, and
# a DEFERRED_STATUSES-only reading would wrongly predict 104.
DEFERRED_STATUSES = {"deferred", "deferred_v4"}

DEFAULT_GENERATION = "v3"


def norm_status(s: Any) -> str:
    """Normalise a node status the same way the closure snapshot does."""
    if not s:
        return "open"
    return str(s).strip().lower().replace(" ", "_").replace("-", "_")


def counts_toward_denominator(status: str) -> bool:
    """True when a node with this status is inside the closure denominator.

    Unknown statuses count (they fall through to weight 0.0, scoring as unstarted
    work) -- D-010 reports them separately because scoring-as-open is a guess,
    not a decision.
    """
    return STATUS_WEIGHTS.get(status, 0.0) is not None


@dataclass
class Node:
    plan_file: str
    plan_id: str
    generation: str
    node_id: str
    status: str
    title: str = ""
    unblocks_claims: list[str] = field(default_factory=list)
    raw: dict = field(default_factory=dict)


@dataclass
class Context:
    """Everything the detectors read, parsed exactly once."""

    repo_root: Path
    claims: list[dict]
    claims_by_id: dict[str, dict]
    nodes: list[Node]
    plans: list[dict]
    owners: dict[str, list[Node]]      # claim id -> nodes whose unblocks_claims name it
    parse_errors: list[str]

    # --- git lane (stage 3). Defaulted so every existing construction of
    # Context keeps working unchanged. ---
    # Repos the git lane inspects. Empty means "just repo_root".
    git_repos: list[Path] = field(default_factory=list)
    # Pins persisted by the PREVIOUS run, loaded by the runner. This is what
    # makes "has origin moved since you last looked?" answerable at all.
    prior_ref_pins: dict = field(default_factory=dict)
    # Pins a git-lane detector computed its verdict against, published for
    # D-102 to re-verify at end of run (the tail window).
    ref_pins: dict = field(default_factory=dict)
    # Pins to persist for the next run. Written by the runner, not by a
    # detector -- detectors stay read-only with respect to state.
    ref_pins_out: dict = field(default_factory=dict)

    def v3_owners(self, claim_id: str) -> list[Node]:
        return [n for n in self.owners.get(claim_id, [])
                if n.generation == DEFAULT_GENERATION]


def _parse_frontmatter(path: Path) -> dict | None:
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
        fm = yaml.load(text[4:end], Loader=_LOADER)
    except Exception:
        return None
    return fm if isinstance(fm, dict) else None


def load_context(repo_root: Path) -> Context:
    repo_root = Path(repo_root).resolve()
    parse_errors: list[str] = []

    claims_path = repo_root / "docs" / "claims" / "claims.yaml"
    claims: list[dict] = []
    if claims_path.exists():
        try:
            with claims_path.open(encoding="utf-8") as fh:
                loaded = yaml.load(fh, Loader=_LOADER)
            if isinstance(loaded, list):
                claims = [c for c in loaded if isinstance(c, dict)]
            else:
                parse_errors.append("claims.yaml did not parse as a list")
        except Exception as exc:
            parse_errors.append("claims.yaml parse failed: %s" % exc)
    else:
        parse_errors.append("claims.yaml not found at %s" % claims_path)

    claims_by_id = {str(c["id"]): c for c in claims if c.get("id")}

    planning = repo_root / "evidence" / "planning"
    nodes: list[Node] = []
    plans: list[dict] = []
    owners: dict[str, list[Node]] = {}

    for path in sorted(planning.glob("*_plan.md")) if planning.exists() else []:
        fm = _parse_frontmatter(path)
        plan = fm.get("closure_plan") if isinstance(fm, dict) else None
        if not isinstance(plan, dict):
            continue  # a *_plan.md with no closure frontmatter is not an error
        gen = str(plan.get("generation") or DEFAULT_GENERATION).strip().lower()
        plan_id = str(plan.get("id") or path.stem)
        raw_nodes = [n for n in (plan.get("nodes") or [])
                     if isinstance(n, dict) and n.get("id")]
        plans.append({
            "id": plan_id,
            "file": path.name,
            "title": plan.get("title") or path.stem,
            "generation": gen,
            "node_count": len(raw_nodes),
        })
        for n in raw_nodes:
            unblocks = [str(c) for c in (n.get("unblocks_claims") or [])]
            node = Node(
                plan_file=path.name,
                plan_id=plan_id,
                generation=gen,
                node_id=str(n["id"]),
                status=norm_status(n.get("status")),
                title=str(n.get("title") or ""),
                unblocks_claims=unblocks,
                raw=n,
            )
            nodes.append(node)
            for cid in unblocks:
                owners.setdefault(cid, []).append(node)

    return Context(
        repo_root=repo_root,
        claims=claims,
        claims_by_id=claims_by_id,
        nodes=nodes,
        plans=plans,
        owners=owners,
        parse_errors=parse_errors,
    )


# --------------------------------------------------------------------------
# Finding schema
# --------------------------------------------------------------------------

SEVERITY_RANK = {"P0": 4, "P1": 3, "P2": 2, "P3": 1}


def finding(
    detector: str,
    subject: str,
    title: str,
    detail: str,
    severity: str = "P2",
    confidence: float = 0.5,
    signal: str = "weak",
    escalate: bool = True,
    evidence: dict | None = None,
    route: str = "/governance",
    tier: str = "T2",
    autofix: bool = False,
) -> dict:
    """Build one finding.

    `finding_id` is `<detector>:<subject>` and is the ONLY identity used for
    state diffing and suppression, so it must be stable across runs for the same
    underlying defect. Never fold a mutable field (status, date, count) into it.

    `escalate` is the detector's own assertion that this finding is worth waking
    a model for. It is not a confidence threshold: severity and confidence RANK
    findings when the escalation budget is contended, they never withhold one.

    `tier` records who can repair this: T0 = mechanically auto-fixable by the
    runner, T1 = needs a human/model decision, T2 = reported for action taken
    elsewhere (the git lane). `autofix` is the per-finding assertion that this
    specific instance is repairable now -- a T0 DETECTOR can still emit a T1
    finding when the particular case turns out ambiguous, which is the
    "demote rather than guess" rule made explicit in the schema.
    """
    if severity not in SEVERITY_RANK:
        raise ValueError("bad severity %r" % severity)
    if tier not in ("T0", "T1", "T2"):
        raise ValueError("bad tier %r" % tier)
    if autofix and tier != "T0":
        raise ValueError("autofix=True requires tier T0 (got %r)" % tier)
    return {
        "tier": tier,
        "autofix": bool(autofix),
        "finding_id": "%s:%s" % (detector, subject),
        "detector": detector,
        "subject": subject,
        "title": title,
        "detail": detail,
        "severity": severity,
        "confidence": round(float(confidence), 3),
        "signal": signal,
        "escalate": bool(escalate),
        "route": route,
        "evidence": evidence or {},
    }


def rank_score(f: dict) -> float:
    """Ranking key for escalation-budget contention: severity x confidence."""
    return SEVERITY_RANK.get(f.get("severity", "P3"), 1) * float(f.get("confidence", 0.0))


def repo_root_from_here() -> Path:
    """REE_assembly root, from scripts/steward/detectors/_common.py."""
    env = os.environ.get("STEWARD_REPO_ROOT")
    if env:
        return Path(env).resolve()
    return Path(__file__).resolve().parents[3]
