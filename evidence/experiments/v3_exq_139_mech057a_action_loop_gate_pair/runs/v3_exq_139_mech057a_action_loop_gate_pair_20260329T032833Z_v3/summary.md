# V3-EXQ-139 -- MECH-057a Action Loop Completion Gate Discriminative Pair

**Status:** FAIL
**Claims:** MECH-057a
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** COMPLETION_GATE_ON vs COMPLETION_GATE_ABLATED
**Warmup:** 400 eps  **Eval:** 50 eps
**Env:** CausalGridWorldV2 size=6, 4 hazards, nav_bias=0.45

## Design

MECH-057a asserts committed action sequences suppress precision updates until execution completes. Completion events are principal policy-propagation opportunities (beta drops, E3 state propagates to action selection).

COMPLETION_GATE_ON: running_variance update suppressed while committed; accumulated errors flushed as batch at completion boundary (uncommitted transition). BetaGate active (elevates when committed, releases at completion).

COMPLETION_GATE_ABLATED: continuous per-step running_variance updates; BetaGate disabled (always released). No sequence-boundary gating.

## Pre-Registered Thresholds

C1: harm_rate_on <= harm_rate_ablated * 0.9 (both seeds)
C2: per-seed absolute gap >= 0.005 (both seeds)
C3: n_harm_contact_min >= 20 per cell
C4: n_committed_steps_min >= 30 in eval (GATE_ON, per seed)
C5: no fatal errors

## Results

| Condition | harm_rate (avg) | harm_contacts |
|-----------|----------------|---------------|
| COMPLETION_GATE_ON      | 0.7244 | 1080 |
| COMPLETION_GATE_ABLATED | 0.7244 | 1080 |

**delta harm_rate (ABLATED - ON): +0.0000**

Per-seed ratios (ON/ABLATED): [1.0, 1.0]
Per-seed absolute gaps (ABLATED-ON): [0.0, 0.0]

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: harm_rate ratio <= 0.9 (both seeds) | FAIL | [1.0, 1.0] |
| C2: per-seed gap >= 0.005 (both seeds) | FAIL | [0.0, 0.0] |
| C3: n_harm_min >= 20 | PASS | 535 |
| C4: n_committed_min >= 30 (GATE_ON) | PASS | 737 |
| C5: no fatal errors | PASS | -- |

Criteria met: 3/5 -> **FAIL**

## Interpretation

MECH-057a NOT supported at V3 proxy: GATE_ON harm_rate (0.7244) not significantly lower than GATE_ABLATED (0.7244). Per-seed ratios [1.0, 1.0] do not meet threshold 0.9. Completion-gated precision suppression does not produce detectable harm reduction at this training scale. Possible: the proxy (manual running_variance manipulation) does not faithfully model the biological completion-boundary mechanism; or the effect requires full ARC-023 + SD-006 substrate to manifest.

## Per-Seed

COMPLETION_GATE_ON:
  seed=42: harm_rate=0.7228 contacts=545/754 n_committed=754 n_seq=0 mean_seq_len=0.0
  seed=123: harm_rate=0.7259 contacts=535/737 n_committed=737 n_seq=0 mean_seq_len=0.0

COMPLETION_GATE_ABLATED:
  seed=42: harm_rate=0.7228 contacts=545/754
  seed=123: harm_rate=0.7259 contacts=535/737

## Failure Notes

- C1 FAIL: harm_rate ratio > 0.9 in seeds [42, 123] -- completion-gated precision suppression does not reduce harm rate by >=10%
- C2 FAIL: per-seed gaps [0.0, 0.0] < 0.005 -- absolute harm rate difference below threshold
