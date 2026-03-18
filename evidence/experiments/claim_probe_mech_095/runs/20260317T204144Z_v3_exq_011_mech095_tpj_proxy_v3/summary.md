# V3-EXQ-011 — MECH-095 TPJ Agency-Detection Proxy

**Status:** FAIL
**Seed:** 0
**Training:** 300 episodes (RANDOM policy)
**Eval:** 100 episodes (RANDOM policy)

## Claim Under Test

MECH-095: TPJ comparator detects world-contributed z_self changes via efference-copy
mismatch (||E2.predict_next_self(z_self_t, a_t) - z_self_observed_t+1||).

## Two-Condition Test

**C1 — Mismatch detects unexpected events (harm_safe_gap > 0.005):**
E2 motor-sensory mismatch should be elevated at harm steps vs safe steps.
The body experienced something the motor model could not predict from the action alone.
This is what the TPJ comparator would detect and flag as `residue_flag=True`.

**C2 — z_self blind to cause type (agent_env_gap < 0.05):**
The mismatch should NOT discriminate agent_caused from env_caused harm.
Both types cause unexpected body-state changes. Only z_world carries the causal
origin information. If C2 fails, SD-005 z_self/z_world separation has leaked.

## Results

| Metric | Value |
|---|---|
| mismatch_safe | 0.00898  (n=2148) |
| mismatch_harm | 0.01368  (n=264) |
| mismatch_agent_caused | 0.01385  (n=136) |
| mismatch_env_caused | 0.01349  (n=128) |
| harm_safe_gap | 0.00470  [threshold > 0.005] |
| agent_env_gap | 0.00035  [threshold < 0.05] |

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: harm_safe_gap > 0.005 | FAIL | 0.00470 |
| C2: agent_env_gap < 0.05 | PASS | 0.00035 |
| C3: n_harm >= 30 | PASS | 264 |
| C4: n_safe >= 200 | PASS | 2148 |
| C5: no fatal errors | PASS | 0 |

Criteria met: 4/5 → **FAIL**

## Failure Notes

- C1 FAIL: harm_safe_gap 0.00470 <= 0.005 (TPJ does not fire at harm events)
