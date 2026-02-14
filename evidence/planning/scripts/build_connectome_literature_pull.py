#!/usr/bin/env python3
"""Build connectome-oriented literature pull queue from architecture pressure signals."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _fmt_number(value: float) -> str:
    if float(value).is_integer():
        return str(int(value))
    return f"{value:.3f}".rstrip("0").rstrip(".")


def _safe_float(value: Any, default: float = 0.0) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value).strip())
    except ValueError:
        return default


def _load_claim_registry(path: Path) -> dict[str, dict[str, Any]]:
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
    out: dict[str, list[str]] = defaultdict(list)
    for claim_id, meta in claims.items():
        for dep in meta.get("depends_on", []):
            out[str(dep)].append(claim_id)
    for key in out:
        out[key].sort()
    return dict(out)


def _claim_summary_plain_english(claim_id: str, meta: dict[str, Any]) -> str:
    subject = str(meta.get("subject", "")).replace(".", " / ").replace("_", " ").strip()
    claim_type = str(meta.get("claim_type", "unknown"))
    labels = {
        "architectural_commitment": "an architecture commitment",
        "mechanism_hypothesis": "a mechanism hypothesis",
        "open_question": "an open question",
        "implementation_note": "an implementation note",
        "invariant": "an invariant",
    }
    label = labels.get(claim_type, "a claim")
    if subject:
        return f"{claim_id} is {label} about {subject}."
    return f"{claim_id} is {label} in REE."


def _claim_fit_plain_english(
    meta: dict[str, Any],
    dependents: list[str],
) -> str:
    claim_type = str(meta.get("claim_type", "unknown"))
    role = {
        "architectural_commitment": "This is in REE's architecture layer and constrains mechanism choices.",
        "mechanism_hypothesis": "This is in REE's mechanism layer and ties architecture commitments to testable signatures.",
        "open_question": "This is in REE's uncertainty layer and defines unresolved boundaries before promotion.",
        "implementation_note": "This is in REE's implementation layer and constrains how architecture should be encoded.",
        "invariant": "This is in REE's invariant layer and constrains all downstream design choices.",
    }.get(claim_type, "This contributes to REE's overall reasoning stack.")

    upstream = [str(x) for x in meta.get("depends_on", []) if str(x).strip()]
    upstream_text = (
        f"It depends on {len(upstream)} upstream claim(s): {', '.join(f'`{x}`' for x in upstream)}."
        if upstream
        else "It currently has no explicit upstream dependencies."
    )
    downstream_text = (
        f"It currently influences {len(dependents)} downstream claim(s): "
        + f"{', '.join(f'`{x}`' for x in dependents)}."
        if dependents
        else "No downstream claims currently list it as a dependency."
    )
    location = str(meta.get("location", "")).strip()
    location_text = f"Primary anchor: `{location}`." if location else ""
    bits = [role, upstream_text, downstream_text]
    if location_text:
        bits.append(location_text)
    return " ".join(bits)


def _connectome_templates(claim_id: str, claim_subject: str) -> dict[str, Any]:
    specific: dict[str, dict[str, Any]] = {
        "MECH-059": {
            "focus": "Identify circuit motifs that separate mismatch coding from confidence-weighting pathways.",
            "questions": [
                "Where do connectome-informed studies suggest dissociable pathways for error coding versus confidence modulation?",
                "Which neuromodulatory/cortical loops look most consistent with confidence gating rather than pure error emission?",
                "What evidence shows confidence weighting is context-sensitive rather than a direct transform of one residual stream?",
            ],
            "tracks": [
                {
                    "track_id": "TRK-01",
                    "focus": "Structural and effective connectivity for confidence gating",
                    "query_stems": [
                        "connectome confidence weighting prediction error dissociation",
                        "effective connectivity uncertainty confidence coding cortex",
                    ],
                },
                {
                    "track_id": "TRK-02",
                    "focus": "Neuromodulatory precision/confidence pathways",
                    "query_stems": [
                        "dopamine noradrenaline acetylcholine precision uncertainty circuit",
                        "hierarchical predictive coding confidence pathway connectomics",
                    ],
                },
                {
                    "track_id": "TRK-03",
                    "focus": "Computational analogues constrained by biological circuitry",
                    "query_stems": [
                        "biologically constrained uncertainty calibration neural circuits",
                        "circuit-inspired confidence channel machine learning",
                    ],
                },
            ],
        },
        "MECH-060": {
            "focus": "Identify circuit evidence for separating planning-time error processing from outcome-attribution learning signals.",
            "questions": [
                "Which circuit pathways support pre-decision simulation/error evaluation versus post-outcome attribution updates?",
                "Where does evidence indicate partial blending, and what boundary conditions separate channels best?",
                "What anatomical or effective-connectivity findings constrain dual-channel implementations?",
            ],
            "tracks": [
                {
                    "track_id": "TRK-01",
                    "focus": "Prefrontal-striatal-thalamic pathways for planning vs attribution",
                    "query_stems": [
                        "prefrontal striatal planning outcome attribution connectivity",
                        "model-based model-free error pathways effective connectivity",
                    ],
                },
                {
                    "track_id": "TRK-02",
                    "focus": "Commitment and action-monitoring circuit separation",
                    "query_stems": [
                        "anterior cingulate commitment monitoring prediction error channel",
                        "efference copy outcome evaluation circuit dissociation",
                    ],
                },
                {
                    "track_id": "TRK-03",
                    "focus": "Cross-species connectome findings for dual-channel control",
                    "query_stems": [
                        "cross-species connectome decision learning pathway separation",
                        "rodent primate planning attribution neural pathway comparison",
                    ],
                },
            ],
        },
    }

    if claim_id in specific:
        return specific[claim_id]

    return {
        "focus": f"Find connectome-constrained evidence that can confirm, refute, or refine `{claim_subject}`.",
        "questions": [
            "Which pathways in connectome/effective-connectivity findings are most relevant to this claim's mechanism?",
            "What results directly contradict a literal REE mapping of this claim?",
            "Which circuit motifs inspire a cleaner architecture split or guardrail in REE?",
        ],
        "tracks": [
            {
                "track_id": "TRK-01",
                "focus": "Structural and effective-connectivity constraints",
                "query_stems": [
                    f"{claim_id} connectome effective connectivity",
                    f"{claim_subject} neural pathway dissociation",
                ],
            },
            {
                "track_id": "TRK-02",
                "focus": "Computational-neuroscience bridge papers",
                "query_stems": [
                    f"{claim_subject} computational neuroscience circuit model",
                    f"{claim_id} predictive coding pathway evidence",
                ],
            },
            {
                "track_id": "TRK-03",
                "focus": "Disconfirming/alternative pathway evidence",
                "query_stems": [
                    f"{claim_subject} conflicting neural evidence",
                    f"{claim_id} alternative mechanism neural circuits",
                ],
            },
        ],
    }


def _priority_for_gap(gap_item: dict[str, Any]) -> str:
    if bool(gap_item.get("consider_new_structure", False)):
        return "high"
    conflict_ratio = _safe_float(gap_item.get("conflict_ratio", 0.0), 0.0)
    if conflict_ratio >= 0.7:
        return "high"
    if conflict_ratio >= 0.5:
        return "medium"
    return "low"


def _build_item(
    idx: int,
    gap_item: dict[str, Any],
    claim_meta: dict[str, Any],
    registry_meta: dict[str, Any],
    dependents: list[str],
) -> dict[str, Any]:
    claim_id = str(gap_item.get("claim_id", "")).strip()
    claim_subject = str(registry_meta.get("subject", "")).replace(".", " / ").replace("_", " ").strip()
    if not claim_subject:
        claim_subject = claim_id

    template = _connectome_templates(claim_id, claim_subject)
    direction_counts = claim_meta.get("direction_counts", {})
    source_counts = claim_meta.get("source_counts", {})

    recurring = gap_item.get("recurring_failure_signatures", [])
    recurring_tokens = [str(x.get("signature", "")) for x in recurring if str(x.get("signature", "")).strip()]

    return {
        "pull_id": f"CPULL-{idx:04d}",
        "claim_id": claim_id,
        "priority": _priority_for_gap(gap_item),
        "status": "proposed",
        "target_repo": "REE_assembly",
        "objective": f"Run targeted connectome literature pull for {claim_id}.",
        "suggested_literature_type": f"targeted_review_connectome_{claim_id.lower().replace('-', '_')}",
        "plain_english_claim_description": _claim_summary_plain_english(claim_id, registry_meta),
        "plain_english_ree_fit_description": _claim_fit_plain_english(registry_meta, dependents),
        "selection_signals": {
            "consider_new_structure": bool(gap_item.get("consider_new_structure", False)),
            "trigger_signals": [str(x) for x in gap_item.get("trigger_signals", [])],
            "conflict_ratio": round(_safe_float(gap_item.get("conflict_ratio", 0.0), 0.0), 3),
            "overall_confidence": round(_safe_float(gap_item.get("overall_confidence", 0.0), 0.0), 3),
            "direction_counts": {
                "supports": int(direction_counts.get("supports", 0)),
                "weakens": int(direction_counts.get("weakens", 0)),
                "mixed": int(direction_counts.get("mixed", 0)),
                "unknown": int(direction_counts.get("unknown", 0)),
            },
            "source_counts": {
                "experimental": int(source_counts.get("experimental", 0)),
                "literature": int(source_counts.get("literature", 0)),
            },
            "recurring_failure_signatures": recurring_tokens[:5],
        },
        "connectome_focus": str(template.get("focus", "")),
        "research_questions": [str(x) for x in template.get("questions", [])],
        "search_tracks": [
            {
                "track_id": str(track.get("track_id", "")),
                "focus": str(track.get("focus", "")),
                "source_preference": "primary",
                "query_stems": [str(q) for q in track.get("query_stems", [])],
            }
            for track in template.get("tracks", [])
        ],
        "required_record_contract": {
            "record": [
                "claim_ids_tested",
                "evidence_class",
                "evidence_direction",
                "confidence",
                "confidence_rationale",
                "mapping",
                "confidence_components",
            ],
            "mapping_fields": [
                "mapping.source_claim_statement",
                "mapping.ree_translation",
                "mapping.mapping_caveat",
            ],
            "confidence_component_fields": [
                "confidence_components.source_quality",
                "confidence_components.mapping_fidelity",
                "confidence_components.transfer_risk",
            ],
            "summary": "preserve source wording and add REE translation with caveat boundaries",
        },
        "acceptance_checks": [
            "At least 3 primary sources per claim pull (peer-reviewed journals, major conference papers, or canonical preprints).",
            "At least 1 disconfirming or mixed-direction source is included.",
            "Each record includes mapping + confidence_components fields.",
            "Summary includes source wording, REE translation, and explicit mapping caveat.",
            "No duplicate DOI+claim linkage unless rationale is materially different.",
        ],
    }


def _format_markdown(doc: dict[str, Any]) -> str:
    generated_at = str(doc.get("generated_at_utc", ""))
    cycle_date = str(doc.get("cycle_date", ""))
    items = doc.get("items", [])

    lines: list[str] = []
    lines.append("# Connectome Literature Pull Queue")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append(f"Cycle: `{cycle_date}`")
    lines.append("")
    lines.append(
        "This queue prioritizes connectome/effective-connectivity evidence pulls for claims under architecture pressure."
    )
    lines.append("")
    lines.append("| pull_id | claim_id | priority | consider_new_structure | conflict_ratio | suggested_literature_type |")
    lines.append("|---|---|---|---|---:|---|")
    if not items:
        lines.append("| _none_ | - | - | - | - | - |")
    else:
        for item in items:
            signals = item.get("selection_signals", {})
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{item.get('pull_id', '')}`",
                        f"`{item.get('claim_id', '')}`",
                        f"`{item.get('priority', '')}`",
                        "yes" if bool(signals.get("consider_new_structure", False)) else "no",
                        _fmt_number(_safe_float(signals.get("conflict_ratio", 0.0), 0.0)),
                        f"`{item.get('suggested_literature_type', '')}`",
                    ]
                )
                + " |"
            )
    lines.append("")

    for item in items:
        claim_id = str(item.get("claim_id", ""))
        lines.append(f"## {claim_id}")
        lines.append("")
        lines.append(f"- Pull ID: `{item.get('pull_id', '')}`")
        lines.append(f"- Objective: {item.get('objective', '')}")
        lines.append(f"- Claim description: {item.get('plain_english_claim_description', '')}")
        lines.append(f"- REE fit: {item.get('plain_english_ree_fit_description', '')}")
        signals = item.get("selection_signals", {})
        lines.append(
            "- Evidence pressure: "
            + f"conflict_ratio={_fmt_number(_safe_float(signals.get('conflict_ratio', 0.0), 0.0))}, "
            + f"overall_confidence={_fmt_number(_safe_float(signals.get('overall_confidence', 0.0), 0.0))}, "
            + f"trigger_signals={','.join(str(x) for x in signals.get('trigger_signals', [])) or '-'}."
        )
        recurring = signals.get("recurring_failure_signatures", [])
        if recurring:
            lines.append(f"- Recurring failure signatures: {', '.join(f'`{x}`' for x in recurring)}")
        lines.append(f"- Connectome focus: {item.get('connectome_focus', '')}")
        lines.append("- Research questions:")
        for q in item.get("research_questions", []):
            lines.append(f"  - {q}")
        lines.append("- Search tracks:")
        for track in item.get("search_tracks", []):
            lines.append(
                f"  - `{track.get('track_id', '')}` {track.get('focus', '')}; "
                + f"query stems: {', '.join(f'`{x}`' for x in track.get('query_stems', []))}"
            )
        lines.append("")

    lines.append("## Copy/Paste Prompt")
    lines.append("")
    lines.append("```md")
    lines.append("You are Codex operating in `REE_assembly`.")
    lines.append("")
    lines.append("Goal: execute the current connectome literature pull queue and emit contract-valid literature entries.")
    lines.append("")
    lines.append("Contract requirements:")
    lines.append("- `evidence/literature/INTERFACE_CONTRACT.md`")
    lines.append("- `evidence/literature/schemas/v1/literature_evidence.schema.json`")
    lines.append("")
    lines.append("Queue items:")
    for item in items:
        lines.append(
            f"- `{item.get('pull_id', '')}` / `{item.get('claim_id', '')}` / `{item.get('suggested_literature_type', '')}`"
        )
    lines.append("")
    lines.append("Per-entry requirements (mandatory):")
    lines.append("- preserve source wording in summary and add explicit REE translation")
    lines.append("- include mapping fields in `record.json`:")
    lines.append("  - `mapping.source_claim_statement`")
    lines.append("  - `mapping.ree_translation`")
    lines.append("  - `mapping.mapping_caveat`")
    lines.append("- include confidence split in `record.json`:")
    lines.append("  - `confidence_components.source_quality`")
    lines.append("  - `confidence_components.mapping_fidelity`")
    lines.append("  - `confidence_components.transfer_risk`")
    lines.append("- include at least 3 primary sources and 1 disconfirming/mixed source per claim pull")
    lines.append("")
    lines.append("After entry creation run:")
    lines.append("- `python3 evidence/experiments/scripts/build_experiment_indexes.py`")
    lines.append("- `python3 evidence/planning/scripts/build_structure_review_dossiers.py`")
    lines.append("- `python3 evidence/planning/scripts/build_connectome_literature_pull.py`")
    lines.append("- `python3 evidence/planning/scripts/run_governance_cycle.py`")
    lines.append("```")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build connectome literature pull queue from architecture gap register."
    )
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
        help="Path to claim registry file.",
    )
    parser.add_argument(
        "--output-json",
        default="evidence/planning/connectome_literature_pull.v1.json",
        help="Output JSON path.",
    )
    parser.add_argument(
        "--output-md",
        default="evidence/planning/CONNECTOME_LITERATURE_PULL.md",
        help="Output markdown path.",
    )
    parser.add_argument(
        "--include-monitor",
        action="store_true",
        help="Include non-triggered architecture gap items.",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    gap_doc = _load_json(repo_root / args.gap_register)
    matrix = _load_json(repo_root / args.claim_matrix)
    claims = _load_claim_registry(repo_root / args.claims_file)
    dependents = _dependents_map(claims)

    generated_at = _now_utc()
    cycle_date = str(gap_doc.get("generated_at_utc", generated_at))[:10]

    gap_items = gap_doc.get("items", []) if isinstance(gap_doc, dict) else []
    selected: list[dict[str, Any]] = []
    for gap_item in gap_items:
        if args.include_monitor or bool(gap_item.get("consider_new_structure", False)):
            selected.append(gap_item)

    selected.sort(
        key=lambda item: (
            0 if bool(item.get("consider_new_structure", False)) else 1,
            -_safe_float(item.get("conflict_ratio", 0.0), 0.0),
            str(item.get("claim_id", "")),
        )
    )

    items: list[dict[str, Any]] = []
    matrix_claims = matrix.get("claims", {}) if isinstance(matrix, dict) else {}
    for idx, gap_item in enumerate(selected, start=1):
        claim_id = str(gap_item.get("claim_id", "")).strip()
        if not claim_id:
            continue
        claim_meta = matrix_claims.get(claim_id, {})
        registry_meta = claims.get(
            claim_id,
            {
                "claim_type": str(gap_item.get("claim_type", "unknown")),
                "status": str(gap_item.get("current_status", "unknown")),
                "subject": "",
                "location": "",
                "depends_on": [],
            },
        )
        items.append(
            _build_item(
                idx=idx,
                gap_item=gap_item,
                claim_meta=claim_meta,
                registry_meta=registry_meta,
                dependents=dependents.get(claim_id, []),
            )
        )

    doc = {
        "schema_version": "connectome_literature_pull/v1",
        "generated_at_utc": generated_at,
        "cycle_date": cycle_date,
        "source": {
            "gap_register": (repo_root / args.gap_register).as_posix(),
            "claim_matrix": (repo_root / args.claim_matrix).as_posix(),
            "claims_file": (repo_root / args.claims_file).as_posix(),
        },
        "selection": {
            "mode": "consider_new_structure_only" if not args.include_monitor else "include_monitor",
            "consider_new_structure_items": sum(
                1 for item in selected if bool(item.get("consider_new_structure", False))
            ),
            "total_selected_items": len(items),
        },
        "items": items,
    }

    output_json_path = repo_root / args.output_json
    output_md_path = repo_root / args.output_md
    output_json_path.parent.mkdir(parents=True, exist_ok=True)
    output_md_path.parent.mkdir(parents=True, exist_ok=True)
    output_json_path.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    output_md_path.write_text(_format_markdown(doc), encoding="utf-8")

    print(f"Wrote connectome literature pull JSON: {output_json_path.as_posix()}")
    print(f"Wrote connectome literature pull MD: {output_md_path.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

