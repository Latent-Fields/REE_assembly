"""Pre-production staging rescore for Option B (multiplicative lit_conf aggregator).

Reads the production claim_evidence.v1.json (snapshot in this dir), recomputes
per-claim confidence using a NEW lit_conf formula, and writes:

  - claim_evidence.v1.staging.json    -- full matrix with re-aggregated scores
  - aggregator_b_diff.md              -- side-by-side delta report

The exp_conf branch and the overall weighted blend are kept identical to
production -- only lit_conf changes. The staging script is standalone: it does
NOT touch the production indexer or any production output paths.

Production lit_conf (additive):
    lit_conf = 0.50*quality + 0.20*consistency + 0.20*volume + 0.10*recency

Staging lit_conf (multiplicative, cap-aware -- Option B):
    lit_conf = quality * (0.70 + 0.15*consistency + 0.10*volume + 0.05*recency)

Coefficients sum to 1.0, so when consistency == volume == recency == 1.0,
lit_conf == quality (per-paper ceiling). When all three are 0, lit_conf
falls to 0.70 * quality. Lit_conf is bounded in [0.70*quality, 1.0*quality].

Run:
    /opt/local/bin/python3 rescore_aggregator_b.py
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
PROD_SNAPSHOT = HERE / "claim_evidence.v1.production_snapshot.json"

# Multiplier coefficients (must sum to <= 1.0 for cap-aware behaviour).
# Floor is the constant term; the three weights distribute the remainder.
DEFAULT_VARIANT = "b_strict"
# B variants are MULTIPLICATIVE (lit_conf = quality * multiplier, capped at quality).
# C variants are ADDITIVE with rebalanced coefficients (no per-paper cap, but
# tighter consistency/volume signals so single weak papers can't inflate scores).
VARIANTS = {
    "b_strict":     {"form": "multiplicative", "floor": 0.70, "consistency": 0.15, "volume": 0.10, "recency": 0.05},
    "b_softened":   {"form": "multiplicative", "floor": 0.85, "consistency": 0.10, "volume": 0.03, "recency": 0.02},
    "c_balanced":   {"form": "additive_v2",    "quality": 0.65, "consistency": 0.10, "volume": 0.15, "recency": 0.10,
                     "single_paper_consistency": 0.0, "volume_log_saturation_n": 10},
}


def _normalize_confidence(raw: Any, default: float = 0.5) -> float:
    value = default
    if isinstance(raw, (int, float)):
        value = float(raw)
    return round(max(0.0, min(1.0, value)), 3)


def _parse_ts(raw: str) -> datetime:
    # Tolerate trailing Z and missing timezone.
    s = str(raw).strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        # Fall back to date-only.
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


def _exp_conf_production(exp_entries: list[dict[str, Any]], now: datetime) -> float:
    """Identical to production exp branch -- preserved as-is."""
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
    return _normalize_confidence(
        0.45 * consistency + 0.25 * volume + 0.20 * recency + 0.10 * quality,
        default=0.0,
    )


def _lit_conf_production(lit_entries: list[dict[str, Any]], now: datetime) -> float:
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
    return _normalize_confidence(
        0.50 * quality + 0.20 * consistency + 0.20 * volume + 0.10 * recency,
        default=0.0,
    )


def _lit_conf_staging(
    lit_entries: list[dict[str, Any]],
    now: datetime,
    coef: dict[str, float],
) -> tuple[float, dict[str, float]]:
    """Dispatch to multiplicative or additive_v2 form per coef['form']."""
    if not lit_entries:
        return 0.0, {}
    n = len(lit_entries)
    counts = Counter(str(e.get("evidence_direction", "unknown")) for e in lit_entries)
    directional = counts.get("supports", 0) + counts.get("weakens", 0)
    quality = sum(float(e.get("confidence", 0.5)) for e in lit_entries) / n
    recency = _recency(lit_entries, now, horizon_days=365)

    form = coef.get("form", "multiplicative")

    if form == "multiplicative":
        if directional:
            consistency = abs(counts.get("supports", 0) - counts.get("weakens", 0)) / directional
        else:
            consistency = 0.5
        volume = min(1.0, n / 4.0)
        multiplier = (
            coef["floor"]
            + coef["consistency"] * consistency
            + coef["volume"] * volume
            + coef["recency"] * recency
        )
        lit_conf = _normalize_confidence(quality * multiplier, default=0.0)
        parts = {
            "quality": round(quality, 3),
            "consistency": round(consistency, 3),
            "volume": round(volume, 3),
            "recency": recency,
            "multiplier": round(multiplier, 3),
        }
        return lit_conf, parts

    if form == "additive_v2":
        # Single-paper consistency is meaningless: one paper agrees with itself.
        if n < 2:
            consistency = float(coef.get("single_paper_consistency", 0.0))
        elif directional:
            consistency = abs(counts.get("supports", 0) - counts.get("weakens", 0)) / directional
        else:
            consistency = 0.5
        # Log-shaped volume: 1 paper ~0, 4 papers ~0.6, 10 papers = 1.0.
        sat_n = float(coef.get("volume_log_saturation_n", 10))
        import math
        volume = min(1.0, math.log2(1 + n) / math.log2(1 + sat_n))
        lit_conf = _normalize_confidence(
            coef["quality"] * quality
            + coef["consistency"] * consistency
            + coef["volume"] * volume
            + coef["recency"] * recency,
            default=0.0,
        )
        parts = {
            "quality": round(quality, 3),
            "consistency": round(consistency, 3),
            "volume": round(volume, 3),
            "recency": recency,
            "multiplier": 1.0,
        }
        return lit_conf, parts

    raise ValueError(f"unknown form: {form}")


# Back-compat alias for the original B-only call site.
_lit_conf_staging_b = _lit_conf_staging


def _overall(exp_conf: float, lit_conf: float, n_exp: int, n_lit: int) -> float:
    weights = 0.0
    weighted = 0.0
    if n_exp:
        w = min(3.0, float(n_exp))
        weighted += exp_conf * w
        weights += w
    if n_lit:
        w = min(3.0, float(n_lit))
        weighted += lit_conf * w
        weights += w
    return _normalize_confidence((weighted / weights) if weights else 0.0, default=0.0)


def _entry_is_scored(entry: dict[str, Any]) -> bool:
    """Mirror the production filter: scoring_excluded entries are logged but not scored."""
    return "scoring_excluded" not in entry


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--variant", choices=sorted(VARIANTS.keys()), default=DEFAULT_VARIANT)
    args = parser.parse_args()
    coef = VARIANTS[args.variant]
    staging_out = HERE / f"claim_evidence.v1.staging_{args.variant}.json"
    diff_out = HERE / f"aggregator_{args.variant}_diff.md"
    print(f"Variant: {args.variant}  coef={coef}")

    matrix = json.loads(PROD_SNAPSHOT.read_text(encoding="utf-8"))
    generated_at = matrix.get("generated_at_utc", "")
    now = _parse_ts(generated_at) if generated_at else datetime.now(timezone.utc)

    # Group SCORED entries by claim (drops scoring_excluded entries to mirror production).
    by_claim: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in matrix.get("entries", []):
        if not _entry_is_scored(entry):
            continue
        cid = str(entry.get("claim_id", ""))
        if cid:
            by_claim[cid].append(entry)

    deltas: list[dict[str, Any]] = []
    new_claims: dict[str, dict[str, Any]] = {}

    for cid, entries in by_claim.items():
        exp_entries = [e for e in entries if e.get("source_type") == "experimental"]
        lit_entries = [e for e in entries if e.get("source_type") == "literature"]

        exp_conf = _exp_conf_production(exp_entries, now)
        lit_conf_prod = _lit_conf_production(lit_entries, now)
        lit_conf_new, parts = _lit_conf_staging_b(lit_entries, now, coef)
        overall_prod = _overall(exp_conf, lit_conf_prod, len(exp_entries), len(lit_entries))
        overall_new = _overall(exp_conf, lit_conf_new, len(exp_entries), len(lit_entries))

        # Reconstruct claim summary mostly from production, swapping scores in place.
        prod_summary = matrix.get("claims", {}).get(cid, {})
        new_summary = dict(prod_summary)
        new_summary["literature_confidence"] = lit_conf_new
        new_summary["overall_confidence"] = overall_new
        if exp_entries or lit_entries:
            new_summary["confidence_rationale"] = (
                f"exp={len(exp_entries)} entry(s), lit={len(lit_entries)} entry(s), "
                f"exp_conf={exp_conf:.3f}, lit_conf={lit_conf_new:.3f} "
                f"[staging_{args.variant}: q={parts.get('quality', 0):.3f} "
                f"x mult={parts.get('multiplier', 0):.3f}]"
            )
        new_claims[cid] = new_summary

        deltas.append(
            {
                "claim_id": cid,
                "n_lit": len(lit_entries),
                "lit_conf_prod": lit_conf_prod,
                "lit_conf_new": lit_conf_new,
                "lit_delta": round(lit_conf_new - lit_conf_prod, 3),
                "overall_prod": overall_prod,
                "overall_new": overall_new,
                "overall_delta": round(overall_new - overall_prod, 3),
                **parts,
            }
        )

    # Write staging matrix.
    staging_matrix = dict(matrix)
    staging_matrix["claims"] = new_claims
    staging_matrix["generated_at_utc"] = (
        datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    )
    staging_matrix["staging_aggregator"] = f"B_multiplicative_{args.variant}"
    staging_matrix["staging_aggregator_coef"] = coef
    staging_out.write_text(
        json.dumps(staging_matrix, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    # Diff report.
    deltas.sort(key=lambda d: d["lit_delta"])
    n = len(deltas)
    deltas_with_lit = [d for d in deltas if d["n_lit"] > 0]
    avg_lit_delta = (
        sum(d["lit_delta"] for d in deltas_with_lit) / len(deltas_with_lit)
        if deltas_with_lit
        else 0.0
    )
    avg_overall_delta = sum(d["overall_delta"] for d in deltas) / n if n else 0.0
    n_drop = sum(1 for d in deltas_with_lit if d["lit_delta"] < -0.05)
    n_significant_drop = sum(1 for d in deltas_with_lit if d["lit_delta"] < -0.10)
    n_rise = sum(1 for d in deltas_with_lit if d["lit_delta"] > 0.05)

    lines: list[str] = []
    lines.append(f"# Aggregator {args.variant} ({coef.get('form','multiplicative')} lit_conf) -- staging diff")
    lines.append("")
    coef_str = ", ".join(f"{k}={v}" for k, v in coef.items())
    lines.append(f"Coefficients: {coef_str}")
    lines.append("")
    lines.append(
        "Compares production claim_evidence.v1.json against rescored output using "
        "the multiplicative lit_conf aggregator. exp_conf and overall blending "
        "logic are unchanged."
    )
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- claims rescored: **{n}** ({len(deltas_with_lit)} with literature evidence)")
    lines.append(f"- avg lit_conf delta (lit-bearing claims): **{avg_lit_delta:+.3f}**")
    lines.append(f"- avg overall_confidence delta (all claims): **{avg_overall_delta:+.3f}**")
    lines.append(f"- claims with lit_conf drop > 0.05: **{n_drop}**")
    lines.append(f"- claims with lit_conf drop > 0.10: **{n_significant_drop}**")
    lines.append(f"- claims with lit_conf rise > 0.05: **{n_rise}**")
    lines.append("")
    lines.append("## Top 25 lit_conf drops")
    lines.append("")
    lines.append("| claim | n_lit | lit_prod | lit_new | delta | overall_prod | overall_new | quality | mult |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for d in deltas[:25]:
        lines.append(
            f"| `{d['claim_id']}` | {d['n_lit']} | "
            f"{d['lit_conf_prod']:.3f} | {d['lit_conf_new']:.3f} | "
            f"**{d['lit_delta']:+.3f}** | {d['overall_prod']:.3f} | {d['overall_new']:.3f} | "
            f"{d.get('quality', 0):.3f} | {d.get('multiplier', 0):.3f} |"
        )
    lines.append("")
    lines.append("## Top 10 lit_conf rises (sanity check -- expect few/none)")
    lines.append("")
    lines.append("| claim | n_lit | lit_prod | lit_new | delta |")
    lines.append("|---|---:|---:|---:|---:|")
    for d in sorted(deltas, key=lambda x: -x["lit_delta"])[:10]:
        if d["lit_delta"] <= 0:
            break
        lines.append(
            f"| `{d['claim_id']}` | {d['n_lit']} | "
            f"{d['lit_conf_prod']:.3f} | {d['lit_conf_new']:.3f} | {d['lit_delta']:+.3f} |"
        )
    lines.append("")
    lines.append("## Promotion-tier impact")
    lines.append("")
    lines.append(
        "Claims that cross typical confidence thresholds (0.50 candidate, 0.65 provisional, 0.80 stable) "
        "based on **overall_confidence** under the new aggregator."
    )
    lines.append("")

    def _tier(c: float) -> str:
        if c >= 0.80:
            return "stable"
        if c >= 0.65:
            return "provisional"
        if c >= 0.50:
            return "candidate"
        return "below_candidate"

    crossings: list[tuple[str, str, str, float, float]] = []
    for d in deltas:
        t_prod = _tier(d["overall_prod"])
        t_new = _tier(d["overall_new"])
        if t_prod != t_new:
            crossings.append((d["claim_id"], t_prod, t_new, d["overall_prod"], d["overall_new"]))

    if crossings:
        lines.append("| claim | prod tier | new tier | overall_prod | overall_new |")
        lines.append("|---|---|---|---:|---:|")
        for cid, tp, tn, op, on in sorted(crossings, key=lambda x: x[4] - x[3]):
            lines.append(f"| `{cid}` | {tp} | {tn} | {op:.3f} | {on:.3f} |")
    else:
        lines.append("_No claims cross promotion tiers._")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"Source snapshot: `{PROD_SNAPSHOT.name}`")
    lines.append(f"Staging matrix: `{staging_out.name}`")

    diff_out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {staging_out.name} ({n} claims rescored)")
    print(f"Wrote {diff_out.name}")
    print(f"avg lit_conf delta: {avg_lit_delta:+.3f}; "
          f"drops>0.05: {n_drop}; drops>0.10: {n_significant_drop}; "
          f"rises>0.05: {n_rise}; tier crossings: {len(crossings)}")


if __name__ == "__main__":
    main()
