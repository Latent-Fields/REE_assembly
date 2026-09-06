#!/usr/bin/env python3
"""Build SCC-collapsed claim dependency process data for explorer.html.

The explorer needs a process view that answers: when claims were added, which
dependency components they attach to, and whether that work is V3 closure or
longer-horizon scope. Creation dates are inferred from git history so older
claims do not need a hand-maintained registered_utc field.
"""

from __future__ import annotations

import json
import re
import subprocess
from collections import Counter, defaultdict
from datetime import date, datetime, timezone, timedelta
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
CLAIMS_PATH = ROOT / "docs" / "claims" / "claims.yaml"
CLAIMS_GIT_PATH = "docs/claims/claims.yaml"
EVIDENCE_PATH = ROOT / "evidence" / "experiments" / "claim_evidence.v1.json"
SUBSTRATE_QUEUE_PATH = ROOT / "evidence" / "planning" / "substrate_queue.json"
EXPERIMENT_PROPOSALS_PATH = ROOT / "evidence" / "planning" / "experiment_proposals.v1.json"
V3_EXPERIMENT_QUEUE_PATH = ROOT.parent / "ree-v3" / "experiment_queue.json"
OUT_PATH = ROOT / "docs" / "assets" / "data" / "claim_dependency_process.v1.json"
CLAIM_ID_RE = re.compile(r"^-\s+id:\s*([A-Z]+-\d{3}[A-Za-z]?)", re.MULTILINE)
CLAIM_TOKEN_RE = re.compile(r"\b(?:ARC|INV|MECH|Q|SD|IMPL)-\d{3}[A-Za-z]?\b")


def run_git(args: list[str]) -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True)


def week_start(day: str) -> str:
    dt = date.fromisoformat(str(day)[:10])
    return (dt - timedelta(days=dt.weekday())).isoformat()


def phase_for(claim: dict[str, Any]) -> str:
    phase = claim.get("implementation_phase")
    if phase:
        return str(phase)
    if claim.get("v3_pending") is True:
        return "v3"
    if str(claim.get("id", "")).startswith("SD-"):
        return "substrate_unspecified"
    return "unset"


def class_for(claim: dict[str, Any]) -> str:
    phase = phase_for(claim)
    claim_type = claim.get("claim_type")
    claim_id = str(claim.get("id", ""))
    epistemic = claim.get("epistemic_category")
    if phase in {"v4", "v5"}:
        return f"horizon_{phase}"
    if phase == "v3" or claim.get("v3_pending") is True:
        return "active_v3_closure"
    if epistemic in {"substrate_ceiling", "substrate_conditional"}:
        return "substrate_gap_marked"
    if claim_id.startswith("SD-") or claim_type in {"substrate_decision", "design_decision"}:
        return "substrate_or_design"
    if claim_type == "open_question":
        return "open_question"
    if claim_type == "invariant":
        return "invariant_or_foundation"
    if claim_type in {"mechanism_hypothesis", "mechanism"}:
        return "mechanism_general"
    if claim_type in {"architectural_commitment", "architecture_hypothesis", "arch_commitment"}:
        return "architecture_general"
    if claim_type == "implementation_note":
        return "implementation_note"
    return "other"


def load_first_seen() -> dict[str, dict[str, str]]:
    log = run_git([
        "log",
        "--follow",
        "--reverse",
        "--format=%H%x09%ad%x09%s",
        "--date=short",
        "--",
        CLAIMS_GIT_PATH,
    ])
    first_seen: dict[str, dict[str, str]] = {}
    for line in log.splitlines():
        if not line.strip():
            continue
        commit_hash, commit_date, subject = line.split("\t", 2)
        try:
            text = run_git(["show", f"{commit_hash}:{CLAIMS_GIT_PATH}"])
        except subprocess.CalledProcessError:
            continue
        for claim_id in CLAIM_ID_RE.findall(text):
            if claim_id not in first_seen:
                first_seen[claim_id] = {
                    "date": commit_date,
                    "week": week_start(commit_date),
                    "commit": commit_hash,
                    "subject": subject,
                }
    return first_seen


def tarjan_scc(graph: dict[str, list[str]]) -> list[list[str]]:
    index = 0
    stack: list[str] = []
    on_stack: set[str] = set()
    indices: dict[str, int] = {}
    lowlink: dict[str, int] = {}
    components: list[list[str]] = []

    def strongconnect(node: str) -> None:
        nonlocal index
        indices[node] = index
        lowlink[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)

        for other in graph.get(node, []):
            if other not in indices:
                strongconnect(other)
                lowlink[node] = min(lowlink[node], lowlink[other])
            elif other in on_stack:
                lowlink[node] = min(lowlink[node], indices[other])

        if lowlink[node] == indices[node]:
            component = []
            while True:
                other = stack.pop()
                on_stack.remove(other)
                component.append(other)
                if other == node:
                    break
            components.append(sorted(component))

    for node in sorted(graph):
        if node not in indices:
            strongconnect(node)
    return components


def counter_dict(counter: Counter[Any]) -> dict[str, int]:
    return {str(k): int(v) for k, v in counter.most_common()}


def load_json(path: Path) -> Any:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def extract_claim_tokens(value: Any) -> set[str]:
    tokens: set[str] = set()
    if isinstance(value, str):
        tokens.update(CLAIM_TOKEN_RE.findall(value))
    elif isinstance(value, list):
        for item in value:
            tokens.update(extract_claim_tokens(item))
    elif isinstance(value, dict):
        for item in value.values():
            tokens.update(extract_claim_tokens(item))
    return tokens


