# Human Decision Standard

All human-governed decisions in REE_assembly must be readable without decoding internal report formats.

Required context for each human decision packet:

1. Mechanism or claim explanation in plain language.
2. How the mechanism maps to architecture function.
3. Decision lane framing (what exact decision is being made).
4. Evidence snapshot with concrete values.
5. Metric glossary link (`HUMAN_DECISION_GLOSSARY.md`).
6. Decision history and current state.
7. Explicit options and operational meaning.
8. Source paths for verification.

Auto-generation path:

- `python3 evidence/planning/scripts/build_human_decision_briefs.py`

Integration:

- `python3 evidence/planning/scripts/run_governance_cycle.py` runs the brief generator by default.

Generated outputs:

- `evidence/decisions/human_decision_briefs/latest/INDEX.md`
- `evidence/decisions/human_decision_briefs/latest/human_decision_briefs_report.v1.json`
- `evidence/decisions/HUMAN_DECISION_GLOSSARY.md`
