"""Pre-production staging for Option E: decouple lit_conf and exp_conf.

Reads the production claim_evidence.v1.json snapshot and rescores per-claim
summaries under the decoupling rule:

  overall_confidence = exp_conf  (lit no longer blended in)
  literature_confidence is reported as a parallel signal
  evidence_quadrant = {confirmed_established | novel_discovery
                       | plausible_unproven | speculative}

Quadrant thresholds (tunable here; should match the production decision criteria
once we land the change):

  high exp == exp_conf >= 0.62 (current candidate->provisional gate)
  high lit == lit_conf >= 0.55

Outputs:
  claim_evidence.v1.staging_e_decoupled.json   -- full matrix with new schema
  option_e_diff.md                             -- side-by-side delta + quadrant report

Run:
  /opt/local/bin/python3 stage_option_e.py
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
PROD_SNAPSHOT = HERE / "claim_evidence.v1.production_snapshot.json"
STAGING_OUT = HERE / "claim_evidence.v1.staging_e_decoupled.json"
DIFF_OUT = HERE / "option_e_diff.md"

# Quadrant thresholds.
HIGH_EXP = 0.62  # candidate->provisional gate
HIGH_LIT = 0.55

# New low-flag thresholds (replace single low_overall_confidence).
LOW_EXP_FLAG = 0.55      # used to be low_overall_confidence
LIT_ONLY_CAP = 0.50      # claims with no exp + lit_conf above this need an exp pull


def _normalize(raw: Any, default: float = 0.5) -> float:
    if isinstance(raw, (int, float)):
        v = float(raw)
    else:
        v = default
    return round(max(0.0, min(1.0, v)), 3)


def _parse_ts(raw: str) -> datetime:
    s = str(raw).strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        dt = datetime.strptime(s[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def _recency(entries: list[dict[str, Any]], now: datetime, horizon_days: int) -> float:
    if not entries:
        return 0.0
    latest = max(_parse_ts(str(e["timestamp_utc"])) for e in entries)
    age_days = max(0.0, (now - latest).total_seconds() / 86400.0)
    return round(max(0.0, 1.0 - (age_days / float(horizon_days))), 3)


def _exp_conf(exp_entries: list[dict[str, Any]], now: datetime) -> float:
    """Identical to production exp branch."""
    if not exp_entries:
        return 0.0
    counts = Counter(str(e.get("evidence_direction", "unknown")) for e in exp_entries)
    directional = counts.get("supports", 0) + counts.get("weakens", 0)
    if directional:
        net = (counts.get("supports", 0) - counts.get("weakens", 0)) / directional
        consistency = (net + 1.0) / 2.0
    else:
        consistency = 0.4
    volume = min(1.0, len(exp_entries) / 5.0)
    recency = _recency(exp_entries, now, horizon_days=90)
    quality = sum(float(e.get("confidence", 0.5)) for e in exp_entries) / len(exp_entries)
    return _normalize(0.45 * consistency + 0.25 * volume + 0.20 * recency + 0.10 * quality, 0.0)


def _lit_conf(lit_entries: list[dict[str, Any]], now: datetime) -> float:
    """Production additive form -- preserved as the parallel signal.
    Inflation isn't a problem any more because lit_conf no longer drives overall.
    """
    if not lit_entries:
        return 0.0
    counts = Counter(str(e.get("evidence_direction", "unknown")) for e in lit_entries)
    directional = counts.get("supports", 0) + counts.get("weakens", 0)
    if directional:
        consistency = abs(counts.get("supports", 0) - counts.get("weakens", 0)) / directional
    else:
        consistency = 0.5
    volume = min(1.0, len(lit_entries) / 4.0)
    recency = _recency(lit_entries, now, horizon_days=365)
    quality = sum(float(e.get("confidence", 0.5)) for e in lit_entries) / len(lit_entries)
    return _normalize(0.50 * quality + 0.20 * consistency + 0.20 * volume + 0.10 * recency, 0.0)


def _quadrant(exp_conf: float, lit_conf: float, n_exp: int, n_lit: int) -> str:
    """Classify the claim's evidence position."""
    has_exp = n_exp > 0 and exp_conf >= HIGH_EXP
    has_lit = n_lit > 0 and lit_conf >= HIGH_LIT
    if has_exp and has_lit:
        return "confirmed_established"
    if has_exp and not has_lit:
        return "novel_discovery"
    if not has_exp and has_lit:
        return "plausible_unproven"
    return "speculative"


def _is_scored(entry: dict[str, Any]) -> bool:
    return "scoring_excluded" not in entry


