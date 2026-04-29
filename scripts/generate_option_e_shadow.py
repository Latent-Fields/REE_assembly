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


def _parse_claim_metadata(yaml_text: str) -> dict[str, dict[str, str]]:
    """Per-claim claim_type and (for invariants) invariant_type. Used to apply
    claim_type-aware evidence gating per CLAUDE.md "Claim-type evidence
    gating"."""
    meta: dict[str, dict[str, str]] = {}
    current: str | None = None
    for line in yaml_text.splitlines():
        m = re.match(r"^-?\s*id:\s*([A-Z0-9_\-]+)", line)
        if m:
            current = m.group(1).strip()
            meta.setdefault(current, {})
            continue
        if current is None:
            continue
        for field in ("claim_type", "invariant_type"):
            m = re.match(rf"^\s+{field}:\s*([A-Za-z_]+)", line)
            if m:
                meta[current][field] = m.group(1).strip()
    return meta


# Claim-type evidence gating policy. The shadow report (and eventually the
# production gates) treats each claim_type by its actual epistemic role:
#
#  - standard           : exp_conf required for promotion. Discrepancy and
#                         impl_no_exp flags fire normally.
#  - substrate_coherence: foundational design choices that ARE the substrate
#                         (ARC + universal invariants). No isolated experiment
#                         expected; "implemented in functional substrate"
#                         suffices. Discrepancy / impl_no_exp flags suppressed.
#  - answer_state       : open questions where the evidence is "we reached an
#                         operating answer." Exempt from exp_conf gating until
#                         restated as a hypothesis.
#
# Mapping:
#   architectural_commitment   -> substrate_coherence
#   invariant + universal      -> substrate_coherence
#   invariant + emergent/grey_zone / unspecified -> standard
#   open_question              -> answer_state
#   mechanism_hypothesis       -> standard
#   design_decision            -> standard
#   implementation             -> standard
#   (anything else / missing)  -> standard (fail-safe: keep flagging)


