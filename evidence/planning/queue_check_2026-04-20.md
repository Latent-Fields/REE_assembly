# Queue Check — 2026-04-20

Generated: 2026-04-20T14:28:29Z  
Session: ree-diagnose-queue-2026-04-20T14 (automated afternoon run)

---

## Summary

No experiment auto-queued. **Multiple substrate-ready candidates found** — the "exactly
one" condition was not met; choosing between them requires human input.

---

## Substrate-ready candidates (script exists, not yet run, not in queue)

### 1. V3-EXQ-126 — MECH-104 (Priority: HIGH)
- **Proposal**: EXP-0062 / EVB-0062
- **Script**: `experiments/v3_exq_126_mech104_surprise_gate_pair.py`
- **Claim**: MECH-104 — Volatility interrupt / LC-NE analog (active, exp_conf=0.9)
- **Why now**: `active_conflict` flag in proposals index
- **Substrate check**: MECH-104 running_variance substrate in `e3_selector.py` — verified
  present; multiple V3 experiments (EXQ-197, EXQ-204, EXQ-365) already ran successfully.
- **Note**: MECH-104 already has conf=0.9 with 7 supports vs 1 weakens vs 3 mixed.
  The "active_conflict" flag may be stale from a prior governance run. This experiment
  is a matched-seed discriminative pair for additional replication.

### 2. V3-EXQ-133 — MECH-091 (Priority: MEDIUM)
- **Proposal**: EXP-0123 / EVB-0121
- **Script**: `experiments/v3_exq_133_mech091_phase_reset_pair.py`
- **Claim**: MECH-091 — Salient event phase-reset of E3 heartbeat clock (candidate, exp_conf=0.0)
- **Why now**: `insufficient_experimental_replication` (no V3 experiments yet)
- **Substrate check**: MECH-091 Layer 2 (urgency_interrupt) IMPLEMENTED 2026-04-15
  per CLAUDE.md. `clock.phase_reset()` wired in agent.py:1220. Script smoke-tested
  successfully (no crash). Progress instrumentation: `ep N/M` format verified.
  Note: Script uses `"status"` not `"outcome"` field — minor fix needed before queuing.
- **Note**: EXP-0123 is a clean single-claim experiment with pre-registered thresholds.
  Zero V3 experimental evidence for MECH-091 currently. Higher marginal value than
  MECH-104 replication.

---

## Stale proposals detected (should be marked executed)

These proposals reference experiment types that already ran and should be marked executed:

| Proposal | Claim | Suggested type | Actual run | Result |
|---|---|---|---|---|
| EXP-0126 / EVB-0124 | INV-043 | v3_exq_206_inv043_ethical_capacity_probe | V3-EXQ-206 | PASS |
| EXP-0127 / EVB-0125 | MECH-187 | v3_exq_252_mech187_zgoal_seeding_gain | V3-EXQ-252 | PASS |
| EXP-0129 / EVB-0127 | SD-032e | v3_exq_448_sd032e_pacc_autonomic | V3-EXQ-448 | UNKNOWN (inline PASS) |

---

## Blocked proposals (top high-priority)

| Proposal | Claim | Reason |
|---|---|---|
| EXP-0061 / EVB-0061 | MECH-033 | Generic `claim_probe_mech_033` — no script; needs interactive session to design |
| EXP-0062 / EVB-0062 | MECH-104 | Script exists (V3-EXQ-126); multiple candidates, not auto-queued |

---

## Recommendation

For next interactive session, queue **V3-EXQ-133 (MECH-091)** as the higher marginal
value experiment (zero V3 evidence, single clean claim, script smoke-tested).

Minor fix required before queuing:
1. Change `"status"` -> `"outcome"` in the JSON output dictionary
2. Add `print(f"verdict: {'PASS' if ...}")` line after each (seed, condition) run
3. Add `Seed {seed} Condition {label}` boundary reset lines

Then run `validate_queue.py` and push.
