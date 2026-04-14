# Diagnose-Errors Staging Report

**Session**: cowork-2026-04-14-b / diagnose-errors wave 1
**Generated**: 2026-04-14T06:00:00Z
**Mode**: STAGING (headless, autonomous)

---

## Summary

**51 total ERRORs analyzed** across two sessions (2026-04-13 and 2026-04-14).

### This session (2026-04-14): 46 new errors

All 46 new errors are **superseded by later successful iterations**. No new fix scripts required.

| Category | Count |
|----------|-------|
| Superseded by later PASS/FAIL/UNKNOWN successor | 42 |
| Superseded by later PASS/FAIL (paired, both ERROR) | 2 (onboard) |
| Onboarding smoke tests (non-scientific) | 2 |
| **Total new errors this session** | **46** |

### Prior session (2026-04-13): 5 errors

| Failed ID | Proposed Fix | Status |
|-----------|-------------|--------|
| V3-EXQ-008 | None | SKIP -- claim superseded (SD-003 redesigned) |
| V3-EXQ-038 | V3-EXQ-396 | **Awaiting human confirmation** |
| V3-EXQ-046 | V3-EXQ-397 | **Awaiting human confirmation** |
| V3-EXQ-046b | Covered by V3-EXQ-397 | (re-queue of EXQ-046) |
| V3-EXQ-057 | None | SKIP -- claim superseded (SD-010 validated) |

---

## Error Chain Analysis (2026-04-14 session)

The 46 new errors fall into chains where later lettered iterations ran to completion:

### Claims with PASS evidence from successor runs

| Error IDs | Successor | Claim |
|-----------|-----------|-------|
| V3-EXQ-074, 074b, 074c, 074d | 074f PASS | MECH-112/117 wanting/liking dissociation |
| V3-EXQ-248a | 248b PASS (248 also PASS) | Q-034 hazard/resource ratio |
| V3-EXQ-249a | 249b PASS (249 also PASS) | INV-053 depression attractor |
| V3-EXQ-251a | 251b PASS (251 also PASS) | MECH-186 VALENCE_WANTING floor |
| V3-EXQ-254a, 254b | 254c PASS (254 also PASS) | INV-052 single mechanism sufficiency |
| V3-EXQ-257, 257a | 257b PASS | SD-018 resource proximity supervision |

### Claims with FAIL evidence from successor runs

| Error IDs | Successor | Claim |
|-----------|-----------|-------|
| V3-EXQ-051b | 051c FAIL | Q-007 z_beta volatility injection |
| V3-EXQ-071 | 071b FAIL | SD-003 rollout-batched attribution |
| V3-EXQ-071c | 071d FAIL | SD-003 world_forward equivalence |
| V3-EXQ-072 | 072b FAIL | Q-021 behavioral flatness |
| V3-EXQ-073 | 073b FAIL | MECH-111 novelty signal |
| V3-EXQ-074, 074b, 074c, 074d | 074e FAIL, 074f PASS | MECH-112/117 (chain) |
| V3-EXQ-075, 075b, 075c | 075d FAIL | MECH-113 self-maintenance |
| V3-EXQ-076, 076b, 076c | 076d/e/f FAIL | MECH-116/ARC-032 E1 goal conditioning |
| V3-EXQ-084, 084b, 084c | 084d FAIL | Q-022/MECH-118/119 D_eff/Hopfield |
| V3-EXQ-138 | 138a FAIL | ARC-030 Go/NoGo symmetry |
| V3-EXQ-192 | 192a FAIL | MECH-075 hippocampal-VTA novelty |
| V3-EXQ-225a, 225b | 225c FAIL | MECH-112 goal lift redesign |
| V3-EXQ-237b, 237c | 237d FAIL | MECH-163 dual system discrimination |
| V3-EXQ-238a, 238b | 238c FAIL | SD-012 drive weight ablation |
| V3-EXQ-240 | 240a FAIL | ARC-038 waking consolidation probe |
| V3-EXQ-253a, 253b | 253c FAIL | MECH-188 z_goal PFC injection |
| V3-EXQ-260, 260a | 260b FAIL | SD-020 z_harm_a surprise PE training |
| V3-EXQ-261, 261a | 261b FAIL | SD-021 descending pain modulation |
| V3-EXQ-262, 262a | 262b FAIL | MECH-220 cross-stream harm hub |

### Special cases

| Error IDs | Successor | Notes |
|-----------|-----------|-------|
| V3-EXQ-250a | 250b UNKNOWN/INCONCLUSIVE | INV-054 phase-transition recovery: 0/3 PASS, 0/3 FAIL across seeds. Scientific finding (latency metric undefined). Both 250 and 250b returned INCONCLUSIVE. |
| V3-EXQ-263 | 263a UNKNOWN (PASS), 263b UNKNOWN (FAIL) | MECH-216 E1 predictive wanting. UNKNOWN result type = runner captured text but could not determine formal status. Evidence present in summary fields. 263a/263b status may need result-type correction via separate review. |
| V3-ONBOARD-smoke-EWIN-PC | -- | Non-scientific onboarding test. No fix needed. |
| V3-ONBOARD-smoke-ree-cloud-1 | -- | Non-scientific onboarding test. No fix needed. |

---

## Pending Actions (Human Required)

### From prior session (2026-04-13) -- still awaiting confirmation:

#### V3-EXQ-396 (fix for V3-EXQ-038)
**Claim**: ARC-016 (dynamic precision tracks environment stability), MECH-093 (z_beta modulates heartbeat frequency)
**Script**: `ree-v3/experiments/v3_exq_396_arc016_precision_sweep.py`
**Smoke test**: Passed (2026-04-13)
To queue:
- queue_id: V3-EXQ-396, priority: 5, machine_affinity: DLAPTOP-4.local
- estimated_minutes: 150, seeds: 1, conditions: 10
- supersedes: V3-EXQ-038

#### V3-EXQ-397 (fix for V3-EXQ-046 + V3-EXQ-046b)
**Claim**: ARC-007 (path memory: hippocampal proposals navigate residue-field terrain)
**Script**: `ree-v3/experiments/v3_exq_397_arc007_path_memory_ablation.py`
**Smoke test**: Passed (2026-04-13)
To queue:
- queue_id: V3-EXQ-397, priority: 5, machine_affinity: DLAPTOP-4.local
- estimated_minutes: 120, seeds: 1, conditions: 3
- supersedes: V3-EXQ-046b

### Optional review action:

**V3-EXQ-263a/263b result type**: Both show `result=UNKNOWN` in runner_status.json with outcome strings in summary fields. If governance scoring needs formal PASS/FAIL status for MECH-216, these manifests may need manual result-type correction. Not urgent -- does not block other work.

---

## EXQ ID Reservation

Reserved range 408-417 for this session. None consumed -- all errors were superseded, no new fix scripts needed.

---

*Structured data: `evidence/planning/diagnose_staging.json`*