def _evidence_gating(meta: dict[str, str]) -> str:
    ct = (meta or {}).get("claim_type", "")
    if ct == "architectural_commitment":
        return "substrate_coherence"
    if ct == "invariant":
        if (meta or {}).get("invariant_type") == "universal":
            return "substrate_coherence"
        return "standard"
    if ct == "open_question":
        return "answer_state"
    return "standard"


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
        yaml_text = CLAIMS_YAML.read_text(encoding="utf-8")
        statuses = _parse_claim_statuses(yaml_text)
        metadata = _parse_claim_metadata(yaml_text)
    else:
        statuses = {}
        metadata = {}

    quadrant_counts: Counter = Counter()
    quadrant_buckets: dict[str, list[tuple[str, float, float, str]]] = defaultdict(list)
    gating_counts: Counter = Counter()
    discrepancies: list[dict[str, Any]] = []
    impl_no_exp: list[dict[str, Any]] = []
    novel_findings: list[dict[str, Any]] = []
    low_exp_flagged: list[dict[str, Any]] = []
    lit_only_above_cap: list[dict[str, Any]] = []
    # Suppressed-by-gating buckets, surfaced separately for transparency.
    suppressed_substrate: list[dict[str, Any]] = []
    suppressed_answer_state: list[dict[str, Any]] = []

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
        meta = metadata.get(cid, {})
        claim_type = meta.get("claim_type", "")
        gating = _evidence_gating(meta)

        quadrant_counts[quadrant] += 1
        quadrant_buckets[quadrant].append((cid, exp_c, lit_c, status))
        gating_counts[gating] += 1

        # Discrepancy: regime-disagreement on the candidate->provisional gate.
        # Only fires for standard-gating claim types; substrate_coherence and
        # answer_state types use different evidence rules so a "discrepancy" by
        # the standard rule is not actionable.
        legacy_above = overall_legacy >= HIGH_EXP
        decoupled_above = overall_decoupled >= HIGH_EXP
        if legacy_above != decoupled_above:
            entry = {
                "claim_id": cid,
                "status": status,
                "claim_type": claim_type,
                "legacy_overall": overall_legacy,
                "decoupled_overall": overall_decoupled,
                "lit_conf": lit_c,
                "n_exp": n_exp,
                "n_lit": n_lit,
                "quadrant": quadrant,
            }
            if gating == "standard":
                discrepancies.append(entry)
            elif gating == "substrate_coherence":
                suppressed_substrate.append(entry)
            else:  # answer_state
                suppressed_answer_state.append(entry)

        # Implementation-cohort claims with zero experimental backing.
        # Only counts as a Phase-2 priority for standard-gating types -- ARC and
        # universal invariants don't expect direct experiments, and Q-claims
        # are exempt by virtue of being questions.
        if status in IMPL_STATUSES and n_exp == 0 and gating == "standard":
            impl_no_exp.append({
                "claim_id": cid,
                "status": status,
                "claim_type": claim_type,
                "lit_conf": lit_c,
                "n_lit": n_lit,
            })

        # Novel discovery surfacing -- still relevant for any claim_type with
        # high experimental backing but low literature.
        if quadrant == "novel_discovery":
            novel_findings.append({
                "claim_id": cid,
                "status": status,
                "claim_type": claim_type,
                "exp_conf": exp_c,
                "lit_conf": lit_c,
                "n_exp": n_exp,
                "n_lit": n_lit,
            })

        # New flags. Both apply only to standard-gating types -- ARC/universal
        # invariants/Q-claims aren't expected to clear an exp_conf bar.
        if n_exp > 0 and exp_c < LOW_EXP_FLAG and gating == "standard":
            low_exp_flagged.append({
                "claim_id": cid, "status": status, "claim_type": claim_type,
                "exp_conf": exp_c, "n_exp": n_exp,
            })
        if n_exp == 0 and lit_c >= LIT_ONLY_CAP and gating == "standard":
            lit_only_above_cap.append({
                "claim_id": cid, "status": status, "claim_type": claim_type,
                "lit_conf": lit_c, "n_lit": n_lit,
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
    lines.append("**Claim-type evidence gating** is applied: "
                 "`architectural_commitment` and universal `invariant` claims "
                 "are gated as `substrate_coherence` (foundational design -- "
                 "no isolated experiment expected); `open_question` claims are "
                 "gated as `answer_state` (exempt from exp_conf until restated "
                 "as a hypothesis). Discrepancy/impl_no_exp/low_exp/lit_only "
                 "flags fire only for standard-gating claim types. Suppressed "
                 "claims are reported separately for transparency.")
    lines.append("")
    lines.append("### Gating distribution")
    lines.append("")
    lines.append("| gating | claims |")
    lines.append("|---|---:|")
    for g in ("standard", "substrate_coherence", "answer_state"):
        lines.append(f"| `{g}` | {gating_counts.get(g, 0)} |")
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
        "other AND have standard gating. These are the priority items for Phase "
        "2 reckoning -- queue an experiment, adjust status, or flag a new "
        "evidence class."
    )
    lines.append("")
    lines.append(f"Total: **{len(discrepancies)}** discrepant claims (standard-gating only).")
    lines.append("")
    if discrepancies:
        lines.append("| claim | type | status | legacy_overall | decoupled_overall | lit_conf | n_exp | n_lit | quadrant |")
        lines.append("|---|---|---|---:|---:|---:|---:|---:|---|")
        for d in sorted(discrepancies, key=lambda x: x["decoupled_overall"]):
            lines.append(
                f"| `{d['claim_id']}` | {d['claim_type'] or '-'} | {d['status'] or '-'} | "
                f"{d['legacy_overall']:.3f} | {d['decoupled_overall']:.3f} | "
                f"{d['lit_conf']:.3f} | {d['n_exp']} | {d['n_lit']} | {d['quadrant']} |"
            )
        lines.append("")
    if suppressed_substrate or suppressed_answer_state:
        lines.append(f"_Suppressed by gating: {len(suppressed_substrate)} "
                     f"substrate_coherence (ARC + universal invariant), "
                     f"{len(suppressed_answer_state)} answer_state (open_question). "
                     f"These cross the gate under one regime but not the other; "
                     f"the discrepancy is not actionable under their evidence "
                     f"rules. See suppressed sections below._")
        lines.append("")

    lines.append("## Implementation-cohort claims with zero experimental backing")
    lines.append("")
    lines.append(
        "Standard-gating claims with status in {stable, active, implemented, "
        "resolved} but no experimental evidence in the matrix. Under the "
        "decoupled regime they would not qualify for promotion on lit alone. "
        "This is the central question for Phase 2 -- queue an experiment per "
        "claim. (`architectural_commitment`, universal `invariant`, and "
        "`open_question` claims with this profile are surfaced separately "
        "below; they don't need experiments under their gating.)"
    )
    lines.append("")
    lines.append(f"Total: **{len(impl_no_exp)}** standard-gating claims with no exp.")
    lines.append("")
    if impl_no_exp:
        lines.append("| claim | type | status | lit_conf | n_lit |")
        lines.append("|---|---|---|---:|---:|")
        for d in sorted(impl_no_exp, key=lambda x: -x["lit_conf"]):
            lines.append(
                f"| `{d['claim_id']}` | {d['claim_type'] or '-'} | {d['status']} | "
                f"{d['lit_conf']:.3f} | {d['n_lit']} |"
            )
        lines.append("")
    # Surface the suppressed buckets transparently.
    impl_substrate = [e for e in suppressed_substrate
                      if e['status'] in IMPL_STATUSES and e['n_exp'] == 0]
    impl_answer = [e for e in suppressed_answer_state
                   if e['status'] in IMPL_STATUSES and e['n_exp'] == 0]
    if impl_substrate:
        lines.append("### Implementation cohort with no exp -- suppressed (substrate_coherence)")
        lines.append("")
        lines.append("These don't need experiments. They're foundational design "
                     "choices (ARC) or universal invariants -- by definition tested "
                     "by the substrate's coherent operation, not isolated probes.")
        lines.append("")
        lines.append("| claim | type | status | lit_conf | n_lit |")
        lines.append("|---|---|---|---:|---:|")
        for d in sorted(impl_substrate, key=lambda x: -x["lit_conf"]):
            lines.append(
                f"| `{d['claim_id']}` | {d['claim_type'] or '-'} | {d['status']} | "
                f"{d['lit_conf']:.3f} | {d['n_lit']} |"
            )
        lines.append("")
    if impl_answer:
        lines.append("### Implementation cohort with no exp -- suppressed (answer_state)")
        lines.append("")
        lines.append("Open questions where the implementation reflects our current "
                     "operating answer, not an experimental result. Restate as a "
                     "MECH or SD if the answer should be tested.")
        lines.append("")
        lines.append("| claim | type | status | lit_conf | n_lit |")
        lines.append("|---|---|---|---:|---:|")
        for d in sorted(impl_answer, key=lambda x: -x["lit_conf"]):
            lines.append(
                f"| `{d['claim_id']}` | {d['claim_type'] or '-'} | {d['status']} | "
                f"{d['lit_conf']:.3f} | {d['n_lit']} |"
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
          f"gating={dict(gating_counts)}, "
          f"discrepancies={len(discrepancies)} (suppressed {len(suppressed_substrate)} substrate + {len(suppressed_answer_state)} answer_state), "
          f"impl_no_exp={len(impl_no_exp)}, "
          f"novel={len(novel_findings)}, "
          f"low_exp={len(low_exp_flagged)}, "
          f"lit_only_above_cap={len(lit_only_above_cap)})")


if __name__ == "__main__":
    main()
