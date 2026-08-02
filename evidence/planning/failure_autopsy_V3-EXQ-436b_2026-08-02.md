# Failure Autopsy: V3-EXQ-436b (SD-017/ARC-045/MECH-166 wall-independent representation confirmer)

**Generated:** 2026-08-02T10:50:16Z | **Status:** confirmed | **Scope:** single

## Facts

- Run: `v3_exq_436b_sd017_mech166_repr_confirmer_20260802T035312Z_v3`, FAIL, claims SD-017/ARC-045/MECH-166. Supersedes V3-EXQ-436a.
- Successor design fixes 436a's own documented defect: MECH-313/ARC-065 noise-floor diversity is now genuinely wired into the driver's own action-selection loop (`agent.noise_floor.compute_effective_temperature -> softmax -> multinomial`), replacing 436a's deterministic argmin, which never consulted it (confirmed as the actual reason 436a saw zero cross-seed variation).
- C1 (sole PASS/FAIL gate): `slot_cosine_sim(SWS_THEN_REM) < slot_cosine_sim(WAKING_ONLY)` in >=3/5 seeds. Result: 0/5. C4 (secondary): `slot_separation > 0.3`, 1/5.
- **Core anomaly**: within every one of 5 seeds, `waking_slot_cosine_sim` and `sws_then_rem_slot_cosine_sim` are bit-identical to full float64 precision (seed 42: `0.000965997576713562` in both). `slot_separation` is exactly `0.0` in both conditions, every seed. Yet `harm_rate_safe/dangerous`, `slot_danger_ema`, and `train_action_class_entropy_mean` genuinely DIFFER between conditions per seed -- so the two conditions are not literally identical runs; only the memory-slot readout is invariant.
- Only 1 of 16 memory slots (index 8) ever receives any visits in either condition (`slot_visit_safe_count`/`slot_visit_dang_count` all-zero elsewhere) -- a secondary observation.

## Code trace

`run_sws_schema_pass()` (`ree_core/agent.py`) DOES call `self.e1.context_memory.write(e1_input)` and returns `metrics["sws_n_writes"] = float(n_writes)` -- a diagnostic write-counter, precisely analogous to V3-EXQ-862's `n_dacc_fires`. But the driver's sleep-invocation line is:
```python
_ = agent.run_sleep_cycle()
```
The entire returned metrics dict -- including `sws_n_writes` and the REM-phase equivalent -- is discarded. There is no manifest field that would let us tell "ContextMemory.write() never fired this run" apart from "it fired but had negligible effect on pairwise cosine structure" apart from "the readout is structurally invariant given this run's config." A bit-identical readout across two conditions that otherwise diverge behaviourally is a strong tell for a recording gap, not a genuine null (independent floating-point computation on different trajectories essentially never lands on exact equality by chance).

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | can't distinguish null from unrecorded |
| Biological reference | unchanged | SWS-REM schema consolidation |
| Prerequisites | present | sleep cycle correctly invoked, behavioural divergence confirms it ran |
| Implementation | present | context_memory.write() exists and is called |
| **Measurement** | **recording gap** | write counter computed, never captured in manifest |

## Learning extracted

1. 436a's fix (noise-floor wired into action selection) genuinely worked -- behavioural stats now differ between conditions.
2. That fix doesn't guarantee the primary DV's own write path is recorded.
3. A bit-identical readout across behaviourally-different conditions is a recording-gap tell, not evidence of a null.
4. `agent.run_sleep_cycle()`'s return value carries exactly the missing diagnostic; discarding it with `_ = ...` is a one-line gap.
5. Single-slot concentration (1/16) is a secondary finding worth a closer look independent of the recording gap.

## Routing

**epistemic_category:** `measurement_gap` (recording gap, per the skill's recording-vs-measurement-debt distinction) | **evidence_direction:** `non_contributory` | **routing:** `/queue-experiment` same-question letter capturing `sws_n_writes`/REM-equivalent counters per sleep pass, per the Experimental Recording Standard.

**User gate (2026-08-02):** Approved as recommended.
