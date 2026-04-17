# Morning Agenda — 2026-04-17

Generated: `2026-04-17T04:20:05Z`

---

## Queue Status

- **Total pending: 0** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0)
- **ALERT: Queue is empty — no experiments queued. Queue new experiments before starting the runner.**

---

## Experiments Awaiting Review (0 indexed / 0 runner-only)

All experiments reviewed. Nothing pending.

---

## Errors to Diagnose (0 unresolved)

51 ERROR entries exist in runner_status.json. All have successors (lettered iterations queued or completed). No action needed.

---

## Governance Agenda (3 pending_user recommendations)

### MECH-230 (candidate) — Recommendation: **hold_candidate_resolve_conflict**
- Evidence: 4 supporting, 1 weakening, 1 mixed (conflict_ratio=0.4, conf=0.74)
- Evidence quality note: EXQ-328a dry run (2026-04-12) non_contributory (z_goal_norm=0.0, episodes too short). SD-012 substrate confirmed implemented. EXQ-328b was queued 2026-04-13 as real run with corrected instrumentation. Decision needed: confirm hold.

### SD-019 (candidate) — Recommendation: **promote_to_provisional**
- Evidence: 1 supporting, 0 weakening, 2 mixed (conflict_ratio=0, conf=0.857)
- Subject: affective_harm_nonredundancy_constraint
- Evidence quality note: empty — no documentation on what the 3 experimental entries were.
- Note: Literature pull also needed for this claim (medium priority, 0 existing entries).

### SD-023 (candidate) — Recommendation: **hold_candidate_resolve_conflict**
- Evidence: 1 supporting, 1 weakening (conflict_ratio=1.0, conf=0.586)
- Subject: body.directional_limb_damage (z_harm_s / z_harm_a causal independence)
- Evidence quality note: empty. Only 2 experimental entries, perfectly conflicted.

---

## Literature Pull Candidates (Top 5 by priority — all medium, 0 existing entries)

| # | Claim | Subject | Priority | Existing entries |
|---|-------|---------|----------|-----------------|
| 1 | SD-019 | Affective harm nonredundancy constraint | medium | 0 |
| 2 | SD-022 | Directional limb damage (z_harm_s/z_harm_a independence) | medium | 0 |
| 3 | onboarding | (general — missing literature evidence) | medium | 0 |
| 4 | Q-036 | Affective harm load state: variables beyond temporal integration | medium | 0 |
| 5 | ARC-028 | HippocampalModule trajectory completion signal wired to BetaGate | medium | 0 |

---

## Serve.py Status

- **RUNNING** on port 8000 (PID 6199)

---

## Blocked Items

None. Governance.sh ran cleanly.

### Pipeline warnings (multi-claim experiments without evidence_direction_per_claim)

These experiments received blanket direction application — may merit per-claim override fixes:

| Run | Claims tagged | Blanket direction applied |
|-----|--------------|--------------------------|
| v3_exq_074e, 074f | MECH-112, MECH-117 | non_contributory |
| v3_exq_076e | MECH-116, ARC-032 | superseded |
| v3_exq_076f | MECH-116, ARC-032 | non_contributory |
| v3_exq_243 | INV-045, MECH-123 | non_contributory |
| v3_exq_242 | SD-017, ARC-045, MECH-166 | non_contributory |
| v3_exq_247 | SD-011, SD-012, ARC-033, ARC-030 | non_contributory |
| v3_exq_038 | ARC-016, MECH-093 | non_contributory |
| v3_exq_046 | ARC-007, SD-004 | non_contributory |

These are recurring warnings — most are likely correct (non_contributory experiments), but the SD-011/SD-012/ARC-033/ARC-030 blanket is worth verifying.

---

## Summary

- **Experiment queue is empty** — primary action item is queuing new experiments before starting the runner.
- **3 governance decisions** awaiting user review (MECH-230, SD-019, SD-023).
- **SD-019** is unusual: promote_to_provisional recommended but evidence quality note is empty and no literature exists. Review carefully before promoting.
- **SD-023** has a perfect 1:1 conflict with no evidence quality note — hold is the only defensible option.
- All errors are resolved (successors exist). No /diagnose-errors needed today.
