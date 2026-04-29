"""Generate the Option E (lit/exp decoupled) shadow recommendations report.

Phase 1 of the lit/exp decoupling transition. The production governance pipeline
continues to use overall_confidence as the promotion gate. This script reads the
same claim_evidence.v1.json matrix and produces a sibling report that shows what
governance decisions WOULD look like under the decoupled regime, where:

  overall_confidence    = exp_conf only  (literature is parallel signal)
  evidence_quadrant     = {confirmed_established | novel_discovery
                           | plausible_unproven | speculative}

The intent is "shadow generation, not shadow execution":
no claim's status changes because of this report. The report exists so we can
discover the discrepancies between the two regimes (especially implementation-
cohort claims that lack experimental backing) before cutover.

Output: evidence/experiments/option_e_recommendations.md

See REE_assembly/CLAUDE.md "Lit/Exp Decoupling Shadow" for the full transition
plan.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
MATRIX_PATH = REPO_ROOT / "evidence/experiments/claim_evidence.v1.json"
CLAIMS_YAML = REPO_ROOT / "docs/claims/claims.yaml"
OUT_PATH = REPO_ROOT / "evidence/experiments/option_e_recommendations.md"

# Match build_experiment_indexes.py constants.
HIGH_EXP = 0.62
HIGH_LIT = 0.55

# New flag thresholds (replace single low_overall_confidence under cutover).
LOW_EXP_FLAG = 0.55
LIT_ONLY_CAP = 0.50

# Implementation cohort: claims that have already been "implemented" by the
# governance process. Used to compute the discrepancy report.
IMPL_STATUSES = {"stable", "active", "implemented", "resolved"}


def _parse_claim_statuses(yaml_text: str) -> dict[str, str]:
    """Lightweight parse to avoid YAML dep. Each top-level claim block has 'id:'
    then a 'status:' line within its body."""
    statuses: dict[str, str] = {}
    current: str | None = None
    for line in yaml_text.splitlines():
        m = re.match(r"^-?\s*id:\s*([A-Z0-9_\-]+)", line)
        if m:
            current = m.group(1).strip()
            continue
        if current is None:
            continue
        m = re.match(r"^\s+status:\s*([A-Za-z_]+)", line)
        if m:
            statuses[current] = m.group(1).strip()
    return statuses


def _quadrant_from_summary(summary: dict[str, Any]) -> str:
    # Prefer the indexer-computed quadrant; recompute if absent for backwards
    # compat with older matrices.
    q = summary.get("evidence_quadrant")
    if isinstance(q, str) and q:
        return q
    exp_c = float(summary.get("experimental_confidence", 0.0))
    lit_c = float(summary.get("literature_confidence", 0.0))
    counts = summary.get("source_counts", {}) or {}
    n_exp = int(counts.get("experimental", 0))
    n_lit = int(counts.get("literature", 0))
    has_exp = n_exp > 0 and exp_c >= HIGH_EXP
    has_lit = n_lit > 0 and lit_c >= HIGH_LIT
    if has_exp and has_lit:
        return "confirmed_established"
    if has_exp:
        return "novel_discovery"
    if has_lit:
        return "plausible_unproven"
    return "speculative"


def main() -> None:
    matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))
    claims = matrix.get("claims", {})
    if CLAIMS_YAML.exists():
        statuses = _parse_claim_statuses(CLAIMS_YAML.read_text(encoding="utf-8"))
    else:
        statuses = {}

    quadrant_counts: Counter = Counter()
    quadrant_buckets: dict[str, list[tuple[str, float, float, str]]] = defaultdict(list)
    discrepancies: list[dict[str, Any]] = []
    impl_no_exp: list[dict[str, Any]] = []
    novel_findings: list[dict[str, Any]] = []
    low_exp_flagged: list[dict[str, Any]] = []
    lit_only_above_cap: list[dict[str, Any]] = []

    for cid in sorted(claims.keys()):
        s = claims[cid]
        exp_c = float(s.get("experimental_confidence_decoupled",
                            s.get("experimental_confidence", 0.0)))
        lit_c = float(s.get("literature_confidence_parallel",
                            s.get("literature_confidence", 0.0)))
        overall_legacy = float(s.get("overall_confidence", 0.0))
        overall_decoupled = exp_c
        counts = s.get("source_counts", {}) or {}
        n_exp = int(counts.get("experimental", 0))
        n_lit = int(counts.get("literature", 0))
        quadrant = _quadrant_from_summary(s)
        status = statuses.get(cid, "")

        quadrant_counts[quadrant] += 1
        quadrant_buckets[quadrant].append((cid, exp_c, lit_c, status))

        # Discrepancy: regime-disagreement on the candidate->provisional gate.
        legacy_above = overall_legacy >= HIGH_EXP
        decoupled_above = overall_decoupled >= HIGH_EXP
        if legacy_above != decoupled_above:
            discrepancies.append({
                "claim_id": cid,
                "status": status,
                "legacy_overall": overall_legacy,
                "decoupled_overall": overall_decoupled,
                "lit_conf": lit_c,
                "n_exp": n_exp,
                "n_lit": n_lit,
                "quadrant": quadrant,
            })

        # Implementation-cohort claims with zero experimental backing.
        if status in IMPL_STATUSES and n_exp == 0:
            impl_no_exp.append({
                "claim_id": cid,
                "status": status,
                "lit_conf": lit_c,
                "n_lit": n_lit,
            })

        # Novel discovery surfacing.
        if quadrant == "novel_discovery":
            novel_findings.append({
                "claim_id": cid,
                "status": status,
                "exp_conf": exp_c,
                "lit_conf": lit_c,
                "n_exp": n_exp,
                "n_lit": n_lit,
            })

        # New flags.
        if n_exp > 0 and exp_c < LOW_EXP_FLAG:
            low_exp_flagged.append({
                "claim_id": cid, "status": status, "exp_conf": exp_c, "n_exp": n_exp,
            })
        if n_exp == 0 and lit_c >= LIT_ONLY_CAP:
            lit_only_above_cap.append({
                "claim_id": cid, "status": status, "lit_conf": lit_c, "n_lit": n_lit,
            })

    # --- Render report --------------------------------------------------------
    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    lines: list[str] = []
    lines.append("# Option E shadow recommendations (lit/exp decoupled regime)")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append(
        "**Phase 1 shadow report.** Production governance still uses "
        "`overall_confidence` (legacy blend). This report shows what governance "
        "would surface under the decoupled regime where `overall = exp_conf` and "
        "literature is a parallel signal. **No claim status is changed by this "
        "report.** See `REE_assembly/CLAUDE.md` Lit/Exp Decoupling Shadow for "
        "the transition plan."
    )
    lines.append("")
    lines.append("## Quadrant distribution")
    lines.append("")
    lines.append("|  | high exp (>= " f"{HIGH_EXP}" ") | low exp |")
    lines.append("|---|---|---|")
    qe = quadrant_counts.get("confirmed_established", 0)
    qn = quadrant_counts.get("novel_discovery", 0)
    qp = quadrant_counts.get("plausible_unproven", 0)
    qs = quadrant_counts.get("speculative", 0)
    lines.append(f"| **high lit (>= {HIGH_LIT})** | confirmed_established: **{qe}** | plausible_unproven: **{qp}** |")
    lines.append(f"| **low lit**             | novel_discovery: **{qn}**         | speculative: **{qs}** |")
    lines.append("")
    lines.append(f"Total scored claims: {sum(quadrant_counts.values())}")
    lines.append("")

    lines.append("## Discrepancy report (regimes disagree on provisional gate)")
    lines.append("")
    lines.append(
        f"Claims that cross the `>= {HIGH_EXP}` line under one regime but not the "
        "other. These are the priority items for Phase 2 reckoning -- queue an "
        "experiment, adjust status, or flag a new evidence class."
    )
    lines.append("")
    lines.append(f"Total: **{len(discrepancies)}** discrepant claims.")
    lines.append("")
    if discrepancies:
        lines.append("| claim | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |")
        lines.append("|---|---|---:|---:|---:|---:|---:|---|")
        for d in sorted(discrepancies, key=lambda x: x["decoupled_overall"]):
            lines.append(
                f"| `{d['claim_id']}` | {d['status'] or '-'} | "
                f"{d['legacy_overall']:.3f} | {d['decoupled_overall']:.3f} | "
                f"{d['lit_conf']:.3f} | {d['n_exp']} | {d['n_lit']} | {d['quadrant']} |"
            )
        lines.append("")

    lines.append("## Implementation-cohort claims with zero experimental backing")
    lines.append("")
    lines.append(
        "These claims have status in {stable, active, implemented, resolved} but "
        "no experimental evidence in the matrix. Under the decoupled regime they "
        "would not qualify for promotion on lit alone. This is the central "
        "question for Phase 2."
    )
    lines.append("")
    lines.append(f"Total: **{len(impl_no_exp)}** implementation-cohort claims with no exp.")
    lines.append("")
    if impl_no_exp:
        lines.append("| claim | status | lit_conf | n_lit |")
        lines.append("|---|---|---:|---:|")
        for d in sorted(impl_no_exp, key=lambda x: -x["lit_conf"]):
            lines.append(
                f"| `{d['claim_id']}` | {d['status']} | {d['lit_conf']:.3f} | {d['n_lit']} |"
            )
        lines.append("")

    lines.append("## Novel discovery quadrant")
    lines.append("")
    lines.append(
        "`exp_conf >= " f"{HIGH_EXP}" "` with `lit_conf < " f"{HIGH_LIT}" "`. "
        "Either a genuine substrate-level finding without prior art, or a missing "
        "lit pull. Either way worth surfacing -- under the legacy regime these "
        "appear weaker than they actually are."
    )
    lines.append("")
    lines.append(f"Total: **{len(novel_findings)}**.")
    lines.append("")
    if novel_findings:
        lines.append("| claim | status | exp_conf | lit_conf | n_exp | n_lit |")
        lines.append("|---|---|---:|---:|---:|---:|")
        for d in sorted(novel_findings, key=lambda x: -x["exp_conf"]):
            lines.append(
                f"| `{d['claim_id']}` | {d['status'] or '-'} | "
                f"{d['exp_conf']:.3f} | {d['lit_conf']:.3f} | {d['n_exp']} | {d['n_lit']} |"
            )
        lines.append("")

    lines.append("## New flags (would replace `low_overall_confidence` at cutover)")
    lines.append("")
    lines.append(f"### `low_exp_conf` (exp_conf < {LOW_EXP_FLAG} with at least one experiment)")
    lines.append("")
    lines.append(f"Total: **{len(low_exp_flagged)}**.")
    if low_exp_flagged:
        lines.append("")
        lines.append("| claim | status | exp_conf | n_exp |")
        lines.append("|---|---|---:|---:|")
        for d in sorted(low_exp_flagged, key=lambda x: x["exp_conf"])[:30]:
            lines.append(
                f"| `{d['claim_id']}` | {d['status'] or '-'} | {d['exp_conf']:.3f} | {d['n_exp']} |"
            )
        if len(low_exp_flagged) > 30:
            lines.append(f"| ... | ... | ... | ... ({len(low_exp_flagged) - 30} more) |")
        lines.append("")
    lines.append("")
    lines.append(f"### `lit_only_above_cap` (no exp, lit_conf >= {LIT_ONLY_CAP})")
    lines.append("")
    lines.append(f"Total: **{len(lit_only_above_cap)}**.")
    if lit_only_above_cap:
        lines.append("")
        lines.append("Claims with literature support and no experiment yet. "
                     "These are candidates for the next round of experiment design.")
        lines.append("")
        lines.append("| claim | status | lit_conf | n_lit |")
        lines.append("|---|---|---:|---:|")
        for d in sorted(lit_only_above_cap, key=lambda x: -x["lit_conf"])[:50]:
            lines.append(
                f"| `{d['claim_id']}` | {d['status'] or '-'} | {d['lit_conf']:.3f} | {d['n_lit']} |"
            )
        if len(lit_only_above_cap) > 50:
            lines.append(f"| ... | ... | ... | ... ({len(lit_only_above_cap) - 50} more) |")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        "Source matrix: `evidence/experiments/claim_evidence.v1.json`. "
        "Generated by `scripts/generate_option_e_shadow.py`."
    )

    OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH.relative_to(REPO_ROOT)} "
          f"(quadrants={dict(quadrant_counts)}, "
          f"discrepancies={len(discrepancies)}, "
          f"impl_no_exp={len(impl_no_exp)}, "
          f"novel={len(novel_findings)}, "
          f"low_exp={len(low_exp_flagged)}, "
          f"lit_only_above_cap={len(lit_only_above_cap)})")


if __name__ == "__main__":
    main()