def main() -> None:
    matrix = json.loads(PROD_SNAPSHOT.read_text(encoding="utf-8"))
    generated_at = matrix.get("generated_at_utc", "")
    now = _parse_ts(generated_at) if generated_at else datetime.now(timezone.utc)

    by_claim: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in matrix.get("entries", []):
        if not _is_scored(entry):
            continue
        cid = str(entry.get("claim_id", ""))
        if cid:
            by_claim[cid].append(entry)

    new_claims: dict[str, dict[str, Any]] = {}
    deltas = []
    quadrant_counts: Counter = Counter()
    quadrant_examples: dict[str, list[tuple[str, float, float]]] = defaultdict(list)

    for cid, entries in by_claim.items():
        exp_entries = [e for e in entries if e.get("source_type") == "experimental"]
        lit_entries = [e for e in entries if e.get("source_type") == "literature"]

        exp_c = _exp_conf(exp_entries, now)
        lit_c = _lit_conf(lit_entries, now)
        # Decoupling: overall = exp only.
        overall_new = exp_c
        quadrant = _quadrant(exp_c, lit_c, len(exp_entries), len(lit_entries))
        quadrant_counts[quadrant] += 1
        quadrant_examples[quadrant].append((cid, exp_c, lit_c))

        prod_summary = matrix.get("claims", {}).get(cid, {})
        prod_overall = prod_summary.get("overall_confidence", 0.0)
        new_summary = dict(prod_summary)
        new_summary["experimental_confidence"] = exp_c
        new_summary["literature_confidence"] = lit_c
        new_summary["overall_confidence"] = overall_new
        new_summary["evidence_quadrant"] = quadrant
        new_summary["confidence_rationale"] = (
            f"exp={len(exp_entries)} entry(s), lit={len(lit_entries)} entry(s), "
            f"exp_conf={exp_c:.3f}, lit_conf={lit_c:.3f}, quadrant={quadrant} "
            f"[option_e: overall = exp_conf only]"
        )
        new_claims[cid] = new_summary

        deltas.append({
            "claim_id": cid,
            "n_exp": len(exp_entries),
            "n_lit": len(lit_entries),
            "exp_conf": exp_c,
            "lit_conf": lit_c,
            "overall_prod": prod_overall,
            "overall_new": overall_new,
            "delta": round(overall_new - prod_overall, 3),
            "quadrant": quadrant,
        })

    # Write staging matrix.
    staging_matrix = dict(matrix)
    staging_matrix["claims"] = new_claims
    staging_matrix["generated_at_utc"] = (
        datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    )
    staging_matrix["staging_aggregator"] = "E_decoupled"
    staging_matrix["staging_thresholds"] = {
        "high_exp": HIGH_EXP,
        "high_lit": HIGH_LIT,
        "low_exp_flag": LOW_EXP_FLAG,
        "lit_only_cap": LIT_ONLY_CAP,
    }
    STAGING_OUT.write_text(
        json.dumps(staging_matrix, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    # Diff report.
    deltas.sort(key=lambda d: d["delta"])
    n = len(deltas)
    avg_delta = sum(d["delta"] for d in deltas) / n if n else 0.0
    n_drop = sum(1 for d in deltas if d["delta"] < -0.05)
    n_drop_big = sum(1 for d in deltas if d["delta"] < -0.10)
    n_rise = sum(1 for d in deltas if d["delta"] > 0.05)

    # Flag summary.
    n_low_exp_flag = sum(1 for d in deltas if d["n_exp"] > 0 and d["exp_conf"] < LOW_EXP_FLAG)
    n_lit_only_above_cap = sum(
        1 for d in deltas if d["n_exp"] == 0 and d["lit_conf"] >= LIT_ONLY_CAP
    )

    lines = []
    lines.append("# Option E (decouple lit_conf / exp_conf) -- staging diff")
    lines.append("")
    lines.append(
        "**overall_confidence = exp_conf only.** Literature is reported as a "
        "parallel signal and via `evidence_quadrant`. Quadrants:"
    )
    lines.append("")
    lines.append(f"- `high_exp` threshold: exp_conf >= {HIGH_EXP}")
    lines.append(f"- `high_lit` threshold: lit_conf >= {HIGH_LIT}")
    lines.append(f"- `low_exp_flag` (replaces low_overall_confidence): exp_conf < {LOW_EXP_FLAG}")
    lines.append(f"- `lit_only_above_cap` flag: no experimental evidence but lit_conf >= {LIT_ONLY_CAP}")
    lines.append("")

    lines.append("## Quadrant distribution")
    lines.append("")
    lines.append("|  | **high exp** | **low exp** |")
    lines.append("|---|---|---|")
    high_lit_high_exp = quadrant_counts.get("confirmed_established", 0)
    low_lit_high_exp = quadrant_counts.get("novel_discovery", 0)
    high_lit_low_exp = quadrant_counts.get("plausible_unproven", 0)
    low_lit_low_exp = quadrant_counts.get("speculative", 0)
    lines.append(f"| **high lit** | confirmed established: **{high_lit_high_exp}** | plausible unproven: **{high_lit_low_exp}** |")
    lines.append(f"| **low lit** | novel discovery: **{low_lit_high_exp}** | speculative: **{low_lit_low_exp}** |")
    lines.append("")
    lines.append(f"Total scored claims: {n}")
    lines.append("")

    lines.append("## Overall delta summary")
    lines.append("")
    lines.append(f"- avg overall_confidence delta: **{avg_delta:+.3f}**")
    lines.append(f"- claims with overall drop > 0.05: **{n_drop}**")
    lines.append(f"- claims with overall drop > 0.10: **{n_drop_big}**")
    lines.append(f"- claims with overall rise > 0.05: **{n_rise}** (claims where stripping lit revealed strong exp underneath)")
    lines.append("")

    lines.append("## New flag summary")
    lines.append("")
    lines.append(f"- `low_exp_flag`: **{n_low_exp_flag}** claims have experiments but exp_conf < {LOW_EXP_FLAG}")
    lines.append(f"- `lit_only_above_cap`: **{n_lit_only_above_cap}** claims have no exp but lit_conf >= {LIT_ONLY_CAP} (need an exp pull)")
    lines.append("")

    lines.append("## Top 25 claims by overall_confidence drop")
    lines.append("")
    lines.append("| claim | n_exp | n_lit | exp_conf | lit_conf | overall_prod | overall_new | delta | quadrant |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---|")
    for d in deltas[:25]:
        lines.append(
            f"| `{d['claim_id']}` | {d['n_exp']} | {d['n_lit']} | "
            f"{d['exp_conf']:.3f} | {d['lit_conf']:.3f} | "
            f"{d['overall_prod']:.3f} | {d['overall_new']:.3f} | "
            f"**{d['delta']:+.3f}** | {d['quadrant']} |"
        )
    lines.append("")

    lines.append("## Top 25 claims by overall_confidence RISE (these were being held back by missing/weak lit)")
    lines.append("")
    lines.append("| claim | n_exp | n_lit | exp_conf | lit_conf | overall_prod | overall_new | delta | quadrant |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---|")
    risers = sorted([d for d in deltas if d["delta"] > 0], key=lambda x: -x["delta"])
    for d in risers[:25]:
        lines.append(
            f"| `{d['claim_id']}` | {d['n_exp']} | {d['n_lit']} | "
            f"{d['exp_conf']:.3f} | {d['lit_conf']:.3f} | "
            f"{d['overall_prod']:.3f} | {d['overall_new']:.3f} | "
            f"**{d['delta']:+.3f}** | {d['quadrant']} |"
        )
    lines.append("")

    lines.append("## Novel discovery quadrant -- worth surfacing in governance")
    lines.append("")
    lines.append(
        "These have exp_conf >= " f"{HIGH_EXP}" " but lit_conf < " f"{HIGH_LIT}" ". "
        "Either a genuine novel finding without prior art, or a missing lit pull."
    )
    lines.append("")
    nov = sorted(quadrant_examples.get("novel_discovery", []), key=lambda x: -x[1])
    lines.append(f"Total in quadrant: **{len(nov)}**")
    lines.append("")
    lines.append("| claim | exp_conf | lit_conf |")
    lines.append("|---|---:|---:|")
    for cid, ec, lc in nov[:30]:
        lines.append(f"| `{cid}` | {ec:.3f} | {lc:.3f} |")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"Source snapshot: `{PROD_SNAPSHOT.name}`")
    lines.append(f"Staging matrix: `{STAGING_OUT.name}`")

    DIFF_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {STAGING_OUT.name} ({n} claims rescored)")
    print(f"Wrote {DIFF_OUT.name}")
    print(f"avg overall delta: {avg_delta:+.3f}; drops>0.05: {n_drop}; drops>0.10: {n_drop_big}; rises>0.05: {n_rise}")
    print(f"Quadrants: {dict(quadrant_counts)}")
    print(f"Flags: low_exp={n_low_exp_flag}, lit_only_above_cap={n_lit_only_above_cap}")


if __name__ == "__main__":
    main()
