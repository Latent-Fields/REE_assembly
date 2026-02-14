#!/usr/bin/env python3
"""Build human-friendly structure review dossiers from architecture gap signals."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _parse_timestamp(raw: str) -> datetime:
    token = raw.strip()
    if token.endswith("Z"):
        token = token[:-1] + "+00:00"
    dt = datetime.fromisoformat(token)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _safe_float(value: Any, default: float = 0.0) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value).strip())
    except ValueError:
        return default


def _fmt_number(value: float) -> str:
    if float(value).is_integer():
        return str(int(value))
    return f"{value:.3f}".rstrip("0").rstrip(".")


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _load_claim_registry(path: Path) -> dict[str, dict[str, Any]]:
    """Parse key claim metadata from docs/claims/claims.yaml."""
    claims: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return claims

    current: dict[str, Any] | None = None
    in_depends = False

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if line.startswith("- id:"):
            if current:
                claims[str(current["id"])] = current
            current = {
                "id": line.split(":", 1)[1].strip(),
                "claim_type": "unknown",
                "status": "unknown",
                "subject": "",
                "location": "",
                "depends_on": [],
            }
            in_depends = False
            continue

        if current is None:
            continue

        if line.startswith("  claim_type:"):
            current["claim_type"] = line.split(":", 1)[1].strip()
            in_depends = False
            continue
        if line.startswith("  status:"):
            current["status"] = line.split(":", 1)[1].strip()
            in_depends = False
            continue
        if line.startswith("  subject:"):
            current["subject"] = line.split(":", 1)[1].strip()
            in_depends = False
            continue
        if line.startswith("  location:"):
            current["location"] = line.split(":", 1)[1].strip()
            in_depends = False
            continue
        if line.startswith("  depends_on:"):
            in_depends = True
            continue

        if in_depends and line.startswith("    - "):
            dep = line.split("-", 1)[1].strip()
            if dep:
                current["depends_on"].append(dep)
            continue

        if in_depends and (not line.startswith("    ") or line.startswith("  ")):
            in_depends = False

    if current:
        claims[str(current["id"])] = current
    return claims


def _dependents_map(claims: dict[str, dict[str, Any]]) -> dict[str, list[str]]:
    reverse: dict[str, list[str]] = defaultdict(list)
    for claim_id, meta in claims.items():
        for dep in meta.get("depends_on", []):
            reverse[str(dep)].append(claim_id)
    for claim_id in reverse:
        reverse[claim_id].sort()
    return dict(reverse)


def _scan_literature_records(root: Path) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    if not root.exists():
        return out
    for path in sorted(root.glob("**/entries/**/record.json")):
        data = _load_json(path)
        entry_id = str(data.get("entry_id", path.parent.name))
        source = data.get("source", {}) if isinstance(data, dict) else {}
        out[entry_id] = {
            "entry_id": entry_id,
            "literature_type": str(data.get("literature_type", "")),
            "title": str(source.get("title", "")),
            "authors": [str(a) for a in source.get("authors", []) if str(a).strip()],
            "year": source.get("year", ""),
            "venue": str(source.get("venue", "")),
            "doi": str(source.get("doi", "")),
            "url": str(source.get("url", "")),
        }
    return out


def _claim_summary_plain_english(claim_id: str, meta: dict[str, Any]) -> str:
    subject = str(meta.get("subject", "")).replace(".", " / ").replace("_", " ").strip()
    claim_type = str(meta.get("claim_type", "unknown"))
    claim_type_labels = {
        "architectural_commitment": "an architecture commitment",
        "mechanism_hypothesis": "a mechanism hypothesis",
        "open_question": "an open question",
        "implementation_note": "an implementation note",
        "invariant": "an invariant",
    }
    label = claim_type_labels.get(claim_type, "a claim")
    if subject:
        return f"{claim_id} is {label} about {subject}."
    return f"{claim_id} is {label} in the REE claim set."


def _claim_fit_plain_english(
    claim_id: str,
    meta: dict[str, Any],
    dependents: list[str],
) -> str:
    claim_type = str(meta.get("claim_type", "unknown"))
    type_role = {
        "architectural_commitment": "This sits in REE's architecture layer and constrains lower-level mechanism design.",
        "mechanism_hypothesis": "This sits in REE's mechanism layer and links architecture commitments to testable signatures.",
        "open_question": "This sits in REE's uncertainty layer and defines what remains unresolved before stronger commitments.",
        "implementation_note": "This sits in REE's implementation layer and constrains how architecture must be encoded.",
        "invariant": "This sits at REE's foundational layer and constrains all downstream claims.",
    }.get(claim_type, "This contributes to REE's overall claim stack.")

    deps = [str(x) for x in meta.get("depends_on", []) if str(x).strip()]
    dep_text = (
        f"It depends on {len(deps)} upstream claim(s): {', '.join(f'`{x}`' for x in deps)}."
        if deps
        else "It currently has no explicit upstream dependencies."
    )
    downstream_text = (
        f"It currently feeds {len(dependents)} downstream claim(s): {', '.join(f'`{x}`' for x in dependents)}."
        if dependents
        else "No downstream claims currently list it as a dependency."
    )
    location = str(meta.get("location", "")).strip()
    location_text = f"Primary architecture anchor: `{location}`." if location else ""
    bits = [type_role, dep_text, downstream_text]
    if location_text:
        bits.append(location_text)
    return " ".join(bits)


def _build_source_direction_counts(entries: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    out = {
        "experimental": {"supports": 0, "weakens": 0, "mixed": 0, "unknown": 0},
        "literature": {"supports": 0, "weakens": 0, "mixed": 0, "unknown": 0},
    }
    for entry in entries:
        source_type = str(entry.get("source_type", "experimental"))
        if source_type not in out:
            out[source_type] = {"supports": 0, "weakens": 0, "mixed": 0, "unknown": 0}
        direction = str(entry.get("evidence_direction", "unknown"))
        if direction not in out[source_type]:
            direction = "unknown"
        out[source_type][direction] += 1
    return out


def _direction_mix_narrative(direction_counts: dict[str, int]) -> str:
    supports = int(direction_counts.get("supports", 0))
    weakens = int(direction_counts.get("weakens", 0))
    mixed = int(direction_counts.get("mixed", 0))
    total = supports + weakens + mixed + int(direction_counts.get("unknown", 0))
    if total == 0:
        return "No linked evidence entries yet; this is a pure hypothesis zone."
    if supports > 0 and weakens > 0:
        return (
            "Evidence is directionally split between support and weakening, which indicates either "
            "claim over-breadth or hidden context dependence."
        )
    if supports > 0 and weakens == 0:
        return "Evidence is mostly convergent in support, with remaining uncertainty in scope and implementation."
    if weakens > 0 and supports == 0:
        return "Evidence is mostly convergent in weakening, suggesting the claim likely needs narrowing or revision."
    if mixed > 0:
        return "Evidence is primarily mixed, suggesting the mechanism may be condition-specific rather than universal."
    return "Evidence direction is currently unresolved."


def _source_mix_narrative(source_direction_counts: dict[str, dict[str, int]]) -> str:
    exp = source_direction_counts.get("experimental", {})
    lit = source_direction_counts.get("literature", {})
    exp_total = sum(int(v) for v in exp.values())
    lit_total = sum(int(v) for v in lit.values())
    if exp_total == 0 and lit_total == 0:
        return "No experimental or literature evidence is linked yet."
    if exp_total == 0:
        return "The picture is literature-heavy; confidence should be treated as provisional until run-pack evidence lands."
    if lit_total == 0:
        return "The picture is experiment-heavy; literature triangulation is still needed for stronger generalization claims."
    return (
        "Both experiment and literature are present. Use disagreement between these sources as a cue to refine claim scope "
        "before making status promotions."
    )


def _ree_translation(entry: dict[str, Any], subject_text: str) -> str:
    direction = str(entry.get("evidence_direction", "unknown"))
    if direction == "supports":
        return (
            f"In REE terms, this is positive pressure on `{subject_text}` and supports keeping the mechanism, "
            "with tighter boundary conditions where failures recur."
        )
    if direction == "weakens":
        return (
            f"In REE terms, this is negative pressure on `{subject_text}` and suggests the claim is likely too strong "
            "or missing a key gating variable."
        )
    if direction == "mixed":
        return (
            f"In REE terms, this implies `{subject_text}` may hold only in some regimes; "
            "the next step is to formalize those regimes explicitly."
        )
    return (
        f"In REE terms, this evidence is currently inconclusive for `{subject_text}` and should be treated as a monitoring signal."
    )


def _evidence_item_background(
    entry: dict[str, Any],
    literature_by_entry_id: dict[str, dict[str, Any]],
) -> str:
    source_type = str(entry.get("source_type", "experimental"))
    run_id = str(entry.get("run_id", ""))
    if source_type == "literature":
        meta = literature_by_entry_id.get(run_id, {})
        title = str(meta.get("title", ""))
        venue = str(meta.get("venue", ""))
        year = str(meta.get("year", ""))
        if title:
            venue_bits = ", ".join(x for x in [year, venue] if x)
            return f"{title} ({venue_bits})" if venue_bits else title
        return f"Literature entry `{run_id}`"
    exp_type = str(entry.get("experiment_type", ""))
    return f"Run-pack `{run_id}` in `{exp_type}`"


def _build_alternative_hypotheses(
    entries: list[dict[str, Any]],
    claim_subject: str,
) -> list[dict[str, Any]]:
    supports = sum(_safe_float(e.get("confidence", 0.5), 0.5) for e in entries if e.get("evidence_direction") == "supports")
    weakens = sum(_safe_float(e.get("confidence", 0.5), 0.5) for e in entries if e.get("evidence_direction") == "weakens")
    mixed = sum(_safe_float(e.get("confidence", 0.5), 0.5) for e in entries if e.get("evidence_direction") == "mixed")
    total = max(supports + weakens + mixed, 1e-9)

    support_conf = round(supports / total, 3)
    weaken_conf = round(weakens / total, 3)
    hybrid_conf = round(max(mixed / total, min(support_conf, weaken_conf)), 3)

    return [
        {
            "alternative_id": "ALT-01",
            "hypothesis": f"{claim_subject} is broadly correct, but failures are boundary-condition failures.",
            "current_findings": "Supporting evidence dominates enough to keep the core mechanism plausible.",
            "confidence_estimate": support_conf,
            "next_evidence_pull": [
                "Target stress regimes where failures cluster and test whether boundary constraints recover stability.",
                "Pull replication papers that test similar mechanisms under distribution shift.",
            ],
        },
        {
            "alternative_id": "ALT-02",
            "hypothesis": f"{claim_subject} is over-scoped and should be narrowed or split.",
            "current_findings": "Weakening evidence indicates at least one sub-regime where the current claim phrasing breaks.",
            "confidence_estimate": weaken_conf,
            "next_evidence_pull": [
                "Extract disconfirming sources and isolate the exact violated assumption.",
                "Run claim-splitting experiments with explicit sub-claim tags in manifests.",
            ],
        },
        {
            "alternative_id": "ALT-03",
            "hypothesis": f"A hybrid architecture is needed: keep the core of {claim_subject} but add explicit gating or interface separation.",
            "current_findings": "Mixed evidence and conflict patterns suggest partial validity with missing structural guardrails.",
            "confidence_estimate": hybrid_conf,
            "next_evidence_pull": [
                "Evaluate an ablation that isolates the proposed guardrail/interface addition.",
                "Collect one adjacent-domain source that uses a similar split architecture.",
            ],
        },
    ]


def _left_field_suggestions(claim_id: str) -> list[dict[str, str]]:
    specific: dict[str, list[dict[str, str]]] = {
        "MECH-059": [
            {
                "idea": "Run a two-agent internal market where one head bids uncertainty and another bids control precision.",
                "why_it_might_help": "Could expose whether uncertainty is being used as a genuine signal or as a score-gaming channel.",
                "first_test": "Add a toy arbitration layer and compare calibration drift against current single-head setup.",
            },
            {
                "idea": "Introduce uncertainty audits with synthetic adversarial ambiguity snapshots.",
                "why_it_might_help": "Could catch hidden calibration collapse earlier than aggregate loss metrics.",
                "first_test": "Inject ambiguity stress cases every N steps and track abstention reliability.",
            },
            {
                "idea": "Use a separately trained uncertainty critic that never sees policy loss.",
                "why_it_might_help": "Could reduce leakage from policy optimization into confidence estimates.",
                "first_test": "Compare uncertainty-channel leakage before/after adding the critic.",
            },
        ],
        "MECH-060": [
            {
                "idea": "Add a hard temporal write barrier after commit events.",
                "why_it_might_help": "Could reduce cross-channel contamination by forcing delayed attribution writes.",
                "first_test": "Ablate commit barrier windows and measure post-commit attribution gain.",
            },
            {
                "idea": "Tag each error packet with causal provenance tokens before learning attribution.",
                "why_it_might_help": "Could improve channel separation by preserving source traceability.",
                "first_test": "Track contamination signatures with and without provenance tags.",
            },
            {
                "idea": "Maintain physically separate replay buffers for pre-commit vs post-commit errors.",
                "why_it_might_help": "Could prevent accidental blending during optimization.",
                "first_test": "Run identical seeds with shared vs split replay and compare leakage rate.",
            },
        ],
        "MECH-058": [
            {
                "idea": "Try a three-timescale anchor (slow/medium/fast) with disagreement alarms.",
                "why_it_might_help": "Could reveal whether current failures come from anchor lag mismatch rather than anchor concept failure.",
                "first_test": "Measure drift and collapse signatures under timescale triad ablations.",
            },
            {
                "idea": "Introduce anchor reset checkpoints only on validated low-drift windows.",
                "why_it_might_help": "Could reduce catastrophic anchor drift under distribution shift.",
                "first_test": "Compare drift under continuous EMA vs gated reset.",
            },
            {
                "idea": "Use predictor ensembles to stress-test anchor stability assumptions.",
                "why_it_might_help": "Could separate target-anchor instability from predictor idiosyncrasy.",
                "first_test": "Track cluster collapse frequency across single vs ensemble predictor runs.",
            },
        ],
    }
    fallback = [
        {
            "idea": "Split the claim into two narrower claims and route evidence independently.",
            "why_it_might_help": "Can reduce hidden regime-mixing that creates persistent conflict ratios.",
            "first_test": "Create two scoped proposal tracks with explicit condition tags.",
        },
        {
            "idea": "Run one synthetic extreme-condition probe outside normal benchmark regime.",
            "why_it_might_help": "Can expose assumptions that are invisible in standard task distributions.",
            "first_test": "Add one adversarial scenario and compare signature incidence.",
        },
        {
            "idea": "Bring in one adjacent-domain analogy as an explicit design option, not just evidence.",
            "why_it_might_help": "Can surface architecture moves that current in-domain framing misses.",
            "first_test": "Add a parallel option in next governance packet and score it with the same gates.",
        },
    ]
    return specific.get(claim_id, fallback)


def _build_dossier(
    claim_id: str,
    gap_item: dict[str, Any],
    claim_meta: dict[str, Any],
    claim_registry_meta: dict[str, Any],
    dependents: list[str],
    entries: list[dict[str, Any]],
    literature_by_entry_id: dict[str, dict[str, Any]],
    generated_at: str,
    cycle_date: str,
) -> dict[str, Any]:
    direction_counts = claim_meta.get("direction_counts", {})
    source_direction_counts = _build_source_direction_counts(entries)

    subject_plain = str(claim_registry_meta.get("subject", "")).replace(".", " / ").replace("_", " ").strip()
    if not subject_plain:
        subject_plain = claim_id

    evidence_items: list[dict[str, Any]] = []
    sorted_entries = sorted(
        entries,
        key=lambda e: (str(e.get("timestamp_utc", "")), str(e.get("run_id", ""))),
        reverse=True,
    )
    for entry in sorted_entries[:10]:
        background = _evidence_item_background(entry, literature_by_entry_id)
        evidence_items.append(
            {
                "timestamp_utc": str(entry.get("timestamp_utc", "")),
                "source_type": str(entry.get("source_type", "experimental")),
                "source_background": background,
                "run_id": str(entry.get("run_id", "")),
                "experiment_type": str(entry.get("experiment_type", "")),
                "evidence_direction": str(entry.get("evidence_direction", "unknown")),
                "confidence": round(_safe_float(entry.get("confidence", 0.5), 0.5), 3),
                "source_wording": str(entry.get("confidence_rationale", "")),
                "ree_translation": _ree_translation(entry, subject_plain),
            }
        )

    alternatives = _build_alternative_hypotheses(entries, subject_plain)

    return {
        "schema_version": "structure_review_dossier/v1",
        "generated_at_utc": generated_at,
        "cycle_date": cycle_date,
        "claim": {
            "claim_id": claim_id,
            "claim_type": str(claim_registry_meta.get("claim_type", "unknown")),
            "status": str(claim_registry_meta.get("status", "unknown")),
            "subject": str(claim_registry_meta.get("subject", "")),
            "location": str(claim_registry_meta.get("location", "")),
            "depends_on": [str(x) for x in claim_registry_meta.get("depends_on", [])],
            "dependents": dependents,
            "plain_english_claim_description": _claim_summary_plain_english(claim_id, claim_registry_meta),
            "plain_english_ree_fit_description": _claim_fit_plain_english(claim_id, claim_registry_meta, dependents),
        },
        "structure_pressure": {
            "gap_id": str(gap_item.get("gap_id", "")),
            "recommendation": str(gap_item.get("recommendation", "")),
            "consider_new_structure": bool(gap_item.get("consider_new_structure", False)),
            "trigger_signals": [str(x) for x in gap_item.get("trigger_signals", [])],
            "conflict_ratio": round(_safe_float(gap_item.get("conflict_ratio", 0.0), 0.0), 3),
            "overall_confidence": round(_safe_float(gap_item.get("overall_confidence", 0.0), 0.0), 3),
            "source_counts": {
                "experimental": int(gap_item.get("source_counts", {}).get("experimental", 0)),
                "literature": int(gap_item.get("source_counts", {}).get("literature", 0)),
            },
            "recurring_failure_signatures": gap_item.get("recurring_failure_signatures", []),
            "latest_decision": gap_item.get("latest_decision", {}),
        },
        "evidence_overview": {
            "direction_counts": direction_counts,
            "source_direction_counts": source_direction_counts,
            "direction_mix_narrative": _direction_mix_narrative(direction_counts),
            "source_mix_narrative": _source_mix_narrative(source_direction_counts),
        },
        "evidence_items": evidence_items,
        "alternative_interpretations": alternatives,
        "left_field_suggestions": _left_field_suggestions(claim_id),
        "decision_prompts": [
            "Which part of the claim appears stable across both supporting and weakening evidence?",
            "If this claim were split into two sub-claims, where is the cleanest boundary?",
            "What is the smallest architecture change that would most likely remove the top recurring failure signature?",
            "What evidence next week would most likely change your current decision?",
        ],
    }


def _format_dossier_md(dossier: dict[str, Any]) -> str:
    claim = dossier.get("claim", {})
    pressure = dossier.get("structure_pressure", {})
    overview = dossier.get("evidence_overview", {})
    direction_counts = overview.get("direction_counts", {})
    source_direction_counts = overview.get("source_direction_counts", {})
    items = dossier.get("evidence_items", [])
    alternatives = dossier.get("alternative_interpretations", [])
    left_field = dossier.get("left_field_suggestions", [])

    lines: list[str] = []
    lines.append(f"# Structure Review Dossier: {claim.get('claim_id', '')}")
    lines.append("")
    lines.append(f"Generated: `{dossier.get('generated_at_utc', '')}`")
    lines.append(f"Cycle: `{dossier.get('cycle_date', '')}`")
    lines.append("")

    lines.append("## Claim Description")
    lines.append("")
    lines.append(str(claim.get("plain_english_claim_description", "")))
    lines.append("")

    lines.append("## Where This Fits in REE as a Whole")
    lines.append("")
    lines.append(str(claim.get("plain_english_ree_fit_description", "")))
    lines.append("")

    lines.append("## Structural Pressure Signals")
    lines.append("")
    lines.append(
        f"- Recommendation: `{pressure.get('recommendation', '')}` "
        + f"(consider_new_structure={str(bool(pressure.get('consider_new_structure', False))).lower()})"
    )
    lines.append(f"- Trigger signals: {', '.join(str(x) for x in pressure.get('trigger_signals', [])) or '-'}")
    lines.append(f"- Conflict ratio: {_fmt_number(_safe_float(pressure.get('conflict_ratio', 0.0), 0.0))}")
    lines.append(f"- Overall confidence: {_fmt_number(_safe_float(pressure.get('overall_confidence', 0.0), 0.0))}")
    lines.append("")

    lines.append("## Evidence Mix and Why It Looks This Way")
    lines.append("")
    lines.append(
        f"- Direction counts: supports={int(direction_counts.get('supports', 0))}, "
        + f"weakens={int(direction_counts.get('weakens', 0))}, "
        + f"mixed={int(direction_counts.get('mixed', 0))}, "
        + f"unknown={int(direction_counts.get('unknown', 0))}."
    )
    exp = source_direction_counts.get("experimental", {})
    lit = source_direction_counts.get("literature", {})
    lines.append(
        f"- Experimental mix: supports={int(exp.get('supports', 0))}, weakens={int(exp.get('weakens', 0))}, "
        + f"mixed={int(exp.get('mixed', 0))}, unknown={int(exp.get('unknown', 0))}."
    )
    lines.append(
        f"- Literature mix: supports={int(lit.get('supports', 0))}, weakens={int(lit.get('weakens', 0))}, "
        + f"mixed={int(lit.get('mixed', 0))}, unknown={int(lit.get('unknown', 0))}."
    )
    lines.append(f"- Direction narrative: {overview.get('direction_mix_narrative', '')}")
    lines.append(f"- Source narrative: {overview.get('source_mix_narrative', '')}")
    lines.append("")

    lines.append("## Evidence Pull (Current Findings + Alternatives)")
    lines.append("")
    lines.append("| alternative | confidence_estimate | current_findings | next_pull_focus |")
    lines.append("|---|---:|---|---|")
    for alt in alternatives:
        pulls = "; ".join(str(x) for x in alt.get("next_evidence_pull", []))
        lines.append(
            "| "
            + " | ".join(
                [
                    str(alt.get("hypothesis", "")).replace("|", "\\|"),
                    _fmt_number(_safe_float(alt.get("confidence_estimate", 0.0), 0.0)),
                    str(alt.get("current_findings", "")).replace("|", "\\|"),
                    pulls.replace("|", "\\|"),
                ]
            )
            + " |"
        )
    lines.append("")

    lines.append("## Source Wording vs REE Translation")
    lines.append("")
    lines.append("| timestamp | source | direction | confidence | evidence wording (preserved) | REE translation |")
    lines.append("|---|---|---|---:|---|---|")
    for item in items[:8]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item.get('timestamp_utc', '')}`",
                    str(item.get("source_background", "")).replace("|", "\\|"),
                    f"`{item.get('evidence_direction', '')}`",
                    _fmt_number(_safe_float(item.get("confidence", 0.0), 0.0)),
                    str(item.get("source_wording", "")).replace("|", "\\|"),
                    str(item.get("ree_translation", "")).replace("|", "\\|"),
                ]
            )
            + " |"
        )
    lines.append("")

    lines.append("## Left-Field Suggestions")
    lines.append("")
    for idx, idea in enumerate(left_field, start=1):
        lines.append(f"{idx}. {idea.get('idea', '')}")
        lines.append(f"- Why it may inspire: {idea.get('why_it_might_help', '')}")
        lines.append(f"- First test: {idea.get('first_test', '')}")
    lines.append("")

    lines.append("## Decision Prompts")
    lines.append("")
    for idx, prompt in enumerate(dossier.get("decision_prompts", []), start=1):
        lines.append(f"{idx}. {prompt}")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build structure review dossiers from architecture gap register.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
        help="Path to REE_assembly repository root.",
    )
    parser.add_argument(
        "--gap-register",
        default="evidence/planning/architecture_gap_register.v1.json",
        help="Path to architecture gap register JSON.",
    )
    parser.add_argument(
        "--claim-matrix",
        default="evidence/experiments/claim_evidence.v1.json",
        help="Path to claim evidence matrix JSON.",
    )
    parser.add_argument(
        "--claims-file",
        default="docs/claims/claims.yaml",
        help="Path to claim registry YAML.",
    )
    parser.add_argument(
        "--output-root",
        default="evidence/planning/structure_review",
        help="Output root for generated dossiers.",
    )
    parser.add_argument(
        "--cycle-date",
        default="auto",
        help="Cycle date label (YYYY-MM-DD) or auto.",
    )
    parser.add_argument(
        "--include-monitor",
        action="store_true",
        help="Include non-triggered architecture register items as dossiers.",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    gap_register_path = repo_root / args.gap_register
    claim_matrix_path = repo_root / args.claim_matrix
    claims_path = repo_root / args.claims_file
    output_root = repo_root / args.output_root

    gap_doc = _load_json(gap_register_path)
    matrix = _load_json(claim_matrix_path)
    claims = _load_claim_registry(claims_path)
    dependents = _dependents_map(claims)
    literature_map = _scan_literature_records(repo_root / "evidence/literature")

    generated_at = _now_utc()
    gap_generated = str(gap_doc.get("generated_at_utc", generated_at))
    if args.cycle_date == "auto":
        cycle_date = gap_generated[:10]
    else:
        cycle_date = args.cycle_date

    register_items = gap_doc.get("items", []) if isinstance(gap_doc, dict) else []
    selected_items: list[dict[str, Any]] = []
    for item in register_items:
        if args.include_monitor or bool(item.get("consider_new_structure", False)):
            selected_items.append(item)

    selected_items.sort(
        key=lambda item: (
            0 if bool(item.get("consider_new_structure", False)) else 1,
            -_safe_float(item.get("conflict_ratio", 0.0), 0.0),
            str(item.get("claim_id", "")),
        )
    )

    claim_entries_by_id: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in matrix.get("entries", []):
        claim_id = str(entry.get("claim_id", "")).strip()
        if claim_id:
            claim_entries_by_id[claim_id].append(entry)

    out_dir = output_root / cycle_date
    out_dir.mkdir(parents=True, exist_ok=True)

    report_items: list[dict[str, Any]] = []
    index_lines: list[str] = []
    index_lines.append("# Structure Review Dossier Index")
    index_lines.append("")
    index_lines.append(f"Generated: `{generated_at}`")
    index_lines.append(f"Cycle: `{cycle_date}`")
    index_lines.append("")
    index_lines.append(
        "These dossiers are designed to support human judgment when claims show structural pressure in the evidence stream."
    )
    index_lines.append("")
    index_lines.append("| claim_id | status | recommendation | consider_new_structure | dossier |")
    index_lines.append("|---|---|---|---|---|")

    if not selected_items:
        index_lines.append("| _none_ | - | - | - | - |")
    else:
        for item in selected_items:
            claim_id = str(item.get("claim_id", "")).strip()
            if not claim_id:
                continue
            registry_meta = claims.get(
                claim_id,
                {
                    "claim_type": str(item.get("claim_type", "unknown")),
                    "status": str(item.get("current_status", "unknown")),
                    "subject": "",
                    "location": "",
                    "depends_on": [],
                },
            )
            claim_meta = matrix.get("claims", {}).get(claim_id, {})
            entries = claim_entries_by_id.get(claim_id, [])
            dossier = _build_dossier(
                claim_id=claim_id,
                gap_item=item,
                claim_meta=claim_meta,
                claim_registry_meta=registry_meta,
                dependents=dependents.get(claim_id, []),
                entries=entries,
                literature_by_entry_id=literature_map,
                generated_at=generated_at,
                cycle_date=cycle_date,
            )

            claim_dir = out_dir / claim_id
            claim_dir.mkdir(parents=True, exist_ok=True)
            dossier_json_path = claim_dir / "dossier.v1.json"
            dossier_md_path = claim_dir / "DOSSIER.md"
            dossier_json_path.write_text(
                json.dumps(dossier, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            dossier_md_path.write_text(_format_dossier_md(dossier), encoding="utf-8")

            rel_md = dossier_md_path.relative_to(repo_root).as_posix()
            index_lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{claim_id}`",
                        f"`{registry_meta.get('status', 'unknown')}`",
                        f"`{item.get('recommendation', '')}`",
                        "yes" if bool(item.get("consider_new_structure", False)) else "no",
                        f"`{rel_md}`",
                    ]
                )
                + " |"
            )
            report_items.append(
                {
                    "claim_id": claim_id,
                    "consider_new_structure": bool(item.get("consider_new_structure", False)),
                    "recommendation": str(item.get("recommendation", "")),
                    "dossier_json_path": dossier_json_path.as_posix(),
                    "dossier_md_path": dossier_md_path.as_posix(),
                }
            )

    index_path = out_dir / "INDEX.md"
    index_path.write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")

    latest_dir = output_root / "latest"
    latest_dir.mkdir(parents=True, exist_ok=True)
    (latest_dir / "INDEX.md").write_text(index_path.read_text(encoding="utf-8"), encoding="utf-8")

    report = {
        "schema_version": "structure_review_report/v1",
        "generated_at_utc": generated_at,
        "cycle_date": cycle_date,
        "source": {
            "gap_register": gap_register_path.as_posix(),
            "claim_matrix": claim_matrix_path.as_posix(),
            "claims_file": claims_path.as_posix(),
        },
        "items_total": len(report_items),
        "consider_new_structure_total": sum(
            1 for item in report_items if bool(item.get("consider_new_structure", False))
        ),
        "output_dir": out_dir.as_posix(),
        "items": report_items,
    }
    report_path = out_dir / "structure_review_report.v1.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (latest_dir / "structure_review_report.v1.json").write_text(
        report_path.read_text(encoding="utf-8"), encoding="utf-8"
    )

    print(f"Wrote structure review dossiers: {out_dir.as_posix()}")
    print(f"Wrote report: {report_path.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

