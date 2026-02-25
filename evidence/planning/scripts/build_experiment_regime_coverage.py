#!/usr/bin/env python3
"""Build a claim-to-regime coverage matrix for active governance pressure claims."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_REGIME_MAP = {
    "ree-v2": "toy_qualification",
    "ree-experiments-lab": "synthetic_stress",
    "ree-openclaw": "runtime_authority",
    "ree-v1-minimal": "backstop_contract",
}


def _now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _clean_claim_id(value: Any) -> str:
    text = str(value or "").strip()
    if text.startswith("`") and text.endswith("`") and len(text) >= 2:
        text = text[1:-1]
    return text.strip()


def _latest_sync_by_repo(sync_reports_dir: Path) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    if not sync_reports_dir.exists():
        return out

    reports = sorted(sync_reports_dir.glob("*.json"))
    for report in reports:
        try:
            payload = _load_json(report)
        except Exception:
            continue
        generated = str(payload.get("generated_at_utc", "")).strip()
        results = payload.get("results", [])
        if not isinstance(results, list):
            continue
        for result in results:
            if not isinstance(result, dict):
                continue
            repo = str(result.get("repo_name", "")).strip()
            if not repo:
                continue
            prior = out.get(repo)
            if prior is None or generated > prior.get("generated_at_utc", ""):
                out[repo] = {
                    "generated_at_utc": generated,
                    "report_path": report.as_posix(),
                    "status": str(result.get("status", "")),
                    "imports_count": len(result.get("imports", []))
                    if isinstance(result.get("imports", []), list)
                    else 0,
                    "handoff_path": str(result.get("handoff_path", "")),
                }
    return out


def _observed_regimes_by_claim(experiments_root: Path) -> dict[str, set[str]]:
    observed: dict[str, set[str]] = {}
    if not experiments_root.exists():
        return observed

    for manifest_path in sorted(experiments_root.glob("*/runs/*/manifest.json")):
        try:
            manifest = _load_json(manifest_path)
        except Exception:
            continue

        source_repo = ""
        source_repo_raw = manifest.get("source_repo")
        if isinstance(source_repo_raw, dict):
            source_repo = str(source_repo_raw.get("name", "")).strip()

        regime = REPO_REGIME_MAP.get(source_repo)
        if not regime:
            experiment_type = str(manifest.get("experiment_type", "")).strip()
            if experiment_type.startswith("runtime_authority_"):
                regime = "runtime_authority"

        if not regime:
            continue

        claim_ids = manifest.get("claim_ids_tested", [])
        if not isinstance(claim_ids, list):
            continue

        for claim_raw in claim_ids:
            claim_id = _clean_claim_id(claim_raw)
            if not claim_id:
                continue
            observed.setdefault(claim_id, set()).add(regime)

    return observed


def _derive_required_regimes(
    claim_id: str,
    *,
    in_governance_queue: bool,
    in_structure_queue: bool,
) -> list[str]:
    required = {"toy_qualification"}

    if in_governance_queue:
        required.add("synthetic_stress")
    if in_structure_queue:
        required.add("literature_connectome")

    runtime_sensitive_claims = {
        "MECH-056",
        "MECH-057",
        "MECH-060",
        "MECH-061",
        "Q-013",
        "Q-014",
        "Q-017",
    }
    if claim_id in runtime_sensitive_claims:
        required.add("runtime_authority")

    return sorted(required)


def _build_claim_rows(
    *,
    governance_agenda: dict[str, Any],
    architecture_gap_register: dict[str, Any],
    proposals: dict[str, Any],
    connectome_pull: dict[str, Any],
    observed_regimes_by_claim: dict[str, set[str]],
) -> list[dict[str, Any]]:
    checkpoints = governance_agenda.get("checkpoints", {})
    if not isinstance(checkpoints, dict):
        checkpoints = {}

    governance_items = checkpoints.get("governance_decisions", {}).get("items", [])
    if not isinstance(governance_items, list):
        governance_items = []

    structure_items = checkpoints.get("architecture_structure", {}).get(
        "consider_new_structure", []
    )
    if not isinstance(structure_items, list):
        structure_items = []

    governance_claims = {
        _clean_claim_id(item.get("claim_id"))
        for item in governance_items
        if _clean_claim_id(item.get("claim_id"))
    }
    structure_claims = {
        _clean_claim_id(item.get("claim_id"))
        for item in structure_items
        if _clean_claim_id(item.get("claim_id"))
    }
    active_claims = sorted(governance_claims | structure_claims)

    gap_items = architecture_gap_register.get("items", [])
    if not isinstance(gap_items, list):
        gap_items = []
    gap_by_claim = {
        _clean_claim_id(item.get("claim_id")): item
        for item in gap_items
        if _clean_claim_id(item.get("claim_id"))
    }

    proposal_items = proposals.get("items", [])
    if not isinstance(proposal_items, list):
        proposal_items = []
    proposal_rows_by_claim: dict[str, list[dict[str, Any]]] = {}
    for proposal in proposal_items:
        if not isinstance(proposal, dict):
            continue
        claim_id = _clean_claim_id(proposal.get("claim_id"))
        if not claim_id:
            continue
        proposal_rows_by_claim.setdefault(claim_id, []).append(proposal)

    connectome_items = connectome_pull.get("items", [])
    if not isinstance(connectome_items, list):
        connectome_items = []
    connectome_completed = connectome_pull.get("completed_items", [])
    if not isinstance(connectome_completed, list):
        connectome_completed = []

    connectome_claims = {
        _clean_claim_id(item.get("claim_id"))
        for item in (connectome_items + connectome_completed)
        if _clean_claim_id(item.get("claim_id"))
    }

    rows: list[dict[str, Any]] = []
    for claim_id in active_claims:
        claim_proposals = proposal_rows_by_claim.get(claim_id, [])
        covered_regimes: set[str] = set(observed_regimes_by_claim.get(claim_id, set()))
        proposal_refs: list[str] = []
        literature_refs: list[str] = []

        for proposal in claim_proposals:
            proposal_type = str(proposal.get("proposal_type", "")).strip()
            target_repo = str(proposal.get("target_repo", "")).strip()
            proposal_id = str(proposal.get("proposal_id", "")).strip()
            experiment_type = str(proposal.get("suggested_experiment_type", "")).strip()
            dispatch_mode = str(proposal.get("dispatch_mode", "")).strip()

            if proposal_type == "experimental":
                regime = REPO_REGIME_MAP.get(target_repo)
                if regime:
                    covered_regimes.add(regime)
            elif proposal_type == "literature_review":
                covered_regimes.add("literature_connectome")

            if proposal_type == "literature_review":
                literature_refs.append(proposal_id or "unknown")
            else:
                proposal_refs.append(
                    f"{proposal_id}@{target_repo}:{experiment_type or 'unknown'}:{dispatch_mode or 'n/a'}"
                )

        if claim_id in connectome_claims:
            covered_regimes.add("literature_connectome")

        required_regimes = _derive_required_regimes(
            claim_id,
            in_governance_queue=claim_id in governance_claims,
            in_structure_queue=claim_id in structure_claims,
        )
        missing_regimes = sorted(set(required_regimes) - covered_regimes)

        nuance_flags: list[str] = []
        if "runtime_authority" in missing_regimes:
            nuance_flags.append("missing_runtime_authority_path")
        if "synthetic_stress" in missing_regimes:
            nuance_flags.append("missing_adversarial_stress_lane")
        if "literature_connectome" in missing_regimes:
            nuance_flags.append("missing_external_constraint_lane")
        if "toy_qualification" in missing_regimes:
            nuance_flags.append("missing_primary_mechanism_harness")
        if not proposal_refs and not literature_refs and not covered_regimes:
            nuance_flags.append("no_active_dispatch_refs")

        gap = gap_by_claim.get(claim_id, {})
        conflict_ratio = (
            float(gap.get("conflict_ratio", 0.0))
            if isinstance(gap.get("conflict_ratio", 0.0), (int, float))
            else 0.0
        )
        if not missing_regimes and conflict_ratio >= 0.8:
            nuance_flags.append("high_conflict_despite_lane_coverage")

        rows.append(
            {
                "claim_id": claim_id,
                "in_governance_queue": claim_id in governance_claims,
                "in_structure_queue": claim_id in structure_claims,
                "claim_type": str(gap.get("claim_type", "")),
                "conflict_ratio": round(conflict_ratio, 3),
                "required_regimes": required_regimes,
                "covered_regimes": sorted(covered_regimes),
                "missing_regimes": missing_regimes,
                "proposal_refs": sorted(proposal_refs),
                "literature_refs": sorted(literature_refs),
                "nuance_gap_flags": nuance_flags,
                "gap_recommendation": str(gap.get("recommendation", "")),
            }
        )
    return rows


def _render_markdown(payload: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Experiment Regime Coverage")
    lines.append("")
    lines.append(f"Generated: `{payload.get('generated_at_utc', '')}`")
    lines.append("")
    lines.append("## Regime Definitions")
    lines.append("")
    lines.append("- `toy_qualification`: primary mechanism harness (typically `ree-v2` toy qualification runs).")
    lines.append("- `synthetic_stress`: adversarial stress lane (typically `ree-experiments-lab`).")
    lines.append("- `runtime_authority`: runtime authority/commit boundary execution lane (typically `ree-openclaw`).")
    lines.append("- `backstop_contract`: contract emitter parity lane (typically `ree-v1-minimal`, non-authoritative).")
    lines.append("- `literature_connectome`: external constraint lane (connectome/literature pulls).")
    lines.append("")

    summary = payload.get("summary", {})
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- active_claims: `{summary.get('active_claims', 0)}`")
    lines.append(f"- claims_with_missing_regimes: `{summary.get('claims_with_missing_regimes', 0)}`")
    lines.append(
        f"- claims_missing_runtime_authority: `{summary.get('claims_missing_runtime_authority', 0)}`"
    )
    lines.append(
        f"- claims_missing_synthetic_stress: `{summary.get('claims_missing_synthetic_stress', 0)}`"
    )
    lines.append(
        f"- claims_missing_literature_connectome: `{summary.get('claims_missing_literature_connectome', 0)}`"
    )
    lines.append("")

    lines.append("## Producer Freshness")
    lines.append("")
    lines.append("| repo | latest_sync_utc | status | imports | report |")
    lines.append("|---|---|---|---:|---|")
    for repo in sorted(payload.get("producer_freshness", {})):
        entry = payload["producer_freshness"][repo]
        lines.append(
            "| "
            + f"`{repo}` | `{entry.get('generated_at_utc', '')}` | "
            + f"`{entry.get('status', '')}` | `{entry.get('imports_count', 0)}` | "
            + f"`{entry.get('report_path', '')}` |"
        )
    lines.append("")

    lines.append("## Claim Matrix")
    lines.append("")
    lines.append("| claim_id | conflict_ratio | required_regimes | covered_regimes | missing_regimes | proposal_refs | nuance_gap_flags |")
    lines.append("|---|---:|---|---|---|---|---|")
    for row in payload.get("claims", []):
        lines.append(
            "| "
            + f"`{row.get('claim_id', '')}` | "
            + f"`{row.get('conflict_ratio', 0)}` | "
            + f"`{', '.join(row.get('required_regimes', [])) or 'none'}` | "
            + f"`{', '.join(row.get('covered_regimes', [])) or 'none'}` | "
            + f"`{', '.join(row.get('missing_regimes', [])) or 'none'}` | "
            + f"`{'; '.join(row.get('proposal_refs', [])) or 'none'}` | "
            + f"`{', '.join(row.get('nuance_gap_flags', [])) or 'none'}` |"
        )
    lines.append("")

    missing_runtime = [
        row for row in payload.get("claims", []) if "runtime_authority" in row.get("missing_regimes", [])
    ]
    missing_synthetic = [
        row for row in payload.get("claims", []) if "synthetic_stress" in row.get("missing_regimes", [])
    ]
    missing_literature = [
        row for row in payload.get("claims", []) if "literature_connectome" in row.get("missing_regimes", [])
    ]

    lines.append("## Priority Gaps")
    lines.append("")
    lines.append("- Runtime authority lane missing:")
    if missing_runtime:
        for row in missing_runtime:
            lines.append(
                f"  - `{row['claim_id']}` -> add `ree-openclaw` runtime probe with irreversible-dispatch interruption/supersession coverage."
            )
    else:
        lines.append("  - none")
    lines.append("- Synthetic stress lane missing:")
    if missing_synthetic:
        for row in missing_synthetic:
            lines.append(
                f"  - `{row['claim_id']}` -> add discriminative stress-lane proposal in `ree-experiments-lab`."
            )
    else:
        lines.append("  - none")
    lines.append("- Literature/connectome lane missing:")
    if missing_literature:
        for row in missing_literature:
            lines.append(
                f"  - `{row['claim_id']}` -> queue/complete connectome pull before stronger architecture promotion."
            )
    else:
        lines.append("  - none")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build active-claim experiment regime coverage report."
    )
    parser.add_argument(
        "--governance-agenda",
        default="evidence/planning/governance_agenda.v1.json",
        help="Governance agenda JSON path.",
    )
    parser.add_argument(
        "--architecture-gap-register",
        default="evidence/planning/architecture_gap_register.v1.json",
        help="Architecture gap register JSON path.",
    )
    parser.add_argument(
        "--proposals",
        default="evidence/planning/experiment_proposals.v1.json",
        help="Experiment proposals JSON path.",
    )
    parser.add_argument(
        "--connectome-pull",
        default="evidence/planning/connectome_literature_pull.v1.json",
        help="Connectome pull queue JSON path.",
    )
    parser.add_argument(
        "--handoff-sync-reports",
        default="evidence/planning/handoff_sync_reports",
        help="Directory containing handoff sync report JSON files.",
    )
    parser.add_argument(
        "--experiments-root",
        default="evidence/experiments",
        help="Experiment packs root path used to detect observed regime coverage.",
    )
    parser.add_argument(
        "--output-json",
        default="evidence/planning/experiment_regime_coverage.v1.json",
        help="Output JSON path.",
    )
    parser.add_argument(
        "--output-md",
        default="evidence/planning/EXPERIMENT_REGIME_COVERAGE.md",
        help="Output markdown path.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[3]
    governance_agenda = _load_json(repo_root / args.governance_agenda)
    architecture_gap_register = _load_json(repo_root / args.architecture_gap_register)
    proposals = _load_json(repo_root / args.proposals)
    connectome_pull = _load_json(repo_root / args.connectome_pull)
    producer_freshness = _latest_sync_by_repo(repo_root / args.handoff_sync_reports)
    observed_regimes_by_claim = _observed_regimes_by_claim(repo_root / args.experiments_root)

    claim_rows = _build_claim_rows(
        governance_agenda=governance_agenda,
        architecture_gap_register=architecture_gap_register,
        proposals=proposals,
        connectome_pull=connectome_pull,
        observed_regimes_by_claim=observed_regimes_by_claim,
    )

    summary = {
        "active_claims": len(claim_rows),
        "claims_with_missing_regimes": sum(1 for row in claim_rows if row.get("missing_regimes")),
        "claims_missing_runtime_authority": sum(
            1 for row in claim_rows if "runtime_authority" in row.get("missing_regimes", [])
        ),
        "claims_missing_synthetic_stress": sum(
            1 for row in claim_rows if "synthetic_stress" in row.get("missing_regimes", [])
        ),
        "claims_missing_literature_connectome": sum(
            1 for row in claim_rows if "literature_connectome" in row.get("missing_regimes", [])
        ),
    }

    payload = {
        "schema_version": "experiment_regime_coverage/v1",
        "generated_at_utc": _now_utc(),
        "summary": summary,
        "producer_freshness": producer_freshness,
        "claims": claim_rows,
    }

    out_json = repo_root / args.output_json
    out_md = repo_root / args.output_md
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    out_md.write_text(_render_markdown(payload), encoding="utf-8")

    print(f"Wrote: {out_json}")
    print(f"Wrote: {out_md}")
    print(
        "Coverage summary: "
        + f"active_claims={summary['active_claims']} "
        + f"missing_any={summary['claims_with_missing_regimes']} "
        + f"missing_runtime={summary['claims_missing_runtime_authority']} "
        + f"missing_synthetic={summary['claims_missing_synthetic_stress']} "
        + f"missing_literature={summary['claims_missing_literature_connectome']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