def reciprocal_category(
    *,
    size: int,
    status_counts: dict[str, int],
    type_counts: dict[str, int],
    members: list[str],
    mutual: bool,
) -> tuple[str, str, str]:
    """Shared reciprocal-structure taxonomy (category, cleanup_priority, rationale).

    Written for cyclic depends_on components; since the 2026-09-04 GOV-EDGE-1
    edge-type split (mutual pairs and cycle-break edges moved to coupled_with)
    depends_on is a DAG, so the same ladder is applied to coupled_with pairs
    where ``size`` is the undirected coupling-cluster size containing the pair
    and ``mutual`` means both endpoints list each other. One function so the
    pair-level labels are literally the component-level rules, not a copy.
    """
    has_question_or_invariant = any(
        key in type_counts
        for key in ("question", "open_question", "derived_prediction", "invariant")
    )
    has_design_and_mechanism = (
        "design_decision" in type_counts
        and ("mechanism_hypothesis" in type_counts or "mechanism" in type_counts)
    )
    has_sd = any(str(member).startswith("SD-") for member in members)
    if "superseded" in status_counts:
        return (
            "legacy_superseded_cycle",
            "low",
            "Cycle includes superseded registry material; preserve history unless it blocks tooling.",
        )
    if size >= 10:
        return (
            "accepted_reciprocal_architecture",
            "low",
            "Large multi-claim reciprocal architecture cluster; likely reflects real feedback coupling rather than a simple ordering bug.",
        )
    if has_question_or_invariant and size <= 3:
        return (
            "semantic_explanation_cycle",
            "medium",
            "Question, prediction, or invariant is mutually explanatory with its mechanism; edge type may be more precise than strict depends_on.",
        )
    if has_sd and has_design_and_mechanism:
        return (
            "co_definition_module_function",
            "low",
            "Substrate/module claim and functional mechanism co-define each other; useful architecture coupling, not necessarily build-order dependency.",
        )
    if size <= 2 and mutual:
        return (
            "edge_type_cleanup_candidate",
            "medium",
            "Small mutual dependency; likely wants an edge type such as co_defines_with, implements, or predicts rather than strict depends_on.",
        )
    if size <= 6 and mutual:
        return (
            "co_definition_module_function",
            "watch",
            "Small reciprocal module/function cluster; probably valid coupling but worth reviewing edge semantics.",
        )
    return (
        "accepted_reciprocal_architecture",
        "watch",
        "Reciprocal structure is present but not clearly a hygiene issue from graph shape alone.",
    )


COUPLED_ENTRY_RE = re.compile(r"^    -\s+(\S+)\s*(#.*)?$")
CLAIM_HEAD_RE = re.compile(r"^-\s+id:\s*(\S+)")


def load_coupled_with_annotations() -> dict[tuple[str, str], str]:
    """Inline comment text per directed coupled_with entry (source, target).

    claims.yaml is comment-bearing; the GOV-EDGE-1 split tagged every moved
    entry (``mutual pair`` / ``cycle-break`` / ``reverse of``), and governance
    ratification notes live in the same comment. yaml.safe_load drops them, so
    this is a text scan keyed on the same ``- id:`` / ``coupled_with:`` layout
    the split script wrote.
    """
    annotations: dict[tuple[str, str], str] = {}
    current = None
    in_block = False
    for line in CLAIMS_PATH.read_text().splitlines():
        head = CLAIM_HEAD_RE.match(line)
        if head:
            current = head.group(1)
            in_block = False
            continue
        if line.startswith("  coupled_with:"):
            in_block = True
            continue
        if not in_block or current is None:
            continue
        entry = COUPLED_ENTRY_RE.match(line)
        if entry:
            annotations[(current, entry.group(1))] = (entry.group(2) or "").strip()
        elif not line.startswith("    "):
            in_block = False
    return annotations


def coupled_edge_origin(comment: str) -> str:
    lowered = comment.lower()
    if "cycle-break" in lowered:
        return "cycle_break"
    if "reverse of" in lowered:
        return "cycle_break_reverse"
    if "mutual pair" in lowered or "mutual-pair" in lowered:
        return "mutual_pair"
    return "native"


def connected_components(adjacency: dict[str, set[str]]) -> list[list[str]]:
    seen: set[str] = set()
    components: list[list[str]] = []
    for start in sorted(adjacency):
        if start in seen:
            continue
        stack = [start]
        members: list[str] = []
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            members.append(node)
            stack.extend(adjacency[node] - seen)
        components.append(sorted(members))
    components.sort(key=lambda comp: (-len(comp), comp[0]))
    return components


