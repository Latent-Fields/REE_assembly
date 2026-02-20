# Human Decision Metric Glossary

Generated for human governance readability.

## Core Metrics

`conflict_ratio`
- How split supporting vs weakening evidence is.
- Formula: `2 * min(supports, weakens) / (supports + weakens)`.
- `0` means one-direction evidence; `1` means maximal split conflict.
- Source formula: `evidence/experiments/scripts/build_experiment_indexes.py:837`.

`overall_confidence`
- Combined confidence channel from experiment+literature evidence.
- Built from consistency, evidence volume, recency, and evidence quality.
- Source: `evidence/experiments/scripts/build_experiment_indexes.py:847`.

`lit_non_support_ratio`
- Fraction of literature evidence marked `weakens` or `mixed`.
- Source: `evidence/experiments/scripts/build_experiment_indexes.py:2146`.

`delta_lit_minus_exp`
- `literature_confidence - experimental_confidence`.
- Positive means literature confidence currently exceeds experimental confidence.
- Source: `evidence/experiments/scripts/build_experiment_indexes.py:2176`.

`recurring_failure_signatures`
- Repeated failure tags aggregated from run-pack `failure_signatures`.
- High counts indicate persistent mechanism failure modes, not one-off noise.
- Source: `evidence/experiments/scripts/build_experiment_indexes.py:2101`.

`stale_ratio` (architecture epoch applicability)
- Fraction of entries that do not satisfy current architecture epoch applicability.
- Source report: `evidence/planning/architecture_epoch_applicability.v1.json`.

## Evidence Labels

`PASS` / `FAIL`
- Derived from both run status and stop-criteria checks.
- Source: `evidence/experiments/INTERFACE_CONTRACT.md:123`.

`supports` / `weakens` / `mixed` / `unknown`
- Directional evidence labels used for conflict and recommendation logic.

`source_disagreement`
- Experimental majority and literature majority point in opposite directions.
- Source logic: `evidence/experiments/scripts/build_experiment_indexes.py:1745`.

`mixed_evidence`
- At least one `mixed` direction entry exists for a claim.
- Source logic: `evidence/experiments/scripts/build_experiment_indexes.py:1759`.
