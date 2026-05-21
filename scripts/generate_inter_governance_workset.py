#!/usr/bin/env python3
"""
Generate the post-governance inter-governance workset (machine + human views).

Usage (from REE_assembly root):
    /opt/local/bin/python3 scripts/generate_inter_governance_workset.py

Outputs:
    evidence/planning/inter_governance_workset.v1.json
    evidence/planning/inter_governance_workset.md

Consumed by GET /api/workset and /workset.html. Regenerate via /inter-governance-brief.
"""
from __future__ import annotations

import json
import re
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
PENDING_REVIEW = EVIDENCE / "pending_review.md"
PROMOTION_MD = EVIDENCE / "promotion_demotion_recommendations.md"
SUBSTRATE_QUEUE = PLANNING / "substrate_queue.json"
PROPOSALS_JSON = PLANNING / "experiment_proposals.v1.json"
RUNNER_STATUS = EVIDENCE / "runner_status.json"
RUNNER_STATUS_DIR = EVIDENCE / "runner_status"
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


def _load_queue() -> list[dict]:
    if not REE_V3_QUEUE.exists():
        return []
    try:
        data = json.loads(REE_V3_QUEUE.read_text(encoding="utf-8"))
    except Exception:
        return []
    return [x for x in (data.get("items") or []) if isinstance(x, dict)]


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


def _substrate_ready_items() -> list[dict]:
    if not SUBSTRATE_QUEUE.exists():
        return []
    try:
        sq = json.loads(SUBSTRATE_QUEUE.read_text(encoding="utf-8"))
    except Exception:
        return []
    out = []
    for item in sq.get("queue") or []:
        if not isinstance(item, dict) or not item.get("ready"):
            continue
        impl = (item.get("implementation_status") or item.get("status") or "").lower()
        if impl in ("implemented", "done", "complete", "phase_2_implemented"):
            continue
        out.append(item)
    return out


def _proposed_experiments() -> list[dict]:
    if not PROPOSALS_JSON.exists():
        return []
    try:
        data = json.loads(PROPOSALS_JSON.read_text(encoding="utf-8"))
    except Exception:
        return []
    return [
        p for p in (data.get("items") or [])
        if isinstance(p, dict) and p.get("status") == "proposed"
    ][:15]


def _undiagnosed_errors(queue_items: list[dict]) -> list[dict]:
    queued_types = {
        (it.get("experiment_type") or "").lower()
        for it in queue_items
    }
    errors: list[dict] = []
    paths = []
    if RUNNER_STATUS.exists():
        paths.append(RUNNER_STATUS)
    if RUNNER_STATUS_DIR.is_dir():
        paths.extend(sorted(RUNNER_STATUS_DIR.glob("*.json")))
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
            et = (entry.get("experiment_type") or "").lower()
            key = qid or et
            if key in seen:
                continue
            seen.add(key)
            if et in queued_types:
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


def _load_plan_registry() -> dict[str, dict]:
    """plan_id -> {title, scope_claims} from *_plan.md frontmatter."""
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
            by_plan.setdefault(str(pid), []).append(it["id"])
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
    if item.get("blocked_by"):
        lines.append(f"Blocked by: {'; '.join(item['blocked_by'])}")
    lines.append(f"Why now: {item.get('why_now', '')}")
    lines.append("")
    lines.append("Instructions:")
    if item["skill"] == "/governance":
        lines.append("- Run /governance from REE_assembly; walk pending_review with user.")
    elif item["skill"] == "/queue-experiment":
        lines.append("- Use /queue-experiment (not manual queue edits). Smoke test before declaring done.")
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


def build_workset() -> dict:
    generated = _utc_now()
    items: list[dict] = []
    seq = 0
    live = _running_exqs()
    queue_items = _load_queue()
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

    for sq in _substrate_ready_items()[:8]:
        sd = sq.get("sd_id") or "?"
        add(
            lane="substrate",
            skill="/implement-substrate",
            status="ready",
            priority=25,
            severity="high",
            title=f"Substrate ready: {sd}",
            why_now=sq.get("implementation_hint", "substrate_queue ready=true")[:200],
            gap_ids=[],
            claim_ids=list(sq.get("unblocks_claims") or [])[:6],
            owner_exq=None,
            blocked_by=[],
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

    retest = sorted(_claim_retest_ids())
    for cid in retest[:10]:
        add(
            lane="experiment",
            skill="/queue-experiment",
            status="ready",
            priority=28,
            severity="medium",
            title=f"Retest after substrate: {cid}",
            why_now="claims.yaml pending_retest_after_substrate=true.",
            gap_ids=[],
            claim_ids=[cid],
            owner_exq=None,
            blocked_by=[],
            unblocks=[cid],
        )

    for prop in _proposed_experiments()[:5]:
        pid = prop.get("proposal_id") or "?"
        cid = prop.get("claim_id") or ""
        add(
            lane="experiment",
            skill="/queue-experiment",
            status="ready",
            priority=40,
            severity="medium",
            title=f"Proposal {pid} ({cid})",
            why_now="; ".join(prop.get("why_now") or [])[:200] or "experiment_proposals status=proposed",
            gap_ids=[],
            claim_ids=[cid] if cid else [],
            owner_exq=None,
            blocked_by=[],
            unblocks=[cid] if cid else [],
        )

    items.sort(key=lambda x: (x.get("priority", 99), x.get("id", "")))

    plan_reg = _load_plan_registry()
    lenses_meta, indexes = _enrich_workset_items(items, plan_reg)

    summary = {
        "total": len(items),
        "ready": sum(1 for x in items if x.get("status") == "ready"),
        "in_flight": sum(1 for x in items if x.get("status") == "in_flight"),
        "blocked": sum(1 for x in items if x.get("status") == "blocked"),
        "pending_review_count": pr,
        "queue_pending": len(pending_q),
        "live_exqs": sorted(live.keys()),
    }

    return {
        "schema_version": "inter_governance_workset/v1.1",
        "generated_at": generated,
        "generator": "scripts/generate_inter_governance_workset.py",
        "summary": summary,
        "lenses": lenses_meta,
        "indexes": indexes,
        "plans": {
            pid: {"title": info["title"], "scope_claims": info["scope_claims"]}
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
        f"- Pending review: **{data['summary']['pending_review_count']}**",
        f"- Queue pending (unclaimed): **{data['summary']['queue_pending']}**",
        "",
    ]
    if data["summary"].get("live_exqs"):
        lines.append("- Live EXQs: " + ", ".join(data["summary"]["live_exqs"][:8]))
        lines.append("")
    lines.extend(["## Work packages", ""])
    for it in data["items"]:
        lines.append(f"### {it['id']} -- {it['title']}")
        lines.append("")
        lines.append(f"- **Lane:** {it['lane']} | **Skill:** `{it['skill']}` | **Status:** {it['status']} | **Priority:** {it.get('priority')}")
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