def main() -> None:
    claims = yaml.safe_load(CLAIMS_PATH.read_text())
    if not isinstance(claims, list):
        raise ValueError("claims.yaml must be a top-level list")

    by_id = {claim["id"]: claim for claim in claims if isinstance(claim, dict) and claim.get("id")}
    first_seen = load_first_seen()

    evidence = {}
    if EVIDENCE_PATH.exists():
        evidence_payload = json.loads(EVIDENCE_PATH.read_text())
        evidence = evidence_payload.get("claims", {}) if isinstance(evidence_payload, dict) else {}

    substrate_queue_payload = load_json(SUBSTRATE_QUEUE_PATH)
    substrate_queue_items = substrate_queue_payload.get("queue", []) if isinstance(substrate_queue_payload, dict) else []
    substrate_target_ids: set[str] = set()
    substrate_unblock_ids: set[str] = set()
    for item in substrate_queue_items:
        if not isinstance(item, dict):
            continue
        sd_id = item.get("sd_id")
        if isinstance(sd_id, str):
            substrate_target_ids.add(sd_id)
        substrate_unblock_ids.update(
            claim_id for claim_id in item.get("unblocks_claims", []) or [] if isinstance(claim_id, str)
        )

    experiment_planned_ids: set[str] = set()
    proposals_payload = load_json(EXPERIMENT_PROPOSALS_PATH)
    proposal_items = proposals_payload.get("items", []) if isinstance(proposals_payload, dict) else []
    for item in proposal_items:
        if not isinstance(item, dict):
            continue
        status = str(item.get("status", "")).lower()
        if status in {"executed", "closed", "retired", "superseded", "cancelled"}:
            continue
        experiment_planned_ids.update(extract_claim_tokens(item))

    v3_queue_payload = load_json(V3_EXPERIMENT_QUEUE_PATH)
    if isinstance(v3_queue_payload, list):
        experiment_planned_ids.update(extract_claim_tokens(v3_queue_payload))
    elif isinstance(v3_queue_payload, dict):
        experiment_planned_ids.update(extract_claim_tokens(v3_queue_payload))

    for claim_id, claim in by_id.items():
        if claim_id not in first_seen:
            explicit_date = claim.get("registered_utc") or claim.get("registered")
            if explicit_date:
                day = str(explicit_date)[:10]
                first_seen[claim_id] = {
                    "date": day,
                    "week": week_start(day),
                    "commit": "",
                    "subject": "registered_utc field",
                }
            else:
                first_seen[claim_id] = {
                    "date": "",
                    "week": "unknown",
                    "commit": "",
                    "subject": "unknown",
                }

    graph: dict[str, list[str]] = {}
    edge_count = 0
    for claim_id, claim in by_id.items():
        deps = [dep for dep in claim.get("depends_on", []) or [] if dep in by_id]
        graph[claim_id] = deps
        edge_count += len(deps)
    incoming_counts = Counter(dep for deps in graph.values() for dep in deps)

    components_raw = tarjan_scc(graph)
    components_raw.sort(key=lambda comp: (-len(comp), comp[0]))

    claim_to_component: dict[str, str] = {}
    components = []
    for idx, members in enumerate(components_raw, start=1):
        component_id = f"C{idx:03d}"
        for member in members:
            claim_to_component[member] = component_id
        class_counts = Counter(class_for(by_id[member]) for member in members)
        phase_counts = Counter(phase_for(by_id[member]) for member in members)
        type_counts = Counter(by_id[member].get("claim_type", "unknown") for member in members)
        status_counts = Counter(by_id[member].get("status", "unknown") for member in members)
        evidence_claims = [evidence.get(member, {}) for member in members]
        components.append({
            "component_id": component_id,
            "size": len(members),
            "cyclic": len(members) > 1,
            "claim_ids": members,
            "sample_claim_ids": members[:18],
            "dominant_class": class_counts.most_common(1)[0][0] if class_counts else "unknown",
            "class_counts": counter_dict(class_counts),
            "phase_counts": counter_dict(phase_counts),
            "type_counts": counter_dict(type_counts),
            "status_counts": counter_dict(status_counts),
            "first_week": min(first_seen[member]["week"] for member in members if first_seen[member]["week"] != "unknown") if any(first_seen[member]["week"] != "unknown" for member in members) else "unknown",
            "latest_week": max(first_seen[member]["week"] for member in members if first_seen[member]["week"] != "unknown") if any(first_seen[member]["week"] != "unknown" for member in members) else "unknown",
            "evidenced_claims": sum(1 for item in evidence_claims if item.get("genuine_exp_count", 0) > 0),
            "genuine_exp_count": sum(int(item.get("genuine_exp_count", 0) or 0) for item in evidence_claims),
            "confirmed_established": sum(1 for item in evidence_claims if item.get("evidence_quadrant") == "confirmed_established"),
        })

    component_edges = set()
    for claim_id, deps in graph.items():
        src_comp = claim_to_component[claim_id]
        for dep in deps:
            dst_comp = claim_to_component[dep]
            if src_comp != dst_comp:
                component_edges.add((src_comp, dst_comp))

    def component_cycle_audit(component: dict[str, Any]) -> dict[str, Any]:
        members = component["claim_ids"]
        member_set = set(members)
        internal_edges = [
            (claim_id, dep)
            for claim_id in members
            for dep in graph.get(claim_id, [])
            if dep in member_set
        ]
        edge_set = set(internal_edges)
        mutual_pairs = sorted(
            (source, target)
            for source, target in internal_edges
            if source < target and (target, source) in edge_set
        )
        in_counts = Counter(target for _, target in internal_edges)
        out_counts = Counter(source for source, _ in internal_edges)
        type_counts = component.get("type_counts", {})
        class_counts = component.get("class_counts", {})
        status_counts = component.get("status_counts", {})
        size = int(component.get("size", 0) or 0)
        if not component.get("cyclic"):
            category = "acyclic"
            cleanup_priority = "none"
            rationale = "No internal dependency cycle."
        else:
            category, cleanup_priority, rationale = reciprocal_category(
                size=size,
                status_counts=status_counts,
                type_counts=type_counts,
                members=members,
                mutual=bool(mutual_pairs),
            )
        return {
            "category": category,
            "cleanup_priority": cleanup_priority,
            "rationale": rationale,
            "internal_edge_count": len(internal_edges),
            "mutual_pair_count": len(mutual_pairs),
            "mutual_pairs": [
                {"source": source, "target": target}
                for source, target in mutual_pairs[:18]
            ],
            "top_internal_targets": [
                {"claim_id": claim_id, "count": int(count), "title": by_id[claim_id].get("title", "")}
                for claim_id, count in in_counts.most_common(8)
            ],
            "top_internal_sources": [
                {"claim_id": claim_id, "count": int(count), "title": by_id[claim_id].get("title", "")}
                for claim_id, count in out_counts.most_common(8)
            ],
            "class_counts": class_counts,
            "type_counts": type_counts,
        }

    for component in components:
        if component["cyclic"]:
            component["cycle_audit"] = component_cycle_audit(component)

    # ---- coupled_with layer (GOV-EDGE-1, 2026-09-04) ------------------------
    # depends_on is now a DAG, so the reciprocal taxonomy above is dormant at
    # component level. It is re-applied here per unordered coupled_with pair,
    # with the pair's undirected coupling cluster standing in for SCC size.
    coupled_annotations = load_coupled_with_annotations()
    coupled_adjacency: dict[str, set[str]] = defaultdict(set)
    coupled_directed: set[tuple[str, str]] = set()
    coupled_dangling: list[dict[str, str]] = []
    for claim_id, claim in by_id.items():
        for other in claim.get("coupled_with", []) or []:
            if other not in by_id:
                coupled_dangling.append({"source": claim_id, "target": str(other)})
                continue
            coupled_directed.add((claim_id, other))
            coupled_adjacency[claim_id].add(other)
            coupled_adjacency[other].add(claim_id)
    coupled_clusters_raw = connected_components(coupled_adjacency)
    claim_to_cluster: dict[str, str] = {}
    coupled_clusters = []
    for idx, members in enumerate(coupled_clusters_raw, start=1):
        cluster_id = f"K{idx:03d}"
        for member in members:
            claim_to_cluster[member] = cluster_id
        coupled_clusters.append({
            "cluster_id": cluster_id,
            "size": len(members),
            "claim_ids": members,
            "type_counts": counter_dict(Counter(by_id[m].get("claim_type", "unknown") for m in members)),
            "status_counts": counter_dict(Counter(by_id[m].get("status", "unknown") for m in members)),
            "class_counts": counter_dict(Counter(class_for(by_id[m]) for m in members)),
            "depends_on_components": sorted({claim_to_component[m] for m in members}),
        })
    cluster_by_id = {cluster["cluster_id"]: cluster for cluster in coupled_clusters}

    coupled_pairs = []
    for left, right in sorted({tuple(sorted(edge)) for edge in coupled_directed}):
        pair_members = [left, right]
        symmetric = (left, right) in coupled_directed and (right, left) in coupled_directed
        forward_comment = coupled_annotations.get((left, right), "")
        reverse_comment = coupled_annotations.get((right, left), "")
        origins = {coupled_edge_origin(c) for c, present in (
            (forward_comment, (left, right) in coupled_directed),
            (reverse_comment, (right, left) in coupled_directed),
        ) if present}
        if "cycle_break" in origins:
            origin = "cycle_break"
        elif "mutual_pair" in origins:
            origin = "mutual_pair"
        elif origins == {"cycle_break_reverse"}:
            origin = "cycle_break"
        else:
            origin = "native"
        # A mixed pair keeps a prerequisite in the other direction (emergent_from
        # is never moved by the split; it stays a subset of depends_on).
        prerequisite_reverse = []
        for src, dst in ((left, right), (right, left)):
            if dst in (by_id[src].get("depends_on", []) or []):
                prerequisite_reverse.append({"source": src, "target": dst})
        cluster_id = claim_to_cluster[left]
        cluster_size = cluster_by_id[cluster_id]["size"]
        status_counts = counter_dict(Counter(by_id[m].get("status", "unknown") for m in pair_members))
        type_counts = counter_dict(Counter(by_id[m].get("claim_type", "unknown") for m in pair_members))
        category, cleanup_priority, rationale = reciprocal_category(
            size=cluster_size,
            status_counts=status_counts,
            type_counts=type_counts,
            members=pair_members,
            mutual=symmetric,
        )
        record: dict[str, Any] = {
            "pair_id": f"{left}|{right}",
            "claim_ids": pair_members,
            "titles": {m: by_id[m].get("title", "") for m in pair_members},
            "symmetric": symmetric,
            "prerequisite_reverse": prerequisite_reverse,
            "origin": origin,
            "cluster_id": cluster_id,
            "cluster_size": cluster_size,
            "category": category,
            "cleanup_priority": cleanup_priority,
            "rationale": rationale,
            "type_counts": type_counts,
            "status_counts": status_counts,
            "class_counts": counter_dict(Counter(class_for(by_id[m]) for m in pair_members)),
        }
        if origin == "cycle_break":
            # The split moved exactly one direction; the other carries "reverse of".
            if coupled_edge_origin(forward_comment) == "cycle_break":
                moved = {"source": left, "target": right, "comment": forward_comment}
            else:
                moved = {"source": right, "target": left, "comment": reverse_comment or forward_comment}
            cycle_match = re.search(r"\(cycle ([^)]*)\)", moved["comment"])
            record["cycle_break"] = {
                "moved_edge": f"{moved['source']} -> {moved['target']}",
                "cycle": cycle_match.group(1).strip() if cycle_match else "",
                "ratified": "ratified" in moved["comment"].lower(),
                "comment": moved["comment"],
            }
        coupled_pairs.append(record)

    coupled_category_counts = Counter(pair["category"] for pair in coupled_pairs)
    coupled_cleanup_counts = Counter(pair["cleanup_priority"] for pair in coupled_pairs)
    coupled_origin_counts = Counter(pair["origin"] for pair in coupled_pairs)
    cycle_break_report = [
        {
            "moved_edge": pair["cycle_break"]["moved_edge"],
            "pair_id": pair["pair_id"],
            "category": pair["category"],
            "cleanup_priority": pair["cleanup_priority"],
            "cluster_id": pair["cluster_id"],
            "cluster_size": pair["cluster_size"],
            "ratified": pair["cycle_break"]["ratified"],
            "cycle": pair["cycle_break"]["cycle"],
        }
        for pair in coupled_pairs
        if pair["origin"] == "cycle_break"
    ]
    coupled_with_section = {
        "method": (
            "Each unordered coupled_with pair is labelled with the same reciprocal taxonomy "
            "the depends_on cycle audit used (reciprocal_category); 'size' is the undirected "
            "coupled_with cluster containing the pair, 'mutual' means both endpoints list each other. "
            "Labels are pair-level; governance re-judgement of cycle-break edges is reported, not applied."
        ),
        "summary": {
            "pair_count": len(coupled_pairs),
            "directed_entry_count": len(coupled_directed),
            "claim_count": len(coupled_adjacency),
            "cluster_count": len(coupled_clusters),
            "largest_cluster_size": max((c["size"] for c in coupled_clusters), default=0),
            "symmetric_pairs": sum(1 for pair in coupled_pairs if pair["symmetric"]),
            "mixed_prerequisite_pairs": sum(1 for pair in coupled_pairs if pair["prerequisite_reverse"]),
            "dangling_targets": len(coupled_dangling),
            "category_counts": counter_dict(coupled_category_counts),
            "cleanup_counts": counter_dict(coupled_cleanup_counts),
            "origin_counts": counter_dict(coupled_origin_counts),
            "cycle_break_category_counts": counter_dict(Counter(row["category"] for row in cycle_break_report)),
        },
        "cycle_break_edges": cycle_break_report,
        "clusters": coupled_clusters,
        "pairs": coupled_pairs,
        "dangling": coupled_dangling,
    }

    def claim_attention_for(claim_id: str) -> dict[str, Any]:
        claim = by_id[claim_id]
        ev = evidence.get(claim_id, {})
        evidence_bearing = (
            int(ev.get("genuine_exp_count", 0) or 0) > 0
            or int(ev.get("entries_total", 0) or 0) > 0
            or bool(ev.get("latest_run_id"))
            or bool(ev.get("source_counts"))
        )
        dependency_referenced = incoming_counts[claim_id] > 0
        experiment_planned = claim_id in experiment_planned_ids
        substrate_active = (
            claim_id in substrate_target_ids
            or phase_for(claim) == "v3"
            or claim.get("v3_pending") is True
        )
        if evidence_bearing:
            lifecycle = "governance_evidence_bearing"
        elif substrate_active:
            lifecycle = "substrate_implementation_active"
        elif experiment_planned:
            lifecycle = "experiment_planned"
        elif dependency_referenced:
            lifecycle = "dependency_referenced"
        else:
            lifecycle = "captured_only"
        return {
            "lifecycle": lifecycle,
            "attention_rank": {
                "captured_only": 0,
                "dependency_referenced": 1,
                "experiment_planned": 2,
                "substrate_implementation_active": 3,
                "governance_evidence_bearing": 4,
            }[lifecycle],
            "dependency_referenced": dependency_referenced,
            "incoming_dependency_count": int(incoming_counts[claim_id]),
            "experiment_planned": experiment_planned,
            "substrate_target": claim_id in substrate_target_ids,
            "substrate_unblocked": claim_id in substrate_unblock_ids,
            "substrate_active": substrate_active,
            "evidence_bearing": evidence_bearing,
        }

    def claim_digest(claim_id: str) -> dict[str, Any]:
        claim = by_id[claim_id]
        ev = evidence.get(claim_id, {})
        attention = claim_attention_for(claim_id)
        return {
            "claim_id": claim_id,
            "title": claim.get("title", ""),
            "type": claim.get("claim_type", "unknown"),
            "status": claim.get("status", "unknown"),
            "phase": phase_for(claim),
            "class": class_for(claim),
            "component_id": claim_to_component[claim_id],
            "evidence_quadrant": ev.get("evidence_quadrant"),
            "genuine_exp_count": int(ev.get("genuine_exp_count", 0) or 0),
            **attention,
        }

    claim_rows = []
    weekly: dict[str, dict[str, Any]] = defaultdict(lambda: {
        "new_claims": 0,
        "created_claim_ids": [],
        "class_counts": Counter(),
        "phase_counts": Counter(),
        "lifecycle_counts": Counter(),
        "type_counts": Counter(),
        "status_counts": Counter(),
        "dependency_target_category_counts": Counter(),
        "dependency_target_claim_counts": Counter(),
        "dependency_target_component_counts": Counter(),
        "outdeps_total": 0,
        "v3_dependency_edges": 0,
        "horizon_dependency_edges": 0,
    })

    for claim_id, claim in sorted(by_id.items(), key=lambda item: (first_seen[item[0]]["date"], item[0])):
        seen = first_seen[claim_id]
        claim_class = class_for(claim)
        claim_phase = phase_for(claim)
        deps = graph.get(claim_id, [])
        ev = evidence.get(claim_id, {})
        attention = claim_attention_for(claim_id)
        row = {
            "id": claim_id,
            "title": claim.get("title", ""),
            "type": claim.get("claim_type", "unknown"),
            "status": claim.get("status", "unknown"),
            "phase": claim_phase,
            "class": claim_class,
            "first_seen_date": seen["date"],
            "first_seen_week": seen["week"],
            "first_seen_commit": seen["commit"][:12],
            "first_seen_subject": seen["subject"],
            "component_id": claim_to_component[claim_id],
            "depends_on_count": len(deps),
            "depends_on": deps,
            "dependency_components": sorted({claim_to_component[dep] for dep in deps}),
            "genuine_exp_count": int(ev.get("genuine_exp_count", 0) or 0),
            "evidence_quadrant": ev.get("evidence_quadrant"),
            **attention,
        }
        claim_rows.append(row)

        wk = row["first_seen_week"]
        bucket = weekly[wk]
        bucket["new_claims"] += 1
        bucket["created_claim_ids"].append(claim_id)
        bucket["class_counts"][claim_class] += 1
        bucket["phase_counts"][claim_phase] += 1
        bucket["lifecycle_counts"][attention["lifecycle"]] += 1
        bucket["type_counts"][row["type"]] += 1
        bucket["status_counts"][row["status"]] += 1
        bucket["outdeps_total"] += len(deps)
        for dep in deps:
            target = by_id[dep]
            target_class = class_for(target)
            bucket["dependency_target_category_counts"][target_class] += 1
            bucket["dependency_target_claim_counts"][dep] += 1
            bucket["dependency_target_component_counts"][claim_to_component[dep]] += 1
            if phase_for(target) == "v3" or target.get("v3_pending") is True:
                bucket["v3_dependency_edges"] += 1
            if phase_for(target) in {"v4", "v5"}:
                bucket["horizon_dependency_edges"] += 1

    weeks = []
    for wk in sorted(weekly):
        item = weekly[wk]
        new_claims = item["new_claims"]
        weeks.append({
            "week_start": wk,
            "new_claims": new_claims,
            "avg_outdeps": round(item["outdeps_total"] / new_claims, 3) if new_claims else 0.0,
            "class_counts": counter_dict(item["class_counts"]),
            "phase_counts": counter_dict(item["phase_counts"]),
            "lifecycle_counts": counter_dict(item["lifecycle_counts"]),
            "type_counts": counter_dict(item["type_counts"]),
            "status_counts": counter_dict(item["status_counts"]),
            "dependency_target_category_counts": counter_dict(item["dependency_target_category_counts"]),
            "top_dependency_targets": [
                {
                    "claim_id": claim_id,
                    "count": count,
                    "title": by_id[claim_id].get("title", ""),
                    "class": class_for(by_id[claim_id]),
                    "phase": phase_for(by_id[claim_id]),
                    "status": by_id[claim_id].get("status", "unknown"),
                    "component_id": claim_to_component[claim_id],
                }
                for claim_id, count in item["dependency_target_claim_counts"].most_common(10)
            ],
            "top_dependency_components": [
                {"component_id": component_id, "count": count}
                for component_id, count in item["dependency_target_component_counts"].most_common(10)
            ],
            "v3_dependency_edges": item["v3_dependency_edges"],
            "horizon_dependency_edges": item["horizon_dependency_edges"],
        })

    recent_weeks = [w["week_start"] for w in weeks[-8:]]
    recent_claim_rows = [row for row in claim_rows if row["first_seen_week"] in recent_weeks]
    recent_target_counts: Counter[str] = Counter()
    recent_target_week_counts: dict[str, Counter[str]] = defaultdict(Counter)
    recent_target_sources: dict[str, list[dict[str, Any]]] = defaultdict(list)
    recent_component_counts: Counter[str] = Counter()
    recent_component_week_counts: dict[str, Counter[str]] = defaultdict(Counter)
    recent_component_sources: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in recent_claim_rows:
        source_digest = {
            "claim_id": row["id"],
            "title": row["title"],
            "class": row["class"],
            "lifecycle": row["lifecycle"],
            "phase": row["phase"],
            "status": row["status"],
            "first_seen_week": row["first_seen_week"],
            "component_id": row["component_id"],
        }
        for dep in graph[row["id"]]:
            recent_target_counts[dep] += 1
            recent_target_week_counts[dep][row["first_seen_week"]] += 1
            recent_target_sources[dep].append(source_digest)
            component_id = claim_to_component[dep]
            recent_component_counts[component_id] += 1
            recent_component_week_counts[component_id][row["first_seen_week"]] += 1
            recent_component_sources[component_id].append(source_digest)

    component_by_id = {component["component_id"]: component for component in components}

    def weekly_counts_payload(counter: Counter[str]) -> list[dict[str, Any]]:
        return [
            {"week_start": wk, "count": int(counter[wk])}
            for wk in sorted(counter)
        ]

    def recent_target_payload(claim_id: str, count: int) -> dict[str, Any]:
        week_counter = recent_target_week_counts[claim_id]
        sources = sorted(
            recent_target_sources[claim_id],
            key=lambda item: (item["first_seen_week"], item["claim_id"]),
            reverse=True,
        )
        return {
            **claim_digest(claim_id),
            "count": int(count),
            "week_count": len(week_counter),
            "weeks": weekly_counts_payload(week_counter),
            "recurrence": "recurrent" if len(week_counter) >= 2 else "single_week",
            "source_claims": sources[:18],
        }

    recurrent_target_ids = {
        claim_id
        for claim_id, counter in recent_target_week_counts.items()
        if len(counter) >= 2
    }
    recent_created_claims = []
    for row in sorted(recent_claim_rows, key=lambda item: (item["first_seen_week"], item["id"]), reverse=True):
        hub_targets = []
        for dep in graph[row["id"]]:
            week_counter = recent_target_week_counts[dep]
            hub_targets.append({
                **claim_digest(dep),
                "recent_dependency_count": int(recent_target_counts[dep]),
                "week_count": len(week_counter),
                "recurrence": "recurrent" if dep in recurrent_target_ids else "single_week",
            })
        hub_targets.sort(
            key=lambda item: (
                1 if item["recurrence"] == "recurrent" else 0,
                item["week_count"],
                item["recent_dependency_count"],
                item["claim_id"],
            ),
            reverse=True,
        )
        recent_created_claims.append({
            "claim_id": row["id"],
            "title": row["title"],
            "type": row["type"],
            "status": row["status"],
            "phase": row["phase"],
            "class": row["class"],
            "lifecycle": row["lifecycle"],
            "attention_rank": row["attention_rank"],
            "first_seen_date": row["first_seen_date"],
            "first_seen_week": row["first_seen_week"],
            "component_id": row["component_id"],
            "depends_on_count": row["depends_on_count"],
            "incoming_dependency_count": row["incoming_dependency_count"],
            "experiment_planned": row["experiment_planned"],
            "substrate_target": row["substrate_target"],
            "substrate_unblocked": row["substrate_unblocked"],
            "substrate_active": row["substrate_active"],
            "evidence_bearing": row["evidence_bearing"],
            "hub_targets": hub_targets,
        })

    recent_edge_count = sum(recent_target_counts.values())
    recurrent_edge_count = sum(
        recent_target_counts[claim_id]
        for claim_id in recurrent_target_ids
    )
    top_target_count = recent_target_counts.most_common(1)[0][1] if recent_target_counts else 0
    cyclic_target_edge_count = sum(
        count
        for claim_id, count in recent_target_counts.items()
        if component_by_id.get(claim_to_component[claim_id], {}).get("cyclic")
    )
    recent_class_counts = Counter(row["class"] for row in recent_claim_rows)
    recent_lifecycle_counts = Counter(row["lifecycle"] for row in recent_claim_rows)
    recent_horizon_claim_count = (
        recent_class_counts.get("horizon_v4", 0) + recent_class_counts.get("horizon_v5", 0)
    )
    recent_horizon_engineering_claim_count = sum(
        1
        for row in recent_claim_rows
        if row["class"] in {"horizon_v4", "horizon_v5"}
        and (
            row["experiment_planned"]
            or row["substrate_active"]
            or row["incoming_dependency_count"] >= 2
        )
    )
    recent_v3_claim_count = recent_class_counts.get("active_v3_closure", 0)
    recent_horizon_dependency_edges = sum(
        count
        for claim_id, count in recent_target_counts.items()
        if phase_for(by_id[claim_id]) in {"v4", "v5"}
    )
    recent_new_claim_count = len(recent_claim_rows)
    avg_outdeps_recent = round(recent_edge_count / recent_new_claim_count, 3) if recent_new_claim_count else 0.0
    recurrent_edge_share = round(recurrent_edge_count / recent_edge_count, 4) if recent_edge_count else 0.0
    top_target_share = round(top_target_count / recent_edge_count, 4) if recent_edge_count else 0.0
    cyclic_target_edge_share = round(cyclic_target_edge_count / recent_edge_count, 4) if recent_edge_count else 0.0
    horizon_claim_share = round(recent_horizon_claim_count / recent_new_claim_count, 4) if recent_new_claim_count else 0.0
    horizon_engineering_claim_share = round(recent_horizon_engineering_claim_count / recent_new_claim_count, 4) if recent_new_claim_count else 0.0
    horizon_dependency_share = round(recent_horizon_dependency_edges / recent_edge_count, 4) if recent_edge_count else 0.0
    v3_claim_share = round(recent_v3_claim_count / recent_new_claim_count, 4) if recent_new_claim_count else 0.0
    captured_claim_share = round(recent_lifecycle_counts.get("captured_only", 0) / recent_new_claim_count, 4) if recent_new_claim_count else 0.0
    active_work_claim_count = sum(
        recent_lifecycle_counts.get(key, 0)
        for key in ("experiment_planned", "substrate_implementation_active", "governance_evidence_bearing")
    )
    active_work_claim_share = round(active_work_claim_count / recent_new_claim_count, 4) if recent_new_claim_count else 0.0

    churn_pressure_score = min(100, round(
        35 * top_target_share
        + 35 * recurrent_edge_share
        + 20 * min(avg_outdeps_recent / 5.0, 1.0)
        + 10 * cyclic_target_edge_share
    ))
    if recent_new_claim_count == 0:
        churn_status = "unknown"
    elif (
        (top_target_share >= 0.25 and recurrent_edge_share >= 0.50)
        or (avg_outdeps_recent >= 4.5 and recurrent_edge_share >= 0.55)
    ):
        churn_status = "warning"
    elif (
        top_target_share >= 0.16
        or recurrent_edge_share >= 0.40
        or cyclic_target_edge_share >= 0.35
        or avg_outdeps_recent >= 3.5
    ):
        churn_status = "watch"
    else:
        churn_status = "stable"

    if recent_new_claim_count == 0:
        drift_status = "unknown"
    elif horizon_engineering_claim_share >= 0.12 or horizon_dependency_share >= 0.15:
        drift_status = "warning"
    elif horizon_engineering_claim_share >= 0.05 or horizon_dependency_share >= 0.05:
        drift_status = "watch"
    else:
        drift_status = "low"

    cycle_audit_counts = Counter(
        component.get("cycle_audit", {}).get("category", "acyclic")
        for component in components
        if component.get("cyclic")
    )
    cycle_cleanup_counts = Counter(
        component.get("cycle_audit", {}).get("cleanup_priority", "none")
        for component in components
        if component.get("cyclic")
    )

    payload = {
        "schema_version": "claim_dependency_process/v1",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source": {
            "claims_path": str(CLAIMS_GIT_PATH),
            "claims_count": len(by_id),
            "dependency_edges": edge_count,
            "component_edges": len(component_edges),
            "coupled_with_pairs": len(coupled_pairs),
            "git_head": run_git(["rev-parse", "--short", "HEAD"]).strip(),
        },
        "summary": {
            "claims_total": len(by_id),
            "dependency_edges": edge_count,
            "components_total": len(components),
            "cyclic_components": sum(1 for component in components if component["cyclic"]),
            "largest_component_size": max((component["size"] for component in components), default=0),
            "class_counts": counter_dict(Counter(row["class"] for row in claim_rows)),
            "phase_counts": counter_dict(Counter(row["phase"] for row in claim_rows)),
            "lifecycle_counts": counter_dict(Counter(row["lifecycle"] for row in claim_rows)),
            "cycle_audit_counts": counter_dict(cycle_audit_counts),
            "cycle_cleanup_counts": counter_dict(cycle_cleanup_counts),
            "coupled_with_pairs": len(coupled_pairs),
            "coupled_with_category_counts": counter_dict(coupled_category_counts),
            "coupled_with_cleanup_counts": counter_dict(coupled_cleanup_counts),
        },
        "weeks": weeks,
        "components": components,
        "component_edges": [
            {"source": source, "target": target}
            for source, target in sorted(component_edges)
        ],
        "claim_rows": claim_rows,
        "coupled_with": coupled_with_section,
        "recent": {
            "weeks": recent_weeks,
            "window": {
                "non_empty_week_count": len(recent_weeks),
                "start_week": recent_weeks[0] if recent_weeks else "",
                "end_week": recent_weeks[-1] if recent_weeks else "",
            },
            "created_claims": recent_created_claims,
            "metrics": {
                "new_claims": recent_new_claim_count,
                "dependency_edges": recent_edge_count,
                "avg_outdeps": avg_outdeps_recent,
                "v3_claims": int(recent_v3_claim_count),
                "v3_claim_share": v3_claim_share,
                "horizon_claims": int(recent_horizon_claim_count),
                "horizon_claim_share": horizon_claim_share,
                "horizon_engineering_claims": int(recent_horizon_engineering_claim_count),
                "horizon_engineering_claim_share": horizon_engineering_claim_share,
                "horizon_dependency_edges": int(recent_horizon_dependency_edges),
                "horizon_dependency_share": horizon_dependency_share,
                "captured_claims": int(recent_lifecycle_counts.get("captured_only", 0)),
                "captured_claim_share": captured_claim_share,
                "active_work_claims": int(active_work_claim_count),
                "active_work_claim_share": active_work_claim_share,
                "recurrent_hub_edges": int(recurrent_edge_count),
                "recurrent_hub_edge_share": recurrent_edge_share,
                "top_target_edge_share": top_target_share,
                "cyclic_target_edge_share": cyclic_target_edge_share,
                "lifecycle_counts": counter_dict(recent_lifecycle_counts),
            },
            "churn_health": {
                "status": churn_status,
                "pressure_score": int(churn_pressure_score),
                "top_target_share": top_target_share,
                "recurrent_hub_edge_share": recurrent_edge_share,
                "avg_outdeps": avg_outdeps_recent,
                "cyclic_target_edge_share": cyclic_target_edge_share,
            },
            "horizon_drift": {
                "status": drift_status,
                "claim_share": horizon_claim_share,
                "engineering_claim_share": horizon_engineering_claim_share,
                "dependency_share": horizon_dependency_share,
                "horizon_claims": int(recent_horizon_claim_count),
                "horizon_engineering_claims": int(recent_horizon_engineering_claim_count),
                "horizon_dependency_edges": int(recent_horizon_dependency_edges),
            },
            "top_dependency_targets": [
                recent_target_payload(claim_id, count)
                for claim_id, count in recent_target_counts.most_common(18)
            ],
            "recurrent_dependency_hubs": [
                recent_target_payload(claim_id, recent_target_counts[claim_id])
                for claim_id in sorted(
                    recurrent_target_ids,
                    key=lambda item: (
                        recent_target_counts[item],
                        len(recent_target_week_counts[item]),
                        item,
                    ),
                    reverse=True,
                )[:18]
            ],
            "top_dependency_components": [
                {
                    **component_by_id[component_id],
                    "recent_dependency_count": count,
                    "week_count": len(recent_component_week_counts[component_id]),
                    "weeks": weekly_counts_payload(recent_component_week_counts[component_id]),
                    "source_claims": sorted(
                        recent_component_sources[component_id],
                        key=lambda item: (item["first_seen_week"], item["claim_id"]),
                        reverse=True,
                    )[:18],
                }
                for component_id, count in recent_component_counts.most_common(12)
                if component_id in component_by_id
            ],
        },
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(f"Wrote {OUT_PATH.relative_to(ROOT)}")
    print(f"Claims: {len(by_id)}")
    print(f"Dependency edges: {edge_count}")
    print(f"SCC components: {len(components)}")
    print(f"Cyclic components: {payload['summary']['cyclic_components']}")
    cw = coupled_with_section["summary"]
    print(f"coupled_with pairs: {cw['pair_count']} (claims {cw['claim_count']}, clusters {cw['cluster_count']}, largest {cw['largest_cluster_size']})")
    print(f"coupled_with origin counts: {cw['origin_counts']}")
    print(f"coupled_with category counts: {cw['category_counts']}")
    print(f"coupled_with cleanup counts: {cw['cleanup_counts']}")
    print(f"cycle-break edges ({len(cycle_break_report)}) -- taxonomy label vs governance re-judgement:")
    for row in cycle_break_report:
        ratified = "RATIFIED" if row["ratified"] else "unratified"
        print(f"  {row['moved_edge']:<24} {row['category']:<34} {row['cleanup_priority']:<7} cluster {row['cluster_id']} (size {row['cluster_size']}) {ratified}")


if __name__ == "__main__":
    main()
