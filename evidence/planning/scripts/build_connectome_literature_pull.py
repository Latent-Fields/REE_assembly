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


def _safe_bool(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    token = str(value).strip().lower()
    if token in {"1", "true", "yes", "on"}:
        return True
    if token in {"0", "false", "no", "off"}:
        return False
    return default


def _string_list(value: Any) -> list[str]:
    out: list[str] = []
    if isinstance(value, list):
        candidates = value
    else:
        candidates = []
    for item in candidates:
        token = str(item).strip()
        if token and token not in out:
            out.append(token)
    return out


def _load_connectome_completion_settings(
    planning_criteria: dict[str, Any],
) -> dict[str, float | int]:
    thresholds = (
        planning_criteria.get("thresholds", {})
        if isinstance(planning_criteria, dict)
        else {}
    )
    if not isinstance(thresholds, dict):
        thresholds = {}
    return {
        "min_entries": max(1, int(thresholds.get("connectome_pull_completion_min_entries", 4))),
        "min_support_entries": max(
            1, int(thresholds.get("connectome_pull_completion_min_support_entries", 1))
        ),
        "min_non_support_entries": max(
            1, int(thresholds.get("connectome_pull_completion_min_non_support_entries", 1))
        ),
        "reopen_conflict_ratio": float(
            thresholds.get("connectome_pull_reopen_conflict_ratio", 0.9)
        ),
    }


def _load_connectome_manual_seed_settings(
    planning_criteria: dict[str, Any],
) -> dict[str, Any]:
    pull_cfg = planning_criteria.get("connectome_pull", {}) if isinstance(planning_criteria, dict) else {}
    if not isinstance(pull_cfg, dict):
        pull_cfg = {}

    raw_claim_ids = pull_cfg.get("manual_claim_ids", [])
    claim_ids = _string_list(raw_claim_ids)

    priority = str(pull_cfg.get("manual_priority", "high")).strip().lower()
    if priority not in {"high", "medium", "low"}:
        priority = "high"

    trigger_signal = str(pull_cfg.get("manual_trigger_signal", "manual_mode_transition_pull")).strip()
    if not trigger_signal:
        trigger_signal = "manual_mode_transition_pull"

    adjudicated_claim_ids = _string_list(
        pull_cfg.get("manual_claim_ids_adjudicated", pull_cfg.get("adjudicated_claim_ids", []))
    )
    require_adjudication = _safe_bool(
        pull_cfg.get("manual_require_adjudication_for_completion", True),
        default=True,
    )

    return {
        "claim_ids": claim_ids,
        "priority": priority,
        "trigger_signal": trigger_signal,
        "adjudicated_claim_ids": adjudicated_claim_ids,
        "require_adjudication_for_completion": require_adjudication,
    }


def _count_literature_completion(
    repo_root: Path,
    literature_type: str,
    claim_id: str,
) -> dict[str, Any]:
    entries_root = repo_root / "evidence" / "literature" / literature_type / "entries"
    counts = {
        "entries_total": 0,
        "non_support_entries": 0,
        "latest_timestamp_utc": "",
    }
    if not entries_root.exists():
        return counts

    latest_ts = ""
    for record_path in sorted(entries_root.glob("**/record.json")):
        payload = _load_json(record_path)
        if claim_id not in payload.get("claim_ids_tested", []):
            continue
        counts["entries_total"] += 1
        direction = str(payload.get("evidence_direction", "unknown")).strip().lower()
        if direction in {"weakens", "mixed"}:
            counts["non_support_entries"] += 1
        ts = str(payload.get("timestamp_utc", "")).strip()
        if ts and ts > latest_ts:
            latest_ts = ts

    counts["latest_timestamp_utc"] = latest_ts
    return counts


def _load_state(path: Path) -> dict[str, dict[str, Any]]:
    payload = _load_json(path)
    items = payload.get("items", []) if isinstance(payload, dict) else []
    out: dict[str, dict[str, Any]] = {}
    for item in items:
        if not isinstance(item, dict):
            continue
        claim_id = str(item.get("claim_id", "")).strip()
        if claim_id:
            out[claim_id] = item
    return out


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
        "ARC-016": {
            "focus": "Map control-plane cognitive modes to empirically constrained network-control regimes and transition signatures.",
            "questions": [
                "Which large-scale network control findings support regime-like mode organization over shared predictive machinery?",
                "What effective-connectivity signatures best mark transitions between task, DMN-like, vigilance, and offline regimes?",
                "Which findings contradict strict discrete-mode assumptions and imply quasi-continuous landscapes?",
            ],
            "tracks": [
                {
                    "track_id": "TRK-01",
                    "focus": "Triple-network and salience-control switching evidence",
                    "query_stems": [
                        "triple network salience switching default mode executive control",
                        "effective connectivity mode transition salience network",
                    ],
                },
                {
                    "track_id": "TRK-02",
                    "focus": "Connectome gradients and controllability constraints",
                    "query_stems": [
                        "connectome gradient default mode control network transition",
                        "network controllability cognitive state transitions connectome",
                    ],
                },
                {
                    "track_id": "TRK-03",
                    "focus": "Disconfirming evidence for strict regime separability",
                    "query_stems": [
                        "continuous cognitive state manifold versus discrete modes fMRI",
                        "dynamic functional connectivity gradual transitions evidence",
                    ],
                },
            ],
        },
        "MECH-025": {
            "focus": "Test action-mode enaction signatures against DMN suppression and commitment-linked precision routing.",
            "questions": [
                "Which pathways reliably increase during action commitment and enaction?",
                "What evidence links action-mode precision shifts to thalamo-cortico-striatal routing?",
                "Where does action-mode evidence fail to separate from vigilance-like readiness?",
            ],
            "tracks": [
                {
                    "track_id": "TRK-01",
                    "focus": "Action execution network integration",
                    "query_stems": [
                        "action enaction network integration corticostriatal thalamic",
                        "task engaged mode suppression default mode network",
                    ],
                },
                {
                    "track_id": "TRK-02",
                    "focus": "Commitment gating and action monitoring",
                    "query_stems": [
                        "preSMA ACC commitment decision threshold action execution",
                        "efference copy action monitoring prediction signals",
                    ],
                },
                {
                    "track_id": "TRK-03",
                    "focus": "Mixed findings and mode boundary failures",
                    "query_stems": [
                        "action mode vigilance overlap neural evidence",
                        "task mode state misclassification neuroimaging",
                    ],
                },
            ],
        },
        "MECH-026": {
            "focus": "Disambiguate ready-vigilance from action commitment using inhibitory priming and salience routing evidence.",
            "questions": [
                "Which circuits express high sensitivity/priming while still suppressing motor release?",
                "What signatures separate restraint-oriented vigilance from imminent action preparation?",
                "What evidence suggests vigilance and action are not cleanly dissociable?",
            ],
            "tracks": [
                {
                    "track_id": "TRK-01",
                    "focus": "Inhibitory control and orienting circuits",
                    "query_stems": [
                        "ready vigilance inhibitory control network",
                        "orienting salience motor inhibition effective connectivity",
                    ],
                },
                {
                    "track_id": "TRK-02",
                    "focus": "Threat/salience and restraint coupling",
                    "query_stems": [
                        "threat vigilance without action neural circuits",
                        "salience network motor suppression pathways",
                    ],
                },
                {
                    "track_id": "TRK-03",
                    "focus": "Boundary cases between vigilance and action",
                    "query_stems": [
                        "hypervigilance transition to action neural markers",
                        "false alarm motor gating neural evidence",
                    ],
                },
            ],
        },
        "MECH-029": {
            "focus": "Test DMN-like reflective replay constraints against action-network suppression and hippocampal-cortical coupling.",
            "questions": [
                "Which data best supports DMN-like reflective replay with commitment suppression?",
                "How strong is evidence for hippocampal-cortical coupling during internally generated simulation?",
                "Where does DMN activity fail to support safe replay assumptions?",
            ],
            "tracks": [
                {
                    "track_id": "TRK-01",
                    "focus": "DMN architecture and anti-correlation with action networks",
                    "query_stems": [
                        "default mode network anti-correlation task positive network",
                        "DMN executive control dynamic coupling transitions",
                    ],
                },
                {
                    "track_id": "TRK-02",
                    "focus": "Hippocampal replay and autobiographical simulation",
                    "query_stems": [
                        "hippocampal cortical replay default mode simulation",
                        "episodic future thinking hippocampus default mode",
                    ],
                },
                {
                    "track_id": "TRK-03",
                    "focus": "DMN instability/pathology boundary evidence",
                    "query_stems": [
                        "rumination default mode control failure connectivity",
                        "psychosis default mode internal model intrusion evidence",
                    ],
                },
            ],
        },
        "MECH-030": {
            "focus": "Constrain sleep/offline consolidation mode assumptions with replay, renormalization, and boundary-protection evidence.",
            "questions": [
                "Which sleep-stage mechanisms support consolidation without online commit leakage?",
                "What evidence supports replay-driven integration across modes?",
                "Which findings suggest offline updates can distort rather than stabilize mode boundaries?",
            ],
            "tracks": [
                {
                    "track_id": "TRK-01",
                    "focus": "Sleep replay and consolidation pathways",
                    "query_stems": [
                        "sleep replay hippocampal cortical consolidation pathways",
                        "sleep stage memory consolidation network connectivity",
                    ],
                },
                {
                    "track_id": "TRK-02",
                    "focus": "Precision recalibration and homeostatic renormalization",
                    "query_stems": [
                        "sleep synaptic homeostasis precision recalibration",
                        "offline neural renormalization predictive processing",
                    ],
                },
                {
                    "track_id": "TRK-03",
                    "focus": "Failure signatures of offline integration",
                    "query_stems": [
                        "sleep disturbance mode switching instability",
                        "maladaptive consolidation replay bias evidence",
                    ],
                },
            ],
        },
        "MECH-047": {
            "focus": "Evaluate mode-commitment hysteresis and switching-cost hypotheses with state-transition neuroscience evidence.",
            "questions": [
                "What evidence supports hysteresis-like switching inertia in brain state transitions?",
                "Which control variables predict stable mode commitment versus thrash?",
                "Where does evidence support continuous adaptation over explicit switching-cost dynamics?",
            ],
            "tracks": [
                {
                    "track_id": "TRK-01",
                    "focus": "State-transition and metastability analyses",
                    "query_stems": [
                        "brain state transition hysteresis metastability",
                        "dynamic functional connectivity state switching costs",
                    ],
                },
                {
                    "track_id": "TRK-02",
                    "focus": "Salience/LC-NE and transition gating",
                    "query_stems": [
                        "locus coeruleus salience network state transitions",
                        "arousal modulation cognitive state switching",
                    ],
                },
                {
                    "track_id": "TRK-03",
                    "focus": "Disconfirming evidence for explicit mode manager dynamics",
                    "query_stems": [
                        "continuous control model cognitive state dynamics evidence",
                        "noisy manifold transitions versus discrete states",
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
    manual_priority = str(gap_item.get("manual_priority", "")).strip().lower()
    if manual_priority in {"high", "medium", "low"}:
        return manual_priority
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
        "manual_seed": bool(gap_item.get("manual_seed", False)),
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
    completed_items = doc.get("completed_items", [])

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
    lines.append(
        f"Active queue items: `{len(items)}`. Completed items tracked: `{len(completed_items)}`."
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
        lines.append(f"- Status: `{item.get('status', 'proposed')}`")
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
        completion = item.get("completion_status", {})
        if isinstance(completion, dict):
            lines.append(
                "- Completion check: "
                + f"entries_total={completion.get('entries_total', 0)}, "
                + f"support_entries={completion.get('support_entries', 0)}, "
                + f"non_support_entries={completion.get('non_support_entries', 0)}, "
                + f"coverage_ready={completion.get('coverage_ready', False)}, "
                + f"clarification_ready={completion.get('clarification_ready', False)}, "
                + f"status_reason={completion.get('status_reason', '-')}"
            )
            if bool(item.get("manual_seed", False)):
                lines.append(
                    "- Manual-seed adjudication: "
                    + f"required={completion.get('manual_adjudication_required', False)}, "
                    + f"adjudicated={completion.get('manual_adjudicated', False)}."
                )
        lines.append("")

    if completed_items:
        lines.append("## Completed Pulls")
        lines.append("")
        lines.append(
            "These claims currently satisfy completion criteria and are excluded from the active queue unless reopened."
        )
        lines.append("")
        lines.append("| pull_id | claim_id | status_reason | conflict_ratio |")
        lines.append("|---|---|---|---:|")
        for item in completed_items:
            signals = item.get("selection_signals", {})
            completion = item.get("completion_status", {})
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{item.get('pull_id', '')}`",
                        f"`{item.get('claim_id', '')}`",
                        str(completion.get("status_reason", "-")),
                        _fmt_number(_safe_float(signals.get("conflict_ratio", 0.0), 0.0)),
                    ]
                )
                + " |"
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
    if not items:
        lines.append("- `_none_` (active queue drained; monitor for reopen conditions)")
    else:
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
        "--planning-criteria",
        default="evidence/planning/planning_criteria.v1.yaml",
        help="Path to planning criteria JSON-compatible YAML.",
    )
    parser.add_argument(
        "--state-json",
        default="evidence/planning/connectome_pull_state.v1.json",
        help="Path to connectome pull persistent state JSON.",
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
    parser.add_argument(
        "--include-completed",
        action="store_true",
        help="Include completed pull items in active queue output.",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    gap_doc = _load_json(repo_root / args.gap_register)
    matrix = _load_json(repo_root / args.claim_matrix)
    claims = _load_claim_registry(repo_root / args.claims_file)
    dependents = _dependents_map(claims)
    planning_criteria = _load_json(repo_root / args.planning_criteria)
    completion_settings = _load_connectome_completion_settings(planning_criteria)
    manual_seed_settings = _load_connectome_manual_seed_settings(planning_criteria)
    state_path = repo_root / args.state_json
    prior_state = _load_state(state_path)

    generated_at = _now_utc()
    cycle_date = str(gap_doc.get("generated_at_utc", generated_at))[:10]

    gap_items = gap_doc.get("items", []) if isinstance(gap_doc, dict) else []
    gap_by_claim: dict[str, dict[str, Any]] = {}
    for raw_gap in gap_items:
        if not isinstance(raw_gap, dict):
            continue
        claim_id = str(raw_gap.get("claim_id", "")).strip()
        if claim_id and claim_id not in gap_by_claim:
            gap_by_claim[claim_id] = raw_gap

    selected: list[dict[str, Any]] = []
    for gap_item in gap_items:
        if args.include_monitor or bool(gap_item.get("consider_new_structure", False)):
            selected.append(gap_item)

    selected_claims = {str(item.get("claim_id", "")).strip() for item in selected}
    for claim_id in manual_seed_settings.get("claim_ids", []):
        if claim_id in selected_claims:
            continue
        seed = dict(gap_by_claim.get(claim_id, {}))
        if not seed:
            seed = {
                "claim_id": claim_id,
                "claim_type": claims.get(claim_id, {}).get("claim_type", "unknown"),
                "current_status": claims.get(claim_id, {}).get("status", "unknown"),
                "conflict_ratio": 0.0,
                "overall_confidence": 0.5,
                "consider_new_structure": False,
                "trigger_signals": [],
                "recurring_failure_signatures": [],
            }
        seed["manual_seed"] = True
        seed["manual_priority"] = str(manual_seed_settings.get("priority", "high"))
        trigger_signals = [str(x) for x in seed.get("trigger_signals", []) if str(x).strip()]
        manual_trigger = str(manual_seed_settings.get("trigger_signal", "")).strip()
        if manual_trigger and manual_trigger not in trigger_signals:
            trigger_signals.append(manual_trigger)
        seed["trigger_signals"] = trigger_signals
        selected.append(seed)
        selected_claims.add(claim_id)

    selected.sort(
        key=lambda item: (
            0 if bool(item.get("manual_seed", False)) else 1,
            0 if bool(item.get("consider_new_structure", False)) else 1,
            -_safe_float(item.get("conflict_ratio", 0.0), 0.0),
            str(item.get("claim_id", "")),
        )
    )

    all_items: list[dict[str, Any]] = []
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
        item = _build_item(
            idx=idx,
            gap_item=gap_item,
            claim_meta=claim_meta,
            registry_meta=registry_meta,
            dependents=dependents.get(claim_id, []),
        )
        lit_type = str(item.get("suggested_literature_type", ""))
        completion = _count_literature_completion(repo_root, lit_type, claim_id)
        support_entries = max(
            0,
            int(completion["entries_total"]) - int(completion["non_support_entries"]),
        )
        coverage_ready = bool(
            int(completion["entries_total"]) >= int(completion_settings["min_entries"])
            and support_entries >= int(completion_settings["min_support_entries"])
            and int(completion["non_support_entries"]) >= int(completion_settings["min_non_support_entries"])
        )
        conflict_ratio = _safe_float(
            item.get("selection_signals", {}).get("conflict_ratio", 0.0), 0.0
        )
        prev = prior_state.get(claim_id, {})
        prev_status = str(prev.get("status", "proposed")).strip().lower()
        was_completed = prev_status == "completed"
        reopen_conflict_ratio = float(completion_settings["reopen_conflict_ratio"])
        is_manual_seed = bool(item.get("manual_seed", False))
        manual_adjudication_required = bool(
            is_manual_seed and bool(manual_seed_settings.get("require_adjudication_for_completion", True))
        )
        adjudicated_claim_ids = {
            str(x).strip() for x in manual_seed_settings.get("adjudicated_claim_ids", []) if str(x).strip()
        }
        manual_adjudicated = claim_id in adjudicated_claim_ids
        manual_adjudication_gate_passed = bool(
            (not manual_adjudication_required) or manual_adjudicated
        )
        clarification_ready = bool(
            coverage_ready
            and conflict_ratio < reopen_conflict_ratio
            and manual_adjudication_gate_passed
        )

        status = "proposed"
        status_reason = "awaiting_connectome_evidence"
        clarification_reason = "awaiting_coverage"
        if clarification_ready:
            status = "completed"
            status_reason = "clarification_criteria_met"
            clarification_reason = "clarification_gate_satisfied"
        elif was_completed and conflict_ratio < reopen_conflict_ratio and manual_adjudication_gate_passed:
            status = "completed"
            status_reason = "preserve_completed_state"
            clarification_reason = "preserved_completed_state"
        elif was_completed and conflict_ratio >= reopen_conflict_ratio:
            status = "proposed"
            status_reason = "reopened_due_conflict_pressure"
            clarification_reason = "conflict_ratio_above_reopen_threshold"
        elif coverage_ready and conflict_ratio >= reopen_conflict_ratio:
            status = "proposed"
            status_reason = "coverage_met_but_reopened_for_high_conflict"
            clarification_reason = "conflict_ratio_above_reopen_threshold"
        elif coverage_ready and manual_adjudication_required and not manual_adjudicated:
            status = "proposed"
            status_reason = "coverage_met_pending_manual_adjudication"
            clarification_reason = "manual_seed_adjudication_pending"
        elif coverage_ready:
            status = "proposed"
            status_reason = "coverage_met_pending_clarification"
            clarification_reason = "clarification_gate_not_satisfied"

        item["status"] = status
        item["completion_status"] = {
            "entries_total": int(completion["entries_total"]),
            "support_entries": int(support_entries),
            "non_support_entries": int(completion["non_support_entries"]),
            "latest_timestamp_utc": str(completion.get("latest_timestamp_utc", "")),
            "min_entries": int(completion_settings["min_entries"]),
            "min_support_entries": int(completion_settings["min_support_entries"]),
            "min_non_support_entries": int(completion_settings["min_non_support_entries"]),
            "reopen_conflict_ratio": float(completion_settings["reopen_conflict_ratio"]),
            "coverage_ready": bool(coverage_ready),
            "clarification_ready": bool(clarification_ready),
            "clarification_reason": clarification_reason,
            "manual_seed": bool(is_manual_seed),
            "manual_adjudication_required": bool(manual_adjudication_required),
            "manual_adjudicated": bool(manual_adjudicated),
            "status_reason": status_reason,
        }
        all_items.append(item)

    active_items = [
        item for item in all_items if args.include_completed or str(item.get("status", "")) != "completed"
    ]
    completed_items = [
        item for item in all_items if str(item.get("status", "")) == "completed"
    ]

    state_items: list[dict[str, Any]] = []
    for item in all_items:
        claim_id = str(item.get("claim_id", "")).strip()
        prev = prior_state.get(claim_id, {})
        prev_status = str(prev.get("status", "")).strip().lower()
        status = str(item.get("status", "proposed")).strip().lower()
        last_status_change = str(prev.get("last_status_change_utc", generated_at))
        if prev_status != status:
            last_status_change = generated_at
        completed_at = str(prev.get("completed_at_utc", ""))
        if status == "completed":
            if not completed_at:
                completed_at = generated_at
        else:
            completed_at = ""
        state_items.append(
            {
                "claim_id": claim_id,
                "pull_id": str(item.get("pull_id", "")),
                "status": status,
                "last_status_change_utc": last_status_change,
                "completed_at_utc": completed_at,
                "status_reason": str(item.get("completion_status", {}).get("status_reason", "")),
                "conflict_ratio": round(
                    _safe_float(item.get("selection_signals", {}).get("conflict_ratio", 0.0), 0.0), 3
                ),
                "entries_total": int(item.get("completion_status", {}).get("entries_total", 0)),
                "support_entries": int(item.get("completion_status", {}).get("support_entries", 0)),
                "non_support_entries": int(
                    item.get("completion_status", {}).get("non_support_entries", 0)
                ),
                "coverage_ready": bool(item.get("completion_status", {}).get("coverage_ready", False)),
                "clarification_ready": bool(
                    item.get("completion_status", {}).get("clarification_ready", False)
                ),
                "manual_seed": bool(item.get("completion_status", {}).get("manual_seed", False)),
                "manual_adjudication_required": bool(
                    item.get("completion_status", {}).get("manual_adjudication_required", False)
                ),
                "manual_adjudicated": bool(
                    item.get("completion_status", {}).get("manual_adjudicated", False)
                ),
                "latest_timestamp_utc": str(
                    item.get("completion_status", {}).get("latest_timestamp_utc", "")
                ),
            }
        )

    state_doc = {
        "schema_version": "connectome_pull_state/v1",
        "generated_at_utc": generated_at,
        "source_queue_json": (repo_root / args.output_json).as_posix(),
        "items": sorted(state_items, key=lambda x: str(x.get("claim_id", ""))),
    }
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state_doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    selection_mode = "include_monitor" if args.include_monitor else "consider_new_structure_only"
    if manual_seed_settings.get("claim_ids"):
        selection_mode = selection_mode + "+manual_seed_claims"

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
            "mode": selection_mode,
            "consider_new_structure_items": sum(
                1 for item in selected if bool(item.get("consider_new_structure", False))
            ),
            "manual_seed_items": sum(1 for item in selected if bool(item.get("manual_seed", False))),
            "manual_seed_claim_ids": [str(x) for x in manual_seed_settings.get("claim_ids", [])],
            "total_selected_items": len(all_items),
            "active_queue_items": len(active_items),
            "completed_items": len(completed_items),
        },
        "completion_policy": {
            "min_entries": int(completion_settings["min_entries"]),
            "min_support_entries": int(completion_settings["min_support_entries"]),
            "min_non_support_entries": int(completion_settings["min_non_support_entries"]),
            "reopen_conflict_ratio": float(completion_settings["reopen_conflict_ratio"]),
            "manual_require_adjudication_for_completion": bool(
                manual_seed_settings.get("require_adjudication_for_completion", True)
            ),
            "manual_claim_ids_adjudicated": [
                str(x) for x in manual_seed_settings.get("adjudicated_claim_ids", [])
            ],
            "state_path": state_path.as_posix(),
        },
        "items": active_items,
        "completed_items": completed_items,
    }

    output_json_path = repo_root / args.output_json
    output_md_path = repo_root / args.output_md
    output_json_path.parent.mkdir(parents=True, exist_ok=True)
    output_md_path.parent.mkdir(parents=True, exist_ok=True)
    output_json_path.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    output_md_path.write_text(_format_markdown(doc), encoding="utf-8")

    print(f"Wrote connectome literature pull JSON: {output_json_path.as_posix()}")
    print(f"Wrote connectome literature pull MD: {output_md_path.as_posix()}")
    print(f"Wrote connectome pull state JSON: {state_path.as_posix()}")
    print(
        "Connectome queue status: "
        + f"active={len(active_items)} completed={len(completed_items)} total_selected={len(all_items)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
